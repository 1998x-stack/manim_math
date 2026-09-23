"""Offline tests for grade-12 audit and guarded edits; no Manim dependency."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1] / 'tools'


def load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


audit = load('audit_grade12')
repair = load('repair_known_issues')


class AuditTests(unittest.TestCase):
    def test_syntax_and_total_probability(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'bad.py').write_text('def f(:\n pass', encoding='utf-8')
            (root / 'formula.py').write_text(
                'formula = r"= 0.3 \\times 0.8 + 0.4 \\times 0.5 + 0.3 \\times 0.3 = 0.52"\n',
                encoding='utf-8')
            findings, counts = audit.audit(root)
            self.assertEqual(counts['python'], 2)
            self.assertEqual({x['code'] for x in findings}, {'SYNTAX', 'TOTAL_PROBABILITY'})

    def test_euler_math_and_global_rng(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'shape.py').write_text(
                'import numpy as np\nclass Shape:\n'
                ' def make(self):\n  np.random.seed(42)\n'
                '  self.euler_data = {"bad": {"V":4,"E":6,"F":5}}\n',
                encoding='utf-8')
            codes = {x['code'] for x in audit.audit(root)[0]}
            self.assertEqual(codes, {'GLOBAL_RNG', 'EULER_DATA'})

    def test_metadata_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'description.json').write_text('[1,2]', encoding='utf-8')
            self.assertEqual(audit.audit(root)[0][0]['code'], 'JSON')


class GuardedRepairTests(unittest.TestCase):
    def test_idempotent_and_reject_ambiguous(self):
        edits = [('old', 'new')]
        self.assertEqual(repair.proposed_edits('old', edits, 'x'), ('new', 1))
        self.assertEqual(repair.proposed_edits('new', edits, 'x'), ('new', 0))
        with self.assertRaises(ValueError):
            repair.proposed_edits('old old', edits, 'x')
        with self.assertRaises(ValueError):
            repair.proposed_edits('missing', edits, 'x')

    def test_plan_is_atomic_and_apply_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, edits in repair.FIXES.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                if name.endswith('cond_prob_animation.py'):
                    source = 'formula = ' + edits[0][0] + '\n'
                elif name.endswith('freq_prob_animation.py'):
                    source = ('import numpy as np\nclass Demo:\n'
                              '    def setup(self):\n' + edits[0][0] + '\n'
                              '        Text("n 越大，频率越接近概率", font=AUTHOR_FONT, color="white")\n'
                              '        sentence = "频率的极限（稳定值）"\n')
                else:
                    source = ('class Demo:\n    def verify(self):\n'
                              '        for name, data in []:\n            result = 3\n'
                              + edits[0][0] + '\n')
                path.write_text(source, encoding='utf-8')
            self.assertEqual(repair.run(root), (3, 5))
            self.assertEqual(repair.run(root, apply=True), (3, 5))
            self.assertEqual(repair.run(root), (0, 0))
            target = root / next(iter(repair.FIXES))
            self.assertIn('0.53', target.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
