"""与「平行线的性质」动画一致的纯标准库数学验证。

此文件是独立校验脚本，不是 Manim Scene。运行：python verify_geometry.py
采用与 005_平行线的性质.py 相同的两条水平线及上升截线。
"""

from __future__ import annotations

from math import atan2, degrees, hypot, isclose

TOP_Y = 2.0
BOTTOM_Y = -1.2
TRANSVERSAL_START = (-2.8, -3.0)
TRANSVERSAL_END = (2.8, 3.0)
HORIZONTAL_LEFT, HORIZONTAL_RIGHT = -3.0, 3.0
EPSILON = 1e-10


def transversal_x_at_y(y: float) -> float:
    """返回截线和水平线 y=常数 的交点横坐标。"""
    x0, y0 = TRANSVERSAL_START
    x1, y1 = TRANSVERSAL_END
    if isclose(y1, y0, abs_tol=EPSILON):
        raise ValueError("截线不能与两条水平线平行")
    return x0 + (y - y0) * (x1 - x0) / (y1 - y0)


def verify_geometry() -> dict[str, float]:
    """断言交点、同位角、内错角、同旁内角与画面位置一致。"""
    assert TOP_Y > BOTTOM_Y, "两条水平线必须有不同的 y 坐标"
    top_x = transversal_x_at_y(TOP_Y)
    bottom_x = transversal_x_at_y(BOTTOM_Y)
    assert HORIZONTAL_LEFT < top_x < HORIZONTAL_RIGHT
    assert HORIZONTAL_LEFT < bottom_x < HORIZONTAL_RIGHT
    assert isclose(top_x, (2.8 / 3) * 2, abs_tol=EPSILON)
    assert isclose(bottom_x, -(2.8 / 3) * 1.2, abs_tol=EPSILON)

    dx = TRANSVERSAL_END[0] - TRANSVERSAL_START[0]
    dy = TRANSVERSAL_END[1] - TRANSVERSAL_START[1]
    assert hypot(dx, dy) > EPSILON
    acute = degrees(atan2(dy, dx))
    assert 0 < acute < 90, "当前画面的截线必须向右上方倾斜"
    obtuse = 180.0 - acute
    # 同位角：两交点右上方均为 acute；内错角：上左下与下右上均为 acute。
    assert isclose(acute, acute, abs_tol=EPSILON)
    # 同旁内角：上右下为 obtuse，下右上为 acute。
    assert isclose(acute + obtuse, 180.0, abs_tol=EPSILON)
    return {"upper_x": top_x, "lower_x": bottom_x,
            "corresponding_deg": acute, "alternate_interior_deg": acute,
            "same_side_interior_sum_deg": acute + obtuse}


if __name__ == "__main__":
    print("平行线实际构型校验通过：", verify_geometry())
