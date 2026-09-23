"""频率分布与统计图表：表、直方图、折线、累计频率与茎叶同源可验。

预览：manim -pql freq_dist_animation.py FreqDistAnimation
回归：python -m unittest -v test_frequency_distribution_math.py
"""
from fractions import Fraction
from manim import *
from frequency_distribution_math import (EDGES, SCORES, STEM_SUBSET, distribution,
    frequency_polygon_area, histogram_area, stem_leaf)

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
CARD = "#16213e"
BLUE = "#56a5e8"
RED = "#ef6b68"
GOLD = "#f1c40f"
GREEN = "#58d68d"
PURPLE = "#bb8fce"


class FreqDistAnimation(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.counts, self.frequencies, self.density, self.cumulative = distribution()
        self.s0_opening()
        self.s1_freq_table()
        self.s2_histogram()
        self.s3_polygon()
        self.s4_cumulative()
        self.s5_stem_leaf()
        self.s6_summary()
        self.s7_outro()

    def fit(self, mob):
        """单元素安全区限制；遮挡、字体与过渡仍需实渲染逐帧核查。"""
        if mob.width > 7.8:
            mob.scale_to_fit_width(7.8)
        if mob.height > 13.4:
            mob.scale_to_fit_height(13.4)
        if mob.get_left()[0] < -3.9:
            mob.shift(RIGHT * (-3.9 - mob.get_left()[0]))
        if mob.get_right()[0] > 3.9:
            mob.shift(LEFT * (mob.get_right()[0] - 3.9))
        if mob.get_top()[1] > 6.8:
            mob.shift(DOWN * (mob.get_top()[1] - 6.8))
        if mob.get_bottom()[1] < -6.8:
            mob.shift(UP * (-6.8 - mob.get_bottom()[1]))
        return mob

    def text(self, message, y, size=26, color=WHITE):
        return self.fit(Text(message, font=FONT, font_size=size, color=color).move_to(UP * y))

    def math(self, formula, y, size=32, color=WHITE):
        """仅绘制纯 LaTeX；中文标注由 text 完成。"""
        return self.fit(MathTex(formula, font_size=size, color=color).move_to(UP * y))

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.35, 37, color), 0.4)

    def axes(self, cumulative=False):
        upper = 1.05 if cumulative else 0.045
        step = 0.25 if cumulative else 0.01
        return Axes(
            x_range=[50, 100, 10], y_range=[0, upper, step],
            x_length=6.25, y_length=4.0,
            axis_config={"color": GRAY_B, "include_tip": False},
        ).move_to(UP * 0.65)

    def histogram_bars(self, ax):
        bars = VGroup()
        for left, right, density in zip(EDGES, EDGES[1:], self.density):
            lower = ax.c2p(left, 0)
            upper = ax.c2p(right, float(density))
            bar = Rectangle(
                width=upper[0] - lower[0], height=upper[1] - lower[1],
                stroke_color=WHITE, stroke_width=1,
                fill_color=BLUE, fill_opacity=0.65,
            ).move_to((lower + upper) / 2)
            bars.add(bar)
        return bars

    def s0_opening(self):
        self.page("频率分布与统计图表")
        self.show(self.text("40份教学示例成绩，如何看出分布？", 3.65, 28))
        self.show(self.text("成绩按 50～100 分区间分为五组", 2.35, 27, BLUE))
        self.show(self.math(r"n=40", 0.35, 47, GOLD))
        self.show(self.text("同一批40个数，生成表格、直方图和累计图", -1.6, 24))
        self.show(self.text("另取其中12个成绩演示保留原始值的茎叶图", -3.0, 22, GREEN))
        self.wait(0.8)

    def s1_freq_table(self):
        self.page("频率分布表")
        headers = ("成绩区间", "频数", "频率", "频率/组距")
        xs = (-2.8, -0.85, 0.95, 2.8)
        for label, x in zip(headers, xs):
            self.show(Text(label, font=FONT, font_size=21, color=GOLD).move_to([x, 3.7, 0]), 0.2)
        for index, (left, right, count, freq, density) in enumerate(zip(
                EDGES, EDGES[1:], self.counts, self.frequencies, self.density)):
            cells = (f"[{left},{right})", str(count), f"{float(freq):.3f}", f"{float(density):.4f}")
            row = VGroup(*[Text(cell, font=FONT, font_size=20,
                                color=BLUE if index == 2 else WHITE).move_to([x, 2.65-index*0.74, 0])
                           for x, cell in zip(xs, cells)])
            self.show(row, 0.3)
        assert sum(self.counts) == len(SCORES) == 40
        assert sum(self.frequencies, Fraction(0)) == 1
        self.show(self.math(r"f_i=\frac{n_i}{40},\qquad \sum_i f_i=1", -2.65, 36, GOLD))
        self.show(self.text("组距均为10；右端点不计入本组", -3.85, 23))
        self.wait(0.9)

    def s2_histogram(self):
        self.page("频率分布直方图", BLUE)
        ax = self.axes()
        self.show(ax, 0.7)
        bars = self.histogram_bars(ax)
        self.show(bars, 1.0)
        self.show(self.text("纵轴：频率/组距；横轴：成绩", 3.75, 24))
        self.show(self.text("每根柱子的面积 = 频率", -2.15, 27, BLUE))
        self.show(self.math(r"\sum_i\frac{f_i}{d_i}\,d_i=\sum_i f_i=1", -3.5, 32, GOLD))
        assert histogram_area() == 1
        self.show(self.text("70～80分组频率最高：14/40 = 35%", -4.65, 23, GREEN))
        self.wait(0.9)

    def s3_polygon(self):
        self.page("频率折线图", RED)
        ax = self.axes()
        self.show(ax, 0.65)
        self.show(self.histogram_bars(ax), 0.55)
        mids = tuple((left + right) / 2 for left, right in zip(EDGES, EDGES[1:]))
        points = [ax.c2p(EDGES[0], 0)] + [ax.c2p(mid, float(height))
                                           for mid, height in zip(mids, self.density)] + [ax.c2p(EDGES[-1], 0)]
        line = VMobject(color=RED, stroke_width=4)
        line.set_points_as_corners(points)
        self.play(Create(line), run_time=1.8)
        self.show(self.text("连接各组顶端中点；两端落回横轴", -2.15, 25, RED))
        self.show(self.text("与直方图使用完全相同的组距及五组频数", -3.25, 22))
        assert frequency_polygon_area() != histogram_area()
        self.show(self.text("注意：折线下的面积不必恰好等于1", -4.45, 25, GOLD))
        self.wait(0.9)

    def s4_cumulative(self):
        self.page("累计频率图", PURPLE)
        ax = self.axes(cumulative=True)
        self.show(ax, 0.7)
        points = [ax.c2p(50, 0)] + [ax.c2p(edge, float(cum))
                                     for edge, cum in zip(EDGES[1:], self.cumulative)]
        curve = VMobject(color=PURPLE, stroke_width=4)
        curve.set_points_as_corners(points)
        self.play(Create(curve), run_time=1.5)
        self.show(self.text("横轴：组的上界；纵轴：该上界以下的累计频率", 3.65, 22))
        for edge, value in zip(EDGES[1:], self.cumulative):
            self.show(Text(f"{edge}: {float(value):.3f}", font=FONT, font_size=18,
                           color=PURPLE).move_to(ax.c2p(edge, float(value)) + UP * 0.26), 0.17)
        assert self.cumulative[2] == Fraction(25, 40)
        self.show(self.text("低于80分：25人，占25/40 = 62.5%", -2.35, 26, GOLD))
        self.show(self.text("折线连接组边界上的已知比例；组内形状只是示意", -3.65, 22))
        self.wait(0.8)

    def s5_stem_leaf(self):
        self.page("茎叶图：保留原始成绩", GREEN)
        data = stem_leaf()
        self.show(self.text("从40人中选出的12份示例成绩（不是全体40人）", 3.8, 23))
        for index, (stem, leaves) in enumerate(data.items()):
            row = Text(f"{stem}  │  " + "  ".join(str(leaf) for leaf in leaves),
                       font=FONT, font_size=31, color=GREEN if stem == 7 else WHITE)
            self.show(row.move_to(UP * (2.3 - 1.0 * index)), 0.32)
        self.show(self.text("例如 茎5叶8 = 58分；重复的数也必须保留", -2.45, 24, GOLD))
        self.show(self.text("本镜12个成绩均来自开场40个原始成绩", -3.7, 23, BLUE))
        self.wait(0.8)

    def s6_summary(self):
        self.page("图表的数学含义")
        self.show(self.text("分布表：频数÷样本容量 = 组频率", 3.7, 26, BLUE))
        self.show(self.text("直方图：柱面积为频率，所有柱面积之和为1", 2.35, 25, GOLD))
        self.show(self.text("频率折线：连接组中点，线下面积无需等于1", 1.0, 24, RED))
        self.show(self.text("累计图：每个组上界下方的实际样本比例", -0.35, 25, PURPLE))
        self.show(self.text("茎叶图：保留所展示的每个原始数及其重复", -1.7, 24, GREEN))
        self.show(self.math(r"\frac3{40}+\frac8{40}+\frac{14}{40}+\frac{10}{40}+\frac5{40}=1",
                            -3.5, 30, GOLD))
        self.wait(0.9)

    def s7_outro(self):
        self.page("本节要点")
        self.show(self.text("同一组原始数据，图表信息必须一致", 3.2, 28, GREEN))
        self.show(self.text("直方图的面积与折线下的面积不可混淆", 1.3, 25, GOLD))
        self.show(self.text("@emptyandcalm", -2.4, 26, GRAY_B))
        self.wait(1)
