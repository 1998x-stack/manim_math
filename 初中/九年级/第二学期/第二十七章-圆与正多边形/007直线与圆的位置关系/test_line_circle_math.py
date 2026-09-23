"""在课件目录运行：python -m unittest -v test_line_circle_math"""
import ast
from pathlib import Path
import unittest
from line_circle_math import horizontal_intersections, verify_case


class LineCircleMathTests(unittest.TestCase):
    def test_two_intersections(self):
        left, right = verify_case(2.0, 1.6, 2)
        self.assertAlmostEqual(left, -1.2)
        self.assertAlmostEqual(right, 1.2)

    def test_exact_tangent_and_disjoint(self):
        self.assertEqual(verify_case(2.0, 2.0, 1), (0.0,))
        self.assertEqual(verify_case(2.0, 3.0, 0), ())

    def test_near_tangent_no_sqrt_of_negative(self):
        self.assertEqual(len(horizontal_intersections(2.0, 2.0 - 1e-7)), 2)
        self.assertEqual(len(horizontal_intersections(2.0, 2.0 + 1e-7)), 0)
        self.assertEqual(len(horizontal_intersections(2.0, 2.0 + 1e-6)), 0)

    def test_zero_distance_and_invalid_inputs(self):
        self.assertEqual(horizontal_intersections(2.0, 0.0), (-2.0, 2.0))
        for r, d in ((0, 1), (-2, 1), (2, -1), (float('nan'), 1), (2, float('inf'))):
            with self.subTest(r=r, d=d), self.assertRaises(ValueError):
                horizontal_intersections(r, d)
        with self.assertRaises(ValueError):
            verify_case(2.0, 2.0, 2)

    def test_scene_structure(self):
        source = Path(__file__).with_name('line_circle_relations.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        scenes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'LineCircleRelations']
        self.assertEqual(len(scenes), 1)
        methods = {n.name for n in scenes[0].body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({'scene_1_opening', 'scene_2_basic_concepts', 'scene_3_intersecting', 'scene_4_tangent', 'scene_5_separate', 'scene_6_summary', 'scene_7_outro'} <= methods)
        self.assertNotIn('sqrt(self.r**2 - d**2)', source)


if __name__ == '__main__':
    unittest.main()
