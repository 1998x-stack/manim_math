"""最简二次根式的纯数学回归；不安装或导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("simplest_radical.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
HELPERS = {"simplify_integer_radicand", "square_factor_root", "quotient_root"}
PURE_NODES = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
              and node.name in HELPERS]
NS = {"math": math}
exec(compile(ast.Module(body=PURE_NODES, type_ignores=[]), str(SOURCE), "exec"), NS)


class SimplestRadicalTests(unittest.TestCase):
    def test_pure_helpers_present(self):
        self.assertEqual({node.name for node in PURE_NODES}, HELPERS)

    def test_simplifying_integer_roots_preserves_value_and_squarefree_remainder(self):
        simplify = NS["simplify_integer_radicand"]
        for n in range(101):
            with self.subTest(radicand=n):
                outside, inside = simplify(n)
                self.assertEqual(outside * outside * inside, n)
                self.assertGreaterEqual(outside, 0)
                self.assertGreaterEqual(inside, 1)
                self.assertFalse(any(inside % (k * k) == 0
                                     for k in range(2, math.isqrt(inside) + 1)))

    def test_specific_lesson_examples(self):
        simplify = NS["simplify_integer_radicand"]
        self.assertEqual(simplify(0), (0, 1))
        self.assertEqual(simplify(3), (1, 3))
        self.assertEqual(simplify(8), (2, 2))
        self.assertEqual(simplify(12), (2, 3))
        self.assertEqual(simplify(72), (6, 2))

    def test_invalid_integer_inputs(self):
        for value in (-1, 2.5, True, "12", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    NS["simplify_integer_radicand"](value)

    def test_symbolic_square_factor_all_signs(self):
        calc = NS["square_factor_root"]
        for a in (-5, -3, -0.5, 0, 0.5, 3, 5):
            for b in (0, 1, 3, 9):
                with self.subTest(a=a, b=b):
                    self.assertTrue(math.isclose(calc(a, b), math.sqrt(a * a * b),
                                                 rel_tol=1e-12, abs_tol=1e-12))
        self.assertEqual(calc(-3, 1), 3)
        self.assertNotEqual(calc(-3, 1), -3)
        self.assertTrue(math.isclose(calc(-2, 3), 2 * math.sqrt(3)))

    def test_symbolic_invalid_radicand(self):
        for a, b in ((1, -1), (float("nan"), 2), (2, float("inf"))):
            with self.assertRaises(ValueError):
                NS["square_factor_root"](a, b)

    def test_quotient_rule_domain_and_examples(self):
        calc = NS["quotient_root"]
        self.assertTrue(math.isclose(calc(3, 4), math.sqrt(3) / 2))
        self.assertEqual(calc(0, 1), 0)
        self.assertTrue(math.isclose(calc(2, 3), math.sqrt(2) / math.sqrt(3)))
        for a, b in ((-1, 1), (1, 0), (0, -1), (float("inf"), 1)):
            with self.assertRaises(ValueError):
                calc(a, b)

    def test_scene_identity_and_nine_sections(self):
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "SimplestRadical")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"scene_opening", "scene_two_conditions", "scene_method",
                         "scene_example1", "scene_example2", "scene_example3",
                         "scene_judge", "scene_summary", "scene_outro"}.issubset(methods))
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)


if __name__ == "__main__":
    unittest.main()
