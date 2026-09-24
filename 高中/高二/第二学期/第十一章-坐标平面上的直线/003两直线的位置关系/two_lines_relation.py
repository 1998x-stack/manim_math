"""两直线的位置关系：用一般式行列式统一处理斜线、水平线及垂线。

保留 TwoLinesRelation 入口和六镜头。仅改源码，不覆盖历史视频或音轨。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
COLOR_L1 = "#e74c3c"
COLOR_L2 = "#3498db"
COLOR_PARALLEL = "#f39c12"
COLOR_INTERSECT = "#2ecc71"
COLOR_COINCIDE = "#9b59b6"
FONT = "PingFang SC"


def validate_line(line):
    a, b, c = line
    if not all(math.isfinite(value) for value in (a, b, c)) or (a == 0 and b == 0):
        raise ValueError("直线要求有限系数且 A、B 不同时为零")
    return a, b, c


def determinant(line1, line2):
    a1, b1, _ = validate_line(line1)
    a2, b2, _ = validate_line(line2)
    return a1 * b2 - a2 * b1


def line_relation(line1, line2):
    """返回 intersect / parallel / coincide，不使用存在除零风险的系数比。"""
    a1, b1, c1 = validate_line(line1)
    a2, b2, c2 = validate_line(line2)
    if not math.isclose(a1 * b2 - a2 * b1, 0.0, abs_tol=1e-10):
        return "intersect"
    if (math.isclose(a1 * c2 - a2 * c1, 0.0, abs_tol=1e-10)
            and math.isclose(b1 * c2 - b2 * c1, 0.0, abs_tol=1e-10)):
        return "coincide"
    return "parallel"


def intersection(line1, line2):
    """克拉默法则求唯一交点；平行和重合没有唯一交点。"""
    a1, b1, c1 = validate_line(line1)
    a2, b2, c2 = validate_line(line2)
    d = a1 * b2 - a2 * b1
    if math.isclose(d, 0.0, abs_tol=1e-10):
        raise ValueError("两直线没有唯一交点")
    return (b1 * c2 - b2 * c1) / d, (c1 * a2 - c2 * a1) / d


def clipped_line(line, xb=(-3.0, 3.0), yb=(-2.0, 4.0)):
    """求一般式直线与图中坐标矩形的线段，图外直线不得假装在图内。"""
    a, b, c = validate_line(line)
    xmin, xmax = xb
    ymin, ymax = yb
    if xmin >= xmax or ymin >= ymax:
        raise ValueError("坐标窗口必须非退化")
    hits = []
    if b != 0:
        for x in (xmin, xmax):
            y = -(a * x + c) / b
            if ymin - 1e-10 <= y <= ymax + 1e-10:
                hits.append((x, min(ymax, max(ymin, y))))
    if a != 0:
        for y in (ymin, ymax):
            x = -(b * y + c) / a
            if xmin - 1e-10 <= x <= xmax + 1e-10:
                hits.append((min(xmax, max(xmin, x)), y))
    distinct = []
    for point in hits:
        if not any(math.dist(point, other) < 1e-9 for other in distinct):
            distinct.append(point)
    if len(distinct) < 2:
        raise ValueError("直线未在坐标窗内形成可绘制线段")
    return max(
        ((p, q) for index, p in enumerate(distinct) for q in distinct[index + 1:]),
        key=lambda pair: math.dist(*pair),
    )


class TwoLinesRelation(Scene):
    """平行、重合、相交，先看方程的有效性再画出结论。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.banner = Text("上海初高中数学直通车  @emptyandcalm", font=FONT,
                           font_size=17, color=GRAY_B).move_to(UP * 6.95)
        self.add(self.banner)
        self.scene_opening()
        self.scene_parallel()
        self.scene_coincident()
        self.scene_intersect()
        self.scene_summary()
        self.scene_outro()

    def cn(self, text, size=25, color=WHITE):
        return Text(text, font=FONT, font_size=size, color=color)

    def stage(self, title, color=GOLD):
        old = [obj for obj in self.mobjects if obj is not self.banner]
        if old:
            self.play(*[FadeOut(obj) for obj in old], run_time=0.4)
        self.play(FadeIn(self.cn(title, 36, color).move_to(UP * 6.0)), run_time=0.4)

    def axes(self):
        ax = Axes(x_range=[-3, 3, 1], y_range=[-2, 4, 1],
                  x_length=6.0, y_length=5.2,
                  axis_config={"color": GRAY_B, "include_numbers": True,
                               "font_size": 19}, tips=False).move_to(UP * 1.45)
        self.play(Create(ax), run_time=0.65)
        return ax

    def draw(self, ax, coeff, color, stroke_width=5):
        p, q = clipped_line(coeff)
        obj = Line(ax.c2p(*p), ax.c2p(*q), color=color, stroke_width=stroke_width)
        self.play(Create(obj), run_time=0.6)
        return obj

    def formula_panel(self, label, tex, note, color):
        panel = RoundedRectangle(width=8.0, height=2.6, corner_radius=0.12,
                                 fill_color="#16213e", fill_opacity=0.95,
                                 stroke_color=color, stroke_width=2).move_to(DOWN * 4.7)
        title = self.cn(label, 23, color).move_to(panel.get_center() + UP * 0.85)
        formula = MathTex(tex, font_size=31).move_to(panel.get_center() + UP * 0.05)
        formula.scale_to_fit_width(min(formula.width, 7.3))
        caution = self.cn(note, 19, GRAY_A).move_to(panel.get_center() + DOWN * 0.85)
        self.play(FadeIn(panel), FadeIn(title), Write(formula), FadeIn(caution), run_time=0.85)

    def scene_opening(self):
        self.stage("两直线有几种位置关系？")
        items = VGroup(self.cn("平行：没有交点", 29, COLOR_PARALLEL),
                       self.cn("重合：有无数个公共点", 29, COLOR_COINCIDE),
                       self.cn("相交：恰好一个交点", 29, COLOR_INTERSECT))
        items.arrange(DOWN, buff=0.7).move_to(UP * 0.7)
        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(0.7)

    def scene_parallel(self):
        self.stage("① 平行：方向相同、位置不同", COLOR_PARALLEL)
        line1 = (-1, 1, -2)  # y=x+2
        line2 = (-1, 1, 1)   # y=x-1
        assert line_relation(line1, line2) == "parallel"
        ax = self.axes()
        self.draw(ax, line1, COLOR_L1)
        self.draw(ax, line2, COLOR_L2)
        self.play(FadeIn(MathTex(r"l_1:y=x+2", color=COLOR_L1, font_size=27).move_to(UP * 4.7)),
                  FadeIn(MathTex(r"l_2:y=x-1", color=COLOR_L2, font_size=27).move_to(DOWN * 2.45)),
                  run_time=0.5)
        self.formula_panel("两线都有斜率时", r"k_1=k_2,\quad b_1\ne b_2",
                           "垂直线也可能平行，不能只比较斜率", COLOR_PARALLEL)
        self.wait(1.0)

    def scene_coincident(self):
        self.stage("② 重合：不同方程也能表示同一条线", COLOR_COINCIDE)
        line1 = (-1, 1, -1)  # y=x+1
        line2 = (2, -2, 2)   # 上式乘以 -2
        assert line_relation(line1, line2) == "coincide"
        ax = self.axes()
        self.draw(ax, line1, COLOR_L1, stroke_width=6)
        self.draw(ax, line2, COLOR_L2, stroke_width=3)
        self.play(FadeIn(MathTex(r"l_1:y=x+1", color=COLOR_L1, font_size=27).move_to(UP * 4.7)),
                  FadeIn(MathTex(r"l_2:2x-2y+2=0", color=COLOR_L2, font_size=27).move_to(DOWN * 2.45)),
                  run_time=0.5)
        self.formula_panel("两组系数成比例", r"A_1B_2-A_2B_1=0",
                           "还需核对常数项；同斜率且同截距才重合", COLOR_COINCIDE)
        self.wait(1.0)

    def scene_intersect(self):
        self.stage("③ 相交：有唯一公共点", COLOR_INTERSECT)
        line1 = (-1, 1, -1)  # y=x+1
        line2 = (1, 1, -3)   # y=-x+3
        assert line_relation(line1, line2) == "intersect"
        p = intersection(line1, line2)
        assert math.dist(p, (1, 2)) < 1e-10
        ax = self.axes()
        self.draw(ax, line1, COLOR_L1)
        self.draw(ax, line2, COLOR_L2)
        dot = Dot(ax.c2p(*p), radius=0.13, color=COLOR_INTERSECT)
        label = MathTex(r"P(1,2)", font_size=27, color=COLOR_INTERSECT).next_to(dot, UR, buff=0.15)
        self.play(FadeIn(dot), FadeIn(label), run_time=0.4)
        self.play(FadeIn(MathTex(r"y=x+1,\quad y=-x+3", font_size=28).move_to(DOWN * 2.4)),
                  run_time=0.35)
        self.formula_panel("联立得到 x=1，y=2", r"D=A_1B_2-A_2B_1\ne0",
                           "两线系数行列式非零，恰有一个交点", COLOR_INTERSECT)
        self.wait(1.0)

    def scene_summary(self):
        self.stage("一般式：适用于所有方向的直线")
        intro = MathTex(r"l_i:A_ix+B_iy+C_i=0", font_size=34).move_to(UP * 4.65)
        self.play(Write(intro), run_time=0.5)
        cases = (
            ("相交", r"D=A_1B_2-A_2B_1\ne0", COLOR_INTERSECT,
             "有唯一交点"),
            ("平行", r"D=0", COLOR_PARALLEL,
             "且两方程不表示同一直线"),
            ("重合", r"D=0", COLOR_COINCIDE,
             "且 (A,B,C) 三项成比例"),
        )
        for index, (name, formula, color, condition) in enumerate(cases):
            y = 2.25 - 2.75 * index
            box = RoundedRectangle(width=8, height=2.3, corner_radius=0.15,
                                   fill_color="#16213e", fill_opacity=0.95,
                                   stroke_color=color, stroke_width=2).move_to(UP * y)
            title = self.cn(name, 27, color).move_to(box.get_center() + UP * 0.64)
            expr = MathTex(formula, font_size=27).move_to(box.get_center())
            note = self.cn(condition, 20, GRAY_A).move_to(box.get_center() + DOWN * 0.7)
            self.play(FadeIn(VGroup(box, title, expr, note)), run_time=0.4)
        self.wait(1.6)

    def scene_outro(self):
        self.stage("三种关系，统一由一般式判断")
        self.play(FadeIn(self.cn("先判断是否重合，再区分平行与相交", 27).move_to(UP * 1.1)),
                  FadeIn(self.cn("@emptyandcalm", 28, GRAY_B).move_to(DOWN * 0.3)),
                  run_time=0.7)
        self.wait(1.4)
