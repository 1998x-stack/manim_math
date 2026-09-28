"""运行：python -m unittest -v test_event_relations_math.py。"""
import unittest
from fractions import Fraction
from event_relations_math import (A, B, OMEGA, complementary, complement,
                                  event, intersection, mutually_exclusive,
                                  probability, union)


class EventRelationsTests(unittest.TestCase):
    def test_initial_six_outcomes(self):
        self.assertEqual(OMEGA, frozenset((1, 2, 3, 4, 5, 6)))
        self.assertEqual(A, frozenset((1, 3, 5)))
        self.assertEqual(B, frozenset((2, 3, 5)))

    def test_overlap_and_union_include_common_outcomes_once(self):
        self.assertEqual(intersection(A, B), frozenset((3, 5)))
        self.assertEqual(union(A, B), frozenset((1, 2, 3, 5)))
        self.assertEqual(probability(union(A, B)), Fraction(2, 3))
        self.assertEqual(probability(A) + probability(B) - probability(intersection(A, B)), Fraction(2, 3))

    def test_subset_and_monotonicity(self):
        subset = event((3,))
        self.assertTrue(subset <= B)
        self.assertLessEqual(probability(subset), probability(B))
        self.assertFalse(B <= subset)

    def test_exclusive_is_not_necessarily_complementary(self):
        even = event((2, 4, 6))
        self.assertTrue(mutually_exclusive(event((1,)), even))
        self.assertFalse(complementary(event((1,)), even))

    def test_complementary_covers_all_outcomes(self):
        a_bar = complement(A)
        self.assertEqual(a_bar, frozenset((2, 4, 6)))
        self.assertTrue(complementary(A, a_bar))
        self.assertEqual(probability(A) + probability(a_bar), 1)

    def test_empty_and_full_events(self):
        self.assertEqual(probability(event(())), 0)
        self.assertEqual(probability(OMEGA), 1)
        self.assertEqual(complement(OMEGA), frozenset())

    def test_invalid_events(self):
        for items in ((7,), (0,), (-1,)):
            with self.subTest(items=items), self.assertRaises(ValueError):
                event(items)
        with self.assertRaises(ValueError):
            event((), ())


if __name__ == "__main__":
    unittest.main()
