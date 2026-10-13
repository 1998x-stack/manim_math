from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools import manimgx_audit, manimgx_migrate


class ManimGXCodemodTests(unittest.TestCase):
    def test_single_frame_width_assignment_is_removed(self):
        source = "from manim import *\nconfig.frame_width = 9\nconfig.frame_height = 16\n"
        migrated, changes = manimgx_migrate.migrate_text(source)
        self.assertIn("from manimgx import *", migrated)
        self.assertNotIn("config.frame_width =", migrated)
        self.assertIn("config.frame_height = 16", migrated)
        self.assertIn("frame_width:1", changes)

    def test_width_height_tuple_assignment_is_split_safely(self):
        source = "config.frame_width, config.frame_height = 9, 16\n"
        migrated, changes = manimgx_migrate.migrate_text(source)
        self.assertNotIn("config.frame_width,", migrated)
        self.assertIn("config.frame_height = 16", migrated)
        self.assertIn("legacy value was 9", migrated)
        self.assertIn("frame_width_tuple:1", changes)

    def test_height_width_tuple_assignment_is_split_safely(self):
        source = "m.config.frame_height, m.config.frame_width = 16, 9\n"
        migrated, changes = manimgx_migrate.migrate_text(source)
        self.assertIn("m.config.frame_height = 16", migrated)
        self.assertNotIn("m.config.frame_width =", migrated)
        self.assertIn("legacy value was 9", migrated)
        self.assertIn("frame_width_tuple:1", changes)

    def test_codemod_is_idempotent(self):
        source = "from manim import *\nconfig.frame_width, config.frame_height = 9, 16\n"
        once, _ = manimgx_migrate.migrate_text(source)
        twice, changes = manimgx_migrate.migrate_text(once)
        self.assertEqual(once, twice)
        self.assertEqual(changes, [])


class ManimGXAuditTests(unittest.TestCase):
    def _audit_source(self, source: str):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "scene.py"
            path.write_text(source, encoding="utf-8")
            return manimgx_audit.audit(Path(tmp))

    def test_tuple_frame_width_assignment_is_a_blocker(self):
        findings = self._audit_source(
            "from manimgx import *\nconfig.frame_width, config.frame_height = 9, 16\n"
        )
        codes = {(f.code, f.severity) for f in findings}
        self.assertIn(("READONLY_FRAME_WIDTH", "error"), codes)

    def test_alias_tuple_frame_width_assignment_is_a_blocker(self):
        findings = self._audit_source(
            "import manimgx as m\nm.config.frame_height, m.config.frame_width = 16, 9\n"
        )
        codes = {(f.code, f.severity) for f in findings}
        self.assertIn(("READONLY_FRAME_WIDTH", "error"), codes)

    def test_tex_template_is_a_python_blocker(self):
        findings = self._audit_source(
            "from manimgx import *\ntemplate = TexTemplate()\n"
        )
        codes = {(f.code, f.severity) for f in findings}
        self.assertIn(("TEX_TEMPLATE", "error"), codes)

    def test_timeline_and_font_debt_are_reported(self):
        findings = self._audit_source(
            'from manimgx import *\nFONT = "PingFang SC"\na = ValueTracker(1)\n'
        )
        codes = {(f.code, f.severity) for f in findings}
        self.assertIn(("SYSTEM_FONT", "warn"), codes)
        self.assertIn(("TIMELINE_SEMANTICS_REVIEW", "warn"), codes)


if __name__ == "__main__":
    unittest.main()
