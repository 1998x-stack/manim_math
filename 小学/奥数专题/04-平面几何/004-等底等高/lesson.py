"""等底等高：先用对角线把长方形等分，再平移顶点观察面积不变量。"""
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height < 0:
        raise ValueError("positive base and nonnegative height required")
    return base * height / 2


class EqualBaseHeightScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        assert triangle_area(4, 3) == 6
        title = Text("三角形：同底同高面积相等", font=FONT, font_size=35).move_to(UP * 6.25)
        premise = Text("先把长方形从对角线分成两半", font=FONT, font_size=27).move_to(UP * 5.03)
        self.play(Write(title), FadeIn(premise))
        A, B = np.array([-2., -1.5, 0]), np.array([2., -1.5, 0])
        P, Q = np.array([-2., 1.5, 0]), np.array([2., 1.5, 0])
        rectangle = Polygon(A, B, Q, P, color=WHITE, stroke_width=2)
        primary = Polygon(A, B, P, color=BLUE_B, fill_color=BLUE_D, fill_opacity=.65)
        complement = Polygon(B, Q, P, color=YELLOW, fill_color=YELLOW_D, fill_opacity=.5)
        diagonal = Line(B, P, color=WHITE, stroke_width=3)
        self.play(Create(rectangle), FadeIn(primary), FadeIn(complement), Create(diagonal))
        width_label = MathTex(r"b=4", font_size=33).next_to(Line(A, B), DOWN, buff=.25)
        height_label = MathTex(r"h=3", font_size=33).move_to([2.8, 0, 0])
        double_area = MathTex(r"S_{\rm rect}=4\times3=12", font_size=33).move_to(DOWN * 3.1)
        half_area = MathTex(r"S_{\triangle}=12\div2=6", font_size=36, color=YELLOW).move_to(DOWN * 4.1)
        self.play(Write(width_label), Write(height_label), Write(double_area), Write(half_area))
        self.wait(.8)

        # 顶点只沿与 AB 平行的 y=1.5 直线移动；高度不会随顶点 x 坐标改变。
        self.play(FadeOut(VGroup(rectangle, primary, complement, diagonal, double_area, premise)))
        guide = DashedLine([-3.45, 1.5, 0], [3.45, 1.5, 0], color=GREY_B)
        base = Line(A, B, color=BLUE_B, stroke_width=6)
        apex_x = ValueTracker(-2.)
        triangle = always_redraw(lambda: Polygon(A, B, [apex_x.get_value(), 1.5, 0],
                                                  color=YELLOW, fill_color=BLUE_D, fill_opacity=.45))
        altitude = always_redraw(lambda: DashedLine([apex_x.get_value(), 1.5, 0],
                                                    [apex_x.get_value(), -1.5, 0], color=GREEN_B))
        foot = always_redraw(lambda: Dot([apex_x.get_value(), -1.5, 0], color=GREEN_B, radius=.08))
        apex = always_redraw(lambda: Dot([apex_x.get_value(), 1.5, 0], color=YELLOW, radius=.10))
        guide_note = Text("顶点沿平行线移动：高始终是 3", font=FONT, font_size=27).move_to(UP * 4.1)
        self.play(Create(guide), Create(base), FadeIn(triangle, altitude, foot, apex), FadeIn(guide_note))
        self.play(apex_x.animate.set_value(2.), run_time=3, rate_func=linear)
        self.play(apex_x.animate.set_value(.25), run_time=1.6)
        conclusion = Text("底 4、高 3 都没变，面积一直是 6", font=FONT, font_size=26,
                          color=YELLOW).move_to(DOWN * 5.42)
        self.play(FadeIn(conclusion))
        self.wait(2)
