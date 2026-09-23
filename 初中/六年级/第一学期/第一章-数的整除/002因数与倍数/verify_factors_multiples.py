"""因数与倍数：无需安装 Manim 的源码数学函数回归。

运行：python verify_factors_multiples.py
"""

import ast
import copy
from pathlib import Path
import unittest


SOURCE = Path(__file__).with_name("factors_multiples.py")


def load_math_functions():
    """从真实 Scene 源码提取纯函数体，避免导入渲染依赖。"""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    scene = next(node for node in tree.body
                 if isinstance(node, ast.ClassDef) and node.name == "FactorsAndMultiples")
    needed = ("positive_factors", "first_positive_multiples")
    functions = []
    for name in needed:
        method = next(node for node in scene.body
                      if isinstance(node, ast.FunctionDef) and node.name == name)
        method_copy = copy.deepcopy(method)
        method_copy.decorator_list = []
        functions.append(method_copy)
    module = ast.fix_missing_locations(ast.Module(body=functions, type_ignores=[]))
    namespace = {}
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return namespace


class FactorsAndMultiplesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.methods = load_math_functions()

    def test_all_positive_factors(self):
        factors = self.methods["positive_factors"]
        self.assertEqual(factors(12), (1, 2, 3, 4, 6, 12))
        self.assertEqual(factors(1), (1,))
        self.assertEqual(factors(13), (1, 13))
        for number in range(1, 51):
            found = factors(number)
            self.assertEqual(found, tuple(i for i in range(1, number + 1)
                                          if number % i == 0))
            self.assertEqual(found[0], 1)
            self.assertEqual(found[-1], number)

    def test_positive_multiples(self):
        multiples = self.methods["first_positive_multiples"]
        self.assertEqual(multiples(3, 6), (3, 6, 9, 12, 15, 18))
        self.assertEqual(multiples(1, 1), (1,))
        self.assertEqual(multiples(7, 4), (7, 14, 21, 28))
        self.assertTrue(all(x > 0 for x in multiples(3, 20)))

    def test_domain_guards_and_zero_integer_multiple(self):
        factors = self.methods["positive_factors"]
        multiples = self.methods["first_positive_multiples"]
        for invalid in (0, -3, 2.5, True):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                factors(invalid)
        for number, count in ((0, 3), (-3, 3), (3, 0), (3, -2), (3, True)):
            with self.subTest(number=number, count=count), self.assertRaises(ValueError):
                multiples(number, count)
        self.assertTrue(all(divisor * 0 == 0 for divisor in (-9, -1, 1, 3, 12)))
        self.assertNotIn(0, factors(12))
        self.assertNotIn(0, multiples(3, 6))

    def test_source_has_all_scenes_and_scope_notes(self):
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "FactorsAndMultiples")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_definition", "show_find_factors",
                         "show_find_multiples", "show_special_rules", "show_summary"} <= methods)
        self.assertIn("正因数：有限个；最小 1，最大 n", source)
        self.assertIn("正倍数：无限个；最小 n", source)
        self.assertIn("0 是每个非零整数的倍数", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
