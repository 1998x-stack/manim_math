"""四年级竖式计算与静态审查回归测试；不依赖 Manim/LaTeX/中文字体。"""

import ast
from pathlib import Path
import tempfile
import unittest

from tools.audit_grade4 import inspect_file

ROOT = Path(__file__).resolve().parents[1]
LESSON = (
    ROOT / "小学" / "四年级" / "第一学期"
    / "第三章-数的运算——三位数乘两位数"
    / "001笔算乘法(竖式计算)" / "001_笔算乘法(竖式计算).py"
)
WRAPPER = LESSON.with_name("001笔算乘法_竖式计算__animation.py")


def load_pure_steps():
    """只提取数学函数，避免导入依赖 Manim 的动画模块。"""
    tree = ast.parse(LESSON.read_text(encoding="utf-8"), filename=str(LESSON))
    function = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "multiplication_steps"
    )
    isolated = ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[]))
    namespace = {}
    exec(compile(isolated, str(LESSON), "exec"), namespace)
    return namespace["multiplication_steps"]


class ColumnMultiplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.steps = staticmethod(load_pure_steps())

    def test_example_with_carries(self):
        self.assertEqual(self.steps(123, 45), (615, 4920, 5535))

    def test_zero_in_multiplicand_and_multiplier(self):
        self.assertEqual(self.steps(105, 40), (0, 4200, 4200))
        self.assertEqual(self.steps(204, 30), (0, 6120, 6120))

    def test_maximum_three_by_two_digit_case(self):
        self.assertEqual(self.steps(999, 99), (8991, 89910, 98901))

    def test_every_valid_operand_pair(self):
        for a in range(100, 1000):
            for b in range(10, 100):
                ones, tens, total = self.steps(a, b)
                self.assertEqual(ones + tens, a * b)
                self.assertEqual(ones % 10, (a * b) % 10)
                self.assertEqual(tens % 10, 0)

    def test_rejects_wrong_operand_types_or_sizes(self):
        for a, b in ((99, 45), (1000, 45), (123, 9), (123, 100), (True, 45), (123, 4.5)):
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                self.steps(a, b)

    def test_both_scene_files_are_syntactically_valid(self):
        for path in (LESSON, WRAPPER):
            with self.subTest(file=path.name):
                ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    def test_portrait_configuration_precedes_scene_definition(self):
        tree = ast.parse(LESSON.read_text(encoding="utf-8"))
        scene_index = next(i for i, node in enumerate(tree.body) if isinstance(node, ast.ClassDef))
        config_nodes = [
            node for node in tree.body[:scene_index]
            if isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Attribute)
            and isinstance(node.targets[0].value, ast.Name)
            and node.targets[0].value.id == "config"
        ]
        self.assertEqual(len(config_nodes), 4)

    def test_auditor_reports_syntax_errors_and_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            broken = root / "broken.py"
            broken.write_text("class Broken(:\n    pass\n", encoding="utf-8")
            self.assertTrue(inspect_file(broken, root)["errors"])
            placeholder = root / "placeholder.py"
            placeholder.write_text("class Demo:\n    note = '正在学习'\n", encoding="utf-8")
            report = inspect_file(placeholder, root)
            self.assertFalse(report["errors"])
            self.assertTrue(any("占位" in msg for msg in report["warnings"]))


if __name__ == "__main__":
    unittest.main()
