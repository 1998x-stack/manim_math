"""Pure-math regression tests for two grade-one scenes.

AST extracts only the named, Manim-free helpers from each real scene file. This
avoids importing Manim or mutating its global render configuration in unit tests.
Run: python -m unittest discover -s tests -p 'test_grade_one_math.py' -v
"""

import ast
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
COUNTING = ROOT / "小学/一年级/上册/第一章-10以内数的认识/001数一数/counting_animation.py"
CHART = ROOT / "小学/一年级/下册/第二章-100以内数的认识/003百数表/003_百数表.py"


def load_pure_helpers(path, names):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    assert {node.name for node in functions} == set(names), "helper missing from scene source"
    namespace = {"math": math}
    module = ast.Module(body=functions, type_ignores=[])
    exec(compile(ast.fix_missing_locations(module), str(path), "exec"), namespace)
    return namespace


class CountingMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        helpers = load_pure_helpers(COUNTING, {"count_labels", "star_vertices"})
        cls.count_labels = staticmethod(helpers["count_labels"])
        cls.star_vertices = staticmethod(helpers["star_vertices"])

    def test_one_to_one_labels(self):
        self.assertEqual(self.count_labels(0), ())
        self.assertEqual(self.count_labels(5), (1, 2, 3, 4, 5))
        self.assertEqual(self.count_labels(6), (1, 2, 3, 4, 5, 6))
        self.assertEqual(self.count_labels(10)[-1], 10)
        for invalid in (-1, 11, 1.5, True):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                self.count_labels(invalid)

    def test_star_vertex_order_and_radius(self):
        vertices = self.star_vertices(1.0, 0.4)
        self.assertEqual(len(vertices), 10)
        for index, (x, y, z) in enumerate(vertices):
            radius = math.hypot(x, y)
            self.assertAlmostEqual(radius, 1.0 if index % 2 == 0 else 0.4)
            self.assertAlmostEqual(z, 0.0)
            expected_angle = -math.pi / 2 + index * math.pi / 5
            self.assertAlmostEqual(x, radius * math.cos(expected_angle))
            self.assertAlmostEqual(y, radius * math.sin(expected_angle))
        self.assertEqual(len(set(vertices)), 10)

    def test_star_rejects_invalid_radius(self):
        for outer, inner in ((0, 0.1), (1, 0), (1, 1), (1, 2)):
            with self.subTest(radii=(outer, inner)), self.assertRaises(ValueError):
                self.star_vertices(outer, inner)


class HundredChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        helpers = load_pure_helpers(
            CHART, {"chart_number", "row_numbers", "column_numbers", "diagonal_numbers"}
        )
        for name, function in helpers.items():
            if name in {"chart_number", "row_numbers", "column_numbers", "diagonal_numbers"}:
                setattr(cls, name, staticmethod(function))

    def test_chart_is_exactly_1_through_100(self):
        values = [self.chart_number(r, c) for r in range(10) for c in range(10)]
        self.assertEqual(values, list(range(1, 101)))
        for r, c in ((-1, 0), (0, 10), (True, 0), (0, 2.5)):
            with self.subTest(index=(r, c)), self.assertRaises(ValueError):
                self.chart_number(r, c)

    def test_rows_increase_by_one_even_at_tens_boundary(self):
        for row in range(10):
            values = self.row_numbers(row)
            self.assertEqual(len(values), 10)
            self.assertTrue(all(b - a == 1 for a, b in zip(values, values[1:])))
        self.assertEqual(self.row_numbers(1), tuple(range(11, 21)))
        self.assertEqual(self.row_numbers(4), tuple(range(41, 51)))
        self.assertNotEqual(self.row_numbers(4)[8] // 10, self.row_numbers(4)[9] // 10)

    def test_columns_and_down_right_diagonals(self):
        for col in range(10):
            values = self.column_numbers(col)
            self.assertTrue(all(b - a == 10 for a, b in zip(values, values[1:])))
            self.assertEqual(len({value % 10 for value in values}), 1)
        self.assertEqual(self.column_numbers(9), tuple(range(10, 101, 10)))
        self.assertEqual(self.diagonal_numbers(), tuple(range(1, 101, 11)))
        self.assertEqual(self.diagonal_numbers(1), tuple(range(2, 91, 11)))
        for invalid in (-1, 10, 1.2, True):
            with self.subTest(start_col=invalid), self.assertRaises(ValueError):
                self.diagonal_numbers(invalid)


if __name__ == "__main__":
    unittest.main()
