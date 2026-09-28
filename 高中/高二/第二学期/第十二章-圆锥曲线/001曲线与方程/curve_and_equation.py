"""《曲线与方程》：圆周几何与方程使用同一模型，验证两个逻辑方向。

保留 CurveAndEquation 入口及原有八镜头；不修改历史 MP4、音轨与 prompt。
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
FONT = "PingFang SC"
RADIUS = 2.0


def circle_point(theta, radius=RADIUS):
    """数据坐标中的圆周点，而不是屏幕单位估算。"""
    if not math.isfinite(theta) or not math.isfinite(radius) or radius <= 0:
        raise ValueError("角度须有限，半径须有限且为正")
    return radius * math.cos(theta), radius * math.sin(theta)


def circle_residual(point, radius=RADIUS):
    """x²+y²-r²；当且仅当为零时坐标是精确解。"""
    x, y = point
    if not all(math.isfinite(v) for v in (x, y, radius)) or radius <= 0:
        raise ValueError("坐标须有限，半径须为正")
    return x*x + y*y - radius*radius


def circle_contains(point, radius=RADIUS, tolerance=1e-9):
    """数值检查容差仅服务浮点计算，圆周数学定义仍以等式为准。"""
    if tolerance < 0 or not math.isfinite(tolerance):
        raise ValueError("容差须有限且非负")
    return abs(circle_residual(point, radius)) <= tolerance


def axis_unit_sizes(x_bounds=(-4.0, 4.0), y_bounds=(-3.0, 3.0),
                    x_length=6.4, y_length=4.8):
    """以同一个画面单位表示 x、y：保证画圆时点、标签和直角一致。"""
    if (x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1]
            or not math.isfinite(x_length) or not math.isfinite(y_length)
            or x_length <= 0 or y_length <= 0):
        raise ValueError("坐标轴窗口或画面长度无效")
    return (x_length / (x_bounds[1]-x_bounds[0]),
            y_length / (y_bounds[1]-y_bounds[0]))


class CurveAndEquation(Scene):
    """依次说明两方向、反例和充要条件，不以一次抽样作为全称证明。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=17, color=GRAY_B).move_to(UP*6.95)
        self.add(self.author)
        self.show_opening()
        self.show_coordinate_system()
        self.show_equation_concept()
        self.show_sufficiency_forward()
        self.show_sufficiency_backward()
        self.show_counterexample()
        self.show_summary()
        self.show_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def stage(self, name, color=GOLD):
        old = [m for m in self.mobjects if m is not self.author]
        if old:
            self.play(*[FadeOut(m) for m in old], run_time=0.4)
        self.play(FadeIn(self.cn(name, 35, color).move_to(UP*6)), run_time=0.4)

    def axes_and_circle(self):
        ux, uy = axis_unit_sizes()
        assert math.isclose(ux, uy, abs_tol=1e-12)
        axes = Axes(x_range=[-4,4,1], y_range=[-3,3,1],
                    x_length=6.4, y_length=4.8, tips=False,
                    axis_config={"color": GRAY_B, "include_numbers": True,
                                 "font_size": 18}).move_to(UP*1.45)
        circle = Circle(radius=RADIUS*ux, color=C_CURVE,
                        stroke_width=5).move_to(axes.c2p(0,0))
        self.play(Create(axes), Create(circle), run_time=0.85)
        return axes, circle

    def mark(self, axes, point, name, color=C_POINT, direction=UR):
        dot = Dot(axes.c2p(*point), radius=0.10, color=color)
        label = MathTex(name, font_size=25, color=color).next_to(dot, direction, buff=0.13)
        self.play(FadeIn(dot), FadeIn(label), run_time=0.4)
        return dot

    def panel(self, name, formula, note, color=C_VALID):
        rect = RoundedRectangle(width=8.0, height=2.6, corner_radius=0.15,
                                stroke_color=color, stroke_width=2,
                                fill_color="#16213e", fill_opacity=0.95).move_to(DOWN*4.7)
        title = self.cn(name, 22, color).move_to(rect.get_center()+UP*0.84)
        equation = MathTex(formula, font_size=30).move_to(rect.get_center()+UP*0.02)
        equation.scale_to_fit_width(min(equation.width, 7.45))
        explanation = self.cn(note, 19, GRAY_A).move_to(rect.get_center()+DOWN*0.82)
        self.play(FadeIn(rect), FadeIn(title), Write(equation), FadeIn(explanation), run_time=0.8)

    def show_opening(self):
        self.stage("一个圆，怎样用方程准确描述？")
        self.play(Create(Circle(radius=1.5, color=C_CURVE, stroke_width=5)
                         .move_to(UP*1.2)), run_time=0.8)
        self.play(FadeIn(self.cn("圆周上的点与方程的解要一致", 26)
                         .move_to(DOWN*2.2)), run_time=0.5)
        self.wait(0.7)

    def show_coordinate_system(self):
        self.stage("先建立横纵单位相同的坐标系")
        axes, circle = self.axes_and_circle()
        self.play(Write(MathTex(r"O(0,0),\quad r=2", font_size=33)
                        .move_to(DOWN*2.6)), run_time=0.5)
        self.panel("圆周上每一点到 O 的距离都是 2", r"x^2+y^2=2^2",
                   "等比例坐标系中，画面半径就是 2 个数据单位", C_CURVE)
        self.wait(0.75)

    def show_equation_concept(self):
        self.stage("圆的方程是什么？")
        axes, circle = self.axes_and_circle()
        self.mark(axes, (2,0), r"A(2,0)", direction=DR)
        self.mark(axes, (0,2), r"B(0,2)", direction=UL)
        self.panel("圆周对应一个等式", r"x^2+y^2=4",
                   "圆盘的范围是 x²+y²≤4，与圆周不同", C_VALID)
        self.wait(0.8)

    def show_sufficiency_forward(self):
        self.stage("正向：曲线上的点都满足方程", C_VALID)
        axes, circle = self.axes_and_circle()
        p = (math.sqrt(2), math.sqrt(2))
        assert circle_contains(p)
        self.mark(axes, p, r"P(\sqrt2,\sqrt2)")
        self.panel("将圆上 P 的坐标代入", r"(\sqrt2)^2+(\sqrt2)^2=2+2=4",
                   "这是圆上点满足等式的一个例子", C_VALID)
        self.wait(0.9)

    def show_sufficiency_backward(self):
        self.stage("反向：方程每个实数解都给出圆周点", C_VALID)
        axes, circle = self.axes_and_circle()
        p = (0.0, 2.0)
        assert circle_contains(p)
        self.play(Write(MathTex(r"x=0,\quad y=2,\quad 0^2+2^2=4",
                                font_size=29).move_to(DOWN*2.65)), run_time=0.5)
        # 确定数对后再按实际坐标出现，禁止从假坐标位置移动“固定坐标”的点。
        self.mark(axes, p, r"Q(0,2)")
        self.panel("把实数解作为点的坐标定位", r"Q(0,2)\in C",
                   "此处 Q 与方程的对应仍是圆周充要定义的特例", C_VALID)
        self.wait(0.85)

    def show_counterexample(self):
        self.stage("反例：不在圆周上的点", C_POINT)
        axes, circle = self.axes_and_circle()
        outside = (3.0, 0.0)
        assert not circle_contains(outside)
        self.mark(axes, outside, r"R(3,0)", direction=DR)
        self.play(Write(MathTex(r"3^2+0^2=9\ne4", font_size=29,
                                color=C_POINT).move_to(DOWN*2.55)), run_time=0.5)
        self.panel("R 不在圆周上，也不满足圆方程", r"R(3,0)\notin C",
                   "这说明等式不可任意推广到圆外点", C_POINT)
        self.wait(0.55)
        self.stage("反例：只验证单方向还不够", C_POINT)
        axes, circle = self.axes_and_circle()
        self.play(FadeOut(circle), run_time=0.3)
        # 将待检验的 C 明确画成右半圆，不让蓝色完整圆造成集合含义混淆。
        right_half = Arc(radius=RADIUS*axis_unit_sizes()[0], start_angle=-PI/2,
                         angle=PI, arc_center=axes.c2p(0,0),
                         color=C_VALID, stroke_width=6)
        self.play(Create(right_half), run_time=0.55)
        left = (-2.0, 0.0)
        assert circle_contains(left) and left[0] < 0
        self.mark(axes, left, r"S(-2,0)", direction=DL)
        self.panel("若曲线 C 只取右半圆", r"(-2)^2+0^2=4",
                   "S 满足完整圆的方程，却不在右半圆 C 上", C_POINT)
        self.wait(0.95)

    def show_summary(self):
        self.stage("曲线和方程：两个方向必须都成立")
        upper = VGroup(self.cn("曲线 C 上每个点的坐标", 26, C_CURVE),
                       MathTex(r"\Longrightarrow F(x,y)=0", font_size=30))
        upper.arrange(DOWN, buff=0.25).move_to(UP*2.35)
        solution_text = VGroup(MathTex(r"F(x,y)=0", font_size=28),
                               self.cn("的每个实数解", 24))
        solution_text.arrange(RIGHT, buff=0.2)
        lower = VGroup(solution_text, self.cn("对应的点也都在曲线 C 上", 25, C_VALID))
        lower.arrange(DOWN, buff=0.25).move_to(DOWN*0.65)
        self.play(FadeIn(upper), FadeIn(lower), run_time=0.8)
        self.play(Write(MathTex(r"P\in C\iff F(x_P,y_P)=0",
                                font_size=32, color=YELLOW).move_to(DOWN*3.2)), run_time=0.65)
        self.wait(1.3)

    def show_outro(self):
        self.stage("判断曲线方程，要验证双向对应")
        self.play(FadeIn(self.cn("一个例子说明现象，但不能代替全称证明", 26)
                         .move_to(UP*1)),
                  FadeIn(self.cn("@emptyandcalm", 26, GRAY_A).move_to(DOWN*0.6)),
                  run_time=0.6)
        self.wait(1.2)
