"""梯形蝴蝶模型：上下三角形面积比是平行底边长度比的平方。"""
from fractions import Fraction
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def butterfly_areas(top: int, bottom: int, height: int) -> tuple[Fraction, Fraction, Fraction]:
    """返回上三角形、一个侧三角形、下三角形面积。"""
    if any(type(v) is not int or v <= 0 for v in (top, bottom, height)):
        raise ValueError("positive integer lengths required")
    total = 2 * (top + bottom)
    return (Fraction(top * top * height, total),
            Fraction(top * bottom * height, total),
            Fraction(bottom * bottom * height, total))


class ButterflyAreaScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        small, side, large = butterfly_areas(3, 6, 4)
        assert (small, side, large) == (2, 4, 8)
        title = Text("蝴蝶模型：梯形面积比", font=FONT, font_size=35).move_to(UP * 6.2)
        given = MathTex(r"AB\parallel CD,\quad AB=3,\ CD=6,\ h=4", font_size=29).move_to(UP * 4.95)
        self.play(Write(title), Write(given))
        A, B = np.array([-1.5, 2.0, 0]), np.array([1.5, 2.0, 0])
        D, C = np.array([-3.0, -2.0, 0]), np.array([3.0, -2.0, 0])
        O = A + (A - C) * (-1 / 3)  # AO:OC = AB:CD = 1:2
        shapes = [
            Polygon(A, B, O, stroke_width=2, color=BLUE_B, fill_color=BLUE_D, fill_opacity=.65),
            Polygon(A, O, D, stroke_width=2, color=GREEN_B, fill_color=GREEN_D, fill_opacity=.4),
            Polygon(B, C, O, stroke_width=2, color=GREEN_B, fill_color=GREEN_D, fill_opacity=.4),
            Polygon(C, D, O, stroke_width=2, color=YELLOW, fill_color=YELLOW_D, fill_opacity=.55),
        ]
        outline = Polygon(A, B, C, D, color=WHITE, stroke_width=3)
        diagonals = VGroup(Line(A, C, color=GREY_A), Line(B, D, color=GREY_A))
        self.play(Create(outline), Create(diagonals))
        self.play(*(FadeIn(shape) for shape in shapes))
        values = [(small, (A+B+O)/3), (side, (A+O+D)/3), (side, (B+C+O)/3), (large, (C+D+O)/3)]
        markers = VGroup(*(MathTex(str(value), font_size=35, color=WHITE).move_to(pos) for value, pos in values))
        self.play(FadeIn(markers))
        relation = MathTex(r"S_{AOB}:S_{COD}=3^2:6^2=1:4", font_size=34, color=YELLOW)
        relation.move_to(DOWN * 3.45)
        summary = Text("左右两翼面积相等", font=FONT, font_size=28).move_to(DOWN * 4.8)
        self.play(Write(relation), FadeIn(summary))
        self.wait(2)
