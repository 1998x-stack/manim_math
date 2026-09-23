"""二年级下册《运算顺序》：竖屏逐步计算教学动画。

教学目标：同级运算从左到右；先乘除后加减；有括号先算括号。
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001运算顺序Animation(Scene):
    """展示具体计算依据，不使用与运算无关的占位圆形或正方形。"""

    EXAMPLES = (
        ("同级运算：从左往右", r"5+3-2", r"8-2", r"6", "先算5+3，再减2"),
        ("先乘除，后加减", r"5+3\times2", r"5+6", r"11", "先算3×2，再加5"),
        ("有括号，先算括号", r"(5+3)\times2", r"8\times2", r"16", "先算括号里面的5+3"),
    )

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=19, color=GRAY_B)
        author.move_to(UP * 7.25)
        title = Text("运算顺序", font_size=48, color=GOLD).move_to(UP * 5.9)
        self.play(FadeIn(author), Write(title), run_time=0.8)
        self.wait(0.5)

        for heading, original, reduced, result, explanation in self.EXAMPLES:
            self.show_worked_example(heading, original, reduced, result, explanation)

        rules = VGroup(
            Text("同级运算，从左到右", font_size=30),
            Text("先乘除，后加减", font_size=30),
            Text("有括号，先算括号里面", font_size=30),
        ).arrange(DOWN, buff=0.65).move_to(ORIGIN)
        self.play(FadeIn(rules, shift=UP * 0.2), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(rules), FadeOut(title), FadeOut(author))

    def show_worked_example(self, heading, original, reduced, result, explanation):
        heading_text = Text(heading, font_size=33, color=BLUE_B).move_to(UP * 3.4)
        explanation_text = Text(explanation, font_size=27, color=YELLOW)
        explanation_text.move_to(DOWN * 3.5)
        line_one = MathTex(original, font_size=62)
        line_two = MathTex("=", reduced, font_size=62)
        line_three = MathTex("=", result, font_size=62, color=GREEN)
        equations = VGroup(line_one, line_two, line_three).arrange(DOWN, buff=0.65)
        equations.move_to(ORIGIN)

        self.play(Write(heading_text), Write(line_one), run_time=0.9)
        self.play(FadeIn(explanation_text), Write(line_two), run_time=0.9)
        self.play(Write(line_three), run_time=0.8)
        self.wait(1)
        self.play(
            FadeOut(heading_text), FadeOut(explanation_text), FadeOut(equations),
            run_time=0.6,
        )
