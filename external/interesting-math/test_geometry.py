"""独立几何不变量测试；只提取 scene.py 的数学函数，不导入 Manim。

python -m unittest discover -s external/interesting-math -p 'test_*.py' -v
"""
import math
import unittest

from test_math import functions


def polygon_area(points):
    return abs(sum(a.real * points[(i+1) % len(points)].imag
                   - points[(i+1) % len(points)].real * a.imag
                   for i, a in enumerate(points)) / 2)


def triangle_area(triangle):
    a, b, c = triangle
    return abs(((b-a).conjugate()*(c-a)).imag) / 2


class GeometryConstructionTests(unittest.TestCase):
    def test_odd_layers_are_exact_disjoint_square_borders(self):
        (layer,) = functions("odd-squares", "odd_layer")
        seen = set()
        for n in range(1, 21):
            current = set(layer(n))
            self.assertEqual(len(current), 2*n-1)
            self.assertFalse(current & seen)
            self.assertTrue(all(x == n-1 or y == n-1 for x, y in current))
            seen |= current
            self.assertEqual(seen, {(x, y) for x in range(n) for y in range(n)})

    def test_pascal_three_self_similar_triangles_exactly_match(self):
        (parity,) = functions("pascal-fractal", "parity_row")
        for power in range(1, 6):
            side = 2**power
            for offset in range(side):
                current = parity(side+offset)
                previous = parity(offset)
                self.assertEqual(current[:offset+1], previous)
                self.assertEqual(current[side:side+offset+1], previous)
                self.assertTrue(all(bit == 0 for bit in current[offset+1:side]))

    def test_complex_coordinate_projection_and_length(self):
        (rotate,) = functions("complex-rotation", "rotate_complex")
        for z in (complex(1.2, 0.5), 1+0j, -0.6-0.9j, 0j):
            for theta in (0, math.pi/6, math.pi/2, math.pi, 1.7*math.pi):
                point = rotate(z, theta)
                self.assertAlmostEqual(point.real,
                                       z.real*math.cos(theta)-z.imag*math.sin(theta),
                                       places=12)
                self.assertAlmostEqual(point.imag,
                                       z.real*math.sin(theta)+z.imag*math.cos(theta),
                                       places=12)
                self.assertAlmostEqual(point.real**2+point.imag**2,
                                       z.real**2+z.imag**2, places=12)

    def test_each_koch_bump_is_equilateral_and_adds_exact_area(self):
        triangle, step, added = functions(
            "koch-snowflake", "initial_triangle", "koch_step", "added_triangles")
        points = triangle()
        for generation in range(3):
            bumps = added(points)
            self.assertEqual(len(bumps), len(points))
            for k, (a, peak, b) in enumerate(bumps):
                original = abs(points[(k+1) % len(points)]-points[k])
                self.assertAlmostEqual(abs(peak-a), original/3, places=12)
                self.assertAlmostEqual(abs(b-peak), original/3, places=12)
                self.assertAlmostEqual(abs(b-a), original/3, places=12)
                self.assertAlmostEqual(triangle_area((a, peak, b)),
                                       math.sqrt(3)/4*(original/3)**2, places=12)
            next_points = step(points)
            self.assertAlmostEqual(polygon_area(next_points)-polygon_area(points),
                                   sum(triangle_area(bump) for bump in bumps),
                                   places=11)
            points = next_points
        with self.assertRaises(ValueError):
            added([0j, 1+0j])


if __name__ == "__main__":
    unittest.main()
