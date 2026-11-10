"""六年级圆的认识：圆心、半径、直径、圆规画法与对称轴。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def circle_measurements(radius):
    """半径和直径的精确关系 d=2r；要求正整数或有理数半径。"""
    from fractions import Fraction

    if type(radius) not in (int, Fraction) or radius <= 0:
        raise ValueError("半径必须为正数且精确表示")
    radius = Fraction(radius)
    return radius, 2 * radius


class Topic001圆的认识Animation(Scene):
    """从圆规的定点、定长旋转引出半径、直径及无穷多条对称轴。"""

    def construct(self):
        assert circle_measurements(2) == (2, 4)
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.compass_circle()
        self.radius_and_diameter()
        self.symmetry()
        self.summary()

    def transition(self):
        self.play(*[
            FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark
        ], run_time=0.3)

    def heading(self, title):
        text = Text(title, font_size=38, color=GOLD).move_to(UP * 5.65)
        self.play(Write(text))
        return text

    def opening(self):
        title = Text("圆的认识", font_size=48).move_to(UP * 3)
        hint = Text("圆心决定位置，半径决定大小", font_size=29, color=BLUE_ACCENT)
        hint.next_to(title, DOWN, buff=0.55)
        self.play(Write(title), FadeIn(hint))
        self.wait(0.7)
        self.transition()

    def compass_circle(self):
        self.heading("圆规画圆：定点、定长")
        center = UP * 0.2
        center_dot = Dot(center, radius=0.10, color=GOLD)
        r = 2.1
        radius_line = Line(center, center + RIGHT * r, color=GOLD, stroke_width=4)
        circle = Circle(radius=r, stroke_color=BLUE_ACCENT, stroke_width=5).move_to(center)
        center_label = MathTex("O", font_size=29).next_to(center_dot, DOWN, buff=0.2)
        tip_label = Text("铅笔沿固定距离旋转一周", font_size=26, color=GREEN_ACCENT)
        tip_label.move_to(DOWN * 3.3)
        self.play(FadeIn(center_dot), Write(center_label), Create(radius_line))
        self.play(
            Create(circle, run_time=2),
            Rotate(radius_line, angle=TAU, about_point=center, rate_func=linear, run_time=2),
        )
        self.play(FadeIn(tip_label))
        self.wait(0.7)
        self.transition()

    def radius_and_diameter(self):
        self.heading("半径 r 与直径 d")
        center = UP * 0.7
        radius = 2.1
        circle = Circle(radius=radius, color=BLUE_ACCENT).move_to(center)
        left = center + LEFT * radius
        right = center + RIGHT * radius
        midpoint = Dot(center, color=GOLD, radius=0.09)
        diameter = Line(left, right, color=GREEN_ACCENT, stroke_width=4)
        radius_line = Line(center, right, color=GOLD, stroke_width=6)
        self.play(Create(circle), FadeIn(midpoint))
        self.play(Create(diameter))
        self.play(Create(radius_line))
        formula = MathTex(r"d=2r,\qquad r=\frac{d}{2}", font_size=46, color=GOLD)
        formula.move_to(DOWN * 3.2)
        explanation = Text("直径通过圆心，等于两条半径", font_size=26)
        explanation.move_to(DOWN * 2.1)
        self.play(Write(formula), FadeIn(explanation))
        self.wait(0.7)
        self.transition()

    def symmetry(self):
        self.heading("圆是轴对称图形")
        circle = Circle(radius=2.0, color=BLUE_ACCENT).move_to(UP * 0.6)
        center = circle.get_center()
        self.play(Create(circle))
        diameters = VGroup(
            DashedLine(center + LEFT * 2.5, center + RIGHT * 2.5, color=GOLD),
            DashedLine(center + UP * 2.5, center + DOWN * 2.5, color=GREEN_ACCENT),
            DashedLine(
                center + (UP + RIGHT) * 1.8,
                center + (DOWN + LEFT) * 1.8,
                color=WHITE
            ),
        )
        for line in diameters:
            self.play(Create(line), run_time=0.55)
        words = Text("每条直径所在的直线都是对称轴", font_size=26)
        words.move_to(DOWN * 3.1)
        count = Text("因此圆有无数条对称轴", font_size=28, color=GOLD)
        count.move_to(DOWN * 4.1)
        self.play(FadeIn(words), FadeIn(count))
        self.wait(0.7)
        self.transition()

    def summary(self):
        self.heading("知识总结")
        rows = VGroup(
            Text("圆心 O：决定圆的位置", font_size=29),
            Text("半径 r：圆心到圆上任一点", font_size=28),
            Text("直径 d：通过圆心，两端在圆上", font_size=27),
            MathTex(r"d=2r", font_size=45, color=GREEN_ACCENT),
            Text("圆有无数条对称轴", font_size=28, color=GOLD),
        ).arrange(DOWN, buff=0.5).move_to(UP * 0.4)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
        self.wait(1)
