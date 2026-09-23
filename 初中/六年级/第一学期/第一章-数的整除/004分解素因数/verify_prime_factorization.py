"""独立验证真实 Scene 数学函数，无需安装 Manim。

运行：python verify_prime_factorization.py
"""

import ast
import copy
from pathlib import Path
from types import SimpleNamespace
import unittest

SOURCE = Path(__file__).with_name("prime_factorization.py")


def load_model():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    scene = next(node for node in tree.body
                 if isinstance(node, ast.ClassDef) and node.name == "PrimeFactorization")
    method_nodes = []
    for name in ("prime_factors", "short_division_steps"):
        method = next(node for node in scene.body
                      if isinstance(node, ast.FunctionDef) and node.name == name)
        node = copy.deepcopy(method)
        node.decorator_list = []
        method_nodes.append(node)
    namespace = {}
    module = ast.fix_missing_locations(ast.Module(body=method_nodes, type_ignores=[]))
    exec(compile(module, str(SOURCE), "exec"), namespace)
    namespace["PrimeFactorization"] = SimpleNamespace(prime_factors=namespace["prime_factors"])
    return namespace


def is_prime_by_division(n):
    return n >= 2 and all(n % divisor != 0 for divisor in range(2, n))


class PrimeFactorizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = load_model()

    def test_known_factorizations_and_order(self):
        factorize = self.model["prime_factors"]
        self.assertEqual(factorize(2), (2,))
        self.assertEqual(factorize(30), (2, 3, 5))
        self.assertEqual(factorize(60), (2, 2, 3, 5))
        self.assertEqual(factorize(97), (97,))
        self.assertEqual(factorize(81), (3, 3, 3, 3))
        self.assertEqual(factorize(100), (2, 2, 5, 5))
        for n in range(2, 501):
            with self.subTest(number=n):
                factors = factorize(n)
                product = 1
                for factor in factors:
                    product *= factor
                    self.assertTrue(is_prime_by_division(factor))
                self.assertEqual(product, n)
                self.assertEqual(factors, tuple(sorted(factors)))

    def test_short_division_rows_are_one_consistent_data_source(self):
        steps = self.model["short_division_steps"]
        self.assertEqual(steps(30), ((30, 2, 15), (15, 3, 5), (5, 5, 1)))
        self.assertEqual(steps(60), ((60, 2, 30), (30, 2, 15),
                                     (15, 3, 5), (5, 5, 1)))
        for n in range(2, 501):
            rows = steps(n)
            self.assertEqual(rows[0][0], n)
            self.assertEqual(rows[-1][-1], 1)
            self.assertEqual(tuple(row[1] for row in rows), self.model["prime_factors"](n))
            for i, (dividend, divisor, quotient) in enumerate(rows):
                self.assertEqual(dividend, divisor * quotient)
                if i + 1 < len(rows):
                    self.assertEqual(quotient, rows[i + 1][0])

    def test_domain_and_scene_contract(self):
        for bad in (0, 1, -30, 2.0, True, False):
            for name in ("prime_factors", "short_division_steps"):
                with self.subTest(value=bad, method=name), self.assertRaises(ValueError):
                    self.model[name](bad)
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "PrimeFactorization")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_prime_composite", "show_definition",
                         "show_division_30", "show_division_60", "show_summary"} <= methods)
        self.assertIn('"\\\\times".join', source)
        self.assertNotIn('"\\text{{ 是素数}}"', source)
        self.assertIn("不计因数的顺序", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
