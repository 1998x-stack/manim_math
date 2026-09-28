"""椭圆定义与标准方程：焦点距离和与屏幕几何由同一数据模型给出。

保留 EllipseEquation Scene 入口和八个原教学分镜；不覆盖 MP4、音轨、prompt。
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
C_MAJOR = "#3498db"
C_MINOR = "#2ecc71"
FONT = "PingFang SC"
A = 3.0
B = 2.0


def ellipse_focal_length(a=A, b=B):
    """真椭圆 a>b>0，半焦距 c=sqrt(a²-b²)。"""
    if not all(math.isfinite(v) for v in (a,b)) or not a > b > 0:
        raise ValueError("椭圆参数必须有限且满足 a>b>0")
    return math.sqrt(a*a-b*b)


def ellipse_point(theta, a=A, b=B, vertical=False):
    if not math.isfinite(theta):
        raise ValueError("参数角必须有限")
    ellipse_focal_length(a,b)
    return (b*math.cos(theta), a*math.sin(theta)) if vertical else (a*math.cos(theta), b*math.sin(theta))


def ellipse_foci(a=A, b=B, vertical=False):
    c = ellipse_focal_length(a,b)
    return ((0,-c),(0,c)) if vertical else ((-c,0),(c,0))


def focal_distance_sum(point, a=A, b=B, vertical=False):
    x,y = point
    if not all(math.isfinite(v) for v in (x,y)):
        raise ValueError("点坐标必须有限")
    f1,f2 = ellipse_foci(a,b,vertical)
    return math.dist(point,f1)+math.dist(point,f2)


def ellipse_residual(point, a=A, b=B, vertical=False):
    ellipse_focal_length(a,b)
    x,y = point
    if not all(math.isfinite(v) for v in (x,y)):
        raise ValueError("点坐标必须有限")
    return x*x/(b*b)+y*y/(a*a)-1 if vertical else x*x/(a*a)+y*y/(b*b)-1


def axis_units(x_bounds=(-4.0,4.0), y_bounds=(-4.0,4.0),
               x_length=5.6, y_length=5.6):
    if (x_bounds[0]>=x_bounds[1] or y_bounds[0]>=y_bounds[1]
            or not math.isfinite(x_length) or not math.isfinite(y_length)
            or x_length<=0 or y_length<=0):
        raise ValueError("轴域和画面长度必须有效")
    return (x_length/(x_bounds[1]-x_bounds[0]),
            y_length/(y_bounds[1]-y_bounds[0]))


class EllipseEquation(Scene):
    """八镜说明双焦点定义、标准式、长短轴及四顶点。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                           font_size=17, color=GRAY_B).move_to(UP*6.95)
        self.add(self.author)
        self.show_opening()
        self.show_definition()
        self.show_dynamic_drawing()
        self.show_standard_equation_x()
        self.show_standard_equation_y()
        self.show_abc_relation()
        self.show_vertices()
        self.show_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def stage(self, heading, color=GOLD):
        previous = [m for m in self.mobjects if m is not self.author]
        if previous:
            self.play(*[FadeOut(m) for m in previous], run_time=0.4)
        self.play(FadeIn(self.cn(heading, 35, color).move_to(UP*6)), run_time=0.4)

    def diagram(self, vertical=False, draw_curve=True):
        ux,uy = axis_units()
        assert math.isclose(ux,uy,abs_tol=1e-12)
        ax = Axes(x_range=[-4,4,1], y_range=[-4,4,1],
                  x_length=5.6, y_length=5.6, tips=False,
                  axis_config={"color": GRAY_B, "include_numbers": True,
                               "font_size": 18}).move_to(UP*1.35)
        self.play(Create(ax), run_time=0.55)
        if draw_curve:
            curve = Ellipse(width=2*(B if vertical else A)*ux,
                            height=2*(A if vertical else B)*uy,
                            color=C_ELLIPSE, stroke_width=5).move_to(ax.c2p(0,0))
            self.play(Create(curve), run_time=0.65)
        for idx, focus in enumerate(ellipse_foci(vertical=vertical), start=1):
            dot = Dot(ax.c2p(*focus), color=C_FOCUS, radius=0.09)
            label = MathTex(r"F_"+str(idx), color=C_FOCUS,
                            font_size=23).next_to(dot, DOWN, buff=0.12)
            self.play(FadeIn(dot), FadeIn(label), run_time=0.25)
        return ax

    def panel(self, title, formula, note, color=YELLOW):
        frame = RoundedRectangle(width=8.0, height=2.55, corner_radius=0.15,
                                 fill_color="#16213e", fill_opacity=0.95,
                                 stroke_color=color, stroke_width=2).move_to(DOWN*4.75)
        title_obj = self.cn(title, 22, color).move_to(frame.get_center()+UP*0.83)
        tex = MathTex(formula, font_size=31).move_to(frame.get_center()+UP*0.04)
        tex.scale_to_fit_width(min(tex.width, 7.45))
        note_obj = self.cn(note, 19, GRAY_A).move_to(frame.get_center()+DOWN*0.8)
        self.play(FadeIn(frame), FadeIn(title_obj), Write(tex), FadeIn(note_obj), run_time=0.8)

    def show_opening(self):
        self.stage("由两个焦点，怎样确定一条椭圆？")
        ax = self.diagram()
        self.panel("焦点 F₁、F₂ 到动点 P 的距离和恒定",
                   r"|PF_1|+|PF_2|=2a=6",
                   "两个焦点之间的距离是 2c，且 2a>2c", C_ELLIPSE)
        self.wait(0.7)

    def show_definition(self):
        self.stage("椭圆定义：到两定点距离之和等于定长")
        ax = self.diagram()
        point = ellipse_point(0)
        f1,f2 = ellipse_foci()
        self.play(Create(Line(ax.c2p(*point), ax.c2p(*f1), color=C_FOCUS)),
                  Create(Line(ax.c2p(*point), ax.c2p(*f2), color=C_FOCUS)),
                  FadeIn(Dot(ax.c2p(*point), color=YELLOW, radius=0.1)),
                  run_time=0.55)
        assert math.isclose(focal_distance_sum(point),2*A,abs_tol=1e-10)
        self.panel("P=(3,0)，两段距离为 3+c 和 3-c",
                   r"(3+\sqrt5)+(3-\sqrt5)=6",
                   "取 P 为另一顶点或任意圆周点，焦距和仍为 6", C_FOCUS)
        self.wait(0.75)

    def show_dynamic_drawing(self):
        self.stage("让 P 移动，检查焦距和是否保持不变")
        ax = self.diagram(draw_curve=False)
        f1,f2 = ellipse_foci()
        t = ValueTracker(0)
        def screen_point():
            return ax.c2p(*ellipse_point(t.get_value()))
        p_dot = always_redraw(lambda: Dot(screen_point(),radius=0.095,color=YELLOW))
        connector1 = always_redraw(lambda: Line(screen_point(),ax.c2p(*f1),color=C_FOCUS))
        connector2 = always_redraw(lambda: Line(screen_point(),ax.c2p(*f2),color=C_FOCUS))
        trace = TracedPath(screen_point, stroke_color=C_ELLIPSE, stroke_width=4)
        label = MathTex(r"|PF_1|+|PF_2|=",font_size=27).move_to(DOWN*2.75+LEFT*0.8)
        number = always_redraw(lambda: DecimalNumber(
            focal_distance_sum(ellipse_point(t.get_value())),
            num_decimal_places=2,font_size=27,color=YELLOW).next_to(label,RIGHT,buff=0.1))
        self.add(trace,p_dot,connector1,connector2,label,number)
        self.play(t.animate.set_value(TAU), run_time=4.0, rate_func=linear)
        self.wait(0.65)
        # 追踪和距离数值来自数据单位，不把屏幕线段长度误认作 2a。
        self.remove(trace,p_dot,connector1,connector2,label,number)

    def show_standard_equation_x(self):
        self.stage("焦点在 x 轴：长半轴 a=3、短半轴 b=2")
        ax = self.diagram()
        self.panel("F₁、F₂ 位于 (±√5,0)",
                   r"\frac{x^2}{9}+\frac{y^2}{4}=1",
                   "长轴沿 x 方向，必须满足 a>b>0", C_MAJOR)
        self.wait(0.9)

    def show_standard_equation_y(self):
        self.stage("焦点在 y 轴：长半轴仍为 a=3")
        ax = self.diagram(vertical=True)
        self.panel("F₁、F₂ 位于 (0,±√5)",
                   r"\frac{x^2}{4}+\frac{y^2}{9}=1",
                   "标准方程中分母较大的一项对应长轴方向", C_MAJOR)
        self.wait(0.9)

    def show_abc_relation(self):
        self.stage("半焦距 c 与长短半轴的关系")
        ax = self.diagram()
        c = ellipse_focal_length()
        p0,p1,p2 = ax.c2p(0,0), ax.c2p(c,0), ax.c2p(c,B)
        self.play(Create(Line(p0,p1,color=C_FOCUS,stroke_width=4)),
                  Create(Line(p1,p2,color=C_MINOR,stroke_width=4)),
                  Create(Line(p2,p0,color=C_MAJOR,stroke_width=4)),run_time=0.7)
        self.panel("直角三角形的三边分别为 c、b、a",
                   r"a^2=b^2+c^2,\quad 9=4+5",
                   "因此 c=√5，且 0<c<a；不能把 c 当作焦距 2c", C_MAJOR)
        self.wait(0.85)

    def show_vertices(self):
        self.stage("椭圆的四个顶点与两条对称轴")
        ax = self.diagram()
        for point,label,color in (((-A,0),r"(-3,0)",C_MAJOR),
                                  ((A,0),r"(3,0)",C_MAJOR),
                                  ((0,-B),r"(0,-2)",C_MINOR),
                                  ((0,B),r"(0,2)",C_MINOR)):
            dot = Dot(ax.c2p(*point),color=color,radius=0.09)
            text = MathTex(label,font_size=22,color=color).next_to(dot,UP,buff=0.12)
            self.play(FadeIn(dot),FadeIn(text),run_time=0.24)
        self.panel("横向椭圆：长轴长 2a，短轴长 2b",
                   r"2a=6,\quad 2b=4",
                   "四个顶点分别是 (±3,0)、(0,±2)", C_MAJOR)
        self.wait(0.85)

    def show_outro(self):
        self.stage("椭圆：由定义到两种标准方程")
        self.play(FadeIn(self.cn("先确认长轴方向，再标注两个焦点",27,YELLOW)
                         .move_to(UP*1.1)),
                  FadeIn(self.cn("@emptyandcalm",26,GRAY_A).move_to(DOWN*0.6)),
                  run_time=0.65)
        self.wait(1.2)
