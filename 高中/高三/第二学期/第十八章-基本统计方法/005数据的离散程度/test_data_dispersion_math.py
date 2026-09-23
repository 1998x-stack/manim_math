"""运行：python -m unittest -v test_data_dispersion_math.py。"""
import math
import unittest
from fractions import Fraction
from data_dispersion_math import (A, B, coefficient_of_variation, data_range,
    descriptive_variance, mean, standard_deviation, unbiased_sample_variance)


class DataDispersionMathTests(unittest.TestCase):
    def test_two_sets_have_same_mean(self):
        self.assertEqual(len(A), len(B))
        self.assertEqual(mean(A), mean(B))
        self.assertEqual(mean(A), 5)

    def test_data_range_values(self):
        self.assertEqual(data_range(A), 4)
        self.assertEqual(data_range(B), 8)
        self.assertEqual(data_range((7,)), 0)

    def test_descriptive_variances_and_squared_deviations(self):
        self.assertEqual(descriptive_variance(A), Fraction(2))
        self.assertEqual(descriptive_variance(B), Fraction(10))
        self.assertEqual(sum((x - 5) ** 2 for x in A), 10)
        self.assertEqual(sum((x - 5) ** 2 for x in B), 50)

    def test_n_and_n_minus_one_are_not_interchangeable(self):
        self.assertEqual(unbiased_sample_variance(A), Fraction(5, 2))
        self.assertEqual(unbiased_sample_variance(B), Fraction(25, 2))
        self.assertNotEqual(descriptive_variance(A), unbiased_sample_variance(A))

    def test_standard_deviation_values(self):
        self.assertAlmostEqual(standard_deviation(A), math.sqrt(2))
        self.assertAlmostEqual(standard_deviation(B), math.sqrt(10))
        self.assertLess(standard_deviation(A), standard_deviation(B))

    def test_cv_uses_common_positive_mean(self):
        self.assertAlmostEqual(coefficient_of_variation(A), math.sqrt(2) / 5)
        self.assertAlmostEqual(coefficient_of_variation(B), math.sqrt(10) / 5)
        self.assertGreater(coefficient_of_variation(B), coefficient_of_variation(A))

    def test_zero_deviation_and_zero_mean(self):
        self.assertEqual(descriptive_variance((3, 3, 3)), 0)
        self.assertEqual(standard_deviation((3, 3)), 0)
        with self.assertRaises(ValueError):
            coefficient_of_variation((-1, 1))

    def test_invalid_empty_and_unbiased_singleton(self):
        for function in (mean, data_range, descriptive_variance,
                         standard_deviation, coefficient_of_variation):
            with self.subTest(function=function.__name__), self.assertRaises(ValueError):
                function(())
        with self.assertRaises(ValueError):
            unbiased_sample_variance((2,))


if __name__ == "__main__":
    unittest.main()
