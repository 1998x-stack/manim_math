"""配方法纯数学与比例几何回归，AST 提取函数，不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("completing_the_square.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
FUNCTIONS = {"complete_parameters", "complete_roots", "area_tiles"}
NODES = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in FUNCTIONS]
NS = {"math": math}
exec(compile(ast.Module(body=NODES, type_ignores=[]), str(SOURCE), "exec"), NS)


class CompletingSquareTests(unittest.TestCase):
    def test_all_independent_helpers(self):
        self.assertEqual({n.name for n in NODES}, FUNCTIONS)

    def test_both_equation_examples_with_substitution(self):
        params, solve = NS["complete_parameters"], NS["complete_roots"]
        self.assertEqual(params(1, 6, 5), (3, 4))
        self.assertEqual(solve(1, 6, 5), (-5, -1))
        self.assertEqual(params(2, -8, 3), (-2, 2.5))
        roots = solve(2, -8, 3)
        self.assertEqual(len(roots), 2)
        self.assertTrue(all(math.isclose(2*x*x - 8*x + 3, 0, abs_tol=1e-12)
                            for x in roots))

    def test_root_count_positive_zero_negative_and_signs(self):
        solve = NS["complete_roots"]
        self.assertEqual(solve(1, 0, -9), (-3, 3))
        self.assertEqual(solve(1, -4, 4), (2,))
        self.assertEqual(solve(1, 0, 1), ())
        self.assertEqual(solve(-1, 0, 1), (-1, 1))
        for a, b, c in ((1, 6, 5), (2, -8, 3), (-1, 0, 1), (1, -4, 4)):
            for x in solve(a, b, c):
                with self.subTest(a=a, b=b, c=c, x=x):
                    self.assertTrue(math.isclose(a*x*x+b*x+c, 0, abs_tol=1e-12))

    def test_nonquadratic_and_nonfinite_inputs(self):
        for a, b, c in ((0, 1, 1), (float("nan"), 0, 1),
                        (1, float("inf"), 1), (1, 2, -float("inf"))):
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    NS["complete_parameters"](a, b, c)

    def test_area_tiles_maintain_exact_ratios(self):
        tiles = NS["area_tiles"]
        for x in (1, 2, 4):
            for k in (1, 3, 5):
                with self.subTest(x=x, k=k):
                    width_x, width_k, areas = tiles(x, k, 0.67)
                    self.assertTrue(math.isclose(width_x / width_k, x / k))
                    self.assertEqual(areas, (x*x, x*k, x*k, k*k))
                    self.assertEqual(sum(areas), (x+k)**2)
        self.assertEqual(tiles(2, 3, 0.67)[2], (4, 6, 6, 9))

    def test_area_geometry_requires_positive_lengths(self):
        for x, k, scale in ((0, 3, 1), (-2, 3, 1), (2, 0, 1),
                            (2, 3, 0), (2, 3, float("nan"))):
            with self.assertRaises(ValueError):
                NS["area_tiles"](x, k, scale)

    def test_scene_name_methods_portrait_and_cjk_tex(self):
        scene = next(n for n in TREE.body if isinstance(n, ast.ClassDef)
                     and n.name == "CompletingTheSquare")
        methods = {n.name for n in scene.body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_perfect_square_review",
                         "show_geometry_visualization", "show_method_steps",
                         "show_example_1", "show_example_2", "show_applications",
                         "show_summary"}.issubset(methods))
        text = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", text)
        self.assertIn("config.frame_height = 16", text)
        for node in ast.walk(TREE):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "MathTex"):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any('\u4e00' <= char <= '\u9fff' for char in arg.value),
                                         f"Chinese must be Text, not MathTex: {arg.value!r}")


if __name__ == "__main__":
    unittest.main()
