"""一元二次方程：直接开平方法，八年级上第十七章。

manim -pql direct_square_root.py DirectSquareRootMethod
保持原有七段教学顺序、Scene 入口、9:16 竖屏与作者署名。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def solve_shifted_square(m, n):
    """求 (x+m)²=n 在实数范围内的互异根，按从小到大排序。"""
    if not math.isfinite(m) or not math.isfinite(n):
        raise ValueError("参数必须为有限实数")
    if n < 0:
        return ()
    if n == 0:
        return (-m,)
    root = math.sqrt(n)
    return (-m - root, -m + root)


def equation_residual(x, m, n):
    """将候选根代回原方程的误差，用于验证动画显示的结果。"""
    return (x + m) ** 2 - n


class DirectSquareRootMethod(Scene):
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    CYAN = "#56d0dc"
    VIOLET = "#b3a4f9"
    GREEN = "#85dfa3"
    CORAL = "#f58c8c"
    MUTED = "#c5cbdb"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font="PingFang SC", font_size=18,
                                color=self.MUTED).move_to(UP * 6.6)
        self.add(self.author_info)
        self.show_opening()
        self.show_method_introduction()
        self.show_basic_derivation()
        self.show_general_formula()
        self.show_example_1()
        self.show_example_2()
        self.show_summary()

    def _title(self, text):
        title = Text(text, font="PingFang SC", font_size=40,
                     color=self.TITLE).move_to(UP * 5.8)
        if title.width > 7.8:
            title.scale_to_fit_width(7.8)
        return title

    def _note(self, text, y, color=None):
        note = Text(text, font="PingFang SC", font_size=27,
                    color=color or self.MUTED).move_to(UP * y)
        if note.width > 7.6:
            note.scale_to_fit_width(7.6)
        return note

    def _card(self, y, height, content, color=None):
        border = color or self.CYAN
        frame = RoundedRectangle(corner_radius=0.25, width=7.7, height=height,
                                 stroke_color=border, stroke_width=2,
                                 fill_color=self.PANEL, fill_opacity=0.92).move_to(UP * y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(frame.get_center())
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height - 0.24:
            body.scale_to_fit_height(height - 0.24)
        return VGroup(frame, body)

    def _clear(self):
        active = [mob for mob in list(self.mobjects) if mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.4)

    def show_opening(self):
        title = self._title("x² = 9，有几个实数解？")
        question = self._card(3.7, 1.9,
                              MathTex(r"x^2=9", font_size=70,
                                      color=self.CYAN), self.CYAN)
        options = self._note("别漏掉负数：(-3)² 和 3² 都等于 9", 1.2)
        answer = self._card(-1.35, 1.9,
                            MathTex(r"x=-3,\quad x=3",
                                    font_size=50, color=self.GREEN), self.GREEN)
        self.play(Write(title), FadeIn(question), run_time=0.8)
        self.play(FadeIn(options), run_time=0.5)
        self.play(FadeIn(answer), run_time=0.6)
        self.wait(1.0)
        self._clear()

    def show_method_introduction(self):
        title = self._title("直接开平方法")
        name = self._card(3.6, 1.85,
                          MathTex(r"(x+m)^2=n", font_size=62,
                                  color=self.CYAN), self.CYAN)
        hint = self._note("平方形式已出现，可直接对两边开平方", 1.2)
        guard = self._card(-1.45, 1.9,
                           MathTex(r"n\geq0:\quad x=-m\pm\sqrt n",
                                   font_size=47, color=self.TITLE), self.TITLE)
        self.play(Write(title), FadeIn(name), run_time=0.8)
        self.play(FadeIn(hint), FadeIn(guard), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def show_basic_derivation(self):
        title = self._title("x² = 9：为什么有正、负两个解？")
        start = self._card(3.8, 1.55,
                           MathTex(r"x^2=9", font_size=59,
                                   color=self.CYAN), self.CYAN)
        equation = self._card(1.45, 1.5,
                              MathTex(r"x=\pm\sqrt9=\pm3", font_size=53,
                                      color=self.TITLE), self.TITLE)
        number_line = NumberLine(x_range=[-4, 4, 1], length=7,
                                 include_numbers=True, font_size=24).move_to(DOWN * 1.1)
        left = Dot(number_line.n2p(-3), color=self.CORAL, radius=0.12)
        right = Dot(number_line.n2p(3), color=self.GREEN, radius=0.12)
        left_label = MathTex(r"-3", font_size=33,
                             color=self.CORAL).next_to(left, UP, buff=0.25)
        right_label = MathTex(r"3", font_size=33,
                              color=self.GREEN).next_to(right, UP, buff=0.25)
        check = self._note("验算：(-3)² = 9，3² = 9", -3.1)
        assert solve_shifted_square(0, 9) == (-3, 3)
        self.play(Write(title), FadeIn(start), FadeIn(equation), run_time=0.9)
        self.play(Create(number_line), FadeIn(left), FadeIn(right),
                  FadeIn(left_label), FadeIn(right_label), run_time=0.8)
        self.play(FadeIn(check), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def show_general_formula(self):
        title = self._title("平方右侧 n 的符号决定解的个数")
        general = self._card(3.7, 1.85,
                             MathTex(r"(x+m)^2=n", font_size=56,
                                     color=self.CYAN), self.CYAN)
        positive = self._card(1.15, 1.75,
                              MathTex(r"n>0:\quad x=-m\pm\sqrt n",
                                      font_size=45, color=self.GREEN), self.GREEN)
        zero = self._card(-1.4, 1.75,
                          MathTex(r"n=0:\quad x=-m", font_size=49,
                                  color=self.TITLE), self.TITLE)
        negative = self._note("n < 0：平方不可能为负，没有实数解", -3.5, self.CORAL)
        assert solve_shifted_square(2, 0) == (-2,)
        assert solve_shifted_square(2, -1) == ()
        self.play(Write(title), FadeIn(general), run_time=0.8)
        self.play(FadeIn(positive), FadeIn(zero), run_time=0.8)
        self.play(FadeIn(negative), run_time=0.4)
        self.wait(1.2)
        self._clear()

    def show_example_1(self):
        title = self._title("例题一：(x+2)² = 16")
        first = self._card(3.7, 1.75,
                           MathTex(r"(x+2)^2=16", font_size=54,
                                   color=WHITE), self.CYAN)
        second = self._card(1.1, 1.75,
                            MathTex(r"x+2=\pm4", font_size=56,
                                    color=self.VIOLET), self.VIOLET)
        third = self._card(-1.5, 1.75,
                           MathTex(r"x=-2\pm4:\quad x=2,-6",
                                   font_size=45, color=self.GREEN), self.GREEN)
        solutions = solve_shifted_square(2, 16)
        assert solutions == (-6, 2)
        assert all(equation_residual(x, 2, 16) == 0 for x in solutions)
        note = self._note("代回原方程检验：4² = 16，(-4)² = 16", -3.5)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def show_example_2(self):
        title = self._title("例题二：先识别完全平方式")
        first = self._card(3.8, 1.65,
                           MathTex(r"x^2+6x+9=25", font_size=49,
                                   color=WHITE), self.CYAN)
        second = self._card(1.5, 1.65,
                            MathTex(r"(x+3)^2=25", font_size=51,
                                    color=self.VIOLET), self.VIOLET)
        third = self._card(-0.8, 1.65,
                           MathTex(r"x+3=\pm5", font_size=53,
                                   color=self.TITLE), self.TITLE)
        fourth = self._card(-3.1, 1.65,
                            MathTex(r"x=-3\pm5:\quad x=2,-8",
                                    font_size=44, color=self.GREEN), self.GREEN)
        solutions = solve_shifted_square(3, 25)
        assert solutions == (-8, 2)
        assert all(equation_residual(x, 3, 25) == 0 for x in solutions)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(fourth), run_time=0.5)
        self.wait(1.1)
        self._clear()

    def show_summary(self):
        title = self._title("总结：先看 n 的符号，再开平方")
        positive = self._card(3.7, 1.75,
                              MathTex(r"n>0:\quad x=-m\pm\sqrt n",
                                      font_size=44, color=self.GREEN), self.GREEN)
        zero = self._card(1.1, 1.75,
                          MathTex(r"n=0:\quad x=-m", font_size=48,
                                  color=self.TITLE), self.TITLE)
        negative = self._card(-1.5, 1.75,
                              self._note("n < 0：没有实数解", 0, self.CORAL), self.CORAL)
        note = self._note("正数两个互异实数解；零只有一个互异实数解", -3.5)
        self.play(Write(title), FadeIn(positive), run_time=0.8)
        self.play(FadeIn(zero), FadeIn(negative), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()
        self.play(FadeOut(self.author_info), run_time=0.35)
