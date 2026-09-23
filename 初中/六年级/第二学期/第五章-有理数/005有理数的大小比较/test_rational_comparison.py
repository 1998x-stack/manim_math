"""不导入 Manim 的有理数大小比较专项回归。"""
import ast
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE = (Path(__file__).parent / "005_有理数的大小比较.py").read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)
MODEL = next(node for node in TREE.body if isinstance(node, ast.FunctionDef)
             and node.name == "compare_rationals")
ENV = {"Fraction": Fraction}
exec(compile(ast.Module(body=[MODEL], type_ignores=[]), "compare_rationals", "exec"), ENV)
compare = ENV["compare_rationals"]


class ComparisonContract(unittest.TestCase):
    def test_negative_zero_positive(self):
        self.assertEqual(compare(-2, 0), -1)
        self.assertEqual(compare(0, 1), -1)
        self.assertEqual(compare(1, -3), 1)

    def test_positive_and_negative_same_sign(self):
        self.assertEqual(compare(1, 3), -1)
        self.assertEqual(compare(-3, -1), -1)
        self.assertEqual(compare(-1, -3), 1)

    def test_fraction_decimal_equivalence(self):
        self.assertEqual(compare(Fraction(1, 2), 0.5), 0)
        self.assertEqual(compare(Fraction(1, 2), Fraction(3, 2)), -1)
        self.assertEqual(compare(-0.8, Fraction(-3, 4)), -1)

    def test_irreflexive_and_symmetry(self):
        for number in [-3, -1, 0, 0.5, 2]:
            self.assertEqual(compare(number, number), 0)
        for a, b in [(-3, 2), (3, 1), (Fraction(1, 2), -1)]:
            self.assertEqual(compare(a, b), -compare(b, a))

    def test_scene_and_all_rule_branches(self):
        scenes = [node for node in TREE.body if isinstance(node, ast.ClassDef)
                  and node.name == "有理数的大小比较Animation"]
        self.assertEqual(len(scenes), 1)
        self.assertIn("config.frame_width = 9", SOURCE)
        self.assertIn("config.frame_height = 16", SOURCE)
        self.assertIn("axis.n2p(left)", SOURCE)
        self.assertIn("axis.n2p(right)", SOURCE)
        self.assertIn("两个负数：绝对值大的数反而更小", SOURCE)


if __name__ == "__main__":
    unittest.main()
