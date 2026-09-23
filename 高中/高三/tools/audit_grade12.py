#!/usr/bin/env python3
"""Grade 12 offline audit: Python syntax, lesson metadata and math-data checks.

Does not import or render Manim lessons (imports mutate global render settings).
Warnings identify review candidates, not confirmed runtime defects.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'tools', 'tests', '__pycache__', '.venv', 'venv'}


def issue(path: Path, line: int, severity: str, code: str, message: str) -> dict:
    return {'file': str(path), 'line': line, 'severity': severity,
            'code': code, 'message': message}


def dotted(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return f'{dotted(node.value)}.{node.attr}'
    return ''


def inspect_source(path: Path, root: Path) -> list[dict]:
    name = path.relative_to(root)
    source = path.read_text(encoding='utf-8')
    try:
        tree = ast.parse(source, filename=str(name))
    except SyntaxError as exc:
        return [issue(name, exc.lineno or 1, 'error', 'SYNTAX', exc.msg)]
    results = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and dotted(node.func) in {'np.random.seed', 'numpy.random.seed', 'random.seed'}:
            results.append(issue(name, node.lineno, 'warning', 'GLOBAL_RNG',
                                 'Global random seed; use a scene-local RNG.'))
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if node in tree.body and dotted(target).startswith('config.'):
                    results.append(issue(name, node.lineno, 'warning', 'IMPORT_CONFIG',
                                         'Module import mutates shared Manim render configuration.'))
                if isinstance(target, ast.Attribute) and target.attr == 'euler_data':
                    try:
                        data = ast.literal_eval(node.value)
                    except (ValueError, TypeError, SyntaxError, MemoryError):
                        continue
                    if not isinstance(data, dict):
                        continue
                    for shape, counts in data.items():
                        if not isinstance(counts, dict) or not {'V', 'E', 'F'} <= counts.keys():
                            continue
                        v, e, f = counts['V'], counts['E'], counts['F']
                        if not all(type(x) is int and x > 0 for x in (v, e, f)) or v - e + f != 2:
                            results.append(issue(name, node.lineno, 'error', 'EULER_DATA',
                                                 f'{shape}: expected positive integer V/E/F with V-E+F=2.'))
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            value = node.value
            if '0.3' in value and '0.8' in value and '0.4' in value and '0.5' in value and '0.52' in value:
                results.append(issue(name, node.lineno, 'error', 'TOTAL_PROBABILITY',
                                     '0.3*0.8+0.4*0.5+0.3*0.3 equals 0.53, not 0.52.'))
            if 'n 越大，频率越接近概率' in value or '频率的极限（稳定值）' in value:
                results.append(issue(name, node.lineno, 'warning', 'LLN_WORDING',
                                     'Explain convergence under independent repetitions; no monotone-error promise.'))
    return results


def audit(root: Path) -> tuple[list[dict], Counter]:
    findings = []
    counts = Counter()
    for path in sorted(root.rglob('*')):
        if not path.is_file() or EXCLUDED.intersection(path.relative_to(root).parts):
            continue
        if path.suffix == '.py':
            counts['python'] += 1
            try:
                findings.extend(inspect_source(path, root))
            except (OSError, UnicodeError) as exc:
                findings.append(issue(path.relative_to(root), 1, 'error', 'READ', str(exc)))
        elif path.name == 'description.json':
            counts['metadata'] += 1
            try:
                data = json.loads(path.read_text(encoding='utf-8'))
                if not isinstance(data, dict):
                    raise ValueError('metadata root must be an object')
            except (OSError, UnicodeError, ValueError) as exc:
                findings.append(issue(path.relative_to(root), 1, 'error', 'JSON', str(exc)))
    return findings, counts


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true', help='print structured JSON')
    parser.add_argument('--strict', action='store_true', help='also fail on review warnings')
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        parser.error('root must be an existing directory')
    findings, counts = audit(args.root)
    if args.json:
        print(json.dumps({'counts': dict(counts), 'findings': findings}, ensure_ascii=False, indent=2))
    else:
        print(f"Scanned {counts['python']} Python files and {counts['metadata']} metadata files")
        for item in findings:
            print(f"{item['severity'].upper()} {item['file']}:{item['line']} "
                  f"[{item['code']}] {item['message']}")
        print(f"Findings: {Counter(item['severity'] for item in findings)}")
    return int(any(x['severity'] == 'error' or args.strict for x in findings))


if __name__ == '__main__':
    raise SystemExit(main())
