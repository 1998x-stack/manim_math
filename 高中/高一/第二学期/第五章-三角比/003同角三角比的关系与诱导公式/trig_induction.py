"""高一《同角三角比关系与诱导公式》：保留 TrigInduction 和十个教学场景。

数学事实由单位圆上的实际坐标验证，正切公式仅在 cos(alpha)!=0 时使用。
本源文件的 9:16 设计仍需最终 Manim/字体/TeX/逐帧/音轨验收。
"""
from manim import *
import math
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
BG_COLOR = "#1a1a2e"
C_SIN = "#e74c3c"
C_COS = "#3498db"
C_TAN = "#f39c12"
C_CIRCLE = "#2ecc71"
AUTHOR = "上海初高中数学直通车 @emptyandcalm"


def cn(value, size=28, color=WHITE):
    return Text(value, font=FONT, font_size=size, color=color)


def fit(item, width=7.5):
    if item.width > width:
        item.scale_to_fit_width(width)
    return item


class TrigInduction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = fit(cn(AUTHOR, 17, GRAY_B)).move_to(UP * 7.45)
        self.add(self.author)
        self.scene_01_opening()
        self.scene_02_unit_circle()
        self.scene_03_pythagorean_identity()
        self.scene_04_tan_identity()
        self.scene_05_induction_intro()
        self.scene_06_induction_pi_minus()
        self.scene_07_induction_halfpi_minus()
        self.scene_08_induction_negative()
        self.scene_09_summary()
        self.scene_10_outro()

    def _title(self, value):
        return fit(cn(value, 36, YELLOW)).move_to(UP * 6.4)

    def _clear(self, *items):
        self.play(*[FadeOut(item) for item in items], run_time=0.5)

    def _unit(self):
        axes = Axes(x_range=[-1.25, 1.25, 0.5], y_range=[-1.25, 1.25, 0.5],
                    x_length=5.2, y_length=5.2,
                    axis_config={"color": GRAY_B}, tips=False).move_to(DOWN * 0.15)
        center = axes.c2p(0, 0)
        radius = np.linalg.norm(axes.c2p(1, 0) - center)
        circle = Circle(radius=radius, color=C_CIRCLE, stroke_width=3).move_to(center)
        return axes, circle

    @staticmethod
    def _xy(theta):
        return math.cos(theta), math.sin(theta)

    def scene_01_opening(self):
        title = self._title("同角三角比与诱导公式")
        question = MathTex(r"\sin^2\alpha+\cos^2\alpha=?", font_size=43,
                           color=YELLOW).move_to(UP * 2.5)
        prompt = cn("一张单位圆揭示三类变换", 29).move_to(UP * 0.5)
        items = VGroup(
            MathTex(r"\pi-\alpha", font_size=36, color=C_SIN),
            MathTex(r"\frac\pi2-\alpha", font_size=36, color=C_COS),
            MathTex(r"-\alpha", font_size=36, color=C_TAN),
        ).arrange(DOWN, buff=0.6).move_to(DOWN * 2.6)
        self.play(Write(title), Write(question), run_time=0.9)
        self.play(FadeIn(prompt), run_time=0.5)
        for item in items:
            self.play(Write(item), run_time=0.45)
        self.wait(0.8)
        self._clear(title, question, prompt, items)

    def scene_02_unit_circle(self):
        title = self._title("单位圆：P 的横纵坐标")
        axes, circle = self._unit()
        theta = math.pi / 3
        x, y = self._xy(theta)
        center, pos = axes.c2p(0, 0), axes.c2p(x, y)
        radial = Line(center, pos, color=YELLOW, stroke_width=4)
        dot = Dot(pos, radius=0.09, color=YELLOW)
        foot = axes.c2p(x, 0)
        vertical = DashedLine(pos, foot, color=C_SIN)
        horizontal = DashedLine(center, foot, color=C_COS)
        point_label = MathTex(r"P=(\cos\alpha,\sin\alpha)", font_size=30,
                              color=YELLOW).move_to(UP * 4.45)
        definitions = MathTex(r"x=\cos\alpha,\qquad y=\sin\alpha", font_size=32)
        fit(definitions).move_to(DOWN * 4.2)
        self.play(Write(title), Create(axes), Create(circle), run_time=1.0)
        self.play(Create(radial), FadeIn(dot), Create(vertical), Create(horizontal), run_time=0.9)
        self.play(Write(point_label), Write(definitions), run_time=0.9)
        self.wait(0.8)
        self._clear(title, axes, circle, radial, dot, vertical, horizontal,
                    point_label, definitions)

    def scene_03_pythagorean_identity(self):
        title = self._title("勾股定理推出同角基本关系")
        axes, circle = self._unit()
        x, y = self._xy(math.pi / 3)
        center, foot, pos = axes.c2p(0, 0), axes.c2p(x, 0), axes.c2p(x, y)
        leg_x = Line(center, foot, color=C_COS, stroke_width=5)
        leg_y = Line(foot, pos, color=C_SIN, stroke_width=5)
        hypotenuse = Line(center, pos, color=YELLOW, stroke_width=5)
        triangle = Polygon(center, foot, pos, stroke_color=GRAY_B,
                           fill_color=YELLOW, fill_opacity=0.1)
        small_square = Polygon(foot, foot + LEFT * 0.15,
                               foot + LEFT * 0.15 + UP * 0.15,
                               foot + UP * 0.15, color=YELLOW, fill_opacity=0)
        step = MathTex(r"x^2+y^2=1^2", font_size=39).move_to(DOWN * 4.0)
        result = MathTex(r"\sin^2\alpha+\cos^2\alpha=1", font_size=36,
                         color=YELLOW).move_to(DOWN * 5.2)
        note = cn("线段长度分别为 |cosα|、|sinα| 和 1", 23).move_to(UP * 4.3)
        self.play(Write(title), Create(axes), Create(circle), run_time=0.9)
        self.play(Create(triangle), Create(leg_x), Create(leg_y), Create(hypotenuse),
                  Create(small_square), run_time=1.0)
        self.play(FadeIn(note), Write(step), run_time=0.8)
        self.play(Write(result), run_time=0.75)
        self.wait(1.0)
        self._clear(title, axes, circle, triangle, leg_x, leg_y, hypotenuse,
                    small_square, note, step, result)

    def scene_04_tan_identity(self):
        title = self._title("正切是纵坐标与横坐标之比")
        axes, circle = self._unit()
        x, y = self._xy(math.pi / 6)
        center, foot, pos = axes.c2p(0, 0), axes.c2p(x, 0), axes.c2p(x, y)
        radius = Line(center, pos, color=YELLOW, stroke_width=4)
        x_leg = Line(center, foot, color=C_COS, stroke_width=4)
        y_leg = Line(foot, pos, color=C_SIN, stroke_width=4)
        formula = MathTex(r"\tan\alpha=\frac{\sin\alpha}{\cos\alpha},\quad\cos\alpha\ne0",
                          font_size=31, color=C_TAN)
        fit(formula).move_to(DOWN * 4.0)
        identity = MathTex(r"1+\tan^2\alpha=\frac{1}{\cos^2\alpha}",
                           font_size=31, color=C_TAN).move_to(DOWN * 5.15)
        explanation = cn("横坐标为 0 时正切不存在", 25, YELLOW).move_to(UP * 4.35)
        self.play(Write(title), Create(axes), Create(circle), run_time=0.9)
        self.play(Create(radius), Create(x_leg), Create(y_leg), run_time=0.9)
        self.play(Write(formula), Write(identity), FadeIn(explanation), run_time=1.0)
        self.wait(0.9)
        self._clear(title, axes, circle, radius, x_leg, y_leg,
                    formula, identity, explanation)

    def scene_05_induction_intro(self):
        title = self._title("诱导公式来自坐标的对称与互换")
        lines = VGroup(
            cn("关于 y 轴对称：横坐标变号", 29, C_SIN),
            cn("关于 x 轴对称：纵坐标变号", 29, C_COS),
            cn("关于 y=x 对称：横纵坐标互换", 27, C_TAN),
        ).arrange(DOWN, buff=0.9).move_to(UP * 1.6)
        note = cn("口诀仅帮助记忆，角与函数的符号要逐一判断", 24, GRAY_A)
        fit(note).move_to(DOWN * 3.5)
        self.play(Write(title), run_time=0.65)
        for line in lines:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.0)
        self._clear(title, lines, note)

    def _compare(self, heading, beta, symmetry, formula1, formula2, formula3):
        theta = math.pi / 6
        title = self._title(heading)
        axes, circle = self._unit()
        x1, y1 = self._xy(theta)
        x2, y2 = self._xy(beta)
        origin = axes.c2p(0, 0)
        p1, p2 = axes.c2p(x1, y1), axes.c2p(x2, y2)
        first = Line(origin, p1, color=C_COS, stroke_width=4)
        second = Line(origin, p2, color=C_SIN, stroke_width=4)
        d1, d2 = Dot(p1, color=C_COS), Dot(p2, color=C_SIN)
        if symmetry == 'y':
            guide = DashedLine(axes.c2p(0, -1), axes.c2p(0, 1), color=YELLOW)
        elif symmetry == 'x':
            guide = DashedLine(axes.c2p(-1, 0), axes.c2p(1, 0), color=YELLOW)
        else:
            guide = DashedLine(axes.c2p(-1, -1), axes.c2p(1, 1), color=YELLOW)
        note = cn("蓝点与红点的坐标通过对称关系对应", 24, GRAY_A).move_to(UP * 4.3)
        formulas = VGroup(
            MathTex(formula1, font_size=30, color=C_SIN),
            MathTex(formula2, font_size=30, color=C_COS),
            MathTex(formula3, font_size=29, color=C_TAN),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 4.5)
        for item in formulas:
            fit(item)
        self.play(Write(title), Create(axes), Create(circle), Create(guide), run_time=1.0)
        self.play(Create(first), FadeIn(d1), run_time=0.6)
        self.play(Create(second), FadeIn(d2), FadeIn(note), run_time=0.7)
        for item in formulas:
            self.play(Write(item), run_time=0.6)
        self.wait(1.0)
        self._clear(title, axes, circle, guide, first, second, d1, d2, note, formulas)

    def scene_06_induction_pi_minus(self):
        self._compare("诱导：π−α 对应关于 y 轴对称", math.pi - math.pi/6, 'y',
                      r"\sin(\pi-\alpha)=\sin\alpha",
                      r"\cos(\pi-\alpha)=-\cos\alpha",
                      r"\tan(\pi-\alpha)=-\tan\alpha\quad(\cos\alpha\ne0)")

    def scene_07_induction_halfpi_minus(self):
        self._compare("诱导：π/2−α 对应关于 y=x 对称", math.pi/2 - math.pi/6, 'diagonal',
                      r"\sin(\frac\pi2-\alpha)=\cos\alpha",
                      r"\cos(\frac\pi2-\alpha)=\sin\alpha",
                      r"\tan(\frac\pi2-\alpha)=\frac{\cos\alpha}{\sin\alpha}\quad(\sin\alpha\ne0)")

    def scene_08_induction_negative(self):
        self._compare("诱导：−α 对应关于 x 轴对称", -math.pi/6, 'x',
                      r"\sin(-\alpha)=-\sin\alpha",
                      r"\cos(-\alpha)=\cos\alpha",
                      r"\tan(-\alpha)=-\tan\alpha\quad(\cos\alpha\ne0)")

    def scene_09_summary(self):
        title = self._title("同角关系与诱导公式总结")
        identities = VGroup(
            MathTex(r"\sin^2\alpha+\cos^2\alpha=1", font_size=34, color=YELLOW),
            MathTex(r"\tan\alpha=\frac{\sin\alpha}{\cos\alpha}\quad(\cos\alpha\ne0)", font_size=28),
            MathTex(r"\sin(\pi-\alpha)=\sin\alpha", font_size=30, color=C_SIN),
            MathTex(r"\cos(\pi-\alpha)=-\cos\alpha", font_size=30, color=C_COS),
            MathTex(r"\sin(\frac\pi2-\alpha)=\cos\alpha", font_size=30, color=C_SIN),
            MathTex(r"\cos(\frac\pi2-\alpha)=\sin\alpha", font_size=30, color=C_COS),
            MathTex(r"\sin(-\alpha)=-\sin\alpha", font_size=30, color=C_SIN),
            MathTex(r"\cos(-\alpha)=\cos\alpha", font_size=30, color=C_COS),
        ).arrange(DOWN, buff=0.4).move_to(UP * 0.5)
        self.play(Write(title), run_time=0.6)
        for item in identities:
            fit(item)
            self.play(FadeIn(item), run_time=0.4)
        self.wait(1.0)
        self._clear(title, identities)

    def scene_10_outro(self):
        title = self._title("记住坐标变换，而不只记口诀")
        recap = VGroup(
            MathTex(r"(x,y)\xrightarrow{\ y\mathrm{-axis}\ }(-x,y)", font_size=31),
            MathTex(r"(x,y)\xrightarrow{\ x\mathrm{-axis}\ }(x,-y)", font_size=31),
            MathTex(r"(x,y)\xrightarrow{\ y=x\ }(y,x)", font_size=31),
            cn("条件明确，才能正确使用诱导公式", 27, YELLOW),
        ).arrange(DOWN, buff=0.9).move_to(UP * 0.6)
        for item in recap:
            fit(item)
        self.play(Write(title), run_time=0.6)
        for item in recap:
            self.play(FadeIn(item), run_time=0.6)
        self.wait(1.0)
        self._clear(title, recap, self.author)
