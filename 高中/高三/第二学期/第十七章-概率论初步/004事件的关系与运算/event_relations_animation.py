"""事件的关系与运算：用同一个六面骰子样本空间核对各镜数据。

预览：manim -pql event_relations_animation.py EventRelations
数学回归：python -m unittest -v test_event_relations_math.py
"""
from manim import *
from event_relations_math import (A, B, OMEGA, complement, complementary,
                                  event, intersection, mutually_exclusive,
                                  probability, union)

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
PURPLE = "#bb8fce"


class EventRelations(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.scene_1_opening()
        self.scene_2_sample_space()
        self.scene_3_containment()
        self.scene_4_union()
        self.scene_5_intersection()
        self.scene_6_exclusive_and_complementary()
        self.scene_7_summary()

    def fit(self, mob):
        """限制单对象安全区；成片仍需检查文字与图形互相遮挡。"""
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

    def show(self, mob, duration=0.45):
        self.play(FadeIn(self.fit(mob)), run_time=duration)
        return mob

    def text(self, caption, y, size=28, color=WHITE):
        return Text(caption, font=FONT, font_size=size, color=color).move_to(UP * y)

    def math(self, formula, y, size=35, color=WHITE):
        return MathTex(formula, font_size=size, color=color).move_to(UP * y)

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.3, 37, color), 0.4)

    def dice_space(self, shaded=None):
        """同一组六个基本事件，集合运算结果与高亮数字一一对应。"""
        shaded = frozenset() if shaded is None else event(shaded)
        cells = VGroup()
        for n in sorted(OMEGA):
            color = GOLD if n in shaded else CARD
            square = RoundedRectangle(
                width=0.8, height=0.8, corner_radius=0.1,
                stroke_color=WHITE if n in shaded else GRAY_B,
                stroke_width=1.5, fill_color=color, fill_opacity=0.95,
            )
            number = MathTex(str(n), font_size=29, color=BG if n in shaded else WHITE)
            cells.add(VGroup(square, number))
        return cells.arrange(RIGHT, buff=0.12)

    def venn(self, highlighted=None):
        """A、B 与 Ω 的六个事件标识和几何位置同时可见。"""
        highlighted = frozenset() if highlighted is None else event(highlighted)
        space = RoundedRectangle(width=7.3, height=4.7, corner_radius=0.17,
                                 stroke_color=GRAY_B, stroke_width=2,
                                 fill_color=CARD, fill_opacity=0.35)
        ca = Circle(radius=1.45, stroke_color=RED, fill_color=RED,
                    fill_opacity=0.13).move_to(LEFT * 0.8)
        cb = Circle(radius=1.45, stroke_color=BLUE, fill_color=BLUE,
                    fill_opacity=0.13).move_to(RIGHT * 0.8)
        members = VGroup()
        positions = {1: (-1.65, 0.5), 2: (1.65, 0.5), 3: (0, 1.1),
                     4: (-2.65, -1.05), 5: (0, 0.2), 6: (2.65, -1.05)}
        for n in sorted(OMEGA):
            x, y = positions[n]
            base_color = PURPLE if n in intersection(A, B) else (RED if n in A else (BLUE if n in B else GRAY_B))
            label = MathTex(str(n), font_size=34, color=GOLD if n in highlighted else base_color)
            label.move_to([x, y, 0])
            members.add(label)
        geom = VGroup(space, ca, cb, members, self.math(r"\Omega", 1.93, 25, GRAY_B))
        return geom.move_to(UP * 0.7)

    def scene_1_opening(self):
        self.page("事件的关系与运算")
        self.show(self.text("掷一枚公平骰子：样本空间", 3.8, 28))
        self.show(self.dice_space().move_to(UP * 2.3))
        self.show(self.text("A = 奇数：{1,3,5}", 0.8, 29, RED))
        self.show(self.text("B = 质数：{2,3,5}", -0.3, 29, BLUE))
        self.show(self.text("3 和 5 属于两个事件：如何描述？", -2, 27, GOLD))
        self.wait(0.8)

    def scene_2_sample_space(self):
        self.page("样本空间与韦恩图")
        self.show(self.venn(), 0.8)
        self.show(self.text("矩形表示 Ω={1,2,3,4,5,6}", -2.7, 26))
        self.show(self.text("重叠区域是两个事件共同的结果：3、5", -3.85, 24, PURPLE))
        self.wait(0.8)

    def scene_3_containment(self):
        self.page("包含关系：A ⊆ B", BLUE)
        self.show(self.text("此处重新定义 A={3}，B={2,3,5}", 4.0, 25))
        space = RoundedRectangle(width=6.5, height=4.0, corner_radius=0.15,
                                 stroke_color=GRAY_B)
        big = Circle(radius=1.45, stroke_color=BLUE,
                     fill_color=BLUE, fill_opacity=0.25)
        small = Circle(radius=0.65, stroke_color=RED,
                       fill_color=RED, fill_opacity=0.35).shift(LEFT * 0.35)
        assert 0.35 + 0.65 < 1.45
        diagram = VGroup(space, big, small,
                         MathTex("B", color=BLUE).move_to(RIGHT * 0.85),
                         MathTex("A", color=RED).move_to(LEFT * 0.4)).move_to(UP * 1.0)
        self.show(diagram)
        self.show(self.math(r"A\subseteq B\ \Rightarrow\ P(A)\leq P(B)", -2.25, 34, GOLD))
        assert event((3,)) <= B and probability((3,)) <= probability(B)
        self.show(self.text("A 发生时，B 必然发生；反过来未必", -3.65, 25))
        self.wait(0.8)

    def scene_4_union(self):
        self.page("并事件：A ∪ B", GREEN)
        hit = union(A, B)
        assert hit == frozenset((1, 2, 3, 5))
        self.show(self.venn(hit), 0.7)
        self.show(self.text("至少一个事件发生：{1,2,3,5}", -2.5, 26, GREEN))
        self.show(self.math(r"P(A\cup B)=P(A)+P(B)-P(A\cap B)", -3.8, 30, GOLD))
        self.show(self.math(r"\frac36+\frac36-\frac26=\frac46", -5.0, 33, GREEN))
        self.wait(0.8)

    def scene_5_intersection(self):
        self.page("交事件：A ∩ B", PURPLE)
        hit = intersection(A, B)
        assert hit == frozenset((3, 5))
        self.show(self.venn(hit), 0.7)
        self.show(self.text("A 和 B 同时发生：{3,5}", -2.55, 26, PURPLE))
        self.show(self.math(r"P(A\cap B)=\frac26=\frac13", -3.8, 35, GOLD))
        self.show(self.math(r"P(A\cap B)\leq\min\{P(A),P(B)\}", -5.0, 31))
        self.wait(0.8)

    def scene_6_exclusive_and_complementary(self):
        self.page("互斥 ≠ 对立", GREEN)
        odd_single = event((1,))
        even = event((2, 4, 6))
        assert mutually_exclusive(odd_single, even) and not complementary(odd_single, even)
        self.show(self.text("互斥示例：A={1}，B={2,4,6}", 3.85, 26))
        self.show(self.dice_space(odd_single | even).move_to(UP * 2.35))
        self.show(self.math(r"A\cap B=\varnothing", 0.95, 36, GREEN))
        self.show(self.text("3、5 不属于 A∪B：互斥不代表覆盖全集", -0.1, 24))
        self.show(self.text("对立示例：A={1,3,5}，补集={2,4,6}", -1.4, 25, GOLD))
        assert complementary(A, complement(A))
        self.show(self.math(r"A\cap\bar A=\varnothing,\quad A\cup\bar A=\Omega",
                            -2.7, 30, BLUE))
        self.show(self.math(r"P(\bar A)=1-P(A)", -4.1, 35, GOLD))
        self.wait(1)

    def scene_7_summary(self):
        self.page("知识点总结")
        self.show(self.text("包含：A ⊆ B 时 P(A) ≤ P(B)", 3.8, 28, BLUE))
        self.show(self.text("并集：至少一个发生；交集：同时发生", 2.55, 27))
        self.show(self.text("互斥：没有交集；对立：互斥且并集为全集", 1.3, 25, GOLD))
        self.show(self.math(r"P(A\cup B)=P(A)+P(B)-P(A\cap B)", -0.2, 30, GREEN))
        self.show(self.math(r"P(A)+P(\bar A)=1", -1.65, 35, PURPLE))
        self.show(self.text("@emptyandcalm", -3.6, 28, GRAY_B))
        self.wait(1.2)
