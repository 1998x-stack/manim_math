"""不需要 Manim 的三点定圆数学及字幕入场专项回归。"""
import ast
import math
import unittest
from pathlib import Path

SOURCE = Path(__file__).with_name('circle_determination.py')
root = ast.parse(SOURCE.read_text(encoding='utf-8'))
fn = [node for node in root.body if isinstance(node, ast.FunctionDef)
      and node.name in {'circumcenter_xy', 'verify_circumcircle'}]
assert len(fn) == 2
namespace = {'hypot': math.hypot}
exec(compile(ast.Module(body=fn, type_ignores=[]), str(SOURCE), 'exec'), namespace)
center = namespace['circumcenter_xy']
verify = namespace['verify_circumcircle']


class ThreePointCircleTests(unittest.TestCase):
    def test_unique_circle_normal_and_right_triangles(self):
        triangles = [((-2.125, 1.5), (2.125, .65), (0, 3.625)),
                     ((0, 0), (4, 0), (0, 3)),
                     ((-4, 1), (1, 2), (2, 9))]
        for triangle in triangles:
            o, r = verify(*triangle)
            self.assertGreater(r, 0)
            for p in triangle:
                self.assertAlmostEqual(math.dist(o, p), r, places=7)
        self.assertEqual(center((0, 0), (4, 0), (0, 3)), (2., 1.5))

    def test_three_collinear_distinct_points_do_not_define_circle(self):
        for triple in [((0, 0), (1, 0), (2, 0)),
                       ((-2, 3), (0, 3), (1, 3)),
                       ((0, 0), (1, 1), (2, 2))]:
            with self.assertRaises(ValueError):
                verify(*triple)

    def test_duplicate_and_nearly_collinear_points(self):
        for triple in [((0, 0), (0, 0), (1, 0)),
                       ((0, 0), (1, 0), (1, 1e-12))]:
            with self.assertRaises(ValueError):
                verify(*triple)

    def test_construction_and_cards_are_reachable(self):
        scenes = [n for n in root.body if isinstance(n, ast.ClassDef)]
        self.assertIn('CircleDetermination', [n.name for n in scenes])
        scene = next(c for c in scenes if c.name == 'CircleDetermination')
        self.assertEqual(len([n for n in scene.body if isinstance(n, ast.FunctionDef)
                              and n.name.startswith('show_')]), 8)
        summary = next(n for n in scene.body if isinstance(n, ast.FunctionDef)
                       and n.name == 'show_summary')
        self.assertIn('FadeIn(card, shift=RIGHT * 0.5)', ast.unparse(summary))
        self.assertNotIn('shift(RIGHT * 0)', ast.unparse(summary))


if __name__ == '__main__':
    unittest.main()
