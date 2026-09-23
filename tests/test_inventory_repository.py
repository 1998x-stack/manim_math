"""Tests for the read-only filesystem inventory."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from inventory_repository import inventory  # noqa: E402


class InventoryTests(unittest.TestCase):
    def test_categories_and_review_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "小学" / "一年级").mkdir(parents=True)
            (root / "小学" / "一年级" / "empty.py").touch()
            (root / "docs").mkdir()
            (root / "docs" / "old.md").write_text("file:///Users/old/local.mp4", encoding="utf-8")
            (root / ".DS_Store").write_bytes(b"cached")
            (root / "videos").mkdir()
            (root / "videos" / "example.mp4").write_bytes(b"media")

            first = inventory(root, include_untracked=True)
            second = inventory(root, include_untracked=True)
            self.assertEqual(json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True))
            self.assertEqual(first["scope"], "working-tree")
            self.assertEqual(first["summary"]["listed_files"], 4)
            self.assertEqual(first["summary"]["by_category"]["curriculum"], 1)
            self.assertEqual(
                {(f["path"], f["code"]) for f in first["findings"]},
                {(".DS_Store", "OS_CACHE"), ("小学/一年级/empty.py", "EMPTY_PYTHON"),
                 ("docs/old.md", "LOCAL_FILE_URL")},
            )
            self.assertTrue((root / ".DS_Store").exists(), "inventory must not delete files")
            self.assertTrue((root / "小学" / "一年级" / "empty.py").exists())

    def test_nonexistent_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                inventory(Path(tmp) / "missing", include_untracked=True)


if __name__ == "__main__":
    unittest.main()
