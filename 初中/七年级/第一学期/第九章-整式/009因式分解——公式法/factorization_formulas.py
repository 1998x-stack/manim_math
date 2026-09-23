"""因式分解——公式法。七镜头以完整公式识别代替不稳定的 MathTex 字形切片。

保留 FactorizationFormulas 场景名称与原有 MP4；公式法只应用于匹配结构的式子。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
BLUE_ACCENT = "#3498db"
GREEN_ACCENT = "#2ecc71"
ORANGE_ACCENT = "#e67e22"
SAFE_WIDTH = 7.4


def recognize_square_trinomial(middle_coefficient, constant):
    """识别 x² + middle*x + constant 是否为 (x±b)²，b 为非负整数。

    返回 (sign, b)；sign=1 对应加法，-1 对应减法，0 表示 b=0；不匹配返回 None。
    本函数并不判断所有三项式能否因式分解，只负责完全平方结构。
    """
    from math import isqrt

    if type(middle_coefficient) is not int or type(constant) is not int:
        raise ValueError("系数需为整数")
    if constant < 0:
        return None
    b = isqrt(constant)
    if b*b != constant:
        return None
    if middle_coefficient == 2*b:
        return (0 if b == 0 else 1, b)
    if middle_coefficient == -2*b:
        return (-1, b)
    return None


class FactorizationFormulas(Scene):
    """平方差、两种完全平方的逆用与不匹配反例。"""

    def fit(self, mob, max_width=SAFE_WIDTH):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, message):
        return self.fit(Text(message, font_size=37, color=BLUE_ACCENT)).move_to(UP * 5.5)

    def formula(self, tex, y, color=WHITE, size=42):
        return self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)

    def note(self, message, y, color=GRAY_A):
        return self.fit(Text(message, font_size=25, color=color)).move_to(UP * y)

    def clear_content(self):
        visible = [mob for mob in tuple(self.mobjects) if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        assert recognize_square_trinomial(6, 9) == (1, 3)
        assert recognize_square_trinomial(-6, 9) == (-1, 3)
        assert recognize_square_trinomial(6, 8) is None
        self.author_info = self.fit(
            Text("上海初高中数学直通车  @emptyandcalm", font_size=19, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_info)
        self.show_opening()
        self.show_difference_of_squares_theory()
        self.show_difference_of_squares_example()
        self.show_perfect_square_theory()
        self.show_perfect_square_example()
        self.show_challenge_example()
        self.show_summary()

    def show_opening(self):
        title = self.heading("乘法公式也能反过来用")
        prompt = self.formula(r"x^2-100=\,?", 2.4, ORANGE_ACCENT, 49)
        summary = self.note("把整式写成几个因式相乘的形式", -0.6, YELLOW)
        self.play(Write(title), Write(prompt), run_time=0.95)
        self.play(FadeIn(summary), run_time=0.55)
        self.wait(0.9)
        self.clear_content()

    def show_difference_of_squares_theory(self):
        title = self.heading("平方差：两平方相减")
        forward = self.formula(r"(a+b)(a-b)=a^2-b^2", 3.35, WHITE, 43)
        backward = self.formula(r"a^2-b^2=(a+b)(a-b)", 1.3, GREEN_ACCENT, 44)
        note = self.note("两个平方项之间是减号；没有中间项", -0.55, YELLOW)
        example = self.formula(r"x^2-100=x^2-10^2", -2.2, WHITE, 42)
        result = self.formula(r"=(x+10)(x-10)", -3.8, GREEN_ACCENT, 44)
        self.play(Write(title), Write(forward), run_time=0.8)
        self.play(Write(backward), FadeIn(note), run_time=0.9)
        self.play(Write(example), Write(result), run_time=1)
        self.wait(1.3)
        self.clear_content()

    def show_difference_of_squares_example(self):
        title = self.heading("例一：先把 9 写成平方")
        source = self.formula(r"x^2-9", 3.55, WHITE, 51)
        rewrite = self.formula(r"=x^2-3^2", 1.65, WHITE, 45)
        result = self.formula(r"=(x+3)(x-3)", -0.55, GREEN_ACCENT, 46)
        verify = self.formula(r"(x+3)(x-3)=x^2-9", -3.05, ORANGE_ACCENT, 37)
        self.play(Write(title), Write(source), run_time=0.9)
        self.play(Write(rewrite), run_time=0.7)
        self.play(Write(result), run_time=0.75)
        self.play(Write(verify), run_time=0.7)
        self.wait(1.2)
        self.clear_content()

    def show_perfect_square_theory(self):
        title = self.heading("完全平方：核对中间项")
        plus = self.formula(r"a^2+2ab+b^2=(a+b)^2", 3.35, GREEN_ACCENT, 41)
        minus = self.formula(r"a^2-2ab+b^2=(a-b)^2", 1.25, ORANGE_ACCENT, 41)
        check = self.formula(r"2ab=2\cdot a\cdot b", -0.65, WHITE, 43)
        note1 = self.note("首末两项要分别是平方；中间项须恰好为两倍乘积", -2.05, YELLOW)
        note2 = self.note("末项 b² 为正；中间项的符号决定括号内的符号", -3.35, WHITE)
        self.play(Write(title), Write(plus), run_time=0.8)
        self.play(Write(minus), Write(check), run_time=1)
        self.play(FadeIn(note1), FadeIn(note2), run_time=0.75)
        self.wait(1.3)
        self.clear_content()

    def show_perfect_square_example(self):
        title = self.heading("例二：检查平方项和中间项")
        original = self.formula(r"x^2+6x+9", 3.8, WHITE, 49)
        square_terms = self.formula(r"x^2=x^2,\quad 9=3^2", 2.0, WHITE, 40)
        middle = self.formula(r"6x=2\cdot x\cdot3", 0.3, ORANGE_ACCENT, 41)
        result = self.formula(r"x^2+6x+9=(x+3)^2", -1.9, GREEN_ACCENT, 43)
        contrast = self.note("对照：x²+6x+8 不是完全平方三项式", -4.0, YELLOW)
        self.play(Write(title), Write(original), run_time=0.9)
        self.play(Write(square_terms), Write(middle), run_time=0.9)
        self.play(Write(result), run_time=0.85)
        self.play(FadeIn(contrast), run_time=0.6)
        self.wait(1.1)
        self.clear_content()

    def show_challenge_example(self):
        title = self.heading("挑战：含系数的平方差")
        source = self.formula(r"4x^2-9y^2", 3.8, WHITE, 50)
        rewrite = self.formula(r"=(2x)^2-(3y)^2", 1.7, WHITE, 44)
        result = self.formula(r"=(2x+3y)(2x-3y)", -0.65, GREEN_ACCENT, 43)
        verify = self.formula(r"(2x+3y)(2x-3y)=4x^2-9y^2", -3.05, ORANGE_ACCENT, 35)
        self.play(Write(title), Write(source), run_time=0.9)
        self.play(Write(rewrite), run_time=0.7)
        self.play(Write(result), run_time=0.75)
        self.play(Write(verify), run_time=0.7)
        self.wait(1.3)
        self.clear_content()

    def show_summary(self):
        title = self.heading("看清结构，再选因式分解公式")
        formulas = VGroup(
            self.formula(r"a^2-b^2=(a+b)(a-b)", 3.0, GREEN_ACCENT, 38),
            self.formula(r"a^2+2ab+b^2=(a+b)^2", 0.95, GREEN_ACCENT, 37),
            self.formula(r"a^2-2ab+b^2=(a-b)^2", -1.15, GREEN_ACCENT, 37),
        )
        reminder = self.note("没有匹配结构时，不能机械地套用公式", -3.55, YELLOW)
        self.play(Write(title), run_time=0.7)
        for item in formulas:
            self.play(Write(item), run_time=0.6)
        self.play(FadeIn(reminder), run_time=0.55)
        self.wait(1.2)
        self.play(*[FadeOut(mob) for mob in tuple(self.mobjects)], run_time=0.7)
