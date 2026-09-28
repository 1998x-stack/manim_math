"""一次函数的性质：独立数学与画面契约测试，无需 manim。"""
import ast
from math import isfinite
from pathlib import Path

src_path = Path(__file__).with_name("linear_function_properties.py")
src = src_path.read_text(encoding="utf-8")
module = ast.parse(src, filename=str(src_path))
functions = {node.name: node for node in module.body if isinstance(node, ast.FunctionDef)}
namespace = {"isfinite": isfinite}
for name in ("visible_interval", "quadrant", "quadrants_for"):
    exec(compile(ast.Module(body=[functions[name]], type_ignores=[]), str(src_path), "exec"), namespace)
visible_interval = namespace["visible_interval"]
quadrant = namespace["quadrant"]
quadrants_for = namespace["quadrants_for"]


def run():
    assert any(isinstance(node, ast.ClassDef) and node.name == "LinearFunctionProperties"
               for node in module.body)
    for method in ("show_opening", "setup_coordinate_system", "show_k_positive_property",
                   "show_k_negative_property", "show_quadrant_relationships",
                   "show_comparison_summary", "show_outro"):
        assert f"def {method}(" in src
    expected = {(1, 1): (1, 2, 3), (1, -1): (1, 3, 4),
                (-1, 1): (1, 2, 4), (-1, -1): (2, 3, 4),
                (1, 0): (1, 3), (-1, 0): (2, 4)}
    assert quadrant(1, 1) == 1
    assert quadrant(-1, 1) == 2
    assert quadrant(-1, -1) == 3
    assert quadrant(1, -1) == 4
    assert quadrant(0, 0) == quadrant(0, 1) == quadrant(1, 0) == 0
    for (k, b), quadrants in expected.items():
        assert quadrants_for(k, b) == quadrants, (k, b)
        left, right = visible_interval(k, b)
        assert -3 < left < right < 3
        for x in (left, (left + right) / 2, right):
            assert -3 < k * x + b < 3, (k, b, x)
        observed = {quadrant(x / 20, k * x / 20 + b)
                    for x in range(-2000, 2001) if x != 0}
        observed.discard(0)
        assert observed == set(quadrants), (k, b, observed, quadrants)
    for k in (0.5, 1, 3):
        assert all(k * (x + 1) + 1 > k * x + 1 for x in (-4, -1, 0, 2))
    for k in (-0.5, -1, -3):
        assert all(k * (x + 1) + 1 < k * x + 1 for x in (-4, -1, 0, 2))
    for bad in ((0, 1), (float("nan"), 1), (1, float("inf"))):
        for func in (visible_interval, quadrants_for):
            try:
                func(*bad)
            except ValueError:
                pass
            else:
                raise AssertionError((func.__name__, bad))
    try:
        visible_interval(1, 100)
    except ValueError:
        pass
    else:
        raise AssertionError("不可见直线应被拒绝")
    print("PASS: seven scenes; six quadrant cases, samples, endpoints, monotonicity, invalid parameters")


if __name__ == "__main__":
    run()
