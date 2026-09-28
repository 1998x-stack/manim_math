"""九年级上学期：30°、45°、60° 特殊角三角比。

统一的正交三角形模型同时决定角顶点、对边、邻边、斜边、画出的线段和公式。
不以一个公式正确代替实际标注正确；数学前提验证不通过则停止生成画面。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


VALUES = {
    30: (0.5, math.sqrt(3) / 2, 1 / math.sqrt(3)),
    45: (math.sqrt(2) / 2, math.sqrt(2) / 2, 1.0),
    60: (math.sqrt(3) / 2, 0.5, math.sqrt(3)),
}

LATEX_VALUES = {
    30: (r"\frac12", r"\frac{\sqrt3}{2}", r"\frac{\sqrt3}{3}"),
    45: (r"\frac{\sqrt2}{2}", r"\frac{\sqrt2}{2}", "1"),
    60: (r"\frac{\sqrt3}{2}", r"\frac12", r"\sqrt3"),
}


def interior_angle(first, vertex, last):
    """实际两条射线所成内角，单位为度。"""
    u = tuple(first[i] - vertex[i] for i in range(2))
    v = tuple(last[i] - vertex[i] for i in range(2))
    lu, lv = math.hypot(*u), math.hypot(*v)
    if min(lu, lv) <= 1e-12:
        raise ValueError("角的两条射线不能退化")
    cosine = max(-1.0, min(1.0, (u[0] * v[0] + u[1] * v[1]) / (lu * lv)))
    return math.degrees(math.acos(cosine))


def special_angle_model(degrees):
    """返回实际顶点、三条对应边、实际长度和 sin/cos/tan。"""
    if degrees not in VALUES:
        raise ValueError("本课只使用 30°、45° 和 60°")
    if degrees == 45:
        points = {"P": (0.0, 0.0), "Q": (math.sqrt(2), 0.0),
                  "R": (0.0, math.sqrt(2))}
        vertex, right = "Q", "P"
        opposite, adjacent, hypotenuse = ("P", "R"), ("P", "Q"), ("Q", "R")
        angle_arms, right_arms = ("P", "R"), ("Q", "R")
    else:
        points = {"A": (-1.0, 0.0), "B": (1.0, 0.0),
                  "C": (0.0, math.sqrt(3)), "D": (0.0, 0.0)}
        right, right_arms = "D", ("A", "C")
        hypotenuse = ("A", "C")
        if degrees == 30:
            vertex, angle_arms = "C", ("A", "D")
            opposite, adjacent = ("A", "D"), ("C", "D")
        else:
            vertex, angle_arms = "A", ("C", "D")
            opposite, adjacent = ("C", "D"), ("A", "D")
    angle = interior_angle(points[angle_arms[0]], points[vertex],
                           points[angle_arms[1]])
    right_angle = interior_angle(points[right_arms[0]], points[right],
                                 points[right_arms[1]])
    sides = tuple(math.dist(points[u], points[v])
                  for u, v in (opposite, adjacent, hypotenuse))
    if not math.isclose(angle, degrees, abs_tol=1e-10):
        raise ValueError("屏幕角标记与设定特殊角不一致")
    if not math.isclose(right_angle, 90, abs_tol=1e-10):
        raise ValueError("图形未构成直角三角形")
    if any(length <= 0 for length in sides):
        raise ValueError("三角形不能包含零长度边")
    if not math.isclose(sides[0] ** 2 + sides[1] ** 2,
                        sides[2] ** 2, rel_tol=1e-11):
        raise ValueError("对应边未满足勾股定理")
    ratios = (sides[0] / sides[2], sides[1] / sides[2], sides[0] / sides[1])
    expected = VALUES[degrees]
    if not all(math.isclose(value, target, rel_tol=1e-11)
               for value, target in zip(ratios, expected)):
        raise ValueError("图形中的对边、邻边与三角比表格不一致")
    radians = math.radians(degrees)
    if not all(math.isclose(value, target, rel_tol=1e-11)
               for value, target in zip(ratios,
                                        (math.sin(radians), math.cos(radians),
                                         math.tan(radians)))):
        raise ValueError("三角比数值未通过解析值验证")
    return dict(points=points, vertex=vertex, right=right,
                opposite=opposite, adjacent=adjacent, hypotenuse=hypotenuse,
                angle_arms=angle_arms, right_arms=right_arms,
                sides=sides, ratios=ratios)


def point3(point, offset=(0.0, 1.15)):
    return np.array((point[0] + offset[0], point[1] + offset[1], 0.0), dtype=float)


class SpecialAngleTrigonometry(Scene):
    FONT = "PingFang SC"
    COLOR_30 = "#e74c3c"
    COLOR_45 = "#2ecc71"
    COLOR_60 = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP * 7.0)
        self.add(self.author_info)
        self.models = {degrees: special_angle_model(degrees)
                       for degrees in (30, 45, 60)}
        self.show_opening()
        self.show_30_degree_construction()
        self.show_30_degree_calculation()
        self.show_45_degree_construction()
        self.show_45_degree_calculation()
        self.show_60_degree_construction()
        self.show_60_degree_calculation()
        self.show_summary_table()
        self.show_outro()

    def clear_section(self, keep_author=True):
        visible = [mob for mob in self.mobjects
                   if not keep_author or mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def heading(self, text, subtitle=None):
        heading = Text(text, font=self.FONT, font_size=33,
                       color=YELLOW).move_to(UP * 5.65)
        self.play(Write(heading), run_time=0.55)
        if subtitle:
            note = Text(subtitle, font=self.FONT, font_size=23,
                        color=GRAY_A).move_to(UP * 4.8)
            self.play(FadeIn(note), run_time=0.35)

    def draw_triangle(self, degrees):
        model = self.models[degrees]
        points = {key: point3(value) for key, value in model["points"].items()}
        if degrees == 45:
            polygon = Polygon(*(points[key] for key in "PQR"),
                              color=self.COLOR_45, stroke_width=4)
            right_mark = Square(side_length=0.17, color=YELLOW,
                                stroke_width=2).move_to(points["P"] +
                                                        RIGHT * 0.085 + UP * 0.085)
            label_direction = {"P": DOWN + LEFT, "Q": RIGHT, "R": UP}
        else:
            polygon = Polygon(*(points[key] for key in "ABC"),
                              color=self.COLOR_30 if degrees == 30 else self.COLOR_60,
                              stroke_width=4)
            altitude = DashedLine(points["C"], points["D"],
                                  color=GRAY_B, dash_length=0.13)
            self.play(Create(altitude), run_time=0.45)
            right_mark = Square(side_length=0.17, color=YELLOW,
                                stroke_width=2).move_to(points["D"] +
                                                        LEFT * 0.085 + UP * 0.085)
            label_direction = {"A": LEFT, "B": RIGHT,
                               "C": UP, "D": DOWN}
        labels = VGroup(*[
            MathTex(key, font_size=27).next_to(points[key], direction, buff=0.12)
            for key, direction in label_direction.items()
        ])
        vertex = model["vertex"]
        arm1, arm2 = model["angle_arms"]
        mark = Angle.from_three_points(points[arm1], points[vertex], points[arm2],
                                       radius=0.36, color=YELLOW)
        color = {30: self.COLOR_30, 45: self.COLOR_45, 60: self.COLOR_60}[degrees]
        angle_label = MathTex(rf"{degrees}^{{\circ}}", font_size=25,
                              color=color).next_to(points[vertex],
                                                  LEFT + DOWN if degrees == 30 else UP,
                                                  buff=0.35)
        self.play(Create(polygon), FadeIn(right_mark), Write(labels),
                  run_time=0.9)
        self.play(Create(mark), Write(angle_label), run_time=0.65)
        # 几何对象的真实长度与数学式 1、sqrt3、2（或 sqrt2、sqrt2、2）一致。
        side_labels = {
            30: (("A", "D", "1", DOWN), ("C", "D", r"\sqrt3", RIGHT),
                 ("A", "C", "2", LEFT)),
            45: (("P", "Q", r"\sqrt2", DOWN), ("P", "R", r"\sqrt2", LEFT),
                 ("Q", "R", "2", RIGHT)),
            60: (("A", "D", "1", DOWN), ("C", "D", r"\sqrt3", RIGHT),
                 ("A", "C", "2", LEFT)),
        }[degrees]
        lengths = VGroup(*[
            MathTex(tex, font_size=29, color=YELLOW)
            .next_to((points[u] + points[v]) / 2, direction, buff=0.16)
            for u, v, tex, direction in side_labels
        ])
        self.play(Write(lengths), run_time=0.7)
        return points

    def show_opening(self):
        self.heading("特殊角三角比：30°、45°、60°")
        text = Text("从直角三角形的边长推导，不靠死记硬背",
                    font=self.FONT, font_size=29, color=WHITE).move_to(UP * 1)
        self.play(Write(text), run_time=0.8)
        self.wait(0.55)
        self.clear_section()

    def show_30_degree_construction(self):
        self.heading("30°：等边三角形的一半", "角在 C，D 为底边中点和垂足")
        self.draw_triangle(30)
        self.wait(0.8)
        self.clear_section()

    def show_45_degree_construction(self):
        self.heading("45°：等腰直角三角形", "P 为直角，Q 为目标锐角")
        self.draw_triangle(45)
        self.wait(0.8)
        self.clear_section()

    def show_60_degree_construction(self):
        self.heading("60°：与 30° 互余", "角在 A，对边和邻边与 30° 互换")
        self.draw_triangle(60)
        self.wait(0.8)
        self.clear_section()

    def show_calculation(self, degrees):
        model = self.models[degrees]
        self.heading(f"{degrees}° 的三角比值", "红色标记对应角的对边、邻边及斜边")
        points = self.draw_triangle(degrees)
        vertex = model["vertex"]
        if vertex not in points:
            raise ValueError("角标记与显示顶点不一致")
        symbols = {30: (("AD", "AC", "CD")),
                   45: (("PR", "QR", "PQ")),
                   60: (("CD", "AC", "AD"))}[degrees]
        opposite_name, hyp_name, adjacent_name = symbols
        if (set(opposite_name) != set(model["opposite"])
                or set(hyp_name) != set(model["hypotenuse"])
                or set(adjacent_name) != set(model["adjacent"])):
            raise ValueError("公式中的边名与实际锐角所对的边不一致")
        texts = (
            rf"\sin {degrees}^\circ=\frac{{{opposite_name}}}{{{hyp_name}}}={LATEX_VALUES[degrees][0]}",
            rf"\cos {degrees}^\circ=\frac{{{adjacent_name}}}{{{hyp_name}}}={LATEX_VALUES[degrees][1]}",
            rf"\tan {degrees}^\circ=\frac{{{opposite_name}}}{{{adjacent_name}}}={LATEX_VALUES[degrees][2]}",
        )
        for index, (formula, edges) in enumerate(zip(
                texts, ((model["opposite"], model["hypotenuse"]),
                        (model["adjacent"], model["hypotenuse"]),
                        (model["opposite"], model["adjacent"])))):
            for start, end in edges:
                highlighted = Line(points[start], points[end],
                                   color=YELLOW, stroke_width=7)
                self.play(ShowPassingFlash(highlighted), run_time=0.35)
            line = MathTex(formula, font_size=33,
                           color=WHITE).move_to(DOWN * (3.15 + index * 1.04))
            self.play(Write(line), run_time=0.65)
        self.wait(0.85)
        self.clear_section()

    def show_30_degree_calculation(self):
        self.show_calculation(30)

    def show_45_degree_calculation(self):
        self.show_calculation(45)

    def show_60_degree_calculation(self):
        self.show_calculation(60)

    def show_summary_table(self):
        self.heading("特殊角三角比值汇总")
        rows = [[r"30^\circ", *LATEX_VALUES[30]],
                [r"45^\circ", *LATEX_VALUES[45]],
                [r"60^\circ", *LATEX_VALUES[60]]]
        table = MathTable(rows, col_labels=[
            MathTex(r"\theta"), MathTex(r"\sin\theta"),
            MathTex(r"\cos\theta"), MathTex(r"\tan\theta")],
            include_outer_lines=True, h_buff=0.36, v_buff=0.36,
            element_to_mobject=lambda entry: MathTex(entry, font_size=31),
        ).scale(0.74).move_to(UP * 0.7)
        self.play(Create(table), run_time=1.0)
        identity = MathTex(r"\sin30^\circ=\cos60^\circ=\frac12",
                           font_size=32, color=YELLOW).move_to(DOWN * 3.0)
        complement = MathTex(r"\sin45^\circ=\cos45^\circ=\frac{\sqrt2}{2}",
                             font_size=29, color=YELLOW).move_to(DOWN * 4.15)
        self.play(Write(identity), Write(complement), run_time=0.8)
        self.wait(1.0)
        self.clear_section()

    def show_outro(self):
        text = Text("角与边一一对应，先找直角，再算三角比",
                    font=self.FONT, font_size=28,
                    color=YELLOW).move_to(UP * 0.6)
        self.play(Write(text), run_time=0.75)
        self.wait(0.7)
        self.clear_section(keep_author=False)


# manim -ql special_angle_trigonometry.py SpecialAngleTrigonometry
