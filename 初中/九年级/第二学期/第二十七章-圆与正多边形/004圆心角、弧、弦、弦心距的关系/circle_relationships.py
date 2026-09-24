"""圆心角、劣弧、弦与弦心距：同圆中的可检验教学示例。"""
import math
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def circle_metrics(radius, theta):
    """返回(劣弧长, 弦长, 弦心距)，0 < theta < pi。"""
    if not (math.isfinite(radius) and math.isfinite(theta)):
        raise ValueError("半径与圆心角必须是有限数")
    if radius <= 0 or not 0 < theta < math.pi:
        raise ValueError("本课示例要求半径为正，且圆心角在(0, pi)内")
    return (radius * theta,
            2 * radius * math.sin(theta / 2),
            radius * math.cos(theta / 2))


class CircleRelationships(Scene):
    """保留八段教学顺序；所有标注均来自同一组实际几何数据。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.R = 2.5
        self.O = np.array([0., 1., 0.])
        self.theta = PI / 3
        self.arc_length, self.chord_length, self.chord_distance = circle_metrics(
            self.R, self.theta)
        self.A = self.on_circle(PI / 2)
        self.B = self.on_circle(PI / 6)
        self.C = self.on_circle(-PI / 6)
        self.D = self.on_circle(-PI / 2)
        self.M = (self.A + self.B) / 2
        self.N = (self.C + self.D) / 2
        self.verify_geometry()
        self.scene_1_opening()
        self.scene_2_introduction()
        self.scene_3_second_group()
        self.scene_4_angle_to_arc()
        self.scene_5_arc_to_chord()
        self.scene_6_chord_to_distance()
        self.scene_7_summary()
        self.scene_8_outro()

    def on_circle(self, angle):
        return self.O + self.R * np.array([math.cos(angle), math.sin(angle), 0])

    def verify_geometry(self):
        eps = 1e-7
        for p in (self.A, self.B, self.C, self.D):
            if not math.isclose(np.linalg.norm(p - self.O), self.R, abs_tol=eps):
                raise ValueError("端点不在圆上")
        for p, q, m in ((self.A, self.B, self.M), (self.C, self.D, self.N)):
            if not math.isclose(np.linalg.norm(p - q), self.chord_length, abs_tol=eps):
                raise ValueError("画出的弦长与标注不符")
            if not math.isclose(np.linalg.norm(m - self.O), self.chord_distance, abs_tol=eps):
                raise ValueError("画出的弦心距与标注不符")
            if not math.isclose(np.dot(p - q, m - self.O), 0, abs_tol=eps):
                raise ValueError("弦心距必须垂直于弦")

    def heading(self, title):
        return Text(title, font_size=32, color=YELLOW).move_to(UP * 6.0)

    def note(self, message):
        return Text(message, font_size=26, color=WHITE).move_to(DOWN * 5.3)

    def scene_1_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 7.1)
        question = self.heading("圆中的四个量，如何相互联系？")
        cue = self.note("先比较同一个圆内的两组劣弧")
        self.play(FadeIn(self.author), Write(question), run_time=1)
        self.play(FadeIn(cue), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(question), FadeOut(cue))

    def scene_2_introduction(self):
        title = self.heading("第一组：圆心角、劣弧、弦、弦心距")
        self.circle = Circle(radius=self.R, color=BLUE, stroke_width=3).move_to(self.O)
        self.center = Dot(self.O, color=RED)
        self.radii_1 = VGroup(Line(self.O, self.A), Line(self.O, self.B))
        self.arc_1 = Arc(radius=self.R, start_angle=PI/6, angle=self.theta,
                         arc_center=self.O, color=GREEN, stroke_width=6)
        self.chord_1 = Line(self.A, self.B, color=ORANGE, stroke_width=5)
        self.dist_1 = DashedLine(self.O, self.M, color=YELLOW, dash_length=0.10)
        self.angle_1 = Arc(radius=0.5, start_angle=PI/6, angle=self.theta,
                           arc_center=self.O, color=RED, stroke_width=4)
        self.points_1 = VGroup(Dot(self.A), Dot(self.B), Dot(self.M, color=YELLOW))
        self.labels_1 = VGroup(MathTex("A").next_to(self.A, UP),
                               MathTex("B").next_to(self.B, RIGHT),
                               MathTex("M").next_to(self.M, UP),
                               MathTex("O").next_to(self.O, LEFT))
        self.diagram = VGroup(self.circle, self.center, self.radii_1,
                              self.arc_1, self.chord_1, self.dist_1,
                              self.angle_1, self.points_1, self.labels_1)
        self.play(Write(title), Create(self.circle), FadeIn(self.center))
        self.play(Create(self.radii_1), Create(self.angle_1), FadeIn(self.points_1))
        self.play(Create(self.arc_1), Create(self.chord_1), Create(self.dist_1),
                  FadeIn(self.labels_1))
        explanation = self.note("OM 垂直于弦 AB；M 是弦 AB 的中点")
        self.play(FadeIn(explanation))
        self.wait(1)
        self.play(FadeOut(explanation), FadeOut(title))

    def scene_3_second_group(self):
        title = self.heading("第二组：取相等的圆心角")
        self.radii_2 = VGroup(Line(self.O, self.C), Line(self.O, self.D))
        self.arc_2 = Arc(radius=self.R, start_angle=-PI/2, angle=self.theta,
                         arc_center=self.O, color=PURPLE, stroke_width=6)
        self.chord_2 = Line(self.C, self.D, color=TEAL, stroke_width=5)
        self.dist_2 = DashedLine(self.O, self.N, color=YELLOW, dash_length=0.10)
        self.angle_2 = Arc(radius=0.5, start_angle=-PI/2, angle=self.theta,
                           arc_center=self.O, color=RED, stroke_width=4)
        self.points_2 = VGroup(Dot(self.C), Dot(self.D), Dot(self.N, color=YELLOW))
        self.labels_2 = VGroup(MathTex("C").next_to(self.C, RIGHT),
                               MathTex("D").next_to(self.D, DOWN),
                               MathTex("N").next_to(self.N, DOWN))
        self.play(Write(title))
        self.play(Create(self.radii_2), Create(self.angle_2), FadeIn(self.points_2))
        self.play(Create(self.arc_2), Create(self.chord_2), Create(self.dist_2),
                  FadeIn(self.labels_2))
        self.diagram.add(self.radii_2, self.arc_2, self.chord_2, self.dist_2,
                         self.angle_2, self.points_2, self.labels_2)
        self.play(FadeOut(title))

    def scene_4_angle_to_arc(self):
        title = self.heading("① 圆心角相等 → 对应劣弧相等")
        formula = MathTex(r"\angle AOB=\angle COD=60^{\circ}",
                          font_size=32).move_to(DOWN * 4.45)
        arc_text = self.note(f"两条劣弧长均为 {self.arc_length:.2f}（同一长度单位）")
        self.play(Write(title), Write(formula))
        self.play(Indicate(self.angle_1), Indicate(self.angle_2),
                  Indicate(self.arc_1), Indicate(self.arc_2))
        self.play(FadeIn(arc_text))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(arc_text))

    def scene_5_arc_to_chord(self):
        title = self.heading("② 劣弧相等 → 所对弦相等")
        formula = MathTex(r"AB=CD=2R\sin(30^{\circ})",
                          font_size=32).move_to(DOWN * 4.4)
        result = self.note(f"两条弦长均为 {self.chord_length:.2f}（同一长度单位）")
        self.play(Write(title), Write(formula))
        self.play(Indicate(self.arc_1), Indicate(self.arc_2),
                  Indicate(self.chord_1), Indicate(self.chord_2))
        self.play(FadeIn(result))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(result))

    def scene_6_chord_to_distance(self):
        title = self.heading("③ 弦相等 → 弦心距相等")
        formula = MathTex(r"OM=ON=R\cos(30^{\circ})",
                          font_size=32).move_to(DOWN * 4.4)
        result = self.note(f"两条弦心距均为 {self.chord_distance:.2f}（同一长度单位）")
        self.play(Write(title), Write(formula))
        self.play(Indicate(self.chord_1), Indicate(self.chord_2),
                  Indicate(self.dist_1), Indicate(self.dist_2))
        self.play(FadeIn(result))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(result))

    def scene_7_summary(self):
        self.play(self.diagram.animate.scale(0.55).move_to(UP * 3.0), run_time=1)
        title = self.heading("同圆或等圆：四个量相互对应")
        lines = VGroup(
            Text("圆心角相等 ⇔ 对应劣弧相等", font_size=27),
            Text("⇔ 所对弦相等 ⇔ 弦心距相等", font_size=27),
            Text("约定比较的是 0° 与 180° 之间的圆心角", font_size=23, color=YELLOW),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 1.6)
        self.play(Write(title), FadeIn(lines))
        self.wait(2)
        self.play(FadeOut(self.diagram), FadeOut(title), FadeOut(lines))

    def scene_8_outro(self):
        ending = Text("圆心角 · 弧 · 弦 · 弦心距", font_size=34, color=YELLOW)
        self.play(FadeIn(ending))
        self.wait(1)
        self.play(FadeOut(ending), FadeOut(self.author))
