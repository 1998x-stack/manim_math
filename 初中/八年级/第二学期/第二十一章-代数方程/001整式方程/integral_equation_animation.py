"""整式方程：因式分解、零乘积法则和三次方程的实数解。"""
from math import copysign, isfinite
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
BG_COLOR = "#1a1a2e"
MAIN_COLOR = "#00d4ff"
FACTOR_COLOR = "#fd79a8"
RESULT_COLOR = "#ffeaa7"
STEP_COLOR = "#a8e6cf"


def polynomial_value(x):
    """本课主例题 p(x)=x³−4x 的因式形式。"""
    if not isfinite(x):
        raise ValueError("x 必须是有限实数")
    return x * (x - 2) * (x + 2)


def factor_roots(a):
    """x(x-a)(x+a)=0 的互异实数根，按从小到大排序。"""
    if not isfinite(a):
        raise ValueError("a 必须是有限实数")
    roots = tuple(sorted({-abs(a), 0.0, abs(a)}))
    if not all(root * (root - a) * (root + a) == 0 for root in roots):
        raise AssertionError("因式分解产生了错误的根")
    return roots


def real_cube_root(a):
    """实数范围内 x³=a 的唯一解，允许 a 为负或零。"""
    if not isfinite(a):
        raise ValueError("a 必须是有限实数")
    return copysign(abs(a) ** (1.0 / 3.0), a)


class IntegralEquation(Scene):
    """保留原有七镜教学结构和公开 Scene 类名。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.roots = factor_roots(2)
        assert self.roots == (-2.0, 0.0, 2.0)
        self.author_bar = self.cn("上海初高中数学直通车 @emptyandcalm", 7.1,
                                  size=20, color=GRAY_B)
        self.add(self.author_bar)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_core_idea()
        self.scene4_example()
        self.scene5_zero_product()
        self.scene6_cube_type()
        self.scene7_outro()

    def cn(self, text, y=0, size=29, color=WHITE):
        obj = Text(text, font_size=size, color=color).move_to([0, y, 0])
        if obj.width > 7.6:
            obj.scale_to_fit_width(7.6)
        return obj

    def tex(self, formula, y=0, size=40, color=WHITE):
        obj = MathTex(formula, font_size=size, color=color).move_to([0, y, 0])
        if obj.width > 7.6:
            obj.scale_to_fit_width(7.6)
        return obj

    def scene1_hook(self):
        title = self.cn("一个三次方程，怎样找出所有实数解？", 5.6, 32, GOLD)
        equation = self.tex(r"x^3-4x=0", 2.0, 60, MAIN_COLOR)
        prompt = self.cn("把高次式分解为低次因式", -0.2, 28, STEP_COLOR)
        self.play(Write(title), Write(equation), run_time=1)
        self.play(FadeIn(prompt), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(equation), FadeOut(prompt), run_time=0.5)

    def scene2_definition(self):
        title = self.cn("整式方程", 5.6, 39, GOLD)
        definition = self.cn("分母中不含未知数，整理后可写成整式等式", 4.3, 26)
        examples = VGroup(
            self.tex(r"2x+1=0", size=34, color=GRAY_A),
            self.tex(r"x^2-5x+6=0", size=34, color=GRAY_A),
            self.tex(r"x^3-4x=0", size=39, color=MAIN_COLOR),
        ).arrange(DOWN, buff=0.57).move_to(UP * 0.5)
        note = self.cn("本课重点：用因式分解求三次整式方程的实数解", -3.2,
                       26, RESULT_COLOR)
        self.play(Write(title), FadeIn(definition), run_time=0.7)
        for example in examples:
            self.play(Write(example), run_time=0.4)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(definition), FadeOut(examples),
                  FadeOut(note), run_time=0.5)

    def scene3_core_idea(self):
        title = self.cn("核心思想：降次", 5.5, 38, GOLD)
        high = self.tex(r"x^3-4x=0", 2.9, 44, MAIN_COLOR)
        arrow = Arrow([0, 2.0, 0], [0, 1.15, 0], color=STEP_COLOR, buff=0.08)
        low = self.tex(r"x(x^2-4)=0", 0.4, 43, FACTOR_COLOR)
        detail = self.cn("先提公因式，再用平方差公式", -1.1, 29, STEP_COLOR)
        conclusion = self.tex(r"x(x+2)(x-2)=0", -2.6, 44, RESULT_COLOR)
        self.play(Write(title), Write(high), run_time=0.7)
        self.play(GrowArrow(arrow), Write(low), run_time=0.8)
        self.play(FadeIn(detail), Write(conclusion), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(high), FadeOut(arrow), FadeOut(low),
                  FadeOut(detail), FadeOut(conclusion), run_time=0.5)

    def scene4_example(self):
        title = self.cn("例题：解 x³−4x=0", 5.6, 37, GOLD)
        steps = VGroup(self.tex(r"x^3-4x=0", size=39, color=MAIN_COLOR),
                       self.tex(r"x(x^2-4)=0", size=39, color=STEP_COLOR),
                       self.tex(r"x(x+2)(x-2)=0", size=39, color=FACTOR_COLOR))
        steps.arrange(DOWN, buff=0.52).move_to(UP * 2.5)
        explanation = self.cn("提公因式 x，再用平方差公式", -0.5, 27, GRAY_A)
        # 避免把中文“或”放进默认 MathTex 的 LaTeX 公式。
        root_formulas = VGroup(self.tex(r"x=-2", size=34, color=RESULT_COLOR),
                               self.cn("或", size=26, color=GRAY_A),
                               self.tex(r"x=0", size=34, color=RESULT_COLOR),
                               self.cn("或", size=26, color=GRAY_A),
                               self.tex(r"x=2", size=34, color=RESULT_COLOR))
        root_formulas.arrange(RIGHT, buff=0.2).move_to(DOWN * 1.6)
        axis = NumberLine(x_range=[-3, 3, 1], length=6.0,
                          include_numbers=False, include_tip=False,
                          color=GRAY_B).move_to(DOWN * 3.5)
        dots = VGroup(*[Dot(axis.n2p(root), radius=0.095, color=RESULT_COLOR)
                        for root in self.roots])
        tick_labels = VGroup(*[self.tex(str(int(root)), size=27, color=RESULT_COLOR)
                               .next_to(axis.n2p(root), DOWN, buff=0.3)
                               for root in self.roots])
        self.play(Write(title), run_time=0.5)
        for step in steps:
            self.play(Write(step), run_time=0.55)
        self.play(FadeIn(explanation), FadeIn(root_formulas), run_time=0.7)
        self.play(Create(axis), FadeIn(dots), FadeIn(tick_labels), run_time=0.9)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(steps), FadeOut(explanation),
                  FadeOut(root_formulas), FadeOut(axis), FadeOut(dots),
                  FadeOut(tick_labels), run_time=0.5)

    def scene5_zero_product(self):
        title = self.cn("零乘积法则", 5.6, 39, GOLD)
        formula = self.tex(r"A\cdot B\cdot C=0", 3.0, 52, MAIN_COLOR)
        premise = self.cn("实数乘积为零，至少有一个因式为零", 1.7, 28, STEP_COLOR)
        branches = VGroup(self.tex(r"A=0", size=39, color=RESULT_COLOR),
                          self.tex(r"B=0", size=39, color=RESULT_COLOR),
                          self.tex(r"C=0", size=39, color=RESULT_COLOR))
        branches.arrange(RIGHT, buff=0.9).move_to(DOWN * 0.3)
        note = self.cn("不能把 x³−4x=0 两边直接除以 x", -2.0, 27, FACTOR_COLOR)
        lost_root = self.cn("那样会遗漏 x=0 这个解", -3.1, 28, RESULT_COLOR)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(premise), FadeIn(branches), run_time=0.7)
        self.play(FadeIn(note), FadeIn(lost_root), run_time=0.7)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(premise),
                  FadeOut(branches), FadeOut(note), FadeOut(lost_root), run_time=0.5)

    def scene6_cube_type(self):
        title = self.cn("另一类：三次方程 x³=a", 5.6, 36, GOLD)
        example = self.tex(r"x^3=8", 3.6, 55, MAIN_COLOR)
        step = self.tex(r"x=\sqrt[3]{8}=2", 1.8, 48, RESULT_COLOR)
        verify = self.tex(r"2^3=8", 0.4, 34, STEP_COLOR)
        general = self.tex(r"x^3=a\ \Longrightarrow\ x=\sqrt[3]{a}", -1.5,
                           37, MAIN_COLOR)
        restriction = self.cn("对任意实数 a，三次方程在实数范围恰有一个解", -2.8,
                              26)
        contrast = self.cn("注意：偶次方程不能套用这一结论", -4.1, 27, FACTOR_COLOR)
        self.play(Write(title), Write(example), run_time=0.8)
        self.play(Write(step), FadeIn(verify), run_time=0.8)
        self.play(Write(general), FadeIn(restriction), run_time=0.7)
        self.play(FadeIn(contrast), run_time=0.4)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(example), FadeOut(step), FadeOut(verify),
                  FadeOut(general), FadeOut(restriction), FadeOut(contrast), run_time=0.5)

    def scene7_outro(self):
        heading = self.cn("整式方程：方法与检查", 5.5, 37, GOLD)
        notes = VGroup(self.cn("第一步：整理并因式分解", size=29, color=STEP_COLOR),
                       self.cn("第二步：各因式分别等于零", size=29, color=STEP_COLOR),
                       self.cn("第三步：逐一代回原方程", size=29, color=RESULT_COLOR))
        notes.arrange(DOWN, buff=0.7).move_to(UP * 1.3)
        verify = self.tex(r"p(-2)=p(0)=p(2)=0", -2.1, 35, MAIN_COLOR)
        ending = self.cn("@emptyandcalm", -4.3, 27, GRAY_B)
        self.play(Write(heading), run_time=0.5)
        for note in notes:
            self.play(FadeIn(note), run_time=0.4)
        self.play(Write(verify), FadeIn(ending), run_time=0.6)
        self.wait(0.9)
        self.play(FadeOut(heading), FadeOut(notes), FadeOut(verify),
                  FadeOut(ending), FadeOut(self.author_bar), run_time=0.7)


# manim -ql integral_equation_animation.py IntegralEquation
