"""六年级有理数的意义：整数、分数与可写为整数比的小数。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def rational_fraction(numerator: int, denominator: int):
    """以非零整数分母表示有理数，自动约分、规范符号。"""
    from fractions import Fraction

    if any(type(n) is not int for n in (numerator, denominator)) or denominator == 0:
        raise ValueError("分子分母须为整数，且分母不能为零")
    return Fraction(numerator, denominator)


def pure_repeating_decimal(repetend: str):
    """0.循环节循环节... 的确切分数，如 0.(3)=1/3，0.(12)=4/33。"""
    from fractions import Fraction

    if (not isinstance(repetend, str) or not repetend or not repetend.isascii()
            or not repetend.isdecimal()):
        raise ValueError("循环节须为非空阿拉伯数字字符串")
    return Fraction(int(repetend), 10 ** len(repetend) - 1)


class Topic001有理数的意义Animation(Scene):
    """统一有理数的正负整数、分数、有限和循环小数表达。"""

    def construct(self):
        assert rational_fraction(-2, 1) == -2
        assert rational_fraction(3, 4) == rational_fraction(75, 100)
        assert pure_repeating_decimal("3") == rational_fraction(1, 3)
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.why_negative_numbers()
        self.definition_and_categories()
        self.decimals()
        self.summary()

    def transition(self):
        self.play(*[
            FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark
        ], run_time=0.3)

    def heading(self, title):
        text = Text(title, font_size=37, color=GOLD).move_to(UP * 5.65)
        self.play(Write(text))
        return text

    def opening(self):
        title = Text("有理数的意义", font_size=46).move_to(UP * 3)
        text = Text("整数和分数有什么共同点？", font_size=29, color=BLUE_ACCENT)
        text.next_to(title, DOWN, buff=0.5)
        self.play(Write(title), FadeIn(text))
        self.wait(0.6)
        self.transition()

    def why_negative_numbers(self):
        self.heading("正负数表达相反意义")
        number_line = NumberLine(
            x_range=[-4, 4, 1], length=7.3, include_numbers=True
        ).move_to(UP * 1.0)
        self.play(Create(number_line))
        left = Dot(number_line.n2p(-2), color=BLUE_ACCENT, radius=0.13)
        right = Dot(number_line.n2p(2), color=GOLD, radius=0.13)
        self.play(FadeIn(left), FadeIn(right))
        labels = VGroup(
            Text("-2：表示下降 2 米", font_size=28, color=BLUE_ACCENT),
            Text("+2：表示上升 2 米", font_size=28, color=GOLD),
            Text("0：正负数的分界", font_size=27),
        ).arrange(DOWN, buff=0.47).move_to(DOWN * 2)
        for row in labels:
            self.play(FadeIn(row), run_time=0.45)
        self.wait(0.7)
        self.transition()

    def definition_and_categories(self):
        self.heading("所有有理数都能写成分数")
        formula = MathTex(
            r"\frac{p}{q},\quad p,q\in\mathbb{Z},\quad q\ne0",
            font_size=43, color=GOLD
        ).move_to(UP * 3.4)
        self.play(Write(formula))
        examples = VGroup(
            Text("整数：正整数、零、负整数", font_size=29, color=BLUE_ACCENT),
            MathTex(r"-2=\frac{-2}{1},\quad 0=\frac{0}{1}", font_size=40),
            Text("分数：正分数和负分数", font_size=29, color=GREEN_ACCENT),
            MathTex(r"\frac34,\quad-\frac52", font_size=42),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 0.4)
        for row in examples:
            self.play(FadeIn(row), run_time=0.45)
        self.wait(0.7)
        self.transition()

    def decimals(self):
        self.heading("小数也能表示为分数")
        finite = VGroup(
            Text("有限小数", font_size=28, color=BLUE_ACCENT),
            MathTex(r"0.125=\frac18", font_size=48, color=GOLD),
        ).arrange(DOWN, buff=0.2).move_to(UP * 2.4)
        repeated = VGroup(
            Text("无限循环小数", font_size=28, color=BLUE_ACCENT),
            MathTex(r"0.\overline{3}=\frac13", font_size=48, color=GREEN_ACCENT),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 0.8)
        self.play(FadeIn(finite), run_time=0.7)
        self.play(FadeIn(repeated), run_time=0.7)
        note = Text("不是所有无限小数都是有理数", font_size=26)
        note.move_to(DOWN * 3.5)
        self.play(Write(note))
        self.wait(0.8)
        self.transition()

    def summary(self):
        self.heading("有理数的分类")
        groups = VGroup(
            Text("有理数", font_size=38, color=GOLD),
            Text("整数：正整数、0、负整数", font_size=28),
            Text("分数：正分数、负分数", font_size=28),
            Text("有限小数和循环小数也能写成分数", font_size=25, color=GREEN_ACCENT),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.8)
        for row in groups:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1)
