"""两点待定系数法：纯数学与 Scene 入口回归，无需安装 manim。"""
import ast
from fractions import Fraction
from math import isfinite
from pathlib import Path

scene_file = Path(__file__).with_name("linear_function_undetermined_coefficients.py")
source = scene_file.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(scene_file))
namespace = {"Fraction": Fraction, "isfinite": isfinite}
for name in ("solve_from_points", "visible_interval"):
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(scene_file), "exec"), namespace)
solve = namespace["solve_from_points"]
interval = namespace["visible_interval"]


def run():
    assert any(isinstance(n, ast.ClassDef) and n.name == "LinearFunctionUndeterminedCoefficients"
               for n in tree.body)
    for index in range(1, 8):
        assert f"def scene_{index}_" in source, index
    assert solve((1, 3), (3, 7)) == (Fraction(2), Fraction(1))
    assert solve((3, 7), (1, 3)) == (Fraction(2), Fraction(1))
    assert solve((-3, 0), (3, 6)) == (Fraction(1), Fraction(3))
    assert solve((0, 2), (2, -4)) == (Fraction(-3), Fraction(2))
    assert solve((0, Fraction(1, 3)), (3, Fraction(4, 3))) == (Fraction(1, 3), Fraction(1, 3))
    for a, b in (((1, 3), (1, 7)), ((1, 3), (2, 3)), ((1,), (2, 3)),
                 ((1, 3), (2, float("nan")))):
        try:
            solve(a, b)
        except ValueError:
            pass
        else:
            raise AssertionError(f"应拒绝非法或非一次函数数据: {a,b}")
    for k, b in ((2, 1), (-1, 1), (Fraction(1, 2), 2), (3, -2)):
        left, right = interval(k, b)
        assert -1 < left < right < 5, (k, b, left, right)
        for x in (left, (left + right) / 2, right):
            assert -1 < float(k) * x + float(b) < 9, (k, b, x)
    for bad in ((0, 1), (float("nan"), 1), (2, float("inf")), (2, 100)):
        try:
            interval(*bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"不应绘出非法线段: {bad}")
    print("PASS: seven scenes, exact unique coefficients, 4 visible segments, invalid/degenerate inputs")


if __name__ == "__main__":
    run()
