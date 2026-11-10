#!/usr/bin/env python3
"""Verify numeric geometry data without importing Manim.

Usage: python verify_geometry.py geometry_spec.json
This checks supplied coordinates and bounding boxes, NOT live Manim objects.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import numpy as np

TOL = 1e-6


def point(points: dict, key: str) -> np.ndarray:
    if key not in points:
        raise ValueError(f"missing point: {key}")
    value = np.asarray(points[key], dtype=float)
    if value.shape not in ((2,), (3,)) or not np.all(np.isfinite(value)):
        raise ValueError(f"invalid point {key}: expected two or three finite numbers")
    return value[:2]


def vector(points: dict, a: str, b: str) -> np.ndarray:
    return point(points, b) - point(points, a)


def nonzero(v: np.ndarray, label: str) -> np.ndarray:
    if float(np.linalg.norm(v)) < TOL:
        raise ValueError(f"degenerate zero-length ray/segment: {label}")
    return v


def verify_angles(spec: dict) -> list[str]:
    """Check directed/undirected angles against explicitly stated expectations."""
    errors: list[str] = []
    points = spec.get("points", {})
    for index, check in enumerate(spec.get("checks", [])):
        if check.get("type") != "angle":
            continue
        label = check.get("label", f"angle[{index}]")
        try:
            u = nonzero(vector(points, check["vertex"], check["a"]), label)
            v = nonzero(vector(points, check["vertex"], check["c"]), label)
            cross = float(u[0] * v[1] - u[1] * v[0])
            dot = float(np.dot(u, v))
            ccw = float(np.degrees(np.arctan2(cross, dot))) % 360.0
            minor = min(ccw, 360.0 - ccw)
            kind = check.get("kind", "minor")
            actual = {"ccw": ccw, "cw": (360.0 - ccw) % 360.0,
                      "minor": minor, "reflex": 360.0 - minor}[kind]
            expected = float(check["expected_degrees"])
            tolerance = float(check.get("tolerance_degrees", 0.01))
            if not np.isfinite(expected) or not np.isfinite(tolerance) or tolerance < 0:
                raise ValueError("invalid expectation or tolerance")
            if abs(actual - expected) > tolerance:
                errors.append(f"{label}: {kind}={actual:.5f}°, expected {expected:.5f}°")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"{label}: {exc}")
    return errors


def verify_boundaries(spec: dict) -> list[str]:
    """Validate *provided* bounding boxes; cannot inspect rendered Mobjects."""
    errors: list[str] = []
    safe = np.asarray(spec.get("safe_bounds", [-4, -7, 4, 7]), dtype=float)
    if safe.shape != (4,) or not np.all(np.isfinite(safe)) or safe[0] >= safe[2] or safe[1] >= safe[3]:
        return ["safe_bounds: expected [xmin,ymin,xmax,ymax] with positive extent"]
    for index, item in enumerate(spec.get("bounding_boxes", [])):
        label = item.get("label", f"bbox[{index}]")
        try:
            box = np.asarray(item["bbox"], dtype=float)
            if box.shape != (4,) or not np.all(np.isfinite(box)) or box[0] > box[2] or box[1] > box[3]:
                raise ValueError("invalid bbox")
            if box[0] < safe[0] - TOL or box[1] < safe[1] - TOL or box[2] > safe[2] + TOL or box[3] > safe[3] + TOL:
                errors.append(f"{label}: bbox {box.tolist()} outside safe bounds {safe.tolist()}")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"{label}: {exc}")
    return errors


def verify_numeric_checks(spec: dict) -> list[str]:
    errors: list[str] = []
    pts = spec.get("points", {})
    for index, check in enumerate(spec.get("checks", [])):
        kind = check.get("type")
        if kind == "angle":
            continue
        label = check.get("label", f"check[{index}]")
        try:
            tol = float(check.get("tolerance", TOL))
            if not np.isfinite(tol) or tol < 0:
                raise ValueError("invalid tolerance")
            if kind == "midpoint":
                observed = point(pts, check["point"])
                expected = (point(pts, check["a"]) + point(pts, check["b"])) / 2
                ok = np.linalg.norm(observed - expected) <= tol
            elif kind == "equal_lengths":
                pairs = check["pairs"]
                if len(pairs) < 2:
                    raise ValueError("equal_lengths needs at least two segments")
                lengths = [float(np.linalg.norm(nonzero(vector(pts, a, b), label))) for a, b in pairs]
                ok = max(lengths) - min(lengths) <= tol
            elif kind in {"parallel", "perpendicular"}:
                u = nonzero(vector(pts, check["a"], check["b"]), label)
                v = nonzero(vector(pts, check["c"], check["d"]), label)
                scale = float(np.linalg.norm(u) * np.linalg.norm(v))
                measure = abs(float(u[0] * v[1] - u[1] * v[0])) if kind == "parallel" else abs(float(np.dot(u, v)))
                ok = measure / scale <= tol
            else:
                raise ValueError(f"unknown check type: {kind}")
            if not ok:
                errors.append(f"{label}: {kind} failed")
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"{label}: {exc}")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    args = parser.parse_args(argv)
    try:
        spec = json.loads(args.spec.read_text(encoding="utf-8"))
        if not isinstance(spec, dict) or not isinstance(spec.get("points", {}), dict):
            raise ValueError("spec and points must be objects")
        checks, boxes = spec.get("checks", []), spec.get("bounding_boxes", [])
        if not isinstance(checks, list) or not isinstance(boxes, list) or not (checks or boxes):
            raise ValueError("provide nonempty checks and/or bounding_boxes")
        errors = verify_numeric_checks(spec) + verify_angles(spec) + verify_boundaries(spec)
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Numeric verification: {len(checks)} check(s), {len(boxes)} supplied bbox(es), {len(errors)} error(s).")
        print("NOT CHECKED: live Manim object bounds, animation frames, and visual correctness.")
        return 2 if errors else 0
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError, KeyError) as exc:
        print(f"ERROR: invalid input: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
