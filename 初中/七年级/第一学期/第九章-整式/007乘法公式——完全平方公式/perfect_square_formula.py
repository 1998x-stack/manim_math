"""完全平方公式：正边长几何图配合对任意实数成立的代数证明。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
RED_AREA = "#e74c3c"
GREEN_AREA = "#2ecc71"
BLUE_AREA = "#3498db"
SAFE_WIDTH = 7.4


def square_regions(a, b):
    """与场景相同的四区域数学数据；正方形画法要求 a,b 均为有限正数。"""
    import math
    try:
        valid = math.isfinite(a) and math.isfinite(b) and a > 0 and b > 0
    except (TypeError, ValueError):
        valid = False
    if not valid:
        raise ValueError("面积拆分需要有限的正边长 a、b")
    side = a + b
    left = -side / 2
    bottom = -side / 2
    x_split = left + a
    y_split = bottom + b
    cells = (
        {"name": "a2", "x0": left, "y0": y_split, "width": a, "height": a, "area": a*a},
        {"name": "ab_top", "x0": x_split, "y0": y_split, "width": b, "height": a, "area": a*b},
        {"name": "ab_bottom", "x0": left, "y0": bottom, "width": a, "height": b, "area": a*b},
        {"name": "b2", "x0": x_split, "y0": bottom, "width": b, "height": b, "area": b*b},
    )
    if not math.isclose(sum(cell["area"] for cell in cells), side*side,
                        rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError("四块面积总和不等于大正方形面积")
    return {"a": a, "b": b, "side": side, "left": left, "bottom": bottom,
            "x_split": x_split, "y_split": y_split, "cells": cells}


class PerfectSquareFormula(Scene):
    """七镜头：两条完全平方恒等式与和的平方四分块。"""

    def fit(self, mob, width=SAFE_WIDTH):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, text):
        return self.fit(Text(text, font_size=38, color=YELLOW)).move_to(UP * 5.5)

    def formula(self, latex, y, color=WHITE, size=42):
        return self.fit(MathTex(latex, font_size=size, color=color)).move_to(UP * y)

    def caption(self, text, y, color=GRAY_A):
        return self.fit(Text(text, font_size=25, color=color)).move_to(UP * y)

    def clear_content(self):
        current = [mob for mob in tuple(self.mobjects) if mob is not self.author_info]
        if current:
            self.play(*[FadeOut(mob) for mob in current], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.spec = square_regions(2.2, 1.1)
        self.square_center = DOWN * 0.6
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_info)
        self.show_opening()
        self.show_formula_introduction()
        self.show_geometric_construction()
        self.show_geometric_division()
        self.show_area_coloring()
        self.show_formula_derivation()
        self.show_example_and_outro()

    def show_opening(self):
        title = self.heading("(a+b) 的平方，为什么不是 a²+b²？")
        question = self.formula(r"(a+b)^2=\,?", 2.2, BLUE_AREA, 52)
        hint = self.caption("看清楚中间项：它来自两个长方形", -0.2, YELLOW)
        self.play(Write(title), Write(question), run_time=1)
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(0.9)
        self.clear_content()

    def show_formula_introduction(self):
        title = self.heading("先用乘法展开，注意符号")
        plus = self.formula(r"(a+b)^2=a^2+2ab+b^2", 3.5, GREEN_AREA, 42)
        minus = self.formula(r"(a-b)^2=a^2-2ab+b^2", 1.6, BLUE_AREA, 42)
        proof_plus = self.formula(r"(a+b)(a+b)=a^2+ab+ab+b^2", -0.75, WHITE, 34)
        proof_minus = self.formula(r"(a-b)(a-b)=a^2-ab-ab+b^2", -2.45, WHITE, 34)
        note = self.caption("中间项有两个；减法平方的常数项仍为正", -4.7, YELLOW)
        self.play(Write(title), run_time=0.65)
        for item in (plus, minus, proof_plus, proof_minus):
            self.play(Write(item), run_time=0.65)
        self.play(FadeIn(note), run_time=0.55)
        self.wait(1.1)
        self.clear_content()

    def show_geometric_construction(self):
        title = self.heading("边长 a+b 的大正方形")
        self.big_square = Square(side_length=self.spec["side"],
                                 color=WHITE, stroke_width=3).move_to(self.square_center)
        self.big_side_label = MathTex(r"a+b", font_size=36, color=YELLOW).next_to(
            self.big_square, UP, buff=0.18
        )
        area = self.formula(r"S=(a+b)^2", -4.65, YELLOW, 39)
        self.play(Write(title), Create(self.big_square), run_time=0.9)
        self.play(Write(self.big_side_label), Write(area), run_time=0.75)
        self.wait(1)
        self.play(FadeOut(title), FadeOut(area), run_time=0.35)

    def show_geometric_division(self):
        title = self.heading("把两条边分别分成 a 和 b")
        spec = self.spec
        self.vertical_split = DashedLine(
            self.square_center + RIGHT * spec["x_split"] + UP * spec["bottom"],
            self.square_center + RIGHT * spec["x_split"] - UP * spec["bottom"],
            color=GRAY_A,
        )
        self.horizontal_split = DashedLine(
            self.square_center + RIGHT * spec["left"] + UP * spec["y_split"],
            self.square_center - RIGHT * spec["left"] + UP * spec["y_split"],
            color=GRAY_A,
        )
        # a+b 总边长在上方；a、b 两段标注放在底边下方，避免叠字。
        a_width = MathTex("a", font_size=31, color=RED_AREA).move_to(
            self.square_center + RIGHT * (spec["left"]+spec["a"]/2)
            + UP * (spec["bottom"]-0.45)
        )
        b_width = MathTex("b", font_size=31, color=BLUE_AREA).move_to(
            self.square_center + RIGHT * (spec["x_split"]+spec["b"]/2)
            + UP * (spec["bottom"]-0.45)
        )
        self.play(Write(title), Create(self.vertical_split),
                  Create(self.horizontal_split), run_time=1)
        self.play(Write(a_width), Write(b_width), run_time=0.65)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(a_width), FadeOut(b_width), run_time=0.35)

    def show_area_coloring(self):
        title = self.heading("四块面积：a²、ab、ab、b²")
        colors = (RED_AREA, GREEN_AREA, GREEN_AREA, BLUE_AREA)
        tex_labels = (r"a^2", r"ab", r"ab", r"b^2")
        self.region_objects = VGroup()
        self.region_labels = VGroup()
        self.play(Write(title), run_time=0.65)
        for cell, color, tex in zip(self.spec["cells"], colors, tex_labels):
            rectangle = Rectangle(width=cell["width"], height=cell["height"],
                                  color=color, stroke_width=1.5, fill_color=color,
                                  fill_opacity=0.5)
            rectangle.move_to(self.square_center
                              + RIGHT * (cell["x0"] + cell["width"] / 2)
                              + UP * (cell["y0"] + cell["height"] / 2))
            area_label = MathTex(tex, font_size=37, color=WHITE).move_to(rectangle)
            self.region_objects.add(rectangle)
            self.region_labels.add(area_label)
            self.play(FadeIn(rectangle), Write(area_label), run_time=0.55)
        note = self.caption("两个 ab 分别来自两个不同的长方形", -4.6, YELLOW)
        self.play(FadeIn(note), run_time=0.55)
        self.wait(1.1)
        self.play(FadeOut(title), FadeOut(note), run_time=0.4)

    def show_formula_derivation(self):
        title = self.heading("面积相加：中间项要算两次")
        first = self.formula(r"(a+b)^2=a^2+ab+ab+b^2", -4.15, WHITE, 37)
        result = self.formula(r"=a^2+2ab+b^2", -5.4, YELLOW, 40)
        self.play(Write(title), Write(first), run_time=0.9)
        self.play(Write(result), run_time=0.8)
        self.wait(1.2)
        self.clear_content()

    def show_example_and_outro(self):
        title = self.heading("应用时，别漏掉两倍乘积")
        example_plus = self.formula(r"(x+3)^2=x^2+6x+9", 3.35, GREEN_AREA, 41)
        example_minus = self.formula(r"(x-3)^2=x^2-6x+9", 1.35, BLUE_AREA, 41)
        reminder = self.caption("几何面积图取 a>0、b>0；代数公式对任意实数成立", -1.45, YELLOW)
        self.play(Write(title), Write(example_plus), run_time=0.9)
        self.play(Write(example_minus), FadeIn(reminder), run_time=0.9)
        self.wait(1.3)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.7)
