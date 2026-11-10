"""六年级：一元一次方程的解法。去分母、去括号、移项、检验。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def solve_fraction_equation(a, b, c):
    """求 ax+b=c 的精确解，a、b、c 只能是整数或有理数。"""
    from fractions import Fraction

    values = (a, b, c)
    if any(type(value) not in (int, Fraction) for value in values):
        raise ValueError("只接受精确整数或 Fraction")
    if a == 0:
        raise ValueError("x 的系数不可为零")
    return (Fraction(c) - Fraction(b)) / Fraction(a)


class Topic001一元一次方程的解法Animation(Scene):
    """用两道分步例题解释解方程与恒等变形。"""

    def construct(self):
        from fractions import Fraction
        assert solve_fraction_equation(Fraction(1, 2), Fraction(1, 3), Fraction(5, 6)) == 1
        assert solve_fraction_equation(2, 1, 9) == 4
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm", font_size=17,
            color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.fraction_example()
        self.bracket_example()
        self.summary()

    def transition(self):
        self.play(
            *[FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark],
            run_time=0.35
        )

    def header(self, section):
        heading = Text(section, font_size=37, color=GOLD).move_to(UP * 5.65)
        self.play(Write(heading), run_time=0.5)
        return heading

    def opening(self):
        title = Text("一元一次方程的解法", font_size=45, color=WHITE).move_to(UP * 3)
        desc = Text("目标：每步都保持等式成立", font_size=29, color=BLUE_ACCENT)
        desc.next_to(title, DOWN, buff=0.5)
        self.play(Write(title), FadeIn(desc, shift=UP * 0.2))
        self.wait(0.6)
        self.transition()

    def fraction_example(self):
        self.header("例一：去分母")
        original = MathTex(
            r"\frac{x}{2}+\frac{1}{3}=\frac{5}{6}",
            font_size=48
        ).move_to(UP * 3.7)
        self.play(Write(original))
        hint = Text("2、3、6 的最小公倍数是 6", font_size=27, color=BLUE_ACCENT)
        hint.move_to(UP * 2.1)
        self.play(FadeIn(hint))
        steps = [
            ("方程两边同时乘以 6", r"3x+2=5"),
            ("两边同时减去 2", r"3x=3"),
            ("两边同时除以 3", r"x=1"),
        ]
        current = None
        reason = None
        for message, expression in steps:
            if current is not None:
                self.play(FadeOut(current), FadeOut(reason), run_time=0.2)
            reason = Text(message, font_size=27, color=WHITE).move_to(UP * 0.4)
            current = MathTex(expression, font_size=51, color=GOLD).move_to(DOWN * 0.6)
            self.play(FadeIn(reason), Write(current), run_time=0.6)
            self.wait(0.35)
        verification = MathTex(
            r"\frac{1}{2}+\frac{1}{3}=\frac{5}{6}",
            font_size=42, color=GREEN_ACCENT
        ).move_to(DOWN * 3)
        check = Text("代回原方程：左右相等", font_size=26, color=GREEN_ACCENT)
        check.next_to(verification, UP, buff=0.3)
        self.play(Write(verification), FadeIn(check))
        self.wait(0.8)
        self.transition()

    def bracket_example(self):
        self.header("例二：去括号、移项")
        original = MathTex(r"2(x-1)+3=9", font_size=50).move_to(UP * 3.7)
        self.play(Write(original))
        stages = [
            ("用分配律去括号", r"2x-2+3=9"),
            ("合并同类项", r"2x+1=9"),
            ("移项，等式两边减 1", r"2x=8"),
            ("系数化为 1", r"x=4"),
        ]
        active = None
        message = None
        for label, formula in stages:
            if active is not None:
                self.play(FadeOut(active), FadeOut(message), run_time=0.2)
            message = Text(label, font_size=26, color=BLUE_ACCENT).move_to(UP * 1)
            active = MathTex(formula, font_size=48, color=GOLD).move_to(ORIGIN)
            self.play(FadeIn(message), Write(active), run_time=0.55)
            self.wait(0.3)
        verification = MathTex(r"2(4-1)+3=9", font_size=44, color=GREEN_ACCENT)
        verification.move_to(DOWN * 2.6)
        self.play(Write(verification))
        self.wait(0.7)
        self.transition()

    def summary(self):
        self.header("解题顺序")
        points = [
            "去分母：两边同乘非零公倍数",
            "去括号：用分配律",
            "移项、合并同类项",
            "系数化为 1，最后代回检验",
        ]
        group = VGroup(*[
            Text(f"{i + 1}. {point}", font_size=27, color=WHITE)
            for i, point in enumerate(points)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(UP * 0.8)
        for row in group:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.35)
        result = Text("每一步都要保持等式成立", font_size=29, color=GREEN_ACCENT)
        result.move_to(DOWN * 3.4)
        self.play(Write(result))
        self.wait(1)
