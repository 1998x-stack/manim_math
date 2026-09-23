#!/usr/bin/env python3
"""Synchronize full self-contained skill bundles to Codex, OpenCode and Claude (stdlib)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills" / "source"
TARGETS = tuple(ROOT / agent / "skills" for agent in (".codex", ".opencode", ".claude"))


def files_in(root: Path) -> dict[Path, Path]:
    result = {}
    if not root.exists():
        return result
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlinks are not allowed in skill bundles: {path}")
        if path.is_file():
            result[path.relative_to(root)] = path
    return result


def sync(check: bool) -> list[str]:
    source = files_in(SOURCE)
    manifests = sorted(p for p in source if len(p.parts) == 2 and p.name == "SKILL.md")
    if not manifests:
        return ["missing canonical SKILL.md files"]
    errors = []
    for base in TARGETS:
        existing = files_in(base)
        for relative, origin in source.items():
            target = base / relative
            if relative not in existing or origin.read_bytes() != target.read_bytes():
                if check:
                    errors.append(f"missing or drifted: {target.relative_to(ROOT)}")
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(origin.read_bytes())
                    print(f"updated {target.relative_to(ROOT)}")
        for relative in sorted(existing.keys() - source.keys()):
            errors.append(f"unmanaged mirror file (not auto-deleted): {(base / relative).relative_to(ROOT)}")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare all files; never write")
    args = parser.parse_args(argv)
    try:
        errors = sync(args.check)
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print("Skill bundle synchronization failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Skill bundle synchronization OK: {len(list(SOURCE.glob('*/SKILL.md')))} skills × {len(TARGETS)} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
