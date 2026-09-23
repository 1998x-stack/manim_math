"""认识面积：以等大的单位正方形表示平面图形所占区域（竖屏）。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FONT = "PingFang SC"


class Topic001认识面积Animation(Scene):
    """保留历史 Scene 名称，避免破坏既有课程入口。"""

    def construct(self):
        self.camera.background_color = BG
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=18, color=GRAY_B).move_to(UP * 7)
        title = Text("认识面积", font=FONT, font_size=46, color=YELLOW).move_to(UP * 5.3)
        self.add(author)
        self.play(Write(title))

        definition = Text("面积表示图形所占区域的大小", font=FONT,
                          font_size=30).move_to(UP * 3.8)
        self.play(Write(definition))

        outline = Rectangle(width=3.6, height=2.4, color=BLUE,
                            fill_color=BLUE, fill_opacity=0.25).move_to(UP)
        self.play(FadeIn(outline))
        self.wait(0.4)
        self.play(FadeOut(outline))

        # 示意图：3 列 × 2 行。每个小正方形表示同一个面积单位。
        unit = 1.2
        tiles = VGroup(*[
            Square(side_length=unit, stroke_width=2, stroke_color=WHITE,
                   fill_color=BLUE, fill_opacity=0.7).move_to(
                       [(column - 1) * unit, (0.5 - row) * unit + 1, 0]
                   )
            for row in range(2) for column in range(3)
        ])
        for tile in tiles:
            self.play(FadeIn(tile), run_time=0.25)
        unit_label = Text("每格代表 1 平方厘米", font=FONT,
                          font_size=28).move_to(DOWN * 1.2)
        count = MathTex(r"3\times 2=6", font_size=54).move_to(DOWN * 2.3)
        answer = Text("面积是 6 平方厘米", font=FONT,
                      font_size=33, color=YELLOW).move_to(DOWN * 3.3)
        self.play(Write(unit_label))
        self.play(Write(count), Write(answer))
        self.wait(1.2)

        self.play(FadeOut(tiles), FadeOut(unit_label), FadeOut(count),
                  FadeOut(answer), FadeOut(definition))
        summary = VGroup(
            Text("面积：数一数同样大小的单位方格", font=FONT, font_size=28),
            Text("常用单位：平方厘米、平方米", font=FONT,
                 font_size=26, color=YELLOW),
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(1.2)
