"""纯 Python 回归，不导入 Manim；独立验证绝对值数学和源码契约。"""
import ast
import unittest
from fractions import Fraction
from pathlib import Path

SOURCE = (Path(__file__).parent / "absolute_value.py").read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)
MODEL = next(node for node in TREE.body if isinstance(node, ast.FunctionDef)
             and node.name == "absolute_distance")
ENV = {}
exec(compile(ast.Module(body=[MODEL], type_ignores=[]), "absolute_distance", "exec"), ENV)
distance = ENV["absolute_distance"]


class AbsoluteValueContract(unittest.TestCase):
    def test_zero_and_nonnegative(self):
        self.assertEqual(distance(0), 0)
        for n in [-5, -3, -0.1, 0, 2.5, 10]:
            self.assertGreaterEqual(distance(n), 0)

    def test_opposites_and_distance(self):
        for n in [0, 1, 3, 4, 2.5, Fraction(1, 2)]:
            with self.subTest(n=n):
                self.assertAlmostEqual(distance(n), distance(-n))
                self.assertAlmostEqual(distance(n), abs(float(n)) * distance(1))

    def test_unit_length_and_invalid_units(self):
        self.assertEqual(distance(3, 2), 6)
        for invalid in (0, -0.5):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                distance(3, invalid)

    def test_scene_and_no_silent_geometry_success(self):
        scenes = [node for node in TREE.body if isinstance(node, ast.ClassDef)
                  and node.name == "AbsoluteValueConcept"]
        self.assertEqual(len(scenes), 1)
        self.assertIn("self.axis.n2p(value)", SOURCE)
        self.assertNotIn("print(\"✓ 几何验证通过\")", SOURCE)
        self.assertNotIn("always_redraw", SOURCE)

    def test_summary_cards_have_real_destination(self):
        self.assertIn("target = card.get_center().copy()", SOURCE)
        self.assertIn("card.animate.move_to(target)", SOURCE)
        self.assertNotIn("shift(RIGHT * 0)", SOURCE)


if __name__ == "__main__":
    unittest.main()
