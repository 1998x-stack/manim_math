"""006 有理数加法：纯数学及 AST 回归，不依赖 Manim。"""
import ast
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE = (Path(__file__).parent / "rational_number_addition.py").read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)
METHODS = [node for node in TREE.body if isinstance(node, ast.FunctionDef) and
           node.name in {"addition_path", "addition_kind"}]
ENV = {"Fraction": Fraction}
exec(compile(ast.Module(body=METHODS, type_ignores=[]), "addition-model", "exec"), ENV)
path, kind = ENV["addition_path"], ENV["addition_kind"]


class AdditionContract(unittest.TestCase):
    def test_same_sign(self):
        self.assertEqual(path(3, 2), (0, 3, 5))
        self.assertEqual(path(-2, -3), (0, -2, -5))
        self.assertEqual(kind(3, 2), "same")
        self.assertEqual(kind(-2, -3), "same")

    def test_different_sign(self):
        self.assertEqual(path(5, -2), (0, 5, 3))
        self.assertEqual(path(-5, 2), (0, -5, -3))
        self.assertEqual(kind(5, -2), "different")
        self.assertEqual(kind(-5, 2), "different")

    def test_zero_and_cancellation(self):
        self.assertEqual(path(3, 0), (0, 3, 3))
        self.assertEqual(path(0, -3), (0, 0, -3))
        self.assertEqual(path(3, -3), (0, 3, 0))
        self.assertEqual(kind(3, -3), "cancel")
        self.assertEqual(kind(0, 0), "zero")
        self.assertEqual(kind(3, 0), "zero")

    def test_fraction_precision_and_commutativity(self):
        for a, b in [(Fraction(1, 3), Fraction(1, 6)),
                     (Fraction(-2, 3), Fraction(1, 3)),
                     (-0.5, 1.5), (-2, 3)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(path(a, b)[2], path(b, a)[2])
                self.assertEqual(path(a, b)[2], Fraction(str(a)) + Fraction(str(b)))

    def test_scene_and_shared_number_line(self):
        scenes = [node for node in TREE.body if isinstance(node, ast.ClassDef)
                  and node.name == "RationalNumberAddition"]
        self.assertEqual(len(scenes), 1)
        self.assertIn("self.number_line.n2p(float(result))", SOURCE)
        self.assertIn("if right != 0:", SOURCE)
        self.assertNotIn("Flash(result_dot", SOURCE)
        self.assertIn("config.frame_height = 16", SOURCE)


if __name__ == "__main__":
    unittest.main()
