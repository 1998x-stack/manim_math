"""随机事件与概率：9:16 Manim 教学场景。

渲染：manim -pql probability.py ProbabilityScene
课程中的数值示例由下方纯数学函数校验；旧 MP4 不由脚本自动覆盖。
"""

from manim import *
from probability_math import union_probability, complement_probability

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
CARD = "#16213e"
BLUE = "#3498db"
ORANGE = "#e67e22"
PURPLE = "#9b59b6"
GREEN = "#2ecc71"
YELLOW = "#f1c40f"
RED = "#e74c3c"
FONT = "Noto Sans CJK SC"


class ProbabilityScene(Scene):
    """依次讲解随机事件、概率范围、事件运算和互补公式。"""

    def construct(self):
        self.camera.background_color = BG
        self.scene_opening()
        self.scene_random_trial()
        self.scene_prob_axis()
        self.scene_venn()
        self.scene_addition()
        self.scene_complement()
        self.scene_summary()
        self.scene_outro()

    def text(self, content, y, size=27, color=WHITE):
        return Text(content, font=FONT, font_size=size, color=color).move_to(UP * y)

    def math(self, content, y, size=32, color=WHITE):
        return MathTex(content, font_size=size, color=color).move_to(UP * y)

    def show(self, mob, duration=0.5):
        """按实际包围盒检查竖屏安全区，不让重要内容被裁切。"""
        if (mob.get_left()[0] < -4.1 or mob.get_right()[0] > 4.1
                or mob.get_bottom()[1] < -7.1 or mob.get_top()[1] > 7.1):
            raise ValueError("画面对象超出 9:16 安全区")
        self.play(FadeIn(mob), run_time=duration)
        return mob

    def page(self, heading, color=YELLOW):
        if self.mobjects:
            self.play(*[FadeOut(mob) for mob in list(self.mobjects)], run_time=0.4)
        self.show(self.text(heading, 5.9, 39, color))
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", -6.85, 18, GRAY_B), 0.2)

    def card(self, title, description, y, color=BLUE):
        panel = RoundedRectangle(
            width=7.6, height=1.65, corner_radius=0.16,
            fill_color=CARD, fill_opacity=1, stroke_color=color, stroke_width=2,
        ).move_to(UP * y)
        name = self.text(title, y + 0.36, 26, color)
        detail = self.text(description, y - 0.34, 22)
        return VGroup(panel, name, detail)

    def venn(self):
        """图形仅表示集合关系，不把示意面积当成事件概率。"""
        center = UP * 1.9
        space = RoundedRectangle(
            width=6.9, height=3.7, corner_radius=0.15,
            stroke_color=WHITE, stroke_width=2,
        ).move_to(center)
        a = Circle(radius=1.35, color=ORANGE, fill_color=ORANGE,
                   fill_opacity=0.28).move_to(center + LEFT * 0.85)
        b = Circle(radius=1.35, color=PURPLE, fill_color=PURPLE,
                   fill_opacity=0.28).move_to(center + RIGHT * 0.85)
        la = MathTex("A", color=ORANGE, font_size=32).move_to(center + LEFT * 1.35)
        lb = MathTex("B", color=PURPLE, font_size=32).move_to(center + RIGHT * 1.35)
        omega = MathTex(r"\Omega", color=WHITE, font_size=28).move_to(
            center + RIGHT * 2.95 + UP * 1.48
        )
        return VGroup(space, a, b, la, lb, omega)

    def scene_opening(self):
        self.page("随机事件与概率")
        self.show(self.text("一次抛硬币：正面还是反面？", 3.1, 29))
        self.show(Circle(radius=0.8, color=YELLOW, stroke_width=4).move_to(UP * 1.2))
        self.show(self.text("?", 1.2, 58, YELLOW))
        self.show(self.text("发生前不确定，发生后可观察", -1.0, 27, BLUE))
        self.show(self.text("用 0 到 1 之间的数描述可能性", -2.3, 25))
        self.wait(0.8)

    def scene_random_trial(self):
        self.page("三类事件", BLUE)
        self.show(self.card("随机事件", "抛一枚普通硬币，结果为正面", 3.5, BLUE))
        self.show(self.card("必然事件", "抛一次硬币，结果为正面或反面", 1.35, GREEN))
        self.show(self.card("不可能事件", "抛一次硬币，结果既是正面又是反面", -0.8, RED))
        self.show(self.text("讨论前提：普通硬币、一次抛掷、两种结果", -3.25, 21, YELLOW))
        self.wait(1)

    def scene_prob_axis(self):
        self.page("概率的范围", BLUE)
        axis = Line(LEFT * 3.1, RIGHT * 3.1, color=WHITE).move_to(UP * 2.5)
        self.show(axis)
        for p, label, color in ((0.0, "0", RED), (0.5, "0.5", BLUE), (1.0, "1", GREEN)):
            x = -3.1 + 6.2 * p
            mark = Dot([x, 2.5, 0], radius=0.09, color=color)
            number = Text(label, font=FONT, font_size=24, color=color).move_to([x, 1.9, 0])
            self.show(VGroup(mark, number), 0.25)
        self.show(self.math(r"0\leq P(A)\leq 1", 0.5, 37, YELLOW))
        self.show(self.card("0：不可能事件", "在该试验中，事件不会发生", -1.3, RED))
        self.show(self.card("1：必然事件", "在该试验中，事件一定发生", -3.35, GREEN))
        self.wait(0.9)

    def scene_venn(self):
        self.page("交集与并集", ORANGE)
        self.show(self.venn())
        self.show(self.math(r"A\cap B", -0.9, 36, YELLOW))
        self.show(self.text("交集：A、B 同时发生", -1.8, 25))
        self.show(self.math(r"A\cup B", -3.0, 36, GREEN))
        self.show(self.text("并集：A、B 至少发生一个", -3.9, 25))
        self.wait(1)

    def scene_addition(self):
        self.page("加法公式", GREEN)
        self.show(self.venn())
        self.show(self.text("分别相加时，交集被计算两次", -0.6, 23, YELLOW))
        formula = self.math(r"P(A\cup B)=P(A)+P(B)-P(A\cap B)", -2.0, 31)
        formula.scale_to_fit_width(7.6)
        self.show(formula)
        p_a, p_b, p_both = 0.5, 0.4, 0.2
        result = union_probability(p_a, p_b, p_both)
        self.show(self.math(r"0.5+0.4-0.2=" + f"{result:.1f}", -3.35, 36, GREEN))
        self.show(self.text("互斥时，交集概率为 0", -4.55, 22, YELLOW))
        self.wait(1)

    def scene_complement(self):
        self.page("互补公式", GREEN)
        self.show(self.text("等可能的 10 个结果：6 个属于 A", 3.8, 25))
        cells = VGroup()
        for index in range(10):
            square = RoundedRectangle(
                width=1.02, height=0.95, corner_radius=0.08,
                fill_color=ORANGE if index < 6 else PURPLE,
                fill_opacity=0.78, stroke_color=WHITE, stroke_width=1,
            )
            label = MathTex("A" if index < 6 else r"\bar A", font_size=26)
            cells.add(VGroup(square, label))
        cells.arrange_in_grid(rows=2, cols=5, buff=0.12).move_to(UP * 1.85)
        self.show(cells, 0.9)
        self.show(self.math(r"P(A)=\frac{6}{10}=0.6", -0.05, 33, ORANGE))
        self.show(self.math(r"P(\bar A)=\frac{4}{10}=" + f"{complement_probability(0.6):.1f}", -1.25, 33, PURPLE))
        self.show(self.math(r"P(A)+P(\bar A)=1", -2.75, 35, YELLOW))
        self.show(self.math(r"P(\bar A)=1-P(A)", -4.0, 34, GREEN))
        self.wait(1)

    def scene_summary(self):
        self.page("核心结论", YELLOW)
        lines = (
            (r"0\leq P(A)\leq 1", BLUE),
            (r"P(\Omega)=1,\quad P(\varnothing)=0", GREEN),
            (r"P(A\cup B)=P(A)+P(B)-P(A\cap B)", ORANGE),
            (r"P(\bar A)=1-P(A)", PURPLE),
        )
        for index, (formula, color) in enumerate(lines):
            item = self.math(formula, 3.7 - index * 2.15, 31, color)
            item.scale_to_fit_width(7.6)
            self.show(item, 0.45)
        self.wait(1.2)

    def scene_outro(self):
        self.page("随机有规律，概率可计算", YELLOW)
        self.show(self.text("先明确样本空间，再判断事件关系", 1.7, 27))
        self.show(self.text("关注我，继续学习数学！", -0.5, 29, GREEN))
        self.wait(0.8)
