#!/usr/bin/env python3
"""ManimGX lesson AST migration/gotchas scanner.

Static evidence only; never imports or renders ManimGX. Use ty + manimgx inspect for API and
runtime/layout validation.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import sys

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
UNSUPPORTED_TEX = re.compile(r"\\(?:usepackage|def|newcommand)\b")
LEGACY_ANIMATIONS = {"ApplyMethod", "ScaleInPlace", "FadeToColor"}


def called_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def literal_strings(node: ast.AST):
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


def is_self_play(call: ast.AST) -> bool:
    return (
        isinstance(call, ast.Call)
        and isinstance(call.func, ast.Attribute)
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "self"
        and call.func.attr == "play"
    )


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
        key = (line, code)
        if key not in seen:
            seen.add(key)
            findings.append({"level": level, "line": line, "code": code, "message": message})

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if isinstance(node, ast.ImportFrom) and node.module and (node.module == "manim" or node.module.startswith("manim.")):
                report("ERROR", node, "CE_IMPORT", "生产 Scene 不得再导入 Manim Community；改用 manimgx 顶层公开 API。")
            elif isinstance(node, ast.Import) and any(alias.name == "manim" or alias.name.startswith("manim.") for alias in node.names):
                report("ERROR", node, "CE_IMPORT", "生产 Scene 不得再导入 Manim Community；改用 manimgx。")

        if isinstance(node, ast.ClassDef):
            base_names = {called_name(base) or "" for base in node.bases}
            if any(name.endswith("Scene") for name in base_names):
                scene_class = True
            if "MovingCameraScene" in base_names:
                report("ERROR", node, "LEGACY_SCENE_ALIAS", "ManimGX 迁移应改为 Scene 并使用 camera/frame 的公开 API。")

        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                if (
                    isinstance(target, ast.Attribute)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == "config"
                ):
                    dimensions.add(target.attr)
                    if target.attr == "frame_width":
                        report("ERROR", target, "READONLY_FRAME_WIDTH", "ManimGX config.frame_width 为推导只读值；设置像素宽高与 frame_height。")

        if not isinstance(node, ast.Call):
            continue
        name = called_name(node.func)

        if name in {"MathTex", "Tex"}:
            text_args = [*node.args, *(kw.value for kw in node.keywords if kw.arg in {"tex_strings", "text"})]
            fragments = [fragment for arg in text_args for fragment in literal_strings(arg)]
            dynamic = not text_args or any(not is_literal(arg) for arg in text_args)
            if any(kw.arg == "tex_template" for kw in node.keywords):
                report("ERROR", node, "LEGACY_TEX_TEMPLATE", "ManimGX 不使用 CE TexTemplate；改为 MathTex 支持语法或 Typst/MathTypst。")
            if any(UNSUPPORTED_TEX.search(fragment) for fragment in fragments):
                report("ERROR", node, "UNSUPPORTED_TEX_MACRO", "ManimGX mitex/Typst 不支持 LaTeX package、\\def 或自定义 package 宏。")
            if any(CJK.search(fragment) for fragment in fragments):
                report("WARN", node, "CJK_IN_MATHTEX_REVIEW", "中文教学文本优先 Text；MathTex/Tex 中 CJK 需用实际 ManimGX inspect/render 核验。")
            if any("°" in fragment for fragment in fragments):
                report("ERROR", node, "DEGREE_IN_MATHTEX", "数学度数优先使用 ^\\circ；普通中文/度号说明使用 Text。")
            if dynamic:
                report("WARN", node, "DYNAMIC_TEX", "动态公式必须对实际展开字符串和 mitex/Typst 排版逐一核验。")

        if name in LEGACY_ANIMATIONS:
            report("ERROR", node, "LEGACY_ANIMATION_ALIAS", f"{name} 属于迁移遗留；新 ManimGX 代码使用 .animate/主 API。")

        if is_self_play(node):
            for arg in node.args:
                if any(is_self_play(item) for item in ast.walk(arg)):
                    report("ERROR", arg, "NESTED_SELF_PLAY", "不可把 self.play(...) 的返回值传给另一次 play。")
                if isinstance(arg, ast.IfExp) and (is_empty_animation_list(arg.body) or is_empty_animation_list(arg.orelse)):
                    report("ERROR", arg, "PLAY_EMPTY_ANIMATION", "条件分支不得把 [] 作为单个 play 参数；先构建列表并展开。")
                if is_empty_animation_list(arg):
                    report("ERROR", arg, "PLAY_EMPTY_ANIMATION", "不可把 [] 直接传给 self.play。")

        if name == "seed" and isinstance(node.func, ast.Attribute):
            parent = node.func.value
            is_numpy = isinstance(parent, ast.Attribute) and parent.attr == "random" and isinstance(parent.value, ast.Name) and parent.value.id in {"np", "numpy"}
            is_python = isinstance(parent, ast.Name) and parent.id == "random"
            if is_numpy or is_python:
                report("WARN", node, "GLOBAL_RNG_SEED", "全局 RNG 会污染后续场景；优先局部 default_rng(seed) / random.Random(seed)。")

        if name == "plot":
            for kw in node.keywords:
                if kw.arg != "x_range" or not isinstance(kw.value, (ast.List, ast.Tuple)) or len(kw.value.elts) < 2:
                    continue
                first, last = kw.value.elts[:2]
                if (
                    isinstance(first, ast.Constant)
                    and isinstance(last, ast.Constant)
                    and type(first.value) in {int, float}
                    and type(last.value) in {int, float}
                    and first.value == last.value
                ):
                    report("ERROR", node, "ZERO_WIDTH_PLOT", "x_range 两端相等；动态曲线还需验证首帧与函数定义域。")

    if not scene_class:
        report("WARN", tree, "NO_SCENE_CLASS", "未静态识别 Scene 类；独立数学测试可忽略，否则核实真实类名。")
    if "frame_height" not in dimensions:
        report("WARN", tree, "FRAME_HEIGHT_NOT_EXPLICIT", "未观察到 frame_height；若依赖仓库/CLI 外部配置请显式记录。")
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
        findings = [{"level": "ERROR", "line": getattr(exc, "lineno", 0) or 0, "code": "INPUT", "message": str(exc)}]
    errors = sum(x["level"] == "ERROR" for x in findings)
    warnings = sum(x["level"] == "WARN" for x in findings)
    if args.json:
        print(json.dumps({"file": str(args.scene), "errors": errors, "warnings": warnings, "findings": findings}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            print(f'{args.scene}:{item["line"]}: {item["level"]} {item["code"]}: {item["message"]}')
        print(f"ManimGX AST audit: {errors} error(s), {warnings} warning(s); no render performed.")
    return 2 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
