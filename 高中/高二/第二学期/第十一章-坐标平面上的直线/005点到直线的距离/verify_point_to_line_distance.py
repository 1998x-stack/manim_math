"""直接抽取课程源码的纯数学函数，不导入 Manim 的专项回归。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("point_to_line_distance.py")
tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
names = {"valid_line", "foot_of_perpendicular", "point_line_distance",
         "parallel_line_distance", "clipped_line"}
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
assert {node.name for node in functions} == names
scope = {"math": math}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
foot = scope["foot_of_perpendicular"]
distance = scope["point_line_distance"]
parallel = scope["parallel_line_distance"]
clip = scope["clipped_line"]

L1 = (3.0, 4.0, -12.0)
L2 = (3.0, 4.0, -2.0)
P = (1.0, 1.0)
R = (0.0, 0.5)


class PointLineDistanceTests(unittest.TestCase):
    def test_visible_foot_and_distance(self):
        q = foot(P, L1)
        self.assertAlmostEqual(q[0], 1.6)
        self.assertAlmostEqual(q[1], 1.8)
        self.assertAlmostEqual(distance(P, L1), 1.0)
        self.assertAlmostEqual(math.dist(P, q), 1.0)
        self.assertAlmostEqual(3*q[0] + 4*q[1] - 12, 0.0)
        self.assertAlmostEqual((q[0]-P[0])*4 + (q[1]-P[1])*(-3), 0.0)

    def test_line_points_and_zero_distance(self):
        for candidate in ((0, 3), (4, 0), (2, 1.5)):
            self.assertAlmostEqual(distance(candidate, L1), 0.0)
            self.assertAlmostEqual(math.dist(foot(candidate, L1), candidate), 0.0)

    def test_vertical_and_horizontal_cases(self):
        self.assertEqual(foot((4, 2), (1, 0, -3)), (3.0, 2.0))
        self.assertEqual(foot((4, 2), (0, 1, -1)), (4.0, 1.0))
        self.assertAlmostEqual(distance((4, 2), (1, 0, -3)), 1.0)
        self.assertAlmostEqual(distance((4, 2), (0, 1, -1)), 1.0)

    def test_parallel_example_has_genuine_normal_connector(self):
        self.assertAlmostEqual(3*R[0] + 4*R[1] - 2, 0)
        s = foot(R, L1)
        self.assertAlmostEqual(s[0], 1.2)
        self.assertAlmostEqual(s[1], 2.1)
        self.assertAlmostEqual(3*s[0] + 4*s[1] - 12, 0)
        self.assertAlmostEqual((s[0]-R[0])*4 + (s[1]-R[1])*(-3), 0)
        self.assertAlmostEqual(math.dist(R, s), 2)
        self.assertAlmostEqual(parallel(L1, L2), 2)

    def test_parallel_scaled_and_reversed_normal(self):
        self.assertAlmostEqual(parallel(L1, (6, 8, -4)), 2)
        self.assertAlmostEqual(parallel(L1, (-6, -8, 4)), 2)
        self.assertAlmostEqual(parallel(L1, (-3, -4, 12)), 0)
        self.assertAlmostEqual(parallel((1, 0, -1), (2, 0, -6)), 2)

    def test_invalid_general_form_and_nonparallel_lines(self):
        for invalid in ((0, 0, 1), (0, 0, 0), (math.inf, 2, 3)):
            with self.assertRaises(ValueError):
                distance(P, invalid)
            with self.assertRaises(ValueError):
                foot(P, invalid)
            with self.assertRaises(ValueError):
                clip(invalid)
        with self.assertRaises(ValueError):
            parallel(L1, (1, 0, -3))

    def test_clipped_endpoints_match_visible_lines(self):
        for line in (L1, L2, (1, 0, -3), (0, 1, -1)):
            a, b, c = line
            p, q = clip(line)
            self.assertGreater(math.dist(p, q), 1e-7)
            for x, y in (p, q):
                self.assertTrue(-2-1e-9 <= x <= 5+1e-9)
                self.assertTrue(-2-1e-9 <= y <= 5+1e-9)
                self.assertAlmostEqual(a*x + b*y + c, 0)

    def test_disjoint_line_and_invalid_window(self):
        with self.assertRaises(ValueError):
            clip((1, 0, -9))
        with self.assertRaises(ValueError):
            clip(L1, (2, 2), (-2, 5))


if __name__ == "__main__":
    unittest.main()
