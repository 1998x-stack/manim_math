"""Unit tests for the dependency-free grade-three source audit."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from audit_grade3 import audit_tree  # noqa: E402


class GradeThreeAuditTests(unittest.TestCase):
    def test_reports_syntax_and_non_latex_text_without_manim(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            grade = root / "小学/三年级/上册/示例"
            grade.mkdir(parents=True)
            (grade / "good.py").write_text(
                'class Good(Scene):\n    def construct(self):\n'
                '        MathTex(r"2 \\times 3")\n', encoding="utf-8")
            (grade / "bad_identifier.py").write_text(
                'class 年、月、日(Scene):\n    pass\n', encoding="utf-8")
            (grade / "bad_tex.py").write_text(
                'class BadTex(Scene):\n    def construct(self):\n'
                '        MathTex("1年 = 12个月")\n', encoding="utf-8")
            (grade / "helper.py").write_text(
                'def add(a, b):\n    return a + b\n', encoding="utf-8")

            result = audit_tree(root)
            self.assertEqual(result["files"], 4)
            self.assertEqual(result["scene_files"], 2)
            self.assertEqual(
                {issue["code"] for issue in result["issues"]},
                {"PYTHON_SYNTAX", "UNICODE_MATHTEX", "NO_SCENE"},
            )
            self.assertTrue(all(issue["file"].startswith("小学/三年级/")
                                for issue in result["issues"]))

    def test_flags_generic_lesson_placeholder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            grade = root / "小学/三年级/下册/统计"
            grade.mkdir(parents=True)
            (grade / "template.py").write_text(
                'class Statistics(Scene):\n'
                '    def construct(self):\n'
                '        Text("正在学习复式条形统计图的概念...")\n',
                encoding="utf-8",
            )
            result = audit_tree(root)
            self.assertEqual(result["files"], 1)
            self.assertEqual(result["scene_files"], 1)
            self.assertEqual(len(result["issues"]), 1)
            self.assertEqual(result["issues"][0]["code"], "GENERIC_LESSON_PLACEHOLDER")
            self.assertEqual(result["issues"][0]["severity"], "warning")

    def test_missing_grade_directory_is_an_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result = audit_tree(Path(directory))
        self.assertEqual(result["files"], 0)
        self.assertEqual(result["scene_files"], 0)
        self.assertEqual(result["issues"][0]["code"], "MISSING_DIRECTORY")


    def test_cli_fails_on_errors_without_strict_but_not_warnings(self):
        import audit_grade3
        from contextlib import redirect_stdout
        from io import StringIO
        from unittest.mock import patch

        error = {"severity": "error", "file": "broken.py", "line": 1,
                 "code": "PYTHON_SYNTAX", "detail": "bad syntax"}
        warning = {"severity": "warning", "file": "lesson.py", "line": 2,
                   "code": "UNICODE_MATHTEX", "detail": "unsafe tex"}
        for issues, arguments, expected in (
            ([error], [], 1),
            ([warning], [], 0),
            ([warning], ["--strict"], 1),
        ):
            with self.subTest(issues=issues, arguments=arguments):
                with (patch.object(audit_grade3, "audit_tree",
                                   return_value={"files": 1, "scene_files": 1, "issues": issues}),
                      patch("sys.argv", ["audit_grade3.py", *arguments]),
                      redirect_stdout(StringIO())):
                    self.assertEqual(audit_grade3.main(), expected)


if __name__ == "__main__":
    unittest.main()
