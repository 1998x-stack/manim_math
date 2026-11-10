"""Sixth-grade Scene deduplication: math, source ownership and legacy Gallery tests.

Read actual lesson sources with AST; no Manim module, LaTeX renderer or video load.
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
    "ratio": {
        "folder": "小学/六年级/第一学期/第三章-比和比例/002比与分数、除法的关系",
        "keep": "002_比与分数除法的关系.py",
        "deleted": "002_比与分数、除法的关系.py",
        "class": "RatioFractionDivisionLesson", "id": "dc6c271f43",
        "video": "RatioFractionDivisionLesson_finish.mp4",
    },
    "gcd": {
        "folder": "小学/六年级/第一学期/第一章-数的整除/003最大公因数和最小公倍数(深化)",
        "keep": "003_最大公因数与最小公倍数.py",
        "deleted": "003_最大公因数和最小公倍数(深化).py",
        "class": "GcfLcmLesson", "id": "912515c904",
        "video": "GcfLcmLesson_finish.mp4",
    },
    "segment": {
        "folder": "小学/六年级/第一学期/第七章-线段与角的画法/001线段的相等与和、差、倍、分",
        "keep": "001_线段的相等与和差倍分.py",
        "deleted": "001_线段的相等与和、差、倍、分.py",
        "class": "SegmentRelationsLesson", "id": "5ea56a3e0f",
        "video": "SegmentRelationsLesson_finish.mp4",
    },
    "angles": {
        "folder": "小学/六年级/第一学期/第七章-线段与角的画法/002余角、补角、对顶角",
        "keep": "002_余角补角对顶角.py",
        "deleted": "002_余角、补角、对顶角.py",
        "class": "ComplementarySupplementaryVerticalLesson",
        "id": "70666cc6c2",
        "video": "ComplementarySupplementaryVerticalLesson_finish.mp4",
    },
}


def extract_function(course, function_name):
    lesson = LESSONS[course]
    path = ROOT / lesson["folder"] / lesson["keep"]
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    nodes = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    ]
    if len(nodes) != 1:
        raise AssertionError(f"{path}: expected one function {function_name}")
    namespace = {}
    isolated_module = ast.fix_missing_locations(ast.Module(body=nodes, type_ignores=[]))
    exec(compile(isolated_module, str(path), "exec"), namespace)
    return namespace[function_name]


def get_gallery():
    payload = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
    result = {}
    for level in payload["levels"]:
        for grade in level.get("grades", []):
            for semester in grade.get("semesters", []):
                for chapter in semester.get("chapters", []):
                    for topic in chapter.get("topics", []):
                        if topic["id"] in result:
                            raise AssertionError(f"duplicate topic id {topic['id']}")
                        result[topic["id"]] = topic
    return result


class SixthGradeSceneDedupTests(unittest.TestCase):
    def test_each_topic_has_one_direct_scene_and_no_obsolete_file(self):
        for key, item in LESSONS.items():
            with self.subTest(topic=key):
                directory = ROOT / item["folder"]
                self.assertFalse((directory / item["deleted"]).exists())
                self.assertTrue((directory / item["keep"]).is_file())
                scene_files = sorted(p.name for p in directory.glob("*.py")
                                     if not p.name.startswith(("verify_", "test_", "__")))
                self.assertEqual(scene_files, [item["keep"]])
                self.assertEqual(find_scene_py(directory), directory / item["keep"])
                tree = ast.parse((directory / item["keep"]).read_text(encoding="utf-8"))
                scenes = [
                    cls.name for cls in tree.body if isinstance(cls, ast.ClassDef)
                    and any(isinstance(base, ast.Name) and base.id == "Scene"
                            for base in cls.bases)
                ]
                self.assertEqual(scenes, [item["class"]])

    def test_legacy_gallery_ids_and_media_are_unchanged(self):
        gallery = get_gallery()
        self.assertEqual(len(gallery), 534)
        for key, item in LESSONS.items():
            with self.subTest(topic=key):
                topic = gallery[item["id"]]
                self.assertEqual(topic["pyFile"], item["folder"] + "/" + item["keep"])
                self.assertEqual(topic["videoFile"], item["folder"] + "/" + item["video"])
                self.assertTrue(topic["hasVideo"])

    def test_ratio_is_exact_and_zero_denominator_is_rejected(self):
        ratio = extract_function("ratio", "ratio_value")
        for a in range(-6, 7):
            for b in range(-6, 7):
                if b == 0:
                    with self.assertRaises(ValueError):
                        ratio(a, b)
                else:
                    self.assertEqual(ratio(a, b), Fraction(a, b))
                    self.assertEqual(ratio(2 * a, 2 * b), ratio(a, b))
        for a, b in ((True, 2), (1.1, 2), (2, False)):
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                ratio(a, b)

    def test_gcd_and_lcm_are_positive_and_obey_product_formula(self):
        values = extract_function("gcd", "gcd_lcm_values")
        self.assertEqual(values(12, 18), (6, 36))
        self.assertEqual(values(12, 18, 24), (6, 72))
        self.assertEqual(values(36, 24), (12, 72))
        self.assertEqual(values(8, 15), (1, 120))
        for a in range(1, 31):
            for b in range(1, 31):
                gcd, lcm = values(a, b)
                self.assertEqual(gcd * lcm, a * b)
                self.assertEqual(a % gcd, 0)
                self.assertEqual(b % gcd, 0)
                self.assertEqual(lcm % a, 0)
                self.assertEqual(lcm % b, 0)
        for args in ((), (5,), (0, 1), (-3, 2), (True, 4)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                values(*args)

    def test_segment_sums_differences_doubles_and_midpoints(self):
        operations = extract_function("segment", "segment_lengths")
        self.assertEqual(operations(4, 2), (6, 2, 8, Fraction(2)))
        self.assertEqual(operations(5, 0), (5, 5, 10, Fraction(5, 2)))
        for a in range(0, 31):
            for b in range(0, a + 1):
                summation, difference, double, half = operations(a, b)
                self.assertEqual(summation, a + b)
                self.assertEqual(difference + b, a)
                self.assertEqual(double, 2 * a)
                self.assertEqual(2 * half, a)
        for args in ((2, 3), (-1, 2), (True, 1), (2.5, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                operations(*args)

    def test_complementary_supplementary_vertical_geometry(self):
        other = extract_function("angles", "angle_partner")
        crossing = extract_function("angles", "crossing_angles")
        self.assertEqual(other(52, 90), 38)
        self.assertEqual(other(75, 180), 105)
        self.assertEqual(other(45, 90), 45)
        for total in (90, 180):
            for angle in range(total + 1):
                self.assertEqual(angle + other(angle, total), total)
        for a in range(1, 180):
            w, x, y, z = crossing(a)
            self.assertEqual((w, y), (a, a))
            self.assertEqual((x, z), (180 - a, 180 - a))
            self.assertEqual(w + x, 180)
        for args in ((91, 90), (-1, 180), (30, 120), (True, 90)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                other(*args)
        for x in (0, 180, True, 60.5):
            with self.subTest(angle=x), self.assertRaises(ValueError):
                crossing(x)


if __name__ == "__main__":
    unittest.main()
