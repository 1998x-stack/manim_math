"""垂径定理数据与弧方向的独立测试（无需 Manim）。"""
import ast
import math
import unittest
from pathlib import Path

SOURCE = Path(__file__).with_name('perpendicular_chord_theorem.py')
tree = ast.parse(SOURCE.read_text(encoding='utf-8'))
fn = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
          and node.name == 'chord_geometry')
namespace = {'asin': math.asin, 'degrees': math.degrees,
             'hypot': math.hypot, 'sqrt': math.sqrt}
exec(compile(ast.Module(body=[fn], type_ignores=[]), str(SOURCE), 'exec'), namespace)
spec = namespace['chord_geometry']


class PerpendicularChordTests(unittest.TestCase):
    def test_bisected_chord_and_both_arcs(self):
        for radius in (0.5, 2.125, 20):
            for factor in (0.1, 0.5, 0.9):
                model = spec(radius, center_y=-1.4, chord_height=radius * factor)
                points, angles = model['points'], model['sweeps']
                a, b, m, o = (points[name] for name in ('A', 'B', 'M', 'O'))
                self.assertAlmostEqual(math.dist(a, m), math.dist(m, b))
                self.assertAlmostEqual((m[0] - o[0]) * (b[0] - a[0])
                                       + (m[1] - o[1]) * (b[1] - a[1]), 0)
                self.assertAlmostEqual(angles['major_AE'], angles['major_EB'])
                self.assertAlmostEqual(angles['minor_AC'], angles['minor_CB'])
                self.assertLess(angles['minor_AC'], 0)
                self.assertGreater(angles['major_AE'], 0)
                self.assertLess(-2 * angles['minor_AC'], 180)
                self.assertGreater(2 * angles['major_AE'], 180)
                self.assertAlmostEqual(2 * angles['major_AE']
                                       - 2 * angles['minor_AC'], 360)

    def test_invalid_or_degenerate_inputs(self):
        for radius, height in ((0, None), (-1, None), (1, 0), (1, 1),
                               (1, -0.1), (1, 1.1)):
            with self.assertRaises(ValueError):
                spec(radius, chord_height=height)

    def test_default_actual_geometry_and_scene(self):
        model = spec(2.125)
        self.assertAlmostEqual(model['alpha'], 30)
        self.assertAlmostEqual(model['sweeps']['minor_AC'], -60)
        self.assertAlmostEqual(model['sweeps']['major_AE'], 120)
        self.assertAlmostEqual(model['points']['C'][0], model['points']['M'][0])
        self.assertAlmostEqual(model['points']['E'][0], model['points']['M'][0])
        scenes = [n for n in tree.body if isinstance(n, ast.ClassDef)]
        scene = next(n for n in scenes if n.name == 'PerpendicularChordTheorem')
        self.assertEqual(len([n for n in scene.body if isinstance(n, ast.FunctionDef)
                              and n.name.startswith('scene_')]), 7)


if __name__ == '__main__':
    unittest.main()
