"""运行：cd 本课目录 && python -m unittest -v test_arithmetic_model.py"""
import unittest
from arithmetic_model import arithmetic_mean, equal_index_sum, first_n_sum, sample, term


class ArithmeticModelTests(unittest.TestCase):
    def test_sample_matches_visible_points(self):
        self.assertEqual(sample(), (2, 5, 8, 11, 14, 17, 20))
        self.assertEqual(tuple((n, term(2, 3, n)) for n in range(1, 8)),
                         ((1, 2), (2, 5), (3, 8), (4, 11), (5, 14), (6, 17), (7, 20)))

    def test_positive_zero_and_negative_difference(self):
        for d in (-3, 0, 3):
            with self.subTest(d=d):
                values = sample(5, d, 9)
                self.assertTrue(all(b - a == d for a, b in zip(values, values[1:])))
                self.assertEqual(term(5, d, 1), 5)

    def test_sum_agrees_with_direct_addition_and_reverse_formula(self):
        for a1 in (-4, 0, 2.0):
            for d in (-3, 0, 3):
                for n in (1, 2, 7, 20):
                    with self.subTest(a1=a1, d=d, n=n):
                        expected = sum(term(a1, d, k) for k in range(1, n + 1))
                        self.assertAlmostEqual(first_n_sum(a1, d, n), expected)
                        self.assertAlmostEqual(first_n_sum(a1, d, n),
                                               n * (a1 + term(a1, d, n)) / 2)

    def test_visible_sum(self):
        self.assertEqual(first_n_sum(2, 3, 7), 77)

    def test_arithmetic_middle_and_application(self):
        self.assertEqual(arithmetic_mean(5, 11), 8)
        self.assertEqual(arithmetic_mean(7, 15), 11)
        self.assertEqual(arithmetic_mean(-8, 4), -2)

    def test_equal_index_sum_requires_valid_indices(self):
        self.assertTrue(equal_index_sum(2, 3, 3, 5, 2, 6))
        self.assertTrue(equal_index_sum(9, -2, 1, 7, 3, 5))
        with self.assertRaises(ValueError):
            equal_index_sum(2, 3, 2, 5, 1, 4)
        with self.assertRaises(ValueError):
            equal_index_sum(2, 3, 0, 5, 1, 4)

    def test_rejects_nonpositive_and_noninteger_indices(self):
        for bad in (0, -1, 1.5, True):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    term(2, 3, bad)
                with self.assertRaises(ValueError):
                    first_n_sum(2, 3, bad)
                with self.assertRaises(ValueError):
                    sample(count=bad)


if __name__ == "__main__":
    unittest.main()
