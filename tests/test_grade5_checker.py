"""Tests for the dependency-free grade-five source inventory."""

from fractions import Fraction
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from check_grade5 import scan_source, scan_tree  # noqa: E402


class GradeFiveAuditTests(unittest.TestCase):
    def test_weighted_average_exact(self):
        self.assertEqual(Fraction(90 * 10 + 85 * 15 + 80 * 5, 30), Fraction(515, 6))
        self.assertEqual(round(float(Fraction(515, 6)), 1), 85.8)

    def test_docstring_mismatch_is_detected(self):
        code = '"""平均分 = 85.5"""\nclass AverageCalculationLesson: pass\n'
        findings = scan_source(code, '小学/五年级/002_平均数的计算.py')
        self.assertIn('MATH_DOC_MISMATCH', [f.code for f in findings])

    def test_generic_placeholder_and_escaped_newline(self):
        code = 'class Lesson:\n def go(self):\n  Text("正在学习某知识...\\\\n继续")\n'
        findings = scan_source(code, '小学/五年级/example.py')
        self.assertEqual({'PLACEHOLDER_SCENE', 'LITERAL_NEWLINE'},
                         {f.code for f in findings})

    def test_grade_scope_and_syntax_errors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            grade = root / '小学' / '五年级'
            grade.mkdir(parents=True)
            (grade / 'bad.py').write_text('def bad(:\n', encoding='utf-8')
            (root / 'outside.py').write_text('def bad(:\n', encoding='utf-8')
            count, findings = scan_tree(root)
            self.assertEqual(count, 1)
            self.assertEqual([f.code for f in findings], ['PYTHON_SYNTAX'])


if __name__ == '__main__':
    unittest.main()
