"""不导入 Manim 的一元二次方程场景契约回归测试。"""
import ast
from pathlib import Path
import unittest

SCENE_PATH = (Path(__file__).resolve().parents[1] / "初中" / "八年级"
              / "第一学期" / "第十七章-一元二次方程"
              / "001一元二次方程的概念" / "001_一元二次方程的概念.py")


class QuadraticConceptContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCENE_PATH.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        cls.scene = next(node for node in cls.tree.body if isinstance(node, ast.ClassDef)
                         and node.name == "一元二次方程的概念Animation")

    def test_stable_public_scene_class(self):
        self.assertTrue(any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in self.scene.bases))
        methods = {node.name: node for node in self.scene.body
                   if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"construct", "show_definition", "show_general_form",
                         "show_coefficient_explanation", "show_comparison", "show_summary"}
                        <= methods.keys())

    def test_actual_scene_objects_are_cleared(self):
        methods = {node.name: node for node in self.scene.body
                   if isinstance(node, ast.FunctionDef)}
        clear = methods["_clear"]
        self.assertIn("self.mobjects", ast.unparse(clear))
        self.assertIn("self.author_info", ast.unparse(clear))
        for name in ("show_opening", "show_definition", "show_general_form",
                     "show_coefficient_explanation", "show_comparison"):
            self.assertIn("self._clear()", ast.unparse(methods[name]))
        self.assertNotIn("FadeOut(SurroundingRectangle(", self.source)

    def test_math_domain_and_cancellation_counterexample(self):
        self.assertIn(r"a\ne0", self.source)
        self.assertIn(r"a\ne 0", self.source)
        self.assertIn(r"x^2-x^2+x=0", self.source)
        for x in (-3, 0, 4):
            self.assertEqual(x * x - x * x + x, x)


if __name__ == "__main__":
    unittest.main()
