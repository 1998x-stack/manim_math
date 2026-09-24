"""提公因式专项回归：独立调用源码中的纯数学模型，不依赖 Manim。"""

import ast
from pathlib import Path
import unittest

SCENE = Path(__file__).with_name("common_factor_method.py")


def factor_model():
    tree = ast.parse(SCENE.read_text(encoding="utf-8"))
    function = next(node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == "common_factor_data")
    scope = {}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(SCENE), "exec"), scope)
    return scope["common_factor_data"]


class CommonFactorLessonTests(unittest.TestCase):
    def test_three_lesson_examples(self):
        factor = factor_model()
        self.assertEqual(factor([(6, 2, 1), (-9, 1, 2)]),
                         ((3, 1, 1), ((2, 1, 0), (-3, 0, 1))))
        self.assertEqual(factor([(12, 2, 1), (-8, 1, 2)]),
                         ((4, 1, 1), ((3, 1, 0), (-2, 0, 1))))
        self.assertEqual(factor([(5, 3, 0), (10, 2, 0), (-15, 1, 0)]),
                         ((5, 1, 0), ((1, 2, 0), (2, 1, 0), (-3, 0, 0))))

    def test_exhaustive_coefficient_and_signed_reconstruction(self):
        factor = factor_model()
        for c1 in range(-8, 9):
            for c2 in range(-8, 9):
                if c1 == 0 or c2 == 0:
                    continue
                terms = [(c1, 4, 2), (c2, 2, 3)]
                common, quotient = factor(terms)
                self.assertEqual(common[1:], (2, 2))
                self.assertEqual(len(quotient), len(terms))
                self.assertGreater(common[0], 0)
                for original, residual in zip(terms, quotient):
                    self.assertEqual(original[0], common[0] * residual[0])
                    self.assertEqual(original[1], common[1] + residual[1])
                    self.assertEqual(original[2], common[2] + residual[2])
                for x in (-3, -1, 0, 1, 4):
                    for y in (-2, 0, 2):
                        lhs = sum(c * x**xp * y**yp for c, xp, yp in terms)
                        rhs = (common[0] * x**common[1] * y**common[2]
                               * sum(c * x**xp * y**yp for c, xp, yp in quotient))
                        self.assertEqual(lhs, rhs)

    def test_invalid_inputs_and_constant_factor(self):
        factor = factor_model()
        for data in ([], [(0, 1, 1)], [(1, -1, 0)], [(1, 0, -1)],
                     [(1.5, 1, 0)], [(True, 1, 0)], [(1, 1)], ["xy"]):
            with self.subTest(data=data), self.assertRaises(ValueError):
                factor(data)
        self.assertEqual(factor([(4, 0, 0), (6, 0, 0)]),
                         ((2, 0, 0), ((2, 0, 0), (3, 0, 0))))

    def test_source_contract(self):
        source = SCENE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SCENE), "exec")
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "CommonFactorMethod")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"construct", "clear_content", "show_opening", "show_concept_intro",
                         "show_extraction_steps", "show_memory_tips", "show_example_1",
                         "show_example_2", "show_summary"} <= methods)
        self.assertIn("self.first_factor, self.first_quotient = common_factor_data(", source)
        self.assertIn("SAFE_WIDTH = 7.4", source)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        self.assertNotIn("formula[0][", source)
        self.assertNotIn("ReplacementTransform(formula.copy()", source)
        for call in ast.walk(scene):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id in {"MathTex", "Tex"}:
                    for literal in call.args:
                        if isinstance(literal, ast.Constant) and isinstance(literal.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in literal.value))


if __name__ == "__main__":
    unittest.main()
