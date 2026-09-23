#!/usr/bin/env python3
"""Audit every grade-three Python source without importing Manim.

This is a static gate, not evidence that a scene renders or teaches correctly.
Run: python tools/audit_grade3.py [--json] [--strict]
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRADE3 = Path("小学/三年级")
UNSAFE_MATH_TEX = re.compile(r"[\u3400-\u9fff×÷＝]")
# Historical generic animations use this sentence in place of actual lesson content.
GENERIC_PLACEHOLDER = re.compile(r"正在学习.{1,80}的概念[.。…]{2,}")
SCENE_BASES = {"Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene"}


def _callee_name(node: ast.expr) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _literal_chunks(node: ast.expr) -> list[str]:
    """Inspect known literal parts of strings or f-strings, not dynamic variables."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return [node.value]
    if isinstance(node, ast.JoinedStr):
        return [part.value for part in node.values
                if isinstance(part, ast.Constant) and isinstance(part.value, str)]
    return []


def audit_file(path: Path, root: Path) -> list[dict[str, object]]:
    relative = path.relative_to(root).as_posix()
    issues: list[dict[str, object]] = []

    def report(code: str, severity: str, line: int, detail: str) -> None:
        issues.append({"file": relative, "line": line, "severity": severity,
                       "code": code, "detail": detail})

    try:
        text = path.read_text(encoding="utf-8")
        module = ast.parse(text, filename=relative)
    except (SyntaxError, UnicodeError, OSError) as error:
        report("PYTHON_SYNTAX", "error", getattr(error, "lineno", 1) or 1,
               str(error))
        return issues

    scenes = [node.name for node in module.body
              if isinstance(node, ast.ClassDef)
              and any(_callee_name(base) in SCENE_BASES for base in node.bases)]
    if not scenes:
        report("NO_SCENE", "info", 1,
               "No direct Scene subclass; may be a helper module or unfinished lesson")

    for node in ast.walk(module):
        if isinstance(node, (ast.Constant, ast.JoinedStr)):
            if any(GENERIC_PLACEHOLDER.search(part) for part in _literal_chunks(node)):
                report("GENERIC_LESSON_PLACEHOLDER", "warning", node.lineno,
                       "Generic lesson-introduction placeholder; implement the actual math content")
        if not isinstance(node, ast.Call) or _callee_name(node.func) not in {"MathTex", "Tex"}:
            continue
        arguments = list(node.args) + [kw.value for kw in node.keywords
                                      if kw.arg in {"tex_string", "tex_strings"}]
        for argument in arguments:
            for chunk in _literal_chunks(argument):
                if UNSAFE_MATH_TEX.search(chunk):
                    report("UNICODE_MATHTEX", "warning", getattr(argument, "lineno", node.lineno),
                           "Chinese or Unicode ×/÷/＝ in Tex; use Text for Chinese and LaTeX commands for operators")
                    break
    return issues


def audit_tree(root: Path = ROOT) -> dict[str, object]:
    course = root / GRADE3
    if not course.is_dir():
        return {"files": 0, "scene_files": 0,
                "issues": [{"file": GRADE3.as_posix(), "line": 1,
                            "severity": "error", "code": "MISSING_DIRECTORY",
                            "detail": "Grade-three directory not found"}]}

    files = sorted(course.rglob("*.py"))
    issues: list[dict[str, object]] = []
    scene_count = 0
    for path in files:
        per_file = audit_file(path, root)
        issues.extend(per_file)
        if not any(issue["code"] in {"PYTHON_SYNTAX", "NO_SCENE"}
                   for issue in per_file):
            scene_count += 1
    return {"files": len(files), "scene_files": scene_count, "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print machine-readable results")
    parser.add_argument("--strict", action="store_true",
                        help="Exit nonzero on errors and warnings")
    args = parser.parse_args()
    result = audit_tree()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Grade-three static audit: {result['files']} Python files, "
              f"{result['scene_files']} direct Scene files")
        for issue in result["issues"]:
            print(f"{issue['severity'].upper()} {issue['file']}:{issue['line']} "
                  f"[{issue['code']}] {issue['detail']}")
    return int(args.strict and any(issue["severity"] in {"error", "warning"}
                                   for issue in result["issues"]))


if __name__ == "__main__":
    raise SystemExit(main())
