"""运行：python -m unittest -v test_central_tendency_math.py。"""
import unittest
from fractions import Fraction
from central_tendency_math import (AFTER, BEFORE, EVEN, MODE_DATA, ODD,
    SCORES, WEIGHTS, mean, median, modes, outlier_comparison, weighted_mean)


class CentralTendencyMathTests(unittest.TestCase):
    def test_odd_sample_mean_and_median(self):
        self.assertEqual(len(ODD), 9)
        self.assertEqual(sum(ODD), 680)
        self.assertEqual(mean(ODD), Fraction(680, 9))
        self.assertEqual(median(ODD), 78)

    def test_even_sample_median(self):
        self.assertEqual(len(EVEN), 6)
        self.assertEqual(median(EVEN), Fraction(74 + 78, 2))
        self.assertEqual(median((1, 2)), Fraction(3, 2))

    def test_weighted_mean_from_visible_scores(self):
        self.assertEqual(sum(WEIGHTS), 1)
        self.assertEqual(weighted_mean(SCORES, WEIGHTS), 79)
        self.assertEqual(weighted_mean((85, 70), (6, 4)), 79)
        self.assertEqual(weighted_mean((52,), (2,)), 52)

    def test_unique_multiple_and_no_repeated_mode(self):
        self.assertEqual(modes(MODE_DATA), (78,))
        self.assertEqual(modes((1, 1, 2, 2, 3)), (1, 2))
        self.assertEqual(modes((1, 2, 3)), ())
        self.assertEqual(modes((5,)), ())

    def test_outlier_is_one_controlled_replacement(self):
        self.assertEqual(BEFORE[:-1], AFTER[:-1])
        self.assertEqual((BEFORE[-1], AFTER[-1]), (78, 200))
        self.assertEqual(outlier_comparison(), ((Fraction(275, 4), Fraction(69)),
                                                (Fraction(84), Fraction(69))))
        self.assertEqual(mean(AFTER) - mean(BEFORE), Fraction(61, 4))
        self.assertEqual(median(AFTER), median(BEFORE))

    def test_mean_and_median_boundary_cases(self):
        self.assertEqual(mean((1,)), 1)
        self.assertEqual(median((1,)), 1)
        self.assertEqual(mean((1, 2, 3)), 2)
        with self.assertRaises(ValueError):
            mean(())
        with self.assertRaises(ValueError):
            median(())

    def test_weight_validation(self):
        for xs, weights in (((), ()), ((1,), ()), ((1, 2), (1,)),
                            ((1, 2), (0, 0)), ((1, 2), (-1, 2))):
            with self.subTest(xs=xs, weights=weights), self.assertRaises(ValueError):
                weighted_mean(xs, weights)
        with self.assertRaises(ValueError):
            modes(())

    def test_outlier_input_validation(self):
        for before, after in (((), ()), ((1, 2), (1,))):
            with self.assertRaises(ValueError):
                outlier_comparison(before, after)


if __name__ == "__main__":
    unittest.main()
