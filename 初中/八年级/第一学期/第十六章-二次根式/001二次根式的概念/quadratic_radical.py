"""二次根式的概念：八年级第一学期，第十六章。

运行：manim -pql quadratic_radical.py QuadraticRadical
保留原有 Scene 入口及 9:16 画幅；中文交由 Text，数学公式交由 MathTex。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def real_sqrt_defined(a):
    """实数范围内，有限被开方数的算术平方根何时有意义。"""
    return isinstance(a, (int, float)) and math.isfinite(a) and a >= 0


def x_plus_one_domain(x):
    """sqrt(x+1) 的实数定义域判定。"""
    return real_sqrt_defined(x + 1)


class QuadraticRadical(Scene):
    FONT = "PingFang SC"
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    VALID = "#22a6b3"
    INVALID = "#eb4d4b"
    RULE = "#a29bfe"
    GREEN = "#6ab04c"

    def construct(self):
        self.camera.background_color = self.BG
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 6.8)
        self.play(FadeIn(self.author), run_time=0.3)
        self.scene_opening()
        self.scene_definition()
        self.scene_condition()
        self.scene_examples()
        self.scene_double_nonneg()
        self.scene_summary()
        self.scene_outro()

    def text(self, value, y, *, size=30, color=WHITE):
        return Text(value, font=self.FONT, font_size=size, color=color).move_to(UP * y)

    def formula(self, value, y, *, size=44, color=WHITE):
        return MathTex(value, font_size=size, color=color).move_to(UP * y)

    def clear_content(self):
        """淡出当前实际显示的对象，保留同一个作者水印引用。"""
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(*[FadeOut(obj) for obj in visible], run_time=0.45)

    def card(self, y, expression, explanation, *, color=WHITE):
        border = RoundedRectangle(
            width=7.4, height=1.55, corner_radius=0.2,
            stroke_width=2, color=color, fill_color="#16213e", fill_opacity=0.8,
        ).move_to(UP * y)
        content = VGroup(
            MathTex(expression, color=color, font_size=38),
            Text(explanation, font=self.FONT, font_size=23, color=WHITE),
        ).arrange(RIGHT, buff=0.4).move_to(UP * y)
        if content.width > 6.9:
            content.scale(6.9 / content.width)
        self.play(Create(border), FadeIn(content), run_time=0.55)

    def scene_opening(self):
        title = self.text("二次根式的概念", 5.5, size=47, color=self.TITLE)
        question = self.text("根号里的数可以是负数吗？", 3.9, size=31)
        example = self.formula(r"\sqrt{-4}\;?", 1.5, size=80, color=self.INVALID)
        self.play(Write(title), FadeIn(question), run_time=0.8)
        self.play(Write(example), run_time=0.65)
        self.wait(0.9)
        self.clear_content()

    def scene_definition(self):
        title = self.text("什么是二次根式？", 5.5, size=41, color=self.TITLE)
        root = self.formula(r"\sqrt{a}", 3.3, size=92, color=self.GREEN)
        condition = self.formula(r"a\geq 0", 1.7, size=49, color=self.VALID)
        description = self.text("在实数范围内，形如根号 a 的式子", -0.1, size=29)
        definition = self.text("当被开方数 a 非负时，叫做二次根式", -1.2,
                               size=27, color=self.TITLE)
        note = self.text("根号表示非负的算术平方根", -2.8, size=26, color=GRAY_A)
        self.play(Write(title), Write(root), run_time=0.9)
        self.play(Write(condition), FadeIn(description), FadeIn(definition), run_time=0.9)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.8)
        self.clear_content()

    def scene_condition(self):
        title = self.text("有意义的条件", 5.6, size=42, color=self.TITLE)
        subtitle = self.text("以下结论都在实数范围内讨论", 4.7, size=24, color=GRAY_A)
        self.play(Write(title), FadeIn(subtitle), run_time=0.65)
        self.card(3.15, r"\sqrt{4}=2", "被开方数为正：有意义", color=self.VALID)
        self.card(1.15, r"\sqrt{0}=0", "零也在定义域内", color=self.VALID)
        self.card(-0.85, r"\sqrt{-4}", "被开方数为负：无意义", color=self.INVALID)
        rule_label = self.text("根式有意义，当且仅当", -3.0,
                               size=28, color=self.TITLE)
        rule_formula = self.formula(r"a\geq0", -4.0, size=54, color=self.GREEN)
        self.play(Write(rule_label), Write(rule_formula), run_time=0.8)
        self.wait(1.0)
        self.clear_content()

    def scene_examples(self):
        title = self.text("先看被开方数，再判断", 5.7, size=40, color=self.TITLE)
        self.play(Write(title), run_time=0.5)
        for y, a in zip((4.2, 2.25, 0.3), (5, 0, -3)):
            defined = real_sqrt_defined(a)
            self.card(
                y, rf"\sqrt{{{a}}}",
                "实数范围内有意义" if defined else "实数范围内无意义",
                color=self.VALID if defined else self.INVALID,
            )
        variable = self.formula(r"\sqrt{x+1}", -1.65, size=49, color=self.TITLE)
        inequality = self.formula(r"x+1\geq0\;\Longleftrightarrow\;x\geq-1",
                                  -3.15, size=36, color=self.VALID)
        domain = self.text("x = -1 可以取；x < -1 不可以取", -4.35,
                           size=25, color=WHITE)
        self.play(Write(variable), run_time=0.45)
        self.play(Write(inequality), FadeIn(domain), run_time=0.8)
        self.wait(1.0)
        self.clear_content()

    def scene_double_nonneg(self):
        title = self.text("双重非负性", 5.6, size=44, color=self.TITLE)
        premise = self.text("前提：根式在实数范围内有意义", 4.5, size=26)
        radicand = self.formula(r"a\geq0", 2.65, size=58, color=self.VALID)
        value = self.formula(r"\sqrt{a}\geq0", 0.95, size=58, color=self.RULE)
        identity = self.formula(r"\sqrt{a}=0\;\Longleftrightarrow\;a=0",
                                -1.35, size=42, color=self.GREEN)
        meaning = self.text("根式的值是非负的算术平方根", -2.75,
                            size=27, color=WHITE)
        self.play(Write(title), FadeIn(premise), run_time=0.65)
        self.play(Write(radicand), Write(value), run_time=0.8)
        self.play(Write(identity), FadeIn(meaning), run_time=0.8)
        self.wait(1.0)
        self.clear_content()

    def scene_summary(self):
        title = self.text("用数轴观察定义域", 5.8, size=40, color=self.TITLE)
        axis = NumberLine(x_range=[-4, 4, 1], length=6.9,
                          include_numbers=True, color=WHITE).move_to(UP * 3.35)
        # 红色仅表示 a<0；端点留出视觉间隙，绿色实心点独占 a=0。
        negative = Line(axis.n2p(-3.7), axis.n2p(-0.12),
                        color=self.INVALID, stroke_width=8)
        nonnegative = Line(axis.n2p(0), axis.n2p(3.7),
                           color=self.VALID, stroke_width=8)
        zero = Dot(axis.n2p(0), color=self.VALID, radius=0.11)
        labels = VGroup(
            self.text("红色：a < 0，在实数范围内无意义", 1.5,
                      size=25, color=self.INVALID),
            self.text("绿色：a ≥ 0，包含零，有意义", 0.4,
                      size=25, color=self.VALID),
        )
        conclusion = self.formula(r"a\geq0,\qquad\sqrt{a}\geq0",
                                  -2.05, size=45, color=self.TITLE)
        self.play(Write(title), Create(axis), run_time=0.95)
        self.play(Create(negative), Create(nonnegative), FadeIn(zero),
                  run_time=0.8)
        self.play(FadeIn(labels), Write(conclusion), run_time=0.8)
        self.wait(1.2)
        self.clear_content()

    def scene_outro(self):
        author_big = self.text("上海初高中数学直通车", 2.6, size=38)
        self.play(Transform(self.author, author_big), run_time=0.7)
        ending = self.text("记住：零也可以放进根号里！", 0.55,
                           size=32, color=self.TITLE)
        final_formula = self.formula(r"\sqrt{0}=0", -1.1,
                                     size=62, color=self.VALID)
        self.play(FadeIn(ending), Write(final_formula), run_time=0.75)
        self.wait(1.0)
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.6)
