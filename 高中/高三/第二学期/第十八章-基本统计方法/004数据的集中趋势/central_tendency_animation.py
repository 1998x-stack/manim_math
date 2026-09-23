"""数据的集中趋势：均值、加权均值、中位数、众数和极端值对比。

预览：manim -pql central_tendency_animation.py CentralTendency
回归：python -m unittest -v test_central_tendency_math.py
"""
from fractions import Fraction
from manim import *
from central_tendency_math import (AFTER, BEFORE, EVEN, MODE_DATA, ODD,
    SCORES, WEIGHTS, mean, median, modes, outlier_comparison, weighted_mean)

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


class CentralTendency(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.s0_opening()
        self.s1_mean()
        self.s2_weighted_mean()
        self.s3_median()
        self.s4_mode()
        self.s5_outlier()
        self.s6_summary()
        self.s7_outro()

    def fit(self, mob):
        """限制单个对象的9:16安全区；整体叠放需渲染审查。"""
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

    def text(self, words, y, size=27, color=WHITE):
        return self.fit(Text(words, font=FONT, font_size=size, color=color).move_to(UP * y))

    def math(self, expression, y, size=34, color=WHITE):
        """中文使用 Text；MathTex 中仅含纯 LaTeX。"""
        return self.fit(MathTex(expression, font_size=size, color=color).move_to(UP * y))

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.3, 37, color), 0.4)

    def data_tiles(self, values, highlights=(), columns=0):
        xs = tuple(sorted(values))
        hits = frozenset(highlights)
        if not columns:
            columns = min(5, len(xs))
        result = VGroup()
        for index, value in enumerate(xs):
            marked = index in hits
            bg = RoundedRectangle(
                width=1.0, height=0.78, corner_radius=0.09,
                fill_color=BLUE if marked else CARD, fill_opacity=0.95,
                stroke_color=GOLD if marked else GRAY_B,
                stroke_width=2 if marked else 1,
            )
            label = Text(str(value), font=FONT, font_size=24,
                         color=BG if marked else WHITE)
            result.add(VGroup(bg, label))
        return result.arrange_in_grid(cols=columns, buff=0.18)

    def s0_opening(self):
        self.page("数据的集中趋势")
        self.show(self.text("9个教学示例成绩：描述典型值", 3.8, 29))
        self.show(self.data_tiles(ODD).move_to(UP * 1.35), 0.8)
        self.show(self.text("均值、中位数、众数回答不同的问题", -1.6, 27, GOLD))
        self.show(self.text("图示仅为本课自设的模拟数据", -3.0, 23, GREEN))
        self.wait(0.7)

    def s1_mean(self):
        self.page("① 平均数", BLUE)
        self.show(self.data_tiles(ODD).move_to(UP * 1.55), 0.8)
        total, n = sum(ODD), len(ODD)
        result = mean(ODD)
        assert total == 680 and result == Fraction(680, 9)
        self.show(self.text("这9个数的总和为" + str(total), -1.0, 26))
        self.show(self.math(r"\bar x=\frac{\sum_{i=1}^{n}x_i}{n}", -2.15, 37, BLUE))
        self.show(self.math(r"\bar x=\frac{680}{9}\approx" + f"{float(result):.2f}", -3.6, 36, GOLD))
        self.show(self.text("均值由全部9个观察值共同决定", -4.8, 24))
        self.wait(0.9)

    def s2_weighted_mean(self):
        self.page("② 加权平均数", PURPLE)
        self.show(self.text("期末成绩85分，权重60%", 3.7, 30, PURPLE))
        self.show(self.text("平时成绩70分，权重40%", 2.5, 30, BLUE))
        result = weighted_mean(SCORES, WEIGHTS)
        assert result == 79 and sum(WEIGHTS) == 1
        self.show(self.math(r"\bar x_w=\frac{\sum_iw_ix_i}{\sum_iw_i}", 0.8, 35))
        self.show(self.math(r"85\times0.6+70\times0.4=79", -0.9, 37, GOLD))
        self.show(self.text("权重均非负，总权重为1；加权均值为79分", -2.4, 23, PURPLE))
        self.show(self.text("若权重未归一化，应除以权重总和", -3.6, 24))
        self.wait(0.8)

    def s3_median(self):
        self.page("③ 中位数：奇数个数据", RED)
        sorted_odd = tuple(sorted(ODD))
        self.show(self.data_tiles(ODD, highlights=(4,)).move_to(UP * 1.45), 0.8)
        assert median(ODD) == sorted_odd[4] == 78
        self.show(self.text("从小到大排9个数：第5个数为78", -1.55, 27, RED))
        self.show(self.math(r"M=x_{(n+1)/2}=78", -2.95, 37, GOLD))
        self.wait(0.6)

        self.page("③ 中位数：偶数个数据", RED)
        sorted_even = tuple(sorted(EVEN))
        self.show(self.data_tiles(EVEN, highlights=(2, 3), columns=3).move_to(UP * 1.45), 0.7)
        assert median(EVEN) == Fraction(76)
        self.show(self.text("排序后取中间两个数：74和78", -1.55, 27, RED))
        self.show(self.math(r"M=\frac{74+78}{2}=76", -2.95, 38, GOLD))
        self.wait(0.8)

    def s4_mode(self):
        self.page("④ 众数：出现最频繁的数", GREEN)
        frequency = modes(MODE_DATA)
        assert frequency == (78,)
        self.show(self.data_tiles(MODE_DATA, highlights=(2, 3, 4), columns=4)
                  .move_to(UP * 1.55), 0.7)
        self.show(self.text("本例78出现3次，其他值各出现1次", -1.1, 26, GREEN))
        self.show(self.math(r"\mathrm{Mo}=78", -2.35, 42, GOLD))
        self.show(self.text("可能并列出现多个众数；本课约定全不重复时无众数", -3.75, 22))
        self.wait(0.8)

    def s5_outlier(self):
        self.page("⑤ 极端值对均值与中位数的影响", GOLD)
        before, after = outlier_comparison()
        assert before == (Fraction(275, 4), Fraction(69))
        assert after == (Fraction(84), Fraction(69))
        self.show(self.text("仅把最后一个78替换为200，其他7个不变", 3.8, 24))
        self.show(self.data_tiles(BEFORE, columns=4).move_to(UP * 2.0), 0.7)
        self.show(self.text("替换后", 0.4, 22, GOLD))
        self.show(self.data_tiles(AFTER, highlights=(7,), columns=4)
                  .move_to(DOWN * 1.15), 0.7)
        self.show(self.math(r"\bar x:\ 68.75\longrightarrow84", -3.0, 34, BLUE))
        self.show(self.math(r"M:\ 69\longrightarrow69", -4.0, 35, RED))
        self.show(self.text("本例中位数未变；它通常对单个极端值较不敏感", -5.1, 21))
        self.wait(0.9)

    def s6_summary(self):
        self.page("三种指标的含义")
        self.show(self.text("均值：全部数据参与计算，会受到极端值影响", 3.75, 25, BLUE))
        self.show(self.text("中位数：排序取中间，通常更不易被极端值拉动", 2.4, 24, RED))
        self.show(self.text("众数：出现次数最多的值，可有并列", 1.05, 26, GREEN))
        self.show(self.text("选择哪个指标要看数据形态和实际问题", -0.55, 26, GOLD))
        self.show(self.math(r"\bar x=\frac{680}{9},\quad M=78", -2.15, 36))
        self.show(self.text("上述数值仅针对开场的9个模拟成绩", -3.55, 22))
        self.wait(0.9)

    def s7_outro(self):
        self.page("本节要点")
        self.show(self.text("求均值先求和；求中位数先排序；求众数数频次", 2.65, 25, GREEN))
        self.show(self.text("极端值对不同集中趋势指标的影响不同", 0.8, 25, GOLD))
        self.show(self.text("@emptyandcalm", -2.2, 28, GRAY_B))
        self.wait(1)
