"""Source and numeric contracts for the five guarded junior gotcha repairs."""
import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
G6 = ROOT / '初中/六年级/第一学期/第四章-圆和扇形/005弧长公式/arc_length_formula.py'
G9Q = ROOT / '初中/九年级/第一学期/第二十六章-二次函数/001二次函数的概念/quadratic_function.py'
G9V = ROOT / '初中/九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_function_vertex.py'
G9V2 = ROOT / '初中/九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_vertex_form.py'
G9S = ROOT / '初中/九年级/第二学期/第二十八章-统计初步/007用样本估计总体/sample_estimation.py'


def read(path):
    source = path.read_text(encoding='utf-8')
    return source, ast.parse(source, filename=str(path))


class JuniorRoundTwoContract(unittest.TestCase):
    def test_arc_all_five_degree_labels_use_latex(self):
        source, tree = read(G6)
        self.assertNotIn('r"n°"', source)
        self.assertNotIn('r"360°"', source)
        self.assertGreaterEqual(source.count(r'n^{\circ}'), 3)
        self.assertGreaterEqual(source.count(r'360^{\circ}'), 2)
        self.assertTrue(any(isinstance(n, ast.ClassDef) and n.name.endswith('Scene')
                            for n in ast.walk(tree)))

    def test_quadratic_no_empty_animation_and_nonzero_initial_range(self):
        source, tree = read(G9Q)
        self.assertNotIn('FadeOut(x_lab) if x_lab else []', source)
        self.assertIn('ValueTracker(self.CURVE_X[0] + 0.02)', source)
        self.assertIn('self.CURVE_X = [-2.0, 2.0]', source)
        self.assertLessEqual(max(abs(-2.0), abs(2.0)) ** 2, 5)
        self.assertTrue(any(isinstance(n, ast.ClassDef) and n.name == 'QuadraticFunctionIntro'
                            for n in tree.body))

    def test_summary_chinese_is_text_not_mathtex(self):
        source, _ = read(G9V)
        self.assertNotIn(r'\text{最小值}', source)
        self.assertNotIn(r'\text{最大值}', source)
        self.assertIn('Text("最小值"', source)
        self.assertIn('Text("最大值"', source)

    def test_vertex_emphasis_keeps_math_formula_and_chinese_text(self):
        source, _ = read(G9V2)
        self.assertIn('MathTex(r"y_{\\min} = k"', source)
        self.assertIn('Text("时，"', source)
        self.assertNotIn(r'\text{当 }', source)

    def test_sampling_local_rng_and_nonmonotone_claim(self):
        source, tree = read(G9S)
        self.assertNotIn('random.seed(', source)
        self.assertNotIn('np.random.seed(', source)
        self.assertNotIn('random.sample(', source)
        self.assertIn('self.rng = np.random.default_rng(42)', source)
        self.assertIn('size=size, replace=False', source)
        self.assertIn('通常更稳定，但仍有波动', source)
        self.assertIn('非随机抽样', source)
        self.assertIn('仍有抽样误差', source)
        self.assertTrue(any(isinstance(n, ast.ClassDef) and n.name == 'SampleEstimation'
                            for n in tree.body))


if __name__ == '__main__':
    unittest.main()
