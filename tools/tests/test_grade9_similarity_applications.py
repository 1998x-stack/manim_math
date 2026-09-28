"""九年级《相似三角形的应用》影子法与河宽法数学专项回归。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
          / "006相似三角形的应用/similar_triangles_app.py")


class SimilarityApplicationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"shadow_model", "river_model"}
        funcs = [n for n in cls.tree.body if isinstance(n, ast.FunctionDef)
                 and n.name in names]
        if {n.name for n in funcs} != names:
            raise AssertionError("缺少两类可测试应用模型")
        namespace = {"math": math}
        exec(compile(ast.Module(body=funcs, type_ignores=[]),
                     str(SOURCE), "exec"), namespace)
        cls.shadow = staticmethod(namespace["shadow_model"])
        cls.river = staticmethod(namespace["river_model"])

    @staticmethod
    def cross(u, v):
        return u[0]*v[1] - u[1]*v[0]

    def test_shadow_uses_parallel_rays_and_corresponding_ratios(self):
        coords, height = self.shadow()
        self.assertAlmostEqual(height, 5)
        self.assertAlmostEqual(coords["building_top"][1]
                               - coords["building_foot"][1], height)
        self.assertAlmostEqual(coords["person_head"][1]
                               - coords["person_foot"][1], 1)
        self.assertAlmostEqual(coords["building_shadow"][0]
                               - coords["building_foot"][0], 3)
        self.assertAlmostEqual(coords["person_shadow"][0]
                               - coords["person_foot"][0], 0.6)
        big = (coords["building_shadow"][0] - coords["building_top"][0],
               coords["building_shadow"][1] - coords["building_top"][1])
        small = (coords["person_shadow"][0] - coords["person_head"][0],
                 coords["person_shadow"][1] - coords["person_head"][1])
        self.assertAlmostEqual(self.cross(big, small), 0)
        self.assertAlmostEqual(height / 1, 3 / 0.6)
        self.assertTrue(all(-3.8 < x < 3.8 and -3.2 < y < 4
                            for x, y in coords.values()))

    def test_shadow_rejects_zero_negative_and_nonfinite_measurements(self):
        for args in ((1, 0, 3), (1, .6, 0), (-1, .6, 3),
                     (1, math.nan, 3), (math.inf, 1, 3)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.shadow(*args)
        coords, height = self.shadow(1.7, .85, 5.1)
        self.assertAlmostEqual(height, 10.2)
        self.assertAlmostEqual(coords["building_top"][1]
                               - coords["building_foot"][1], 10.2)

    def test_river_geometric_assumptions_match_bank_and_labelled_distance(self):
        p, distance = self.river()
        self.assertEqual(set(p), set("ABCDE"))
        self.assertAlmostEqual(distance, 3)
        self.assertAlmostEqual(p["A"][1] - p["B"][1], distance)
        self.assertAlmostEqual(p["B"][1], p["C"][1])
        self.assertAlmostEqual(p["C"][1], p["D"][1])
        self.assertAlmostEqual(math.dist(p["B"], p["C"]),
                               math.dist(p["C"], p["D"]))
        self.assertAlmostEqual(p["A"][0], p["B"][0])
        self.assertAlmostEqual(p["D"][0], p["E"][0])
        ac = (p["C"][0]-p["A"][0], p["C"][1]-p["A"][1])
        ce = (p["E"][0]-p["C"][0], p["E"][1]-p["C"][1])
        self.assertAlmostEqual(self.cross(ac, ce), 0)
        self.assertTrue(all(-3.9 < x < 3.9 and -3.8 < y < 3.9
                            for x, y in p.values()))
        # 两条水平岸线分别经过对岸 A 与本岸 B，非仅覆盖河内浮点。
        self.assertEqual(p["A"][1], 2.7)
        self.assertEqual(p["B"][1], -0.3)

    def test_river_model_rejects_invalid_dimensions(self):
        for args in ((0, 1.8), (3, 0), (-1, 1.8),
                     (math.nan, 1.8), (3, math.inf), (3, 2.1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.river(*args)
        points, result = self.river(2, 1)
        self.assertAlmostEqual(result, 2)
        self.assertAlmostEqual(math.dist(points["A"], points["B"]), 2)

    def test_scene_uses_models_and_never_builds_chinese_mathtex(self):
        scene = next(n for n in self.tree.body if isinstance(n, ast.ClassDef)
                     and n.name == "SimilarTrianglesApp")
        methods = {n.name: ast.get_source_segment(self.source, n)
                   for n in scene.body if isinstance(n, ast.FunctionDef)}
        self.assertIn("self.shadow, self.building_height = shadow_model()",
                      methods["construct"])
        self.assertIn("self.river, self.river_width = river_model()",
                      methods["construct"])
        self.assertIn('p["A"][1], p["B"][1]', methods["show_river_width"])
        self.assertIn('Text("且 A、C、E 三点共线"', methods["show_river_width"])
        self.assertIn('MathTex(r"\\triangle ABC\\sim\\triangle EDC"',
                      methods["show_river_width"])
        for n in ast.walk(scene):
            if (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in {"Tex", "MathTex"}):
                for arg in n.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any("\u4e00" <= ch <= "\u9fff"
                                             for ch in arg.value))


if __name__ == "__main__":
    unittest.main()
