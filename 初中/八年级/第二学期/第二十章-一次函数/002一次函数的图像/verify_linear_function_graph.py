"""本课独立数学回归测试：无需安装 Manim，失败时非零退出。"""
import ast
import math
from pathlib import Path

SCENE_PATH = Path(__file__).with_name("linear_function_graph.py")
source = SCENE_PATH.read_text(encoding="utf-8")
module = ast.parse(source, filename=str(SCENE_PATH))
helper = next(node for node in module.body
              if isinstance(node, ast.FunctionDef) and node.name == "visible_interval")
namespace = {"isfinite": math.isfinite}
exec(compile(ast.Module(body=[helper], type_ignores=[]), str(SCENE_PATH), "exec"), namespace)
visible_interval = namespace["visible_interval"]


def verify_segment(k, b, x_bounds=(-4, 4), y_bounds=(-3, 5)):
    left, right = visible_interval(k, b, x_bounds, y_bounds)
    assert x_bounds[0] < left < right < x_bounds[1], (k, b, left, right)
    for x in (left, (left + right) / 2, right):
        y = k * x + b
        assert y_bounds[0] < y < y_bounds[1], (k, b, x, y)


def run():
    scenes = {node.name for node in module.body if isinstance(node, ast.ClassDef)}
    assert "LinearFunctionGraph" in scenes
    for index in range(1, 8):
        assert f"scene_{index}_" in source, index
    # 主函数、正斜率对比、负斜率对比，以及固定 k 后的上下平移。
    for k, b in ((2, 1), (0.5, 1), (-1, 1), (2, 2), (2, -1), (-1, 2)):
        verify_segment(k, b)
    assert 2 * (-0.5) + 1 == 0
    assert 2 * 0 + 1 == 1
    assert 2 * 0 + 2 == 2
    assert 2 * 0 - 1 == -1
    assert (2 * 1 + 1) - (2 * 0 + 1) == 2
    assert 0.5 * 1 + 1 > 0.5 * 0 + 1
    assert -1 * 1 + 1 < -1 * 0 + 1
    assert (2 * 1 + 2) - (2 * 1 + 1) == 1
    assert (2 * 1 + 1) - (2 * 1 - 1) == 2
    for bad in ((0, 1), (float("nan"), 1), (2, float("inf"),),):
        try:
            visible_interval(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"无效输入应报错: {bad}")
    for invalid_bounds in (((2, 2), (-3, 5)), ((-4, 4), (5, 5))):
        try:
            visible_interval(2, 1, *invalid_bounds)
        except ValueError:
            pass
        else:
            raise AssertionError(f"无效范围应报错: {invalid_bounds}")
    try:
        visible_interval(2, 1000)
    except ValueError:
        pass
    else:
        raise AssertionError("无可见线段应报错")
    print("PASS: seven-scene contract, 6 visible segments, intercepts, slopes and invalid inputs")


if __name__ == "__main__":
    run()
