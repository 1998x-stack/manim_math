"""一年级《数一数》：一一对应地数 5 个苹果和 6 颗星星。

渲染：manim -pql counting_animation.py CountingAnimation
沿用原课程的四段分镜、9:16 画幅与作者标识；不自动替换已发布的视频。
"""

import math

import numpy as np
from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
BACKGROUND = "#1a1a2e"
PRIMARY = "#3498db"
SECONDARY = "#e74c3c"
HIGHLIGHT = "#f1c40f"


def count_labels(total):
    """返回与物体一一对应的自然数标签；本课最多展示 10 个物体。"""
    if type(total) is not int or not 0 <= total <= 10:
        raise ValueError("本课物体数量必须是 0～10 的整数")
    return tuple(range(1, total + 1))


def star_vertices(outer_radius=1.0, inner_radius=0.4):
    """按极角递增交替排列五个外顶点和五个内顶点，得到不自交的五角星轮廓。"""
    if not 0 < inner_radius < outer_radius:
        raise ValueError("需要满足 0 < inner_radius < outer_radius")
    vertices = []
    for index in range(10):
        radius = outer_radius if index % 2 == 0 else inner_radius
        angle = -math.pi / 2 + index * math.pi / 5
        vertices.append((radius * math.cos(angle), radius * math.sin(angle), 0.0))
    return tuple(vertices)


class Star(Polygon):
    """可填充的简单五角星（不是相互交叉的五芒星折线）。"""

    def __init__(self, outer_radius=1.0, inner_radius=0.4, **kwargs):
        vertices = [np.array(vertex) for vertex in star_vertices(outer_radius, inner_radius)]
        super().__init__(*vertices, **kwargs)


class CountingAnimation(Scene):
    """四个教学阶段：引题、苹果点数、星星练习、总结。"""

    def construct(self):
        self.camera.background_color = BACKGROUND
        self.grid_positions = [
            np.array([-3.2 + col * 1.6, 2.0 - row * 2.5, 0.0])
            for row in range(2)
            for col in range(5)
        ]
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=20, color=GRAY_B,
        ).move_to(UP * 7.4)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.5)
        self.show_opening()
        self.show_counting_demo()
        self.show_interactive_practice()
        self.show_summary()

    def show_opening(self):
        title = Text("数一数", font=FONT, font_size=48, color=GOLD).move_to(UP * 6)
        subtitle = Text(
            "学会一个一个地数", font=FONT, font_size=28, color=GRAY_A,
        ).move_to(UP * 5.2)
        shapes = VGroup(
            Circle(radius=0.4, color=PRIMARY, fill_opacity=0.7),
            Square(side_length=0.8, color=SECONDARY, fill_opacity=0.7),
            Triangle(color=HIGHLIGHT, fill_opacity=0.7).scale(0.65),
        ).arrange(RIGHT, buff=1.2).move_to(UP * 2)
        marks = VGroup(*[
            Text("?", font_size=32, color=WHITE).move_to(shape.get_center())
            for shape in shapes
        ])
        hint = Text(
            "这里有几个图形？", font=FONT, font_size=30, color=HIGHLIGHT,
        ).move_to(DOWN * 4.5)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        self.play(Create(shapes), Write(marks), run_time=1.2)
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1.5)
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(hint),
            FadeOut(marks), FadeOut(shapes), run_time=0.6,
        )

    def _show_counting(self, objects, pause=0.8):
        """始终只有一个数字标签；先替换上一数字，再高亮当前物体。"""
        current_number = None
        for index, label in enumerate(count_labels(len(objects))):
            next_number = Text(
                str(label), font=FONT, font_size=60, color=HIGHLIGHT,
            ).move_to(UP * 4)
            highlight = Circle(radius=0.48, color=HIGHLIGHT, stroke_width=6)
            highlight.move_to(objects[index].get_center())
            if current_number is None:
                number_animation = FadeIn(next_number)
            else:
                number_animation = ReplacementTransform(current_number, next_number)
            self.play(number_animation, Create(highlight), run_time=0.6)
            current_number = next_number
            self.wait(pause)
            self.play(FadeOut(highlight), run_time=0.25)
        return current_number

    def show_counting_demo(self):
        instruction = Text(
            "数数要一个一个地数哦！", font=FONT, font_size=32, color=PRIMARY,
        ).move_to(UP * 6)
        self.play(Write(instruction), run_time=0.8)
        apples = VGroup()
        for position in self.grid_positions[:5]:
            fruit = Circle(radius=0.35, color=SECONDARY, fill_opacity=0.8)
            stem = Line(fruit.get_top(), fruit.get_top() + UP * 0.2, color="#8B4513")
            leaf = Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(
                fruit.get_top() + UP * 0.15 + RIGHT * 0.1
            )
            apples.add(VGroup(fruit, stem, leaf).move_to(position))
        self.play(LaggedStart(*[FadeIn(a) for a in apples], lag_ratio=0.4), run_time=2.0)
        number = self._show_counting(apples)
        total = Text("一共有5个苹果！", font=FONT, font_size=32, color=SECONDARY)
        total.move_to(DOWN * 4)
        self.play(Write(total), run_time=0.8)
        self.wait(1.5)
        self.play(
            FadeOut(instruction), FadeOut(total), FadeOut(apples),
            FadeOut(number), run_time=0.7,
        )

    def show_interactive_practice(self):
        title = Text("现在轮到你啦！", font=FONT, font_size=40, color=HIGHLIGHT)
        title.move_to(UP * 6)
        instruction = Text("一起来数星星吧！", font=FONT, font_size=32, color=PRIMARY)
        instruction.move_to(UP * 5)
        self.play(Write(title), Write(instruction), run_time=0.8)
        stars = VGroup(*[
            Star(outer_radius=0.3, inner_radius=0.13, color=YELLOW, fill_opacity=1)
            .move_to(position)
            for position in self.grid_positions[:6]
        ])
        self.play(LaggedStart(*[FadeIn(star) for star in stars], lag_ratio=0.4), run_time=2.5)
        self.wait(1.5)  # 留出学生先独立点数的时间
        number = self._show_counting(stars, pause=0.9)
        result = Text("一共有6颗星星！", font=FONT, font_size=32, color=SECONDARY)
        result.move_to(DOWN * 4)
        self.play(Write(result), run_time=0.7)
        self.wait(1.5)
        self.play(
            FadeOut(title), FadeOut(instruction), FadeOut(result),
            FadeOut(stars), FadeOut(number), run_time=0.8,
        )

    def show_summary(self):
        title = Text("今天学到的知识：", font=FONT, font_size=36, color=GOLD)
        title.move_to(UP * 4)
        points = VGroup(
            Text("① 一个物体对应一个数", font=FONT, font_size=28, color=PRIMARY),
            Text("② 手指一个，嘴巴数一个", font=FONT, font_size=28, color=SECONDARY),
            Text("③ 不重复，也不漏掉", font=FONT, font_size=28, color=HIGHLIGHT),
        ).arrange(DOWN, buff=0.7, aligned_edge=LEFT).move_to(UP * 0.8)
        encouragement = Text(
            "你已经学会了数数！\n继续加油哦！", font=FONT,
            font_size=32, color=HIGHLIGHT,
        ).move_to(DOWN * 2.2)
        follow = Text(
            "关注我，获得更多数学技巧！", font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 5)
        self.play(Write(title), run_time=0.6)
        self.play(LaggedStart(*[Write(point) for point in points], lag_ratio=0.6), run_time=2.4)
        self.wait(2)
        self.play(FadeIn(encouragement), run_time=0.8)
        self.play(FadeIn(follow), run_time=0.5)
        self.wait(2)
