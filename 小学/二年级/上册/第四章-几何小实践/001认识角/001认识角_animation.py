"""认识角（完整版）：一个顶点，两条射线；张开程度决定角的大小。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001认识角Animation(Scene):
    """用真正的角结构和两边伸长的对照实验代替泛化模板。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=19, color=GRAY_B)
        author.move_to(UP * 7.2)
        title = Text("认识角", font_size=48, color=GOLD).move_to(UP * 5.85)
        self.play(FadeIn(author), Write(title))

        definition = Text("从同一个顶点出发的两条射线组成一个角", font_size=26)
        definition.move_to(UP * 4.45)
        self.play(Write(definition))

        first = self.make_angle(60, 2.4)
        self.play(FadeIn(first), run_time=1.1)
        vertex_label = Text("顶点", font_size=27, color=YELLOW).move_to(LEFT * 0.7 + DOWN * 0.75)
        side_label = Text("角的两条边", font_size=27, color=BLUE_B).move_to(RIGHT * 1.3 + UP * 2.1)
        self.play(FadeIn(vertex_label), FadeIn(side_label))
        self.wait(0.8)
        self.play(FadeOut(vertex_label), FadeOut(side_label), FadeOut(definition))

        unchanged = Text("两条射线延长，张开程度不变", font_size=28)
        unchanged.move_to(DOWN * 3.25)
        self.play(Write(unchanged))
        self.play(
            first[1].animate.scale(1.25, about_point=ORIGIN),
            first[2].animate.scale(1.25, about_point=ORIGIN),
            run_time=1.25,
        )
        same_angle = Text("角的大小仍然相同", font_size=28, color=GREEN)
        same_angle.move_to(DOWN * 4.3)
        self.play(FadeIn(same_angle))
        self.wait(1)
        self.play(FadeOut(first), FadeOut(unchanged), FadeOut(same_angle))

        # 比较的是张开的程度，弧度和射线端点由同一个角度参数产生。
        narrow = self.make_angle(35, 2.1).shift(LEFT * 1.4)
        wide = self.make_angle(105, 2.1).shift(RIGHT * 1.1)
        narrow_label = Text("张开小", font_size=26, color=BLUE_B).move_to(LEFT * 2 + DOWN * 2.25)
        wide_label = Text("张开大", font_size=26, color=YELLOW).move_to(RIGHT * 2 + DOWN * 2.25)
        self.play(FadeIn(narrow), FadeIn(wide))
        self.play(FadeIn(narrow_label), FadeIn(wide_label))
        self.wait(2)

    @staticmethod
    def make_angle(degrees, length):
        assert 0 < degrees < 180
        vertex = Dot(ORIGIN, radius=0.12, color=YELLOW)
        first = Arrow(ORIGIN, RIGHT * length, buff=0, color=BLUE_B)
        second = Arrow(ORIGIN, RIGHT * length, buff=0, color=BLUE_B)
        second.rotate(degrees * DEGREES, about_point=ORIGIN)
        arc = Arc(radius=0.65, start_angle=0, angle=degrees * DEGREES, color=YELLOW)
        return VGroup(vertex, first, second, arc)
