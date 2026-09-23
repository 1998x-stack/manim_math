"""两位数除法试商的简短示例；完整课程见同目录 TwoDigitDivisionLesson。"""

from manim import *


class TrialQuotientPreview(Scene):
    """比较相邻候选商的乘积，确定 96 ÷ 32 的商是 3。"""

    def construct(self):
        title = Text("两位数除法：试商", font_size=38).to_edge(UP)
        problem = MathTex(r"96 \div 32 = \, ?", font_size=54).next_to(
            title, DOWN, buff=0.55
        )
        self.play(Write(title), Write(problem))

        steps = VGroup(
            MathTex(r"32 \times 2 = 64 < 96", font_size=43),
            MathTex(r"32 \times 3 = 96", font_size=43),
            MathTex(r"32 \times 4 = 128 > 96", font_size=43),
        ).arrange(DOWN, buff=0.45).next_to(problem, DOWN, buff=0.65)
        for step in steps:
            self.play(Write(step))
            self.wait(0.2)

        answer = MathTex(r"96 \div 32 = 3", font_size=54).next_to(
            steps, DOWN, buff=0.6
        )
        self.play(Write(answer))
        self.wait(1)
