"""高三第十四章：平面的基本性质。所有平面多边形仅为无限平面的局部示意。"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE = "#4FC3F7"
GREEN = "#81C784"
YELLOW = "#FFD54F"
ORANGE = "#FF8A65"
PURPLE = "#CE93D8"
PINK = "#F06292"


def patch(vertices, color):
    """画出无限平面的一块有限示意区域，而非平面的边界。"""
    return Polygon(*[np.array((x, y, 0.0)) for x, y in vertices],
                   color=color, fill_color=color, fill_opacity=0.17,
                   stroke_width=2.5)


def safe_text(message, size=27, color=WHITE):
    """长中文句子适配竖屏安全区。"""
    label = Text(message, font_size=size, color=color)
    if label.width > 7.4:
        label.scale_to_fit_width(7.4)
    return label


class PlaneAxiomsScene(Scene):
    """保留原入口类名；依次解释平面概念和三个公理。"""

    def construct(self):
        self.camera.background_color = BG
        self.author_info = safe_text("高中数学 · 空间直线与平面", 20, GRAY_B)
        self.author_info.move_to(UP * 7.25)
        self.add(self.author_info)
        self.scene_1_opening()
        self.scene_2_plane_concept()
        self.scene_3_axiom1()
        self.scene_4_axiom2()
        self.scene_5_axiom3()
        self.scene_6_conditions()
        self.scene_7_outro()

    def clear_lesson(self):
        """只移除当前镜头对象，不重复 FadeOut 未添加的临时对象。"""
        others = [m for m in self.mobjects if m is not self.author_info]
        if others:
            self.play(*[FadeOut(m) for m in others], run_time=0.4)

    def heading(self, title, subtitle):
        header = safe_text(title, 39, PURPLE).move_to(UP * 5.8)
        detail = safe_text(subtitle, 25, GRAY_A).move_to(UP * 5.05)
        self.play(Write(header), FadeIn(detail), run_time=0.7)

    def point(self, x, y, name, direction=UP):
        dot = Dot([x, y, 0], radius=0.10, color=ORANGE)
        label = MathTex(name, font_size=35, color=WHITE).next_to(dot, direction, buff=0.12)
        return dot, label

    def scene_1_opening(self):
        self.heading("为什么三点可以确定平面？", "先看三脚架的三个落地点")
        coordinates = [(-1.6, 0.2), (1.6, 0.2), (0.0, 2.0)]
        dots_and_labels = [self.point(x, y, name) for (x, y), name in
                           zip(coordinates, ("A", "B", "C"))]
        triangle = Polygon(*[np.array([x, y, 0]) for x, y in coordinates],
                           color=BLUE, fill_opacity=0.12)
        for dot, label in dots_and_labels:
            self.play(FadeIn(dot), Write(label), run_time=0.25)
        self.play(Create(triangle), run_time=0.7)
        claim = safe_text("关键条件：这三个点不共线", 30, PINK).move_to(DOWN * 2.8)
        self.play(Write(claim), run_time=0.7)
        self.wait(0.8)
        self.clear_lesson()

    def scene_2_plane_concept(self):
        self.heading("平面是什么？", "平行四边形只是平面的局部示意")
        plane = patch([(-3.1, -0.6), (3.1, -0.6), (2.2, 1.7), (-2.2, 1.7)], BLUE)
        alpha = MathTex(r"\alpha", font_size=48, color=BLUE).move_to([2.55, 2.2, 0])
        self.play(Create(plane), Write(alpha), run_time=1.1)
        extension = safe_text("实际平面向四周无限延展，没有图示边界", 26)
        extension.move_to(DOWN * 2.9)
        self.play(FadeIn(extension), run_time=0.7)
        self.wait(0.8)
        self.clear_lesson()

    def scene_3_axiom1(self):
        self.heading("公理 1 · 线在面内", "直线上的两个不同点都属于平面")
        plane = patch([(-3.1, -0.6), (3.1, -0.6), (2.2, 1.7), (-2.2, 1.7)], BLUE)
        line = Line([-2.5, 0.5, 0], [2.5, 0.5, 0], color=YELLOW, stroke_width=4)
        a, la = self.point(-1.2, 0.5, "A", UP)
        b, lb = self.point(1.2, 0.5, "B", UP)
        symbol = MathTex(r"\alpha", font_size=42, color=BLUE).move_to([2.6, 2.2, 0])
        line_label = MathTex("l", font_size=38, color=YELLOW).next_to(line, RIGHT, buff=0.14)
        self.play(Create(plane), Write(symbol), run_time=0.7)
        self.play(Create(line), FadeIn(a), FadeIn(b), Write(la), Write(lb),
                  Write(line_label), run_time=0.9)
        premise = MathTex(r"A\ne B,\quad A,B\in l,\quad A,B\in\alpha",
                          font_size=35).move_to(DOWN * 3.5)
        result = MathTex(r"\Longrightarrow\ l\subset\alpha", font_size=44,
                         color=PINK).move_to(DOWN * 4.7)
        self.play(Write(premise), run_time=0.7)
        self.play(line.animate.set_color(PINK), Write(result), run_time=0.8)
        self.wait(0.9)
        self.clear_lesson()

    def scene_4_axiom2(self):
        self.heading("公理 2 · 三点定面", "必须是不在同一条直线上的三点")
        coordinates = [(-1.5, -0.3), (1.5, -0.3), (0.0, 1.25)]
        dots = [self.point(x, y, name) for (x, y), name in
                zip(coordinates, ("A", "B", "C"))]
        for dot, label in dots:
            self.play(FadeIn(dot), Write(label), run_time=0.35)
        triangle = Polygon(*[np.array([x, y, 0]) for x, y in coordinates],
                           color=PINK, fill_opacity=0.12)
        self.play(Create(triangle), run_time=0.6)
        plane = patch([(-3.0, -1.0), (3.0, -1.0), (2.15, 2.0), (-2.15, 2.0)], BLUE)
        self.play(FadeIn(plane), run_time=0.8)
        alpha = MathTex(r"\alpha", font_size=45, color=BLUE).move_to([2.6, 2.35, 0])
        self.play(Write(alpha), run_time=0.3)
        rule = safe_text("不共线三点，有且只有一个平面经过它们", 26, PINK)
        rule.move_to(DOWN * 3.45)
        counter = safe_text("反例：若三点共线，经过该直线的平面不唯一", 23)
        counter.move_to(DOWN * 4.45)
        self.play(Write(rule), run_time=0.8)
        self.play(FadeIn(counter), run_time=0.6)
        self.wait(1.0)
        self.clear_lesson()

    def scene_5_axiom3(self):
        self.heading("公理 3 · 两平面相交", "前提：两个平面不重合，且有一个公共点")
        # 透视示意：两块局部平面只共享中间的黄色边；黄色边表示无限交线的一段。
        alpha = patch([(-3.0, 0.0), (3.0, 0.0), (2.0, 2.2), (-2.0, 2.2)], BLUE)
        beta = patch([(-3.0, 0.0), (3.0, 0.0), (2.0, -2.2), (-2.0, -2.2)], GREEN)
        alpha_label = MathTex(r"\alpha", font_size=43, color=BLUE).move_to([-2.25, 2.55, 0])
        beta_label = MathTex(r"\beta", font_size=43, color=GREEN).move_to([2.25, -2.55, 0])
        p, p_label = self.point(0.0, 0.0, "P", UP)
        self.play(Create(alpha), Write(alpha_label), run_time=0.75)
        self.play(Create(beta), Write(beta_label), run_time=0.75)
        self.play(FadeIn(p), Write(p_label), run_time=0.5)
        # 未添加额外虚构的“只有一个公共点”状态。
        intersection = Line([-3.0, 0, 0], [3.0, 0, 0], color=YELLOW, stroke_width=4)
        line_label = MathTex("l", font_size=38, color=YELLOW).next_to(intersection, RIGHT, buff=0.13)
        self.play(Create(intersection), Write(line_label), run_time=0.9)
        condition = MathTex(r"\alpha\ne\beta,\quad P\in\alpha\cap\beta",
                            font_size=35).move_to(DOWN * 4.0)
        conclusion = MathTex(r"\alpha\cap\beta=l,\quad P\in l",
                             font_size=39, color=PINK).move_to(DOWN * 5.1)
        self.play(Write(condition), run_time=0.6)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.0)
        self.clear_lesson()

    def scene_6_conditions(self):
        self.heading("确定平面的四种条件", "下列每组条件都能确定唯一平面")
        items = (
            "① 不共线的三个点",
            "② 一条直线和直线外一点",
            "③ 两条相交的直线",
            "④ 两条不同的平行直线",
        )
        colors = (BLUE, GREEN, PINK, YELLOW)
        for index, (item, color) in enumerate(zip(items, colors)):
            row = safe_text(item, 30, color).move_to([0, 3.1 - 1.6 * index, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
        note = safe_text("注意：三点共线、两条重合直线都不能唯一确定平面", 22)
        note.move_to(DOWN * 4.1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.0)
        self.clear_lesson()

    def scene_7_outro(self):
        self.heading("本课小结", "三个公理 · 四种定面条件")
        summary = safe_text("两点定线 · 三点不共线定面", 31, BLUE).move_to(UP * 1.0)
        summary2 = safe_text("两异面有公共点，交集是一条直线", 28, GREEN)
        summary2.move_to(DOWN * 0.4)
        reminder = safe_text("图形只是示意；判断空间关系要核对前提", 24, PINK)
        reminder.move_to(DOWN * 2.2)
        self.play(Write(summary), Write(summary2), run_time=1.1)
        self.play(FadeIn(reminder), run_time=0.6)
        self.wait(1.5)
        self.clear_lesson()
