"""整式的乘法：用两行两列的可见乘积格解释分配律。

保留原有 PolynomialMultiplication Scene 和七镜头教学入口；不覆盖已发布视频。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE_ACCENT = "#3498db"
GREEN_ACCENT = "#2ecc71"
ORANGE_ACCENT = "#f39c12"
SAFE_WIDTH = 7.5


class PolynomialMultiplication(Scene):
    """从单项式相乘、分配律，到实际四项乘积表。"""

    def fit(self, mob, width=SAFE_WIDTH):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, message):
        return self.fit(Text(message, font_size=38, color=BLUE_ACCENT)).move_to(UP * 5.5)

    def formula(self, expression, y, size=43, color=WHITE):
        return self.fit(MathTex(expression, font_size=size, color=color)).move_to(UP * y)

    def caption(self, message, y, color=GRAY_A):
        return self.fit(Text(message, font_size=26, color=color)).move_to(UP * y)

    def clear_content(self):
        """仅清除真实在屏上的对象；保留作者标签到最后一镜。"""
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
        self.show_monomial_times_monomial()
        self.show_monomial_times_polynomial()
        self.show_polynomial_times_polynomial_intro()
        self.show_polynomial_times_polynomial_expansion()
        self.show_concrete_example()
        self.show_summary()

    def show_opening(self):
        title = self.heading("每一项，都要乘到")
        expressions = VGroup(
            MathTex(r"(2x)(3x^2)", font_size=44),
            MathTex(r"2x(3x+4)", font_size=44),
            MathTex(r"(x+2)(x+3)", font_size=44),
        ).arrange(DOWN, buff=0.8).move_to(UP * 1.2)
        self.play(Write(title), run_time=0.7)
        for expression in expressions:
            self.play(Write(expression), run_time=0.6)
        self.wait(0.8)
        self.clear_content()

    def show_monomial_times_monomial(self):
        title = self.heading("单项式 × 单项式")
        problem = self.formula(r"(2x)(3x^2)", 3.7, size=53)
        coefficient = self.formula(r"2\cdot3=6", 1.8, color=GREEN_ACCENT)
        powers = self.formula(r"x^1\cdot x^2=x^{1+2}=x^3", 0.0, size=38)
        result = self.formula(r"(2x)(3x^2)=6x^3", -2.3, color=ORANGE_ACCENT)
        note = self.caption("系数相乘；同底数幂指数相加", -4.35, YELLOW)
        self.play(Write(title), Write(problem), run_time=0.95)
        self.play(Write(coefficient), run_time=0.65)
        self.play(Write(powers), run_time=0.75)
        self.play(Write(result), run_time=0.75)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.3)
        self.clear_content()

    def show_monomial_times_polynomial(self):
        title = self.heading("单项式 × 多项式")
        formula = self.formula(r"a(b+c)=ab+ac", 3.7)
        note = self.caption("括号里的每一项都要乘到", 2.35, YELLOW)
        start = self.formula(r"2x(3x+4)", 0.5, size=48)
        first = self.formula(r"2x\cdot3x=6x^2", -1.25, color=GREEN_ACCENT)
        second = self.formula(r"2x\cdot4=8x", -2.6, color=BLUE_ACCENT)
        result = self.formula(r"2x(3x+4)=6x^2+8x", -4.6, size=38, color=ORANGE_ACCENT)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(FadeIn(note), Write(start), run_time=0.7)
        self.play(Write(first), run_time=0.6)
        self.play(Write(second), run_time=0.6)
        self.play(Write(result), run_time=0.8)
        self.wait(1.3)
        self.clear_content()

    def product_grid(self, row_terms, column_terms, products):
        """同一行/列因子生成四个独立可见结果格；不依赖 MathTex 字形索引。"""
        headers = VGroup()
        cells = VGroup()
        headers.add(MathTex(r"\times", font_size=35).move_to([-3.1, 1.05, 0]))
        centers_x = (-1.05, 1.25)
        centers_y = (-0.6, -2.05)
        for index, term in enumerate(column_terms):
            headers.add(MathTex(term, font_size=37, color=GREEN_ACCENT)
                        .move_to([centers_x[index], 1.05, 0]))
        for index, term in enumerate(row_terms):
            headers.add(MathTex(term, font_size=37, color=BLUE_ACCENT)
                        .move_to([-3.1, centers_y[index], 0]))
        for row in range(2):
            for col in range(2):
                index = 2 * row + col
                box = Rectangle(width=2.1, height=1.2, color=BLUE_ACCENT,
                                stroke_width=2, fill_color=BLUE_ACCENT,
                                fill_opacity=0.09).move_to([centers_x[col], centers_y[row], 0])
                product = self.fit(MathTex(products[index], font_size=35,
                                           color=ORANGE_ACCENT), width=1.85)
                product.move_to(box.get_center())
                cells.add(VGroup(box, product))
        return headers, cells

    def show_polynomial_times_polynomial_intro(self):
        title = self.heading("多项式 × 多项式")
        formula = self.formula(r"(a+b)(c+d)", 3.65, size=52)
        explanation = self.caption("两项 × 两项 = 四个乘积", 1.3, YELLOW)
        rule = self.formula(r"(a+b)(c+d)=ac+ad+bc+bd", -0.8, size=39)
        reminder = self.caption("不能漏项，也不能丢掉原来的正负号", -3.0)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(Write(rule), run_time=0.95)
        self.play(FadeIn(reminder), run_time=0.5)
        self.wait(1.1)
        self.clear_content()

    def show_polynomial_times_polynomial_expansion(self):
        title = self.heading("四格乘积：每行乘每列")
        problem = self.formula(r"(a+b)(c+d)", 3.75, size=48)
        headers, cells = self.product_grid(("a", "b"), ("c", "d"),
                                           ("ac", "ad", "bc", "bd"))
        result = self.formula(r"=ac+ad+bc+bd", -4.15, size=41, color=ORANGE_ACCENT)
        self.play(Write(title), Write(problem), run_time=0.85)
        self.play(FadeIn(headers), run_time=0.5)
        for cell in cells:
            self.play(FadeIn(cell), run_time=0.38)
        self.play(Write(result), run_time=0.85)
        self.wait(1.3)
        self.clear_content()

    def show_concrete_example(self):
        title = self.heading("例题：四项展开再合并")
        problem = self.formula(r"(x+2)(x+3)", 3.75, size=50)
        headers, cells = self.product_grid(("x", "2"), ("x", "3"),
                                           ("x^2", "3x", "2x", "6"))
        expanded = self.formula(r"=x^2+3x+2x+6", -3.85, size=39)
        result = self.formula(r"=x^2+5x+6", -5.15, size=43, color=ORANGE_ACCENT)
        self.play(Write(title), Write(problem), run_time=0.85)
        self.play(FadeIn(headers), run_time=0.5)
        for cell in cells:
            self.play(FadeIn(cell), run_time=0.4)
        self.play(Write(expanded), run_time=0.8)
        self.play(Write(result), run_time=0.8)
        self.wait(1.4)
        self.clear_content()

    def create_rule_card(self, heading, expression, explanation, color, y):
        box = RoundedRectangle(width=7.5, height=1.62, corner_radius=0.13,
                               stroke_color=color, stroke_width=2)
        title = self.fit(Text(heading, font_size=24, color=color), width=6.8)
        equation = self.fit(MathTex(expression, font_size=32), width=6.8)
        note = self.fit(Text(explanation, font_size=18, color=GRAY_A), width=6.8)
        content = VGroup(title, equation, note).arrange(DOWN, buff=0.07)
        return VGroup(box, content).move_to(UP * y)

    def show_summary(self):
        title = self.heading("整式乘法：三条法则")
        cards = VGroup(
            self.create_rule_card("单项式乘单项式", r"(2x)(3x^2)=6x^3",
                                  "系数乘系数，指数相加", GREEN_ACCENT, 3.5),
            self.create_rule_card("单项式乘多项式", r"a(b+c)=ab+ac",
                                  "每一项都要乘到", BLUE_ACCENT, 1.3),
            self.create_rule_card("多项式乘多项式", r"(a+b)(c+d)=ac+ad+bc+bd",
                                  "每项与每项相乘，再合并同类项", ORANGE_ACCENT, -0.9),
        )
        reminder = self.caption("先完整展开，最后合并同类项", -3.25, YELLOW)
        self.play(Write(title), run_time=0.65)
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(reminder), run_time=0.6)
        self.wait(1.3)
        self.clear_content()
        closing = self.caption("会用分配律，就能算整式乘法", 0, YELLOW)
        self.play(FadeIn(closing), run_time=0.65)
        self.wait(1)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.7)
