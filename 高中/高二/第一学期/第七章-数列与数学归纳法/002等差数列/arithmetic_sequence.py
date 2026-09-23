"""高二等差数列｜八镜教学动画（竖屏 9:16）。

数学计算统一从 arithmetic_model 读取；此文件只负责画面与动画。
预览：manim -pql arithmetic_sequence.py ArithmeticSequenceLesson
"""
from manim import *
from arithmetic_model import arithmetic_mean, first_n_sum, sample, term

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ArithmeticSequenceLesson(Scene):
    """定义、通项、求和、中项、离散图像、性质与应用。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.a1, self.d = 2, 3
        self.terms = sample(self.a1, self.d, 7)
        self.blue, self.orange = "#55b5f7", "#ffb35c"
        self.green, self.muted = "#66daa7", "#b9c3d4"
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_general_term()
        self.scene_4_sum_formula()
        self.scene_5_arithmetic_mean()
        self.scene_6_graphical_pattern()
        self.scene_7_properties()
        self.scene_8_outro()

    @staticmethod
    def _fit(mob, width=7.3):
        """使用实际对象宽度缩放，而非仅用文本长度猜测。"""
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def _text(self, content, size=27, color=WHITE):
        return self._fit(Text(content, font_size=size, color=color))

    def _math(self, formula, size=32, color=WHITE):
        return self._fit(MathTex(formula, font_size=size, color=color))

    def _header(self, title):
        author = self._text("上海初高中数学直通车 @emptyandcalm", 18, self.muted)
        author.move_to(UP * 6.8)
        heading = self._text(title, 37, self.blue).move_to(UP * 5.5)
        self.play(FadeIn(author), Write(heading), run_time=0.8)

    def _clear(self):
        """只淡出确实存在于场景中的对象，避免对临时副本 FadeOut。"""
        visible = tuple(self.mobjects)
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)
        self.clear()

    def scene_1_opening(self):
        self._header("下一个数字是什么？")
        prompt = self._math(r"2,\ 5,\ 8,\ 11,\ 14,\ \ldots", 40, self.orange)
        prompt.move_to(UP * 3.4)
        line = NumberLine(x_range=[0, 23, 1], length=7,
                          include_numbers=False, color=self.muted).move_to(UP * 0.5)
        dots = VGroup(*[Dot(line.number_to_point(a), radius=0.085, color=self.blue)
                        for a in self.terms])
        labels = VGroup(*[self._math(str(a), 21).next_to(dot, DOWN, buff=0.2)
                          for a, dot in zip(self.terms, dots)])
        self.play(Write(prompt), Create(line), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots],
                              lag_ratio=0.13), run_time=1.5)
        self.play(FadeIn(labels), run_time=0.6)
        answer = self._math(r"20+3=23", 37, self.green).move_to(DOWN * 2.3)
        self.play(Write(answer), run_time=0.9)
        self.wait(0.7)
        self._clear()

    def scene_2_definition(self):
        self._header("等差数列：相邻项之差相同")
        terms = VGroup(*[self._math(str(a), 34, self.blue)
                         for a in self.terms[:5]]).arrange(RIGHT, buff=0.78)
        terms.move_to(UP * 2.8)
        self.play(FadeIn(terms), run_time=0.7)
        arrows = VGroup()
        increments = VGroup()
        for left, right in zip(terms, terms[1:]):
            arrow = Arrow(left.get_right(), right.get_left(), buff=0.08,
                          color=self.orange, stroke_width=3)
            arrows.add(arrow)
            increments.add(self._math(r"+3", 22, self.orange)
                           .next_to(arrow, UP, buff=0.05))
        self.play(*[Create(arrow) for arrow in arrows],
                  *[FadeIn(note) for note in increments], run_time=0.9)
        definition = self._math(r"a_{n+1}-a_n=d\quad(n\geq 1)", 34, self.green)
        definition.move_to(UP * 0.5)
        detail = self._text("公差 d 是常数；可以为正、负或零", 26, self.muted)
        detail.move_to(DOWN * 1.1)
        example = self._math(r"2,5,8,11,\ldots\quad d=3", 30, self.orange)
        example.move_to(DOWN * 2.8)
        self.play(Write(definition), FadeIn(detail), run_time=1.0)
        self.play(FadeIn(example), run_time=0.6)
        self.wait(1.3)
        self._clear()

    def scene_3_general_term(self):
        self._header("从相邻差推导通项公式")
        derivation = VGroup(
            self._math(r"a_1=2", 30),
            self._math(r"a_2=a_1+d=5", 30),
            self._math(r"a_3=a_1+2d=8", 30),
            self._math(r"a_4=a_1+3d=11", 30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.52).move_to(UP * 1.9)
        for line in derivation:
            self.play(Write(line), run_time=0.55)
        general = self._math(r"a_n=a_1+(n-1)d\quad(n\geq1)", 36, self.green)
        general.move_to(DOWN * 1.4)
        verification = self._math(
            rf"a_7=2+(7-1)\times3={term(self.a1, self.d, 7)}", 30, self.orange
        ).move_to(DOWN * 3.1)
        self.play(Write(general), run_time=0.9)
        self.play(Write(verification), run_time=0.7)
        self.wait(1.3)
        self._clear()

    def scene_4_sum_formula(self):
        self._header("前 n 项和：倒序相加")
        rows = VGroup(
            self._math(r"S_7=2+5+8+11+14+17+20", 29),
            self._math(r"S_7=20+17+14+11+8+5+2", 29),
        ).arrange(DOWN, buff=0.65).move_to(UP * 3)
        self.play(Write(rows[0]), run_time=0.95)
        self.play(Write(rows[1]), run_time=0.95)
        pairing = self._math(r"2S_7=7(2+20)", 34, self.orange).move_to(UP * 0.6)
        value = self._math(rf"S_7={first_n_sum(self.a1, self.d, 7):g}",
                           40, self.green).move_to(DOWN * 0.55)
        self.play(Write(pairing), run_time=0.8)
        self.play(Write(value), run_time=0.7)
        general = self._math(r"S_n=\frac{n(a_1+a_n)}2", 34, self.green)
        general.move_to(DOWN * 2.3)
        alternative = self._math(r"S_n=na_1+\frac{n(n-1)d}2", 31, self.green)
        alternative.move_to(DOWN * 3.65)
        self.play(Write(general), run_time=0.7)
        self.play(Write(alternative), run_time=0.7)
        self.wait(1.5)
        self._clear()

    def scene_5_arithmetic_mean(self):
        self._header("等差中项：两边的差相同")
        line = NumberLine(x_range=[0, 15, 1], length=6.4,
                          include_numbers=False, color=self.muted).move_to(UP * 1.3)
        values = (5, 8, 11)
        points = VGroup(*[Dot(line.number_to_point(v), radius=0.11,
                              color=self.orange if v == 8 else self.blue)
                          for v in values])
        labels = VGroup(*[self._math(rf"{symbol}={value}", 25)
                          .next_to(point, DOWN, buff=0.25)
                          for symbol, value, point in zip(("a", "A", "b"), values, points)])
        braces = VGroup()
        marks = VGroup()
        for i in (0, 1):
            brace = Brace(Line(points[i].get_center(), points[i + 1].get_center()),
                          direction=UP, buff=0.12, color=self.orange)
            braces.add(brace)
            marks.add(self._math(r"d=3", 23, self.orange).next_to(brace, UP, buff=0.06))
        self.play(Create(line), FadeIn(points), FadeIn(labels), run_time=1.0)
        self.play(FadeIn(braces), FadeIn(marks), run_time=0.7)
        formula = self._math(r"A-a=b-A\ \Longrightarrow\ A=\frac{a+b}{2}",
                             32, self.green).move_to(DOWN * 1.65)
        instance = self._math(
            rf"A=\frac{{5+11}}{{2}}={arithmetic_mean(5, 11):g}",
            33, self.orange).move_to(DOWN * 3.15)
        self.play(Write(formula), run_time=1.0)
        self.play(Write(instance), run_time=0.7)
        self.wait(1.2)
        self._clear()

    def scene_6_graphical_pattern(self):
        self._header("图像是离散点，而非连续线段")
        axes = Axes(x_range=[0, 8, 1], y_range=[0, 22, 5],
                    x_length=6.1, y_length=4.6, tips=False,
                    axis_config={"include_numbers": True, "font_size": 16,
                                 "color": self.muted}).move_to(UP * 0.2)
        n_label = self._math(r"n", 25).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        a_label = self._math(r"a_n", 25).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        dots = VGroup(*[Dot(axes.c2p(n, term(self.a1, self.d, n)), radius=0.085,
                            color=self.orange) for n in range(1, 8)])
        self.play(Create(axes), FadeIn(n_label), FadeIn(a_label), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots],
                              lag_ratio=0.16), run_time=1.6)
        # 参考虚线只表示各离散点共线，并非数列连续图像。
        guide = DashedLine(axes.c2p(1, self.terms[0]),
                           axes.c2p(7, self.terms[-1]),
                           color=self.green, stroke_width=2, dash_length=0.11)
        self.play(Create(guide), run_time=0.8)
        note = self._text("虚线辅助观察共线；实际图像只有整数下标处的点", 23, self.muted)
        note.move_to(DOWN * 4.1)
        relation = self._math(r"(n,a_n),\quad a_n=3n-1", 30, self.green)
        relation.move_to(DOWN * 5.25)
        self.play(FadeIn(note), Write(relation), run_time=1.0)
        self.wait(1.2)
        self._clear()

    def scene_7_properties(self):
        self._header("重要性质与应用")
        condition = self._math(r"m+n=p+q\ \Longrightarrow\ a_m+a_n=a_p+a_q",
                               30, self.green).move_to(UP * 3.65)
        note = self._text("四个下标均为正整数，且来自同一等差数列", 23, self.muted)
        note.move_to(UP * 2.45)
        example = self._math(r"a_3+a_5=8+14=22=a_2+a_6", 30, self.orange)
        example.move_to(UP * 1.1)
        self.play(Write(condition), FadeIn(note), run_time=1.0)
        self.play(Write(example), run_time=0.75)
        question = self._math(r"\text{另一数列：}\ a_3=7,\ a_7=15,\ a_5=?",
                              29).move_to(DOWN * 1.2)
        # 中文单独使用 Text；MathTex 仅书写纯 LaTeX 数学内容。
        question = VGroup(
            self._text("另一等差数列：", 24, self.muted),
            self._math(r"a_3=7,\ a_7=15,\ a_5=?", 29)
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 1.2)
        self._fit(question)
        answer = self._math(r"a_5=\frac{a_3+a_7}{2}=\frac{7+15}{2}=11",
                            30, self.green).move_to(DOWN * 2.9)
        self.play(FadeIn(question), run_time=0.65)
        self.play(Write(answer), run_time=1.0)
        self.wait(1.4)
        self._clear()

    def scene_8_outro(self):
        self._header("等差数列：四个核心结论")
        summary = VGroup(
            self._math(r"a_{n+1}-a_n=d\quad(n\geq1)", 30),
            self._math(r"a_n=a_1+(n-1)d", 33, self.green),
            self._math(r"S_n=\frac{n(a_1+a_n)}2", 33, self.green),
            self._math(r"A=\frac{a+b}{2}", 33, self.orange),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.65)
        for line in summary:
            self.play(Write(line), run_time=0.65)
        ending = self._text("下标是正整数；图像是离散点", 25, self.muted)
        ending.move_to(DOWN * 3.65)
        self.play(FadeIn(ending), run_time=0.6)
        self.wait(1.3)
        self._clear()
