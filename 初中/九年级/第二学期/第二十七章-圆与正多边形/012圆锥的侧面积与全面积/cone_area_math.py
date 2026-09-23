"""圆锥面积的独立数学模型；输入 r 为底面半径，h 为垂直高度。"""
from math import hypot, isclose, isfinite, pi


def cone_metrics(radius: float, height: float) -> dict[str, float]:
    if not all(isfinite(v) for v in (radius, height)) or radius <= 0 or height <= 0:
        raise ValueError("圆锥底面半径与高度都必须是正的有限实数")
    slant = hypot(radius, height)
    base_perimeter = 2 * pi * radius
    sector_angle = base_perimeter / slant
    lateral = pi * radius * slant
    base = pi * radius**2
    total = lateral + base
    if not 0 < sector_angle < 2*pi:
        raise ValueError("非退化圆锥展开扇形的圆心角应小于 360°")
    if not isclose(slant * sector_angle, base_perimeter, rel_tol=1e-12):
        raise ValueError("展开扇形弧长与底面周长不一致")
    if not isclose(slant**2 * sector_angle / 2, lateral, rel_tol=1e-12):
        raise ValueError("展开扇形面积与圆锥侧面积不一致")
    return {"radius": radius, "height": height, "slant": slant,
            "base_circumference": base_perimeter,
            "sector_radius": slant, "sector_angle": sector_angle,
            "sector_angle_deg": 360*radius/slant,
            "lateral": lateral, "base": base, "total": total}


def verify_cone(radius: float, height: float, *, expected_slant: float,
                expected_lateral: float, expected_total: float) -> None:
    data = cone_metrics(radius, height)
    for name, expected in (("slant", expected_slant),
                           ("lateral", expected_lateral), ("total", expected_total)):
        if not isclose(data[name], expected, rel_tol=1e-10, abs_tol=1e-10):
            raise ValueError(f"{name} 的教学结果与实际圆锥不一致")
