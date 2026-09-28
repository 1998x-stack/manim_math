"""无 Manim 依赖的源码/数学回归；不替代真实渲染与关键帧验收。"""

import ast
from fractions import Fraction
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).with_name("rational_numbers.py").read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)
SCENE = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
             and node.name == "RationalNumbers")


def method(name):
    return next(node for node in SCENE.body if isinstance(node, ast.FunctionDef)
                and node.name == name)


def assignment(function, variable):
    return next(node.value for node in ast.walk(function)
                if isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == variable
                        for target in node.targets))


def latex_fraction(value):
    match = re.fullmatch(r"(-?)\\frac\{(\d+)\}\{(\d+)\}", value)
    if match:
        return Fraction(-1 if match[1] else 1) * Fraction(int(match[2]), int(match[3]))
    return Fraction(value)


class RationalNumbersRegression(unittest.TestCase):
    def test_scene_and_seven_beats(self):
        called = [node.func.attr for node in ast.walk(method("construct"))
                  if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)]
        for name in ("show_opening", "show_definition", "show_classification_by_sign",
                     "show_classification_by_type", "show_decimal_representation",
                     "show_practice", "show_summary"):
            self.assertIn(name, called)

    def test_number_line_labels_match_values(self):
        cases = assignment(method("show_classification_by_sign"), "cases")
        points = [(ast.literal_eval(item.elts[0]), ast.literal_eval(item.elts[1]))
                  for item in cases.elts]
        self.assertEqual(len(points), 5)
        for value, label in points:
            self.assertEqual(Fraction(str(value)), latex_fraction(label))
        function = ast.get_source_segment(SOURCE, method("show_classification_by_sign"))
        self.assertIn("line.n2p(value)", function)
        self.assertIn("Dot(position", function)
        self.assertIn("text.move_to(position", function)
        self.assertIn("include_numbers=False", function)

    def test_practice_answers(self):
        function = method("show_practice")
        self.assertEqual(ast.literal_eval(assignment(function, "values")),
                         ["7", r"-\frac{3}{5}", r"0.\overline{6}", r"\sqrt{3}"])
        self.assertEqual(ast.literal_eval(assignment(function, "rational")),
                         [True, True, True, False])
        self.assertEqual(latex_fraction(r"-\frac{3}{5}"), Fraction(-3, 5))
        self.assertEqual(Fraction(2, 3), Fraction(6, 9))  # 0.\overline{6}

    def test_definition_examples(self):
        self.assertEqual(Fraction(3, 1), Fraction(3))
        self.assertEqual(Fraction(-5, 2), Fraction('-2.5'))
        self.assertEqual(Fraction(0, 1), Fraction(0))
        definition = ast.get_source_segment(SOURCE, method("show_definition"))
        self.assertIn(r"q\ne0", definition)

    def test_no_nested_play_or_chinese_in_mathtex(self):
        for node in ast.walk(TREE):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Attribute) and node.func.attr == "play":
                for arg in node.args:
                    self.assertFalse(isinstance(arg, ast.Call)
                                     and isinstance(arg.func, ast.Attribute)
                                     and arg.func.attr == "play")
            if isinstance(node.func, ast.Name) and node.func.id == "MathTex":
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(re.search(r"[\u4e00-\u9fff]", arg.value))


if __name__ == "__main__":
    unittest.main()
