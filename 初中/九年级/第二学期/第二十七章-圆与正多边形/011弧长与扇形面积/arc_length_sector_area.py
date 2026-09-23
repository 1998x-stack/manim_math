"""九年级《弧长与扇形面积》：半径与圆心角驱动的九段教学动画。"""
from manim import *
import numpy as np
from arc_sector_math import sector_metrics, verify_example

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ArcLengthAndSectorArea(Scene):
    C_ARC = "#e74c3c"
    C_RADIUS = "#3498db"
    C_FORMULA = "#2ecc71"
    C_HIGHLIGHT = YELLOW

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.center = np.array([0.0, 0.95, 0.0])
        self.radius, self.degrees = 2.0, 60.0
        self.data = sector_metrics(self.radius, self.degrees)
        verify_example(self.radius, self.degrees,
                       expected_length=2 * PI / 3, expected_area=2 * PI / 3)
        self.theta = self.data['theta_rad']
        self.circle = Circle(radius=self.radius, color=WHITE, stroke_width=3).move_to(self.center)
        self.arc = Arc(radius=self.radius, start_angle=0, angle=self.theta,
                       arc_center=self.center, color=self.C_ARC, stroke_width=8)
        self.sector = Sector(radius=self.radius, start_angle=0, angle=self.theta,
                             arc_center=self.center, color=self.C_ARC,
                             fill_opacity=0.26, stroke_width=2)
        self.center_dot = Dot(self.center, radius=0.09, color=self.C_HIGHLIGHT)
        self.radii = VGroup(
            Line(self.center, self.center + self.radius * RIGHT,
                 color=self.C_RADIUS, stroke_width=3),
            Line(self.center, self.center + self.radius *
                 np.array([np.cos(self.theta), np.sin(self.theta), 0.0]),
                 color=self.C_RADIUS, stroke_width=3)
        )
        self.diagram = VGroup(self.circle, self.sector, self.arc, self.radii, self.center_dot)
        self.scene_1_opening()
        self.scene_2_central_angle()
        self.scene_3_arc_length_formula()
        self.scene_4_arc_length_example()
        self.scene_5_sector_definition()
        self.scene_6_sector_area_formula_1()
        self.scene_7_sector_area_formula_2()
        self.scene_8_comprehensive_example()
        self.scene_9_outro()

    def heading(self, words):
        return Text(words, font="sans-serif", font_size=35,
                    color=self.C_HIGHLIGHT).move_to(UP * 5.3)

    def arc_label(self, words, radius_offset=0.48):
        angle = self.theta / 2
        direction = np.array([np.cos(angle), np.sin(angle), 0.0])
        position = self.center + (self.radius + radius_offset) * direction
        return MathTex(words, font_size=31, color=self.C_ARC).move_to(position)

    def scene_1_opening(self):
        self.author = Text("上海初高中数学直通车 @emptyandcalm", font="sans-serif",
                           font_size=19, color=GRAY_B).move_to(UP * 6.8)
        header = self.heading("一块扇形披萨：弧多长、面积多大？")
        preview = self.sector.copy()
        self.play(FadeIn(self.author), Write(header))
        self.play(Create(preview))
        self.wait(0.7)
        self.play(FadeOut(header), FadeOut(preview))

    def scene_2_central_angle(self):
        header = self.heading("圆心角决定圆弧所占的份额")
        center_label = MathTex("O", font_size=28).next_to(self.center_dot, DL, buff=0.14)
        angle = Angle(self.radii[0], self.radii[1], radius=0.60, color=self.C_HIGHLIGHT)
        measured = MathTex(r"\theta=60^\circ", font_size=35,
                           color=self.C_HIGHLIGHT).move_to(DOWN * 4.2)
        self.play(Write(header), Create(self.circle), FadeIn(self.center_dot))
        self.play(Create(self.radii), Create(angle), FadeIn(center_label))
        self.play(Write(measured))
        self.wait(0.7)
        self.play(FadeOut(VGroup(header, angle, center_label, measured)))

    def scene_3_arc_length_formula(self):
        header = self.heading("弧长 = 圆周长 × 圆心角占比")
        arc_label = self.arc_label("l")
        proportion = MathTex(r"\frac{l}{2\pi R}=\frac{n}{360}",
                             font_size=36).move_to(DOWN * 4.1)
        formula = MathTex(r"l=\frac{n\pi R}{180}=R\theta", font_size=37,
                          color=self.C_FORMULA).move_to(DOWN * 5.1)
        self.play(Write(header), Create(self.arc))
        self.play(FadeIn(arc_label))
        self.play(Write(proportion))
        self.play(Write(formula))
        self.wait(1.1)
        self.play(FadeOut(VGroup(header, arc_label, proportion, formula)))

    def scene_4_arc_length_example(self):
        header = self.heading("例题：R=2，圆心角为 60°")
        arc_label = self.arc_label(r"l=\frac{2\pi}{3}")
        calculation = MathTex(r"l=\frac{60\pi\times2}{180}=\frac{2\pi}{3}",
                              font_size=36, color=self.C_FORMULA).move_to(DOWN * 4.2)
        decimal = Text(f"弧长约为 {self.data['arc_length']:.2f}（长度单位）",
                       font="sans-serif", font_size=26,
                       color=GRAY_A).move_to(DOWN * 5.25)
        self.play(Write(header), FadeIn(arc_label))
        self.play(Write(calculation), FadeIn(decimal))
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, arc_label, calculation, decimal)))

    def scene_5_sector_definition(self):
        header = self.heading("两条半径与其间圆弧围成扇形")
        radial = MathTex(r"R=2,\quad\theta=\frac{\pi}{3}",
                         font_size=35).move_to(DOWN * 4.25)
        note = Text("红色填充区域是扇形；红色曲线是对应的弧", font="sans-serif",
                    font_size=23, color=GRAY_A).move_to(DOWN * 5.15)
        self.play(Write(header), Create(self.sector))
        self.play(self.arc.animate.set_stroke(width=8), Write(radial), FadeIn(note))
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, radial, note)))

    def scene_6_sector_area_formula_1(self):
        header = self.heading("扇形面积 = 圆面积 × 圆心角占比")
        proportion = MathTex(r"\frac{S}{\pi R^2}=\frac{n}{360}",
                             font_size=35).move_to(DOWN * 4.05)
        formula = MathTex(r"S=\frac{n\pi R^2}{360}", font_size=39,
                          color=self.C_FORMULA).move_to(DOWN * 5.1)
        self.play(Write(header), Write(proportion))
        self.play(Write(formula))
        self.wait(1.0)
        self.play(FadeOut(VGroup(header, proportion, formula)))

    def scene_7_sector_area_formula_2(self):
        header = self.heading("另一种面积公式：利用弧长 l")
        first = MathTex(r"l=R\theta,\qquad S=\frac{R^2\theta}{2}",
                        font_size=34).move_to(DOWN * 4.10)
        second = MathTex(r"S=\frac{1}{2}Rl", font_size=42,
                         color=self.C_FORMULA).move_to(DOWN * 5.3)
        self.play(Write(header), Write(first))
        self.play(Write(second))
        self.wait(1.1)
        self.play(FadeOut(VGroup(header, first, second)))

    def scene_8_comprehensive_example(self):
        self.play(FadeOut(self.diagram))
        new_radius, new_angle = 3.0, 120.0
        metrics = sector_metrics(new_radius, new_angle)
        verify_example(new_radius, new_angle, expected_length=2 * PI, expected_area=3 * PI)
        center = np.array([0.0, 0.50, 0.0])
        header = self.heading("综合例题：R=3，圆心角 120°")
        shape = Sector(radius=new_radius, start_angle=0, angle=metrics['theta_rad'],
                       arc_center=center, color=self.C_ARC, fill_opacity=0.23)
        curve = Arc(radius=new_radius, start_angle=0, angle=metrics['theta_rad'],
                    arc_center=center, stroke_width=7, color=self.C_ARC)
        direction = np.array([np.cos(PI / 3), np.sin(PI / 3), 0.0])
        arc_caption = MathTex(r"l=2\pi", font_size=31, color=self.C_ARC).move_to(center + 3.55 * direction)
        length = MathTex(r"l=\frac{120\pi\times3}{180}=2\pi",
                         font_size=32).move_to(DOWN * 4.55)
        area = MathTex(r"S=\frac{120\pi\times3^2}{360}=3\pi",
                       font_size=32, color=self.C_FORMULA).move_to(DOWN * 5.45)
        self.play(Write(header), Create(shape), Create(curve))
        self.play(FadeIn(arc_caption), Write(length))
        self.play(Write(area))
        self.wait(1.1)
        self.play(FadeOut(VGroup(header, shape, curve, arc_caption, length, area)))

    def scene_9_outro(self):
        title = self.heading("弧长与扇形面积：记住角度单位")
        formulas = VGroup(
            MathTex(r"l=R\theta", font_size=40),
            MathTex(r"S=\frac12 Rl=\frac12 R^2\theta", font_size=37),
            Text("上式 θ 使用弧度；若给角度 n°，先转为 nπ/180",
                 font="sans-serif", font_size=23)
        ).arrange(DOWN, buff=0.55).move_to(ORIGIN)
        self.play(Write(title))
        self.play(FadeIn(formulas))
        self.wait(1.1)
        self.play(FadeOut(formulas), FadeOut(title), FadeOut(self.author))


# manim -ql arc_length_sector_area.py ArcLengthAndSectorArea
