"""Lesson-specific tests: algebraic claims, graph data, domains, degenerate cases."""
import math
import unittest
from fractions import Fraction
from math_model import Quadratic, UP, DOWN, PRACTICE


class QuadraticExtremaTests(unittest.TestCase):
    def test_original_example_and_vertex(self):
        self.assertEqual((UP.h, UP.k, UP.kind), (2, -3, 'minimum'))
        self.assertEqual((UP.value(0), UP.value(1), UP.value(3)), (1, -2, -2))

    def test_vertex_identity_general_and_fractional(self):
        for q in (UP, DOWN, PRACTICE, Quadratic(2, 3, -7), Quadratic(-3, 5, 2)):
            for x in (Fraction(-5, 2), 0, 1, Fraction(13, 7)):
                self.assertTrue(q.verify_vertex_identity(x))

    def test_symmetric_values(self):
        for q in (UP, DOWN, PRACTICE):
            for distance in (0, Fraction(1, 3), 1, 2):
                self.assertEqual(q.value(q.h-distance), q.value(q.h+distance))

    def test_discriminant_and_roots(self):
        self.assertEqual(UP.discriminant, 12)
        self.assertEqual(DOWN.roots(), (1.0, 5.0))
        self.assertEqual(PRACTICE.discriminant, 20)
        for q in (UP, DOWN, PRACTICE):
            for root in q.roots():
                self.assertTrue(math.isclose(float(q.value(Fraction(root))), 0, abs_tol=1e-10))

    def test_exact_max_and_vertex_intercepts(self):
        self.assertEqual((DOWN.h, DOWN.k, DOWN.kind), (3, 4, 'maximum'))
        self.assertEqual((DOWN.value(0), DOWN.value(1), DOWN.value(5)), (-5, 0, 0))

    def test_interval_extrema_vertex_excluded(self):
        answer = UP.interval_extrema(3, 4)
        self.assertEqual(answer['min'], (-2, 3))
        self.assertEqual(answer['max'], (1, 4))

    def test_interval_extrema_vertex_included(self):
        answer = DOWN.interval_extrema(1, 5)
        self.assertEqual(answer['max'], (4, 3))
        self.assertEqual(answer['min'][0], 0)

    def test_interval_singleton_and_invalid(self):
        self.assertEqual(UP.interval_extrema(1, 1)['min'], (Fraction(-2), Fraction(1)))
        with self.assertRaises(ValueError):
            UP.interval_extrema(3, 2)

    def test_nonquadratic_rejected(self):
        with self.assertRaises(ValueError):
            Quadratic(0, 3, 2)

    def test_negative_discriminant_and_tangency(self):
        self.assertEqual(Quadratic(1, 0, 1).roots(), ())
        self.assertEqual(Quadratic(1, -4, 4).roots(), (2.0,))

    def test_practice_answer(self):
        self.assertEqual((PRACTICE.h, PRACTICE.k, PRACTICE.value(0)), (2, 5, 1))
        x1, x2 = PRACTICE.roots()
        self.assertTrue(math.isclose(x1, 2-math.sqrt(5), abs_tol=1e-12))
        self.assertTrue(math.isclose(x2, 2+math.sqrt(5), abs_tol=1e-12))

    def test_vertex_constructor(self):
        self.assertEqual(Quadratic.from_vertex(-2, 2, 5), Quadratic(-2, 8, -3))


if __name__ == '__main__':
    unittest.main()
