"""分式方程：明确原方程定义域、去分母的必要条件和增根检验。"""
from math import isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
FRACTION_COLOR = "#00d4ff"
LCD_COLOR = "#a8e6cf"
WARNING_COLOR = "#ff6b6b"
RESULT_COLOR = "#ffeaa7"


def lcd_value(x):
    """本课分母的最简公分母 x²−1。"""
    if not isfinite(x):
        raise ValueError("x 必须是有限实数")
    return (x - 1) * (x + 1)


def original_defined(x):
    """只有 x≠±1 时原分式方程左右两侧均有意义。"""
    return lcd_value(x) != 0


def cleared_equation_residual(x):
    """去分母后的整式方程：(x+1)−2=0；它不是无条件的等价变形。"""
    lcd_value(x)
    return x + 1 - 2


def original_equation_residual(x):
    """仅在原方程定义域内计算两边之差。"""
    if not original_defined(x):
        raise ValueError("原方程的分母为零，不能代入")
    return 1 / (x - 1) - 2 / lcd_value(x)


def equation_solutions():
    """本课去分母只得到候选值 x=1，但其不在原方程定义域。"""
    candidates = (1.0,)
    return tuple(x for x in candidates
                 if original_defined(x) and original_equation_residual(x) == 0)


class FractionalEquation(Scene):
    """原七镜结构：引入、定义、四步法、去分母、求候选值、检验、总结。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        assert equation_solutions() == ()
        self.author_bar = self.cn("上海初高中数学直通车 @emptyandcalm", y=7.1,
                                  size=20, color=GRAY_B)
        self.add(self.author_bar)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_four_steps()
        self.scene4_remove_denom()
        self.scene5_solve_integral()
        self.scene6_verify_extraneous()
        self.scene7_outro()

    def cn(self, content, y=0, size=28, color=WHITE):
        label = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if label.width > 7.6:
            label.scale_to_fit_width(7.6)
        return label

    def tex(self, expression, y=0, size=40, color=WHITE):
        formula = MathTex(expression, font_size=size, color=color).move_to([0, y, 0])
        if formula.width > 7.6:
            formula.scale_to_fit_width(7.6)
        return formula

    def scene1_hook(self):
        title = self.cn("分母里有 x，能直接去分母吗？", 5.6, 33, GOLD)
        equation = self.tex(r"\frac{1}{x-1}=\frac{2}{x^2-1}", 2.1, 48, FRACTION_COLOR)
        note = self.cn("先看定义域，最后还要检验候选解", -0.3, 29, LCD_COLOR)
        self.play(Write(title), Write(equation), run_time=1)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(equation), FadeOut(note), run_time=0.5)

    def scene2_definition(self):
        title = self.cn("分式方程：分母中含有未知数", 5.5, 34, GOLD)
        original = self.tex(r"\frac{1}{x-1}=\frac{2}{x^2-1}", 3.6, 44, FRACTION_COLOR)
        factored = self.tex(r"x^2-1=(x-1)(x+1)", 1.8, 39, LCD_COLOR)
        restriction = self.tex(r"x\ne1,\quad x\ne-1", 0.2, 42, WARNING_COLOR)
        note = self.cn("分母为零时，原方程没有定义", -1.5, 29, WARNING_COLOR)
        self.play(Write(title), Write(original), run_time=0.8)
        self.play(Write(factored), Write(restriction), run_time=0.8)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(original), FadeOut(factored),
                  FadeOut(restriction), FadeOut(note), run_time=0.5)

    def scene3_four_steps(self):
        title = self.cn("分式方程：四个步骤", 5.6, 36, GOLD)
        rows = VGroup(*[self.cn(text, size=30, color=color)
                        for text, color in (
                            ("① 确定定义域与最简公分母", LCD_COLOR),
                            ("② 去分母，得到整式方程", FRACTION_COLOR),
                            ("③ 解整式方程，得到候选值", RESULT_COLOR),
                            ("④ 代回原方程，舍去增根", WARNING_COLOR),
                        )])
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.72).move_to(UP * 0.7)
        note = self.cn("去分母前后，只在分母不为零时等价", -3.9, 26, WARNING_COLOR)
        self.play(Write(title), run_time=0.4)
        for row in rows:
            self.play(FadeIn(row), run_time=0.4)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(rows), FadeOut(note), run_time=0.5)

    def scene4_remove_denom(self):
        self.original = self.tex(r"\frac{1}{x-1}=\frac{2}{x^2-1}", 5.5,
                                 41, FRACTION_COLOR)
        domain = self.tex(r"x\ne-1,\quad x\ne1", 4.3, 32, WARNING_COLOR)
        lcd = self.tex(r"\mathrm{LCD}=(x-1)(x+1)\ne0", 2.7, 37, LCD_COLOR)
        multiply = self.cn("两边同乘最简公分母，前提是它不为零", 1.4, 26, GRAY_A)
        # 这一步只在 x≠±1 的定义域内与原方程等价。
        self.cleared = self.tex(r"x+1=2", -0.4, 50, RESULT_COLOR)
        arrow = Arrow([0, 0.75, 0], [0, 0.0, 0], color=LCD_COLOR, buff=0.08)
        self.play(Write(self.original), Write(domain), run_time=0.8)
        self.play(Write(lcd), FadeIn(multiply), run_time=0.7)
        self.play(GrowArrow(arrow), Write(self.cleared), run_time=0.8)
        self.wait(0.7)
        self.play(FadeOut(domain), FadeOut(lcd), FadeOut(multiply),
                  FadeOut(arrow), run_time=0.4)
        self.play(self.original.animate.move_to(UP * 5.6).scale(0.85),
                  self.cleared.animate.move_to(UP * 2.9).scale(0.9), run_time=0.5)

    def scene5_solve_integral(self):
        title = self.cn("解整式方程，得到的是候选值", 1.7, 29, GOLD)
        step = self.tex(r"x+1=2\quad\Longrightarrow\quad x=1", 0.25,
                        39, RESULT_COLOR)
        self.candidate_label = self.tex(r"x=1", -1.7, 58, RESULT_COLOR)
        warning = self.cn("还不能写成原方程的解！", -3.3, 28, WARNING_COLOR)
        self.play(FadeIn(title), Write(step), run_time=0.8)
        self.play(Write(self.candidate_label), FadeIn(warning), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(step), FadeOut(warning), run_time=0.4)
        self.play(self.candidate_label.animate.move_to(DOWN * 0.25), run_time=0.4)

    def scene6_verify_extraneous(self):
        title = self.cn("检验：代入原方程的最简公分母", 5.0, 31, GOLD)
        check = self.tex(r"(x^2-1)\big|_{x=1}=1^2-1=0", 3.4, 36,
                         WARNING_COLOR)
        domain = self.tex(r"x\ne-1,\quad x\ne1", 2.2, 35, WARNING_COLOR)
        note = self.cn("候选值 x=1 使分母为零，原方程无意义", 1.0, 25, WARNING_COLOR)
        self.play(Write(title), Write(check), FadeIn(domain), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        number_line = NumberLine(x_range=[-3, 3, 1], length=6,
                                 include_numbers=False, include_tip=False,
                                 color=GRAY_B).move_to(DOWN * 2.4)
        excluded = VGroup(*[Circle(radius=0.095, color=WARNING_COLOR,
                                    stroke_width=3, fill_opacity=0).move_to(number_line.n2p(x))
                            for x in (-1, 1)])
        x_labels = VGroup(*[self.tex(str(x), size=27, color=WARNING_COLOR)
                            .next_to(number_line.n2p(x), DOWN, buff=0.25)
                            for x in (-1, 1)])
        excluded_candidate = Dot(number_line.n2p(1), radius=0.055,
                                  color=RESULT_COLOR)
        cross = Cross(excluded_candidate, color=WARNING_COLOR, stroke_width=5)
        self.play(Create(number_line), FadeIn(excluded), FadeIn(x_labels),
                  FadeIn(excluded_candidate), run_time=0.8)
        self.play(Create(cross), self.candidate_label.animate.set_opacity(0.25),
                  run_time=0.6)
        answer = self.cn("舍去增根 x=1：原方程无实数解", -4.7, 31, RESULT_COLOR)
        self.play(FadeIn(answer), run_time=0.6)
        self.wait(1.1)
        self.play(FadeOut(title), FadeOut(check), FadeOut(domain), FadeOut(note),
                  FadeOut(number_line), FadeOut(excluded), FadeOut(x_labels),
                  FadeOut(excluded_candidate), FadeOut(cross), FadeOut(answer),
                  FadeOut(self.original), FadeOut(self.cleared),
                  FadeOut(self.candidate_label), run_time=0.7)

    def scene7_outro(self):
        title = self.cn("解分式方程，检验不能省略", 5.4, 35, GOLD)
        steps = VGroup(*[self.cn(text, size=27, color=color)
                         for text, color in (
                             ("确定定义域：分母均不为零", LCD_COLOR),
                             ("去分母与解整式方程", FRACTION_COLOR),
                             ("检验：候选值若使原分母为零则舍去", WARNING_COLOR),
                             ("本例候选值为 1，但原方程无解", RESULT_COLOR),
                         )]).arrange(DOWN, buff=0.64).move_to(UP * 0.7)
        ending = self.cn("@emptyandcalm", -4.8, 27, GRAY_B)
        self.play(Write(title), run_time=0.5)
        for step in steps:
            self.play(FadeIn(step), run_time=0.4)
        self.play(FadeIn(ending), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(steps), FadeOut(ending),
                  FadeOut(self.author_bar), run_time=0.7)


# manim -ql fractional_equation_animation.py FractionalEquation
