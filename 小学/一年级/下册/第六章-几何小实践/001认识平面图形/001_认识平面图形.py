"""认识平面图形：对应展示圆形、三角形、正方形和长方形。

四个图形是例子而不是互斥且穷尽的数学分类。
渲染：manim -pql '001_认识平面图形.py' 认识平面图形Animation
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 认识平面图形Animation(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("认识平面图形", font="PingFang SC", font_size=50,
                     color=YELLOW).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.8)

        examples = (
            (Circle(radius=0.55, color=BLUE, fill_opacity=0.7), "圆形"),
            (Triangle(color=GREEN, fill_opacity=0.7).scale(0.75), "三角形"),
            (Square(side_length=1.05, color=ORANGE, fill_opacity=0.7), "正方形"),
            (Rectangle(width=1.45, height=0.9, color=PURPLE,
                       fill_opacity=0.7), "长方形"),
        )
        tiles = VGroup()
        for shape, name in examples:
            label = Text(name, font="PingFang SC", font_size=29,
                         color=WHITE).next_to(shape, DOWN, buff=0.35)
            tiles.add(VGroup(shape, label))
        tiles.arrange_in_grid(rows=2, cols=2, buff=(1.0, 1.0)).move_to(UP * 0.7)

        question = Text("你能说出它们的名字吗？", font="PingFang SC",
                        font_size=29, color=WHITE).move_to(DOWN * 3.7)
        self.play(LaggedStart(*[FadeIn(tile) for tile in tiles],
                              lag_ratio=0.35), run_time=2.0)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(2)
        answer = Text("这些都是平面图形的例子", font="PingFang SC",
                      font_size=29, color=YELLOW).move_to(DOWN * 4.8)
        self.play(FadeIn(answer), run_time=0.6)
        self.wait(2)
