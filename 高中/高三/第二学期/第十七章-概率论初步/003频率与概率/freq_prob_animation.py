"""频率与概率：公平硬币的可复现抽样与大数定律的正确表述。

预览：manim -pql freq_prob_animation.py FreqProbAnimation
纯数学测试：python -m unittest -v test_frequency_math.py
"""
from manim import *

from frequency_math import benchmark_probability, experiment

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
CARD = "#16213e"
RED = "#ef6b68"
BLUE = "#56a5e8"
GOLD = "#f1c40f"
GREEN = "#58d68d"


class FreqProbAnimation(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.data = experiment(200, seed=42)
        self.p = benchmark_probability()
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_simulation_small_n()
        self.scene_4_law_of_large_numbers()
        self.scene_5_summary()
        self.scene_6_outro()

    def text(self, message, y, size=27, color=WHITE):
        mob = Text(message, font=FONT, font_size=size, color=color)
        mob.move_to(UP * y)
        return self.fit(mob)

    def math(self, expression, y, size=35, color=WHITE):
        """仅传纯 LaTeX；中文一律交给 text。"""
        return self.fit(MathTex(expression, font_size=size, color=color).move_to(UP * y))

    def fit(self, mob):
        """单对象竖屏安全区约束，不能替代逐帧视觉复核。"""
        if mob.width > 7.8:
            mob.scale_to_fit_width(7.8)
        if mob.height > 13.4:
            mob.scale_to_fit_height(13.4)
        if mob.get_left()[0] < -3.9:
            mob.shift(RIGHT * (-3.9 - mob.get_left()[0]))
        if mob.get_right()[0] > 3.9:
            mob.shift(LEFT * (mob.get_right()[0] - 3.9))
        if mob.get_top()[1] > 6.8:
            mob.shift(DOWN * (mob.get_top()[1] - 6.8))
        if mob.get_bottom()[1] < -6.8:
            mob.shift(UP * (-6.8 - mob.get_bottom()[1]))
        return mob

    def show(self, mob, seconds=0.5):
        self.play(FadeIn(self.fit(mob)), run_time=seconds)
        return mob

    def page(self, title, color=GOLD):
        if self.mobjects:
            self.play(*[FadeOut(m) for m in tuple(self.mobjects)], run_time=0.3)
        self.show(self.text("上海初高中数学直通车  @emptyandcalm", 6.5, 19, GRAY_B), 0.15)
        self.show(self.text(title, 5.45, 39, color), 0.4)

    def formula_card(self, formula, y, color=GREEN):
        inner = MathTex(formula, font_size=35)
        if inner.width > 7.1:
            inner.scale_to_fit_width(7.1)
        box = RoundedRectangle(
            width=min(7.8, inner.width + 0.5), height=inner.height + 0.45,
            corner_radius=0.15, stroke_color=color, stroke_width=2,
            fill_color=CARD, fill_opacity=1,
        )
        return VGroup(box, inner).move_to(UP * y)

    def scene_1_opening(self):
        self.page("频率与概率")
        self.show(self.text("抛一枚公平硬币 1000 次", 3.25, 34))
        self.show(self.text("正面一定出现 500 次吗？", 2.0, 31, GOLD))
        self.show(self.math(r"P(\mathrm{H})=\frac12", 0.2, 45, BLUE))
        self.show(self.text("概率为 1/2，不代表每次试验正反面各半", -1.25, 24))
        self.show(self.text("一起观察同一次模拟中的累计频率", -2.8, 25, GREEN))
        self.wait(0.8)

    def scene_2_definition(self):
        self.page("什么是频率？", GOLD)
        self.show(self.text("n 次试验中，事件 A 发生了 m 次", 3.75, 29))
        self.show(self.formula_card(r"f_n(A)=\frac{m}{n},\qquad n\geq1", 2.0))
        n, heads, freq = self.data[9]
        assert n == 10 and freq == heads / n
        self.show(self.text(f"本次模拟的前 {n} 次：正面 {heads} 次", 0.5, 27))
        self.show(self.math(r"f_{10}(A)=\frac{" + str(heads) + r"}{10}=" + f"{float(freq):.2f}",
                            -0.8, 32, RED))
        self.show(self.math(r"0\le f_n(A)\le 1", -2.3, 35, BLUE))
        self.show(self.text("频率是实际数据；概率是指定模型中的数值", -3.7, 24, GOLD))
        self.wait(0.8)

    def plot_data(self, end_n):
        """两个镜头共用 self.data 的前缀，绝不重新抽样造另一条曲线。"""
        if not 2 <= end_n <= len(self.data):
            raise ValueError("折线至少需要两个样本点")
        x_step = 5 if end_n <= 30 else 50
        axes = Axes(
            x_range=[0, end_n, x_step], y_range=[0, 1, 0.25],
            x_length=6.25, y_length=4.4,
            axis_config={"color": GRAY_B, "include_tip": False},
        ).move_to(UP * 0.7)
        baseline = DashedLine(axes.c2p(0, float(self.p)),
                              axes.c2p(end_n, float(self.p)), color=BLUE)
        points = [axes.c2p(n, float(freq)) for n, _, freq in self.data[:end_n]]
        polyline = VMobject(color=RED, stroke_width=3)
        polyline.set_points_as_corners(points)
        return axes, baseline, polyline

    def scene_3_simulation_small_n(self):
        self.page("小样本：频率会波动", RED)
        axes, baseline, line = self.plot_data(30)
        self.show(axes, 0.7)
        self.show(baseline, 0.35)
        self.show(self.math(r"P(A)=0.5", 3.8, 29, BLUE))
        self.play(Create(line), run_time=2.0)
        self.show(self.text("红线：同一次模拟的累计正面频率", -2.3, 23, RED))
        n, heads, freq = self.data[29]
        self.show(self.text(f"n={n}，正面 {heads} 次，频率 {float(freq):.3f}", -3.45, 26, GOLD))
        self.show(self.text("频率可能向理论值靠近，也可能暂时远离", -4.6, 23))
        self.wait(0.9)

    def scene_4_law_of_large_numbers(self):
        self.page("继续观察：200 次模拟", BLUE)
        axes, baseline, line = self.plot_data(200)
        self.show(axes, 0.7)
        self.show(baseline, 0.3)
        self.show(self.math(r"P(A)=0.5", 3.8, 29, BLUE))
        self.play(Create(line), run_time=3.0)
        checkpoints = (10, 50, 100, 200)
        for n in checkpoints:
            _, heads, freq = self.data[n - 1]
            assert freq == heads / n
        n, heads, freq = self.data[-1]
        self.show(self.text(f"本次 n={n}，正面 {heads} 次，频率 {float(freq):.3f}", -2.4, 26, RED))
        self.show(self.math(r"f_n(A)\xrightarrow[n\to\infty]{\mathrm{P}}P(A)",
                            -3.65, 34, GOLD))
        self.show(self.text("独立、同分布且概率固定：频率依概率收敛", -4.65, 22))
        self.show(self.text("这不是逐次靠近的保证，也不是 200 次的证明", -5.55, 22, GREEN))
        self.wait(1.1)

    def scene_5_summary(self):
        self.page("频率 vs 概率", GOLD)
        self.show(self.text("频率：本次试验发生次数 / 总次数", 3.65, 28, RED))
        self.show(self.text("概率：模型规定的事件发生可能性", 2.4, 28, BLUE))
        self.show(self.formula_card(r"f_n(A)=\frac{m}{n}", 0.8, RED))
        self.show(self.formula_card(r"P(A)=\frac12\quad\text{(fair coin)}", -1.0, BLUE))
        self.show(self.text("独立重复试验下：次数增多时偏差较小的", -2.6, 24))
        self.show(self.text("概率增大；单次模拟仍可能波动", -3.4, 24, GREEN))
        self.wait(1)

    def scene_6_outro(self):
        self.page("本节要点", GREEN)
        self.show(self.math(r"f_n(A)=\frac{m}{n}", 3.2, 42, RED))
        self.show(self.math(r"0\leq f_n(A)\leq1", 1.8, 38, BLUE))
        self.show(self.text("不要把理论概率当作固定的实验次数", 0.1, 26, GOLD))
        self.show(self.text("同一实验的数据、图像、字幕应保持一致", -1.3, 25))
        self.show(self.text("@emptyandcalm", -3.0, 27, GRAY_B))
        self.wait(1.2)
