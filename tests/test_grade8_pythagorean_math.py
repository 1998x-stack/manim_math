"""勾股定理逆定理的无 Manim 数学/源码契约回归测试。"""
import ast
from pathlib import Path
import unittest

SCENE = (Path(__file__).resolve().parents[1] / "初中" / "八年级" / "第一学期"
         / "第十九章-几何证明" / "008勾股定理的逆定理" / "pythagorean_inverse.py")


class PythagoreanConverseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SCENE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        pure = next(node for node in cls.tree.body if isinstance(node, ast.FunctionDef)
                    and node.name == "is_right_triangle_sides")
        import math
        namespace = {"isclose": math.isclose, "isfinite": math.isfinite}
        exec(compile(ast.Module(body=[pure], type_ignores=[]), str(SCENE), "exec"), namespace)
        cls.check = staticmethod(namespace["is_right_triangle_sides"])

    def test_true_integer_triples_and_order(self):
        for sides in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10), (5, 4, 3)):
            with self.subTest(sides=sides):
                self.assertTrue(self.check(sides))

    def test_rejects_non_right_and_invalid_triangles(self):
        for sides in ((2, 3, 4), (1, 2, 3), (0, 4, 4), (-3, 4, 5),
                      (1, 1, 1), (float("inf"), 3, 4), (float("nan"), 3, 4),
                      (3, 4), ("wrong", 4, 5)):
            with self.subTest(sides=sides):
                self.assertFalse(self.check(sides))

    def test_scene_name_geometry_and_tex_degree(self):
        classes = [node for node in self.tree.body if isinstance(node, ast.ClassDef)]
        self.assertIn("PythagoreanInverse", [node.name for node in classes])
        # a=BC, b=CA, c=AB；示意中 C 是直角顶点；不把原来 A 的直角标成 C。
        self.assertIn("a=BC、b=CA、c=AB", self.source)
        self.assertIn("RightAngle(Line(C, B), Line(C, A)", self.source)
        latex_strings = [arg.value for node in ast.walk(self.tree)
                         if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                         and node.func.id in ("MathTex", "Tex")
                         for arg in node.args if isinstance(arg, ast.Constant)
                         and isinstance(arg.value, str)]
        self.assertFalse(any("°" in tex for tex in latex_strings))
        self.assertIn(r"\angle C=90^\circ", self.source)


if __name__ == "__main__":
    unittest.main()
