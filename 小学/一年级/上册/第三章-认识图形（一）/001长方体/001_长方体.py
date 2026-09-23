"""认识长方体：用投影示意图展示正面、顶面、侧面三个可见面。

这是二维示意图，并不声称可见的三个面就是全部六个面。
渲染：manim -pql '001_长方体.py' 长方体Animation
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 长方体Animation(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("认识长方体", font="PingFang SC", font_size=52,
                     color=YELLOW).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.8)

        # 三个投影可见面：不用圆形冒充立体图形，也不把可见面数误认为总面数。
        front = Polygon(
            [-2.0, -1.0, 0], [0.8, -1.0, 0], [0.8, 1.1, 0], [-2.0, 1.1, 0],
            color=WHITE, fill_color=BLUE_D, fill_opacity=0.9,
        )
        right = Polygon(
            [0.8, -1.0, 0], [1.55, -0.4, 0], [1.55, 1.7, 0], [0.8, 1.1, 0],
            color=WHITE, fill_color=BLUE_E, fill_opacity=0.9,
        )
        top = Polygon(
            [-2.0, 1.1, 0], [0.8, 1.1, 0], [1.55, 1.7, 0], [-1.25, 1.7, 0],
            color=WHITE, fill_color=BLUE_B, fill_opacity=0.9,
        )
        cuboid = VGroup(front, right, top).move_to(UP * 0.9)
        self.play(FadeIn(front), FadeIn(right), FadeIn(top), run_time=1.5)
        note = Text("图中能看见3个面", font="PingFang SC", font_size=32,
                    color=WHITE).move_to(DOWN * 3.0)
        answer = Text("长方体一共有6个面", font="PingFang SC", font_size=40,
                      color=YELLOW).move_to(DOWN * 4.2)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1)
        self.play(Write(answer), run_time=0.8)
        self.wait(2)
