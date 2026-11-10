"""四年级：单式折线统计图，按描点、连线、标数观察变化趋势。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
BG = "#1a1a2e"
DAYS = (1, 2, 3, 4, 5)
VALUES = (18, 20, 19, 23, 25)


def line_chart_changes(days, values):
    """同一量按时间排列，返回相邻差值、首尾净变化及最大涨幅。"""
    xs, ys = tuple(days), tuple(values)
    if (len(xs) < 2 or len(xs) != len(ys)
            or any(type(v) is not int for v in xs + ys)
            or any(xs[i] >= xs[i + 1] for i in range(len(xs) - 1))):
        raise ValueError("日期必须严格递增，且两列为等长整数序列")
    differences = tuple(ys[i + 1] - ys[i] for i in range(len(ys) - 1))
    return differences, ys[-1] - ys[0], max(differences)


class Topic001单式折线统计图Animation(Scene):
    """同一统计量的五日变化：先描点、后连线、再读趋势。"""

    def construct(self):
        assert line_chart_changes(DAYS, VALUES) == ((2, -1, 4, 2), 7, 4)
        self.camera.background_color = BG
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7)
        title = Text("单式折线统计图", font=FONT, font_size=44,
                     color=YELLOW).move_to(UP * 5.6)
        self.add(author)
        self.play(Write(title))

        question = Text(
            "五天读书人数的变化（示例数据）",
            font=FONT, font_size=27
        ).move_to(UP * 4.5)
        self.play(FadeIn(question))

        axes = Axes(
            x_range=[0, 6, 1], y_range=[0, 30, 5],
            x_length=6.0, y_length=5.0, tips=False,
            axis_config={"include_numbers": True}
        ).move_to(UP * 0.5)
        x_label = Text("日期（天）", font=FONT, font_size=22)
        x_label.next_to(axes.x_axis, DOWN, buff=0.4)
        y_label = Text("人数", font=FONT, font_size=22)
        y_label.next_to(axes.y_axis, UP, buff=0.3)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        points = [axes.c2p(day, value) for day, value in zip(DAYS, VALUES)]
        dots = VGroup(*[Dot(point, color=YELLOW, radius=0.09)
                        for point in points])
        values = VGroup(*[
            Text(str(value), font=FONT, font_size=22).next_to(dot, UP, buff=0.12)
            for value, dot in zip(VALUES, dots)
        ])
        # 教学顺序：逐个描点，明确每个点对应一个日期和值。
        for dot, label in zip(dots, values):
            self.play(FadeIn(dot), FadeIn(label), run_time=0.38)
        segments = VGroup(*[
            Line(points[i], points[i + 1], color=BLUE_B, stroke_width=5)
            for i in range(len(points) - 1)
        ])
        for segment in segments:
            self.play(Create(segment), run_time=0.4)

        differences, net, greatest = line_chart_changes(DAYS, VALUES)
        assert net == 7 and greatest == 4
        notes = VGroup(
            Text("第3天比第2天少1人", font=FONT, font_size=26),
            Text("第3天到第4天增加4人，涨幅最大", font=FONT, font_size=24,
                 color=YELLOW),
            Text("第5天比第1天多7人", font=FONT, font_size=26,
                 color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 4.25)
        self.play(LaggedStart(*(FadeIn(note) for note in notes),
                              lag_ratio=0.3))
        self.wait(1.0)
        self.play(FadeOut(axes), FadeOut(dots), FadeOut(values),
                  FadeOut(segments), FadeOut(x_label), FadeOut(y_label),
                  FadeOut(question), FadeOut(notes))

        takeaway = VGroup(
            Text("描点 → 连线 → 标数", font=FONT, font_size=36,
                 color=YELLOW),
            Text("线段向上：数量增加", font=FONT, font_size=29),
            Text("线段向下：数量减少", font=FONT, font_size=29),
            Text("预测趋势应结合更多实际信息", font=FONT, font_size=26),
        ).arrange(DOWN, buff=0.65).move_to(UP * 0.6)
        self.play(LaggedStart(*(Write(row) for row in takeaway),
                              lag_ratio=0.3))
        self.wait(1.2)
