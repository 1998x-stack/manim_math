"""同角三角比与诱导公式纯数学回归；不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('trig_induction.py')


def near(a, b):
    return math.isclose(a, b, rel_tol=1e-11, abs_tol=1e-11)


class TrigInductionTest(unittest.TestCase):
    def test_pythagorean_identity_all_quadrants(self):
        for alpha in (-7.5, -math.pi, -math.pi/2, 0, .1, math.pi/6, math.pi/2, math.pi, 9):
            self.assertTrue(near(math.sin(alpha)**2 + math.cos(alpha)**2, 1))

    def test_tangent_relation_when_defined(self):
        for alpha in (-3.7, -1.2, -.2, 0, .1, math.pi/6, 1.2, math.pi):
            self.assertGreater(abs(math.cos(alpha)), 1e-8)
            tangent = math.sin(alpha) / math.cos(alpha)
            self.assertTrue(near(tangent, math.tan(alpha)))
            self.assertTrue(near(1+tangent*tangent, 1/(math.cos(alpha)**2)))

    def test_undefined_tangent_on_vertical_axis(self):
        for alpha in (math.pi/2, 3*math.pi/2, -math.pi/2):
            self.assertLess(abs(math.cos(alpha)), 1e-12)

    def test_pi_minus_induction(self):
        for alpha in (-2, -.4, 0, math.pi/6, 2.3):
            self.assertTrue(near(math.sin(math.pi-alpha), math.sin(alpha)))
            self.assertTrue(near(math.cos(math.pi-alpha), -math.cos(alpha)))
            self.assertTrue(near(math.tan(math.pi-alpha), -math.tan(alpha)))

    def test_halfpi_minus_induction(self):
        for alpha in (-2, -.4, math.pi/6, 1.2, 2.3):
            self.assertTrue(near(math.sin(math.pi/2-alpha), math.cos(alpha)))
            self.assertTrue(near(math.cos(math.pi/2-alpha), math.sin(alpha)))
            self.assertGreater(abs(math.sin(alpha)), 1e-8)
            self.assertTrue(near(math.tan(math.pi/2-alpha),
                                 math.cos(alpha)/math.sin(alpha)))

    def test_negative_angle_induction(self):
        for alpha in (-3, -1, 0, math.pi/6, 2):
            self.assertTrue(near(math.sin(-alpha), -math.sin(alpha)))
            self.assertTrue(near(math.cos(-alpha), math.cos(alpha)))
            self.assertTrue(near(math.tan(-alpha), -math.tan(alpha)))

    def test_reflection_coordinates(self):
        alpha = math.pi/6
        x, y = math.cos(alpha), math.sin(alpha)
        self.assertTrue(near(math.cos(math.pi-alpha), -x))
        self.assertTrue(near(math.sin(math.pi-alpha), y))
        self.assertTrue(near(math.cos(math.pi/2-alpha), y))
        self.assertTrue(near(math.sin(math.pi/2-alpha), x))
        self.assertTrue(near(math.cos(-alpha), x))
        self.assertTrue(near(math.sin(-alpha), -y))

    def test_real_scene_contains_domain_and_true_unit_scaling(self):
        source = SOURCE.read_text(encoding='utf-8')
        tree = ast.parse(source)
        self.assertTrue(any(isinstance(node, ast.ClassDef) and node.name == 'TrigInduction'
                            for node in tree.body))
        self.assertIn('np.linalg.norm(axes.c2p(1, 0) - center)', source)
        self.assertIn(r'\cos\alpha\ne0', source)
        self.assertIn(r'\sin\alpha\ne0', source)
        self.assertNotIn('set_font_size(', source)
        self.assertNotIn('tan_seg_lbl', source)


if __name__ == '__main__':
    unittest.main()
