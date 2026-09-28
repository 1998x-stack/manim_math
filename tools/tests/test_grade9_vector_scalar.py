"""九年级《向量的数乘》：抽取课件真实数学模型的无 Manim 回归。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
          / "007向量的数乘运算/vector_scalar_mult.py")


class ScalarMultiplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"scalar_geometry", "distributive_example"}
        funcs = [node for node in cls.tree.body
                 if isinstance(node, ast.FunctionDef) and node.name in names]
        if {node.name for node in funcs} != names:
            raise AssertionError("缺少可验证的数乘及分配律模型")
        namespace = {"math": math}
        exec(compile(ast.Module(body=funcs, type_ignores=[]),
                     str(SOURCE), "exec"), namespace)
        cls.geometry = staticmethod(namespace["scalar_geometry"])
        cls.distribute = staticmethod(namespace["distributive_example"])

    def test_direction_length_and_endpoint_follow_scalar_sign(self):
        base = (1.4, .7)
        length = math.hypot(*base)
        for scalar, direction in ((.5, "same"), (1, "same"),
                                  (2, "same"), (-1, "opposite"),
                                  (-2, "opposite"), (0, "zero")):
            with self.subTest(scalar=scalar):
                actual = self.geometry(base, scalar, (0, .8))
                self.assertEqual(actual["direction"], direction)
                self.assertAlmostEqual(actual["norm"], abs(scalar)*length)
                self.assertAlmostEqual(actual["end"][0], scalar*base[0])
                self.assertAlmostEqual(actual["end"][1], .8+scalar*base[1])
                self.assertTrue(-3.8 < actual["end"][0] < 3.8)
                self.assertTrue(-2.2 < actual["end"][1] < 3.8)

    def test_zero_scalar_has_no_arrow_direction_and_no_length(self):
        actual = self.geometry((1.4, .7), 0)
        self.assertEqual(actual["start"], actual["end"])
        self.assertEqual(actual["norm"], 0)
        self.assertEqual(actual["direction"], "zero")

    def test_invalid_inputs_and_overflow_fail(self):
        for vector, scalar in (((0, 0), 1), ((1, 0), math.nan),
                               ((1, math.inf), 2), ((1, 0), math.inf),
                               ((1e308, 1e308), 2)):
            with self.subTest(vector=vector, scalar=scalar), self.assertRaises(ValueError):
                self.geometry(vector, scalar)
        with self.assertRaises(ValueError):
            self.distribute((math.nan, 1), (1, 1), 2)

    def test_distributive_model_is_a_real_vector_calculation(self):
        for a, b, factor in (((2, 1), (1, -2), 2),
                             ((1.5, -1), (-2, 5), -.5),
                             ((0, 0), (1, -2), 0)):
            lhs, rhs = self.distribute(a, b, factor)
            for value, expected in zip(lhs, rhs):
                self.assertAlmostEqual(value, expected)
        lhs, rhs = self.distribute()
        self.assertEqual(lhs, (6.0, -2.0))
        self.assertEqual(lhs, rhs)

    def test_scene_renders_dot_for_zero_and_never_builds_invalid_mathtex(self):
        scene = next(node for node in self.tree.body
                     if isinstance(node, ast.ClassDef)
                     and node.name == "VectorScalarMult")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertIn('if model["direction"] == "zero":', methods["arrow"])
        self.assertIn("return Dot(point3(model[\"start\"])", methods["arrow"])
        self.assertNotIn("always_redraw(", self.source)
        self.assertNotIn("->->", self.source)
        self.assertNotIn("-><-", self.source)
        self.assertIn('self.arrow(0)', methods["scene_5_zero_lambda"])
        self.assertIn("self.clear_section(keep_author=False)",
                      methods["scene_8_outro"])
        for node in ast.walk(scene):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id in {"MathTex", "Tex"}):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any("\u4e00" <= ch <= "\u9fff"
                                             for ch in arg.value))


if __name__ == "__main__":
    unittest.main()
