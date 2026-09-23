"""通过数轴比较有理数大小：右边的数大于左边的数。"""

from manim import *


class 有理数的大小比较Animation(Scene):
    """在数轴上同时比较负数、零与正数，保留旧课程 Scene 入口。"""

    def construct(self):
        title = Text("有理数的大小比较", font_size=42).to_edge(UP)
        self.play(Write(title))

        # 一条数轴对应同一个单位长度；位置比较不能被无关圆形代替。
        axis = NumberLine(
            x_range=[-3, 3, 1], length=8, include_numbers=True,
            color=BLUE,
        ).shift(DOWN * 0.3)
        self.play(Create(axis))

        values = (-2, 0, 1)
        colors = (RED, YELLOW, GREEN)
        dots = VGroup(*[
            Dot(axis.n2p(value), color=color, radius=0.11)
            for value, color in zip(values, colors)
        ])
        self.play(*[FadeIn(dot) for dot in dots])

        # 中文解释用 Text；MathTex 只承载可由 LaTeX 解析的数字和比较符号。
        example = MathTex(r"-2 < 0 < 1", font_size=44)
        example.next_to(axis, DOWN, buff=1.1)
        rule = Text("数轴上右边的数大于左边的数", font_size=30)
        rule.next_to(example, DOWN, buff=0.4)
        summary = Text("负数 < 0 < 正数", font_size=30, color=YELLOW)
        summary.next_to(rule, DOWN, buff=0.4)

        self.play(Write(example))
        self.play(FadeIn(rule))
        self.play(FadeIn(summary))
        self.wait(2)


if __name__ == "__main__":
    # manim -pql '005_有理数的大小比较.py' '有理数的大小比较Animation'
    pass
