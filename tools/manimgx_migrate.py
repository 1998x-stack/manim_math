#!/usr/bin/env python3
"""Conservative ManimCE -> ManimGX source migration.

Only transformations that are mechanically safe are applied. Ambiguous APIs are left
intact and are reported by tools/manimgx_audit.py for manual redesign.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re


SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "media", "__pycache__"}
IMPORT_RULES = (
    # Keep imported names unchanged; ManimGX intentionally mirrors much of the CE API.
    (re.compile(r"(?m)^(\s*)from\s+manim\s+import\s+(.+)$"), r"\1from manimgx import \2"),
    # Preserve aliases used by the rest of the source file.
    (re.compile(r"(?m)^(\s*)import\s+manim\s+as\s+([A-Za-z_]\w*)\s*$"), r"\1import manimgx as \2"),
    # Preserve existing `manim.X` references without rewriting every use site.
    (re.compile(r"(?m)^(\s*)import\s+manim\s*$"), r"\1import manimgx as manim"),
)

_CONFIG = r"(?:(?P<alias>[A-Za-z_]\w*)\.)?config"
FRAME_WIDTH_ASSIGNMENT = re.compile(
    rf"(?m)^(?P<indent>\s*){_CONFIG}\.frame_width\s*=\s*(?P<value>[^#\n]+)(?P<comment>\s*#.*)?$"
)
FRAME_WIDTH_HEIGHT_TUPLE = re.compile(
    rf"(?m)^(?P<indent>\s*){_CONFIG}\.frame_width\s*,\s*(?:(?P=alias)\.)?config\.frame_height\s*=\s*(?P<width>[^,\n]+),\s*(?P<height>[^#\n]+?)(?P<comment>\s*#.*)?$"
)
FRAME_HEIGHT_WIDTH_TUPLE = re.compile(
    rf"(?m)^(?P<indent>\s*){_CONFIG}\.frame_height\s*,\s*(?:(?P=alias)\.)?config\.frame_width\s*=\s*(?P<height>[^,\n]+),\s*(?P<width>[^#\n]+?)(?P<comment>\s*#.*)?$"
)


def _config_prefix(alias: str | None) -> str:
    return f"{alias}.config" if alias else "config"


def _legacy_comment(indent: str, width: str) -> str:
    return (
        f"{indent}# ManimGX: frame_width is derived from pixel aspect ratio "
        f"and frame_height (legacy value was {width.strip()})."
    )


def migrate_text(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    for pattern, replacement in IMPORT_RULES:
        text, count = pattern.subn(replacement, text)
        if count:
            changes.append(f"imports:{count}")

    def drop_width_height_tuple(match: re.Match[str]) -> str:
        changes.append("frame_width_tuple:1")
        prefix = _config_prefix(match.group("alias"))
        return "\n".join(
            (
                _legacy_comment(match.group("indent"), match.group("width")),
                f"{match.group('indent')}{prefix}.frame_height = {match.group('height').strip()}",
            )
        )

    def drop_height_width_tuple(match: re.Match[str]) -> str:
        changes.append("frame_width_tuple:1")
        prefix = _config_prefix(match.group("alias"))
        return "\n".join(
            (
                f"{match.group('indent')}{prefix}.frame_height = {match.group('height').strip()}",
                _legacy_comment(match.group("indent"), match.group("width")),
            )
        )

    # Tuple assignments must run before the single-assignment rule. They were the
    # main hole in the v1 codemod because `config.frame_width, ... = ...` has no `=`
    # directly after frame_width.
    text = FRAME_WIDTH_HEIGHT_TUPLE.sub(drop_width_height_tuple, text)
    text = FRAME_HEIGHT_WIDTH_TUPLE.sub(drop_height_width_tuple, text)

    def drop_frame_width(match: re.Match[str]) -> str:
        changes.append("frame_width:1")
        return _legacy_comment(match.group("indent"), match.group("value"))

    text = FRAME_WIDTH_ASSIGNMENT.sub(drop_frame_width, text)
    return text, changes


def iter_python(root: Path):
    for path in root.rglob("*.py"):
        if not any(part in SKIP_DIRS for part in path.parts):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Write mechanically safe migrations")
    mode.add_argument(
        "--check",
        action="store_true",
        help="Fail when any mechanically safe migration is still pending",
    )
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
        mode_name = "WRITE" if args.write else "WOULD-WRITE"
        print(f"{mode_name:11} {path} ({', '.join(changes)})")
        if args.write:
            path.write_text(after, encoding="utf-8")

    print(f"\n{touched} Python file(s) need safe mechanical migration")
    if args.check and touched:
        print("Codemod check failed: run with --write and commit the generated source changes.")
        return 1
    if not args.write and not args.check and touched:
        print("Run again with --write, then run tools/manimgx_audit.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
