"""抽屉原理：n+1 个物体分到 n 个抽屉，至少有一个装两个或更多。"""

from manim import *


class 抽屉原理Animation(Scene):
    """用 4 个物体与 3 个抽屉说明反证思路。"""

    def construct(self):
        title = Text("抽屉原理", font_size=43).to_edge(UP, buff=0.55)
        self.play(Write(title))
        prompt = Text("把 4 个物体放入 3 个抽屉", font_size=31).move_to(UP * 2)
        self.play(FadeIn(prompt))

        boxes = VGroup(*[
            Rectangle(width=1.5, height=1.05, color=BLUE)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.58).move_to(UP * 0.3)
        self.play(*(Create(box) for box in boxes))
        positions = (boxes[0].get_center(), boxes[1].get_center(),
                     boxes[2].get_center() + LEFT * 0.25,
                     boxes[2].get_center() + RIGHT * 0.25)
        balls = VGroup(*[Dot(pos, color=YELLOW, radius=0.1) for pos in positions])
        self.play(LaggedStart(*(FadeIn(ball) for ball in balls), lag_ratio=0.35))

        explanation = VGroup(
            Text("如果每个抽屉最多只能放 1 个", font_size=29),
            Text("那么 3 个抽屉最多只能放 3 个物体", font_size=29),
            MathTex(r"4>3", font_size=43, color=YELLOW),
            Text("与已有 4 个物体矛盾，所以至少有 1 个抽屉放了 2 个", font_size=26),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 2.15)
        self.play(LaggedStart(*(FadeIn(item) for item in explanation), lag_ratio=0.3))
        self.wait(2)
