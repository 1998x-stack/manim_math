"""频率与概率的关系：八年级第二学期，第二十三章。

使用同一条独立、公平硬币模拟路径驱动所有数值和图像；不将
“样本量增加”误说成每一步的频率必然更接近概率。
运行：manim -ql probability_frequency.py ProbabilityFrequency
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
GOLD = "#f9ca24"
CYAN = "#22a6b3"
GREEN = "#6ab04c"
ORANGE = "#f0932b"
BG = "#1a1a2e"


def simulate_frequencies(n, *, probability=0.5, seed=42):
    """n 次独立伯努利试验的 0/1 结果及每一次后的累计频率。

    不修改全局 NumPy RNG；概率参数必须是区间 [0,1] 内的有限实数。
    """
    if type(n) is not int or n <= 0:
        raise ValueError("试验次数 n 必须为正整数")
    if not np.isfinite(probability) or not 0 <= probability <= 1:
        raise ValueError("概率必须是 [0,1] 内的有限数")
    flips = np.random.default_rng(seed).binomial(1, probability, size=n)
    frequency = np.cumsum(flips) / np.arange(1, n + 1)
    return flips, frequency


class ProbabilityFrequency(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.flips, self.frequency = simulate_frequencies(1000, seed=42)
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font=FONT, font_size=18, color=GRAY_B).move_to(UP * 7.0)
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
        items = [mob for mob in self.mobjects if mob is not self.author]
        if items:
            self.play(*[FadeOut(mob) for mob in items], run_time=0.4)

    def _sample(self, n):
        count = int(np.sum(self.flips[:n]))
        frequency = float(self.frequency[n - 1])
        return count, frequency

    def scene_opening(self):
        title = self._text("硬币抛得越多，正面频率会怎样？", 5.6, 32, GOLD)
        note = self._text("以下为固定随机种子的模拟示例", 4.5, 23, GRAY_A)
        self.play(Write(title), FadeIn(note), run_time=0.8)
        for n, y in ((10, 2.7), (1000, 1.3)):
            count, frequency = self._sample(n)
            equation = self._math(rf"f_{{{n}}}=\frac{{{count}}}{{{n}}}={frequency:.3f}",
                                  y, 37, GREEN if n == 1000 else ORANGE)
            self.play(Write(equation), run_time=0.65)
        self.play(FadeIn(self._text("频率会波动，长期总体趋近于理论概率", -0.8, 26, GOLD)),
                  run_time=0.5)
        self.wait(1.2)
        self.fade_rest()

    def scene_freq_def(self):
        title = self._text("什么是频率？", 5.6, 39, GOLD)
        formula = self._math(r"f_n(A)=\frac{k}{n},\quad n>0", 3.4, 46, CYAN)
        k_label = self._text("k：事件 A 在 n 次试验中发生的次数", 1.7, 25)
        n_label = self._text("n：独立重复试验的总次数", 0.7, 25)
        bound = self._math(r"0\le f_n(A)\le 1", -1.1, 40, GREEN)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(FadeIn(k_label), FadeIn(n_label), Write(bound), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_freq_chart(self):
        title = self._text("同一条模拟路径的频率变化", 5.6, 32, GOLD)
        ax = Axes(x_range=[0, 1000, 200], y_range=[0, 1, 0.25],
                  x_length=6.6, y_length=3.4, tips=False,
                  axis_config={"include_numbers": False}).move_to(UP * 1.8)
        baseline = DashedLine(ax.c2p(0, 0.5), ax.c2p(1000, 0.5),
                              color=GOLD, dash_length=0.1)
        label = self._math(r"P(\text{正面})=\frac12", -0.7, 32, GOLD)
        ns = (10, 25, 50, 100, 200, 400, 600, 800, 1000)
        points = [ax.c2p(n, float(self.frequency[n - 1])) for n in ns]
        curve = VGroup(*[Line(start, end, color=CYAN, stroke_width=3)
                         for start, end in zip(points, points[1:])])
        dots = VGroup(*[Dot(point, radius=0.06, color=GREEN) for point in points])
        explanation = self._text("上下波动是正常的，不保证每一次都更靠近 0.5", -2.4, 24)
        self.play(Write(title), Create(ax), Create(baseline), run_time=0.9)
        self.play(Create(curve), FadeIn(dots), FadeIn(label), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.3)
        self.fade_rest()

    def scene_limit(self):
        title = self._text("为什么可以用频率估计概率？", 5.6, 33, GOLD)
        assumptions = self._text("条件：同一种试验，独立重复，概率保持不变", 3.6, 24)
        rule = self._math(r"f_n(A)\ \longrightarrow\ P(A)", 1.9, 45, GREEN)
        clarification = self._text("这是长期统计规律，不是每次实验都精确相等", 0.0, 24)
        caution = self._text("样本量增加不保证误差单调减小", -1.8, 27, ORANGE)
        self.play(Write(title), FadeIn(assumptions), run_time=0.8)
        self.play(Write(rule), FadeIn(clarification), FadeIn(caution), run_time=0.9)
        self.wait(1.3)
        self.fade_rest()

    def scene_history(self):
        """展示可复现模拟数据，不冒充未经核对的历史实验记录。"""
        title = self._text("固定模拟数据：正面次数与频率", 5.6, 33, GOLD)
        self.play(Write(title), run_time=0.6)
        headers = self._text("试验次数     正面次数       频率", 3.9, 26, CYAN)
        self.play(FadeIn(headers), run_time=0.4)
        for idx, n in enumerate((10, 100, 1000)):
            count, frequency = self._sample(n)
            row = self._text(f"{n:<6}             {count:<6}       {frequency:.3f}",
                             2.7 - 1.25 * idx, 25, GREEN)
            self.play(FadeIn(row), run_time=0.45)
        self.play(FadeIn(self._text("这里只展示一次模拟，不代表每次实验的结果", -2.1, 24, GOLD)),
                  run_time=0.4)
        self.wait(1.2)
        self.fade_rest()

    def scene_comparison(self):
        title = self._text("频率与概率：概念不同", 5.6, 36, GOLD)
        frequency_label = self._text("频率：某次实验中实际发生的比例", 3.6, 27, ORANGE)
        probability_label = self._text("概率：固定实验条件下的理论规律", 2.3, 27, GREEN)
        example = self._math(r"P(\text{公平硬币正面})=\frac12", 0.7, 33, CYAN)
        equal_cases = self._text("某一次的频率也可能恰好等于概率", -1.1, 26)
        condition = self._text("P=m/N 的计数公式只适用于等可能样本空间", -2.4, 24, GOLD)
        self.play(Write(title), FadeIn(frequency_label), FadeIn(probability_label),
                  run_time=0.9)
        self.play(Write(example), FadeIn(equal_cases), FadeIn(condition), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_quick_practice(self):
        title = self._text("练习：用模拟频率估计正面概率", 5.6, 33, GOLD)
        count, frequency = self._sample(100)
        question = self._text(f"抛 100 次硬币，观察到 {count} 次正面", 3.7, 28)
        f = self._math(rf"f_{{100}}=\frac{{{count}}}{{100}}={frequency:.2f}",
                       1.9, 39, CYAN)
        p = self._math(rf"P(\text{{正面}})\approx {frequency:.2f}", 0.2, 37, GREEN)
        note = self._text("估计值可能与真实概率 0.5 有偏差", -1.5, 26, ORANGE)
        self.play(Write(title), FadeIn(question), run_time=0.7)
        self.play(Write(f), Write(p), FadeIn(note), run_time=0.9)
        self.wait(1.2)
        self.fade_rest()

    def scene_summary(self):
        title = self._text("总结：统计值与理论值", 5.6, 38, GOLD)
        formula = self._math(r"f_n(A)=\frac{k}{n}", 3.6, 48, CYAN)
        relation = self._text("在独立重复、概率不变的条件下", 1.7, 25)
        result = self._math(r"f_n(A)\ \longrightarrow\ P(A)", 0.4, 42, GREEN)
        warning = self._text("长期趋近 ≠ 每次都更接近", -1.5, 27, ORANGE)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(relation), Write(result), FadeIn(warning), run_time=0.9)
        self.wait(1.3)
        self.fade_rest()

    def scene_outro(self):
        title = self._text("用数据认识随机规律", 3.0, 38, GOLD)
        ending = self._text("下次可以试试改变随机种子再比较！", 1.6, 27)
        self.play(FadeIn(title), FadeIn(ending), run_time=0.8)
        self.wait(1.2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.7)
