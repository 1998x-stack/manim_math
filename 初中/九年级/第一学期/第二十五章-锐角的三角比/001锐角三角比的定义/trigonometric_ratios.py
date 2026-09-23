"""九年级：锐角三角比的定义（Manim Community Edition）。

统一的几何约定：C 为直角顶点，A 为目标锐角；BC=a（A 的对边）、
CA=b（A 的邻边）、AB=c（斜边）。数学数值由同一份几何参数计算。
"""

from manim import *
import math
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TrigonometricRatios(Scene):
    FONT = "PingFang SC"
    BG = "#1a1a2e"
    OPP_COLOR = "#e74c3c"
    ADJ_COLOR = "#3498db"
    HYP_COLOR = "#2ecc71"
    ACCENT = "#f39c12"

    def construct(self):
        self.camera.background_color = self.BG
        self.setup_geometry()
        self.show_opening()
        self.show_three_sides()
        self.show_sine_definition()
        self.show_cosine_definition()
        self.show_tangent_definition()
        self.show_invariance()
        self.show_summary()
        self.show_outro()

    def setup_geometry(self):
        self.angle_A_value = math.radians(35)
        self.adjacent = 3.0
        self.opposite = self.adjacent * math.tan(self.angle_A_value)
        self.hypotenuse = math.hypot(self.adjacent, self.opposite)
        self.sin_A = self.opposite / self.hypotenuse
        self.cos_A = self.adjacent / self.hypotenuse
        self.tan_A = self.opposite / self.adjacent
        self.verify_geometry()
        self.diagram, self.sides = self.make_triangle(scale=1.0, center=UP * 0.9)

    def verify_geometry(self):
        """在渲染前失败，而非仅打印数学不一致警告。"""
        assert 0 < self.angle_A_value < math.pi / 2
        assert self.adjacent > 0 and self.opposite > 0
        assert math.isclose(
            self.hypotenuse**2,
            self.adjacent**2 + self.opposite**2,
            rel_tol=1e-12,
        )
        assert math.isclose(self.sin_A, math.sin(self.angle_A_value), rel_tol=1e-12)
        assert math.isclose(self.cos_A, math.cos(self.angle_A_value), rel_tol=1e-12)
        assert math.isclose(self.tan_A, math.tan(self.angle_A_value), rel_tol=1e-12)

    def make_triangle(self, scale=1.0, center=ORIGIN):
        """返回以 C 为直角顶点、A 为 35° 锐角的相似直角三角形。"""
        c = np.array([-self.opposite / 2, -self.adjacent / 2, 0.0]) * scale
        b = c + RIGHT * self.opposite * scale
        a = c + UP * self.adjacent * scale
        opposite_line = Line(c, b, color=self.OPP_COLOR, stroke_width=5)
        adjacent_line = Line(c, a, color=self.ADJ_COLOR, stroke_width=5)
        hypotenuse_line = Line(a, b, color=self.HYP_COLOR, stroke_width=5)
        right_mark = RightAngle(
            Line(c, b), Line(c, a), length=0.22 * scale,
            quadrant=(1, 1), color=YELLOW,
        )
        angle_mark = Angle.from_three_points(b, a, c, radius=0.37 * scale,
                                             color=self.ACCENT)
        labels = VGroup(
            MathTex("A", font_size=25 * scale).next_to(a, UP + LEFT, buff=0.1),
            MathTex("B", font_size=25 * scale).next_to(b, DOWN + RIGHT, buff=0.1),
            MathTex("C", font_size=25 * scale).next_to(c, DOWN + LEFT, buff=0.1),
            MathTex("a", font_size=26 * scale, color=self.OPP_COLOR)
            .next_to(opposite_line, DOWN, buff=0.13),
            MathTex("b", font_size=26 * scale, color=self.ADJ_COLOR)
            .next_to(adjacent_line, LEFT, buff=0.13),
            MathTex("c", font_size=26 * scale, color=self.HYP_COLOR)
            .next_to(hypotenuse_line, RIGHT, buff=0.13),
        )
        diagram = VGroup(opposite_line, adjacent_line, hypotenuse_line,
                         right_mark, angle_mark, labels)
        diagram.move_to(center)
        return diagram, (opposite_line, adjacent_line, hypotenuse_line)

    def show_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font=self.FONT, font_size=19, color=GRAY_B)
        self.author.move_to(UP * 7.25)
        self.title = Text("锐角三角比", font=self.FONT, font_size=38,
                          color=self.ACCENT).move_to(UP * 5.65)
        subtitle = Text("同一个锐角，如何用边长来表示？", font=self.FONT,
                        font_size=25).move_to(UP * 4.7)
        self.play(FadeIn(self.author), Write(self.title), run_time=0.8)
        self.play(Write(subtitle), Create(self.diagram), run_time=1.3)
        self.wait(0.7)
        self.play(FadeOut(subtitle), run_time=0.4)

    def show_three_sides(self):
        labels = VGroup(
            Text("红色 BC：角 A 的对边 a", font=self.FONT,
                 font_size=23, color=self.OPP_COLOR),
            Text("蓝色 CA：角 A 的邻边 b", font=self.FONT,
                 font_size=23, color=self.ADJ_COLOR),
            Text("绿色 AB：直角 C 的对边（斜边）c", font=self.FONT,
                 font_size=23, color=self.HYP_COLOR),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 3.4)
        self.play(FadeIn(labels, shift=UP * 0.2), run_time=0.7)
        for line in self.sides:
            self.play(Indicate(line), run_time=0.45)
        self.wait(0.4)
        self.play(FadeOut(labels), run_time=0.4)

    def show_ratio(self, name, text, formula, numerical, indices):
        title = Text(name, font=self.FONT, font_size=31,
                     color=self.ACCENT).move_to(UP * 4.75)
        caption = Text(text, font=self.FONT, font_size=24).move_to(DOWN * 2.7)
        symbolic = MathTex(formula, font_size=34).move_to(DOWN * 3.7)
        value = MathTex(numerical, font_size=29,
                        color=YELLOW).move_to(DOWN * 4.65)
        self.play(Write(title), FadeIn(caption), run_time=0.65)
        for index in indices:
            self.play(Indicate(self.sides[index]), run_time=0.4)
        self.play(Write(symbolic), Write(value), run_time=0.9)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(caption), FadeOut(symbolic),
                  FadeOut(value), run_time=0.45)

    def show_sine_definition(self):
        self.show_ratio(
            "正弦 sin A", "正弦 = 对边 ÷ 斜边",
            r"\sin A=\frac{a}{c}",
            rf"\sin 35^\circ\approx {self.sin_A:.3f}", (0, 2),
        )

    def show_cosine_definition(self):
        self.show_ratio(
            "余弦 cos A", "余弦 = 邻边 ÷ 斜边",
            r"\cos A=\frac{b}{c}",
            rf"\cos 35^\circ\approx {self.cos_A:.3f}", (1, 2),
        )

    def show_tangent_definition(self):
        self.show_ratio(
            "正切 tan A", "正切 = 对边 ÷ 邻边",
            r"\tan A=\frac{a}{b}",
            rf"\tan 35^\circ\approx {self.tan_A:.3f}", (0, 1),
        )
        relation = MathTex(r"\tan A=\frac{\sin A}{\cos A}",
                           font_size=30, color=YELLOW).move_to(DOWN * 3.5)
        self.play(Write(relation), run_time=0.7)
        self.wait(0.6)
        self.play(FadeOut(relation), run_time=0.4)

    def show_invariance(self):
        self.play(FadeOut(self.diagram), run_time=0.5)
        small, _ = self.make_triangle(scale=0.65, center=LEFT * 2.1 + UP * 1.1)
        large, _ = self.make_triangle(scale=1.15, center=RIGHT * 1.5 + UP * 1.1)
        note = Text("同角的三角比与三角形的大小无关", font=self.FONT,
                    font_size=24, color=YELLOW).move_to(DOWN * 2.5)
        values = MathTex(
            rf"\sin A\approx {self.sin_A:.3f},\quad"
            rf"\cos A\approx {self.cos_A:.3f},\quad"
            rf"\tan A\approx {self.tan_A:.3f}",
            font_size=22,
        ).move_to(DOWN * 3.55)
        self.play(Create(small), Create(large), run_time=1.0)
        self.play(FadeIn(note), Write(values), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(small), FadeOut(large), FadeOut(note),
                  FadeOut(values), run_time=0.5)

    def show_summary(self):
        formulas = VGroup(
            MathTex(r"\sin A=\frac{a}{c}", font_size=35,
                    color=self.OPP_COLOR),
            MathTex(r"\cos A=\frac{b}{c}", font_size=35,
                    color=self.ADJ_COLOR),
            MathTex(r"\tan A=\frac{a}{b}", font_size=35,
                    color=YELLOW),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.8)
        condition = Text("仅针对直角三角形中的锐角；先确认直角与对边",
                         font=self.FONT, font_size=23).move_to(DOWN * 3.5)
        self.play(FadeIn(formulas), FadeIn(condition), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(formulas), FadeOut(condition),
                  FadeOut(self.title), run_time=0.5)

    def show_outro(self):
        closing = Text("三角比：角确定，比值就确定！", font=self.FONT,
                       font_size=31, color=self.ACCENT)
        closing.move_to(UP * 0.6)
        self.play(Write(closing), run_time=0.8)
        self.wait(1.1)
        self.play(FadeOut(closing), FadeOut(self.author), run_time=0.5)
