"""九年级静态审计、三角比及平行线定理的无 Manim 回归检查。"""

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
PARALLEL = (ROOT / GRADE_REL / "第一学期" / "第二十四章-相似三角形"
            / "002平行线分线段成比例定理" / "parallel_lines_theorem.py")


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


class ParallelLinesGeometryTests(unittest.TestCase):
    """只运行课件真实数学函数，避免用另一份算法自证正确。"""

    @classmethod
    def setUpClass(cls):
        cls.source = PARALLEL.read_text(encoding="utf-8")
        cls.tree = ast.parse(cls.source)
        names = {"proportional", "transversal_intersections", "triangle_sections"}
        functions = [node for node in cls.tree.body
                     if isinstance(node, ast.FunctionDef) and node.name in names]
        assert {node.name for node in functions} == names
        namespace = {"math": math}
        exec(compile(ast.Module(body=functions, type_ignores=[]),
                     str(PARALLEL), "exec"), namespace)
        cls.proportional = staticmethod(namespace["proportional"])
        cls.transversals = staticmethod(namespace["transversal_intersections"])
        cls.sections = staticmethod(namespace["triangle_sections"])

    def test_three_parallel_lines_use_exact_intersections_and_corresponding_ratios(self):
        p = self.transversals()
        self.assertEqual(set(p), set("ABCDEF"))
        for start, end, level in (("A", "D", 2.0), ("B", "E", 0.8),
                                  ("C", "F", -2.0)):
            self.assertAlmostEqual(p[start][1], level)
            self.assertAlmostEqual(p[end][1], level)
            self.assertLess(p[start][0], p[end][0])
        ab = math.dist(p["A"], p["B"])
        bc = math.dist(p["B"], p["C"])
        de = math.dist(p["D"], p["E"])
        ef = math.dist(p["E"], p["F"])
        self.assertTrue(self.proportional(ab, bc, de, ef))
        self.assertAlmostEqual(ab / bc, 3 / 7)
        self.assertAlmostEqual(de / ef, 3 / 7)

    def test_invalid_inputs_and_nonproportional_values_fail(self):
        self.assertFalse(self.proportional(2, 3, 4, 7))
        self.assertFalse(self.proportional(1e-90, 1e-90, 2e-90, 3e-90))
        for lengths in ((0, 2, 3, 4), (1, 0, 2, 3),
                        (1, math.inf, 2, 3), (-1, 2, 3, 4)):
            with self.subTest(lengths=lengths), self.assertRaises(ValueError):
                self.proportional(*lengths)
        for levels in ((2, 2, -2), (0, 1, -2), (1, 0),
                       (2, math.nan, -2), (2, 2 - 1e-10, 0)):
            with self.subTest(levels=levels), self.assertRaises(ValueError):
                self.transversals(levels)

    def test_triangle_corollary_converse_and_degenerate_cases(self):
        a, b, c = (0.0, 2.6), (-2.5, -1.3), (2.5, -1.3)
        for t in (0.1, 0.4, 0.85):
            d, e = self.sections(a, b, c, t)
            self.assertTrue(self.proportional(math.dist(a, d), math.dist(d, b),
                                              math.dist(a, e), math.dist(e, c)))
            de = (e[0] - d[0], e[1] - d[1])
            bc = (c[0] - b[0], c[1] - b[1])
            self.assertAlmostEqual(de[0] * bc[1] - de[1] * bc[0], 0.0)
        for t in (-0.1, 0, 1, 1.1):
            with self.subTest(t=t), self.assertRaises(ValueError):
                self.sections(a, b, c, t)
        with self.assertRaises(ValueError):
            self.sections((0, 0), (1, 1), (2, 2), 0.4)

    def test_application_labels_match_drawing_scale(self):
        a, b, c = (0.0, 2.7), (-1.5, 0.7), (3.0, -1.3)
        d, e = self.sections(a, b, c, 2 / 5)
        for actual, displayed in ((math.dist(a, d), 2),
                                  (math.dist(d, b), 3),
                                  (math.dist(a, e), 4),
                                  (math.dist(e, c), 6)):
            self.assertAlmostEqual(actual * 2, displayed)
        self.assertEqual(2 * 6, 3 * 4)

    def test_scene_preserves_displayed_mobject_identity_and_safe_parallel_drawing(self):
        cls = next(node for node in self.tree.body
                   if isinstance(node, ast.ClassDef) and node.name == "ParallelLinesTheorem")
        methods = {node.name: ast.get_source_segment(self.source, node)
                   for node in cls.body if isinstance(node, ast.FunctionDef)}
        self.assertIn("Line(screen_point((-3.65, y)), screen_point((3.35, y))",
                      methods["show_three_parallel_lines"])
        self.assertIn("self.play(Indicate(line_de)", methods["show_converse_theorem"])
        self.assertIn("ReplacementTransform(relation, substituted)",
                      methods["show_application"])
        self.assertIn("relation = substituted", methods["show_application"])
        self.assertIn("Transform(known[3], answer_label)", methods["show_application"])
        self.assertIn("if mob is not self.author_info", methods["clear_section"])


if __name__ == "__main__":
    unittest.main()
