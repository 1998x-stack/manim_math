"""七年级课程静态巡检（仅依赖 Python 标准库；不执行场景源码）。

用法：python tools/audit_grade7.py [--json] [--strict-warnings] [--root REPO]
本工具只检查语法、结构和可静态确认的排版风险；不能证明数学或渲染正确。
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

GRADE = Path("初中/七年级")
SCENE_BASES = {"Scene", "ThreeDScene", "MovingCameraScene", "ZoomedScene", "LinearTransformationScene"}
PLACEHOLDERS = ("更多动画元素可以根据需要添加", "正在学习", "这是一个重要的数学概念")
UNSAFE_TEX = set("÷×∠°")


def _name(expression: ast.expr) -> str | None:
    if isinstance(expression, ast.Name):
        return expression.id
    if isinstance(expression, ast.Attribute):
        return expression.attr
    return None


def _literals(call: ast.Call):
    return (arg.value for arg in call.args if isinstance(arg, ast.Constant) and isinstance(arg.value, str))


def _scene_classes(tree: ast.Module):
    return [node for node in tree.body if isinstance(node, ast.ClassDef)
            and any(_name(base) in SCENE_BASES for base in node.bases)]


def audit_tree(root: Path) -> dict:
    """扫描七年级所有源码/知识点；按文件、行号返回可复核的问题。"""
    root = Path(root).resolve()
    grade = root / GRADE
    issues: list[dict] = []

    def add(level: str, code: str, path: Path, line: int, message: str):
        issues.append({"severity": level, "code": code,
                       "file": path.relative_to(root).as_posix(), "line": line,
                       "message": message})

    if not grade.is_dir():
        add("error", "MISSING_DIRECTORY", grade, 0, "七年级课程目录不存在")
        return {"python_files": 0, "scene_files": 0, "topic_dirs": 0,
                "json_files": 0, "issues": issues}

    python_files = sorted(grade.rglob("*.py"))
    json_files = sorted(grade.rglob("*.json"))
    scene_files = 0
    for path in python_files:
        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
            compile(tree, str(path), "exec", dont_inherit=True)
        except (OSError, UnicodeError) as exc:
            add("error", "PYTHON_READ", path, 0, f"源码读取失败：{exc}")
            continue
        except SyntaxError as exc:
            add("error", "PYTHON_SYNTAX", path, exc.lineno or 0, f"语法错误：{exc.msg}")
            continue

        scenes = _scene_classes(tree)
        if scenes:
            scene_files += 1
        elif not path.name.startswith("_"):
            add("warning", "NO_DIRECT_SCENE", path, 0,
                "未发现直接继承 Manim Scene 的类；可能是辅助模块或自定义场景基类")
        for scene in scenes:
            constructs = [node for node in scene.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                          and node.name == "construct"]
            if not constructs:
                add("warning", "NO_CONSTRUCT", path, scene.lineno,
                    f"{scene.name} 没有直接定义 construct；检查是否预期继承实现")
            for method in constructs:
                statements = [stmt for stmt in method.body if not isinstance(stmt, ast.Expr)
                              or not isinstance(stmt.value, ast.Constant)
                              or not isinstance(stmt.value.value, str)]
                if not statements or all(isinstance(stmt, ast.Pass) for stmt in statements):
                    add("warning", "EMPTY_SCENE", path, method.lineno,
                        f"{scene.name}.construct 没有实际动画逻辑")

        if any(phrase in source for phrase in PLACEHOLDERS):
            add("warning", "TEMPLATE_CONTENT", path, 0,
                "存在泛化占位语句；请人工确认是否已完成真实教学内容")
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = _name(node.func)
            if name in {"MathTex", "Tex"}:
                for value in _literals(node):
                    if (any("\u4e00" <= ch <= "\u9fff" for ch in value)
                            or UNSAFE_TEX.intersection(value)):
                        add("warning", "NON_LATEX_MATH", path, node.lineno,
                            "MathTex/Tex 包含中文或非 LaTeX 数学字符；请检查 TeX 排版")
                        break
                    if any(ch in value for ch in ("\b", "\f", "\r")):
                        add("warning", "ESCAPED_TEX", path, node.lineno,
                            "MathTex/Tex 包含控制字符；检查是否误写了非 raw LaTeX 字符串")
                        break
            if name in {"Text", "MarkupText"}:
                for value in _literals(node):
                    if "\\n" in value:
                        add("warning", "LITERAL_NEWLINE", path, node.lineno,
                            "文字含字面量 \\n；请确认是否需要真正的换行")

    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            add("error", "INVALID_JSON", path, 0, f"JSON 读取或解析失败：{exc}")

    topic_dirs = {path.parent for path in json_files if path.name == "description.json"}
    for directory in sorted(topic_dirs):
        if not any(directory.glob("*.py")):
            add("warning", "TOPIC_WITHOUT_SOURCE", directory, 0,
                "知识点有 description.json 但没有同目录 Python 源码")
    issues.sort(key=lambda issue: (issue["file"], issue["line"], issue["code"]))
    return {"python_files": len(python_files), "scene_files": scene_files,
            "topic_dirs": len(topic_dirs), "json_files": len(json_files),
            "issues": issues}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true", help="输出可机器处理的完整报告")
    parser.add_argument("--strict-warnings", action="store_true", help="警告也导致退出码非零")
    args = parser.parse_args(argv)
    result = audit_tree(args.root)
    errors = sum(item["severity"] == "error" for item in result["issues"])
    warnings = len(result["issues"]) - errors
    if args.json:
        print(json.dumps({**result, "errors": errors, "warnings": warnings}, ensure_ascii=False, indent=2))
    else:
        print(f"七年级：{result['python_files']} 个 Python 文件，{result['scene_files']} 个 Scene 文件，"
              f"{result['topic_dirs']} 个知识点目录，{result['json_files']} 个 JSON 文件；"
              f"{errors} 个错误，{warnings} 个警告")
        for item in result["issues"]:
            print(f"[{item['severity']}] {item['code']} {item['file']}:{item['line']} {item['message']}")
    return int(bool(errors or (args.strict_warnings and warnings)))


if __name__ == "__main__":
    raise SystemExit(main())
