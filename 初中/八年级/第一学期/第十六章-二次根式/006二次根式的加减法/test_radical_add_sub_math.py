"""根式加减法的独立数学回归；仅抽取纯 Python 函数，无需 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("radical_add_sub.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
PURE_NAMES = {"normalized_term", "add_subtract_radicals"}
NODES = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
         and node.name in PURE_NAMES]
NS = {"math": math}
exec(compile(ast.Module(body=NODES, type_ignores=[]), str(SOURCE), "exec"), NS)


class RadicalAddSubTests(unittest.TestCase):
    def test_pure_helpers_exist(self):
        self.assertEqual({node.name for node in NODES}, PURE_NAMES)

    def test_normalized_terms_preserve_sign_and_value(self):
        normalize = NS["normalized_term"]
        for n in range(101):
            for coefficient in (-5, -1, 0, 1, 3):
                with self.subTest(n=n, c=coefficient):
                    outside, inside = normalize(coefficient, n)
                    self.assertEqual(outside * outside * inside,
                                     coefficient * coefficient * n)
                    self.assertGreaterEqual(inside, 1)
                    if n and coefficient:
                        self.assertEqual(outside > 0, coefficient > 0)
                    self.assertFalse(any(inside % (k * k) == 0
                                         for k in range(2, math.isqrt(inside) + 1)))

    def test_all_original_lesson_examples(self):
        add = NS["add_subtract_radicals"]
        self.assertEqual(add(((2, 3), (3, 3))), {3: 5})
        self.assertEqual(add(((1, 8), (1, 18))), {2: 5})
        self.assertEqual(add(((1, 12), (-1, 3))), {3: 1})
        self.assertEqual(add(((1, 8), (1, 18), (-1, 2))), {2: 4})
        self.assertEqual(add(((3, 5), (2, 5))), {5: 5})
        self.assertEqual(add(((1, 50), (-1, 8))), {2: 3})
        self.assertEqual(add(((1, 12), (1, 27))), {3: 5})
        self.assertEqual(add(((1, 3), (1, 5))), {3: 1, 5: 1})

    def test_unlike_radicals_remain_separate(self):
        self.assertEqual(NS["add_subtract_radicals"](((1, 2), (1, 3))),
                         {2: 1, 3: 1})
        self.assertNotEqual(math.sqrt(2) + math.sqrt(3), math.sqrt(5))

    def test_zero_and_negative_coefficients(self):
        add = NS["add_subtract_radicals"]
        self.assertEqual(add(((1, 8), (-2, 2))), {})
        self.assertEqual(add(((3, 5), (-5, 5))), {5: -2})
        self.assertEqual(add(((2, 0), (0, 5))), {})
        self.assertEqual(add(()), {})

    def test_invalid_domain_and_types(self):
        for c, n in ((1, -2), (1.0, 2), (1, 2.0), (True, 2), (1, None)):
            with self.subTest(c=c, n=n):
                with self.assertRaises(ValueError):
                    NS["normalized_term"](c, n)

    def test_ten_real_scene_methods_and_portrait(self):
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "RadicalAddSub")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        expected = {"scene_opening", "scene_three_steps", "scene_ex1_direct",
                    "scene_ex2_main", "scene_ex3_subtract", "scene_ex4_mixed",
                    "scene_cannot_merge", "scene_quick_practice",
                    "scene_summary", "scene_outro"}
        self.assertTrue(expected.issubset(methods))
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", text)
        self.assertIn("config.frame_height = 16", text)


if __name__ == "__main__":
    unittest.main()
