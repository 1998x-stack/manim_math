"""第 001 课专项回归；仅依赖 Python 标准库，无需安装 Manim。"""

import ast
from pathlib import Path
import unittest


SOURCE = Path(__file__).with_name("algebraic_expression.py")


def monomial_degree(*powers):
    if any(not isinstance(p, int) or p < 0 for p in powers):
        raise ValueError("整式中字母的指数必须是非负整数")
    return sum(powers)


def evaluate_monomial(coefficient, x, y, x_power, y_power):
    return coefficient * x**x_power * y**y_power


def evaluate_polynomial(x):
    return 2 * x * x + 3 * x - 1


class AlgebraLessonMathTests(unittest.TestCase):
    def test_monomial_examples(self):
        self.assertEqual(monomial_degree(2, 1), 3)
        self.assertEqual(monomial_degree(3, 1), 4)
        self.assertEqual(monomial_degree(1, 2, 3), 6)
        self.assertEqual(monomial_degree(0), 0)  # 非零常数单项式的次数为零
        with self.assertRaises(ValueError):
            monomial_degree(-1)
        with self.assertRaises(ValueError):
            monomial_degree(0.5)
        for x, y in ((0, 0), (1, 2), (-2, 3), (3, -1)):
            self.assertEqual(evaluate_monomial(3, x, y, 2, 1), 3 * x * x * y)

    def test_polynomial_three_terms_degree_two(self):
        self.assertEqual(max(monomial_degree(2), monomial_degree(1), monomial_degree(0)), 2)
        for x in (-5, -1, 0, 1, 4):
            self.assertEqual(evaluate_polynomial(x), sum((2 * x**2, 3 * x, -1)))
        self.assertEqual(evaluate_polynomial(0), -1)

    def test_scene_syntax_and_entrypoint(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
        lessons = [node for node in tree.body if isinstance(node, ast.ClassDef)
                   and node.name == "AlgebraicExpressionConcept"]
        self.assertEqual(len(lessons), 1)
        methods = {node.name for node in lessons[0].body if isinstance(node, ast.FunctionDef)}
        for required in ("construct", "show_opening", "show_algebraic_expression",
                         "show_monomial_definition", "show_monomial_properties",
                         "show_polynomial", "show_wholestyle_summary", "show_outro"):
            self.assertIn(required, methods)

    def test_no_known_manim_api_regressions(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        for call in (node for node in ast.walk(tree) if isinstance(node, ast.Call)):
            if isinstance(call.func, ast.Attribute):
                self.assertNotEqual(call.func.attr, "get_tex_string",
                                    "不能对 MathTex 子对象进行 get_tex_string 调用")
            if isinstance(call.func, ast.Name) and call.func.id == "SurroundingRectangle":
                self.assertNotIn("corner_radius", [kw.arg for kw in call.keywords],
                                 "圆角效果应使用 RoundedRectangle")
            if isinstance(call.func, ast.Name) and call.func.id == "MathTex":
                for argument in call.args:
                    if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                        self.assertFalse(any("\u4e00" <= c <= "\u9fff" or c == "\u00a0"
                                             for c in argument.value),
                                         "MathTex 不允许中文或不间断空格")


if __name__ == "__main__":
    unittest.main()
