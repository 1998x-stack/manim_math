"""正多边形几何模型：无 Manim 依赖，显示数据与数学断言共用。"""
from math import cos, hypot, isfinite, pi, sin


def polygon_metrics(n: int, circumradius: float) -> dict[str, float]:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError("正多边形边数必须是不小于 3 的整数")
    if not isfinite(circumradius) or circumradius <= 0:
        raise ValueError("外接圆半径必须是正的有限实数")
    angle = 2 * pi / n
    side = 2 * circumradius * sin(pi / n)
    apothem = circumradius * cos(pi / n)
    perimeter = n * side
    return {"central_angle": angle, "side": side, "apothem": apothem,
            "perimeter": perimeter, "area": perimeter * apothem / 2}


def polygon_vertices(n: int, circumradius: float,
                     center: tuple[float, float] = (0.0, 0.0),
                     phase: float = pi / 2) -> tuple[tuple[float, float], ...]:
    polygon_metrics(n, circumradius)
    if not all(isfinite(value) for value in (*center, phase)):
        raise ValueError("圆心与起始角必须为有限实数")
    ox, oy = center
    return tuple((ox + circumradius * cos(phase + 2 * pi * i / n),
                  oy + circumradius * sin(phase + 2 * pi * i / n)) for i in range(n))


def verify_polygon(n: int, circumradius: float) -> None:
    data = polygon_metrics(n, circumradius)
    verts = polygon_vertices(n, circumradius)
    sides = [hypot(verts[(i + 1) % n][0] - verts[i][0],
                   verts[(i + 1) % n][1] - verts[i][1]) for i in range(n)]
    for vertex, length in zip(verts, sides):
        if abs(hypot(*vertex) - circumradius) > 1e-9 * circumradius:
            raise ValueError("顶点不在外接圆上")
        if abs(length - data["side"]) > 1e-9 * circumradius:
            raise ValueError("显示边长与公式不一致")
    shoelace = abs(sum(verts[i][0] * verts[(i + 1) % n][1] -
                        verts[(i + 1) % n][0] * verts[i][1] for i in range(n))) / 2
    if abs(shoelace - data["area"]) > 1e-9 * max(1, data["area"]):
        raise ValueError("面积推导与顶点几何不一致")
