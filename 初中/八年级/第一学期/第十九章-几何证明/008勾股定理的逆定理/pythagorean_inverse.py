"""勾股定理的逆定理：八年级第一学期，第十九章。

示意采用 C 为直角顶点；a=|BC|、b=|CA|、c=|AB|，避免图示角标和
公式中的对边约定冲突。运行：manim -ql pythagorean_inverse.py PythagoreanInverse
"""

from math import isclose, isfinite

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#0D1B2A"
GOLD = "#FFD700"
GREEN = "#4CAF50"
BLUE = "#4FC3F7"
RED = "#EF5350"
FONT = "PingFang SC"


def is_right_triangle_sides(sides):
    """独立于 Manim 的数学判断：三条有限正边，三角形成立且满足勾股关系。"""
    if len(sides) != 3:
        return False
    try:
        a, b, c = sorted(float(side) for side in sides)
    except (ValueError, TypeError, OverflowError):
        return False
    if not all(isfinite(side) and side > 0 for side in (a, b, c)):
        return False
    if a + b <= c:
        return False
    return isclose(a * a + b * b, c * c, rel_tol=1e-10, abs_tol=1e-10)


class PythagoreanInverse(Scene):
    """通过对应的角和边证明勾股定理及其逆定理。"""

    def construct(self):
        self.camera.background_color = BG
        self.author = self._text("上海初高中数学直通车 @emptyandcalm", 7.0, 19, GRAY_B)
        self.play(FadeIn(self.author), run_time=0.3)
        self.scene1_intro()
        self.scene2_forward()
        self.scene3_inverse_concept()
        self.scene4_example_345()
        self.scene5_pythagorean_triples()
        self.scene6_summary()

    def _text(self, content, y, size=29, color=WHITE):
        return Text(content, font=FONT, font_size=size, color=color).move_to(UP * y)

    def _math(self, latex, y, size=39, color=WHITE):
        return MathTex(latex, font_size=size, color=color).move_to(UP * y)

    def _clear(self):
        visible = [mob for mob in self.mobjects if mob is not self.author]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.4)

    def _triangle(self, scale=0.88, shift=ORIGIN, show_lengths=True):
        """C=(-2,-1)、A=(-2,2)、B=(2,-1)，CA=3、CB=4、AB=5。"""
        C = np.array([-2.0, -1.0, 0.0]) * scale + shift
        A = np.array([-2.0, 2.0, 0.0]) * scale + shift
        B = np.array([2.0, -1.0, 0.0]) * scale + shift
        shape = Polygon(A, B, C, color=BLUE, fill_color=BLUE,
                        fill_opacity=0.2, stroke_width=3)
        vertex_labels = VGroup(
            MathTex("A", font_size=27).next_to(A, UP + LEFT, buff=0.16),
            MathTex("B", font_size=27).next_to(B, RIGHT + DOWN, buff=0.16),
            MathTex("C", font_size=27).next_to(C, LEFT + DOWN, buff=0.16),
        )
        legs = VGroup(
            MathTex("a=4" if show_lengths else "a", font_size=31,
                    color=GOLD).next_to((B + C) / 2, DOWN, buff=0.18),
            MathTex("b=3" if show_lengths else "b", font_size=31,
                    color=GOLD).next_to((A + C) / 2, LEFT, buff=0.17),
            MathTex("c=5" if show_lengths else "c", font_size=31,
                    color=GOLD).next_to((A + B) / 2, UP + RIGHT, buff=0.20),
        )
        mark = RightAngle(Line(C, B), Line(C, A), length=0.24, color=GREEN)
        return VGroup(shape, vertex_labels, legs), mark

    def scene1_intro(self):
        title = self._text("只知道三边，怎样判断直角？", 5.5, 34, GOLD)
        prompt = self._text("用勾股定理的逆定理来判断", 3.7, 28)
        self.play(Write(title), FadeIn(prompt), run_time=0.9)
        self.wait(1.1)
        self._clear()

    def scene2_forward(self):
        title = self._text("回顾：勾股定理", 5.6, 36, BLUE)
        triangle, marker = self._triangle(show_lengths=False, shift=UP * 0.7)
        given = self._math(r"\angle C=90^\circ", -2.3, 39, GREEN)
        result = self._math(r"a^2+b^2=c^2", -3.4, 47, GOLD)
        self.play(Write(title), Create(triangle[0]), run_time=0.8)
        self.play(FadeIn(triangle[1:]), Create(marker), run_time=0.5)
        self.play(Write(given), Write(result), run_time=0.8)
        self.wait(1.3)
        self._clear()

    def scene3_inverse_concept(self):
        title = self._text("逆定理：条件与结论交换", 5.5, 34, GOLD)
        forward = self._math(r"\angle C=90^\circ\ \Longrightarrow\ a^2+b^2=c^2", 3.7, 34, BLUE)
        inverse = self._math(r"a^2+b^2=c^2\ \Longrightarrow\ \angle C=90^\circ", 1.8, 34, GREEN)
        rule = self._text("已知三角形三边满足这个等式，", -0.2, 28)
        consequence = self._text("最长边 c 的对角 C 就是直角", -1.0, 28, GOLD)
        order = self._text("前提：a=BC，b=CA，c=AB", -2.7, 26, GRAY_A)
        box = SurroundingRectangle(inverse, color=GREEN, buff=0.23)
        self.play(Write(title), Write(forward), run_time=0.9)
        self.play(Write(inverse), Create(box), run_time=0.9)
        self.play(FadeIn(rule), FadeIn(consequence), FadeIn(order), run_time=0.7)
        self.wait(1.3)
        self._clear()

    def scene4_example_345(self):
        title = self._text("例题：三边分别为 3、4、5", 5.5, 34, GOLD)
        question = self._text("不用量角器，可以判定直角吗？", 4.6, 26)
        diagram, mark = self._triangle(scale=0.73, shift=UP * 1.7)
        calc1 = self._math(r"3^2+4^2=9+16=25", -2.4, 36)
        calc2 = self._math(r"5^2=25", -3.2, 36)
        conclusion = self._math(r"\therefore\ \angle C=90^\circ", -4.2, 40, GREEN)
        self.play(Write(title), FadeIn(question), run_time=0.7)
        self.play(Create(diagram[0]), FadeIn(diagram[1:]), run_time=0.9)
        self.play(Write(calc1), Write(calc2), run_time=0.8)
        self.play(Create(mark), Write(conclusion), run_time=0.7)
        self.wait(1.3)
        self._clear()

    def scene5_pythagorean_triples(self):
        title = self._text("常见勾股数与反例", 5.5, 36, GOLD)
        examples = ((3, 4, 5), (5, 12, 13), (8, 15, 17), (2, 3, 4))
        self.play(Write(title), run_time=0.5)
        for idx, triple in enumerate(examples):
            a, b, c = triple
            works = is_right_triangle_sides(triple)
            lhs = a * a + b * b
            rhs = c * c
            formula = self._math(
                rf"{a}^2+{b}^2={lhs}\ {'=' if works else '\\ne'}\ {rhs}={c}^2",
                3.3 - idx * 1.65, size=28,
                color=GREEN if works else RED,
            )
            self.play(Write(formula), run_time=0.5)
        reminder = self._text("先找最长边；三边都为正且构成三角形", -4.0, 24, GOLD)
        self.play(FadeIn(reminder), run_time=0.5)
        self.wait(1.4)
        self._clear()

    def scene6_summary(self):
        title = self._text("逆定理的判断步骤", 5.5, 39, GOLD)
        rule = self._math(r"a^2+b^2=c^2\ \Longrightarrow\ \angle C=90^\circ", 3.5, 35, GREEN)
        note1 = self._text("① 确认三边能构成三角形", 1.4, 28)
        note2 = self._text("② 找最长边 c，核对平方关系", 0.0, 28)
        note3 = self._text("③ 得到最长边所对的直角", -1.4, 28)
        self.play(Write(title), Write(rule), run_time=0.9)
        self.play(FadeIn(note1), FadeIn(note2), FadeIn(note3), run_time=0.9)
        self.wait(1.6)
