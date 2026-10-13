#!/usr/bin/env python3
"""Conservative ManimCE -> ManimGX source migration.

Only transformations that are mechanically safe are applied.  Ambiguous APIs are
left intact and are reported by tools/manimgx_audit.py for manual redesign.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re


SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "media", "__pycache__"}
IMPORT_RULES = (
    (re.compile(r"(?m)^(\s*)from\s+manim\s+import\s+\*\s*$"), r"\1from manimgx import *"),
    (re.compile(r"(?m)^(\s*)import\s+manim\s+as\s+([A-Za-z_]\w*)\s*$"), r"\1import manimgx as \2"),
    (re.compile(r"(?m)^(\s*)import\s+manim\s*$"), r"\1import manimgx"),
)
FRAME_WIDTH_ASSIGNMENT = re.compile(
    r"(?m)^(?P<indent>\s*)config\.frame_width\s*=\s*(?P<value>[^#\n]+)(?P<comment>\s*#.*)?$"
)


def migrate_text(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    for pattern, replacement in IMPORT_RULES:
        text, count = pattern.subn(replacement, text)
        if count:
            changes.append(f"imports:{count}")

    def drop_frame_width(match: re.Match[str]) -> str:
        value = match.group("value").strip()
        changes.append("frame_width:1")
        return (
            f"{match.group('indent')}# ManimGX: frame_width is derived from pixel aspect ratio "
            f"and frame_height (legacy value was {value})."
        )

    text = FRAME_WIDTH_ASSIGNMENT.sub(drop_frame_width, text)
    return text, changes


def iter_python(root: Path):
    for path in root.rglob("*.py"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--write", action="store_true", help="Write changes; default is dry-run")
    args = parser.parse_args()

    touched = 0
    for path in iter_python(args.root):
        try:
            before = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        after, changes = migrate_text(before)
        if after == before:
            continue
        touched += 1
        mode = "WRITE" if args.write else "WOULD-WRITE"
        print(f"{mode:11} {path} ({', '.join(changes)})")
        if args.write:
            path.write_text(after, encoding="utf-8")

    print(f"\n{touched} Python file(s) need safe mechanical migration")
    if not args.write and touched:
        print("Run again with --write, then run tools/manimgx_audit.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
