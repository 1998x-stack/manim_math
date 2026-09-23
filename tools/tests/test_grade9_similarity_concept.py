"""九年级《相似三角形的概念》纯数学与源码回归；无需安装 Manim。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
               / "003相似三角形的概念/similar_triangles_concept.py")


class SimilarTrianglesConceptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE_PATH.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        wanted = {"interior_angle", "similarity_model"}
        nodes = [node for node in cls.tree.body
                 if isinstance(node, ast.FunctionDef) and node.name in wanted]
        if {node.name for node in nodes} != wanted:
            raise AssertionError("课件缺少可独立回归的几何算法")
        namespace = {"math": math}
        exec(compile(ast.Module(body=nodes, type_ignores=[]),
                     str(SOURCE_PATH), "exec"), namespace)
        cls.angle = staticmethod(namespace["interior_angle"])
        cls.model = staticmethod(namespace["similarity_model"])
        cls.base = ((-1.5, 0.5), (0.5, -1.0), (1.0, 1.2))

    def test_corresponding_edges_and_angles_are_exact(self):
        small, large, short, long, angles = self.model(
            self.base, 2.0, (-2.1, 2.1), (1.35, 0.1))
        self.assertEqual(len(short), 3)
        self.assertAlmostEqual(sum(angles), math.pi)
        for s, l in zip(short, long):
            self.assertAlmostEqual(l / s, 2.0)
        for i in range(3):
            j, k = (i + 1) % 3, (i + 2) % 3
            a, start, turn = self.angle(small[j], small[i], small[k])
            other, _, other_turn = self.angle(large[j], large[i], large[k])
            self.assertAlmostEqual(a, angles[i])
            self.assertAlmostEqual(other, angles[i])
            self.assertAlmostEqual(turn, other_turn)
            self.assertAlmostEqual(abs(turn), a)

    def test_reverse_comparison_and_congruence(self):
        for scale in (0.5, 1.0, 2.0, 3.0):
            _, _, short, long, _ = self.model(
                self.base, scale, (-2, 1), (2, 1))
            for s, l in zip(short, long):
                self.assertAlmostEqual(l / s, scale)
                self.assertAlmostEqual(s / l, 1 / scale)
                if scale == 1:
                    self.assertAlmostEqual(s, l)

    def test_degenerate_or_nonfinite_input_rejected(self):
        for scale in (0.0, -1, math.inf, math.nan):
            with self.subTest(scale=scale), self.assertRaises(ValueError):
                self.model(self.base, scale, (0, 0), (1, 1))
        with self.assertRaises(ValueError):
            self.model(((0, 0), (1, 1), (2, 2)), 2, (0, 0), (1, 1))
        with self.assertRaises(ValueError):
            self.angle((0, 0), (0, 0), (1, 1))

    def test_diagram_is_inside_portrait_safe_region_and_disjoint(self):
        small, large, *_ = self.model(
            self.base, 2.0, (-2.1, 2.1), (1.35, 0.1))
        self.assertTrue(all(-3.8 < x < 3.8 and -3 < y < 4
                            for x, y in small + large))
        # 小三角形在左上，大三角形向右下错位，正文从 y=-3.45 开始。
        self.assertGreater(min(y for x, y in small), 0.7)
        self.assertLess(max(y for x, y in large), 2.2)

    def test_scene_math_and_mobject_lifecycle(self):
        cls = next(node for node in self.tree.body
                   if isinstance(node, ast.ClassDef) and node.name == "SimilarTrianglesConcept")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in cls.body if isinstance(node, ast.FunctionDef)}
        self.assertIn("self.first, self.second, self.short, self.long, self.angles = similarity_model(",
                      methods["construct"])
        self.assertIn("self.angle_arc(p, u, v, w", methods["show_corresponding_angles"])
        self.assertIn("self.angle_arc(p, x, y, z", methods["show_corresponding_angles"])
        self.assertIn("math.degrees(self.angles[index])", methods["show_corresponding_angles"])
        self.assertIn("self.draw_pair(first, second)", methods["show_congruence_special_case"])
        self.assertIn("FadeOut(mob) for mob in active", methods["clear_section"])
        for node in ast.walk(cls):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr == "play":
                self.assertFalse(any(isinstance(arg, ast.Call)
                                     and isinstance(arg.func, ast.Attribute)
                                     and arg.func.attr == "play" for arg in node.args))


if __name__ == "__main__":
    unittest.main()
