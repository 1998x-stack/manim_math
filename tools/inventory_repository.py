#!/usr/bin/env python3
"""Read-only inventory of a Manim curriculum repository (stdlib only)."""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import subprocess

COURSE_ROOTS = {"小学", "初中", "高中"}
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache", "media"}


def get_paths(root: Path, include_untracked: bool) -> tuple[list[str], str]:
    if not include_untracked:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "--cached", "-z"],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
        )
        if result.returncode == 0:
            return sorted(set(os.fsdecode(part) for part in result.stdout.split(b"\0") if part)), "git-tracked"

    found: list[str] = []
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            found.append((Path(current) / name).relative_to(root).as_posix())
    return sorted(found), "working-tree"


def category(parts: tuple[str, ...]) -> str:
    head = parts[0]
    if head in COURSE_ROOTS:
        return "curriculum"
    if head == "external":
        return "independent-topics"
    if head in {"assets", "catalog"}:
        return "catalog-and-publication"
    if head in {"tools", "tests", ".github"}:
        return "engineering"
    if head == "docs":
        return "documentation"
    if head in {"skills", ".codex", ".opencode", ".claude"}:
        return "agent-skills"
    if head in {"files", "videos"}:
        return "legacy-resources"
    return "repository-root"


def inventory(root: Path, include_untracked: bool = False) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"not a directory: {root}")
    paths, scope = get_paths(root, include_untracked)
    revision = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True, capture_output=True, check=False,
    )
    files, findings = [], []
    groups: Counter[str] = Counter()
    extensions: Counter[str] = Counter()
    missing = 0
    total_bytes = 0

    for rel in paths:
        path = root / rel
        parts = Path(rel).parts
        group = category(parts)
        groups[group] += 1
        suffix = Path(rel).suffix.lower() or "[no extension]"
        extensions[suffix] += 1
        if not path.is_file() and not path.is_symlink():
            missing += 1
            files.append({"path": rel, "category": group, "status": "not-checked-out", "bytes": None})
            findings.append({"path": rel, "code": "NOT_CHECKED_OUT", "severity": "info"})
            continue
        if path.is_symlink():
            files.append({"path": rel, "category": group, "status": "symlink", "bytes": None})
            findings.append({"path": rel, "code": "SYMLINK_REVIEW", "severity": "review"})
            continue
        size = path.stat().st_size
        total_bytes += size
        files.append({"path": rel, "category": group, "status": "present", "bytes": size})
        if path.name == ".DS_Store":
            findings.append({"path": rel, "code": "OS_CACHE", "severity": "safe-cleanup-candidate"})
        if suffix == ".py" and size == 0:
            findings.append({"path": rel, "code": "EMPTY_PYTHON", "severity": "review"})
        if suffix == ".md" and size <= 262144:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                findings.append({"path": rel, "code": "UNREADABLE_MARKDOWN", "severity": "review"})
            else:
                if "file:///" in text:
                    findings.append({"path": rel, "code": "LOCAL_FILE_URL", "severity": "review"})

    return {
        "schema_version": 1,
        "root": ".",
        "revision": revision.stdout.strip() if revision.returncode == 0 else None,
        "scope": scope,
        "complete_checkout": missing == 0,
        "summary": {
            "listed_files": len(paths), "present_files": len(paths) - missing,
            "not_checked_out": missing, "present_bytes": total_bytes,
            "by_category": dict(sorted(groups.items())),
            "by_extension": dict(sorted(extensions.items())),
            "finding_counts": dict(sorted(Counter(x["code"] for x in findings).items())),
        },
        "files": files,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--include-untracked", action="store_true", help="Scan the working tree rather than Git's tracked-file index")
    parser.add_argument("--output", type=Path, help="Write JSON to an explicit path; otherwise print to stdout")
    args = parser.parse_args()
    report = inventory(args.root, args.include_untracked)
    data = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(data, encoding="utf-8")
        print(f"Inventory: {report['summary']['listed_files']} listed; {report['summary']['not_checked_out']} missing from checkout; {len(report['findings'])} findings -> {args.output}")
    else:
        print(data, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
