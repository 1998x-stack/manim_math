"""运行：python -m unittest discover -s tests -p 'test_audit_grade8.py'。"""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "audit_grade8.py"
spec = importlib.util.spec_from_file_location("audit_grade8", SCRIPT)
audit = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit)


class AuditGrade8Tests(unittest.TestCase):
    def test_detects_new_rectangle_fadeout(self):
        code = "self.play(FadeOut(SurroundingRectangle(word).set_opacity(0)))"
        self.assertEqual(audit.audit_source(code)[0]["code"], "FADEOUT_NEW_RECT")

    def test_preserved_rectangle_is_safe(self):
        code = "rect = SurroundingRectangle(word)\nself.play(FadeOut(rect))"
        self.assertEqual(audit.audit_source(code), [])

    def test_chinese_mathtex_and_plain_text(self):
        code = 'a = MathTex(r"\\text{必然事件}")\nb = Text("必然事件")'
        self.assertEqual(audit.audit_source(code)[0]["code"], "CJK_IN_LATEX")

    def test_global_seed_vs_local_generator(self):
        code = "np.random.seed(42)\nrng = np.random.default_rng(42)"
        self.assertEqual([i["code"] for i in audit.audit_source(code)], ["GLOBAL_RNG_SEED"])

    def test_syntax_error_retains_location(self):
        finding = audit.audit_source("def broken(:\n", "bad.py")[0]
        self.assertEqual((finding["code"], finding["path"], finding["line"]),
                         ("PY_SYNTAX", "bad.py", 1))

    def test_inventory_and_strict_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            topic = root / "第一学期" / "第十七章" / "001"
            topic.mkdir(parents=True)
            (topic / "scene.py").write_text(
                "class Example(Scene):\n    pass\n", encoding="utf-8"
            )
            (topic / "broken.py").write_text("def bad(:\n", encoding="utf-8")
            report = audit.audit_tree(root)
            self.assertEqual(report["files_scanned"], 2)
            self.assertEqual(report["chapters"], {"第一学期/第十七章": 2})
            self.assertEqual(report["finding_counts"], {"PY_SYNTAX": 1})
            self.assertIn("Example", [scene for entry in report["files"] for scene in entry["scenes"]])
            self.assertEqual(audit.main(["--root", str(root), "--strict"]), 1)


if __name__ == "__main__":
    unittest.main()
