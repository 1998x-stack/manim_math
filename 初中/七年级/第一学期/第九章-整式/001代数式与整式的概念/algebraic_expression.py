"""七年级第一学期：代数式与整式的概念。

七个教学镜头，保留历史 Scene 入口 AlgebraicExpressionConcept。
中文使用 Text，数学公式使用 MathTex；竖屏逻辑尺寸 9×16。
运行：manim -pql algebraic_expression.py AlgebraicExpressionConcept
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE_C = "#3498db"
RED_C = "#e74c3c"
GREEN_C = "#2ecc71"
ORANGE_C = "#f39c12"
PURPLE_C = "#9b59b6"


class AlgebraicExpressionConcept(Scene):
    """从数与字母的表达式逐步建立单项式、多项式、整式的概念。"""

    @staticmethod
    def fit(mob, width=7.5):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, content, color=WHITE):
        return self.fit(Text(content, font_size=40, color=color)).move_to(UP * 5.8)

    def caption(self, content, position=DOWN * 3.5, color=GRAY_A):
        return self.fit(Text(content, font_size=26, color=color)).move_to(position)

    def clear_content(self):
        """保留固定署名，清理当前镜头中实际存在的对象。"""
        remaining = [mob for mob in self.mobjects if mob is not self.author_info]
        if remaining:
            self.play(*[FadeOut(mob) for mob in remaining], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.7)
        self.add(self.author_info)
        self.show_opening()
        self.show_algebraic_expression()
        self.show_monomial_definition()
        self.show_monomial_properties()
        self.show_polynomial()
        self.show_wholestyle_summary()
        self.show_outro()

    def show_opening(self):
        title = self.heading("数学式子的秘密", YELLOW)
        examples = VGroup(
            MathTex("3+5", color=WHITE),
            MathTex("a+b", color=BLUE_C),
            MathTex("3x^2y", color=RED_C),
            MathTex("2x^2+3x-1", color=GREEN_C),
        ).arrange(DOWN, buff=0.65).move_to(UP * 1.2)
        question = self.caption("它们之间有什么关系？", DOWN * 3.7, YELLOW)
        self.play(Write(title), run_time=0.7)
        for example in examples:
            self.play(FadeIn(example, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(1)
        self.clear_content()

    def show_algebraic_expression(self):
        title = self.heading("代数式", BLUE_C)
        definition = self.caption(
            "数、字母及其通过运算组成的式子", UP * 3.6
        )
        concrete = MathTex("3", "+", "5", font_size=56).move_to(UP * 1.5)
        abstract = MathTex("a", "+", "b", font_size=56, color=BLUE_C)
        abstract.move_to(DOWN * 0.3)
        operator = SurroundingRectangle(abstract[1], color=YELLOW, buff=0.12)
        label = self.caption("运算符号：加、减、乘、除、乘方等", DOWN * 2.0)
        examples = self.fit(MathTex(r"2x-y\qquad x^2+1\qquad \frac{1}{x}", font_size=34))
        examples.move_to(DOWN * 4.5)
        condition = self.caption("1/x 是代数式，但 x 不能等于 0", DOWN * 5.55, YELLOW)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(Write(concrete), run_time=0.55)
        self.play(TransformFromCopy(concrete, abstract), run_time=0.75)
        self.play(Create(operator), FadeIn(label), run_time=0.6)
        self.play(FadeIn(examples), FadeIn(condition), run_time=0.65)
        self.wait(1)
        self.clear_content()

    def show_monomial_definition(self):
        title = self.heading("单项式", RED_C)
        definition = self.caption(
            "数与字母的乘积；单独的数或字母也算", UP * 3.7
        )
        mono = MathTex("3", "x^2", "y", font_size=66, color=RED_C)
        mono.move_to(UP * 1.2)
        number_box = SurroundingRectangle(mono[0], color=ORANGE_C, buff=0.12)
        letters_box = SurroundingRectangle(VGroup(mono[1], mono[2]), color=BLUE_C, buff=0.12)
        coefficient = self.caption("数字因数：3", DOWN * 1.1, ORANGE_C)
        letters = self.caption("字母部分：x²y", DOWN * 2.1, BLUE_C)
        other = self.fit(MathTex("5", "\u00a0\u00a0", "x", "\u00a0\u00a0", "-2ab", font_size=38))
        # 数字、单独字母及数与字母的乘积都是单项式。
        other = self.fit(MathTex(r"5\qquad x\qquad -2ab", font_size=38))
        other.move_to(DOWN * 4.1)
        non_example = self.caption("x+1 是两个单项式的和，不是单项式", DOWN * 5.3, YELLOW)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(Write(mono), run_time=0.65)
        self.play(Create(number_box), FadeIn(coefficient), run_time=0.55)
        self.play(ReplacementTransform(number_box, letters_box), FadeIn(letters), run_time=0.55)
        self.play(FadeIn(other), FadeIn(non_example), run_time=0.6)
        self.wait(1)
        self.clear_content()

    def show_monomial_properties(self):
        title = self.heading("单项式的系数与次数", PURPLE_C)
        mono = MathTex("3", "x^2", "y", font_size=65, color=RED_C)
        mono.move_to(UP * 2.8)
        coefficient = self.caption("系数：数字因数 3", UP * 0.6, ORANGE_C)
        degree = MathTex(r"2+1=3", font_size=52, color=PURPLE_C).move_to(DOWN * 1.2)
        explanation = self.caption("次数：所有字母的指数之和", DOWN * 2.5)
        examples = VGroup(
            MathTex(r"-5a^3b:\quad -5,\ 4", font_size=34),
            MathTex(r"xy^2z^3:\quad 1,\ 6", font_size=34),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 4.3)
        note = self.caption("上方例子依次给出系数与次数", DOWN * 5.75, YELLOW)
        self.play(Write(title), Write(mono), run_time=0.85)
        self.play(Circumscribe(mono[0], color=ORANGE_C), FadeIn(coefficient))
        self.play(Circumscribe(VGroup(mono[1], mono[2]), color=PURPLE_C), Write(degree))
        self.play(FadeIn(explanation), run_time=0.5)
        for example in examples:
            self.play(FadeIn(example, shift=UP * 0.15), run_time=0.4)
        self.play(FadeIn(note), run_time=0.35)
        self.wait(1)
        self.clear_content()

    def show_polynomial(self):
        title = self.heading("多项式", GREEN_C)
        polynomial = MathTex(r"2x^2+3x-1", font_size=57, color=GREEN_C)
        polynomial.move_to(UP * 3.3)
        # 三项的符号归属于对应项，-1 不是 +1。
        terms = VGroup(
            MathTex(r"2x^2", font_size=42, color=RED_C),
            MathTex(r"+3x", font_size=42, color=RED_C),
            MathTex(r"-1", font_size=42, color=RED_C),
        ).arrange(RIGHT, buff=0.45).move_to(UP * 0.7)
        boxes = VGroup(*[SurroundingRectangle(term, color=ORANGE_C, buff=0.13) for term in terms])
        labels = VGroup(*[
            self.fit(Text("单项式", font_size=21, color=GRAY_A))
            .next_to(term, DOWN, buff=0.35) for term in terms
        ])
        definition = self.caption("几个单项式的和，叫作多项式", DOWN * 2.1)
        degree = self.caption("三项，二次：最高次项 2x² 的次数为 2", DOWN * 3.6, YELLOW)
        self.play(Write(title), Write(polynomial), run_time=1.1)
        for term, box, label in zip(terms, boxes, labels):
            self.play(FadeIn(term), Create(box), FadeIn(label), run_time=0.55)
        self.play(FadeIn(definition), FadeIn(degree), run_time=0.6)
        self.wait(1)
        self.clear_content()

    def show_wholestyle_summary(self):
        title = self.heading("整式：单项式与多项式", GOLD)
        outline = RoundedRectangle(width=7.6, height=7.5, corner_radius=0.2, color=GOLD)
        outline.move_to(UP * 0.3)
        # 两张卡片边框互不重叠：中心相距 3.8，宽度均为 3.5。
        card_data = (
            ("单项式", r"3x^2y", RED_C, -1.9),
            ("多项式", r"2x^2+3x-1", GREEN_C, 1.9),
        )
        cards = VGroup()
        for name, example, color, x_pos in card_data:
            box = RoundedRectangle(
                width=3.5, height=2.6, corner_radius=0.15,
                stroke_color=color, fill_color=color, fill_opacity=0.12
            )
            label = Text(name, font_size=28, color=color).move_to(box.get_center() + UP * 0.65)
            formula = self.fit(MathTex(example, font_size=36, color=color), width=3.1)
            formula.move_to(box.get_center() + DOWN * 0.45)
            card = VGroup(box, label, formula).move_to([x_pos, 0.9, 0])
            cards.add(card)
        note = self.caption("整式中，字母不能出现在分母里", DOWN * 3.7, YELLOW)
        counterexample = MathTex(r"\frac{1}{x}\quad (x\ne0)", font_size=42)
        counterexample.move_to(DOWN * 4.7)
        counter_note = self.caption("这是分式，不是整式", DOWN * 5.65)
        self.play(Write(title), Create(outline), run_time=0.8)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(note), Write(counterexample), FadeIn(counter_note), run_time=0.9)
        self.wait(1.2)
        self.clear_content()

    def show_outro(self):
        title = self.heading("回顾三个概念", YELLOW)
        rows = VGroup(*[
            self.fit(Text(item, font_size=33, color=color))
            for item, color in (
                ("代数式：用数、字母和运算表示", BLUE_C),
                ("单项式：数与字母的乘积", RED_C),
                ("多项式：单项式的和", GREEN_C),
            )
        ]).arrange(DOWN, buff=0.65).move_to(UP * 0.65)
        reminder = self.caption("整式包括单项式和多项式", DOWN * 3.9, GOLD)
        self.play(Write(title), run_time=0.65)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(reminder), run_time=0.55)
        self.wait(1.7)
        self.clear_content()
        self.play(FadeOut(self.author_info), run_time=0.3)
