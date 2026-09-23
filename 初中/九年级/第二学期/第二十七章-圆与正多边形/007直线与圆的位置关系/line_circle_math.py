"""水平直线与圆的位置关系：标准库纯数学模型。"""
from math import isfinite, sqrt


def horizontal_intersections(radius: float, distance: float) -> tuple[float, ...]:
    """返回以圆心 x=0 为原点时全部交点的相对 x 坐标；0/1/2 个点。"""
    if not (isfinite(radius) and isfinite(distance)) or radius <= 0 or distance < 0:
        raise ValueError("半径须为正、垂距须非负，二者均须为有限实数")
    if distance > radius:
        return ()
    if distance == radius:
        return (0.0,)
    offset = sqrt((radius - distance) * (radius + distance))
    return (-offset, offset)


def verify_case(radius: float, distance: float, expected_count: int) -> tuple[float, ...]:
    """让课件显示的状态和实际交点个数保持一致。"""
    points = horizontal_intersections(radius, distance)
    if len(points) != expected_count:
        raise ValueError(f"显示 {expected_count} 个交点，实际有 {len(points)} 个")
    for x in points:
        if abs(x * x + distance * distance - radius * radius) > 1e-9 * max(1, radius * radius):
            raise ValueError("交点不在圆上")
    return points
