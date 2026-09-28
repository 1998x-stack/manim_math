"""两直线的垂直与夹角：区分锐角公式、直角特例及垂直线。

保留 TwoLinesAngle 入口和五个教学分镜。原视频及音轨不作修改。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#0f0c29"
LINE1_COLOR = "#00d4ff"
LINE2_COLOR = "#ff6b6b"
LINE3_COLOR = "#ffd93d"
ANGLE_COLOR = "#a8ff78"
FONT = "PingFang SC"


def direction_from_general(a, b):
    """一般式 Ax+By+C=0 的方向向量 (B,-A)。"""
    if not math.isfinite(a) or not math.isfinite(b) or (a == 0 and b == 0):
        raise ValueError("直线的 A、B 必须有限且不同时为零")
    return b, -a


def acute_line_angle(v, w):
    """无向直线的较小夹角：[0, pi/2]；不以斜率公式处理垂线。"""
    x1, y1 = v
    x2, y2 = w
    if not all(math.isfinite(c) for c in (x1, y1, x2, y2)):
        raise ValueError("方向向量需要有限分量")
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        raise ValueError("零方向向量不能确定直线")
    cross = abs(x1 * y2 - y1 * x2)
    dot = abs(x1 * x2 + y1 * y2)
    return math.atan2(cross, dot)


def slopes_perpendicular(k1, k2):
    """仅对两条斜率都存在的直线适用。"""
    if not math.isfinite(k1) or not math.isfinite(k2):
        raise ValueError("无定义的斜率不得代入乘积条件")
    return math.isclose(k1 * k2, -1.0, rel_tol=1e-10, abs_tol=1e-10)


def tangent_acute_angle(k1, k2):
    """当两线不垂直且都有斜率时，返回非负的 tan(theta)。"""
    if not math.isfinite(k1) or not math.isfinite(k2):
        raise ValueError("斜率必须存在且有限")
    denominator = 1 + k1 * k2
    if math.isclose(denominator, 0.0, abs_tol=1e-10):
        raise ValueError("直角时 tan(theta) 不存在，不能套用分式")
    return abs(k1 - k2) / abs(denominator)


def clipped_slope(k, xb=(-3.0, 3.0), yb=(-2.5, 2.5)):
    """求 y=kx 与可见坐标窗口的交段，确保数据坐标与画面一致。"""
    if not math.isfinite(k):
        raise ValueError("本工具只接受有限斜率，竖直线应单独绘制")
    xmin, xmax = xb
    ymin, ymax = yb
    if not xmin < xmax or not ymin < ymax:
        raise ValueError("坐标窗口必须非退化")
    points = []
    for x in (xmin, xmax):
        y = k * x
        if ymin - 1e-10 <= y <= ymax + 1e-10:
            points.append((x, min(ymax, max(ymin, y))))
    if k != 0:
        for y in (ymin, ymax):
            x = y / k
            if xmin - 1e-10 <= x <= xmax + 1e-10:
                points.append((min(xmax, max(xmin, x)), y))
    distinct = []
    for point in points:
        if not any(math.dist(point, other) < 1e-9 for other in distinct):
            distinct.append(point)
    if len(distinct) < 2:
        raise ValueError("直线在窗口内没有非退化可见线段")
    return max(((p, q) for i, p in enumerate(distinct) for q in distinct[i + 1:]),
               key=lambda pair: math.dist(*pair))


class TwoLinesAngle(Scene):
    K1 = 2.0
    K2 = -0.5
    K3 = 1 / 3

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=17, color=GRAY_B).move_to(UP * 6.95)
        self.add(self.author)
        self.scene_1_title()
        self.scene_2_perpendicular()
        self.scene_3_angle_formula()
        self.scene_4_summary()
        self.scene_5_outro()

    def cn(self, text, size=26, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def heading(self, text, color=WHITE):
        old = [obj for obj in self.mobjects if obj is not self.author]
        if old:
            self.play(*[FadeOut(obj) for obj in old], run_time=0.4)
        self.play(FadeIn(self.cn(text, 36, color).move_to(UP * 6.0)), run_time=0.4)

    def axes(self):
        ax = Axes(x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1],
                  x_length=6, y_length=5, tips=False,
                  axis_config={"color": GRAY_B, "include_numbers": True,
                               "font_size": 18}).move_to(UP * 1.5)
        self.play(Create(ax), run_time=0.65)
        return ax

    def draw(self, ax, k, color):
        p, q = clipped_slope(k)
        obj = Line(ax.c2p(*p), ax.c2p(*q), color=color, stroke_width=5)
        self.play(Create(obj), run_time=0.55)
        return obj

    def panel(self, text, formula, note, color=ANGLE_COLOR):
        rect = RoundedRectangle(width=8.0, height=2.5, corner_radius=0.15,
                                stroke_color=color, stroke_width=2,
                                fill_color="#16213e", fill_opacity=0.95).move_to(DOWN * 4.75)
        label = self.cn(text, 22, color).move_to(rect.get_center() + UP * 0.78)
        equation = MathTex(formula, font_size=30).move_to(rect.get_center() + UP * 0.05)
        equation.scale_to_fit_width(min(equation.width, 7.5))
        note_label = self.cn(note, 19, GRAY_A).move_to(rect.get_center() + DOWN * 0.79)
        self.play(FadeIn(rect), FadeIn(label), Write(equation), FadeIn(note_label), run_time=0.85)

    def scene_1_title(self):
        self.heading("两直线的垂直与夹角")
        self.play(FadeIn(self.cn("垂直用点积，夹角用点积与叉积", 29, ANGLE_COLOR).move_to(UP * 1)),
                  run_time=0.6)
        self.wait(0.8)

    def scene_2_perpendicular(self):
        self.heading("① 两直线垂直", LINE2_COLOR)
        assert slopes_perpendicular(self.K1, self.K2)
        assert math.isclose(acute_line_angle((1, self.K1), (1, self.K2)), math.pi / 2)
        ax = self.axes()
        self.draw(ax, self.K1, LINE1_COLOR)
        self.draw(ax, self.K2, LINE2_COLOR)
        origin = ax.c2p(0, 0)
        arm1 = Line(origin, ax.c2p(0.35, 0.7))
        arm2 = Line(origin, ax.c2p(0.7, -0.35))
        self.play(Create(RightAngle(arm1, arm2, length=0.27, color=ANGLE_COLOR)),
                  run_time=0.4)
        self.play(FadeIn(MathTex(r"k_1=2,\quad k_2=-\frac12",
                                font_size=27).move_to(DOWN * 2.45)), run_time=0.5)
        self.panel("两条直线斜率均存在时", r"k_1k_2=-1",
                   "本例两方向向量点积为零，夹角为 90°", LINE2_COLOR)
        self.wait(0.85)

    def scene_3_angle_formula(self):
        self.heading("② 两直线的较小夹角", ANGLE_COLOR)
        theta = acute_line_angle((1, self.K3), (1, self.K1))
        assert math.isclose(theta, math.pi / 4, abs_tol=1e-10)
        assert math.isclose(tangent_acute_angle(self.K1, self.K3), 1.0)
        ax = self.axes()
        self.draw(ax, self.K1, LINE1_COLOR)
        self.draw(ax, self.K3, LINE3_COLOR)
        origin = ax.c2p(0, 0)
        start = math.atan(self.K3)
        arc = Arc(radius=0.65, start_angle=start, angle=theta,
                  arc_center=origin, color=ANGLE_COLOR, stroke_width=4)
        label = MathTex(r"\theta=45^{\circ}", font_size=27, color=ANGLE_COLOR)
        label.move_to(origin + 1.15 * (RIGHT * math.cos(start + theta / 2)
                                      + UP * math.sin(start + theta / 2)))
        self.play(Create(arc), FadeIn(label), run_time=0.55)
        self.play(FadeIn(MathTex(r"k_1=2,\quad k_2=\frac13", font_size=28)
                         .move_to(DOWN * 2.4)), run_time=0.5)
        self.panel("两线不垂直且斜率存在", r"\tan\theta=\frac{|k_1-k_2|}{|1+k_1k_2|}=1",
                   "本例 θ=45°；分母为零时夹角是 90°", LINE3_COLOR)
        self.wait(0.85)

    def scene_4_summary(self):
        self.heading("公式总结与适用范围")
        cards = (
            ("一般式垂直", r"A_1A_2+B_1B_2=0", "包括水平线与垂直线", LINE1_COLOR),
            ("有斜率的垂直条件", r"k_1k_2=-1", "两条直线都不是垂直线", LINE2_COLOR),
            ("较小夹角", r"\theta=\arctan\frac{|k_1-k_2|}{|1+k_1k_2|}",
             "仅在两条斜率存在且不垂直时使用", LINE3_COLOR),
            ("所有方向的夹角", r"\theta=\operatorname{atan2}(|u\times v|,|u\cdot v|)",
             "u、v 为非零方向向量；0°≤θ≤90°", ANGLE_COLOR),
        )
        for index, (title, tex, note, color) in enumerate(cards):
            y = 4.4 - index * 2.75
            panel = RoundedRectangle(width=8, height=2.35, corner_radius=0.15,
                                     fill_color="#16213e", fill_opacity=0.95,
                                     stroke_color=color, stroke_width=2).move_to(UP * y)
            heading = self.cn(title, 23, color).move_to(panel.get_center() + UP * 0.67)
            equation = MathTex(tex, font_size=25).move_to(panel.get_center())
            equation.scale_to_fit_width(min(equation.width, 7.45))
            note_text = self.cn(note, 19, GRAY_A).move_to(panel.get_center() + DOWN * 0.73)
            self.play(FadeIn(VGroup(panel, heading, equation, note_text)), run_time=0.42)
        self.wait(1.4)

    def scene_5_outro(self):
        self.heading("先看方向，再选夹角公式")
        self.play(FadeIn(self.cn("一般式点积条件没有斜率除零问题", 27, ANGLE_COLOR)
                         .move_to(UP * 1)),
                  FadeIn(self.cn("@emptyandcalm", 26, GRAY_A).move_to(DOWN * 0.5)),
                  run_time=0.7)
        self.wait(1.4)
