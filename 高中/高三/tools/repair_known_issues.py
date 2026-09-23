#!/usr/bin/env python3
"""Apply narrowly scoped, auditable Grade 12 lesson fixes. Stdlib only.

By default, check whether fixes are necessary without writing. --apply edits
only files matching an exact, reviewed original snippet. Unrecognised upstream
edits cause a failure rather than a speculative replacement.
"""
from __future__ import annotations

import argparse
import ast
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# Each edit documents a concrete, source-reviewed issue; never modify other grades.
FIXES = {
    '第二学期/第十七章-概率论初步/005条件概率与独立事件/cond_prob_animation.py': [
        ('r"= 0.3 \\times 0.8 + 0.4 \\times 0.5 + 0.3 \\times 0.3 = 0.52"',
         'r"= 0.3 \\times 0.8 + 0.4 \\times 0.5 + 0.3 \\times 0.3 = 0.53"'),
    ],
    '第二学期/第十七章-概率论初步/003频率与概率/freq_prob_animation.py': [
        ('        np.random.seed(42)\n        self.N = 200\n        flips = np.random.randint(0, 2, self.N)',
         '        rng = np.random.default_rng(42)\n        self.N = 200\n        flips = rng.integers(0, 2, self.N)'),
        ('Text("n 越大，频率越接近概率", font=AUTHOR_FONT,',
         'Text("试验次数增大时，频率通常更接近概率", font=AUTHOR_FONT,'),
        ('"频率的极限（稳定值）"',
         '"独立重复试验中的长期趋势"'),
    ],
    '第一学期/第十五章-简单几何体/001多面体的概念/polyhedron_concepts.py': [
        ('            if result != 2:\n                print(f"WARNING: {name} 不满足欧拉公式! V-E+F = {result}")',
         '            if result != 2:\n                raise ValueError(f"{name} 不满足欧拉公式: V-E+F = {result}")'),
    ],
}


def proposed_edits(source: str, replacements: list[tuple[str, str]], label: str) -> tuple[str, int]:
    """Prepare atomic edit: reject missing/duplicate anchors and partially fixed files."""
    updated = source
    changed = 0
    for before, after in replacements:
        old_count, new_count = updated.count(before), updated.count(after)
        if old_count == 0 and new_count == 1:
            continue  # idempotent, already repaired
        if old_count != 1 or new_count != 0:
            raise ValueError(f'{label}: ambiguous anchor (old={old_count}, new={new_count})')
        updated = updated.replace(before, after, 1)
        changed += 1
    ast.parse(updated, filename=label)
    return updated, changed


def run(root: Path, apply: bool = False) -> tuple[int, int]:
    planned = []
    for relative, replacements in FIXES.items():
        target = root / relative
        source = target.read_text(encoding='utf-8')
        updated, changed = proposed_edits(source, replacements, relative)
        if changed:
            planned.append((target, updated, changed))
    # All inputs verified before the first write: avoid partial repairs on bad anchors.
    if apply:
        for target, updated, _ in planned:
            target.write_text(updated, encoding='utf-8')
    return len(planned), sum(item[2] for item in planned)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='高中/高三 directory')
    parser.add_argument('--apply', action='store_true', help='write reviewed fixes to source')
    args = parser.parse_args(argv)
    try:
        files, edits = run(args.root, args.apply)
    except (OSError, SyntaxError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    print(f'{"Applied" if args.apply else "Pending"}: {edits} edits in {files} lesson files')
    return 0 if args.apply or not edits else 1


if __name__ == '__main__':
    raise SystemExit(main())
