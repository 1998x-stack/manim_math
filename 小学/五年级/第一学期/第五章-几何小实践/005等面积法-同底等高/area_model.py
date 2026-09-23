"""同底等高的纯几何模型：图形派生点必须由坐标计算，不依赖 Manim。"""


def triangle_area(base: float, height: float) -> float:
    """非退化三角形面积；底与对应高均为正。"""
    if base <= 0 or height <= 0:
        raise ValueError("底和高必须为正")
    return base * height / 2


def signed_double_area(a, b, c) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def lesson_triangle(apex_x: float):
    """AB=6，C 位于平行线 y=1.3；动点可在该线上水平移动。"""
    if not -2.5 <= apex_x <= 2.5:
        raise ValueError("动画顶点须位于预定的可视区间")
    return (-3.0, -1.7), (3.0, -1.7), (float(apex_x), 1.3)


def altitude_foot(a, b, c):
    """点 C 到底边 AB 所在直线的正交投影；允许垂足落在线段延长线上。"""
    dx, dy = b[0] - a[0], b[1] - a[1]
    norm_sq = dx * dx + dy * dy
    if norm_sq == 0:
        raise ValueError("底边两端点不能重合")
    t = ((c[0] - a[0]) * dx + (c[1] - a[1]) * dy) / norm_sq
    return (a[0] + t * dx, a[1] + t * dy)


def lesson_area(apex_x: float) -> float:
    a, b, c = lesson_triangle(apex_x)
    return abs(signed_double_area(a, b, c)) / 2


def rectangle_diagonal_areas(base: float, height: float):
    """从左下到右上的对角线，将长方形切为两个同底等高三角形。"""
    total = base * height
    half = triangle_area(base, height)
    return {"rectangle": total, "lower": half, "upper": half}
