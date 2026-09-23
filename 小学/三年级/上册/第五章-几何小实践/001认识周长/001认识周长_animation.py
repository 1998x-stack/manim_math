"""认识周长：以闭合边界和长度加法解释周长（竖屏）。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FONT = "PingFang SC"


class Topic001认识周长Animation(Scene):
    """保留历史 Scene 名称，避免破坏既有课程入口。"""

    def construct(self):
        self.camera.background_color = BG
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=18, color=GRAY_B).move_to(UP * 7)
        title = Text("认识周长", font=FONT, font_size=46, color=YELLOW).move_to(UP * 5.3)
        self.add(author)
        self.play(Write(title))

        definition = Text("封闭图形一周边线的长度，就是周长", font=FONT,
                          font_size=26).move_to(UP * 3.8)
        self.play(Write(definition))

        # 长 4、宽 2 的长方形（示意图）；沿四条边连续描画，最终回到起点。
        vertices = [(-2, 2), (2, 2), (2, 0), (-2, 0), (-2, 2)]
        border = VGroup(*[
            Line([*vertices[i], 0], [*vertices[i + 1], 0],
                 color=YELLOW, stroke_width=8)
            for i in range(4)
        ])
        for edge in border:
            self.play(Create(edge), run_time=0.65)
        lengths = VGroup(
            Text("长 4 厘米", font=FONT, font_size=26).move_to(UP * 2.65),
            Text("宽 2 厘米", font=FONT, font_size=26).move_to(RIGHT * 3 + UP),
        )
        self.play(FadeIn(lengths))
        self.wait(0.5)

        question = Text("四条边的长度相加", font=FONT, font_size=30,
                        color=BLUE).move_to(DOWN * 1.1)
        formula = MathTex(r"4+2+4+2=12", font_size=50).move_to(DOWN * 2.2)
        answer = Text("周长是 12 厘米", font=FONT, font_size=32,
                      color=YELLOW).move_to(DOWN * 3.2)
        self.play(Write(question))
        self.play(Write(formula), Write(answer))
        self.wait(1.2)

        self.play(FadeOut(border), FadeOut(lengths), FadeOut(question),
                  FadeOut(formula), FadeOut(answer), FadeOut(definition))
        summary = VGroup(
            Text("周长：沿边界一周的长度", font=FONT, font_size=34),
            Text("用厘米、米等长度单位表示", font=FONT, font_size=28,
                 color=YELLOW),
        ).arrange(DOWN, buff=0.65).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(1.2)
