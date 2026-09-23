"""三线八角：八个角弧、数字和配对从两个真实交点与同一射线序列产生。"""
from math import atan2, cos, degrees, pi, sin
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = '#1a1a2e'


def intersect_horizontal(start, end, y):
    """求非水平直线与水平线 y=常数 的交点（可以位于画出的线段外）。"""
    dy = end[1] - start[1]
    if abs(dy) < 1e-12:
        raise ValueError('transversal is parallel to horizontal lines')
    t = (y - start[1]) / dy
    return start[0] + t * (end[0] - start[0]), y


def angle_sector(index, theta):
    """返回本课第 index 个角的起始方向、逆时针短弧和弧中线。

    每个交点的四条射线按 right、up-right、left、down-left 顺序逆时针排列。
    """
    assert 0 <= index < 8 and 0 < theta < pi
    rays = (0.0, theta, pi, pi + theta, 2 * pi)
    local = index % 4
    start, end = rays[local], rays[local + 1]
    return start, end - start, (start + end) / 2


class ThreeLinesEightAngles(Scene):
    def fit(self, obj, max_width=7.5):
        if obj.width > max_width:
            obj.scale_to_fit_width(max_width)
        return obj

    def title(self, text):
        obj = self.fit(Text(text, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(obj), run_time=0.55)
        return obj

    def note(self, text, y, color=WHITE, size=25):
        obj = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(obj), run_time=0.4)
        return obj

    def formula(self, tex, y, color=YELLOW, size=34):
        obj = self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(obj), run_time=0.6)
        return obj

    def setup_geometry(self):
        self.top_y, self.bottom_y = 2.0, -0.8
        self.t_start = (-2.0, -3.6)
        self.t_end = (2.2, 4.8)
        self.P = np.array([*intersect_horizontal(self.t_start, self.t_end, self.top_y), 0.0])
        self.Q = np.array([*intersect_horizontal(self.t_start, self.t_end, self.bottom_y), 0.0])
        direction = np.array([self.t_end[0] - self.t_start[0],
                              self.t_end[1] - self.t_start[1]])
        self.theta = atan2(direction[1], direction[0])
        assert 0 < self.theta < pi / 2
        assert self.P[1] > self.Q[1] and self.P[0] > self.Q[0]
        assert abs((self.P[0] - self.Q[0]) / (self.P[1] - self.Q[1]) - .5) < 1e-9
        self.sectors = tuple(angle_sector(i, self.theta) for i in range(8))
        self.angle_values = tuple(degrees(spec[1]) for spec in self.sectors)
        for a, b in ((0,4), (1,5), (2,6), (3,7), (2,4), (3,5)):
            assert abs(self.angle_values[a] - self.angle_values[b]) < 1e-9
        for a, b in ((2,5), (3,4)):
            assert abs(self.angle_values[a] + self.angle_values[b] - 180) < 1e-9

    def draw_lines(self):
        top = Line([-3.5, self.top_y, 0], [3.5, self.top_y, 0], color=BLUE_C, stroke_width=4)
        bottom = Line([-3.5, self.bottom_y, 0], [3.5, self.bottom_y, 0], color=RED_C, stroke_width=4)
        transversal = Line([*self.t_start, 0], [*self.t_end, 0], color=GREEN_C, stroke_width=4)
        self.play(Create(top), Create(bottom), Create(transversal), run_time=0.7)

    def draw_angles(self, highlighted=(), color=YELLOW):
        for i, (start, sweep, midpoint) in enumerate(self.sectors):
            center = self.P if i < 4 else self.Q
            ink = color if i + 1 in highlighted else GRAY_B
            arc = Arc(radius=0.42, start_angle=start, angle=sweep,
                      color=ink, stroke_width=4).move_arc_center_to(center)
            label_pos = center + np.array([.84 * cos(midpoint), .84 * sin(midpoint), 0])
            label = MathTex(r'\angle '+str(i + 1), font_size=22, color=ink).move_to(label_pos)
            self.play(Create(arc), FadeIn(label), run_time=0.25)

    def clear_stage(self):
        visible = [obj for obj in self.mobjects if obj is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.4)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = self.fit(Text('上海初高中数学直通车 @emptyandcalm',
                                    font_size=18, color=GRAY_B)).move_to(UP * 6.75)
        self.add(self.author)
        self.show_opening()
        self.show_construction()
        self.show_corresponding_angles()
        self.show_alternate_angles()
        self.show_consecutive_angles()
        self.show_summary()
        self.show_outro()

    def show_opening(self):
        self.title('两条直线被一条截线所截')
        self.draw_lines()
        self.note('每个交点都有四个角，两个交点共八个', -3.2, YELLOW)
        self.wait(0.8)
        self.clear_stage()

    def show_construction(self):
        self.title('八个角：上交点 1–4，下交点 5–8')
        self.draw_lines()
        self.draw_angles()
        self.note('每个编号与实际短角弧和角平分线方向一致', -3.1)
        self.wait(0.7)
        self.clear_stage()

    def show_corresponding_angles(self):
        self.title('同位角：截线同侧、位置相同')
        self.draw_lines()
        self.draw_angles((1, 5, 2, 6), ORANGE)
        self.formula(r'\angle1,\angle5\qquad\angle2,\angle6', -2.8, ORANGE, 30)
        self.note('还有：角 3 与 7、角 4 与 8', -3.85)
        self.note('本例两条被截线平行，故对应的同位角相等', -5.0, ORANGE, 23)
        self.wait(0.9)
        self.clear_stage()

    def show_alternate_angles(self):
        self.title('内错角：两线之间、截线两侧')
        self.draw_lines()
        self.draw_angles((3, 5, 4, 6), PURPLE_C)
        self.formula(r'\angle3,\angle5\qquad\angle4,\angle6', -2.8, PURPLE_C, 30)
        self.note('在本例的平行线条件下，两对内错角分别相等', -4.1, PURPLE_C, 23)
        self.wait(0.9)
        self.clear_stage()

    def show_consecutive_angles(self):
        self.title('同旁内角：两线之间、截线同侧')
        self.draw_lines()
        self.draw_angles((3, 6, 4, 5), GREEN_C)
        self.formula(r'\angle3+\angle6=180^{\circ}', -2.8, GREEN_C, 34)
        self.formula(r'\angle4+\angle5=180^{\circ}', -4.0, GREEN_C, 34)
        self.note('互补结论成立的前提：被截两条直线平行', -5.15, GREEN_C, 23)
        self.wait(0.9)
        self.clear_stage()

    def show_summary(self):
        self.title('按位置识别，再判断能否算角度')
        self.draw_lines()
        self.draw_angles()
        self.note('同位角 4 对，内错角 2 对，同旁内角 2 对', -3.0)
        self.note('只有在有平行条件时，才能直接套用相等或互补', -4.2, YELLOW)
        self.wait(1.0)
        self.clear_stage()

    def show_outro(self):
        self.title('位置关系不是角度大小关系')
        self.note('先找到哪两条线被截、哪条是截线', 1.8)
        self.note('再核对角位于截线哪侧、两线内还是两线外', 0.2, YELLOW)
        self.wait(1.8)
