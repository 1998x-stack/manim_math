#!/usr/bin/env python3
"""Static checks for common Manim Scene pitfalls; does not import or render Manim.

Usage: python audit_scene.py scene.py [--json]
Exit 0: no confirmed errors; exit 2: error or unreadable/unparseable input.
Warnings require human review; AST analysis cannot prove render correctness.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
PROBLEMATIC = {
    "Sector": {"inner_radius", "outer_radius"},
    "Rectangle": {"corner_radius"},
}


def called_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def literal_strings(node: ast.AST):
    """Collect statically visible string pieces, including strings in nested lists."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        yield node.value
    elif isinstance(node, ast.JoinedStr):
        for child in node.values:
            yield from literal_strings(child)
    elif isinstance(node, (ast.Tuple, ast.List)):
        for child in node.elts:
            yield from literal_strings(child)


def audit_source(source: str) -> list[dict]:
    tree = ast.parse(source)
    findings: list[dict] = []
    has_scene = False
    has_width = False
    has_height = False

    def report(level: str, line: int, code: str, message: str):
        findings.append({"level": level, "line": line, "code": code, "message": message})

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and any(
            (called_name(base) or "").endswith("Scene") for base in node.bases
        ):
            has_scene = True
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "config":
                    has_width |= target.attr == "frame_width"
                    has_height |= target.attr == "frame_height"
        if not isinstance(node, ast.Call):
            continue
        name = called_name(node.func)
        if name == "MathTex":
            # Literal arguments only; dynamic values are deliberately not treated as safe.
            for arg in [*node.args, *(kw.value for kw in node.keywords if kw.arg not in {"font_size", "color", "tex_template"})]:
                for text in literal_strings(arg):
                    if CJK.search(text):
                        report("ERROR", node.lineno, "CJK_IN_MATHTEX", "将中文拆为 Text；MathTex 仅放数学 LaTeX。")
                    if "°" in text:
                        report("ERROR", node.lineno, "DEGREE_IN_MATHTEX", "将度数写为 ^\\circ。")
            if not any(literal_strings(arg) for arg in node.args):
                report("WARN", node.lineno, "DYNAMIC_MATHTEX", "动态公式字符串需要检查编译与中文字符。")
        if name in PROBLEMATIC:
            invalid = PROBLEMATIC[name]
            for kw in node.keywords:
                if kw.arg in invalid:
                    report("ERROR", node.lineno, "UNSUPPORTED_KEYWORD", f"{name} 不应传入 {kw.arg}；检查实际 Manim 版本。")

    if not has_scene:
        report("WARN", 1, "NO_SCENE_CLASS", "未静态找到继承 Scene 的类；核实真实类名。")
    if not (has_width and has_height):
        report("WARN", 1, "FRAME_NOT_EXPLICIT", "未发现完整逻辑画幅配置；确认最终为 9×16 竖屏。")
    return sorted(findings, key=lambda d: (d["line"], d["level"], d["code"]))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", type=Path)
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    args = parser.parse_args(argv)
    try:
        findings = audit_source(args.scene.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        findings = [{"level": "ERROR", "line": getattr(exc, "lineno", 0) or 0,
                     "code": "INPUT", "message": str(exc)}]
    errors = sum(item["level"] == "ERROR" for item in findings)
    warnings = sum(item["level"] == "WARN" for item in findings)
    if args.json:
        print(json.dumps({"file": str(args.scene), "errors": errors, "warnings": warnings,
                          "findings": findings}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f'{args.scene}:{item["line"]}: {item["level"]} {item["code"]}: {item["message"]}')
        print(f"AST audit: {errors} error(s), {warnings} warning(s). No Manim render was performed.")
    return 2 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
