"""圆的方程：圆心、半径、点线距离和三个位置关系由同一数学数据得到。

保留 CircleEquation 入口及原八镜，旧 MP4、音轨、prompt.md 不覆盖。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_CURVE = "#3498db"
C_CENTER = "#e74c3c"
C_LINE = "#2ecc71"
FONT = "PingFang SC"
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
                           font_size=17, color=GRAY_B).move_to(UP*6.95)
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
        segment = Line(ax.c2p(-4,y), ax.c2p(4,y), color=color, stroke_width=5)
        self.play(Create(segment), run_time=0.6)
        return segment

    def show_opening(self):
        self.stage("由圆心和半径建立一个圆")
        ax = self.diagram()
        self.panel("圆心 O(2,1)，半径 r=1.5",
                   r"(x-2)^2+(y-1)^2=2.25",
                   "同一坐标尺度，点与圆周能严格对应", C_CURVE)
        self.wait(0.75)

    def show_definition(self):
        self.stage("圆：到定点距离等于定长的点的轨迹")
        ax = self.diagram()
        edge = (CENTER[0]+RADIUS, CENTER[1])
        self.play(Create(Line(ax.c2p(*CENTER), ax.c2p(*edge),
                              color=YELLOW, stroke_width=4)), run_time=0.5)
        self.panel("中心到每个圆周点的距离都是 r",
                   r"\sqrt{(x-2)^2+(y-1)^2}=1.5",
                   "点恰好在圆周上，不包括圆盘内部", C_CURVE)
        self.wait(0.8)

    def show_standard_equation(self):
        self.stage("圆的标准方程")
        ax = self.diagram()
        self.panel("圆心 (a,b)，半径 r>0",
                   r"(x-a)^2+(y-b)^2=r^2",
                   "本例 a=2、b=1、r=1.5", C_CURVE)
        self.wait(0.6)
        self.play(Write(MathTex(r"(x-2)^2+(y-1)^2=2.25",
                                font_size=28, color=YELLOW).move_to(DOWN*2.65)), run_time=0.5)
        self.wait(0.55)

    def show_general_equation(self):
        self.stage("一般式：先配方再判断是否为圆")
        ax = self.diagram()
        self.play(Write(MathTex(r"x^2+y^2+Dx+Ey+F=0", font_size=30)
                        .move_to(DOWN*2.45)), run_time=0.5)
        self.panel("判别量须为正，圆心与半径才能确定",
                   r"O=(-D/2,-E/2),\quad r=\frac{\sqrt{D^2+E^2-4F}}{2}",
                   "判别量为零仅为单点，负数没有实点", C_CURVE)
        self.wait(0.75)
        self.play(Write(MathTex(r"D=-4,\ E=-2,\ F=2.75,\quad r=1.5",
                                font_size=26).move_to(DOWN*2.45)), run_time=0.5)
        self.wait(0.5)

    def show_line_separate(self):
        self.stage("① 相离：圆心到直线的距离大于半径")
        assert center_line_distance(CENTER, SEPARATE) > RADIUS
        assert len(line_circle_intersections(CENTER, RADIUS, SEPARATE)) == 0
        ax = self.diagram()
        self.draw_line(ax, -1)
        foot = (2.0, -1.0)
        self.play(Create(DashedLine(ax.c2p(*CENTER), ax.c2p(*foot),
                                    color=YELLOW, dash_length=0.12)), run_time=0.5)
        self.panel("l：y=-1，垂足 Q(2,-1)", r"d=|1-(-1)|=2>1.5=r",
                   "圆与直线没有公共点", C_LINE)
        self.wait(0.9)

    def show_line_tangent(self):
        self.stage("② 相切：圆心到直线的距离等于半径")
        points = line_circle_intersections(CENTER, RADIUS, TANGENT)
        assert len(points) == 1 and math.dist(points[0], (2,2.5)) < 1e-10
        ax = self.diagram()
        self.draw_line(ax, 2.5)
        self.play(Create(Line(ax.c2p(*CENTER), ax.c2p(*points[0]),
                              color=YELLOW, stroke_width=4)), run_time=0.5)
        self.play(FadeIn(Dot(ax.c2p(*points[0]), color=YELLOW, radius=0.11)),
                  run_time=0.4)
        self.panel("l：y=2.5，唯一公共点 T(2,2.5)", r"d=|1-2.5|=1.5=r",
                   "半径垂直于该水平切线", C_LINE)
        self.wait(0.9)

    def show_line_intersect(self):
        self.stage("③ 相交：圆心到直线的距离小于半径")
        points = line_circle_intersections(CENTER, RADIUS, INTERSECT)
        assert len(points) == 2
        ax = self.diagram()
        self.draw_line(ax, 1)
        for p in points:
            self.play(FadeIn(Dot(ax.c2p(*p), color=YELLOW, radius=0.11)), run_time=0.25)
        self.panel("l：y=1，两个公共点", r"(0.5,1),\quad (3.5,1)",
                   "中心到直线距离 d=0，小于 r=1.5", C_LINE)
        self.wait(0.75)
        self.stage("三种位置关系由 d 与 r 的大小决定")
        cases = VGroup(self.cn("d>r：相离，零个公共点", 27, C_CENTER),
                       self.cn("d=r：相切，一个公共点", 27, YELLOW),
                       self.cn("d<r：相交，两个公共点", 27, C_LINE))
        cases.arrange(DOWN, buff=0.7).move_to(UP*0.8)
        self.play(FadeIn(cases), run_time=0.65)
        self.wait(1.0)

    def show_outro(self):
        self.stage("由标准式求圆心半径，再比较 d 与 r")
        self.play(FadeIn(self.cn("注意一般式的判别量须大于零", 27, YELLOW)
                         .move_to(UP*1.1)),
                  FadeIn(self.cn("@emptyandcalm", 26, GRAY_A).move_to(DOWN*0.7)),
                  run_time=0.65)
        self.wait(1.25)
