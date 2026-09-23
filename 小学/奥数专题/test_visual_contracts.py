"""Geometry/data checks for eight visual lessons; extract math functions without importing Manim.

Run: python 小学/奥数专题/test_visual_contracts.py
This proves model invariants, NOT rendered Mobject bounds, font quality or animation behavior.
"""
import ast
from fractions import Fraction
from itertools import combinations
from math import comb, hypot
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
PATHS = {
    "gauss": "01-计算与巧算/001-高斯求和/lesson.py",
    "animals": "02-典型应用题/002-鸡兔同笼/lesson.py",
    "fraction": "03-分数与数形结合/003-分数乘法面积模型/lesson.py",
    "triangle": "04-平面几何/004-等底等高/lesson.py",
    "butterfly": "04-平面几何/005-蝴蝶模型/lesson.py",
    "encounter": "05-行程问题/006-相遇问题/lesson.py",
    "venn": "06-集合与计数/007-容斥原理/lesson.py",
    "paths": "06-集合与计数/008-方格最短路径/lesson.py",
}


def isolated_model(key, name):
    path = ROOT / PATHS[key]
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    matches = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one function {name} in {path}")
    namespace = {"Fraction": Fraction, "combinations": combinations, "comb": comb}
    exec(compile(ast.Module(body=matches, type_ignores=[]), str(path), "exec"), namespace)
    return namespace[name]


def polygon_area(vertices):
    return abs(sum(x1*y2 - x2*y1 for (x1, y1), (x2, y2)
                   in zip(vertices, vertices[1:] + vertices[:1]))) / 2


class VisualContractsTest(unittest.TestCase):
    def test_eight_sources_have_real_scene_entrypoints(self):
        expected = {"gauss": "GaussPairingScene", "animals": "ChickenRabbitScene",
                    "fraction": "FractionAreaScene", "triangle": "EqualBaseHeightScene",
                    "butterfly": "ButterflyAreaScene", "encounter": "EncounterScene",
                    "venn": "InclusionExclusionScene", "paths": "GridPathScene"}
        for key, path in PATHS.items():
            with self.subTest(scene=key):
                syntax = ast.parse((ROOT / path).read_text(encoding="utf-8"))
                names = [node.name for node in syntax.body if isinstance(node, ast.ClassDef)]
                self.assertIn(expected[key], names)
                cls = next(node for node in syntax.body if isinstance(node, ast.ClassDef)
                           and node.name == expected[key])
                self.assertTrue(any(isinstance(node, ast.FunctionDef) and node.name == "construct"
                                    for node in cls.body))

    def test_gauss_triangle_and_complement_make_exact_rectangle(self):
        sigma = isolated_model("gauss", "arithmetic_sum")
        for n in (1, 2, 10, 99, 100):
            self.assertEqual(sum(range(1, n+1)), sigma(n))
        first = {(r, c) for r in range(10) for c in range(11) if c <= r}
        other = {(r, c) for r in range(10) for c in range(11) if c > r}
        self.assertEqual((len(first), len(other), len(first | other)), (55, 55, 110))
        self.assertFalse(first & other)
        self.assertEqual({i + (101-i) for i in range(1, 51)}, {101})

    def test_chicken_rabbit_each_step_has_exact_visible_leg_count(self):
        solve = isolated_model("animals", "solve_chicken_rabbit")
        for rabbits in range(9):
            chickens = 8-rabbits
            legs = 2*chickens+4*rabbits
            self.assertEqual(solve(8, legs), (chickens, rabbits))
            self.assertEqual(legs, 16+2*rabbits)
        self.assertEqual([16+2*i for i in range(4)], [16, 18, 20, 22])

    def test_fraction_grid_has_precisely_six_intersection_cells(self):
        product = isolated_model("fraction", "area_product")
        cols = {(r, c) for r in range(3) for c in range(3)}
        rows = {(r, c) for r in range(2) for c in range(4)}
        self.assertEqual((len(cols), len(rows), len(cols & rows)), (9, 8, 6))
        self.assertEqual(product(3, 4, 2, 3), Fraction(len(cols & rows), 12))
        for c in range(5):
            for r in range(4):
                self.assertEqual(product(c, 4, r, 3), Fraction(c*r, 12))

    def test_equal_base_height_for_every_key_apex_position(self):
        area = isolated_model("triangle", "triangle_area")
        a, b = (-2, Fraction(-3, 2)), (2, Fraction(-3, 2))
        for x in (-2, -1, 0, Fraction(1, 4), 2):
            self.assertEqual(polygon_area([a, b, (x, Fraction(3, 2))]), 6)
            self.assertEqual(area(4, 3), 6)
        self.assertEqual(polygon_area([a, b, (2, Fraction(3, 2)), (-2, Fraction(3, 2))]), 12)

    def test_butterfly_intersection_and_all_four_polygon_areas(self):
        model = isolated_model("butterfly", "butterfly_areas")
        for top, bottom, height in ((3, 6, 4), (6, 3, 4), (2, 5, 7)):
            a, b = (-Fraction(top, 2), Fraction(height, 2)), (Fraction(top, 2), Fraction(height, 2))
            c, d = (Fraction(bottom, 2), -Fraction(height, 2)), (-Fraction(bottom, 2), -Fraction(height, 2))
            f = Fraction(top, top+bottom)
            o = (a[0]+f*(c[0]-a[0]), a[1]+f*(c[1]-a[1]))
            self.assertEqual(o, (b[0]+f*(d[0]-b[0]), b[1]+f*(d[1]-b[1])))
            four = (polygon_area([a, b, o]), polygon_area([a, o, d]),
                    polygon_area([b, c, o]), polygon_area([c, d, o]))
            small, side, large = model(top, bottom, height)
            self.assertEqual(four, (small, side, side, large))
            self.assertEqual(sum(four), Fraction((top+bottom)*height, 2))
            self.assertEqual(small*large, side*side)

    def test_encounter_segment_endpoints_and_remaining_distance(self):
        model = isolated_model("encounter", "encounter_time")
        self.assertEqual(model(200, 60, 40), 2)
        scale = Fraction(6, 200)
        for t in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)):
            xa, xb = -3+60*t*scale, 3-40*t*scale
            self.assertEqual((xb-xa)/scale, 200-100*t)
            self.assertGreaterEqual(xb, xa)
        self.assertEqual(-3+60*2*scale, 3-40*2*scale)

    def test_venn_points_really_lie_in_appropriate_regions(self):
        left = [(-2.48, y) for y in (-.49, .19, .87, 1.55)] + [(-1.81, y) for y in (-.49, .19, .87, 1.55)]
        common = [(-.34, .25), (.34, .25), (-.34, .98), (.34, .98)]
        right = [(x, y) for x in (1.78, 2.44) for y in (-.36, .40, 1.16)]
        self.assertEqual((len(left), len(common), len(right)), (8, 4, 6))
        for points, memberships in ((left, (True, False)), (common, (True, True)),
                                    (right, (False, True))):
            for x, y in points:
                self.assertEqual((hypot(x+1.25, y-.67) < 2,
                                  hypot(x-1.25, y-.67) < 2), memberships)
        self.assertEqual(len(set(left+common+right)), 18)

    def test_ten_grid_routes_have_unique_five_step_geometries(self):
        routes = isolated_model("paths", "shortest_routes")(3, 2)
        table = isolated_model("paths", "path_table")(3, 2)
        self.assertEqual(len(routes), table[2][3])
        self.assertEqual(len({tuple(route) for route in routes}), 10)
        for route in routes:
            self.assertEqual((route[0], route[-1], len(route)), ((0, 0), (3, 2), 6))
            self.assertEqual(sorted((x2-x1, y2-y1) for (x1, y1), (x2, y2)
                                    in zip(route, route[1:])), [(0, 1)]*2 + [(1, 0)]*3)


if __name__ == "__main__":
    unittest.main()
