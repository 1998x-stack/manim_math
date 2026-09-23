"""Ensure Skill mirrors never write via redirected target roots."""
import tempfile
import unittest
from pathlib import Path

from tools.sync_skills import sync_packages


class UnsafeMirrorRootTests(unittest.TestCase):
    def test_target_root_symlink_is_rejected_before_any_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "source" / "demo"
            package.mkdir(parents=True)
            (package / "SKILL.md").write_text("demo", encoding="utf-8")
            unrelated = root / "unrelated"
            unrelated.mkdir()
            mirror = root / "mirror"
            try:
                mirror.symlink_to(unrelated, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            errors = sync_packages(root / "source", (mirror,), check=False)
            self.assertTrue(any("symlink skills directory" in error for error in errors))
            self.assertEqual(list(unrelated.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
