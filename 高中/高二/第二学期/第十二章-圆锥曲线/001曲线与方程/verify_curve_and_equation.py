"""圆周/方程双向性和画面轴比例校验：无需导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("curve_and_equation.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"circle_point", "circle_residual", "circle_contains", "axis_unit_sizes"}
functions = [node for node in TREE.body if isinstance(node, ast.FunctionDef) and node.name in NAMES]
assert {node.name for node in functions} == NAMES
scope = {"math": math, "RADIUS": 2.0}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
point = scope["circle_point"]
residual = scope["circle_residual"]
contains = scope["circle_contains"]
units = scope["axis_unit_sizes"]


class CurveEquationTests(unittest.TestCase):
    def test_forward_all_sampled_circle_points_satisfy_equation(self):
        for index in range(144):
            p = point(index * 2 * math.pi / 144)
            self.assertAlmostEqual(residual(p), 0, places=9)
            self.assertTrue(contains(p))

    def test_backward_solution_reconstructs_point_on_circle(self):
        for x in (-2, -1, 0, 1, 2):
            y = math.sqrt(4 - x * x)
            self.assertTrue(contains((x, y)))
            self.assertTrue(contains((x, -y)))
            theta = math.atan2(y, x)
            reconstructed = point(theta)
            self.assertLess(math.dist(reconstructed, (x, y)), 1e-9)

    def test_visible_examples_and_counterexamples(self):
        self.assertTrue(contains((math.sqrt(2), math.sqrt(2))))
        self.assertTrue(contains((0, 2)))
        self.assertFalse(contains((3, 0)))
        self.assertAlmostEqual(residual((3, 0)), 5)
        self.assertTrue(contains((-2, 0)))
        self.assertLess((-2, 0)[0], 0)  # right semicircle is not the full circle

    def test_equal_axis_units_required_for_true_screen_circle(self):
        ux, uy = units()
        self.assertAlmostEqual(ux, 0.8)
        self.assertAlmostEqual(uy, 0.8)
        self.assertAlmostEqual(ux, uy)
        badx, bady = units(x_length=7, y_length=5)
        self.assertNotAlmostEqual(badx, bady)

    def test_invalid_geometry_rejected(self):
        for angle, radius in ((math.inf, 2), (0, 0), (0, -1)):
            with self.assertRaises(ValueError):
                point(angle, radius)
        with self.assertRaises(ValueError):
            residual((math.nan, 0))
        with self.assertRaises(ValueError):
            contains((0, 2), tolerance=-1)
        with self.assertRaises(ValueError):
            units(x_bounds=(1, 1))

    def test_tex_literals_do_not_contain_chinese(self):
        for node in ast.walk(TREE):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            if node.func.id not in ("MathTex", "Tex"):
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    self.assertFalse(any("\u3400" <= ch <= "\u9fff" for ch in arg.value),
                                     f"Use Text for Chinese instead of MathTex (line {node.lineno})")


if __name__ == "__main__":
    unittest.main()
