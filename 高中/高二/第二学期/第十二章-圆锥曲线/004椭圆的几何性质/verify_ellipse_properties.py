"""第十二章004：只抽取课程实际纯数学函数，不导入 Manim。"""
import ast
import math
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name("ellipse_properties.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
NAMES = {"ellipse_parameters", "ellipse_point", "ellipse_residual", "ellipse_foci",
         "focal_radii", "focal_radius_formula", "directrix_positions",
         "latus_rectum_endpoints", "axis_units"}
functions = [n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in NAMES]
assert {n.name for n in functions} == NAMES
scope = {"math": math, "A": 3., "B": 2.}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), "exec"), scope)
params = scope["ellipse_parameters"]
point = scope["ellipse_point"]
residual = scope["ellipse_residual"]
foci = scope["ellipse_foci"]
radii = scope["focal_radii"]
formula = scope["focal_radius_formula"]
directrix = scope["directrix_positions"]
latus = scope["latus_rectum_endpoints"]
units = scope["axis_units"]


class EllipsePropertiesTests(unittest.TestCase):
    def test_focal_geometry_and_eccentricity(self):
        c,e = params()
        self.assertAlmostEqual(c*c, 9-4)
        self.assertAlmostEqual(e, math.sqrt(5)/3)
        self.assertTrue(0<e<1)
        self.assertEqual(foci(), ((-c,0.), (c,0.)))

    def test_all_mirrored_example_points_belong_to_ellipse(self):
        x,y = point(math.pi/4)
        for reflected in ((x,y),(x,-y),(-x,y),(-x,-y)):
            self.assertAlmostEqual(residual(reflected), 0, places=10)
        self.assertGreater(abs(residual((2,1.3))), 0.01)

    def test_focal_radii_formula_for_many_curve_points(self):
        for index in range(144):
            p=point(index*math.tau/144)
            actual=radii(p)
            expected=formula(p)
            for x,y in zip(actual,expected):
                self.assertAlmostEqual(x,y,places=9)
            self.assertAlmostEqual(sum(actual),6,places=9)
        with self.assertRaises(ValueError):
            formula((0,0))

    def test_focal_radius_signs_at_right_vertex(self):
        c,e = params()
        self.assertAlmostEqual(radii((3,0))[0],3+c)
        self.assertAlmostEqual(radii((3,0))[1],3-c)
        self.assertAlmostEqual(formula((3,0))[0],3+3*e)
        self.assertAlmostEqual(formula((3,0))[1],3-3*e)

    def test_directrices_and_focus_directrix_ratio(self):
        left,right=directrix()
        c,e=params()
        self.assertAlmostEqual(right,9/c)
        self.assertAlmostEqual(left,-right)
        self.assertTrue(-5<left<-3<3<right<5)
        for index in range(72):
            p=point(index*math.tau/72)
            d_focus=radii(p)[1]
            d_directrix=right-p[0]
            self.assertAlmostEqual(d_focus/d_directrix,e,places=9)

    def test_latus_rectum_endpoints_and_data_length(self):
        p,q=latus()
        self.assertAlmostEqual(p[0],params()[0])
        self.assertAlmostEqual(q[0],params()[0])
        self.assertAlmostEqual(p[1],-4/3)
        self.assertAlmostEqual(q[1],4/3)
        self.assertAlmostEqual(math.dist(p,q),8/3)
        self.assertAlmostEqual(residual(p),0)
        self.assertAlmostEqual(residual(q),0)

    def test_eccentricity_change_at_fixed_major_axis(self):
        e_flat=params(3,.65)[1]
        e_orig=params(3,2)[1]
        e_round=params(3,2.99)[1]
        self.assertTrue(0<e_round<e_orig<e_flat<1)

    def test_equal_screen_coordinate_units_and_directrix_visibility(self):
        ux,uy=units()
        self.assertAlmostEqual(ux,.7)
        self.assertAlmostEqual(uy,.7)
        self.assertAlmostEqual(ux,uy)
        self.assertNotAlmostEqual(*units(x_length=5.0))
        with self.assertRaises(ValueError):
            units(y_bounds=(4,4))

    def test_invalid_inputs(self):
        for a,b in ((3,3),(2,3),(3,0),(math.inf,2)):
            with self.assertRaises(ValueError):
                params(a,b)
        with self.assertRaises(ValueError):
            point(math.inf)
        with self.assertRaises(ValueError):
            residual((math.nan,1))

    def test_scene_preserves_nine_stages_and_no_literal_chinese_tex(self):
        classes=[n for n in TREE.body if isinstance(n, ast.ClassDef) and n.name=="EllipseProperties"]
        self.assertEqual(len(classes),1)
        names={n.name for n in classes[0].body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({"show_opening","show_range_symmetry","show_eccentricity_concept",
                         "show_eccentricity_effect","show_directrix","show_focal_radius",
                         "show_latus_rectum","show_summary","show_outro"}<=names)
        for node in ast.walk(TREE):
            if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Name):
                continue
            if node.func.id not in {"MathTex","Tex"}:
                continue
            for arg in node.args:
                if isinstance(arg,ast.Constant) and isinstance(arg.value,str):
                    self.assertFalse(any('\u3400'<=char<='\u9fff' for char in arg.value),
                                     f"Chinese literal in {node.func.id}, line {node.lineno}")


if __name__=='__main__':
    unittest.main()
