"""不等式性质：加减保持方向，乘除负数必须反向。"""

from manim import *


class 不等式及其性质Animation(Scene):
    """使用 5>3 的具体例子区分正、负、零因子的影响。"""

    def construct(self):
        title = Text("不等式及其性质", font_size=41).to_edge(UP, buff=0.55)
        self.play(Write(title))
        premise = MathTex(r"5>3", font_size=50, color=YELLOW).move_to(UP * 2.0)
        self.play(Write(premise))

        cases = VGroup(
            VGroup(Text("两边加上或减去相同的数，方向不变", font_size=27),
                   MathTex(r"5-2>3-2", font_size=40)),
            VGroup(Text("两边乘以正数，方向不变", font_size=27),
                   MathTex(r"5\times2>3\times2", font_size=40)),
            VGroup(Text("两边乘以负数，方向反转", font_size=27, color=YELLOW),
                   MathTex(r"5\times(-2)<3\times(-2)", font_size=40)),
        )
        for case in cases:
            case.arrange(DOWN, buff=0.13)
        cases.arrange(DOWN, buff=0.4).move_to(DOWN * 0.6)
        self.play(LaggedStart(*(FadeIn(case) for case in cases), lag_ratio=0.5))

        footnote = Text("两边乘以 0 时都变成 0，不能保留严格不等号", font_size=25)
        footnote.next_to(cases, DOWN, buff=0.35)
        self.play(FadeIn(footnote))
        self.wait(2)
