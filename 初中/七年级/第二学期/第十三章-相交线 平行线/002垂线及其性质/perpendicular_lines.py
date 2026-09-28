"""七年级下·垂线及其性质：以实际投影点驱动画面及距离计算。"""
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = '#1a1a2e'
BLUE_LINE = BLUE_C
RED_PERP = RED_C
GOLD_VALUE = YELLOW


def foot_of_perpendicular(point, line_start, line_end):
    """在二维欧氏平面上，求点到由两个不同点确定的无限直线的垂足。"""
    vx = line_end[0] - line_start[0]
    vy = line_end[1] - line_start[1]
    norm_sq = vx * vx + vy * vy
    if norm_sq <= 1e-12:
        raise ValueError('line requires two distinct points')
    t = ((point[0] - line_start[0]) * vx
         + (point[1] - line_start[1]) * vy) / norm_sq
    return (line_start[0] + t * vx, line_start[1] + t * vy)


class PerpendicularLines(Scene):
    def fit(self, obj, max_width=7.5):
        if obj.width > max_width:
            obj.scale_to_fit_width(max_width)
        return obj

    def title(self, text):
        obj = self.fit(Text(text, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(obj), run_time=0.6)
        return obj

    def note(self, text, y, color=WHITE, size=26):
        obj = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(obj), run_time=0.45)
        return obj

    def formula(self, tex, y, color=GOLD_VALUE, size=36):
        obj = self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(obj), run_time=0.65)
        return obj

    def setup_geometry(self):
        self.line_start = np.array([-3.5, 0.0, 0.0])
        self.line_end = np.array([3.5, 0.0, 0.0])
        self.P = np.array([-1.5, 2.5, 0.0])
        self.Q = np.array([1.8, 2.8, 0.0])
        self.H = np.array([*foot_of_perpendicular(self.P, self.line_start,
                                                  self.line_end), 0.0])
        self.K = np.array([*foot_of_perpendicular(self.Q, self.line_start,
                                                  self.line_end), 0.0])
        self.A = np.array([0.8, 0.0, 0.0])
        self.B = np.array([-3.2, 0.0, 0.0])
        self.PH = float(np.linalg.norm(self.P - self.H))
        self.PA = float(np.linalg.norm(self.P - self.A))
        self.PB = float(np.linalg.norm(self.P - self.B))
        self.QK = float(np.linalg.norm(self.Q - self.K))
        self.verify_geometry()

    def verify_geometry(self):
        direction = self.line_end - self.line_start
        assert np.linalg.norm(direction) > 1e-8
        assert abs(np.dot((self.P - self.H)[:2], direction[:2])) < 1e-8
        assert abs(np.dot((self.Q - self.K)[:2], direction[:2])) < 1e-8
        assert abs(np.cross(direction[:2], (self.H - self.line_start)[:2])) < 1e-8
        assert abs(np.cross(direction[:2], (self.K - self.line_start)[:2])) < 1e-8
        assert self.PH < self.PA and self.PH < self.PB
        assert np.isclose(self.PH, 2.5) and np.isclose(self.QK, 2.8)

    def right_angle_mark(self, foot, point, scale=0.22):
        direction = self.line_end - self.line_start
        u = direction / np.linalg.norm(direction)
        v = (point - foot) / np.linalg.norm(point - foot)
        assert abs(float(np.dot(u, v))) < 1e-8
        return Polygon(foot, foot + u * scale, foot + (u + v) * scale,
                       foot + v * scale, color=GREEN_C, stroke_width=3)

    def draw_geometry(self):
        baseline = Line(self.line_start, self.line_end, color=BLUE_LINE, stroke_width=4)
        perpendicular = Line(self.P, self.H, color=RED_PERP, stroke_width=4)
        p_dot = Dot(self.P, color=RED_PERP)
        h_dot = Dot(self.H, color=GOLD_VALUE)
        p_label = MathTex('P', font_size=30).next_to(p_dot, UP, buff=0.1)
        h_label = MathTex('H', font_size=30).next_to(h_dot, DOWN, buff=0.15)
        marker = self.right_angle_mark(self.H, self.P)
        self.play(Create(baseline), FadeIn(p_dot), FadeIn(p_label), run_time=0.65)
        self.play(Create(perpendicular), FadeIn(h_dot), FadeIn(h_label),
                  Create(marker), run_time=0.65)

    def clear_stage(self):
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = self.fit(
            Text('上海初高中数学直通车 @emptyandcalm', font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.show_opening()
        self.show_definition()
        self.show_uniqueness()
        self.show_shortest_distance()
        self.show_application()
        self.show_summary()
        self.show_outro()

    def show_opening(self):
        self.title('从点到直线，哪条线段最短？')
        self.draw_geometry()
        self.note('先观察与直线成直角的线段 PH', -1.7, GOLD_VALUE)
        self.wait(0.8)
        self.clear_stage()

    def show_definition(self):
        self.title('两条直线垂直：夹角为 90°')
        self.draw_geometry()
        self.formula(r'PH\perp l\quad 90^{\circ}', -1.6, GOLD_VALUE, 31)
        self.note('H 是点 P 到直线 l 的垂足', -3.0)
        self.wait(0.9)
        self.clear_stage()

    def show_uniqueness(self):
        self.title('过一点，有且只有一条垂线')
        self.draw_geometry()
        for target in (self.A, self.B):
            candidate = DashedLine(self.P, target, color=GRAY_B, dash_length=0.11)
            self.play(Create(candidate), run_time=0.4)
        self.note('虚线虽然也连到直线 l，但没有形成直角', -1.9)
        self.note('通过点 P 的垂线是唯一的', -3.0, GOLD_VALUE)
        self.wait(1.0)
        self.clear_stage()

    def show_shortest_distance(self):
        self.title('垂线段最短：比较三条实际线段')
        self.draw_geometry()
        for name, target, color in (('A', self.A, BLUE_C), ('B', self.B, ORANGE)):
            line = Line(self.P, target, color=color, stroke_width=3)
            dot = Dot(target, color=color)
            label = MathTex(name, font_size=29, color=color).next_to(dot, DOWN, buff=0.12)
            self.play(Create(line), FadeIn(dot), FadeIn(label), run_time=0.5)
        comparison = (rf'PH={self.PH:.2f}<PB\approx{self.PB:.2f}'
                      rf'<PA\approx{self.PA:.2f}')
        self.formula(comparison, -1.9, GOLD_VALUE, 34)
        self.note('对直线上的其他点，连线长度不会短于 PH', -3.1, GOLD_VALUE)
        self.wait(1.0)
        self.clear_stage()

    def show_application(self):
        self.title('再看另一个点：距离由垂线段给出')
        baseline = Line(self.line_start, self.line_end, color=BLUE_LINE, stroke_width=4)
        vertical = Line(self.Q, self.K, color=RED_PERP, stroke_width=4)
        q_dot, k_dot = Dot(self.Q, color=RED_PERP), Dot(self.K, color=GOLD_VALUE)
        marker = self.right_angle_mark(self.K, self.Q)
        self.play(Create(baseline), FadeIn(q_dot), FadeIn(k_dot), run_time=0.7)
        self.play(Create(vertical), Create(marker), run_time=0.6)
        self.formula(rf'QK=d(Q,l)={self.QK:.1f}', -1.6, GOLD_VALUE)
        self.note('求点到直线的距离：先作垂线，再量垂线段', -3.0)
        self.wait(0.9)
        self.clear_stage()

    def show_summary(self):
        self.title('垂线的两个关键性质')
        self.draw_geometry()
        self.note('唯一性：过一点，有且只有一条垂线', -1.5, GOLD_VALUE)
        self.note('最短性：垂足对应的线段长度最短', -2.7)
        self.wait(1.0)
        self.clear_stage()

    def show_outro(self):
        self.title('记住：垂线段的长度就是距离')
        self.formula(r'PH\perp l\quad\Longrightarrow\quad d(P,l)=PH', 2.1, GOLD_VALUE, 32)
        self.note('前提：H 是 P 在直线 l 上的垂足', 0.5)
        self.wait(1.8)
