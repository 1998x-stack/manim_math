"""独立测试本课 Scene 的素数/正因数/分类函数，无需导入 Manim。

运行：python verify_primes_composites.py
"""

import ast
import copy
import math
from pathlib import Path
from types import SimpleNamespace
import unittest

SOURCE = Path(__file__).with_name("primes_composites.py")


def load_scene_math():
    """仅提取课程源码的纯数学方法，测试真实算法而非另一份实现。"""
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    scene = next(node for node in tree.body
                 if isinstance(node, ast.ClassDef) and node.name == "PrimesComposites")
    methods = {}
    nodes = []
    for name in ("is_prime", "get_factors", "classify"):
        method = next(node for node in scene.body
                      if isinstance(node, ast.FunctionDef) and node.name == name)
        method = copy.deepcopy(method)
        method.decorator_list = []
        nodes.append(method)
        methods[name] = True
    namespace = {"math": math}
    module = ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[]))
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return namespace


class PrimeCompositeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.algorithms = load_scene_math()
        cls.scene_stub = SimpleNamespace(is_prime=cls.algorithms["is_prime"])

    def test_known_primes_and_composites(self):
        is_prime = self.algorithms["is_prime"]
        for n in (2, 3, 5, 7, 11, 13, 17, 19, 97, 101):
            with self.subTest(prime=n):
                self.assertTrue(is_prime(n))
        for n in (-7, -1, 0, 1, 4, 6, 9, 25, 49, 121, 221):
            with self.subTest(not_prime=n):
                self.assertFalse(is_prime(n))
        for n in range(2, 201):
            factors = self.algorithms["get_factors"](n)
            self.assertEqual(is_prime(n), len(factors) == 2, n)

    def test_factors_and_domain(self):
        factors = self.algorithms["get_factors"]
        self.assertEqual(factors(1), (1,))
        self.assertEqual(factors(6), (1, 2, 3, 6))
        self.assertEqual(factors(7), (1, 7))
        self.assertEqual(factors(20), (1, 2, 4, 5, 10, 20))
        for bad in (0, -2, 3.0, True):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                factors(bad)
        for bad in (True, 2.0, "7"):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                self.algorithms["is_prime"](bad)

    def test_classification_of_first_twenty(self):
        classify = self.algorithms["classify"]
        by_kind = {kind: tuple(n for n in range(1, 21)
                               if classify(self.scene_stub, n) == kind)
                   for kind in ("special", "prime", "composite")}
        self.assertEqual(by_kind["special"], (1,))
        self.assertEqual(by_kind["prime"], (2, 3, 5, 7, 11, 13, 17, 19))
        self.assertEqual(by_kind["composite"],
                         (4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20))
        self.assertEqual(sum(map(len, by_kind.values())), 20)
        for bad in (0, -1, 4.0, False):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                classify(self.scene_stub, bad)

    def test_scene_and_color_lifecycle_contract(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "PrimesComposites")
        functions = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_factors_review", "show_prime_definition",
                         "show_composite_definition", "show_special_cases",
                         "show_classification", "show_outro"} <= functions)
        self.assertTrue(any(isinstance(node, ast.ClassDef) and node.name == "TestPrimesComposites"
                            for node in tree.body))
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn("nodes[i][0].animate.set_fill", source)
        self.assertIn('self.text(str(number), font_size, WHITE)', source)
        self.assertNotIn('number_circles[i].animate.set_color', source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
