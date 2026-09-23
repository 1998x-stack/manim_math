"""任意角三角比独立数学/源码回归；无需导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('any_angle_trigonometry.py')


class AnyAngleMathTest(unittest.TestCase):
    def test_unit_circle_points(self):
        for degrees in (30, 150, 210, 330):
            theta = math.radians(degrees)
            x, y = math.cos(theta), math.sin(theta)
            self.assertAlmostEqual(x*x + y*y, 1)

    def test_four_quadrant_signs(self):
        for degrees, sine, cosine, tangent in (
            (30, 1, 1, 1), (150, 1, -1, -1),
            (210, -1, -1, 1), (330, -1, 1, -1),
        ):
            x, y = math.cos(math.radians(degrees)), math.sin(math.radians(degrees))
            self.assertEqual(1 if y > 0 else -1, sine)
            self.assertEqual(1 if x > 0 else -1, cosine)
            self.assertEqual(1 if y/x > 0 else -1, tangent)

    def test_exact_sample_coordinate_magnitudes(self):
        for degrees in (30, 150, 210, 330):
            x, y = math.cos(math.radians(degrees)), math.sin(math.radians(degrees))
            self.assertAlmostEqual(abs(x), math.sqrt(3)/2)
            self.assertAlmostEqual(abs(y), 0.5)
            self.assertAlmostEqual(abs(y/x), 1/math.sqrt(3))

    def test_tangent_undefined_on_vertical_axis(self):
        for degrees in (90, 270):
            cosine = math.cos(math.radians(degrees))
            self.assertLess(abs(cosine), 1e-12)
        for degrees, expected in ((0, 0), (180, 0)):
            self.assertAlmostEqual(math.sin(math.radians(degrees)), expected, places=12)

    def test_angle_turns_preserve_unit_circle_coordinates(self):
        for degrees in (30, 150, 210, 330):
            original = math.radians(degrees)
            shifted = original + 2 * math.pi
            self.assertAlmostEqual(math.cos(original), math.cos(shifted))
            self.assertAlmostEqual(math.sin(original), math.sin(shifted))

    def test_actual_scene_uses_axes_unit_size(self):
        text = SOURCE.read_text(encoding='utf-8')
        ast.parse(text)
        self.assertIn('radius = np.linalg.norm(axes.c2p(1, 0) - origin)', text)
        self.assertNotIn('Circle(radius=2.0', text)
        self.assertNotIn('circle = Circle(\n            radius=self.RADIUS', text)
        self.assertIn(r'\tan\alpha=\frac{y}{x},\quad x\ne0', text)
        self.assertIn('tracker.animate.set_value(TAU)', text)
        self.assertIn('class AnyAngleTrigonometry(Scene)', text)


if __name__ == '__main__':
    unittest.main()
