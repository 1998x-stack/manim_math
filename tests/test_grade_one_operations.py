"""Check the arithmetic used by the grade-one stepwise animation without Manim."""

import ast
from pathlib import Path
import unittest


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "小学/一年级/上册/第二章-10以内数的加减法/005连加、连减、加减混合"
    / "005_连加、连减、加减混合.py"
)


def load_calculator():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    functions = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "calculate_steps"
    ]
    if len(functions) != 1:
        raise AssertionError("计算函数在原课程源码中缺失")
    namespace = {}
    exec(compile(ast.fix_missing_locations(ast.Module(body=functions, type_ignores=[])),
                 str(SOURCE), "exec"), namespace)
    return namespace["calculate_steps"]


class StepwiseOperationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calculate_steps = staticmethod(load_calculator())

    def test_three_course_examples(self):
        self.assertEqual(self.calculate_steps(2, 3, 1, "+", "+"), (5, 6))
        self.assertEqual(self.calculate_steps(5, 2, 1, "-", "-"), (3, 2))
        self.assertEqual(self.calculate_steps(5, 2, 3, "+", "-"), (7, 4))

    def test_subtraction_order_is_left_to_right(self):
        self.assertEqual(self.calculate_steps(8, 3, 2, "-", "-"), (5, 3))
        self.assertEqual(self.calculate_steps(5, 3, 2, "-", "+"), (2, 4))

    def test_zero_and_ten(self):
        self.assertEqual(self.calculate_steps(0, 10, 10, "+", "-"), (10, 0))
        self.assertEqual(self.calculate_steps(10, 0, 0, "-", "+"), (10, 10))

    def test_invalid_amounts_and_symbols(self):
        invalid = (
            (-1, 1, 1, "+", "+"),
            (11, 0, 0, "+", "+"),
            (True, 1, 0, "+", "+"),
            (5, 6, 0, "+", "+"),
            (1, 2, 0, "-", "+"),
            (1, 0, 0, "*", "+"),
        )
        for args in invalid:
            with self.subTest(args=args), self.assertRaises(ValueError):
                self.calculate_steps(*args)


if __name__ == "__main__":
    unittest.main()
