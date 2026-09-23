"""条件概率与独立事件：条件、乘法、二项及全概率的可核验图示。

预览：manim -pql cond_prob_animation.py CondProbAnimation
回归：python -m unittest -v test_conditional_probability_math.py
"""
from fractions import Fraction
from itertools import product
from manim import *
from conditional_probability_math import (
    A, B, OMEGA, binomial, conditional, fair_coin_pairs, independent,
    probability, total_from_partition,
)

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


class CondProbAnimation(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.scene_1_opening()
        self.scene_2_conditional_prob()
        self.scene_3_multiplication_rule()
        self.scene_4_independence()
        self.scene_5_binomial()
        self.scene_6_total_prob()
        self.scene_7_summary()

    def fit(self, mob):
        """限制单对象安全区；图形遮挡和字体实际效果仍待渲染检查。"""
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
        return Text(words, font=FONT, font_size=size, color=color).move_to(UP * y)

    def math(self, formula, y, size=33, color=WHITE):
        """默认 TeX 环境仅接收纯数学/ASCII，不将中文交给 MathTex。"""
        return MathTex(formula, font_size=size, color=color).move_to(UP * y)

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.3, 39, color), 0.4)

    def tile_grid(self, outcomes, blues=frozenset(), golds=frozenset()):
        """数字是可区分且等可能的基本事件，着色对应同一数据模型。"""
        group = VGroup()
        for outcome in outcomes:
            bg = RoundedRectangle(
                width=0.93, height=0.9, corner_radius=0.09,
                fill_color=BLUE if outcome in blues else CARD,
                fill_opacity=0.9, stroke_color=GOLD if outcome in golds else GRAY_B,
                stroke_width=3 if outcome in golds else 1,
            )
            label = MathTex(str(outcome), font_size=30)
            group.add(VGroup(bg, label))
        cols = 5 if len(outcomes) == 10 else 4
        return group.arrange_in_grid(cols=cols, buff=0.16)

    def scene_1_opening(self):
        self.page("条件概率与独立事件")
        self.show(self.text("十张等可能票：编号 1～10", 3.75, 29))
        self.show(self.tile_grid(tuple(sorted(OMEGA))).move_to(UP * 2.2))
        self.show(self.text("B = 抽到 1、2、3、4；A = 抽到 1、5、6、7、8", 0.3, 22))
        self.show(self.text("已知抽中 B，再抽中 A 的条件概率？", -1.25, 26, GOLD))
        self.show(self.math(r"P(A\mid B)=\frac14", -2.65, 40, GREEN))
        self.wait(0.8)

    def scene_2_conditional_prob(self):
        self.page("条件概率：缩小样本空间", GREEN)
        assert probability(B) == Fraction(2, 5)
        assert probability(A & B) == Fraction(1, 10)
        self.show(self.tile_grid(tuple(sorted(OMEGA)), blues=B, golds=A & B)
                  .move_to(UP * 2.15), 0.7)
        self.show(self.text("蓝色四格为已知 B；金边的一格属于 A∩B", 0.4, 24))
        self.show(self.math(r"P(B)=\frac4{10},\quad P(A\cap B)=\frac1{10}",
                            -1.15, 31, BLUE))
        self.show(self.math(r"P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac14", -2.65, 31, GREEN))
        self.show(self.text("条件概率要求 P(B)>0；面积并非天然等于概率", -4.0, 22, GOLD))
        self.wait(0.9)

    def scene_3_multiplication_rule(self):
        self.page("乘法公式：先 B 后 A", GREEN)
        self.show(self.text("先看 B 是否发生，再看 B 中 A 是否发生", 3.85, 26))
        self.show(self.math(r"P(B)=\frac25=0.4", 2.45, 36, BLUE))
        self.show(self.math(r"P(A\mid B)=\frac14=0.25", 1.0, 36, RED))
        product_probability = probability(B) * conditional(A, B)
        assert product_probability == probability(A & B) == Fraction(1, 10)
        self.show(self.math(r"P(A\cap B)=P(B)P(A\mid B)", -0.6, 35, GREEN))
        self.show(self.math(r"=\frac25\cdot\frac14=\frac1{10}", -2.0, 40, GOLD))
        self.show(self.text("也可先 A 后 B：乘积是同一个交集概率", -3.55, 24))
        self.wait(0.9)

    def scene_4_independence(self):
        self.page("独立事件：两次公平硬币", GOLD)
        coins = fair_coin_pairs()
        first = frozenset(pair for pair in coins if pair[0] == "H")
        second = frozenset(pair for pair in coins if pair[1] == "H")
        assert independent(first, second, coins)
        sample = VGroup(*[Text("".join(pair), font=FONT, font_size=36,
                                color=GREEN if pair == ("H", "H") else WHITE)
                          for pair in coins]).arrange_in_grid(cols=2, buff=1)
        self.show(sample.move_to(UP * 2.15))
        self.show(self.text("A：第一次正面；B：第二次正面", 0.15, 27))
        self.show(self.math(r"P(A)=P(B)=\frac12,\quad P(A\cap B)=\frac14",
                            -1.45, 31, BLUE))
        self.show(self.math(r"P(A\cap B)=P(A)P(B)", -2.8, 35, GREEN))
        self.show(self.text("本例独立；原十张票模型中的 A、B 并不独立", -4.05, 23, GOLD))
        self.wait(0.9)

    def scene_5_binomial(self):
        self.page("三次独立投币：恰好两次正面", RED)
        outcomes = tuple(product(("H", "T"), repeat=3))
        good = tuple(outcome for outcome in outcomes if outcome.count("H") == 2)
        assert len(outcomes) == 8 and len(good) == 3
        labels = VGroup(*[Text("".join(outcome), font=FONT, font_size=28,
                               color=GREEN if outcome in good else GRAY_B)
                          for outcome in outcomes])
        self.show(labels.arrange_in_grid(cols=4, buff=0.55).move_to(UP * 2.4))
        self.show(self.text("命中：HHT、HTH、THH（3条等可能路径）", 0.4, 24, GREEN))
        assert binomial(3, 2) == Fraction(3, 8)
        self.show(self.math(r"P(X=2)={3\choose2}(\tfrac12)^2(\tfrac12)=\tfrac38",
                            -1.1, 33, GOLD))
        self.show(self.math(r"P(X=k)={n\choose k}p^k(1-p)^{n-k}",
                            -2.65, 33, RED))
        self.show(self.text("前提：每次独立，成功概率 p 相同，0≤k≤n", -4.0, 23))
        self.wait(0.9)

    def scene_6_total_prob(self):
        self.page("全概率公式：分情况求和", BLUE)
        rest = OMEGA - B
        assert conditional(A, rest) == Fraction(2, 3)
        assert total_from_partition(A, (B, rest)) == probability(A) == Fraction(1, 2)
        self.show(self.text("把十张票分成 B（4张）与 B 的补集（6张）", 3.8, 25))
        self.show(self.tile_grid(tuple(sorted(OMEGA)), blues=B, golds=A)
                  .move_to(UP * 2.0), 0.7)
        self.show(self.math(r"P(A)=P(B)P(A\mid B)+P(\bar B)P(A\mid\bar B)",
                            0.05, 29, GREEN))
        self.show(self.math(r"=\frac4{10}\cdot\frac14+\frac6{10}\cdot\frac46",
                            -1.4, 35, GOLD))
        self.show(self.math(r"=\frac1{10}+\frac4{10}=\frac12", -2.75, 36))
        self.show(self.text("两部分不重叠、覆盖全集；每个分区概率都大于零", -4.05, 22))
        self.wait(0.9)

    def scene_7_summary(self):
        self.page("核心公式总结")
        self.show(self.math(r"P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0",
                            3.65, 32, GREEN))
        self.show(self.math(r"P(A\cap B)=P(B)P(A\mid B)", 2.1, 33, BLUE))
        self.show(self.math(r"P(A\cap B)=P(A)P(B)\ \mathrm{(independent)}",
                            0.55, 29, GOLD))
        self.show(self.math(r"P(X=k)={n\choose k}p^k(1-p)^{n-k}", -1.15, 31, RED))
        self.show(self.math(r"P(A)=\sum_iP(B_i)P(A\mid B_i)", -2.75, 33, GREEN))
        self.show(self.text("@emptyandcalm", -4.35, 27, GRAY_B))
        self.wait(1.2)
