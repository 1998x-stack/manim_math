"""点与圆的位置关系：不依赖 Manim 的数学模型。"""
from math import isfinite


def classify_distance(distance: float, radius: float) -> str:
    """严格数学判定：距离小于、等于或大于半径。"""
    if not (isfinite(distance) and isfinite(radius)):
        raise ValueError("距离与半径必须是有限实数")
    if radius <= 0 or distance < 0:
        raise ValueError("圆半径必须为正，点到圆心距离不能为负")
    if distance < radius:
        return "inside"
    if distance == radius:
        return "on"
    return "outside"


def validate_points(radius: float, points: dict[str, float]) -> None:
    """验证动画中用于三种位置关系的准确距离。"""
    expected = {"inside": "inside", "on": "on", "outside": "outside"}
    if points.keys() != expected.keys():
        raise ValueError("必须提供 inside/on/outside 三类点")
    for key, expected_state in expected.items():
        if classify_distance(points[key], radius) != expected_state:
            raise ValueError(f"{key} 的距离与预期位置不匹配")
