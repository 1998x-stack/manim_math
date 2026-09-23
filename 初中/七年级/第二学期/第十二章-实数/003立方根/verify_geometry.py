"""立方根独立验证脚本（仅标准库，不运行或替代 Manim 渲染）。

对比动画中的典型正、零、负立方根及正方体 2D 投影宽高。
运行：python verify_geometry.py
"""

from __future__ import annotations

from math import isclose


def real_cube_root(value: float) -> float:
    """实数立方根，避免对负数直接使用 value ** (1/3) 的复数分支。"""
    if value == 0:
        return 0.0
    return (1.0 if value > 0 else -1.0) * abs(value) ** (1.0 / 3.0)


def verify_cube_roots() -> None:
    for value, expected in ((-125, -5), (-27, -3), (-8, -2), (-1, -1),
                            (0, 0), (1, 1), (8, 2), (27, 3), (125, 5)):
        actual = real_cube_root(value)
        assert isclose(actual, expected, rel_tol=1e-12, abs_tol=1e-12), (value, actual)
        assert isclose(actual ** 3, value, rel_tol=1e-12, abs_tol=1e-12)
    for value in (-17.0, -0.125, 0.125, 17.0):
        root = real_cube_root(value)
        assert isclose(root ** 3, value, rel_tol=1e-12, abs_tol=1e-12)
    assert real_cube_root(-8) < 0 < real_cube_root(8)


def verify_cube_projection(side: float = 1.8) -> None:
    """验证 cube_root.py 的等轴测示意：顶面/侧面顶点和总尺寸。"""
    assert side > 0, "正方体示意边长应为正"
    ox, oy = side * 0.45, side * 0.25
    front = ((0, 0), (side, 0), (side, side), (0, side))
    top = ((0, side), (side, side), (side + ox, side + oy), (ox, side + oy))
    right = ((side, 0), (side, side), (side + ox, side + oy), (side + ox, oy))
    assert front[2] == top[1] == right[1]
    assert top[2] == right[2]
    points = front + top + right
    assert isclose(max(x for x, _ in points) - min(x for x, _ in points), side + ox)
    assert isclose(max(y for _, y in points) - min(y for _, y in points), side + oy)
    # 注意：该图仅为平面透视示意，不能用屏幕面积当作真实立体表面积。


def verify_geometry() -> None:
    verify_cube_roots()
    verify_cube_projection()


if __name__ == "__main__":
    verify_geometry()
    print("立方根例题与 2D 正方体投影数学校验通过")
