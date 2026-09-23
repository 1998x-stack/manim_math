#!/usr/bin/env python3
"""Sync standalone AI skill manifests from one canonical source (stdlib only)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills" / "source"
TARGETS = (ROOT / ".codex" / "skills", ROOT / ".opencode" / "skills", ROOT / ".claude" / "skills")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare only; never write")
    args = parser.parse_args()
    source_files = sorted(SOURCE.glob("*/SKILL.md"))
    if not source_files:
        print("No canonical skills found", file=sys.stderr)
        return 1
    errors = []
    for source in source_files:
        content = source.read_bytes()
        for base in TARGETS:
            target = base / source.parent.name / "SKILL.md"
            if target.exists() and target.read_bytes() == content:
                continue
            if args.check:
                errors.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
                print(f"updated {target.relative_to(ROOT)}")
    expected = {p.parent.name for p in source_files}
    for base in TARGETS:
        if base.exists():
            for target in base.glob("*/SKILL.md"):
                if target.parent.name not in expected:
                    errors.append(f"orphan {target.relative_to(ROOT)}")
    if errors:
        print("Skill synchronization failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"Skill synchronization OK: {len(source_files)} skills × {len(TARGETS)} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
