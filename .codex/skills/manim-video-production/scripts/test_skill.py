"""Run: python -m unittest discover -s scripts -p 'test_*.py' -v."""
import json
from pathlib import Path
import unittest

import audit_scene

BASE = (
    "import manimgx as m\n"
    "m.config.pixel_width = 1080\n"
    "m.config.pixel_height = 1920\n"
    "m.config.frame_height = 16\n"
    "class Demo(m.Scene):\n"
    "    pass\n"
)


def findings(source, level=None):
    return [item for item in audit_scene.audit_source(BASE + source)
            if level is None or item["level"] == level]


def codes(source, level=None):
    return {item["code"] for item in findings(source, level)}


class SceneAuditTests(unittest.TestCase):
    def test_ce_import_rejected(self):
        self.assertIn("CE_IMPORT", codes("from manim import Circle\n", "ERROR"))
        self.assertIn("CE_IMPORT", codes("import manim\n", "ERROR"))

    def test_frame_width_assignment_rejected(self):
        self.assertIn("READONLY_FRAME_WIDTH", codes("config.frame_width = 9\n", "ERROR"))

    def test_mathtex_cjk_is_review_and_degree_rejected(self):
        self.assertIn("CJK_IN_MATHTEX_REVIEW", codes('MathTex(r"\\text{中文}")\n', "WARN"))
        self.assertIn("DEGREE_IN_MATHTEX", codes('MathTex("90°")\n', "ERROR"))
        self.assertNotIn("CJK_IN_MATHTEX_REVIEW", codes('Text("中文 90°")\n'))

    def test_legacy_tex_template_and_macros_rejected(self):
        self.assertIn(
            "LEGACY_TEX_TEMPLATE",
            codes('MathTex("x", tex_template=TexTemplateLibrary.ctex)\n', "ERROR"),
        )
        self.assertIn("UNSUPPORTED_TEX_MACRO", codes(r'MathTex(r"\\def\\x{1}\\x")' + "\n", "ERROR"))
        self.assertIn("UNSUPPORTED_TEX_MACRO", codes(r'MathTex(r"\\usepackage{amsmath}")' + "\n", "ERROR"))

    def test_dynamic_tex_requires_review(self):
        self.assertIn("DYNAMIC_TEX", codes('MathTex(formula)\n'))
        self.assertIn("DYNAMIC_TEX", codes('MathTex(rf"{angle}^\\circ")\n'))

    def test_normal_text_and_mathtex_are_allowed(self):
        self.assertEqual(findings('Text("90°")\nMathTex(r"1+2=3")\n', "ERROR"), [])

    def test_legacy_scene_and_animation_aliases(self):
        self.assertIn("LEGACY_SCENE_ALIAS", codes("class Legacy(MovingCameraScene):\n    pass\n", "ERROR"))
        for expression in (
            "ApplyMethod(x.shift, RIGHT)",
            "ScaleInPlace(x, 2)",
            "FadeToColor(x, RED)",
        ):
            self.assertIn("LEGACY_ANIMATION_ALIAS", codes(expression + "\n", "ERROR"))

    def test_nested_play_detected_not_normal_sequential_play(self):
        self.assertIn("NESTED_SELF_PLAY", codes('self.play(self.play(FadeOut(x)))\n', "ERROR"))
        self.assertNotIn("NESTED_SELF_PLAY", codes('self.play(FadeOut(x))\nself.play(FadeIn(y))\n', "ERROR"))

    def test_play_with_empty_branch_or_list(self):
        self.assertIn("PLAY_EMPTY_ANIMATION", codes('self.play(FadeOut(x) if x else [])\n', "ERROR"))
        self.assertIn("PLAY_EMPTY_ANIMATION", codes('self.play([])\n', "ERROR"))
        self.assertNotIn("PLAY_EMPTY_ANIMATION", codes('self.play(*animations)\n'))

    def test_random_seed_warning(self):
        self.assertIn("GLOBAL_RNG_SEED", codes('np.random.seed(42)\n'))
        self.assertIn("GLOBAL_RNG_SEED", codes('random.seed(42)\n'))
        self.assertNotIn("GLOBAL_RNG_SEED", codes('rng = np.random.default_rng(42)\n'))

    def test_only_literal_zero_width_is_confirmed(self):
        self.assertIn("ZERO_WIDTH_PLOT", codes('axes.plot(f, x_range=[2, 2])\n', "ERROR"))
        self.assertNotIn("ZERO_WIDTH_PLOT", codes('axes.plot(f, x_range=[start, tracker.get_value()])\n', "ERROR"))

    def test_syntax_error_not_silently_accepted(self):
        with self.assertRaises(SyntaxError):
            audit_scene.audit_source('class Bad、Scene(Scene): pass')


class GeometryVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import verify_geometry
        except ImportError as exc:
            raise unittest.SkipTest(f"NumPy unavailable: {exc}")
        cls.validator = verify_geometry

    def test_sample_fixture_passes(self):
        spec = json.loads((Path(__file__).resolve().parent.parent / "references"
                           / "geometry_spec.example.json").read_text(encoding="utf-8"))
        v = self.validator
        self.assertEqual(v.verify_numeric_checks(spec) + v.verify_angles(spec)
                         + v.verify_boundaries(spec), [])

    def test_wrong_angle_and_overflow_detected(self):
        spec = {"points": {"A": [0, 0], "B": [1, 0], "C": [1, 1]},
                "checks": [{"type": "angle", "a": "A", "vertex": "B", "c": "C",
                            "kind": "minor", "expected_degrees": 45}],
                "bounding_boxes": [{"label": "outside", "bbox": [3.9, 0, 4.2, 2]}]}
        self.assertTrue(self.validator.verify_angles(spec))
        self.assertTrue(self.validator.verify_boundaries(spec))

    def test_zero_length_segment_rejected(self):
        spec = {"points": {"A": [1, 1], "B": [1, 1], "C": [0, 0], "D": [1, 0]},
                "checks": [{"type": "parallel", "a": "A", "b": "B", "c": "C", "d": "D"}]}
        self.assertTrue(self.validator.verify_numeric_checks(spec))


if __name__ == "__main__":
    unittest.main()
