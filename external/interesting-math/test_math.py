"""不导入 Manim 的数学回归：提取 Scene 文件中的纯数学函数执行。

Run: python -m unittest discover -s external/interesting-math -p 'test_*.py' -v
Note: 此检查不能代替 Manim 渲染、排版或音视频验收。
"""
import ast
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent


def functions(slug, *names):
    """执行与 Scene 同源的纯数学函数，同时排除 Manim 导入和动画代码。"""
    path = ROOT / slug / "scene.py"
    module = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    selection = [node for node in module.body
                 if isinstance(node, ast.ImportFrom) and node.module == "math"]
    selection += [node for node in module.body
                  if isinstance(node, ast.FunctionDef) and node.name in names]
    found = {node.name for node in selection if isinstance(node, ast.FunctionDef)}
    if found != set(names):
        raise AssertionError(f"missing math functions in {slug}: {set(names) - found}")
    namespace = {"__name__": "math_test"}
    compiled = compile(ast.Module(body=selection, type_ignores=[]), str(path), "exec")
    exec(compiled, namespace)
    return tuple(namespace[name] for name in names)


class VisualMathTests(unittest.TestCase):
    def test_odd_squares(self):
        layer, odd_sum = functions("odd-squares", "odd_layer", "odd_sum")
        for n in range(1, 16):
            self.assertEqual(odd_sum(n), n * n)
            self.assertEqual(len(layer(n)), 2 * n - 1)
            self.assertEqual(set().union(*(set(layer(k)) for k in range(1, n + 1))),
                             {(x, y) for x in range(n) for y in range(n)})
        self.assertEqual(odd_sum(0), 0)
        with self.assertRaises(ValueError):
            layer(0)

    def test_monty_hall(self):
        host, switched, wins = functions("monty-hall", "host_opens", "switched_door", "switch_wins")
        for chosen in range(3):
            self.assertEqual(sum(wins(prize, chosen) for prize in range(3)), 2)
            for prize in range(3):
                self.assertNotIn(host(prize, chosen), (prize, chosen))
                self.assertEqual(len({host(prize, chosen), chosen, switched(prize, chosen)}), 3)
                self.assertEqual(wins(prize, chosen), prize != chosen)
        with self.assertRaises(ValueError):
            host(3)

    def test_pascal_parity(self):
        row, parity = functions("pascal-fractal", "pascal_row", "parity_row")
        for n in range(32):
            values = row(n)
            self.assertEqual(sum(values), 2 ** n)
            self.assertEqual(values, list(reversed(values)))
            self.assertEqual(parity(n), [value % 2 for value in values])
            if n >= 1:
                self.assertEqual(values[0], 1)
                self.assertEqual(values[-1], 1)
                for k in range(1, n):
                    self.assertEqual(values[k], row(n - 1)[k - 1] + row(n - 1)[k])
        for m in range(1, 5):
            self.assertTrue(all(parity(2 ** m - 1)))
        with self.assertRaises(ValueError):
            row(-1)

    def test_complex_rotation(self):
        (rotate,) = functions("complex-rotation", "rotate_complex")
        for z in (0j, 1 + 0j, 1.2 + 0.5j, -2 + 1j):
            for theta in (0, math.pi / 2, math.pi, 2 * math.pi, -0.75):
                self.assertAlmostEqual(abs(rotate(z, theta)), abs(z), places=12)
                self.assertAlmostEqual(abs(rotate(z, theta + 2 * math.pi) - rotate(z, theta)),
                                       0, places=12)
                self.assertAlmostEqual(abs(rotate(rotate(z, theta), 0.43) - rotate(z, theta + 0.43)),
                                       0, places=12)

    def test_koch_area_and_perimeter(self):
        triangle, step, perimeter_ratio, area_ratio = functions(
            "koch-snowflake", "initial_triangle", "koch_step", "perimeter_ratio", "area_ratio")

        def perimeter(vertices):
            return sum(abs(vertices[(k + 1) % len(vertices)] - p)
                       for k, p in enumerate(vertices))

        def area(vertices):
            return abs(sum(p.real * vertices[(k + 1) % len(vertices)].imag
                           - vertices[(k + 1) % len(vertices)].real * p.imag
                           for k, p in enumerate(vertices)) / 2)

        points = triangle()
        p0, a0 = perimeter(points), area(points)
        for n in range(5):
            self.assertEqual(len(points), 3 * 4 ** n)
            self.assertAlmostEqual(perimeter(points) / p0, perimeter_ratio(n), places=9)
            self.assertAlmostEqual(area(points) / a0, area_ratio(n), places=9)
            self.assertLess(area_ratio(n), 8 / 5)
            points = step(points)
        with self.assertRaises(ValueError):
            area_ratio(-1)
        with self.assertRaises(ValueError):
            step([0j])


if __name__ == "__main__":
    unittest.main()
