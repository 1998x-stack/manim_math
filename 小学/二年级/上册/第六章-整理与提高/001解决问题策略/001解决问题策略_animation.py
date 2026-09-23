"""解决问题策略完整版：固定上衣、逐一搭配裤子，不重复、不遗漏。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001解决问题策略Animation(Scene):
    """完整展示 2×3 的六个有序配对，解释分类枚举。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=19, color=GRAY_B)
        author.move_to(UP * 7.2)
        title = Text("解决问题策略：有序搭配", font_size=41, color=GOLD)
        title.move_to(UP * 5.85)
        problem = Text("2件上衣，每件配3条裤子，怎样不重不漏？", font_size=27)
        problem.move_to(UP * 4.6)
        self.play(FadeIn(author), Write(title), FadeIn(problem))

        shirts, trousers = ("甲", "乙"), ("1", "2", "3")
        combinations = [(shirt, trouser) for shirt in shirts for trouser in trousers]
        assert len(combinations) == len(set(combinations)) == 6
        heading = Text("固定上衣，分别选择第1、2、3条裤子", font_size=27)
        heading.move_to(UP * 3.25)
        self.play(Write(heading))

        all_cards = VGroup()
        for row, shirt in enumerate(shirts):
            row_label = Text(f"上衣{shirt}", font_size=23, color=YELLOW)
            row_label.move_to([-3.85, 1.45 - row * 2.1, 0])
            self.play(FadeIn(row_label))
            cards = VGroup()
            for col, trouser in enumerate(trousers):
                cell = VGroup(
                    RoundedRectangle(width=1.75, height=1.1,
                                     corner_radius=0.13, color=BLUE_B),
                    Text(f"{shirt} + {trouser}", font_size=28),
                )
                cell.move_to([(col - 1) * 2.2, 1.45 - row * 2.1, 0])
                cards.add(cell)
            self.play(LaggedStart(*[FadeIn(card) for card in cards], lag_ratio=0.3))
            all_cards.add(cards)

        count = Text("每件上衣有3种搭配，共2组", font_size=29, color=YELLOW)
        count.move_to(DOWN * 3.15)
        formula = MathTex(r"3+3=2\times3=6", font_size=56)
        formula.move_to(DOWN * 4.3)
        summary = Text("按顺序列举：6种，不重复、不遗漏", font_size=27, color=GREEN)
        summary.move_to(DOWN * 5.4)
        self.play(FadeIn(count), Write(formula))
        self.play(Write(summary))
        self.wait(2)
