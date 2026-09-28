"""《圆的确定》：用实际垂直平分线构造三点的唯一外接圆。"""

from math import hypot

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def circumcenter_xy(a, b, c):
    """不共线三点的唯一外心；重合、共线或病态近共线时明确拒绝。"""
    bx, by = b[0] - a[0], b[1] - a[1]
    cx, cy = c[0] - a[0], c[1] - a[1]
    squared_b = bx * bx + by * by
    squared_c = cx * cx + cy * cy
    squared_bc = (bx - cx) ** 2 + (by - cy) ** 2
    scale = max(squared_b, squared_c, squared_bc)
    determinant = 2 * (bx * cy - by * cx)
    if not scale or abs(determinant) <= 1e-10 * scale:
        raise ValueError("三点共线或过于接近共线，不能确定唯一外接圆")
    ux = (cy * squared_b - by * squared_c) / determinant
    uy = (bx * squared_c - cx * squared_b) / determinant
    return a[0] + ux, a[1] + uy


def verify_circumcircle(a, b, c):
    """与场景共用的数学规格：等距且在 AB、BC 两条中垂线上。"""
    o = circumcenter_xy(a, b, c)
    radius = hypot(o[0] - a[0], o[1] - a[1])
    if radius <= 0:
        raise ValueError("外接圆半径必须为正")
    for p in (b, c):
        if abs(hypot(o[0] - p[0], o[1] - p[1]) - radius) > 1e-8 * radius:
            raise ArithmeticError("外心到三个顶点距离不相等")
    for p, q in ((a, b), (b, c)):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dot = (o[0] - mx) * (q[0] - p[0]) + (o[1] - my) * (q[1] - p[1])
        if abs(dot) > 1e-8 * radius * hypot(q[0] - p[0], q[1] - p[1]):
            raise ArithmeticError("外心不在边的垂直平分线上")
    return o, radius


class CircleDetermination(Scene):
    """保留原 Scene 入口和八段教学顺序。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.blue, self.red, self.orange = "#3498db", "#e74c3c", "#f39c12"
        self.green, self.purple = "#2ecc71", "#9b59b6"
        self.A = np.array([-2.125, 1.5, 0])
        self.B = np.array([2.125, 0.65, 0])
        self.C = np.array([0, 3.625, 0])
        (ox, oy), self.radius = verify_circumcircle(self.A[:2], self.B[:2], self.C[:2])
        self.O = np.array([ox, oy, 0])
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 6.65)
        self.show_opening()
        self.show_collinear_check()
        self.show_non_collinear()
        self.show_perpendicular_bisector_AB()
        self.show_perpendicular_bisector_BC()
        self.show_circumcenter()
        self.show_circumcircle()
        self.show_summary()

    def _title(self, text, color=YELLOW):
        return Text(text, font_size=33, color=color).move_to(UP * 5.45)

    def _caption(self, text, y=-4.6):
        return Text(text, font_size=24, color=GRAY_A).move_to(UP * y)

    def _bisector(self, p, q, color):
        midpoint = (p + q) / 2
        side = q - p
        length = np.linalg.norm(side)
        if length <= 1e-10:
            raise ValueError("不能为零长度线段画垂直平分线")
        normal = np.array([-side[1], side[0], 0]) / length
        # 保证显示的有限虚线线段覆盖外心，不能让外心落在虚线的延长线上。
        half = max(1.9, abs(np.dot(self.O - midpoint, normal)) + 0.4)
        start, end = midpoint - half * normal, midpoint + half * normal
        return DashedLine(start, end, color=color, dash_length=0.11,
                          stroke_width=3), midpoint, start

    def show_opening(self):
        self.hook = self._title("三个点，能确定一个圆吗？")
        self.dot_A = Dot(LEFT * 2 + UP * 1.0, color=WHITE, radius=0.095)
        self.dot_B = Dot(RIGHT * 2 + UP * 0.5, color=WHITE, radius=0.095)
        self.dot_C = Dot(UP * 3, color=WHITE, radius=0.095)
        self.play(FadeIn(self.author), Write(self.hook), run_time=0.7)
        self.play(FadeIn(self.dot_A), FadeIn(self.dot_B), FadeIn(self.dot_C), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(self.hook), run_time=0.4)

    def show_collinear_check(self):
        title = self._title("反例：三个不同的点共线")
        col_a, col_b, col_c = LEFT * 2.7 + UP, UP, RIGHT * 2.7 + UP
        self.play(Write(title), self.dot_A.animate.move_to(col_a),
                  self.dot_B.animate.move_to(col_b), self.dot_C.animate.move_to(col_c),
                  run_time=1.0)
        line = Line(col_a, col_c, color=GRAY_B, stroke_width=3)
        caption = self._caption("不存在同时经过这三个不同点的圆")
        self.play(Create(line), FadeIn(caption), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(line), FadeOut(caption), run_time=0.5)

    def show_non_collinear(self):
        title = self._title("条件：三个点不在同一直线上")
        self.play(Write(title), self.dot_A.animate.move_to(self.A),
                  self.dot_B.animate.move_to(self.B), self.dot_C.animate.move_to(self.C),
                  run_time=1.0)
        self.triangle = Polygon(self.A, self.B, self.C, color=self.blue,
                                stroke_width=3, fill_opacity=0)
        self.vertex_labels = VGroup(
            Text("A", font_size=23).next_to(self.dot_A, LEFT, buff=0.16),
            Text("B", font_size=23).next_to(self.dot_B, RIGHT, buff=0.16),
            Text("C", font_size=23).next_to(self.dot_C, UP, buff=0.16),
        )
        self.play(Create(self.triangle), FadeIn(self.vertex_labels), run_time=1.0)
        self.play(FadeOut(title), run_time=0.4)

    def show_perpendicular_bisector_AB(self):
        self.construction_title = self._title("先画 AB 的垂直平分线", self.green)
        self.bisector_AB, m, start = self._bisector(self.A, self.B, self.green)
        self.midpoint_M = Dot(m, color=WHITE, radius=0.085)
        self.label_M = Text("M", font_size=20).next_to(self.midpoint_M, DOWN, buff=0.14)
        self.mark_AB = RightAngle(Line(m, self.A), Line(m, start),
                                  length=0.16, color=YELLOW)
        caption = self._caption("中垂线上的点到 A、B 的距离相等")
        self.play(Write(self.construction_title), FadeIn(self.midpoint_M),
                  FadeIn(self.label_M), run_time=0.7)
        self.play(Create(self.bisector_AB), FadeIn(self.mark_AB), FadeIn(caption),
                  run_time=1.0)
        self.wait(0.7)
        self.play(FadeOut(caption), run_time=0.4)

    def show_perpendicular_bisector_BC(self):
        title = self._title("再画 BC 的垂直平分线", self.green)
        self.bisector_BC, n, start = self._bisector(self.B, self.C, self.green)
        self.midpoint_N = Dot(n, color=WHITE, radius=0.085)
        self.label_N = Text("N", font_size=20).next_to(self.midpoint_N, RIGHT, buff=0.14)
        self.mark_BC = RightAngle(Line(n, self.B), Line(n, start),
                                  length=0.16, color=YELLOW)
        self.play(FadeOut(self.construction_title), Write(title), run_time=0.5)
        self.play(FadeIn(self.midpoint_N), FadeIn(self.label_N),
                  Create(self.bisector_BC), FadeIn(self.mark_BC), run_time=1.0)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(self.label_M), FadeOut(self.label_N),
                  FadeOut(self.mark_AB), FadeOut(self.mark_BC), run_time=0.5)

    def show_circumcenter(self):
        title = self._title("两条中垂线相交于外心 O", self.orange)
        self.center_dot = Dot(self.O, radius=0.12, color=self.orange)
        self.center_label = Text("O", font_size=25, color=self.orange).next_to(
            self.center_dot, DOWN + RIGHT, buff=0.12)
        self.radii = VGroup(*[DashedLine(self.O, vertex, color=self.purple,
                                         dash_length=0.1, stroke_width=2)
                              for vertex in (self.A, self.B, self.C)])
        formula = MathTex(r"OA=OB=OC", font_size=33).move_to(DOWN * 3.7)
        self.play(Write(title), FadeIn(self.center_dot), FadeIn(self.center_label),
                  run_time=0.7)
        self.play(*[Create(line) for line in self.radii], run_time=1.0)
        self.play(FadeIn(formula), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(self.bisector_AB),
                  FadeOut(self.bisector_BC), FadeOut(self.midpoint_M),
                  FadeOut(self.midpoint_N), run_time=0.6)

    def show_circumcircle(self):
        title = self._title("以 O 为圆心、OA 为半径作圆", self.red)
        self.circumcircle = Circle(radius=self.radius, color=self.red,
                                   stroke_width=4).move_to(self.O)
        result = self._caption("这个圆经过 A、B、C，叫作三角形的外接圆")
        theorem = Text("不在同一直线上的三点确定一个圆",
                       font_size=28, color=YELLOW).move_to(DOWN * 3.5)
        self.play(Write(title), Create(self.circumcircle), run_time=1.3)
        self.play(FadeIn(result), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(result), FadeIn(theorem), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(theorem), FadeOut(self.radii), run_time=0.6)

    def show_summary(self):
        diagram = VGroup(self.triangle, self.circumcircle, self.dot_A,
                         self.dot_B, self.dot_C, self.vertex_labels,
                         self.center_dot, self.center_label)
        self.play(diagram.animate.scale(0.46).move_to(UP * 4.25), run_time=0.9)
        entries = (("条件", "三个不同的点不共线"),
                   ("作图", "连接两边，作垂直平分线"),
                   ("外心", "两条中垂线交点，OA=OB=OC"))
        cards = VGroup()
        for i, (name, detail) in enumerate(entries):
            card = VGroup(Dot(radius=0.11, color=self.green),
                          Text(name, font_size=26, color=WHITE),
                          Text(detail, font_size=23, color=GRAY_A))
            card.arrange(RIGHT, buff=0.17).move_to(UP * (1.95 - 1.55 * i))
            cards.add(card)
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.5)
        end = Text("外心是三角形三边垂直平分线的交点",
                   font_size=26, color=YELLOW).move_to(DOWN * 4.4)
        self.play(FadeIn(end), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(diagram), FadeOut(cards), FadeOut(end),
                  FadeOut(self.author), run_time=0.8)
