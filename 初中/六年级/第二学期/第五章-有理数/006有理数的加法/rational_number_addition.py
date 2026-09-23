"""六年级下册 · 有理数加法：八镜竖屏、精确分数模型及数轴位移。"""
from fractions import Fraction
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def addition_path(left, right):
    """可独立测试的数轴加法路径：0 → left → left + right。"""
    a, b = Fraction(str(left)), Fraction(str(right))
    return Fraction(0), a, a + b


def addition_kind(left, right):
    """返回教学分类：zero、cancel、same、different。"""
    a, b = Fraction(str(left)), Fraction(str(right))
    if a == 0 or b == 0:
        return "zero"
    if a + b == 0:
        return "cancel"
    if (a > 0) == (b > 0):
        return "same"
    return "different"


class RationalNumberAddition(Scene):
    """保持原有八镜入口与每镜方法名；同一根数轴展示所有算例。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.green, self.orange = "#2ecc71", "#e74c3c"
        self.gold, self.gray = "#f39c12", "#95a5a6"
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 6.7)
        self.number_line = NumberLine(x_range=[-6, 6, 1], length=7.2,
                                      include_numbers=True, font_size=18,
                                      include_tip=True, color=WHITE)
        self.number_line.shift(UP * 1.4 - self.number_line.n2p(0))
        self.add(self.author)
        self.show_opening()
        self.show_positive_plus_positive()
        self.show_negative_plus_negative()
        self.show_positive_plus_negative_case1()
        self.show_negative_plus_positive_case2()
        self.show_add_zero()
        self.show_summary()
        self.show_outro()

    def heading(self, words, color=YELLOW):
        return Text(words, font_size=33, color=color).move_to(UP * 5.4)

    def show_opening(self):
        title = self.heading("正数与负数怎样相加？")
        subtitle = Text("从原点出发，向右表示加正数，向左表示加负数",
                        font_size=24).move_to(UP * 4.2)
        self.play(FadeIn(title), FadeIn(subtitle))
        self.play(Create(self.number_line))
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(subtitle))

    def demonstrate(self, left, right, formula, title_text, rule_text):
        """同一数据派生首段、第二段、结果点及文字；加零时不创建零长箭头。"""
        origin, midpoint, result = addition_path(left, right)
        assert -6 <= origin <= 6 and -6 <= midpoint <= 6 and -6 <= result <= 6
        heading = self.heading(title_text)
        question = MathTex(formula, font_size=34).move_to(UP * 4.1)
        point = Dot(self.number_line.n2p(0), color=self.gold, radius=0.13)
        self.play(FadeIn(heading), Write(question), FadeIn(point))
        arrows = VGroup()
        if left != 0:
            first = Arrow(self.number_line.n2p(0) + UP * 0.48,
                          self.number_line.n2p(float(midpoint)) + UP * 0.48,
                          buff=0, color=self.green if left > 0 else self.orange)
            arrows.add(first)
            self.play(GrowArrow(first), point.animate.move_to(self.number_line.n2p(float(midpoint))))
        if right != 0:
            second = Arrow(self.number_line.n2p(float(midpoint)) + DOWN * 0.44,
                           self.number_line.n2p(float(result)) + DOWN * 0.44,
                           buff=0, color=self.green if right > 0 else self.orange)
            arrows.add(second)
            self.play(GrowArrow(second), point.animate.move_to(self.number_line.n2p(float(result))))
        else:
            stay = Text("加 0：位置不变", font_size=24,
                        color=YELLOW).move_to(DOWN * 0.4)
            self.play(Indicate(point), FadeIn(stay))
            self.play(FadeOut(stay))
        result_label = MathTex(str(result), font_size=29,
                               color=self.gold).next_to(point, UP, buff=0.25)
        conclusion = MathTex(formula.split("=")[0] + "=" + str(result),
                             font_size=34, color=self.gold).move_to(DOWN * 2.3)
        rule = Text(rule_text, font_size=24, color=YELLOW).move_to(DOWN * 3.5)
        self.play(FadeIn(result_label), Write(conclusion), FadeIn(rule))
        self.wait(0.85)
        self.play(FadeOut(heading), FadeOut(question), FadeOut(point),
                  FadeOut(arrows), FadeOut(result_label),
                  FadeOut(conclusion), FadeOut(rule))

    def show_positive_plus_positive(self):
        self.demonstrate(3, 2, r"(+3)+(+2)=?", "同号：正数与正数相加",
                         "取相同的正号，绝对值相加")

    def show_negative_plus_negative(self):
        self.demonstrate(-2, -3, r"(-2)+(-3)=?", "同号：负数与负数相加",
                         "取相同的负号，绝对值相加")

    def show_positive_plus_negative_case1(self):
        self.demonstrate(5, -2, r"(+5)+(-2)=?", "异号：正数的绝对值较大",
                         "较大绝对值减较小绝对值，取正号")

    def show_negative_plus_positive_case2(self):
        self.demonstrate(-5, 2, r"(-5)+(+2)=?", "异号：负数的绝对值较大",
                         "较大绝对值减较小绝对值，取负号")

    def show_add_zero(self):
        self.demonstrate(3, 0, r"(+3)+0=?", "与零相加",
                         "加零不改变原数；数轴上的点不移动")
        self.demonstrate(3, -3, r"(+3)+(-3)=?", "互为相反数相加",
                         "互为相反数相加等于零")

    def show_summary(self):
        self.play(FadeOut(self.number_line))
        title = self.heading("有理数加法法则", self.gold)
        statements = [
            "同号两数：取相同符号，绝对值相加",
            "异号两数：绝对值相减，取绝对值较大数的符号",
            "互为相反数：和为零；加零：原数不变",
        ]
        cards = VGroup()
        self.play(FadeIn(title))
        for index, sentence in enumerate(statements):
            card = Text(sentence, font_size=23, color=WHITE).move_to(UP * (3.2 - index * 1.7))
            destination = card.get_center().copy()
            card.shift(LEFT * 7)
            self.play(card.animate.move_to(destination), run_time=0.6)
            cards.add(card)
        commutative = MathTex(r"a+b=b+a", font_size=31).move_to(DOWN * 2.4)
        associative = MathTex(r"(a+b)+c=a+(b+c)", font_size=30).move_to(DOWN * 3.5)
        self.play(Write(commutative), Write(associative))
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(cards), FadeOut(commutative), FadeOut(associative))

    def show_outro(self):
        recap = Text("用数轴理解方向，用法则确定符号", font_size=29,
                     color=YELLOW).move_to(UP * 1.2)
        self.play(FadeIn(recap))
        self.wait(1.0)
        self.play(FadeOut(recap), FadeOut(self.author))
