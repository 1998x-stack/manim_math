"""六年级：二元一次方程组。加减消元与代入消元并行展示。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def solve_linear_system(a, b, c, d, e, f):
    """精确求解 ax+by=c, dx+ey=f；无唯一解时明确拒绝。"""
    from fractions import Fraction

    values = (a, b, c, d, e, f)
    if any(type(value) not in (int, Fraction) for value in values):
        raise ValueError("系数必须是整数或 Fraction")
    determinant = a * e - b * d
    if determinant == 0:
        raise ValueError("行列式为零，不能得到唯一解")
    return (
        Fraction(c * e - b * f, determinant),
        Fraction(a * f - c * d, determinant)
    )


class Topic002二元一次方程组Animation(Scene):
    """用相同的方程组展示加减消元和代入消元。"""

    def construct(self):
        assert solve_linear_system(1, 1, 5, 1, -1, 1) == (3, 2)
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.elimination()
        self.substitution()
        self.check_and_summary()

    def transition(self):
        self.play(
            *[FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark],
            run_time=0.35
        )

    def heading(self, words):
        title = Text(words, font_size=37, color=GOLD).move_to(UP * 5.6)
        self.play(Write(title))
        return title

    def opening(self):
        title = Text("二元一次方程组", font_size=46).move_to(UP * 4)
        self.play(Write(title))
        system = MathTex(
            r"\begin{cases}x+y=5\\x-y=1\end{cases}",
            font_size=54, color=BLUE_ACCENT
        ).move_to(UP * 1)
        self.play(Write(system))
        hint = Text("两式必须同时成立", font_size=29, color=WHITE).move_to(DOWN * 2)
        self.play(FadeIn(hint))
        self.wait(0.7)
        self.transition()

    def elimination(self):
        self.heading("方法一：加减消元")
        system = MathTex(
            r"\begin{cases}x+y=5\\x-y=1\end{cases}",
            font_size=44
        ).move_to(UP * 3)
        self.play(Write(system))
        sequence = [
            ("左右两式相加，消去 y", r"2x=6"),
            ("两边除以 2", r"x=3"),
            ("代回 x+y=5", r"3+y=5"),
            ("求出 y", r"y=2"),
        ]
        active = None
        text = None
        for label, formula in sequence:
            if active is not None:
                self.play(FadeOut(active), FadeOut(text), run_time=0.2)
            text = Text(label, font_size=26, color=WHITE).move_to(UP * 0.7)
            active = MathTex(formula, font_size=51, color=GOLD).move_to(DOWN * 0.6)
            self.play(FadeIn(text), Write(active), run_time=0.5)
            self.wait(0.35)
        answer = MathTex(r"(x,y)=(3,2)", font_size=42, color=GREEN_ACCENT)
        answer.move_to(DOWN * 3.2)
        self.play(Write(answer))
        self.wait(0.6)
        self.transition()

    def substitution(self):
        self.heading("方法二：代入消元")
        stages = [
            ("从第一式得到", r"y=5-x"),
            ("将 y 代入第二式", r"x-(5-x)=1"),
            ("合并同类项", r"2x-5=1"),
            ("求得 x，再求 y", r"x=3,\quad y=2"),
        ]
        explanation = None
        formula = None
        for message, tex in stages:
            if formula is not None:
                self.play(FadeOut(formula), FadeOut(explanation), run_time=0.2)
            explanation = Text(message, font_size=28, color=BLUE_ACCENT).move_to(UP * 2.5)
            formula = MathTex(tex, font_size=48, color=GOLD).move_to(UP * 0.8)
            self.play(Write(formula), FadeIn(explanation), run_time=0.6)
            self.wait(0.4)
        remark = Text("两种方法都在消去一个未知数", font_size=27)
        remark.move_to(DOWN * 2.7)
        self.play(FadeIn(remark))
        self.wait(0.8)
        self.transition()

    def check_and_summary(self):
        self.heading("把答案代入两式")
        check1 = MathTex(r"3+2=5", font_size=48, color=GREEN_ACCENT)
        check2 = MathTex(r"3-2=1", font_size=48, color=GREEN_ACCENT)
        group = VGroup(check1, check2).arrange(DOWN, buff=0.7).move_to(UP * 1)
        self.play(LaggedStart(*(Write(item) for item in group), lag_ratio=0.4))
        rule = Text("加减消元、代入消元，最后都要检验", font_size=26)
        rule.move_to(DOWN * 2.5)
        self.play(Write(rule))
        self.wait(1)
