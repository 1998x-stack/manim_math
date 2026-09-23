"""Guarded one-time fixes for junior Manim scene gotchas (stdlib only).

Run from repository root: python tools/repair_junior_gotchas_round2.py --apply
Every change checks its exact preimage. Refuse to alter an unexpected revision;
no media, indexing, or unrelated scenes are touched.
"""
from __future__ import annotations

import argparse
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
G6 = Path('初中/六年级/第一学期/第四章-圆和扇形/005弧长公式/arc_length_formula.py')
G9_Q = Path('初中/九年级/第一学期/第二十六章-二次函数/001二次函数的概念/quadratic_function.py')
G9_V = Path('初中/九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_function_vertex.py')
G9_V2 = Path('初中/九年级/第一学期/第二十六章-二次函数/004二次函数y=a(x-h)²+k的图像与性质/quadratic_vertex_form.py')
G9_S = Path('初中/九年级/第二学期/第二十八章-统计初步/007用样本估计总体/sample_estimation.py')


def substitute(text: str, old: str, new: str, count: int, path: Path) -> str:
    """Replace only a known exact source pattern and reject unexpected drift."""
    actual = text.count(old)
    if actual != count:
        raise ValueError(f'{path}: expected {count} occurrences of {old!r}; found {actual}')
    if old == new:
        raise ValueError('no-op repair rule')
    return text.replace(old, new)


def repair_arc(text: str, path: Path) -> str:
    # The original five MathTex Unicode-degree labels are n° (three) and 360° (two).
    for old, new, count in ((r'r"n°"', r'r"n^{\circ}"', 3),
                            (r'r"360°"', r'r"360^{\circ}"', 2)):
        text = substitute(text, old, new, count, path)
    return text


def repair_quadratic(text: str, path: Path) -> str:
    # Standard x^2 is visible for x in [-2,2], since axes y_max=5.
    text = substitute(text, 'self.CURVE_X = [-2.5, 2.5]',
                      'self.CURVE_X = [-2.0, 2.0]', 1, path)
    # x_lab is constructed but never added to the Scene in the opening shot.
    text = substitute(text, '            FadeOut(x_lab) if x_lab else [],\n', '', 1, path)
    text = substitute(text, 't = ValueTracker(self.CURVE_X[0])',
                      't = ValueTracker(self.CURVE_X[0] + 0.02)', 1, path)
    return text


def repair_vertex_summary(text: str, path: Path) -> str:
    for Chinese in ('最小值', '最大值'):
        old = f'MathTex(r"\\text{{{Chinese}}} = k", font_size=22, color=WHITE)'
        new = (f'VGroup(Text("{Chinese}", font="PingFang SC", font_size=22, color=WHITE),\n'
               '                   MathTex("= k", font_size=22, color=WHITE))'
               '.arrange(RIGHT, buff=0.12)')
        text = substitute(text, old, new, 1, path)
    return text


def repair_vertex_formula(text: str, path: Path) -> str:
    old = '''formula_emphasis = MathTex(
            r"\\text{当 } x = h \\text{ 时，} y_{\\min} = k",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)'''
    new = '''formula_emphasis = VGroup(
            Text("当", font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex("x = h", font_size=24, color=self.COLOR_HIGHLIGHT),
            Text("时，", font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex(r"y_{\\min} = k", font_size=24, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 5.5)'''
    return substitute(text, old, new, 1, path)


def repair_sample(text: str, path: Path) -> str:
    text = substitute(text, 'import random\n', '', 1, path)
    text = substitute(text, '        random.seed(42)\n        np.random.seed(42)',
                      '        self.rng = np.random.default_rng(42)', 1, path)
    text = substitute(text, 'self.population_data = np.random.normal(',
                      'self.population_data = self.rng.normal(', 1, path)
    text = substitute(text, 'random.sample(range(self.population_size), sample_size)',
                      'self.rng.choice(self.population_size, size=sample_size, replace=False).tolist()', 1, path)
    text = substitute(text, 'random.sample(range(self.population_size), size)',
                      'self.rng.choice(self.population_size, size=size, replace=False).tolist()', 1, path)
    text = substitute(text, 'random.sample(range(self.population_size), 10)',
                      'self.rng.choice(self.population_size, size=10, replace=False).tolist()', 1, path)
    # A single realized sequence cannot demonstrate monotonically improving accuracy.
    text = substitute(text, 'Text("估计越准确", font=self.FONT_CHINESE, font_size=28, color=self.COLOR_ESTIMATE, weight=BOLD)',
                      'Text("通常更稳定，但仍有波动", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_ESTIMATE, weight=BOLD)', 1, path)
    # First ten i.i.d. population members are not proven statistically biased.
    text = substitute(text, '"❌ 有偏样本（集中某区域）"',
                      '"固定选取前 10 个：非随机抽样"', 1, path)
    text = substitute(text, '"✓ 代表性样本（随机分布）"',
                      '"简单随机抽样：仍有抽样误差"', 1, path)
    return text


REPAIRS = ((G6, repair_arc), (G9_Q, repair_quadratic),
           (G9_V, repair_vertex_summary), (G9_V2, repair_vertex_formula),
           (G9_S, repair_sample))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='write verified source edits')
    args = parser.parse_args(argv)
    pending = []
    for rel, fix in REPAIRS:
        path = ROOT / rel
        before = path.read_text(encoding='utf-8')
        after = fix(before, rel)
        ast.parse(after, filename=str(rel))
        pending.append((path, after))
        print('checked:', rel)
    if args.apply:
        for path, after in pending:
            path.write_text(after, encoding='utf-8')
        print('applied:', len(pending), 'source files')
    else:
        print('dry run: no files changed; pass --apply to write')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
