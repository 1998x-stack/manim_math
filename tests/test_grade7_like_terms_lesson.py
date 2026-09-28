"""七年级第一学期第 002 课：不依赖 Manim 的数学和代码专项测试。"""
import ast
from collections import defaultdict
from pathlib import Path
import unittest

SOURCE = (Path(__file__).resolve().parents[1]
          / '初中/七年级/第一学期/第九章-整式/002同类项与合并同类项/like_terms.py')


def signature(exponents):
    """字母次幂的规范表示，系数无关，常数项返回空签名。"""
    if any(not isinstance(power, int) or power < 0 for power in exponents.values()):
        raise ValueError('单项式的字母指数必须为非负整数')
    return tuple(sorted((name, power) for name, power in exponents.items() if power))


def combine(terms):
    """每项为 (系数, 指数字典)，按相同字母部分合并。"""
    result = defaultdict(int)
    for coefficient, powers in terms:
        result[signature(powers)] += coefficient
    return {key: value for key, value in result.items() if value}


class LikeTermsLessonTests(unittest.TestCase):
    def test_signatures_and_counterexamples(self):
        self.assertEqual(signature({'y': 1, 'x': 2}), signature({'x': 2, 'y': 1}))
        self.assertNotEqual(signature({'x': 2, 'y': 1}), signature({'x': 1, 'y': 2}))
        self.assertNotEqual(signature({'a': 2}), signature({'a': 1}))
        self.assertEqual(signature({}), signature({'x': 0}))
        with self.assertRaises(ValueError):
            signature({'x': -1})

    def test_example_arithmetic(self):
        x2y = {'x': 2, 'y': 1}
        xy = {'x': 1, 'y': 1}
        terms = [(3, x2y), (-5, x2y), (2, xy), (4, x2y), (-1, xy)]
        self.assertEqual(combine(terms), {signature(x2y): 2, signature(xy): 1})
        self.assertEqual(combine([(3, x2y), (-5, x2y)]), {signature(x2y): -2})
        self.assertEqual(combine([(5, {}), (-3, {})]), {(): 2})
        self.assertEqual(combine([(3, x2y), (-3, x2y)]), {})
        for x, y in ((0, 0), (1, 1), (-2, 3), (3, -2)):
            original = 3*x*x*y - 5*x*x*y + 2*x*y + 4*x*x*y - x*y
            simplified = 2*x*x*y + x*y
            self.assertEqual(original, simplified)

    def test_scene_entrypoint_and_manim_gotchas(self):
        source = SOURCE.read_text(encoding='utf-8')
        tree = ast.parse(source, filename=str(SOURCE))
        scene = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                     and node.name == 'LikeTerms')
        methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
        for name in ('construct', 'show_opening', 'show_definition', 'show_examples',
                     'show_rule', 'show_full_example', 'show_outro'):
            self.assertIn(name, methods)
        for call in (node for node in ast.walk(tree) if isinstance(node, ast.Call)):
            if isinstance(call.func, ast.Attribute):
                self.assertNotEqual(call.func.attr, 'get_tex_string')
            if isinstance(call.func, ast.Name) and call.func.id in {'MathTex', 'Tex'}:
                for value in call.args:
                    if isinstance(value, ast.Constant) and isinstance(value.value, str):
                        self.assertFalse(any('\u4e00' <= c <= '\u9fff' or c == '\u00a0'
                                             for c in value.value))

    def test_card_width_and_source_safe_area(self):
        # 五个分类行依次相距 1.95，行标签与下行不存在中心重合。
        centers = [3.8 - i * 1.95 for i in range(5)]
        self.assertTrue(all(centers[i] > centers[i + 1] for i in range(4)))
        self.assertLess(max(centers), 7)
        self.assertGreater(min(centers) - 0.72, -7)


if __name__ == '__main__':
    unittest.main()
