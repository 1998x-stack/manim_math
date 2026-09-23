"""平行线的三条判定：先展示不平行反例，再在正确的两交点角对上判定。"""
from math import atan2, cos, degrees, pi, radians, sin
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = '#1a1a2e'
PARALLEL_TILT = 0.0
COUNTEREXAMPLE_TILT = radians(15)


def sector_spec(index, transversal_angle, lower_tilt):
    """返回第 1..8 角所对应的真实逆时针弧：起点、张角、中线。

    顶点上/下依次编号 1..4/5..8，射线从被截线右向依次逆时针
    经过截线向上、被截线左向、截线向下方向。本课限制下线倾角
    0<=lower_tilt<transversal_angle<π/2，以免改变编号拓扑。
    """
    assert 1 <= index <= 8
    assert 0 <= lower_tilt < transversal_angle < pi / 2
    direction = 0.0 if index <= 4 else lower_tilt
    rays = (direction, transversal_angle, direction + pi,
            transversal_angle + pi, direction + 2 * pi)
    local = (index - 1) % 4
    start, end = rays[local], rays[local + 1]
    return start, end - start, (start + end) / 2


class ParallelLineDetermination(Scene):
    def fit(self, obj, max_width=7.5):
        if obj.width > max_width:
            obj.scale_to_fit_width(max_width)
        return obj

    def heading(self, text):
        obj = self.fit(Text(text, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(obj), run_time=0.55)
        return obj

    def note(self, text, y, color=WHITE, size=26):
        obj = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(obj), run_time=0.4)
        return obj

    def formula(self, tex, y, color=YELLOW, size=34):
        obj = self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(obj), run_time=0.6)
        return obj

    def setup_geometry(self):
        self.P = np.array([0.6, 1.2, 0.0])
        self.Q = np.array([-0.75, -1.5, 0.0])
        td = self.P - self.Q
        self.tdir = td / np.linalg.norm(td)
        self.theta = atan2(self.tdir[1], self.tdir[0])
        assert 0 < COUNTEREXAMPLE_TILT < self.theta < pi / 2
        assert abs((self.P[0] - self.Q[0]) / (self.P[1] - self.Q[1]) - 0.5) < 1e-9
        self.check_model()

    def angle(self, index, lower_tilt):
        return degrees(sector_spec(index, self.theta, lower_tilt)[1])

    def check_model(self):
        for index in range(1, 9):
            start, sweep, midpoint = sector_spec(index, self.theta, PARALLEL_TILT)
            assert 0 < sweep < pi and start < midpoint < start + sweep
        # 非平行反例：在 P、Q 处相应的同位角不相等。
        assert self.angle(1, COUNTEREXAMPLE_TILT) > self.angle(5, COUNTEREXAMPLE_TILT)
        # 同一交点相邻两角始终互补，不能据此判定平行。
        for tilt in (PARALLEL_TILT, COUNTEREXAMPLE_TILT):
            assert abs(self.angle(5, tilt) + self.angle(6, tilt) - 180) < 1e-9
        # 本例线 m 变为水平线后，三条判定条件都满足。
        assert abs(self.angle(1, 0) - self.angle(5, 0)) < 1e-9
        assert abs(self.angle(3, 0) - self.angle(5, 0)) < 1e-9
        assert abs(self.angle(4, 0) + self.angle(5, 0) - 180) < 1e-9

    def draw_model(self, lower_tilt, selected=(), color=YELLOW):
        upper = Line([-3.1, self.P[1], 0], [3.5, self.P[1], 0],
                     color=BLUE_C, stroke_width=4)
        direction = np.array([cos(lower_tilt), sin(lower_tilt), 0])
        lower = Line(self.Q - direction * 3.1, self.Q + direction * 3.1,
                     color=GREEN_C, stroke_width=4)
        crossing = Line(self.Q - self.tdir * 1.2, self.P + self.tdir * 1.1,
                        color=RED_C, stroke_width=4)
        self.play(Create(upper), Create(lower), Create(crossing), run_time=0.65)
        for index in selected:
            anchor = self.P if index <= 4 else self.Q
            start, sweep, middle = sector_spec(index, self.theta, lower_tilt)
            arc = Arc(radius=0.45, start_angle=start, angle=sweep,
                      color=color, stroke_width=5).move_arc_center_to(anchor)
            label = MathTex(r'\angle '+str(index), font_size=26, color=color)
            label.move_to(anchor + .90 * np.array([cos(middle), sin(middle), 0]))
            self.play(Create(arc), FadeIn(label), run_time=0.35)

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
        self.scene_1_opening()
        self.scene_2_diagram()
        self.scene_3_corresponding()
        self.scene_4_alternate()
        self.scene_5_cointerior()
        self.scene_6_summary()
        self.scene_7_outro()

    def scene_1_opening(self):
        self.heading('如何从角的关系判定两直线平行？')
        self.draw_model(COUNTEREXAMPLE_TILT)
        self.note('此时下方直线略微倾斜，尚不能判断为平行', -3.0)
        self.wait(0.7)
        self.clear_stage()

    def scene_2_diagram(self):
        self.heading('反例：只看一个交点的平角不够')
        self.draw_model(COUNTEREXAMPLE_TILT, (5, 6), ORANGE)
        self.formula(r'\angle5+\angle6=180^{\circ}', -2.9, ORANGE)
        self.note('这是邻补角，直线并未平行', -4.1, ORANGE)
        self.wait(0.9)
        self.clear_stage()

    def scene_3_corresponding(self):
        self.heading('方法一：同位角相等')
        self.draw_model(COUNTEREXAMPLE_TILT, (1, 5), ORANGE)
        before = (rf'\angle1\approx{self.angle(1,COUNTEREXAMPLE_TILT):.1f}^{{\circ}},\quad'
                  rf'\angle5\approx{self.angle(5,COUNTEREXAMPLE_TILT):.1f}^{{\circ}}')
        self.formula(before, -2.7, ORANGE, 33)
        self.note('两角不相等，下方直线尚未平行', -4.0)
        self.wait(0.4)
        self.clear_stage()
        self.heading('让同位角相等，再判定平行')
        self.draw_model(PARALLEL_TILT, (1, 5), GREEN_C)
        self.formula(r'\angle1=\angle5\ \Longrightarrow\ l\parallel m', -2.8, GREEN_C, 32)
        self.note('角来自两个交点，分别处于相同位置', -4.1)
        self.wait(0.9)
        self.clear_stage()

    def scene_4_alternate(self):
        self.heading('方法二：内错角相等')
        self.draw_model(PARALLEL_TILT, (3, 5), PURPLE_C)
        self.formula(r'\angle3=\angle5\ \Longrightarrow\ l\parallel m', -2.9, PURPLE_C, 32)
        self.note('两线之间，截线两侧；是不同交点的角', -4.2)
        self.wait(0.9)
        self.clear_stage()

    def scene_5_cointerior(self):
        self.heading('方法三：同旁内角互补')
        self.draw_model(PARALLEL_TILT, (4, 5), YELLOW)
        self.formula(r'\angle4+\angle5=180^{\circ}', -2.7)
        self.formula(r'\Longrightarrow\ l\parallel m', -4.0)
        self.note('两线之间、截线同侧，且来自不同交点', -5.0, YELLOW, 23)
        self.wait(0.9)
        self.clear_stage()

    def scene_6_summary(self):
        self.heading('判定平行：必须选对角对')
        self.formula(r'\angle1=\angle5\ \Longrightarrow\ l\parallel m', 3.9, ORANGE, 31)
        self.note('同位角相等', 3.0, ORANGE, 23)
        self.formula(r'\angle3=\angle5\ \Longrightarrow\ l\parallel m', 1.35, PURPLE_C, 31)
        self.note('内错角相等', 0.4, PURPLE_C, 23)
        self.formula(r'\angle4+\angle5=180^{\circ}\ \Longrightarrow\ l\parallel m', -1.5, YELLOW, 29)
        self.note('同旁内角互补；不可用同一交点的邻补角', -3.0, YELLOW, 23)
        self.wait(1.2)
        self.clear_stage()

    def scene_7_outro(self):
        self.heading('先辨位置，再核对度数')
        self.note('同位、内错、同旁内角都要核对两个交点', 1.7)
        self.note('把邻补角误作平行判据，是常见陷阱', 0.2, YELLOW)
        self.wait(1.8)
