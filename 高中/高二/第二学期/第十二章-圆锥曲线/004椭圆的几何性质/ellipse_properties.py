"""椭圆几何性质：数据坐标驱动焦点、准线、焦半径、通径和可见动画。

保留 EllipseProperties 与九个原分镜入口；不覆盖原有视频、音轨及 prompt。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_ELLIPSE = "#e74c3c"
C_FOCUS = "#f39c12"
C_DIRECTRIX = "#9b59b6"
C_LATUS = "#16a085"
FONT = "Noto Sans CJK SC"
A, B = 3.0, 2.0


def ellipse_parameters(a=A, b=B):
    """横向非退化椭圆的半焦距和离心率，要求 a>b>0。"""
    if not all(math.isfinite(v) for v in (a, b)) or not a > b > 0:
        raise ValueError("椭圆需要有限参数 a>b>0")
    c = math.sqrt((a-b)*(a+b))
    return c, c/a


def ellipse_point(theta, a=A, b=B):
    if not math.isfinite(theta):
        raise ValueError("参数角必须有限")
    ellipse_parameters(a, b)
    return a*math.cos(theta), b*math.sin(theta)


def ellipse_residual(point, a=A, b=B):
    ellipse_parameters(a, b)
    x, y = point
    if not all(math.isfinite(v) for v in (x, y)):
        raise ValueError("点坐标必须有限")
    return (x/a)**2+(y/b)**2-1


def ellipse_foci(a=A, b=B):
    c, _ = ellipse_parameters(a, b)
    return (-c, 0.), (c, 0.)


def focal_radii(point, a=A, b=B):
    f1, f2 = ellipse_foci(a, b)
    return math.dist(point, f1), math.dist(point, f2)


def focal_radius_formula(point, a=A, b=B):
    """仅对椭圆上的点适用：|PF1|=a+ex，|PF2|=a-ex。"""
    if abs(ellipse_residual(point, a, b)) > 1e-8:
        raise ValueError("焦半径公式的点必须位于椭圆上")
    _, e = ellipse_parameters(a, b)
    return a+e*point[0], a-e*point[0]


def directrix_positions(a=A, b=B):
    c, _ = ellipse_parameters(a, b)
    d = a*a/c
    return -d, d


def latus_rectum_endpoints(a=A, b=B):
    c, _ = ellipse_parameters(a, b)
    y = b*b/a
    return (c, -y), (c, y)


def axis_units(x_bounds=(-5., 5.), y_bounds=(-4., 4.),
               x_length=7., y_length=5.6):
    if (x_bounds[0]>=x_bounds[1] or y_bounds[0]>=y_bounds[1]
            or not all(math.isfinite(v) and v>0 for v in (x_length, y_length))):
        raise ValueError("轴域和画面长度必须有效")
    return x_length/(x_bounds[1]-x_bounds[0]), y_length/(y_bounds[1]-y_bounds[0])


class EllipseProperties(Scene):
    """九镜：范围对称、离心率、准线、焦半径、通径及可见总结。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font=FONT, font_size=17, color=GRAY_B).move_to(UP*6.8)
        self.add(self.author)
        self.show_opening()
        self.show_range_symmetry()
        self.show_eccentricity_concept()
        self.show_eccentricity_effect()
        self.show_directrix()
        self.show_focal_radius()
        self.show_latus_rectum()
        self.show_summary()
        self.show_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def stage(self, heading, color=GOLD):
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(*[FadeOut(obj) for obj in visible], run_time=0.4)
        self.play(FadeIn(self.cn(heading, 34, color).move_to(UP*5.9)), run_time=0.4)

    def diagram(self, a=A, b=B, draw_foci=True):
        ux, uy = axis_units()
        assert math.isclose(ux, uy, rel_tol=0, abs_tol=1e-12)
        axes = Axes(x_range=[-5,5,1], y_range=[-4,4,1],
                    x_length=7., y_length=5.6, tips=False,
                    axis_config={"color": GRAY_B, "include_numbers": False}).move_to(UP*1.4)
        curve = Ellipse(width=2*a*ux, height=2*b*uy,
                        stroke_width=5, color=C_ELLIPSE).move_to(axes.c2p(0,0))
        self.play(Create(axes), Create(curve), run_time=0.8)
        if draw_foci:
            for index, focus in enumerate(ellipse_foci(a, b), start=1):
                dot = Dot(axes.c2p(*focus), radius=0.085, color=C_FOCUS)
                label = MathTex(f"F_{index}", font_size=22, color=C_FOCUS).next_to(dot, DOWN, buff=0.1)
                self.play(FadeIn(dot), FadeIn(label), run_time=0.17)
        return axes, curve

    def panel(self, title, tex, note, color=YELLOW):
        rect = RoundedRectangle(width=8.0, height=2.45, corner_radius=0.14,
                                stroke_width=2, stroke_color=color,
                                fill_color="#16213e", fill_opacity=0.95).move_to(DOWN*4.6)
        title_obj = self.cn(title, 22, color).move_to(rect.get_center()+UP*0.75)
        equation = MathTex(tex, font_size=30).move_to(rect.get_center()+UP*0.02)
        equation.scale_to_fit_width(min(equation.width, 7.45))
        note_obj = self.cn(note, 18, GRAY_A).move_to(rect.get_center()+DOWN*0.76)
        note_obj.scale_to_fit_width(min(note_obj.width, 7.5))
        self.play(FadeIn(rect), FadeIn(title_obj), Write(equation), FadeIn(note_obj), run_time=0.75)

    def show_opening(self):
        self.stage("从椭圆方程探索几何性质")
        self.diagram()
        self.panel("标准方程：a=3，b=2，c=√5", r"\frac{x^2}{9}+\frac{y^2}{4}=1",
                   "以下所有点与长度都使用该坐标系", C_ELLIPSE)
        self.wait(0.7)

    def show_range_symmetry(self):
        self.stage("① 椭圆范围与四重对称")
        ax, curve = self.diagram()
        bounds = Rectangle(width=2*A*axis_units()[0], height=2*B*axis_units()[1],
                           color=GRAY_B, stroke_width=2).move_to(ax.c2p(0,0))
        self.play(Create(bounds), run_time=0.45)
        theta = math.pi/4
        x, y = ellipse_point(theta)
        # 原例 (2, 1.3) 不在曲线上；四个对称点必须与标准方程逐个对应。
        for px, py in ((x,y), (x,-y), (-x,y), (-x,-y)):
            assert abs(ellipse_residual((px, py))) < 1e-10
            self.play(FadeIn(Dot(ax.c2p(px,py), radius=0.11, color=YELLOW)), run_time=0.23)
        self.panel("横轴、纵轴与原点均为对称元素",
                   r"-3\le x\le3,\quad -2\le y\le2",
                   "每个对称点都满足同一个椭圆方程", C_ELLIPSE)
        self.wait(0.75)

    def show_eccentricity_concept(self):
        self.stage("② 离心率是半焦距与长半轴之比")
        ax, curve = self.diagram()
        c, e = ellipse_parameters()
        self.play(Create(Line(ax.c2p(0,0), ax.c2p(c,0), color=C_FOCUS, stroke_width=4)),
                  run_time=0.5)
        self.panel("焦距为 2c，不要把焦距和半焦距混淆",
                   r"e=\frac ca=\frac{\sqrt5}{3}\approx0.745",
                   "非退化椭圆满足 0<e<1", C_FOCUS)
        self.wait(0.85)

    def show_eccentricity_effect(self):
        self.stage("③ 固定长半轴 a，比较不同离心率")
        ax, base = self.diagram()
        flat_b, round_b = 0.65, 2.99
        _, flat_e = ellipse_parameters(A, flat_b)
        _, round_e = ellipse_parameters(A, round_b)
        for b, e, explanation in ((flat_b, flat_e, "e 接近 1：椭圆较扁"),
                                  (round_b, round_e, "e 接近 0：椭圆接近圆")):
            new_ellipse = Ellipse(width=2*A*axis_units()[0],
                                  height=2*b*axis_units()[1],
                                  color=YELLOW, stroke_width=5).move_to(ax.c2p(0,0))
            label = self.cn(explanation, 23, YELLOW).move_to(DOWN*2.55)
            formula = MathTex(rf"a=3,\quad b={b:.2f},\quad e\approx{e:.3f}",
                              font_size=27).move_to(DOWN*3.05)
            self.play(Create(new_ellipse), FadeIn(label), FadeIn(formula), run_time=0.65)
            self.wait(0.55)
            self.play(FadeOut(new_ellipse), FadeOut(label), FadeOut(formula), run_time=0.35)
        self.panel("圆是 e→0 的极限，线段是 e→1 的退化极限",
                   r"e=\sqrt{1-\frac{b^2}{a^2}}",
                   "本课只讨论 a>b>0 的非退化椭圆", C_ELLIPSE)
        self.wait(0.75)

    def show_directrix(self):
        self.stage("④ 两条准线 x=±a²/c", C_DIRECTRIX)
        ax, curve = self.diagram()
        left, right = directrix_positions()
        for coordinate, sign in ((left, "-"), (right, "+")):
            line = DashedLine(ax.c2p(coordinate,-3.7), ax.c2p(coordinate,3.7),
                              color=C_DIRECTRIX, stroke_width=3, dash_length=0.13)
            label = MathTex(rf"x={sign}\frac{{9}}{{\sqrt5}}",
                            font_size=21, color=C_DIRECTRIX).next_to(line, UP, buff=0.08)
            self.play(Create(line), FadeIn(label), run_time=0.5)
        self.panel("准线分别位于焦点外侧，且都在轴域内",
                   r"x=\pm\frac{a^2}{c}=\pm\frac9{\sqrt5}",
                   "准线与焦点不可画在同一个 x 坐标上", C_DIRECTRIX)
        self.wait(0.75)

    def show_focal_radius(self):
        self.stage("⑤ 焦半径：同一椭圆点的两段距离")
        ax, curve = self.diagram()
        p = ellipse_point(math.pi/4)
        f1, f2 = ellipse_foci()
        actual = focal_radii(p)
        expected = focal_radius_formula(p)
        assert all(math.isclose(x,y,abs_tol=1e-10) for x,y in zip(actual, expected))
        dot = Dot(ax.c2p(*p), radius=0.1, color=YELLOW)
        self.play(FadeIn(dot), Create(Line(ax.c2p(*p), ax.c2p(*f1), color=C_FOCUS)),
                  Create(Line(ax.c2p(*p), ax.c2p(*f2), color=C_LATUS)), run_time=0.65)
        self.panel("左焦点 F₁ 与右焦点 F₂ 的符号不同",
                   r"|PF_1|=a+ex_0,\quad |PF_2|=a-ex_0",
                   "两条焦半径之和恒为 2a=6", C_FOCUS)
        self.wait(0.8)

    def show_latus_rectum(self):
        self.stage("⑥ 通径：过焦点且垂直长轴的弦", C_LATUS)
        ax, curve = self.diagram()
        p, q = latus_rectum_endpoints()
        assert abs(ellipse_residual(p))<1e-10 and abs(ellipse_residual(q))<1e-10
        segment = Line(ax.c2p(*p), ax.c2p(*q), color=C_LATUS, stroke_width=5)
        self.play(Create(segment), FadeIn(Dot(ax.c2p(*p), color=YELLOW)),
                  FadeIn(Dot(ax.c2p(*q), color=YELLOW)), run_time=0.65)
        self.panel("端点 (c,±b²/a)，实际坐标长度 8/3",
                   r"\ell=\frac{2b^2}{a}=\frac83",
                   "通径过右焦点；左焦点处有对称的一条", C_LATUS)
        self.wait(0.85)

    def show_summary(self):
        self.stage("椭圆几何性质：由方程到图形")
        cards = (
            ("范围与对称", r"|x|\le a,\ |y|\le b", C_ELLIPSE),
            ("离心率", r"e=c/a,\quad 0<e<1", C_FOCUS),
            ("两条准线", r"x=\pm a^2/c", C_DIRECTRIX),
            ("焦半径", r"|PF_1|+|PF_2|=2a", YELLOW),
            ("通径", r"\ell=2b^2/a", C_LATUS),
        )
        for index, (name, formula, color) in enumerate(cards):
            center_y = 3.9-index*2.1
            box = RoundedRectangle(width=7.8, height=1.7, corner_radius=0.12,
                                   stroke_color=color, stroke_width=2,
                                   fill_color="#16213e", fill_opacity=0.95).move_to(UP*center_y)
            title = self.cn(name, 23, color).move_to(box.get_center()+UP*0.45)
            math_formula = MathTex(formula, font_size=28).move_to(box.get_center()+DOWN*0.35)
            self.play(FadeIn(VGroup(box,title,math_formula), shift=RIGHT*0.25), run_time=0.35)
        self.wait(1.4)

    def show_outro(self):
        self.stage("核对条件、坐标和实际图形")
        self.play(FadeIn(self.cn("每个公式都应与同一幅几何图相对应", 26)
                         .move_to(UP*1.1)),
                  FadeIn(self.cn("@emptyandcalm", 26, GRAY_A).move_to(DOWN*0.6)),
                  run_time=0.65)
        self.wait(1.3)
