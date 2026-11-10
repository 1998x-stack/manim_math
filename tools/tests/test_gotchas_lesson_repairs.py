"""Dependency-free regression contracts for confirmed historical gotcha repairs."""
from __future__ import annotations

import ast
import unittest
from pathlib import Path

from tools.commit_gotchas import ROOT, inspect_source

LESSONS = {
    "小学/四年级/第一学期/第五章-几何小实践——圆与角/001线段、射线、直线/001_线段射线直线.py": "LineSegmentRayLesson",
    "小学/四年级/第一学期/第四章-数的运算——除数是两位数的除法/002笔算除法(试商与调商)/002_笔算除法.py": "WrittenDivisionLesson",
    "小学/四年级/第二学期/第三章-统计/001单式折线统计图/001单式折线统计图_animation.py": "Topic001单式折线统计图Animation",
    "初中/九年级/第二学期/第二十七章-圆与正多边形/008切线的性质与判定/tangent_properties.py": "TangentProperties",
    "external/monge_circle.py": "MongeCircle",
}


class LessonRepairTests(unittest.TestCase):
    def test_five_repaired_scenes_parse_and_eliminate_original_risks(self):
        for relative, scene in LESSONS.items():
            with self.subTest(relative=relative):
                path = ROOT / relative
                tree = ast.parse(path.read_bytes(), filename=relative)
                classes = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}
                self.assertIn(scene, classes)
                self.assertTrue(any(isinstance(base, ast.Name) and base.id == 'Scene'
                                    for base in classes[scene].bases))
                found = {item['rule'] for item in inspect_source(path)}
                self.assertNotIn('SYNTAX_ERROR', found)
                self.assertNotIn('NESTED_PLAY', found)
                self.assertNotIn('CHINESE_IN_TEX', found)

    def test_division_example_and_chart_data(self):
        root = ROOT / '小学/四年级'
        division = next(root.rglob('002_笔算除法.py'))
        source = division.read_text(encoding='utf-8')
        tree = ast.parse(source)
        classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
        self.assertIn('WrittenDivisionLesson', classes)
        self.assertIn('self.eg1_dividend = 952', source)
        self.assertIn('self.eg1_divisor = 34', source)
        dividend, divisor = 952, 34
        quotient, remainder = divmod(dividend, divisor)
        self.assertEqual((quotient, remainder), (28, 0))
        self.assertEqual(dividend, divisor * quotient + remainder)
        self.assertLess(remainder, divisor)

        chart = next(root.rglob('001单式折线统计图_animation.py'))
        chart_tree = ast.parse(chart.read_bytes())
        chart_values = {target.id: ast.literal_eval(node.value)
                        for node in chart_tree.body if isinstance(node, ast.Assign)
                        and isinstance(node.value, ast.Tuple)
                        for target in node.targets if isinstance(target, ast.Name)}
        self.assertEqual(len(chart_values['DAYS']), len(chart_values['VALUES']))
        self.assertEqual(chart_values['VALUES'], (18, 20, 19, 23, 25))
        self.assertEqual(chart_values['VALUES'][-1] - chart_values['VALUES'][0], 7)


if __name__ == '__main__':
    unittest.main()
