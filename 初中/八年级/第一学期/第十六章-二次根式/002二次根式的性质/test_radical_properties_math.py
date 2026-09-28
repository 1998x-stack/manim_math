"""不导入 Manim 的本课数学与源码契约回归：python -m unittest test_radical_properties_math.py -v。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("radical_properties.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
HELPERS = {"root_then_square", "square_then_root"}
NODES = [node for node in TREE.body if isinstance(node, ast.FunctionDef) and node.name in HELPERS]
NAMESPACE = {"math": math}
exec(compile(ast.Module(body=NODES, type_ignores=[]), str(SOURCE), "exec"), NAMESPACE)


class RadicalPropertiesMathTests(unittest.TestCase):
    def test_two_pure_math_helpers_exist(self):
        self.assertEqual({node.name for node in NODES}, HELPERS)

    def test_first_property_for_nonnegative_values(self):
        for value in (0, 1e-8, 0.25, 1, 2, 5, 9, 100):
            with self.subTest(value=value):
                self.assertTrue(math.isclose(NAMESPACE["root_then_square"](value),
                                             value, rel_tol=1e-12, abs_tol=1e-12))

    def test_first_property_rejects_negative_domain(self):
        for value in (-9, -3, -1e-8):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    NAMESPACE["root_then_square"](value)

    def test_second_property_all_signs(self):
        for value in (-12, -5, -3, -0.25, 0, 0.25, 3, 5, 12):
            with self.subTest(value=value):
                result = NAMESPACE["square_then_root"](value)
                self.assertEqual(result, abs(value))
                self.assertTrue(math.isclose(result, math.sqrt(value * value)))
                self.assertGreaterEqual(result, 0)

    def test_negative_counterexample_and_zero(self):
        self.assertEqual(NAMESPACE["square_then_root"](-3), 3)
        self.assertNotEqual(NAMESPACE["square_then_root"](-3), -3)
        self.assertEqual(NAMESPACE["square_then_root"](0), 0)
        self.assertEqual(NAMESPACE["root_then_square"](0), 0)

    def test_reject_nonfinite_values_in_examples(self):
        for name in HELPERS:
            for value in (float("nan"), float("inf"), -float("inf")):
                with self.subTest(helper=name, value=value):
                    with self.assertRaises(ValueError):
                        NAMESPACE[name](value)

    def test_scene_identity_and_seven_sections(self):
        scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "QuadraticRadicalProperties")
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({f"scene_{i}_{suffix}" for i, suffix in (
            (1, "hook"), (2, "review"), (3, "prop1"), (4, "prop2_trap"),
            (5, "prop2_full"), (6, "pitfall"), (7, "summary"),
        )}.issubset(methods))
        source = SOURCE.read_text(encoding="utf-8")
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)

    def test_pitfall_cards_have_math_consistent_marks(self):
        self.assertTrue(math.isclose(NAMESPACE["square_then_root"](-5), 5))
        self.assertTrue(math.isclose(NAMESPACE["square_then_root"](-2), 2))
        self.assertNotEqual(math.sqrt(4), -2)
        self.assertNotEqual(NAMESPACE["square_then_root"](-5), -5)


if __name__ == "__main__":
    unittest.main()
