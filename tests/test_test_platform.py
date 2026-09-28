import unittest
from pathlib import Path

from tools.test_platform import (
    changed_lessons,
    changed_render_matrix,
    render_matrix,
    renders_for_changes,
    selected_renders,
    validate_manifest,
)


class TestTestingPlatform(unittest.TestCase):
    def test_changed_lessons_deduplicates_course_directories(self):
        paths = ["初中/八年级/课/lesson.py", "初中/八年级/课/math_model.py", "docs/README.md"]
        self.assertEqual(["初中/八年级/课"], changed_lessons(paths))

    def test_changed_lessons_ignores_generated_media(self):
        self.assertEqual([], changed_lessons(["高中/高一/课/output.mp4"]))

    def test_render_tiers_are_cumulative(self):
        data = {"renders": [{"id": "a", "tier": "pr"}, {"id": "b", "tier": "main"}, {"id": "c", "tier": "nightly"}]}
        self.assertEqual(["a"], [x["id"] for x in selected_renders(data, "pr")])
        self.assertEqual(["a", "b"], [x["id"] for x in selected_renders(data, "main")])
        self.assertEqual(["a", "b", "c"], [x["id"] for x in selected_renders(data, "nightly")])

    def test_changed_render_selects_only_registered_lesson(self):
        data = {"renders": [
            {"id": "a", "source": "高中/高一/课A/lesson.py", "scene": "A", "tier": "nightly", "width": 270, "height": 480},
            {"id": "b", "source": "高中/高一/课B/lesson.py", "scene": "B", "tier": "nightly", "width": 270, "height": 480},
        ]}
        selected = renders_for_changes(data, ["高中/高一/课B/storyboard.md", "docs/x.md"])
        self.assertEqual(["b"], [item["id"] for item in selected])

    def test_changed_matrix_can_be_empty_without_fallback_render(self):
        data = {"renders": [{"id": "a", "source": "高中/高一/课A/lesson.py", "scene": "A", "tier": "nightly", "width": 270, "height": 480}]}
        self.assertEqual({"include": []}, changed_render_matrix(data, ["docs/README.md"]))

    def test_matrix_is_derived_from_manifest(self):
        data = {"renders": [{"id": "a", "tier": "nightly", "source": "a.py", "scene": "A", "width": 270, "height": 480}]}
        expected = {"include": [{"id": "a", "source": "a.py", "scene": "A", "width": 270, "height": 480, "resolution": "270,480"}]}
        self.assertEqual(expected, render_matrix(data, "nightly"))

    def test_manifest_rejects_duplicates_missing_sources_dimensions_and_domains(self):
        data = {
            "schema_version": 1,
            "required_render_domains": ["primary"],
            "suites": [{"id": "same"}],
            "renders": [{"id": "same", "source": "missing.py", "scene": "Scene", "tier": "nightly", "width": 0, "height": 480}],
        }
        errors = validate_manifest(data, Path("/definitely-not-a-repository"))
        self.assertTrue(any("duplicate id" in e for e in errors))
        self.assertTrue(any("source missing" in e for e in errors))
        self.assertTrue(any("positive width" in e for e in errors))
        self.assertTrue(any("needs domain" in e for e in errors))
        self.assertTrue(any("missing required render domains" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
