"""九年级课程静态审计（不依赖 Manim；不替代视频或数学验收）。

Usage: python tools/audit_grade9.py [--json] [--warnings-as-errors]
"""

import argparse
import ast
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
GRADE_REL = Path("初中/九年级")
CHAPTERS = {
    "第一学期": ("第二十四章-相似三角形", "第二十五章-锐角的三角比", "第二十六章-二次函数"),
    "第二学期": ("第二十七章-圆与正多边形", "第二十八章-统计初步"),
}
LATEX_UNSAFE = set("÷×∠°≤≥")


def _call_name(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return ""


def _literal_strings(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        yield node.value
    elif isinstance(node, ast.JoinedStr):
        for item in node.values:
            if isinstance(item, ast.Constant) and isinstance(item.value, str):
                yield item.value


def _call_strings(call):
    for arg in call.args:
        yield from _literal_strings(arg)


def _is_zero_width_plot(call):
    if _call_name(call.func) != "plot":
        return False
    for keyword in call.keywords:
        if keyword.arg != "x_range" or not isinstance(keyword.value, (ast.List, ast.Tuple)):
            continue
        values = keyword.value.elts
        if len(values) >= 2:
            try:
                left = ast.literal_eval(values[0])
                right = ast.literal_eval(values[1])
            except (ValueError, TypeError, MemoryError, RecursionError):
                continue
            if isinstance(left, (int, float)) and left == right:
                return True
    return False


def _quadratic_plot_risk(tree):
    """仅识别可证明的标准 x² 抛物线示例；不执行任意源代码。"""
    y_top = x_limit = None
    has_square = False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Attribute) or not isinstance(target.value, ast.Name) or target.value.id != "self":
            continue
        if target.attr in {"AX_Y", "CURVE_X"}:
            try:
                sequence = ast.literal_eval(node.value)
                if target.attr == "AX_Y":
                    y_top = sequence[1]
                else:
                    x_limit = max(abs(sequence[0]), abs(sequence[1]))
            except (ValueError, TypeError, IndexError, MemoryError, RecursionError):
                pass
        if target.attr == "f_std" and isinstance(node.value, ast.Lambda):
            body = node.value.body
            has_square = (isinstance(body, ast.BinOp) and isinstance(body.op, ast.Pow)
                          and isinstance(body.left, ast.Name) and body.left.id == "x"
                          and isinstance(body.right, ast.Constant) and body.right.value == 2)
    return (has_square and isinstance(y_top, (int, float))
            and isinstance(x_limit, (int, float)) and x_limit**2 > y_top), x_limit, y_top


def audit(root=REPO_ROOT):
    """返回结构化报告：每课源码与 JSON 的可读性、语法和已知高风险写法。"""
    root = Path(root)
    grade = root / GRADE_REL
    issues = []
    files = []
    if not grade.is_dir():
        return {"python_files": 0, "json_files": 0, "topics": 0,
                "issues": [{"severity": "error", "path": str(GRADE_REL),
                            "line": 0, "message": "九年级目录不存在"}]}

    def report(severity, path, line, message):
        issues.append({"severity": severity, "path": path.relative_to(root).as_posix(),
                       "line": line, "message": message})

    topics = 0
    for semester, chapters in CHAPTERS.items():
        for chapter in chapters:
            chapter_path = grade / semester / chapter
            if not chapter_path.is_dir():
                report("error", chapter_path, 0, "课程章节目录缺失")
                continue
            for lesson in sorted(path for path in chapter_path.iterdir() if path.is_dir()):
                topics += 1
                scene_files = sorted(lesson.glob("*.py"))
                if not scene_files:
                    report("warning", lesson, 0, "知识点未提供 Python 场景源码")
                files.extend(scene_files)
                metadata = lesson / "description.json"
                if not metadata.is_file():
                    report("warning", lesson, 0, "缺少 description.json")
                else:
                    try:
                        payload = json.loads(metadata.read_text(encoding="utf-8"))
                        if not isinstance(payload, dict) or payload.get("年级") != "九年级":
                            report("warning", metadata, 0, "元数据年级不匹配")
                        elif payload.get("学期") != semester:
                            report("warning", metadata, 0, "元数据学期与目录不匹配")
                    except (OSError, UnicodeError, ValueError) as exc:
                        report("error", metadata, 0, f"JSON 无法读取或解析：{exc}")

    for path in files:
        try:
            source = path.read_text(encoding="utf-8")
            tree = ast.parse(source, filename=str(path))
        except (OSError, UnicodeError) as exc:
            report("error", path, 0, f"Python 源码无法读取：{exc}")
            continue
        except SyntaxError as exc:
            report("error", path, exc.lineno or 0, f"Python 语法错误：{exc.msg}")
            continue

        scene_classes = [node for node in tree.body if isinstance(node, ast.ClassDef)
                         and any(_call_name(base).endswith("Scene") for base in node.bases)]
        if not scene_classes:
            report("warning", path, 0, "未发现直接继承 Scene 的场景类；确认是否为可渲染课件")
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            call_name = _call_name(node.func)
            if call_name in {"MathTex", "Tex"}:
                for text in _call_strings(node):
                    if any("\u4e00" <= char <= "\u9fff" for char in text) or LATEX_UNSAFE.intersection(text):
                        report("warning", path, node.lineno,
                               "MathTex/Tex 中有中文或不兼容的 Unicode 数学符号")
                        break
            if call_name == "play":
                if any(isinstance(arg, ast.IfExp) and isinstance(arg.orelse, ast.List)
                       and not arg.orelse.elts for arg in node.args):
                    report("warning", path, node.lineno,
                           "self.play 的分支可能传入 [] 而不是 Animation")
            if _is_zero_width_plot(node):
                report("error", path, node.lineno, "Axes.plot 的固定 x_range 宽度为零")

        if path.name == "quadratic_function.py":
            at_risk, x_limit, y_top = _quadratic_plot_risk(tree)
            if at_risk:
                report("warning", path, 0,
                       f"标准抛物线 x² 在 |x|={x_limit:g} 时高为 {x_limit**2:g}，超出纵轴上限 {y_top:g}")
            if "ValueTracker(self.CURVE_X[0])" in source and "x_range=[self.CURVE_X[0], t.get_value()]" in source:
                report("warning", path, 0, "动态曲线初始 x_range 端点重合；应从正区间开始绘制")

    issues.sort(key=lambda issue: (issue["path"], issue["line"], issue["severity"], issue["message"]))
    return {"python_files": len(files), "json_files": len(list(grade.rglob("*.json"))),
            "topics": topics, "issues": issues}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args(argv)
    result = audit()
    errors = sum(issue["severity"] == "error" for issue in result["issues"])
    warnings = len(result["issues"]) - errors
    if args.json:
        print(json.dumps({**result, "errors": errors, "warnings": warnings},
                         ensure_ascii=False, indent=2))
    else:
        print(f"九年级：{result['topics']} 个知识点，{result['python_files']} 个 Python 场景，"
              f"{result['json_files']} 个 JSON 文件；{errors} 个错误，{warnings} 个警告")
        for issue in result["issues"]:
            print(f"[{issue['severity']}] {issue['path']}:{issue['line']} {issue['message']}")
    return int(bool(errors or (warnings and args.warnings_as_errors)))


if __name__ == "__main__":
    raise SystemExit(main())
