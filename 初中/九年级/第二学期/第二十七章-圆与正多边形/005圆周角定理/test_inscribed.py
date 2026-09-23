"""抽取纯数学函数，不依赖 Manim 执行边界和反例测试。"""
import ast
import math
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).with_name("inscribed_angle_theorem.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"))
SCOPE = {"math": math}
FUNCTIONS = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in
             ("point", "angle_at", "check_inscribed_example")]
exec(compile(ast.Module(body=FUNCTIONS, type_ignores=[]), str(SOURCE), "exec"), SCOPE)


class InscribedTests(unittest.TestCase):
    def test_same_arc(self):
        c, p, q = SCOPE["check_inscribed_example"]()
        self.assertAlmostEqual(math.degrees(c), 120)
        self.assertAlmostEqual(math.degrees(p), 60)
        self.assertAlmostEqual(p, q)

    def test_opposite_arc_counterexample(self):
        point, angle_at = SCOPE["point"], SCOPE["angle_at"]
        a, b = point(30), point(150)
        self.assertAlmostEqual(math.degrees(angle_at(a, point(90), b)), 120)
        self.assertAlmostEqual(math.degrees(angle_at(a, point(240), b)), 60)

    def test_diameter(self):
        point, angle_at = SCOPE["point"], SCOPE["angle_at"]
        for vertex in (45, 90, 135, 260):
            self.assertAlmostEqual(math.degrees(angle_at(point(0), point(vertex), point(180))), 90)

    def test_invalid_inputs(self):
        for degrees, radius in ((0, 0), (45, -2), (float("nan"), 1)):
            with self.assertRaises(ValueError):
                SCOPE["point"](degrees, radius)
        with self.assertRaises(ValueError):
            SCOPE["angle_at"]((0, 0), (0, 0), (1, 1))

    def test_scene_structure(self):
        cls = next(n for n in TREE.body if isinstance(n, ast.ClassDef) and n.name == "InscribedAngleTheorem")
        methods = {n.name for n in cls.body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"show_opening", "show_inscribed_angle_definition", "show_central_angle",
                         "show_main_theorem", "show_corollary_1", "show_corollary_2",
                         "show_corollary_3", "show_summary"} <= methods)
        self.assertNotIn("shift(RIGHT * 0)", SOURCE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
