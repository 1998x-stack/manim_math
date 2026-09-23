"""对数函数纯数学专项测试；不需要 Manim，不代表成片渲染验证。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('logarithm_function.py')


def log_base(x, base):
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError('x>0, base>0, base!=1 required')
    return math.log(x) / math.log(base)


class LogarithmMathTest(unittest.TestCase):
    def test_domains(self):
        for x, base in [(0, 2), (-1, 2), (1, 0), (1, -2), (1, 1)]:
            with self.subTest(x=x, base=base), self.assertRaises(ValueError):
                log_base(x, base)

    def test_fixed_point(self):
        for base in (0.125, 0.5, 2, 10):
            self.assertAlmostEqual(log_base(1, base), 0)

    def test_sample_points(self):
        for x, expected_up, expected_down in [(1, 0, 0), (2, 1, -1), (4, 2, -2)]:
            self.assertAlmostEqual(log_base(x, 2), expected_up)
            self.assertAlmostEqual(log_base(x, 0.5), expected_down)

    def test_monotonicity_on_domain(self):
        xs = [0.125 + (6 - 0.125) * i / 128 for i in range(129)]
        up = [log_base(x, 2) for x in xs]
        down = [log_base(x, 0.5) for x in xs]
        self.assertTrue(all(a < b for a, b in zip(up, up[1:])))
        self.assertTrue(all(a > b for a, b in zip(down, down[1:])))

    def test_both_plot_ranges_fit_axes(self):
        for base in (2, 0.5):
            for i in range(129):
                x = 0.125 + (6 - 0.125) * i / 128
                self.assertGreaterEqual(x, 0)
                self.assertLessEqual(x, 6)
                self.assertGreaterEqual(log_base(x, base), -3 - 1e-12)
                self.assertLessEqual(log_base(x, base), 3 + 1e-12)

    def test_reciprocal_base_symmetry(self):
        for x in (0.125, 0.5, 1, 2, 4, 6):
            self.assertAlmostEqual(log_base(x, 0.5), -log_base(x, 2))

    def test_vertical_asymptote_not_a_domain_point(self):
        with self.assertRaises(ValueError):
            log_base(0, 2)
        self.assertLess(log_base(1e-6, 2), log_base(1e-3, 2))
        self.assertGreater(log_base(1e-6, 0.5), log_base(1e-3, 0.5))

    def test_actual_scene_source_preserves_safe_plot(self):
        source = SOURCE.read_text(encoding='utf-8')
        ast.parse(source)
        self.assertEqual(source.count('x_range=[0.125, 6]'), 2)
        self.assertNotIn('y_pos = -5.5', source)
        self.assertNotIn('a 不同, 单调性相反!', source)
        self.assertIn('class LogarithmFunction(Scene)', source)


if __name__ == '__main__':
    unittest.main()
