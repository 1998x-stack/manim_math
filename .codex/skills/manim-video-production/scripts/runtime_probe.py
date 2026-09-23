#!/usr/bin/env python3
"""Explicit runtime checkpoints for real Manim Scenes (no Manim import here).

Import from a Scene and call assert_checkpoint *after* play/update. This is NOT
an automatic every-frame inspector and does not replace watching rendered frames.
Set MANIM_PROBE_REPORT to an existing writable report path to append JSON lines.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Mapping

DEFAULT_SAFE_BOUNDS = (-4.0, -7.0, 4.0, 7.0)  # xmin,ymin,xmax,ymax


def _xy(value, label: str) -> tuple[float, float]:
    try:
        if len(value) < 2:
            raise ValueError("requires x and y")
        x, y = float(value[0]), float(value[1])
    except (TypeError, IndexError, ValueError) as exc:
        raise ValueError(f"{label}: invalid 2D coordinates: {exc}") from exc
    if not (math.isfinite(x) and math.isfinite(y)):
        raise ValueError(f"{label}: non-finite coordinates")
    return x, y


def _family(scene) -> set[int]:
    """Resolve Scene.mobjects and all submobjects by identity, not equality."""
    result: set[int] = set()
    stack = list(scene.mobjects)
    while stack:
        mob = stack.pop()
        ident = id(mob)
        if ident in result:
            continue
        result.add(ident)
        stack.extend(getattr(mob, "submobjects", ()))
    return result


def inspect_checkpoint(
    scene,
    objects: Mapping[str, object],
    *,
    safe_bounds=DEFAULT_SAFE_BOUNDS,
    expected_centers: Mapping[str, tuple[float, float]] | None = None,
    tolerance: float = 1e-3,
) -> dict:
    """Inspect explicitly registered, visible Mobjects *at the current state*.

    No frame interpolation or video pixels are inspected. Register each meaningful
    label/diagram separately; group bounds alone cannot detect internal overlap.
    """
    xmin, ymin = _xy(safe_bounds[:2], "safe_bounds min")
    xmax, ymax = _xy(safe_bounds[2:], "safe_bounds max")
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("safe_bounds must have positive extent")
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and nonnegative")
    centers = expected_centers or {}
    if not isinstance(objects, Mapping) or not objects:
        raise ValueError("register at least one named visible object")
    unknown = set(centers) - set(objects)
    if unknown:
        raise ValueError(f"expected_centers refer to unregistered objects: {sorted(unknown)}")
    active = _family(scene)
    findings: list[dict] = []
    samples: dict[str, dict] = {}
    for name, mob in objects.items():
        if not isinstance(name, str) or not name:
            raise ValueError("object names must be nonempty strings")
        if id(mob) not in active:
            findings.append({"object": name, "code": "NOT_IN_SCENE", "message": "object is not in the current Scene family"})
            continue
        try:
            left, _ = _xy(mob.get_left(), f"{name}.left")
            right, _ = _xy(mob.get_right(), f"{name}.right")
            _, bottom = _xy(mob.get_bottom(), f"{name}.bottom")
            _, top = _xy(mob.get_top(), f"{name}.top")
            center = _xy(mob.get_center(), f"{name}.center")
        except (AttributeError, ValueError) as exc:
            findings.append({"object": name, "code": "INVALID_GEOMETRY", "message": str(exc)})
            continue
        bbox = [left, bottom, right, top]
        samples[name] = {"bbox": bbox, "center": list(center)}
        if left > right or bottom > top or left < xmin - tolerance or right > xmax + tolerance or bottom < ymin - tolerance or top > ymax + tolerance:
            findings.append({"object": name, "code": "OUT_OF_SAFE_BOUNDS", "message": f"bbox={bbox}"})
        if name in centers:
            target = _xy(centers[name], f"{name}.expected_center")
            if math.dist(center, target) > tolerance:
                findings.append({"object": name, "code": "CENTER_MISMATCH", "message": f"actual={center}, expected={target}"})
    return {"status": "fail" if findings else "pass", "samples": samples, "findings": findings,
            "safe_bounds": [xmin, ymin, xmax, ymax]}


def assert_checkpoint(scene, label: str, objects: Mapping[str, object], **kwargs) -> dict:
    """Inspect then optionally append machine-readable evidence; fail on findings."""
    if not isinstance(label, str) or not label:
        raise ValueError("checkpoint label must be a nonempty string")
    result = {"checkpoint": label, **inspect_checkpoint(scene, objects, **kwargs)}
    report = os.environ.get("MANIM_PROBE_REPORT")
    if report:
        path = Path(report)
        if not path.parent.is_dir():
            raise FileNotFoundError(f"checkpoint report directory does not exist: {path.parent}")
        with path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(result, ensure_ascii=False, allow_nan=False) + "\n")
    if result["findings"]:
        raise AssertionError(f"checkpoint {label}: {result['findings']}")
    return result
