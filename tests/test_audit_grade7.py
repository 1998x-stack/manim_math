"""七年级审计器与整式加减法教学脚本的无 Manim 回归检查。"""

from __future__ import annotations

import ast
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from audit_grade7 import audit_tree, main  # noqa: E402


class GradeSevenAuditTests(unittest.TestCase):
    def test_catches_broken_source_and_lesson_placeholders(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            topic = root / "初中/七年级/第一学期/第九章-整式/001示例"
            topic.mkdir(parents=True)
            (topic / "scene.py").write_text(
                'class Lesson(Scene):\n'
                '    def construct(self):\n'
                '        MathTex("\\\\frac{1}{2} × 3")\n'
                '        Text("正在学习")\n', encoding="utf-8")
            (topic / "broken.py").write_text('class Bad(Scene):\n def construct(self)\n  pass\n', encoding="utf-8")
            (topic / "description.json").write_text('{invalid', encoding="utf-8")
            result = audit_tree(root)
            self.assertEqual(result["python_files"], 2)
            self.assertEqual(result["scene_files"], 1)
            self.assertEqual(result["topic_dirs"], 1)
            self.assertEqual({item["code"] for item in result["issues"]},
                             {"PYTHON_SYNTAX", "INVALID_JSON", "NON_LATEX_MATH", "TEMPLATE_CONTENT"})

    def test_warning_only_scene_without_construct_and_missing_source(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            grade = root / "初中/七年级/第二学期"
            scene_dir = grade / "一章/001场景"
            scene_dir.mkdir(parents=True)
            (scene_dir / "lesson.py").write_text('class Lesson(Scene):\n    pass\n', encoding="utf-8")
            doc_dir = grade / "二章/002仅文档"
            doc_dir.mkdir(parents=True)
            (doc_dir / "description.json").write_text(json.dumps({"知识点": "测试"}), encoding="utf-8")
            result = audit_tree(root)
            self.assertEqual({item["code"] for item in result["issues"]},
                             {"NO_CONSTRUCT", "TOPIC_WITHOUT_SOURCE"})
            self.assertEqual(main(["--root", str(root), "--json"]), 0)
            self.assertEqual(main(["--root", str(root), "--strict-warnings"]), 1)

    def test_empty_scene_and_bad_escape(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            grade = root / "初中/七年级/第一学期"
            grade.mkdir(parents=True)
            (grade / "empty.py").write_text(
                'class Empty(Scene):\n    def construct(self):\n        pass\n', encoding="utf-8")
            (grade / "bad_tex.py").write_text(
                'class BadTex(Scene):\n    def construct(self):\n'
                '        MathTex("\\\\frac{1}{2}")\n', encoding="utf-8")
            result = audit_tree(root)
            self.assertIn("EMPTY_SCENE", {i["code"] for i in result["issues"]})

    def test_missing_course_is_error(self):
        with tempfile.TemporaryDirectory() as temp:
            result = audit_tree(Path(temp))
        self.assertEqual(result["issues"][0]["code"], "MISSING_DIRECTORY")

    def test_polynomial_subtraction_scene_retains_name_and_all_steps(self):
        path = ROOT / "初中/七年级/第一学期/第九章-整式/003整式的加减法/003_整式的加减法.py"
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=str(path))
        compile(tree, str(path), "exec", dont_inherit=True)
        self.assertIn("整式的加减法Animation", {node.name for node in tree.body
                      if isinstance(node, ast.ClassDef)})
        literals = {node.value for node in ast.walk(tree)
                    if isinstance(node, ast.Constant) and isinstance(node.value, str)}
        for step in (r"+(a+b)", r"-(a+b)", r"-a-b", r"=2x+3-x+1",
                     r"=(2x-x)+(3+1)", r"=x+4", r"=3x+2"):
            self.assertIn(step, literals)
        self.assertNotIn("更多动画元素可以根据需要添加", text)
        for x in (-7, -1, 0, 1, 2, 13):
            self.assertEqual((2 * x + 3) - (x - 1), x + 4)
            self.assertEqual((2 * x + 3) + (x - 1), 3 * x + 2)


if __name__ == "__main__":
    unittest.main()
