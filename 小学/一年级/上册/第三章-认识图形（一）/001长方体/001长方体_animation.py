"""认识长方体：二维投影画出三张可见面，讲清六个面。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"


def opposite_face_pairs():
    return (("前面", "后面"), ("左面", "右面"), ("上面", "下面"))


class Topic001长方体Animation(Scene):
    """保留历史 Scene 名称，避免将三个可见面误认为全部面。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm",
                      font=FONT, font_size=20, color=GRAY_B).move_to(UP * 7.3)
        title = Text("认识长方体", font=FONT, font_size=48,
                     color=GOLD).move_to(UP * 5.5)
        question = Text("文具盒有几个面？", font=FONT,
                        font_size=31).move_to(UP * 4.3)
        self.play(FadeIn(author), Write(title), FadeIn(question))
        front = Polygon([-2.0, -1.2, 0], [1.2, -1.2, 0],
                        [1.2, 1.2, 0], [-2.0, 1.2, 0],
                        color=BLUE_B, fill_opacity=0.3, stroke_width=4)
        top = Polygon([-2.0, 1.2, 0], [1.2, 1.2, 0],
                      [2.1, 2.0, 0], [-1.1, 2.0, 0],
                      color=YELLOW, fill_opacity=0.25, stroke_width=4)
        side = Polygon([1.2, -1.2, 0], [2.1, -0.4, 0],
                       [2.1, 2.0, 0], [1.2, 1.2, 0],
                       color=GREEN, fill_opacity=0.3, stroke_width=4)
        VGroup(front, top, side).shift(UP * 0.3)
        self.play(Create(front), FadeIn(top), FadeIn(side), run_time=2)
        names = VGroup(
            Text("前面", font=FONT, font_size=28).move_to([-0.5, 0.4, 0]),
            Text("上面", font=FONT, font_size=26).move_to([0, 2.05, 0]),
            Text("侧面", font=FONT, font_size=24).move_to([2.4, 0.3, 0]),
        )
        self.play(FadeIn(names))
        visible = Text("图中能看见3个面", font=FONT,
                       font_size=30).move_to(DOWN * 3)
        total = Text("长方体一共有6个面", font=FONT,
                     font_size=37, color=YELLOW).move_to(DOWN * 4)
        self.play(Write(visible), Write(total))
        self.play(Indicate(front), Indicate(top), Indicate(side))
        pairs = opposite_face_pairs()
        assert len(pairs) == 3
        fact = Text("前后、左右、上下面两两相对", font=FONT,
                    font_size=26, color=GREEN).move_to(DOWN * 5.1)
        equal = Text("相对的面形状、大小相同", font=FONT,
                     font_size=27).move_to(DOWN * 6.05)
        self.play(FadeIn(fact), Write(equal))
        self.wait(2)
