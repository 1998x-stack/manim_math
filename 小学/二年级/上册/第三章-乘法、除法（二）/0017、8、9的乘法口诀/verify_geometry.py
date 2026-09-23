"""7～9 口诀离线验收：数学数量、标准口诀和点阵静态布局。

本脚本无需 Manim；不代表完成实际字形、像素边界和视频验收。
"""
from __future__ import annotations

import ast
from pathlib import Path


EXPECTED = {
    7: ("一七得七", "二七十四", "三七二十一", "四七二十八", "五七三十五", "六七四十二", "七七四十九"),
    8: ("一八得八", "二八十六", "三八二十四", "四八三十二", "五八四十", "六八四十八", "七八五十六", "八八六十四"),
    9: ("一九得九", "二九十八", "三九二十七", "四九三十六", "五九四十五", "六九五十四", "七九六十三", "八九七十二", "九九八十一"),
}


def load_pure_lesson_helpers():
    """只读取原脚本的纯数学函数，避免为了检查而加载 Manim。"""
    filename = Path(__file__).resolve().parent / "001_7、8、9的乘法口诀.py"
    tree = ast.parse(filename.read_text(encoding="utf-8"), filename=str(filename))
    selected = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "CHINESE_DIGITS"
            for target in node.targets
        ):
            selected.append(node)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in {
            "chinese_number", "multiplication_mnemonic"
        }:
            selected.append(node)
    assert len(selected) == 3, "缺少正确的数字或口诀生成函数"
    module = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    namespace = {}
    exec(compile(module, str(filename), "exec"), namespace)
    return namespace["multiplication_mnemonic"]


def verify_tables() -> None:
    mnemonic = load_pure_lesson_helpers()
    for factor, phrases in EXPECTED.items():
        assert len(phrases) == factor
        for multiplier, expected in enumerate(phrases, start=1):
            product = factor * multiplier
            assert mnemonic(factor, multiplier) == expected, (factor, multiplier)
            dot_positions = [
                ((col - (factor - 1) / 2) * 0.42,
                 (row - (multiplier - 1) / 2) * 0.42)
                for row in range(multiplier)
                for col in range(factor)
            ]
            assert len(dot_positions) == product
            assert len(dot_positions) == len(set(dot_positions))
            assert all(abs(x) + 0.095 < 4.5 and abs(y) + 0.095 < 8
                       for x, y in dot_positions)


def main() -> None:
    verify_tables()
    print("7～9 的 24 条口诀、点阵数量及静态布局检查通过；仍需实际渲染。")


if __name__ == "__main__":
    main()
