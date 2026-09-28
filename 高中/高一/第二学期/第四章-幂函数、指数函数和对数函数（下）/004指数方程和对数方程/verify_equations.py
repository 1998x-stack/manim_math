"""指数/对数方程专项纯数学与源码 AST 测试；不代表 Manim 渲染验收。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('exponential_logarithmic.py')


class EquationMathTest(unittest.TestCase):
    def test_exponential_solution(self):
        self.assertEqual(2**3, 8)
        self.assertTrue(all((2**x - 8) * (x - 3) > 0 for x in (-1, 0, 2, 4)))

    def test_logarithm_solution(self):
        self.assertAlmostEqual(math.log2(8), 3)
        self.assertGreater(8, 0)

    def test_exp_curve_within_axes(self):
        low, high = -1, math.log2(9)
        for i in range(101):
            x = low + (high - low) * i / 100
            self.assertLessEqual(2**x, 9 + 1e-12)
            self.assertGreaterEqual(2**x, 0)
            self.assertLessEqual(x, 4)

    def test_log_curve_within_axes(self):
        for i in range(101):
            x = 0.5 + (10 - 0.5) * i / 100
            self.assertGreater(x, 0)
            self.assertGreaterEqual(math.log2(x), -1)
            self.assertLessEqual(math.log2(x), 4)

    def test_log_equation_domain_and_extraneous_root(self):
        # log₂(x-1)+log₂(x-3)=3 的原始定义域 x>3。
        roots = (5, -1)
        self.assertTrue(all((x-1)*(x-3) == 8 for x in roots))
        admissible = [x for x in roots if x - 1 > 0 and x - 3 > 0]
        self.assertEqual(admissible, [5])
        self.assertEqual(math.log2(5 - 1) + math.log2(5 - 3), 3)

    def test_source_restricts_plots_and_keeps_scene(self):
        text = SOURCE.read_text(encoding='utf-8')
        tree = ast.parse(text)
        self.assertTrue(any(isinstance(item, ast.ClassDef) and
                            item.name == 'ExponentialLogarithmicEquations'
                            for item in tree.body))
        self.assertIn('math.log2(9)', text)
        self.assertIn('x_range=[0.5, 10]', text)
        self.assertNotIn('if x > 0 else 0', text)
        self.assertNotIn('eq2[0][3]', text)
        self.assertIn('x=-1', text)


if __name__ == '__main__':
    unittest.main()
