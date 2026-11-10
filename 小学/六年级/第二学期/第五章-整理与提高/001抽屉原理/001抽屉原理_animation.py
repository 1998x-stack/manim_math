"""六年级：抽屉原理。4 件物品进 3 个盒子，推广到上取整界。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def pigeonhole_lower_bound(objects: int, boxes: int) -> int:
    """保证至少有一个盒子的物体数不小于 ceil(objects / boxes)。"""
    if type(objects) is not int or type(boxes) is not int:
        raise ValueError("物体数、盒子数必须是整数")
    if objects < 0 or boxes <= 0:
        raise ValueError("物体数非负且盒子数为正")
    return (objects + boxes - 1) // boxes


class Topic001抽屉原理Animation(Scene):
    """从四进三的矛盾论证出发，介绍一般形式。"""

    def construct(self):
        assert pigeonhole_lower_bound(4, 3) == 2
        assert pigeonhole_lower_bound(10, 3) == 4
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.box_example()
        self.proof()
        self.generalization()

    def transition(self):
        self.play(*[
            FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark
        ], run_time=0.35)

    def heading(self, title):
        text = Text(title, font_size=38, color=GOLD).move_to(UP * 5.6)
        self.play(Write(text))
        return text

    def opening(self):
        title = Text("抽屉原理", font_size=49, color=WHITE).move_to(UP * 3.5)
        challenge = Text("4 个苹果，放进 3 个盒子", font_size=29, color=BLUE_ACCENT)
        challenge.move_to(UP * 1.2)
        self.play(Write(title))
        self.play(FadeIn(challenge))
        question = Text("能让每个盒子最多只有 1 个吗？", font_size=27, color=GOLD)
        question.move_to(DOWN * 1.5)
        self.play(Write(question))
        self.wait(0.8)
        self.transition()

    def box_example(self):
        self.heading("把四个苹果放进去")
        rectangles = VGroup(*[
            RoundedRectangle(
                width=2, height=1.5, corner_radius=0.15,
                stroke_color=BLUE_ACCENT, stroke_width=3
            )
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.5).move_to(UP * 1)
        self.play(*[Create(box) for box in rectangles])
        # 在同一个盒子里放两个真实物体，其余各一个。
        locations = [
            rectangles[0].get_center() + LEFT * 0.38,
            rectangles[0].get_center() + RIGHT * 0.38,
            rectangles[1].get_center(),
            rectangles[2].get_center(),
        ]
        apples = VGroup(*[
            Dot(position, radius=0.15, color=GOLD)
            for position in locations
        ])
        self.play(LaggedStart(*(FadeIn(dot) for dot in apples), lag_ratio=0.3))
        numbers = VGroup(*[
            Text(str(qty), font_size=29, color=GREEN_ACCENT).next_to(box, DOWN, buff=0.32)
            for qty, box in zip((2, 1, 1), rectangles)
        ])
        self.play(FadeIn(numbers))
        conclusion = Text("至少有一个盒子装了 2 个", font_size=28, color=GREEN_ACCENT)
        conclusion.move_to(DOWN * 2.5)
        self.play(Write(conclusion))
        self.wait(0.8)
        self.transition()

    def proof(self):
        self.heading("为什么一定如此？")
        statements = VGroup(
            Text("假设每个盒子最多装 1 个", font_size=28),
            MathTex(r"1+1+1=3", font_size=51, color=BLUE_ACCENT),
            Text("三个盒子最多只能装 3 个", font_size=27),
            MathTex(r"4>3", font_size=50, color=GOLD),
            Text("与 4 个物体矛盾，所以假设不成立", font_size=25, color=GREEN_ACCENT),
        ).arrange(DOWN, buff=0.57).move_to(UP * 0.7)
        for statement in statements:
            self.play(FadeIn(statement, shift=UP * 0.15), run_time=0.45)
        self.wait(0.8)
        self.transition()

    def generalization(self):
        self.heading("推广：不只是多一个")
        rule = MathTex(r"\left\lceil\frac{m}{n}\right\rceil",
                       font_size=64, color=GOLD).move_to(UP * 3.5)
        label = Text("m 个物体分到 n 个盒子", font_size=29)
        label.move_to(UP * 2.2)
        self.play(Write(rule), FadeIn(label))
        example = MathTex(r"\left\lceil\frac{10}{3}\right\rceil=4",
                          font_size=50, color=GREEN_ACCENT).move_to(ORIGIN)
        self.play(Write(example))
        explanation = VGroup(
            Text("10 个物体放进 3 个盒子", font_size=28),
            Text("总有一个盒子至少 4 个", font_size=28, color=GREEN_ACCENT),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 2.1)
        self.play(FadeIn(explanation))
        self.wait(1)
