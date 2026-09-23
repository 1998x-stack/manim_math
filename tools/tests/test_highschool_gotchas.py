"""Static regression contracts for high-school historical Manim gotchas."""
import ast
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from audit_highschool_gotchas import audit, extra_findings, _ctex_calls
from audit_junior_gotchas import audit_source
from repair_highschool_gotchas import _span, ANGLE, RATIO, SINE


class HighSchoolGotchaContracts(unittest.TestCase):
    def test_unicode_ast_span_stays_exact(self):
        source = '变量 = Tex("中文公式", color=WHITE).move_to(UP)\n'
        call = next(n for n in ast.walk(ast.parse(source))
                    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id == 'Tex')
        a, b = _span(source, call)
        self.assertEqual(source[a:b], 'Tex("中文公式", color=WHITE)')

    def test_degree_labels_are_valid_latex(self):
        for path in (ANGLE, RATIO):
            source = path.read_text(encoding='utf-8')
            findings = audit_source(source, str(path))
            self.assertFalse(any(item['code'] == 'UNICODE_IN_TEX' for item in findings),
                             findings)
            self.assertIn('^{{\\circ}}', source)
        self.assertIn('int(round(np.degrees(angle)))', RATIO.read_text(encoding='utf-8'))

    def test_sine_scene_is_not_nested_play_or_chinese_tex(self):
        source = SINE.read_text(encoding='utf-8')
        self.assertEqual([], extra_findings(source, str(SINE)))
        self.assertFalse(any(item['code'] == 'CHINESE_IN_TEX'
                             for item in audit_source(source, str(SINE))))
        self.assertIn('self.play(*[FadeOut(m) for m in list(self.mobjects)]', source)
        self.assertNotIn('self.play(self.play(', source)
        self.assertIn('self.x_range = [-2*np.pi, 2*np.pi, np.pi/2]', source)
        self.assertIn('T=\\frac{2\\pi}{|\\omega|}', source)

    def test_math_invariants_for_negative_omega(self):
        for omega in (-4.0, -2.0, 1.0, 2.0, 4.0):
            period = 2 * math.pi / abs(omega)
            for x in (-1.0, 0.2, 1.0):
                self.assertAlmostEqual(math.sin(omega * (x + period)),
                                       math.sin(omega * x), places=12)

    def test_custom_ctex_is_explicit_opt_in(self):
        ctex = ast.parse('MathTex(r"\\text{圆心}", tex_template=TexTemplateLibrary.ctex)')
        default = ast.parse('MathTex(r"\\text{圆心}")')
        self.assertEqual({1}, _ctex_calls(ctex))
        self.assertEqual(set(), _ctex_calls(default))

    def test_all_grades_have_no_untriaged_gotchas(self):
        data = audit(ROOT)
        # 新课程增加文件数；把历史基线作为下界，同时要求错误/警告为零。
        for grade, baseline in {'高一': 49, '高二': 42, '高三': 40}.items():
            self.assertGreaterEqual(data['grades'][grade], baseline, data['grades'])
        self.assertEqual(0, data['errors'], data['findings'])
        self.assertEqual(0, data['warnings'], data['findings'])
        # 修复中文 MathTex/ctex 依赖后，信息级待渲染提醒应当减少；
        # 固定等于 3 会把真实改进错误地判为 CI 失败。
        self.assertLessEqual(data['information'], 3, data['findings'])


if __name__ == '__main__':
    unittest.main()
