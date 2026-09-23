"""蝴蝶模型专项回归：交点、两段高、面积分割与公共部分消去。"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from area_model import (altitude_segments, butterfly_areas, common_area_decomposition,
                        cross, lesson_points, trapezoid_points, triangle_area)


class ButterflyAreaTests(unittest.TestCase):
    def test_numeric_lesson(self):
        area = butterfly_areas(6, 3, 4)
        self.assertEqual(area, {"bottom": 8, "top": 2, "left": 4, "right": 4})
        self.assertEqual(sum(area.values()), (6 + 3) * 4 / 2)
        self.assertEqual(area["left"], area["right"])
        self.assertEqual(area["bottom"] / area["top"], (6 / 3) ** 2)

    def test_lesson_heights_are_true_perpendicular_distances(self):
        p = lesson_points()
        h = altitude_segments(p)
        self.assertAlmostEqual(h["bottom"], 8 / 3)
        self.assertAlmostEqual(h["top"], 4 / 3)
        self.assertAlmostEqual(h["bottom"] + h["top"], 4)
        self.assertAlmostEqual(h["bottom"] / h["top"], 2)
        self.assertAlmostEqual(p["O"][0], 0)
        self.assertAlmostEqual(p["O"][1], 2 / 3)

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

    def test_common_part_subtraction_proves_equal_wings(self):
        for shift in (-2, -0.8, 0, 0.5, 1.75, 3):
            with self.subTest(shift=shift):
                p = trapezoid_points(6, 3, 4, top_shift=shift)
                pieces = common_area_decomposition(p)
                self.assertAlmostEqual(pieces["ABD"], 12)
                self.assertAlmostEqual(pieces["ABC"], 12)
                self.assertAlmostEqual(pieces["ABD"], pieces["ABO"] + pieces["AOD"])
                self.assertAlmostEqual(pieces["ABC"], pieces["ABO"] + pieces["BOC"])
                self.assertAlmostEqual(pieces["AOD"], pieces["BOC"])
                self.assertAlmostEqual(pieces["AOD"], 4)

    def test_skewed_trapezoids_obey_intersection_and_partition(self):
        for bottom, top, height, shift in ((6, 3, 4, 0.5), (1, 1, 2, 3),
                                           (7, 2, 5, -3), (3, 8, 4, 2.2)):
            with self.subTest(data=(bottom, top, height, shift)):
                p = trapezoid_points(bottom, top, height, top_shift=shift)
                a, b, c, d, o = (p[k] for k in "ABCDO")
                self.assertAlmostEqual(cross(a, c, o), 0)
                self.assertAlmostEqual(cross(b, d, o), 0)
                self.assertAlmostEqual((o[1] - a[1]) / (d[1] - o[1]), bottom / top)
                pieces = butterfly_areas(bottom, top, height)
                observed = {"bottom": triangle_area(a, b, o),
                            "top": triangle_area(c, d, o),
                            "left": triangle_area(a, d, o),
                            "right": triangle_area(b, c, o)}
                for key in pieces:
                    self.assertAlmostEqual(observed[key], pieces[key])
                self.assertAlmostEqual(sum(observed.values()), (bottom + top) * height / 2)

    def test_degenerate_rejected(self):
        for bottom, top, height in ((0, 3, 4), (6, 0, 4), (6, 3, 0), (-6, 3, 4)):
            with self.assertRaises(ValueError):
                butterfly_areas(bottom, top, height)
            with self.assertRaises(ValueError):
                trapezoid_points(bottom, top, height)


if __name__ == "__main__":
    unittest.main()
