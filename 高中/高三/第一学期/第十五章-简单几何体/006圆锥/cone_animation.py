"""
cone_animation.py - 圆锥 (Cone) Teaching Animation
高三数学 - 简单几何体 - 圆锥
TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

Render:
  manim -pql cone_animation.py ConeLesson   # quick preview
  manim -qh  cone_animation.py ConeLesson   # high quality
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# Global config: TikTok vertical
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
# Design tokens
# ─────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
CONE_BLUE     = "#64b5f6"
CONE_DARK     = "#1565c0"
ACCENT_RED    = "#ef5350"
ACCENT_GREEN  = "#66bb6a"
ACCENT_ORANGE = "#ffa726"
TEXT_DIM      = "#9e9e9e"
FONT          = "Noto Sans CJK SC"

# ─────────────────────────────────────────────
# Helper: Chinese label
# ─────────────────────────────────────────────
def cn(text, size=22, color=WHITE, **kw):
    return Text(text, font=FONT, font_size=size, color=color, **kw)


class ConeLesson(ThreeDScene):
    """完整圆锥教学动画"""

    # ═══════════════════════════════════════════
    # SETUP
    # ═══════════════════════════════════════════

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_opening()
        self.scene_formation()
        self.scene_label_parts()
        self.scene_slant_height()
        self.scene_unfold()
        self.scene_formulas()
        self.scene_outro()

    def setup_geometry(self):
        """All cone parameters — 3-4-5 right triangle scaled."""
        # 3-4-5 right triangle (r:h:l = 3:4:5) → scale 0.55
        S = 0.55
        self.r = 3 * S   # 1.65  base radius
        self.h = 4 * S   # 2.20  height
        self.l = 5 * S   # 2.75  slant height

        # Verify: l = sqrt(r²+h²)
        l_check = np.sqrt(self.r**2 + self.h**2)
        assert abs(l_check - self.l) < 1e-10, f"Slant height error: {l_check} ≠ {self.l}"

        # Sector angle (>180° so MUST use Arc, not Angle class)
        # θ = 2πr/l → 216° for 3-4-5
        self.sector_angle = 2 * np.pi * self.r / self.l   # 3.7699 rad = 216°
        self.sector_angle_deg = np.degrees(self.sector_angle)  # 216.0

        # Cone display position in 3D: apex UP, base at z=0
        # Shift up so it sits in the top portion of the TikTok frame
        self.cone_z_offset = 0.8   # base starts here (z)
        self.cone_apex_z   = self.cone_z_offset + self.h

        print(f"✓ Cone geometry: r={self.r:.3f}, h={self.h:.3f}, l={self.l:.3f}")
        print(f"✓ Sector angle: {self.sector_angle_deg:.1f}° (>180° → use Arc)")

    # ═══════════════════════════════════════════
    # SCENE 1: Opening hook
    # ═══════════════════════════════════════════
    def scene_opening(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)

        # ── Author tag (fixed 2D) ──────────────
        author = cn("上海初高中数学直通车 @emptyandcalm",
                    size=18, color=TEXT_DIM)
        author.to_edge(UP).shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(author)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # ── Hook question ──────────────────────
        hook = cn("冰淇淋、漏斗、山峰…", size=30, color=YELLOW)
        hook.move_to(UP * 5.8)
        hook2 = cn("它们都是圆锥体！", size=36, color=WHITE)
        hook2.move_to(UP * 5.0)
        self.add_fixed_in_frame_mobjects(hook, hook2)
        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.5)

        # ── Quick 3D cone teaser ───────────────
        cone_preview = Cone(
            base_radius=self.r, height=self.h, direction=OUT,
            fill_color=CONE_DARK, fill_opacity=0.85,
            stroke_color=CONE_BLUE, stroke_width=1.5
        )
        cone_preview.shift(IN * self.cone_z_offset)   # shift back so apex faces OUT

        self.play(GrowFromCenter(cone_preview), run_time=1.2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(1.2)
        self.stop_ambient_camera_rotation()

        # ── Title ──────────────────────────────
        title = cn("圆　锥", size=48, color=CONE_BLUE)
        title.move_to(UP * 3.8)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.7)
        self.wait(0.5)

        # Clean up
        self.play(FadeOut(cone_preview), FadeOut(hook), FadeOut(hook2),
                  FadeOut(title), run_time=0.5)

    # ═══════════════════════════════════════════
    # SCENE 2: Formation — right triangle rotating
    # ═══════════════════════════════════════════
    def scene_formation(self):
        self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=0.5)

        # ── Section title ──────────────────────
        sec_title = cn("直角三角形旋转一周", size=30, color=CONE_BLUE)
        sec_title.move_to(UP * 5.8)
        self.add_fixed_in_frame_mobjects(sec_title)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # ── Right triangle in xz-plane ─────────
        # Vertices: O=(0,0,0), A=(r,0,0), C=(0,0,h)
        O = np.array([0, 0, 0])
        A = np.array([self.r, 0, 0])   # base edge point
        C = np.array([0, 0, self.h])   # apex

        # Shift so base is at z=cone_z_offset
        O = O + np.array([0, 0, self.cone_z_offset])
        A = A + np.array([0, 0, self.cone_z_offset])
        C = C + np.array([0, 0, self.cone_z_offset])

        leg_vert  = Line3D(O, C, color=ACCENT_RED,    thickness=0.02)
        leg_horiz = Line3D(O, A, color=ACCENT_GREEN,  thickness=0.02)
        hypotenuse= Line3D(A, C, color=YELLOW,         thickness=0.02)

        # Right angle marker (manual square at O)
        sq_size = 0.1
        sq_pts = [
            O + np.array([sq_size, 0, 0]),
            O + np.array([sq_size, 0, sq_size]),
            O + np.array([0, 0, sq_size])
        ]
        right_mark = Polygon(*sq_pts, color=WHITE, stroke_width=1.5, fill_opacity=0)

        self.play(
            Create(leg_vert), Create(leg_horiz),
            Create(hypotenuse), run_time=1.0
        )
        self.play(Create(right_mark), run_time=0.3)

        # Label: "旋转轴"
        axis_label = cn("旋转轴", size=22, color=ACCENT_RED)
        axis_label.move_to(LEFT * 1.5 + UP * 3.5)
        self.add_fixed_in_frame_mobjects(axis_label)
        self.play(FadeIn(axis_label), run_time=0.4)

        # ── Show rotation axis ─────────────────
        rot_axis = DashedLine(
            np.array([0, 0, self.cone_z_offset - 0.3]),
            np.array([0, 0, self.cone_z_offset + self.h + 0.3]),
            color=ACCENT_RED, dash_length=0.12, stroke_width=2
        )
        self.play(Create(rot_axis), run_time=0.5)

        # ── Rotate camera around to show it spinning ──
        explain = cn("绕直角边旋转360°", size=26, color=YELLOW)
        explain.move_to(DOWN * 4.5)
        self.add_fixed_in_frame_mobjects(explain)
        self.play(FadeIn(explain), run_time=0.4)

        # Animate camera orbit to simulate the triangle sweeping
        self.begin_ambient_camera_rotation(rate=1.2)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()
        # Return to -90 degrees
        self.move_camera(theta=-90 * DEGREES, run_time=0.5)

        # ── Reveal the cone ────────────────────
        cone = Cone(
            base_radius=self.r, height=self.h, direction=OUT,
            fill_color=CONE_DARK, fill_opacity=0.75,
            stroke_color=CONE_BLUE, stroke_width=1.5
        )
        # In Manim, Cone direction=OUT → apex at +z, base at -z
        # Shift so base is at z=cone_z_offset
        cone.shift(np.array([0, 0, self.cone_z_offset]))

        self.play(
            FadeIn(cone, run_time=1.0),
            FadeOut(leg_horiz), FadeOut(hypotenuse),
            FadeOut(right_mark)
        )
        self.wait(0.5)

        # Keep cone for next scene
        self.cone_obj   = cone
        self.leg_vert   = leg_vert
        self.rot_axis   = rot_axis
        self.cone_apex  = C
        self.cone_base_center = O

        # Clean temp labels
        self.play(FadeOut(sec_title), FadeOut(axis_label),
                  FadeOut(explain), run_time=0.4)

    # ═══════════════════════════════════════════
    # SCENE 3: Label parts
    # ═══════════════════════════════════════════
    def scene_label_parts(self):
        sec_title = cn("认识圆锥各部分", size=30, color=CONE_BLUE)
        sec_title.move_to(UP * 5.8)
        self.add_fixed_in_frame_mobjects(sec_title)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.5)

        # ── Apex dot ──────────────────────────
        apex_dot = Dot3D(self.cone_apex, color=YELLOW, radius=0.07)
        apex_label = cn("顶点 (Apex)", size=22, color=YELLOW)
        apex_label.move_to(RIGHT * 2.5 + UP * 4.0)
        arrow_apex = Arrow(
            apex_label.get_left() + LEFT * 0.1,
            RIGHT * 0.3 + UP * 4.2,
            buff=0.05, color=YELLOW, stroke_width=2
        )
        self.add_fixed_in_frame_mobjects(apex_label)

        self.play(FadeIn(apex_dot), run_time=0.4)
        self.play(Write(apex_label), run_time=0.5)

        # ── Base circle label ──────────────────
        base_circle = Circle(radius=self.r, color=ACCENT_GREEN,
                             stroke_width=2.5)
        # Position base circle at base of cone in 3D
        # Use a flat circle at z = cone_z_offset
        base_circle_3d = Circle(radius=self.r, color=ACCENT_GREEN, stroke_width=2.5)
        base_circle_3d.rotate(PI/2, axis=RIGHT)   # lay flat (xy-plane → xz-plane)
        base_circle_3d.move_to(np.array([0, 0, self.cone_z_offset]))

        base_label = cn("底面 (圆)", size=22, color=ACCENT_GREEN)
        base_label.move_to(LEFT * 3.0 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(base_label)

        self.play(Create(base_circle_3d), Write(base_label), run_time=0.8)
        self.wait(0.3)

        # ── Height line ───────────────────────
        h_start = np.array([0, 0, self.cone_z_offset])
        h_end   = self.cone_apex
        height_line = Line3D(h_start, h_end,
                             color=ACCENT_RED, thickness=0.025)
        h_label = cn("高 h", size=24, color=ACCENT_RED)
        h_label.move_to(LEFT * 2.5 + UP * 2.8)
        self.add_fixed_in_frame_mobjects(h_label)

        self.play(Create(height_line), Write(h_label), run_time=0.7)

        # ── Radius line ───────────────────────
        r_end   = np.array([self.r, 0, self.cone_z_offset])
        r_line  = Line3D(h_start, r_end, color=ACCENT_GREEN, thickness=0.025)
        r_label = cn("底面半径 r", size=24, color=ACCENT_GREEN)
        r_label.move_to(RIGHT * 2.0 + UP * 1.2)
        self.add_fixed_in_frame_mobjects(r_label)

        self.play(Create(r_line), Write(r_label), run_time=0.7)

        # ── Slant height (母线) ───────────────
        slant_line = Line3D(self.cone_apex, r_end,
                            color=YELLOW, thickness=0.03)
        slant_label = cn("母线 l", size=24, color=YELLOW)
        slant_label.move_to(RIGHT * 2.5 + UP * 3.0)
        self.add_fixed_in_frame_mobjects(slant_label)

        self.play(Create(slant_line), Write(slant_label), run_time=0.7)
        self.wait(0.5)

        # ── Side surface label ────────────────
        side_label = cn("侧面 (曲面)", size=22, color=CONE_BLUE)
        side_label.move_to(LEFT * 3.0 + UP * 3.2)
        self.add_fixed_in_frame_mobjects(side_label)
        self.play(
            self.cone_obj.animate.set_fill(color=CONE_BLUE, opacity=0.6),
            Write(side_label), run_time=0.7
        )
        self.wait(1.0)

        # Store references
        self.base_circle_3d = base_circle_3d
        self.height_line    = height_line
        self.r_line         = r_line
        self.slant_line     = slant_line
        self.apex_dot       = apex_dot
        self.h_end_pt       = r_end   # save base-edge point

        # Clean
        self.play(
            FadeOut(sec_title), FadeOut(apex_label),
            FadeOut(base_label), FadeOut(h_label),
            FadeOut(r_label), FadeOut(slant_label),
            FadeOut(side_label), run_time=0.4
        )

    # ═══════════════════════════════════════════
    # SCENE 4: Slant height formula
    # ═══════════════════════════════════════════
    def scene_slant_height(self):
        sec_title = cn("母线公式", size=30, color=YELLOW)
        sec_title.move_to(UP * 5.8)
        self.add_fixed_in_frame_mobjects(sec_title)
        self.play(FadeIn(sec_title), run_time=0.4)

        # Show the right triangle: h (vertical), r (horizontal), l (slant)
        # Highlight with bright colors
        self.play(
            self.height_line.animate.set_color(ACCENT_RED),
            self.r_line.animate.set_color(ACCENT_GREEN),
            self.slant_line.animate.set_color(YELLOW),
            run_time=0.5
        )

        # ── Formula build-up ──────────────────
        formula_box_bg = RoundedRectangle(
            width=7.5, height=4.5, corner_radius=0.3,
            fill_color="#0d1b2a", fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=1.5
        ).move_to(DOWN * 4.0)
        self.add_fixed_in_frame_mobjects(formula_box_bg)
        self.play(FadeIn(formula_box_bg), run_time=0.4)

        # Pythagorean theorem
        pyth = MathTex(r"l^2 = r^2 + h^2", font_size=42, color=WHITE)
        pyth.move_to(DOWN * 2.8)
        self.add_fixed_in_frame_mobjects(pyth)
        self.play(Write(pyth), run_time=0.8)

        # Arrow down
        arrow_down = Arrow(DOWN * 3.5, DOWN * 3.9, color=GRAY_B,
                           stroke_width=2, buff=0.05)
        self.add_fixed_in_frame_mobjects(arrow_down)
        self.play(GrowArrow(arrow_down), run_time=0.4)

        # Final formula
        final_f = MathTex(r"l = \sqrt{r^2 + h^2}", font_size=46, color=YELLOW)
        final_f.move_to(DOWN * 4.5)
        self.add_fixed_in_frame_mobjects(final_f)
        self.play(Write(final_f), run_time=0.8)

        # ── Example with 3-4-5 ─────────────────
        example_label = cn("例: r=3, h=4", size=22, color=TEXT_DIM)
        example_label.move_to(DOWN * 5.3)
        example_calc = MathTex(
            r"l = \sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5",
            font_size=28, color=ACCENT_GREEN
        )
        example_calc.move_to(DOWN * 5.9)
        self.add_fixed_in_frame_mobjects(example_label, example_calc)
        self.play(FadeIn(example_label), Write(example_calc), run_time=0.9)
        self.wait(2.0)

        # Clean
        self.play(
            FadeOut(sec_title), FadeOut(formula_box_bg),
            FadeOut(pyth), FadeOut(arrow_down),
            FadeOut(final_f), FadeOut(example_label),
            FadeOut(example_calc), run_time=0.5
        )

    # ═══════════════════════════════════════════
    # SCENE 5: Unfold lateral surface → sector
    # ═══════════════════════════════════════════
    def scene_unfold(self):
        sec_title = cn("侧面展开图", size=30, color=CONE_BLUE)
        sec_title.move_to(UP * 5.8)
        self.add_fixed_in_frame_mobjects(sec_title)
        self.play(FadeIn(sec_title), run_time=0.4)

        # Fade cone to show just outline
        self.play(
            self.cone_obj.animate.set_fill(opacity=0.25),
            FadeOut(self.height_line),
            FadeOut(self.r_line),
            FadeOut(self.base_circle_3d),
            FadeOut(self.slant_line),
            FadeOut(self.apex_dot),
            run_time=0.6
        )

        # ── Transition: move camera to face-on ─
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.0)

        # ── Now draw the 2D sector ─────────────
        # Sector angle = 216° > 180° → use Arc construction
        # Sector radius = l (slant height) → scaled for display
        display_l = 2.5   # display radius for sector

        # Center of sector at (0, 1.5) in screen coords
        sector_center = np.array([0, 1.5, 0])

        # Arc from -sector_angle/2 to +sector_angle/2 (symmetric about top)
        # Start angle: 90° - sector_angle/2 (so sector fans upward and to the sides)
        start_angle = PI/2 - self.sector_angle/2   # ≈ -18° in radians

        # Build sector as: two radii + arc (angle > PI, must use Arc not Angle)
        # Left radius endpoint
        p_left  = sector_center + display_l * np.array([
            np.cos(start_angle), np.sin(start_angle), 0])
        # Right radius endpoint
        p_right = sector_center + display_l * np.array([
            np.cos(start_angle + self.sector_angle),
            np.sin(start_angle + self.sector_angle), 0])

        # Arc (216° > 180°, so it wraps around the bottom)
        sector_arc = Arc(
            radius=display_l,
            start_angle=start_angle,
            angle=self.sector_angle,      # 3.77 rad = 216°
            color=CONE_BLUE,
            stroke_width=2.5
        ).move_arc_center_to(sector_center)

        # Radii lines
        r_line_left  = Line(sector_center, p_left,  color=YELLOW, stroke_width=2)
        r_line_right = Line(sector_center, p_right, color=YELLOW, stroke_width=2)

        # Fill: create sector polygon approximation
        sector_fill = Sector(
            radius=display_l,
            start_angle=start_angle,
            angle=self.sector_angle,
            fill_color=CONE_DARK,
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(sector_center)

        self.add_fixed_in_frame_mobjects(sector_fill, sector_arc,
                                         r_line_left, r_line_right)
        self.play(
            FadeIn(sector_fill),
            Create(sector_arc),
            Create(r_line_left), Create(r_line_right),
            run_time=1.2
        )

        # ── Labels on sector ──────────────────
        # Radius = l (mother line)
        mid_left_r = (sector_center + p_left) / 2 + np.array([-0.3, 0, 0])
        l_label = MathTex(r"l", font_size=32, color=YELLOW)
        l_label.move_to(LEFT * 3.2 + UP * 2.3)
        self.add_fixed_in_frame_mobjects(l_label)
        self.play(Write(l_label), run_time=0.4)

        # Arc length = 2πr (bottom of arc)
        arc_label = cn("弧长 = 2πr", size=22, color=ACCENT_GREEN)
        arc_label.move_to(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(arc_label)
        self.play(FadeIn(arc_label, shift=UP * 0.2), run_time=0.5)

        # Angle = θ = 360°×r/l
        angle_note = cn(f"圆心角 θ = 360°×r/l", size=20, color=ACCENT_ORANGE)
        angle_note.move_to(DOWN * 2.0)
        angle_val  = MathTex(
            r"\theta = \frac{2\pi r}{l} = \frac{360^\circ \times r}{l}",
            font_size=28, color=ACCENT_ORANGE
        )
        angle_val.move_to(DOWN * 2.8)
        self.add_fixed_in_frame_mobjects(angle_note, angle_val)
        self.play(FadeIn(angle_note), Write(angle_val), run_time=0.8)

        # For 3-4-5: θ = 216°
        angle_specific = cn(f"(r=3, l=5 → θ = 216°)", size=20, color=TEXT_DIM)
        angle_specific.move_to(DOWN * 3.5)
        self.add_fixed_in_frame_mobjects(angle_specific)
        self.play(FadeIn(angle_specific), run_time=0.4)
        self.wait(2.0)

        # Key insight box
        insight_bg = RoundedRectangle(
            width=7.0, height=1.2, corner_radius=0.2,
            fill_color="#1b3a2a", fill_opacity=0.95,
            stroke_color=ACCENT_GREEN, stroke_width=1.5
        ).move_to(DOWN * 5.0)
        insight_txt = cn("扇形弧长 = 底面周长 2πr", size=22, color=ACCENT_GREEN)
        insight_txt.move_to(DOWN * 5.0)
        self.add_fixed_in_frame_mobjects(insight_bg, insight_txt)
        self.play(FadeIn(insight_bg), Write(insight_txt), run_time=0.6)
        self.wait(1.5)

        # Clean
        self.play(
            FadeOut(sec_title), FadeOut(sector_fill), FadeOut(sector_arc),
            FadeOut(r_line_left), FadeOut(r_line_right),
            FadeOut(l_label), FadeOut(arc_label), FadeOut(angle_note),
            FadeOut(angle_val), FadeOut(angle_specific),
            FadeOut(insight_bg), FadeOut(insight_txt),
            FadeOut(self.cone_obj), FadeOut(self.leg_vert),
            FadeOut(self.rot_axis), run_time=0.6
        )

    # ═══════════════════════════════════════════
    # SCENE 6: Formulas
    # ═══════════════════════════════════════════
    def scene_formulas(self):
        # Switch to 2D perspective
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=0.1)

        sec_title = cn("核心公式总结", size=32, color=YELLOW)
        sec_title.move_to(UP * 6.5)
        self.add_fixed_in_frame_mobjects(sec_title)
        self.play(Write(sec_title), run_time=0.5)

        # ── 2D diagram: cone cross-section ─────
        # Draw an isosceles triangle representing axial cross-section
        apex_2d    = np.array([0, 5.2, 0])
        base_L_2d  = np.array([-self.r * 1.8, 3.3, 0])
        base_R_2d  = np.array([self.r  * 1.8, 3.3, 0])
        base_C_2d  = (base_L_2d + base_R_2d) / 2

        triangle_2d = Polygon(apex_2d, base_L_2d, base_R_2d,
                              color=CONE_BLUE, stroke_width=2,
                              fill_color=CONE_DARK, fill_opacity=0.5)
        # Base ellipse (show 3D feel)
        base_ellipse = Ellipse(
            width=self.r * 3.6, height=self.r * 0.7,
            color=CONE_BLUE, stroke_width=1.5
        ).move_to(base_C_2d)
        # Height line dashed
        h_dash_2d = DashedLine(apex_2d, base_C_2d,
                               color=ACCENT_RED, dash_length=0.12, stroke_width=2)
        # Radius line
        r_line_2d = Line(base_C_2d, base_R_2d, color=ACCENT_GREEN, stroke_width=2)
        # Slant
        slant_2d = Line(apex_2d, base_R_2d, color=YELLOW, stroke_width=2)

        # Labels
        lbl_h = MathTex(r"h", font_size=28, color=ACCENT_RED).move_to(LEFT * 0.4 + UP * 4.2)
        lbl_r = MathTex(r"r", font_size=28, color=ACCENT_GREEN).move_to(RIGHT * 1.5 + UP * 3.1)
        lbl_l = MathTex(r"l", font_size=28, color=YELLOW).move_to(RIGHT * 1.0 + UP * 4.2)

        diagram_group = VGroup(triangle_2d, base_ellipse, h_dash_2d,
                               r_line_2d, slant_2d, lbl_h, lbl_r, lbl_l)
        self.add_fixed_in_frame_mobjects(*diagram_group)
        self.play(
            FadeIn(triangle_2d), FadeIn(base_ellipse),
            Create(h_dash_2d), Create(r_line_2d), Create(slant_2d),
            Write(lbl_h), Write(lbl_r), Write(lbl_l),
            run_time=1.0
        )

        # ── Formula cards ──────────────────────
        formulas = [
            # (Chinese label, formula, color)
            ("母　线", r"l = \sqrt{r^2 + h^2}",           YELLOW),
            ("体　积", r"V = \dfrac{1}{3}\pi r^2 h",       ACCENT_GREEN),
            ("侧面积", r"S_{\text{side}} = \pi r l",        CONE_BLUE),
            ("表面积", r"S = \pi r^2 + \pi r l = \pi r(r+l)", ACCENT_ORANGE),
        ]

        card_y_start = 1.5
        card_spacing = 1.8

        all_cards = []
        for i, (label_cn, formula, color) in enumerate(formulas):
            y = card_y_start - i * card_spacing

            # Card background
            card_bg = RoundedRectangle(
                width=8.0, height=1.5, corner_radius=0.25,
                fill_color="#0d1b2a", fill_opacity=0.9,
                stroke_color=color, stroke_width=1.5
            ).move_to(UP * y)

            # Chinese label on left
            c_label = cn(label_cn, size=22, color=color)
            c_label.move_to(LEFT * 2.8 + UP * y)

            # Formula on right
            f_tex = MathTex(formula, font_size=28, color=WHITE)
            f_tex.move_to(RIGHT * 1.0 + UP * y)

            self.add_fixed_in_frame_mobjects(card_bg, c_label, f_tex)
            all_cards.extend([card_bg, c_label, f_tex])
            self.play(
                FadeIn(card_bg, shift=RIGHT * 0.3),
                Write(c_label), Write(f_tex),
                run_time=0.7
            )
            self.wait(0.3)

        self.wait(2.0)

        # ── Axial cross-section highlight ──────
        cross_note = cn("轴截面 = 等腰三角形", size=24, color=ACCENT_ORANGE)
        cross_note.move_to(DOWN * 5.8)
        self.add_fixed_in_frame_mobjects(cross_note)
        self.play(
            triangle_2d.animate.set_stroke(color=ACCENT_ORANGE, width=3),
            Write(cross_note), run_time=0.7
        )
        self.wait(1.5)

        # Clean
        self.play(
            FadeOut(sec_title),
            *[FadeOut(m) for m in diagram_group],
            *[FadeOut(m) for m in all_cards],
            FadeOut(cross_note),
            run_time=0.6
        )

    # ═══════════════════════════════════════════
    # SCENE 7: Outro
    # ═══════════════════════════════════════════
    def scene_outro(self):
        # Bring back cone with rotation
        self.move_camera(phi=65 * DEGREES, theta=-90 * DEGREES, run_time=0.5)

        final_cone = Cone(
            base_radius=self.r, height=self.h, direction=OUT,
            fill_color=CONE_DARK, fill_opacity=0.85,
            stroke_color=CONE_BLUE, stroke_width=1.5
        ).shift(np.array([0, 0, self.cone_z_offset]))

        self.play(GrowFromCenter(final_cone), run_time=0.8)
        self.begin_ambient_camera_rotation(rate=0.4)

        # Summary card
        summary_bg = RoundedRectangle(
            width=8.0, height=5.0, corner_radius=0.4,
            fill_color="#0d1b2a", fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=2
        ).move_to(DOWN * 4.3)
        summary_title = cn("圆锥公式速记", size=28, color=YELLOW)
        summary_title.move_to(DOWN * 2.4)

        lines = VGroup(
            cn("母线  l = √(r²+h²)", size=20, color=YELLOW),
            cn("体积  V = ⅓πr²h",    size=20, color=ACCENT_GREEN),
            cn("侧面积 S = πrl",      size=20, color=CONE_BLUE),
            cn("表面积 S = πr(r+l)", size=20, color=ACCENT_ORANGE),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(DOWN * 4.3)

        self.add_fixed_in_frame_mobjects(summary_bg, summary_title, lines)
        self.play(FadeIn(summary_bg), Write(summary_title), run_time=0.6)
        for line in lines:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.3)

        # Author info large
        author_big = cn("上海初高中数学直通车", size=32, color=WHITE)
        author_big.move_to(UP * 6.2)
        author_id = cn("@emptyandcalm", size=24, color=CONE_BLUE)
        author_id.move_to(UP * 5.5)
        follow = cn("关注我，学更多数学技巧！", size=26, color=YELLOW)
        follow.move_to(UP * 4.7)

        self.add_fixed_in_frame_mobjects(author_big, author_id, follow)
        self.play(
            Write(author_big), FadeIn(author_id), FadeIn(follow),
            run_time=0.8
        )

        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(final_cone), FadeOut(summary_bg),
            FadeOut(summary_title), FadeOut(lines),
            FadeOut(author_big), FadeOut(author_id), FadeOut(follow),
            run_time=1.0
        )