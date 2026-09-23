"""运行：python -m unittest discover -s 本目录 -p 'test_area_model.py'"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from area_model import lesson_area, lesson_triangle, signed_double_area, triangle_area


class SameBaseEqualHeightTests(unittest.TestCase):
    def test_fixed_area_over_entire_animation(self):
        for x in (-2.5, -2.3, -1, 0, 1.1, 2.3, 2.5):
            with self.subTest(x=x):
                a, b, c = lesson_triangle(x)
                self.assertAlmostEqual(c[1] - a[1], 3)
                self.assertAlmostEqual(b[0] - a[0], 6)
                self.assertAlmostEqual(lesson_area(x), 9)

    def test_area_matches_shoelace(self):
        a, b, c = lesson_triangle(0.4)
        self.assertAlmostEqual(signed_double_area(a, b, c), 18)
        self.assertEqual(triangle_area(6, 3), 9)

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
