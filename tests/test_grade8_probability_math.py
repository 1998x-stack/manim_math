"""频率模拟数学契约；无 Manim。无 NumPy 的全局静态 CI 可安全跳过数值用例。

专用 Grade 8 CI 显式安装并运行 NumPy 数值测试，不允许跳过。
"""
import ast
from pathlib import Path
import unittest

try:
    import numpy as np
except ImportError:
    np = None

SOURCE = (Path(__file__).resolve().parents[1] / "初中" / "八年级" / "第二学期"
          / "第二十三章-概率初步" / "004频率与概率的关系" / "probability_frequency.py")


class ProbabilityFrequencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if np is None:
            raise unittest.SkipTest("NumPy 未安装：本组数值检查由专用 Grade 8 CI 安装依赖执行")
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        function = next(node for node in cls.tree.body
                        if isinstance(node, ast.FunctionDef) and node.name == "simulate_frequencies")
        namespace = {"np": np}
        exec(compile(ast.Module(body=[function], type_ignores=[]), str(SOURCE), "exec"), namespace)
        cls.simulate = staticmethod(namespace["simulate_frequencies"])

    def test_frequency_equals_cumulative_successes_over_trials(self):
        outcomes, observed = self.simulate(1000, seed=42)
        self.assertEqual((len(outcomes), len(observed)), (1000, 1000))
        self.assertTrue(np.all(np.isin(outcomes, (0, 1))))
        np.testing.assert_allclose(observed, np.cumsum(outcomes) / np.arange(1, 1001))
        self.assertTrue(np.all((observed >= 0) & (observed <= 1)))

    def test_reproducible_without_global_rng_pollution(self):
        np.random.seed(123)
        previous = np.random.get_state()
        first = self.simulate(50, seed=7)
        second = self.simulate(50, seed=7)
        next_state = np.random.get_state()
        np.testing.assert_array_equal(first[0], second[0])
        np.testing.assert_array_equal(first[1], second[1])
        self.assertEqual(previous[0], next_state[0])
        np.testing.assert_array_equal(previous[1], next_state[1])
        self.assertEqual(previous[2:], next_state[2:])

    def test_extremes_and_invalid_parameters(self):
        self.assertTrue(np.all(self.simulate(20, probability=0)[1] == 0))
        self.assertTrue(np.all(self.simulate(20, probability=1)[1] == 1))
        for n in (0, -1, 3.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                self.simulate(n)
        for p in (-0.1, 1.01, float("nan")):
            with self.subTest(probability=p), self.assertRaises(ValueError):
                self.simulate(10, probability=p)

    def test_latex_is_ascii_and_original_scene_name_preserved(self):
        self.assertIn("ProbabilityFrequency", [node.name for node in self.tree.body
                                              if isinstance(node, ast.ClassDef)])
        self.assertNotIn("np.random.seed(", self.source)
        self.assertIn("default_rng(seed)", self.source)
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in ("MathTex", "Tex"):
                    for argument in node.args:
                        if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                            self.assertTrue(argument.value.isascii())


if __name__ == "__main__":
    unittest.main()
