"""标准库数学回归：用 AST 仅提取课件中的纯数学函数，不加载 Manim。"""
import ast
from fractions import Fraction
from math import comb
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
LESSONS = {
    "gauss": ("01-计算与巧算/001-高斯求和/lesson.py", "arithmetic_sum"),
    "animals": ("02-典型应用题/002-鸡兔同笼/lesson.py", "solve_chicken_rabbit"),
    "fraction": ("03-分数与数形结合/003-分数乘法面积模型/lesson.py", "area_product"),
    "triangle": ("04-平面几何/004-等底等高/lesson.py", "triangle_area"),
    "butterfly": ("04-平面几何/005-蝴蝶模型/lesson.py", "butterfly_areas"),
    "encounter": ("05-行程问题/006-相遇问题/lesson.py", "encounter_time"),
    "union": ("06-集合与计数/007-容斥原理/lesson.py", "union_count"),
    "path": ("06-集合与计数/008-方格最短路径/lesson.py", "path_table"),
}


def models():
    functions = {}
    for key, (relative, name) in LESSONS.items():
        source = ROOT / relative
        syntax = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        matches = [node for node in syntax.body if isinstance(node, ast.FunctionDef) and node.name == name]
        if len(matches) != 1:
            raise AssertionError(f"expected exactly one model: {source}: {name}")
        isolated = ast.Module(body=matches, type_ignores=[])
        namespace = {"Fraction": Fraction, "comb": comb}
        exec(compile(isolated, str(source), "exec"), namespace)
        functions[key] = namespace[name]
    return functions


class MathModelsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.f = models()

    def test_gauss(self):
        self.assertEqual(self.f["gauss"](1), 1)
        self.assertEqual(self.f["gauss"](100), 5050)
        with self.assertRaises(ValueError): self.f["gauss"](0)

    def test_animals(self):
        self.assertEqual(self.f["animals"](8, 22), (5, 3))
        self.assertEqual(self.f["animals"](0, 0), (0, 0))
        for legs in (15, 17, 34):
            with self.assertRaises(ValueError): self.f["animals"](8, legs)

    def test_fraction(self):
        self.assertEqual(self.f["fraction"](3, 4, 2, 3), Fraction(1, 2))
        self.assertEqual(self.f["fraction"](0, 4, 2, 3), 0)
        with self.assertRaises(ValueError): self.f["fraction"](5, 4, 1, 2)

    def test_triangle(self):
        self.assertEqual(self.f["triangle"](6, 4), 12)
        self.assertEqual(self.f["triangle"](6, 0), 0)
        with self.assertRaises(ValueError): self.f["triangle"](0, 4)

    def test_butterfly(self):
        self.assertEqual(self.f["butterfly"](3, 6, 4), (2, 4, 8))
        self.assertEqual(self.f["butterfly"](6, 3, 4), (8, 4, 2))
        self.assertEqual(sum((2, 4, 4, 8)), Fraction((3 + 6) * 4, 2))
        with self.assertRaises(ValueError): self.f["butterfly"](3, 6, 0)

    def test_encounter(self):
        self.assertEqual(self.f["encounter"](200, 60, 40), 2)
        self.assertEqual(self.f["encounter"](12, 5, 1), 2)
        with self.assertRaises(ValueError): self.f["encounter"](200, 0, 0)

    def test_union(self):
        self.assertEqual(self.f["union"](12, 10, 4), 18)
        self.assertEqual(self.f["union"](4, 4, 4), 4)
        with self.assertRaises(ValueError): self.f["union"](3, 4, 5)

    def test_paths(self):
        self.assertEqual(self.f["path"](3, 2)[2][3], 10)
        self.assertEqual(self.f["path"](0, 0), [[1]])
        self.assertEqual(self.f["path"](3, 0), [[1, 1, 1, 1]])
        with self.assertRaises(ValueError): self.f["path"](-1, 2)


if __name__ == "__main__":
    unittest.main()
