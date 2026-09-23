"""Isolated regressions for read-only legacy resource audit."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'tools' / 'audit_resource_references.py'
spec = importlib.util.spec_from_file_location('audit_resource_references', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class LegacyResourceAuditTests(unittest.TestCase):
    def test_reports_literal_references_without_changing_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'files').mkdir()
            (root / 'tools').mkdir()
            (root / 'files/grade1.json').write_text('{"grade": 1}', encoding='utf-8')
            (root / 'tools/consumer.py').write_text('SOURCE = "files/grade1.json"\n', encoding='utf-8')
            before = (root / 'files/grade1.json').read_bytes()
            report = module.audit(root, include_untracked=True)
            item = next(x for x in report['candidates'] if x['path'] == 'files/grade1.json')
            self.assertEqual(item['path_references'], ['tools/consumer.py'])
            self.assertEqual(item['decision'], 'needs_review')
            self.assertEqual((root / 'files/grade1.json').read_bytes(), before)

    def test_empty_python_and_legacy_skills_are_review_not_delete(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'external').mkdir()
            (root / 'skills').mkdir()
            (root / 'external/ceva_theorem.py').write_bytes(b'')
            (root / 'skills/manim.skill').write_text('archive', encoding='utf-8')
            report = module.audit(root, include_untracked=True)
            results = {x['path']: x for x in report['candidates']}
            self.assertEqual(results['external/ceva_theorem.py']['kind'], 'empty-python')
            self.assertEqual(results['skills/manim.skill']['kind'], 'legacy-skill-archive')
            self.assertTrue(all(x['decision'] == 'needs_review' for x in results.values()))


if __name__ == '__main__':
    unittest.main()
