"""高三上第十四章 004：线面垂直数学断言纳入仓库标准单测。"""

import runpy
import unittest
from pathlib import Path


LESSON = (Path(__file__).resolve().parents[1] / '第一学期'
          / '第十四章-空间直线与平面' / '004直线与平面垂直'
          / 'verify_line_plane_perpendicular.py')


class LinePlanePerpendicularTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tests = runpy.run_path(str(LESSON), run_name='line_plane_perpendicular_test')

    def test_intersecting_lines_criterion(self):
        self.tests['test_criterion_requires_intersection']()

    def test_plane_normal_and_parallel_normals(self):
        self.tests['test_plane_properties']()

    def test_skew_perpendicular_requires_projection_care(self):
        self.tests['test_skew_perpendicular_does_not_intersect']()


if __name__ == '__main__':
    unittest.main()
