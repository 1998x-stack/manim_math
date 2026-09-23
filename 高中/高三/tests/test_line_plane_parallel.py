"""高三上第十四章 003：将纯数学验证加入已有 Grade 12 CI。"""

import runpy
import unittest
from pathlib import Path


LESSON = (Path(__file__).resolve().parents[1] / '第一学期'
          / '第十四章-空间直线与平面' / '003直线与平面平行'
          / 'verify_line_plane_parallel.py')


class LinePlaneParallelMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checks = runpy.run_path(str(LESSON), run_name='line_plane_test')

    def test_definition_and_counterexample(self):
        self.checks['test_definition_and_counterexample']()

    def test_criterion_and_required_outside_condition(self):
        self.checks['test_criterion']()

    def test_property_and_required_intersection(self):
        self.checks['test_property']()


if __name__ == '__main__':
    unittest.main()
