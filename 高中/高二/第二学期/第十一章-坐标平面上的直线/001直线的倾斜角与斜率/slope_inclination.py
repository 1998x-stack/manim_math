"""高二下·直线的倾斜角与斜率（Manim 0.19.x，9:16）。

数学模型与画面坐标分离；保留原有七镜头及 Scene 入口。
旧 MP4 和音轨不在本次源码修复范围内。
"""

import math

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
C_POS = "#e74c3c"
C_NEG = "#3498db"
C_ZERO = "#2ecc71"
C_INF = "#9b59b6"
C_ANG = "#f39c12"
FONT = "PingFang SC"


def slope_between(a, b):
    """两点确定直线的斜率；垂直线返回 None，重合点不是直线。"""
    x1, y1 = a
    x2, y2 = b
    if x1 == x2 and y1 == y2:
        raise ValueError("重合点不能确定唯一的直线")
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)


def inclination_between(a, b):
    """直线（无方向）的倾斜角，范围为 [0, pi)。"""
    x1, y1 = a
    x2, y2 = b
    if x1 == x2 and y1 == y2:
        raise ValueError("重合点不能确定唯一的直线")
    return math.atan2(y2 - y1, x2 - x1) % math.pi


def clipped_origin_line(alpha, x_bounds=(-3.0, 3.0), y_bounds=(-2.0, 3.0)):
    """将过原点、倾斜角为 alpha 的无穷直线裁到数据坐标矩形内。"""
    if not (0 <= alpha < math.pi):
        raise ValueError("倾斜角须在 [0, pi) 内")
    if x_bounds[0] >= x_bounds[1] or y_bounds[0] >= y_bounds[1]:
        raise ValueError("坐标范围必须严格递增")
    dx, dy = math.cos(alpha), math.sin(alpha)
    t_min, t_max = -math.inf, math.inf
    for component, (low, high) in ((dx, x_bounds), (dy, y_bounds)):
        if abs(component) < 1e-12:
            if not low <= 0 <= high:
                raise ValueError("直线不经过当前坐标窗口")
            continue
        first, second = sorted((low / component, high / component))
        t_min, t_max = max(t_min, first), min(t_max, second)
    if not t_min < t_max:
        raise ValueError("直线与坐标窗口没有非退化交段")
    return (dx * t_min, dy * t_min), (dx * t_max, dy * t_max)


class SlopeAndInclinationAngle(Scene):
    """保留原课程七个分镜，所有图形取自同一组数学数据。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm", font=FONT,
            font_size=17, color=GRAY_B,
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.scene_1_opening()
        self.scene_2_inclination_angle()
        self.scene_3_k_tan_alpha()
        self.scene_4_two_point_formula()
        self.scene_5_four_cases()
        self.scene_6_summary()
        self.scene_7_outro()

    def cn(self, content, size=26, color=WHITE):
        return Text(content, font=FONT, font_size=size, color=color)

    def reset_stage(self):
        """只清理当前真实在屏对象，不重新构造 FadeOut 的目标。"""
        previous = [obj for obj in self.mobjects if obj is not self.author]
        if previous:
            self.play(*[FadeOut(obj) for obj in previous], run_time=0.45)

    def make_axes(self, small=False):
        x_range = (-2.5, 2.5, 1) if small else (-3, 3, 1)
        y_range = (-2, 2, 1) if small else (-2, 3, 1)
        axes = Axes(
            x_range=list(x_range), y_range=list(y_range),
            x_length=5.6 if small else 6.2,
            y_length=4.3 if small else 4.7,
            axis_config={"include_numbers": not small, "font_size": 19, "color": GRAY_A},
            tips=False,
        ).move_to(UP * (2.0 if small else 1.7))
        return axes

    def origin_line(self, axes, alpha, color, small=False):
        x_bounds = (-2.5, 2.5) if small else (-3.0, 3.0)
        y_bounds = (-2.0, 2.0) if small else (-2.0, 3.0)
        start, end = clipped_origin_line(alpha, x_bounds, y_bounds)
        return Line(axes.c2p(*start), axes.c2p(*end), color=color, stroke_width=5)

    def angle_arc(self, axes, alpha, color=C_ANG, radius=0.52):
        return Arc(
            radius=radius, start_angle=0, angle=alpha,
            arc_center=axes.c2p(0, 0), color=color, stroke_width=4,
        )

    def scene_1_opening(self):
        title = self.cn("直线有多斜？", 49).move_to(UP * 4.5)
        subtitle = self.cn("用倾斜角与斜率来描述", 29, YELLOW).move_to(UP * 3.6)
        axes = self.make_axes(small=True).move_to(DOWN * 0.2)
        examples = VGroup(
            self.origin_line(axes, math.pi / 4, C_POS, small=True),
            self.origin_line(axes, 3 * math.pi / 4, C_NEG, small=True),
            self.origin_line(axes, 0, C_ZERO, small=True),
        )
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        self.play(Create(axes), run_time=0.6)
        for line in examples:
            self.play(Create(line), run_time=0.35)
        self.wait(0.6)
        self.reset_stage()

    def scene_2_inclination_angle(self):
        title = self.cn("倾斜角 α 的定义", 35, GOLD).move_to(UP * 5.7)
        axes = self.make_axes()
        line = self.origin_line(axes, math.pi / 4, C_POS)
        arc = self.angle_arc(axes, math.pi / 4)
        label = MathTex(r"\alpha=45^{\circ}", color=C_ANG, font_size=30).next_to(
            axes.c2p(0, 0), UR, buff=0.35,
        )
        explanation = self.cn(
            "从 x 轴正方向逆时针转到直线上方射线", 23,
        ).move_to(DOWN * 3.35)
        interval = MathTex(
            r"0^{\circ}\leq\alpha<180^{\circ}", font_size=34, color=YELLOW,
        ).move_to(DOWN * 4.25)
        self.play(FadeIn(title), Create(axes), run_time=0.8)
        self.play(Create(line), Create(arc), FadeIn(label), run_time=0.8)
        self.play(FadeIn(explanation), Write(interval), run_time=0.75)
        self.wait(1.0)
        self.reset_stage()

    def scene_3_k_tan_alpha(self):
        title = self.cn("斜率与倾斜角", 35, GOLD).move_to(UP * 5.7)
        formula = MathTex(
            r"k=\tan\alpha\quad(\alpha\ne90^{\circ})",
            font_size=33,
        ).move_to(UP * 4.8)
        axes = self.make_axes(small=True)
        self.play(FadeIn(title), Write(formula), Create(axes), run_time=0.9)
        cases = (
            (math.pi / 4, C_POS, r"45^{\circ}", r"k=1"),
            (3 * math.pi / 4, C_NEG, r"135^{\circ}", r"k=-1"),
            (0.0, C_ZERO, r"0^{\circ}", r"k=0"),
            (math.pi / 2, C_INF, r"90^{\circ}", None),
        )
        current = None
        for alpha, color, alpha_text, k_text in cases:
            line = self.origin_line(axes, alpha, color, small=True)
            arc = self.angle_arc(axes, alpha, color, radius=0.42) if alpha else None
            math_label = MathTex(
                rf"\alpha={alpha_text}", font_size=32, color=color,
            )
            slope_label = (
                MathTex(k_text, font_size=32, color=color)
                if k_text is not None else self.cn("斜率不存在", 27, color)
            )
            details = VGroup(math_label, slope_label).arrange(DOWN, buff=0.2).move_to(
                DOWN * 3.6,
            )
            shown = VGroup(line, details, *([arc] if arc is not None else []))
            if current is not None:
                self.play(FadeOut(current), run_time=0.3)
            self.play(Create(line), FadeIn(details), run_time=0.6)
            if arc is not None:
                self.play(Create(arc), run_time=0.3)
            self.wait(0.4)
            current = shown
        self.reset_stage()

    def scene_4_two_point_formula(self):
        title = self.cn("两点斜率公式", 35, GOLD).move_to(UP * 5.8)
        axes = self.make_axes()
        a, b = (1.0, 1.0), (3.0, 3.0)
        c = (b[0], a[1])
        assert slope_between(a, b) == 1
        assert abs(inclination_between(a, b) - math.pi / 4) < 1e-12
        dot_a, dot_b = Dot(axes.c2p(*a), color=C_POS), Dot(axes.c2p(*b), color=C_POS)
        lbl_a = MathTex(r"A(1,1)", font_size=24, color=C_POS).next_to(dot_a, DL, buff=0.12)
        lbl_b = MathTex(r"B(3,3)", font_size=24, color=C_POS).next_to(dot_b, LEFT, buff=0.15)
        ab_line = self.origin_line(axes, inclination_between(a, b), C_POS)
        dx_line = DashedLine(axes.c2p(*a), axes.c2p(*c), color=YELLOW)
        dy_line = DashedLine(axes.c2p(*c), axes.c2p(*b), color=YELLOW)
        equation = MathTex(
            r"k=\frac{y_2-y_1}{x_2-x_1}=\frac{3-1}{3-1}=1",
            font_size=33,
        ).move_to(DOWN * 3.45)
        condition = MathTex(r"x_1\ne x_2", font_size=29, color=YELLOW).move_to(
            DOWN * 4.4,
        )
        self.play(FadeIn(title), Create(axes), run_time=0.75)
        self.play(Create(ab_line), FadeIn(dot_a), FadeIn(dot_b), run_time=0.75)
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), Create(dx_line), Create(dy_line), run_time=0.7)
        self.play(Write(equation), FadeIn(condition), run_time=1.2)
        self.wait(1.4)
        self.reset_stage()

    def scene_5_four_cases(self):
        title = self.cn("斜率的四种情况", 35, GOLD).move_to(UP * 5.8)
        axes = self.make_axes(small=True)
        cases = (
            (math.pi / 4, C_POS, "k > 0：锐角"),
            (3 * math.pi / 4, C_NEG, "k < 0：钝角"),
            (0.0, C_ZERO, "k = 0：水平线"),
            (math.pi / 2, C_INF, "α = 90°：斜率不存在"),
        )
        labels = VGroup(*[
            self.cn(text, 23, color) for _, color, text in cases
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.26).move_to(DOWN * 3.6)
        self.play(FadeIn(title), Create(axes), run_time=0.7)
        for (angle, color, _), label in zip(cases, labels):
            line = self.origin_line(axes, angle, color, small=True)
            self.play(Create(line), FadeIn(label), run_time=0.5)
        self.wait(1.4)
        self.reset_stage()

    def scene_6_summary(self):
        title = self.cn("核心公式总结", 35, GOLD).move_to(UP * 5.6)
        formulas = VGroup(
            MathTex(r"0^{\circ}\leq\alpha<180^{\circ}", font_size=34),
            MathTex(r"k=\tan\alpha\quad(\alpha\ne90^{\circ})", font_size=32),
            MathTex(r"k=\frac{y_2-y_1}{x_2-x_1}\quad(x_1\ne x_2)", font_size=31),
            self.cn("水平线：k = 0；垂直线：斜率不存在", 23, YELLOW),
        ).arrange(DOWN, buff=0.68).move_to(UP * 0.9)
        self.play(FadeIn(title), run_time=0.4)
        for item in formulas:
            self.play(FadeIn(item), run_time=0.55)
        self.wait(1.7)
        self.reset_stage()

    def scene_7_outro(self):
        name = self.cn("上海初高中数学直通车", 39).move_to(UP * 1.8)
        handle = self.cn("@emptyandcalm", 31, GRAY_B).move_to(UP * 0.65)
        caption = self.cn("关注我，获得更多数学技巧！", 29, YELLOW).move_to(DOWN * 0.5)
        self.play(FadeIn(name), FadeIn(handle), FadeIn(caption), run_time=0.8)
        self.wait(1.4)
        self.play(FadeOut(name), FadeOut(handle), FadeOut(caption), FadeOut(self.author))
