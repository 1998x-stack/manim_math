"""六年级下册 · 绝对值；七镜竖屏教学动画。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def absolute_distance(value, unit_length=0.75):
    """数轴上 value 到原点的图示长度；无需 Manim 即可测试。"""
    if unit_length <= 0:
        raise ValueError("单位长度必须大于零")
    return abs(float(value)) * unit_length


class AbsoluteValueConcept(Scene):
    """引入、距离定义、记号、分段规则、对称性、应用、总结。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.blue, self.orange = "#3498db", "#e67e22"
        self.green, self.purple = "#2ecc71", "#9b59b6"
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=19, color=GRAY_B).move_to(UP * 6.7)
        self.add(self.author)
        self.axis = NumberLine(x_range=[-5, 5, 1], length=7.5,
                               include_numbers=False, include_tip=True,
                               color=WHITE, stroke_width=3)
        self.axis.shift(UP * 1.4 - self.axis.n2p(0))
        self.axis_labels = VGroup()
        for value in [-5, -3, 0, 3, 5]:
            label = MathTex(str(value), font_size=23, color=GRAY_A)
            label.next_to(self.axis.n2p(value), DOWN, buff=0.22)
            self.axis_labels.add(label)
        self.scene_1_opening()
        self.scene_2_introduce_concept()
        self.scene_3_absolute_value_notation()
        self.scene_4_mathematical_rules()
        self.scene_5_symmetry()
        self.scene_6_real_world_applications()
        self.scene_7_summary()

    def heading(self, wording, color=YELLOW):
        return Text(wording, font_size=35, color=color).move_to(UP * 5.5)

    def point_pair(self, value):
        """点、数值和距离线段均从同一条 NumberLine 和相同 value 构造。"""
        if value <= 0:
            raise ValueError("对称示例使用正数；0 的绝对值单独说明")
        positive = Dot(self.axis.n2p(value), radius=0.11, color=self.green)
        negative = Dot(self.axis.n2p(-value), radius=0.11, color=self.orange)
        labels = VGroup(
            MathTex(str(value), font_size=28, color=self.green).next_to(positive, UP, buff=0.2),
            MathTex(str(-value), font_size=28, color=self.orange).next_to(negative, UP, buff=0.2),
        )
        left = Line(self.axis.n2p(-value) + DOWN * 0.45,
                    self.axis.n2p(0) + DOWN * 0.45, color=self.purple, stroke_width=6)
        right = Line(self.axis.n2p(0) + DOWN * 0.45,
                     self.axis.n2p(value) + DOWN * 0.45, color=self.purple, stroke_width=6)
        assert abs(left.get_length() - absolute_distance(value)) < 1e-6
        assert abs(right.get_length() - absolute_distance(value)) < 1e-6
        return VGroup(positive, negative, labels, left, right)

    def scene_1_opening(self):
        title = self.heading("3 和 -3 谁离原点更远？")
        self.play(FadeIn(title), Create(self.axis), FadeIn(self.axis_labels))
        self.wait(0.8)
        self.play(FadeOut(title))

    def scene_2_introduce_concept(self):
        title = self.heading("绝对值是到原点的距离", self.blue)
        pair = self.point_pair(3)
        equation = MathTex(r"|3|=|-3|=3", font_size=38, color=YELLOW).move_to(DOWN * 2.4)
        note = Text("距离不能为负，0 到原点的距离为 0", font_size=25).move_to(DOWN * 3.5)
        self.play(FadeIn(title), FadeIn(pair))
        self.play(Write(equation), FadeIn(note))
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(pair), FadeOut(equation), FadeOut(note))

    def scene_3_absolute_value_notation(self):
        title = self.heading("绝对值的记号与计算", self.blue)
        examples = VGroup(MathTex(r"|3|=3", font_size=37),
                          MathTex(r"|-3|=3", font_size=37),
                          MathTex(r"|0|=0", font_size=37))
        examples.arrange(DOWN, buff=0.55).move_to(UP * 3.7)
        property_formula = MathTex(r"|a|\geq 0", font_size=39,
                                   color=YELLOW).move_to(DOWN * 2.5)
        self.play(FadeIn(title))
        for example in examples:
            self.play(Write(example), run_time=0.5)
        self.play(FadeIn(property_formula))
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(examples), FadeOut(property_formula))

    def scene_4_mathematical_rules(self):
        title = self.heading("绝对值的分段定义", self.blue)
        formula = MathTex(r"|a|=\begin{cases}a,&a\geq 0\\-a,&a<0\end{cases}",
                          font_size=35).move_to(UP * 3.9)
        self.play(FadeIn(title), Write(formula))
        for start, end, example, color in [(0, 5, r"|5|=5", self.green),
                                            (-5, 0, r"|-5|=-(-5)=5", self.orange)]:
            region = Line(self.axis.n2p(start), self.axis.n2p(end),
                          color=color, stroke_width=9)
            equation = MathTex(example, font_size=33, color=color).move_to(DOWN * 2.1)
            self.play(Create(region), FadeIn(equation))
            self.wait(0.6)
            self.play(FadeOut(region), FadeOut(equation))
        zero = MathTex(r"|0|=0", font_size=35).move_to(DOWN * 2.1)
        self.play(FadeIn(zero))
        self.wait(0.6)
        self.play(FadeOut(zero), FadeOut(formula), FadeOut(title))

    def scene_5_symmetry(self):
        title = self.heading("相反数的绝对值相等", self.blue)
        formula = MathTex(r"|-a|=|a|", font_size=39,
                          color=YELLOW).move_to(UP * 4.2)
        self.play(FadeIn(title), Write(formula))
        current = self.point_pair(3)
        self.play(FadeIn(current))
        for value in (4, 2.5):
            following = self.point_pair(value)
            self.play(ReplacementTransform(current, following), run_time=0.8)
            current = following  # 更新真实屏幕对象的引用，不淡出临时目标。
        self.wait(0.8)
        self.play(FadeOut(current), FadeOut(title), FadeOut(formula))
        # 切换到生活数轴之前，清理整条课堂数轴及其全部标签。
        self.play(FadeOut(self.axis), FadeOut(self.axis_labels))

    def scene_6_real_world_applications(self):
        title = self.heading("生活中的绝对值", self.blue)
        self.play(FadeIn(title))
        temperature = NumberLine(x_range=[-10, 10, 5], length=6.5,
                                 include_numbers=True, font_size=22, color=WHITE)
        temperature.shift(UP * 1.3 - temperature.n2p(0))
        marker = Dot(temperature.n2p(-5), color=self.orange, radius=0.13)
        question = Text("温度为 -5°C，与 0°C 相差多少？", font_size=27).move_to(UP * 4.2)
        answer = MathTex(r"|-5-0|=5", font_size=37, color=YELLOW).move_to(DOWN * 2.0)
        self.play(Create(temperature), FadeIn(marker), FadeIn(question))
        self.play(Write(answer))
        self.wait(0.7)
        self.play(FadeOut(temperature), FadeOut(marker), FadeOut(question), FadeOut(answer))
        money = NumberLine(x_range=[-400, 400, 100], length=6.5,
                           include_numbers=False, color=WHITE)
        money.shift(UP * 1.3 - money.n2p(0))
        zero = MathTex("0", font_size=24).next_to(money.n2p(0), DOWN, buff=0.25)
        debt = Dot(money.n2p(-300), color=self.orange, radius=0.13)
        debt_label = MathTex("-300", font_size=28, color=self.orange).next_to(debt, UP, buff=0.2)
        note = Text("以 0 元为基准，余额 -300 元表示欠款 300 元", font_size=24)
        note.move_to(UP * 4.2)
        formula = MathTex(r"|-300|=300", font_size=37,
                          color=YELLOW).move_to(DOWN * 2.0)
        self.play(Create(money), FadeIn(zero), FadeIn(debt), FadeIn(debt_label), FadeIn(note))
        self.play(Write(formula))
        self.wait(0.8)
        self.play(FadeOut(money), FadeOut(zero), FadeOut(debt), FadeOut(debt_label),
                  FadeOut(note), FadeOut(formula), FadeOut(title))

    def create_summary_card(self, heading, content, color, target):
        bar = Rectangle(width=0.15, height=0.78, fill_color=color,
                        fill_opacity=1, stroke_width=0)
        words = VGroup(Text(heading, font_size=26),
                       Text(content, font_size=24, color=GRAY_A)).arrange(DOWN, buff=0.1)
        return VGroup(bar, words).arrange(RIGHT, buff=0.25).move_to(target)

    def scene_7_summary(self):
        title = self.heading("绝对值知识回顾", self.blue)
        cards = VGroup(
            self.create_summary_card("定义", "到原点的距离", self.blue, UP * 3.3),
            self.create_summary_card("非负性", "绝对值大于或等于零", self.green, UP * 1.8),
            self.create_summary_card("对称性", "相反数的绝对值相等", YELLOW, UP * 0.3),
        )
        formula = MathTex(r"|a|=\begin{cases}a,&a\geq0\\-a,&a<0\end{cases}",
                          font_size=32).move_to(DOWN * 2.7)
        self.play(FadeIn(title))
        for card in cards:
            target = card.get_center().copy()
            card.shift(LEFT * 7)
            # 只对卡片执行一项动画；不得并发 FadeIn 和 animate 作用于同一对象。
            self.play(card.animate.move_to(target), run_time=0.65)
        self.play(Write(formula))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(cards), FadeOut(formula), FadeOut(self.author))
