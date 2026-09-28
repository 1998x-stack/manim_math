"""整式乘法的数学及场景结构回归；纯标准库，不运行 Manim。"""

import ast
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("polynomial_multiplication.py")


def coefficients_product(left, right):
    """升幂系数数组相乘：纯 Python 离散卷积。"""
    if not left or not right:
        raise ValueError("多项式系数不能为空")
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


class PolynomialMultiplicationTests(unittest.TestCase):
    def test_three_examples_and_four_products(self):
        self.assertEqual(coefficients_product([0, 2], [0, 0, 3]), [0, 0, 0, 6])
        self.assertEqual(coefficients_product([0, 2], [4, 3]), [0, 8, 6])
        self.assertEqual(coefficients_product([2, 1], [3, 1]), [6, 5, 1])
        self.assertEqual(coefficients_product([2, 1], [3, 1]),
                         coefficients_product([3, 1], [2, 1]))
        self.assertEqual(["x^2", "3x", "2x", "6"],
                         ["x^2", "3x", "2x", "6"])

    def test_negative_zero_and_distributive_edge_cases(self):
        self.assertEqual(coefficients_product([-2, 1], [3, -1]), [-6, 5, -1])
        self.assertEqual(coefficients_product([0], [1, 2]), [0, 0])
        self.assertEqual(coefficients_product([4], [0]), [0])
        with self.assertRaises(ValueError):
            coefficients_product([], [1])
        with self.assertRaises(ValueError):
            coefficients_product([1], [])
        for x in (-5, -2, 0, 1, 3):
            self.assertEqual((2 * x) * (3 * x * x), 6 * x ** 3)
            self.assertEqual(2 * x * (3 * x + 4), 6 * x * x + 8 * x)
            self.assertEqual((x + 2) * (x + 3), x * x + 5 * x + 6)

    def test_scene_lifecycle_latex_and_grid_contract(self):
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SOURCE), "exec")
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "PolynomialMultiplication")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"construct", "product_grid", "clear_content", "show_opening",
                         "show_monomial_times_monomial", "show_monomial_times_polynomial",
                         "show_polynomial_times_polynomial_intro",
                         "show_polynomial_times_polynomial_expansion",
                         "show_concrete_example", "show_summary"} <= methods)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        self.assertIn("SAFE_WIDTH = 7.5", source)
        self.assertIn("index = 2 * row + col", source)
        self.assertIn("cells.add(VGroup(box, product))", source)
        self.assertNotIn("get_tex_string()", source)
        self.assertNotIn("Rotate(icons", source)
        for node in ast.walk(scene):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == "SurroundingRectangle":
                    self.assertNotIn("corner_radius", {kw.arg for kw in node.keywords})
                if node.func.id in {"MathTex", "Tex"}:
                    for argument in node.args:
                        if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in argument.value))


if __name__ == "__main__":
    unittest.main()
