"""因式分解——提公因式法。保留 CommonFactorMethod 和原有七镜头入口。

公因式系数取非零项系数绝对值的 GCD；字母取各项对应指数的最小值。
原有 MP4 不在本次代码修复中修改。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
PRIMARY = "#3498db"
FACTOR_COLOR = "#e74c3c"
RESULT_COLOR = "#2ecc71"
SAFE_WIDTH = 7.4


def common_factor_data(terms):
    """接收非零整系数 (coefficient, x_power, y_power)，返回公因式及商项。

    返回值 (gcd_coefficient, min_x_power, min_y_power), quotient_terms。
    与具体变量名无关，适用于场景示例中的 (x,y) 或 (a,b)。
    """
    from math import gcd

    if not isinstance(terms, (tuple, list)) or not terms:
        raise ValueError("至少需要一个非零单项式")
    normalized = []
    for term in terms:
        if (not isinstance(term, (tuple, list)) or len(term) != 3
                or any(type(value) is not int for value in term)):
            raise ValueError("每一项必须提供三个整数：系数和两个指数")
        coefficient, x_power, y_power = term
        if coefficient == 0 or x_power < 0 or y_power < 0:
            raise ValueError("系数必须非零，指数必须是非负整数")
        normalized.append((coefficient, x_power, y_power))
    factor_coefficient = 0
    for coefficient, _, _ in normalized:
        factor_coefficient = gcd(factor_coefficient, abs(coefficient))
    x_min = min(term[1] for term in normalized)
    y_min = min(term[2] for term in normalized)
    quotient = tuple((coef // factor_coefficient, xp - x_min, yp - y_min)
                     for coef, xp, yp in normalized)
    return (factor_coefficient, x_min, y_min), quotient


class CommonFactorMethod(Scene):
    """通过实际商项和反向展开讲解提公因式。"""

    def fit(self, mob, max_width=SAFE_WIDTH):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, content):
        return self.fit(Text(content, font_size=38, color=PRIMARY)).move_to(UP * 5.5)

    def formula(self, tex, y, color=WHITE, size=41):
        return self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)

    def note(self, content, y, color=GRAY_A):
        return self.fit(Text(content, font_size=25, color=color)).move_to(UP * y)

    def clear_content(self):
        visible = [mob for mob in tuple(self.mobjects) if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.first_factor, self.first_quotient = common_factor_data(
            ((6, 2, 1), (-9, 1, 2))
        )
        self.second_factor, self.second_quotient = common_factor_data(
            ((12, 2, 1), (-8, 1, 2))
        )
        self.third_factor, self.third_quotient = common_factor_data(
            ((5, 3, 0), (10, 2, 0), (-15, 1, 0))
        )
        assert self.first_factor == (3, 1, 1)
        assert self.first_quotient == ((2, 1, 0), (-3, 0, 1))
        assert self.second_factor == (4, 1, 1)
        assert self.third_factor == (5, 1, 0)
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_info)
        self.show_opening()
        self.show_concept_intro()
        self.show_extraction_steps()
        self.show_memory_tips()
        self.show_example_1()
        self.show_example_2()
        self.show_summary()

    def show_opening(self):
        title = self.heading("因式分解：乘法的逆过程")
        problem = self.formula(r"6x^2y-9xy^2=\,?", 2.0, PRIMARY, 48)
        hint = self.note("先找出两项共同含有的因式", -0.7, YELLOW)
        self.play(Write(title), Write(problem), run_time=1)
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(0.9)
        self.clear_content()

    def show_concept_intro(self):
        title = self.heading("什么是公因式？")
        original = self.formula(r"ab+ac", 3.7, PRIMARY, 53)
        expanded = self.formula(r"a\cdot b+a\cdot c", 1.7, WHITE, 42)
        factored = self.formula(r"=a(b+c)", -0.5, RESULT_COLOR, 48)
        note = self.note("两个乘积都含有 a，把 a 提到括号外", -3.0, YELLOW)
        self.play(Write(title), Write(original), run_time=0.8)
        self.play(Write(expanded), run_time=0.65)
        self.play(Write(factored), run_time=0.75)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)
        self.clear_content()

    def show_extraction_steps(self):
        title = self.heading("例题：找、提、除、验")
        original = self.formula(r"6x^2y-9xy^2", 3.9, WHITE, 48)
        analysis = self.note("系数最大公因数是 3；x 与 y 的最低指数都为 1", 2.4, YELLOW)
        common = self.formula(r"3xy", 0.95, FACTOR_COLOR, 56)
        quotients = VGroup(
            self.formula(r"\frac{6x^2y}{3xy}=2x", -0.75, WHITE, 36),
            self.formula(r"\frac{-9xy^2}{3xy}=-3y", -2.05, WHITE, 36),
        )
        answer = self.formula(r"6x^2y-9xy^2=3xy(2x-3y)", -3.6, RESULT_COLOR, 38)
        self.play(Write(title), Write(original), run_time=0.85)
        self.play(FadeIn(analysis), Write(common), run_time=0.85)
        for quotient in quotients:
            self.play(Write(quotient), run_time=0.65)
        self.play(Write(answer), run_time=0.85)
        self.wait(1.2)
        self.clear_content()
        # 清屏后才展示反向乘法检查；不留下原式与新公式叠在同一位置。
        check_title = self.heading("检验：再乘回原式")
        verification = self.formula(r"3xy(2x-3y)", 2.4, FACTOR_COLOR, 48)
        expanded = self.formula(r"=6x^2y-9xy^2", 0.25, RESULT_COLOR, 45)
        self.play(Write(check_title), Write(verification), run_time=0.8)
        self.play(Write(expanded), run_time=0.85)
        self.wait(1.0)
        self.clear_content()

    def show_memory_tips(self):
        title = self.heading("提公因式：四个动作")
        instructions = (
            "找：系数取最大公因数",
            "提：字母取公有的最低次幂",
            "除：每一项除以公因式，保留符号",
            "验：把括号乘开，核对原式",
        )
        lines = VGroup(*[self.fit(Text(s, font_size=26, color=WHITE))
                         for s in instructions]).arrange(DOWN, buff=0.52)
        lines.move_to(UP * 0.65)
        self.play(Write(title), run_time=0.65)
        for line in lines:
            self.play(FadeIn(line, shift=RIGHT * 0.15), run_time=0.6)
        self.wait(1.2)
        self.clear_content()

    def show_example_1(self):
        title = self.heading("练习一：两项式")
        original = self.formula(r"12a^2b-8ab^2", 3.65, WHITE, 47)
        gcd_note = self.note("系数取 4；字母取 ab", 1.85, YELLOW)
        quotient = self.formula(r"12a^2b\div 4ab=3a", 0.35, WHITE, 36)
        quotient2 = self.formula(r"-8ab^2\div 4ab=-2b", -1.1, WHITE, 36)
        result = self.formula(r"=4ab(3a-2b)", -3.1, RESULT_COLOR, 46)
        self.play(Write(title), Write(original), run_time=0.85)
        self.play(FadeIn(gcd_note), run_time=0.45)
        self.play(Write(quotient), Write(quotient2), run_time=0.9)
        self.play(Write(result), run_time=0.75)
        self.wait(1.2)
        self.clear_content()

    def show_example_2(self):
        title = self.heading("练习二：三项式")
        original = self.formula(r"5x^3+10x^2-15x", 3.75, WHITE, 46)
        gcd_note = self.note("系数取 5；最低次幂 x¹，公因式为 5x", 2.1, YELLOW)
        quotient = self.formula(r"x^2+2x-3", 0.5, WHITE, 47)
        factor = self.formula(r"5x(x^2+2x-3)", -1.6, RESULT_COLOR, 48)
        check = self.formula(r"=5x^3+10x^2-15x", -3.8, WHITE, 40)
        self.play(Write(title), Write(original), run_time=0.85)
        self.play(FadeIn(gcd_note), Write(quotient), run_time=0.8)
        self.play(Write(factor), run_time=0.8)
        self.play(Write(check), run_time=0.75)
        self.wait(1.2)
        self.clear_content()

    def show_summary(self):
        title = self.heading("公因式提取完整，结果才正确")
        formula = self.formula(r"6x^2y-9xy^2=3xy(2x-3y)", 2.4, RESULT_COLOR, 38)
        rule = self.note("系数取最大公因数，字母取最低次幂", 0.1, YELLOW)
        warning = self.note("括号内每一项的正负号也必须保留", -2.1, WHITE)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(FadeIn(rule), FadeIn(warning), run_time=0.7)
        self.wait(1.2)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.7)
