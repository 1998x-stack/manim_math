"""九年级上学期：比例线段（Manim Community Edition）。

所有长度为正；线段长度与展示的比例由同一组数值生成。
"""

from manim import *
import math
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def valid_proportion(a, b, c, d, *, tol=1e-10):
    """判断四条正长度线段是否满足 a/b=c/d，不进行零分母运算。"""
    values = (a, b, c, d)
    if not all(math.isfinite(value) and value > 0 for value in values):
        return False
    return math.isclose(a * d, b * c, rel_tol=tol, abs_tol=tol)


def proportional_mean(a, c):
    """两条正长度线段的唯一正比例中项。"""
    if not all(math.isfinite(value) and value > 0 for value in (a, c)):
        raise ValueError("比例中项要求两条线段的长度都为正")
    return math.sqrt(a * c)


class ProportionalSegments(Scene):
    """比例定义、内外项、比例中项、合比与等比性质。"""

    FONT = "PingFang SC"
    BG = "#1a1a2e"
    COLORS = ("#e74c3c", "#3498db", "#2ecc71", "#f39c12")

    def construct(self):
        self.camera.background_color = self.BG
        self.setup_geometry()
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=19, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info), run_time=0.4)
        self.scene_1_opening()
        self.scene_2_proportion_definition()
        self.scene_3_inner_outer()
        self.scene_4_geometric_mean()
        self.scene_5_properties()
        self.scene_6_outro()

    def setup_geometry(self):
        self.lengths = (2.0, 3.0, 4.0, 6.0)
        a, b, c, d = self.lengths
        assert valid_proportion(a, b, c, d)
        self.mean_lengths = (2.0, proportional_mean(2.0, 8.0), 8.0)
        assert valid_proportion(
            self.mean_lengths[0], self.mean_lengths[1],
            self.mean_lengths[1], self.mean_lengths[2],
        )

    def heading(self, title, subtitle=None):
        head = Text(title, font=self.FONT, font_size=32, color=YELLOW)
        if head.width > 7.6:
            head.scale_to_fit_width(7.6)
        head.move_to(UP * 5.65)
        self.play(Write(head), run_time=0.55)
        if subtitle is not None:
            sub = Text(subtitle, font=self.FONT, font_size=23, color=GRAY_A)
            sub.move_to(UP * 4.8)
            self.play(FadeIn(sub), run_time=0.35)
        return head

    def clear_section(self):
        """只淡出当前实际在场对象，保留片尾使用的作者信息。"""
        to_remove = [obj for obj in self.mobjects if obj is not self.author_info]
        if to_remove:
            self.play(*[FadeOut(obj) for obj in to_remove], run_time=0.45)

    def segment_row(self, label, length, color, y, unit=0.72):
        start = np.array([-2.9, y, 0.0])
        line = Line(start, start + RIGHT * length * unit,
                    color=color, stroke_width=6)
        name = MathTex(label, font_size=29, color=color).next_to(
            line, LEFT, buff=0.35,
        )
        length_text = Text(f"{length:g}", font=self.FONT, font_size=24)
        length_text.next_to(line, RIGHT, buff=0.25)
        return VGroup(line, name, length_text)

    def scene_1_opening(self):
        self.heading("四条线段有什么关系？")
        rows = VGroup(*[
            self.segment_row(name, length, color, 2.6 - 1.25 * idx)
            for idx, (name, length, color) in enumerate(
                zip("abcd", self.lengths, self.COLORS)
            )
        ])
        for row in rows:
            self.play(Create(row[0]), FadeIn(row[1:]), run_time=0.4)
        self.wait(0.65)
        self.clear_section()

    def scene_2_proportion_definition(self):
        self.heading("比例线段", "四条线段的长度单位相同")
        rows = VGroup(*[
            self.segment_row(name, length, color, 2.5 - 1.16 * idx)
            for idx, (name, length, color) in enumerate(
                zip("abcd", self.lengths, self.COLORS)
            )
        ])
        for row in rows:
            self.play(Create(row[0]), FadeIn(row[1:]), run_time=0.32)
        a, b, c, d = self.lengths
        ratio = MathTex(
            rf"\frac{{a}}{{b}}=\frac{{{a:g}}}{{{b:g}}}"
            rf"=\frac{{{c:g}}}{{{d:g}}}=\frac{{c}}{{d}}",
            font_size=34, color=YELLOW,
        ).move_to(DOWN * 3.25)
        conclusion = Text("两组对应线段的比相等", font=self.FONT,
                          font_size=25).move_to(DOWN * 4.55)
        definition = MathTex(r"\frac{a}{b}=\frac{c}{d}\quad (b>0,\ d>0)",
                             font_size=32).move_to(DOWN * 5.55)
        self.play(Write(ratio), run_time=0.85)
        self.play(FadeIn(conclusion), Write(definition), run_time=0.85)
        self.wait(0.8)
        self.clear_section()

    def scene_3_inner_outer(self):
        self.heading("内项与外项")
        terms = MathTex("a", ":", "b", "=", "c", ":", "d",
                        font_size=54).move_to(UP * 2.6)
        for idx, color in zip((0, 2, 4, 6), self.COLORS):
            terms[idx].set_color(color)
        self.play(Write(terms), run_time=0.75)
        outer = Text("a、d 为外项", font=self.FONT, font_size=26,
                     color=YELLOW).move_to(UP * 1.1)
        self.play(Indicate(terms[0]), Indicate(terms[6]),
                  FadeIn(outer), run_time=0.65)
        self.play(FadeOut(outer), run_time=0.3)
        inner = Text("b、c 为内项", font=self.FONT, font_size=26,
                     color=YELLOW).move_to(UP * 1.1)
        self.play(Indicate(terms[2]), Indicate(terms[4]),
                  FadeIn(inner), run_time=0.65)
        basic = MathTex(r"ad=bc", font_size=46,
                        color=YELLOW).move_to(DOWN * 1.3)
        example = MathTex(r"2\times 6=3\times 4=12",
                          font_size=35).move_to(DOWN * 2.7)
        condition = Text("分母不为零时，可由比例式交叉相乘", font=self.FONT,
                         font_size=23).move_to(DOWN * 4.1)
        self.play(Write(basic), Write(example), run_time=0.85)
        self.play(FadeIn(condition), run_time=0.35)
        self.wait(0.75)
        self.clear_section()

    def scene_4_geometric_mean(self):
        self.heading("比例中项", "三条正长度线段：2、4、8")
        a, b, c = self.mean_lengths
        rows = VGroup(*[
            self.segment_row(name, length, color, 2.75 - idx * 1.35, unit=0.62)
            for idx, (name, length, color) in enumerate(
                zip("abc", self.mean_lengths, self.COLORS)
            )
        ])
        for row in rows:
            self.play(Create(row[0]), FadeIn(row[1:]), run_time=0.4)
        relation = MathTex(r"\frac{a}{b}=\frac{b}{c}\ \Longrightarrow\ b^2=ac",
                           font_size=34, color=YELLOW).move_to(DOWN * 2.65)
        value = MathTex(rf"{b:g}^2={a:g}\times {c:g}=16",
                        font_size=34).move_to(DOWN * 3.9)
        note = Text("b 是 a 与 c 的正比例中项", font=self.FONT,
                    font_size=25).move_to(DOWN * 5.15)
        self.play(Write(relation), run_time=0.8)
        self.play(Write(value), FadeIn(note), run_time=0.7)
        self.wait(0.85)
        self.clear_section()

    def scene_5_properties(self):
        self.heading("比例的性质", "这里的 a、b、c、d 均表示正长度")
        given = MathTex(r"\frac{a}{b}=\frac{c}{d}\qquad b,d>0",
                        font_size=34).move_to(UP * 3.0)
        self.play(Write(given), run_time=0.7)
        first_name = Text("合比性质", font=self.FONT, font_size=26,
                          color=YELLOW).move_to(UP * 1.6)
        first = MathTex(r"\frac{a+b}{b}=\frac{c+d}{d}",
                        font_size=36).move_to(UP * 0.65)
        self.play(FadeIn(first_name), Write(first), run_time=0.8)
        second_name = Text("等比性质", font=self.FONT, font_size=26,
                           color=YELLOW).move_to(DOWN * 1.2)
        second = MathTex(r"\frac{a}{b}=\frac{c}{d}=\frac{a+c}{b+d}",
                         font_size=34).move_to(DOWN * 2.15)
        note = Text("b+d>0，合并后的分母仍不为零", font=self.FONT,
                    font_size=23).move_to(DOWN * 3.6)
        self.play(FadeIn(second_name), Write(second), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.8)
        self.clear_section()

    def scene_6_outro(self):
        self.heading("核心要点")
        notes = VGroup(
            MathTex(r"\frac{a}{b}=\frac{c}{d}", font_size=43),
            MathTex(r"ad=bc", font_size=43),
            MathTex(r"b^2=ac", font_size=43),
        ).arrange(DOWN, buff=0.85).move_to(UP * 0.6)
        caption = Text("比例中项：三条正长度线段", font=self.FONT,
                       font_size=24).move_to(DOWN * 3.35)
        self.play(*[Write(line) for line in notes], run_time=1.1)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(1.15)
        self.clear_section()
        self.play(FadeOut(self.author_info), run_time=0.45)
