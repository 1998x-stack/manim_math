"""数据的离散程度：同均值两组数据的极差、描述性方差、标准差与变异系数。

预览：manim -pql data_dispersion.py DataDispersion
测试：python -m unittest -v test_data_dispersion_math.py
"""
from fractions import Fraction
from manim import *
from data_dispersion_math import (A, B, coefficient_of_variation, data_range,
    descriptive_variance, mean, standard_deviation, unbiased_sample_variance)

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


class DataDispersion(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.scene_1_opening()
        self.scene_2_range()
        self.scene_3_variance()
        self.scene_4_std()
        self.scene_5_summary()
        self.scene_6_outro()

    def fit(self, mob):
        """单个屏上对象限于竖屏安全区；多对象位置仍需实渲染审查。"""
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

    def text(self, message, y, size=27, color=WHITE):
        return self.fit(Text(message, font=FONT, font_size=size, color=color).move_to(UP * y))

    def math(self, formula, y, size=33, color=WHITE):
        """中文说明均采用 Text，公式只传入纯 LaTeX。"""
        return self.fit(MathTex(formula, font_size=size, color=color).move_to(UP * y))

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.3, 39, color), 0.4)

    @staticmethod
    def data_x(value):
        """10等分数轴上真实值的线性位置，适用于0到10之间的教学数据。"""
        if not 0 <= value <= 10:
            raise ValueError("数轴值超出0至10")
        return -3.1 + value * 6.2 / 10

    def data_panel(self):
        rows = VGroup()
        for values, name, color, y in ((A, "A组", BLUE, 1.9), (B, "B组", RED, 0.3)):
            row = VGroup(Line([self.data_x(0), y, 0], [self.data_x(10), y, 0],
                              color=GRAY_B, stroke_width=2))
            for value in values:
                row.add(Dot([self.data_x(value), y, 0], radius=0.11, color=color))
                row.add(Text(str(value), font=FONT, font_size=19, color=color)
                        .move_to([self.data_x(value), y - 0.35, 0]))
            row.add(Text(name, font=FONT, font_size=21, color=color)
                    .move_to([-3.6, y + 0.15, 0]))
            mean_x = self.data_x(mean(values))
            row.add(DashedLine([mean_x, y - 0.2, 0], [mean_x, y + 0.6, 0],
                               color=GOLD, stroke_width=2))
            rows.add(row)
        return rows

    def scene_1_opening(self):
        self.page("两组同均值数据的离散程度")
        self.show(self.text("A组：3、4、5、6、7；B组：1、2、5、8、9", 3.75, 24))
        self.show(self.data_panel(), 0.9)
        assert mean(A) == mean(B) == 5
        self.show(self.math(r"\bar x_A=\bar x_B=5", -1.45, 40, GOLD))
        self.show(self.text("均值相同，并不代表数据分散情况相同", -2.9, 24))
        self.wait(0.8)

    def scene_2_range(self):
        self.page("① 极差：最大值减最小值", BLUE)
        self.show(self.data_panel(), 0.7)
        for values, y, color in ((A, 1.45, BLUE), (B, -0.15, RED)):
            self.show(Line([self.data_x(min(values)), y, 0],
                           [self.data_x(max(values)), y, 0],
                           color=color, stroke_width=5), 0.4)
        assert data_range(A) == 4 and data_range(B) == 8
        self.show(self.math(r"R_A=7-3=4", -1.4, 37, BLUE))
        self.show(self.math(r"R_B=9-1=8", -2.65, 37, RED))
        self.show(self.text("极差只由最小值与最大值决定", -4.05, 26, GOLD))
        self.wait(0.9)

    def scene_3_variance(self):
        self.page("② 描述性方差：偏差平方的平均", GREEN)
        self.show(self.data_panel(), 0.7)
        assert descriptive_variance(A) == Fraction(2)
        assert descriptive_variance(B) == Fraction(10)
        self.show(self.math(r"v=\frac1n\sum_{i=1}^n(x_i-\bar x)^2", -1.4, 34, GREEN))
        self.show(self.math(r"v_A=\frac{4+1+0+1+4}{5}=2", -2.65, 31, BLUE))
        self.show(self.math(r"v_B=\frac{16+9+0+9+16}{5}=10", -3.75, 31, RED))
        self.show(self.text("此处描述五个观测值，用分母n；不是无偏估计", -4.9, 22, GOLD))
        self.wait(0.9)

    def scene_4_std(self):
        self.page("③ 标准差：方差的非负平方根", GOLD)
        self.show(self.data_panel(), 0.7)
        self.show(self.math(r"\sigma=\sqrt{v}\geq0", -1.35, 37, GREEN))
        self.show(self.math(r"\sigma_A=\sqrt2\approx1.41", -2.55, 37, BLUE))
        self.show(self.math(r"\sigma_B=\sqrt{10}\approx3.16", -3.75, 37, RED))
        assert standard_deviation(A) < standard_deviation(B)
        self.show(self.text("标准差与原始数据使用相同单位", -4.95, 23, GOLD))
        self.wait(0.8)

    def scene_5_summary(self):
        self.page("④ 变异系数与方法对比", GREEN)
        assert coefficient_of_variation(A) < coefficient_of_variation(B)
        assert unbiased_sample_variance(A) == Fraction(5, 2)
        self.show(self.text("在可比较的比率尺度、非零均值下：", 3.7, 25))
        self.show(self.math(r"CV=\frac{\sigma}{|\bar x|}", 2.35, 38, GOLD))
        self.show(self.math(r"CV_A=\frac{\sqrt2}{5}\approx28.3\%", 0.85, 32, BLUE))
        self.show(self.math(r"CV_B=\frac{\sqrt{10}}5\approx63.2\%", -0.4, 32, RED))
        self.show(self.text("本例均值相同，B组的极差、方差和标准差均更大", -1.85, 23))
        self.show(self.text("若任务是由样本无偏估计方差，分母改为n−1", -3.2, 23, GOLD))
        self.show(self.text("变异系数不适用于均值为0的情形", -4.4, 24))
        self.wait(0.9)

    def scene_6_outro(self):
        self.page("本节要点")
        self.show(self.math(r"R=x_{\max}-x_{\min}", 3.35, 34, BLUE))
        self.show(self.math(r"v=\frac1n\sum_i(x_i-\bar x)^2", 1.9, 31, GREEN))
        self.show(self.math(r"\sigma=\sqrt v", 0.4, 38, GOLD))
        self.show(self.text("先区分描述性方差与无偏样本方差的分母", -1.25, 23))
        self.show(self.text("@emptyandcalm", -3.2, 26, GRAY_B))
        self.wait(1)
