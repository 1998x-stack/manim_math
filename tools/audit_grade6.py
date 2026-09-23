"""Sixth-grade source audit; runs with the Python standard library only.

Usage: python tools/audit_grade6.py [--json] [--warnings-as-errors]
This is a static check, not a Manim render or a mathematical proof.
"""

import argparse
import ast
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GRADE_PATH = Path("小学/六年级")
PLACEHOLDERS = ("正在学习", "更多动画元素可以根据需要添加", "这是一个重要的数学概念")
LATEX_UNSAFE = set("÷×∠°")


def _call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _static_strings(call):
    """Return only literal strings; do not try to evaluate arbitrary code."""
    return [arg.value for arg in call.args if isinstance(arg, ast.Constant) and isinstance(arg.value, str)]


def audit(root=REPO_ROOT):
    """Return (Python count, JSON count, issues); issues are structured dicts."""
    grade = Path(root) / GRADE_PATH
    issues = []
    if not grade.is_dir():
        return 0, 0, [{"severity": "error", "path": str(GRADE_PATH), "line": 0,
                       "message": "六年级目录不存在"}]

    def record(severity, path, line, message):
        issues.append({"severity": severity, "path": str(path.relative_to(root)),
                       "line": line, "message": message})

    python_files = sorted(grade.rglob("*.py"))
    json_files = sorted(grade.rglob("*.json"))
    for path in python_files:
        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
        except (UnicodeError, OSError) as exc:
            record("error", path, 0, f"无法读取 Python 源码：{exc}")
            continue
        except SyntaxError as exc:
            record("error", path, exc.lineno or 0, f"Python 语法错误：{exc.msg}")
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = _call_name(node.func)
            if name in {"MathTex", "Tex"}:
                for text in _static_strings(node):
                    if any("\u4e00" <= ch <= "\u9fff" for ch in text) or LATEX_UNSAFE.intersection(text):
                        record("warning", path, node.lineno,
                               "公式包含中文或非 LaTeX 数学字符；请将中文交给 Text，并检查 LaTeX 命令")
                        break
            if name in {"Text", "MarkupText"}:
                for text in _static_strings(node):
                    if "\\n" in text:
                        record("warning", path, node.lineno,
                               "Text 含字面的反斜杠 n，可能期望使用真正的换行符")
                    if any(phrase in text for phrase in PLACEHOLDERS):
                        record("warning", path, node.lineno, "发现未替换的教学占位内容")

    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError, OSError) as exc:
            record("error", path, 0, f"JSON 无法解析：{exc}")

    return len(python_files), len(json_files), sorted(
        issues, key=lambda item: (item["path"], item["line"], item["severity"])
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="输出机器可读的审计结果")
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args(argv)
    python_count, json_count, issues = audit()
    error_count = sum(issue["severity"] == "error" for issue in issues)
    warning_count = len(issues) - error_count
    if args.json:
        print(json.dumps({"python_files": python_count, "json_files": json_count,
                          "errors": error_count, "warnings": warning_count,
                          "issues": issues}, ensure_ascii=False, indent=2))
    else:
        print(f"六年级静态审计：{python_count} 个 Python 文件，{json_count} 个 JSON 文件；"
              f"{error_count} 个错误，{warning_count} 个警告")
        for issue in issues:
            print(f"[{issue['severity'].upper()}] {issue['path']}:{issue['line']} {issue['message']}")
    return int(bool(error_count or (args.warnings_as_errors and warning_count)))


if __name__ == "__main__":
    raise SystemExit(main())
