"""弧长与扇形面积的可独立测试数学模型。角度输入以度为单位。"""
from math import isclose, isfinite, pi


def sector_metrics(radius: float, degrees: float) -> dict[str, float]:
    if not all(isfinite(v) for v in (radius, degrees)) or radius <= 0:
        raise ValueError("圆半径须为正且角度、半径均须为有限实数")
    if not 0 <= degrees <= 360:
        raise ValueError("普通扇形的圆心角必须介于 0° 与 360° 之间")
    theta = pi * degrees / 180.0
    length = radius * theta
    area = radius * length / 2
    if not isclose(area, pi * radius**2 * degrees / 360, rel_tol=1e-12, abs_tol=1e-12):
        raise ValueError("扇形面积的两种公式不一致")
    return {"theta_rad": theta, "arc_length": length, "area": area,
            "perimeter": length + 2 * radius}


def verify_example(radius: float, degrees: float, *, expected_length: float,
                   expected_area: float) -> None:
    metrics = sector_metrics(radius, degrees)
    if not isclose(metrics['arc_length'], expected_length, rel_tol=1e-10, abs_tol=1e-10):
        raise ValueError("弧长示例数据与真实圆心角不匹配")
    if not isclose(metrics['area'], expected_area, rel_tol=1e-10, abs_tol=1e-10):
        raise ValueError("扇形面积示例数据与真实圆心角不匹配")
