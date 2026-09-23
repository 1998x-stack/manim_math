"""运行：python -m unittest -v test_stat_estimation_math.py。"""
from fractions import Fraction
from math import sqrt
import unittest
from stat_estimation_math import (MU_DEMO, SAMPLE, SIGMA_DEMO, Z_95_APPROX,
    normal_ci_known_sigma, normal_coverage, sample_mean,
    sample_variance_unbiased, variance_of_sample_mean)


class StatEstimationMathTests(unittest.TestCase):
    def test_sample_center_is_exactly_computed(self):
        self.assertEqual(len(SAMPLE), 5)
        self.assertEqual(sum(SAMPLE, Fraction(0)), Fraction(3, 5))
        self.assertEqual(sample_mean(), Fraction(3, 25))
        self.assertEqual(MU_DEMO, Fraction(0))

    def test_unbiased_variance_uses_n_minus_one(self):
        self.assertEqual(sample_variance_unbiased(), Fraction(997, 1000))
        self.assertEqual(sample_variance_unbiased((2, 4)), Fraction(2))

    def test_ci_is_centered_on_actual_sample_mean(self):
        left, right = normal_ci_known_sigma()
        margin = Z_95_APPROX / sqrt(5)
        self.assertAlmostEqual((left + right) / 2, float(sample_mean()))
        self.assertAlmostEqual(right - left, 2 * margin)
        self.assertAlmostEqual(left, 0.12 - margin)
        self.assertAlmostEqual(right, 0.12 + margin)
        self.assertLessEqual(left, float(MU_DEMO))
        self.assertGreaterEqual(right, float(MU_DEMO))

    def test_coverage_is_a_repeated_sampling_property(self):
        coverage = normal_coverage()
        self.assertAlmostEqual(coverage, 0.95, places=4)
        self.assertLess(coverage, 1)
        self.assertGreater(coverage, 0.9)

    def test_known_sigma_sampling_variance(self):
        self.assertAlmostEqual(variance_of_sample_mean(5), SIGMA_DEMO ** 2 / 5)
        self.assertAlmostEqual(variance_of_sample_mean(20), SIGMA_DEMO ** 2 / 20)
        self.assertLess(variance_of_sample_mean(20), variance_of_sample_mean(5))

    def test_generator_sample_is_consumed_once(self):
        self.assertAlmostEqual(sum(normal_ci_known_sigma((x for x in SAMPLE))) / 2,
                               float(sample_mean()))

    def test_invalid_confidence_inputs(self):
        for sample, sigma, z in (((), 1, 1.96), (SAMPLE, 0, 1.96),
                                 (SAMPLE, -1, 1.96), (SAMPLE, 1, 0),
                                 (SAMPLE, 1, -1)):
            with self.subTest(sigma=sigma, z=z, sample=sample), self.assertRaises(ValueError):
                normal_ci_known_sigma(sample, sigma, z)
        with self.assertRaises(ValueError):
            normal_coverage(0)

    def test_invalid_sample_statistics_and_sizes(self):
        with self.assertRaises(ValueError):
            sample_mean(())
        with self.assertRaises(ValueError):
            sample_variance_unbiased((1,))
        for n in (0, -1, True, 1.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                variance_of_sample_mean(n)


if __name__ == "__main__":
    unittest.main()
