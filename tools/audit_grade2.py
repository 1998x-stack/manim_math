#!/usr/bin/env python3
"""静态审查小学二年级所有 Python 源文件；不依赖 Manim 或视频渲染。

运行：python tools/audit_grade2.py [--root 小学/二年级] [--json] [--strict]
--strict 在发现任意问题时返回非零退出码；默认只有语法错误使检查失败。
静态检查无法证明几何与教学内容正确，仍需逐课渲染并人工验收。
"""
from __future__ import annotations

import argparse
import ast
import json
from collections import Counter
from pathlib import Path


PLACEHOLDER_MARKERS = (
    "更多动画元素可以根据需要添加",
    "正在学习",
    "根据主题创建相应内容",
    "让我们看一个例子:",
    "让我们看一个例子：",
)


def _find_tex_unicode(tree: ast.AST) -> list[int]:
    """只检查 MathTex 的字面量参数；动态生成的公式需另行审查。"""
    findings = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        name = func.id if isinstance(func, ast.Name) else (
            func.attr if isinstance(func, ast.Attribute) else ""
        )
        if name != "MathTex":
            continue
        for argument in node.args:
            if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                if any(ord(char) > 127 for char in argument.value):
                    findings.append(argument.lineno)
    return findings


def audit_source(source: str, filename: str) -> list[dict[str, object]]:
    issues: list[dict[str, object]] = []
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as error:
        return [{"code": "PY_SYNTAX", "line": error.lineno or 1,
                 "message": error.msg}]

    for marker in PLACEHOLDER_MARKERS:
        if marker in source:
            line = source[:source.index(marker)].count("\n") + 1
            issues.append({"code": "GENERIC_PLACEHOLDER", "line": line,
                           "message": f"疑似未完成的教学占位内容：{marker}"})
            break

    for line in sorted(set(_find_tex_unicode(tree))):
        issues.append({"code": "MATH_TEX_UNICODE", "line": line,
                       "message": "MathTex 字面量包含非 ASCII 字符，检查 LaTeX 兼容性"})

    if filename.endswith("verify_geometry.py"):
        has_assertion = any(isinstance(node, (ast.Assert, ast.Raise))
                            for node in ast.walk(tree))
        if not has_assertion:
            issues.append({"code": "NON_ASSERTING_VERIFIER", "line": 1,
                           "message": "验证脚本没有 assert/raise，成功提示不等于实际验收"})
    return issues


def audit_tree(root: Path) -> dict[str, object]:
    if not root.is_dir():
        raise FileNotFoundError(f"不存在的二年级目录：{root}")
    python_files = sorted(root.rglob("*.py"))
    results = []
    for path in python_files:
        source = path.read_text(encoding="utf-8")
        issues = audit_source(source, str(path))
        if issues:
            results.append({"file": str(path.relative_to(root)), "issues": issues})
    counts = Counter(issue["code"] for result in results for issue in result["issues"])
    return {"root": str(root), "files_scanned": len(python_files),
            "files_with_findings": len(results), "finding_counts": dict(sorted(counts.items())),
            "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[1] / "小学" / "二年级")
    parser.add_argument("--json", action="store_true", help="输出机器可读 JSON")
    parser.add_argument("--strict", action="store_true", help="任何发现均视为失败")
    args = parser.parse_args()
    report = audit_tree(args.root)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"扫描 {report['files_scanned']} 个 Python 文件；"
              f"{report['files_with_findings']} 个文件有待核查项目")
        for code, count in report["finding_counts"].items():
            print(f"  {code}: {count}")
        for result in report["results"]:
            for issue in result["issues"]:
                print(f"{result['file']}:{issue['line']}: "
                      f"{issue['code']}: {issue['message']}")
    if report["finding_counts"].get("PY_SYNTAX", 0):
        return 1
    return int(args.strict and report["files_with_findings"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
