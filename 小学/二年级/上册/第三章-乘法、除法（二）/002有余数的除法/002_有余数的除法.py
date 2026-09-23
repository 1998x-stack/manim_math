"""有余数的除法：将同一批 13 个物体分给 4 人，每人 3 个，余 1 个。"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920


class 有余数的除法Animation(Scene):
    """移动原始物体完成分配，避免凭空新增分组对象。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        total, children = 13, 4
        per_child, remainder = divmod(total, children)
        assert (per_child, remainder) == (3, 1)
        assert total == children * per_child + remainder
        assert 0 <= remainder < children

        title = Text("有余数的除法", font_size=46, color=YELLOW).move_to(UP * 6.4)
        prompt = Text("13个苹果平均分给4个小朋友", font_size=29).move_to(UP * 4.8)
        self.play(Write(title), FadeIn(prompt))

        # 每个圆点代表一个苹果；整个场景只构造这一批 13 个苹果。
        apples = VGroup(*[
            Dot(radius=0.14, color=RED_B).move_to(
                [((i % 4) - 1.5) * 0.56, 3.45 - (i // 4) * 0.52, 0]
            )
            for i in range(total)
        ])
        self.play(FadeIn(apples), run_time=0.8)

        centers = [-3.1, -1.05, 1.05, 3.1]
        boxes = VGroup(*[
            RoundedRectangle(width=1.88, height=1.35, corner_radius=0.15,
                             color=BLUE_B).move_to([x, -0.7, 0])
            for x in centers
        ])
        labels = VGroup(*[
            Text(f"第{i + 1}人", font_size=22).next_to(box, UP, buff=0.2)
            for i, box in enumerate(boxes)
        ])
        self.play(Create(boxes), FadeIn(labels))

        # 按轮分给 4 人；每一轮移动 4 个不同的原始苹果。
        for round_index in range(per_child):
            moves = []
            for child_index, center_x in enumerate(centers):
                source_index = round_index * children + child_index
                target = [center_x + (round_index - 1) * 0.43, -0.7, 0]
                moves.append(apples[source_index].animate.move_to(target))
            self.play(*moves, run_time=0.7)

        leftover = apples[children * per_child]
        self.play(leftover.animate.move_to([0, -2.8, 0]).set_color(YELLOW))
        caption = Text("每人3个，还剩1个", font_size=30, color=YELLOW).move_to(DOWN * 3.65)
        formula = MathTex(r"13\div4=3\cdots1", font_size=60).move_to(DOWN * 4.75)
        check = MathTex(r"13=4\times3+1", font_size=52).move_to(DOWN * 5.85)
        rule = MathTex(r"0\leq1<4", font_size=47, color=GREEN).move_to(DOWN * 6.8)
        self.play(FadeIn(caption), Write(formula))
        self.play(Write(check), Write(rule))
        self.wait(2)
