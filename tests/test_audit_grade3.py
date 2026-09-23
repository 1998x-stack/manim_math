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

    def test_missing_grade_directory_is_an_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result = audit_tree(Path(directory))
        self.assertEqual(result["files"], 0)
        self.assertEqual(result["issues"][0]["code"], "MISSING_DIRECTORY")


if __name__ == "__main__":
    unittest.main()
