"""九年级《圆的定义与基本概念》：9:16 教学动画。

修复要点：数学前提可验证；动画仅清理实际在屏幕上的对象；总结卡片确实入场。
"""

from math import cos, hypot, radians, sin

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def circle_point_xy(cx, cy, radius, angle_degrees):
    """返回圆上的点；半径必须为正。独立于 Manim，可单元测试。"""
    if radius <= 0:
        raise ValueError("圆的半径必须大于零")
    theta = radians(angle_degrees)
    return (cx + radius * cos(theta), cy + radius * sin(theta))


def verify_circle_geometry(cx, cy, radius):
    """验证各教学点、直径、非直径弦及两段弧。失败时中止场景。"""
    points = {name: circle_point_xy(cx, cy, radius, angle)
              for name, angle in (("A", 0), ("B", 60), ("C", 150), ("D", 180))}
    tol = 1e-9
    for x, y in points.values():
        assert abs(hypot(x - cx, y - cy) - radius) < tol
    ax, ay = points["A"]
    dx, dy = points["D"]
    assert abs(hypot(ax - dx, ay - dy) - 2 * radius) < tol
    assert abs((ax + dx) / 2 - cx) < tol
    assert abs((ay + dy) / 2 - cy) < tol
    bx, by = points["B"]
    ex, ey = points["C"]
    assert 0 < hypot(bx - ex, by - ey) < 2 * radius
    assert 0 < 150 - 60 < 180 < 360 - (150 - 60)
    return points


class CircleBasicConcepts(Scene):
    """保留原 Scene 入口和七段教学顺序。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 1.0, 0.0])
        self.radius = 1.8
        xy = verify_circle_geometry(self.O[0], self.O[1], self.radius)
        self.points = {name: np.array([*point, 0.0]) for name, point in xy.items()}
        self.blue, self.red, self.orange = "#3498db", "#e74c3c", "#f39c12"
        self.green, self.purple = "#2ecc71", "#9b59b6"
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 6.65)
        self.circle = Circle(radius=self.radius, color=self.blue,
                             stroke_width=4).move_to(self.O)
        self.center_dot = Dot(self.O, radius=0.10, color=self.red)
        self.show_opening()
        self.show_definition()
        self.show_radius()
        self.show_diameter()
        self.show_chord()
        self.show_arc()
        self.show_summary()

    def point_on_circle(self, angle):
        return np.array([*circle_point_xy(*self.O[:2], self.radius, angle), 0.0])

    def _title(self, name, color=GOLD):
        return Text(name, font_size=35, color=color).move_to(UP * 5.45)

    def _caption(self, content, y=-4.7):
        return Text(content, font_size=24, color=GRAY_A).move_to(UP * y)

    def _show_and_clear(self, title, focus, formula, caption, hold=1.1):
        """focus 中每个对象只入场和退场一次，不构造临时 FadeOut 对象。"""
        self.play(Write(title), run_time=0.5)
        self.play(*[Create(m) if isinstance(m, (Line, DashedLine, Arc))
                    else FadeIn(m) for m in focus], run_time=0.9)
        self.play(FadeIn(formula), FadeIn(caption), run_time=0.6)
        self.wait(hold)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(caption),
                  *[FadeOut(m) for m in focus], run_time=0.6)

    def show_opening(self):
        hook = self._title("为什么车轮是圆的？", YELLOW)
        spoke = Line(self.O, self.point_on_circle(35), color=self.red, stroke_width=3)
        self.play(FadeIn(self.author), Write(hook), run_time=0.8)
        self.play(Create(self.circle), Create(spoke), run_time=1.0)
        # 旋转轮辐，圆的旋转不变性可见，而非只旋转不可见的圆周轮廓。
        self.play(Rotate(spoke, angle=PI, about_point=self.O), run_time=1.0)
        self.play(FadeOut(spoke), FadeOut(hook), run_time=0.4)

    def show_definition(self):
        title = self._title("圆的定义")
        spokes = [Line(self.O, self.point_on_circle(angle), color=self.red,
                       stroke_width=2) for angle in (0, 45, 90, 135, 180, 225, 270, 315)]
        formula = MathTex(r"\{P\mid |PO|=r\},\quad r>0", font_size=33).move_to(DOWN * 3.65)
        caption = self._caption("到定点 O 的距离等于定长 r 的所有点")
        self.play(Write(title), FadeIn(self.center_dot), run_time=0.6)
        self.play(LaggedStart(*[Create(m) for m in spokes], lag_ratio=0.12), run_time=1.4)
        self.play(FadeIn(formula), FadeIn(caption), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(caption),
                  *[FadeOut(m) for m in spokes], run_time=0.6)

    def show_radius(self):
        focus = [Line(self.O, self.point_on_circle(a), color=self.red,
                      stroke_width=3) for a in (0, 75, 160, 270)]
        self._show_and_clear(self._title("半径 Radius", self.red), focus,
                             MathTex(r"OA=OB=OC=r", font_size=33).move_to(DOWN * 3.65),
                             self._caption("连接圆心与圆上任意一点的线段"))

    def show_diameter(self):
        title = self._title("直径 Diameter", self.orange)
        a, d = self.points["A"], self.points["D"]
        left = Line(self.O, d, color=self.red, stroke_width=3)
        right = Line(self.O, a, color=self.red, stroke_width=3)
        diameter = Line(d, a, color=self.orange, stroke_width=5)
        formula = MathTex(r"d=2r", font_size=35).move_to(DOWN * 3.65)
        caption = self._caption("经过圆心的弦；圆中最长的弦")
        self.play(Write(title), Create(left), Create(right), run_time=0.9)
        # 清除已显示的两条半径，再创建单独追踪的直径对象。
        self.play(FadeOut(left), FadeOut(right), Create(diameter), run_time=0.7)
        self.play(FadeIn(formula), FadeIn(caption), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(diameter), FadeOut(formula),
                  FadeOut(caption), run_time=0.6)

    def show_chord(self):
        b, c = self.points["B"], self.points["C"]
        chord = Line(b, c, color=self.green, stroke_width=4)
        diameter = DashedLine(self.points["D"], self.points["A"],
                              color=self.orange, dash_length=0.1)
        dots = [Dot(p, radius=0.075, color=WHITE) for p in (b, c)]
        self._show_and_clear(self._title("弦 Chord", self.green),
                             [chord, diameter, *dots],
                             MathTex(r"BC<AD=2r", font_size=33).move_to(DOWN * 3.65),
                             self._caption("连接圆上两点的线段；直径是特殊的弦"))

    def show_arc(self):
        title = self._title("劣弧与优弧", self.purple)
        b, c = self.points["B"], self.points["C"]
        dots = VGroup(Dot(b, radius=0.075), Dot(c, radius=0.075))
        minor = Arc(radius=self.radius, start_angle=60 * DEGREES,
                    angle=90 * DEGREES, arc_center=self.O,
                    color=self.purple, stroke_width=6)
        major = DashedVMobject(Arc(radius=self.radius,
                                  start_angle=150 * DEGREES, angle=270 * DEGREES,
                                  arc_center=self.O, color=self.orange,
                                  stroke_width=5), num_dashes=36)
        small_label = MathTex(r"\overset{\frown}{BC}", font_size=30,
                              color=self.purple).move_to(self.point_on_circle(105) + UP * 0.55)
        big_label = MathTex(r"\overset{\frown}{BAC}", font_size=30,
                            color=self.orange).move_to(self.point_on_circle(285) + DOWN * 0.55)
        minor_text = self._caption("劣弧：小于半圆的弧", -3.9)
        major_text = self._caption("优弧：大于半圆的弧", -4.9)
        self.play(Write(title), FadeIn(dots), Create(minor), run_time=1.1)
        self.play(FadeIn(small_label), FadeIn(minor_text), run_time=0.5)
        self.play(Create(major), FadeIn(big_label), FadeIn(major_text), run_time=1.1)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(dots), FadeOut(minor), FadeOut(major),
                  FadeOut(small_label), FadeOut(big_label), FadeOut(minor_text),
                  FadeOut(major_text), run_time=0.7)

    def show_summary(self):
        self.play(self.circle.animate.scale(0.5).move_to(UP * 4.25),
                  self.center_dot.animate.move_to(UP * 4.25), run_time=0.9)
        entries = (("圆心", "定点 O", self.red),
                   ("半径", "圆心到圆上任一点", self.red),
                   ("直径", "经过圆心的弦，d=2r", self.orange),
                   ("弦", "连接圆上两点的线段", self.green),
                   ("弧", "圆上两点间的一段", self.purple))
        cards = VGroup()
        for index, (name, detail, color) in enumerate(entries):
            card = VGroup(Dot(radius=0.11, color=color),
                          Text(name, font_size=27, color=WHITE),
                          Text(detail, font_size=23, color=GRAY_A))
            card.arrange(RIGHT, buff=0.18).move_to(UP * (2.45 - 1.2 * index))
            cards.add(card)
            # 真实位移入场；原实现 shift(RIGHT * 0) 导致卡片一直停在画外。
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.4)
        ending = Text("掌握圆的基本元素，开启几何新篇章！",
                      font_size=27, color=YELLOW).move_to(DOWN * 4.6)
        self.play(FadeIn(ending), run_time=0.5)
        self.wait(1.3)
        self.play(FadeOut(cards), FadeOut(ending), FadeOut(self.circle),
                  FadeOut(self.center_dot), FadeOut(self.author), run_time=0.8)
