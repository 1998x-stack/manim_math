"""两位数除以一位数的简短示例；完整课程参见同目录的教学场景。"""

from manim import *


class TwoDigitDivisionPreview(Scene):
    """从 52 ÷ 4 = 13 解释先分十位、再分个位的计算。"""

    def construct(self):
        title = Text("两位数除以一位数：竖式", font_size=36).to_edge(UP)
        problem = MathTex(r"52 \div 4 = \, ?", font_size=54).next_to(
            title, DOWN, buff=0.5
        )
        self.play(Write(title), Write(problem))

        steps = VGroup(
            Text("5 个十 ÷ 4：商 1 个十，余 1 个十", font_size=27),
            Text("余下的 1 个十与 2 个一合成 12", font_size=27),
            Text("12 ÷ 4 = 3，个位商 3", font_size=27),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).next_to(
            problem, DOWN, buff=0.6
        )
        for step in steps:
            self.play(Write(step))
            self.wait(0.2)

        result = MathTex(r"52 \div 4 = 13", font_size=54).next_to(
            steps, DOWN, buff=0.6
        )
        check = MathTex(r"13 \times 4 = 52", font_size=44).next_to(
            result, DOWN, buff=0.35
        )
        self.play(Write(result))
        self.play(Write(check))
        self.wait(1)
