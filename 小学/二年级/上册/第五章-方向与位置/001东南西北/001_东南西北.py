"""东南西北：以指北针为依据阅读常见上北地图。"""
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920


class 东南西北Animation(Scene):
    """展示四个基本方向，说明“上北”是地图约定而非普遍规律。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("东南西北", font_size=48, color=GOLD).move_to(UP * 6.1)
        subtitle = Text("观察地图上的指北针", font_size=29).move_to(UP * 4.6)
        self.play(Write(title), FadeIn(subtitle))

        horizontal = Line(LEFT * 2.0, RIGHT * 2.0, color=GRAY_B)
        vertical = Line(DOWN * 2.0, UP * 2.0, color=GRAY_B)
        center = Dot(color=WHITE, radius=0.1)
        self.play(Create(horizontal), Create(vertical), FadeIn(center))

        directions = (
            ("北", UP * 2.55, UP * 1.85, RED_B),
            ("南", DOWN * 2.55, DOWN * 1.85, BLUE_B),
            ("西", LEFT * 2.55, LEFT * 1.85, BLUE_B),
            ("东", RIGHT * 2.55, RIGHT * 1.85, BLUE_B),
        )
        for name, label_position, arrow_end, color in directions:
            arrow = Arrow(ORIGIN, arrow_end, buff=0.15, color=color)
            label = Text(name, font_size=46, color=color).move_to(label_position)
            self.play(GrowArrow(arrow), FadeIn(label), run_time=0.6)

        convention = Text("常见地图：上北下南，左西右东", font_size=27)
        convention.move_to(DOWN * 4.4)
        reminder = Text("实际方向请看图例或指北针", font_size=26, color=YELLOW)
        reminder.move_to(DOWN * 5.4)
        self.play(Write(convention), FadeIn(reminder))
        self.wait(2)
