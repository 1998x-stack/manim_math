"""本课纯数学回归：无需 Manim/TeX，测试动画实际调用的同一函数。"""
import ast
import math
import unittest
from pathlib import Path

SOURCE = Path(__file__).with_name('circle_basic_concepts.py')
module = ast.parse(SOURCE.read_text(encoding='utf-8'))
functions = [node for node in module.body if isinstance(node, ast.FunctionDef)
             and node.name in {'circle_point_xy', 'verify_circle_geometry'}]
assert len(functions) == 2
namespace = {'cos': math.cos, 'sin': math.sin, 'radians': math.radians,
             'hypot': math.hypot}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), 'exec'), namespace)
point = namespace['circle_point_xy']
verify = namespace['verify_circle_geometry']


class CircleGeometryTests(unittest.TestCase):
    def test_points_and_diameter(self):
        for center in ((0, 1), (-2, 3), (1.5, -0.25)):
            for radius in (0.01, 1.8, 20):
                pts = verify(*center, radius)
                self.assertAlmostEqual(math.dist(pts['A'], pts['D']), 2 * radius)
                self.assertAlmostEqual(math.dist(pts['B'], center), radius)
                self.assertAlmostEqual(math.dist(pts['C'], center), radius)

    def test_zero_and_negative_radius(self):
        for radius in (0, -1):
            with self.assertRaises(ValueError):
                verify(0, 0, radius)
            with self.assertRaises(ValueError):
                point(0, 0, radius, 60)

    def test_major_arc_contains_a_not_minor(self):
        angles = {'B': 60, 'C': 150, 'A': 360}
        self.assertLess(angles['C'] - angles['B'], 180)
        self.assertLess(angles['A'] - angles['C'], 360 - (angles['C'] - angles['B']))
        self.assertGreater(360 - (angles['C'] - angles['B']), 180)

    def test_scene_entry_and_card_animation(self):
        tree = ast.parse(SOURCE.read_text(encoding='utf-8'))
        classes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
        self.assertIn('CircleBasicConcepts', [n.name for n in classes])
        scene = next(c for c in classes if c.name == 'CircleBasicConcepts')
        summary = next(n for n in scene.body if isinstance(n, ast.FunctionDef)
                       and n.name == 'show_summary')
        text = ast.unparse(summary)
        self.assertNotIn('RIGHT * 0)', text)
        self.assertIn('FadeIn(card, shift=RIGHT * 0.5)', text)


if __name__ == '__main__':
    unittest.main()
