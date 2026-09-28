"""充分、必要与充要条件：固定论域、同一蕴含方向及明确的集合例子。

预览：manim -ql sufficient_necessary_conditions.py SufficientNecessaryConditions
"""
from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# 前两镜共用 p(x): x>2，q(x): x>0；充要镜另明确引入 r、s。
SAMPLE_P_BOUND = 2.0
SAMPLE_Q_BOUND = 0.0
SAMPLE_COUNTEREXAMPLE = 1.0
EQUIVALENT_BOUND = 1.0


def p_condition(x):
    return x > SAMPLE_P_BOUND


def q_condition(x):
    return x > SAMPLE_Q_BOUND


def r_condition(x):
    return abs(x) < EQUIVALENT_BOUND


def s_condition(x):
    return -EQUIVALENT_BOUND < x < EQUIVALENT_BOUND


class SufficientNecessaryConditions(Scene):
    """保留原五镜入口，图像始终与当前正在陈述的条件对应。"""

    FONT = "Noto Sans CJK SC"
    COLOR_P = "#e74c3c"
    COLOR_Q = "#3498db"
    COLOR_NECESSARY = "#2ecc71"
    COLOR_EQUIV = "#f39c12"
    RADIUS_P = 1.12
    RADIUS_Q = 1.92
    CENTER_P = np.array([-0.5, 1.35, 0.0])
    CENTER_Q = np.array([0.0, 1.35, 0.0])
    RADIUS_EQUAL = 1.65
    CENTER_EQUAL = np.array([0.0, 1.35, 0.0])

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self._validate_geometry()
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 19, GRAY_B)
        self.author_info.move_to(UP * 6.8)
        self.add(self.author_info)
        self.show_opening()
        self.show_sufficient_condition()
        self.show_necessary_condition()
        self.show_equivalent_condition()
        self.show_summary()

    def _validate_geometry(self):
        distance = np.linalg.norm(self.CENTER_P - self.CENTER_Q)
        if not (self.RADIUS_P > 0 and self.RADIUS_P + distance < self.RADIUS_Q):
            raise ValueError("充分/必要示意图必须严格满足 P 真包含于 Q")
        if self.RADIUS_Q + abs(self.CENTER_Q[0]) > 3.8:
            raise ValueError("集合圆超出竖屏水平安全区")

    def _text(self, text, size=27, color=WHITE):
        return Text(text, font=self.FONT, font_size=size, color=color)

    def _math(self, tex, size=33, color=WHITE):
        result = MathTex(tex, font_size=size, color=color)
        if result.width > 7.35:
            result.scale_to_fit_width(7.35)
        return result

    def _header(self, title, color=YELLOW):
        obj = self._text(title, 37, color).move_to(UP * 5.65)
        self.play(FadeIn(obj), run_time=0.55)
        return obj

    def _draw_inclusion(self):
        # P 是 p 成立的全部实数；Q 是 q 成立的全部实数。
        outer = Circle(radius=self.RADIUS_Q, color=self.COLOR_Q,
                       stroke_width=3, fill_color=self.COLOR_Q,
                       fill_opacity=0.10).move_to(self.CENTER_Q)
        inner = Circle(radius=self.RADIUS_P, color=self.COLOR_P,
                       stroke_width=3, fill_color=self.COLOR_P,
                       fill_opacity=0.17).move_to(self.CENTER_P)
        label_p = self._math("P", 34, self.COLOR_P).move_to((-0.58, 1.30, 0))
        label_q = self._math("Q", 34, self.COLOR_Q).move_to((1.12, 2.08, 0))
        self.inclusion = VGroup(outer, inner, label_p, label_q)
        self.play(FadeIn(self.inclusion), run_time=0.8)

    def show_opening(self):
        title = self._header("充分条件与必要条件")
        formula = self._math(r"p\Rightarrow q", 44).move_to(UP * 2.4)
        subtitle = self._text("先判断能推出什么，再辨认充分与必要", 24, GRAY_A)
        subtitle.move_to(DOWN * 0.6)
        self.play(Write(formula), FadeIn(subtitle), run_time=0.85)
        self.wait(0.55)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(subtitle), run_time=0.5)

    def show_sufficient_condition(self):
        title = self._header("p 是 q 的充分条件", self.COLOR_P)
        self._draw_inclusion()
        relation = self._math(r"P\subsetneq Q\quad\Longrightarrow\quad p\Rightarrow q",
                              31, self.COLOR_P).move_to(DOWN * 1.9)
        p = self._math(r"p:\ x>2\quad (x\in\mathbb{R})", 30).move_to(DOWN * 3.0)
        q = self._math(r"q:\ x>0", 30).move_to(DOWN * 3.9)
        explanation = self._text("x>2 必定推出 x>0，但反过来不成立", 22, GRAY_A)
        explanation.move_to(DOWN * 5.0)
        self.play(Write(relation), Write(p), Write(q), run_time=1.1)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(relation), FadeOut(p), FadeOut(q),
                  FadeOut(explanation), run_time=0.55)

    def show_necessary_condition(self):
        # 使用上一镜完全相同的 P/Q 图，不反转箭头或重定义集合。
        title = self._header("q 是 p 的必要条件", self.COLOR_NECESSARY)
        formula = self._math(r"p\Rightarrow q\quad\Longleftrightarrow\quad q\Leftarrow p",
                             29, self.COLOR_NECESSARY).move_to(DOWN * 1.9)
        explanation = self._text("p 成立时 q 必须成立；方向仍是 p 推出 q", 23, GRAY_A)
        explanation.move_to(DOWN * 3.0)
        counterexample = self._math(r"x=1:\quad q\ \mathrm{true},\quad p\ \mathrm{false}",
                                    29, self.COLOR_NECESSARY).move_to(DOWN * 4.1)
        note = self._text("因此 q 对 p 必要，但 q 对 p 不充分", 23, GRAY_A)
        note.move_to(DOWN * 5.05)
        self.play(Write(formula), FadeIn(explanation), run_time=0.9)
        self.play(Write(counterexample), FadeIn(note), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation),
                  FadeOut(counterexample), FadeOut(note), FadeOut(self.inclusion), run_time=0.6)

    def show_equivalent_condition(self):
        title = self._header("充要条件：改用一组等价的条件", self.COLOR_EQUIV)
        r = self._math(r"r:\ |x|<1", 33, self.COLOR_P).move_to(UP * 3.95)
        s = self._math(r"s:\ -1<x<1", 33, self.COLOR_Q).move_to(UP * 3.32)
        # 新例子的 R 与 S 完全重合；两条边界圆具有相同圆心和半径。
        circle_r = Circle(radius=self.RADIUS_EQUAL, color=self.COLOR_P,
                          stroke_width=3).move_to(self.CENTER_EQUAL)
        circle_s = DashedVMobject(
            Circle(radius=self.RADIUS_EQUAL, color=self.COLOR_Q,
                   stroke_width=3).move_to(self.CENTER_EQUAL), num_dashes=32,
        )
        label = self._math("R=S", 40, self.COLOR_EQUIV).move_to(self.CENTER_EQUAL)
        self.play(Write(r), Write(s), run_time=0.85)
        self.play(Create(circle_r), Create(circle_s), FadeIn(label), run_time=0.95)
        formula = self._math(r"r\Leftrightarrow s", 36, self.COLOR_EQUIV)
        formula.move_to(DOWN * 2.0)
        explanation = self._text("R=S：r 和 s 互为充分必要条件", 25, GRAY_A)
        explanation.move_to(DOWN * 3.1)
        note = self._text("注意：本镜已更换为 r、s，并非声称前面 P=Q", 20, GRAY_B)
        note.move_to(DOWN * 4.35)
        self.play(Write(formula), FadeIn(explanation), FadeIn(note), run_time=0.8)
        self.wait(0.8)
        self.play(*[FadeOut(m) for m in (title, r, s, circle_r, circle_s, label,
                                        formula, explanation, note)], run_time=0.7)

    def show_summary(self):
        title = self._header("从蕴含方向判断条件")
        rows = (
            ("p 对 q 充分", r"p\Rightarrow q", self.COLOR_P),
            ("q 对 p 必要", r"q\Leftarrow p", self.COLOR_NECESSARY),
            ("r 与 s 互为充要", r"r\Leftrightarrow s", self.COLOR_EQUIV),
        )
        groups = VGroup()
        for index, (label, formula, color) in enumerate(rows):
            left = self._text(label, 26, color)
            right = self._math(formula, 31, color)
            row = VGroup(left, right).arrange(RIGHT, buff=0.4)
            row.move_to(UP * (3.6 - 1.6 * index))
            if row.width > 7.35:
                row.scale_to_fit_width(7.35)
            groups.add(row)
            self.play(FadeIn(row), run_time=0.65)
        note = self._text("充分看 p⇒q，必要也看同一方向；充要需双向成立", 22, GRAY_A)
        note.move_to(DOWN * 2.9)
        if note.width > 7.35:
            note.scale_to_fit_width(7.35)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.3)
        self.play(FadeOut(title), FadeOut(groups), FadeOut(note),
                  FadeOut(self.author_info), run_time=0.7)
