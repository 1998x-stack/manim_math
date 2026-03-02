"""
球 (Sphere) - 高三数学教学动画
3D TikTok 竖屏教学视频

manim -qh sphere_lesson.py SphereLesson

知识点: 球的定义、截面、表面积、体积、外接球与内切球
目标: 高三学生
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── Global Config ──────────────────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

FONT     = "Noto Sans CJK SC"
BG_COLOR = "#0d0d1a"

C_SPHERE  = "#4fc3f7"   # light blue sphere
C_GOLD    = "#ffd54f"   # gold highlights
C_PINK    = "#f48fb1"   # cross-section pink
C_GREEN   = "#a5d6a7"   # circumscribed green
C_ORANGE  = "#ffb74d"   # inscribed orange
C_AXIS    = "#90caf9"   # axis color
C_RADIUS  = "#ffe082"   # radius lines


# ══════════════════════════════════════════════════════════════════════════════
class SphereLesson(ThreeDScene):

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_params()

        self.scene_01_opening()
        self.scene_02_definition()
        self.scene_03_cross_section()
        self.scene_04_great_circle()
        self.scene_05_surface_area()
        self.scene_06_volume()
        self.scene_07_circumscribed()
        self.scene_08_outro()

    # ── Parameters ─────────────────────────────────────────────────────────────
    def setup_params(self):
        self.R = 1.8          # sphere radius in scene units
        self.sphere_center = np.array([0, 0.5, 0])   # 3-D center

        # Cross-section: distance d from center
        self.d = 0.9
        self.r_cross = np.sqrt(self.R**2 - self.d**2)

        # Verification
        assert abs(self.r_cross**2 - (self.R**2 - self.d**2)) < 1e-10, "Cross-section error"
        print(f"✓ R={self.R}, d={self.d}, r={self.r_cross:.4f}")

    # ── Helper: persistent author strip ────────────────────────────────────────
    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)

    # ── Helper: title card ─────────────────────────────────────────────────────
    def make_title(self, zh, formula_str=None, y=5.8):
        title = Text(zh, font=FONT, font_size=36, color=WHITE).move_to(UP * y)
        if formula_str:
            fml = MathTex(formula_str, font_size=30, color=C_GOLD).next_to(title, DOWN, buff=0.2)
            return VGroup(title, fml)
        return title

    # ── Helper: bottom explanation ─────────────────────────────────────────────
    def bottom_text(self, *lines, start_y=-4.2, color=GRAY_A):
        texts = []
        for i, line in enumerate(lines):
            t = Text(line, font=FONT, font_size=22, color=color).move_to(
                UP * (start_y - i * 0.6)
            )
            texts.append(t)
        return VGroup(*texts)

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 1 – Opening Hook
    # ══════════════════════════════════════════════════════════════════════════
    def scene_01_opening(self):
        self.set_camera_orientation(phi=0, theta=0)

        author = self.make_author()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # Big hook question
        q1 = Text("你知道球的", font=FONT, font_size=44, color=WHITE)
        q2 = Text("表面积和体积", font=FONT, font_size=44, color=C_GOLD)
        q3 = Text("怎么算吗？", font=FONT, font_size=44, color=WHITE)
        hook = VGroup(q1, q2, q3).arrange(DOWN, buff=0.15).move_to(UP * 5.0)

        self.play(Write(q1), run_time=0.5)
        self.play(Write(q2), run_time=0.5)
        self.play(Write(q3), run_time=0.5)
        self.wait(0.5)

        # Mini sphere preview – 2D circle placeholder before 3D kicks in
        preview_circle = Circle(radius=1.4, color=C_SPHERE, stroke_width=3,
                                fill_color=C_SPHERE, fill_opacity=0.15
                                ).move_to(UP * 1.5)
        preview_label = Text("球", font=FONT, font_size=72, color=C_SPHERE
                             ).move_to(UP * 1.5)
        self.play(Create(preview_circle), run_time=0.8)
        self.play(Write(preview_label), run_time=0.4)

        formulas_preview = VGroup(
            MathTex(r"S = 4\pi R^2", font_size=32, color=C_PINK),
            MathTex(r"V = \dfrac{4}{3}\pi R^3", font_size=32, color=C_GREEN),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 3.5)

        self.play(FadeIn(formulas_preview, shift=UP * 0.4), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(preview_circle), FadeOut(preview_label),
            FadeOut(formulas_preview),
            run_time=0.5
        )
        self.author_mob = author   # keep author throughout

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 2 – Definition: rotation of semicircle
    # ══════════════════════════════════════════════════════════════════════════
    def scene_02_definition(self):
        # Switch to a nice 3-D angle
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.2)

        # ── Title (2-D overlay) ──
        title = Text("球的定义", font=FONT, font_size=36, color=C_GOLD
                     ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # ── Draw the rotation axis ──
        axis_line = Line3D(
            start=np.array([0, -self.R - 0.3, 0]) + self.sphere_center,
            end  =np.array([0,  self.R + 0.3, 0]) + self.sphere_center,
            color=C_AXIS, thickness=0.02
        )
        axis_label = Text("旋转轴", font=FONT, font_size=20, color=C_AXIS
                          ).move_to(UP * (self.sphere_center[1] + self.R + 0.8))
        self.add_fixed_in_frame_mobjects(axis_label)
        self.play(Create(axis_line), FadeIn(axis_label), run_time=0.7)

        # ── Semicircle (the generating curve) ──
        sc_offset = np.array([self.sphere_center[0], self.sphere_center[1], 0.0])
        semicircle = Arc(
            radius=self.R, start_angle=PI/2, angle=PI,
            color=C_PINK, stroke_width=4
        ).shift(sc_offset)

        self.play(Create(semicircle), run_time=0.8)

        # Explanation
        explain = self.bottom_text(
            "以直径所在直线为轴，",
            "将半圆旋转一周，",
            "得到的旋转体叫做球。",
            start_y=-3.8, color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.8)

        # ── Animate the sphere appearing (simulate rotation) ──
        sphere = Sphere(
            radius=self.R,
            resolution=(24, 24),
            fill_color=C_SPHERE,
            fill_opacity=0.35,
        ).move_to(self.sphere_center)
        sphere.set_stroke(color=C_SPHERE, width=0.5, opacity=0.6)

        self.play(
            FadeOut(semicircle),
            Create(sphere),
            run_time=1.5
        )

        # Ambient rotation to show 3-D nature
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        # Center dot
        center_dot = Dot3D(point=self.sphere_center, radius=0.08, color=C_GOLD)
        center_label = Text("球心 O", font=FONT, font_size=22, color=C_GOLD
                            ).move_to(UP * (self.sphere_center[1] + 0.4) + RIGHT * 0.8)
        self.add_fixed_in_frame_mobjects(center_label)
        self.play(FadeIn(center_dot), Write(center_label), run_time=0.5)

        # Radius line
        tip = self.sphere_center + np.array([self.R * np.sin(PI/4),
                                              self.R * np.cos(PI/4) * 0.5,
                                              self.R * np.cos(PI/4)])
        radius_line = Line3D(self.sphere_center, tip, color=C_RADIUS, thickness=0.03)
        r_label = MathTex(r"R", font_size=28, color=C_RADIUS
                          ).move_to(UP * 1.6 + RIGHT * 1.5)
        self.add_fixed_in_frame_mobjects(r_label)
        self.play(Create(radius_line), Write(r_label), run_time=0.6)
        self.wait(1.5)

        # Clean-up (keep sphere, center_dot, axis_line for next scene)
        self.play(
            FadeOut(title), FadeOut(axis_label), FadeOut(explain),
            FadeOut(center_label), FadeOut(r_label),
            FadeOut(axis_line), FadeOut(radius_line),
            run_time=0.5
        )
        self.sphere_mob    = sphere
        self.center_dot_mob = center_dot

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 3 – Cross-sections
    # ══════════════════════════════════════════════════════════════════════════
    def scene_03_cross_section(self):
        self.move_camera(phi=65 * DEGREES, theta=-50 * DEGREES, run_time=0.8)

        title = Text("球的截面", font=FONT, font_size=36, color=C_GOLD
                     ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.4)

        # Cross-section plane at height d above center
        # The cross-section is a circle of radius r_cross in the XZ-plane at y = d
        cx, cy, cz = self.sphere_center
        section_y = cy + self.d

        # Draw the cross-section circle (as an Annulus / circle in 3D)
        cross_circle = Circle(
            radius=self.r_cross,
            color=C_PINK, stroke_width=5, fill_opacity=0.2, fill_color=C_PINK
        )
        cross_circle.rotate(PI/2, axis=RIGHT)  # lay flat (XZ plane)
        cross_circle.move_to(np.array([cx, section_y, cz]))

        # Dashed diameter of cross-section
        p1 = np.array([cx - self.r_cross, section_y, cz])
        p2 = np.array([cx + self.r_cross, section_y, cz])
        diam_line = DashedLine(p1, p2, color=C_PINK, dash_length=0.12)

        # Distance line d
        d_line = DashedLine(
            self.sphere_center,
            np.array([cx, section_y, cz]),
            color=C_AXIS, dash_length=0.1
        )
        d_label = MathTex(r"d", font_size=26, color=C_AXIS
                          ).move_to(UP * (section_y - 0.15) + LEFT * 0.8)
        self.add_fixed_in_frame_mobjects(d_label)

        # r label
        r_label = MathTex(r"r", font_size=26, color=C_PINK
                          ).move_to(UP * (section_y + 0.25) + RIGHT * (self.r_cross * 0.5 + 0.1))
        self.add_fixed_in_frame_mobjects(r_label)

        self.play(Create(cross_circle), run_time=0.8)
        self.play(Create(d_line), Write(d_label), run_time=0.5)
        self.play(Create(diam_line), Write(r_label), run_time=0.5)

        # Formula
        formula = MathTex(
            r"r = \sqrt{R^2 - d^2}",
            font_size=34, color=C_PINK
        ).move_to(UP * (-3.8))
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=0.8)

        explain = self.bottom_text(
            "球的截面都是圆，",
            "d 为球心到截面距离",
            start_y=-5.0
        )
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)

        # Gentle rotation
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(title), FadeOut(cross_circle), FadeOut(diam_line),
            FadeOut(d_line), FadeOut(d_label), FadeOut(r_label),
            FadeOut(formula), FadeOut(explain),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 4 – Great Circle
    # ══════════════════════════════════════════════════════════════════════════
    def scene_04_great_circle(self):
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=0.7)

        title = Text("大圆", font=FONT, font_size=36, color=C_GOLD
                     ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.4)

        cx, cy, cz = self.sphere_center

        # Great circle = section through center, r = R
        great_circle = Circle(
            radius=self.R,
            color=C_GOLD, stroke_width=5, fill_opacity=0.12, fill_color=C_GOLD
        )
        great_circle.rotate(PI/2, axis=RIGHT)
        great_circle.move_to(self.sphere_center)

        self.play(Create(great_circle), run_time=1.0)

        # d = 0 line
        center_mark = DashedLine(
            self.sphere_center, self.sphere_center,  # zero length -> just a dot flash
            color=C_AXIS
        )

        # Radius labels
        r1 = Line3D(self.sphere_center,
                    self.sphere_center + np.array([self.R, 0, 0]),
                    color=C_RADIUS, thickness=0.03)
        r_label = MathTex(r"R", font_size=28, color=C_RADIUS
                          ).move_to(UP * (cy + 0.3) + RIGHT * (self.R * 0.5 + 0.3))
        self.add_fixed_in_frame_mobjects(r_label)
        self.play(Create(r1), Write(r_label), run_time=0.5)

        # Formula
        formula = VGroup(
            MathTex(r"d = 0 \Rightarrow r = R", font_size=30, color=C_GOLD),
            MathTex(r"S = \pi R^2", font_size=34, color=C_GOLD),
        ).arrange(DOWN, buff=0.3).move_to(UP * (-3.7))
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=0.9)

        explain = self.bottom_text(
            "过球心的截面叫大圆，",
            "大圆是球面上最大的圆",
            start_y=-5.2, color=C_GOLD
        )
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(title), FadeOut(great_circle), FadeOut(r1),
            FadeOut(r_label), FadeOut(formula), FadeOut(explain),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 5 – Surface Area
    # ══════════════════════════════════════════════════════════════════════════
    def scene_05_surface_area(self):
        self.move_camera(phi=65 * DEGREES, theta=-40 * DEGREES, run_time=0.7)

        title = Text("球的表面积", font=FONT, font_size=36, color=C_PINK
                     ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # Re-color sphere to highlight
        self.play(
            self.sphere_mob.animate.set_fill(color=C_PINK, opacity=0.45),
            run_time=0.6
        )

        # Unwrap visual: 4 circles
        cx, cy, cz = self.sphere_center

        # 4 flat circles representing "4 great circles"
        circle_positions = [
            np.array([-3.5, -3.0, 0]),
            np.array([-1.1, -3.0, 0]),
            np.array([ 1.3, -3.0, 0]),
            np.array([ 3.7, -3.0, 0]),
        ]
        circles_2d = VGroup(*[
            Circle(radius=0.55, color=C_PINK, fill_opacity=0.5, fill_color=C_PINK,
                   stroke_width=2)
            .move_to(p)
            for p in circle_positions
        ])
        label_4 = Text("= 4 个大圆面积", font=FONT, font_size=22, color=C_PINK
                       ).move_to(UP * (-4.2))
        self.add_fixed_in_frame_mobjects(circles_2d, label_4)
        self.play(FadeIn(circles_2d), FadeIn(label_4), run_time=0.7)

        # Main formula
        formula = MathTex(
            r"S = 4\pi R^2",
            font_size=50, color=C_PINK
        ).move_to(UP * (-5.3))
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=0.8)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.2)
        self.stop_ambient_camera_rotation()

        # Example
        example_text = VGroup(
            Text("例: R = 3", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"S = 4\pi \times 9 = 36\pi", font_size=24, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(UP * (-6.3))
        self.add_fixed_in_frame_mobjects(example_text)
        self.play(FadeIn(example_text), run_time=0.5)
        self.wait(1.5)

        # Restore sphere color
        self.play(
            self.sphere_mob.animate.set_fill(color=C_SPHERE, opacity=0.35),
            run_time=0.4
        )
        self.play(
            FadeOut(title), FadeOut(circles_2d), FadeOut(label_4),
            FadeOut(formula), FadeOut(example_text),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 6 – Volume
    # ══════════════════════════════════════════════════════════════════════════
    def scene_06_volume(self):
        self.move_camera(phi=60 * DEGREES, theta=-35 * DEGREES, run_time=0.7)

        title = Text("球的体积", font=FONT, font_size=36, color=C_GREEN
                     ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        self.play(
            self.sphere_mob.animate.set_fill(color=C_GREEN, opacity=0.5),
            run_time=0.6
        )

        # Volume formula – step by step
        formula_1 = MathTex(
            r"V = \dfrac{4}{3}\pi R^3",
            font_size=50, color=C_GREEN
        ).move_to(UP * (-3.8))
        self.add_fixed_in_frame_mobjects(formula_1)
        self.play(Write(formula_1), run_time=1.0)

        # Memory tip
        tip_title = Text("记忆口诀", font=FONT, font_size=24, color=C_GOLD
                         ).move_to(UP * (-5.0))
        tip_body  = Text("三分之四π R 三次方", font=FONT, font_size=22,
                         color=GRAY_A).move_to(UP * (-5.7))
        self.add_fixed_in_frame_mobjects(tip_title, tip_body)
        self.play(FadeIn(tip_title), FadeIn(tip_body), run_time=0.5)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        # Example
        example = VGroup(
            Text("例: R = 3", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"V = \dfrac{4}{3}\pi \times 27 = 36\pi", font_size=24, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(UP * (-6.5))
        self.add_fixed_in_frame_mobjects(example)
        self.play(FadeIn(example), run_time=0.5)
        self.wait(1.5)

        # Summary of both formulas
        summary_bg = RoundedRectangle(
            width=6.5, height=1.8, corner_radius=0.2,
            fill_color="#1a2a3a", fill_opacity=0.95, stroke_color=C_GOLD, stroke_width=1.5
        ).move_to(UP * (-2.0))
        s_fml = MathTex(r"S = 4\pi R^2", font_size=30, color=C_PINK).move_to(UP * (-1.6))
        v_fml = MathTex(r"V = \dfrac{4}{3}\pi R^3", font_size=30, color=C_GREEN
                        ).move_to(UP * (-2.5))
        self.add_fixed_in_frame_mobjects(summary_bg, s_fml, v_fml)
        self.play(FadeIn(summary_bg), Write(s_fml), Write(v_fml), run_time=0.8)
        self.wait(1.5)

        self.play(
            self.sphere_mob.animate.set_fill(color=C_SPHERE, opacity=0.35),
            run_time=0.4
        )
        self.play(
            FadeOut(title), FadeOut(formula_1), FadeOut(tip_title), FadeOut(tip_body),
            FadeOut(example), FadeOut(summary_bg), FadeOut(s_fml), FadeOut(v_fml),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 7 – Circumscribed & Inscribed Sphere
    # ══════════════════════════════════════════════════════════════════════════
    def scene_07_circumscribed(self):
        self.move_camera(phi=70 * DEGREES, theta=-55 * DEGREES, run_time=0.8)

        # ── Fade out main sphere, shrink ──
        self.play(
            self.sphere_mob.animate.scale(0.55).move_to(np.array([-2.2, 1.5, 0])),
            self.center_dot_mob.animate.move_to(np.array([-2.2, 1.5, 0])).scale(0.6),
            run_time=0.7
        )

        # ── CIRCUMSCRIBED SPHERE (外接球) ──
        title_circ = Text("外接球", font=FONT, font_size=32, color=C_GREEN
                          ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title_circ)
        self.play(Write(title_circ), run_time=0.4)

        # Cube inscribed in sphere
        cube_side = 1.5
        half = cube_side / 2
        cube_verts = np.array([
            [ half,  half,  half], [-half,  half,  half],
            [-half, -half,  half], [ half, -half,  half],
            [ half,  half, -half], [-half,  half, -half],
            [-half, -half, -half], [ half, -half, -half],
        ]) + np.array([-2.2, 1.5, 0])

        cube_edges = [
            (0,1),(1,2),(2,3),(3,0),   # top face
            (4,5),(5,6),(6,7),(7,4),   # bottom face
            (0,4),(1,5),(2,6),(3,7),   # verticals
        ]
        cube_lines = VGroup(*[
            Line3D(cube_verts[a], cube_verts[b], color=C_GOLD, thickness=0.018)
            for a, b in cube_edges
        ])

        # Circumscribed sphere radius for cube: R = (√3/2) * side
        R_circ = (np.sqrt(3) / 2) * cube_side
        circ_sphere = Sphere(
            radius=R_circ, resolution=(20, 20),
            fill_color=C_GREEN, fill_opacity=0.12
        ).move_to(np.array([-2.2, 1.5, 0]))
        circ_sphere.set_stroke(color=C_GREEN, width=1.0, opacity=0.7)

        self.play(Create(cube_lines), run_time=0.8)
        self.play(Create(circ_sphere), run_time=0.8)

        explain_circ = self.bottom_text(
            "外接球: 各顶点在球面上",
            start_y=-3.8, color=C_GREEN
        )
        self.add_fixed_in_frame_mobjects(explain_circ)
        self.play(FadeIn(explain_circ), run_time=0.4)
        self.wait(1.5)

        # ── INSCRIBED SPHERE (内切球) ──
        self.play(
            FadeOut(title_circ), FadeOut(explain_circ),
            run_time=0.4
        )
        title_insc = Text("内切球", font=FONT, font_size=32, color=C_ORANGE
                          ).move_to(UP * 6.0)
        self.add_fixed_in_frame_mobjects(title_insc)
        self.play(Write(title_insc), run_time=0.4)

        # Inscribed sphere radius for cube: R = side/2
        R_insc = cube_side / 2
        insc_sphere = Sphere(
            radius=R_insc, resolution=(20, 20),
            fill_color=C_ORANGE, fill_opacity=0.4
        ).move_to(np.array([-2.2, 1.5, 0]))
        insc_sphere.set_stroke(color=C_ORANGE, width=0.5, opacity=0.8)

        self.play(FadeOut(circ_sphere), run_time=0.3)
        self.play(Create(insc_sphere), run_time=0.8)

        explain_insc = self.bottom_text(
            "内切球: 各面都与球面相切",
            start_y=-3.8, color=C_ORANGE
        )
        self.add_fixed_in_frame_mobjects(explain_insc)
        self.play(FadeIn(explain_insc), run_time=0.4)
        self.wait(1.5)

        # ── Ratio card ──
        ratio_bg = RoundedRectangle(
            width=7.0, height=2.0, corner_radius=0.2,
            fill_color="#1a1a2e", fill_opacity=0.95,
            stroke_color=GRAY_B, stroke_width=1.2
        ).move_to(UP * (-4.8))
        ratio_title = Text("正方体外接球 vs 内切球", font=FONT, font_size=20, color=WHITE
                           ).move_to(UP * (-4.2))
        ratio_body = VGroup(
            Text("R外 : R内 = ", font=FONT, font_size=22, color=GRAY_A),
            MathTex(
                r"\dfrac{\sqrt{3}}{2}s\;:\;\dfrac{s}{2}\;=\;\sqrt{3}:1",
                font_size=22, color=GRAY_A
            ),
        ).arrange(RIGHT, buff=0.12).move_to(UP * (-5.3))
        self.add_fixed_in_frame_mobjects(ratio_body)
        self.play(FadeIn(ratio_body), run_time=0.8)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(title_insc), FadeOut(explain_insc),
            FadeOut(insc_sphere), FadeOut(cube_lines),
            FadeOut(ratio_bg), FadeOut(ratio_title), FadeOut(ratio_body),
            FadeOut(self.sphere_mob), FadeOut(self.center_dot_mob),
            run_time=0.6
        )

    # ══════════════════════════════════════════════════════════════════════════
    # Scene 8 – Outro / Summary
    # ══════════════════════════════════════════════════════════════════════════
    def scene_08_outro(self):
        self.move_camera(phi=0, theta=0, run_time=0.8)   # back to 2-D view

        # Final summary card
        bg = RoundedRectangle(
            width=7.5, height=8.5, corner_radius=0.35,
            fill_color="#0d1b2a", fill_opacity=0.96,
            stroke_color=C_GOLD, stroke_width=2.0
        ).move_to(UP * 1.2)

        t_title = Text("球 — 公式总结", font=FONT, font_size=34, color=C_GOLD
                       ).move_to(UP * 4.8)

        row_circum = VGroup(
            Text("外接球:", font=FONT, font_size=22, color=GRAY_A),
            VGroup(
                Text("R外", font=FONT, font_size=26, color=C_GREEN),
                MathTex(r"\geq", font_size=26, color=C_GREEN),
                Text("R内", font=FONT, font_size=26, color=C_GREEN),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.9)

        rows = VGroup(
            self._summary_row("表面积",  r"S = 4\pi R^2",               C_PINK,   UP * 3.5),
            self._summary_row("体积",    r"V = \dfrac{4}{3}\pi R^3",    C_GREEN,  UP * 2.4),
            self._summary_row("截面半径", r"r = \sqrt{R^2 - d^2}",      C_SPHERE, UP * 1.3),
            self._summary_row("大圆面积", r"S = \pi R^2",               C_GOLD,   UP * 0.2),
            row_circum,   # ← 替换原来含CJK的行
        )

        self.add_fixed_in_frame_mobjects(bg, t_title, rows)
        self.play(FadeIn(bg), Write(t_title), run_time=0.6)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.35)

        # Follow call-to-action
        cta = Text("关注我，获得更多数学技巧！", font=FONT, font_size=28, color=C_GOLD
                   ).move_to(DOWN * 5.5)
        author_big = Text(
            "上海初高中数学直通车", font=FONT, font_size=30, color=WHITE
        ).move_to(DOWN * 6.5)
        id_text = Text("@emptyandcalm", font=FONT, font_size=22, color=GRAY_B
                       ).move_to(DOWN * 7.2)
        self.add_fixed_in_frame_mobjects(cta, author_big, id_text)
        self.play(FadeIn(cta, shift=UP * 0.3), FadeIn(author_big), FadeIn(id_text),
                  run_time=0.6)

        self.wait(3.0)

    def _summary_row(self, zh_label, formula_str, color, pos):
        lbl = Text(zh_label + ":", font=FONT, font_size=22, color=GRAY_A)
        fml = MathTex(formula_str, font_size=26, color=color)
        row = VGroup(lbl, fml).arrange(RIGHT, buff=0.3)
        row.move_to(pos)
        return row