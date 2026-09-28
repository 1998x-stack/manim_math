import unittest
from pathlib import Path
from tools.test_platform import changed_lessons, selected_renders, validate_manifest

class TestTestingPlatform(unittest.TestCase):
    def test_changed_lessons_deduplicates_course_directories(self):
        paths=["初中/八年级/课/lesson.py","初中/八年级/课/math_model.py","docs/README.md"]
        self.assertEqual(["初中/八年级/课"], changed_lessons(paths))
    def test_changed_lessons_ignores_generated_media(self):
        self.assertEqual([], changed_lessons(["高中/高一/课/output.mp4"]))
    def test_render_tiers_are_cumulative(self):
        data={"renders":[{"id":"a","tier":"pr"},{"id":"b","tier":"main"},{"id":"c","tier":"nightly"}]}
        self.assertEqual(["a"],[x["id"] for x in selected_renders(data,"pr")])
        self.assertEqual(["a","b"],[x["id"] for x in selected_renders(data,"main")])
        self.assertEqual(["a","b","c"],[x["id"] for x in selected_renders(data,"nightly")])
    def test_manifest_rejects_duplicates_and_missing_sources(self):
        data={"schema_version":1,"suites":[{"id":"same"}],"renders":[{"id":"same","source":"missing.py","scene":"Scene","tier":"nightly"}]}
        errors=validate_manifest(data,Path("/definitely-not-a-repository"))
        self.assertTrue(any("duplicate id" in e for e in errors))
        self.assertTrue(any("source missing" in e for e in errors))

if __name__ == "__main__": unittest.main()
