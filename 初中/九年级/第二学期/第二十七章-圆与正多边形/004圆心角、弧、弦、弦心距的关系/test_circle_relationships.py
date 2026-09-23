"""不安装 Manim 也可运行的数学与场景结构回归。"""
import ast
import math
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).with_name("circle_relationships.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"))
MATH_FN = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == "circle_metrics")
SCOPE = {"math": math}
exec(compile(ast.Module(body=[MATH_FN], type_ignores=[]), str(SOURCE), "exec"), SCOPE)
circle_metrics = SCOPE["circle_metrics"]


class CircleRelationshipTests(unittest.TestCase):
    def test_values_and_equal_groups(self):
        arc, chord, distance = circle_metrics(2.5, math.pi / 3)
        self.assertAlmostEqual(arc, 2.5 * math.pi / 3)
        self.assertAlmostEqual(chord, 2.5)
        self.assertAlmostEqual(distance, 2.5 * math.sqrt(3) / 2)
        self.assertEqual(circle_metrics(2.5, math.pi/3), circle_metrics(2.5, math.pi/3))

    def test_chord_and_distance_identity(self):
        for radius in (0.1, 1, 2.5, 100):
            for angle in (0.01, math.pi/3, math.pi - 0.01):
                _, chord, d = circle_metrics(radius, angle)
                self.assertAlmostEqual((chord/2)**2 + d*d, radius*radius)

    def test_invalid_domain(self):
        for r, a in ((0, .5), (-1, .5), (1, 0), (1, math.pi),
                     (1, -0.1), (1, 2*math.pi), (float('nan'), 1),
                     (1, float('inf'))):
            with self.subTest(radius=r, theta=a), self.assertRaises(ValueError):
                circle_metrics(r, a)

    def test_scene_sections_and_api_risks(self):
        cls = next(n for n in TREE.body if isinstance(n, ast.ClassDef) and n.name == "CircleRelationships")
        names = {n.name for n in cls.body if isinstance(n, ast.FunctionDef)}
        for i, n in enumerate(("opening", "introduction", "second_group", "angle_to_arc",
                               "arc_to_chord", "chord_to_distance", "summary", "outro"), 1):
            self.assertIn(f"scene_{i}_{n}", names)
        text = SOURCE.read_text(encoding="utf-8")
        self.assertNotIn("sagitta", text)
        self.assertNotIn("self.play(self.play", text)
        self.assertNotIn("shift(RIGHT * 0)", text)


if __name__ == "__main__":
    unittest.main()
