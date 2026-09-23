"""有余数的除法：不依赖 Manim 的数学和静态布局检查。

执行：python verify_geometry.py。该文件不检查实际字形、遮挡或视频帧，渲染验收仍必需。
"""
from __future__ import annotations

import ast
from pathlib import Path


TOTAL = 13
CHILDREN = 4
FRAME_WIDTH = 9.0
FRAME_HEIGHT = 16.0
BOX_WIDTH = 1.88
DOT_RADIUS = 0.14
CENTERS = (-3.1, -1.05, 1.05, 3.1)


def verify_distribution() -> None:
    """检查每个原始物体最多分配一次，分配数量与余数、除数一致。"""
    quotient, remainder = divmod(TOTAL, CHILDREN)
    assert (quotient, remainder) == (3, 1)
    assert TOTAL == CHILDREN * quotient + remainder
    assert 0 <= remainder < CHILDREN
    assigned_indices = [
        round_index * CHILDREN + child_index
        for round_index in range(quotient)
        for child_index in range(CHILDREN)
    ]
    leftover_indices = set(range(TOTAL)) - set(assigned_indices)
    assert len(assigned_indices) == len(set(assigned_indices)) == 12
    assert leftover_indices == {12}


def verify_static_positions() -> None:
    """检查与当前分组动画一致的数值布局；不等同于实际画面边界检查。"""
    quotient, _ = divmod(TOTAL, CHILDREN)
    half_width, half_height = FRAME_WIDTH / 2, FRAME_HEIGHT / 2
    assert len(CENTERS) == CHILDREN
    for center_x in CENTERS:
        assert abs(center_x) + BOX_WIDTH / 2 <= half_width
        for round_index in range(quotient):
            x = center_x + (round_index - 1) * 0.43
            y = -0.7
            assert abs(x - center_x) + DOT_RADIUS < BOX_WIDTH / 2
            assert abs(x) + DOT_RADIUS < half_width
            assert abs(y) + DOT_RADIUS < half_height
    for index in range(TOTAL):
        x = ((index % 4) - 1.5) * 0.57
        y = 3.45 - (index // 4) * 0.53
        assert abs(x) + DOT_RADIUS < half_width
        assert abs(y) + DOT_RADIUS < half_height
    assert abs(-2.75) + DOT_RADIUS < half_height  # 余数位置


def verify_latex_literals() -> None:
    """检查同一课两个 Scene 的 MathTex 字面量没有直接放入中文或 Unicode 符号。"""
    directory = Path(__file__).resolve().parent
    scene_files = (
        directory / "002_有余数的除法.py",
        directory / "you_shu_shu_de_chu_fa.py",
    )
    for filename in scene_files:
        tree = ast.parse(filename.read_text(encoding="utf-8"), filename=str(filename))
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else ""
            )
            if name == "MathTex":
                for argument in node.args:
                    if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                        assert argument.value.isascii(), (
                            f"{filename.name}:{argument.lineno}: MathTex 字面量含非 ASCII 字符"
                        )


def main() -> None:
    verify_distribution()
    verify_static_positions()
    verify_latex_literals()
    print("数学不变量和静态布局检查通过；尚需真实渲染与逐帧验收。")


if __name__ == "__main__":
    main()
