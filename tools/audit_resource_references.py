#!/usr/bin/env python3
"""Report legacy resource references without changing files (stdlib only)."""
from __future__ import annotations

import argparse
from collections import Counter
import json
import os
from pathlib import Path
import subprocess

TEXT_SUFFIXES = {'.md', '.py', '.sh', '.json', '.yml', '.yaml', '.toml', '.txt', '.html'}
SKIP_DIRS = {'.git', '.venv', 'venv', '__pycache__', 'media', '.pytest_cache', '.mypy_cache', '.ruff_cache'}
MAX_TEXT_BYTES = 512 * 1024


def tracked_paths(root: Path, include_untracked: bool = False) -> tuple[list[str], str]:
    if not include_untracked:
        completed = subprocess.run(['git', '-C', str(root), 'ls-files', '--cached', '-z'], capture_output=True, check=False)
        if completed.returncode == 0:
            return sorted({os.fsdecode(p) for p in completed.stdout.split(b'\0') if p}), 'git-tracked'
    result = []
    for here, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        result.extend((Path(here) / f).relative_to(root).as_posix() for f in sorted(files))
    return sorted(result), 'working-tree'


def candidate(rel: str, size: int | None) -> str | None:
    p = Path(rel)
    if len(p.parts) == 1 and p.suffix == '.sh':
        return 'root-shell'
    if p.parts[0] == 'files' and len(p.parts) == 2 and p.suffix.lower() in {'.json', '.py', '.mp3', '.pdf', '.png', '.md'}:
        return 'mixed-legacy-resource'
    if p.parts[0] == 'skills' and len(p.parts) == 2 and p.suffix == '.skill':
        return 'legacy-skill-archive'
    if rel == '小学/a.sh':
        return 'legacy-curriculum-script'
    if p.suffix == '.py' and size == 0:
        return 'empty-python'
    return None


def audit(root: Path, include_untracked: bool = False) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f'not a directory: {root}')
    paths, scope = tracked_paths(root, include_untracked)
    revision = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=False)
    candidates = []
    text_files = {}
    incomplete = []
    for rel in paths:
        path = root / rel
        available = path.is_file() and not path.is_symlink()
        size = path.stat().st_size if available else None
        kind = candidate(rel, size)
        if kind:
            candidates.append({'path': rel, 'kind': kind, 'bytes': size, 'status': 'present' if available else 'not-checked-out', 'path_references': [], 'filename_mentions': [], 'decision': 'needs_review'})
        if not available:
            incomplete.append(rel)
        elif path.suffix.lower() in TEXT_SUFFIXES and size is not None and size <= MAX_TEXT_BYTES:
            try:
                text_files[rel] = path.read_text(encoding='utf-8')
            except (UnicodeError, OSError):
                incomplete.append(rel)
    name_counts = Counter(Path(p).name for p in paths)
    for item in candidates:
        path_ref = item['path']
        name = Path(path_ref).name
        for rel, text in text_files.items():
            if rel == path_ref:
                continue
            if path_ref in text:
                item['path_references'].append(rel)
            elif name_counts[name] == 1 and name in text:
                item['filename_mentions'].append(rel)
        # These are text observations, not proof that a runtime dependency exists or does not exist.
        item['decision'] = 'not_evaluated' if item['status'] != 'present' else 'needs_review'
    candidates.sort(key=lambda row: row['path'])
    counts = Counter(item['kind'] for item in candidates)
    return {'schema_version': 1, 'revision': revision.stdout.strip() if revision.returncode == 0 else None,
            'scope': scope, 'complete_checkout': not incomplete,
            'limitations': ['String matches do not prove runtime dependencies.', 'No string matches do not prove a file is unused.', 'Files larger than 512 KiB and binary files are not scanned for references.', 'No files are moved or deleted.'],
            'summary': {'listed_files': len(paths), 'candidates': len(candidates), 'not_scanned_or_missing': len(incomplete), 'by_kind': dict(sorted(counts.items()))},
            'candidates': candidates}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--include-untracked', action='store_true')
    parser.add_argument('--output', type=Path, help='Optional explicit JSON report path')
    args = parser.parse_args()
    report = audit(args.root, args.include_untracked)
    output = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
    if args.output:
        args.output.write_text(output, encoding='utf-8')
        print(f"Reference audit: {report['summary']['candidates']} candidates, {report['summary']['not_scanned_or_missing']} skipped/missing -> {args.output}")
    else:
        print(output, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
