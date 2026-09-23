"""一元一次方程：同乘非零最小公倍数，并代回检验。"""

from manim import *


class 一元一次方程的解法Animation(Scene):
    """求解 x/2 + 1/3 = 5/6，演示去分母时必须同乘方程两边。"""

    def construct(self):
        title = Text("一元一次方程的解法", font_size=40).to_edge(UP, buff=0.55)
        self.play(Write(title))

        equation = MathTex(r"\frac{x}{2}+\frac13=\frac56", font_size=45)
        equation.move_to(UP * 2.0)
        self.play(Write(equation))

        steps = VGroup(
            Text("分母 2、3、6 的最小公倍数为 6；两边同乘 6", font_size=25),
            MathTex(r"3x+2=5", font_size=42),
            MathTex(r"3x=3", font_size=42),
            MathTex(r"x=1", font_size=46, color=YELLOW),
            Text("代回原方程检验", font_size=27),
            MathTex(r"\frac12+\frac13=\frac56", font_size=40, color=GREEN),
        ).arrange(DOWN, buff=0.25)
        steps.next_to(equation, DOWN, buff=0.5)
        self.play(LaggedStart(*(FadeIn(step) for step in steps), lag_ratio=0.3))
        self.wait(2)
