"""Test mathematical fixtures separately from Manim objects and rendered frames."""
import math
import unittest

from geometry_model import Triangle2D, midpoint, point2


class TriangleModelTests(unittest.TestCase):
    def test_right_triangle_area_and_centers(self):
        triangle = Triangle2D((0, 0), (4, 0), (0, 3))
        self.assertAlmostEqual(triangle.area, 6)
        self.assertEqual(triangle.circumcenter, (2, 1.5))
        self.assertEqual(triangle.orthocenter, (0, 0))
        for actual, expected in zip(triangle.incenter, (1, 1)):
            self.assertAlmostEqual(actual, expected)
        for actual, expected in zip(triangle.centroid, (4 / 3, 1)):
            self.assertAlmostEqual(actual, expected)
        self.assertEqual(triangle.as_scene_points()["b"], (4.0, 0.0, 0.0))

    def test_translated_triangle_shares_centers_and_lengths(self):
        base = Triangle2D((0, 0), (4, 0), (0, 3))
        shifted = Triangle2D((5, -2), (9, -2), (5, 1))
        self.assertEqual(shifted.circumcenter, (7, -0.5))
        self.assertEqual(shifted.orthocenter, (5, -2))
        self.assertAlmostEqual(shifted.area, base.area)
        self.assertEqual(midpoint(shifted.a, shifted.b), (7, -2))

    def test_collinear_and_nearly_collinear_rejected(self):
        with self.assertRaises(ValueError):
            Triangle2D((0, 0), (1, 0), (2, 0))
        with self.assertRaises(ValueError):
            Triangle2D((0, 0), (4, 0), (2, 1e-12))

    def test_nonfinite_and_three_dimensional_inputs_rejected(self):
        with self.assertRaises(ValueError):
            point2((float("nan"), 1))
        with self.assertRaises(ValueError):
            Triangle2D((0, 0), (1, 0), (0, math.inf))
        with self.assertRaises(ValueError):
            point2((1, 2, 3))


if __name__ == "__main__":
    unittest.main()
