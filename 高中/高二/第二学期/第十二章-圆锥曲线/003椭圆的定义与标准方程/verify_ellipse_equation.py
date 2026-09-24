"""椭圆八镜数学回归；AST 抽取原脚本实际函数，不加载 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("ellipse_equation.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"ellipse_focal_length", "ellipse_point", "ellipse_foci",
         "focal_distance_sum", "ellipse_residual", "axis_units"}
functions = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in NAMES]
assert {n.name for n in functions} == NAMES
scope = {"math": math, "A": 3.0, "B": 2.0}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
c = scope["ellipse_focal_length"]
point = scope["ellipse_point"]
foci = scope["ellipse_foci"]
sumdist = scope["focal_distance_sum"]
residual = scope["ellipse_residual"]
units = scope["axis_units"]


class EllipseGeometryTests(unittest.TestCase):
    def test_a_b_c_relation(self):
        self.assertAlmostEqual(c(), math.sqrt(5))
        self.assertAlmostEqual(3**2, 2**2 + c()**2)
        self.assertLess(c(), 3)

    def test_horizontal_foci_and_vertices(self):
        self.assertEqual(foci(), ((-math.sqrt(5), 0), (math.sqrt(5), 0)))
        expected = {(3, 0), (0, 2), (-3, 0), (0, -2)}
        self.assertEqual({tuple(round(value) for value in point(k*math.pi/2))
                          for k in range(4)}, expected)

    def test_vertical_foci_and_vertices(self):
        self.assertEqual(foci(vertical=True), ((0, -math.sqrt(5)), (0, math.sqrt(5))))
        expected = {(2, 0), (0, 3), (-2, 0), (0, -3)}
        self.assertEqual({tuple(round(value) for value in point(k*math.pi/2, vertical=True))
                          for k in range(4)}, expected)

    def test_horizontal_definition_and_standard_equation(self):
        for i in range(144):
            p = point(2*math.pi*i/144)
            self.assertAlmostEqual(residual(p), 0, places=10)
            self.assertAlmostEqual(sumdist(p), 6, places=10)

    def test_vertical_definition_and_standard_equation(self):
        for i in range(144):
            p = point(2*math.pi*i/144, vertical=True)
            self.assertAlmostEqual(residual(p, vertical=True), 0, places=10)
            self.assertAlmostEqual(sumdist(p, vertical=True), 6, places=10)

    def test_nonellipse_points_differ(self):
        self.assertGreater(abs(residual((0, 0))), 0)
        self.assertLess(sumdist((0, 0)), 6)
        self.assertGreater(abs(residual((4, 0))), 0)
        self.assertGreater(sumdist((4, 0)), 6)

    def test_invalid_and_degenerate_parameters(self):
        for a, b in ((3, 3), (2, 3), (1, 0), (math.inf, 2)):
            with self.assertRaises(ValueError):
                c(a,b)
        with self.assertRaises(ValueError):
            point(math.nan)
        with self.assertRaises(ValueError):
            sumdist((math.inf, 0))

    def test_true_screen_lengths_and_scene_contract(self):
        self.assertEqual(units(), (0.7, 0.7))
        self.assertNotAlmostEqual(*units(x_length=7*0.65, y_length=5*0.65))
        with self.assertRaises(ValueError):
            units(x_bounds=(4, 4))
        classes = [n for n in TREE.body if isinstance(n, ast.ClassDef) and n.name == "EllipseEquation"]
        self.assertEqual(len(classes), 1)
        method_names = {n.name for n in classes[0].body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"show_definition", "show_dynamic_drawing", "show_standard_equation_x",
                         "show_standard_equation_y", "show_abc_relation", "show_vertices"} <= method_names)


if __name__ == "__main__":
    unittest.main()
