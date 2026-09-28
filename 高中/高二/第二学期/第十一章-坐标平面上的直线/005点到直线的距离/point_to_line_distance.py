"""点到直线距离与平行线距离：公式、垂足和屏幕几何使用同一模型。

保留 PointToLineDistance 入口及七个分镜，原有 MP4 和音轨不覆盖。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_LINE1 = "#3498db"
C_LINE2 = "#9b59b6"
C_POINT = "#e74c3c"
C_FOOT = "#2ecc71"
C_PERP = "#f39c12"
FONT_CN = "PingFang SC"


def valid_line(line):
    a, b, c = line
    if not all(math.isfinite(v) for v in line) or a == 0 and b == 0:
        raise ValueError("一般式 Ax+By+C=0 要求有限系数且 (A,B) 非零")
    return a, b, c


def foot_of_perpendicular(point, line):
    """点到无限直线的正交投影，不依赖倾斜角或斜率。"""
    x, y = point
    a, b, c = valid_line(line)
    t = (a * x + b * y + c) / (a * a + b * b)
    return x - a * t, y - b * t


def point_line_distance(point, line):
    x, y = point
    a, b, c = valid_line(line)
    return abs(a * x + b * y + c) / math.hypot(a, b)


def parallel_line_distance(line1, line2):
    """两线法向量平行才可直接计算距离；等比化后允许系数不同。"""
    a1, b1, c1 = valid_line(line1)
    a2, b2, c2 = valid_line(line2)
    n1 = math.hypot(a1, b1)
    n2 = math.hypot(a2, b2)
    unit1 = (a1 / n1, b1 / n1)
    unit2 = (a2 / n2, b2 / n2)
    if not math.isclose(unit1[0] * unit2[1] - unit1[1] * unit2[0],
                        0.0, abs_tol=1e-10):
        raise ValueError("两直线不平行")
    dot = unit1[0] * unit2[0] + unit1[1] * unit2[1]
    return abs(c1 / n1 - (1 if dot >= 0 else -1) * c2 / n2)


def clipped_line(line, xb=(-2.0, 5.0), yb=(-2.0, 5.0)):
    """直线与数据窗口矩形的交段；不绘制超出轴域的函数端点。"""
    a, b, c = valid_line(line)
    xmin, xmax = xb
    ymin, ymax = yb
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("窗口范围必须严格递增")
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
        if not any(math.dist(p, other) < 1e-9 for other in unique):
            unique.append(p)
    if len(unique) < 2:
        raise ValueError("直线未在坐标窗口内形成可见线段")
    return max(((p, q) for i, p in enumerate(unique) for q in unique[i + 1:]),
               key=lambda pair: math.dist(*pair))


class PointToLineDistance(Scene):
    L1 = (3.0, 4.0, -12.0)
    L2 = (3.0, 4.0, -2.0)
    P = (1.0, 1.0)
    R = (0.0, 0.5)  # 第二条平行线上一固定点

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT_CN,
                           font_size=17, color=GRAY_B).move_to(UP * 6.95)
        self.add(self.author)
        self.scene1_opening()
        self.scene2_model()
        self.scene3_perpendicular()
        self.scene4_formula()
        self.scene5_calculation()
        self.scene6_parallel()
        self.scene7_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT_CN, font_size=size, color=color)

    def heading(self, name, color=GOLD):
        old = [obj for obj in self.mobjects if obj is not self.author]
        if old:
            self.play(*[FadeOut(obj) for obj in old], run_time=0.4)
        self.play(FadeIn(self.cn(name, 36, color).move_to(UP * 6.0)), run_time=0.4)

    def axes(self):
        # 等比例：x、y 均为每单位 0.8 场景坐标，画面上的直角仍为直角。
        axes = Axes(x_range=[-2, 5, 1], y_range=[-2, 5, 1],
                    x_length=5.6, y_length=5.6,
                    axis_config={"color": GRAY_B, "include_numbers": True,
                                 "font_size": 18}, tips=False).move_to(UP * 1.2)
        self.play(Create(axes), run_time=0.65)
        return axes

    def draw(self, axes, line, color):
        p, q = clipped_line(line)
        path = Line(axes.c2p(*p), axes.c2p(*q), color=color, stroke_width=5)
        self.play(Create(path), run_time=0.65)
        return path

    def mark(self, axes, point, name, color, direction=UR):
        dot = Dot(axes.c2p(*point), radius=0.1, color=color)
        label = MathTex(name, font_size=24, color=color).next_to(dot, direction, buff=0.12)
        self.play(FadeIn(dot), FadeIn(label), run_time=0.4)
        return dot

    def panel(self, name, expression, note, color=YELLOW):
        rect = RoundedRectangle(width=8.0, height=2.5, corner_radius=0.15,
                                stroke_color=color, stroke_width=2,
                                fill_color="#16213e", fill_opacity=0.95).move_to(DOWN * 4.75)
        title = self.cn(name, 23, color).move_to(rect.get_center() + UP * 0.76)
        formula = MathTex(expression, font_size=32).move_to(rect.get_center() + UP * 0.04)
        formula.scale_to_fit_width(min(formula.width, 7.4))
        note_label = self.cn(note, 19, GRAY_A).move_to(rect.get_center() + DOWN * 0.75)
        self.play(FadeIn(rect), FadeIn(title), Write(formula), FadeIn(note_label), run_time=0.85)

    def scene1_opening(self):
        self.heading("点到直线：哪一条线段最短？")
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        self.mark(axes, self.P, r"P(1,1)", C_POINT, DL)
        # 所有候选端点严格位于 3x+4y-12=0。
        for endpoint in ((0, 3), (4, 0), (2, 1.5)):
            self.play(Create(DashedLine(axes.c2p(*self.P), axes.c2p(*endpoint),
                                        color=GRAY_A, dash_length=0.1)), run_time=0.25)
        self.play(FadeIn(self.cn("垂足对应的线段最短", 26, C_PERP).move_to(DOWN * 2.5)),
                  run_time=0.4)
        self.wait(0.75)

    def scene2_model(self):
        self.heading("建立模型：点与一般式直线")
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        self.mark(axes, self.P, r"P(1,1)", C_POINT, DL)
        self.play(Write(MathTex(r"3x+4y-12=0", font_size=29,
                                color=C_LINE1).move_to(DOWN * 2.45)), run_time=0.5)
        self.panel("一般式：A、B 不同时为零",
                   r"Ax+By+C=0,\quad P(x_0,y_0)",
                   "d 为 P 到该直线上所有点的最短距离", C_LINE1)
        self.wait(0.75)

    def scene3_perpendicular(self):
        self.heading("过 P 作垂线，垂足记为 Q")
        q = foot_of_perpendicular(self.P, self.L1)
        assert math.dist(q, (1.6, 1.8)) < 1e-10
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        self.mark(axes, self.P, r"P(1,1)", C_POINT, DL)
        self.mark(axes, q, r"Q(1.6,1.8)", C_FOOT, UR)
        foot_segment = Line(axes.c2p(*self.P), axes.c2p(*q),
                            color=C_PERP, stroke_width=5)
        self.play(Create(foot_segment), run_time=0.55)
        # PQ 的数据方向与直线方向 (B,-A) 点积为 0；等比例轴保证屏幕角度相符。
        tangent = (self.L1[1], -self.L1[0])
        offset = (q[0] + tangent[0] * 0.08, q[1] + tangent[1] * 0.08)
        side1 = Line(axes.c2p(*q), axes.c2p(*self.P))
        side2 = Line(axes.c2p(*q), axes.c2p(*offset))
        self.play(Create(RightAngle(side1, side2, length=0.19,
                                    color=C_FOOT)), run_time=0.45)
        self.panel("垂线段 PQ 的长度就是距离", r"Q=(1.6,1.8),\quad |PQ|=1",
                   "垂足满足直线方程，且 PQ 与直线垂直", C_PERP)
        self.wait(0.8)

    def scene4_formula(self):
        self.heading("点到一般式直线的距离公式")
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        self.mark(axes, self.P, r"P(1,1)", C_POINT, DL)
        self.panel("将点坐标代入直线方程，取绝对值",
                   r"d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}",
                   "分母是非零法向量 (A,B) 的模长", YELLOW)
        self.wait(1.1)

    def scene5_calculation(self):
        self.heading("例题：P(1,1) 到 3x+4y-12=0")
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        q = foot_of_perpendicular(self.P, self.L1)
        self.play(Create(Line(axes.c2p(*self.P), axes.c2p(*q),
                              color=C_PERP, stroke_width=5)), run_time=0.55)
        self.mark(axes, self.P, r"P", C_POINT, DL)
        self.mark(axes, q, r"Q", C_FOOT, UR)
        self.panel("代入 A=3, B=4, C=-12",
                   r"d=\frac{|3+4-12|}{\sqrt{9+16}}=1",
                   "公式结果与图上 PQ 的长度一致", YELLOW)
        self.wait(1.0)

    def scene6_parallel(self):
        self.heading("拓展：两条平行直线的距离")
        d = parallel_line_distance(self.L1, self.L2)
        assert math.isclose(d, 2)
        s = foot_of_perpendicular(self.R, self.L1)
        assert math.dist(s, (1.2, 2.1)) < 1e-10
        axes = self.axes()
        self.draw(axes, self.L1, C_LINE1)
        self.draw(axes, self.L2, C_LINE2)
        self.mark(axes, self.R, r"R(0,0.5)", C_POINT, DL)
        self.mark(axes, s, r"S(1.2,2.1)", C_FOOT, UR)
        self.play(Create(Line(axes.c2p(*self.R), axes.c2p(*s),
                              color=C_PERP, stroke_width=5)), run_time=0.6)
        self.panel("同法向量 (A,B) 的两条平行线",
                   r"d=\frac{|C_1-C_2|}{\sqrt{A^2+B^2}}=\frac{10}{5}=2",
                   "本例 RS 真正沿公共法向量方向连接两线", C_LINE2)
        self.wait(1.0)

    def scene7_outro(self):
        self.heading("距离公式：垂足与法向量")
        self.play(FadeIn(self.cn("先检查 A、B 不同时为零", 28, YELLOW).move_to(UP * 1)),
                  FadeIn(self.cn("@emptyandcalm", 27, GRAY_A).move_to(DOWN * 0.5)),
                  run_time=0.65)
        self.wait(1.5)
