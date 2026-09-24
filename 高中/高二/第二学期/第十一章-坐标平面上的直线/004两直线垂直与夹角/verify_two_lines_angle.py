"""独立数学回归，不导入 Manim，直接抽取本课源码实际函数。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("two_lines_angle.py")
tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
names = {"direction_from_general", "acute_line_angle", "slopes_perpendicular",
         "tangent_acute_angle", "clipped_slope"}
functions = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
assert {n.name for n in functions} == names
scope = {"math": math}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
direction = scope["direction_from_general"]
angle = scope["acute_line_angle"]
perp = scope["slopes_perpendicular"]
tangent = scope["tangent_acute_angle"]
clip = scope["clipped_slope"]


class AngleGeometryTests(unittest.TestCase):
    def test_visible_example_45_degrees(self):
        self.assertAlmostEqual(angle((1, 2), (1, 1 / 3)), math.pi / 4)
        self.assertAlmostEqual(tangent(2, 1 / 3), 1)

    def test_visible_example_perpendicular(self):
        self.assertTrue(perp(2, -0.5))
        self.assertAlmostEqual(angle((1, 2), (1, -0.5)), math.pi / 2)
        with self.assertRaises(ValueError):
            tangent(2, -0.5)

    def test_negative_denominator_is_absolute(self):
        self.assertAlmostEqual(tangent(2, -1), 3)
        self.assertAlmostEqual(angle((1, 2), (1, -1)), math.atan(3))

    def test_vertical_horizontal_and_general_form(self):
        self.assertEqual(direction(1, 0), (0, -1))
        self.assertEqual(direction(0, 1), (1, 0))
        self.assertAlmostEqual(angle(direction(1, 0), direction(0, 1)), math.pi / 2)
        self.assertAlmostEqual(angle(direction(1, -2), direction(1, -2)), 0)

    def test_reversing_direction_does_not_change_line_angle(self):
        for first, second in (((1, 2), (1, 1 / 3)), ((0, 1), (2, 1)), ((1, 0), (0, 1))):
            expected = angle(first, second)
            self.assertAlmostEqual(angle(tuple(-x for x in first), second), expected)
            self.assertAlmostEqual(angle(first, tuple(-x for x in second)), expected)
            self.assertTrue(0 <= expected <= math.pi / 2)

    def test_zero_and_nonfinite_vectors_rejected(self):
        for left, right in (((0, 0), (1, 2)), ((1, 2), (0, 0)), ((math.inf, 2), (1, 2))):
            with self.assertRaises(ValueError):
                angle(left, right)
        with self.assertRaises(ValueError):
            direction(0, 0)
        with self.assertRaises(ValueError):
            tangent(math.inf, 2)

    def test_visible_segments_belong_to_lines_and_axes(self):
        for k in (2, -0.5, 1 / 3, 0, -2, 100):
            p, q = clip(k)
            self.assertGreater(math.dist(p, q), 1e-7)
            for x, y in (p, q):
                self.assertTrue(-3 - 1e-9 <= x <= 3 + 1e-9)
                self.assertTrue(-2.5 - 1e-9 <= y <= 2.5 + 1e-9)
                self.assertAlmostEqual(y, k * x)

    def test_invalid_window_and_vertical_as_slope(self):
        with self.assertRaises(ValueError):
            clip(math.inf)
        with self.assertRaises(ValueError):
            clip(1, (2, 2), (-2, 2))
        with self.assertRaises(ValueError):
            perp(math.inf, 0)


if __name__ == "__main__":
    unittest.main()
