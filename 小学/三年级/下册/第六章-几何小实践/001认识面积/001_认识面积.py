"""认识面积的简短示例；完整课程见同目录 001认识面积_animation.py。"""

from manim import *


class AreaIntroductionPreview(Scene):
    """用 3 × 2 个相同的小正方形表示封闭平面区域的面积。"""

    def construct(self):
        title = Text("认识面积", font_size=42).to_edge(UP)
        explanation = Text("面积表示平面图形所占区域的大小", font_size=29)
        explanation.next_to(title, DOWN, buff=0.4)
        self.play(Write(title), Write(explanation))

        tiles = VGroup(*[
            Square(
                side_length=0.9, stroke_color=WHITE,
                fill_color=BLUE, fill_opacity=0.65,
            ).move_to([(column - 1) * 0.9, (0.5 - row) * 0.9, 0])
            for row in range(2)
            for column in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(tile) for tile in tiles], lag_ratio=0.13))
        result = Text("6 个同样大小的小正方形", font_size=30).next_to(
            tiles, DOWN, buff=0.5
        )
        self.play(Write(result))
        self.wait(1)
