"""六年级上：因数与倍数（9:16）。

manim -ql factors_multiples.py FactorsAndMultiples
manim -qh factors_multiples.py FactorsAndMultiples

本课将“正整数的正因数和正倍数”与“整数范围内的零倍数”分开叙述。
"""

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FactorsAndMultiples(Scene):
    PRIMARY = "#3498db"
    FACTOR = "#e74c3c"
    MULTIPLE = "#2ecc71"
    HIGHLIGHT = "#f39c12"
    SPECIAL = "#9b59b6"

    @staticmethod
    def positive_factors(number):
        """正整数的全部正因数；不把零当作有有限因数集合的对象。"""
        if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
            raise ValueError("number 必须是正整数")
        return tuple(i for i in range(1, number + 1) if number % i == 0)

    @staticmethod
    def first_positive_multiples(number, count):
        if (not isinstance(number, int) or isinstance(number, bool) or number <= 0
                or not isinstance(count, int) or isinstance(count, bool) or count <= 0):
            raise ValueError("number 和 count 必须是正整数")
        return tuple(number * i for i in range(1, count + 1))

    def text(self, value, size=30, color=WHITE):
        label = Text(value, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def math(self, latex, size=40, color=WHITE):
        label = MathTex(latex, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def finish(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.5)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self.text("上海初高中数学直通车 @emptyandcalm", 20, GRAY_B)
        self.author_info.move_to(UP * 7.15)
        self.play(FadeIn(self.author_info), run_time=0.4)
        self.show_opening()
        self.show_definition()
        self.show_find_factors()
        self.show_find_multiples()
        self.show_special_rules()
        self.show_summary()

    def show_opening(self):
        title = self.text("12 颗糖，可以平均分给几个人？", 35, self.HIGHLIGHT)
        title.move_to(UP * 5.35)
        candies = VGroup(*(
            Circle(radius=0.17, color=YELLOW, fill_color=GOLD, fill_opacity=0.95)
            for _ in range(12)
        )).arrange_in_grid(rows=2, cols=6, buff=0.25).move_to(UP * 2.6)
        hint = self.text("2 人、3 人、4 人、6 人都可以", 29).move_to(ORIGIN)
        question = self.text("怎样找出所有可行人数？", 29, self.PRIMARY).move_to(DOWN * 1.5)
        self.play(Write(title), FadeIn(candies), run_time=1.1)
        self.play(FadeIn(hint), FadeIn(question), run_time=0.7)
        self.wait(0.8)
        self.finish(title, candies, hint, question)

    def show_definition(self):
        title = self.text("因数与倍数", 42, self.PRIMARY).move_to(UP * 5.4)
        premise = self.text("先在正整数范围内讨论", 28, GRAY_A).move_to(UP * 3.9)
        equality = self.math(r"a=b\times q,\quad a,b,q\in\mathbb{Z}_{>0}", 36).move_to(UP * 2.4)
        factor = self.text("b 和 q 是 a 的因数", 32, self.FACTOR).move_to(UP * 0.5)
        multiple = self.text("a 是 b 和 q 的倍数", 32, self.MULTIPLE).move_to(DOWN * 1)
        example = self.math(r"12=3\times4", 43, self.HIGHLIGHT).move_to(DOWN * 2.8)
        self.play(Write(title), FadeIn(premise), run_time=0.8)
        self.play(Write(equality), run_time=0.8)
        self.play(FadeIn(factor), FadeIn(multiple), run_time=0.9)
        self.play(Write(example), run_time=0.6)
        self.wait(1)
        self.finish(title, premise, equality, factor, multiple, example)

    @staticmethod
    def factor_array(rows, cols, color):
        """每一幅数组恰含 rows×cols 个方块，按真实行列布局。"""
        return VGroup(*(
            Square(side_length=0.27, fill_color=color, fill_opacity=0.88,
                   stroke_color=WHITE, stroke_width=1)
            for _ in range(rows * cols)
        )).arrange_in_grid(rows=rows, cols=cols, buff=0.12)

    def show_find_factors(self):
        title = self.text("找出 12 的全部正因数", 38, self.FACTOR).move_to(UP * 5.35)
        intro = self.text("把 12 个方块排成长方形", 28).move_to(UP * 4.3)
        rows_and_cols = ((1, 12), (2, 6), (3, 4))
        layouts = VGroup()
        labels = VGroup()
        for (rows, cols), y in zip(rows_and_cols, (2.95, 0.35, -2.4)):
            layout = self.factor_array(rows, cols, self.FACTOR).move_to((0, y, 0))
            label = self.math(fr"{rows}\times{cols}=12", 32).next_to(layout, DOWN, buff=0.24)
            layouts.add(layout)
            labels.add(label)
        answer = self.math(r"1,\ 2,\ 3,\ 4,\ 6,\ 12", 40, self.HIGHLIGHT)
        answer.move_to(DOWN * 4.55)
        self.play(Write(title), FadeIn(intro), run_time=0.9)
        for layout, label in zip(layouts, labels):
            self.play(FadeIn(layout), Write(label), run_time=0.8)
        self.play(Write(answer), run_time=0.7)
        self.wait(1)
        self.finish(title, intro, layouts, labels, answer)

    def show_find_multiples(self):
        title = self.text("找 3 的正倍数", 41, self.MULTIPLE).move_to(UP * 5.4)
        intro = self.math(r"3,\ 6,\ 9,\ 12,\ 15,\ 18,\ldots", 36).move_to(UP * 3.8)
        line = NumberLine(
            x_range=[0, 21, 3], length=6.8, include_numbers=True,
            font_size=22, label_direction=DOWN,
        ).move_to(UP * 1.1)
        dots = VGroup(*(
            Dot(line.n2p(m), color=self.MULTIPLE, radius=0.10)
            for m in self.first_positive_multiples(3, 6)
        ))
        arrow = Arrow(line.get_right() + RIGHT * 0.07,
                      line.get_right() + RIGHT * 0.55,
                      buff=0, color=self.MULTIPLE, stroke_width=4)
        note = self.text("每次加 3，还能得到更大的正倍数", 27, self.HIGHLIGHT)
        note.move_to(DOWN * 1.5)
        conclusion = self.text("3 的正倍数有无限多个", 30, self.MULTIPLE).move_to(DOWN * 3)
        self.play(Write(title), Write(intro), run_time=0.9)
        self.play(Create(line), run_time=0.9)
        self.play(FadeIn(dots), GrowArrow(arrow), run_time=0.8)
        self.play(FadeIn(note), FadeIn(conclusion), run_time=0.8)
        self.wait(1)
        self.finish(title, intro, dots, arrow, line, note, conclusion)

    def show_special_rules(self):
        title = self.text("特殊规律：看清讨论范围", 38, self.SPECIAL).move_to(UP * 5.3)
        positive = self.text("对于任意正整数 n", 30, self.HIGHLIGHT).move_to(UP * 3.9)
        one = self.math(r"n=1\times n", 43).move_to(UP * 2.65)
        rule_one = self.text("1 是 n 的因数；n 也是自身的因数", 27, self.FACTOR).move_to(UP * 1.35)
        integer_domain = self.text("回到整数范围：b 是非零整数", 28, self.HIGHLIGHT).move_to(DOWN * 0.5)
        zero = self.math(r"0=b\times 0,\quad b\ne0", 42).move_to(DOWN * 1.7)
        rule_zero = self.text("因此 0 是每个非零整数的倍数", 28, self.MULTIPLE).move_to(DOWN * 3)
        caution = self.text("0 不是正倍数，不参与上一镜的正倍数列表", 25, GRAY_A)
        caution.move_to(DOWN * 4.25)
        self.play(Write(title), FadeIn(positive), run_time=0.8)
        self.play(Write(one), FadeIn(rule_one), run_time=0.8)
        self.play(FadeIn(integer_domain), Write(zero), run_time=0.9)
        self.play(FadeIn(rule_zero), FadeIn(caution), run_time=0.7)
        self.wait(1)
        self.finish(title, positive, one, rule_one, integer_domain, zero, rule_zero, caution)

    def show_summary(self):
        title = self.text("知识总结", 42, self.PRIMARY).move_to(UP * 5.4)
        context = self.text("对于正整数 n，只看它的正因数与正倍数", 28)
        context.move_to(UP * 3.9)
        rules = VGroup(
            self.text("正因数：有限个；最小 1，最大 n", 28, self.FACTOR),
            self.text("正倍数：无限个；最小 n", 28, self.MULTIPLE),
            self.text("整除关系要明确：谁是谁的因数？", 27),
        ).arrange(DOWN, buff=0.8).move_to(UP * 1.05)
        integer_extension = self.text("补充：0 是任意非零整数的整数倍数", 27, self.SPECIAL)
        integer_extension.move_to(DOWN * 2.2)
        signature = self.text("上海初高中数学直通车", 30).move_to(DOWN * 4)
        self.play(Write(title), FadeIn(context), run_time=0.8)
        for rule in rules:
            self.play(FadeIn(rule), run_time=0.5)
        self.play(FadeIn(integer_extension), FadeIn(signature), run_time=0.8)
        self.wait(1)
        self.finish(title, context, rules, integer_extension, signature, self.author_info)
