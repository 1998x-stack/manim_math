"""Pure-Python regression for the three deduplicated primary-school lessons.

No Manim import, rendering, media mutation, or video-file read.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import unittest

from assets.build_catalog import find_scene_py

ROOT = Path(__file__).resolve().parents[1]
LESSONS = {
    "grade1": (
        "小学/一年级/上册/第二章-10以内数的加减法/005连加、连减、加减混合",
        "005_连加连减加减混合.py", "ConsecutiveOperationsLesson",
    ),
    "grade2": (
        "小学/二年级/上册/第三章-乘法、除法（二）/002有余数的除法",
        "you_shu_shu_de_chu_fa.py", "YouShuShuDeChuFa",
    ),
    "grade3": (
        "小学/三年级/上册/第四章-用一位数除/001两位数除以一位数（竖式计算）",
        "001_两位数除以一位数.py", "TwoDigitDivideOneLesson",
    ),
}
REMOVED = (
    LESSONS["grade1"][0] + "/005_连加、连减、加减混合.py",
    LESSONS["grade2"][0] + "/002_有余数的除法.py",
    LESSONS["grade3"][0] + "/001_两位数除以一位数_竖式计算.py",
    LESSONS["grade3"][0] + "/001_两位数除以一位数（竖式计算）.py",
)


def pure_function(key: str, name: str):
    folder, file, _ = LESSONS[key]
    path = ROOT / folder / file
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    candidates = [node for node in tree.body
                  if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(candidates) != 1:
        raise AssertionError(f"expected one pure function {name} in {path}")
    namespace = {}
    module = ast.fix_missing_locations(ast.Module(body=candidates, type_ignores=[]))
    exec(compile(module, str(path), "exec"), namespace)
    return namespace[name]


def gallery_topics():
    catalog = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
    return [
        topic
        for lv in catalog["levels"]
        for grade in lv.get("grades", [])
        for sem in grade.get("semesters", [])
        for chapter in sem.get("chapters", [])
        for topic in chapter.get("topics", [])
    ]


class PrimarySceneDeduplicationTests(unittest.TestCase):
    def test_single_scene_file_per_consolidated_lesson(self):
        for key, (folder, filename, scene_name) in LESSONS.items():
            with self.subTest(lesson=key):
                directory = ROOT / folder
                scene_sources = [
                    p for p in directory.glob("*.py")
                    if not p.name.startswith(("verify_", "test_", "__"))
                ]
                self.assertEqual([p.name for p in scene_sources], [filename])
                self.assertEqual(find_scene_py(directory), directory / filename)
                tree = ast.parse((directory / filename).read_text(encoding="utf-8"))
                scenes = [c.name for c in tree.body if isinstance(c, ast.ClassDef)
                          and any(isinstance(b, ast.Name) and b.id == "Scene"
                                  for b in c.bases)]
                self.assertEqual(scenes, [scene_name])

    def test_duplicate_sources_are_truly_removed(self):
        for path in REMOVED:
            with self.subTest(source=path):
                self.assertFalse((ROOT / path).exists(), path)

    def test_grade_one_arithmetic_matches_three_teaching_examples(self):
        calculate = pure_function("grade1", "calculate_steps")
        self.assertEqual(calculate(2, 3, 1, "+", "+"), (5, 6))
        self.assertEqual(calculate(5, 2, 1, "-", "-"), (3, 2))
        self.assertEqual(calculate(5, 2, 3, "+", "-"), (7, 4))
        with self.assertRaises(ValueError):
            calculate(9, 5, 0, "+", "+")

    def test_grade_two_original_objects_are_neither_duplicated_nor_lost(self):
        plan = pure_function("grade2", "distribution_plan")
        for total in range(0, 40):
            for children in range(1, 10):
                assigned, remaining = plan(total, children)
                all_ids = [i for group in assigned for i in group] + list(remaining)
                self.assertEqual(sorted(all_ids), list(range(total)))
                self.assertEqual(len(all_ids), len(set(all_ids)))
                self.assertEqual(len({len(group) for group in assigned}), 1)
                self.assertEqual(len(remaining), total % children)
        self.assertEqual(plan(13, 4)[1], (12,))
        for args in ((-1, 4), (13, 0), (True, 4), (13, False)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                plan(*args)

    def test_grade_three_long_division_and_middle_zero(self):
        trace = pure_function("grade3", "long_division_trace")
        self.assertEqual(trace(52, 4), ((5, 1, 1), (12, 3, 0)))
        self.assertEqual(trace(57, 4), ((5, 1, 1), (17, 4, 1)))
        self.assertEqual(trace(312, 3), ((3, 1, 0), (1, 0, 1), (12, 4, 0)))
        for dividend in range(10, 1000):
            for divisor in range(1, 10):
                stages = trace(dividend, divisor)
                digits = "".join(str(part[1]) for part in stages)
                self.assertEqual((int(digits), stages[-1][2]), divmod(dividend, divisor))
                self.assertTrue(all(0 <= step[2] < divisor for step in stages))
        for args in ((9, 3), (1000, 3), (52, 0), (52, 10), (True, 3)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                trace(*args)

    def test_gallery_ids_video_links_and_only_two_source_switches(self):
        rows = {topic["id"]: topic for topic in gallery_topics()}
        expected = {
            "333882b1af": ("grade1", "ConsecutiveOperationsLesson_finish.mp4"),
            "e5b1915a70": ("grade2", "YouShuShuDeChuFa_finish.mp4"),
            "002f488641": ("grade3", "TwoDigitDivideOneLesson_finish.mp4"),
        }
        for topic_id, (key, video_name) in expected.items():
            with self.subTest(topic=topic_id):
                lesson_path, filename, _ = LESSONS[key]
                entry = rows[topic_id]
                self.assertEqual(entry["pyFile"], lesson_path + "/" + filename)
                self.assertEqual(entry["videoFile"], lesson_path + "/" + video_name)
                self.assertTrue(entry["hasVideo"])
        self.assertEqual(len(rows), 534)


if __name__ == "__main__":
    unittest.main()
