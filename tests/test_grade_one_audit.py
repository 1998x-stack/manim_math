"""Small synthetic fixtures exercise the full-folder grade-one AST scanner."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "tools/audit_grade_one.py"
spec = importlib.util.spec_from_file_location("grade_one_audit", SCRIPT)
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)


class AuditTests(unittest.TestCase):
    def test_catalogues_all_py_without_importing_manim(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            topic = root / "上册" / "第一章" / "001示例"
            topic.mkdir(parents=True)
            (topic / "lesson.py").write_text(
                "from manim import *\nclass ExampleScene(Scene):\n    def construct(self):\n        pass\n",
                encoding="utf-8",
            )
            report = audit_module.audit(root)
            self.assertEqual(report["python_count"], 1)
            self.assertEqual(report["scene_count"], 1)
            self.assertEqual(report["files"][0]["scenes"], ["ExampleScene"])
            self.assertEqual(report["files"][0]["syntax"], "ok")
            self.assertEqual(
                {record["message"] for record in report["diagnostics"]
                 if record["rule"] == "missing-companion"},
                {"同目录缺少 description.json", "同目录缺少 prompt.md", "同目录缺少 storyboard.md"},
            )

    def test_catches_broken_python_and_literal_chinese_in_mathtex(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            topic = root / "下册" / "第二章"
            topic.mkdir(parents=True)
            (topic / "broken.py").write_text("def f(:\n", encoding="utf-8")
            (topic / "tex.py").write_text('MathTex("一个苹果")\n', encoding="utf-8")
            report = audit_module.audit(root)
            rules = {(record["rule"], record["severity"]) for record in report["diagnostics"]}
            self.assertIn(("python-syntax", "error"), rules)
            self.assertIn(("chinese-in-tex", "warning"), rules)
            self.assertEqual(report["by_semester"], {"下册": 2})


if __name__ == "__main__":
    unittest.main()
