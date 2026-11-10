"""认识平面图形：描出轮廓，区分四种基本图形。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"


def straight_side_counts():
    return {"长方形": 4, "正方形": 4, "三角形": 3, "圆": 0}


class Topic001认识平面图形Animation(Scene):
    """完整二维描边与图形识别课，保留历史类名。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=20, color=GRAY_B).move_to(UP * 7.3)
        title = Text("认识平面图形", font=FONT,
                     font_size=44, color=GOLD).move_to(UP * 5.5)
        hint = Text("沿着平平的面描一圈", font=FONT,
                    font_size=29).move_to(UP * 4.4)
        self.play(FadeIn(author), Write(title), FadeIn(hint))
        outline = Rectangle(width=2.7, height=1.5,
                            color=YELLOW, stroke_width=5).move_to(UP * 2.65)
        self.play(Create(outline), run_time=1.3)
        self.play(FadeIn(Text("描出的轮廓是平面图形", font=FONT,
                              font_size=26).next_to(outline, DOWN, buff=0.3)))
        self.wait(0.5)
        self.clear()
        self.add(author, title)
        shapes = [
            ("长方形", Rectangle(width=2.1, height=1.3, color=BLUE_B)),
            ("正方形", Square(side_length=1.55, color=GREEN)),
            ("三角形", Polygon([-0.95, -0.75, 0], [0.95, -0.75, 0],
                              [0, 0.9, 0], color=ORANGE)),
            ("圆", Circle(radius=0.82, color=YELLOW)),
        ]
        points = [LEFT*1.8 + UP*1.9, RIGHT*1.8 + UP*1.9,
                  LEFT*1.8 + DOWN*1.5, RIGHT*1.8 + DOWN*1.5]
        for (name, shape), position in zip(shapes, points):
            shape.move_to(position)
            label = Text(name, font=FONT, font_size=29).next_to(
                shape, DOWN, buff=0.3)
            self.play(Create(shape), FadeIn(label), run_time=0.8)
        counts = straight_side_counts()
        assert counts == {"长方形": 4, "正方形": 4, "三角形": 3, "圆": 0}
        note = Text("三角形有3条直边；圆没有直边", font=FONT,
                    font_size=26, color=YELLOW).move_to(DOWN * 5.0)
        find = Text("在生活中寻找这些图形", font=FONT,
                    font_size=27, color=GREEN).move_to(DOWN * 6.0)
        self.play(Write(note), FadeIn(find))
        self.wait(2)
