"""高一第二学期：反函数（竖屏教学动画）。

数学约定：f:A→B，其中 B=f(A)；当 f 在 A 上单射时，f^{-1}:B→A 存在。
运行：manim -ql inverse_functions.py InverseFunctions
真实渲染、字体、关键帧及音轨须在目标环境另行验收。
"""
from manim import *
import math

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
BLUE = "#3498db"
RED = "#e74c3c"
GREEN = "#2ecc71"
PURPLE = "#ab86f7"


def cn(value, size=28, color=WHITE):
    """中文与数学公式分离，避免默认 MathTex 的 CJK 编译失败。"""
    return Text(value, font=FONT, font_size=size, color=color)


def fitted(mobject, width=7.6):
    if mobject.width > width:
        mobject.scale_to_fit_width(width)
    return mobject


class InverseFunctions(Scene):
    """保持仓库已有 Scene 入口和原七段教学结构。"""

    def construct(self):
        self.camera.background_color = BG
        self.author_info = fitted(cn(f"{AUTHOR_NAME} {AUTHOR_ID}", 17, GRAY_B))
        self.author_info.move_to(UP * 7.45)
        self.add(self.author_info)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_symmetry()
        self.scene_4_verification()
        self.scene_5_properties()
        self.scene_6_monotonic()
        self.scene_7_outro()

    def _title(self, text):
        return fitted(cn(text, 37, BLUE)).move_to(UP * 6.45)

    def _clear(self, *objects):
        self.play(*[FadeOut(obj) for obj in objects], run_time=0.5)

    def scene_1_opening(self):
        title = self._title("反函数：把输入和输出交换")
        question = cn("已知指数函数", 33).move_to(UP * 3.9)
        original = MathTex(r"y=2^x", font_size=47, color=BLUE).move_to(UP * 2.4)
        step = MathTex(r"x=\log_2 y\quad(y>0)", font_size=37, color=RED).move_to(UP * 0.7)
        answer = MathTex(r"f^{-1}(x)=\log_2 x\quad(x>0)", font_size=34, color=GREEN).move_to(DOWN * 1.3)
        caption = cn("交换变量名称后，定义域也随之交换", 24, GRAY_A).move_to(DOWN * 3.0)
        self.play(Write(title), FadeIn(question), run_time=0.8)
        self.play(Write(original), run_time=0.7)
        self.play(Write(step), run_time=0.8)
        self.play(Write(answer), FadeIn(caption), run_time=0.9)
        self.wait(1.0)
        self._clear(title, question, original, step, answer, caption)

    def scene_2_definition(self):
        title = self._title("定义：每个输出有唯一的输入")
        condition = fitted(MathTex(r"f:A\to B,\qquad B=f(A)", font_size=36)).move_to(UP * 4.5)
        mapping = MathTex(r"x\in A\quad\xrightarrow{\quad f\quad}\quad y\in B", font_size=36, color=BLUE).move_to(UP * 2.8)
        reverse = MathTex(r"y\in B\quad\xrightarrow{\quad f^{-1}\quad}\quad x\in A", font_size=34, color=RED).move_to(UP * 1.1)
        criterion = fitted(cn("若每个 y∈B 恰有一个 x∈A 与之对应", 26, GREEN)).move_to(DOWN * 0.8)
        formula = MathTex(r"y=f(x)\iff x=f^{-1}(y)", font_size=37, color=YELLOW).move_to(DOWN * 2.3)
        domains = VGroup(
            cn("原函数的定义域 A = 反函数的值域", 23),
            cn("原函数的值域 B = 反函数的定义域", 23),
        ).arrange(DOWN, buff=0.28).move_to(DOWN * 4.3)
        self.play(Write(title), Write(condition), run_time=1)
        self.play(Write(mapping), run_time=0.8)
        self.play(Write(reverse), run_time=0.8)
        self.play(FadeIn(criterion), Write(formula), run_time=1.0)
        self.play(FadeIn(domains), run_time=0.8)
        self.wait(1.1)
        self._clear(title, condition, mapping, reverse, criterion, formula, domains)

    def scene_3_symmetry(self):
        title = self._title("图像关于 y = x 对称")
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 5, 1],
            x_length=5.6, y_length=5.6,
            axis_config={"color": GRAY_B, "stroke_width": 2}, tips=False,
        ).move_to(DOWN * 0.35)
        # 最大函数值不超过 y 轴上限 5；对数曲线也严格位于所设轴域内。
        exp_end = math.log2(5.0)
        original = axes.plot(lambda x: 2**x, x_range=[-1, exp_end], color=BLUE, stroke_width=4)
        inverse = axes.plot(lambda x: math.log2(x), x_range=[0.5, 5], color=RED, stroke_width=4)
        diagonal = DashedLine(axes.c2p(-1, -1), axes.c2p(5, 5), color=YELLOW, stroke_width=2)
        axis_label = MathTex(r"y=x", font_size=24, color=YELLOW).next_to(axes.c2p(3.7, 3.7), UL, buff=0.12)
        labels = VGroup(
            MathTex(r"y=2^x", font_size=28, color=BLUE),
            MathTex(r"y=\log_2 x", font_size=28, color=RED),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 5.05)
        explanation = cn("交换坐标：(a,b) ↔ (b,a)", 25, GREEN).move_to(UP * 4.35)
        self.play(Write(title), Create(axes), run_time=1)
        self.play(Create(diagonal), FadeIn(axis_label), run_time=0.7)
        self.play(Create(original), FadeIn(labels[0]), run_time=1.0)
        self.play(Create(inverse), FadeIn(labels[1]), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.6)
        # 三组点均在真实曲线上且关于同一条 y=x 交换坐标。
        for x, y in [(0, 1), (1, 2), (2, 4)]:
            source = Dot(axes.c2p(x, y), color=BLUE, radius=0.07)
            reflected = Dot(axes.c2p(y, x), color=RED, radius=0.07)
            bridge = DashedLine(source.get_center(), reflected.get_center(), color=PURPLE)
            self.play(FadeIn(source), Create(bridge), FadeIn(reflected), run_time=0.55)
            self.wait(0.12)
            self._clear(source, bridge, reflected)
        self.wait(0.6)
        self._clear(title, axes, diagonal, axis_label, original, inverse, labels, explanation)

    def scene_4_verification(self):
        title = self._title("用点对验证交换坐标")
        data = [(0, 1), (1, 2), (2, 4)]
        rows = VGroup(*[
            MathTex(fr"({x},{y})\longleftrightarrow({y},{x})", font_size=38, color=WHITE)
            for x, y in data
        ]).arrange(DOWN, buff=0.8).move_to(UP * 1.9)
        identity = MathTex(r"(a,b)\in G_f\iff (b,a)\in G_{f^{-1}}", font_size=31, color=GREEN)
        fitted(identity).move_to(DOWN * 2.25)
        caption = cn("对称轴是 y=x；仅靠几个点不能代替一般证明", 23, GRAY_A)
        fitted(caption).move_to(DOWN * 3.9)
        self.play(Write(title), run_time=0.6)
        for row in rows:
            self.play(Write(row), run_time=0.6)
        self.play(Write(identity), FadeIn(caption), run_time=0.9)
        self.wait(1.2)
        self._clear(title, rows, identity, caption)

    def scene_5_properties(self):
        title = self._title("反函数的三个基本性质")
        line1 = MathTex(r"f^{-1}(f(x))=x,\quad x\in A", font_size=32, color=GREEN)
        line2 = MathTex(r"f(f^{-1}(y))=y,\quad y\in B", font_size=32, color=GREEN)
        line3 = MathTex(r"(f^{-1})^{-1}=f", font_size=36, color=YELLOW)
        formulas = VGroup(line1, line2, line3).arrange(DOWN, buff=0.8).move_to(UP * 1.3)
        example = MathTex(r"2^{\log_2 4}=4,\qquad\log_2 2^3=3", font_size=31, color=BLUE)
        fitted(example).move_to(DOWN * 3.1)
        note = cn("复合恒等式的自变量必须在对应定义域内", 24, GRAY_A)
        fitted(note).move_to(DOWN * 4.4)
        self.play(Write(title), run_time=0.6)
        for formula in formulas:
            self.play(Write(formula), run_time=0.65)
        self.play(Write(example), FadeIn(note), run_time=0.9)
        self.wait(1.2)
        self._clear(title, formulas, example, note)

    def scene_6_monotonic(self):
        title = self._title("严格单调是充分条件")
        note = fitted(cn("严格单调 ⇒ 单射 ⇒ 在自身值域上有反函数", 25, GREEN)).move_to(UP * 4.7)
        axes = Axes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], x_length=4, y_length=4,
                    axis_config={"color": GRAY_B}, tips=False).move_to(UP * 0.6)
        increasing = axes.plot(lambda x: x / 2, x_range=[-2, 2], color=GREEN, stroke_width=4)
        parabola = axes.plot(lambda x: x * x - 1, x_range=[-1.5, 1.5], color=RED, stroke_width=4)
        test_line = DashedLine(axes.c2p(-1.5, 0), axes.c2p(1.5, 0), color=YELLOW)
        first = cn("严格递增：每条水平线至多交一个点", 23, GREEN).move_to(DOWN * 3.55)
        second = cn("整个实数域上的 x²−1：水平线可交两个点", 22, RED).move_to(DOWN * 4.5)
        self.play(Write(title), FadeIn(note), Create(axes), run_time=1.1)
        self.play(Create(increasing), FadeIn(first), run_time=0.9)
        self.wait(0.6)
        self._clear(increasing, first)
        self.play(Create(parabola), Create(test_line), FadeIn(second), run_time=1.0)
        self.wait(1.2)
        self._clear(title, note, axes, parabola, test_line, second)

    def scene_7_outro(self):
        title = self._title("反函数 · 核心回顾")
        lines = VGroup(
            cn("① 每个输出对应唯一输入", 29, BLUE),
            cn("② 定义域与值域交换", 29, GREEN),
            cn("③ 图像关于 y=x 对称", 29, YELLOW),
            cn("④ 严格单调是充分而非必要条件", 24, RED),
        ).arrange(DOWN, buff=0.75).move_to(UP * 1.0)
        final = MathTex(r"f^{-1}(f(x))=x\quad(x\in A)", font_size=32, color=WHITE).move_to(DOWN * 4.35)
        self.play(Write(title), run_time=0.6)
        for item in lines:
            self.play(FadeIn(item, shift=UP * 0.15), run_time=0.45)
        self.play(Write(final), run_time=0.8)
        self.wait(1.1)
        self._clear(title, lines, final, self.author_info)
