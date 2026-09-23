"""在本课目录执行：python -m unittest -v test_two_circles_math"""
import ast
from math import hypot
from pathlib import Path
import unittest
from two_circles_math import circle_relation, circle_intersections


class CircleCircleTests(unittest.TestCase):
    def test_five_relations_and_intersection_counts(self):
        R, r = 1.5, 1.0
        for distance, state, count in ((3.0, 'external_separation', 0),
                                       (2.5, 'external_tangency', 1),
                                       (1.8, 'intersection', 2),
                                       (0.5, 'internal_tangency', 1),
                                       (0.2, 'containment', 0)):
            with self.subTest(distance=distance):
                self.assertEqual(circle_relation(R, r, distance), state)
                points = circle_intersections((-1.0, 1.0), R, (-1.0 + distance, 1.0), r)
                self.assertEqual(len(points), count)
                for x, y in points:
                    self.assertAlmostEqual(hypot(x + 1.0, y - 1.0), R)
                    self.assertAlmostEqual(hypot(x + 1.0 - distance, y - 1.0), r)

    def test_equal_radii_and_coincident_circles(self):
        self.assertEqual(circle_relation(1.0, 1.0, 0.0), 'coincident')
        with self.assertRaises(ValueError):
            circle_intersections((0, 0), 1.0, (0, 0), 1.0)
        self.assertEqual(circle_relation(2.0, 1.0, 0.0), 'containment')
        self.assertEqual(circle_relation(1.0, 1.0, 1.0), 'intersection')

    def test_scaled_diagram_machine_roundoff(self):
        # 预览使用 0.4 缩放：0.6 - 0.4 与 0.2 相差数个 ULP，不应漏掉切点。
        scale = 0.4
        R, r = 1.5 * scale, 1.0 * scale
        self.assertEqual(len(circle_intersections((-1.65, 0), R, (-1.65 + 0.5 * scale, 0), r)), 1)
        self.assertEqual(len(circle_intersections((-1.65, 0), R, (-1.65 + 2.5 * scale, 0), r)), 1)
        self.assertEqual(circle_relation(1.5, 1.0, 2.5 + 1e-8), 'external_separation')
        self.assertEqual(circle_relation(1.5, 1.0, 2.5 - 1e-8), 'intersection')

    def test_invalid_geometry(self):
        for R, r, d in ((0, 1, 1), (-1, 1, 1), (1, 0, 1), (1, 1, -1), (float('nan'), 1, 1)):
            with self.subTest(R=R, r=r, d=d), self.assertRaises(ValueError):
                circle_relation(R, r, d)
        with self.assertRaises(ValueError):
            circle_intersections((0, 0), 1, (float('inf'), 0), 1)

    def test_scene_entrypoint(self):
        content = Path(__file__).with_name('two_circles_relations.py').read_text(encoding='utf-8')
        scene = [node for node in ast.parse(content).body
                 if isinstance(node, ast.ClassDef) and node.name == 'TwoCirclesRelations']
        self.assertEqual(len(scene), 1)
        methods = {node.name for node in scene[0].body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({'scene_1_opening','scene_2_basic_concepts','scene_3_external_separation',
                         'scene_4_external_tangency','scene_5_intersection','scene_6_internal_tangency',
                         'scene_7_containment','scene_8_summary','scene_9_outro'} <= methods)


if __name__ == '__main__':
    unittest.main()
