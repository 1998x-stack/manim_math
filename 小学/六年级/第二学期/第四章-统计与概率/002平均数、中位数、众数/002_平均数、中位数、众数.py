"""平均数、中位数与众数：同一组数据的三个不同统计量。"""

from manim import *


class 平均数中位数众数Animation(Scene):
    """数据 1,2,2,3,7 的平均数为 3，中位数和众数均为 2。"""

    def construct(self):
        title = Text("平均数、中位数、众数", font_size=39).to_edge(UP, buff=0.55)
        self.play(Write(title))

        dataset = Text("从小到大排列：1，2，2，3，7", font_size=31)
        dataset.move_to(UP * 2.0)
        self.play(Write(dataset))

        mean_note = Text("平均数：总和除以数据个数", font_size=27, color=BLUE)
        mean_formula = MathTex(r"\bar{x}=\frac{1+2+2+3+7}{5}=3", font_size=40)
        median_note = Text("中位数：中间第 3 个数是 2", font_size=28, color=YELLOW)
        mode_note = Text("众数：2 出现了 2 次，出现次数最多", font_size=27, color=GREEN)
        summary = VGroup(mean_note, mean_formula, median_note, mode_note)
        summary.arrange(DOWN, buff=0.42).move_to(DOWN * 0.4)
        self.play(FadeIn(mean_note), Write(mean_formula))
        self.play(FadeIn(median_note), FadeIn(mode_note))

        conclusion = Text("平均数、中位数、众数不一定相等", font_size=29)
        conclusion.next_to(summary, DOWN, buff=0.55)
        self.play(FadeIn(conclusion))
        self.wait(2)
