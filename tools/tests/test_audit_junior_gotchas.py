"""Regression tests for the junior historical-gotchas scanner (no Manim needed)."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "audit_junior_gotchas.py"
spec = importlib.util.spec_from_file_location("audit_junior_gotchas", SCRIPT)
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)


class AuditJuniorGotchasTests(unittest.TestCase):
    def codes(self, text):
        return {item["code"] for item in scanner.audit_source(text, "scene.py")}

    def test_historical_api_incompatibilities(self):
        source = """from manim import *
a = Rectangle(corner_radius=0.1)
b = Sector(inner_radius=0.3, outer_radius=1)
c = arrow.scale(0.5, scale_tips=True)
"""
        self.assertEqual(self.codes(source), {
            "RECTANGLE_CORNER_RADIUS", "SECTOR_RADIUS_KEYWORD", "LEGACY_SCALE_TIPS"
        })

    def test_corrected_api_uses_do_not_trigger(self):
        source = """from manim import *
a = RoundedRectangle(corner_radius=0.1)
b = AnnularSector(inner_radius=0.3, outer_radius=1)
c = Sector(outer_radius_unused=1)  # other unsupported keywords are outside this audit
"""
        self.assertFalse(self.codes(source) & {
            "RECTANGLE_CORNER_RADIUS", "SECTOR_RADIUS_KEYWORD"
        })

    def test_chinese_and_degree_sign_in_latex(self):
        self.assertEqual(self.codes('MathTex("周角 = 360°")'),
                         {"CHINESE_IN_TEX", "UNICODE_IN_TEX"})
        self.assertNotIn("UNICODE_IN_TEX", self.codes('MathTex(r"360^{\\circ}")'))
        self.assertNotIn("CHINESE_IN_TEX", self.codes('Text("周角")'))

    def test_f_string_literal_part_detected(self):
        self.assertIn("CHINESE_IN_TEX", self.codes('MathTex(f"角 {value}")'))

    def test_dynamic_and_zero_width_plot(self):
        self.assertIn("ZERO_WIDTH_PLOT", self.codes('axes.plot(f, x_range=[-1, -1])'))
        self.assertNotIn("ZERO_WIDTH_PLOT", self.codes('axes.plot(f, x_range=[-1, t.get_value()])'))
        self.assertNotIn("ZERO_WIDTH_PLOT", self.codes('axes.plot(f, x_range=[-1, 1])'))

    def test_empty_animation_branch(self):
        self.assertIn("PLAY_EMPTY_ANIMATION", self.codes('self.play(FadeOut(a) if a else [])'))
        self.assertNotIn("PLAY_EMPTY_ANIMATION", self.codes('self.play(*animations)'))

    def test_global_rng_mutation(self):
        self.assertIn("GLOBAL_NUMPY_SEED", self.codes('np.random.seed(42)'))
        self.assertNotIn("GLOBAL_NUMPY_SEED", self.codes('np.random.default_rng(42)'))

    def test_syntax_error_is_reported(self):
        result = scanner.audit_source('def broken(:\n pass', "broken.py")
        self.assertEqual([item["code"] for item in result], ["PY_SYNTAX"])
        self.assertEqual(result[0]["severity"], "error")

    def test_all_four_grades_and_only_python_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for grade in scanner.GRADES:
                folder = root / "初中" / grade
                folder.mkdir(parents=True)
                (folder / "scene.py").write_text('MathTex("中文")', encoding="utf-8")
                (folder / "video.mp4").write_bytes(b"not python")
            result = scanner.audit(root)
            self.assertEqual(result["files"], 4)
            self.assertEqual(result["warnings"], 4)
            self.assertEqual(result["errors"], 0)
            self.assertEqual(set(result["grades"]), set(scanner.GRADES))
            self.assertEqual(len({x["path"] for x in result["findings"]}), 4)

    def test_missing_grade_is_not_silently_reported_as_clean(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = scanner.audit(Path(temporary), ("九年级",))
            self.assertEqual(result["errors"], 1)
            self.assertEqual(result["findings"][0]["code"], "GRADE_MISSING")


if __name__ == "__main__":
    unittest.main()
