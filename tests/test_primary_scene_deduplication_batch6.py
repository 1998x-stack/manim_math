"""Sixth primary deduplication batch: five real lesson owners and exact math helpers.

No Manim import or video rendering required. Functions are extracted from the
same source files whose Scenes will be rendered in production.
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
    "equation": (
        "小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/001一元一次方程的解法",
        "001一元一次方程的解法_animation.py", "001_一元一次方程的解法.py",
        "Topic001一元一次方程的解法Animation", "b4fb824ca8",
    ),
    "system": (
        "小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/002二元一次方程组",
        "002二元一次方程组_animation.py", "002_二元一次方程组.py",
        "Topic002二元一次方程组Animation", "3875f23dcf",
    ),
    "inequality": (
        "小学/六年级/第一学期/第六章-一次方程(组)和一次不等式(组)/003不等式及其性质",
        "003不等式及其性质_animation.py", "003_不等式及其性质.py",
        "Topic003不等式及其性质Animation", "1994079dfc",
    ),
    "direct": (
        "小学/六年级/第二学期/第二章-比例/001正比例",
        "001正比例_animation.py", "001_正比例.py",
        "Topic001正比例Animation", "8883bec7e6",
    ),
    "pigeonhole": (
        "小学/六年级/第二学期/第五章-整理与提高/001抽屉原理",
        "001抽屉原理_animation.py", "001_抽屉原理.py",
        "Topic001抽屉原理Animation", "843369bcf3",
    ),
}


def pure_helper(course: str, name: str):
    folder, source, *_ = LESSONS[course]
    path = ROOT / folder / source
    parsed = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    selected = [node for node in parsed.body
                if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(selected) != 1:
        raise AssertionError(f"{path}: expected exactly one {name}")
    namespace = {}
    isolated = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    exec(compile(isolated, str(path), "exec"), namespace)
    return namespace[name]


def gallery_topics():
    d = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
    topics = [
        t for level in d["levels"]
        for g in level.get("grades", [])
        for s in g.get("semesters", [])
        for ch in s.get("chapters", [])
        for t in ch.get("topics", [])
    ]
    return topics


class BatchSixDeduplicationTests(unittest.TestCase):
    def test_every_topic_has_only_one_real_scene_and_no_template(self):
        for key, (folder, source, obsolete, scene, _id) in LESSONS.items():
            with self.subTest(topic=key):
                directory = ROOT / folder
                self.assertFalse((directory / obsolete).exists())
                py_files = [
                    p for p in directory.glob("*.py")
                    if not p.name.startswith(("verify_", "test_", "__"))
                ]
                self.assertEqual([p.name for p in py_files], [source])
                self.assertEqual(find_scene_py(directory), directory / source)
                code = (directory / source).read_text(encoding="utf-8")
                self.assertNotIn("正在学习", code)
                self.assertNotIn("更多动画元素可以根据需要添加", code)
                self.assertIn("上海初高中数学直通车", code)
                tree = ast.parse(code)
                scenes = [
                    cls.name for cls in tree.body
                    if isinstance(cls, ast.ClassDef)
                    and any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in cls.bases)
                ]
                self.assertEqual(scenes, [scene])
                # Avoid unrelated Chinese text inside LaTeX math literals.
                for node in ast.walk(tree):
                    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                            and node.func.id == "MathTex"):
                        for arg in node.args:
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                self.assertTrue(arg.value.isascii(), (source, arg.value))
                methods = [
                    node.name for cls in tree.body
                    if isinstance(cls, ast.ClassDef) and cls.name == scene
                    for node in cls.body if isinstance(node, ast.FunctionDef)
                ]
                self.assertGreaterEqual(len(methods), 4)
                self.assertIn("construct", methods)

    def test_catalog_keep_ids_and_exact_media_links(self):
        all_rows = gallery_topics()
        self.assertEqual(len(all_rows), 534)
        self.assertEqual(len({r["id"] for r in all_rows}), 534)
        mapping = {r["id"]: r for r in all_rows}
        for key, (folder, source, _obsolete, scene, topic_id) in LESSONS.items():
            with self.subTest(topic=key):
                record = mapping[topic_id]
                self.assertEqual(record["pyFile"], folder + "/" + source)
                self.assertEqual(record["videoFile"], folder + "/" + scene + "_finish.mp4")
                self.assertTrue(record["hasVideo"])

    def test_exact_fraction_equation_solver(self):
        solve = pure_helper("equation", "solve_fraction_equation")
        self.assertEqual(solve(Fraction(1, 2), Fraction(1, 3), Fraction(5, 6)), 1)
        self.assertEqual(solve(2, 1, 9), 4)
        self.assertEqual(solve(3, 2, 3), Fraction(1, 3))
        for a in (-5, -2, 1, 2, 7):
            for b in range(-4, 5):
                for x in range(-4, 5):
                    self.assertEqual(solve(a, b, a * x + b), x)
        for args in ((0, 1, 2), (True, 0, 1), (1.5, 0, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                solve(*args)

    def test_two_variable_system_unique_solution_and_substitution(self):
        solve = pure_helper("system", "solve_linear_system")
        self.assertEqual(solve(1, 1, 5, 1, -1, 1), (3, 2))
        self.assertEqual(solve(2, 3, 12, 1, -1, 1), (3, 2))
        for a, b, d, e in ((1, 1, 1, -1), (2, 3, 1, -1),
                           (3, -2, 1, 4), (-1, 5, 2, -1)):
            for x, y in ((0, 0), (3, 2), (-2, 5)):
                c, f = a * x + b * y, d * x + e * y
                self.assertEqual(solve(a, b, c, d, e, f), (x, y))
        for args in ((1, 1, 2, 2, 2, 4), (True, 1, 3, 1, 1, 4)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                solve(*args)

    def test_inequality_reverses_only_for_negative_factor(self):
        f = pure_helper("inequality", "transformed_inequality")
        self.assertEqual(f(5, 3, -2), (3, 1, ">"))
        self.assertEqual(f(5, 3, factor=2), (10, 6, ">"))
        self.assertEqual(f(5, 3, factor=-2), (-10, -6, "<"))
        self.assertEqual(f(5, 3, factor=0), (0, 0, "="))
        for a in range(-3, 7):
            for b in range(-7, a):
                for factor in (-3, -1, 0, 1, 5):
                    left, right, relation = f(a, b, 2, factor)
                    self.assertEqual(left - right, (a - b) * factor)
                    self.assertEqual(relation, "<" if factor < 0 else ">" if factor > 0 else "=")
        for args in ((3, 5, 0, 1), (True, 3, 0, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                f(*args)

    def test_proportional_ratio_and_zero_origin(self):
        rate = pure_helper("direct", "direct_proportion_rate")
        self.assertEqual(rate(((1, 2), (2, 4), (3, 6))), 2)
        self.assertEqual(rate(((0, 0), (1, 2), (-3, -6))), 2)
        self.assertEqual(rate(((2, 1), (4, 2))), Fraction(1, 2))
        self.assertIsNone(rate(((1, 2), (2, 5))))
        self.assertIsNone(rate(((0, 2), (1, 2))))
        self.assertIsNone(rate(((1, 0), (2, 0))))  # k=0 excluded by lesson contract.
        for data in ([], [(1, 2)], [(True, 1), (2, 4)], [(1, 2, 3), (4, 5)]):
            with self.subTest(data=data), self.assertRaises(ValueError):
                rate(data)

    def test_pigeonhole_ceil_bound(self):
        f = pure_helper("pigeonhole", "pigeonhole_lower_bound")
        self.assertEqual(f(4, 3), 2)
        self.assertEqual(f(10, 3), 4)
        for boxes in range(1, 15):
            for objects in range(0, 80):
                m = f(objects, boxes)
                self.assertGreaterEqual(m * boxes, objects)
                self.assertLess((m - 1) * boxes, objects) if objects else self.assertEqual(m, 0)
        for args in ((1, 0), (-1, 2), (True, 2), (2, 1.5)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                f(*args)


if __name__ == "__main__":
    unittest.main()
