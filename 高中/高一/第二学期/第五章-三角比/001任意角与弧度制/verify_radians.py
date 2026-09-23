"""《任意角与弧度制》独立数学回归；标准库即可运行。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('001_任意角与弧度制.py')


def endpoint(theta, radius=2.3):
    return radius * math.cos(theta), radius * math.sin(theta)


def sector_area(radius, theta):
    if radius <= 0 or abs(theta) > 2 * math.pi:
        raise ValueError('ordinary sector needs r>0 and |theta|<=2π')
    return 0.5 * radius * radius * abs(theta)


class RadianMathTest(unittest.TestCase):
    def test_angle_conversions_positive_and_negative(self):
        for degrees in (-315, -45, 0, 45, 60, 90, 180, 405):
            radians = degrees * math.pi / 180
            self.assertAlmostEqual(radians * 180 / math.pi, degrees)
        self.assertAlmostEqual(180 * math.pi / 180, math.pi)

    def test_one_radian_has_arc_length_equal_radius(self):
        for radius in (0.5, 2.3, 3, 10):
            self.assertAlmostEqual(radius * abs(1), radius)

    def test_arc_length_and_signed_angle(self):
        self.assertAlmostEqual(3 * abs(math.pi / 3), math.pi)
        self.assertAlmostEqual(3 * abs(-math.pi / 3), math.pi)

    def test_sector_area_in_valid_range(self):
        self.assertAlmostEqual(sector_area(3, math.pi / 3), 1.5 * math.pi)
        self.assertAlmostEqual(sector_area(3, -math.pi / 3), 1.5 * math.pi)
        self.assertAlmostEqual(sector_area(3, 0), 0)
        self.assertAlmostEqual(sector_area(3, 2 * math.pi), 9 * math.pi)
        with self.assertRaises(ValueError):
            sector_area(3, 3 * math.pi)

    def test_coterminal_angles_same_endpoint(self):
        theta = math.pi / 4
        for turns in (-4, -1, 0, 1, 3):
            point1, point2 = endpoint(theta), endpoint(theta + 2 * turns * math.pi)
            self.assertAlmostEqual(point1[0], point2[0])
            self.assertAlmostEqual(point1[1], point2[1])
        self.assertAlmostEqual(-315 * math.pi / 180, theta - 2 * math.pi)
        self.assertAlmostEqual(405 * math.pi / 180, theta + 2 * math.pi)

    def test_scene_has_real_entry_and_no_old_stale_circle(self):
        text = SOURCE.read_text(encoding='utf-8')
        tree = ast.parse(text)
        self.assertTrue(any(isinstance(node, ast.ClassDef) and
                            node.name == '任意角与弧度制Animation' for node in tree.body))
        self.assertIn('self._clear(title, circle, horizontal, vertical, start, negative', text)
        self.assertIn('0\\le|\\theta|\\le2\\pi', text)
        self.assertNotIn('all_mobjects = [summary_title]', text)


if __name__ == '__main__':
    unittest.main()
