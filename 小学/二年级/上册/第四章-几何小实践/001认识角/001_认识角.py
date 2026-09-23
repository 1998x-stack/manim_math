"""认识角：一个顶点，两条从同一点出发的射线。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 认识角Animation(Scene):
    """使用有共同顶点的两条射线与角弧，不用无关圆形充当角。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("认识角", font_size=47, color=GOLD).move_to(UP * 6.2)
        definition = Text("一个顶点，两条从顶点出发的射线", font_size=29)
        definition.move_to(UP * 4.7)
        self.play(Write(title), FadeIn(definition))

        vertex = Dot(ORIGIN, radius=0.12, color=YELLOW)
        side_one = Arrow(ORIGIN, RIGHT * 2.7, buff=0, color=BLUE_B)
        side_two = Arrow(ORIGIN, RIGHT * 2.7, buff=0, color=BLUE_B)
        side_two.rotate(PI / 3, about_point=ORIGIN)
        interior = Arc(radius=0.72, start_angle=0, angle=PI / 3, color=YELLOW)
        vertex_label = Text("顶点", font_size=27, color=YELLOW)
        vertex_label.move_to(LEFT * 0.65 + DOWN * 0.75)
        side_label = Text("两条边", font_size=29, color=BLUE_B).move_to(RIGHT * 1.0 + UP * 2.7)

        self.play(FadeIn(vertex), GrowArrow(side_one), GrowArrow(side_two))
        self.play(Create(interior), FadeIn(vertex_label), FadeIn(side_label))
        self.wait(0.8)
        self.play(FadeOut(vertex_label), FadeOut(side_label))

        takeaway = Text("角的大小与张开的程度有关", font_size=28)
        takeaway.move_to(DOWN * 3.5)
        self.play(Write(takeaway))
        self.play(
            side_one.animate.scale(1.25, about_point=ORIGIN),
            side_two.animate.scale(1.25, about_point=ORIGIN),
            run_time=1.2,
        )
        self.play(FadeIn(Text("两边变长，角的大小不变", font_size=27, color=GREEN)
                         .move_to(DOWN * 4.45)))
        self.wait(2)
