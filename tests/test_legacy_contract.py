"""No-Manim contract tests for the legacy Gallery baseline."""
import json
import unittest

from tools.legacy_contract import canonical_bytes, compare, snapshot


def catalog(*topics):
    return {"levels": [{"id": "xiaoxue", "grades": [{"name": "一年级", "semesters": [{"name": "上册", "chapters": [{"name": "第一章", "topics": list(topics)}]}]}]}]}


def topic(identifier="old-1", path="小学/a/scene.py", video=None):
    return {"id": identifier, "number": "001", "name": "示例", "docstring": "测试", "pyFile": path, "videoFile": video, "hasVideo": video is not None}


def make_snapshot(*topics):
    return snapshot(canonical_bytes(catalog(*topics)))


class LegacyContractTests(unittest.TestCase):
    def test_snapshot_is_deterministic_and_retains_all_legacy_fields(self):
        first = make_snapshot(topic("z"), topic("a"))
        second = make_snapshot(topic("z"), topic("a"))
        self.assertEqual(canonical_bytes(first), canonical_bytes(second))
        self.assertEqual([entry["legacy_id"] for entry in first["records"]], ["a", "z"])
        self.assertEqual(first["records"][0]["pyFile"], "小学/a/scene.py")
        self.assertEqual(first["count"], 2)

    def test_duplicate_id_is_rejected_even_when_titles_differ(self):
        with self.assertRaisesRegex(ValueError, "duplicate legacy id"):
            make_snapshot(topic("same"), topic("same", path="小学/b.py"))

    def test_inconsistent_video_status_is_rejected(self):
        data = catalog(topic())
        data["levels"][0]["grades"][0]["semesters"][0]["chapters"][0]["topics"][0]["hasVideo"] = True
        with self.assertRaisesRegex(ValueError, "inconsistent video flags"):
            snapshot(json.dumps(data).encode("utf-8"))

    def test_rename_is_reported_without_reassigning_legacy_id(self):
        old = make_snapshot(topic("old-1", "external/old.py"))
        new = make_snapshot(topic("old-1", "external/new.py"))
        delta = compare(new, old)
        self.assertEqual(delta["added"], [])
        self.assertEqual(delta["removed"], [])
        self.assertEqual(delta["changed"]["old-1"]["pyFile"], {"before": "external/old.py", "after": "external/new.py"})

    def test_removed_entry_is_explicitly_reported(self):
        old = make_snapshot(topic("old-1"), topic("old-2"))
        new = make_snapshot(topic("old-1"))
        self.assertEqual(compare(new, old)["removed"], ["old-2"])


if __name__ == "__main__":
    unittest.main()
