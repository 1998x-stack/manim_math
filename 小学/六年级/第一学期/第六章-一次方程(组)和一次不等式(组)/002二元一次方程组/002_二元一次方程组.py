"""二元一次方程组：用加减消元法求解并代入两式检验。"""

from manim import *


class 二元一次方程组Animation(Scene):
    """x+y=5、x-y=1 的唯一解是 (3,2)。"""

    def construct(self):
        title = Text("二元一次方程组", font_size=41).to_edge(UP, buff=0.55)
        self.play(Write(title))
        system = MathTex(r"\begin{cases}x+y=5\\x-y=1\end{cases}", font_size=45)
        system.move_to(UP * 1.9)
        self.play(Write(system))

        steps = VGroup(
            Text("两式相加，消去 y", font_size=28, color=BLUE),
            MathTex(r"2x=6\quad\Longrightarrow\quad x=3", font_size=40),
            Text("将 x=3 代回第一式", font_size=28),
            MathTex(r"3+y=5\quad\Longrightarrow\quad y=2", font_size=39),
            Text("检验：两式都成立", font_size=28, color=GREEN),
            MathTex(r"3+2=5,\qquad3-2=1", font_size=40),
        ).arrange(DOWN, buff=0.27)
        steps.next_to(system, DOWN, buff=0.52)
        self.play(LaggedStart(*(FadeIn(step) for step in steps), lag_ratio=0.3))
        self.wait(2)
