"""两位数乘两位数的简短示例；完整课程见同目录 TwoDigitMultiplyLesson。"""

from manim import *


class TwoDigitByTwoDigitPreview(Scene):
    """用部分积展示 23 × 14 的位值含义。"""

    def construct(self):
        title = Text("两位数乘两位数", font_size=38).to_edge(UP)
        problem = MathTex(r"23 \times 14", font_size=58).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(title), Write(problem))

        steps = VGroup(
            Text("先乘个位：23 × 4 = 92", font_size=29),
            Text("再乘十位：23 × 10 = 230", font_size=29),
            Text("部分积相加：92 + 230 = 322", font_size=28),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(
            problem, DOWN, buff=0.65
        )
        for step in steps:
            self.play(Write(step))
            self.wait(0.2)

        answer = MathTex(r"23 \times 14 = 322", font_size=52).next_to(
            steps, DOWN, buff=0.65
        )
        self.play(Write(answer))
        self.wait(1)
