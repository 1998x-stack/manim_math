"""Audit each high-school Python lesson against documented historical Manim gotchas.

Read-only, standard-library AST inspection, without importing lesson modules or Manim.
A ctex source exception is *visible* in the report as info, never treated as
proof that its selected LaTeX and CJK environment can render successfully.
"""
import argparse
import ast
import json
from pathlib import Path

from audit_junior_gotchas import audit_source

ROOT = Path(__file__).resolve().parents[1]
GRADES = ('高一', '高二', '高三')


def _self_play(call):
    return (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
            and call.func.attr == 'play' and isinstance(call.func.value, ast.Name)
            and call.func.value.id == 'self')


def _ctex_calls(tree):
    """Only explicit per-call TexTemplateLibrary.ctex is exempted from default-TeX warning."""
    lines = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not ((isinstance(node.func, ast.Name) and node.func.id in ('Tex', 'MathTex'))
                or (isinstance(node.func, ast.Attribute) and node.func.attr in ('Tex', 'MathTex'))):
            continue
        for kw in node.keywords:
            v = kw.value
            if (kw.arg == 'tex_template' and isinstance(v, ast.Attribute) and v.attr == 'ctex'
                    and isinstance(v.value, ast.Name) and v.value.id == 'TexTemplateLibrary'):
                lines.add(node.lineno)
    return lines


def extra_findings(source, path, tree=None):
    """Supplement historical detection with two runtime hazards and a ctex review label."""
    tree = tree if tree is not None else ast.parse(source, filename=str(path))
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if _self_play(node) and any(_self_play(arg) for arg in node.args):
            results.append({'path': str(path), 'line': node.lineno,
                            'code': 'NESTED_SELF_PLAY', 'severity': 'error',
                            'message': 'An inner self.play returns None, not an Animation'})
        if (isinstance(node.func, ast.Attribute) and node.func.attr == 'seed'
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == 'random'):
            results.append({'path': str(path), 'line': node.lineno,
                            'code': 'GLOBAL_PYTHON_RANDOM_SEED', 'severity': 'warning',
                            'message': 'random.seed mutates process-wide state; prefer local Random'})
    return results


def audit(root=ROOT):
    root = Path(root)
    files, findings = {}, []
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
            shared = audit_source(source, relative)
            if any(issue['code'] == 'PY_SYNTAX' for issue in shared):
                findings.extend(shared)
                continue
            tree = ast.parse(source, filename=relative)
            ctex_lines = _ctex_calls(tree)
            for issue in shared:
                if issue['code'] == 'CHINESE_IN_TEX' and issue['line'] in ctex_lines:
                    issue = {**issue, 'code': 'CTEX_CHINESE_REVIEW', 'severity': 'info',
                             'message': 'Explicit ctex handles CJK; confirm installed template/fonts by rendering'}
                findings.append(issue)
            findings.extend(extra_findings(source, relative, tree))
    findings.sort(key=lambda issue: (issue['path'], issue['line'], issue['code']))
    return {'grades': files, 'files': sum(files.values()),
            'errors': sum(issue['severity'] == 'error' for issue in findings),
            'warnings': sum(issue['severity'] == 'warning' for issue in findings),
            'information': sum(issue['severity'] == 'info' for issue in findings),
            'findings': findings}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--strict', action='store_true', help='Fail on warnings as well as errors')
    args = parser.parse_args(argv)
    result = audit(args.root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"High school: {result['grades']}; {result['files']} files, "
              f"{result['errors']} errors, {result['warnings']} warnings, "
              f"{result['information']} ctex review items")
        for issue in result['findings']:
            print(f"{issue['path']}:{issue['line']} [{issue['severity']}] "
                  f"{issue['code']}: {issue['message']}")
    return int(bool(result['errors'] or (args.strict and result['warnings'])))


if __name__ == '__main__':
    raise SystemExit(main())
