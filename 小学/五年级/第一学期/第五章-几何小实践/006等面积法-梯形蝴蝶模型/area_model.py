"""梯形蝴蝶模型的纯数学模型；长度单位 cm，面积单位 cm²。"""


def butterfly_areas(bottom: float, top: float, height: float) -> dict:
    """AB∥DC，O=AC∩BD；返回 AOB/COD/AOD/BOC 四块面积。

    对任意凸梯形均成立，顶点不要求关于中轴对称。
    """
    if bottom <= 0 or top <= 0 or height <= 0:
        raise ValueError("两底及高须为正，退化图形不适用")
    denominator = 2 * (bottom + top)
    return {
        "bottom": bottom * bottom * height / denominator,
        "top": top * top * height / denominator,
        "left": bottom * top * height / denominator,
        "right": bottom * top * height / denominator,
    }


def lesson_points():
    """对称示例：AB=6，DC=3，高=4，交点 O=(0,2/3)。"""
    a, b = (-3.0, -2.0), (3.0, -2.0)
    c, d = (1.5, 2.0), (-1.5, 2.0)
    o = (0.0, -2.0 + 4.0 * 6.0 / 9.0)
    return {"A": a, "B": b, "C": c, "D": d, "O": o}


def cross(a, b, c) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def triangle_area(a, b, c) -> float:
    return abs(cross(a, b, c)) / 2
