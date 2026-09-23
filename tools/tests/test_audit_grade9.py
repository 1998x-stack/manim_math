"""九年级静态审计与三角比的无 Manim 回归检查。"""

import ast
import json
import math
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_grade9 import CHAPTERS, GRADE_REL, _quadratic_plot_risk, audit

ROOT = Path(__file__).resolve().parents[2]
TRIG = (ROOT / GRADE_REL / "第一学期" / "第二十五章-锐角的三角比"
        / "001锐角三角比的定义" / "trigonometric_ratios.py")


class Grade9AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for semester, chapters in CHAPTERS.items():
            for chapter in chapters:
                (self.root / GRADE_REL / semester / chapter).mkdir(parents=True)
        self.lesson = (self.root / GRADE_REL / "第一学期"
                       / "第二十五章-锐角的三角比" / "001例题")
        self.lesson.mkdir()
        (self.lesson / "description.json").write_text(
            json.dumps({"年级": "九年级", "学期": "第一学期"}, ensure_ascii=False),
            encoding="utf-8",
        )

    def test_valid_scene(self):
        (self.lesson / "lesson.py").write_text(
            "class Lesson(Scene):\n    def construct(self):\n        pass\n", encoding="utf-8",
        )
        result = audit(self.root)
        self.assertEqual(result["topics"], 1)
        self.assertEqual(result["python_files"], 1)
        self.assertEqual(result["issues"], [])

    def test_syntax_and_json_errors(self):
        (self.lesson / "lesson.py").write_text("def invalid(:\n", encoding="utf-8")
        (self.lesson / "description.json").write_text("{", encoding="utf-8")
        result = audit(self.root)
        self.assertEqual(sum(issue["severity"] == "error" for issue in result["issues"]), 2)

    def test_latex_and_zero_width_are_detected(self):
        (self.lesson / "lesson.py").write_text(
            "class Lesson(Scene):\n"
            "    def construct(self):\n"
            "        MathTex('角A=30°')\n"
            "        axes.plot(lambda x: x*x, x_range=[1, 1])\n", encoding="utf-8",
        )
        messages = [issue["message"] for issue in audit(self.root)["issues"]]
        self.assertTrue(any("Unicode" in message for message in messages))
        self.assertTrue(any("宽度为零" in message for message in messages))

    def test_quadratic_range_is_checked_without_eval(self):
        tree = ast.parse(
            "def setup_geometry(self):\n"
            "    self.AX_Y = [-2.5, 5, 1]\n"
            "    self.CURVE_X = [-2.5, 2.5]\n"
            "    self.f_std = lambda x: x**2\n",
        )
        self.assertEqual(_quadratic_plot_risk(tree), (True, 2.5, 5))


class TrigonometricGeometryTests(unittest.TestCase):
    def test_angle_a_is_35_degrees_and_c_is_right_angle(self):
        angle = math.radians(35)
        adjacent = 3.0
        opposite = adjacent * math.tan(angle)
        hypotenuse = math.hypot(adjacent, opposite)
        c, b, a = (0.0, 0.0), (opposite, 0.0), (0.0, adjacent)
        cb = (b[0] - c[0], b[1] - c[1])
        ca = (a[0] - c[0], a[1] - c[1])
        self.assertAlmostEqual(cb[0] * ca[0] + cb[1] * ca[1], 0.0)
        self.assertAlmostEqual(math.hypot(*cb) / hypotenuse, math.sin(angle))
        self.assertAlmostEqual(math.hypot(*ca) / hypotenuse, math.cos(angle))
        self.assertAlmostEqual(math.hypot(*cb) / math.hypot(*ca), math.tan(angle))

    def test_scene_uses_the_same_side_to_vertex_mapping(self):
        source = TRIG.read_text(encoding="utf-8")
        tree = ast.parse(source)
        cls = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                   and node.name == "TrigonometricRatios")
        method = next(node for node in cls.body if isinstance(node, ast.FunctionDef)
                      and node.name == "make_triangle")
        source_block = ast.get_source_segment(source, method)
        self.assertIn("b = c + RIGHT * self.opposite * scale", source_block)
        self.assertIn("a = c + UP * self.adjacent * scale", source_block)
        self.assertIn("opposite_line = Line(c, b", source_block)
        self.assertIn("adjacent_line = Line(c, a", source_block)
        self.assertIn("hypotenuse_line = Line(a, b", source_block)
        self.assertIn("Line(c, b), Line(c, a)", source_block)


if __name__ == "__main__":
    unittest.main()
