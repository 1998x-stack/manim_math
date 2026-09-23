"""解决问题策略：按上衣分类，不重不漏地列举 2×3=6 种搭配。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 解决问题策略Animation(Scene):
    """使用真实的 2 行×3 列搭配表，解释乘法原理。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("解决问题策略：有序搭配", font_size=42, color=GOLD)
        title.move_to(UP * 6.1)
        problem = Text("2件上衣，每件配3条裤子，有几种搭配？", font_size=28)
        problem.move_to(UP * 4.6)
        self.play(Write(title), FadeIn(problem))

        instruction = Text("先固定上衣，再依次选择裤子", font_size=28, color=YELLOW)
        instruction.move_to(UP * 3.3)
        self.play(Write(instruction))
        shirts, trousers = ("甲", "乙"), ("1", "2", "3")
        combinations = [(shirt, trouser) for shirt in shirts for trouser in trousers]
        assert len(combinations) == len(set(combinations)) == 2 * 3

        cards = VGroup()
        for row, shirt in enumerate(shirts):
            for col, trouser in enumerate(trousers):
                card = VGroup(
                    RoundedRectangle(width=2.1, height=1.15, corner_radius=0.12,
                                     color=BLUE_B),
                    Text(f"{shirt} + {trouser}", font_size=31),
                )
                card.move_to([(col - 1) * 2.5, 1.45 - row * 2.05, 0])
                cards.add(card)
        self.play(LaggedStart(*[FadeIn(card) for card in cards], lag_ratio=0.3))

        formula = MathTex(r"2\times3=6", font_size=64).move_to(DOWN * 3.1)
        explanation = Text("每件上衣有3种搭配，2件共6种", font_size=29)
        explanation.move_to(DOWN * 4.3)
        self.play(Write(formula), FadeIn(explanation))
        self.wait(2)
