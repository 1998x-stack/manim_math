#!/usr/bin/env python3
"""不导入 Manim，静态巡检四年级全部 Python 教学脚本。

用法：python tools/audit_grade4.py [--json] [--strict] [--root PATH]
--strict 对 Python 语法错误返回非零状态；其他检查只提示人工复核。
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "小学" / "四年级"
PLACEHOLDER_MARKERS = ("正在学习", "更多动画元素可以根据需要添加", "这是一个重要的数学概念")
UNSAFE_MATHTEX = set("×÷＝，。：；！？中文")


def inspect_file(path: Path, root: Path) -> dict:
    """返回可复现的源代码检查结果；警告不等同于已证实的渲染错误。"""
    rel = path.relative_to(root).as_posix()
    result = {"file": rel, "errors": [], "warnings": []}
    try:
        source = path.read_text(encoding="utf-8")
    except (UnicodeError, OSError) as exc:
        result["errors"].append(f"无法读取 UTF-8 源码：{exc}")
        return result
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as exc:
        result["errors"].append(f"语法错误，第 {exc.lineno} 行：{exc.msg}")
        return result

    for marker in PLACEHOLDER_MARKERS:
        if marker in source:
            result["warnings"].append(f"可能包含模板占位内容：{marker}")

    classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    if not classes:
        result["warnings"].append("没有场景类：检查是否为工具脚本或遗漏动画实现")

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id != "MathTex":
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    chars = set(arg.value)
                    if (chars & UNSAFE_MATHTEX) or any("\u4e00" <= char <= "\u9fff" for char in chars):
                        result["warnings"].append(
                            f"第 {node.lineno} 行：MathTex 传入中文或非 LaTeX 数学符号，需人工核实"
                        )
                        break
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "construct":
            for child in ast.walk(node):
                if isinstance(child, (ast.Assign, ast.AnnAssign)):
                    targets = child.targets if isinstance(child, ast.Assign) else [child.target]
                    for target in targets:
                        if (isinstance(target, ast.Attribute)
                                and isinstance(target.value, ast.Name)
                                and target.value.id == "config"
                                and target.attr in {"frame_width", "frame_height", "pixel_width", "pixel_height"}):
                            result["warnings"].append(
                                f"第 {child.lineno} 行：画幅配置位于 construct 中，可能晚于摄像机初始化"
                            )
    result["warnings"] = list(dict.fromkeys(result["warnings"]))
    return result


def audit(root: Path) -> dict:
    if not root.is_dir():
        raise FileNotFoundError(f"四年级目录不存在：{root}")
    results = [inspect_file(path, root) for path in sorted(root.rglob("*.py"))]
    return {
        "root": str(root),
        "files": len(results),
        "error_files": sum(bool(item["errors"]) for item in results),
        "warning_files": sum(bool(item["warnings"]) for item in results),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--json", action="store_true", help="输出完整 JSON 报告")
    parser.add_argument("--strict", action="store_true", help="存在源码错误时返回退出码 1")
    args = parser.parse_args()
    try:
        report = audit(args.root)
    except FileNotFoundError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"检查 {report['files']} 个 Python 文件；源码错误 {report['error_files']} 个；含警告 {report['warning_files']} 个")
        for item in report["results"]:
            for kind in ("errors", "warnings"):
                for detail in item[kind]:
                    print(f"{kind}: {item['file']}: {detail}")
    return int(args.strict and report["error_files"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
