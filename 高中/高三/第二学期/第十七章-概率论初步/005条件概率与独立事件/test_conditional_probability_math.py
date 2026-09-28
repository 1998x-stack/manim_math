"""运行：python -m unittest -v test_conditional_probability_math.py。"""
import unittest
from fractions import Fraction
from conditional_probability_math import (A, B, OMEGA, binomial, conditional,
                                          fair_coin_pairs, independent, probability,
                                          total_from_partition)


class ConditionalProbabilityMathTests(unittest.TestCase):
    def test_initial_model_counts(self):
        self.assertEqual((len(OMEGA), len(A), len(B), len(A & B)), (10, 5, 4, 1))
        self.assertEqual(probability(A), Fraction(1, 2))
        self.assertEqual(probability(B), Fraction(2, 5))
        self.assertEqual(conditional(A, B), Fraction(1, 4))

    def test_conditional_multiplication_identity(self):
        self.assertEqual(probability(A & B), probability(B) * conditional(A, B))
        self.assertEqual(conditional(A, OMEGA), probability(A))

    def test_b_zero_denominator_and_invalid_events(self):
        with self.assertRaises(ValueError):
            conditional(A, ())
        with self.assertRaises(ValueError):
            conditional(A, (11,))
        with self.assertRaises(ValueError):
            probability((11,))

    def test_original_events_are_not_independent(self):
        self.assertFalse(independent(A, B))
        self.assertNotEqual(conditional(A, B), probability(A))

    def test_two_independent_fair_coin_tosses(self):
        coins = fair_coin_pairs()
        first = tuple(pair for pair in coins if pair[0] == 'H')
        second = tuple(pair for pair in coins if pair[1] == 'H')
        self.assertTrue(independent(first, second, coins))
        self.assertEqual(probability(set(first) & set(second), coins), Fraction(1, 4))

    def test_binomial_three_tosses(self):
        self.assertEqual(binomial(3, 2), Fraction(3, 8))
        self.assertEqual(sum((binomial(3, k) for k in range(4)), Fraction(0)), 1)
        self.assertEqual(binomial(3, 0, Fraction(0)), 1)
        self.assertEqual(binomial(3, 3, Fraction(1)), 1)

    def test_invalid_binomial_parameters(self):
        for n, k, p in ((-1, 0, 0.5), (3, 4, 0.5), (True, 1, 0.5), (3, 2, -0.1), (3, 2, 1.1)):
            with self.subTest(n=n, k=k, p=p), self.assertRaises(ValueError):
                binomial(n, k, p)

    def test_total_probability_same_model(self):
        complement_b = OMEGA - B
        self.assertEqual(conditional(A, complement_b), Fraction(2, 3))
        self.assertEqual(total_from_partition(A, (B, complement_b)), Fraction(1, 2))
        for bad in ((B,), (B, B), (B, frozenset())):
            with self.subTest(parts=bad), self.assertRaises(ValueError):
                total_from_partition(A, bad)


if __name__ == '__main__':
    unittest.main()
