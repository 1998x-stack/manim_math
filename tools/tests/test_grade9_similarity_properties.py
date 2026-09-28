"""九年级上《相似三角形的性质》：直接抽取课件数学函数做无 Manim 回归。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
               / "005相似三角形的性质/similar_triangles.py")


class SimilarityPropertiesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE_PATH.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"geometry_metrics", "transformed_pair"}
        nodes = [node for node in cls.tree.body
                 if isinstance(node, ast.FunctionDef) and node.name in names]
        if {node.name for node in nodes} != names:
            raise AssertionError("缺少可独立验证的相似性质数学函数")
        scope = {"math": math}
        exec(compile(ast.Module(body=nodes, type_ignores=[]),
                     str(SOURCE_PATH), "exec"), scope)
        cls.measure = staticmethod(scope["geometry_metrics"])
        cls.pair = staticmethod(scope["transformed_pair"])
        cls.base = ((0.1, 1.35), (-1.55, -0.95), (1.65, -0.95))

    def test_mathematical_scaling_of_every_corresponding_object(self):
        for k, rotation in ((0.4, 0), (0.6, 15), (1, -30), (2, 45)):
            with self.subTest(k=k, rotation=rotation):
                first, second, before, after = self.pair(
                    self.base, k, rotation)
                for name in ("ab", "bc", "ca", "altitude", "median",
                             "bisector", "perimeter"):
                    self.assertAlmostEqual(after[name] / before[name], k,
                                           msg=name)
                self.assertAlmostEqual(after["area"] / before["area"], k*k)
                self.assertEqual(len(first), len(second))

    def test_foot_midpoint_bisector_and_area_refer_to_actual_coordinates(self):
        for triangle, metrics in ((self.base, self.measure(self.base)),
                                  (lambda result: (result[1], result[3]))(
                                      self.pair(self.base, 0.6))):
            a, b, c = triangle
            foot, middle, bisector = (metrics["foot"], metrics["midpoint"],
                                      metrics["bisector_foot"])
            bc = (c[0] - b[0], c[1] - b[1])
            self.assertAlmostEqual((a[0]-foot[0])*bc[0]
                                   + (a[1]-foot[1])*bc[1], 0)
            self.assertAlmostEqual(middle[0], (b[0]+c[0])/2)
            self.assertAlmostEqual(middle[1], (b[1]+c[1])/2)
            self.assertAlmostEqual(math.dist(b, bisector)/
                                   math.dist(bisector, c),
                                   math.dist(a, b)/math.dist(a, c))
            self.assertAlmostEqual(metrics["area"],
                                   metrics["bc"]*metrics["altitude"]/2)

    def test_display_data_and_safe_layout_for_default_pair(self):
        first, second, before, after = self.pair(self.base, .6)
        self.assertTrue(all(-3.8 < x < 3.8 and -2.8 < y < 4.0
                            for x, y in first + second))
        self.assertAlmostEqual(after["perimeter"] / before["perimeter"], .6)
        self.assertAlmostEqual(after["area"] / before["area"], .36)
        self.assertAlmostEqual(before["bisector_parameter"],
                               after["bisector_parameter"])
        self.assertAlmostEqual(before["foot_parameter"],
                               after["foot_parameter"])

    def test_invalid_inputs_fail_before_animation(self):
        for vertices in (((0, 0), (1, 1), (2, 2)),
                         ((0, 0), (0, 0), (1, 2)),
                         ((0, math.nan), (1, 0), (2, 1))):
            with self.subTest(vertices=vertices), self.assertRaises(ValueError):
                self.measure(vertices)
        for k in (0, -1, math.inf, math.nan):
            with self.subTest(k=k), self.assertRaises(ValueError):
                self.pair(self.base, k)

    def test_scene_source_uses_current_metrics_and_chinese_text_mobjects(self):
        cls = next(node for node in self.tree.body
                   if isinstance(node, ast.ClassDef)
                   and node.name == "SimilarTrianglesProperties")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in cls.body if isinstance(node, ast.FunctionDef)}
        self.assertIn("self.first, self.second, self.before, self.after = transformed_pair(",
                      methods["construct"])
        self.assertIn('self.before["foot"]', methods["show_altitude_ratio"])
        self.assertIn('self.after["foot"]', methods["show_altitude_ratio"])
        self.assertIn('self.before["bisector_foot"]',
                      methods["show_median_bisector_ratio"])
        self.assertIn('self.after["bisector_foot"]',
                      methods["show_median_bisector_ratio"])
        self.assertIn('Text("对应边、高、中线、角平分线的长度之比 = k"',
                      methods["show_summary"])
        self.assertIn('MathTex(r"\\frac{S\'}{S}=k^2=0.6^2=0.36"',
                      methods["show_perimeter_area_ratio"])
        self.assertNotIn("from manim.utils.unit import *", self.source)
        for node in ast.walk(cls):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id in {"MathTex", "Tex"}):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in arg.value),
                                         msg="中文不可直接交给默认 MathTex/Tex")


if __name__ == "__main__":
    unittest.main()
