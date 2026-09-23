"""高二静态审查回归测试：仅依赖 Python 标准库。"""
from __future__ import annotations

import ast
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from audit_grade11 import audit_tree  # noqa: E402

COURSE = ROOT / "高中/高二/第二学期/第十三章-复数"
ROOTS = COURSE / "004复数的平方根与立方根"


class Grade11AuditTests(unittest.TestCase):
    def test_audits_both_semesters_and_reports_risky_source(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            first = root / "高中/高二/第一学期/例题"
            second = root / "高中/高二/第二学期/例题"
            first.mkdir(parents=True)
            second.mkdir(parents=True)
            (first / "broken.py").write_text("class Bad(Scene):\n  def construct(self):\n    /\n", encoding="utf-8")
            (second / "lesson.py").write_text(
                'class Lesson(Scene):\n'
                '    def construct(self):\n'
                '        MathTex(r"\\sqrt{4} = \\pm 2")\n'
                '        MathTex("a ∈ R, i²=-1")\n'
                '        Text("正在学习数列的概念......")\n'
                '        self.play(Write(Text("完成")))\n', encoding="utf-8",
            )
            report = audit_tree(root)
        self.assertEqual(report["files"], 2)
        self.assertEqual(report["scene_files"], 1)
        self.assertEqual(
            {item["code"] for item in report["issues"]},
            {"PYTHON_SYNTAX", "AMBIGUOUS_SQRT", "UNICODE_MATHTEX",
             "GENERIC_LESSON_PLACEHOLDER"},
        )

    def test_helper_chain_is_not_an_empty_scene(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            lesson = root / "高中/高二/第一学期/归纳法"
            lesson.mkdir(parents=True)
            (lesson / "helpers.py").write_text(
                'class Helper(Scene):\n'
                '    def construct(self):\n        self.intro()\n'
                '    def intro(self):\n        self.animation()\n'
                '    def animation(self):\n        self.play(Write(Text("hello")))\n',
                encoding="utf-8",
            )
            report = audit_tree(root)
        self.assertEqual(report["issues"], [])
        self.assertEqual(report["scene_files"], 1)

    def test_ctex_chinese_note_is_not_syntax_error(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            lesson = root / "高中/高二/第二学期/圆"
            lesson.mkdir(parents=True)
            (lesson / "ctex.py").write_text(
                'class Ctex(Scene):\n    def construct(self):\n'
                '        self.play(Write(MathTex(r"\\text{圆心}", tex_template=TexTemplateLibrary.ctex)))\n',
                encoding="utf-8",
            )
            report = audit_tree(root)
        self.assertEqual([(item["code"], item["severity"]) for item in report["issues"]],
                         [("UNICODE_MATHTEX", "info")])

    def test_missing_directory_is_an_error(self):
        with tempfile.TemporaryDirectory() as folder:
            report = audit_tree(Path(folder))
        self.assertEqual(report["files"], 0)
        self.assertEqual(report["issues"][0]["code"], "MISSING_DIRECTORY")

    def test_valid_formula_not_misidentified_as_two_valued_radical(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            lesson = root / "高中/高二/第二学期/例题"
            lesson.mkdir(parents=True)
            (lesson / "valid.py").write_text(
                'class Correct(Scene):\n    def construct(self):\n'
                '        self.play(Write(MathTex(r"w^2=-4 \\Longleftrightarrow w=\\pm2i")))\n',
                encoding="utf-8",
            )
            report = audit_tree(root)
        self.assertEqual(report["issues"], [])
        self.assertEqual(report["scene_files"], 1)

    def test_complex_root_lesson_regression_without_importing_manim(self):
        scene = (ROOTS / "complex_roots.py").read_text(encoding="utf-8")
        module = ast.parse(scene)
        self.assertTrue(any(isinstance(node, ast.ClassDef) and node.name == "ComplexRoots"
                            for node in module.body))
        self.assertIn(r"\sqrt{4}=2", scene)
        self.assertNotIn(r"\sqrt{4} = \pm", scene)
        self.assertNotIn(r"\sqrt{-4} = \pm", scene)
        self.assertIn(r"z=0", scene)
        self.assertIn("PLANE_CENTER + UNIT_R", scene)
        metadata = json.loads((ROOTS / "description.json").read_text(encoding="utf-8"))
        self.assertIn("z=0", metadata["知识点内容详细描述"])
        for k in range(3):
            omega = complex(math.cos(2 * math.pi * k / 3),
                            math.sin(2 * math.pi * k / 3))
            self.assertLess(abs(omega ** 3 - 1), 1e-12)
        self.assertEqual(len({complex(round(math.cos(2 * math.pi * k / 3), 12),
                                     round(math.sin(2 * math.pi * k / 3), 12))
                              for k in range(3)}), 3)


if __name__ == "__main__":
    unittest.main()
