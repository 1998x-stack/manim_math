"""复式条形统计图简短示例；完整课程见同目录 001复式条形统计图_animation.py。"""

from manim import *


class GroupedBarChartPreview(Scene):
    """同一类别内并列展示两组数据，数据值与柱形高度一一对应。"""

    def construct(self):
        title = Text("复式条形统计图", font_size=42).to_edge(UP)
        legend = VGroup(
            Text("■ 男生", color=BLUE, font_size=26),
            Text("■ 女生", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.55).next_to(title, DOWN, buff=0.25)
        self.play(Write(title), FadeIn(legend))

        # 示例数据：一班男生 6、女生 8；二班男生 5、女生 7。
        baseline_y = -1.7
        scale = 0.36
        baseline = Line(LEFT * 2.7, RIGHT * 2.7).shift(UP * baseline_y)
        self.play(Create(baseline))
        for x, value, color in [(-1.8, 6, BLUE), (-1.0, 8, ORANGE),
                                (1.0, 5, BLUE), (1.8, 7, ORANGE)]:
            height = value * scale
            bar = Rectangle(
                width=0.56, height=height, fill_color=color,
                fill_opacity=0.85, stroke_color=color,
            ).move_to([x, baseline_y + height / 2, 0])
            number = Text(str(value), font_size=26).next_to(bar, UP, buff=0.08)
            self.play(FadeIn(bar), Write(number), run_time=0.4)

        labels = VGroup(
            Text("一班", font_size=28).move_to([-1.4, -2.25, 0]),
            Text("二班", font_size=28).move_to([1.4, -2.25, 0]),
        )
        self.play(FadeIn(labels))
        self.wait(1)
