"""Lesson-specific pure Python tests; run: python -m unittest -v test_math.py."""
import unittest
from fractions import Fraction
from math_model import (completed_square, polynomial, square_form,
                        square_completion_tiles, parabola_vertex_and_roots,
                        solve_example_via_square)


class CompletingSquareTests(unittest.TestCase):
    def test_monic_identity_for_negative_and_fractional_x(self):
        a, shift, offset = completed_square(1, 6, 5)
        self.assertEqual((a, shift, offset), (1, 3, -4))
        for x in (-20, -5, -3, -1, 0, 2, Fraction(1, 3)):
            self.assertEqual(polynomial(1, 6, 5, x),
                             square_form(a, shift, offset, x))

    def test_general_nonmonic_and_negative_a(self):
        for coefficients in ((2, -8, 3), (-2, 8, -3), (3, 5, 7), (1, 2, 5)):
            a, b, c = coefficients
            A, shift, offset = completed_square(a, b, c)
            for x in (-13, 0, Fraction(2, 5), 17):
                self.assertEqual(polynomial(a, b, c, x),
                                 square_form(A, shift, offset, x))
        self.assertEqual(completed_square(2, -8, 3), (2, -2, -5))

    def test_not_quadratic(self):
        with self.assertRaises(ValueError):
            completed_square(0, 4, 5)

    def test_area_model_and_invalid_inputs(self):
        data = square_completion_tiles()
        self.assertEqual(data, dict(base=4, bottom=6, right=6,
                                    corner_filled=5, corner_missing=4,
                                    whole=25, expression=21))
        self.assertEqual(data['expression']+data['corner_missing'], data['whole'])
        for bad in ((-1, 3, 5), (2, -3, 5), (2, 3, 10), (2.5, 3, 5)):
            with self.assertRaises(ValueError):
                square_completion_tiles(*bad)

    def test_solution_vertex_and_nonreal(self):
        self.assertEqual(solve_example_via_square(), (-5, -1))
        self.assertEqual(parabola_vertex_and_roots(), ((-3, -4), (-5, -1)))
        self.assertEqual(polynomial(1, 6, 5, -5), 0)
        self.assertEqual(polynomial(1, 6, 5, -1), 0)
        # x^2+2x+5 = (x+1)^2+4 is strictly positive on R.
        self.assertEqual(completed_square(1, 2, 5), (1, 1, 4))
        self.assertTrue(all(polynomial(1, 2, 5, x) > 0 for x in (-10, -1, 0, 10)))


if __name__ == '__main__':
    unittest.main()
