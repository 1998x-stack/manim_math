"""平方差课程独立数学/布局模型回归；不导入 Manim。"""

import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("difference_of_squares.py")


def load_geometry_model():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    func = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                and n.name == "area_geometry")
    namespace = {}
    exec(compile(ast.Module(body=[func], type_ignores=[]), str(SOURCE), "exec"), namespace)
    return namespace["area_geometry"]


class DifferenceOfSquaresLessonTests(unittest.TestCase):
    def test_area_rearrangement_non_overlap_and_no_gaps(self):
        area_geometry = load_geometry_model()
        for a, b in ((3.6, 1.2), (5, 2), (6, 1), (2.5, 0.5), (1.1, 1)):
            spec = area_geometry(a, b)
            h = a - b
            self.assertEqual(spec["pieces"], ((a, h), (h, b)))
            self.assertEqual(spec["target"], (a + b, h))
            self.assertTrue(math.isclose(spec["remaining_area"], (a+b)*h, rel_tol=1e-12))
            self.assertTrue(math.isclose(a*a, spec["remaining_area"] + b*b, rel_tol=1e-12))
            # 底块宽 a，中心 x=-b/2；旋转块宽 b，中心 x=a/2。
            bottom_right = -b / 2 + a / 2
            rotated_left = a / 2 - b / 2
            self.assertTrue(math.isclose(bottom_right, rotated_left, abs_tol=1e-12))
            self.assertTrue(math.isclose(-b/2-a/2, -(a+b)/2, abs_tol=1e-12))
            self.assertTrue(math.isclose(a/2+b/2, (a+b)/2, abs_tol=1e-12))
            self.assertTrue(math.isclose(spec["pieces"][0][1],
                                         spec["pieces"][1][0], abs_tol=1e-12))

    def test_invalid_geometry_is_rejected(self):
        area_geometry = load_geometry_model()
        for a, b in ((1, 1), (1, 2), (0, 0), (-2, -3),
                     (math.inf, 1), (2, math.nan), (1, 0), ("a", 2)):
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                area_geometry(a, b)

    def test_identity_for_all_signs_not_inferred_from_area_only(self):
        for a in (-5, -2, 0, 2, 5):
            for b in (-4, -1, 0, 1, 4):
                self.assertEqual((a+b)*(a-b), a*a-b*b)
                self.assertEqual(a*a-b*b, a*a-a*b+a*b-b*b)
        self.assertEqual((7+3)*(7-3), 7*7-3*3)
        self.assertEqual((5+2)*(5-2), 21)

    def test_scene_source_contract(self):
        source = SOURCE.read_text(encoding="utf-8")
        tree = ast.parse(source)
        compile(tree, str(SOURCE), "exec")
        scene = next(n for n in tree.body if isinstance(n, ast.ClassDef)
                     and n.name == "DifferenceOfSquares")
        methods = {n.name for n in scene.body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"construct", "scene_3_build_square_a",
                         "scene_4_subtract_square_b", "scene_5_rearrange_rectangles",
                         "scene_6_concrete_example", "scene_7_outro"} <= methods)
        self.assertIn("self.geometry = area_geometry(3.6, 1.2)", source)
        self.assertIn("width=self.a, height=self.h", source)
        self.assertIn("width=self.h, height=self.b", source)
        self.assertIn("rotate(-PI / 2).move_to([self.a / 2, -0.8, 0])", source)
        self.assertIn("move_to([-self.b / 2, -0.8, 0])", source)
        self.assertNotIn("self.remove(full_formula)", source)
        self.assertIn("config.frame_width = 9", source)
        self.assertIn("config.frame_height = 16", source)
        for call in ast.walk(scene):
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name):
                if call.func.id in {"MathTex", "Tex"}:
                    for value in call.args:
                        if isinstance(value, ast.Constant) and isinstance(value.value, str):
                            self.assertFalse(any("\u4e00" <= ch <= "\u9fff" for ch in value.value))
                if call.func.id == "SurroundingRectangle":
                    self.assertNotIn("corner_radius", {kw.arg for kw in call.keywords})


if __name__ == "__main__":
    unittest.main()
