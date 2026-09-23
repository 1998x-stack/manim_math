#!/usr/bin/env python3
"""静态审查高中/高二下的每个 Python 文件，不导入 Manim。

使用：python tools/audit_grade11.py [--json] [--strict]
静态检查只能定位风险，不能替代数学证明、Manim 渲染及关键帧验收。
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRADE = Path("高中/高二")
SCENE_BASES = {"Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene"}
UNSAFE_TEX = re.compile(r"[\u3400-\u9fff∈²±×÷＝]")
# 仅匹配已知错误的单值根号与 ± 的等式；不把方程全部根误报为错误。
AMBIGUOUS_SQRT = re.compile(r"\\sqrt\s*\{(?:-4|4|-a)\}\s*=\s*\\pm")
GENERIC_PLACEHOLDER = re.compile(r"正在学习.{1,80}的概念[.。…]{2,}")


def _name(expr: ast.expr) -> str | None:
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.Attribute):
        return expr.attr
    return None


def _chunks(expr: ast.expr) -> list[str]:
    if isinstance(expr, ast.Constant) and isinstance(expr.value, str):
        return [expr.value]
    if isinstance(expr, ast.JoinedStr):
        return [piece.value for piece in expr.values
                if isinstance(piece, ast.Constant) and isinstance(piece.value, str)]
    return []


def audit_file(path: Path, root: Path) -> tuple[bool, list[dict[str, object]]]:
    relative = path.relative_to(root).as_posix()
    issues: list[dict[str, object]] = []

    def emit(code: str, severity: str, line: int, detail: str) -> None:
        issues.append({"file": relative, "line": line, "code": code,
                       "severity": severity, "detail": detail})

    try:
        source = path.read_text(encoding="utf-8")
        module = ast.parse(source, filename=relative)
    except (SyntaxError, UnicodeError, OSError) as exc:
        emit("PYTHON_SYNTAX", "error", getattr(exc, "lineno", 1) or 1, str(exc))
        return False, issues

    scene_classes = [cls for cls in module.body if isinstance(cls, ast.ClassDef)
                     and any(_name(base) in SCENE_BASES for base in cls.bases)]
    if not scene_classes:
        emit("NO_SCENE", "info", 1, "无直接 Scene 子类；可能是辅助模块或未完成课件")
    seen: set[str] = set()
    for cls in scene_classes:
        if cls.name in seen:
            emit("DUPLICATE_SCENE", "error", cls.lineno, "同文件重复的 Scene 类名")
        seen.add(cls.name)
        construct = next((item for item in cls.body
                          if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                          and item.name == "construct"), None)
        if construct is None or not any(isinstance(node, ast.Call)
                                       and _name(node.func) in {"play", "add", "wait"}
                                       for node in ast.walk(construct)):
            emit("EMPTY_SCENE", "warning", cls.lineno, "construct 没有直接场景操作，需人工确认")

    for node in ast.walk(module):
        if isinstance(node, ast.Call) and _name(node.func) in {"MathTex", "Tex"}:
            for argument in node.args:
                for chunk in _chunks(argument):
                    if UNSAFE_TEX.search(chunk):
                        emit("UNICODE_MATHTEX", "warning", node.lineno,
                             "公式含中文或 Unicode 数学符号；应使用 LaTeX 命令，中文用 Text")
                    if AMBIGUOUS_SQRT.search(chunk):
                        emit("AMBIGUOUS_SQRT", "error", node.lineno,
                             "不能将单值根号写成 ± 两个值；改写为对应方程的解")
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if GENERIC_PLACEHOLDER.search(node.value):
                emit("GENERIC_LESSON_PLACEHOLDER", "warning", node.lineno,
                     "疑似通用教学占位稿，尚未实现知识点")
    return bool(scene_classes), issues


def audit_tree(root: Path = ROOT) -> dict[str, object]:
    folder = root / GRADE
    if not folder.is_dir():
        return {"files": 0, "scene_files": 0, "issues": [
            {"file": GRADE.as_posix(), "line": 1, "code": "MISSING_DIRECTORY",
             "severity": "error", "detail": "高二课程目录不存在"}]}
    files = sorted(folder.rglob("*.py"))
    issues: list[dict[str, object]] = []
    scenes = 0
    for file in files:
        is_scene, found = audit_file(file, root)
        scenes += int(is_scene)
        issues.extend(found)
    return {"files": len(files), "scene_files": scenes, "issues": issues}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true",
                        help="发现 error 或 warning 时返回非零状态码")
    args = parser.parse_args()
    report = audit_tree()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"高二代码审查：{report['files']} 个 Python 文件；"
              f"{report['scene_files']} 个包含直接 Scene 子类的文件")
        for issue in report["issues"]:
            print(f"{issue['severity']} {issue['file']}:{issue['line']} "
                  f"[{issue['code']}] {issue['detail']}")
    return int(args.strict and any(item["severity"] in {"error", "warning"}
                                   for item in report["issues"]))


if __name__ == "__main__":
    raise SystemExit(main())
