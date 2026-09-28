"""独立抽取课程实际数学函数，检验圆方程、交点和屏幕坐标比例。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("circle_equation.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"circle_from_general", "circle_residual", "valid_line",
         "center_line_distance", "line_circle_intersections", "axis_units"}
found = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in NAMES]
assert {n.name for n in found} == NAMES
scope = {"math": math, "CENTER": (2., 1.), "RADIUS": 1.5}
exec(compile(ast.Module(body=found, type_ignores=[]), str(SOURCE), "exec"), scope)
circle = scope["circle_from_general"]
residual = scope["circle_residual"]
distance = scope["center_line_distance"]
meet = scope["line_circle_intersections"]
units = scope["axis_units"]
CENTER = (2., 1.)
RADIUS = 1.5
SEPARATE = (0., 1., 1.)
TANGENT = (0., 1., -2.5)
INTERSECT = (0., 1., -1.)


class CircleEquationTests(unittest.TestCase):
    def test_general_and_standard_equations_agree(self):
        actual_center, actual_radius = circle(-4, -2, 2.75)
        self.assertEqual(actual_center, CENTER)
        self.assertAlmostEqual(actual_radius, RADIUS)
        for x, y in ((3.5, 1), (0.5, 1), (2, 2.5), (2, -0.5)):
            self.assertAlmostEqual(residual((x, y)), 0)
            self.assertAlmostEqual(x*x+y*y-4*x-2*y+2.75, 0)

    def test_general_equation_degenerate_cases(self):
        for coefficients in ((0, 0, 0), (0, 0, 1), (math.inf, 0, 0)):
            with self.assertRaises(ValueError):
                circle(*coefficients)
        with self.assertRaises(ValueError):
            residual((2, 1), radius=0)

    def test_three_visible_lines_have_zero_one_two_intersections(self):
        self.assertAlmostEqual(distance(CENTER, SEPARATE), 2)
        self.assertAlmostEqual(distance(CENTER, TANGENT), RADIUS)
        self.assertAlmostEqual(distance(CENTER, INTERSECT), 0)
        self.assertEqual(len(meet(CENTER, RADIUS, SEPARATE)), 0)
        self.assertEqual(len(meet(CENTER, RADIUS, TANGENT)), 1)
        self.assertEqual(len(meet(CENTER, RADIUS, INTERSECT)), 2)

    def test_tangent_point_and_intersection_point_coordinates(self):
        self.assertEqual(meet(CENTER, RADIUS, TANGENT), ((2.0, 2.5),))
        points = meet(CENTER, RADIUS, INTERSECT)
        self.assertEqual(set(points), {(0.5, 1.), (3.5, 1.)})
        for x, y in points:
            self.assertAlmostEqual(residual((x,y)), 0)
            self.assertAlmostEqual(y, 1)

    def test_general_oblique_and_vertical_lines(self):
        for line in ((1, 0, -2), (1, 1, -3), (3, 4, -10), (-6, -8, 20)):
            points = meet(CENTER, RADIUS, line)
            self.assertIn(len(points), (0, 1, 2))
            a,b,c = line
            for p in points:
                self.assertAlmostEqual(residual(p), 0, places=8)
                self.assertAlmostEqual(a*p[0]+b*p[1]+c, 0, places=8)

    def test_invalid_lines_and_geometry(self):
        for line in ((0, 0, 1), (math.nan, 1, 0), (math.inf, 1, 0)):
            with self.assertRaises(ValueError):
                distance(CENTER, line)
            with self.assertRaises(ValueError):
                meet(CENTER, RADIUS, line)
        with self.assertRaises(ValueError):
            meet(CENTER, 0, INTERSECT)
        with self.assertRaises(ValueError):
            meet(CENTER, RADIUS, INTERSECT, tolerance=-1)

    def test_axes_equal_unit_scale(self):
        ux, uy = units()
        self.assertAlmostEqual(ux, 0.8)
        self.assertAlmostEqual(uy, 0.8)
        with self.assertRaises(ValueError):
            units(x_range=(2, 2))

    def test_literal_mathtex_has_no_chinese(self):
        for node in ast.walk(TREE):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            if node.func.id not in ("MathTex", "Tex"):
                continue
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    self.assertFalse(any("\u3400" <= c <= "\u9fff" for c in arg.value),
                                     f"CJK in MathTex, line {node.lineno}")


if __name__ == "__main__":
    unittest.main()
