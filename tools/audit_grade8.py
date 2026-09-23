"""八年级 Manim 场景静态审计；不导入或执行课程脚本，也不依赖 Manim。

运行：python tools/audit_grade8.py [--root 初中/八年级] [--json] [--strict]
检查仅发现可静态定位的问题；不能取代数学证明、运行时或逐帧画面审核。
"""

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import re

GRADE_ROOT = Path(__file__).resolve().parents[1] / "初中" / "八年级"
CJK = re.compile(r"[\u3400-\u9fff]")


def _call_name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _call_name(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return ""


def audit_source(source, filename="<source>"):
    """输出明确的风险码和 1-based 行号；不执行传入的任何代码。"""
    findings = []

    def record(node, code, level, message):
        findings.append({"path": str(filename), "line": node.lineno,
                         "code": code, "level": level, "message": message})

    try:
        tree = ast.parse(source, filename=str(filename))
    except SyntaxError as exc:
        findings.append({"path": str(filename), "line": exc.lineno or 1,
                         "code": "PY_SYNTAX", "level": "error",
                         "message": exc.msg})
        return findings

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = _call_name(node.func)
        if name in {"MathTex", "Tex"}:
            # 仅对字面量直接判断；动态拼接必须由人工/渲染审阅。
            if any(isinstance(arg, ast.Constant)
                   and isinstance(arg.value, str) and CJK.search(arg.value)
                   for arg in node.args):
                record(node, "CJK_IN_LATEX", "warning",
                       "中文直接传入 MathTex/Tex；建议中文用 Text 或配置明确的中文 LaTeX 模板")
        if name == "FadeOut" and node.args:
            arg = node.args[0]
            # FadeOut(SurroundingRectangle(...).set_opacity(0)) 也属于此类。
            while isinstance(arg, ast.Call) and isinstance(arg.func, ast.Attribute):
                if arg.func.attr in {"set_opacity", "set_fill", "set_stroke", "move_to"}:
                    arg = arg.func.value
                else:
                    break
            if isinstance(arg, ast.Call) and _call_name(arg.func) == "SurroundingRectangle":
                record(node, "FADEOUT_NEW_RECT", "error",
                       "FadeOut 新建高亮框不会移除先前显示的对象；保存并淡出原对象")
        if name in {"np.random.seed", "numpy.random.seed", "random.seed"}:
            record(node, "GLOBAL_RNG_SEED", "warning",
                   "全局随机种子可能污染其他场景；建议使用独立 Generator/Random 实例")
        if name == "scene.render" or name == "self.render":
            record(node, "DIRECT_RENDER", "info",
                   "直接调用 render 的入口需人工确认与 Manim CLI/配置兼容")
    return sorted(findings, key=lambda finding: (finding["line"], finding["code"]))


def audit_tree(root=GRADE_ROOT):
    """遍历两学期全部 Python 文件，按章节统计，并记录真实 Scene 类名。"""
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"八年级目录不存在：{root}")
    files = sorted(root.rglob("*.py"))
    reports = []
    chapters = Counter()
    findings = []
    for path in files:
        relative = path.relative_to(root)
        chapter = "/".join(relative.parts[:2]) if len(relative.parts) >= 2 else "未分类"
        chapters[chapter] += 1
        source = path.read_text(encoding="utf-8-sig")
        diagnostics = audit_source(source, relative.as_posix())
        findings.extend(diagnostics)
        scenes = []
        try:
            tree = ast.parse(source, filename=str(relative))
        except SyntaxError:
            pass
        else:
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and any(
                    _call_name(base).endswith("Scene")
                    for base in node.bases
                ):
                    scenes.append(node.name)
        reports.append({"path": relative.as_posix(), "chapter": chapter,
                        "scenes": scenes, "finding_codes": [item["code"] for item in diagnostics]})
    return {"root": str(root), "files_scanned": len(files),
            "chapters": dict(sorted(chapters.items())),
            "finding_counts": dict(sorted(Counter(item["code"] for item in findings).items())),
            "files": reports, "findings": findings}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=GRADE_ROOT)
    parser.add_argument("--json", action="store_true", help="输出可机器读取的审计报告")
    parser.add_argument("--strict", action="store_true", help="存在静态 error 时退出 1")
    args = parser.parse_args(argv)
    try:
        report = audit_tree(args.root)
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"扫描 {report['files_scanned']} 个 Python 文件，覆盖 {len(report['chapters'])} 个章节")
        for entry in report["findings"]:
            print(f"{entry['level']} {entry['code']} {entry['path']}:{entry['line']}: {entry['message']}")
    return int(args.strict and any(item["level"] == "error" for item in report["findings"]))


if __name__ == "__main__":
    raise SystemExit(main())
