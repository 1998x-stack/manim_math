"""本课目录执行：python -m unittest -v test_regular_polygon_math"""
import ast
from math import cos, isclose, pi, sqrt
from pathlib import Path
import unittest
from regular_polygon_math import polygon_metrics, polygon_vertices, verify_polygon


class RegularPolygonMathTests(unittest.TestCase):
    def test_regular_triangle_square_hexagon_and_dodecagon(self):
        for n in (3, 4, 6, 12):
            with self.subTest(n=n):
                verify_polygon(n, 2.0)
                metrics = polygon_metrics(n, 2.0)
                self.assertAlmostEqual(metrics['central_angle'], 2*pi/n)
                self.assertEqual(len(polygon_vertices(n, 2.0)), n)
                self.assertAlmostEqual(metrics['perimeter'], n*metrics['side'])
                self.assertAlmostEqual(metrics['area'], metrics['perimeter']*metrics['apothem']/2)

    def test_hexagon_side_equals_radius(self):
        result = polygon_metrics(6, 2.0)
        self.assertAlmostEqual(result['side'], 2.0)
        self.assertAlmostEqual(result['central_angle'], pi/3)
        self.assertAlmostEqual(result['apothem'], sqrt(3))

    def test_square_formula(self):
        result = polygon_metrics(4, 1.0)
        self.assertAlmostEqual(result['side'], sqrt(2))
        self.assertAlmostEqual(result['area'], 2.0)

    def test_invalid_inputs(self):
        for n, R in ((2, 1), (0, 1), (6, 0), (6, -2), (6, float('nan')), (6, float('inf')), (True, 2)):
            with self.subTest(n=n, R=R), self.assertRaises(ValueError):
                polygon_metrics(n, R)

    def test_vertex_translation(self):
        shifted = polygon_vertices(6, 2.0, (1.25, -0.5))
        origin = polygon_vertices(6, 2.0)
        for a, b in zip(shifted, origin):
            self.assertTrue(isclose(a[0]-b[0], 1.25, abs_tol=1e-12))
            self.assertTrue(isclose(a[1]-b[1], -0.5, abs_tol=1e-12))

    def test_scene_structure_and_mathtex_safety(self):
        scene = Path(__file__).with_name('regular_polygon_circle.py').read_text(encoding='utf-8')
        tree = ast.parse(scene)
        class_nodes = [n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'RegularPolygonAndCircle']
        self.assertEqual(len(class_nodes), 1)
        methods = {n.name for n in class_nodes[0].body if isinstance(n, ast.FunctionDef)}
        self.assertTrue({'scene_1_opening','scene_2_core_elements','scene_3_central_angle',
                         'scene_4_hexagon_special','scene_5_area_formula','scene_6_summary'} <= methods)
        self.assertIn('about_point=self.circle.get_center()', scene)
        self.assertNotIn('about_point=self.O', scene)
        self.assertNotIn('为等边三角形', scene)


if __name__ == '__main__':
    unittest.main()
