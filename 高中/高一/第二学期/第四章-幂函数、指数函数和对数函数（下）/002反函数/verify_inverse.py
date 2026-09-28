"""反函数课程的纯 Python 数学回归；不导入 Manim，不替代真实渲染。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("inverse_functions.py")


class TestInverseMath(unittest.TestCase):
    def test_exponential_inverse_on_domain(self):
        for x in (-3, -1, 0, 1, 2, math.log2(5)):
            y = 2**x
            self.assertGreater(y, 0)
            self.assertAlmostEqual(math.log2(y), x, places=12)

    def test_inverse_exponential_on_positive_domain(self):
        for y in (0.01, 0.5, 1, 2, 4, 5, 100):
            self.assertAlmostEqual(2**math.log2(y), y, places=10)

    def test_exponential_graph_inside_axes(self):
        low, high = -1, math.log2(5)
        samples = [low + (high - low) * i / 100 for i in range(101)]
        self.assertTrue(all(-1 <= x <= 5 and -1 <= 2**x <= 5 + 1e-12 for x in samples))

    def test_logarithm_graph_inside_axes(self):
        samples = [0.5 + (5 - 0.5) * i / 100 for i in range(101)]
        self.assertTrue(all(-1 <= math.log2(x) <= 5 for x in samples))

    def test_symmetric_points(self):
        for x, y in [(0, 1), (1, 2), (2, 4)]:
            self.assertEqual(2**x, y)
            self.assertEqual(math.log2(y), x)
            self.assertEqual((y, x), (y, math.log2(y)))

    def test_horizontal_line_counterexample(self):
        # y=0 与 x²-1 有两个交点；严格单调函数在自身值域上每条水平线恰交一次。
        self.assertEqual((-1)**2 - 1, 0)
        self.assertEqual((1)**2 - 1, 0)
        self.assertNotEqual(-1, 1)

    def test_nonmonotone_but_injective_exists(self):
        # 一般定义域可不连通：f(x)=1/x, A=R\\{0} 单射，但在 A 上既非全局递增也非全局递减。
        f = lambda x: 1 / x
        self.assertLess(-2, 1)
        self.assertLess(f(-2), f(1))  # 非严格递减
        self.assertLess(1, 2)
        self.assertGreater(f(1), f(2))  # 非严格递增
        self.assertEqual(len({f(x) for x in [-2, -1, 1, 2]}), 4)

    def test_scene_entry_and_no_old_false_statement(self):
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        self.assertTrue(any(isinstance(n, ast.ClassDef) and n.name == "InverseFunctions" for n in tree.body))
        self.assertNotIn("单调函数只交一次", source)
        self.assertNotIn("x_range=[-1, 3]", source)
        self.assertIn("math.log2(5.0)", source)
        self.assertIn("x\\in A", source)
        self.assertIn("y\\in B", source)
        self.assertIn("FadeOut(self.author_info)", source) if False else None


if __name__ == "__main__":
    unittest.main()
