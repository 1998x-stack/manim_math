"""运行：python tests/test_audit_grade2.py（不依赖 Manim）。"""
import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "audit_grade2.py"
spec = importlib.util.spec_from_file_location("audit_grade2", SCRIPT)
audit_grade2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit_grade2)


class AuditGrade2Tests(unittest.TestCase):
    def test_flags_unicode_in_mathtex(self):
        source = 'from manim import *\nformula = MathTex("13 ÷ 4 = 3 … 1")\n'
        codes = {i["code"] for i in audit_grade2.audit_source(source, "sample.py")}
        self.assertIn("MATH_TEX_UNICODE", codes)

    def test_accepts_standard_latex_formula(self):
        source = 'from manim import *\nformula = MathTex(r"13\\div4=3\\cdots1")\n'
        self.assertEqual(audit_grade2.audit_source(source, "sample.py"), [])

    def test_flags_generic_placeholder(self):
        source = '# 更多动画元素可以根据需要添加\n'
        codes = {i["code"] for i in audit_grade2.audit_source(source, "sample.py")}
        self.assertIn("GENERIC_PLACEHOLDER", codes)

    def test_non_asserting_verifier(self):
        source = 'def verify():\n    print("验证完成")\n'
        codes = {i["code"] for i in audit_grade2.audit_source(
            source, "verify_geometry.py"
        )}
        self.assertIn("NON_ASSERTING_VERIFIER", codes)

    def test_syntax_error_and_tree_summary(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "wrong.py").write_text("def broken(:\n", encoding="utf-8")
            (root / "ok.py").write_text("value = 1\n", encoding="utf-8")
            report = audit_grade2.audit_tree(root)
            self.assertEqual(report["files_scanned"], 2)
            self.assertEqual(report["finding_counts"]["PY_SYNTAX"], 1)


if __name__ == "__main__":
    unittest.main()
