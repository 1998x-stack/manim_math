"""Standard-library regression tests for curriculum prompt generator."""
import json
import tempfile
import unittest
from pathlib import Path
from prompt_suite import (PLATFORMS, entry_text, git_blob_sha, inventory,
                          make_index, problem_data, prompt_path, sync_or_check,
                          validate_vars, expanded)


class CurriculumPromptSuiteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.lesson = "小学/一年级/上册/第一章/001数一数/prompt.md"
        self.source = self.root / self.lesson
        self.source.parent.mkdir(parents=True)
        self.source.write_text('<problem>{"年级":"一年级","学期":"上册","知识点":"数一数"}</problem>', encoding="utf-8")

    def test_inventory_and_three_platforms(self):
        rows = inventory(self.root)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["git_blob_sha"], git_blob_sha(self.source.read_bytes()))
        self.assertEqual(make_index(rows)["count"], 1)
        self.assertEqual(len({prompt_path(p, self.lesson) for p in PLATFORMS}), 3)
        self.assertEqual(sync_or_check(self.root, rows, False, False), [])
        self.assertEqual(sync_or_check(self.root, rows, True, False), [])
        text = (self.root / prompt_path(".pi", self.lesson)).read_text(encoding="utf-8")
        self.assertIn("GOAL={{GOAL}}", text)
        self.assertIn("SOURCE_PROMPT=" + self.lesson, text)

    def test_drift_and_non_destructive_repair(self):
        rows = inventory(self.root)
        sync_or_check(self.root, rows, False, False)
        entry = self.root / prompt_path(".codex", self.lesson)
        entry.write_text("manual edit", encoding="utf-8")
        self.assertTrue(sync_or_check(self.root, rows, True, False))
        self.assertTrue(sync_or_check(self.root, rows, False, False))
        self.assertEqual(entry.read_text(), "manual edit")
        self.assertEqual(sync_or_check(self.root, rows, False, True), [])
        self.source.write_text(self.source.read_text() + "\n", encoding="utf-8")
        self.assertTrue(sync_or_check(self.root, inventory(self.root), True, False))

    def test_problem_and_conflict(self):
        rows = inventory(self.root)
        self.assertEqual(problem_data(self.root, rows[0])["status"], "parsed")
        self.source.write_text('<problem>{"年级":"二年级"}</problem>', encoding="utf-8")
        self.assertEqual(problem_data(self.root, inventory(self.root)[0])["status"], "needs_review")
        self.source.write_text('<problem>{}</problem><problem>{}</problem>', encoding="utf-8")
        with self.assertRaises(ValueError):
            problem_data(self.root, inventory(self.root)[0])

    def test_variables_and_unknown_sources(self):
        values = validate_vars(["GOAL=完成一一对应点数", "SCENE_CLASS=CountObjects"])
        result = expanded(entry_text(".pi", inventory(self.root)[0]), values)
        self.assertIn("GOAL=完成一一对应点数", result)
        self.assertNotIn("{{GOAL}}", result)
        for var in ("DURATION_S=0", "SCENE_CLASS=bad name", "QUALITY=ultra",
                    "MUSIC_POLICY=download", "INVALID=something"):
            with self.assertRaises(ValueError):
                validate_vars([var])

    def test_symlink_and_extra_file(self):
        rows = inventory(self.root)
        sync_or_check(self.root, rows, False, False)
        extra = self.root / ".pi/prompts/curriculum/extra/prompt.txt"
        extra.parent.mkdir(parents=True)
        extra.write_text("preserve", encoding="utf-8")
        self.assertTrue(any("orphan" in x for x in sync_or_check(self.root, rows, True, False)))
        self.assertTrue(extra.exists())


if __name__ == "__main__":
    unittest.main()
