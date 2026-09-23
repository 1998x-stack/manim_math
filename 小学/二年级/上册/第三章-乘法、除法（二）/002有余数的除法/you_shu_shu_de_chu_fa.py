"""有余数的除法：13 个苹果平均分给 4 人。

教学模型：13 = 4 × 3 + 1，0 <= 1 < 4。始终移动同一批对象，不复制苹果。
"""
from manim import *

# 本文件作为独立竖屏视频渲染；从其他脚本导入时请注意 Manim 全局配置。
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


TOTAL = 13
CHILDREN = 4
PER_CHILD, REMAINDER = divmod(TOTAL, CHILDREN)
assert (PER_CHILD, REMAINDER) == (3, 1)
assert TOTAL == CHILDREN * PER_CHILD + REMAINDER
assert 0 <= REMAINDER < CHILDREN


class YouShuShuDeChuFa(Scene):
    """用原始 13 个对象展示逐轮平均分、余数及数学验算。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.introduction()
        self.distribute()
        self.explain_result()

    def introduction(self):
        self.title = Text("有余数的除法", font_size=46, color=GOLD).move_to(UP * 6.1)
        self.subtitle = Text("13个苹果平均分给4个小朋友", font_size=29).move_to(UP * 4.65)
        self.play(Write(self.title), FadeIn(self.subtitle))

        # 创建一次：后续分配直接移动这些对象，不再产生新的“苹果”。
        self.apples = VGroup(*[
            Dot(radius=0.14, color=RED_B).move_to(
                [((index % 4) - 1.5) * 0.57, 3.45 - (index // 4) * 0.53, 0]
            )
            for index in range(TOTAL)
        ])
        self.play(FadeIn(self.apples), run_time=0.9)
        self.wait(0.4)

    def distribute(self):
        self.centers = [-3.1, -1.05, 1.05, 3.1]
        self.boxes = VGroup(*[
            RoundedRectangle(
                width=1.88, height=1.35, corner_radius=0.14,
                color=BLUE_B, stroke_width=3
            ).move_to([center_x, -0.7, 0])
            for center_x in self.centers
        ])
        self.labels = VGroup(*[
            Text(f"第{i + 1}人", font_size=23).next_to(box, UP, buff=0.2)
            for i, box in enumerate(self.boxes)
        ])
        self.play(Create(self.boxes), FadeIn(self.labels), run_time=0.9)

        # 第 1 轮每人 1 个，第 2 轮每人 2 个，第 3 轮每人 3 个。
        # index = round_index * CHILDREN + child_index 确保恰好移动 12 个不同对象。
        for round_index in range(PER_CHILD):
            moves = []
            for child_index, center_x in enumerate(self.centers):
                index = round_index * CHILDREN + child_index
                target = [center_x + (round_index - 1) * 0.43, -0.7, 0]
                moves.append(self.apples[index].animate.move_to(target))
            self.play(*moves, run_time=0.75)

        # 第 13 个对象始终没有分给任何人，即真实的余数。
        self.leftover = self.apples[CHILDREN * PER_CHILD]
        self.play(self.leftover.animate.move_to([0, -2.75, 0]).set_color(YELLOW))
        remainder_caption = Text("剩下1个，不能再给每人1个", font_size=27, color=YELLOW)
        remainder_caption.move_to(DOWN * 3.6)
        self.play(Write(remainder_caption))
        self.wait(0.6)
        self.play(FadeOut(remainder_caption))

    def explain_result(self):
        # \cdots 是 LaTeX 命令；不要把中文或原生省略号直接写进 MathTex。
        formula = MathTex(r"13\div4=3\cdots1", font_size=57).move_to(DOWN * 4.3)
        interpretation = Text("每人3个，余1个", font_size=29, color=GOLD)
        interpretation.move_to(DOWN * 5.05)
        verification = MathTex(r"13=4\times3+1", font_size=48).move_to(DOWN * 5.9)
        rule = MathTex(r"0\leq1<4", font_size=45, color=GREEN).move_to(DOWN * 6.8)

        self.play(Write(formula))
        self.play(FadeIn(interpretation))
        self.play(Write(verification), Write(rule))
        self.wait(2)
