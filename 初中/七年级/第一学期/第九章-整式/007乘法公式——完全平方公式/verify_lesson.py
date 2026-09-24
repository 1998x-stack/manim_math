"""完全平方课程数学回归：独立验证原 Scene 使用的面积模型。"""

import ast
import math
from pathlib import Path
import unittest

SCENE = Path(__file__).with_name("perfect_square_formula.py")


def load_square_model():
    source = SCENE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    func = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                and n.name == "square_regions")
    scope = {}
    exec(compile(ast.Module(body=[func], type_ignores=[]), str(SCENE), "exec"), scope)
    return scope["square_regions"]


class PerfectSquareLessonTests(unittest.TestCase):
    def test_four_tiles_exact_dimensions_and_adjacency(self):
        model = load_square_model()
        for a, b in ((2.2, 1.1), (1, 1), (3, 2), (5, 0.5), (0.1, 0.3)):
            spec = model(a, b)
            aa, ab_top, ab_bottom, bb = spec["cells"]
            self.assertEqual(len(spec["cells"]), 4)
            self.assertEqual([c["name"] for c in spec["cells"]],
                             ["a2", "ab_top", "ab_bottom", "b2"])
            self.assertEqual([(c["width"], c["height"]) for c in spec["cells"]],
                             [(a, a), (b, a), (a, b), (b, b)])
            self.assertTrue(math.isclose(spec["x_split"], aa["x0"]+aa["width"]))
            self.assertTrue(math.isclose(spec["x_split"], ab_top["x0"]))
            self.assertTrue(math.isclose(spec["y_split"], bb["y0"]+bb["height"]))
            self.assertTrue(math.isclose(spec["y_split"], aa["y0"]))
            self.assertTrue(math.isclose(spec["left"]+spec["side"],
                                         ab_top["x0"]+ab_top["width"]))
            self.assertTrue(math.isclose(spec["bottom"]+spec["side"],
                                         aa["y0"]+aa["height"]))
            self.assertTrue(math.isclose(sum(c["area"] for c in spec["cells"]),
                                         (a+b)**2, rel_tol=1e-12, abs_tol=1e-12))

    def test_zero_negative_nonfinite_rejected_for_picture(self):
        model = load_square_model()
        for a, b in ((0, 1), (-1, 2), (2, 0), (2, -1),
                     (math.nan, 2), (2, math.inf), ("x", 1)):
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                model(a, b)

    def test_both_identities_for_all_signs_and_examples(self):
        for a in range(-6, 7):
            for b in range(-6, 7):
                self.assertEqual((a+b)**2, a*a+2*a*b+b*b)
                self.assertEqual((a-b)**2, a*a-2*a*b+b*b)
                self.assertNotEqual((a+b)**2, a*a+b*b) if a*b != 0 else None
        self.assertEqual((4+3)**2, 16+24+9)
        self.assertEqual((4-3)**2, 16-24+9)

    def test_scene_uses_same_model_and_no_chinese_mathtex(self):
        source = SCENE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SCENE), "exec")
        scene = next(n for n in tree.body if isinstance(n, ast.ClassDef)
                     and n.name == "PerfectSquareFormula")
        methods = {n.name for n in scene.body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"construct", "show_geometric_construction",
                         "show_geometric_division", "show_area_coloring",
                         "show_formula_derivation", "show_example_and_outro"} <= methods)
        self.assertIn("self.spec = square_regions(2.2, 1.1)", source)
        self.assertIn('for cell, color, tex in zip(self.spec["cells"]', source)
        self.assertIn('width=cell["width"], height=cell["height"]', source)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        self.assertNotIn("print(\"WARNING:", source)
        for call in ast.walk(scene):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id in {"MathTex", "Tex"}:
                    for literal in call.args:
                        if isinstance(literal, ast.Constant) and isinstance(literal.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in literal.value))


if __name__ == "__main__":
    unittest.main()
