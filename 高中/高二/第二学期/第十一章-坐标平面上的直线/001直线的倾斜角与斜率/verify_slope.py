"""纯数学回归：无需安装 Manim 即可验证本课的数学模型。

运行：python verify_slope.py
"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("slope_inclination.py")
HELPERS = {"slope_between", "inclination_between", "clipped_origin_line"}


def load_math_helpers():
    """仅装载无图形依赖的数学函数，不执行 Manim 导入或 Scene。"""
    root = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    functions = [node for node in root.body if isinstance(node, ast.FunctionDef) and node.name in HELPERS]
    if {node.name for node in functions} != HELPERS:
        raise AssertionError("缺少斜率、倾斜角或裁剪数学函数")
    namespace = {"math": math}
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), namespace)
    return namespace


M = load_math_helpers()


class SlopeGeometryTests(unittest.TestCase):
    def test_two_point_examples(self):
        slope = M["slope_between"]
        self.assertEqual(slope((1, 1), (3, 3)), 1)
        self.assertEqual(slope((3, 3), (1, 1)), 1)
        self.assertEqual(slope((0, 0), (1, -1)), -1)
        self.assertEqual(slope((0, 2), (4, 2)), 0)
        self.assertIsNone(slope((2, -1), (2, 4)))
        with self.assertRaises(ValueError):
            slope((1, 1), (1, 1))

    def test_inclination_domain(self):
        angle = M["inclination_between"]
        for a, b, expected in (
            ((1, 1), (3, 3), math.pi / 4),
            ((3, 3), (1, 1), math.pi / 4),
            ((0, 0), (1, -1), 3 * math.pi / 4),
            ((0, 0), (-1, 1), 3 * math.pi / 4),
            ((0, 0), (0, 2), math.pi / 2),
            ((0, 0), (0, -2), math.pi / 2),
            ((0, 0), (-2, 0), 0),
        ):
            result = angle(a, b)
            self.assertGreaterEqual(result, 0)
            self.assertLess(result, math.pi)
            self.assertAlmostEqual(result, expected, places=10)
        with self.assertRaises(ValueError):
            angle((0, 0), (0, 0))

    def test_all_lines_stay_within_plot_window(self):
        clip = M["clipped_origin_line"]
        for alpha in (0, math.pi / 6, math.pi / 4, math.pi / 2,
                      3 * math.pi / 4, math.pi - 1e-8):
            start, end = clip(alpha, (-3, 3), (-2, 3))
            self.assertGreater(math.dist(start, end), 1)
            for x, y in (start, end):
                self.assertGreaterEqual(x, -3 - 1e-9)
                self.assertLessEqual(x, 3 + 1e-9)
                self.assertGreaterEqual(y, -2 - 1e-9)
                self.assertLessEqual(y, 3 + 1e-9)
                self.assertAlmostEqual(
                    x * math.sin(alpha) - y * math.cos(alpha), 0, places=8,
                )
        for alpha in (0, math.pi / 4, math.pi / 2, 3 * math.pi / 4):
            for x, y in clip(alpha, (-2.5, 2.5), (-2, 2)):
                self.assertLessEqual(abs(x), 2.5 + 1e-9)
                self.assertLessEqual(abs(y), 2 + 1e-9)

    def test_invalid_window_and_angle(self):
        clip = M["clipped_origin_line"]
        for angle in (-0.01, math.pi, math.pi + 0.1):
            with self.assertRaises(ValueError):
                clip(angle)
        with self.assertRaises(ValueError):
            clip(0, (1, 1), (-2, 3))
        with self.assertRaises(ValueError):
            clip(math.pi / 2, (1, 3), (-2, 3))


if __name__ == "__main__":
    unittest.main()
