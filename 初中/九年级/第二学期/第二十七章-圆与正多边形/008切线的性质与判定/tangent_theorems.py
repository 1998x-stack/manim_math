"""九年级《切线的性质与判定》：性质、判定、切线长定理（七段）。"""
from manim import *
import numpy as np
from tangent_math import tangent_points, verify_tangent_geometry

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TangentTheorems(Scene):
    BLUE_CIRCLE = "#3498db"
    RED_TANGENT = "#e74c3c"
    GREEN_RADIUS = "#2ecc71"
    GOLD_EQUAL = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 0.8, 0.0])
        self.r = 1.8
        self.T = self.O + self.r * RIGHT
        self.P = np.array([3.0, 2.5, 0.0])
        self.A, self.B = (np.array([*v, 0.0]) for v in tangent_points(tuple(self.O[:2]), self.r, tuple(self.P[:2])))
        self.length = verify_tangent_geometry(tuple(self.O[:2]), self.r, tuple(self.P[:2]))
        self.circle = Circle(radius=self.r, color=self.BLUE_CIRCLE, stroke_width=4).move_to(self.O)
        self.scene_1_opening()
        self.scene_2_tangent_property()
        self.scene_3_tangent_criterion()
        self.scene_4_tangent_length_prep()
        self.scene_5_tangent_length_theorem()
        self.scene_6_summary()
        self.scene_7_outro()

    def headline(self, message, color=YELLOW):
        return Text(message, font="sans-serif", font_size=33, color=color).move_to(UP * 5.35)

    def foot_square(self, point, length=0.19):
        # 几何场景中的示例半径指向右侧，切线竖直向上。
        return Polygon(point, point + LEFT * length,
                       point + (LEFT + UP) * length, point + UP * length,
                       color=YELLOW, stroke_width=2, fill_opacity=0)

    def scene_1_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font="sans-serif", font_size=19,
                           color=GRAY_B).move_to(UP * 6.8)
        title = self.headline("一条直线何时是圆的切线？")
        self.center = Dot(self.O, color=WHITE, radius=0.10)
        self.play(FadeIn(self.author), Write(title))
        self.play(Create(self.circle), FadeIn(self.center))
        self.wait(0.7)
        self.play(FadeOut(title))

    def scene_2_tangent_property(self):
        title = self.headline("切线性质：切点处垂直于半径")
        radius = Line(self.O, self.T, color=self.GREEN_RADIUS, stroke_width=4)
        tangent = Line(self.T + DOWN * 2.4, self.T + UP * 2.4, color=self.RED_TANGENT, stroke_width=4)
        mark = Dot(self.T, color=self.GOLD_EQUAL, radius=0.10)
        square = self.foot_square(self.T)
        formula = MathTex(r"OT\perp l", font_size=40).move_to(DOWN * 4.0)
        premise = Text("已知 l 在 T 处与圆相切", font="sans-serif", font_size=24, color=GRAY_A).move_to(DOWN * 5.1)
        self.play(Write(title), Create(radius), Create(tangent))
        self.play(FadeIn(mark), Create(square))
        self.play(Write(formula), FadeIn(premise))
        self.wait(1.1)
        self.play(FadeOut(VGroup(title, radius, tangent, mark, square, formula, premise)))

    def scene_3_tangent_criterion(self):
        title = self.headline("切线判定：过半径外端且与半径垂直")
        radius = Line(self.O, self.T, color=self.GREEN_RADIUS, stroke_width=4)
        tangent = Line(self.T + DOWN * 2.4, self.T + UP * 2.4, color=self.RED_TANGENT, stroke_width=4)
        mark = Dot(self.T, color=self.GOLD_EQUAL, radius=0.10)
        right_angle = self.foot_square(self.T)
        premise = MathTex(r"OT=r,\quad l\perp OT\ \text{ at }\ T", font_size=29).move_to(DOWN * 4.0)
        conclusion = Text("T 在圆上，l 过 T，所以 l 是圆的切线", font="sans-serif",
                          font_size=23, color=YELLOW).move_to(DOWN * 5.2)
        self.play(Write(title), Create(radius), FadeIn(mark))
        self.play(Create(tangent), Create(right_angle))
        self.play(Write(premise), FadeIn(conclusion))
        self.wait(1.1)
        self.play(FadeOut(VGroup(title, radius, tangent, mark, right_angle, premise, conclusion)))

    def scene_4_tangent_length_prep(self):
        title = self.headline("从圆外一点 P 引出两条切线")
        point = Dot(self.P, color=self.GOLD_EQUAL, radius=0.11)
        label = MathTex("P", font_size=28).next_to(point, UR, buff=0.12)
        center_line = DashedLine(self.O, self.P, color=GRAY_A, dash_length=0.12)
        hint = Text("P 在圆外，可以引出两条切线", font="sans-serif", font_size=26, color=GRAY_A).move_to(DOWN * 4.5)
        self.play(Write(title), FadeIn(point), Write(label))
        self.play(Create(center_line), FadeIn(hint))
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(hint))
        self.external_group = VGroup(point, label, center_line)

    def scene_5_tangent_length_theorem(self):
        title = self.headline("切线长定理：PA = PB")
        tangent_a = Line(self.P, self.A, color=self.RED_TANGENT, stroke_width=4)
        tangent_b = Line(self.P, self.B, color=self.RED_TANGENT, stroke_width=4)
        radius_a = Line(self.O, self.A, color=self.GREEN_RADIUS, stroke_width=3)
        radius_b = Line(self.O, self.B, color=self.GREEN_RADIUS, stroke_width=3)
        dots = VGroup(Dot(self.A, color=YELLOW), Dot(self.B, color=YELLOW))
        labels = VGroup(MathTex("A", font_size=25).next_to(dots[0], LEFT, buff=0.12),
                        MathTex("B", font_size=25).next_to(dots[1], DOWN, buff=0.12))
        step1 = MathTex(r"OA\perp PA,\quad OB\perp PB", font_size=29).move_to(DOWN * 3.55)
        step2 = MathTex(r"OA=OB=r,\quad OP=OP", font_size=29).move_to(DOWN * 4.45)
        step3 = MathTex(r"\triangle OAP\cong\triangle OBP\quad(RHS)", font_size=29).move_to(DOWN * 5.35)
        result = MathTex(rf"PA=PB=\sqrt{{OP^2-r^2}}\approx {self.length:.2f}", font_size=30,
                         color=self.GOLD_EQUAL).move_to(DOWN * 6.2)
        self.play(Write(title), Create(tangent_a), Create(tangent_b))
        self.play(Create(radius_a), Create(radius_b), FadeIn(dots), FadeIn(labels))
        self.play(Write(step1))
        self.play(Write(step2))
        self.play(Write(step3))
        self.play(Write(result))
        self.wait(1.4)
        self.play(FadeOut(VGroup(title, tangent_a, tangent_b, radius_a, radius_b,
                                 dots, labels, step1, step2, step3, result, self.external_group)))

    def scene_6_summary(self):
        self.play(FadeOut(self.circle), FadeOut(self.center))
        title = self.headline("三个切线结论")
        self.play(Write(title))
        cards = VGroup()
        for y, message in ((2.5, "性质：切线垂直于切点处半径"),
                           (0.5, "判定：经过半径外端且垂直"),
                           (-1.5, "切线长：同一外点引出的两段相等")):
            card = Text(message, font="sans-serif", font_size=25, color=WHITE).move_to(UP * y)
            cards.add(card)
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(cards), FadeOut(title))

    def scene_7_outro(self):
        outro = Text("用垂直关系识别切线", font="sans-serif", font_size=34,
                     color=YELLOW).move_to(UP * 0.3)
        self.play(Write(outro))
        self.wait(0.7)
        self.play(FadeOut(outro), FadeOut(self.author))


# manim -ql tangent_theorems.py TangentTheorems
