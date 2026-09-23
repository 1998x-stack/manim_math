"""纯数学模型：同底、等高三角形（无 Manim 依赖）。

坐标单位对应 cm；改变第三个顶点的水平坐标，不改变面积。
"""


def triangle_area(base: float, height: float) -> float:
    """返回非退化三角形的面积；长度必须为正。"""
    if base <= 0 or height <= 0:
        raise ValueError("底和高必须为正")
    return base * height / 2


def signed_double_area(a, b, c) -> float:
    """有向面积的两倍；接受二维点坐标。"""
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def lesson_triangle(apex_x: float):
    """底 AB=6，高=3；C 在与 AB 平行的直线 y=1.3 上。"""
    if not -2.5 <= apex_x <= 2.5:
        raise ValueError("动画顶点须位于预定的可视区间")
    a, b, c = (-3.0, -1.7), (3.0, -1.7), (float(apex_x), 1.3)
    return a, b, c


def lesson_area(apex_x: float) -> float:
    a, b, c = lesson_triangle(apex_x)
    return abs(signed_double_area(a, b, c)) / 2
