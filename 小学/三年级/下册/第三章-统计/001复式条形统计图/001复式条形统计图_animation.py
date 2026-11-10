"""复式条形统计图：双组数据用相同刻度、并列柱形和图例展示（竖屏）。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FONT = "PingFang SC"
# 一班和二班阅读人数的教学示例；非真实调查数据。
SAMPLE = (("一班", 6, 8), ("二班", 5, 7))


def group_differences(sample):
    """每组第二类人数减第一类人数；同一刻度下比较。"""
    records = tuple(sample)
    if not records:
        raise ValueError("至少需要一组数据")
    diffs = []
    for name, boys, girls in records:
        if not isinstance(name, str) or any(type(n) is not int or n < 0 for n in (boys, girls)):
            raise ValueError("类别名需是文本且人数为非负整数")
        diffs.append(girls - boys)
    return tuple(diffs)


class Topic001复式条形统计图Animation(Scene):
    """保留历史 Scene 名称，避免破坏既有课程入口。"""

    def construct(self):
        differences = group_differences(SAMPLE)
        assert differences == (2, 2)
        self.camera.background_color = BG
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=18, color=GRAY_B).move_to(UP * 7)
        title = Text("复式条形统计图", font=FONT,
                     font_size=43, color=YELLOW).move_to(UP * 5.4)
        self.add(author)
        self.play(Write(title))

        question = Text("示例：两班课外阅读人数（人）", font=FONT,
                        font_size=28).move_to(UP * 4.3)
        legend = VGroup(
            Text("■ 男生", font=FONT, font_size=27, color=BLUE),
            Text("■ 女生", font=FONT, font_size=27, color=ORANGE),
        ).arrange(RIGHT, buff=0.5).move_to(UP * 3.5)
        self.play(Write(question), FadeIn(legend))

        baseline_y, scale = -2.0, 0.42
        axis = VGroup(
            Line([-2.9, baseline_y, 0], [2.9, baseline_y, 0], color=WHITE),
            Line([-2.9, baseline_y, 0], [-2.9, baseline_y + 10 * scale, 0],
                 color=WHITE),
        )
        tick_labels = VGroup()
        for value in range(0, 11, 2):
            tick_y = baseline_y + value * scale
            tick_labels.add(Text(str(value), font_size=20).move_to([-3.3, tick_y, 0]))
        self.play(Create(axis), FadeIn(tick_labels))

        # 相同刻度下，一班和二班各展示男女生两根并列的柱形。
        for index, (name, boys, girls) in enumerate(SAMPLE):
            x_center = -1.4 if index == 0 else 1.4
            for offset, value, color in ((-0.38, boys, BLUE), (0.38, girls, ORANGE)):
                height = value * scale
                bar = Rectangle(width=0.62, height=height,
                                stroke_color=color, fill_color=color,
                                fill_opacity=0.86).move_to(
                                    [x_center + offset, baseline_y + height / 2, 0]
                                )
                value_label = Text(str(value), font_size=25).next_to(bar, UP, buff=0.08)
                self.play(FadeIn(bar), FadeIn(value_label), run_time=0.35)
            name_label = Text(name, font=FONT, font_size=27).move_to(
                [x_center, baseline_y - 0.48, 0]
            )
            self.play(Write(name_label))

        conclusion = Text(f"两班女生均比男生多 {differences[0]} 人", font=FONT,
                          font_size=29, color=YELLOW).move_to(DOWN * 4.1)
        self.play(Write(conclusion))
        self.wait(1.2)
