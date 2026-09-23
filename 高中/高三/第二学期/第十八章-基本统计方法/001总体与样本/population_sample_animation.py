"""总体与样本：20 个编号个体的可复现简单随机抽样教学动画。

预览：manim -pql population_sample_animation.py PopulationSample
数学测试：python -m unittest -v test_population_sample_math.py
"""
from fractions import Fraction
from math import comb
from manim import *
from population_sample_math import (POPULATION, MEASUREMENTS, inclusion_probability,
                                    sample_mean, sample_without_replacement)

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
CARD = "#16213e"
RED = "#ef6b68"
BLUE = "#56a5e8"
GOLD = "#f1c40f"
GREEN = "#58d68d"


class PopulationSample(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.selected = sample_without_replacement(POPULATION, size=6, seed=42)
        self.sample_average = sample_mean(MEASUREMENTS, self.selected)
        self.population_average = sample_mean(MEASUREMENTS, POPULATION)
        self.scene_1_opening()
        self.scene_2_population()
        self.scene_3_sampling()
        self.scene_4_sample_size()
        self.scene_5_random_sampling()
        self.scene_6_formula()
        self.scene_7_core_idea()
        self.scene_8_outro()

    def fit(self, mob):
        """单元素安全区保护；多对象相互遮挡需在实际渲染中复核。"""
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

    def text(self, message, y, size=28, color=WHITE):
        return self.fit(Text(message, font=FONT, font_size=size, color=color).move_to(UP * y))

    def math(self, expression, y, size=34, color=WHITE):
        """MathTex 只处理不含中文的数学表达式。"""
        return self.fit(MathTex(expression, font_size=size, color=color).move_to(UP * y))

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.3, 39, color), 0.4)

    def member_grid(self, highlighted=()):
        """所有格子均使用真正的个体编号，抽样高亮由同一份索引驱动。"""
        hits = frozenset(highlighted)
        assert hits <= set(POPULATION)
        cells = VGroup()
        for individual in POPULATION:
            chosen = individual in hits
            bg = RoundedRectangle(
                width=0.91, height=0.9, corner_radius=0.09,
                fill_color=BLUE if chosen else CARD, fill_opacity=0.95,
                stroke_color=GOLD if chosen else GRAY_B,
                stroke_width=2.5 if chosen else 1,
            )
            num = MathTex(str(individual), font_size=27,
                          color=BG if chosen else WHITE)
            cells.add(VGroup(bg, num))
        return cells.arrange_in_grid(rows=4, cols=5, buff=0.16)

    def scene_1_opening(self):
        self.page("总体与样本")
        self.show(self.text("研究20个编号个体的测量值", 3.65, 30))
        self.show(self.member_grid().move_to(UP * 1.35), 0.8)
        self.show(self.text("一定要测量全部20个吗？", -1.7, 30, GOLD))
        self.show(self.text("抽取一部分，借助统计方法了解总体", -2.95, 25, GREEN))
        self.show(self.text("这是教学用模拟总体，不代表真实调查数据", -4.25, 21, GRAY_B))
        self.wait(0.7)

    def scene_2_population(self):
        self.page("总体与个体", RED)
        self.show(self.text("总体：研究对象的全体", 3.65, 31))
        self.show(self.member_grid().move_to(UP * 1.35), 0.7)
        self.show(self.math(r"N=20", -1.65, 40, RED))
        self.show(self.text("个体：每一个编号所代表的研究对象", -2.95, 26, GOLD))
        self.show(self.text("此例中，测量值与个体编号一一对应", -4.25, 23, BLUE))
        self.wait(0.8)

    def scene_3_sampling(self):
        self.page("从总体抽取样本", BLUE)
        assert len(self.selected) == len(set(self.selected)) == 6
        self.show(self.member_grid(self.selected).move_to(UP * 1.35), 0.8)
        chosen = "、".join(str(individual) for individual in self.selected)
        self.show(self.text("蓝色格子：本次抽取的个体", -1.6, 27, BLUE))
        self.show(self.text("实际抽中编号：" + chosen, -2.8, 24, GOLD))
        self.show(self.text("样本是总体中的一部分；抽中者仍属于总体", -4.05, 23))
        self.wait(0.8)

    def scene_4_sample_size(self):
        self.page("样本容量", GREEN)
        self.show(self.member_grid(self.selected).move_to(UP * 1.35), 0.7)
        self.show(self.text("样本容量是抽中的个体数量，不是测量值之和", -1.6, 23))
        self.show(self.math(r"n=6,\qquad N=20", -2.9, 41, GREEN))
        self.show(self.text("这次为无放回抽样：六个编号互不重复", -4.15, 24, GOLD))
        self.wait(0.8)

    def scene_5_random_sampling(self):
        self.page("什么是简单随机抽样？", BLUE)
        self.show(self.text("从20人中无放回抽取6人", 3.8, 29))
        self.show(self.text("使每个大小为6的子集有相同入选机会", 2.7, 24, GREEN))
        assert comb(len(POPULATION), len(self.selected)) == 38760
        self.show(self.math(r"{20\choose6}=38760", 1.25, 37, GOLD))
        inclusion = inclusion_probability(len(POPULATION), len(self.selected))
        assert inclusion == Fraction(3, 10)
        self.show(self.math(r"P(\text{一个指定个体被抽中})=\frac6{20}=\frac3{10}",
                            -0.5, 29, BLUE))
        self.show(self.member_grid(self.selected).scale(0.72).move_to(DOWN * 2.45), 0.7)
        self.show(self.text("图中是固定随机种子产生的一次样本", -4.65, 22))
        self.show(self.text("无放回意味着各个抽中事件并非相互独立", -5.5, 21, GOLD))
        self.wait(0.9)

    def scene_6_formula(self):
        self.page("样本均值：来自实际抽样数据", GREEN)
        values = [MEASUREMENTS[i] for i in self.selected]
        total = sum(values)
        assert self.sample_average == Fraction(total, len(values))
        self.show(self.text("本课自设测量值：第 i 个个体取 50+2i", 3.75, 23))
        self.show(self.text("抽中的六个数值：" + "、".join(map(str, values)), 2.4, 23, BLUE))
        self.show(self.math(r"\bar x=\frac{x_1+\cdots+x_n}{n}", 0.7, 35, GREEN))
        self.show(self.math(r"\bar x=\frac{" + str(total) + r"}{6}=\frac{" +
                            str(self.sample_average.numerator) + r"}{" +
                            str(self.sample_average.denominator) + r"}",
                            -0.9, 34, GOLD))
        assert self.population_average == Fraction(71)
        self.show(self.math(r"\mu=\frac{\sum_{i=1}^{20}x_i}{20}=71", -2.65, 32, RED))
        self.show(self.text("样本均值用于估计总体均值；一次抽样不保证相等", -4.15, 23))
        self.wait(1)

    def scene_7_core_idea(self):
        self.page("用样本了解总体", GREEN)
        for caption, y, color in (("总体：20个个体", 3.7, RED),
                                  ("↓ 随机抽取6个", 2.5, GOLD),
                                  ("样本：6个可核对的编号", 1.3, BLUE),
                                  ("↓ 计算样本统计量", 0.1, GOLD),
                                  ("用样本均值估计总体均值", -1.2, GREEN)):
            self.show(self.text(caption, y, 29, color))
        self.show(self.text("随机抽样减少选择偏差，不保证单次样本完全代表总体", -3.3, 22))
        self.wait(0.8)

    def scene_8_outro(self):
        self.page("本节要点")
        self.show(self.text("总体 = 全部个体；样本 = 抽取的部分", 3.5, 26))
        self.show(self.math(r"N=20,\quad n=6", 2.1, 40, BLUE))
        self.show(self.text("抽样规则、样本编号和计算结果应相互对应", 0.3, 25, GREEN))
        self.show(self.text("@emptyandcalm", -2.6, 28, GRAY_B))
        self.wait(1)
