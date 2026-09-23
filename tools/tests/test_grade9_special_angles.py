"""九年级《特殊角的三角比值》数学与源码回归；不依赖 Manim。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = (ROOT / "初中/九年级/第一学期/第二十五章-锐角的三角比"
          / "002特殊角的三角比值/special_angle_trigonometry.py")


class SpecialAnglesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        functions = {"interior_angle", "special_angle_model"}
        body = [node for node in cls.tree.body
                if isinstance(node, ast.Assign) and any(
                    isinstance(target, ast.Name) and target.id in {"VALUES", "LATEX_VALUES"}
                    for target in node.targets)
                or isinstance(node, ast.FunctionDef) and node.name in functions]
        names = {node.name for node in body if isinstance(node, ast.FunctionDef)}
        if names != functions:
            raise AssertionError("课件缺少特殊角纯数学模型")
        namespace = {"math": math}
        exec(compile(ast.Module(body=body, type_ignores=[]), str(SOURCE), "exec"),
             namespace)
        cls.model = staticmethod(namespace["special_angle_model"])
        cls.angle = staticmethod(namespace["interior_angle"])
        cls.values = namespace["VALUES"]
        cls.latex = namespace["LATEX_VALUES"]

    def test_every_angle_is_true_and_sides_are_physically_correct(self):
        for degrees in (30, 45, 60):
            with self.subTest(degrees=degrees):
                result = self.model(degrees)
                p = result["points"]
                a, b = result["angle_arms"]
                self.assertAlmostEqual(self.angle(p[a], p[result["vertex"]], p[b]),
                                       degrees)
                a, b = result["right_arms"]
                self.assertAlmostEqual(self.angle(p[a], p[result["right"]], p[b]), 90)
                sides = result["sides"]
                for length, (u, v) in zip(sides, (result["opposite"],
                                                   result["adjacent"],
                                                   result["hypotenuse"])):
                    self.assertAlmostEqual(length, math.dist(p[u], p[v]))
                self.assertAlmostEqual(sides[0]**2+sides[1]**2, sides[2]**2)
                expected = (math.sin(math.radians(degrees)),
                            math.cos(math.radians(degrees)),
                            math.tan(math.radians(degrees)))
                for actual, analytic, table in zip(result["ratios"], expected,
                                                   self.values[degrees]):
                    self.assertAlmostEqual(actual, analytic)
                    self.assertAlmostEqual(actual, table)

    def test_30_and_60_have_inverted_opposite_and_adjacent_not_hypotenuse(self):
        thirty, sixty = self.model(30), self.model(60)
        self.assertEqual(set(thirty["opposite"]), set(sixty["adjacent"]))
        self.assertEqual(set(thirty["adjacent"]), set(sixty["opposite"]))
        self.assertEqual(set(thirty["hypotenuse"]), set(sixty["hypotenuse"]))
        self.assertEqual(thirty["vertex"], "C")
        self.assertEqual(sixty["vertex"], "A")
        self.assertAlmostEqual(thirty["ratios"][0], sixty["ratios"][1])
        self.assertAlmostEqual(thirty["ratios"][1], sixty["ratios"][0])

    def test_45_triangle_has_two_equal_legs_and_unit_tangent(self):
        result = self.model(45)
        self.assertEqual(result["right"], "P")
        self.assertEqual(result["vertex"], "Q")
        self.assertAlmostEqual(result["sides"][0], math.sqrt(2))
        self.assertAlmostEqual(result["sides"][1], math.sqrt(2))
        self.assertAlmostEqual(result["sides"][2], 2)
        self.assertAlmostEqual(result["ratios"][2], 1)

    def test_invalid_angles_and_degenerate_rays_fail(self):
        for degrees in (-30, 0, 15, 90, 180, math.nan):
            with self.subTest(degrees=degrees), self.assertRaises(ValueError):
                self.model(degrees)
        with self.assertRaises(ValueError):
            self.angle((0, 0), (0, 0), (1, 0))

    def test_table_and_screen_formula_are_derived_from_same_model(self):
        self.assertEqual(set(self.latex), {30, 45, 60})
        self.assertEqual(len(self.latex[30]), 3)
        cls = next(node for node in self.tree.body
                   if isinstance(node, ast.ClassDef)
                   and node.name == "SpecialAngleTrigonometry")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in cls.body if isinstance(node, ast.FunctionDef)}
        self.assertIn("self.models = {degrees: special_angle_model(degrees)",
                      methods["construct"])
        self.assertIn('set(opposite_name) != set(model["opposite"])',
                      methods["show_calculation"])
        self.assertIn('set(adjacent_name) != set(model["adjacent"])',
                      methods["show_calculation"])
        self.assertIn("*LATEX_VALUES[30]", methods["show_summary_table"])
        self.assertIn("*LATEX_VALUES[60]", methods["show_summary_table"])
        self.assertIn("MathTable(rows", methods["show_summary_table"])
        self.assertIn("self.clear_section(keep_author=False)", methods["show_outro"])
        for node in ast.walk(cls):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id in {"Tex", "MathTex"}):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any("\u4e00" <= c <= "\u9fff"
                                             for c in arg.value),
                                         msg="中文必须使用 Text")


if __name__ == "__main__":
    unittest.main()
