"""二年级：运算顺序（竖屏教学短片）。

数学核对：同级运算从左到右，先乘除后加减，有括号先算括号。
"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920


class 运算顺序Animation(Scene):
    """用逐步计算而非无关的圆形解释运算顺序。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("运算顺序", font_size=46, color=YELLOW).move_to(UP * 6.3)
        self.play(Write(title))

        examples = (
            ("只有加减：从左往右", r"5+3-2", r"8-2", r"6"),
            ("有乘法：先乘后加", r"5+3\times2", r"5+6", r"11"),
            ("有括号：先算括号", r"(5+3)\times2", r"8\times2", r"16"),
        )
        for heading, expression, intermediate, answer in examples:
            self.show_example(heading, expression, intermediate, answer)

        summary = VGroup(
            Text("同级运算，从左往右", font_size=30),
            Text("先乘除，后加减", font_size=30),
            Text("有括号，先算括号里面", font_size=30),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(summary), FadeOut(title))

    def show_example(self, heading, expression, intermediate, answer):
        label = Text(heading, font_size=30, color=BLUE_B).move_to(UP * 3.5)
        first = MathTex(expression, font_size=63)
        second = MathTex("=", intermediate, font_size=63)
        third = MathTex("=", answer, font_size=63, color=GREEN)
        lines = VGroup(first, second, third).arrange(DOWN, buff=0.65)
        lines.move_to(ORIGIN)
        # 每一步保留上一行，使学生能够检查被替换的子表达式。
        self.play(FadeIn(label), Write(first), run_time=0.8)
        self.play(Write(second), run_time=0.7)
        self.play(Write(third), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(label), FadeOut(lines), run_time=0.5)
