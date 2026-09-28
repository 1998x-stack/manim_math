"""运行：python -m unittest -v test_population_sample_math.py。"""
import random
import unittest
from collections import Counter
from fractions import Fraction
from population_sample_math import (POPULATION, MEASUREMENTS, all_equal_size_subsets,
                                    inclusion_probability, sample_mean,
                                    sample_without_replacement)


class PopulationSampleMathTests(unittest.TestCase):
    def test_population_and_measurements(self):
        self.assertEqual(POPULATION, tuple(range(1, 21)))
        self.assertEqual(set(MEASUREMENTS), set(POPULATION))
        self.assertEqual(len(POPULATION), 20)

    def test_six_distinct_members_from_population(self):
        selected = sample_without_replacement()
        self.assertEqual(len(selected), 6)
        self.assertEqual(len(set(selected)), 6)
        self.assertTrue(set(selected) <= set(POPULATION))
        self.assertEqual(selected, sample_without_replacement())

    def test_local_rng_does_not_modify_global_random(self):
        before = random.getstate()
        sample_without_replacement(seed=7)
        self.assertEqual(before, random.getstate())

    def test_all_fixed_size_subsets_are_symmetric(self):
        subsets = all_equal_size_subsets((1, 2, 3, 4), 2)
        self.assertEqual(len(subsets), 6)
        frequencies = Counter(member for subset in subsets for member in subset)
        self.assertEqual(set(frequencies.values()), {3})
        self.assertEqual(inclusion_probability(4, 2), Fraction(1, 2))
        self.assertEqual(inclusion_probability(20, 6), Fraction(3, 10))

    def test_mean_uses_actual_sample_ids(self):
        selected = sample_without_replacement()
        values = [MEASUREMENTS[id_] for id_ in selected]
        self.assertEqual(sample_mean(MEASUREMENTS, selected), Fraction(sum(values), 6))
        self.assertEqual(sample_mean(MEASUREMENTS, POPULATION), Fraction(71))

    def test_sample_mean_edge_cases(self):
        self.assertEqual(sample_mean(MEASUREMENTS, (1,)), Fraction(52))
        for ids in ((), (1, 1), (1, 21)):
            with self.subTest(ids=ids), self.assertRaises(ValueError):
                sample_mean(MEASUREMENTS, ids)

    def test_invalid_sample_sizes_and_population(self):
        for n in (0, -1, 21, True, 2.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                sample_without_replacement(size=n)
        for population in ((), (1, 1)):
            with self.subTest(population=population), self.assertRaises(ValueError):
                sample_without_replacement(population, 1)
        for total, size in ((0, 0), (3, 4), (True, 1), (3, -1)):
            with self.subTest(total=total, size=size), self.assertRaises(ValueError):
                inclusion_probability(total, size)


if __name__ == "__main__":
    unittest.main()
