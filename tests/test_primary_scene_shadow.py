"""Fixture tests: shadow mapping must never rewrite Gallery or load Manim."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.primary_scene_shadow import build_shadow, main, safe_topic


class PrimarySceneShadowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.topic = "小学/三年级/上册/第一章/001认识数"
        self.directory = self.root / self.topic
        self.directory.mkdir(parents=True)
        (self.directory / "preview.py").write_text(
            "from manim import *\nclass ExamplePreview(Scene):\n"
            "    def construct(self): pass\n", encoding="utf-8",
        )
        (self.directory / "lesson.py").write_text(
            "from manim import *\nclass ExampleLesson(Scene):\n"
            "    def construct(self): pass\n", encoding="utf-8",
        )
        self.gallery = self.root / "assets/catalog.json"
        self.gallery.parent.mkdir(parents=True)
        self.gallery.write_text(json.dumps({"levels": [{
            "id": "xiaoxue", "grades": [{"semesters": [{"chapters": [{
                "topics": [{"id": "legacy-01", "pyFile": self.topic + "/preview.py",
                            "videoFile": self.topic + "/preview_finish.mp4"}]
            }]}]}]
        }]}), encoding="utf-8")
        self.manifest = self.root / "scene-manifest.json"
        self.entry = {
            "topic": self.topic, "status": "source-reviewed",
            "source": self.topic + "/lesson.py", "scene_class": "ExampleLesson",
            "evidence": "The dedicated full lesson source declares ExampleLesson.",
        }
        self.write_entries([self.entry])

    def write_entries(self, entries):
        self.manifest.write_text(
            json.dumps({"schema_version": 1, "mode": "shadow", "topics": entries},
                       ensure_ascii=False), encoding="utf-8",
        )

    def test_reviewed_selection_is_report_only_and_preserves_legacy_media(self):
        original_gallery = self.gallery.read_bytes()
        report = build_shadow(self.root, self.manifest)
        self.assertEqual(report["validation_errors"], [])
        self.assertEqual(report["summary"]["multi_python_topics_scanned"], 1)
        self.assertEqual(report["summary"]["source_reviewed"], 1)
        self.assertEqual(report["summary"]["shadow_gallery_source_diffs"], 1)
        self.assertEqual(report["summary"]["requires_media_review"], 1)
        item = report["records"][0]
        self.assertEqual(item["selected"]["scene_class"], "ExampleLesson")
        self.assertEqual(item["legacy_gallery"][0]["legacy_id"], "legacy-01")
        self.assertEqual(item["legacy_gallery"][0]["videoFile"],
                         self.topic + "/preview_finish.mp4")
        self.assertEqual(original_gallery, self.gallery.read_bytes())
        self.assertEqual(report, build_shadow(self.root, self.manifest))

    def test_unresolved_is_explicit_and_does_not_change_gallery(self):
        self.write_entries([{"topic": self.topic, "status": "needs-review",
                             "reason": "Two versions may implement different teaching sequences."}])
        report = build_shadow(self.root, self.manifest)
        self.assertEqual(report["validation_errors"], [])
        self.assertEqual(report["summary"]["needs_review"], 1)
        self.assertEqual(report["summary"]["shadow_gallery_source_diffs"], 0)
        self.assertIsNone(report["records"][0]["selected"])

    def test_rejects_mismatched_scene_class_and_missing_file(self):
        for source, scene in (
            (self.topic + "/lesson.py", "Unrelated"),
            (self.topic + "/unknown.py", "ExampleLesson"),
        ):
            with self.subTest(source=source):
                self.write_entries([{**self.entry, "source": source, "scene_class": scene}])
                report = build_shadow(self.root, self.manifest)
                self.assertTrue(report["validation_errors"])

    def test_rejects_escape_duplicate_and_unmapped_topic(self):
        bad = {**self.entry, "source": self.topic + "/../other.py"}
        self.write_entries([bad, self.entry])
        report = build_shadow(self.root, self.manifest)
        self.assertTrue(any("duplicate" in error for error in report["validation_errors"]))
        self.assertTrue(any("source must" in error for error in report["validation_errors"]))
        self.write_entries([])
        self.assertTrue(any("missing manifest topic" in error
                            for error in build_shadow(self.root, self.manifest)["validation_errors"]))

    def test_rejects_unreviewed_selection_and_absent_reason(self):
        self.write_entries([{"topic": self.topic, "status": "needs-review",
                             "source": self.topic + "/lesson.py", "scene_class": "ExampleLesson"}])
        report = build_shadow(self.root, self.manifest)
        self.assertEqual(len(report["validation_errors"]), 2)

    def test_path_validator_and_cli_non_git_completeness(self):
        self.assertTrue(safe_topic(self.topic))
        self.assertFalse(safe_topic(self.topic + "/../outside"))
        self.assertFalse(safe_topic("/" + self.topic))
        self.assertFalse(safe_topic("高中/三年级/上册/第一章/001"))
        outfile = self.root / "shadow.json"
        self.assertEqual(main(["--root", str(self.root), "--manifest", str(self.manifest),
                               "--output", str(outfile)]), 0)
        self.assertTrue(outfile.exists())
        self.assertEqual(main(["--root", str(self.root), "--manifest", str(self.manifest),
                               "--output", str(outfile), "--require-complete"]), 1)


if __name__ == "__main__":
    unittest.main()
