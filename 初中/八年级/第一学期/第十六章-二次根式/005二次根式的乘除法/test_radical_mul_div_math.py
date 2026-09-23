"""二次根式乘除法数学回归：使用 AST 抽取纯函数，不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("radical_mul_div.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"root_product", "root_quotient", "rationalize"}
NODES = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
         and node.name in NAMES]
NS = {"math": math}
exec(compile(ast.Module(body=NODES, type_ignores=[]), str(SOURCE), "exec"), NS)


class RadicalMulDivTests(unittest.TestCase):
    def test_pure_helpers_present(self):
        self.assertEqual({node.name for node in NODES}, NAMES)

    def test_multiplication_positive_and_zero(self):
        calc = NS["root_product"]
        for a in (0, 0.25, 2, 3, 5, 9):
            for b in (0, 0.25, 2, 3, 5, 8):
                with self.subTest(a=a, b=b):
                    self.assertTrue(math.isclose(calc(a, b), math.sqrt(a * b),
                                                 rel_tol=1e-12, abs_tol=1e-12))
        self.assertEqual(calc(2, 8), 4)
        self.assertTrue(math.isclose(calc(3, 5), math.sqrt(15)))

    def test_multiplication_invalid_domain(self):
        for a, b in ((-1, 1), (1, -1), (float("nan"), 2), (2, float("inf"))):
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    NS["root_product"](a, b)

    def test_division_boundary_and_positive_denominator(self):
        calc = NS["root_quotient"]
        for a in (0, 0.25, 2, 12):
            for b in (0.25, 1, 3, 12):
                with self.subTest(a=a, b=b):
                    self.assertTrue(math.isclose(calc(a, b), math.sqrt(a / b),
                                                 rel_tol=1e-12, abs_tol=1e-12))
        self.assertEqual(calc(12, 3), 2)

    def test_division_invalid_domain(self):
        for a, b in ((-1, 2), (0, 0), (5, 0), (5, -2), (float("inf"), 2)):
            with self.assertRaises(ValueError):
                NS["root_quotient"](a, b)

    def test_rationalization_equivalence_and_domain(self):
        calc = NS["rationalize"]
        for numerator in (-6, -1, 0, 1, 6):
            for radicand in (0.25, 1, 3, 9):
                with self.subTest(n=numerator, a=radicand):
                    self.assertTrue(math.isclose(calc(numerator, radicand),
                                                 numerator / math.sqrt(radicand),
                                                 rel_tol=1e-12, abs_tol=1e-12))
        self.assertTrue(math.isclose(calc(6, 3), 2 * math.sqrt(3)))
        for numerator, radicand in ((1, 0), (1, -1), (1, float("nan")),
                                    (float("inf"), 2)):
            with self.assertRaises(ValueError):
                calc(numerator, radicand)

    def test_geometric_ratio_and_scene_contract(self):
        self.assertTrue(math.isclose(3.8 / 1.9, math.sqrt(8) / math.sqrt(2)))
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "RadicalMultDiv")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"scene_opening", "scene_mul_formula", "scene_mul_ex1",
                         "scene_mul_ex2", "scene_div_formula", "scene_div_ex1",
                         "scene_rationalize_intro", "scene_rationalize_ex",
                         "scene_quick_practice", "scene_summary", "scene_outro"}.issubset(methods))
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", text)
        self.assertIn("config.frame_height = 16", text)


if __name__ == "__main__":
    unittest.main()
