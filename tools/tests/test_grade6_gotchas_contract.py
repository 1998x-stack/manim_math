"""Source-level contract for the six-grade rational-number scene; no Manim import."""

import ast
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SCENE = (REPO_ROOT / "初中" / "六年级" / "第二学期" / "第五章-有理数"
         / "005有理数的大小比较" / "005_有理数的大小比较.py")


class RationalComparisonContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCENE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source, filename=str(SCENE))
        cls.calls = [node for node in ast.walk(cls.tree) if isinstance(node, ast.Call)]

    def test_legacy_scene_entrypoint_is_preserved(self):
        classes = [node for node in cls_tree_body(self.tree)
                   if isinstance(node, ast.ClassDef)
                   and node.name == "有理数的大小比较Animation"]
        self.assertEqual(len(classes), 1)
        self.assertTrue(any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in classes[0].bases))
        self.assertTrue(any(isinstance(node, ast.FunctionDef) and node.name == "construct"
                            for node in classes[0].body))

    def test_number_line_has_ordered_signed_example(self):
        names = [node.func.id for node in self.calls if isinstance(node.func, ast.Name)]
        self.assertIn("NumberLine", names)
        self.assertIn("Dot", names)
        values = [node for node in ast.walk(self.tree)
                  if isinstance(node, ast.Assign)
                  and any(isinstance(target, ast.Name) and target.id == "values"
                          for target in node.targets)]
        self.assertEqual(len(values), 1)
        self.assertEqual(ast.literal_eval(values[0].value), (-2, 0, 1))
        self.assertIn("数轴上右边的数大于左边的数", self.source)

    def test_mathtex_literals_are_ascii_and_example_is_consistent(self):
        mathtex = [node for node in self.calls
                   if isinstance(node.func, ast.Name) and node.func.id == "MathTex"]
        self.assertGreaterEqual(len(mathtex), 1)
        literals = [arg.value for node in mathtex for arg in node.args
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str)]
        self.assertIn("-2 < 0 < 1", literals)
        self.assertTrue(all(text.isascii() for text in literals))
        self.assertTrue(-2 < 0 < 1)


def cls_tree_body(tree):
    """Get module statements without importing the animation runtime."""
    return tree.body


if __name__ == "__main__":
    unittest.main()
