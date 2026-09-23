"""整十数乘一位数的简短示例；完整课程见同目录 RoundNumberMultiplyLesson。"""

from manim import *


class RoundTensMultiplicationPreview(Scene):
    """用三个“2 个十”直观展示 20 × 3 = 60。"""

    def construct(self):
        title = Text("整十数乘一位数", font_size=38).to_edge(UP)
        question = MathTex(r"20 \times 3 = \, ?", font_size=56).next_to(
            title, DOWN, buff=0.6
        )
        self.play(Write(title), Write(question))

        # 每个框代表 20，而不是把一个无含义的圆当成 20。
        groups = VGroup(*[
            VGroup(
                Rectangle(width=2.4, height=0.7, color=BLUE),
                Text("2 个十", font_size=26),
            )
            for _ in range(3)
        ])
        for group in groups:
            group[1].move_to(group[0])
        groups.arrange(DOWN, buff=0.22).next_to(question, DOWN, buff=0.45)
        self.play(LaggedStart(*[FadeIn(group) for group in groups], lag_ratio=0.25))

        reasoning = Text("2 × 3 = 6（个十）", font_size=30).next_to(
            groups, DOWN, buff=0.45
        )
        result = MathTex(r"20 \times 3 = 60", font_size=48).next_to(
            reasoning, DOWN, buff=0.28
        )
        self.play(Write(reasoning))
        self.play(Transform(question, result))
        self.wait(1)
