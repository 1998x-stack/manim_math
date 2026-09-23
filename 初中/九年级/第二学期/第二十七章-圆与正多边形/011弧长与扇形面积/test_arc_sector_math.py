"""本课目录执行：python -m unittest -v test_arc_sector_math"""
import ast
from math import pi
from pathlib import Path
import unittest
from arc_sector_math import sector_metrics, verify_example


class ArcSectorTests(unittest.TestCase):
    def test_sixty_degree_example(self):
        metrics = sector_metrics(2.0, 60)
        self.assertAlmostEqual(metrics['theta_rad'], pi/3)
        self.assertAlmostEqual(metrics['arc_length'], 2*pi/3)
        self.assertAlmostEqual(metrics['area'], 2*pi/3)
        self.assertAlmostEqual(metrics['perimeter'], 4 + 2*pi/3)
        verify_example(2, 60, expected_length=2*pi/3, expected_area=2*pi/3)

    def test_one_hundred_twenty_degree_example(self):
        verify_example(3, 120, expected_length=2*pi, expected_area=3*pi)

    def test_angle_units_and_full_circle(self):
        for angle in (0, 30, 90, 180, 270, 360):
            with self.subTest(angle=angle):
                data = sector_metrics(3, angle)
                self.assertAlmostEqual(data['arc_length'], angle*pi*3/180)
                self.assertAlmostEqual(data['area'], angle*pi*9/360)
        self.assertAlmostEqual(sector_metrics(3, 360)['area'], 9*pi)

    def test_invalid_geometry_and_incorrect_examples(self):
        for R, degree in ((0, 60), (-1, 60), (2, -1), (2, 361), (2, float('inf')),
                          (float('nan'), 60)):
            with self.subTest(R=R, degree=degree), self.assertRaises(ValueError):
                sector_metrics(R, degree)
        with self.assertRaises(ValueError):
            verify_example(2, 60, expected_length=4, expected_area=2*pi/3)

    def test_scene_entrypoint_and_arc_annotation(self):
        source = Path(__file__).with_name('arc_length_sector_area.py').read_text(encoding='utf-8')
        classes = [node for node in ast.parse(source).body
                   if isinstance(node, ast.ClassDef) and node.name == 'ArcLengthAndSectorArea']
        self.assertEqual(len(classes), 1)
        methods = {node.name for node in classes[0].body if isinstance(node, ast.FunctionDef)}
        self.assertTrue({f'scene_{i}_{name}' for i, name in (
            (1,'opening'),(2,'central_angle'),(3,'arc_length_formula'),
            (4,'arc_length_example'),(5,'sector_definition'),(6,'sector_area_formula_1'),
            (7,'sector_area_formula_2'),(8,'comprehensive_example'),(9,'outro'))} <= methods)
        self.assertIn('self.arc_label(', source)
        self.assertNotIn('Brace(Line(', source)
        self.assertNotIn('Transform(VGroup(', source)
        self.assertNotIn('corner_radius=', source)


if __name__ == '__main__':
    unittest.main()
