"""七年级第一学期：同类项与合并同类项。

保留历史 Manim 场景入口 LikeTerms 与六个教学环节。
运行：manim -pql like_terms.py LikeTerms
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE_C = "#3498db"
RED_C = "#e74c3c"
GREEN_C = "#2ecc71"
PURPLE_C = "#9b59b6"
ORANGE_C = "#f39c12"


class LikeTerms(Scene):
    """同类项的定义、反例、抵消模型、综合化简。"""

    @staticmethod
    def fit(mob, width=7.5):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, label, color=WHITE):
        return self.fit(Text(label, font_size=40, color=color)).move_to(UP * 5.8)

    def note(self, label, y=-3.8, color=GRAY_A):
        return self.fit(Text(label, font_size=26, color=color)).move_to(UP * y)

    def clear_content(self):
        visible = [mob for mob in self.mobjects if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.7)
        self.add(self.author_info)
        self.show_opening()
        self.show_definition()
        self.show_examples()
        self.show_rule()
        self.show_full_example()
        self.show_outro()

    def show_opening(self):
        title = self.heading("这个式子能化简吗？", YELLOW)
        expression = self.fit(MathTex(
            r"3x^2y-5x^2y+2xy+4x^2y-xy", font_size=42
        )).move_to(UP * 1.4)
        question = self.note("先按字母及其指数分组", y=-1.2, color=BLUE_C)
        self.play(Write(title), run_time=0.65)
        self.play(Write(expression), run_time=1.3)
        self.play(FadeIn(question), run_time=0.55)
        self.wait(1)
        self.clear_content()

    def show_definition(self):
        title = self.heading("什么是同类项？", BLUE_C)
        definition = VGroup(
            self.note("所含字母相同", y=3.9),
            self.note("相同字母的指数分别相同", y=3.1),
        )
        left = MathTex("3", "x^2y", font_size=52).move_to(LEFT * 1.9 + UP * 1)
        right = MathTex("-5", "x^2y", font_size=52).move_to(RIGHT * 1.9 + UP * 1)
        # 分离传给 MathTex 的字母部分，避免依赖 TeX 字形数目的硬编码切片。
        frames = VGroup(
            SurroundingRectangle(left[1], color=PURPLE_C, buff=0.12),
            SurroundingRectangle(right[1], color=PURPLE_C, buff=0.12),
        )
        conclusion = self.note("字母部分都为 x²y，系数可以不同", y=-1.4, color=PURPLE_C)
        self.play(Write(title), FadeIn(definition), run_time=0.9)
        self.play(Write(left), Write(right), run_time=0.75)
        self.play(*[Create(frame) for frame in frames], run_time=0.55)
        self.play(FadeIn(conclusion), run_time=0.55)
        self.wait(1)
        self.clear_content()

    def show_examples(self):
        title = self.heading("正例与反例", BLUE_C)
        examples = (
            (r"3x^2y", r"-5x^2y", "同类项：系数不同不影响", GREEN_C),
            (r"2a", r"-7a", "同类项：字母、指数相同", GREEN_C),
            (r"5", r"-3", "同类项：常数项互为同类项", GREEN_C),
            (r"3x^2y", r"3xy^2", "不是同类项：对应指数不同", RED_C),
            (r"2a^2", r"2a", "不是同类项：指数 2 与 1 不同", RED_C),
        )
        self.play(Write(title), run_time=0.65)
        for idx, (left_tex, right_tex, reason, color) in enumerate(examples):
            y = 3.8 - idx * 1.95
            pair = self.fit(MathTex(
                left_tex, r"\quad\text{和}\quad", right_tex, font_size=35
            )).move_to(UP * y)
            # MathTex 不承载中文，另以图形/文字容器表达两项之间的“和”。
            pair = self.fit(VGroup(
                MathTex(left_tex, font_size=36),
                Text("与", font_size=24),
                MathTex(right_tex, font_size=36),
            ).arrange(RIGHT, buff=0.35)).move_to(UP * y)
            verdict = self.note(reason, y=y - 0.72, color=color)
            self.play(FadeIn(pair, shift=UP * 0.12), FadeIn(verdict), run_time=0.58)
        self.wait(1.2)
        self.clear_content()

    def show_rule(self):
        title = self.heading("合并同类项的法则", BLUE_C)
        rule = self.note("系数相加，字母及其指数不变", y=3.65, color=PURPLE_C)
        formula = MathTex(r"3x^2y+(-5x^2y)", font_size=46).move_to(UP * 2)
        numbers = MathTex(r"3+(-5)=-2", font_size=48, color=GREEN_C).move_to(UP * 0.35)
        # 同一类字母块分别画出三个正块和五个负块：配对抵消剩两个负块。
        def tile(color):
            square = Square(side_length=0.59, stroke_color=color,
                            fill_color=color, fill_opacity=0.25)
            symbol = MathTex(r"x^2y", font_size=16, color=color)
            return VGroup(square, symbol.move_to(square))
        positives = VGroup(*[tile(BLUE_C) for _ in range(3)]).arrange(RIGHT, buff=0.16)
        negatives = VGroup(*[tile(RED_C) for _ in range(5)]).arrange(RIGHT, buff=0.16)
        positives.move_to(DOWN * 1.3)
        negatives.move_to(DOWN * 2.4)
        result = MathTex(r"=-2x^2y", font_size=47, color=GREEN_C).move_to(DOWN * 4.25)
        conclusion = self.note("正负三个配对抵消，剩余两个负块", y=-5.4, color=YELLOW)
        self.play(Write(title), FadeIn(rule), run_time=0.8)
        self.play(Write(formula), Write(numbers), run_time=1)
        self.play(FadeIn(positives), FadeIn(negatives), run_time=0.8)
        self.play(*[FadeOut(positives[i]) for i in range(3)],
                  *[FadeOut(negatives[i]) for i in range(3)], run_time=0.9)
        self.play(Write(result), FadeIn(conclusion), run_time=0.8)
        self.wait(1)
        self.clear_content()

    def show_full_example(self):
        title = self.heading("完整例题：先分类，再相加", BLUE_C)
        original = self.fit(MathTex(
            r"3x^2y-5x^2y+2xy+4x^2y-xy", font_size=39
        )).move_to(UP * 4.05)
        # 每项是独立的 MathTex：符号随项移动，不依赖原公式的 glyph 索引。
        x2y_terms = self.fit(VGroup(*[
            MathTex(term, font_size=40, color=BLUE_C)
            for term in (r"3x^2y", r"-5x^2y", r"+4x^2y")
        ]).arrange(RIGHT, buff=0.35)).move_to(UP * 2.05)
        xy_terms = self.fit(VGroup(*[
            MathTex(term, font_size=40, color=RED_C)
            for term in (r"+2xy", r"-xy")
        ]).arrange(RIGHT, buff=0.35)).move_to(UP * 0.4)
        brackets = VGroup(
            SurroundingRectangle(x2y_terms, color=BLUE_C, buff=0.14),
            SurroundingRectangle(xy_terms, color=RED_C, buff=0.14),
        )
        coefficients = MathTex(
            r"(3-5+4)x^2y+(2-1)xy", font_size=40
        ).move_to(DOWN * 2.1)
        arithmetic = MathTex(r"2x^2y+1xy", font_size=40).move_to(DOWN * 3.3)
        answer = MathTex(r"2x^2y+xy", font_size=49, color=GREEN_C).move_to(DOWN * 4.5)
        note = self.note("只合并相同字母部分；不能把 x²y 与 xy 合并", y=-5.65, color=YELLOW)
        self.play(Write(title), Write(original), run_time=1)
        self.play(FadeIn(x2y_terms), Create(brackets[0]), run_time=0.8)
        self.play(FadeIn(xy_terms), Create(brackets[1]), run_time=0.8)
        self.play(Write(coefficients), run_time=0.85)
        self.play(Write(arithmetic), run_time=0.6)
        self.play(Write(answer), FadeIn(note), run_time=0.9)
        self.wait(1.2)
        self.clear_content()

    def show_outro(self):
        title = self.heading("记住三个要点", YELLOW)
        points = VGroup(*[
            self.fit(Text(item, font_size=31, color=color))
            for item, color in (
                ("字母相同且对应指数相同", BLUE_C),
                ("合并时系数相加", GREEN_C),
                ("字母和指数保持不变", PURPLE_C),
            )
        ]).arrange(DOWN, buff=0.8).move_to(UP * 0.65)
        answer = MathTex(r"2x^2y+xy", font_size=52, color=GREEN_C).move_to(DOWN * 3.3)
        self.play(Write(title), run_time=0.65)
        for point in points:
            self.play(FadeIn(point, shift=UP * 0.15), run_time=0.6)
        self.play(Write(answer), run_time=0.7)
        self.wait(1.5)
        self.clear_content()
        self.play(FadeOut(self.author_info), run_time=0.3)
