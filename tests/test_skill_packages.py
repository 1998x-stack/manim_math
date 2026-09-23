"""Full Skill package sync regression tests; Python stdlib only, no real repo writes."""
import tempfile
import unittest
from pathlib import Path

from tools.sync_skills import sync_packages


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.source = root / "source"
        self.package = self.source / "demo"
        (self.package / "references").mkdir(parents=True)
        (self.package / "scripts").mkdir()
        (self.package / "SKILL.md").write_text("---\nname: demo\n---\n", encoding="utf-8")
        (self.package / "references" / "guide.md").write_text("instructions", encoding="utf-8")
        (self.package / "scripts" / "check.py").write_text("print('fixture')\n", encoding="utf-8")
        self.targets = tuple(root / name / "skills" for name in ("codex", "opencode", "claude"))

    def test_missing_packages_fail_check_and_sync_copies_every_file(self):
        self.assertTrue(sync_packages(self.source, self.targets, check=True))
        self.assertEqual(sync_packages(self.source, self.targets), [])
        self.assertEqual(sync_packages(self.source, self.targets, check=True), [])
        for base in self.targets:
            self.assertEqual((base / "demo" / "references" / "guide.md").read_text(), "instructions")
            self.assertEqual((base / "demo" / "scripts" / "check.py").read_text(), "print('fixture')\n")

    def test_nested_drift_is_detected_and_repaired(self):
        self.assertEqual(sync_packages(self.source, self.targets), [])
        reference = self.targets[0] / "demo" / "references" / "guide.md"
        reference.write_text("outdated", encoding="utf-8")
        self.assertIn("drifted", " ".join(sync_packages(self.source, self.targets, check=True)))
        self.assertEqual(sync_packages(self.source, self.targets), [])
        self.assertEqual(reference.read_text(), "instructions")

    def test_orphans_are_reported_not_deleted(self):
        self.assertEqual(sync_packages(self.source, self.targets), [])
        extra = self.targets[0] / "demo" / "scripts" / "extra.py"
        extra.write_text("keep", encoding="utf-8")
        self.assertIn("orphan skill file", " ".join(sync_packages(self.source, self.targets)))
        self.assertTrue(extra.exists())

    def test_missing_manifest_and_symlinks_are_rejected(self):
        (self.package / "SKILL.md").unlink()
        self.assertIn("missing canonical SKILL.md", " ".join(sync_packages(self.source, self.targets, check=True)))
        (self.package / "SKILL.md").write_text("demo", encoding="utf-8")
        link = self.package / "references" / "outside.md"
        try:
            link.symlink_to(Path(self.temp.name) / "missing-target")
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        self.assertIn("symlink", " ".join(sync_packages(self.source, self.targets, check=True)))


if __name__ == "__main__":
    unittest.main()
