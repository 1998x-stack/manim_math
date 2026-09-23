"""两圆位置关系与交点的纯数学模型，不依赖 Manim/NumPy。"""
from math import hypot, isfinite, sqrt


def circle_relation(R: float, r: float, distance: float) -> str:
    if not all(isfinite(x) for x in (R, r, distance)) or min(R, r) <= 0 or distance < 0:
        raise ValueError("两半径必须为正，圆心距必须非负，所有数值须有限")
    total, difference = R + r, abs(R - r)
    if distance == 0 and R == r:
        return "coincident"
    if distance > total:
        return "external_separation"
    if distance == total:
        return "external_tangency"
    if distance > difference:
        return "intersection"
    if distance == difference:
        return "internal_tangency"
    return "containment"


def circle_intersections(c1: tuple[float, float], R: float,
                         c2: tuple[float, float], r: float) -> tuple[tuple[float, float], ...]:
    x1, y1 = c1
    x2, y2 = c2
    if not all(isfinite(v) for v in (*c1, *c2)):
        raise ValueError("圆心坐标必须有限")
    dx, dy = x2 - x1, y2 - y1
    d = hypot(dx, dy)
    relation = circle_relation(R, r, d)
    if relation in ("external_separation", "containment"):
        return ()
    if relation == "coincident":
        raise ValueError("重合圆有无穷多个公共点，不能绘制有限个交点")
    ux, uy = dx / d, dy / d
    if relation == "external_tangency":
        return ((x1 + R * ux, y1 + R * uy),)
    if relation == "internal_tangency":
        sign = 1 if R > r else -1
        return ((x1 + sign * R * ux, y1 + sign * R * uy),)
    a = (R * R - r * r + d * d) / (2 * d)
    h_squared = (R - a) * (R + a)
    # 对严格处于相交范围的输入，舍入误差可使理论非负的 h² 略小于零。
    if h_squared < -1e-10 * max(1, R * R):
        raise ValueError("两圆交点的几何约束不一致")
    h = sqrt(max(0.0, h_squared))
    foot_x, foot_y = x1 + a * ux, y1 + a * uy
    return ((foot_x - uy * h, foot_y + ux * h),
            (foot_x + uy * h, foot_y - ux * h))
