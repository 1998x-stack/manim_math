"""六年级下 · 有理数的概念（竖屏 9:16）。

保持原来的 Manim 入口 RationalNumbers；音频和已发布视频不在本文件中处理。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class RationalNumbers(Scene):
    """整数/分数定义、两种分类、数轴、小数与判断练习。"""

    def construct(self):
        self.camera.background_color = "#141827"
        self.teal = "#59DAC6"
        self.green = "#75DB9D"
        self.orange = "#FFBC70"
        self.purple = "#C7A7FF"
        self.muted = "#BFCADD"
        self.current = None
        self.brand = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=21, color=self.muted,
        ).move_to(UP * 6.7)
        self.heading = Text("有理数的概念", font_size=40, color=self.teal)
        self.heading.move_to(UP * 5.65)
        self.add(self.brand)
        self.play(Write(self.heading), run_time=0.6)
        self.show_opening()
        self.show_definition()
        self.show_classification_by_sign()
        self.show_classification_by_type()
        self.show_decimal_representation()
        self.show_practice()
        self.show_summary()

    def switch_to(self, heading, *objects):
        """退出上一镜，保持标题、品牌引用一致。"""
        if self.current is not None:
            self.play(FadeOut(self.current), run_time=0.4)
        new_heading = Text(heading, font_size=40, color=self.teal)
        new_heading.move_to(UP * 5.65)
        self.play(Transform(self.heading, new_heading), run_time=0.4)
        self.current = VGroup(*objects)

    def show_opening(self):
        prompt = Text("这些数有什么共同点？", font_size=35, color=YELLOW)
        prompt.move_to(UP * 4.5)
        values = VGroup(
            MathTex("3"), MathTex("-5"), MathTex(r"\frac{1}{2}"),
            MathTex("0"), MathTex("-2.5"), MathTex(r"0.\overline{3}"),
        )
        values.arrange_in_grid(rows=2, cols=3, buff=(0.9, 1.1))
        values.move_to(UP * 1.6)
        values.set_color(WHITE)
        clue = Text("它们都能写成两个整数的比", font_size=28, color=self.muted)
        clue.move_to(DOWN * 1.6)
        self.switch_to("有理数的概念", prompt, values, clue)
        self.play(Write(prompt), FadeIn(values, shift=UP * 0.2), run_time=1.1)
        self.play(FadeIn(clue), run_time=0.6)
        self.wait(0.8)

    def show_definition(self):
        formula = MathTex(
            r"\mathbb{Q}=\left\{\frac{p}{q}\mid p,q\in\mathbb{Z},\ q\ne0\right\}",
            font_size=37, color=self.teal,
        ).move_to(UP * 3.7)
        definition = Text("有理数：整数和分数的统称", font_size=32)
        definition.move_to(UP * 2)
        examples = VGroup(
            MathTex(r"3=\frac{3}{1}"),
            MathTex(r"-2.5=-\frac{5}{2}"),
            MathTex(r"0=\frac{0}{1}"),
        ).arrange(DOWN, buff=0.65).move_to(DOWN * 0.7)
        note = Text("分子、分母都是整数；分母不能为零", font_size=27, color=YELLOW)
        note.move_to(DOWN * 3.7)
        self.switch_to("什么是有理数？", formula, definition, examples, note)
        self.play(Write(definition), Write(formula), run_time=1.4)
        self.play(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.2) for x in examples], lag_ratio=0.2))
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1)

    def show_classification_by_sign(self):
        line = NumberLine(x_range=[-4, 4, 1], length=7.1, include_numbers=False,
                          font_size=24, include_tip=True, color=self.muted)
        line.move_to(UP * 1.2)
        # 数值与标注位置由同一份 data 驱动，避免示例值/数轴坐标错位。
        cases = [
            (-3, "-3", self.orange, UP),
            (-1, "-1", self.orange, UP),
            (0, "0", self.purple, DOWN),
            (0.5, r"\frac{1}{2}", self.green, UP),
            (3, "3", self.green, UP),
        ]
        marks = VGroup()
        for value, label, color, direction in cases:
            position = line.n2p(value)
            dot = Dot(position, radius=0.09, color=color)
            text = MathTex(label, font_size=29, color=color)
            text.move_to(position + direction * 0.75)
            marks.add(VGroup(dot, text))
        pos = Text("右侧：正有理数", font_size=29, color=self.green)
        zero = Text("原点：零（既不正也不负）", font_size=28, color=self.purple)
        neg = Text("左侧：负有理数", font_size=29, color=self.orange)
        captions = VGroup(neg, zero, pos).arrange(DOWN, buff=0.55)
        captions.move_to(DOWN * 2.1)
        self.switch_to("按符号分类", line, marks, captions)
        self.play(Create(line), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(m) for m in marks], lag_ratio=0.2), run_time=1.5)
        self.play(FadeIn(captions), run_time=0.6)
        self.wait(0.8)

    def show_classification_by_type(self):
        root = self.node("有理数", self.teal, (0, 4.4), 2.6)
        integer = self.node("整数", BLUE_C, (-2.0, 2.6), 2.1)
        fraction = self.node("分数", self.orange, (2.0, 2.6), 2.1)
        leaves = VGroup(
            self.node("正整数", self.green, (-3.3, 0.5), 1.45),
            self.node("零", self.purple, (-1.8, 0.5), 0.85),
            self.node("负整数", self.orange, (-0.3, 0.5), 1.45),
            self.node("正分数", self.green, (1.4, 0.5), 1.45),
            self.node("负分数", self.orange, (3.1, 0.5), 1.45),
        )
        branches = VGroup(
            Line(root.get_bottom(), integer.get_top(), color=self.muted),
            Line(root.get_bottom(), fraction.get_top(), color=self.muted),
        )
        branches.add(*[
            Line(integer.get_bottom() if i < 3 else fraction.get_bottom(),
                 leaf.get_top(), color=self.muted)
            for i, leaf in enumerate(leaves)
        ])
        samples = VGroup(
            MathTex("3"), MathTex("0"), MathTex("-5"),
            MathTex(r"\frac{1}{2}"), MathTex(r"-\frac{3}{4}"),
        )
        for sample, leaf in zip(samples, leaves):
            sample.set_color(WHITE).scale(0.8).next_to(leaf, DOWN, buff=0.35)
        note = Text("整数也可写成分母为 1 的分数", font_size=28, color=YELLOW)
        note.move_to(DOWN * 3.5)
        self.switch_to("按类型分类", branches, root, integer, fraction,
                       leaves, samples, note)
        self.play(FadeIn(root), Create(branches), run_time=1.0)
        self.play(FadeIn(integer), FadeIn(fraction), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(leaf) for leaf in leaves], lag_ratio=0.12))
        self.play(FadeIn(samples), FadeIn(note), run_time=0.8)
        self.wait(1)

    def node(self, label, color, xy, width):
        box = RoundedRectangle(width=width, height=0.75, corner_radius=0.13,
                               stroke_color=color, fill_color=color,
                               fill_opacity=0.16)
        box.move_to(xy[0] * RIGHT + xy[1] * UP)
        text = Text(label, font_size=24, color=WHITE).move_to(box)
        return VGroup(box, text)

    def show_decimal_representation(self):
        rows = VGroup(
            MathTex(r"\frac{1}{2}=0.5", font_size=43),
            MathTex(r"\frac{1}{4}=0.25", font_size=43),
            MathTex(r"\frac{1}{3}=0.\overline{3}", font_size=43),
        ).arrange(DOWN, buff=0.9).move_to(UP * 1.8)
        caption = Text("有理数的小数表示：有限小数或无限循环小数", font_size=25)
        caption.move_to(DOWN * 1.7)
        reverse = Text("反过来，这两类小数都能写成整数之比", font_size=26,
                       color=self.teal).move_to(DOWN * 2.7)
        counter = MathTex(r"\sqrt{2}\notin\mathbb{Q}", font_size=37,
                          color=self.orange).move_to(DOWN * 4.3)
        self.switch_to("小数表示", rows, caption, reverse, counter)
        self.play(LaggedStart(*[Write(row) for row in rows], lag_ratio=0.25))
        self.play(FadeIn(caption), FadeIn(reverse), run_time=0.7)
        self.play(FadeIn(counter), run_time=0.5)
        self.wait(0.8)

    def show_practice(self):
        question = Text("下列哪些是有理数？", font_size=31, color=YELLOW)
        question.move_to(UP * 4.7)
        values = ["7", r"-\frac{3}{5}", r"0.\overline{6}", r"\sqrt{3}"]
        rational = [True, True, True, False]
        cards = VGroup()
        badges = VGroup()
        for index, (value, is_rational) in enumerate(zip(values, rational)):
            x = -1.8 if index % 2 == 0 else 1.8
            y = 2.8 if index < 2 else 0.5
            frame = RoundedRectangle(width=3.1, height=1.8, corner_radius=0.16,
                                     stroke_color=self.muted)
            frame.move_to(x * RIGHT + y * UP)
            number = MathTex(value, font_size=39).move_to(frame.get_center() + UP * 0.23)
            verdict = Text("有理数" if is_rational else "无理数",
                           font_size=23, color=self.green if is_rational else self.orange)
            verdict.move_to(frame.get_center() + DOWN * 0.53)
            cards.add(VGroup(frame, number))
            badges.add(verdict)
        reason = MathTex(r"\sqrt{3}\notin\mathbb{Q}", font_size=39,
                         color=self.orange).move_to(DOWN * 3.1)
        self.switch_to("判断练习", question, cards, badges, reason)
        self.play(Write(question), FadeIn(cards), run_time=0.8)
        self.wait(0.6)
        self.play(LaggedStart(*[FadeIn(b) for b in badges], lag_ratio=0.25))
        self.play(FadeIn(reason), run_time=0.5)
        self.wait(1)

    def show_summary(self):
        facts = VGroup(
            Text("整数和分数统称有理数", font_size=31),
            MathTex(r"\frac{p}{q}\quad(p,q\in\mathbb{Z},\ q\ne0)", font_size=36),
            Text("按符号：正有理数、零、负有理数", font_size=28),
            Text("按类型：整数、分数", font_size=29),
            Text("小数：有限或无限循环", font_size=29),
        ).arrange(DOWN, buff=0.75).move_to(UP * 0.7)
        takeaway = Text("判断关键：能否写成两个整数的比？", font_size=28,
                        color=YELLOW).move_to(DOWN * 4)
        self.switch_to("知识要点", facts, takeaway)
        self.play(LaggedStart(*[FadeIn(f, shift=RIGHT * 0.15) for f in facts],
                              lag_ratio=0.15))
        self.play(FadeIn(takeaway), run_time=0.5)
        self.wait(1.5)
