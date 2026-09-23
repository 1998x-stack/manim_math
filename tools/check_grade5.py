"""Static, dependency-free inventory of fifth-grade Manim scenes.

This is a triage tool, not proof of mathematical or visual correctness.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import asdict, dataclass
from fractions import Fraction
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GRADE = Path('小学/五年级')
HAN = re.compile(r'[\u3400-\u9fff]')


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    line: int
    detail: str


def _name(node: ast.expr) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return ''


def scan_source(source: str, path: str) -> list[Finding]:
    """Check only patterns with a traceable source location."""
    findings: list[Finding] = []

    def emit(severity: str, code: str, line: int, detail: str) -> None:
        findings.append(Finding(severity, code, path, line, detail))

    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as exc:
        emit('error', 'PYTHON_SYNTAX', exc.lineno or 0, exc.msg)
        return findings

    if not any(isinstance(node, ast.ClassDef) for node in tree.body):
        emit('warning', 'NO_CLASS', 1, 'No Scene class found; verify this file is a helper.')

    if '平均数的计算' in path and path.endswith('002_平均数的计算.py'):
        expected = Fraction(90 * 10 + 85 * 15 + 80 * 5, 10 + 15 + 5)
        if '85.5' in (ast.get_docstring(tree) or ''):
            emit('warning', 'MATH_DOC_MISMATCH', 1,
                 f'Docstring says 85.5; exact weighted mean is {expected}, ≈{float(expected):.2f}. '
                 'Inspect on-screen MathTex separately.')

    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name)
                   and t.value.id == 'config' for t in targets):
                emit('info', 'GLOBAL_RENDER_CONFIG', node.lineno,
                     'Module import mutates global Manim config; isolate scenes in separate render processes.')
                break

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        callee = _name(node.func)
        if callee not in {'Text', 'MathTex', 'Tex'}:
            continue
        literals = [a.value for a in node.args if isinstance(a, ast.Constant)
                    and isinstance(a.value, str)]
        if callee == 'Text':
            if any('正在学习' in text for text in literals):
                emit('warning', 'PLACEHOLDER_SCENE', node.lineno,
                     'Generic placeholder is shown instead of an actual mathematics lesson.')
            if any('\\n' in text for text in literals):
                emit('warning', 'LITERAL_NEWLINE', node.lineno,
                     'Text contains a literal backslash-n; use a real newline if line wrapping is intended.')
        elif any(HAN.search(text) for text in literals):
            emit('warning', 'CHINESE_IN_TEX', node.lineno,
                 'Render Chinese in Text rather than relying on MathTex/Tex default LaTeX fonts.')
    return findings


def scan_tree(root: Path) -> tuple[int, list[Finding]]:
    grade = root / GRADE
    if not grade.is_dir():
        raise FileNotFoundError(f'Missing fifth-grade directory: {grade}')
    files = sorted(grade.rglob('*.py'))
    findings: list[Finding] = []
    for file in files:
        relative = file.relative_to(root).as_posix()
        try:
            content = file.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            findings.append(Finding('error', 'READ_FAILURE', relative, 0, str(exc)))
            continue
        findings.extend(scan_source(content, relative))
    return len(files), findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Repository root')
    parser.add_argument('--json', action='store_true', help='Machine-readable report')
    parser.add_argument('--strict', action='store_true',
                        help='Also fail on outstanding warnings (legacy content may fail)')
    args = parser.parse_args(argv)
    try:
        count, findings = scan_tree(args.root.resolve())
    except FileNotFoundError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps({'files_scanned': count, 'findings': [asdict(f) for f in findings]},
                         ensure_ascii=False, indent=2))
    else:
        print(f'Fifth-grade Python files scanned: {count}')
        for f in findings:
            print(f'{f.severity.upper():7} {f.path}:{f.line}: {f.code}: {f.detail}')
        print(f'Findings: {len(findings)}; errors: '
              f'{sum(f.severity == "error" for f in findings)}; warnings: '
              f'{sum(f.severity == "warning" for f in findings)}')
    return int(any(f.severity == 'error' or (args.strict and f.severity == 'warning')
                   for f in findings))


if __name__ == '__main__':
    raise SystemExit(main())
