"""运行：python -m unittest -v test_frequency_math.py"""
import random
import unittest
from fractions import Fraction

from frequency_math import (benchmark_probability, experiment,
                            fair_coin_trials, running_frequency)


class FrequencyMathTests(unittest.TestCase):
    def test_exact_counts_match_every_displayed_frequency(self):
        flips = fair_coin_trials(200, 42)
        data = experiment(200, 42)
        self.assertEqual(len(data), 200)
        for n, heads, freq in data:
            self.assertEqual(heads, sum(flips[:n]))
            self.assertEqual(freq, Fraction(heads, n))
            self.assertTrue(0 <= freq <= 1)

    def test_local_rng_is_reproducible_and_does_not_touch_global_state(self):
        old_state = random.getstate()
        first = fair_coin_trials(200, 42)
        self.assertEqual(random.getstate(), old_state)
        self.assertEqual(first, fair_coin_trials(200, 42))

    def test_boundary_sequences(self):
        self.assertEqual(running_frequency((0, 0)), ((1, 0, Fraction(0)), (2, 0, Fraction(0))))
        self.assertEqual(running_frequency((1, 1)), ((1, 1, Fraction(1)), (2, 2, Fraction(1))))
        self.assertEqual(running_frequency((1, 0, 1))[-1][2], Fraction(2, 3))

    def test_frequency_need_not_improve_every_step(self):
        data = running_frequency((1, 0, 1))
        errors = [abs(item[2] - benchmark_probability()) for item in data]
        self.assertLess(errors[1], errors[2])

    def test_invalid_inputs(self):
        for count in (0, -1, True, 1.5):
            with self.subTest(count=count), self.assertRaises(ValueError):
                fair_coin_trials(count)
        for data in ((), (2,), (True,), (0.5,), (-1,)):
            with self.subTest(data=data), self.assertRaises(ValueError):
                running_frequency(data)

    def test_theoretical_probability(self):
        self.assertEqual(benchmark_probability(), Fraction(1, 2))


if __name__ == "__main__":
    unittest.main()
