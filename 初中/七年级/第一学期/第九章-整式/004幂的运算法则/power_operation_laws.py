"""幂的运算法则：七年级竖屏教学动画。

Scene 入口沿用 PowerOperationLaws；数学例题与可见因子数量保持一致。
使用：manim power_operation_laws.py PowerOperationLaws
注意：本文件不执行渲染，也不会修改已有视频或音轨。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
ACCENT = "#3498db"
FACTOR = "#e74c3c"
EXPONENT = "#2ecc71"
SAFE_WIDTH = 7.5


class PowerOperationLaws(Scene):
    """用可见的因子展开和反例条件说明四条幂的运算法则。"""

    def fit(self, mob, width=SAFE_WIDTH):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, message):
        return self.fit(Text(message, font_size=38, color=ACCENT)).move_to(UP * 5.5)

    def equation(self, tex, y=2.9, size=46, color=WHITE):
        return self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)

    def note(self, message, y, color=YELLOW):
        return self.fit(Text(message, font_size=26, color=color)).move_to(UP * y)

    def clear_content(self):
        """仅淡出真正位于 Scene 内的对象，持续保留顶部作者标识。"""
        visible = [mob for mob in tuple(self.mobjects) if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_info)
        self.show_opening()
        self.show_law_1_same_base_multiply()
        self.show_law_2_power_of_power()
        self.show_law_3_product_power()
        self.show_law_4_same_base_divide()
        self.show_summary()
        self.show_outro()

    def show_opening(self):
        title = self.heading("四种幂的运算，分清指数")
        question = self.equation(r"2^3\cdot 2^5 = \, ?", y=2)
        hint = self.note("每条法则都有适用条件", -0.5)
        self.play(Write(title), Write(question), run_time=1)
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1)
        self.clear_content()

    def show_law_1_same_base_multiply(self):
        title = self.heading("法则一：同底数幂相乘")
        formula = self.equation(r"a^m\cdot a^n=a^{m+n}")
        assumption = self.note("m、n 为非负整数；底数相同", 1.5, GRAY_A)
        rule = self.note("底数不变，指数相加", 0.4)
        example = self.equation(r"2^3\cdot 2^5=2^{3+5}=2^8", y=-1.2, size=39)
        # 八个真实显示的因子，而非只用一句文字声称有八个。
        factors = VGroup(*[MathTex("2", font_size=37, color=FACTOR) for _ in range(8)])
        factors.arrange(RIGHT, buff=0.29).move_to(DOWN * 3.0)
        explanation = self.note("左边 3 个，右边 5 个：一共 8 个因子", -4.55)
        self.play(Write(title), Write(formula), run_time=1)
        self.play(FadeIn(assumption), FadeIn(rule), run_time=0.65)
        self.play(Write(example), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(factor) for factor in factors], lag_ratio=0.08), run_time=1)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.1)
        self.clear_content()

    def show_law_2_power_of_power(self):
        title = self.heading("法则二：幂的乘方")
        formula = self.equation(r"(a^m)^n=a^{mn}")
        assumption = self.note("m、n 为非负整数", 1.5, GRAY_A)
        rule = self.note("底数不变，指数相乘", 0.4)
        example = self.equation(r"(2^3)^2=2^{3\cdot2}=2^6", y=-1.2, size=40)
        rows = VGroup(
            MathTex(r"2\cdot2\cdot2", font_size=39, color=FACTOR),
            MathTex(r"2\cdot2\cdot2", font_size=39, color=FACTOR),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 3.05)
        explanation = self.note("每组 3 个，共 2 组，指数为 6", -4.65)
        self.play(Write(title), Write(formula), run_time=1)
        self.play(FadeIn(assumption), FadeIn(rule), run_time=0.6)
        self.play(Write(example), run_time=0.8)
        for row in rows:
            self.play(Write(row), run_time=0.55)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.1)
        self.clear_content()

    def show_law_3_product_power(self):
        title = self.heading("法则三：积的乘方")
        formula = self.equation(r"(ab)^n=a^nb^n")
        assumption = self.note("n 为非负整数", 1.5, GRAY_A)
        rule = self.note("每个因数分别乘方，再相乘", 0.4)
        example = self.equation(r"(2\cdot3)^2=2^2\cdot3^2", y=-1.2, size=40)
        expanded = self.equation(
            r"(2\cdot3)(2\cdot3)=(2\cdot2)(3\cdot3)", y=-2.9, size=35
        )
        result = self.equation(r"=4\cdot9=36", y=-4.5, size=39, color=EXPONENT)
        self.play(Write(title), Write(formula), run_time=1)
        self.play(FadeIn(assumption), FadeIn(rule), run_time=0.6)
        self.play(Write(example), run_time=0.8)
        self.play(Write(expanded), run_time=0.9)
        self.play(Write(result), run_time=0.65)
        self.wait(1.4)
        self.clear_content()

    def show_law_4_same_base_divide(self):
        title = self.heading("法则四：同底数幂相除")
        formula = self.equation(r"\frac{a^m}{a^n}=a^{m-n}", y=3.2)
        condition = self.note("a ≠ 0；本课约分演示取 m ≥ n ≥ 0", 1.65, GRAY_A)
        rule = self.note("底数不变，指数相减", 0.4)
        example = self.equation(r"\frac{2^5}{2^3}=2^{5-3}=2^2=4", y=-1.0, size=39)
        expanded = self.equation(
            r"\frac{2\cdot2\cdot2\cdot2\cdot2}{2\cdot2\cdot2}", y=-2.7, size=42
        )
        remainder = self.equation(r"=2\cdot2=4", y=-4.45, size=39, color=EXPONENT)
        footnote = self.note("分母非零，约去三对因子后剩两对中的两个", -5.75, GRAY_A)
        self.play(Write(title), Write(formula), run_time=1)
        self.play(FadeIn(condition), FadeIn(rule), run_time=0.6)
        self.play(Write(example), run_time=0.8)
        self.play(Write(expanded), run_time=0.8)
        self.play(Write(remainder), FadeIn(footnote), run_time=0.75)
        self.wait(1.2)
        self.clear_content()

    def create_law_card(self, heading, formula_tex, description, color, y):
        number = Text(heading, font_size=23, color=color)
        formula = self.fit(MathTex(formula_tex, font_size=29), width=6.8)
        note = self.fit(Text(description, font_size=18, color=GRAY_A), width=6.8)
        content = VGroup(number, formula, note).arrange(DOWN, buff=0.08)
        box = RoundedRectangle(width=7.7, height=1.62, corner_radius=0.13,
                               stroke_color=color, stroke_width=2)
        return VGroup(box, content).move_to(UP * y)

    def show_summary(self):
        title = self.heading("四条法则：运算对象不同")
        cards = VGroup(
            self.create_law_card("同底数幂相乘", r"a^m\cdot a^n=a^{m+n}", "底数不变，指数相加", ACCENT, 3.55),
            self.create_law_card("幂的乘方", r"(a^m)^n=a^{mn}", "底数不变，指数相乘", EXPONENT, 1.65),
            self.create_law_card("积的乘方", r"(ab)^n=a^nb^n", "每个因数分别乘方", YELLOW, -0.25),
            self.create_law_card("同底数幂相除", r"\frac{a^m}{a^n}=a^{m-n}", "a ≠ 0；指数相减", FACTOR, -2.15),
        )
        reminder = self.note("乘除法不要与幂的乘方混淆", -4.35)
        self.play(Write(title), run_time=0.6)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(reminder), run_time=0.5)
        self.wait(1.3)
        self.clear_content()

    def show_outro(self):
        title = self.heading("运算之前，先看底数与指数")
        formula = self.equation(r"2^3\cdot2^5=2^8", y=2, color=EXPONENT)
        reminder = self.note("同底数相乘，指数相加", -0.4)
        self.play(Write(title), Write(formula), FadeIn(reminder), run_time=1)
        self.wait(1.1)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.65)
