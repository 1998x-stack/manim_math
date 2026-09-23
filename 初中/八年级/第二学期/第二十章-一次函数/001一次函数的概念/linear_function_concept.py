"""八年级下册：一次函数的概念。保持原有的七镜教学顺序。"""

from manim import *

# 竖屏教学画面。标题、曲线和总结均布置在 9 x 16 的安全范围内。
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def linear_value(k, b, x):
    """一次函数的函数值；允许 b=0，但一次函数必须 k!=0。"""
    if k == 0:
        raise ValueError("一次函数的斜率 k 不能为 0")
    return k * x + b


def visible_interval(k, b, x_min, x_max, y_min, y_max):
    """返回函数图像同时位于给定 x/y 轴范围内的非退化区间。"""
    if k == 0 or x_min >= x_max or y_min >= y_max:
        raise ValueError("无效的函数或坐标范围")
    x_at_bottom = (y_min - b) / k
    x_at_top = (y_max - b) / k
    start = max(x_min, min(x_at_bottom, x_at_top))
    stop = min(x_max, max(x_at_bottom, x_at_top))
    if stop <= start:
        raise ValueError("函数图像不与坐标系的可见区域相交")
    return (start, stop)


class LinearFunctionConcept(Scene):
    """正比例函数 → 平移 → 截距 → 斜率 → 通式 → 对比 → 总结。"""

    BLUE_LINE = "#3498db"
    RED_LINE = "#e74c3c"
    GREEN_B = "#2ecc71"
    ORANGE_K = "#f39c12"

    def caption(self, words, y=-4.5, color=WHITE, size=26):
        return Text(words, color=color, font_size=size).move_to(UP * y)

    def graph(self, k, b, color, x_min=-3, x_max=3):
        # 同时裁剪 x、y：画出的端点与坐标轴刻度始终一致。
        domain = visible_interval(k, b, x_min, x_max, -3, 3)
        return self.axes.plot(lambda x: linear_value(k, b, x),
                              x_range=list(domain), color=color, stroke_width=4)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author = self.caption("上海初高中数学直通车 @emptyandcalm", 7.05,
                                   GRAY_B, 18)
        self.axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                         x_length=6.4, y_length=5.4, tips=False,
                         axis_config={"include_numbers": False, "stroke_width": 2,
                                      "stroke_color": GRAY_A}).move_to(DOWN * 0.35)
        self.axes_labels = VGroup(
            Text("x", font_size=20).next_to(self.axes.x_axis.get_end(), RIGHT, buff=.1),
            Text("y", font_size=20).next_to(self.axes.y_axis.get_end(), UP, buff=.1),
        )
        self.scene_1_opening()
        self.scene_2_introduction()
        self.scene_3_intercept()
        self.scene_4_slope()
        self.scene_5_complete_formula()
        self.scene_6_comparison()
        self.scene_7_outro()

    def scene_1_opening(self):
        hook = self.caption("正比例函数的图像\n一定过原点吗？", 5.4, YELLOW, 34)
        self.play(FadeIn(self.author), Write(hook), run_time=1.0)
        self.play(Create(self.axes), FadeIn(self.axes_labels), run_time=.9)
        self.proportional_graph = self.graph(2, 0, self.RED_LINE, -1, 1)
        origin = Dot(self.axes.c2p(0, 0), color=self.RED_LINE)
        origin_label = MathTex("O", font_size=24).next_to(origin, DL, buff=.1)
        self.play(Create(self.proportional_graph), FadeIn(origin),
                  FadeIn(origin_label), run_time=1.1)
        self.wait(.5)
        self.play(FadeOut(hook), FadeOut(origin), FadeOut(origin_label), run_time=.5)

    def scene_2_introduction(self):
        self.title = self.caption("一次函数", 5.6, WHITE, 36)
        formula = MathTex(r"y=kx+b\quad(k\ne 0)", font_size=34).next_to(
            self.title, DOWN, buff=.35)
        note = self.caption("正比例函数向上平移 1 个单位", -4.5, GRAY_A)
        self.play(Write(self.title), FadeIn(formula), FadeIn(note), run_time=.8)
        self.linear_graph = self.proportional_graph.copy()
        self.add(self.linear_graph)  # 复制对象先入场，之后的 animate 才是可见对象。
        unit_y = self.axes.c2p(0, 1) - self.axes.c2p(0, 0)
        self.play(self.linear_graph.animate.shift(unit_y).set_color(self.BLUE_LINE),
                  run_time=1.2)
        label = MathTex("y=2x+1", color=self.BLUE_LINE, font_size=27).next_to(
            self.axes.c2p(.6, 2.2), RIGHT, buff=.15)
        arrow = Arrow(self.axes.c2p(0, 0), self.axes.c2p(0, 1), buff=0,
                      color=YELLOW, stroke_width=3)
        self.play(FadeIn(label), GrowArrow(arrow), run_time=.6)
        self.wait(.6)
        self.play(FadeOut(note), FadeOut(formula), FadeOut(label),
                  FadeOut(arrow), run_time=.5)

    def scene_3_intercept(self):
        note = self.caption("截距 b：与 y 轴交点的纵坐标", 4.6, self.GREEN_B)
        self.play(FadeIn(note), self.proportional_graph.animate.set_opacity(.3),
                  run_time=.6)
        self.intercept_dot = Dot(self.axes.c2p(0, 1), color=self.GREEN_B,
                                 radius=.10)
        point_label = MathTex(r"(0,1),\ b=1", color=self.GREEN_B,
                              font_size=28).next_to(self.intercept_dot, RIGHT, buff=.25)
        fact = self.caption("当 x=0 时，y=b", -4.8, GRAY_A)
        self.play(FadeIn(self.intercept_dot), FadeIn(point_label), run_time=.6)
        self.play(FadeIn(fact), run_time=.4)
        self.wait(.7)
        self.play(FadeOut(note), FadeOut(point_label), FadeOut(fact), run_time=.5)

    def scene_4_slope(self):
        note = self.caption("斜率 k：纵向变化量 ÷ 横向变化量", 4.6,
                            self.ORANGE_K, 24)
        a = self.axes.c2p(0, 1)
        b = self.axes.c2p(1, 1)
        c = self.axes.c2p(1, 3)
        triangle = Polygon(a, b, c, stroke_color=self.ORANGE_K,
                           stroke_width=3, fill_color=self.ORANGE_K,
                           fill_opacity=.15)
        marker = Dot(c, radius=.08, color=self.ORANGE_K)
        p_label = MathTex("(1,3)", color=self.ORANGE_K, font_size=24).next_to(
            marker, RIGHT, buff=.1)
        dx = MathTex(r"\Delta x=1", color=self.ORANGE_K, font_size=25).next_to(
            Line(a, b), DOWN, buff=.12)
        dy = MathTex(r"\Delta y=2", color=self.ORANGE_K, font_size=25).next_to(
            Line(b, c), RIGHT, buff=.12)
        equation = MathTex(r"k=\frac{\Delta y}{\Delta x}=\frac{2}{1}=2",
                           color=self.ORANGE_K, font_size=31).move_to(DOWN * 5.3)
        self.play(FadeIn(note), FadeIn(marker), FadeIn(p_label),
                  Create(triangle), run_time=.8)
        self.play(FadeIn(dx), FadeIn(dy), Write(equation), run_time=.9)
        self.wait(.8)
        self.play(*[FadeOut(item) for item in
                    (note, marker, p_label, triangle, dx, dy, equation)], run_time=.5)

    def scene_5_complete_formula(self):
        formula = MathTex("y=", "k", "x+", "b", font_size=43).move_to(UP * 5.2)
        formula[1].set_color(self.ORANGE_K)
        formula[3].set_color(self.GREEN_B)
        k_box = SurroundingRectangle(formula[1], buff=.12, color=self.ORANGE_K)
        b_box = SurroundingRectangle(formula[3], buff=.12, color=self.GREEN_B)
        k_name = self.caption("k：斜率，k ≠ 0", -4.3, self.ORANGE_K)
        b_name = self.caption("b：y 轴截距，b 可以为 0", -5.1, self.GREEN_B)
        special = self.caption("当 b=0 时，y=kx 是正比例函数", -6.0,
                               self.RED_LINE, 24)
        self.play(FadeOut(self.title), Write(formula), run_time=.8)
        self.play(Create(k_box), FadeIn(k_name), run_time=.5)
        self.play(Create(b_box), FadeIn(b_name), FadeIn(special), run_time=.6)
        self.wait(.8)
        self.play(*[FadeOut(obj) for obj in
                    (formula, k_box, b_box, k_name, b_name, special)], run_time=.5)

    def scene_6_comparison(self):
        self.play(FadeOut(self.proportional_graph), FadeOut(self.linear_graph),
                  FadeOut(self.intercept_dot), run_time=.5)
        specs = [
            (1, 1, self.GREEN_B, r"y=x+1"),
            (-1, 2, self.RED_LINE, r"y=-x+2"),
            (.5, -1, "#9b59b6", r"y=0.5x-1"),
            (-2, 0, self.ORANGE_K, r"y=-2x"),
        ]
        lines = VGroup(*[self.graph(k, b, color) for k, b, color, _ in specs])
        formulas = VGroup(*[MathTex(label, color=color, font_size=27)
                            for _, _, color, label in specs]).arrange(
            DOWN, aligned_edge=LEFT, buff=.18).move_to(DOWN * 4.8)
        headline = self.caption("比较：k 的正负决定增减方向", 5.1, YELLOW, 29)
        self.play(FadeIn(headline), run_time=.4)
        for line in lines:
            self.play(Create(line), run_time=.55)
        self.play(FadeIn(formulas), run_time=.5)
        self.play(lines[0].animate.set_stroke(width=6),
                  lines[2].animate.set_stroke(width=6), run_time=.35)
        self.wait(.5)
        self.play(lines[0].animate.set_stroke(width=4),
                  lines[2].animate.set_stroke(width=4),
                  lines[1].animate.set_stroke(width=6),
                  lines[3].animate.set_stroke(width=6), run_time=.4)
        self.wait(.6)
        self.play(FadeOut(headline), FadeOut(lines), FadeOut(formulas), run_time=.6)

    def scene_7_outro(self):
        self.play(FadeOut(self.axes), FadeOut(self.axes_labels), run_time=.5)
        title = self.caption("一次函数 · 核心回顾", 3.2, YELLOW, 37)
        facts = VGroup(
            MathTex(r"y=kx+b\quad(k\ne 0)", font_size=36),
            Text("k：斜率，决定增减方向", color=self.ORANGE_K, font_size=28),
            Text("b：与 y 轴交点的纵坐标", color=self.GREEN_B, font_size=28),
            Text("b=0 时是正比例函数", color=self.RED_LINE, font_size=28),
        ).arrange(DOWN, buff=.5).move_to(DOWN * .1)
        self.play(Write(title), run_time=.7)
        for fact in facts:
            self.play(FadeIn(fact), run_time=.5)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(facts), FadeOut(self.author), run_time=.7)
