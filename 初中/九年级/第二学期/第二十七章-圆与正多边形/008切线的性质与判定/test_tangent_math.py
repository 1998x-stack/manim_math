"""从本课目录运行：python -m unittest -v test_tangent_math"""
import ast
from math import hypot
from pathlib import Path
import unittest
from tangent_math import tangent_points, verify_tangent_geometry


class TangentGeometryTests(unittest.TestCase):
    def test_example_equal_lengths_and_perpendicular(self):
        center, external, radius = (0.0, 0.8), (3.0, 2.5), 1.8
        length = verify_tangent_geometry(center, radius, external)
        a, b = tangent_points(center, radius, external)
        self.assertGreater(hypot(*[external[i] - center[i] for i in (0, 1)]), radius)
        self.assertAlmostEqual(hypot(a[0]-external[0], a[1]-external[1]), length)
        self.assertAlmostEqual(hypot(b[0]-external[0], b[1]-external[1]), length)
        self.assertNotEqual(a, b)

    def test_rotation_and_translation(self):
        for center, external, radius in (((0, 0), (5, 0), 2), ((2, -3), (2, 7), 1), ((-1, 2), (2, 3), 1.5)):
            with self.subTest(center=center, external=external):
                self.assertGreater(verify_tangent_geometry(center, radius, external), 0)

    def test_exterior_point_required(self):
        for point in ((0, 0), (2, 0), (1, 0)):
            with self.subTest(point=point), self.assertRaises(ValueError):
                tangent_points((0, 0), 2, point)

    def test_invalid_radius_and_nonfinite(self):
        for center, radius, point in (((0, 0), 0, (3, 0)), ((0, 0), -1, (3, 0)), ((0, 0), 1, (float('inf'), 0)), ((float('nan'), 0), 1, (3, 0))):
            with self.subTest(center=center, radius=radius, point=point), self.assertRaises(ValueError):
                tangent_points(center, radius, point)

    def test_two_scene_entrypoints(self):
        root = Path(__file__).parent
        for filename, klass, method in (("tangent_theorems.py", "TangentTheorems", "scene_7_outro"),
                                        ("tangent_properties.py", "TangentProperties", "scene_8_summary_outro")):
            text = (root / filename).read_text(encoding="utf-8")
            tree = ast.parse(text)
            classes = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == klass]
            self.assertEqual(len(classes), 1)
            self.assertTrue(any(isinstance(n, ast.FunctionDef) and n.name == method for n in classes[0].body))
            self.assertNotIn('RIGHT * 0', text)
            self.assertNotIn('LEFT * 10', text)


if __name__ == '__main__':
    unittest.main()
