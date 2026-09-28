"""Run: python -m unittest -v test_math.py"""
import unittest
from fractions import Fraction as F
from math_model import (Line, Parabola, MAIN_CURVE, MAIN_LINE, TANGENT,
                        MISSED, PRACTICE_CURVE, PRACTICE_LINE,
                        eliminated_coefficients, discriminant, intersections,
                        circle_line_points, exact_sqrt_fraction)


class ModelChecks(unittest.TestCase):
    def test_elimination(self):
        self.assertEqual(eliminated_coefficients(MAIN_CURVE, MAIN_LINE),
                         (F(1), F(-3), F(0)))

    def test_two_exact_points(self):
        self.assertEqual(intersections(MAIN_CURVE, MAIN_LINE),
                         ((F(0), F(1)), (F(3), F(4))))

    def test_both_equations_checked(self):
        for x, y in intersections(MAIN_CURVE, MAIN_LINE):
            self.assertEqual(MAIN_CURVE.at(x), y)
            self.assertEqual(MAIN_LINE.at(x), y)

    def test_tangent_single_point(self):
        self.assertEqual(discriminant(MAIN_CURVE, TANGENT), 0)
        self.assertEqual(intersections(MAIN_CURVE, TANGENT),
                         ((F(3, 2), F(1, 4)),))

    def test_no_real_intersection(self):
        self.assertLess(discriminant(MAIN_CURVE, MISSED), 0)
        self.assertEqual(intersections(MAIN_CURVE, MISSED), ())

    def test_line_sweep_classification(self):
        self.assertEqual(tuple(len(intersections(MAIN_CURVE, Line(F(1), F(k))))
                               for k in (1, F(-5, 4), -2)), (2, 1, 0))

    def test_circle_conic(self):
        self.assertEqual(circle_line_points(F(5), MAIN_LINE),
                         ((F(-2), F(-1)), (F(1), F(2))))

    def test_practice(self):
        self.assertEqual(intersections(PRACTICE_CURVE, PRACTICE_LINE),
                         ((F(1), F(1)), (F(3), F(5))))

    def test_non_square_discriminant(self):
        self.assertIsNone(exact_sqrt_fraction(F(2)))
        points = intersections(Parabola(F(1), F(0), F(-2)), Line(F(0), F(0)))
        self.assertAlmostEqual(float(points[0][0]), -2**.5)
        self.assertAlmostEqual(float(points[1][0]), 2**.5)

    def test_domain_errors(self):
        with self.assertRaises(ValueError):
            Parabola(F(0), F(1), F(2))
        with self.assertRaises(ValueError):
            circle_line_points(F(0), MAIN_LINE)
        with self.assertRaises(ValueError):
            exact_sqrt_fraction(F(-1))


if __name__ == '__main__':
    unittest.main()
