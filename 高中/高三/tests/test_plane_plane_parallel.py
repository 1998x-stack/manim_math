"""高三上第十四章 005 面面平行的纯数学回归。"""

import runpy
import unittest
from pathlib import Path


LESSON = (Path(__file__).resolve().parents[1] / '第一学期'
          / '第十四章-空间直线与平面' / '005平面与平面平行'
          / 'verify_plane_plane_parallel.py')


class PlanePlaneParallelMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = runpy.run_path(str(LESSON), run_name='plane_plane_test')

    def test_criterion_and_parallel_in_plane_counterexample(self):
        self.model['test_definition_and_criterion']()

    def test_two_sections_are_parallel(self):
        self.model['test_sections']()

    def test_equal_segments_require_endpoint_conditions(self):
        self.model['test_segments_and_endpoint_conditions']()


if __name__ == '__main__':
    unittest.main()
