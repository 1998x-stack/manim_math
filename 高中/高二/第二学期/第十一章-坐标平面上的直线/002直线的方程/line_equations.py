"""高二下《直线的方程》：五种形式及各自适用条件（Manim 0.19.x）。

数学模型独立于 Manim；保留 LineEquations 入口及原八个教学分镜。
旧视频、音轨及课程原始提示不随源码修改。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_PS = "#e74c3c"
C_SI = "#3498db"
C_TP = "#2ecc71"
C_IC = "#f39c12"
C_GN = "#9b59b6"
FONT = "PingFang SC"


def coefficients_through_points(p, q):
    """返回 Ax+By+C=0 的系数；同一点不能确定唯一的直线。"""
    x1, y1 = p
    x2, y2 = q
    if x1 == x2 and y1 == y2:
        raise ValueError("两个重合点不能确定唯一直线")
    return y1 - y2, x2 - x1, x1 * y2 - x2 * y1


def slope_intercept(coefficients):
    """垂直线不能写成 y=kx+b，返回 None；禁止零法向量。"""
    a, b, c = coefficients
    if a == 0 and b == 0:
        raise ValueError("一般式要求 A、B 不同时为零")
    if b == 0:
        return None
    return -a / b, -c / b


def intercepts(coefficients):
    """仅当 x、y 截距均非零时，才能写 x/a+y/b=1。"""
    a, b, c = coefficients
    if a == 0 or b == 0 or c == 0:
        raise ValueError("截距式要求 A、B、C 均非零")
    return -c / a, -c / b


def clip_line(coefficients, x_bounds=(-4.0, 4.0), y_bounds=(-2.0, 5.0)):
    """与数据坐标矩形求交；不把越界端点交给 Manim 裁剪。"""
    a, b, c = coefficients
    if a == 0 and b == 0:
        raise ValueError("一般式要求 A、B 不同时为零")
    xmin, xmax = x_bounds
    ymin, ymax = y_bounds
    if not xmin < xmax or not ymin < ymax:
        raise ValueError("坐标窗口必须非退化")
    points = []
    if b != 0:
        for x in (xmin, xmax):
            y = -(a * x + c) / b
            if ymin - 1e-10 <= y <= ymax + 1e-10:
                points.append((x, min(ymax, max(ymin, y))))
    if a != 0:
        for y in (ymin, ymax):
            x = -(b * y + c) / a
            if xmin - 1e-10 <= x <= xmax + 1e-10:
                points.append((min(xmax, max(xmin, x)), y))
    unique = []
    for p in points:
        if not any(math.dist(p, q) < 1e-9 for q in unique):
            unique.append(p)
    if len(unique) < 2:
        raise ValueError("直线与坐标窗口没有非退化交段")
    return max(
        ((p, q) for i, p in enumerate(unique) for q in unique[i + 1:]),
        key=lambda pq: math.dist(*pq),
    )


class LineEquations(Scene):
    """八镜教学：点斜式、斜截式、两点式、截距式、一般式及总结。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author_banner = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=17, color=GRAY_B,
        ).move_to(UP * 6.95)
        self.add(self.author_banner)
        self.scene_opening()
        self.scene_point_slope()
        self.scene_slope_intercept()
        self.scene_two_point()
        self.scene_intercept()
        self.scene_general()
        self.scene_summary()
        self.scene_outro()

    def cn(self, text, size=26, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def clear_stage(self):
        visible = [item for item in self.mobjects if item is not self.author_banner]
        if visible:
            self.play(*[FadeOut(item) for item in visible], run_time=0.45)

    def heading(self, name, color=GOLD):
        self.clear_stage()
        title = self.cn(name, size=36, color=color).move_to(UP * 6.05)
        self.play(FadeIn(title), run_time=0.4)
        return title

    def axes(self):
        ax = Axes(
            x_range=[-4, 4, 1], y_range=[-2, 5, 1],
            x_length=6.0, y_length=5.0,
            axis_config={"include_numbers": True, "font_size": 18, "color": GRAY_B},
            tips=False,
        ).move_to(UP * 1.35)
        self.play(Create(ax), run_time=0.7)
        return ax

    def draw_line(self, ax, coeff, color):
        p, q = clip_line(coeff)
        line = Line(ax.c2p(*p), ax.c2p(*q), color=color, stroke_width=5)
        self.play(Create(line), run_time=0.65)
        return line

    def mark(self, ax, point, name, direction=UR, color=YELLOW):
        dot = Dot(ax.c2p(*point), radius=0.09, color=color)
        label = MathTex(name, font_size=23, color=color).next_to(dot, direction, buff=0.13)
        self.play(FadeIn(dot), FadeIn(label), run_time=0.35)
        return dot, label

    def formula(self, label, expression, explanation, color, size=31):
        panel = RoundedRectangle(
            width=8.0, height=2.45, corner_radius=0.15,
            fill_color="#16213e", fill_opacity=0.95,
            stroke_color=color, stroke_width=2,
        ).move_to(DOWN * 4.75)
        heading = self.cn(label, 23, color).move_to(panel.get_center() + UP * 0.77)
        math_label = MathTex(expression, font_size=size).move_to(panel.get_center() + UP * 0.10)
        note = self.cn(explanation, 20, GRAY_A).move_to(panel.get_center() + DOWN * 0.77)
        math_label.scale_to_fit_width(min(math_label.width, 7.5))
        self.play(FadeIn(panel), FadeIn(heading), Write(math_label), FadeIn(note), run_time=0.85)
        return VGroup(panel, heading, math_label, note)

    def scene_opening(self):
        self.heading("直线的方程：五种形式")
        prompts = VGroup(*[
            self.cn(text, 27, color)
            for text, color in (
                ("① 点斜式：一点与斜率", C_PS),
                ("② 斜截式：斜率与纵截距", C_SI),
                ("③ 两点式：两个不同点", C_TP),
                ("④ 截距式：两个非零截距", C_IC),
                ("⑤ 一般式：包括垂直线", C_GN),
            )
        ]).arrange(DOWN, buff=0.45).move_to(UP * 0.6)
        for line in prompts:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(0.9)

    def scene_point_slope(self):
        self.heading("① 点斜式", C_PS)
        ax = self.axes()
        self.draw_line(ax, (-2, 1, 0), C_PS)  # y=2x
        self.mark(ax, (1, 2), r"P(1,2)", UR)
        self.mark(ax, (0, 0), r"O(0,0)", DL, C_PS)
        right = DashedLine(ax.c2p(0, 0), ax.c2p(1, 0), color=GRAY_A)
        rise = DashedLine(ax.c2p(1, 0), ax.c2p(1, 2), color=GRAY_A)
        self.play(Create(right), Create(rise), run_time=0.5)
        self.formula("已知 P(1,2)，斜率 k=2", r"y-2=2(x-1)",
                     "点斜式要求斜率存在；本例化简为 y=2x", C_PS)
        self.wait(1.0)

    def scene_slope_intercept(self):
        self.heading("② 斜截式", C_SI)
        ax = self.axes()
        self.draw_line(ax, (1, -1, 3), C_SI)  # y=x+3
        self.mark(ax, (0, 3), r"(0,3)", UR)
        self.formula("斜率 k=1，纵截距 b=3", r"y=kx+b=x+3",
                     "纵截距是交点的纵坐标，可正可负或为零", C_SI)
        self.wait(1.0)

    def scene_two_point(self):
        self.heading("③ 两点式", C_TP)
        ax = self.axes()
        p, q = (-1, 1), (2, 4)
        coeff = coefficients_through_points(p, q)
        self.draw_line(ax, coeff, C_TP)
        self.mark(ax, p, r"P_1(-1,1)", DL)
        self.mark(ax, q, r"P_2(2,4)", UR)
        corner = (q[0], p[1])
        self.play(Create(DashedLine(ax.c2p(*p), ax.c2p(*corner), color=GRAY_A)),
                  Create(DashedLine(ax.c2p(*corner), ax.c2p(*q), color=GRAY_A)),
                  run_time=0.45)
        self.formula("两点确定一条直线", r"3(y-1)=3(x+1)",
                     "交叉相乘适用于水平线和垂直线", C_TP)
        self.wait(0.45)
        self.play(Write(MathTex(r"y=x+2", color=C_TP, font_size=30).move_to(DOWN * 2.9)),
                  run_time=0.5)
        self.wait(0.8)

    def scene_intercept(self):
        self.heading("④ 截距式", C_IC)
        ax = self.axes()
        self.draw_line(ax, (2, 3, -6), C_IC)
        self.mark(ax, (3, 0), r"(3,0)", DR, C_IC)
        self.mark(ax, (0, 2), r"(0,2)", UL, C_IC)
        self.formula("横截距 a=3，纵截距 b=2", r"\frac{x}{3}+\frac{y}{2}=1",
                     "a、b 都必须非零；过原点的直线不适用", C_IC)
        self.wait(1.0)

    def scene_general(self):
        self.heading("⑤ 一般式", C_GN)
        ax = self.axes()
        self.draw_line(ax, (2, 3, -6), C_GN)
        self.mark(ax, (3, 0), r"(3,0)", DR, C_GN)
        self.mark(ax, (0, 2), r"(0,2)", UL, C_GN)
        self.formula("与上一镜截距式表示同一条直线", r"2x+3y-6=0",
                     "Ax+By+C=0，A、B 不同时为零", C_GN)
        self.wait(0.5)
        self.play(Write(MathTex(r"x=3\;(A=1,B=0,C=-3)", font_size=28,
                                color=C_GN).move_to(DOWN * 2.9)), run_time=0.5)
        self.wait(0.8)

    def scene_summary(self):
        self.heading("五种形式：条件决定写法")
        rows = (
            ("点斜式", r"y-y_0=k(x-x_0)", "斜率存在", C_PS),
            ("斜截式", r"y=kx+b", "斜率存在", C_SI),
            ("两点式", r"(y-y_1)(x_2-x_1)=(x-x_1)(y_2-y_1)", "两点不同", C_TP),
            ("截距式", r"\frac{x}{a}+\frac{y}{b}=1", "a、b非零", C_IC),
            ("一般式", r"Ax+By+C=0", "A、B不同时为零", C_GN),
        )
        for index, (name, expression, condition, color) in enumerate(rows):
            y = 4.65 - index * 2.12
            panel = RoundedRectangle(width=8.0, height=1.82, corner_radius=0.12,
                                     fill_color="#16213e", fill_opacity=0.95,
                                     stroke_color=color, stroke_width=1.5).move_to(UP * y)
            title = self.cn(name, 21, color).move_to(panel.get_center() + UP * 0.55)
            equation = MathTex(expression, font_size=26).move_to(panel.get_center())
            equation.scale_to_fit_width(min(equation.width, 7.5))
            note = self.cn(condition, 19, GRAY_B).move_to(panel.get_center() + DOWN * 0.58)
            self.play(FadeIn(VGroup(panel, title, equation, note)), run_time=0.28)
        self.wait(1.7)

    def scene_outro(self):
        self.clear_stage()
        heading = self.cn("一条直线，多种写法", 39, GOLD).move_to(UP * 2.2)
        message = self.cn("先核实条件，再选择方程形式", 27).move_to(UP * 0.8)
        byline = self.cn("@emptyandcalm", 27, GRAY_A).move_to(DOWN * 0.8)
        self.play(Write(heading), FadeIn(message), FadeIn(byline), run_time=0.9)
        self.wait(1.5)
