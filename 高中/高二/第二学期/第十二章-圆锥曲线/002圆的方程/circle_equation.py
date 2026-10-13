"""圆的方程：圆心、半径、点线距离和三个位置关系由同一数学数据得到。

保留 CircleEquation 入口及原八镜，旧 MP4、音轨、prompt.md 不覆盖。
"""

import math
import os

from manimgx import *

config.pixel_width = 1080
config.pixel_height = 1920
# ManimGX: frame_width is derived from pixel aspect ratio and frame_height (legacy value was 9).
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_CURVE = "#3498db"
C_CENTER = "#e74c3c"
C_LINE = "#2ecc71"
# ManimGX ships Noto CJK and resolves the generic family consistently across platforms.
# Override with MANIM_MATH_CJK_FONT="PingFang SC" when exact legacy macOS typography is required.
FONT = os.getenv("MANIM_MATH_CJK_FONT", "sans-serif")
CENTER = (2.0, 1.0)
RADIUS = 1.5
GENERAL = (-4.0, -2.0, 2.75)
SEPARATE = (0.0, 1.0, 1.0)     # y=-1: d=2>1.5
TANGENT = (0.0, 1.0, -2.5)     # y=2.5: d=1.5
INTERSECT = (0.0, 1.0, -1.0)  # y=1: d=0<1.5


def circle_from_general(d, e, f):
    """一般方程 x²+y²+Dx+Ey+F=0 代表真圆须有 D²+E²-4F>0。"""
    if not all(math.isfinite(v) for v in (d, e, f)):
        raise ValueError("一般式系数须有限")
    radius_sq = (d*d + e*e - 4*f) / 4
    if radius_sq <= 0:
        raise ValueError("判别量非正：单点或空集不是正半径的圆")
    return (-d/2, -e/2), math.sqrt(radius_sq)


def circle_residual(point, center=CENTER, radius=RADIUS):
    x, y = point
    a, b = center
    if not all(math.isfinite(v) for v in (x, y, a, b, radius)) or radius <= 0:
        raise ValueError("坐标须有限且圆半径须为正")
    return (x-a)**2 + (y-b)**2 - radius**2


def valid_line(line):
    a, b, c = line
    if not all(math.isfinite(v) for v in line) or (a == 0 and b == 0):
        raise ValueError("直线法向量必须非零且系数须有限")
    return a, b, c


def center_line_distance(center, line):
    a, b, c = valid_line(line)
    x, y = center
    return abs(a*x+b*y+c)/math.hypot(a, b)


def line_circle_intersections(center, radius, line, tolerance=1e-10):
    """无限直线与圆的 0/1/2 个交点，沿法向量求垂足再沿切向量偏移。"""
    a, b, c = valid_line(line)
    cx, cy = center
    if not all(math.isfinite(v) for v in (cx, cy, radius, tolerance)) or radius <= 0 or tolerance < 0:
        raise ValueError("中心、半径、容差须有效")
    norm = math.hypot(a, b)
    signed = (a*cx+b*cy+c)/norm
    foot = (cx-signed*a/norm, cy-signed*b/norm)
    if abs(signed) > radius + tolerance:
        return ()
    if abs(abs(signed)-radius) <= tolerance:
        return (foot,)
    offset = math.sqrt(max(0.0, radius*radius-signed*signed))
    tx, ty = -b/norm, a/norm
    return ((foot[0]-offset*tx, foot[1]-offset*ty),
            (foot[0]+offset*tx, foot[1]+offset*ty))


def axis_units(x_range=(-4.0, 4.0), y_range=(-3.0, 3.0),
               x_length=6.4, y_length=4.8):
    if (x_range[0] >= x_range[1] or y_range[0] >= y_range[1]
            or not math.isfinite(x_length) or not math.isfinite(y_length)
            or x_length <= 0 or y_length <= 0):
        raise ValueError("轴域与画面长度必须有效")
    return x_length/(x_range[1]-x_range[0]), y_length/(y_range[1]-y_range[0])


class CircleEquation(Scene):
    """通过圆方程和法向量距离逐镜说明相离、相切、相交。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=22, color=GRAY_B).move_to(UP*6.95)
        self.add(self.author)
        self.show_opening()
        self.show_definition()
        self.show_standard_equation()
        self.show_general_equation()
        self.show_line_separate()
        self.show_line_tangent()
        self.show_line_intersect()
        self.show_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def stage(self, name, color=GOLD):
        previous = [obj for obj in self.mobjects if obj is not self.author]
        if previous:
            self.play(*[FadeOut(obj) for obj in previous], run_time=0.4)
        self.play(FadeIn(self.cn(name, 35, color).move_to(UP*6)), run_time=0.4)

    def diagram(self):
        ux, uy = axis_units()
        assert math.isclose(ux, uy, abs_tol=1e-12)
        center, radius = circle_from_general(*GENERAL)
        assert center == CENTER and math.isclose(radius, RADIUS)
        ax = Axes(x_range=[-4,4,1], y_range=[-3,3,1],
                  x_length=6.4, y_length=4.8, tips=False,
                  axis_config={"color": GRAY_B, "include_numbers": True,
                               "font_size": 18}).move_to(UP*1.45)
        circle = Circle(radius=radius*ux, color=C_CURVE,
                        stroke_width=5).move_to(ax.c2p(*center))
        center_dot = Dot(ax.c2p(*center), radius=0.08, color=C_CENTER)
        center_label = MathTex(r"O(2,1)", font_size=24, color=C_CENTER)
        center_label.next_to(center_dot, DL, buff=0.15)
        self.play(Create(ax), Create(circle), FadeIn(center_dot), FadeIn(center_label), run_time=0.8)
        return ax

    def panel(self, title, tex, note, color=YELLOW):
        rect = RoundedRectangle(width=8.0, height=2.6, corner_radius=0.14,
                                stroke_color=color, stroke_width=2,
                                fill_color="#16213e", fill_opacity=0.95).move_to(DOWN*4.7)
        heading = self.cn(title, 22, color).move_to(rect.get_center()+UP*0.84)
        equation = MathTex(tex, font_size=30).move_to(rect.get_center()+UP*0.04)
        equation.scale_to_fit_width(min(equation.width, 7.45))
        note_text = self.cn(note, 19, GRAY_A).move_to(rect.get_center()+DOWN*0.81)
        self.play(FadeIn(rect), FadeIn(heading), Write(equation), FadeIn(note_text), run_time=0.8)

    def draw_line(self, ax, y, color=C_LINE):
        line = Line(ax.c2p(-3.6, y), ax.c2p(3.6, y), color=color, stroke_width=4)
        self.play(Create(line), run_time=0.55)
        return line

    def show_opening(self):
        title = self.cn("圆的方程", 46, C_CURVE).move_to(UP*2.2)
        subtitle = self.cn("一条方程，统一圆的几何信息", 27, GRAY_A).next_to(title, DOWN, buff=0.55)
        formula = MathTex(r"(x-a)^2+(y-b)^2=r^2", font_size=44, color=YELLOW).next_to(subtitle, DOWN, buff=0.9)
        self.play(Write(title), FadeIn(subtitle), run_time=0.9)
        self.play(Write(formula), run_time=0.8)
        self.wait(0.7)

    def show_definition(self):
        self.stage("从定义到标准方程")
        ax = self.diagram()
        point = Dot(ax.c2p(3.06, 2.06), radius=0.075, color=YELLOW)
        radius_line = Line(ax.c2p(*CENTER), point.get_center(), color=YELLOW, stroke_width=3)
        p_label = MathTex(r"P(x,y)", font_size=24, color=YELLOW).next_to(point, UR, buff=0.12)
        relation = MathTex(r"|PO|=r", font_size=32, color=YELLOW).move_to(DOWN*2.1)
        self.play(FadeIn(point), Create(radius_line), FadeIn(p_label), Write(relation), run_time=0.8)
        self.panel("平方距离", r"(x-a)^2+(y-b)^2=r^2", "圆：到定点 O 的距离恒为 r")
        self.wait(0.35)

    def show_standard_equation(self):
        self.stage("标准方程读图")
        ax = self.diagram()
        center = MathTex(r"O(a,b)", font_size=28, color=C_CENTER).move_to(DOWN*2.0)
        radius = MathTex(r"r>0", font_size=28, color=YELLOW).next_to(center, DOWN, buff=0.32)
        self.play(FadeIn(center), FadeIn(radius), run_time=0.5)
        self.panel("例", r"(x-2)^2+(y-1)^2=\frac94", "圆心 (2,1)，半径 3/2")
        self.wait(0.35)

    def show_general_equation(self):
        self.stage("一般式如何还原")
        line1 = MathTex(r"x^2+y^2+Dx+Ey+F=0", font_size=36).move_to(UP*2.4)
        line2 = MathTex(r"(x+\frac D2)^2+(y+\frac E2)^2=\frac{D^2+E^2-4F}{4}", font_size=31).next_to(line1, DOWN, buff=0.65)
        cond = MathTex(r"D^2+E^2-4F>0", font_size=31, color=YELLOW).next_to(line2, DOWN, buff=0.58)
        self.play(Write(line1), run_time=0.6)
        self.play(TransformFromCopy(line1, line2), FadeIn(cond), run_time=0.9)
        self.panel("结论", r"O(-\frac D2,-\frac E2),\quad r=\frac12\sqrt{D^2+E^2-4F}", "判别量必须为正")
        self.wait(0.35)

    def show_line_separate(self):
        self.stage("直线与圆：相离")
        ax = self.diagram()
        self.draw_line(ax, -1)
        d = center_line_distance(CENTER, SEPARATE)
        assert d > RADIUS and line_circle_intersections(CENTER, RADIUS, SEPARATE) == ()
        self.panel("比较距离", rf"d={d:g}>r={RADIUS:g}", "没有交点 → 相离", RED)
        self.wait(0.3)

    def show_line_tangent(self):
        self.stage("直线与圆：相切")
        ax = self.diagram()
        self.draw_line(ax, 2.5)
        points = line_circle_intersections(CENTER, RADIUS, TANGENT)
        assert len(points) == 1
        tangent = Dot(ax.c2p(*points[0]), radius=0.085, color=YELLOW)
        self.play(FadeIn(tangent), run_time=0.35)
        d = center_line_distance(CENTER, TANGENT)
        self.panel("比较距离", rf"d={d:g}=r={RADIUS:g}", "一个交点 → 相切", YELLOW)
        self.wait(0.3)

    def show_line_intersect(self):
        self.stage("直线与圆：相交")
        ax = self.diagram()
        self.draw_line(ax, 1)
        points = line_circle_intersections(CENTER, RADIUS, INTERSECT)
        assert len(points) == 2
        dots = VGroup(*[Dot(ax.c2p(*p), radius=0.075, color=YELLOW) for p in points])
        self.play(FadeIn(dots), run_time=0.4)
        d = center_line_distance(CENTER, INTERSECT)
        self.panel("比较距离", rf"d={d:g}<r={RADIUS:g}", "两个交点 → 相交", GREEN)
        self.wait(0.3)

    def show_outro(self):
        self.stage("一个统一框架", C_CURVE)
        rows = VGroup(
            self.cn("标准式 → 圆心与半径", 26, WHITE),
            self.cn("一般式 → 配方还原", 26, WHITE),
            self.cn("点与圆 → 代入看残差", 26, WHITE),
            self.cn("直线与圆 → 比较 d 与 r", 26, WHITE),
        ).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to(UP*0.5)
        self.play(LaggedStart(*[FadeIn(row, shift=RIGHT*0.2) for row in rows], lag_ratio=0.18), run_time=1.3)
        final = MathTex(r"d>r,\ d=r,\ d<r", font_size=38, color=YELLOW).move_to(DOWN*2.0)
        self.play(Write(final), run_time=0.7)
        self.wait(0.8)
