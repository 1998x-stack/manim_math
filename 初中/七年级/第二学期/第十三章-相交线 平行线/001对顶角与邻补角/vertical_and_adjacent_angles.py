"""七年级下·对顶角与邻补角。保留 VerticalAndAdjacentAngles Scene 入口。

同一组射线角度驱动弧线、标签和角度数值，避免短角错绘成优角。
"""
from math import atan2, cos, degrees, radians, sin
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
COLORS = (ORANGE, BLUE_C, ORANGE, BLUE_C)


def signed_short_sweep(start_angle, end_angle):
    """从 start 到 end 的有向短角（弧度）；本课射线不共线。"""
    return (end_angle - start_angle + PI) % TAU - PI


class VerticalAndAdjacentAngles(Scene):
    def fit(self, mob, width=7.5):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, text):
        title = self.fit(Text(text, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)
        return title

    def note(self, text, y=-3.5, color=WHITE):
        mob = self.fit(Text(text, font_size=26, color=color)).move_to(UP * y)
        self.play(FadeIn(mob), run_time=0.5)
        return mob

    def formula(self, text, y=-2.1, color=YELLOW):
        mob = self.fit(MathTex(text, font_size=37, color=color)).move_to(UP * y)
        self.play(Write(mob), run_time=0.7)
        return mob

    def clear_stage(self):
        visible = [mob for mob in self.mobjects if mob is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.45)

    def setup_geometry(self):
        self.O = np.array([0.0, 1.1, 0.0])
        # 射线按角1、角2、角3、角4顺时针顺序排列。
        self.directions = tuple(radians(d) for d in (30, -40, 210, 140))
        self.sweeps = tuple(
            signed_short_sweep(self.directions[i], self.directions[(i + 1) % 4])
            for i in range(4)
        )
        self.angle_values = tuple(abs(degrees(s)) for s in self.sweeps)
        self.verify_geometry()

    def verify_geometry(self):
        a, b, c, d = self.angle_values
        assert all(0 < value < 180 for value in self.angle_values)
        assert abs(a - c) < 1e-9 and abs(b - d) < 1e-9
        assert abs(a + b - 180) < 1e-9
        assert all(sweep < 0 for sweep in self.sweeps)

    def draw_cross(self):
        for index in (0, 1):
            angle = self.directions[index]
            unit = np.array([cos(angle), sin(angle), 0.0])
            self.play(Create(Line(self.O - unit * 3.1, self.O + unit * 3.1,
                                  color=BLUE_C if index == 0 else RED_C,
                                  stroke_width=4)), run_time=0.35)
        self.play(FadeIn(Dot(self.O, radius=0.075, color=WHITE)), run_time=0.2)

    def draw_sector(self, index):
        start = self.directions[index]
        sweep = self.sweeps[index]
        # 负 sweep 表示顺时针短弧；标签使用同一短弧中间方向。
        arc = Arc(radius=0.63, start_angle=start, angle=sweep,
                  color=COLORS[index], stroke_width=5).move_arc_center_to(self.O)
        midpoint = start + sweep / 2
        location = self.O + 1.12 * np.array([cos(midpoint), sin(midpoint), 0])
        label = MathTex(r"\angle " + str(index + 1), font_size=27,
                        color=COLORS[index]).move_to(location)
        self.play(Create(arc), FadeIn(label), run_time=0.45)
        return VGroup(arc, label)

    def construct(self):
        self.camera.background_color = BG
        self.setup_geometry()
        self.author = self.fit(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.show_opening()
        self.show_intersecting_lines()
        self.show_vertical_angles()
        self.show_adjacent_angles()
        self.show_numerical_example()
        self.show_summary()
        self.show_outro()

    def show_opening(self):
        self.heading("相交的两条直线，会形成什么角？")
        self.draw_cross()
        self.note("观察两条直线形成的四个小角", -2.6, YELLOW)
        self.wait(0.8)
        self.clear_stage()

    def show_intersecting_lines(self):
        self.heading("从同一个顶点出发的四个角")
        self.draw_cross()
        for index in range(4):
            self.draw_sector(index)
        self.note("角弧和数字标签都对应同一片扇形", -2.7)
        self.wait(0.9)
        self.clear_stage()

    def show_vertical_angles(self):
        self.heading("对顶角：两边互为反向延长线")
        self.draw_cross()
        self.draw_sector(0)
        self.draw_sector(2)
        self.formula(r"\angle1=\angle3=70^{\circ}", -1.65)
        self.note("对顶角相等：位置相对、度数相同", -3.0)
        self.wait(1.0)
        self.clear_stage()

    def show_adjacent_angles(self):
        self.heading("邻补角：共边，另两边成一直线")
        self.draw_cross()
        self.draw_sector(0)
        self.draw_sector(1)
        self.formula(r"\angle1+\angle2=180^{\circ}", -1.5)
        self.formula(r"70^{\circ}+110^{\circ}=180^{\circ}", -2.7)
        self.wait(1.0)
        self.clear_stage()

    def show_numerical_example(self):
        self.heading("已知一个角，求其余三个角")
        self.draw_cross()
        for index in range(4):
            self.draw_sector(index)
        self.formula(r"\angle1=70^{\circ}\ \Longrightarrow\ \angle3=70^{\circ}", -1.4)
        self.formula(r"\angle2=\angle4=110^{\circ}", -2.8)
        self.wait(1.0)
        self.clear_stage()

    def show_summary(self):
        self.heading("两个重要的角度关系")
        self.draw_cross()
        for index in range(4):
            self.draw_sector(index)
        self.formula(r"\angle1=\angle3,\quad\angle2=\angle4", -1.5)
        self.formula(r"\angle1+\angle2=180^{\circ}", -2.8)
        self.wait(1.1)
        self.clear_stage()

    def show_outro(self):
        self.heading("邻补角互补，对顶角相等")
        self.note("判断关系时先确认顶点、边和角弧方向", 1.2, YELLOW)
        self.wait(1.8)
