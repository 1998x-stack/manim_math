"""高一数学自检脚本的无 Manim 回归测试。"""
import importlib.util
from pathlib import Path
import unittest
from math import pi

ROOT = Path(__file__).resolve().parents[1]
SET_CHECKER = (ROOT / '高中' / '高一' / '第一学期' / '第一章-集合与命题'
               / '002集合间的关系' / 'verify_sets.py')
TRIG_CHECKER = (ROOT / '高中' / '高一' / '第二学期' / '第六章-三角函数'
                / '003函数y=Asin(ωx+φ)的图像与性质' / 'verify_geometry.py')


def load_checker(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HighSchoolMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sets = load_checker(SET_CHECKER, 'gaoyi_verify_sets')
        cls.trig = load_checker(TRIG_CHECKER, 'gaoyi_verify_trigonometry')

    def test_set_theory(self):
        self.sets.verify_set_theory()
        self.sets.verify_geometry()
        self.sets.verify_boundaries()
        self.assertEqual(self.sets.powerset(set()), [frozenset()])
        self.assertEqual(len(self.sets.powerset({1, 2, 3})), 8)

    def test_venn_rejects_noncontaining_and_negative_radius(self):
        inside = self.sets.circle_inside_circle
        self.assertTrue(inside((0, 0), 1, (0, 0), 2))
        self.assertFalse(inside((2, 0), 1, (0, 0), 2))
        self.assertFalse(inside((0, 0), -1, (0, 0), 2))

    def test_sine_non_degenerate(self):
        self.trig.verify_trigonometric_transform()
        props = self.trig.sine_properties(-2, -4, pi / 2, 1)
        self.assertAlmostEqual(props['period'], pi / 2)
        self.assertAlmostEqual(props['horizontal_shift'], pi / 8)
        self.assertEqual(props['range'], (-1, 3))

    def test_sine_degenerate(self):
        self.assertIsNone(self.trig.sine_properties(0, 2, 0, 3)['period'])
        props = self.trig.sine_properties(2, 0, pi / 2, 1)
        self.assertEqual(props['range'], (3, 3))
        self.assertIsNone(props['period'])
        self.assertIsNone(props['horizontal_shift'])


if __name__ == '__main__':
    unittest.main()
