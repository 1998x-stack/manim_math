"""高一·集合间的关系：子集、真子集、相等、空集与有限子集计数。"""

from itertools import combinations
from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

A_MEMBERS = (1, 2, 3)
B_MEMBERS = (1, 2, 3, 4, 5)


class SetRelationsAnimation(Scene):
    A_COLOR = "#3498db"
    B_COLOR = "#e74c3c"
    GOOD_COLOR = "#2ecc71"
    CENTER_A = np.array([-0.5, 2.0, 0.0])
    CENTER_B = np.array([0.0, 2.0, 0.0])
    RADIUS_A = 1.2
    RADIUS_B = 2.0

    def fit_width(self, mob, width=7.5):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, words):
        title = self.fit_width(Text(words, font_size=37, color=YELLOW))
        title.move_to([0, 5.35, 0])
        self.play(FadeIn(title, shift=0.15 * DOWN), run_time=0.4)
        return title

    def formula(self, latex, y=-2.15, size=40):
        return self.fit_width(MathTex(latex, font_size=size)).move_to([0, y, 0])

    def note(self, words, y=-4.25):
        return self.fit_width(Text(words, font_size=26, color=GRAY_A)).move_to([0, y, 0])

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = self.fit_width(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=20, color=GRAY_B)
        ).move_to([0, 6.85, 0])
        self.add(author)
        self.scene_1_opening()
        self.scene_2_subset()
        self.scene_3_proper_subset()
        self.scene_4_set_equality()
        self.scene_5_empty_set()
        self.scene_6_subset_count()
        self.scene_7_proper_subset_count()
        self.scene_8_outro()
        self.play(FadeOut(author), run_time=0.4)

    def point_with_label(self, value, point, color):
        dot = Dot(point, radius=0.22, color=color)
        label = MathTex(str(value), font_size=27, color=WHITE).move_to(point)
        return VGroup(dot, label)

    def subset_diagram(self):
        """圆心距 0.5 加小圆半径 1.2 小于大圆半径 2.0。"""
        circle_b = Circle(radius=self.RADIUS_B, color=self.B_COLOR).move_to(self.CENTER_B)
        circle_a = Circle(radius=self.RADIUS_A, color=self.A_COLOR).move_to(self.CENTER_A)
        label_a = MathTex("A", font_size=36, color=self.A_COLOR).move_to([-1.1, 3.35, 0])
        label_b = MathTex("B", font_size=36, color=self.B_COLOR).move_to([2.25, 3.7, 0])
        points_a = VGroup()
        for i, value in enumerate(A_MEMBERS):
            theta = -PI / 2 + i * TAU / len(A_MEMBERS)
            point = self.CENTER_A + np.array([0.63 * np.cos(theta), 0.63 * np.sin(theta), 0])
            points_a.add(self.point_with_label(value, point, self.A_COLOR))
        points_b_extra = VGroup(
            self.point_with_label(4, [1.2, 2.55, 0], self.B_COLOR),
            self.point_with_label(5, [1.2, 1.45, 0], self.B_COLOR),
        )
        diagram = VGroup(circle_b, circle_a, label_a, label_b, points_a, points_b_extra)
        return diagram, points_b_extra

    def scene_1_opening(self):
        title = self.heading("两个集合之间有什么关系？")
        example = self.formula(r"A=\{1,2,3\},\quad B=\{1,2,3,4,5\}", y=0, size=36)
        question = self.note("A 的所有元素都在 B 中吗？", y=-2.1)
        self.play(Write(example), FadeIn(question), run_time=1.0)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(example), FadeOut(question), run_time=0.45)

    def scene_2_subset(self):
        title = self.heading("子集：A 的每个元素都属于 B")
        self.diagram, self.extra_points = self.subset_diagram()
        formula = self.formula(r"A\subseteq B")
        example = self.note("A={1,2,3}，B={1,2,3,4,5}")
        self.play(FadeIn(self.diagram), run_time=0.9)
        self.play(Write(formula), FadeIn(example), run_time=0.8)
        self.wait(0.65)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(example), run_time=0.45)

    def scene_3_proper_subset(self):
        title = self.heading("真子集：A 包含于 B，且 A 不等于 B")
        formula = self.formula(r"A\subsetneq B\qquad(A\subseteq B,\ A\ne B)", size=36)
        explanation = self.note("B 还有元素 4、5，而 A 没有")
        self.play(
            Indicate(self.extra_points, color=YELLOW),
            Write(formula), FadeIn(explanation), run_time=0.9,
        )
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))
        self.play(FadeOut(self.diagram), run_time=0.5)

    def scene_4_set_equality(self):
        title = self.heading("集合相等：必须双向包含")
        # 使用新的 C、D：不把前两镜中含 4、5 的 B 突然说成与 A 相等。
        center = np.array([0, 2, 0])
        circle_c = Circle(radius=1.7, color=self.A_COLOR).move_to(center)
        circle_d = Circle(radius=1.7, color=self.B_COLOR).move_to(center)
        labels = VGroup(
            MathTex("C", color=self.A_COLOR).move_to([-2.0, 3.7, 0]),
            MathTex("D", color=self.B_COLOR).move_to([2.0, 3.7, 0]),
        )
        dots = VGroup(*[
            self.point_with_label(value, center + 0.75 * np.array([
                np.cos(-PI / 2 + i * TAU / 3), np.sin(-PI / 2 + i * TAU / 3), 0
            ]), self.GOOD_COLOR)
            for i, value in enumerate(A_MEMBERS)
        ])
        diagram = VGroup(circle_c, circle_d, labels, dots)
        members = self.formula(r"C=\{1,2,3\},\quad D=\{3,2,1\}", y=-1.5, size=35)
        relation = self.formula(r"C\subseteq D,\quad D\subseteq C\ \Longrightarrow\ C=D", y=-2.8, size=34)
        explanation = self.note("相同的元素组成相同的集合")
        self.play(FadeIn(diagram), run_time=0.7)
        self.play(Write(members), Write(relation), FadeIn(explanation), run_time=1.15)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(diagram), FadeOut(members),
                  FadeOut(relation), FadeOut(explanation), run_time=0.55)

    def scene_5_empty_set(self):
        title = self.heading("空集：没有任何元素的集合")
        circle = Circle(radius=1.7, color=self.A_COLOR).move_to([0, 2, 0])
        label = MathTex(r"A=\{1,2,3\}", font_size=33, color=self.A_COLOR).move_to([0, 4.15, 0])
        points = VGroup(*[
            self.point_with_label(value, [-0.85 + 0.85 * i, 2, 0], self.A_COLOR)
            for i, value in enumerate(A_MEMBERS)
        ])
        formula_1 = self.formula(r"\emptyset\subseteq A", y=-1.7)
        formula_2 = self.formula(r"A\ne\emptyset\ \Longrightarrow\ \emptyset\subsetneq A", y=-2.8, size=35)
        explanation = self.note("空集是所有集合的子集；是非空集合的真子集")
        diagram = VGroup(circle, label, points)
        self.play(FadeIn(diagram), Write(formula_1), run_time=0.8)
        self.play(Write(formula_2), FadeIn(explanation), run_time=0.8)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(diagram), FadeOut(formula_1),
                  FadeOut(formula_2), FadeOut(explanation), run_time=0.5)

    def build_subset_cards(self):
        """屏上八个真子集候选，与统一的组合数据一一对应。"""
        members = tuple(A_MEMBERS)
        subsets = [subset for count in range(len(members) + 1)
                   for subset in combinations(members, count)]
        cards = VGroup()
        for i, subset in enumerate(subsets):
            content = ",".join(map(str, subset))
            latex = r"\emptyset" if not subset else r"\{" + content + r"\}"
            card = self.fit_width(MathTex(latex, font_size=32), width=1.65)
            card.move_to([-2.7 + (i % 4) * 1.8, 1.9 - (i // 4) * 1.5, 0])
            cards.add(card)
        return cards

    def scene_6_subset_count(self):
        title = self.heading("有 n 个元素的集合，有多少个子集？")
        self.subset_cards = self.build_subset_cards()
        members = self.formula(r"A=\{1,2,3\},\qquad n=3", y=3.55, size=34)
        formula = self.formula(r"2^3=8\qquad\Longrightarrow\qquad 2^n", y=-2.2)
        explanation = self.note("每个元素独立选择：选入或不选入")
        self.play(Write(members), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(card) for card in self.subset_cards], lag_ratio=0.1),
                  run_time=1.2)
        self.play(Write(formula), FadeIn(explanation), run_time=0.75)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(members), FadeOut(formula),
                  FadeOut(explanation), run_time=0.5)

    def scene_7_proper_subset_count(self):
        title = self.heading("真子集比全部子集少 1 个")
        # 枚举顺序最后一项恰为 A 本身；从原有卡片中排除同一屏幕对象。
        whole_set = self.subset_cards[-1]
        self.play(Indicate(whole_set, color=RED), run_time=0.55)
        self.play(FadeOut(whole_set), run_time=0.5)
        formula = self.formula(r"2^3-1=7\qquad\Longrightarrow\qquad 2^n-1")
        explanation = self.note("被去掉的正是 A 自己；n=0 时真子集个数为 0")
        self.play(Write(formula), FadeIn(explanation), run_time=0.8)
        self.wait(0.7)
        # whole_set 已经被移出场景，只清除剩余七个当前显示的卡片。
        self.play(FadeOut(VGroup(*self.subset_cards[:-1])), FadeOut(title),
                  FadeOut(formula), FadeOut(explanation), run_time=0.55)

    def scene_8_outro(self):
        title = self.heading("集合间关系小结")
        summary = VGroup(
            self.formula(r"A\subseteq B,\qquad A\subsetneq B", y=0, size=34),
            self.formula(r"\emptyset\subseteq A", y=0),
            self.formula(r"C\subseteq D,\ D\subseteq C\iff C=D", y=0, size=33),
            self.formula(r"\#\mathcal P(A)=2^n,\quad\#\{X\mid X\subsetneq A\}=2^n-1", y=0, size=30),
        ).arrange(DOWN, buff=0.75).move_to([0, 0, 0])
        self.play(LaggedStart(*[FadeIn(line) for line in summary], lag_ratio=0.15))
        self.wait(1.3)
        self.play(FadeOut(title), FadeOut(summary), run_time=0.55)
