"""高二下《曲线与方程》：屏幕圆和方程共用精确的圆模型。

保留 CurveAndEquation 和原八镜头入口；旧 MP4、音轨、prompt.md 不覆盖。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_CURVE = "#3498db"
C_POINT = "#e74c3c"
C_VALID = "#2ecc71"
C_AUX = GRAY_B
FONT = "PingFang SC"
RADIUS = 2.0


def circle_point(theta, radius=RADIUS):
    """数据坐标：参数圆上的点，而非屏幕单位猜测。"""
    if not math.isfinite(theta) or not math.isfinite(radius) or radius <= 0:
        raise ValueError("角度须有限，圆半径须有限且为正")
    return radius * math.cos(theta), radius * math.sin(theta)


def circle_residual(point, radius=RADIUS):
    """点的坐标满足 x²+y²=r² 当且仅当余量为零。"""
    x, y = point
    if not all(math.isfinite(value) for value in (x, y, radius)) or radius <= 0:
        raise ValueError("点坐标须有限，圆半径必须为正")
    return x * x + y * y - radius * radius


def circle_contains(point, radius=RADIUS, tolerance=1e-9):
    """离散数值用于测试、标签；数学命题的精确圆由参数曲线定义。"""
    if tolerance < 0 or not math.isfinite(tolerance):
        raise ValueError("误差必须是有限非负值")
    return abs(circle_residual(point, radius)) <= tolerance


def axis_unit_sizes(x_bounds=(-4.0, 4.0), y_bounds=(-3.0, 3.0),
                    x_length=6.4, y_length=4.8):
    """两轴每单位的画面长度，等尺度时圆在画面上仍为圆。"""
    if (x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1]
            or not math.isfinite(x_length) or not math.isfinite(y_length)
            or x_length <= 0 or y_length <= 0):
        raise ValueError("坐标区间及轴画面长度必须有效")
    return (x_length / (x_bounds[1] - x_bounds[0]),
            y_length / (y_bounds[1] - y_bounds[0]))


class CurveAndEquation(Scene):
    """正向、反向和反例必须以同一组真实坐标证明，而非视觉接近。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=17, color=GRAY_B).move_to(UP * 6.95)
        self.add(self.author)
        self.show_opening()
        self.show_coordinate_system()
        self.show_equation_concept()
        self.show_sufficiency_forward()
        self.show_sufficiency_backward()
        self.show_counterexample()
        self.show_summary()
        self.show_outro()

    def cn(self, value, size=25, color=WHITE):
        return Text(value, font=FONT, font_size=size, color=color)

    def stage(self, heading, color=GOLD):
        existing = [m for m in self.mobjects if m is not self.author]
        if existing:
            self.play(*[FadeOut(m) for m in existing], run_time=0.4)
        self.play(FadeIn(self.cn(heading, 35, color).move_to(UP * 6.0)), run_time=0.4)

    def axes_and_circle(self):
        unit_x, unit_y = axis_unit_sizes()
        assert math.isclose(unit_x, unit_y, abs_tol=1e-12)
        axes = Axes(x_range=[-4, 4, 1], y_range=[-3, 3, 1],
                    x_length=6.4, y_length=4.8,
                    axis_config={"color": GRAY_B, "include_numbers": True,
                                 "font_size": 18}, tips=False).move_to(UP * 1.45)
        circle = Circle(radius=RADIUS * unit_x, color=C_CURVE,
                        stroke_width=5).move_to(axes.c2p(0, 0))
        self.play(Create(axes), Create(circle), run_time=0.9)
        return axes, circle

    def mark(self, axes, point, label, color=C_POINT, direction=UR):
        dot = Dot(axes.c2p(*point), radius=0.10, color=color)
        text = MathTex(label, font_size=25, color=color).next_to(dot, direction, buff=0.13)
        self.play(FadeIn(dot), FadeIn(text), run_time=0.4)
        return dot

    def panel(self, label, formula, explanation, color=C_VALID):
        box = RoundedRectangle(width=8.0, height=2.6, corner_radius=0.15,
                               stroke_color=color, stroke_width=2,
                               fill_color="#16213e", fill_opacity=0.95).move_to(DOWN * 4.7)
        title = self.cn(label, 22, color).move_to(box.get_center() + UP * 0.86)
        equation = MathTex(formula, font_size=31).move_to(box.get_center() + UP * 0.04)
        equation.scale_to_fit_width(min(equation.width, 7.45))
        note = self.cn(explanation, 19, GRAY_A).move_to(box.get_center() + DOWN * 0.82)
        self.play(FadeIn(box), FadeIn(title), Write(equation), FadeIn(note), run_time=0.8)

    def show_opening(self):
        self.stage("一个圆，怎样用方程准确描述？")
        self.play(Create(Circle(radius=1.5, color=C_CURVE, stroke_width=5)
                         .move_to(UP * 1.2)), run_time=0.8)
        self.play(FadeIn(self.cn("图像上的点与方程的解要一一对应", 26)
                         .move_to(DOWN * 2.2)), run_time=0.5)
        self.wait(0.7)

    def show_coordinate_system(self):
        self.stage("同一坐标尺度下建立圆的模型")
        axes, circle = self.axes_and_circle()
        self.play(Write(MathTex(r"O(0,0),\quad r=2", font_size=33)
                        .move_to(DOWN * 2.6)), run_time=0.5)
        self.panel("两坐标轴的单位长度相同", r"x^2+y^2=2^2",
                   "圆心 O 到圆上每一点的距离都是 2", C_CURVE)
        self.wait(0.75)

    def show_equation_concept(self):
        self.stage("圆的方程是什么？")
        axes, circle = self.axes_and_circle()
        self.mark(axes, (2, 0), r"A(2,0)", C_POINT, DR)
        self.mark(axes, (0, 2), r"B(0,2)", C_POINT, UL)
        self.panel("圆周是满足这一等式的点的集合", r"x^2+y^2=4",
                   "这里表示圆周，不是圆盘 x²+y²≤4", C_VALID)
        self.wait(0.8)

    def show_sufficiency_forward(self):
        self.stage("正向：曲线上的点都满足方程", C_VALID)
        axes, circle = self.axes_and_circle()
        point = (math.sqrt(2), math.sqrt(2))
        assert circle_contains(point)
        self.mark(axes, point, r"P(\sqrt2,\sqrt2)", C_POINT, UR)
        self.panel("将圆上 P 的坐标代入方程", r"(\sqrt2)^2+(\sqrt2)^2=2+2=4",
                   "P 在圆上，因此 P 的坐标满足圆的方程", C_VALID)
        self.wait(0.9)

    def show_sufficiency_backward(self):
        self.stage("反向：方程的每个实数解都在曲线上", C_VALID)
        axes, circle = self.axes_and_circle()
        point = (0.0, 2.0)
        assert circle_contains(point)
        self.play(Write(MathTex(r"x=0,\quad y=2,\quad 0^2+2^2=4",
                                font_size=29).move_to(DOWN * 2.65)), run_time=0.5)
        # 先给出数对，再在同一坐标位置标点；不把一个固定坐标的点从错误位置移动。
        self.mark(axes, point, r"Q(0,2)", C_POINT, UR)
        self.panel("由方程的实数解确定唯一坐标点", r"Q(0,2)\in C",
                   "验证等式后按坐标定位，点恰好落在圆周", C_VALID)
        self.wait(0.85)

    def show_counterexample(self):
        self.stage("为什么两个方向缺一不可？", C_POINT)
        axes, circle = self.axes_and_circle()
        outside = (3.0, 0.0)
        left = (-2.0, 0.0)
        assert not circle_contains(outside) and circle_contains(left)
        self.mark(axes, outside, r"R(3,0)", C_POINT, DR)
        self.play(Write(MathTex(r"3^2+0^2=9\ne4", font_size=29,
                                color=C_POINT).move_to(DOWN * 2.55)), run_time=0.5)
        self.panel("圆外点不满足圆的方程", r"R(3,0)\notin C",
                   "等式未成立，就不能把该点当作圆周上的点", C_POINT)
        self.wait(0.55)
        self.stage("只有一个方向成立，不够称为曲线的方程", C_POINT)
        axes, circle = self.axes_and_circle()
        # 若把曲线误当成右半圆，(-2,0) 满足等式，却不在右半圆上。
        right_semicircle = Arc(radius=1.6, start_angle=-PI/2,
                               angle=PI, arc_center=axes.c2p(0, 0),
                               color=C_VALID, stroke_width=7)
        self.play(Create(right_semicircle), run_time=0.6)
        self.mark(axes, left, r"S(-2,0)", C_POINT, DL)
        self.panel("如果把曲线 C 限定为右半圆", r"(-2)^2+0^2=4",
                   "S 满足圆方程，却不在右半圆：反向条件失败", C_POINT)
        self.wait(1.0)

    def show_summary(self):
        self.stage("曲线与方程：两个方向同时成立")
        upper = VGroup(self.cn("曲线 C 上的每个点", 26, C_CURVE),
                       MathTex(r"\Longrightarrow F(x,y)=0", font_size=30)).arrange(DOWN, buff=0.2)
        lower = VGroup(MathTex(r"F(x,y)=0\ \text{的每个实数解}", font_size=29),
                       self.cn("对应的点也都在曲线 C 上", 25, C_VALID)).arrange(DOWN, buff=0.2)
        upper.move_to(UP * 2.3)
        lower.move_to(DOWN * 0.75)
        self.play(FadeIn(upper), FadeIn(lower), run_time=0.8)
        self.play(Write(MathTex(r"P\in C\iff F(x_P,y_P)=0",
                                font_size=32, color=YELLOW).move_to(DOWN * 3.1)), run_time=0.65)
        self.wait(1.3)

    def show_outro(self):
        self.stage("点和方程：看是否真正一一对应")
        self.play(FadeIn(self.cn("别只验证曲线上一个点，就宣称充要条件", 26)
                         .move_to(UP * 1)),
                  FadeIn(self.cn("@emptyandcalm", 26, GRAY_A).move_to(DOWN * 0.6)),
                  run_time=0.6)
        self.wait(1.2)
