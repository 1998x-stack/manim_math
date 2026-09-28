"""抽样技术：简单随机、随机起点系统抽样、比例分层抽样。

预览：manim -pql sampling_techniques_animation.py SamplingTechniques
回归：python -m unittest -v test_sampling_techniques_math.py
"""
from fractions import Fraction
from math import comb
from manim import *
from sampling_techniques_math import (ALLOCATIONS, LAYERS, POPULATION,
    allocation_rates, random_systematic, simple_random, stratified)

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


class SamplingTechniques(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.simple_ids = simple_random(size=5, seed=7)
        self.system_start, self.system_ids = random_systematic(size=5, seed=13)
        self.layer_samples = stratified(seed=19)
        self.stratified_ids = frozenset(i for layer in self.layer_samples for i in layer)
        self.s0_opening()
        self.s1_simple_random()
        self.s2_systematic()
        self.s3_stratified()
        self.s4_summary()
        self.s5_outro()

    def fit(self, mob):
        """对象安全区保护；成片仍需逐帧查多对象交叠。"""
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

    def text(self, content, y, size=26, color=WHITE):
        return self.fit(Text(content, font=FONT, font_size=size, color=color).move_to(UP * y))

    def math(self, latex, y, size=34, color=WHITE):
        """仅使用纯数学 LaTeX，中文文本单独绘制。"""
        return self.fit(MathTex(latex, font_size=size, color=color).move_to(UP * y))

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def page(self, heading, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(obj) for obj in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(heading, 5.35, 37, color), 0.4)

    def member_grid(self, highlighted=()):
        """40个编号严格采用1..40顺序排列，抽样序列与高亮格子一致。"""
        chosen = frozenset(highlighted)
        assert chosen <= set(POPULATION)
        cells = VGroup()
        for member in POPULATION:
            hit = member in chosen
            box = RoundedRectangle(
                width=0.63, height=0.62, corner_radius=0.06,
                stroke_color=GOLD if hit else GRAY_B,
                stroke_width=2 if hit else 0.8,
                fill_color=BLUE if hit else CARD, fill_opacity=0.95,
            )
            label = Text(str(member), font=FONT, font_size=19,
                         color=BG if hit else WHITE)
            cells.add(VGroup(box, label))
        return cells.arrange_in_grid(rows=5, cols=8, buff=0.12)

    def s0_opening(self):
        self.page("三种常见抽样技术")
        self.show(self.text("从40个编号个体中抽取一部分", 3.8, 29))
        self.show(self.member_grid().move_to(UP * 1.1), 0.8)
        self.show(self.text("不同抽样方案，能够产生的样本集合不同", -1.9, 25, GOLD))
        self.show(self.text("以下均为教学用模拟总体", -3.15, 23, GREEN))
        self.wait(0.7)

    def s1_simple_random(self):
        self.page("① 简单随机抽样", RED)
        assert len(self.simple_ids) == len(set(self.simple_ids)) == 5
        self.show(self.text("40人中等可能选出任意一个5人子集", 3.8, 26))
        self.show(self.member_grid(self.simple_ids).move_to(UP * 1.1), 0.8)
        self.show(self.text("本次抽到：" + "、".join(map(str, self.simple_ids)), -1.8, 23, GOLD))
        assert comb(40, 5) == 658008
        self.show(self.math(r"{40\choose5}=658008", -3.05, 37, RED))
        self.show(self.math(r"P(i\in S)=\frac5{40}=\frac18", -4.35, 32, BLUE))
        self.wait(0.8)

    def s2_systematic(self):
        self.page("② 等距系统抽样", BLUE)
        assert len(self.system_ids) == 5 and 1 <= self.system_start <= 8
        self.show(self.text("按编号顺序每8人一段，首段随机选一个起点", 3.8, 24))
        self.show(self.member_grid(self.system_ids).move_to(UP * 1.1), 0.8)
        self.show(self.math(r"k=\frac{40}{5}=8", -1.9, 37, BLUE))
        self.show(self.text("本次首段起点：" + str(self.system_start), -2.85, 25, GOLD))
        self.show(self.text("依次选出编号：" + "、".join(map(str, self.system_ids)), -3.7, 23))
        self.show(self.text("仅有8种等距样本，不能当作全部5人组合等可能", -4.8, 21, GREEN))
        self.wait(0.8)

    def s3_stratified(self):
        self.page("③ 按比例分层抽样", GREEN)
        assert tuple(map(len, LAYERS)) == (20, 12, 8)
        assert tuple(map(len, self.layer_samples)) == ALLOCATIONS
        assert allocation_rates() == (Fraction(1, 4),) * 3
        self.show(self.text("总体分三层：20人、12人、8人；共抽10人", 3.85, 24))
        self.show(self.member_grid(self.stratified_ids).move_to(UP * 1.1), 0.8)
        for group, layer, size, y, color in zip(
                self.layer_samples, ("第一层", "第二层", "第三层"), ALLOCATIONS,
                (-1.85, -2.7, -3.55), (RED, BLUE, GREEN)):
            self.show(self.text(layer + "抽" + str(size) + "人：" + "、".join(map(str, group)),
                                y, 21, color))
        self.show(self.math(r"\frac5{20}=\frac3{12}=\frac2{8}=\frac14", -4.7, 31, GOLD))
        self.show(self.text("各层内部独立实施无放回随机抽样", -5.65, 22))
        self.wait(0.9)

    def s4_summary(self):
        self.page("三种方法的不同", GOLD)
        self.show(self.text("简单随机：任意5人子集都有相同抽中概率", 3.7, 25, RED))
        self.show(self.text("系统抽样：随机起点，再按固定间隔抽5人", 2.45, 25, BLUE))
        self.show(self.text("分层抽样：按20、12、8分层，分别抽5、3、2人", 1.2, 23, GREEN))
        self.show(self.math(r"n_{\mathrm{simple}}=n_{\mathrm{system}}=5", -0.65, 29))
        self.show(self.math(r"n_{\mathrm{stratified}}=10", -1.85, 31, GOLD))
        self.show(self.text("等入样概率，不等于所有方案都允许任意子集", -3.3, 23))
        self.show(self.text("抽样规则应与总体构成、推断目标相匹配", -4.5, 24, GREEN))
        self.wait(0.8)

    def s5_outro(self):
        self.page("本节要点")
        self.show(self.text("随机选子集 · 随机起点等距 · 层内按比例随机", 3.0, 26))
        self.show(self.text("同一组抽样数据必须对应同一组高亮编号", 1.35, 24, GREEN))
        self.show(self.text("@emptyandcalm", -2.3, 27, GRAY_B))
        self.wait(1)
