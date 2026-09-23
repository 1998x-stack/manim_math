"""No Manim dependency: exercise checkpoint logic with faithful Mobject-like fakes."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from runtime_probe import assert_checkpoint, inspect_checkpoint


class FakeMobject:
    def __init__(self, bbox, *, children=()):
        self.bbox = bbox
        self.submobjects = list(children)

    def get_left(self):
        return (self.bbox[0], 0, 0)

    def get_right(self):
        return (self.bbox[2], 0, 0)

    def get_bottom(self):
        return (0, self.bbox[1], 0)

    def get_top(self):
        return (0, self.bbox[3], 0)

    def get_center(self):
        return ((self.bbox[0] + self.bbox[2]) / 2, (self.bbox[1] + self.bbox[3]) / 2, 0)


class FakeScene:
    def __init__(self, *mobjects):
        self.mobjects = list(mobjects)


class RuntimeProbeTests(unittest.TestCase):
    def test_visible_object_and_child_pass(self):
        child = FakeMobject([-1, -1, 1, 1])
        group = FakeMobject([-1, -1, 1, 1], children=[child])
        result = inspect_checkpoint(FakeScene(group), {"child": child}, expected_centers={"child": (0, 0)})
        self.assertEqual(result["status"], "pass")
        self.assertEqual(result["samples"]["child"]["bbox"], [-1.0, -1.0, 1.0, 1.0])

    def test_full_bbox_catches_partial_overflow(self):
        obj = FakeMobject([3.8, -1, 4.2, 1])
        result = inspect_checkpoint(FakeScene(obj), {"label": obj})
        self.assertIn("OUT_OF_SAFE_BOUNDS", [f["code"] for f in result["findings"]])

    def test_detached_identity_catches_replaced_object(self):
        old, new = FakeMobject([-1, -1, 1, 1]), FakeMobject([-1, -1, 1, 1])
        result = inspect_checkpoint(FakeScene(new), {"old": old})
        self.assertEqual(result["findings"][0]["code"], "NOT_IN_SCENE")

    def test_model_screen_disagreement_detected(self):
        obj = FakeMobject([-1, -1, 1, 1])
        result = inspect_checkpoint(FakeScene(obj), {"A": obj}, expected_centers={"A": (1, 0)}, tolerance=0.01)
        self.assertEqual(result["findings"][0]["code"], "CENTER_MISMATCH")

    def test_different_animation_states_must_be_checked_separately(self):
        obj = FakeMobject([-1, -1, 1, 1])
        scene = FakeScene(obj)
        self.assertEqual(inspect_checkpoint(scene, {"point": obj})["status"], "pass")
        obj.bbox = [-1, -1, 5, 1]
        self.assertEqual(inspect_checkpoint(scene, {"point": obj})["status"], "fail")

    def test_report_written_on_failed_checkpoint(self):
        obj = FakeMobject([-1, -1, 5, 1])
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "probe.jsonl"
            with patch.dict(os.environ, {"MANIM_PROBE_REPORT": str(report)}):
                with self.assertRaises(AssertionError):
                    assert_checkpoint(FakeScene(obj), "ending", {"plot": obj})
            row = json.loads(report.read_text(encoding="utf-8").splitlines()[0])
            self.assertEqual(row["checkpoint"], "ending")
            self.assertEqual(row["status"], "fail")

    def test_invalid_inputs_rejected(self):
        obj = FakeMobject([0, 0, 1, 1])
        with self.assertRaises(ValueError):
            inspect_checkpoint(FakeScene(obj), {"point": obj}, safe_bounds=[0, 0, 0, 1])
        with self.assertRaises(ValueError):
            inspect_checkpoint(FakeScene(obj), {"point": obj}, expected_centers={"missing": (0, 0)})


if __name__ == "__main__":
    unittest.main()
