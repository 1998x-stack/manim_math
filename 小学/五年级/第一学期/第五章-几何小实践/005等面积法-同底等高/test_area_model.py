"""同底等高：验证连续移动的几何性质与长方形对角线等积。"""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from area_model import (altitude_foot, lesson_area, lesson_triangle,
                        rectangle_diagonal_areas, signed_double_area, triangle_area)


class SameBaseEqualHeightTests(unittest.TestCase):
    def test_fixed_area_over_entire_animation(self):
        for i in range(101):
            x = -2.5 + i * 0.05
            with self.subTest(x=x):
                a, b, c = lesson_triangle(x)
                self.assertAlmostEqual(c[1] - a[1], 3)
                self.assertAlmostEqual(b[0] - a[0], 6)
                self.assertAlmostEqual(lesson_area(x), 9)

    def test_moving_altitude_is_perpendicular_and_three_units_high(self):
        for x in (-2.5, -2.3, 0, 1.37, 2.3, 2.5):
            with self.subTest(x=x):
                a, b, c = lesson_triangle(x)
                h = altitude_foot(a, b, c)
                base = (b[0] - a[0], b[1] - a[1])
                altitude = (c[0] - h[0], c[1] - h[1])
                self.assertAlmostEqual(h[1], a[1])
                self.assertAlmostEqual(h[0], x)
                self.assertAlmostEqual(base[0] * altitude[0] + base[1] * altitude[1], 0)
                self.assertAlmostEqual(math.hypot(*altitude), 3)

    def test_project_on_oblique_extended_base(self):
        a, b, c = (1, 1), (3, 3), (5, 1)
        h = altitude_foot(a, b, c)
        self.assertAlmostEqual(h[0], 3)
        self.assertAlmostEqual(h[1], 3)
        with self.assertRaises(ValueError):
            altitude_foot(a, a, c)

    def test_area_matches_shoelace(self):
        a, b, c = lesson_triangle(0.4)
        self.assertAlmostEqual(signed_double_area(a, b, c), 18)
        self.assertEqual(triangle_area(6, 3), 9)

    def test_diagonal_splits_rectangle_into_equal_triangles(self):
        for base, height in ((6, 3), (2, 7), (1, 1)):
            with self.subTest(base=base, height=height):
                parts = rectangle_diagonal_areas(base, height)
                self.assertEqual(parts["lower"], parts["upper"])
                self.assertAlmostEqual(parts["lower"] + parts["upper"], parts["rectangle"])

    def test_reject_degenerate_base_or_height(self):
        for base, height in ((0, 3), (6, 0), (-6, 3), (6, -1)):
            with self.subTest(base=base, height=height):
                with self.assertRaises(ValueError):
                    triangle_area(base, height)

    def test_reject_offscreen_apex(self):
        for x in (-2.51, 2.51):
            with self.assertRaises(ValueError):
                lesson_triangle(x)


if __name__ == "__main__":
    unittest.main()
