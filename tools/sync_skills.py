#!/usr/bin/env python3
"""Mirror entire standalone AI skill packages from one canonical source (stdlib only).

Never execute packaged scripts or follow symlinks. Extra files are reported, not
silently deleted. --check is read-only and suitable for CI.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills" / "source"
TARGETS = (ROOT / ".codex" / "skills", ROOT / ".opencode" / "skills", ROOT / ".claude" / "skills")


def inventory(package: Path) -> dict[str, Path]:
    """Return all package files, including references/ and scripts/, without following links."""
    files = {}
    for path in sorted(package.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink is not allowed in skill package: {path}")
        if path.is_file():
            files[path.relative_to(package).as_posix()] = path
        elif not path.is_dir():
            raise ValueError(f"unsupported skill package entry: {path}")
    return files


def sync_packages(source: Path, targets: tuple[Path, ...], check: bool = False) -> list[str]:
    """Return drift errors. In write mode, copy missing/changed files only."""
    errors = []
    if not source.is_dir() or source.is_symlink():
        return [f"missing or invalid canonical skills directory: {source}"]
    packages = sorted(path for path in source.iterdir() if path.is_dir() or path.is_symlink())
    if not packages:
        return ["No canonical skills found"]
    expected_names = set()
    for package in packages:
        if package.is_symlink():
            errors.append(f"symlink skill package: {package}")
            continue
        expected_names.add(package.name)
        try:
            source_files = inventory(package)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if "SKILL.md" not in source_files:
            errors.append(f"missing canonical SKILL.md: {package}")
            continue
        for base in targets:
            target = base / package.name
            if target.is_symlink():
                errors.append(f"symlink skill mirror: {target}")
                continue
            try:
                mirror_files = inventory(target) if target.is_dir() else {}
            except ValueError as exc:
                errors.append(str(exc))
                continue
            for rel, src in source_files.items():
                dst = target / rel
                if rel in mirror_files and src.read_bytes() == mirror_files[rel].read_bytes():
                    continue
                if check:
                    errors.append(f"missing or drifted skill file: {dst}")
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(src.read_bytes())
                    print(f"updated {dst}")
            for rel in sorted(mirror_files.keys() - source_files.keys()):
                errors.append(f"orphan skill file (manual review required): {target / rel}")
    for base in targets:
        if not base.exists():
            continue
        if base.is_symlink():
            errors.append(f"symlink skills directory: {base}")
            continue
        for target in sorted(base.iterdir()):
            if target.is_symlink() or (target.is_dir() and target.name not in expected_names):
                errors.append(f"orphan or symlink skill package: {target}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare only; never write")
    args = parser.parse_args(argv)
    errors = sync_packages(SOURCE, TARGETS, check=args.check)
    if errors:
        print("Skill synchronization failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    count = len([p for p in SOURCE.iterdir() if p.is_dir()])
    print(f"Skill synchronization OK: {count} complete packages × {len(TARGETS)} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
