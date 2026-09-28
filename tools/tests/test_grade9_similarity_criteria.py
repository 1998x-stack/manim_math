"""九年级上《相似三角形的判定》：从真实源码抽取纯数学函数运行测试。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
LESSON = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
          / "004相似三角形的判定")
SOURCE = LESSON / "similar_triangles.py"
DUPLICATE = LESSON / "similar_triangles1.py"


class SimilarityCriteriaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"lengths", "interior_angle", "triangle_aa", "triangle_sas",
                 "triangle_sss", "similar_pair"}
        functions = [node for node in cls.tree.body
                     if isinstance(node, ast.FunctionDef) and node.name in names]
        if {node.name for node in functions} != names:
            raise AssertionError("AA/SAS/SSS 数学模型不完整")
        namespace = {"math": math}
        exec(compile(ast.Module(body=functions, type_ignores=[]),
                     str(SOURCE), "exec"), namespace)
        for name in names:
            setattr(cls, name, staticmethod(namespace[name]))

    def test_aa_uses_the_correct_two_vertex_angles(self):
        triangle = self.triangle_aa(60, 50, 4)
        a, b, c = triangle
        self.assertAlmostEqual(math.dist(a, b), 4)
        self.assertAlmostEqual(math.degrees(self.interior_angle(b, a, c)), 60)
        self.assertAlmostEqual(math.degrees(self.interior_angle(c, b, a)), 50)
        self.assertAlmostEqual(math.degrees(self.interior_angle(a, c, b)), 70)
        small, large = self.similar_pair(triangle, 0.6)
        for s, l in zip(self.lengths(small), self.lengths(large)):
            self.assertAlmostEqual(l / s, 0.6)

    def test_sas_included_angle_and_displayed_lengths(self):
        base = self.triangle_sas(3.5, 2.8, 70)
        a, b, c = base
        self.assertAlmostEqual(math.dist(a, b), 3.5)
        self.assertAlmostEqual(math.dist(a, c), 2.8)
        self.assertAlmostEqual(math.degrees(self.interior_angle(b, a, c)), 70)
        first, second = self.similar_pair(base, 0.65)
        self.assertAlmostEqual(math.dist(second[0], second[1]) /
                               math.dist(first[0], first[1]), 0.65)
        self.assertAlmostEqual(3.5 * 0.65, 2.275)
        self.assertAlmostEqual(2.8 * 0.65, 1.82)
        self.assertAlmostEqual(3.5 / 2.275, 20 / 13)
        self.assertAlmostEqual(2.8 / 1.82, 20 / 13)

    def test_sss_constructor_uses_correct_corresponding_edge_order(self):
        base = self.triangle_sss(5, 4, 3.5)
        self.assertEqual(len(base), 3)
        for actual, given in zip(self.lengths(base), (5, 4, 3.5)):
            self.assertAlmostEqual(actual, given)
        small, large = self.similar_pair(base, 0.7)
        for before, after in zip(self.lengths(small), self.lengths(large)):
            self.assertAlmostEqual(before / after, 10 / 7)
        self.assertAlmostEqual(5 * .7, 3.5)
        self.assertAlmostEqual(4 * .7, 2.8)
        self.assertAlmostEqual(3.5 * .7, 2.45)

    def test_degenerate_or_invalid_geometry_is_rejected(self):
        for args in ((60, 120, 4), (0, 40, 4), (60, 50, 0),
                     (90, math.inf, 2)):
            with self.subTest(aa=args), self.assertRaises(ValueError):
                self.triangle_aa(*args)
        for args in ((1, 0, 40), (1, 2, 180), (1, 2, -1)):
            with self.subTest(sas=args), self.assertRaises(ValueError):
                self.triangle_sas(*args)
        for args in ((1, 2, 3), (0, 2, 3), (1, 1, 3),
                     (3, math.nan, 4)):
            with self.subTest(sss=args), self.assertRaises(ValueError):
                self.triangle_sss(*args)
        with self.assertRaises(ValueError):
            self.similar_pair(((0, 0), (1, 1), (2, 2)), 0.7)
        with self.assertRaises(ValueError):
            self.similar_pair(self.triangle_sss(5, 4, 3.5), 0)

    def test_scene_geometry_and_formula_are_consistent(self):
        cls = next(node for node in self.tree.body
                   if isinstance(node, ast.ClassDef) and node.name == "SimilarTriangles")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in cls.body if isinstance(node, ast.FunctionDef)}
        self.assertIn("self.aa = triangle_aa(60, 50, 4.0)", methods["construct"])
        self.assertIn("self.sas = triangle_sas(3.5, 2.8, 70)", methods["construct"])
        self.assertIn("self.sss = triangle_sss(5.0, 4.0, 3.5)", methods["construct"])
        self.assertIn("self.draw_pair(self.sas, 0.65)", methods["scene_4_sas_determination"])
        self.assertIn("self.draw_pair(self.sss, 0.7)", methods["scene_5_sss_determination"])
        self.assertIn("frac{3.5}{2.275}", methods["scene_4_sas_determination"])
        self.assertIn("frac{CA}{FD}", methods["scene_5_sss_determination"])
        self.assertNotIn("self.play(self.play(", self.source)
        self.assertEqual(self.source, DUPLICATE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
