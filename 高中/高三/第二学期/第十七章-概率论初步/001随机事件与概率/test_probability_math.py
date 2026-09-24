"""运行：python -m unittest -v test_probability_math.py"""

import unittest
from probability_math import union_probability, complement_probability


class ProbabilityMathTests(unittest.TestCase):
    def test_lesson_example(self):
        self.assertAlmostEqual(union_probability(0.5, 0.4, 0.2), 0.7)

    def test_disjoint_events(self):
        self.assertAlmostEqual(union_probability(0.3, 0.4, 0), 0.7)

    def test_certain_union(self):
        self.assertAlmostEqual(union_probability(0.7, 0.6, 0.3), 1)

    def test_same_event(self):
        self.assertAlmostEqual(union_probability(0.4, 0.4, 0.4), 0.4)

    def test_invalid_triples(self):
        for triple in ((0.8, 0.7, 0.1), (0.2, 0.4, 0.3),
                       (0.2, 0.4, -0.1), (1.1, 0.3, 0.2)):
            with self.subTest(triple=triple), self.assertRaises(ValueError):
                union_probability(*triple)

    def test_complement_extremes(self):
        self.assertEqual(complement_probability(0), 1)
        self.assertEqual(complement_probability(1), 0)
        self.assertAlmostEqual(complement_probability(0.6), 0.4)

    def test_complement_invalid(self):
        for value in (-0.01, 1.01):
            with self.subTest(value=value), self.assertRaises(ValueError):
                complement_probability(value)


if __name__ == "__main__":
    unittest.main()
