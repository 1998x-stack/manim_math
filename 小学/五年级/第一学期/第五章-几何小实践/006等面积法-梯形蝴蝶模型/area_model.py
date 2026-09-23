"""蝴蝶模型纯几何：允许任意水平错位的凸梯形，不依赖 Manim。"""


def butterfly_areas(bottom: float, top: float, height: float) -> dict:
    """AB∥CD，O=AC∩BD；顺序为 AOB、COD、AOD、BOC。"""
    if bottom <= 0 or top <= 0 or height <= 0:
        raise ValueError("两底及高须为正，退化图形不适用")
    den = 2 * (bottom + top)
    return {
        "bottom": bottom * bottom * height / den,
        "top": top * top * height / den,
        "left": bottom * top * height / den,
        "right": bottom * top * height / den,
    }


def trapezoid_points(bottom: float, top: float, height: float, top_shift: float = 0.0):
    """A、B 在下，D、C 在上；O 由对角线内分比 AO:OC=bottom:top 求得。"""
    butterfly_areas(bottom, top, height)  # 对退化输入使用同一校验约定
    a, b = (-bottom / 2, -height / 2), (bottom / 2, -height / 2)
    d = (top_shift - top / 2, height / 2)
    c = (top_shift + top / 2, height / 2)
    t = bottom / (bottom + top)
    o = (a[0] + t * (c[0] - a[0]), a[1] + t * (c[1] - a[1]))
    return {"A": a, "B": b, "C": c, "D": d, "O": o}


def lesson_points():
    """主课配图：两底 6、3，梯形高 4，O=(0,2/3)。"""
    return trapezoid_points(6, 3, 4)


def altitude_segments(points):
    """交点 O 到下底和上底的垂直距离（而非两条斜线的长度）。"""
    o, a, d = points["O"], points["A"], points["D"]
    return {"bottom": o[1] - a[1], "top": d[1] - o[1]}


def cross(a, b, c) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def triangle_area(a, b, c) -> float:
    return abs(cross(a, b, c)) / 2


def common_area_decomposition(points):
    """O∈BD/AC：ABD=ABO+AOD；ABC=ABO+BOC。"""
    a, b, c, d, o = (points[key] for key in "ABCDO")
    return {
        "ABD": triangle_area(a, b, d),
        "ABC": triangle_area(a, b, c),
        "ABO": triangle_area(a, b, o),
        "AOD": triangle_area(a, o, d),
        "BOC": triangle_area(b, o, c),
    }
