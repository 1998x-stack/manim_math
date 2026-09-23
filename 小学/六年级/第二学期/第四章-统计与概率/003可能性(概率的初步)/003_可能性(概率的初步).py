"""概率初步：只在有限且等可能的结果中使用有利结果数之比。"""

from manim import *


class 可能性概率的初步Animation(Scene):
    """公平六面骰子，掷得偶数的概率是 3/6。"""

    def construct(self):
        title = Text("可能性：概率的初步", font_size=39).to_edge(UP, buff=0.5)
        self.play(Write(title))

        premise = Text("公平的六面骰子：6 种结果机会相同", font_size=28)
        premise.move_to(UP * 2.0)
        self.play(FadeIn(premise))

        outcomes = VGroup()
        for value in range(1, 7):
            border = Square(side_length=0.74, color=GREEN if value % 2 == 0 else BLUE)
            number = Text(str(value), font_size=30).move_to(border)
            outcomes.add(VGroup(border, number))
        outcomes.arrange_in_grid(rows=2, cols=3, buff=(0.28, 0.38))
        outcomes.move_to(UP * 0.45)
        self.play(LaggedStart(*(FadeIn(item) for item in outcomes), lag_ratio=0.18))

        event = Text("事件 E：掷出偶数 2、4、6（3 种结果）", font_size=27)
        event.next_to(outcomes, DOWN, buff=0.55)
        formula = MathTex(r"P(E)=\frac{3}{6}=\frac12", font_size=45)
        formula.next_to(event, DOWN, buff=0.4)
        self.play(FadeIn(event), Write(formula))

        condition = Text("仅在各种基本结果等可能时，才可直接按个数计算", font_size=23, color=YELLOW)
        condition.next_to(formula, DOWN, buff=0.55)
        self.play(FadeIn(condition))
        self.wait(2)
