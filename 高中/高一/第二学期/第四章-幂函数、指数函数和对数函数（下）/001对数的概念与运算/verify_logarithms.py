"""无需导入 Manim 的本课数学回归。

python -m unittest verify_logarithms.py -v
"""

import ast
import math
from pathlib import Path
import unittest


SCENE = Path(__file__).with_name("logarithm_concepts.py")


def log_base(value, base):
    if not (math.isfinite(value) and value > 0):
        raise ValueError("真数必须为正有限实数")
    if not (math.isfinite(base) and base > 0 and base != 1):
        raise ValueError("底数必须为正有限实数且不等于 1")
    return math.log(value) / math.log(base)


class LogarithmMathTests(unittest.TestCase):
    def test_exponent_logarithm_equivalence(self):
        for base in (0.5, 2.0, 10.0):
            for exponent in (-3.0, 0.0, 0.5, 3.0):
                with self.subTest(base=base, exponent=exponent):
                    self.assertAlmostEqual(log_base(base ** exponent, base), exponent)

    def test_invalid_domains(self):
        for base, value in ((0, 8), (1, 8), (-2, 8), (2, 0),
                            (2, -8), (float("inf"), 8), (2, float("nan"))):
            with self.subTest(base=base, value=value):
                with self.assertRaises(ValueError):
                    log_base(value, base)

    def test_special_logs_and_identities(self):
        self.assertAlmostEqual(log_base(100, 10), 2)
        self.assertAlmostEqual(log_base(math.e, math.e), 1)
        for base in (0.5, 2, 3):
            self.assertAlmostEqual(log_base(1, base), 0)
            self.assertAlmostEqual(log_base(base, base), 1)
            for value in (0.25, 1, 8):
                self.assertAlmostEqual(base ** log_base(value, base), value)

    def test_product_and_quotient(self):
        for base in (0.5, 2, 10):
            for left, right in ((4, 8), (0.25, 3), (1, 2)):
                self.assertAlmostEqual(
                    log_base(left * right, base),
                    log_base(left, base) + log_base(right, base),
                )
                self.assertAlmostEqual(
                    log_base(left / right, base),
                    log_base(left, base) - log_base(right, base),
                )

    def test_power_and_change_of_base(self):
        for base in (0.5, 2, 10):
            for value in (0.5, 8):
                for exponent in (-2, 0, 1.5):
                    self.assertAlmostEqual(
                        log_base(value ** exponent, base),
                        exponent * log_base(value, base),
                    )
                for new_base in (0.25, 3, math.e):
                    self.assertAlmostEqual(
                        log_base(value, base),
                        log_base(value, new_base) / log_base(base, new_base),
                    )
        self.assertAlmostEqual(log_base(8, 2), math.log10(8) / math.log10(2))
        self.assertAlmostEqual(log_base(8, 2), 3)

    def test_seven_scene_entrypoints_and_mathtex_sources(self):
        source = SCENE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        scene = next(node for node in tree.body
                     if isinstance(node, ast.ClassDef) and node.name == "LogarithmConcepts")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        for number in range(1, 8):
            self.assertTrue(any(name.startswith(f"scene_{number}_") for name in methods))
        for node in ast.walk(scene):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            if node.func.attr == "_page":
                self.assertIsInstance(node.args[1], ast.List)
                for card in node.args[1].elts:
                    self.assertIsInstance(card, ast.Tuple)
                    self.assertIsInstance(card.elts[1], ast.List)
                    for formula in card.elts[1].elts:
                        self.assertIsInstance(formula, ast.Constant)
                        self.assertIsInstance(formula.value, str)
                        self.assertFalse(any("\u3400" <= character <= "\u9fff" for character in formula.value))
        self.assertIn(r"\log_2 8=\frac{\lg 8}{\lg 2}=3", source)


if __name__ == "__main__":
    unittest.main()
