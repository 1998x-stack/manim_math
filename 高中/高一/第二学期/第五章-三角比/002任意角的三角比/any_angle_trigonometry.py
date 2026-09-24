"""高一第二学期《任意角的三角比》：九段教学场景、真实单位圆坐标。

屏上单位圆的半径必须等于坐标轴的 1 个单位，而非简单写 Circle(radius=2)。
正切仅在 cos(alpha)!=0 时存在；象限符号规则不包括坐标轴上的角。
"""
from manim import *
import math
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
BG = "#1a1a2e"
COLORS = ("#3498db", "#e74c3c", "#9b59b6", "#2ecc71")
AUTHOR = "上海初高中数学直通车 @emptyandcalm"

# (角度制、象限、点坐标、正弦符号、余弦符号、正切符号、配色)
QUADRANTS = (
    (30, "第一象限", r"P(\frac{\sqrt3}{2},\frac12)", r"\sin\alpha>0", r"\cos\alpha>0", r"\tan\alpha>0", COLORS[0]),
    (150, "第二象限", r"P(-\frac{\sqrt3}{2},\frac12)", r"\sin\alpha>0", r"\cos\alpha<0", r"\tan\alpha<0", COLORS[1]),
    (210, "第三象限", r"P(-\frac{\sqrt3}{2},-\frac12)", r"\sin\alpha<0", r"\cos\alpha<0", r"\tan\alpha>0", COLORS[2]),
    (330, "第四象限", r"P(\frac{\sqrt3}{2},-\frac12)", r"\sin\alpha<0", r"\cos\alpha>0", r"\tan\alpha<0", COLORS[3]),
)


def cn(text, size=26, color=WHITE):
    return Text(text, font=FONT, font_size=size, color=color)


def fit(mob, width=7.5):
    if mob.width > width:
        mob.scale_to_fit_width(width)
    return mob


def trig_coordinates(degrees):
    radians = math.radians(degrees)
    return math.cos(radians), math.sin(radians)


class AnyAngleTrigonometry(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.author_info = fit(cn(AUTHOR, 17, GRAY_B)).move_to(UP * 7.45)
        self.add(self.author_info)
        self.show_opening()
        self.show_unit_circle_definition()
        self.show_quadrant_1()
        self.show_quadrant_2()
        self.show_quadrant_3()
        self.show_quadrant_4()
        self.show_sign_rule_mnemonic()
        self.show_rotation_demo()
        self.show_outro()

    def _title(self, name):
        return fit(cn(name, 35, YELLOW)).move_to(UP * 6.35)

    def _clear(self, *items):
        self.play(*[FadeOut(item) for item in items], run_time=0.5)

    def _diagram(self):
        axes = Axes(x_range=[-1.25, 1.25, 0.5], y_range=[-1.25, 1.25, 0.5],
                    x_length=5.2, y_length=5.2,
                    axis_config={"color": GRAY_B}, tips=False).move_to(DOWN * 0.1)
        origin = axes.c2p(0, 0)
        radius = np.linalg.norm(axes.c2p(1, 0) - origin)
        circle = Circle(radius=radius, color=WHITE, stroke_width=3).move_to(origin)
        return axes, circle

    def show_opening(self):
        title = self._title("任意角的三角比")
        hook = cn("锐角之外，也能定义正弦、余弦和正切", 28).move_to(UP * 2.5)
        angles = MathTex(r"30^\circ,\ 150^\circ,\ 210^\circ,\ 330^\circ",
                         font_size=37, color=YELLOW).move_to(UP * 0.2)
        note = cn("单位圆把角度与坐标联系起来", 27, GRAY_A).move_to(DOWN * 2.6)
        self.play(Write(title), FadeIn(hook), run_time=0.9)
        self.play(Write(angles), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear(title, hook, angles, note)

    def show_unit_circle_definition(self):
        title = self._title("单位圆：圆心在原点，半径为 1")
        axes, circle = self._diagram()
        origin = axes.c2p(0, 0)
        x, y = trig_coordinates(30)
        point = Dot(axes.c2p(x, y), color=COLORS[0], radius=0.09)
        radius = Line(origin, point.get_center(), color=COLORS[0], stroke_width=4)
        projection = DashedLine(point.get_center(), axes.c2p(x, 0), color=YELLOW)
        label = MathTex(r"P=(\cos\alpha,\sin\alpha)", font_size=30, color=YELLOW)
        fit(label).move_to(UP * 4.45)
        formulas = VGroup(
            MathTex(r"\sin\alpha=y", font_size=33),
            MathTex(r"\cos\alpha=x", font_size=33),
            MathTex(r"\tan\alpha=\frac{y}{x},\quad x\ne0", font_size=31, color=YELLOW),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 4.6)
        self.play(Write(title), Create(axes), Create(circle), run_time=1.1)
        self.play(Create(radius), FadeIn(point), Create(projection), Write(label), run_time=0.9)
        for formula in formulas:
            self.play(Write(formula), run_time=0.6)
        self.wait(1.0)
        self._clear(title, axes, circle, radius, point, projection, label, formulas)

    def _quadrant(self, spec):
        degrees, heading, point_tex, sin_tex, cos_tex, tan_tex, color = spec
        title = self._title(heading)
        angle = MathTex(fr"\alpha={degrees}^\circ", font_size=36, color=color).move_to(UP * 4.55)
        axes, circle = self._diagram()
        x, y = trig_coordinates(degrees)
        origin = axes.c2p(0, 0)
        pos = axes.c2p(x, y)
        radial = Line(origin, pos, color=color, stroke_width=4)
        dot = Dot(pos, color=color, radius=0.09)
        x_projection = DashedLine(pos, axes.c2p(x, 0), color=YELLOW)
        y_projection = DashedLine(pos, axes.c2p(0, y), color=YELLOW)
        coord_label = MathTex(point_tex, font_size=30, color=color).move_to(DOWN * 3.45)
        signs = VGroup(
            MathTex(sin_tex, font_size=28),
            MathTex(cos_tex, font_size=28),
            MathTex(tan_tex, font_size=28),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 4.8)
        fit(signs)
        self.play(Write(title), Write(angle), Create(axes), Create(circle), run_time=1.1)
        self.play(Create(radial), FadeIn(dot), Create(x_projection), Create(y_projection), run_time=0.9)
        self.play(Write(coord_label), FadeIn(signs), run_time=0.9)
        self.wait(0.9)
        self._clear(title, angle, axes, circle, radial, dot, x_projection, y_projection,
                    coord_label, signs)

    def show_quadrant_1(self):
        self._quadrant(QUADRANTS[0])

    def show_quadrant_2(self):
        self._quadrant(QUADRANTS[1])

    def show_quadrant_3(self):
        self._quadrant(QUADRANTS[2])

    def show_quadrant_4(self):
        self._quadrant(QUADRANTS[3])

    def show_sign_rule_mnemonic(self):
        title = self._title("象限符号取决于终边的坐标")
        header = MathTex(r"\sin\alpha\ (y),\quad\cos\alpha\ (x),\quad\tan\alpha\ (y/x)",
                         font_size=31, color=YELLOW).move_to(UP * 4.65)
        rows = VGroup(
            cn("第一象限：sin +   cos +   tan +", 28, COLORS[0]),
            cn("第二象限：sin +   cos −   tan −", 28, COLORS[1]),
            cn("第三象限：sin −   cos −   tan +", 28, COLORS[2]),
            cn("第四象限：sin −   cos +   tan −", 28, COLORS[3]),
        ).arrange(DOWN, buff=0.7).move_to(UP * 0.9)
        caveat = cn("坐标轴上的角另算；cos=0 时 tan 不存在", 24, YELLOW)
        fit(caveat).move_to(DOWN * 4.65)
        self.play(Write(title), Write(header), run_time=0.9)
        for row in rows:
            self.play(FadeIn(row, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(caveat), run_time=0.6)
        self.wait(1.0)
        self._clear(title, header, rows, caveat)

    def show_rotation_demo(self):
        title = self._title("旋转一周：坐标始终决定 sin 与 cos")
        axes, circle = self._diagram()
        tracker = ValueTracker(0)
        origin = axes.c2p(0, 0)
        radial = always_redraw(lambda: Line(origin,
                            axes.c2p(math.cos(tracker.get_value()), math.sin(tracker.get_value())),
                            color=YELLOW, stroke_width=4))
        point = always_redraw(lambda: Dot(
            axes.c2p(math.cos(tracker.get_value()), math.sin(tracker.get_value())),
            color=GREEN, radius=0.09))
        projected = always_redraw(lambda: DashedLine(
            point.get_center(), axes.c2p(math.cos(tracker.get_value()), 0), color=GRAY_A))
        label = MathTex(r"P=(\cos\alpha,\sin\alpha)", font_size=32).move_to(DOWN * 4.2)
        note = cn("过上下端点时 cos=0，不能计算 tan", 24, YELLOW).move_to(UP * 4.4)
        self.play(Write(title), Create(axes), Create(circle), run_time=0.9)
        self.add(radial, point, projected)
        self.play(Write(label), FadeIn(note), run_time=0.7)
        self.play(tracker.animate.set_value(TAU), run_time=3, rate_func=linear)
        self.wait(0.7)
        self._clear(title, axes, circle, radial, point, projected, label, note)

    def show_outro(self):
        title = self._title("任意角三角比 · 重点回顾")
        summary = VGroup(
            MathTex(r"P=(\cos\alpha,\sin\alpha)", font_size=37, color=YELLOW),
            MathTex(r"\sin\alpha=y,\quad\cos\alpha=x", font_size=35),
            MathTex(r"\tan\alpha=y/x\quad (x\ne0)", font_size=32, color=GREEN),
            cn("象限判断：先看 x 和 y 的正负", 27),
            cn("坐标轴上的角不能直接套象限符号", 24, YELLOW),
        ).arrange(DOWN, buff=0.7).move_to(UP * 1.0)
        self.play(Write(title), run_time=0.6)
        for item in summary:
            fit(item)
            self.play(FadeIn(item), run_time=0.5)
        self.wait(1.0)
        self._clear(title, summary, self.author_info)
