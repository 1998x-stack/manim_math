#!/usr/bin/env python3
"""Manim lesson AST gotchas scanner. Static evidence only; never imports/renders Manim.

python audit_scene.py lesson.py [--json] [--strict]
Exit 2 for parse failure or confirmed AST errors; strict also fails on review warnings.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
BAD_KW = {"Sector": {"inner_radius", "outer_radius"}, "Rectangle": {"corner_radius"}}


def called_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def literal_strings(node: ast.AST):
    """Yield static literal fragments, including f-string text; expressions stay unknown."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        yield node.value
    elif isinstance(node, ast.JoinedStr):
        for part in node.values:
            yield from literal_strings(part)
    elif isinstance(node, (ast.Tuple, ast.List)):
        for part in node.elts:
            yield from literal_strings(part)


def is_literal(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def ctex_explicit(call: ast.Call) -> bool:
    """Only an explicit ctex template at this call qualifies for a review exception."""
    for kw in call.keywords:
        if kw.arg != "tex_template":
            continue
        value = kw.value
        if (isinstance(value, ast.Attribute) and value.attr == "ctex"
                and isinstance(value.value, ast.Name) and value.value.id == "TexTemplateLibrary"):
            return True
    return False


def is_self_play(call: ast.AST) -> bool:
    return (isinstance(call, ast.Call) and isinstance(call.func, ast.Attribute)
            and isinstance(call.func.value, ast.Name)
            and call.func.value.id == "self" and call.func.attr == "play")


def is_empty_animation_list(node: ast.AST) -> bool:
    return isinstance(node, (ast.List, ast.Tuple)) and not node.elts


def audit_source(source: str) -> list[dict]:
    tree = ast.parse(source)
    findings: list[dict] = []
    scene_class = False
    dimensions: set[str] = set()
    seen: set[tuple[int, str]] = set()

    def report(level: str, node: ast.AST, code: str, message: str):
        line = getattr(node, "lineno", 1)
        if (line, code) not in seen:
            seen.add((line, code))
            findings.append({"level": level, "line": line, "code": code, "message": message})

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and any(
            (called_name(base) or "").endswith("Scene") for base in node.bases
        ):
            scene_class = True
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if (isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name)
                        and target.value.id == "config"):
                    dimensions.add(target.attr)
        if not isinstance(node, ast.Call):
            continue
        name = called_name(node.func)
        if name in {"MathTex", "Tex"}:
            text_args = [*node.args, *(kw.value for kw in node.keywords if kw.arg == "tex_strings")]
            fragments = [fragment for arg in text_args for fragment in literal_strings(arg)]
            dynamic = not text_args or any(not is_literal(arg) for arg in text_args)
            has_ctex = ctex_explicit(node)
            if any(CJK.search(fragment) for fragment in fragments):
                if has_ctex:
                    report("WARN", node, "CTEX_REVIEW", "显式 ctex 中文仍需在目标 LaTeX/字体环境编译核验。")
                else:
                    report("ERROR", node, "CJK_IN_TEX", "默认 Tex/MathTex 不应包含中文；拆分为 Text + MathTex 或配置并实测 ctex。")
            if any("°" in fragment for fragment in fragments):
                report("ERROR", node, "DEGREE_IN_TEX", "数学度数用 ^\\circ；Text 中的 Unicode 度号可以保留。")
            if dynamic:
                report("WARN", node, "DYNAMIC_TEX", "含动态参数/f-string 的 TeX 必须对实际字符串、中文和编译逐一核验。")
        if name in BAD_KW:
            for kw in node.keywords:
                if kw.arg in BAD_KW[name]:
                    report("ERROR", node, "UNSUPPORTED_KEYWORD", f"检查当前 Manim 版本；{name} 不接受 {kw.arg}，考虑对应专用图形类。")
        if is_self_play(node):
            for arg in node.args:
                if any(is_self_play(item) for item in ast.walk(arg)):
                    report("ERROR", arg, "NESTED_SELF_PLAY", "不可把 self.play(...) 的返回值当作另一次 play 的动画参数。")
                if isinstance(arg, ast.IfExp) and (is_empty_animation_list(arg.body)
                                                    or is_empty_animation_list(arg.orelse)):
                    report("ERROR", arg, "PLAY_EMPTY_ANIMATION", "条件分支不得把 [] 作为单个 play 参数；先构建列表，再使用 *animations。")
                if is_empty_animation_list(arg):
                    report("ERROR", arg, "PLAY_EMPTY_ANIMATION", "不可把 [] 直接传给 self.play；展开动画列表或跳过调用。")
        if name == "seed" and isinstance(node.func, ast.Attribute):
            parent = node.func.value
            is_numpy = (isinstance(parent, ast.Attribute) and parent.attr == "random"
                        and isinstance(parent.value, ast.Name) and parent.value.id in {"np", "numpy"})
            is_python = isinstance(parent, ast.Name) and parent.id == "random"
            if is_numpy or is_python:
                report("WARN", node, "GLOBAL_RNG_SEED", "全局 RNG 影响后续场景；优先使用局部 default_rng(seed) / random.Random(seed)。")
        if name == "plot":
            for kw in node.keywords:
                if kw.arg != "x_range" or not isinstance(kw.value, (ast.List, ast.Tuple)) or len(kw.value.elts) < 2:
                    continue
                first, last = kw.value.elts[:2]
                if (isinstance(first, ast.Constant) and isinstance(last, ast.Constant)
                        and type(first.value) in {int, float} and type(last.value) in {int, float}
                        and first.value == last.value):
                    report("ERROR", node, "ZERO_WIDTH_PLOT", "x_range 两端字面量相等；动态图另需检验首帧非零宽与函数实际值域。")
    if not scene_class:
        report("WARN", tree, "NO_SCENE_CLASS", "未静态识别 Scene 类；核实真实类名，独立数学测试脚本可忽略。")
    if not {"frame_width", "frame_height"}.issubset(dimensions):
        report("WARN", tree, "FRAME_NOT_EXPLICIT", "未静态观察到完整画幅配置；核实运行时 9:16 配置或外部配置文件。")
    return sorted(findings, key=lambda item: (item["line"], item["code"]))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scene", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="also fail on warnings after manual triage")
    args = parser.parse_args(argv)
    try:
        findings = audit_source(args.scene.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        findings = [{"level": "ERROR", "line": getattr(exc, "lineno", 0) or 0,
                     "code": "INPUT", "message": str(exc)}]
    errors = sum(x["level"] == "ERROR" for x in findings)
    warnings = sum(x["level"] == "WARN" for x in findings)
    if args.json:
        print(json.dumps({"file": str(args.scene), "errors": errors, "warnings": warnings,
                          "findings": findings}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f'{args.scene}:{item["line"]}: {item["level"]} {item["code"]}: {item["message"]}')
        print(f"AST audit: {errors} error(s), {warnings} warning(s); no Manim render performed.")
    return 2 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
