"""两位数乘一位数的简短示例；完整课程见同目录 TwoDigitTimeOneLesson。"""

from manim import *


class TwoDigitMultiplicationPreview(Scene):
    """逐步解释 28 × 4 的个位进位与十位计算。"""

    def construct(self):
        title = Text("两位数乘一位数：竖式", font_size=36).to_edge(UP)
        problem = MathTex(r"28 \times 4", font_size=60).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(title), Write(problem))

        steps = VGroup(
            Text("个位：8 × 4 = 32，写 2，向十位进 3", font_size=25),
            Text("十位：2 × 4 + 3 = 11", font_size=28),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).next_to(
            problem, DOWN, buff=0.65
        )
        for step in steps:
            self.play(Write(step))
            self.wait(0.3)

        answer = MathTex(r"28 \times 4 = 112", font_size=56).next_to(
            steps, DOWN, buff=0.7
        )
        self.play(Write(answer))
        self.wait(1)
