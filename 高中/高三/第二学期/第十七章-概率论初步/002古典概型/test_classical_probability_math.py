"""运行：python -m unittest -v test_classical_probability_math.py。"""
import unittest
from fractions import Fraction

from classical_probability_math import (
    ball_outcomes, die_outcomes, double_die_outcomes, example_probabilities,
    probability, sum_seven_outcomes, two_coin_outcomes,
)


class ClassicalProbabilityTests(unittest.TestCase):
    def test_die_space_and_even_event(self):
        self.assertEqual(die_outcomes(), (1, 2, 3, 4, 5, 6))
        self.assertEqual(probability(die_outcomes(), (2, 4, 6)), Fraction(1, 2))

    def test_double_die_order_matters(self):
        outcomes = double_die_outcomes()
        self.assertEqual(len(outcomes), 36)
        self.assertIn((1, 6), outcomes)
        self.assertIn((6, 1), outcomes)
        self.assertEqual(len(sum_seven_outcomes()), 6)
        self.assertEqual(probability(outcomes, sum_seven_outcomes()), Fraction(1, 6))

    def test_balls_are_individually_distinguishable(self):
        balls = ball_outcomes(3, 5)
        self.assertEqual(len(balls), 8)
        self.assertEqual(len(set(balls)), 8)
        self.assertEqual(probability(balls, (b for b in balls if b[0] == '红')), Fraction(3, 8))

    def test_two_coins_are_four_ordered_results(self):
        coins = two_coin_outcomes()
        self.assertEqual(coins, (('H', 'H'), ('H', 'T'), ('T', 'H'), ('T', 'T')))
        self.assertEqual(probability(coins, (c for c in coins if 'H' in c)), Fraction(3, 4))

    def test_empty_and_full_events(self):
        self.assertEqual(probability(die_outcomes(), ()), 0)
        self.assertEqual(probability(die_outcomes(), die_outcomes()), 1)

    def test_invalid_outcomes_and_non_subset(self):
        for omega, hits in (((), ()), ((1, 1), (1,)), ((1, 2), (3,))):
            with self.subTest(omega=omega, hits=hits), self.assertRaises(ValueError):
                probability(omega, hits)

    def test_invalid_ball_counts(self):
        for counts in ((0, 0), (-1, 4), (2.5, 3), (True, 2)):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                ball_outcomes(*counts)

    def test_all_teaching_examples(self):
        self.assertEqual(example_probabilities(), {
            'die_one': Fraction(1, 6), 'die_even': Fraction(1, 2),
            'double_sum_seven': Fraction(1, 6), 'red_ball': Fraction(3, 8),
            'at_least_one_head': Fraction(3, 4),
        })


if __name__ == '__main__':
    unittest.main()
