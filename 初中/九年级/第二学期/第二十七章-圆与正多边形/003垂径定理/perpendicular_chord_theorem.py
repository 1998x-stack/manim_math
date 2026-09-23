"""垂径定理：先验证弦、直径与两条弧，再生成可核对的教学动画。"""

from math import asin, degrees, hypot, sqrt

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def chord_geometry(radius, center_y=1.0, chord_height=None):
    """以水平非直径弦作图；返回真实顶点及四段分弧的有向角（度）。"""
    if radius <= 0:
        raise ValueError("半径必须为正")
    if chord_height is None:
        chord_height = radius / 2
    if not 0 < chord_height < radius:
        raise ValueError("本课选用不经过圆心且两端不同的弦：0<h<r")
    half_chord = sqrt(radius * radius - chord_height * chord_height)
    alpha = degrees(asin(chord_height / radius))
    o = (0.0, center_y)
    m = (0.0, center_y + chord_height)
    points = {'O': o, 'A': (-half_chord, m[1]), 'B': (half_chord, m[1]),
              'M': m, 'C': (0.0, center_y + radius),
              'E': (0.0, center_y - radius)}
    sweeps = {'minor_AC': alpha - 90, 'minor_CB': alpha - 90,
              'major_AE': 90 + alpha, 'major_EB': 90 + alpha}
    tol = 1e-8 * radius
    for name in ('A', 'B', 'C', 'E'):
        if abs(hypot(points[name][0] - o[0], points[name][1] - o[1]) - radius) > tol:
            raise ArithmeticError(f'{name} 不在圆上')
    if abs(hypot(points['A'][0] - m[0], points['A'][1] - m[1])
           - hypot(points['B'][0] - m[0], points['B'][1] - m[1])) > tol:
        raise ArithmeticError('MA 与 MB 不等长')
    if not (0 < -2 * sweeps['minor_AC'] < 180
            and 180 < 2 * sweeps['major_AE'] < 360):
        raise ArithmeticError('优劣弧范围与几何坐标不一致')
    return {'points': points, 'alpha': alpha, 'radius': radius,
            'sweeps': sweeps}


class PerpendicularChordTheorem(Scene):
    """保留原 Scene 入口和七个教学阶段。"""

    def construct(self):
        self.camera.background_color = '#1a1a2e'
        spec = chord_geometry(radius=2.125, center_y=1.0)
        self.r, self.alpha, self.sweeps = spec['radius'], spec['alpha'], spec['sweeps']
        self.p = {k: np.array([*xy, 0.0]) for k, xy in spec['points'].items()}
        self.blue, self.red, self.orange = '#3498db', '#e74c3c', '#f39c12'
        self.green, self.purple = '#2ecc71', '#9b59b6'
        self.author = Text('上海初高中数学直通车 @emptyandcalm',
                           font_size=19, color=GRAY_B).move_to(UP * 6.65)
        self.circle = Circle(radius=self.r, color=self.blue,
                             stroke_width=4).move_to(self.p['O'])
        self.chord = Line(self.p['A'], self.p['B'], color=self.orange, stroke_width=5)
        self.scene_1_opening()
        self.scene_2_draw_diameter()
        self.scene_3_bisect_chord()
        self.scene_4_bisect_major_arc()
        self.scene_5_bisect_minor_arc()
        self.scene_6_theorem_summary()
        self.scene_7_outro()

    def _title(self, value, color=YELLOW):
        return Text(value, font_size=33, color=color).move_to(UP * 5.45)

    def _caption(self, value, y=-4.8):
        return Text(value, font_size=24, color=GRAY_A).move_to(UP * y)

    def _arc(self, start, sweep, color):
        return Arc(radius=self.r, start_angle=start * DEGREES,
                   angle=sweep * DEGREES, arc_center=self.p['O'],
                   color=color, stroke_width=6)

    def scene_1_opening(self):
        hook = self._title('如何找到弦 AB 的中点？')
        self.dot_A = Dot(self.p['A'], radius=0.085, color=WHITE)
        self.dot_B = Dot(self.p['B'], radius=0.085, color=WHITE)
        self.label_A = Text('A', font_size=23).next_to(self.dot_A, LEFT, buff=0.13)
        self.label_B = Text('B', font_size=23).next_to(self.dot_B, RIGHT, buff=0.13)
        self.play(FadeIn(self.author), Write(hook), run_time=0.7)
        self.play(Create(self.circle), Create(self.chord), run_time=1.1)
        self.play(FadeIn(self.dot_A), FadeIn(self.dot_B),
                  FadeIn(self.label_A), FadeIn(self.label_B), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(hook), run_time=0.4)

    def scene_2_draw_diameter(self):
        self.title = self._title('过圆心作垂直于弦 AB 的直径', self.red)
        self.diameter = Line(self.p['C'], self.p['E'], color=self.red,
                             stroke_width=4)
        self.center_dot = Dot(self.p['O'], color=self.red, radius=0.09)
        self.foot_dot = Dot(self.p['M'], color=YELLOW, radius=0.085)
        self.dot_C = Dot(self.p['C'], radius=0.07)
        self.dot_E = Dot(self.p['E'], radius=0.07)
        self.labels = VGroup(
            Text('O', font_size=23, color=self.red).next_to(self.center_dot, LEFT, buff=0.15),
            Text('M', font_size=23, color=YELLOW).next_to(self.foot_dot, DOWN + RIGHT, buff=0.12),
            Text('C', font_size=23).next_to(self.dot_C, UP, buff=0.13),
            Text('E', font_size=23).next_to(self.dot_E, DOWN, buff=0.13),
        )
        right_angle = RightAngle(Line(self.p['M'], self.p['A']),
                                 Line(self.p['M'], self.p['O']),
                                 length=0.17, color=YELLOW)
        self.right_angle = right_angle
        caption = self._caption('CE 经过圆心 O，且 CE 垂直于弦 AB')
        self.play(Write(self.title), Create(self.diameter), run_time=0.9)
        self.play(FadeIn(self.center_dot), FadeIn(self.foot_dot),
                  FadeIn(self.dot_C), FadeIn(self.dot_E), FadeIn(self.labels),
                  FadeIn(right_angle), FadeIn(caption), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(caption), run_time=0.4)

    def scene_3_bisect_chord(self):
        step = self._caption('直角三角形 OMA 与 OMB：斜边相等，OM 为公共边', -3.9)
        result = MathTex(r'MA=MB', font_size=35, color=YELLOW).move_to(DOWN * 4.9)
        radii = VGroup(Line(self.p['O'], self.p['A'], color=self.purple, stroke_width=3),
                       Line(self.p['O'], self.p['B'], color=self.purple, stroke_width=3))
        self.play(*[Create(line) for line in radii], FadeIn(step), run_time=1.0)
        self.play(FadeIn(result), Indicate(self.foot_dot, color=YELLOW), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(radii), FadeOut(step), FadeOut(result), run_time=0.6)

    def scene_4_bisect_major_arc(self):
        # A(180-alpha°) -> E(270°) -> B(360+alpha°)：两段各 90+alpha°。
        major_ae = self._arc(180 - self.alpha, self.sweeps['major_AE'], self.purple)
        major_eb = self._arc(270, self.sweeps['major_EB'], self.purple)
        step = self._caption('优弧 AEB 经过 E：两段弧的圆心角相等', -3.9)
        result = MathTex(r'\overset{\frown}{AE}=\overset{\frown}{EB}',
                         font_size=34, color=self.purple).move_to(DOWN * 4.9)
        self.play(Create(major_ae), Create(major_eb), FadeIn(step), run_time=1.1)
        self.play(FadeIn(result), Indicate(self.dot_E, color=YELLOW), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(major_ae), FadeOut(major_eb),
                  FadeOut(step), FadeOut(result), run_time=0.6)

    def scene_5_bisect_minor_arc(self):
        # A(180-alpha°) -> C(90°) -> B(alpha°)：两段各 alpha-90°（顺时针）。
        minor_ac = self._arc(180 - self.alpha, self.sweeps['minor_AC'], self.green)
        minor_cb = self._arc(90, self.sweeps['minor_CB'], self.green)
        step = self._caption('劣弧 ACB 经过 C：两段弧的圆心角相等', -3.9)
        result = MathTex(r'\overset{\frown}{AC}=\overset{\frown}{CB}',
                         font_size=34, color=self.green).move_to(DOWN * 4.9)
        self.play(Create(minor_ac), Create(minor_cb), FadeIn(step), run_time=1.1)
        self.play(FadeIn(result), Indicate(self.dot_C, color=YELLOW), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(minor_ac), FadeOut(minor_cb),
                  FadeOut(step), FadeOut(result), run_time=0.6)

    def scene_6_theorem_summary(self):
        self.play(FadeOut(self.title), run_time=0.3)
        title = self._title('垂径定理', GOLD)
        text = VGroup(Text('垂直于弦的直径', font_size=29),
                      Text('平分这条弦和弦所对的两条弧', font_size=28))
        text.arrange(DOWN, buff=0.28).move_to(DOWN * 3.9)
        formula = MathTex(r'CE\perp AB\;\Rightarrow\;MA=MB',
                          font_size=31, color=YELLOW).move_to(DOWN * 5.6)
        self.play(Write(title), FadeIn(text), run_time=0.8)
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(1.3)
        self.play(FadeOut(title), FadeOut(text), FadeOut(formula), run_time=0.6)

    def scene_7_outro(self):
        diagram = VGroup(self.circle, self.chord, self.diameter, self.dot_A,
                         self.dot_B, self.dot_C, self.dot_E, self.center_dot,
                         self.foot_dot, self.label_A, self.label_B,
                         self.labels, self.right_angle)
        self.play(diagram.animate.scale(0.5).move_to(UP * 3.8), run_time=0.9)
        summary = VGroup(
            Text('弦被平分：MA=MB', font_size=28, color=self.orange),
            Text('优弧被平分：弧 AE=弧 EB', font_size=27, color=self.purple),
            Text('劣弧被平分：弧 AC=弧 CB', font_size=27, color=self.green),
        ).arrange(DOWN, buff=0.33).move_to(DOWN * 1.6)
        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT * 0.4)
                                for line in summary], lag_ratio=0.25), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(diagram), FadeOut(summary), FadeOut(self.author), run_time=0.8)
