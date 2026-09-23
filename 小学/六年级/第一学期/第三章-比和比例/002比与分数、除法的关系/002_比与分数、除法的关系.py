"""比与除法、分数：同一个比值的三种表达，后项不能为零。"""

from manim import *


class 比与分数除法的关系Animation(Scene):
    """a:b 的比值等于 a÷b，也等于 a/b；条件 b≠0。"""

    def construct(self):
        title = Text("比与分数、除法的关系", font_size=39).to_edge(UP, buff=0.6)
        self.play(Write(title))

        rule = MathTex(r"a:b=a\div b=\frac{a}{b}", font_size=48)
        rule.move_to(UP * 1.7)
        condition = Text("a 是前项，b 是后项；b 不能为 0", font_size=28)
        condition.next_to(rule, DOWN, buff=0.5)
        self.play(Write(rule), FadeIn(condition))

        example = MathTex(r"2:3=2\div3=\frac{2}{3}", font_size=45, color=YELLOW)
        example.next_to(condition, DOWN, buff=0.8)
        self.play(Write(example))

        correspondences = VGroup(
            Text("前项 ↔ 被除数 ↔ 分子", font_size=28, color=BLUE),
            Text("后项 ↔ 除数 ↔ 分母", font_size=28, color=GREEN),
            Text("三种写法不同，比值相同", font_size=27),
        ).arrange(DOWN, buff=0.32)
        correspondences.next_to(example, DOWN, buff=0.65)
        self.play(LaggedStart(*(FadeIn(item) for item in correspondences), lag_ratio=0.4))
        self.wait(2)
