"""幂的运算法则课内回归；仅使用 Python 标准库，不导入 Manim。"""

import ast
from fractions import Fraction
from pathlib import Path
import unittest

SCENE = Path(__file__).with_name("power_operation_laws.py")


class PowerLawsLessonTests(unittest.TestCase):
    def test_exact_arithmetic_and_zero_boundary(self):
        for a in (-3, -2, -1, 0, 1, 2, 3):
            for b in (-3, -1, 0, 1, 2):
                for m in range(1, 5):
                    for n in range(1, 5):
                        self.assertEqual(a ** m * a ** n, a ** (m + n))
                        self.assertEqual((a ** m) ** n, a ** (m * n))
                        self.assertEqual((a * b) ** n, a ** n * b ** n)
                        if a and m >= n:
                            self.assertEqual(Fraction(a ** m, a ** n), a ** (m - n))
        self.assertEqual(2 ** 3 * 2 ** 5, 2 ** 8)
        self.assertEqual((2 ** 3) ** 2, 2 ** 6)
        self.assertEqual((2 * 3) ** 2, 2 ** 2 * 3 ** 2)
        self.assertEqual(Fraction(2 ** 5, 2 ** 3), 4)
        self.assertEqual(Fraction(3 ** 2, 3 ** 2), 1)
        with self.assertRaises(ZeroDivisionError):
            Fraction(0 ** 2, 0 ** 1)

    def test_counterexamples_and_domain(self):
        self.assertNotEqual(2 ** 3 * 3 ** 5, 2 ** (3 + 5))
        self.assertNotEqual((2 ** 3) ** 2, 2 ** (3 + 2))
        self.assertNotEqual((2 * 3) ** 2, 2 ** 2 * 3)
        self.assertNotEqual(Fraction(2 ** 3, 2 ** 5), 2 ** (3 - 5 + 1))

    def test_scene_entrypoint_portrait_layout_and_latex(self):
        source = SCENE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SCENE), "exec")
        classes = [c for c in tree.body if isinstance(c, ast.ClassDef)]
        scene = next(c for c in classes if c.name == "PowerOperationLaws")
        methods = {item.name for item in scene.body if isinstance(item, ast.FunctionDef)}
        self.assertTrue({"construct", "show_opening", "show_law_1_same_base_multiply",
                         "show_law_2_power_of_power", "show_law_3_product_power",
                         "show_law_4_same_base_divide", "show_summary", "show_outro"} <= methods)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        self.assertIn("SAFE_WIDTH = 7.5", source)
        self.assertNotIn("UP * self.EXPLAIN_Y", source)
        self.assertNotIn("get_tex_string()", source)
        self.assertIn("m ≥ n ≥ 0", source)
        self.assertIn("a ≠ 0", source)
        self.assertIn("Fraction", Path(__file__).read_text(encoding="utf-8"))
        for node in ast.walk(scene):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"MathTex", "Tex"}:
                    for arg in node.args:
                        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in arg.value))
                if node.func.id == "SurroundingRectangle":
                    self.assertNotIn("corner_radius", {kw.arg for kw in node.keywords})


if __name__ == "__main__":
    unittest.main()
