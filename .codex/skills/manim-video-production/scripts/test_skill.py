"""Run: python -m unittest discover -s scripts -p 'test_*.py'"""
import json
from pathlib import Path
import tempfile
import unittest

import audit_scene


BASE = "config.frame_width = 9\nconfig.frame_height = 16\nclass Demo(Scene):\n    pass\n"


class SceneAuditTests(unittest.TestCase):
    def test_cjk_and_degree_in_mathtex_are_errors(self):
        source = BASE + 'MathTex(r"\\text{中文}")\nMathTex("90°")\n'
        codes = {finding["code"] for finding in audit_scene.audit_source(source) if finding["level"] == "ERROR"}
        self.assertEqual(codes, {"CJK_IN_MATHTEX", "DEGREE_IN_MATHTEX"})

    def test_supported_mathtex_is_not_flagged(self):
        source = BASE + 'MathTex(r"A=\\\\{1,2,3\\\\}")\n'
        errors = [f for f in audit_scene.audit_source(source) if f["level"] == "ERROR"]
        self.assertEqual(errors, [])

    def test_dynamic_mathtex_warns(self):
        codes = {f["code"] for f in audit_scene.audit_source(BASE + "MathTex(formula)\n")}
        self.assertIn("DYNAMIC_MATHTEX", codes)

    def test_bad_keywords(self):
        codes = {f["code"] for f in audit_scene.audit_source(BASE + "Sector(inner_radius=1)\nRectangle(corner_radius=1)\n")}
        self.assertIn("UNSUPPORTED_KEYWORD", codes)


class GeometryVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import verify_geometry
        except ImportError as exc:
            raise unittest.SkipTest(f"NumPy unavailable: {exc}")
        cls.validator = verify_geometry

    def test_sample_fixture_passes(self):
        path = Path(__file__).resolve().parent.parent / "references" / "geometry_spec.example.json"
        spec = json.loads(path.read_text(encoding="utf-8"))
        v = self.validator
        self.assertEqual(v.verify_numeric_checks(spec) + v.verify_angles(spec) + v.verify_boundaries(spec), [])

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
