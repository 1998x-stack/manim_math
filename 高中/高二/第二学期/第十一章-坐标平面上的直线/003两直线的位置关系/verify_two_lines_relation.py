"""不导入 Manim，使用源文件实际数学函数回归三种位置关系。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("two_lines_relation.py")
tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
names = {"validate_line", "determinant", "line_relation", "intersection", "clipped_line"}
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in functions} == names
scope = {"math": math}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
relation = scope["line_relation"]
meet = scope["intersection"]
clip = scope["clipped_line"]


class TwoLinesMathTests(unittest.TestCase):
    def test_three_visible_cases(self):
        self.assertEqual(relation((-1, 1, -2), (-1, 1, 1)), "parallel")
        self.assertEqual(relation((-1, 1, -1), (2, -2, 2)), "coincide")
        self.assertEqual(relation((-1, 1, -1), (1, 1, -3)), "intersect")

    def test_intersection_on_both_visible_lines(self):
        one = (-1, 1, -1)
        two = (1, 1, -3)
        x, y = meet(one, two)
        self.assertEqual((x, y), (1.0, 2.0))
        for a, b, c in (one, two):
            self.assertAlmostEqual(a * x + b * y + c, 0)

    def test_parallel_vertical_and_horizontal(self):
        self.assertEqual(relation((1, 0, -1), (2, 0, -4)), "parallel")
        self.assertEqual(relation((0, 1, -1), (0, 3, -6)), "parallel")
        self.assertEqual(relation((1, 0, -1), (0, 1, -1)), "intersect")
        self.assertEqual(meet((1, 0, -1), (0, 1, -1)), (1.0, 1.0))

    def test_coincident_scaled_and_reversed(self):
        self.assertEqual(relation((1, 0, -3), (-7, 0, 21)), "coincide")
        self.assertEqual(relation((0, 1, -2), (0, -3, 6)), "coincide")
        self.assertEqual(relation((2, 3, -6), (-4, -6, 12)), "coincide")

    def test_no_unique_intersection(self):
        with self.assertRaises(ValueError):
            meet((1, 0, -1), (2, 0, -4))
        with self.assertRaises(ValueError):
            meet((1, 0, -1), (-1, 0, 1))

    def test_invalid_general_forms_rejected(self):
        for line in ((0, 0, 0), (0, 0, 1), (math.inf, 1, 1), (math.nan, 1, 0)):
            with self.assertRaises(ValueError):
                relation(line, (1, 0, -3))
            with self.assertRaises(ValueError):
                clip(line)

    def test_clipped_geometry_in_plot_window(self):
        for line in ((-1, 1, -2), (-1, 1, 1), (-1, 1, -1), (2, -2, 2),
                     (1, 1, -3), (1, 0, -3), (0, 1, -2)):
            p, q = clip(line)
            self.assertGreater(math.dist(p, q), 1e-7)
            for x, y in (p, q):
                self.assertTrue(-3 - 1e-9 <= x <= 3 + 1e-9)
                self.assertTrue(-2 - 1e-9 <= y <= 4 + 1e-9)
                self.assertAlmostEqual(line[0] * x + line[1] * y + line[2], 0)

    def test_unrenderable_or_degenerate_window(self):
        with self.assertRaises(ValueError):
            clip((1, 0, -9))
        with self.assertRaises(ValueError):
            clip((1, 0, -2), (2, 2), (-2, 4))


if __name__ == "__main__":
    unittest.main()
