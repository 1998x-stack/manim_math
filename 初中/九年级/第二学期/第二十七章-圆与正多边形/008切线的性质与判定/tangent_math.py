"""切线性质与切线长定理的无 Manim 依赖数学模型。"""
from math import hypot, isfinite, sqrt


def tangent_points(center: tuple[float, float], radius: float,
                   external: tuple[float, float]) -> tuple[tuple[float, float], tuple[float, float]]:
    """外点到同一个圆的两个切点。外点必须严格在圆外。"""
    ox, oy = center
    px, py = external
    if not all(isfinite(v) for v in (ox, oy, px, py, radius)) or radius <= 0:
        raise ValueError("半径与所有坐标必须是合法有限实数，且半径为正")
    vx, vy = px - ox, py - oy
    squared = vx * vx + vy * vy
    if squared <= radius * radius:
        raise ValueError("切线长定理的引线点必须严格位于圆外")
    base_x = ox + radius * radius * vx / squared
    base_y = oy + radius * radius * vy / squared
    offset = radius * sqrt(squared - radius * radius) / squared
    return ((base_x - offset * vy, base_y + offset * vx),
            (base_x + offset * vy, base_y - offset * vx))


def verify_tangent_geometry(center: tuple[float, float], radius: float,
                            external: tuple[float, float]) -> float:
    """检验切点在圆上、切线与半径垂直，以及两条切线段等长。"""
    points = tangent_points(center, radius, external)
    ox, oy = center
    px, py = external
    expected = sqrt((px - ox) ** 2 + (py - oy) ** 2 - radius * radius)
    for tx, ty in points:
        if abs(hypot(tx - ox, ty - oy) - radius) > 1e-8 * max(1, radius):
            raise ValueError("切点未落在圆上")
        dot = (px - tx) * (tx - ox) + (py - ty) * (ty - oy)
        if abs(dot) > 1e-8 * max(1, expected * radius):
            raise ValueError("切线与切点处半径不垂直")
        if abs(hypot(px - tx, py - ty) - expected) > 1e-8 * max(1, expected):
            raise ValueError("两条切线长与勾股定理的结果不一致")
    return expected
