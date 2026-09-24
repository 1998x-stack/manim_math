"""高三上第十四章 002 的三维数学断言纳入现有 unittest 发现机制。"""

import runpy
import unittest
from pathlib import Path


LESSON = (Path(__file__).resolve().parents[1] / '第一学期'
          / '第十四章-空间直线与平面' / '002空间直线的位置关系'
          / 'verify_spatial_lines.py')


class SpatialLinesMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = runpy.run_path(str(LESSON), run_name='spatial_lines_test')

    def test_three_relationships(self):
        self.model['test_three_relationships']()

    def test_parallel_construction_and_angle(self):
        self.model['test_angle_and_parallel_construction']()

    def test_common_perpendicular_and_distance(self):
        self.model['test_common_perpendicular']()


if __name__ == '__main__':
    unittest.main()
