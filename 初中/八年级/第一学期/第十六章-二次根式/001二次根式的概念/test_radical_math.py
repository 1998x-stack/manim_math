"""无需 Manim 的本课数学回归：python -m unittest test_radical_math.py -v。"""

import ast
import math
from pathlib import Path
import unittest


SOURCE = Path(__file__).with_name("quadratic_radical.py")


def load_math_functions():
    """仅提取纯数学函数，不导入 Manim 或执行 Scene。"""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    selected = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"real_sqrt_defined", "x_plus_one_domain"}
    ]
    assert len(selected) == 2, "必须保留两个可独立验证的数学函数"
    module = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    namespace = {"math": math}
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return namespace


class RadicalDomainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_math_functions()

    def test_real_sqrt_boundary(self):
        defined = self.model["real_sqrt_defined"]
        for value in (0, 0.0, 4, 0.0001):
            with self.subTest(value=value):
                self.assertTrue(defined(value))
        for value in (-4, -0.0001, float("inf"), float("nan")):
            with self.subTest(value=value):
                self.assertFalse(defined(value))

    def test_x_plus_one_includes_endpoint(self):
        defined = self.model["x_plus_one_domain"]
        self.assertFalse(defined(-1.0001))
        self.assertTrue(defined(-1))
        self.assertTrue(defined(0))
        self.assertTrue(defined(4))

    def test_principal_square_root_is_nonnegative(self):
        for value in (0, 1, 2, 9, 100):
            with self.subTest(value=value):
                self.assertGreaterEqual(math.sqrt(value), 0)
                self.assertEqual(math.sqrt(value) == 0, value == 0)

    def test_scene_and_math_wording(self):
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        scenes = [node for node in tree.body if isinstance(node, ast.ClassDef)
                  and node.name == "QuadraticRadical"]
        self.assertEqual(len(scenes), 1)
        methods = {node.name for node in scenes[0].body
                   if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"scene_definition", "scene_condition", "scene_examples",
                         "scene_double_nonneg", "scene_summary", "scene_outro"} <= methods)
        self.assertNotIn(r"\sqrt{a} \Leftrightarrow a \geq 0", source)
        self.assertIn("axis.n2p(-0.12)", source)
        self.assertIn("zero = Dot(axis.n2p(0)", source)


if __name__ == "__main__":
    unittest.main()
