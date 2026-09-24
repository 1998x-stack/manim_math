"""高一第二学期《任意角与弧度制》，保留原有八段结构与 Scene 入口。

数学约定：弧长计量 l=r|θ|；通常扇形的面积公式限定 0≤|θ|≤2π。
数值断言不等于最终画面包围盒或视频渲染验收。
"""
from manim import *
import math
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
BLUE_C = "#3498db"
RED_C = "#e74c3c"
GREEN_C = "#2ecc71"
AUTHOR = "上海初高中数学直通车 @emptyandcalm"


def cn(value, size=28, color=WHITE):
    return Text(value, font=FONT, font_size=size, color=color)


def fit(obj, width=7.6):
    if obj.width > width:
        obj.scale_to_fit_width(width)
    return obj


def terminal(radius, theta, center=ORIGIN):
    """由圆心、半径、弧度导出真实终边端点。"""
    return center + radius * np.array([math.cos(theta), math.sin(theta), 0.0])


class 任意角与弧度制Animation(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.RADIUS = 2.3
        self.CENTER = DOWN * 0.2
        self.author_info = fit(cn(AUTHOR, 17, GRAY_B)).move_to(UP * 7.45)
        self.add(self.author_info)
        self.show_opening()
        self.show_arbitrary_angle()
        self.show_radian_measure()
        self.show_conversion()
        self.show_arc_length()
        self.show_sector_area()
        self.show_terminal_angle()
        self.show_outro()

    def _title(self, value):
        return fit(cn(value, 37, BLUE_C)).move_to(UP * 6.45)

    def _clear(self, *items):
        self.play(*[FadeOut(item) for item in items], run_time=0.5)

    def _circle_axes(self):
        circle = Circle(radius=self.RADIUS, color=BLUE_C).move_to(self.CENTER)
        horizontal = Line(self.CENTER + LEFT * 3, self.CENTER + RIGHT * 3, color=GRAY_B)
        vertical = Line(self.CENTER + DOWN * 3, self.CENTER + UP * 3, color=GRAY_B)
        return circle, horizontal, vertical

    def show_opening(self):
        title = self._title("任意角与弧度制")
        lead = cn("角不只在 0° 到 360° 之间", 32, WHITE).move_to(UP * 2.8)
        examples = MathTex(r"45^\circ,\quad -45^\circ,\quad 405^\circ", font_size=40,
                           color=YELLOW).move_to(UP * 0.6)
        premise = cn("用旋转方向、弧长和终边统一理解", 28, GREEN_C).move_to(DOWN * 2.5)
        self.play(Write(title), FadeIn(lead), run_time=0.8)
        self.play(Write(examples), run_time=0.8)
        self.play(FadeIn(premise), run_time=0.6)
        self.wait(0.8)
        self._clear(title, lead, examples, premise)

    def show_arbitrary_angle(self):
        title = self._title("逆时针为正，顺时针为负")
        circle, horizontal, vertical = self._circle_axes()
        start = Line(self.CENTER, terminal(self.RADIUS, 0, self.CENTER), color=GREEN_C,
                     stroke_width=4)
        positive = Line(self.CENTER, terminal(self.RADIUS, math.pi / 4, self.CENTER),
                        color=RED_C, stroke_width=4)
        pos_arc = Arc(radius=0.85, start_angle=0, angle=math.pi / 4,
                      color=YELLOW, stroke_width=4).move_arc_center_to(self.CENTER)
        pos_label = MathTex(r"+45^\circ", font_size=31, color=YELLOW).move_to(UP * 3.7)
        negative = Line(self.CENTER, terminal(self.RADIUS, -math.pi / 4, self.CENTER),
                        color=RED_C, stroke_width=4)
        neg_arc = Arc(radius=0.85, start_angle=0, angle=-math.pi / 4,
                      color=YELLOW, stroke_width=4).move_arc_center_to(self.CENTER)
        neg_label = MathTex(r"-45^\circ", font_size=31, color=YELLOW).move_to(DOWN * 3.7)
        self.play(Write(title), Create(circle), Create(horizontal), Create(vertical), run_time=1.0)
        self.play(Create(start), Create(positive), Create(pos_arc), Write(pos_label), run_time=1.0)
        self.wait(0.5)
        self._clear(positive, pos_arc, pos_label)
        self.play(Create(negative), Create(neg_arc), Write(neg_label), run_time=0.9)
        self.wait(0.7)
        self._clear(title, circle, horizontal, vertical, start, negative, neg_arc, neg_label)

    def show_radian_measure(self):
        title = self._title("1 弧度：弧长恰等于半径")
        circle, horizontal, vertical = self._circle_axes()
        radius_line = Line(self.CENTER, terminal(self.RADIUS, 0, self.CENTER),
                           color=GREEN_C, stroke_width=4)
        arc = Arc(radius=self.RADIUS, start_angle=0, angle=1, color=YELLOW,
                  stroke_width=6).move_arc_center_to(self.CENTER)
        endpoint = Line(self.CENTER, terminal(self.RADIUS, 1, self.CENTER),
                        color=RED_C, stroke_width=4)
        small_angle = Arc(radius=0.7, start_angle=0, angle=1, color=YELLOW,
                          stroke_width=4).move_arc_center_to(self.CENTER)
        equation = MathTex(r"\theta=\frac{l}{r}=\frac{r}{r}=1\ \mathrm{rad}",
                           font_size=33, color=YELLOW).move_to(DOWN * 4.4)
        note = cn("这里的弧长取非负值；逆时针角为正", 23).move_to(UP * 4.5)
        self.play(Write(title), Create(circle), Create(horizontal), Create(vertical), run_time=0.9)
        self.play(Create(radius_line), Create(arc), Create(endpoint), Create(small_angle), run_time=1.0)
        self.play(Write(equation), FadeIn(note), run_time=0.9)
        self.wait(1.0)
        self._clear(title, circle, horizontal, vertical, radius_line, arc,
                    endpoint, small_angle, equation, note)

    def show_conversion(self):
        title = self._title("角度与弧度的换算")
        identity = MathTex(r"180^\circ=\pi\ \mathrm{rad}", font_size=43,
                           color=YELLOW).move_to(UP * 4.3)
        forward = MathTex(r"\theta_{\rm rad}=\theta_{\rm deg}\cdot\frac{\pi}{180}",
                          font_size=35).move_to(UP * 2)
        reverse = MathTex(r"\theta_{\rm deg}=\theta_{\rm rad}\cdot\frac{180}{\pi}",
                          font_size=35).move_to(UP * 0.3)
        examples = VGroup(
            MathTex(r"90^\circ=\frac\pi2\ \mathrm{rad}", font_size=32, color=GREEN_C),
            MathTex(r"60^\circ=\frac\pi3\ \mathrm{rad}", font_size=32, color=GREEN_C),
            MathTex(r"-45^\circ=-\frac\pi4\ \mathrm{rad}", font_size=32, color=GREEN_C),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 2.9)
        self.play(Write(title), Write(identity), run_time=0.9)
        self.play(Write(forward), Write(reverse), run_time=1.0)
        for item in examples:
            self.play(Write(item), run_time=0.6)
        self.wait(0.9)
        self._clear(title, identity, forward, reverse, examples)

    def show_arc_length(self):
        title = self._title("弧长公式：角度必须用弧度")
        equation = MathTex(r"l=r|\theta|", font_size=46, color=YELLOW).move_to(UP * 4.2)
        circle, horizontal, vertical = self._circle_axes()
        arc = Arc(radius=self.RADIUS, start_angle=0, angle=math.pi / 3,
                  color=YELLOW, stroke_width=6).move_arc_center_to(self.CENTER)
        initial = Line(self.CENTER, terminal(self.RADIUS, 0, self.CENTER), color=RED_C)
        final = Line(self.CENTER, terminal(self.RADIUS, math.pi / 3, self.CENTER), color=RED_C)
        example = MathTex(r"r=3,\quad \theta=\frac\pi3\ \Rightarrow\ l=\pi",
                          font_size=34, color=GREEN_C).move_to(DOWN * 4.4)
        note = cn("负角使用角度绝对值，弧长不能为负", 24).move_to(UP * 3.2)
        self.play(Write(title), Write(equation), run_time=0.9)
        self.play(Create(circle), Create(horizontal), Create(vertical), run_time=0.8)
        self.play(Create(initial), Create(final), Create(arc), run_time=0.9)
        self.play(Write(example), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear(title, equation, circle, horizontal, vertical, arc, initial, final, example, note)

    def show_sector_area(self):
        title = self._title("扇形面积：一周以内的圆心角")
        domain = MathTex(r"0\le|\theta|\le2\pi", font_size=32,
                         color=YELLOW).move_to(UP * 5.0)
        formulas = VGroup(
            MathTex(r"S=\frac12 r^2|\theta|", font_size=40),
            MathTex(r"S=\frac12 rl", font_size=40),
        ).arrange(DOWN, buff=0.35).move_to(UP * 3.7)
        circle = Circle(radius=self.RADIUS, color=BLUE_C).move_to(self.CENTER)
        sector = Sector(radius=self.RADIUS, start_angle=0, angle=math.pi / 3,
                        color=BLUE_C, fill_opacity=0.4).move_arc_center_to(self.CENTER)
        edge1 = Line(self.CENTER, terminal(self.RADIUS, 0, self.CENTER), color=RED_C)
        edge2 = Line(self.CENTER, terminal(self.RADIUS, math.pi / 3, self.CENTER), color=RED_C)
        example = MathTex(r"r=3,\ \theta=\frac\pi3\ \Rightarrow\ S=\frac{3\pi}{2}",
                          font_size=33, color=GREEN_C).move_to(DOWN * 4.0)
        note = fit(cn("超过整周的旋转角不能直接当成普通扇形面积", 22, GRAY_A))
        note.move_to(DOWN * 5.1)
        self.play(Write(title), Write(domain), Write(formulas), run_time=1.0)
        self.play(Create(circle), FadeIn(sector), Create(edge1), Create(edge2), run_time=1.1)
        self.play(Write(example), FadeIn(note), run_time=0.9)
        self.wait(0.9)
        self._clear(title, domain, formulas, circle, sector, edge1, edge2, example, note)

    def show_terminal_angle(self):
        title = self._title("终边相同，不等于旋转角相同")
        formula = MathTex(r"\beta=\alpha+2k\pi,\qquad k\in\mathbb{Z}",
                          font_size=35, color=YELLOW).move_to(UP * 4.7)
        circle, horizontal, vertical = self._circle_axes()
        start = Line(self.CENTER, terminal(self.RADIUS, 0, self.CENTER), color=GREEN_C)
        angle = math.pi / 4
        endpoint = terminal(self.RADIUS, angle, self.CENTER)
        terminal_line = Line(self.CENTER, endpoint, color=RED_C, stroke_width=4)
        arc = Arc(radius=0.8, start_angle=0, angle=angle, color=YELLOW,
                  stroke_width=4).move_arc_center_to(self.CENTER)
        examples = VGroup(
            MathTex(r"45^\circ", font_size=33),
            MathTex(r"405^\circ=45^\circ+360^\circ", font_size=32),
            MathTex(r"-315^\circ=45^\circ-360^\circ", font_size=32),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 4.2)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(Create(circle), Create(horizontal), Create(vertical), Create(start), run_time=0.8)
        self.play(Create(terminal_line), Create(arc), run_time=0.8)
        for item in examples:
            self.play(Write(item), run_time=0.6)
        self.wait(0.9)
        self._clear(title, formula, circle, horizontal, vertical, start,
                    terminal_line, arc, examples)

    def show_outro(self):
        title = self._title("任意角与弧度制 · 重点回顾")
        cards = VGroup(
            cn("逆时针为正，顺时针为负", 27),
            MathTex(r"180^\circ=\pi\ \mathrm{rad}", font_size=33, color=YELLOW),
            MathTex(r"l=r|\theta|", font_size=35, color=GREEN_C),
            MathTex(r"S=\frac12r^2|\theta|\quad (|\theta|\le2\pi)", font_size=32),
            MathTex(r"\beta=\alpha+2k\pi\quad (k\in\mathbb{Z})", font_size=31),
        ).arrange(DOWN, buff=0.7).move_to(UP * 0.9)
        self.play(Write(title), run_time=0.6)
        for card in cards:
            fit(card)
            self.play(FadeIn(card), run_time=0.5)
        self.wait(1.0)
        self._clear(title, cards, self.author_info)
