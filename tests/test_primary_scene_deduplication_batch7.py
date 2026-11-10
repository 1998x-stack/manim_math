"""Batch 7: one Scene per topic, exact math, stable Gallery and no placeholder.

AST isolates helpers without importing Manim or rendering a video.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import json
from pathlib import Path
import unittest

from assets.build_catalog import find_scene_py

ROOT = Path(__file__).resolve().parents[1]
LESSONS = {
    "inequality": {
        "folder": "小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/004一元一次不等式的解法",
        "keep": "004一元一次不等式的解法_animation.py",
        "deleted": "004_一元一次不等式的解法.py",
        "scene": "Topic004一元一次不等式的解法Animation",
        "id": "50da4a7d82",
    },
    "division": {
        "folder": "小学/六年级/第一学期/第一章-数的整除/001整数与整除",
        "keep": "001整数与整除_animation.py",
        "deleted": "001_整数与整除.py",
        "scene": "Topic001整数与整除Animation",
        "id": "0f6a97a71a",
    },
    "circle": {
        "folder": "小学/六年级/第一学期/第四章-圆和扇形/001圆的认识",
        "keep": "001圆的认识_animation.py",
        "deleted": "001_圆的认识.py",
        "scene": "Topic001圆的认识Animation",
        "id": "df4bbd48d1",
    },
    "rational": {
        "folder": "小学/六年级/第一学期/第五章-有理数/001有理数的意义",
        "keep": "001有理数的意义_animation.py",
        "deleted": "001_有理数的意义.py",
        "scene": "Topic001有理数的意义Animation",
        "id": "982929f902",
    },
}


def pure_function(course: str, name: str):
    lesson = LESSONS[course]
    path = ROOT / lesson["folder"] / lesson["keep"]
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(f"{path}: expected one function {name}")
    module = ast.fix_missing_locations(ast.Module(body=matches, type_ignores=[]))
    namespace = {}
    exec(compile(module, str(path), "exec"), namespace)
    return namespace[name]


def gallery_items():
    source = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
    return [
        topic for level in source["levels"]
        for grade in level.get("grades", [])
        for semester in grade.get("semesters", [])
        for chapter in semester.get("chapters", [])
        for topic in chapter.get("topics", [])
    ]


class BatchSevenSceneTests(unittest.TestCase):
    def test_one_direct_scene_and_no_obsolete_or_placeholder(self):
        for name, lesson in LESSONS.items():
            with self.subTest(course=name):
                directory = ROOT / lesson["folder"]
                self.assertFalse((directory / lesson["deleted"]).exists())
                python_files = [
                    f.name for f in directory.glob("*.py")
                    if not f.name.startswith(("test_", "verify_", "__"))
                ]
                self.assertEqual(python_files, [lesson["keep"]])
                self.assertEqual(find_scene_py(directory), directory / lesson["keep"])
                code = (directory / lesson["keep"]).read_text(encoding="utf-8")
                for placeholder in ("正在学习", "更多动画元素可以根据需要添加", "这是一个重要的数学概念"):
                    self.assertNotIn(placeholder, code)
                self.assertIn("上海初高中数学直通车", code)
                self.assertIn("config.frame_width = 9", code)
                self.assertIn("config.frame_height = 16", code)
                tree = ast.parse(code)
                declared = [
                    cls.name for cls in tree.body
                    if isinstance(cls, ast.ClassDef)
                    and any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in cls.bases)
                ]
                self.assertEqual(declared, [lesson["scene"]])
                for node in ast.walk(tree):
                    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                            and node.func.id == "MathTex"):
                        for arg in node.args:
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                self.assertTrue(arg.value.isascii(), (name, arg.value))

    def test_catalog_keeps_exact_ids_videos_and_total(self):
        items = gallery_items()
        self.assertEqual(len(items), 534)
        by_id = {topic["id"]: topic for topic in items}
        self.assertEqual(len(by_id), 534)
        for key, lesson in LESSONS.items():
            with self.subTest(topic=key):
                row = by_id[lesson["id"]]
                self.assertEqual(row["pyFile"], lesson["folder"] + "/" + lesson["keep"])
                self.assertEqual(
                    row["videoFile"],
                    lesson["folder"] + "/" + lesson["scene"] + "_finish.mp4"
                )
                self.assertTrue(row["hasVideo"])

    def test_linear_inequality_exact_boundary_and_direction(self):
        solver = pure_function("inequality", "solve_linear_inequality")
        self.assertEqual(solver(2, 3, 7, ">"), (">", 2))
        self.assertEqual(solver(-2, 3, 7, ">"), ("<", -2))
        self.assertEqual(solver(2, 3, 7, ">="), (">=", 2))
        self.assertEqual(solver(3, 0, 2, "<"), ("<", Fraction(2, 3)))
        comparisons = {
            ">": lambda x, y: x > y,
            ">=": lambda x, y: x >= y,
            "<": lambda x, y: x < y,
            "<=": lambda x, y: x <= y,
        }
        for a in range(-4, 5):
            if a == 0:
                continue
            for b in (-3, 0, 2):
                for c in (-2, 1, 4):
                    for relation, cmp in comparisons.items():
                        new_relation, bound = solver(a, b, c, relation)
                        for x in range(-5, 6):
                            self.assertEqual(
                                cmp(a * x + b, c),
                                comparisons[new_relation](x, bound),
                                (a, b, c, relation, x)
                            )
        for args in ((0, 1, 2, ">"), (2, 3, 4, "="), (True, 2, 4, ">")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                solver(*args)

    def test_integer_division_direction_and_zero_remainder(self):
        calc = pure_function("division", "integer_division")
        self.assertEqual(calc(12, 3), (4, 0, True))
        self.assertEqual(calc(13, 3), (4, 1, False))
        self.assertEqual(calc(-12, 3), (-4, 0, True))
        for a in range(-20, 21):
            for b in range(-9, 10):
                if b == 0:
                    continue
                quotient, remainder, divides = calc(a, b)
                self.assertEqual(a, b * quotient + remainder)
                self.assertTrue(0 <= remainder < abs(b))
                self.assertIs(divides, remainder == 0)
        for args in ((3, 0), (True, 3), (12, 2.5)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                calc(*args)

    def test_circle_radius_diameter(self):
        measure = pure_function("circle", "circle_measurements")
        self.assertEqual(measure(2), (Fraction(2), Fraction(4)))
        self.assertEqual(measure(Fraction(3, 2)), (Fraction(3, 2), Fraction(3)))
        for radius in range(1, 50):
            r, d = measure(radius)
            self.assertEqual(d, 2 * r)
        for radius in (0, -2, True, 1.5):
            with self.subTest(radius=radius), self.assertRaises(ValueError):
                measure(radius)
        code = (ROOT / LESSONS["circle"]["folder"] / LESSONS["circle"]["keep"]).read_text(encoding="utf-8")
        self.assertIn("圆规", code)
        self.assertIn("对称轴", code)

    def test_rational_numbers_integers_fractions_finite_and_repeating(self):
        make = pure_function("rational", "rational_fraction")
        repeat = pure_function("rational", "pure_repeating_decimal")
        self.assertEqual(make(-2, 1), -2)
        self.assertEqual(make(0, 7), 0)
        self.assertEqual(make(3, 4), Fraction(3, 4))
        self.assertEqual(make(75, 100), Fraction(3, 4))
        self.assertEqual(make(1, -2), Fraction(-1, 2))
        self.assertEqual(repeat("3"), Fraction(1, 3))
        self.assertEqual(repeat("12"), Fraction(4, 33))
        self.assertEqual(repeat("9"), 1)
        self.assertEqual(repeat("0"), 0)
        for args in ((1, 0), (True, 2), (2.0, 3)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                make(*args)
        for value in ("", "abc", "3.3", "٣", None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                repeat(value)


if __name__ == "__main__":
    unittest.main()
