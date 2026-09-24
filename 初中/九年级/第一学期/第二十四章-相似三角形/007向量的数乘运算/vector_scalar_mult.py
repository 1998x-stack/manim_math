"""九年级上学期：向量的数乘。几何数据与公式来自同一可测试模型。

零向量以 Dot 和数学公式表示，不创建退化的 Arrow；负数演示在新方向
创建新的箭头，不通过从正向箭头插值到反向而隐式生成零长度箭头。
"""

import math

import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BASE = (1.4, 0.7)
ORIGIN = (0.0, 0.8)


def scalar_geometry(vector, scalar, origin=(0.0, 0.8)):
    """计算起点、终点、模长和相对方向；零向量无确定方向。"""
    if (len(vector) != 2 or len(origin) != 2
            or not all(math.isfinite(v) for v in (*vector, *origin, scalar))):
        raise ValueError("数乘需要有限二维向量和实数")
    base_length = math.hypot(*vector)
    if base_length <= 1e-10:
        raise ValueError("方向比较的基准向量不可为零向量")
    start = (float(origin[0]), float(origin[1]))
    end = (start[0] + scalar * vector[0],
           start[1] + scalar * vector[1])
    norm = math.dist(start, end)
    if not all(math.isfinite(x) for x in end) or not math.isfinite(norm):
        raise ValueError("数乘产生不可表示的向量")
    if not math.isclose(norm, abs(scalar) * base_length, rel_tol=1e-10,
                        abs_tol=1e-12):
        raise ValueError("实际箭头长度与模长公式不一致")
    dot = vector[0] * (end[0] - start[0]) + vector[1] * (end[1] - start[1])
    direction = "zero" if scalar == 0 else "same" if scalar > 0 else "opposite"
    if (direction == "same" and dot <= 0
            or direction == "opposite" and dot >= 0
            or direction == "zero" and norm != 0):
        raise ValueError("数乘方向与实际屏幕箭头不一致")
    return dict(start=start, end=end, norm=norm,
                base_norm=base_length, direction=direction)


def distributive_example(a=(2.0, 1.0), b=(1.0, -2.0), factor=2.0):
    """分别求 λ(a+b) 和 λa+λb，返回真实坐标计算结果。"""
    if (len(a) != 2 or len(b) != 2
            or not all(math.isfinite(x) for x in (*a, *b, factor))):
        raise ValueError("分配律只接受有限实二维向量")
    lhs = tuple(factor * (a[i] + b[i]) for i in range(2))
    rhs = tuple(factor * a[i] + factor * b[i] for i in range(2))
    if not all(math.isclose(x, y, abs_tol=1e-12) for x, y in zip(lhs, rhs)):
        raise ValueError("分配律计算不一致")
    return lhs, rhs


def point3(point):
    return np.array((point[0], point[1], 0.0), dtype=float)


class VectorScalarMult(Scene):
    FONT = "PingFang SC"
    PRIMARY = "#e94560"
    SCALED = "#00d4ff"
    ACCENT = "#f5c518"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font=self.FONT, font_size=19,
                                color=GRAY_B).move_to(UP * 7.0)
        self.add(self.author_info)
        for factor in (0.5, 1, 2, -1, -2, 0):
            scalar_geometry(BASE, factor, ORIGIN)
        distributive_example()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_positive_lambda()
        self.scene_4_negative_lambda()
        self.scene_5_zero_lambda()
        self.scene_6_magnitude_formula()
        self.scene_7_laws()
        self.scene_8_outro()

    def clear_section(self, keep_author=True):
        active = [mob for mob in self.mobjects
                  if not keep_author or mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.45)

    def title(self, title, subtitle=None):
        self.play(Write(Text(title, font=self.FONT, font_size=33,
                             color=YELLOW).move_to(UP*5.75)), run_time=0.55)
        if subtitle:
            self.play(FadeIn(Text(subtitle, font=self.FONT, font_size=23,
                                  color=GRAY_A).move_to(UP*4.85)), run_time=0.4)

    def arrow(self, factor, color=None, origin=ORIGIN):
        model = scalar_geometry(BASE, factor, origin)
        if model["direction"] == "zero":
            return Dot(point3(model["start"]), radius=0.11, color=color or self.SCALED)
        return Arrow(point3(model["start"]), point3(model["end"]),
                     buff=0, color=color or self.SCALED, stroke_width=5)

    def draw_reference(self):
        reference = self.arrow(1, color=self.PRIMARY)
        label = MathTex(r"\vec a", font_size=35, color=self.PRIMARY)
        label.next_to(reference.get_end(), UP + RIGHT, buff=0.14)
        self.play(GrowArrow(reference), Write(label), run_time=0.75)
        return reference, label

    def scene_1_opening(self):
        self.title("一个向量乘上不同实数，会怎样变化？")
        self.draw_reference()
        question = MathTex(r"\lambda\vec a=?", font_size=48,
                           color=self.ACCENT).move_to(DOWN*2.3)
        self.play(Write(question), run_time=0.75)
        self.wait(0.6)
        self.clear_section()

    def scene_2_definition(self):
        self.title("定义：数与向量相乘", "数乘同时改变长度，也可能改变方向")
        self.draw_reference()
        double = self.arrow(2)
        label = MathTex(r"2\vec a", font_size=34,
                        color=self.SCALED).next_to(double.get_end(), UP, buff=0.13)
        self.play(GrowArrow(double), Write(label), run_time=0.8)
        formula = MathTex(r"|2\vec a|=2|\vec a|",
                          font_size=39, color=YELLOW).move_to(DOWN*3.15)
        self.play(Write(formula), run_time=0.65)
        self.wait(0.75)
        self.clear_section()

    def scene_3_positive_lambda(self):
        self.title("正数倍：与原向量同向", "比例为 0.5、1、2 时长度依次变化")
        self.draw_reference()
        shown = self.arrow(.5)
        self.play(GrowArrow(shown), run_time=0.65)
        for factor, latex in ((1, r"\lambda=1"), (2, r"\lambda=2"),
                              (.5, r"\lambda=\frac12")):
            changed = self.arrow(factor)
            self.play(Transform(shown, changed), run_time=0.7)
            info = MathTex(latex, font_size=30, color=YELLOW)
            info.move_to(DOWN*2.3)
            self.play(FadeIn(info), run_time=0.3)
            self.wait(0.2)
            self.play(FadeOut(info), run_time=0.25)
        self.play(Write(Text("λ>0：方向不变，模长乘 λ", font=self.FONT,
                             font_size=25).move_to(DOWN*3.8)), run_time=0.6)
        self.wait(0.65)
        self.clear_section()

    def scene_4_negative_lambda(self):
        self.title("负数倍：与原向量反向", "不经过零长度箭头的退化变换")
        self.draw_reference()
        negative = self.arrow(-1)
        self.play(GrowArrow(negative), run_time=0.65)
        first = MathTex(r"-\vec a", color=self.SCALED,
                        font_size=34).next_to(negative.get_end(), LEFT, buff=0.1)
        self.play(Write(first), run_time=0.4)
        twice = self.arrow(-2)
        self.play(Transform(negative, twice), run_time=0.9)
        after = MathTex(r"-2\vec a", color=YELLOW,
                        font_size=36).next_to(negative.get_end(), LEFT, buff=0.1)
        self.play(ReplacementTransform(first, after), run_time=0.5)
        formula = MathTex(r"|-2\vec a|=2|\vec a|",
                          color=YELLOW, font_size=38).move_to(DOWN*3.45)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.7)
        self.clear_section()

    def scene_5_zero_lambda(self):
        self.title("λ=0：零向量没有确定的方向")
        base, label = self.draw_reference()
        zero = self.arrow(0)
        self.play(FadeOut(base), FadeOut(label), FadeIn(zero), run_time=0.8)
        formula = MathTex(r"0\vec a=\vec 0,\quad|\vec 0|=0",
                          font_size=40, color=YELLOW).move_to(DOWN*2.5)
        self.play(Write(formula), run_time=0.7)
        self.wait(0.8)
        self.clear_section()

    def scene_6_magnitude_formula(self):
        self.title("模长公式：注意数乘的绝对值")
        formula = MathTex(r"|\lambda\vec a|=|\lambda|\cdot|\vec a|",
                          font_size=39, color=YELLOW).move_to(UP*3.0)
        self.play(Write(formula), run_time=0.8)
        self.draw_reference()
        samples = VGroup(
            MathTex(r"|2\vec a|=2|\vec a|", font_size=30),
            MathTex(r"|-2\vec a|=2|\vec a|", font_size=30),
            MathTex(r"|0\vec a|=0", font_size=30),
        ).arrange(DOWN, buff=0.55).move_to(DOWN*3.0)
        self.play(*[Write(m) for m in samples], run_time=1)
        self.wait(0.75)
        self.clear_section()

    def scene_7_laws(self):
        self.title("数乘的分配律与结合律")
        lhs, rhs = distributive_example()
        if lhs != rhs or lhs != (6.0, -2.0):
            raise ValueError("分配律例题与实际数据不符")
        lines = VGroup(
            MathTex(r"\lambda(\vec a+\vec b)=\lambda\vec a+\lambda\vec b",
                    font_size=29),
            MathTex(r"(\lambda+\mu)\vec a=\lambda\vec a+\mu\vec a",
                    font_size=29),
            MathTex(r"(\lambda\mu)\vec a=\lambda(\mu\vec a)",
                    font_size=30),
            MathTex(r"2[(2,1)+(1,-2)]=(6,-2)",
                    font_size=31, color=YELLOW),
        ).arrange(DOWN, buff=0.62).move_to(UP*0.3)
        self.play(*[Write(line) for line in lines], run_time=1.2)
        self.wait(0.85)
        self.clear_section()

    def scene_8_outro(self):
        self.title("数乘三要点")
        notes = VGroup(
            Text("正数倍同向，负数倍反向", font=self.FONT, font_size=26),
            Text("零向量没有确定方向", font=self.FONT, font_size=26),
            Text("模长乘数的绝对值", font=self.FONT, font_size=26),
        ).arrange(DOWN, buff=0.8).move_to(UP*.4)
        self.play(*[FadeIn(note) for note in notes], run_time=0.85)
        self.wait(0.75)
        self.clear_section(keep_author=False)


# manim -ql vector_scalar_mult.py VectorScalarMult
