"""运行：python -m unittest -v test_sampling_techniques_math.py。"""
import random
import unittest
from fractions import Fraction
from sampling_techniques_math import (ALLOCATIONS, LAYERS, POPULATION,
    allocation_rates, random_systematic, simple_random, stratified, systematic)


class SamplingTechniquesMathTests(unittest.TestCase):
    def test_population_and_layers(self):
        self.assertEqual(len(POPULATION), 40)
        self.assertEqual(tuple(map(len, LAYERS)), (20, 12, 8))
        self.assertEqual(set().union(*map(set, LAYERS)), set(POPULATION))

    def test_simple_random_is_local_and_without_replacement(self):
        state = random.getstate()
        sample = simple_random()
        self.assertEqual(state, random.getstate())
        self.assertEqual(sample, simple_random())
        self.assertEqual(len(set(sample)), len(sample))
        self.assertEqual(len(sample), 5)
        self.assertTrue(set(sample) <= set(POPULATION))

    def test_systematic_numbering_and_start(self):
        self.assertEqual(systematic(start=4), (4, 12, 20, 28, 36))
        self.assertEqual(systematic(start=1), (1, 9, 17, 25, 33))
        self.assertEqual(systematic(start=8), (8, 16, 24, 32, 40))
        starts = [systematic(start=s) for s in range(1, 9)]
        self.assertEqual(len({tuple(sample) for sample in starts}), 8)
        self.assertEqual(set().union(*map(set, starts)), set(POPULATION))

    def test_random_systematic_reproducible_and_valid(self):
        state = random.getstate()
        start, sample = random_systematic(seed=13)
        self.assertEqual(state, random.getstate())
        self.assertTrue(1 <= start <= 8)
        self.assertEqual(sample, systematic(start=start))
        self.assertEqual((start, sample), random_systematic(seed=13))

    def test_strata_are_actual_disjoint_samples(self):
        draws = stratified()
        self.assertEqual(tuple(map(len, draws)), ALLOCATIONS)
        self.assertEqual(len(set().union(*map(set, draws))), 10)
        for sample, layer in zip(draws, LAYERS):
            self.assertTrue(set(sample) <= set(layer))

    def test_proportionate_allocation(self):
        self.assertEqual(allocation_rates(), (Fraction(1, 4),) * 3)
        self.assertEqual(sum(ALLOCATIONS), 10)
        self.assertEqual(tuple(len(layer) for layer in LAYERS), (20, 12, 8))

    def test_invalid_parameters(self):
        for bad in (0, 41, -1, True, 1.5):
            with self.subTest(simple_size=bad), self.assertRaises(ValueError):
                simple_random(size=bad)
        for start in (0, 9, 1.5):
            with self.subTest(start=start), self.assertRaises(ValueError):
                systematic(start=start)
        with self.assertRaises(ValueError):
            systematic(size=6)
        with self.assertRaises(ValueError):
            stratified(((1, 2), (2, 3)), (1, 1))
        with self.assertRaises(ValueError):
            stratified(LAYERS, (5, 3, 9))
        with self.assertRaises(ValueError):
            allocation_rates(LAYERS, (5, 3, 9))


if __name__ == "__main__":
    unittest.main()
