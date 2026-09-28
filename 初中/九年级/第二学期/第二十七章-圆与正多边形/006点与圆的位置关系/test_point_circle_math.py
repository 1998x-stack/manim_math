"""与 Manim 无关的数学回归；从课程目录运行：python -m unittest -v test_point_circle_math"""
import ast
from pathlib import Path
import unittest

from point_circle_math import classify_distance, validate_points


class PointCircleMathTests(unittest.TestCase):
    def test_three_positions(self):
        self.assertEqual(classify_distance(0.0, 1.8), "inside")
        self.assertEqual(classify_distance(1.0, 1.8), "inside")
        self.assertEqual(classify_distance(1.8, 1.8), "on")
        self.assertEqual(classify_distance(2.8, 1.8), "outside")

    def test_strict_boundary(self):
        self.assertEqual(classify_distance(1.8 - 1e-8, 1.8), "inside")
        self.assertEqual(classify_distance(1.8 + 1e-8, 1.8), "outside")

    def test_reject_invalid_inputs(self):
        for distance, radius in ((-1, 2), (1, 0), (1, -2), (float('nan'), 2), (1, float('inf'))):
            with self.subTest(distance=distance, radius=radius), self.assertRaises(ValueError):
                classify_distance(distance, radius)

    def test_reject_wrong_demo_data(self):
        validate_points(1.8, {'inside': 1, 'on': 1.8, 'outside': 2.8})
        with self.assertRaises(ValueError):
            validate_points(1.8, {'inside': 1, 'on': 1.7, 'outside': 2.8})

    def test_scene_structure_without_manim(self):
        source = Path(__file__).with_name('point_circle_position.py').read_text(encoding='utf-8')
        tree = ast.parse(source)
        scenes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'PointCirclePosition']
        self.assertEqual(len(scenes), 1)
        methods = {n.name: n for n in scenes[0].body if isinstance(n, ast.FunctionDef)}
        for required in ('show_opening', 'show_distance_concept', 'show_point_inside', 'show_point_on_circle', 'show_point_outside', 'show_dynamic_demo', 'show_summary'):
            self.assertIn(required, methods)
        dynamic = ast.get_source_segment(source, methods['show_dynamic_demo'])
        self.assertNotIn('always_redraw(lambda: MathTex(', dynamic)
        self.assertNotIn('always_redraw(lambda: Text(', dynamic)
        # Match a literal zero displacement only; RIGHT * 0.8 is a valid nonzero offset.
        self.assertNotRegex(source, r'\bRIGHT\s*\*\s*0(?![\d.])')
        self.assertNotIn('LEFT * 10', source)


if __name__ == '__main__':
    unittest.main()
