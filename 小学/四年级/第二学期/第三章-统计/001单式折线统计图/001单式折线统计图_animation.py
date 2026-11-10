"""单式折线统计图：五天数据，描点、连线、标数，分析变化。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
DAYS = (1, 2, 3, 4, 5)
VALUES = (18, 20, 19, 23, 25)


def daily_changes(values):
    if len(values) < 2:
        raise ValueError("at least two observations")
    return tuple(b - a for a, b in zip(values, values[1:]))


class Topic001单式折线统计图Animation(Scene):
    """与历史渲染入口同名的真实折线统计课程。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=20, color=GRAY_B).move_to(UP * 7.3)
        title = Text("单式折线统计图", font=FONT, font_size=43,
                     color=GOLD).move_to(UP * 5.6)
        prompt = Text("五天的阅读数量怎样变化？", font=FONT,
                      font_size=27).move_to(UP * 4.5)
        self.play(FadeIn(author), Write(title), FadeIn(prompt))
        axes = Axes(x_range=[0, 6, 1], y_range=[0, 30, 5],
                    x_length=6.0, y_length=5.0, tips=False,
                    axis_config={"color": GRAY_B}).move_to(UP * 0.1)
        self.play(Create(axes))
        for day in DAYS:
            tick = Text(str(day), font_size=23).move_to(axes.c2p(day, 0) + DOWN * 0.4)
            self.play(FadeIn(tick), run_time=0.12)
        for value in range(0, 31, 5):
            tick = Text(str(value), font_size=21).move_to(axes.c2p(0, value) + LEFT * 0.35)
            self.add(tick)
        self.play(FadeIn(Text("横轴：日期  纵轴：数量", font=FONT,
                              font_size=25).move_to(DOWN * 3.25)))
        dots = [Dot(axes.c2p(day, value), radius=0.075, color=YELLOW)
                for day, value in zip(DAYS, VALUES)]
        for i, dot in enumerate(dots):
            self.play(FadeIn(dot), FadeIn(Text(str(VALUES[i]), font_size=23,
                          color=YELLOW).next_to(dot, UP, buff=0.13)), run_time=0.33)
            if i:
                self.play(Create(Line(dots[i-1].get_center(), dot.get_center(),
                                      color=BLUE_B, stroke_width=5)), run_time=0.42)
        changes = daily_changes(VALUES)
        assert changes == (2, -1, 4, 2)
        assert sum(changes) == VALUES[-1] - VALUES[0] == 7
        down = Text("第3天比第2天少1，随后连续上升", font=FONT,
                    font_size=26, color=GREEN).move_to(DOWN * 4.5)
        diff = MathTex(r"25-18=7", font_size=52).move_to(DOWN * 5.45)
        summary = Text("描点、连线、标数，读出增减趋势", font=FONT,
                       font_size=26, color=YELLOW).move_to(DOWN * 6.35)
        self.play(Write(down), Write(diff), FadeIn(summary))
        self.wait(2)
