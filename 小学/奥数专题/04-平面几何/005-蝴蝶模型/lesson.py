"""梯形蝴蝶模型：由真实对角线交点生成四块面积，显示两翼相等与平方比。"""
from fractions import Fraction
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def butterfly_areas(top: int, bottom: int, height: int) -> tuple[Fraction, Fraction, Fraction]:
    if any(type(v) is not int or v <= 0 for v in (top, bottom, height)):
        raise ValueError("positive integer lengths required")
    total = 2 * (top + bottom)
    return (Fraction(top * top * height, total),
            Fraction(top * bottom * height, total),
            Fraction(bottom * bottom * height, total))


class ButterflyAreaScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        top, bottom, h = 3, 6, 4
        small, wing, large = butterfly_areas(top, bottom, h)
        assert (small, wing, large) == (2, 4, 8)
        title = Text("蝴蝶模型：四块面积的联系", font=FONT, font_size=35).move_to(UP * 6.2)
        premise = MathTex(r"AB\parallel CD,\quad AB=3,\ CD=6,\ h=4", font_size=29).move_to(UP * 4.94)
        self.play(Write(title), Write(premise))
        A, B = np.array([-1.5, 2., 0]), np.array([1.5, 2., 0])
        D, C = np.array([-3., -2., 0]), np.array([3., -2., 0])
        # 相似三角形 AOB 和 COD：AO:OC=AB:CD=1:2。
        O = A + top / (top + bottom) * (C - A)
        assert np.allclose(O, B + top / (top + bottom) * (D - B))
        outline = Polygon(A, B, C, D, color=WHITE, stroke_width=3)
        diagonals = VGroup(Line(A, C, color=GREY_A), Line(B, D, color=GREY_A))
        names = VGroup(*(MathTex(name, font_size=27).move_to(pos) for name, pos in [
            ("A", [-1.78, 2.36, 0]), ("B", [1.78, 2.36, 0]),
            ("C", [3.28, -2.21, 0]), ("D", [-3.28, -2.21, 0]),
            ("O", [.15, .91, 0])]))
        self.play(Create(outline), Create(diagonals), FadeIn(names))
        top_tri = Polygon(A, B, O, color=BLUE_B, fill_color=BLUE_D, fill_opacity=.65)
        left_tri = Polygon(A, O, D, color=GREEN_B, fill_color=GREEN_D, fill_opacity=.48)
        right_tri = Polygon(B, C, O, color=GREEN_B, fill_color=GREEN_D, fill_opacity=.48)
        bottom_tri = Polygon(C, D, O, color=YELLOW, fill_color=YELLOW_D, fill_opacity=.6)
        regions = (top_tri, left_tri, right_tri, bottom_tri)
        values = (small, wing, wing, large)
        centers = ((A+B+O)/3, (A+O+D)/3, (B+C+O)/3, (C+D+O)/3)
        area_labels = VGroup(*(MathTex(str(value), font_size=36, color=WHITE).move_to(center)
                               for value, center in zip(values, centers)))
        self.play(LaggedStart(*(FadeIn(part) for part in regions), lag_ratio=.22))
        self.play(FadeIn(area_labels))

        # 在交点处可看见上、下两种高度，面积数值与构型尺寸逐一对应。
        horizontal = DashedLine([-3.15, O[1], 0], [3.15, O[1], 0], color=GREY_B)
        self.play(Create(horizontal))
        similar = MathTex(r"AO:OC=AB:CD=1:2", font_size=32).move_to(DOWN * 3.02)
        heights = MathTex(r"h_{\rm top}=\frac43,\quad h_{\rm bottom}=\frac83",
                          font_size=30).move_to(DOWN * 3.89)
        self.play(Write(similar), Write(heights))
        self.play(Indicate(left_tri, color=GREEN_B), Indicate(right_tri, color=GREEN_B))
        wings = MathTex(r"S_{AOD}=S_{BOC}=4", font_size=32, color=GREEN_B).move_to(DOWN * 4.78)
        ratio = MathTex(r"S_{AOB}:S_{COD}=2:8=1:4", font_size=32, color=YELLOW).move_to(DOWN * 5.70)
        self.play(Write(wings), Write(ratio))
        self.wait(2)
