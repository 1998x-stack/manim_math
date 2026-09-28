"""高一·集合的概念与表示：竖屏 Manim 教学场景。

画面中的集合始终为 A={1,2,3,4,5}；保持入口 SetsConceptAnimation。
中文使用 Text，数学公式使用 MathTex；旧视频及音轨不由此脚本修改。
"""

from manim import *
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

DISPLAYED_ELEMENTS = (1, 2, 3, 4, 5)


class SetsConceptAnimation(Scene):
    BLUE_SET = "#3498db"
    RED_ELEMENT = "#e74c3c"
    GREEN_OK = "#2ecc71"

    def fit_width(self, mob, width=7.4):
        """按实际对象宽度收缩，避免竖屏长公式横向裁切。"""
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, words):
        item = self.fit_width(Text(words, font_size=38, color=YELLOW))
        item.move_to([0, 5.25, 0])
        self.play(FadeIn(item, shift=0.15 * DOWN), run_time=0.45)
        return item

    def note(self, words):
        return self.fit_width(Text(words, font_size=27, color=GRAY_A)).move_to(
            [0, -4.3, 0]
        )

    def formula(self, latex, font_size=43):
        return self.fit_width(MathTex(latex, font_size=font_size)).move_to(
            [0, -2.1, 0]
        )

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = self.fit_width(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=20, color=GRAY_B)
        ).move_to([0, 6.85, 0])
        self.add(author)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_properties()
        self.scene_4_membership()
        self.scene_5_roster_notation()
        self.scene_6_set_builder_notation()
        self.scene_7_outro()
        self.play(FadeOut(author), run_time=0.4)

    def scene_1_opening(self):
        title = self.heading("哪些对象可以构成一个集合？")
        question = self.fit_width(
            Text("1、2、3、4、5 有什么共同点？", font_size=31, color=WHITE)
        ).move_to([0, 1, 0])
        example = self.formula(r"A=\{1,2,3,4,5\}")
        self.play(FadeIn(question), Write(example), run_time=1.0)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(question), FadeOut(example), run_time=0.45)

    def scene_2_definition(self):
        title = self.heading("集合：由确定对象组成的整体")
        self.set_circle = Circle(
            radius=1.8, color=self.BLUE_SET, stroke_width=4
        ).move_to([0, 1, 0])
        self.set_label = MathTex("A", color=self.BLUE_SET, font_size=46).next_to(
            self.set_circle, UP, buff=0.2
        )
        self.element_dots = VGroup()
        self.element_labels = VGroup()
        for i, element in enumerate(DISPLAYED_ELEMENTS):
            angle = -PI / 2 + i * TAU / len(DISPLAYED_ELEMENTS)
            position = np.array([1.08 * np.cos(angle), 1 + 1.08 * np.sin(angle), 0])
            self.element_dots.add(Dot(position, radius=0.26, color=self.RED_ELEMENT))
            self.element_labels.add(
                MathTex(str(element), font_size=33, color=WHITE).move_to(position)
            )
        definition = self.note("圈内的 1、2、3、4、5 是集合 A 的元素")
        self.play(Create(self.set_circle), Write(self.set_label), run_time=0.8)
        self.play(
            *[FadeIn(dot) for dot in self.element_dots],
            *[FadeIn(label) for label in self.element_labels],
            FadeIn(definition),
            run_time=0.9,
        )
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(definition), run_time=0.4)

    def scene_3_properties(self):
        title = self.heading("特性一：确定性")
        formula = self.formula(r"3\in A,\qquad 6\notin A")
        explanation = self.note("任意对象，要么属于 A，要么不属于 A")
        self.play(Write(formula), FadeIn(explanation), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))

        title = self.heading("特性二：互异性")
        formula = self.formula(r"\{1,2,2,3,4,5\}=\{1,2,3,4,5\}", 37)
        explanation = self.note("重复写同一个元素，不会增加新元素")
        self.play(Write(formula), FadeIn(explanation), run_time=0.9)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))

        title = self.heading("特性三：无序性")
        formula = self.formula(r"\{1,2,3,4,5\}=\{5,3,1,4,2\}", 38)
        explanation = self.note("交换元素的书写顺序，集合不变")
        self.play(Write(formula), FadeIn(explanation), run_time=0.9)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))

    def scene_4_membership(self):
        title = self.heading("元素与集合：属于、不属于")
        formula = self.formula(r"3\in A")
        explanation = self.note("3 在集合 A 中")
        self.play(Indicate(self.element_labels[2]), Write(formula), FadeIn(explanation))
        self.wait(0.5)
        next_formula = self.formula(r"6\notin A")
        next_explanation = self.note("6 不在集合 A 中")
        dot_6 = Dot([2.85, 1, 0], radius=0.26, color=ORANGE)
        label_6 = MathTex("6", font_size=33, color=WHITE).move_to(dot_6)
        self.play(
            ReplacementTransform(formula, next_formula),
            ReplacementTransform(explanation, next_explanation),
            FadeIn(dot_6), FadeIn(label_6), run_time=0.85,
        )
        self.wait(0.6)
        self.play(
            FadeOut(title), FadeOut(next_formula), FadeOut(next_explanation),
            FadeOut(dot_6), FadeOut(label_6), run_time=0.45,
        )

    def scene_5_roster_notation(self):
        title = self.heading("列举法：逐一写出所有元素")
        formula = self.formula(r"A=\{1,2,3,4,5\}")
        explanation = self.note("花括号内的每个数字，对应圈内一个元素")
        self.play(Write(formula), FadeIn(explanation), run_time=0.9)
        for label in self.element_labels:
            self.play(Indicate(label, color=YELLOW), run_time=0.32)
        self.wait(0.4)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))

    def scene_6_set_builder_notation(self):
        title = self.heading("描述法：说明元素的共同特征")
        formula = self.formula(r"A=\{x\in\mathbb{Z}\mid 1\leq x\leq 5\}", 39)
        explanation = self.note("x 是整数，且从 1 到 5（包含两端）")
        self.play(Write(formula), FadeIn(explanation), run_time=1.1)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(explanation))
        self.play(
            FadeOut(self.set_circle), FadeOut(self.set_label),
            FadeOut(self.element_dots), FadeOut(self.element_labels), run_time=0.55,
        )

    def scene_7_outro(self):
        title = self.heading("集合知识小结")
        lines = VGroup(
            Text("确定性 · 互异性 · 无序性", font_size=32, color=WHITE),
            self.fit_width(MathTex(r"3\in A,\quad 6\notin A", font_size=42)),
            self.fit_width(MathTex(r"A=\{1,2,3,4,5\}", font_size=42)),
            self.fit_width(MathTex(r"A=\{x\in\mathbb{Z}\mid 1\leq x\leq5\}", font_size=37)),
        ).arrange(DOWN, buff=0.85).move_to([0, 0, 0])
        self.play(LaggedStart(*[FadeIn(line) for line in lines], lag_ratio=0.22))
        self.wait(1.3)
        self.play(FadeOut(title), FadeOut(lines), run_time=0.6)
