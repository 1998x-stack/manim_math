"""不依赖 Manim 的课程数学与分镜数据回归。运行：python verify_divisibility.py。"""

import ast
import pathlib
import unittest


SOURCE = pathlib.Path(__file__).with_name("divisibility_meaning.py")


def divides(divisor: int, dividend: int) -> bool:
    """b|a 的定义：b 不为零，且 a=bq 对某个整数 q 成立。"""
    if not isinstance(divisor, int) or not isinstance(dividend, int):
        raise TypeError("整除关系只在整数之间定义")
    if divisor == 0:
        raise ValueError("除数不能为零")
    return dividend % divisor == 0


def equal_groups(total: int, groups: int) -> tuple[int, int]:
    """正整数组数下的均分结果：(每组数量, 剩余数量)。"""
    if not isinstance(total, int) or not isinstance(groups, int):
        raise TypeError("数量和组数必须是整数")
    if total < 0 or groups <= 0:
        raise ValueError("总量不能为负数，组数必须为正数")
    return divmod(total, groups)


class DivisibilityTests(unittest.TestCase):
    def test_divisible_and_non_divisible_examples(self):
        self.assertTrue(divides(3, 12))
        self.assertTrue(divides(4, 12))
        self.assertFalse(divides(5, 12))
        self.assertTrue(divides(-3, 12))
        self.assertTrue(divides(3, 0))
        self.assertFalse(divides(3, 10))

    def test_invalid_divisor_and_input_type(self):
        with self.assertRaises(ValueError):
            divides(0, 12)
        with self.assertRaises(TypeError):
            divides(3.0, 12)

    def test_twelve_squares_preserved_across_groupings(self):
        self.assertEqual(equal_groups(12, 3), (4, 0))
        self.assertEqual(equal_groups(12, 5), (2, 2))
        self.assertEqual(3 * 4 + 0, 12)
        self.assertEqual(5 * 2 + 2, 12)
        self.assertEqual(sum((4, 4, 4)), 12)
        self.assertEqual(sum((2, 2, 2, 2, 2, 2)), 12)

    def test_zero_and_invalid_group_counts(self):
        self.assertEqual(equal_groups(0, 3), (0, 0))
        self.assertEqual(equal_groups(2, 5), (0, 2))
        with self.assertRaises(ValueError):
            equal_groups(12, 0)
        with self.assertRaises(ValueError):
            equal_groups(-1, 3)

    def test_scene_entries_and_formula_content(self):
        """轻量静态回归；并不声称渲染或视觉验收。"""
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
        classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
        self.assertIn("DivisibilityMeaning", classes)
        self.assertIn("TestDivisibility", classes)
        scene = classes["DivisibilityMeaning"]
        methods = {n.name: n for n in scene.body if isinstance(n, ast.FunctionDef)}
        for method in (
            "show_opening", "show_concept", "show_example_divisible",
            "show_example_not_divisible", "show_factor_multiple",
            "show_notation", "show_outro",
        ):
            self.assertIn(method, methods)
        text_constants = [n.value for n in ast.walk(scene)
                          if isinstance(n, ast.Constant) and isinstance(n.value, str)]
        for required in (r"12=3\times4", r"12=5\times2+2", r"5\nmid12"):
            self.assertIn(required, text_constants)
        self.assertFalse(any("因数 ≤ 倍数" == text for text in text_constants))


if __name__ == "__main__":
    unittest.main(verbosity=2)
