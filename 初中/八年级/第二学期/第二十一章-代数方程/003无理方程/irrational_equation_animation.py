"""无理方程：明确根式定义域与非负右侧条件，平方后逐根检验。"""
from math import isfinite, isclose, sqrt
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
BG_COLOR = "#1a1a2e"
RADICAL_COLOR = "#00d4ff"
SQUARE_COLOR = "#a8e6cf"
GOOD_COLOR = "#55efc4"
BAD_COLOR = "#ff6b6b"


def radical_defined(x):
    """√(2x+1) 在实数范围的定义域 x≥−1/2。"""
    if not isfinite(x):
        raise ValueError("x 必须是有限实数")
    return 2*x + 1 >= 0


def necessary_sign_condition(x):
    """√(2x+1)=x−1 要求右侧非负，即 x≥1。"""
    return radical_defined(x) and x-1 >= 0


def squared_residual(x):
    """平方后方程 (x−1)²−(2x+1)=x(x−4)。"""
    radical_defined(x)
    return (x-1)**2 - (2*x+1)


def original_residual(x):
    """只在根式定义域内计算原方程左右两侧的差。"""
    if not radical_defined(x):
        raise ValueError("根号内为负数，原方程无实数意义")
    return sqrt(2*x + 1) - (x-1)


def validated_solutions():
    """平方后候选值为 0 和 4；需满足非负右侧并代回原方程。"""
    candidates = (0, 4)
    return tuple(x for x in candidates
                 if necessary_sign_condition(x)
                 and isclose(original_residual(x), 0, abs_tol=1e-12))


class IrrationalEquation(Scene):
    """保留七镜及原入口：引入、定义、流程、平方、候选值、检验、总结。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        assert validated_solutions() == (4,)
        self.author_bar = self.cn("上海初高中数学直通车 @emptyandcalm", y=7.1,
                                  size=20, color=GRAY_B)
        self.add(self.author_bar)
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_four_steps()
        self.scene4_square_both_sides()
        self.scene5_solve_quadratic()
        self.scene6_verify()
        self.scene7_outro()

    def cn(self, content, y=0, size=29, color=WHITE):
        result = Text(content, font_size=size, color=color).move_to([0, y, 0])
        if result.width > 7.6:
            result.scale_to_fit_width(7.6)
        return result

    def tex(self, formula, y=0, size=40, color=WHITE):
        result = MathTex(formula, font_size=size, color=color).move_to([0, y, 0])
        if result.width > 7.6:
            result.scale_to_fit_width(7.6)
        return result

    def scene1_hook(self):
        title = self.cn("两边平方得到的根，都能代回原方程吗？", 5.5, 30, GOLD)
        original = self.tex(r"\sqrt{2x+1}=x-1", 2.0, 53, RADICAL_COLOR)
        note = self.cn("平方前，先考虑根式与右侧的符号", -0.2, 28, SQUARE_COLOR)
        self.play(Write(title), Write(original), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(original), FadeOut(note), run_time=0.5)

    def scene2_definition(self):
        title = self.cn("无理方程：根号内含有未知数", 5.5, 34, GOLD)
        original = self.tex(r"\sqrt{2x+1}=x-1", 3.6, 48, RADICAL_COLOR)
        domain = self.tex(r"2x+1\ge0\quad\Longrightarrow\quad x\ge-\tfrac12",
                          1.6, 36, SQUARE_COLOR)
        rhs = self.tex(r"\sqrt{2x+1}\ge0\quad\Longrightarrow\quad x-1\ge0",
                       -0.1, 31, SQUARE_COLOR)
        necessary = self.tex(r"x\ge1", -1.8, 46, GOOD_COLOR)
        note = self.cn("有实数解时，必须同时满足根式有定义、右侧非负", -3.3,
                       26, BAD_COLOR)
        self.play(Write(title), Write(original), run_time=0.8)
        self.play(Write(domain), Write(rhs), run_time=1)
        self.play(Write(necessary), FadeIn(note), run_time=0.8)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(original), FadeOut(domain),
                  FadeOut(rhs), FadeOut(necessary), FadeOut(note), run_time=0.5)

    def scene3_four_steps(self):
        title = self.cn("解无理方程：四步法", 5.6, 35, GOLD)
        steps = VGroup(*[self.cn(text, size=29, color=color)
                         for text, color in (
                             ("① 整理方程，确定根式和右侧的条件", RADICAL_COLOR),
                             ("② 两边平方，得到整式方程", SQUARE_COLOR),
                             ("③ 求得候选根，不能直接宣布答案", GOLD),
                             ("④ 代回原方程，舍去增根", BAD_COLOR),
                         )]).arrange(DOWN, buff=0.68).move_to(UP * 0.5)
        self.play(Write(title), run_time=0.5)
        for step in steps:
            self.play(FadeIn(step), run_time=0.45)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(steps), run_time=0.5)

    def scene4_square_both_sides(self):
        self.original = self.tex(r"\sqrt{2x+1}=x-1", 5.5, 42, RADICAL_COLOR)
        restriction = self.tex(r"x\ge1", 4.4, 34, BAD_COLOR)
        squared = self.tex(r"2x+1=(x-1)^2", 2.6, 40, SQUARE_COLOR)
        expanded = self.tex(r"2x+1=x^2-2x+1", 0.9, 36, SQUARE_COLOR)
        self.quadratic = self.tex(r"x^2-4x=0", -0.9, 44, GOLD)
        note = self.cn("平方只能保证原方程的解也是新方程的解", -2.5,
                       26, BAD_COLOR)
        self.play(Write(self.original), Write(restriction), run_time=0.7)
        self.play(Write(squared), Write(expanded), run_time=0.9)
        self.play(Write(self.quadratic), FadeIn(note), run_time=0.7)
        self.wait(0.7)
        self.play(FadeOut(restriction), FadeOut(squared), FadeOut(expanded),
                  FadeOut(note), run_time=0.5)
        self.play(self.quadratic.animate.move_to(UP * 2.8), run_time=0.4)

    def scene5_solve_quadratic(self):
        factoring = self.tex(r"x(x-4)=0", 1.1, 45, SQUARE_COLOR)
        left = self.tex(r"x=0", -0.6, 42, BAD_COLOR)
        right = self.tex(r"x=4", -0.6, 42, GOOD_COLOR)
        candidates = VGroup(left, right).arrange(RIGHT, buff=1.5)
        candidates.move_to(DOWN * 0.7)
        condition = self.cn("候选值 x=0、x=4；还要逐一检验", -2.4,
                            28, GOLD)
        self.play(Write(factoring), run_time=0.6)
        self.play(FadeIn(candidates), FadeIn(condition), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(self.original), FadeOut(self.quadratic),
                  FadeOut(factoring), FadeOut(candidates), FadeOut(condition),
                  run_time=0.5)

    def scene6_verify(self):
        title = self.cn("原方程检验：x=0 舍去，x=4 保留", 5.7, 33, GOLD)
        bad = self.tex(r"x=0:\ \sqrt1=1\ne-1=0-1", 4.2, 29, BAD_COLOR)
        good = self.tex(r"x=4:\ \sqrt9=3=4-1", 3.2, 29, GOOD_COLOR)
        self.play(Write(title), Write(bad), Write(good), run_time=1.0)
        # 图像只是示意：根式函数定义域从 -1/2 开始；在此镜只绘制 x≥0 部分。
        axes = Axes(x_range=[0, 5, 1], y_range=[-2, 4, 1],
                    x_length=6.0, y_length=5.6, tips=False,
                    axis_config={"include_numbers": False, "stroke_width": 2})
        axes.move_to(DOWN * 0.6)
        radical = axes.plot(lambda x: sqrt(2*x+1), x_range=[0, 4.8],
                            color=RADICAL_COLOR, stroke_width=4)
        line = axes.plot(lambda x: x-1, x_range=[0, 4.8],
                         color=SQUARE_COLOR, stroke_width=4)
        false_points = VGroup(Dot(axes.c2p(0, 1), color=BAD_COLOR, radius=0.08),
                              Dot(axes.c2p(0, -1), color=BAD_COLOR, radius=0.08))
        difference = DashedLine(axes.c2p(0, 1), axes.c2p(0, -1),
                                color=BAD_COLOR, stroke_width=3)
        true_point = Dot(axes.c2p(4, 3), color=GOOD_COLOR, radius=0.11)
        true_label = self.tex(r"(4,3)", size=27, color=GOOD_COLOR)
        true_label.next_to(true_point, RIGHT, buff=0.15)
        graph_group = VGroup(axes, radical, line, false_points, difference,
                             true_point, true_label)
        self.play(Create(axes), Create(radical), Create(line), run_time=1.2)
        self.play(FadeIn(false_points), Create(difference),
                  FadeIn(true_point), FadeIn(true_label), run_time=0.7)
        note = self.cn("只有交点 x=4 同时满足原方程两侧相等", -5.4,
                       26, GOOD_COLOR)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(bad), FadeOut(good),
                  FadeOut(graph_group), FadeOut(note), run_time=0.6)

    def scene7_outro(self):
        title = self.cn("无理方程：平方后必须代回检验", 5.3, 34, GOLD)
        steps = VGroup(*[self.cn(text, size=28, color=color)
                         for text, color in (
                             ("根式有定义，右边不能为负", RADICAL_COLOR),
                             ("平方得候选值：0 和 4", SQUARE_COLOR),
                             ("x=0 不满足原方程；x=4 满足", GOOD_COLOR),
                             ("最终实数解：x=4", GOLD),
                         )]).arrange(DOWN, buff=0.66).move_to(UP * 0.7)
        ending = self.cn("@emptyandcalm", -4.8, 28, GRAY_B)
        self.play(Write(title), run_time=0.5)
        for step in steps:
            self.play(FadeIn(step), run_time=0.45)
        self.play(FadeIn(ending), run_time=0.4)
        self.wait(0.9)
        self.play(FadeOut(title), FadeOut(steps), FadeOut(ending),
                  FadeOut(self.author_bar), run_time=0.7)


# manim -ql irrational_equation_animation.py IrrationalEquation
