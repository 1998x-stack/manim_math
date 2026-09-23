"""相反数课程的纯 Python 数学/结构回归；不代表 Manim 渲染通过。"""

import ast
from fractions import Fraction
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).with_name('opposite_numbers.py').read_text(encoding='utf-8')
TREE = ast.parse(SOURCE)


def isolated_opposite():
    function = next(n for n in TREE.body if isinstance(n, ast.FunctionDef)
                    and n.name == 'opposite')
    module = ast.Module(body=[function], type_ignores=[])
    namespace = {}
    exec(compile(module, '<opposite-only>', 'exec'), namespace)
    return namespace['opposite']


class OppositeNumbersRegression(unittest.TestCase):
    def test_mathematics_and_zero(self):
        opposite = isolated_opposite()
        for number in (Fraction(0), Fraction(3), Fraction(-5),
                       Fraction(3, 2), Fraction(-7, 4)):
            self.assertEqual(number + opposite(number), 0)
            self.assertEqual(opposite(opposite(number)), number)
            self.assertEqual(abs(opposite(number)), abs(number))
        self.assertEqual(opposite(0), 0)

    def test_scene_entry_and_six_beats(self):
        scene = next(n for n in TREE.body if isinstance(n, ast.ClassDef)
                     and n.name == 'OppositeNumbers')
        names = {n.name for n in scene.body if isinstance(n, ast.FunctionDef)}
        for index, name in enumerate(('opening', 'number_line', 'definition',
                                      'more_examples', 'special_case', 'summary'), 1):
            self.assertIn(f'scene_{index}_{name}', names)

    def test_points_derive_from_single_axis(self):
        self.assertIn('self.axis.n2p(value)', SOURCE)
        self.assertIn('self.axis.n2p(opposite(0))', SOURCE)
        self.assertIn('left_value, right_value = opposite(3), 3', SOURCE)
        self.assertIn('origin = self.axis.n2p(0)', SOURCE)

    def test_no_nested_play_or_chinese_mathtex(self):
        for node in ast.walk(TREE):
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'play':
                for arg in node.args:
                    self.assertFalse(isinstance(arg, ast.Call)
                                     and isinstance(arg.func, ast.Attribute)
                                     and arg.func.attr == 'play')
            if isinstance(node.func, ast.Name) and node.func.id == 'MathTex':
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        self.assertFalse(re.search(r'[\u4e00-\u9fff]', arg.value))

    def test_portrait_configuration(self):
        self.assertIn('config.frame_width = 9', SOURCE)
        self.assertIn('config.frame_height = 16', SOURCE)
        self.assertIn('UP * 6.7', SOURCE)


if __name__ == '__main__':
    unittest.main()
