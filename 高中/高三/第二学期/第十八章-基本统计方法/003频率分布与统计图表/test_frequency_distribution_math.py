"""运行：python -m unittest -v test_frequency_distribution_math.py。"""
from collections import Counter
from fractions import Fraction
import unittest
from frequency_distribution_math import (EDGES, SCORES, STEM_SUBSET,
    distribution, frequency_polygon_area, grouped_counts, histogram_area, stem_leaf)


class FrequencyDistributionMathTests(unittest.TestCase):
    def test_all_groups_come_from_forty_actual_scores(self):
        self.assertEqual(len(SCORES), 40)
        self.assertEqual(grouped_counts(), (3, 8, 14, 10, 5))
        self.assertEqual(sum(grouped_counts()), len(SCORES))

    def test_frequencies_densities_and_histogram_area(self):
        counts, freqs, density, cumulative = distribution()
        self.assertEqual(freqs[2], Fraction(14, 40))
        self.assertEqual(density[2], Fraction(14, 400))
        self.assertEqual(sum(freqs, Fraction(0)), 1)
        self.assertEqual(histogram_area(), 1)
        for width, dens, fr in zip((10,) * 5, density, freqs):
            self.assertEqual(width * dens, fr)

    def test_cumulative_frequency_is_consistent_with_score_threshold(self):
        _, _, _, cumulative = distribution()
        self.assertEqual(cumulative, (Fraction(3, 40), Fraction(11, 40),
                                      Fraction(25, 40), Fraction(35, 40), Fraction(1)))
        self.assertEqual(cumulative[2], Fraction(sum(x < 80 for x in SCORES), len(SCORES)))
        self.assertEqual(cumulative[-1], 1)

    def test_polygon_area_is_not_histogram_area(self):
        self.assertEqual(frequency_polygon_area(), Fraction(19, 20))
        self.assertNotEqual(frequency_polygon_area(), histogram_area())

    def test_stem_leaf_represents_real_subset_without_losing_repetitions(self):
        self.assertEqual(len(STEM_SUBSET), 12)
        self.assertFalse(Counter(STEM_SUBSET) - Counter(SCORES))
        leaves = stem_leaf()
        reconstructed = tuple(stem * 10 + leaf for stem, endings in leaves.items() for leaf in endings)
        self.assertEqual(reconstructed, STEM_SUBSET)
        self.assertEqual(leaves[5], (2, 5, 8))
        self.assertEqual(leaves[8], (2, 6))

    def test_invalid_bounds_and_scores(self):
        for edges in ((50,), (50, 50, 60), (50, 60, 59)):
            with self.subTest(edges=edges), self.assertRaises(ValueError):
                grouped_counts((52,), edges)
        for scores in ((), (49,), (100,)):
            with self.subTest(scores=scores), self.assertRaises(ValueError):
                grouped_counts(scores)

    def test_invalid_stem_leaf_data(self):
        for scores in ((), (100,), (-1,), (52.5,)):
            with self.subTest(scores=scores), self.assertRaises(ValueError):
                stem_leaf(scores)


if __name__ == "__main__":
    unittest.main()
