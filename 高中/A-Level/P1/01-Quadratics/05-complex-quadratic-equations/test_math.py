"""Lesson-specific independent tests; runs without Manim."""
import math
import unittest
from math_model import (MAIN_T, MAIN_X, SURD_X, POWER_X, PRACTICE_X, CHALLENGE_X,
                        evaluate_transformed, preimages, quadratic_roots, solve_transformed)


class TransformQuadraticsTests(unittest.TestCase):
    def test_main_intermediate_roots(self):
        self.assertEqual(MAIN_T, (1., 4.))

    def test_main_four_roots(self):
        self.assertEqual(MAIN_X, (-2., -1., 1., 2.))
        for x in MAIN_X:
            self.assertAlmostEqual(evaluate_transformed(x, 1, -5, 4, 'square'), 0)

    def test_negative_t_not_in_range_of_square(self):
        self.assertEqual(preimages(-2, 'square'), ())
        self.assertEqual(solve_transformed(1, -1, -6, 'square'), (-math.sqrt(3), math.sqrt(3)))

    def test_zero_has_one_preimage(self):
        self.assertEqual(preimages(0, 'square'), (0.,))
        self.assertEqual(solve_transformed(1, -1, 0, 'square'), (-1., 0., 1.))

    def test_repeated_root_has_two_preimages_not_four(self):
        self.assertEqual(quadratic_roots(1, -2, 1), (1.,))
        self.assertEqual(solve_transformed(1, -2, 1, 'square'), (-1., 1.))

    def test_no_real_intermediate_roots(self):
        self.assertEqual(solve_transformed(1, 0, 1, 'square'), ())

    def test_sqrt_example_and_original_equation(self):
        self.assertEqual(SURD_X, (4., 9.))
        for x in SURD_X:
            self.assertAlmostEqual(evaluate_transformed(x, 1, -5, 6, 'square_root'), 0)
        self.assertEqual(preimages(-1, 'square_root'), ())
        with self.assertRaises(ValueError):
            evaluate_transformed(-1, 1, -5, 6, 'square_root')

    def test_power_example_and_range(self):
        self.assertAlmostEqual(POWER_X[0], 0., places=10)
        self.assertAlmostEqual(POWER_X[1], 2., places=10)
        self.assertEqual(preimages(0, 'power3'), ())
        self.assertEqual(preimages(-2, 'power3'), ())
        for x in POWER_X:
            self.assertAlmostEqual(evaluate_transformed(x, 1, -10, 9, 'power3'), 0)

    def test_practice_filters_negative_intermediate_root(self):
        self.assertEqual(quadratic_roots(1, -1, -6), (-2., 3.))
        self.assertEqual(PRACTICE_X, (-math.sqrt(3), math.sqrt(3)))

    def test_new_independent_challenge(self):
        self.assertEqual(CHALLENGE_X, (-3., -1., 1., 3.))
        for x in CHALLENGE_X:
            self.assertAlmostEqual(evaluate_transformed(x, 1, -10, 9, 'square'), 0)

    def test_invalid_coefficient_and_unknown_mode(self):
        with self.assertRaises(ValueError):
            quadratic_roots(0, 1, 2)
        with self.assertRaises(ValueError):
            preimages(1, 'cube')


if __name__ == '__main__':
    unittest.main()
