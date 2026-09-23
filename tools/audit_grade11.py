#!/usr/bin/env python3
"""静态审查高中/高二的 Python 文件，不导入 Manim。

使用：python tools/audit_grade11.py [--json] [--strict]
静态检查只识别可判定的风险，不能替代数学证明、渲染和关键帧验收。
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
AMBIGUOUS_SQRT = re.compile(r"\\sqrt\s*\{(?:-4|4|-a)\}\s*=\s*\\pm")
GENERIC_PLACEHOLDER = re.compile(r"正在学习.{1,80}的概念[.。…]{2,}")
SCENE_ACTIONS = {"play", "add", "wait", "add_sound"}


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
        return [part.value for part in expr.values
                if isinstance(part, ast.Constant) and isinstance(part.value, str)]
    return []


def _scene_has_actions(cls: ast.ClassDef) -> bool:
    """从 construct 追踪 self.helper() 调用；不能仅查 construct 内的 self.play。

    同名方法及循环委托使用 visited 防止无限递归。本检测仅涵盖当前类的显式方法，
    动态分派、基类中实现的 construct 需单独复核。
    """
    methods = {method.name: method for method in cls.body
               if isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef))}
    if "construct" not in methods:
        return False
    visited: set[str] = set()

    def walk_method(name: str) -> bool:
        if name in visited or name not in methods:
            return False
        visited.add(name)
        for node in ast.walk(methods[name]):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if not isinstance(node.func.value, ast.Name) or node.func.value.id != "self":
                continue
            if node.func.attr in SCENE_ACTIONS:
                return True
            if node.func.attr in methods and walk_method(node.func.attr):
                return True
        return False

    return walk_method("construct")


def audit_file(path: Path, root: Path) -> tuple[bool, list[dict[str, object]]]:
    relative = path.relative_to(root).as_posix()
    issues: list[dict[str, object]] = []

    def emit(code: str, severity: str, line: int, detail: str) -> None:
        issues.append({"file": relative, "line": line, "code": code,
                       "severity": severity, "detail": detail})

    try:
        module = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
    except (SyntaxError, UnicodeError, OSError) as exc:
        emit("PYTHON_SYNTAX", "error", getattr(exc, "lineno", 1) or 1, str(exc))
        return False, issues

    scene_classes = [cls for cls in module.body if isinstance(cls, ast.ClassDef)
                     and any(_name(base) in SCENE_BASES for base in cls.bases)]
    if not scene_classes:
        emit("NO_SCENE", "info", 1, "无直接 Scene 子类；可能是辅助模块")
    seen: set[str] = set()
    for cls in scene_classes:
        if cls.name in seen:
            emit("DUPLICATE_SCENE", "error", cls.lineno, "同文件重复的 Scene 类名")
        seen.add(cls.name)
        if not _scene_has_actions(cls):
            emit("EMPTY_SCENE", "warning", cls.lineno,
                 "construct 及可追踪的 self.helper 没有场景操作；需人工确认")

    for node in ast.walk(module):
        if isinstance(node, ast.Call) and _name(node.func) in {"MathTex", "Tex"}:
            for argument in node.args:
                for chunk in _chunks(argument):
                    if UNSAFE_TEX.search(chunk):
                        has_ctex = any(kw.arg == "tex_template"
                                       and _name(kw.value) == "ctex"
                                       for kw in node.keywords)
                        emit("UNICODE_MATHTEX", "info" if has_ctex else "warning",
                             node.lineno,
                             "数学公式含中文或 Unicode；ctex 可编译中文时仍建议中文独立使用 Text"
                             if has_ctex else "数学公式含中文或 Unicode；应使用 LaTeX 命令、中文使用 Text")
                    if AMBIGUOUS_SQRT.search(chunk):
                        emit("AMBIGUOUS_SQRT", "error", node.lineno,
                             "单值根号不可写成 ± 两个值；应列出方程的全部解")
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if GENERIC_PLACEHOLDER.search(node.value):
                emit("GENERIC_LESSON_PLACEHOLDER", "warning", node.lineno,
                     "疑似通用教学占位稿，需确认是否完成数学内容")
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
