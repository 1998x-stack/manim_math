"""公式法课程专项测试：提取实际源码的纯数学模型，不导入 Manim。"""

import ast
from pathlib import Path
import unittest

SCENE = Path(__file__).with_name("factorization_formulas.py")


def recognizer():
    tree = ast.parse(SCENE.read_text(encoding="utf-8"))
    node = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                and n.name == "recognize_square_trinomial")
    scope = {}
    exec(compile(ast.Module(body=[node], type_ignores=[]), str(SCENE), "exec"), scope)
    return scope["recognize_square_trinomial"]


class FormulaFactorizationLessonTests(unittest.TestCase):
    def test_difference_of_squares_reverse_is_exact(self):
        for a in range(-8, 9):
            for b in range(-8, 9):
                self.assertEqual((a+b)*(a-b), a*a-b*b)
        for x in (-5, -2, 0, 1, 7):
            self.assertEqual(x*x-100, (x+10)*(x-10))
            self.assertEqual(x*x-9, (x+3)*(x-3))
            for y in (-3, -1, 0, 2, 6):
                self.assertEqual(4*x*x-9*y*y, (2*x+3*y)*(2*x-3*y))

    def test_perfect_square_recognizer_and_counterexamples(self):
        recognize = recognizer()
        for b in range(0, 21):
            sign, recovered = recognize(2*b, b*b)
            self.assertEqual(recovered, b)
            self.assertEqual(sign, 0 if b == 0 else 1)
            sign_minus, recovered_minus = recognize(-2*b, b*b)
            self.assertEqual(recovered_minus, b)
            self.assertEqual(sign_minus, 0 if b == 0 else -1)
            for x in (-7, -2, 0, 1, 5):
                self.assertEqual(x*x+2*b*x+b*b, (x+b)**2)
                self.assertEqual(x*x-2*b*x+b*b, (x-b)**2)
        self.assertIsNone(recognize(6, 8))  # 可因式分解，但不是完全平方
        self.assertIsNone(recognize(4, 9))  # 首末平方不够，中间项还须匹配
        self.assertIsNone(recognize(6, -9))
        self.assertIsNone(recognize(0, 9))
        self.assertEqual(recognize(0, 0), (0, 0))
        for m, c in ((6.0, 9), (6, 9.0), (True, 1), (6, None)):
            with self.subTest(m=m, c=c), self.assertRaises(ValueError):
                recognize(m, c)

    def test_syntax_and_scene_contract(self):
        source = SCENE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SCENE), "exec")
        scene = next(n for n in tree.body if isinstance(n, ast.ClassDef)
                     and n.name == "FactorizationFormulas")
        methods = {n.name for n in scene.body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"construct", "clear_content", "show_opening",
                         "show_difference_of_squares_theory",
                         "show_difference_of_squares_example", "show_perfect_square_theory",
                         "show_perfect_square_example", "show_challenge_example",
                         "show_summary"} <= methods)
        self.assertIn("recognize_square_trinomial(6, 8) is None", source)
        self.assertIn("SAFE_WIDTH = 7.4", source)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        self.assertNotIn("original_expr[0][", source)
        self.assertNotIn("corner_radius=0.1", source)
        for call in ast.walk(scene):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id in {"MathTex", "Tex"}:
                    for arg in call.args:
                        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in arg.value))


if __name__ == "__main__":
    unittest.main()
