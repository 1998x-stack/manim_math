"""一年级：认识长方体，观察立体示意及三组相等的相对面。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
FONT = "PingFang SC"


def cuboid_face_pairs(length: int, width: int, height: int):
    """返回长方体三组相对面的面积；每组有两个大小相同的面。"""
    if any(type(v) is not int or v <= 0 for v in (length, width, height)):
        raise ValueError("长、宽、高必须是正整数")
    return ((length * width, length * width),
            (length * height, length * height),
            (width * height, width * height))


class Topic001长方体Animation(Scene):
    """二维投影表示立体长方体；图上可见三面不等于总共三面。"""

    def construct(self):
        assert cuboid_face_pairs(3, 2, 1) == ((6, 6), (3, 3), (2, 2))
        self.camera.background_color = BG
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7)
        title = Text("认识长方体", font=FONT, font_size=47, color=YELLOW)
        title.move_to(UP * 5.65)
        self.add(author)
        self.play(Write(title))

        introduction = Text(
            "文具盒的形状，常常像长方体",
            font=FONT, font_size=27
        ).move_to(UP * 4.3)
        self.play(FadeIn(introduction))

        # 平行投影仅展示正面、侧面与顶面三块可见面。
        front = Polygon(
            [-2.0, -0.7, 0], [0.8, -0.7, 0], [0.8, 1.4, 0],
            [-2.0, 1.4, 0],
            color=WHITE, fill_color=BLUE_D, fill_opacity=0.9
        )
        right = Polygon(
            [0.8, -0.7, 0], [1.7, 0.0, 0], [1.7, 2.1, 0],
            [0.8, 1.4, 0],
            color=WHITE, fill_color=BLUE_E, fill_opacity=0.9
        )
        top = Polygon(
            [-2.0, 1.4, 0], [0.8, 1.4, 0], [1.7, 2.1, 0],
            [-1.1, 2.1, 0],
            color=WHITE, fill_color=BLUE_B, fill_opacity=0.9
        )
        solid = VGroup(front, right, top).move_to(UP * 0.5)
        self.play(
            FadeIn(front), FadeIn(right), FadeIn(top),
            run_time=1.4
        )

        visible_note = Text(
            "图中能看见 3 个面，背后还有看不见的面",
            font=FONT, font_size=25
        ).move_to(DOWN * 2.35)
        self.play(Write(visible_note))

        total = Text("长方体共有 6 个面", font=FONT,
                     font_size=35, color=YELLOW).move_to(DOWN * 3.45)
        self.play(Write(total))
        self.wait(0.6)
        self.play(FadeOut(visible_note), FadeOut(total), FadeOut(solid),
                  FadeOut(introduction))

        pairs = [
            ("上面与下面", "大小相同"),
            ("前面与后面", "大小相同"),
            ("左面与右面", "大小相同")
        ]
        heading = Text("相对的两个面大小相同", font=FONT,
                       font_size=31, color=YELLOW).move_to(UP * 3.3)
        self.play(Write(heading))
        rows = VGroup(*[
            VGroup(
                Text(side, font=FONT, font_size=28),
                Text(label, font=FONT, font_size=26, color=GREEN)
            ).arrange(RIGHT, buff=0.6)
            for side, label in pairs
        ]).arrange(DOWN, buff=0.8).move_to(UP * 0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.45)
        summary = Text(
            "记住：6 个面，分成 3 组相对的面",
            font=FONT, font_size=27, color=YELLOW
        ).move_to(DOWN * 3.2)
        self.play(Write(summary))
        self.wait(1.4)
