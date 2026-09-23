"""整数与整除：通过十二个点的等分与余数反例解释整除。"""

from manim import *


class 整数与整除Animation(Scene):
    """演示 12 能被 3 整除，而 13 不能被 3 整除。"""

    def construct(self):
        title = Text("整数与整除", font_size=42).to_edge(UP, buff=0.5)
        self.play(Write(title))

        dots = VGroup(*[Dot(radius=0.11, color=BLUE) for _ in range(12)])
        dots.arrange_in_grid(rows=3, cols=4, buff=(0.28, 0.28))
        dots.move_to(UP * 0.65)
        self.play(LaggedStart(*(FadeIn(dot) for dot in dots), lag_ratio=0.07))

        groups = [VGroup(*dots[index * 4:(index + 1) * 4]) for index in range(3)]
        outlines = VGroup(*[
            SurroundingRectangle(group, color=YELLOW, buff=0.16)
            for group in groups
        ])
        self.play(*(Create(outline) for outline in outlines))
        equation = MathTex(r"12 \div 3 = 4", font_size=48)
        equation.next_to(dots, DOWN, buff=0.75)
        explanation = Text("12 个点平均分成 3 组，每组 4 个，余数是 0", font_size=24)
        explanation.next_to(equation, DOWN, buff=0.32)
        self.play(Write(equation), FadeIn(explanation))
        self.wait(1)

        remainder_dot = Dot(radius=0.11, color=RED).next_to(dots, RIGHT, buff=0.45)
        remainder_text = Text("再增加 1 个点：13 ÷ 3 = 4……1", font_size=26)
        remainder_text.move_to(explanation)
        self.play(FadeIn(remainder_dot), FadeOut(explanation), FadeIn(remainder_text))
        self.wait(1)

        conclusion = VGroup(
            Text("12 能被 3 整除；3 能整除 12", font_size=28, color=GREEN),
            Text("13 不能被 3 整除；除数不能为 0", font_size=25, color=YELLOW),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 3.2)
        self.play(FadeOut(remainder_text), FadeIn(conclusion))
        self.wait(2)
