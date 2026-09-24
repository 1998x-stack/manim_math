"""高三第一学期第十四章第001课：不依赖 Manim 的三维数学回归。"""

import runpy
import unittest
from pathlib import Path


LESSON = (Path(__file__).resolve().parents[1]
          / '第一学期' / '第十四章-空间直线与平面'
          / '001平面的基本性质' / 'verify_plane_axioms.py')


class PlaneAxiomsMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = runpy.run_path(str(LESSON), run_name='plane_axioms_test')

    def test_line_in_plane(self):
        self.model['test_axiom_1']()

    def test_three_points_and_collinear_counterexample(self):
        self.model['test_axiom_2']()

    def test_distinct_planes_intersect_in_line(self):
        self.model['test_axiom_3']()

    def test_four_plane_determination_conditions(self):
        self.model['test_four_plane_conditions']()


if __name__ == '__main__':
    unittest.main()
