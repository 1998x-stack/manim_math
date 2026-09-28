"""Lesson-specific tests independent of Manim and its renderer."""
import unittest
from fractions import Fraction
from math import sqrt
from math_model import Quadratic, EXAMPLE, PRACTICE, area_square_model, discriminant_family


class FormulaTests(unittest.TestCase):
    def test_non_quadratic_rejected(self):
        with self.assertRaises(ValueError):
            Quadratic(0, 2, 3)

    def test_algebraic_completed_square_identity(self):
        for a, b, c in [(1, 4, 0), (2, -2, -1), (-3, 5, 8), (Fraction(1, 2), -3, 7)]:
            q = Quadratic(a, b, c)
            aa, h, k = q.completed_square()
            for x in [Fraction(-3, 2), 0, Fraction(5, 4)]:
                self.assertEqual(q.value(x), aa * (x - h) ** 2 + k)

    def test_exact_example_claims(self):
        self.assertEqual(EXAMPLE.delta, 12)
        self.assertEqual(EXAMPLE.axis, Fraction(1, 2))
        self.assertEqual(EXAMPLE.vertex_y, Fraction(-3, 2))
        low, high = EXAMPLE.real_roots()
        self.assertAlmostEqual(low, (1 - sqrt(3)) / 2)
        self.assertAlmostEqual(high, (1 + sqrt(3)) / 2)
        self.assertAlmostEqual(float(EXAMPLE.value(Fraction(1, 2))), -1.5)

    def test_root_count_and_repeated_root(self):
        for k, count in [(2, 2), (1, 2), (0, 1), (-1, 0)]:
            q = discriminant_family(k)
            self.assertEqual(q.real_root_count, count)
            self.assertEqual(q.delta, 4 * k)
        self.assertEqual(discriminant_family(0).real_roots(), (1.0,))
        self.assertEqual(discriminant_family(-1).real_roots(), ())

    def test_negative_leading_coefficient(self):
        q = Quadratic(-2, 2, 1)
        self.assertEqual(q.delta, 12)
        for root in q.real_roots():
            self.assertAlmostEqual(float(q.a) * root ** 2 + float(q.b) * root + float(q.c), 0, places=10)

    def test_geometry_tile_counts_and_domain(self):
        data = area_square_model(2, 2)
        self.assertEqual((data['base'], data['strips'], data['corner'], data['whole']), (4, 8, 4, 16))
        with self.assertRaises(ValueError):
            area_square_model(-1, 2)

    def test_practice_radicals_and_residual(self):
        self.assertEqual(PRACTICE.delta, 28)
        low, high = PRACTICE.real_roots()
        self.assertAlmostEqual(low, (-1 - sqrt(7)) / 3)
        self.assertAlmostEqual(high, (-1 + sqrt(7)) / 3)
        for root in (low, high):
            a, b, c = map(float, (PRACTICE.a, PRACTICE.b, PRACTICE.c))
            self.assertAlmostEqual(a * root ** 2 + b * root + c, 0, places=10)

    def test_rounded_example_is_3sf(self):
        low, high = EXAMPLE.real_roots()
        self.assertEqual(f'{low:.3g}', '-0.366')
        self.assertEqual(f'{high:.3g}', '1.37')


if __name__ == '__main__':
    unittest.main()
