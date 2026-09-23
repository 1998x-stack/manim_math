"""无需安装 Manim 的数轴数学规格与源码结构检查。"""
import ast
import json
import unittest
from fractions import Fraction
from pathlib import Path

DIR = Path(__file__).resolve().parent
SOURCE = (DIR / "number_line_lesson.py").read_text(encoding="utf-8")
TREE = ast.parse(SOURCE)
MODEL = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and
             n.name == "number_line_coordinate")
NAMESPACE = {}
exec(compile(ast.Module(body=[MODEL], type_ignores=[]), str(DIR / "number_line_lesson.py"), "exec"), NAMESPACE)
coordinate = NAMESPACE["number_line_coordinate"]


class NumberLineContract(unittest.TestCase):
    def test_origin_and_direction(self):
        self.assertEqual(coordinate(0), 0)
        self.assertLess(coordinate(-1), coordinate(0))
        self.assertLess(coordinate(0), coordinate(1))

    def test_equal_steps_and_fraction(self):
        self.assertAlmostEqual(coordinate(3) - coordinate(2), coordinate(1))
        self.assertAlmostEqual(coordinate(Fraction(1, 2)), coordinate(1) / 2)
        self.assertAlmostEqual(coordinate(Fraction(-3, 2)), coordinate(-1.5))

    def test_invalid_unit_length(self):
        for unit in (0, -1):
            with self.subTest(unit=unit), self.assertRaises(ValueError):
                coordinate(1, unit)

    def test_comparison_order(self):
        for a, b in [(-3, -2), (-1, 2), (0, 0.5), (2.5, 3)]:
            with self.subTest(a=a, b=b):
                self.assertLess(coordinate(a), coordinate(b))

    def test_scene_structure_and_no_false_bijection(self):
        scenes = [n for n in TREE.body if isinstance(n, ast.ClassDef) and n.name == "NumberLineLesson"]
        self.assertEqual(len(scenes), 1)
        self.assertIn("number_line.n2p(value)", SOURCE)
        self.assertIn("数轴上也有无理数对应的点", SOURCE)
        self.assertNotIn("每个点对应一个有理数", SOURCE)
        self.assertNotIn("always_redraw", SOURCE)
        metadata = json.loads((DIR / "description.json").read_text(encoding="utf-8"))
        self.assertIn("不一定对应有理数", metadata["知识点内容详细描述"])


if __name__ == "__main__":
    unittest.main()
