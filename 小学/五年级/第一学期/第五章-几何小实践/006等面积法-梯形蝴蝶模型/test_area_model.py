"""无需 Manim 的蝴蝶模型数学回归测试。"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from area_model import butterfly_areas, cross, lesson_points, triangle_area


class ButterflyAreaTests(unittest.TestCase):
    def test_numeric_lesson(self):
        area = butterfly_areas(6, 3, 4)
        self.assertEqual(area, {"bottom": 8, "top": 2, "left": 4, "right": 4})
        self.assertEqual(sum(area.values()), (6 + 3) * 4 / 2)
        self.assertEqual(area["left"], area["right"])
        self.assertEqual(area["bottom"] / area["top"], (6 / 3) ** 2)

    def test_scene_vertices_and_diagonal_intersection(self):
        p = lesson_points()
        a, b, c, d, o = (p[k] for k in "ABCDO")
        self.assertAlmostEqual(cross(a, c, o), 0)
        self.assertAlmostEqual(cross(b, d, o), 0)
        self.assertAlmostEqual(a[1], b[1])
        self.assertAlmostEqual(c[1], d[1])
        model = butterfly_areas(6, 3, 4)
        for key, vertices in {
            "bottom": (a, b, o), "top": (c, d, o),
            "left": (a, d, o), "right": (b, c, o),
        }.items():
            self.assertAlmostEqual(triangle_area(*vertices), model[key])

    def test_skewed_trapezoid_still_has_equal_wings(self):
        a, b, c, d, o = (-3, -2), (3, -2), (2, 2), (-1, 2), (1 / 3, 2 / 3)
        self.assertAlmostEqual(cross(a, c, o), 0)
        self.assertAlmostEqual(cross(b, d, o), 0)
        self.assertAlmostEqual(triangle_area(a, d, o), triangle_area(b, c, o))
        self.assertAlmostEqual(triangle_area(a, d, o), 4)

    def test_other_positive_bases(self):
        for bottom, top, height in ((1, 1, 2), (7, 2, 5), (3, 8, 4)):
            with self.subTest(bottom=bottom, top=top, height=height):
                areas = butterfly_areas(bottom, top, height)
                self.assertAlmostEqual(areas["left"], areas["right"])
                self.assertAlmostEqual(sum(areas.values()), (bottom + top) * height / 2)

    def test_degenerate_rejected(self):
        for bottom, top, height in ((0, 3, 4), (6, 0, 4), (6, 3, 0), (-6, 3, 4)):
            with self.assertRaises(ValueError):
                butterfly_areas(bottom, top, height)


if __name__ == "__main__":
    unittest.main()
