"""No-Manim regression tests for the grade-one high-school static scanner."""
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from audit_gaoyi import audit, audit_source


class AuditGaoyiTests(unittest.TestCase):
    def test_scene_and_duplicate_target(self):
        source = '''from manim import *
class Lesson(Scene):
    def construct(self):
        label = Text("集合")
        self.play(Write(label), Indicate(label))
'''
        scenes, findings = audit_source(source)
        self.assertEqual(scenes, ['Lesson'])
        self.assertEqual([f['rule'] for f in findings], ['duplicate-play-target'])

    def test_chinese_tex_and_import_side_effect(self):
        source = 'config.frame_width = 9\nx = MathTex("中文")\ny = Text("中文")\n'
        _, findings = audit_source(source)
        self.assertEqual({f['rule'] for f in findings}, {'chinese-in-tex', 'module-config'})

    def test_syntax_error_produces_error(self):
        _, findings = audit_source('def scene(:\n')
        self.assertEqual(findings[0]['severity'], 'error')

    def test_recursive_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            file = base / '第一学期' / '第一章' / 'lesson.py'
            file.parent.mkdir(parents=True)
            file.write_text('class Lesson(Scene):\n    pass\n', encoding='utf-8')
            report = audit(base)
            self.assertEqual(report['python_count'], 1)
            self.assertEqual(report['scene_count'], 1)
            self.assertEqual(report['by_semester'], {'第一学期': 1})
            self.assertEqual(report['findings'], [])

    def test_nonexistent_or_empty_directory_not_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                audit(Path(tmp) / 'missing')
            with self.assertRaises(FileNotFoundError):
                audit(Path(tmp))


if __name__ == '__main__':
    unittest.main()
