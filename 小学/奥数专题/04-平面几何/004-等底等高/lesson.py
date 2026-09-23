"""等底等高的三角形：顶点沿与底边平行的直线移动，面积不变。"""
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height < 0:
        raise ValueError("positive base and nonnegative height required")
    return base * height / 2


class EqualBaseHeightScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        assert triangle_area(6, 4) == 12
        title = Text("等底等高，面积相等", font=FONT, font_size=36).move_to(UP * 6.2)
        given = Text("底边固定，顶点可以左右移动吗？", font=FONT, font_size=28).move_to(UP * 4.9)
        self.play(Write(title), FadeIn(given))
        left, right = np.array([-3.0, -2.0, 0]), np.array([3.0, -2.0, 0])
        x = ValueTracker(-2.5)
        top_line = DashedLine([-3.3, 2.0, 0], [3.3, 2.0, 0], color=GREY_B)
        base = Line(left, right, color=BLUE_B, stroke_width=7)
        triangle = always_redraw(lambda: Polygon(left, right, [x.get_value(), 2.0, 0], color=YELLOW, fill_color=BLUE_D, fill_opacity=0.28))
        altitude = always_redraw(lambda: DashedLine([x.get_value(), 2.0, 0], [x.get_value(), -2.0, 0], color=GREEN_B))
        apex = always_redraw(lambda: Dot([x.get_value(), 2.0, 0], color=YELLOW))
        self.play(Create(base), Create(top_line), Create(triangle), Create(altitude), FadeIn(apex))
        lengths = MathTex(r"b=6\qquad h=4", font_size=34).move_to(DOWN * 3.15)
        result = MathTex(r"S=\frac{6\times4}{2}=12", font_size=40, color=YELLOW).move_to(DOWN * 4.35)
        self.play(Write(lengths), Write(result))
        self.play(x.animate.set_value(2.5), run_time=3, rate_func=linear)
        conclusion = Text("形状在变，底和高不变，面积也不变", font=FONT, font_size=27).move_to(DOWN * 5.65)
        self.play(FadeIn(conclusion))
        self.wait(2)
