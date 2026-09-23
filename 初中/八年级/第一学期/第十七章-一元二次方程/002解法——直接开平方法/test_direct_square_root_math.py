"""直接开平方法：纯数学回归，不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("direct_square_root.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
HELPERS = {"solve_shifted_square", "equation_residual"}
PURE = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
        and node.name in HELPERS]
NS = {"math": math}
exec(compile(ast.Module(body=PURE, type_ignores=[]), str(SOURCE), "exec"), NS)


class DirectSquareRootMathTests(unittest.TestCase):
    def test_pure_math_helpers_exist(self):
        self.assertEqual({node.name for node in PURE}, HELPERS)

    def test_positive_rhs_has_two_distinct_real_roots(self):
        solve, residual = NS["solve_shifted_square"], NS["equation_residual"]
        for m in (-7, -2, 0, 2, 3, 7):
            for n in (0.25, 1, 9, 16, 25):
                with self.subTest(m=m, n=n):
                    roots = solve(m, n)
                    self.assertEqual(len(roots), 2)
                    self.assertLess(roots[0], roots[1])
                    self.assertTrue(all(math.isclose(residual(x, m, n), 0,
                                                         rel_tol=1e-12, abs_tol=1e-12)
                                        for x in roots))
                    self.assertTrue(math.isclose(roots[0] + roots[1], -2 * m,
                                                 rel_tol=1e-12, abs_tol=1e-12))

    def test_zero_has_one_distinct_root(self):
        for m in (-3, 0, 2, 5):
            with self.subTest(m=m):
                self.assertEqual(NS["solve_shifted_square"](m, 0), (-m,))
                self.assertEqual(NS["equation_residual"](-m, m, 0), 0)

    def test_negative_rhs_has_no_real_roots(self):
        for m, n in ((0, -1), (2, -4), (-3, -9), (4, -0.01)):
            self.assertEqual(NS["solve_shifted_square"](m, n), ())

    def test_lesson_examples(self):
        solve = NS["solve_shifted_square"]
        self.assertEqual(solve(0, 9), (-3, 3))
        self.assertEqual(solve(2, 16), (-6, 2))
        self.assertEqual(solve(3, 25), (-8, 2))
        self.assertTrue(all(x*x + 6*x + 9 == 25 for x in solve(3, 25)))

    def test_invalid_inputs(self):
        for m, n in ((float("nan"), 4), (0, float("inf")),
                     (-float("inf"), 2), (0, float("nan"))):
            with self.assertRaises(ValueError):
                NS["solve_shifted_square"](m, n)

    def test_scene_and_cjk_tex_contract(self):
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "DirectSquareRootMethod")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_method_introduction", "show_basic_derivation",
                         "show_general_formula", "show_example_1", "show_example_2",
                         "show_summary"}.issubset(methods))
        for node in ast.walk(TREE):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "MathTex":
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any('\u4e00' <= ch <= '\u9fff' for ch in arg.value),
                                         f"Chinese text must be Text, not MathTex: {arg.value!r}")
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", text)
        self.assertIn("config.frame_height = 16", text)


if __name__ == "__main__":
    unittest.main()
