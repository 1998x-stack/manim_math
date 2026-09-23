"""圆周角定理：用同一组精确点验证图形、公式与教学结论。"""
import math
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def point(degrees, radius=1.0):
    if not math.isfinite(degrees) or not math.isfinite(radius) or radius <= 0:
        raise ValueError("角度与正半径须为有限数")
    angle = math.radians(degrees)
    return (radius * math.cos(angle), radius * math.sin(angle))


def angle_at(a, vertex, b):
    u = (a[0] - vertex[0], a[1] - vertex[1])
    v = (b[0] - vertex[0], b[1] - vertex[1])
    if math.hypot(*u) < 1e-10 or math.hypot(*v) < 1e-10:
        raise ValueError("顶点不得与角的端点重合")
    return math.atan2(abs(u[0] * v[1] - u[1] * v[0]), u[0] * v[0] + u[1] * v[1])


def check_inscribed_example():
    o = (0., 0.)
    a, b = point(30), point(150)
    p, q, other_side = point(240), point(290), point(90)
    center = angle_at(a, o, b)
    first, second = angle_at(a, p, b), angle_at(a, q, b)
    if not (math.isclose(center, 2 * first, abs_tol=1e-8)
            and math.isclose(first, second, abs_tol=1e-8)
            and math.isclose(first + angle_at(a, other_side, b), math.pi, abs_tol=1e-8)):
        raise ValueError("圆周角关系与实际点位不符")
    da, db, c = point(0), point(180), point(90)
    if not math.isclose(angle_at(da, c, db), math.pi / 2, abs_tol=1e-8):
        raise ValueError("直径对应圆周角应为 90°")
    return center, first, second


class InscribedAngleTheorem(Scene):
    """八段场景：定义、圆心角、定理、同弧、直径及其逆向结论。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.radius = 2.0
        self.O = np.array([0., 1., 0.])
        self.A, self.B, self.P, self.Q = (self.at(t) for t in (30, 150, 240, 290))
        self.center_angle, self.p_angle, self.q_angle = check_inscribed_example()
        self.geometry = VGroup()
        self.show_opening()
        self.show_inscribed_angle_definition()
        self.show_central_angle()
        self.show_main_theorem()
        self.show_corollary_1()
        self.show_corollary_2()
        self.show_corollary_3()
        self.show_summary()

    def at(self, degrees):
        return self.O + np.array([*point(degrees, self.radius), 0.])

    def heading(self, value):
        return Text(value, font_size=31, color=YELLOW).move_to(UP * 5.7)

    def note(self, value):
        return Text(value, font_size=25).move_to(DOWN * 4.8)

    def show_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 7.0)
        title = self.heading("圆上的角，与圆心角有什么关系？")
        self.circle = Circle(radius=self.radius, color=BLUE).move_to(self.O)
        self.geometry.add(self.circle)
        self.play(FadeIn(self.author), Write(title), Create(self.circle))
        self.wait(0.6)
        self.play(FadeOut(title))

    def show_inscribed_angle_definition(self):
        title = self.heading("圆周角：顶点在圆上，两边与圆相交")
        self.chords = VGroup(Line(self.P, self.A, color=RED),
                             Line(self.P, self.B, color=RED))
        self.points = VGroup(Dot(self.A), Dot(self.B), Dot(self.P, color=RED))
        self.point_labels = VGroup(MathTex("A").next_to(self.A, RIGHT),
                                   MathTex("B").next_to(self.B, LEFT),
                                   MathTex("P").next_to(self.P, DOWN))
        self.geometry.add(self.chords, self.points, self.point_labels)
        self.play(Write(title), Create(self.chords), FadeIn(self.points),
                  FadeIn(self.point_labels))
        self.wait(1)
        self.play(FadeOut(title))

    def show_central_angle(self):
        title = self.heading("圆心角和圆周角对着同一条劣弧 AB")
        self.radii = VGroup(Line(self.O, self.A, color=ORANGE),
                            Line(self.O, self.B, color=ORANGE))
        self.center_dot = Dot(self.O, color=ORANGE)
        self.minor_arc = Arc(radius=self.radius, start_angle=PI/6,
                             angle=2*PI/3, arc_center=self.O,
                             color=PURPLE, stroke_width=6)
        self.geometry.add(self.radii, self.center_dot, self.minor_arc)
        self.play(Write(title), Create(self.radii), FadeIn(self.center_dot),
                  Create(self.minor_arc))
        self.wait(1)
        self.play(FadeOut(title))

    def show_main_theorem(self):
        title = self.heading("圆周角等于同弧所对圆心角的一半")
        equation = MathTex(r"\angle APB=\frac12\angle AOB",
                           font_size=36).move_to(DOWN * 3.7)
        values = self.note(f"{math.degrees(self.p_angle):.0f}° = {math.degrees(self.center_angle):.0f}° ÷ 2")
        self.play(Write(title), Write(equation))
        self.play(Indicate(self.chords), Indicate(self.radii),
                  Indicate(self.minor_arc), FadeIn(values))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(equation), FadeOut(values))

    def show_corollary_1(self):
        title = self.heading("同一条弧所对的圆周角相等")
        q_lines = VGroup(Line(self.Q, self.A, color=TEAL),
                         Line(self.Q, self.B, color=TEAL))
        q_dot = Dot(self.Q, color=TEAL)
        q_label = MathTex("Q").next_to(self.Q, DOWN)
        q_group = VGroup(q_lines, q_dot, q_label)
        formula = MathTex(r"\angle APB=\angle AQB=60^{\circ}",
                          font_size=32).move_to(DOWN * 3.7)
        caution = self.note("P、Q 均在劣弧 AB 以外的同一段圆弧上")
        self.play(Write(title), Create(q_lines), FadeIn(q_dot), FadeIn(q_label))
        self.play(Write(formula), FadeIn(caution), Indicate(self.minor_arc))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(caution), FadeOut(q_group))

    def show_corollary_2(self):
        self.play(FadeOut(self.geometry))
        title = self.heading("直径所对的圆周角是直角")
        self.end_a, self.end_b, self.C = (self.at(t) for t in (0, 180, 90))
        self.diameter_circle = Circle(radius=self.radius, color=BLUE).move_to(self.O)
        self.diameter = Line(self.end_a, self.end_b, color=GREEN, stroke_width=5)
        self.diameter_rays = VGroup(Line(self.C, self.end_a, color=RED),
                                    Line(self.C, self.end_b, color=RED))
        self.diameter_points = VGroup(Dot(self.end_a), Dot(self.end_b), Dot(self.C))
        self.diameter_labels = VGroup(MathTex("A").next_to(self.end_a, RIGHT),
                                      MathTex("B").next_to(self.end_b, LEFT),
                                      MathTex("C").next_to(self.C, UP))
        self.diameter_group = VGroup(self.diameter_circle, self.diameter,
                                     self.diameter_rays, self.diameter_points,
                                     self.diameter_labels)
        equation = MathTex(r"\angle ACB=90^{\circ}", font_size=34).move_to(DOWN * 4.3)
        self.play(Write(title), Create(self.diameter_circle), Create(self.diameter))
        self.play(Create(self.diameter_rays), FadeIn(self.diameter_points),
                  FadeIn(self.diameter_labels), Write(equation))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(equation))

    def show_corollary_3(self):
        title = self.heading("逆向推论：直角圆周角所对的弦是直径")
        center = Dot(self.O, color=ORANGE)
        label = MathTex("O").next_to(self.O, DOWN)
        formula = MathTex(r"\angle ACB=90^{\circ}\Rightarrow\angle AOB=180^{\circ}",
                          font_size=28).move_to(DOWN * 4.3)
        self.diameter_group.add(center, label)
        self.play(Write(title), FadeIn(center), FadeIn(label), Write(formula))
        self.play(Indicate(self.diameter, color=YELLOW))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(formula))

    def show_summary(self):
        self.play(FadeOut(self.diameter_group))
        title = self.heading("圆周角定理 · 三条核心结论")
        cards = VGroup(
            Text("同弧：圆周角 = 圆心角的一半", font_size=29),
            Text("同弧所对圆周角相等（顶点位于同侧圆弧）", font_size=25),
            Text("直径 ⇔ 所对圆周角为 90°", font_size=29),
        ).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        self.play(Write(title))
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(cards), FadeOut(title), FadeOut(self.author))
