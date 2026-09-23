"""Standard-library regression tests for tools/audit_grade6.py."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

TOOL_PATH = Path(__file__).resolve().parents[1] / "audit_grade6.py"
spec = importlib.util.spec_from_file_location("audit_grade6", TOOL_PATH)
audit_grade6 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_grade6)


class GradeSixAuditTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = tempfile.TemporaryDirectory()
        self.addCleanup(self.sandbox.cleanup)
        self.root = Path(self.sandbox.name)
        self.grade = self.root / "小学" / "六年级" / "第一学期"
        self.grade.mkdir(parents=True)

    def write(self, relative, content):
        path = self.grade / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_valid_python_and_json(self):
        self.write("good.py", 'from manim import *\nclass Example(Scene):\n    def construct(self):\n        MathTex(r"12 \\div 3 = 4")\n')
        self.write("description.json", '{"年级": "六年级"}')
        python_count, json_count, issues = audit_grade6.audit(self.root)
        self.assertEqual((python_count, json_count, issues), (1, 1, []))

    def test_invalid_class_name_is_error(self):
        self.write("broken.py", "class 数学(深化)Animation(Scene):\n    pass\n")
        _, _, issues = audit_grade6.audit(self.root)
        self.assertTrue(any(i["severity"] == "error" and "语法" in i["message"] for i in issues))

    def test_unicode_formula_and_literal_backslash_n_are_warnings(self):
        source = "\n".join([
            "from manim import *",
            "class Example(Scene):",
            "    def construct(self):",
            '        MathTex("12 ÷ 3 = 4 (余数为0)")',
            r'        Text("first\\nsecond")',
        ])
        self.write("warnings.py", source)
        _, _, issues = audit_grade6.audit(self.root)
        self.assertEqual(len(issues), 2)
        self.assertTrue(all(i["severity"] == "warning" for i in issues))

    def test_bad_json_is_error(self):
        self.write("description.json", '{"年级": "六年级",}')
        _, _, issues = audit_grade6.audit(self.root)
        self.assertTrue(any(i["severity"] == "error" and "JSON" in i["message"] for i in issues))

    def test_missing_grade_directory_is_error(self):
        _, _, issues = audit_grade6.audit(self.root / "other")
        self.assertEqual(issues[0]["severity"], "error")


if __name__ == "__main__":
    unittest.main()
