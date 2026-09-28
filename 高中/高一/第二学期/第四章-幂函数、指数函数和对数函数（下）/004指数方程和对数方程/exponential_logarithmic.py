"""高一第二学期《指数方程和对数方程》：保留原 Scene 入口及七段结构。

三层分离：方程的定义域、真实交点坐标、屏上可见图像窗口。
运行：manim -ql exponential_logarithmic.py ExponentialLogarithmicEquations
"""
from manim import *
import math

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
EXP = "#e74c3c"
LOG = "#3498db"
GOOD = "#2ecc71"
WARN = "#f39c12"
AUTHOR = "上海初高中数学直通车 @emptyandcalm"


def cn(value, size=28, color=WHITE):
    return Text(value, font=FONT, font_size=size, color=color)


def fit(item, max_width=7.6):
    if item.width > max_width:
        item.scale_to_fit_width(max_width)
    return item


class ExponentialLogarithmicEquations(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.author_info = fit(cn(AUTHOR, 17, GRAY_B)).move_to(UP * 7.45)
        self.add(self.author_info)
        self.setup_geometry()
        self.show_opening()
        self.show_exponential_definition()
        self.show_exponential_graph_solution()
        self.show_same_base_method()
        self.show_logarithm_definition()
        self.show_logarithm_graph_solution()
        self.show_verification_outro()

    def setup_geometry(self):
        # 关键点是数学坐标；实际像素边界由 Axes.c2p 与渲染后 Mobject 包围盒另行检查。
        self.solution_exp = 3
        self.solution_log = 8
        assert 2**self.solution_exp == 8
        assert math.log2(self.solution_log) == 3

    def _title(self, value, color=YELLOW):
        return fit(cn(value, 37, color)).move_to(UP * 6.4)

    def _clear(self, *objects):
        self.play(*[FadeOut(obj) for obj in objects], run_time=0.5)

    def show_opening(self):
        title = self._title("指数方程与对数方程")
        question = MathTex(r"2^x=8", font_size=54, color=EXP).move_to(UP * 3.0)
        answer = MathTex(r"x=3", font_size=49, color=GOOD).move_to(UP * 0.6)
        follow = MathTex(r"\log_2 t=3\quad\Rightarrow\quad t=8", font_size=36, color=LOG)
        fit(follow).move_to(DOWN * 2.0)
        note = cn("两个方程的未知数位置不同", 27).move_to(DOWN * 4)
        self.play(Write(title), Write(question), run_time=0.9)
        self.wait(0.5)
        self.play(Write(answer), run_time=0.6)
        self.play(Write(follow), FadeIn(note), run_time=0.8)
        self.wait(0.8)
        self._clear(title, question, answer, follow, note)

    def show_exponential_definition(self):
        title = self._title("指数方程：未知数出现在指数中", EXP)
        equation = MathTex(r"2^x=8", font_size=48).move_to(UP * 3)
        steps = VGroup(
            MathTex(r"8=2^3", font_size=42, color=YELLOW),
            MathTex(r"2^x=2^3", font_size=42),
            MathTex(r"x=3", font_size=46, color=GOOD),
        ).arrange(DOWN, buff=0.75).move_to(DOWN * 0.5)
        note = cn("底数 2>0 且不为 1，指数函数严格递增", 24, GRAY_A)
        fit(note).move_to(DOWN * 5)
        self.play(Write(title), Write(equation), run_time=0.9)
        for step in steps:
            self.play(Write(step), run_time=0.6)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.9)
        self._clear(title, equation, steps, note)

    def show_exponential_graph_solution(self):
        title = self._title("图像法：2 的 x 次方等于 8", EXP)
        axes = Axes(x_range=[-1, 4, 1], y_range=[0, 9, 1], x_length=5.2, y_length=6,
                    axis_config={"color": GRAY_B}, tips=False).move_to(DOWN * 0.2)
        # 最大可见 x=log₂9，避免原源码 x=4.5 对应 22.63 越出 y=9 轴域。
        graph = axes.plot(lambda x: 2**x, x_range=[-1, math.log2(9)], color=EXP, stroke_width=4)
        level = DashedLine(axes.c2p(-1, 8), axes.c2p(4, 8), color=LOG)
        vertical = DashedLine(axes.c2p(3, 0), axes.c2p(3, 8), color=GRAY_A)
        dot = Dot(axes.c2p(3, 8), color=GOOD, radius=0.1)
        label = MathTex(r"(3,8)", font_size=30, color=GOOD).next_to(dot, LEFT, buff=0.2)
        answer = MathTex(r"x=3", font_size=40, color=GOOD).move_to(DOWN * 5.1)
        self.play(Write(title), Create(axes), run_time=1.0)
        self.play(Create(graph), run_time=1.1)
        self.play(Create(level), run_time=0.7)
        self.play(Create(vertical), FadeIn(dot), Write(label), run_time=0.9)
        self.play(Write(answer), run_time=0.6)
        self.wait(0.9)
        self._clear(title, axes, graph, level, vertical, dot, label, answer)

    def show_same_base_method(self):
        title = self._title("同底数法的依据")
        steps = VGroup(
            MathTex(r"2^x=8", font_size=45),
            MathTex(r"2^x=2^3", font_size=45, color=EXP),
            MathTex(r"x=3", font_size=47, color=GOOD),
        ).arrange(DOWN, buff=0.9).move_to(UP * 1.5)
        condition = MathTex(r"a^u=a^v\iff u=v\quad (a>0,\ a\ne1)", font_size=31, color=YELLOW)
        fit(condition).move_to(DOWN * 3.2)
        warning = cn("底数必须合法，不能靠 TeX 字符索引框选底数", 22, GRAY_A)
        fit(warning).move_to(DOWN * 4.5)
        self.play(Write(title), run_time=0.6)
        for step in steps:
            self.play(Write(step), run_time=0.75)
        self.play(Write(condition), FadeIn(warning), run_time=0.8)
        self.wait(1.0)
        self._clear(title, steps, condition, warning)

    def show_logarithm_definition(self):
        title = self._title("对数方程：先检查真数与底数", LOG)
        formula = MathTex(r"\log_2 x=3", font_size=48, color=LOG).move_to(UP * 3.6)
        conditions = MathTex(r"x>0,\quad 2>0,\quad 2\ne1", font_size=34).move_to(UP * 1.8)
        equivalent = MathTex(r"x=2^3=8", font_size=42, color=GOOD).move_to(DOWN * 0.8)
        check = MathTex(r"\log_2 8=3", font_size=40, color=GOOD).move_to(DOWN * 3.0)
        explanation = cn("求解后还要代回原方程验证", 26, WARN).move_to(DOWN * 4.5)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(Write(conditions), run_time=0.6)
        self.play(Write(equivalent), run_time=0.7)
        self.play(Write(check), FadeIn(explanation), run_time=0.8)
        self.wait(1.0)
        self._clear(title, formula, conditions, equivalent, check, explanation)

    def show_logarithm_graph_solution(self):
        title = self._title("图像法：交点的横坐标为 8", LOG)
        axes = Axes(x_range=[0, 10, 2], y_range=[-1, 4, 1],
                    x_length=6, y_length=5.6,
                    axis_config={"color": GRAY_B}, tips=False).move_to(DOWN * 0.2)
        # x≥1/2 保证 log₂x≥-1；禁止用 x≤0 时返回 0 伪造函数值。
        graph = axes.plot(lambda x: math.log2(x), x_range=[0.5, 10], color=LOG, stroke_width=4)
        level = DashedLine(axes.c2p(0, 3), axes.c2p(10, 3), color=EXP)
        vertical = DashedLine(axes.c2p(8, 0), axes.c2p(8, 3), color=GRAY_A)
        dot = Dot(axes.c2p(8, 3), color=GOOD, radius=0.1)
        label = MathTex(r"(8,3)", font_size=30, color=GOOD).next_to(dot, UL, buff=0.2)
        answer = MathTex(r"x=8\quad (x>0)", font_size=38, color=GOOD).move_to(DOWN * 5)
        self.play(Write(title), Create(axes), run_time=1.0)
        self.play(Create(graph), run_time=1.1)
        self.play(Create(level), run_time=0.7)
        self.play(Create(vertical), FadeIn(dot), Write(label), run_time=0.9)
        self.play(Write(answer), run_time=0.6)
        self.wait(0.9)
        self._clear(title, axes, graph, level, vertical, dot, label, answer)

    def show_verification_outro(self):
        title = self._title("验根：代数候选值不一定合法", WARN)
        original = MathTex(r"\log_2(x-1)+\log_2(x-3)=3", font_size=35, color=WHITE)
        fit(original).move_to(UP * 4.7)
        domain = MathTex(r"x>3", font_size=36, color=WARN).move_to(UP * 3.4)
        transformed = MathTex(r"(x-1)(x-3)=8", font_size=37).move_to(UP * 1.7)
        roots = MathTex(r"x^2-4x-5=0\ \Rightarrow\ x=5\ \text{or}\ x=-1", font_size=30)
        fit(roots).move_to(UP * 0.2)
        rejected = MathTex(r"x=-1\notin(3,+\infty)", font_size=32, color=WARN).move_to(DOWN * 1.7)
        accepted = MathTex(r"x=5:\ \log_2 4+\log_2 2=3", font_size=32, color=GOOD)
        fit(accepted).move_to(DOWN * 3.2)
        finish = cn("代回原方程，确认真数均为正", 27, GOOD).move_to(DOWN * 4.6)
        self.play(Write(title), Write(original), run_time=0.9)
        self.play(Write(domain), run_time=0.6)
        self.play(Write(transformed), run_time=0.6)
        self.play(Write(roots), run_time=0.8)
        self.play(Write(rejected), Write(accepted), run_time=0.9)
        self.play(FadeIn(finish), run_time=0.6)
        self.wait(1.2)
        self._clear(title, original, domain, transformed, roots, rejected, accepted,
                    finish, self.author_info)
