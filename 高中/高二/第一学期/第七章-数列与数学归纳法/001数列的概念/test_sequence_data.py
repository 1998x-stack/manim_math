"""Run with python -m unittest -v test_sequence_data.py (no Manim required)."""

import unittest

from sequence_data import arithmetic_terms, classification_samples, prefix_sums


class SequenceDataTest(unittest.TestCase):
    def test_terms_and_coordinates(self):
        terms = arithmetic_terms(8)
        self.assertEqual(terms, (2, 4, 6, 8, 10, 12, 14, 16))
        self.assertTrue(all(0 <= value <= 18 for value in terms))
        self.assertEqual(tuple(zip(range(1, 9), terms))[-1], (8, 16))

    def test_recurrence_and_prefix_sums(self):
        terms = arithmetic_terms(8)
        sums = prefix_sums(terms)
        self.assertEqual(sums[0], terms[0])
        self.assertEqual(sums[4], 30)
        for index in range(1, 8):
            self.assertEqual(terms[index], terms[index - 1] + 2)
            self.assertEqual(terms[index], sums[index] - sums[index - 1])

    def test_all_classifications(self):
        samples = classification_samples()
        self.assertTrue(all(a < b for a, b in zip(samples["递增数列"], samples["递增数列"][1:])))
        self.assertTrue(all(a > b for a, b in zip(samples["递减数列"], samples["递减数列"][1:])))
        self.assertEqual(len(set(samples["常数列"])), 1)
        self.assertTrue(all(samples["周期数列"][i] == samples["周期数列"][i + 3] for i in range(5)))
        self.assertTrue(all(0 <= v <= 18 for values in samples.values() for v in values))

    def test_invalid_length(self):
        for invalid in (0, -1, True, 2.5):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    arithmetic_terms(invalid)
                with self.assertRaises(ValueError):
                    classification_samples(invalid)


if __name__ == "__main__":
    unittest.main()
