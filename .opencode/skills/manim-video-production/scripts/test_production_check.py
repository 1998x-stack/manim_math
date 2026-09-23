"""Stdlib-only regression for the opt-in production gate."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import production_check


LESSON = "config.frame_width = 9\nconfig.frame_height = 16\nclass Demo(Scene):\n    pass\n"


class ProductionGateTests(unittest.TestCase):
    def test_static_only_must_be_partial_not_video_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lesson = root / "lesson.py"
            lesson.write_text(LESSON, encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                status = production_check.main([str(lesson), "Demo", "--out-dir", str(root / "out")])
            self.assertEqual(status, 0)
            report_path = next((root / "out").glob("*/report.json"))
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "partial")
            self.assertEqual(report["checks"]["syntax"]["status"], "pass")
            self.assertEqual(report["checks"]["manim_render"]["status"], "not_run")

    def test_lesson_math_failure_blocks_render(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lesson, math_test = root / "lesson.py", root / "test_math.py"
            lesson.write_text(LESSON, encoding="utf-8")
            math_test.write_text("raise SystemExit(1)\n", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                status = production_check.main([str(lesson), "Demo", "--math-test", str(math_test),
                                                "--out-dir", str(root / "out")])
            self.assertEqual(status, 2)
            report = json.loads(next((root / "out").glob("*/report.json")).read_text(encoding="utf-8"))
            self.assertEqual(report["checks"]["math_test"]["status"], "fail")
            self.assertNotIn("manim_render", report["checks"])

    def test_ffprobe_rejects_wrong_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            log = root / "probe.log"
            payload = {"streams": [{"codec_type": "video", "width": 1920, "height": 1080}],
                       "format": {"duration": "4.0"}}
            def fake_command(cmd, target, **kwargs):
                target.write_text(json.dumps(payload), encoding="utf-8")
                return {"status": "pass", "command": cmd}
            with patch.object(production_check, "run_command", side_effect=fake_command):
                result = production_check.probe_video(root / "video.mp4", log, 1080, 1920)
            self.assertEqual(result["status"], "fail")
            self.assertIn("actual dimensions", result["reason"])

    def test_checkpoint_log_cannot_pass_with_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.jsonl"
            self.assertEqual(production_check.inspect_checkpoints(path)["status"], "not_run")
            path.write_text(json.dumps({"status": "fail", "findings": [{"code": "OVERFLOW"}]}) + "\n", encoding="utf-8")
            self.assertEqual(production_check.inspect_checkpoints(path)["status"], "fail")
            path.write_text(json.dumps({"status": "pass", "findings": []}) + "\n", encoding="utf-8")
            self.assertEqual(production_check.inspect_checkpoints(path)["status"], "pass")


if __name__ == "__main__":
    unittest.main()
