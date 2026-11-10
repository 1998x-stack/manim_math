"""Dependency-free regression tests for the complete primary-school source inventory."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.audit_primary_sources import audit, main, scene_names
import ast


class PrimarySourcesAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.topic = self.root / "小学/二年级/上册/第一章/001乘法"
        self.topic.mkdir(parents=True)
        (self.topic / "description.json").write_text("{}", encoding="utf-8")
        (self.topic / "prompt.md").write_text("题目", encoding="utf-8")
        (self.topic / "storyboard.md").write_text("分镜", encoding="utf-8")

    def make_file(self, name: str, content: str):
        (self.topic / name).write_text(content, encoding="utf-8")

    def test_finds_all_files_including_wrappers_helpers_and_tests(self):
        self.make_file("lesson.py", "from manim import *\nclass Lesson(Scene): pass\n")
        self.make_file("old_entry.py", 'from runpy import run_path\nBase = run_path("lesson.py")["Lesson"]\nclass Old(Base): pass\n')
        self.make_file("model.py", "def add(a,b): return a+b\n")
        self.make_file("verify_geometry.py", "assert 2 * 3 == 6\n")
        self.make_file("test_model.py", "assert True\n")
        report = audit(self.root)
        self.assertEqual(report["summary"]["python_files"], 5)
        self.assertEqual(report["summary"]["parse_errors"], 0)
        self.assertEqual(report["summary"]["multiple_python_directories"], 1)
        self.assertEqual(
            report["summary"]["by_role"],
            {"compatibility-wrapper": 1, "direct-scene": 1,
             "helper-or-indirect-scene": 1, "test": 1, "verifier": 1},
        )
        topic = report["topics"][0]
        self.assertEqual(topic["direct_scenes"][0]["classes"], ["Lesson"])
        self.assertFalse(topic["needs_scene_review"])
        self.assertEqual(topic["companions"]["storyboard.md"], True)
        self.assertEqual(report, audit(self.root))

    def test_recognizes_import_aliases_but_does_not_guess_indirect_scenes(self):
        src = ast.parse("from manim import Scene as Base\n"
                        "import manim as mn\n"
                        "class A(Base): pass\n"
                        "class B(mn.ThreeDScene): pass\n"
                        "class Helper(UnknownScene): pass\n")
        self.assertEqual(scene_names(src), ["A", "B"])

    def test_reports_syntax_and_missing_storyboard_without_importing_manim(self):
        (self.topic / "storyboard.md").unlink()
        self.make_file("bad.py", "class Oops(:\n")
        report = audit(self.root)
        self.assertEqual(report["summary"]["parse_errors"], 1)
        self.assertEqual(report["summary"]["missing_storyboards"], 1)
        self.assertTrue(report["topics"][0]["needs_scene_review"])
        self.assertEqual(main(["--root", str(self.root), "--output", str(self.root / "out.json")]), 1)
        self.assertEqual(main(["--root", str(self.root), "--fail-on", "none",
                               "--output", str(self.root / "out.json")]), 0)
        self.assertTrue((self.root / "out.json").exists())

    def test_olympiad_test_files_are_kept_without_false_missing_metadata(self):
        self.make_file("lesson.py", "class Main(Scene): pass\n")
        olympiad = self.root / "小学/奥数专题"
        olympiad.mkdir(parents=True)
        (olympiad / "test_math_models.py").write_text("assert 1 + 1 == 2\n", encoding="utf-8")
        report = audit(self.root)
        olympiad_topic = next(t for t in report["topics"] if t["path"] == "小学/奥数专题")
        self.assertIsNone(olympiad_topic["companions"])
        self.assertFalse(olympiad_topic["needs_scene_review"])
        self.assertEqual(report["summary"]["by_grade"], {"二年级": 1, "奥数专题": 1})

    def test_missing_school_directory_fails_loudly(self):
        with tempfile.TemporaryDirectory() as empty:
            with self.assertRaises(FileNotFoundError):
                audit(Path(empty))


if __name__ == "__main__":
    unittest.main()
