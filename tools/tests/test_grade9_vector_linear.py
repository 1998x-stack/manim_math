"""九年级《向量的线性运算》：回归箭头首尾关系、斜基底真实分量与平行性。"""

import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCE = (ROOT / "初中/九年级/第一学期/第二十四章-相似三角形"
          / "008向量的线性运算/vector_linear_operations.py")


class VectorLinearTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"addition_model", "basis_decomposition", "parallel_relation"}
        funcs = [node for node in cls.tree.body
                 if isinstance(node, ast.FunctionDef) and node.name in names]
        if {node.name for node in funcs} != names:
            raise AssertionError("缺少向量加法、二维基底或平行向量数学函数")
        namespace = {"math": math, "A": (2.0, 1.0), "B": (1.0, 2.0),
                     "E1": (1.0, 0.0), "E2": (.5, 1.0)}
        exec(compile(ast.Module(body=funcs, type_ignores=[]),
                     str(SOURCE), "exec"), namespace)
        cls.add = staticmethod(namespace["addition_model"])
        cls.basis = staticmethod(namespace["basis_decomposition"])
        cls.parallel = staticmethod(namespace["parallel_relation"])

    def test_addition_arrow_endpoints_are_one_shared_point(self):
        result = self.add()
        self.assertEqual(result["sum_end"], result["a_then_b"])
        self.assertEqual(result["sum_end"], result["b_then_a"])
        self.assertEqual(result["sum_end"], (1.35, 3.2))
        self.assertTrue(all(-3.8 < x < 3.8 and -3.8 < y < 3.8
                            for x, y in result.values()))
        alternative = self.add((1, -2), (-3, 2), (0, 0))
        self.assertEqual(alternative["sum_end"], (-2.0, 0.0))

    def test_nonorthogonal_basis_uses_actual_second_component(self):
        c1, c2, v1, v2 = self.basis()
        self.assertAlmostEqual(c1, 1.5)
        self.assertAlmostEqual(c2, 1)
        self.assertEqual(v1, (1.5, 0.0))
        self.assertEqual(v2, (.5, 1.0))
        self.assertEqual(tuple(v1[i]+v2[i] for i in range(2)), (2, 1))
        self.assertNotEqual(v2, (0, 1))
        for target in ((0, 0), (3, -2), (-5, 2.5)):
            a, b, first, second = self.basis(target)
            for index in range(2):
                self.assertAlmostEqual(first[index]+second[index], target[index])

    def test_parallel_same_opposite_and_not_parallel(self):
        self.assertEqual(self.parallel((1.2, .6), (2.4, 1.2)), "same")
        self.assertEqual(self.parallel((1.2, .6), (-1.2, -.6)), "opposite")
        self.assertEqual(self.parallel((1, 0), (0, 1)), "not_parallel")
        self.assertEqual(self.parallel((2, 1), (.5, .25)), "same")

    def test_invalid_or_degenerate_inputs_raise_instead_of_drawing(self):
        for a, b in (((0, 0), (1, 2)), ((1, 2), (0, 0)),
                     ((1, 2), (-1, -2)), ((math.inf, 1), (1, 2))):
            with self.subTest(add=(a, b)), self.assertRaises(ValueError):
                self.add(a, b)
        for e1, e2 in ((((1, 0), (2, 0))), (((1, 1), (-2, -2))),
                       (((0, 0), (0, 1)))):
            with self.subTest(basis=(e1, e2)), self.assertRaises(ValueError):
                self.basis((2, 1), e1, e2)
        for a, b in (((0, 0), (1, 0)), ((1, 0), (0, 0)),
                     ((math.nan, 1), (1, 2))):
            with self.subTest(parallel=(a, b)), self.assertRaises(ValueError):
                self.parallel(a, b)

    def test_scene_draws_translated_b_and_true_oblique_component(self):
        scene = next(node for node in self.tree.body
                     if isinstance(node, ast.ClassDef)
                     and node.name == "VectorLinearOperations")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertIn('p["a_end"], p["a_then_b"]', methods["show_vector_addition"])
        self.assertIn('p["b_end"]), point3(p["b_then_a"]',
                      methods["show_vector_addition"])
        self.assertIn('result_end = tuple(first_end[i]+v2[i]',
                      methods["show_vector_decomposition"])
        self.assertIn('self.arrow(first_end, result_end, self.PURPLE)',
                      methods["show_vector_decomposition"])
        self.assertNotIn("Transform(arrow_b.copy()", self.source)
        self.assertNotIn("self.play(self.play(", self.source)
        for node in ast.walk(scene):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id in {"Tex", "MathTex"}):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(any("\u4e00" <= c <= "\u9fff"
                                             for c in arg.value))


if __name__ == "__main__":
    unittest.main()
