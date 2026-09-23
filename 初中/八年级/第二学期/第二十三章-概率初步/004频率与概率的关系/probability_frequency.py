"""八年级概率：频率与概率的关系。使用独立随机生成器，数据/图像同源。

H 表示硬币正面事件；中文一律使用 Text，公式使用 MathTex。
运行：manim -ql probability_frequency.py ProbabilityFrequency
"""
from manim import *
import numpy as np

config.pixel_width, config.pixel_height = 1080, 1920
config.frame_width, config.frame_height = 9, 16
FONT = "PingFang SC"
GOLD, CYAN, GREEN, ORANGE, BG = "#f9ca24", "#22a6b3", "#6ab04c", "#f0932b", "#1a1a2e"


def simulate_frequencies(n, *, probability=0.5, seed=42):
    """独立重复伯努利试验；返回 0/1 结果及逐次累积频率，不污染全局随机状态。"""
    if type(n) is not int or n <= 0:
        raise ValueError("试验次数必须为正整数")
    if not np.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("概率必须是 [0,1] 内的有限实数")
    flips = np.random.default_rng(seed).binomial(1, probability, size=n)
    frequency = np.cumsum(flips) / np.arange(1, n + 1)
    return flips, frequency


class ProbabilityFrequency(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.flips, self.frequency = simulate_frequencies(1000, seed=42)
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=18, color=GRAY_B).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)
        self.scene_opening()
        self.scene_freq_def()
        self.scene_freq_chart()
        self.scene_limit()
        self.scene_history()
        self.scene_comparison()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    def _text(self, value, y, size=27, color=WHITE):
        return Text(value, font=FONT, font_size=size, color=color).move_to(UP * y)

    def _math(self, value, y, size=37, color=WHITE):
        return MathTex(value, font_size=size, color=color).move_to(UP * y)

    def fade_rest(self):
        visible = [mob for mob in self.mobjects if mob is not self.author]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.4)

    def _sample(self, n):
        return int(np.sum(self.flips[:n])), float(self.frequency[n - 1])

    def scene_opening(self):
        self.play(Write(self._text("硬币抛得越多，正面频率会怎样？", 5.6, 32, GOLD)),
                  FadeIn(self._text("以下是固定随机种子的模拟示例", 4.5, 23, GRAY_A)), run_time=0.8)
        for n, y in ((10, 2.7), (1000, 1.3)):
            count, f = self._sample(n)
            self.play(Write(self._math(rf"f_{{{n}}}=\frac{{{count}}}{{{n}}}={f:.3f}",
                                       y, 37, GREEN if n == 1000 else ORANGE)), run_time=0.65)
        self.play(FadeIn(self._text("频率会波动，长期总体趋近理论概率", -0.8, 26, GOLD)), run_time=0.5)
        self.wait(1.2)
        self.fade_rest()

    def scene_freq_def(self):
        self.play(Write(self._text("什么是频率？", 5.6, 39, GOLD)),
                  Write(self._math(r"f_n(A)=\frac{k}{n},\quad n>0", 3.4, 46, CYAN)), run_time=0.9)
        self.play(FadeIn(self._text("k：事件 A 实际发生的次数", 1.7, 26)),
                  FadeIn(self._text("n：试验总次数", 0.7, 26)),
                  Write(self._math(r"0\le f_n(A)\le1", -1.1, 40, GREEN)), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_freq_chart(self):
        title = self._text("同一次模拟中，频率如何变化？", 5.6, 32, GOLD)
        ax = Axes(x_range=[0, 1000, 200], y_range=[0, 1, 0.25],
                  x_length=6.6, y_length=3.4, tips=False,
                  axis_config={"include_numbers": False}).move_to(UP * 1.8)
        baseline = DashedLine(ax.c2p(0, 0.5), ax.c2p(1000, 0.5), color=GOLD, dash_length=0.1)
        ns = (10, 25, 50, 100, 200, 400, 600, 800, 1000)
        points = [ax.c2p(n, float(self.frequency[n - 1])) for n in ns]
        curve = VGroup(*[Line(start, end, color=CYAN, stroke_width=3)
                         for start, end in zip(points, points[1:])])
        dots = VGroup(*[Dot(point, radius=0.06, color=GREEN) for point in points])
        self.play(Write(title), Create(ax), Create(baseline), run_time=0.9)
        self.play(Create(curve), FadeIn(dots),
                  Write(self._math(r"P(H)=\frac12", -0.7, 34, GOLD)), run_time=1.0)
        self.play(FadeIn(self._text("H 表示正面事件；波动不保证每次更接近 0.5", -2.4, 24)), run_time=0.5)
        self.wait(1.3)
        self.fade_rest()

    def scene_limit(self):
        self.play(Write(self._text("频率为什么可以估计概率？", 5.6, 33, GOLD)),
                  FadeIn(self._text("前提：相同条件下独立重复试验，概率不变", 3.6, 24)), run_time=0.8)
        self.play(Write(self._math(r"f_n(A)\ \longrightarrow\ P(A)", 1.9, 45, GREEN)),
                  FadeIn(self._text("长期统计规律：不是每次实验都精确相等", 0.0, 24)),
                  FadeIn(self._text("样本量增加，不保证误差单调减小", -1.8, 27, ORANGE)), run_time=0.9)
        self.wait(1.3)
        self.fade_rest()

    def scene_history(self):
        """使用可复算的模拟表格，不借用未经核对的历史实验统计。"""
        self.play(Write(self._text("模拟数据：正面次数与频率", 5.6, 33, GOLD)),
                  FadeIn(self._text("试验次数       正面次数        频率", 3.9, 25, CYAN)), run_time=0.8)
        for idx, n in enumerate((10, 100, 1000)):
            count, f = self._sample(n)
            self.play(FadeIn(self._text(f"{n:4d}          {count:4d}           {f:.3f}",
                                         2.7 - 1.25 * idx, 25, GREEN)), run_time=0.45)
        self.play(FadeIn(self._text("这只是一条模拟路径，不是每次实验的固定结果", -2.1, 24, GOLD)),
                  run_time=0.4)
        self.wait(1.2)
        self.fade_rest()

    def scene_comparison(self):
        self.play(Write(self._text("频率和概率：概念不同", 5.6, 36, GOLD)),
                  FadeIn(self._text("频率：某次实验中事件发生的比例", 3.6, 27, ORANGE)),
                  FadeIn(self._text("概率：固定实验条件下的理论规律", 2.3, 27, GREEN)), run_time=0.9)
        self.play(Write(self._math(r"P(H)=\frac12", 0.7, 37, CYAN)),
                  FadeIn(self._text("某一次的频率，也可能恰好等于概率", -1.1, 26)),
                  FadeIn(self._text("P=m/N 只适用于有限等可能的样本空间", -2.4, 24, GOLD)), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_quick_practice(self):
        count, f = self._sample(100)
        self.play(Write(self._text("练习：用频率估计正面概率", 5.6, 33, GOLD)),
                  FadeIn(self._text(f"抛 100 次硬币，观察到 {count} 次正面", 3.7, 28)), run_time=0.7)
        self.play(Write(self._math(rf"f_{{100}}=\frac{{{count}}}{{100}}={f:.2f}", 1.9, 39, CYAN)),
                  Write(self._math(rf"P(H)\approx {f:.2f}", 0.2, 37, GREEN)),
                  FadeIn(self._text("估计值可能与真实概率 0.5 不同", -1.5, 26, ORANGE)), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_summary(self):
        self.play(Write(self._text("总结：统计值与理论值", 5.6, 38, GOLD)),
                  Write(self._math(r"f_n(A)=\frac{k}{n}", 3.6, 48, CYAN)), run_time=0.8)
        self.play(FadeIn(self._text("在独立重复、概率不变的条件下", 1.7, 25)),
                  Write(self._math(r"f_n(A)\ \longrightarrow\ P(A)", 0.4, 42, GREEN)),
                  FadeIn(self._text("长期趋近，不意味着每次都更接近", -1.5, 27, ORANGE)), run_time=0.9)
        self.wait(1.3)
        self.fade_rest()

    def scene_outro(self):
        self.play(FadeIn(self._text("用数据认识随机规律", 3.0, 38, GOLD)),
                  FadeIn(self._text("换一个随机种子，再比较一次试试！", 1.6, 27)), run_time=0.8)
        self.wait(1.2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.7)
