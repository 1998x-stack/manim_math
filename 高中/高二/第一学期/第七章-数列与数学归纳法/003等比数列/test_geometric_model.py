"""运行：cd 本课目录 && python -m unittest -v test_geometric_model.py"""
import unittest
from geometric_model import (
    area_tiles, equal_index_product, finite_sum, infinite_sum, sample, term,
)


class GeometricModelTests(unittest.TestCase):
    def test_visible_terms_and_ratio(self):
        self.assertEqual(sample(), (2, 4, 8, 16, 32))
        self.assertTrue(all(b / a == 2 for a, b in zip(sample(), sample()[1:])))

    def test_negative_ratio_and_constant_sequence(self):
        self.assertEqual(sample(3, -2, 4), (3, -6, 12, -24))
        self.assertEqual(sample(3, 1, 4), (3, 3, 3, 3))
        self.assertEqual(sample(3, 0.5, 4), (3, 1.5, 0.75, 0.375))

    def test_finite_sum_matches_direct_summation(self):
        for a1 in (-2, 2):
            for q in (-2, -0.5, 0.5, 1, 2):
                for n in (1, 2, 4, 8):
                    with self.subTest(a1=a1, q=q, n=n):
                        self.assertAlmostEqual(finite_sum(a1, q, n),
                                               sum(term(a1, q, k) for k in range(1, n + 1)))
        self.assertEqual(finite_sum(2, 2, 4), 30)
        self.assertEqual(finite_sum(2, 1, 4), 8)

    def test_infinite_sum_requires_strict_convergence(self):
        self.assertEqual(infinite_sum(2, 0.5), 4)
        self.assertAlmostEqual(infinite_sum(2, -0.5), 4 / 3)
        for bad in (-2, -1, 0, 1, 2):
            with self.subTest(q=bad), self.assertRaises(ValueError):
                infinite_sum(2, bad)

    def test_square_label_area_matches_side_squared(self):
        tiles = area_tiles()
        self.assertEqual(tuple(area for area, _ in tiles), (2, 4, 8, 16))
        for area, side in tiles:
            self.assertAlmostEqual((side / 0.55) ** 2, area)
        self.assertAlmostEqual(tiles[1][1] / tiles[0][1], 2 ** 0.5)
        self.assertNotAlmostEqual(tiles[1][1] / tiles[0][1], 2)

    def test_square_group_fits_portrait_safe_width(self):
        widths = [side for _, side in area_tiles()]
        total_width = sum(widths) + 3 * 0.3
        self.assertLess(total_width, 7.1)

    def test_index_product_property(self):
        self.assertTrue(equal_index_product(2, 2, 2, 5, 3, 4))
        self.assertTrue(equal_index_product(3, -2, 2, 5, 3, 4))
        with self.assertRaises(ValueError):
            equal_index_product(2, 2, 2, 5, 1, 3)

    def test_rejects_zero_terms_and_invalid_indices(self):
        with self.assertRaises(ValueError):
            term(0, 2, 1)
        with self.assertRaises(ValueError):
            term(2, 0, 1)
        for bad in (0, -1, 1.5, True):
            with self.subTest(index=bad), self.assertRaises(ValueError):
                finite_sum(2, 2, bad)
        with self.assertRaises(ValueError):
            area_tiles(ratio=-2)


if __name__ == "__main__":
    unittest.main()
