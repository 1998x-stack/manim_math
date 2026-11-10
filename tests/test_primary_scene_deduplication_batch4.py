"""Pure-Python contracts for batch four's six retained primary-school Scenes."""
from __future__ import annotations

import ast
from fractions import Fraction
import json
from pathlib import Path
import unittest

from assets.build_catalog import find_scene_py

ROOT = Path(__file__).resolve().parents[1]
LESSONS = {
    "lines": ("小学/四年级/第一学期/第五章-几何小实践——圆与角/001线段、射线、直线",
              "001_线段射线直线.py", "001_线段、射线、直线.py",
              "LineSegmentRayLesson", "6ce457db4d", "LineSegmentRayLesson_finish.mp4"),
    "letters": ("小学/五年级/第一学期/第四章-简易方程(一)/001用字母表示数",
                "001_用字母表示数.py", "001用字母表示数_animation.py",
                "LetterRepresentLesson", "2e1ca2aed3", "LetterRepresentLesson_finish.mp4"),
    "meaning": ("小学/五年级/第一学期/第四章-简易方程(一)/002方程的意义",
                "002_方程的意义.py", "002方程的意义_animation.py",
                "EquationMeaningLesson", "a85b511269", "EquationMeaningLesson_finish.mp4"),
    "solving": ("小学/五年级/第一学期/第四章-简易方程(一)/004解简易方程",
                "004_解简易方程.py", "004解简易方程_animation.py",
                "SolveEquationLesson", "de012f5986", "SolveEquationLesson_finish.mp4"),
    "statistics": ("小学/六年级/第二学期/第四章-统计与概率/002平均数、中位数、众数",
                   "002_平均数中位数众数.py", "002_平均数、中位数、众数.py",
                   "MeanMedianModeLesson", "c989d22f18", "MeanMedianModeLesson_finish.mp4"),
    "probability": ("小学/六年级/第二学期/第四章-统计与概率/003可能性(概率的初步)",
                    "003_可能性.py", "003_可能性(概率的初步).py",
                    "ProbabilityIntroLesson", "c01d77a5f9", "ProbabilityIntroLesson_finish.mp4"),
}


def load_helper(lesson: str, name: str):
    folder, filename, *_ = LESSONS[lesson]
    file = ROOT / folder / filename
    tree = ast.parse(file.read_text(encoding="utf-8"), filename=str(file))
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(nodes) != 1:
        raise AssertionError(f"missing or duplicated helper: {file}:{name}")
    ns = {}
    module = ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[]))
    exec(compile(module, str(file), "exec"), ns)
    return ns[name]


def catalog_items():
    catalog = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
    return {
        topic["id"]: topic
        for lv in catalog["levels"]
        for grade in lv.get("grades", [])
        for sem in grade.get("semesters", [])
        for ch in sem.get("chapters", [])
        for topic in ch.get("topics", [])
    }


class PrimarySceneDeduplicationBatchFourTests(unittest.TestCase):
    def test_each_lesson_has_one_scene_and_deleted_version_is_absent(self):
        for key, (folder, filename, removed, scene, _id, _video) in LESSONS.items():
            with self.subTest(lesson=key):
                directory = ROOT / folder
                self.assertTrue((directory / filename).is_file())
                self.assertFalse((directory / removed).exists())
                scene_files = sorted(
                    p.name for p in directory.glob("*.py")
                    if not p.name.startswith(("test_", "verify_", "__"))
                )
                self.assertEqual(scene_files, [filename])
                self.assertEqual(find_scene_py(directory), directory / filename)
                tree = ast.parse((directory / filename).read_text(encoding="utf-8"))
                classes = [
                    node.name for node in tree.body
                    if isinstance(node, ast.ClassDef)
                    and any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in node.bases)
                ]
                self.assertEqual(classes, [scene])

    def test_gallery_sources_and_media_are_stable(self):
        topics = catalog_items()
        self.assertEqual(len(topics), 534)
        for key, (folder, filename, _removed, _scene, topic_id, video_name) in LESSONS.items():
            with self.subTest(lesson=key):
                self.assertIn(topic_id, topics)
                topic = topics[topic_id]
                self.assertEqual(topic["pyFile"], folder + "/" + filename)
                self.assertEqual(topic["videoFile"], folder + "/" + video_name)
                self.assertTrue(topic["hasVideo"])

    def test_letter_simplification(self):
        product = load_helper("letters", "literal_product")
        self.assertEqual(product(0, "a"), "0")
        self.assertEqual(product(1, "a"), "a")
        self.assertEqual(product(-1, "x"), "-x")
        self.assertEqual(product(5, "a"), "5a")
        self.assertEqual(product(-3, "x"), "-3x")
        for args in ((True, "a"), (2.5, "a"), (3, "xy"), (2, "")):
            with self.subTest(args=args), self.assertRaises(ValueError):
                product(*args)

    def test_equation_classifier_matches_course_exercises(self):
        classifier = load_helper("meaning", "is_equation")
        examples = (
            (r"x + 3 = 10", True),
            (r"5 + 7 = 12", False),
            (r"2x - 1 = 9", True),
            (r"3x + 2 > 8", False),
            (r"y = 4", True),
            (r"6 \times 3", False),
            (r"6 \times 3 = 18", False),
        )
        for expression, expected in examples:
            with self.subTest(expression=expression):
                self.assertIs(classifier(expression), expected)
        with self.assertRaises(ValueError):
            classifier(None)

    def test_exact_linear_equation_solver(self):
        solve = load_helper("solving", "solve_linear_equation")
        self.assertEqual(solve(1, 8, 15), Fraction(7))
        self.assertEqual(solve(3, 0, 24), Fraction(8))
        self.assertEqual(solve(2, 3, 4), Fraction(1, 2))
        self.assertEqual(solve(-3, 2, -4), Fraction(2))
        for args in ((0, 3, 5), (True, 3, 5), (2.5, 1, 8)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                solve(*args)

    def test_statistics_for_odd_even_unimodal_and_ties(self):
        stats = load_helper("statistics", "describe_data")
        self.assertEqual(stats([85, 90, 78, 90, 92]), (Fraction(87), Fraction(90), (90,)))
        self.assertEqual(stats([1, 2, 3, 4]), (Fraction(5, 2), Fraction(5, 2), ()))
        self.assertEqual(stats([1, 1, 2, 2, 3]), (Fraction(9, 5), Fraction(2), (1, 2)))
        for values in ([], [True, 1], [1.2, 3]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                stats(values)

    def test_equal_probability_requires_valid_count(self):
        probability = load_helper("probability", "probability_from_equal_outcomes")
        self.assertEqual(probability(1, 2), Fraction(1, 2))
        self.assertEqual(probability(3, 6), Fraction(1, 2))
        self.assertEqual(probability(0, 6), Fraction(0))
        self.assertEqual(probability(6, 6), Fraction(1))
        for favorable, total in ((-1, 3), (4, 3), (1, 0), (True, 3), (1, False)):
            with self.subTest(favorable=favorable, total=total), self.assertRaises(ValueError):
                probability(favorable, total)

    def test_segment_ray_line_traits_are_consistent(self):
        traits = load_helper("lines", "shape_traits")
        self.assertEqual(traits("segment"), ("2 个", "有限", "不延伸"))
        self.assertEqual(traits("ray"), ("1 个", "无限", "一端"))
        self.assertEqual(traits("line"), ("0 个", "无限", "两端"))
        with self.assertRaises(ValueError):
            traits("circle")


if __name__ == "__main__":
    unittest.main()
