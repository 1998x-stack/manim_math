"""同类二次根式：独立数学、边界与 Scene 入口回归，不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("like_radicals.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"normalized_term", "collect_like_terms"}
PURE_NODES = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
              and node.name in NAMES]
NS = {"math": math}
exec(compile(ast.Module(body=PURE_NODES, type_ignores=[]), str(SOURCE), "exec"), NS)


class LikeRadicalsTests(unittest.TestCase):
    def test_both_helpers_present(self):
        self.assertEqual({node.name for node in PURE_NODES}, NAMES)

    def test_normalization_preserves_value_and_removes_square_factors(self):
        normal = NS["normalized_term"]
        for radicand in range(101):
            for coefficient in (-3, -1, 0, 1, 2, 5):
                with self.subTest(n=radicand, c=coefficient):
                    outside, inside = normal(coefficient, radicand)
                    self.assertEqual(outside * outside * inside,
                                     coefficient * coefficient * radicand)
                    self.assertGreaterEqual(inside, 1)
                    self.assertFalse(any(inside % (k * k) == 0
                                         for k in range(2, math.isqrt(inside) + 1)))
                    if coefficient < 0 and radicand > 0:
                        self.assertLess(outside, 0)
                    if coefficient == 0 or radicand == 0:
                        self.assertEqual(outside, 0)

    def test_lesson_examples(self):
        normal = NS["normalized_term"]
        group = NS["collect_like_terms"]
        self.assertEqual(normal(1, 12), (2, 3))
        self.assertEqual(normal(1, 8), (2, 2))
        self.assertEqual(group(((2, 3), (5, 3))), {3: 7})
        self.assertEqual(group(((1, 12), (1, 3))), {3: 3})
        self.assertEqual(group(((1, 8), (1, 2))), {2: 3})
        self.assertEqual(group(((4, 6), (-1, 6))), {6: 3})
        self.assertEqual(group(((1, 2), (1, 3))), {2: 1, 3: 1})
        self.assertEqual(group(((1, 3), (-1, 7))), {3: 1, 7: -1})

    def test_zero_and_cancellation(self):
        group = NS["collect_like_terms"]
        self.assertEqual(group(((1, 3), (-1, 3))), {})
        self.assertEqual(group(((0, 3), (5, 0))), {})
        self.assertEqual(group(((2, 12), (-4, 3))), {})

    def test_invalid_radicands_and_coefficients(self):
        for coeff, radicand in ((1, -1), (1.0, 3), (1, 3.0), (True, 3), (1, None)):
            with self.subTest(coeff=coeff, radicand=radicand):
                with self.assertRaises(ValueError):
                    NS["normalized_term"](coeff, radicand)

    def test_ten_scene_methods_and_portrait_contract(self):
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "LikeRadicals")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"scene_opening", "scene_definition", "scene_check_method",
                         "scene_merge_rule", "scene_example_basic",
                         "scene_example_advanced", "scene_counter_example",
                         "scene_quick_judge", "scene_summary", "scene_outro"}.issubset(methods))
        content = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", content)
        self.assertIn("config.frame_height = 16", content)


if __name__ == "__main__":
    unittest.main()
