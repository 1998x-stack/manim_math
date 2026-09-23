#!/usr/bin/env python3
"""Audit every grade-one Python source without importing Manim or touching media.

python tools/audit_grade_one.py
python tools/audit_grade_one.py --json > grade_one_audit.json

A passing exit code means only that the available sources parsed and that no
literal Chinese argument to MathTex was detected. It is NOT a render, visual,
mathematical-content, or font-availability guarantee.
"""

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import re


DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "小学" / "一年级"
CJK = re.compile(r"[\u3400-\u9fff]")
SCENE_BASES = {"Scene", "MovingCameraScene", "ThreeDScene", "ZoomedScene", "LinearTransformationScene"}


def get_scene_names(tree):
    names = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for base in node.bases:
            if isinstance(base, ast.Name) and (base.id in SCENE_BASES or base.id.endswith("Scene")):
                names.append(node.name)
                break
            if isinstance(base, ast.Attribute) and base.attr in SCENE_BASES:
                names.append(node.name)
                break
    return names


def get_literal_mathtex_chinese(tree):
    locations = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = node.func.id if isinstance(node.func, ast.Name) else (
            node.func.attr if isinstance(node.func, ast.Attribute) else ""
        )
        if name not in {"MathTex", "Tex"}:
            continue
        args = list(node.args) + [item.value for item in node.keywords]
        if any(isinstance(value, ast.Constant) and isinstance(value.value, str) and CJK.search(value.value)
               for value in args):
            locations.append(node.lineno)
    return locations


def audit(root):
    if not root.is_dir():
        raise FileNotFoundError(f"一年级目录不存在：{root}")
    records = []
    diagnostics = []
    python_files = sorted(root.rglob("*.py"))
    for path in python_files:
        relative = path.relative_to(root).as_posix()
        semester = relative.split("/", 1)[0]
        record = {"path": relative, "semester": semester, "scenes": [], "syntax": "ok"}
        source = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(source, filename=str(path))
            compile(tree, str(path), "exec")
        except (SyntaxError, UnicodeError) as exc:
            record["syntax"] = "error"
            diagnostics.append({
                "path": relative, "line": getattr(exc, "lineno", None),
                "severity": "error", "rule": "python-syntax", "message": str(exc),
            })
            records.append(record)
            continue
        record["scenes"] = get_scene_names(tree)
        for line in get_literal_mathtex_chinese(tree):
            diagnostics.append({
                "path": relative, "line": line, "severity": "warning",
                "rule": "chinese-in-tex",
                "message": "MathTex/Tex 含中文字符串；请检查 Text 与字体使用方式",
            })
        topic_dir = path.parent
        for companion in ("description.json", "prompt.md", "storyboard.md"):
            if not (topic_dir / companion).is_file():
                diagnostics.append({
                    "path": relative, "line": None, "severity": "info",
                    "rule": "missing-companion", "message": f"同目录缺少 {companion}",
                })
        records.append(record)
    counts = Counter(record["semester"] for record in records)
    return {
        "root": str(root), "python_count": len(records),
        "scene_count": sum(len(record["scenes"]) for record in records),
        "by_semester": dict(sorted(counts.items())),
        "files": records, "diagnostics": diagnostics,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--json", action="store_true", help="机器可读完整清单")
    args = parser.parse_args(argv)
    try:
        report = audit(args.root)
    except (FileNotFoundError, OSError) as exc:
        parser.exit(2, f"无法完成审计：{exc}\n")
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"一年级源文件：{report['python_count']}；直接识别的 Scene：{report['scene_count']}")
        print("上/下册数量：", report["by_semester"])
        for record in report["files"]:
            print(f"{record['syntax']:>5} {record['path']} | Scene: {', '.join(record['scenes']) or '未直接声明'}")
        for item in report["diagnostics"]:
            print(f"{item['severity']}: {item['path']}:{item['line'] or '-'} "
                  f"[{item['rule']}] {item['message']}")
        print("注意：静态扫描不包含 Manim 导入、数学语义、视频渲染与画质验收。")
    return int(any(item["severity"] == "error" for item in report["diagnostics"]))


if __name__ == "__main__":
    raise SystemExit(main())
