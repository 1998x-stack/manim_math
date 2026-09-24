"""不依赖 Manim 的直线方程数学回归；python verify_line_equations.py -v。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("line_equations.py")
code = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
functions = {"coefficients_through_points", "slope_intercept", "intercepts", "clip_line"}
math_functions = [node for node in code.body if isinstance(node, ast.FunctionDef) and node.name in functions]
assert {node.name for node in math_functions} == functions
scope = {"math": math}
exec(compile(ast.Module(body=math_functions, type_ignores=[]), str(SOURCE), "exec"), scope)
through = scope["coefficients_through_points"]
slope = scope["slope_intercept"]
intercepts = scope["intercepts"]
clip = scope["clip_line"]


class LineEquationsTests(unittest.TestCase):
    def test_examples_match_visible_equations(self):
        for coeff, points in (
            ((-2, 1, 0), [(0, 0), (1, 2)]),
            ((1, -1, 3), [(0, 3), (2, 5)]),
            ((2, 3, -6), [(3, 0), (0, 2)]),
        ):
            a, b, c = coeff
            for x, y in points:
                self.assertAlmostEqual(a * x + b * y + c, 0)

    def test_two_points_regular_vertical_and_horizontal(self):
        for p, q in (((-1, 1), (2, 4)), ((3, -2), (3, 5)), ((-2, 4), (4, 4))):
            a, b, c = through(p, q)
            for x, y in (p, q):
                self.assertAlmostEqual(a * x + b * y + c, 0)
            self.assertNotEqual((a, b), (0, 0))
            self.assertEqual(through(q, p), (-a, -b, -c))

    def test_coincident_points_rejected(self):
        with self.assertRaises(ValueError):
            through((1, 2), (1, 2))

    def test_slope_intercept_vertical_is_undefined(self):
        self.assertIsNone(slope((1, 0, -3)))
        self.assertEqual(slope((1, -1, 3)), (1, 3))
        self.assertEqual(slope((2, 3, -6)), (-2 / 3, 2))
        with self.assertRaises(ValueError):
            slope((0, 0, 7))

    def test_intercept_form_requires_nonzero_intercepts(self):
        self.assertEqual(intercepts((2, 3, -6)), (3, 2))
        for invalid in ((0, 2, -4), (1, 0, -4), (1, 2, 0), (0, 0, 3)):
            with self.assertRaises(ValueError):
                intercepts(invalid)

    def test_window_clipping_and_on_line(self):
        for equation in ((-2, 1, 0), (1, -1, 3), (2, 3, -6),
                         (1, 0, -3), (0, 1, 0), (1, 1e-12, 0)):
            a, b, c = equation
            p, q = clip(equation)
            self.assertGreater(math.dist(p, q), 1e-7)
            for x, y in (p, q):
                self.assertTrue(-4 - 1e-9 <= x <= 4 + 1e-9)
                self.assertTrue(-2 - 1e-9 <= y <= 5 + 1e-9)
                self.assertAlmostEqual(a * x + b * y + c, 0, places=7)

    def test_window_without_line_rejected(self):
        for equation in ((1, 0, -9), (0, 1, -8), (1, 1, -100), (0, 0, 1)):
            with self.assertRaises(ValueError):
                clip(equation)
        with self.assertRaises(ValueError):
            clip((1, 1, 0), (2, 2), (-2, 5))

    def test_parallel_and_equivalent_equations(self):
        p1, p2 = clip((2, 3, -6))
        q1, q2 = clip((1, 1.5, -3))
        for p, q in zip((p1, p2), (q1, q2)):
            self.assertLess(math.dist(p, q), 1e-8)


if __name__ == "__main__":
    unittest.main()
