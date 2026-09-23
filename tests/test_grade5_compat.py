"""Verify legacy fifth-grade scene entrypoints without requiring Manim."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASES = (
    ('第一学期/第三章-统计/001平均数的意义', '001平均数的意义_animation.py',
     '001_平均数的意义.py', 'Topic001平均数的意义Animation', 'AverageMeaningLesson'),
    ("第一学期/第四章-简易方程(一)/003等式的性质", '003等式的性质_animation.py',
     '003_等式的性质.py', 'Topic003等式的性质Animation', 'EqualityPropertyLesson'),
    ("第二学期/第三章-分数的意义和性质/001单位'1'", '001单位_1__animation.py',
     "001_单位'1'.py", 'Topic001单位1Animation', 'UnitOneLesson'),
)


class LegacyEntrypointTests(unittest.TestCase):
    def test_aliases_reuse_the_correct_primary_lesson(self):
        for directory, wrapper, primary, old_class, primary_class in CASES:
            with self.subTest(directory=directory), tempfile.TemporaryDirectory() as tmp:
                wrapper_source = (ROOT / '小学' / '五年级' / directory / wrapper).read_text(
                    encoding='utf-8')
                self.assertNotIn('正在学习', wrapper_source)
                # A minimal primary scene avoids importing Manim in a pure-Python unit test.
                folder = Path(tmp)
                (folder / wrapper).write_text(wrapper_source, encoding='utf-8')
                (folder / primary).write_text(
                    f'class {primary_class}:\n    def construct(self):\n        return "primary"\n',
                    encoding='utf-8')
                spec = importlib.util.spec_from_file_location('legacy_compat', folder / wrapper)
                module = importlib.util.module_from_spec(spec)
                assert spec.loader is not None
                spec.loader.exec_module(module)
                alias = getattr(module, old_class)
                self.assertTrue(issubclass(alias, getattr(module, primary_class)))
                self.assertEqual(alias().construct(), 'primary')


if __name__ == '__main__':
    unittest.main()
