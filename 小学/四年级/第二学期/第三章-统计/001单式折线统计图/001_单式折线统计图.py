"""单式折线统计图：同一统计量随时间的变化与相邻数据差值。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

DAYS = (1, 2, 3, 4, 5)
VALUES = (18, 20, 19, 23, 25)
assert len(DAYS) == len(VALUES)
assert VALUES[-1] - VALUES[0] == 7


class SingleLineChartLesson(Scene):
    """展示五天的同一观测指标；横轴是日期，纵轴是数量。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("单式折线统计图", font_size=38).to_edge(UP, buff=0.7)
        self.play(Write(title))
        axes = Axes(
            x_range=[1, 5, 1], y_range=[0, 30, 5],
            x_length=6, y_length=6,
            axis_config={"include_numbers": True}, tips=False,
        ).move_to(UP * 0.8)
        x_label = Text("日期（天）", font_size=22).next_to(axes.x_axis, DOWN, buff=0.5)
        y_label = Text("数量", font_size=22).next_to(axes.y_axis, UP, buff=0.3)
        self.play(Create(axes), Write(x_label), Write(y_label))

        points = [axes.c2p(day, value) for day, value in zip(DAYS, VALUES)]
        dots = VGroup(*[Dot(point, color=YELLOW, radius=0.07) for point in points])
        segments = VGroup(*[Line(points[i], points[i + 1], color=BLUE)
                            for i in range(len(points) - 1)])
        self.play(*[FadeIn(dot) for dot in dots])
        self.play(*[Create(segment) for segment in segments])
        note = Text("第 3 天略降，之后持续上升", font_size=27).move_to(DOWN * 4.2)
        summary = Text("第 5 天比第 1 天多 7", font_size=27).next_to(note, DOWN, buff=0.45)
        self.play(Write(note), Write(summary))
        self.wait(2)


if __name__ == "__main__":
    # manim -ql 001_单式折线统计图.py SingleLineChartLesson
    pass
