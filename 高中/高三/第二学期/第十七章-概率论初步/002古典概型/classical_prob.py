"""古典概型：有限、等可能的样本空间与四种计算模型。

预览：manim -pql classical_prob.py ClassicalProbability
目标：9:16；先运行 test_classical_probability_math.py 验证数值。
"""
from manim import *

from classical_probability_math import (
    ball_outcomes, die_outcomes, double_die_outcomes, example_probabilities,
    sum_seven_outcomes, two_coin_outcomes,
)

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
CARD = "#16213e"
FONT = "Noto Sans CJK SC"
RED = "#ef6b68"
BLUE = "#56a5e8"
GOLD = "#f1c40f"
GREEN = "#58d68d"


def die_face(value, size=0.72):
    """使用可数点阵，点数与所代表的基本事件严格一致。"""
    spots = {
        1: ((0, 0),),
        2: ((-1, 1), (1, -1)),
        3: ((-1, 1), (0, 0), (1, -1)),
        4: ((-1, -1), (-1, 1), (1, -1), (1, 1)),
        5: ((-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)),
        6: ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)),
    }
    if value not in spots:
        raise ValueError("骰子点数应在 1 至 6 之间")
    face = RoundedRectangle(
        width=size, height=size, corner_radius=0.09,
        fill_color=WHITE, fill_opacity=1, stroke_color=BLUE, stroke_width=2,
    )
    dots = [Dot([x * size * 0.28, y * size * 0.28, 0], radius=size * 0.065,
                color=BG) for x, y in spots[value]]
    return VGroup(face, *dots)


def coin_face(side):
    if side not in ("H", "T"):
        raise ValueError("硬币面必须是 H 或 T")
    circle = Circle(radius=0.38, fill_color=GOLD if side == "H" else BLUE,
                    fill_opacity=1, stroke_color=WHITE, stroke_width=2)
    label = MathTex(side, font_size=35, color=BG)
    return VGroup(circle, label)


class ClassicalProbability(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.values = example_probabilities()
        self.scene_opening()
        self.scene_definition()
        self.scene_die_single()
        self.scene_die_double()
        self.scene_balls()
        self.scene_coins()
        self.scene_summary()
        self.scene_outro()

    def text(self, content, y, size=28, color=WHITE):
        return Text(content, font=FONT, font_size=size, color=color).move_to(UP * y)

    def math(self, formula, y, size=34, color=WHITE):
        return MathTex(formula, font_size=size, color=color).move_to(UP * y)

    def show(self, mob, duration=0.55):
        """防止单个对象超出 9:16 的逻辑安全区；实际帧仍须渲染审查。"""
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
        self.play(FadeIn(mob), run_time=duration)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.65, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.35, 39, color), 0.4)

    def formula_card(self, formula, y, color=GREEN, size=34):
        formula_mob = MathTex(formula, font_size=size)
        if formula_mob.width > 7.1:
            formula_mob.scale_to_fit_width(7.1)
        bg = RoundedRectangle(
            width=min(7.8, formula_mob.width + 0.5), height=formula_mob.height + 0.4,
            corner_radius=0.13, fill_color=CARD, fill_opacity=1,
            stroke_color=color, stroke_width=2,
        )
        return VGroup(bg, formula_mob).move_to(UP * y)

    def scene_opening(self):
        self.page("古典概型")
        self.show(die_face(6, 1.45).move_to(UP * 2.1))
        self.show(self.text("一枚公平骰子，掷出 6 的概率是多少？", 0.15, 28))
        self.show(self.formula_card(r"P(6)=\frac{1}{6}", -1.2))
        self.show(self.text("先数结果，再检查是否等可能", -3, 25, BLUE))
        self.wait(0.8)

    def scene_definition(self):
        self.page("公式何时能用？", GREEN)
        self.show(self.text("① 有限：基本事件只有有限个", 3.9, 28))
        self.show(self.text("② 等可能：每个基本事件概率相同", 2.65, 27))
        self.show(VGroup(*[die_face(face, 0.7) for face in die_outcomes()])
                  .arrange(RIGHT, buff=0.25).move_to(UP * 1.1))
        self.show(self.formula_card(r"P(A)=\frac{m}{n},\quad n>0", -0.45))
        self.show(self.text("n：总基本事件数；m：事件 A 包含的个数", -2.0, 22))
        self.show(self.text("不能只因结果有限，就假定它们等可能", -3.3, 24, GOLD))
        self.wait(0.9)

    def scene_die_single(self):
        self.page("模型一：一枚公平骰子", RED)
        outcomes = die_outcomes()
        dice = VGroup(*[die_face(face) for face in outcomes]).arrange(RIGHT, buff=0.31)
        dice.move_to(UP * 2.9)
        self.show(dice)
        self.show(self.text("六个面等可能：n = 6", 1.65, 25))
        self.show(self.text("掷出 1：命中一个基本事件", 0.2, 26))
        self.show(self.formula_card(r"P(1)=\frac{1}{6}", -1.0, RED))
        even = (2, 4, 6)
        self.play(*[dice[number - 1][0].animate.set_fill(RED) for number in even],
                  run_time=0.5)
        self.show(self.text("掷出偶数：命中 2、4、6 三个基本事件", -2.35, 25))
        assert self.values["die_even"].numerator == len(even)
        self.show(self.formula_card(r"P(\text{偶数})=\frac{3}{6}=\frac12", -3.7, GREEN, 30))
        self.wait(0.8)

    def scene_die_double(self):
        self.page("进阶：独立掷两次公平骰子", RED)
        omega = double_die_outcomes()
        hits = set(sum_seven_outcomes())
        self.show(self.text("有序结果 (第一次, 第二次)，共 6×6 = 36 种", 4.15, 24))
        cells = VGroup()
        for second in die_outcomes():
            for first in die_outcomes():
                square = Square(side_length=0.57, fill_color=RED if (first, second) in hits else CARD,
                                fill_opacity=0.85, stroke_color=GRAY_B, stroke_width=1)
                digit = Text(str(first + second), font=FONT, font_size=17)
                cells.add(VGroup(square, digit))
        cells.arrange_in_grid(rows=6, cols=6, buff=0.055).move_to(UP * 1.3)
        self.show(cells, 0.8)
        self.show(self.text("列：第一次的点数；行：第二次的点数", -1.4, 22, BLUE))
        self.show(self.text("红格：点数和为 7，共 6 格", -2.55, 26, RED))
        assert len(cells) == len(omega) == 36 and len(hits) == 6
        self.show(self.formula_card(r"P(\text{和}=7)=\frac{6}{36}=\frac16", -3.9, GREEN, 29))
        self.wait(0.8)

    def scene_balls(self):
        self.page("模型二：从袋中随机摸一个球", RED)
        balls = ball_outcomes(3, 5)
        self.show(self.text("3 个红球、5 个蓝球，每个球被摸出机会相等", 4.1, 24))
        icons = VGroup()
        for color, number in balls:
            circle = Circle(radius=0.31, fill_color=RED if color == "红" else BLUE,
                            fill_opacity=1, stroke_color=WHITE, stroke_width=1)
            label = Text(str(number), font=FONT, font_size=19)
            icons.add(VGroup(circle, label))
        icons.arrange_in_grid(rows=2, cols=4, buff=0.45).move_to(UP * 1.8)
        self.show(icons)
        self.show(self.text("八个可区分的基本事件，红色命中 3 个", -0.5, 26))
        assert len(icons) == len(balls) == 8
        self.show(self.formula_card(r"P(\text{摸到红球})=\frac38", -1.95, RED, 30))
        self.show(self.text("只有明确了等可能性，才可按球数计算", -3.3, 24, GOLD))
        self.wait(0.8)

    def scene_coins(self):
        self.page("模型三：独立抛两次公平硬币", GOLD)
        outcomes = two_coin_outcomes()
        groups = VGroup()
        for first, second in outcomes:
            pair = VGroup(coin_face(first), coin_face(second)).arrange(RIGHT, buff=0.2)
            label = MathTex(first + second, font_size=27,
                            color=GREEN if "H" in (first, second) else GRAY_B)
            groups.add(VGroup(pair, label).arrange(DOWN, buff=0.15))
        groups.arrange_in_grid(rows=2, cols=2, buff=0.65).move_to(UP * 1.85)
        self.show(groups, 0.9)
        self.show(self.text("HH、HT、TH、TT 是四种不同的等可能结果", -0.2, 23))
        self.show(self.text("至少一次正面：HH、HT、TH", -1.65, 26, GREEN))
        assert len(groups) == len(outcomes) == 4
        self.show(self.formula_card(r"P(\text{至少一次正面})=\frac34", -3.15, GREEN, 30))
        self.wait(0.8)

    def scene_summary(self):
        self.page("解题四步", GREEN)
        for label, y in (("① 确认有限性、等可能性", 3.75),
                         ("② 列出所有基本事件", 2.4),
                         ("③ 数出总数 n 和命中数 m", 1.05),
                         ("④ 计算 P(A)=m/n", -0.3)):
            self.show(self.text(label, y, 28))
        self.show(self.formula_card(r"P(A)=\frac{m}{n},\quad 0\le P(A)\le 1", -2.2))
        self.show(self.text("不等可能时，不能直接数个数求概率", -3.8, 24, GOLD))
        self.wait(1)

    def scene_outro(self):
        self.page("古典概型 · 一图记牢")
        self.show(self.text("有限 + 等可能 + 准确计数", 2.7, 32, GREEN))
        self.show(self.formula_card(r"P(A)=\frac{m}{n}", 0.7))
        self.show(self.text("@emptyandcalm", -2.1, 28, GRAY_B))
        self.wait(1)
