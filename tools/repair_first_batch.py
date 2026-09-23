#!/usr/bin/env python3
"""Guarded, byte-for-byte repairs for the two confirmed 2026-09-23 batch-zero hits.

This script edits *only* the two listed lesson files when --apply is supplied.
It refuses changed or ambiguous inputs; --check validates that the fixes exist.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    (
        "external/monge_circle.py",
        "41756dea30c1c58363e2c9ead405c437615c192ed3a6ff7e166008fca2e00fc2",
        'MathTex(r"\\text{✓ 半径 } R = \\sqrt{a^2 + b^2}", font_size=24, color=GRAY_A)',
        'VGroup(Text("✓ 半径", font="PingFang SC", font_size=24, color=GRAY_A), '
        'MathTex(r"R = \\sqrt{a^2 + b^2}", font_size=24, color=GRAY_A))'
        '.arrange(RIGHT, buff=0.12)',
    ),
    (
        "初中/九年级/第二学期/第二十七章-圆与正多边形/008切线的性质与判定/tangent_properties.py",
        "048ddbba3f528f820e1e77753fbdbdf44add7affbe8df5d94a75ac0c2028a05e",
        "self.play(\n            self.play(*[FadeOut(m) for m in self.mobjects]),\n            run_time=1.0\n        )",
        "self.play(*[FadeOut(m) for m in list(self.mobjects)], run_time=1.0)",
    ),
)


def repair(path: Path, expected_sha256: str, old: str, new: str, *, apply: bool) -> str:
    original = path.read_bytes()
    text = original.decode("utf-8")
    if old not in text and new in text:
        ast.parse(text, filename=str(path))
        return "already fixed"
    if hashlib.sha256(original).hexdigest() != expected_sha256:
        raise RuntimeError(f"Source changed since first-batch audit; manually recheck {path}")
    if text.count(old) != 1 or new in text:
        raise RuntimeError(f"Expected exactly one unfixed occurrence in {path}")
    if not apply:
        raise RuntimeError(f"Unfixed source: {path} (run --apply to repair)")
    changed = text.replace(old, new, 1)
    ast.parse(changed, filename=str(path))
    path.write_text(changed, encoding="utf-8")
    return "patched"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Apply guarded one-time repairs")
    args = parser.parse_args(argv)
    for relative, sha256, old, new in TARGETS:
        path = ROOT / relative
        print(f"{relative}: {repair(path, sha256, old, new, apply=args.apply)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
