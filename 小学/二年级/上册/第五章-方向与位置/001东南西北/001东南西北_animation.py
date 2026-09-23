"""《东南西北》竖屏完整版：认识四个基本方向，辨别地图方向与实际朝向。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001东南西北Animation(Scene):
    """以指北针为基准讲解方位，避免把“上北”表述为绝对方向。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=19, color=GRAY_B)
        author.move_to(UP * 7.2)
        title = Text("东南西北", font_size=47, color=GOLD).move_to(UP * 5.9)
        self.play(FadeIn(author), Write(title))

        self.show_compass()
        self.show_map_example()
        self.play(FadeOut(title), FadeOut(author))

    def show_compass(self):
        introduction = Text("以指北针为依据，认识四个方向", font_size=26)
        introduction.move_to(UP * 4.65)
        cross = VGroup(
            Line(LEFT * 2.0, RIGHT * 2.0, color=GRAY_B),
            Line(DOWN * 2.0, UP * 2.0, color=GRAY_B),
            Dot(radius=0.12, color=WHITE),
        )
        self.play(FadeIn(introduction), Create(cross))

        self.compass_items = VGroup()
        for character, vector, color in (
            ("北", UP, RED_B),
            ("南", DOWN, BLUE_B),
            ("西", LEFT, BLUE_B),
            ("东", RIGHT, BLUE_B),
        ):
            pointer = Arrow(ORIGIN, vector * 1.85, buff=0.15, color=color)
            label = Text(character, font_size=46, color=color).move_to(vector * 2.55)
            item = VGroup(pointer, label)
            self.play(GrowArrow(pointer), FadeIn(label), run_time=0.6)
            self.compass_items.add(item)
        self.play(FadeOut(introduction))
        self.compass = VGroup(cross, self.compass_items)

    def show_map_example(self):
        convention = Text("常见地图：上北下南，左西右东", font_size=27)
        convention.move_to(DOWN * 4.4)
        reminder = Text("地图旋转后，要重新看指北针", font_size=27, color=YELLOW)
        reminder.move_to(DOWN * 5.35)
        self.play(Write(convention), FadeIn(reminder))
        self.wait(1.5)
        # 把整个地图坐标示意（含指北针）一起旋转，而不是孤立改变某个方向。
        self.play(self.compass.animate.rotate(PI / 2), run_time=1.5)
        rotated = Text("旋转后的地图，上方不一定是北方", font_size=27, color=YELLOW)
        rotated.move_to(DOWN * 6.25)
        self.play(FadeIn(rotated))
        self.wait(1.5)
        self.play(FadeOut(self.compass), FadeOut(convention), FadeOut(reminder), FadeOut(rotated))
