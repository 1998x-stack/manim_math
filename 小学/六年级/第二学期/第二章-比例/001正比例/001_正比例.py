"""正比例：y=kx (k 为非零常数)，比值 y/x 只在 x≠0 时定义。"""

from manim import *


class 正比例Animation(Scene):
    """例：y=2x，观察 (1,2)、(2,4)、(3,6) 共线且过原点。"""

    def construct(self):
        title = Text("正比例", font_size=43).to_edge(UP, buff=0.5)
        self.play(Write(title))
        rule = MathTex(r"y=kx,\quad k\ne0", font_size=44)
        example = MathTex(r"y=2x", font_size=43, color=YELLOW)
        VGroup(rule, example).arrange(DOWN, buff=0.3).move_to(UP * 2.25)
        self.play(Write(rule), Write(example))

        axes = Axes(x_range=[0, 4, 1], y_range=[0, 8, 2],
                    x_length=4.3, y_length=3.1, tips=False)
        axes.move_to(DOWN * 0.45)
        graph = axes.plot(lambda x: 2 * x, x_range=[0, 3.5], color=YELLOW)
        points = VGroup(*[
            Dot(axes.c2p(x, 2 * x), color=GREEN, radius=0.08)
            for x in (1, 2, 3)
        ])
        self.play(Create(axes), Create(graph), FadeIn(points))

        statement = Text("x 不为 0 时，比值 y/x 恒为 2", font_size=26)
        statement.move_to(DOWN * 2.85)
        exception = Text("x=0 时，y=0；但 0/0 没有定义", font_size=25, color=YELLOW)
        exception.next_to(statement, DOWN, buff=0.3)
        self.play(FadeIn(statement), FadeIn(exception))
        self.wait(2)
