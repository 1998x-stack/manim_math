"""Audit each high-school Python lesson against the historical junior Manim gotchas.

No imports of Manim or execution of lesson code. Warnings require source review;
zero warnings never certifies successful rendering or mathematical correctness.

Usage: python tools/audit_highschool_gotchas.py --json > highschool-gotchas.json
"""
import argparse
import ast
import json
from pathlib import Path

from audit_junior_gotchas import audit_source

ROOT = Path(__file__).resolve().parents[1]
GRADES = ('高一', '高二', '高三')


def extra_findings(source, path):
    """Supplement the shared historical checks without duplicating their findings."""
    tree = ast.parse(source, filename=str(path))
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        func = node.func
        if func.attr == 'seed' and isinstance(func.value, ast.Name) and func.value.id == 'random':
            results.append({'path': str(path), 'line': node.lineno,
                            'code': 'GLOBAL_PYTHON_RANDOM_SEED', 'severity': 'warning',
                            'message': 'random.seed mutates process-wide state; prefer a local Random'})
        if (func.attr == 'plot' and isinstance(func.value, ast.Name)
                and func.value.id in ('plt', 'pyplot') and not node.args):
            # pyplot is not Manim Axes.plot; no judgement without arguments.
            continue
    return results


def audit(root=ROOT):
    root = Path(root)
    files = {}
    findings = []
    for grade in GRADES:
        directory = root / '高中' / grade
        paths = sorted(directory.rglob('*.py')) if directory.is_dir() else []
        files[grade] = len(paths)
        if not directory.is_dir():
            findings.append({'path': f'高中/{grade}', 'line': 0, 'code': 'GRADE_MISSING',
                             'severity': 'error', 'message': 'Grade directory is missing'})
        for path in paths:
            relative = path.relative_to(root).as_posix()
            try:
                source = path.read_text(encoding='utf-8')
            except (OSError, UnicodeError) as exc:
                findings.append({'path': relative, 'line': 0, 'code': 'READ_ERROR',
                                 'severity': 'error', 'message': str(exc)})
                continue
            existing = audit_source(source, relative)
            findings.extend(existing)
            if not any(item['code'] == 'PY_SYNTAX' for item in existing):
                findings.extend(extra_findings(source, relative))
    findings.sort(key=lambda entry: (entry['path'], entry['line'], entry['code']))
    return {'grades': files, 'files': sum(files.values()),
            'errors': sum(item['severity'] == 'error' for item in findings),
            'warnings': sum(item['severity'] == 'warning' for item in findings),
            'findings': findings}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--strict', action='store_true', help='Fail for warnings as well as errors')
    args = parser.parse_args(argv)
    result = audit(args.root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"High school: {result['grades']}; {result['files']} files, "
              f"{result['errors']} errors, {result['warnings']} warnings")
        for item in result['findings']:
            print(f"{item['path']}:{item['line']} [{item['severity']}] {item['code']}: {item['message']}")
    return int(bool(result['errors'] or (args.strict and result['warnings'])))


if __name__ == '__main__':
    raise SystemExit(main())
