"""
长方体的直观图画法 - 斜二测画法
TikTok vertical (1080×1920), Manim 0.19.2, ThreeDScene
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ─── Color palette ───────────────────────────────────────────────────────────
BG          = "#0d0d1a"
C_TITLE     = "#f1c40f"
C_AUTHOR    = "#6c7a89"
C_WHITE     = "#ecf0f1"
C_HORIZ     = "#e74c3c"   # Red  – horizontal
C_VERT      = "#2ecc71"   # Green – vertical
C_DEPTH     = "#f39c12"   # Orange – depth
C_FRONT     = "#3498db"   # Blue  – front face
C_HIDDEN    = "#7f8c8d"   # Gray  – hidden edges
C_GRID      = "#2c3e50"
C_RULE_BOX  = "#1a2533"


def proj_oblique(x, y, z, scale=0.5, angle=np.pi/4):
    """斜二测画法 projection: x/y kept, z → (z*scale @ angle)."""
    return np.array([
        x + z * scale * np.cos(angle),
        y + z * scale * np.sin(angle),
        0
    ])


class CuboidObliqueDrawing(ThreeDScene):
    # ═══════════════════════════════════════════════════════════════════════
    def construct(self):
        self.camera.background_color = BG

        self.setup_geometry()

        self.scene_1_hook()
        self.scene_2_rules()
        self.scene_3_step_by_step()
        self.scene_4_summary()
        self.scene_5_outro()

    # ── GEOMETRY SETUP ──────────────────────────────────────────────────────
    def setup_geometry(self):
        # ─ 3D cuboid (centered at origin) ─
        W, H, D = 2.2, 1.4, 1.4
        self.dim3 = (W, H, D)
        w2, h2, d2 = W/2, H/2, D/2

        self.v3 = {
            'A': np.array([-w2, -h2, -d2]),  # front-bottom-left
            'B': np.array([ w2, -h2, -d2]),  # front-bottom-right
            'C': np.array([ w2,  h2, -d2]),  # front-top-right
            'D': np.array([-w2,  h2, -d2]),  # front-top-left
            'E': np.array([-w2, -h2,  d2]),  # back-bottom-left
            'F': np.array([ w2, -h2,  d2]),  # back-bottom-right
            'G': np.array([ w2,  h2,  d2]),  # back-top-right
            'H': np.array([-w2,  h2,  d2]),  # back-top-left
        }

        # ─ 2D oblique drawing (in xy-plane) ─
        W2, H2, D2 = 3.0, 1.8, 1.8
        self.dim2 = (W2, H2, D2)

        raw = {
            'A': proj_oblique(0, 0, 0),
            'B': proj_oblique(W2, 0, 0),
            'C': proj_oblique(W2, H2, 0),
            'D': proj_oblique(0, H2, 0),
            'E': proj_oblique(0, 0, D2),
            'F': proj_oblique(W2, 0, D2),
            'G': proj_oblique(W2, H2, D2),
            'H': proj_oblique(0, H2, D2),
        }

        # Center the 2D drawing
        xs = [v[0] for v in raw.values()]
        ys = [v[1] for v in raw.values()]
        cx = (max(xs) + min(xs)) / 2
        cy = (max(ys) + min(ys)) / 2

        self.v2 = {k: v - np.array([cx, cy, 0]) for k, v in raw.items()}

        # ─ verify ─
        depth_vec = self.v2['E'] - self.v2['A']
        angle_deg = np.degrees(np.arctan2(depth_vec[1], depth_vec[0]))
        depth_len = np.linalg.norm(depth_vec)
        assert abs(angle_deg - 45) < 1e-4, f"Depth angle error: {angle_deg}"
        assert abs(depth_len - D2/2) < 1e-4, f"Depth length error: {depth_len}"
        print("✓ geometry verified")

    # ── helpers ─────────────────────────────────────────────────────────────
    def cuboid_3d(self, color=C_FRONT, hidden_color=C_HIDDEN,
                  stroke=3, offset=ORIGIN):
        v = self.v3
        def L(a, b, col, sw=stroke, dashed=False):
            s, e = v[a] + offset, v[b] + offset
            if dashed:
                return DashedLine(s, e, color=col, stroke_width=sw,
                                  dash_length=0.12)
            return Line3D(s, e, color=col, stroke_width=sw)

        visible = VGroup(
            L('A','B', color), L('B','C', color), L('C','D', color), L('D','A', color),
            L('C','G', color), L('B','F', color), L('G','F', color),
            L('D','H', color), L('H','G', color),
        )
        hidden = VGroup(
            L('A','E', hidden_color, dashed=True),
            L('E','F', hidden_color, dashed=True),
            L('E','H', hidden_color, dashed=True),
        )
        return visible, hidden

    def line2d(self, a, b, color=WHITE, stroke=3, dashed=False):
        s, e = self.v2[a], self.v2[b]
        if dashed:
            return DashedLine(s, e, color=color, stroke_width=stroke,
                              dash_length=0.12)
        return Line(s, e, color=color, stroke_width=stroke)

    def fixed_text(self, txt, font_size=26, color=C_WHITE, pos=ORIGIN):
        t = Text(txt, font="Noto Sans CJK SC",
                 font_size=font_size, color=color)
        t.move_to(pos)
        return t

    def rule_card(self, number, desc, color, y_pos):
        num = Text(f"规则 {number}", font="Noto Sans CJK SC",
                   font_size=28, color=color)
        txt = Text(desc, font="Noto Sans CJK SC",
                   font_size=22, color=C_WHITE)
        card = VGroup(num, txt).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        card.move_to(np.array([0, y_pos, 0]))
        return card

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 1: Hook – rotating 3D cuboid
    # ═══════════════════════════════════════════════════════════════════════
    def scene_1_hook(self):
        # Camera
        self.set_camera_orientation(phi=68*DEGREES, theta=-50*DEGREES)
        self.camera.set_zoom(0.75)

        # Author tag
        author = self.fixed_text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=19, color=C_AUTHOR,
            pos=np.array([0, 7.3, 0])
        )
        self.add_fixed_in_frame_mobjects(author)
        self.play(FadeIn(author), run_time=0.3)

        # Title hook
        hook = self.fixed_text(
            "长方体怎么画？",
            font_size=48, color=C_TITLE,
            pos=np.array([0, 5.8, 0])
        )
        sub = self.fixed_text(
            "斜二测画法 · 三步搞定",
            font_size=30, color=C_WHITE,
            pos=np.array([0, 5.0, 0])
        )
        self.add_fixed_in_frame_mobjects(hook, sub)
        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP*0.2), run_time=0.4)

        # 3D cuboid — shifted up slightly in 3D space
        offset = np.array([0, 0.8, 0])
        visible, hidden = self.cuboid_3d(
            color=C_FRONT, hidden_color=C_HIDDEN, offset=offset
        )
        self.play(
            LaggedStart(*[Create(l) for l in visible], lag_ratio=0.08),
            run_time=1.4
        )
        self.play(
            LaggedStart(*[Create(l) for l in hidden], lag_ratio=0.15),
            run_time=0.6
        )

        # Ambient camera rotation
        self.begin_ambient_camera_rotation(rate=0.35)
        self.wait(2.8)
        self.stop_ambient_camera_rotation()

        # Fade out hook texts
        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(visible), FadeOut(hidden),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 2: Rules – three rules explanation
    # ═══════════════════════════════════════════════════════════════════════
    def scene_2_rules(self):
        # Move camera to near-front view for 2D explanation
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES,
                         zoom=0.85, run_time=1.0)

        title = self.fixed_text("斜二测画法规则", 40, C_TITLE,
                                np.array([0, 5.8, 0]))
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.6)

        # ─ Draw axes in xy-plane ─
        axis_o = np.array([0, 0.5, 0])
        ax_len = 3.0
        ax_x = Arrow(axis_o, axis_o + RIGHT*ax_len, color=C_HORIZ,
                     stroke_width=4, buff=0, tip_length=0.2)
        ax_y = Arrow(axis_o, axis_o + UP*ax_len, color=C_VERT,
                     stroke_width=4, buff=0, tip_length=0.2)
        ax_z = Arrow(axis_o, axis_o + (RIGHT+UP)*0.707*ax_len,
                     color=C_DEPTH, stroke_width=4, buff=0, tip_length=0.2)

        lx = Text("x (水平)", font="Noto Sans CJK SC",
                  font_size=22, color=C_HORIZ)
        lx.next_to(ax_x, RIGHT, buff=0.1)
        ly = Text("y (竖直)", font="Noto Sans CJK SC",
                  font_size=22, color=C_VERT)
        ly.next_to(ax_y, UP, buff=0.1)
        lz = Text("z (深度)", font="Noto Sans CJK SC",
                  font_size=22, color=C_DEPTH)
        lz.next_to(ax_z, UR, buff=0.05)

        axes_group = VGroup(ax_x, ax_y, ax_z, lx, ly, lz)
        axes_group.move_to(np.array([0, 0.5, 0]))

        self.play(
            Create(ax_x), Create(ax_y), Create(ax_z),
            run_time=1.0
        )
        self.play(Write(lx), Write(ly), Write(lz), run_time=0.6)
        self.wait(0.4)

        # ─ Rule 1 ─
        rule1 = self.rule_card("①", "水平方向保持原长", C_HORIZ,
                                y_pos=-2.5)
        # Show a horizontal line with "= 原长" label
        hr_start = np.array([-1.5, -0.2, 0])
        hr_end   = np.array([ 1.5, -0.2, 0])
        h_line = Line(hr_start, hr_end, color=C_HORIZ, stroke_width=5)
        h_brace = BraceBetweenPoints(hr_start, hr_end, direction=DOWN,
                                     color=C_HORIZ)
        h_brace_lbl = Text("原长 a", font="Noto Sans CJK SC",
                           font_size=20, color=C_HORIZ)
        h_brace_lbl.next_to(h_brace, DOWN, buff=0.1)

        self.add_fixed_in_frame_mobjects(rule1)
        self.play(FadeIn(rule1, shift=RIGHT*0.4), run_time=0.5)
        self.play(Create(h_line), run_time=0.5)
        self.play(
            GrowFromCenter(h_brace),
            FadeIn(h_brace_lbl),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(FadeOut(h_line), FadeOut(h_brace), FadeOut(h_brace_lbl),
                  run_time=0.3)

        # ─ Rule 2 ─
        rule2 = self.rule_card("②", "竖直方向保持原长", C_VERT,
                                y_pos=-3.4)
        vr_start = np.array([0, -0.5, 0])
        vr_end   = np.array([0,  1.5, 0])
        v_line = Line(vr_start, vr_end, color=C_VERT, stroke_width=5)
        v_brace = BraceBetweenPoints(vr_start, vr_end, direction=RIGHT,
                                     color=C_VERT)
        v_brace_lbl = Text("原长 b", font="Noto Sans CJK SC",
                           font_size=20, color=C_VERT)
        v_brace_lbl.next_to(v_brace, RIGHT, buff=0.1)

        self.add_fixed_in_frame_mobjects(rule2)
        self.play(FadeIn(rule2, shift=RIGHT*0.4), run_time=0.5)
        self.play(Create(v_line), run_time=0.5)
        self.play(
            GrowFromCenter(v_brace),
            FadeIn(v_brace_lbl),
            run_time=0.5
        )
        self.wait(0.8)
        self.play(FadeOut(v_line), FadeOut(v_brace), FadeOut(v_brace_lbl),
                  run_time=0.3)

        # ─ Rule 3 ─
        rule3 = self.rule_card("③", "深度方向: 长度减半, 倾斜45°", C_DEPTH,
                                y_pos=-4.4)
        # Depth arrow at 45°
        d_origin = np.array([0, 0, 0])
        d_vec    = np.array([1.0, 1.0, 0])  # 45°, length √2
        d_full_end = d_origin + d_vec * 1.2
        d_half_end = d_origin + d_vec * 0.6  # half

        d_full_arrow = Arrow(d_origin, d_full_end, color=GRAY_B,
                             stroke_width=3, buff=0, tip_length=0.18)
        d_half_arrow = Arrow(d_origin, d_half_end, color=C_DEPTH,
                             stroke_width=5, buff=0, tip_length=0.18)

        angle_arc = Arc(radius=0.45, start_angle=0,
                        angle=PI/4, color=C_DEPTH, stroke_width=3)
        angle_arc.move_to(d_origin, aligned_edge=ORIGIN)
        angle_lbl = MathTex(r"45^\circ", font_size=22, color=C_DEPTH)
        angle_lbl.next_to(angle_arc, RIGHT, buff=0.05)
        half_lbl = MathTex(r"\times\frac{1}{2}", font_size=22, color=C_DEPTH)
        half_lbl.next_to(d_half_arrow, UR, buff=0.1)

        self.add_fixed_in_frame_mobjects(rule3)
        self.play(FadeIn(rule3, shift=RIGHT*0.4), run_time=0.5)
        self.play(GrowArrow(d_full_arrow), run_time=0.5)
        self.play(GrowArrow(d_half_arrow), run_time=0.5)
        self.play(
            Create(angle_arc), Write(angle_lbl),
            Write(half_lbl),
            run_time=0.6
        )
        self.wait(1.2)

        # Clear rules section
        self.play(
            FadeOut(title), FadeOut(axes_group),
            FadeOut(rule1), FadeOut(rule2), FadeOut(rule3),
            FadeOut(d_full_arrow), FadeOut(d_half_arrow),
            FadeOut(angle_arc), FadeOut(angle_lbl), FadeOut(half_lbl),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 3: Step-by-step oblique drawing
    # ═══════════════════════════════════════════════════════════════════════
    def scene_3_step_by_step(self):
        v = self.v2

        # Position all 2D drawing slightly up
        draw_offset = np.array([0, 1.2, 0])

        def dv(k):
            return v[k] + draw_offset

        # ─ Title ─
        title = self.fixed_text("跟我一步步画！", 40, C_TITLE,
                                np.array([0, 5.8, 0]))
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)

        # ─ Step indicator ─
        step_lbl = self.fixed_text("第 1 步：画坐标轴", 30, C_WHITE,
                                   np.array([0, -3.0, 0]))
        self.add_fixed_in_frame_mobjects(step_lbl)
        self.play(FadeIn(step_lbl), run_time=0.4)

        # Draw axes cross
        ax_o = draw_offset
        ax = VGroup(
            Line(ax_o + LEFT*3.5, ax_o + RIGHT*3.5, color=GRAY_C, stroke_width=1.5),
            Line(ax_o + DOWN*2.5, ax_o + UP*2.5, color=GRAY_C, stroke_width=1.5),
        )
        # x' axis label
        ax_x_lbl = Text("x'", font="Noto Sans CJK SC",
                         font_size=22, color=GRAY_C)
        ax_x_lbl.next_to(ax_o + RIGHT*3.5, RIGHT, buff=0.1)
        ax_y_lbl = Text("y'", font="Noto Sans CJK SC",
                         font_size=22, color=GRAY_C)
        ax_y_lbl.next_to(ax_o + UP*2.5, UP, buff=0.1)
        ax_z_dir = Arrow(ax_o, ax_o + RIGHT*0.6+UP*0.6,
                         color=GRAY_C, stroke_width=2, buff=0, tip_length=0.15)

        self.play(Create(ax), run_time=0.6)
        self.play(Write(ax_x_lbl), Write(ax_y_lbl), run_time=0.3)
        self.wait(0.5)

        # ─ Step 2: Front face ─
        new_step = self.fixed_text("第 2 步：画正面（原尺寸）", 30, C_FRONT,
                                   np.array([0, -3.0, 0]))
        self.add_fixed_in_frame_mobjects(new_step)
        self.play(Transform(step_lbl, new_step), run_time=0.4)

        # Front face: A B C D (z=0 face)
        front_face = Polygon(
            dv('A'), dv('B'), dv('C'), dv('D'),
            color=C_FRONT, stroke_width=4, fill_opacity=0.08,
            fill_color=C_FRONT
        )
        self.play(Create(front_face), run_time=1.0)

        # Dimension labels for front face
        W2, H2, D2 = self.dim2
        w_brace = BraceBetweenPoints(dv('A'), dv('B'), direction=DOWN, color=C_HORIZ)
        w_lbl = MathTex(r"a", font_size=24, color=C_HORIZ)
        w_lbl.next_to(w_brace, DOWN, buff=0.08)

        h_brace = BraceBetweenPoints(dv('B'), dv('C'), direction=RIGHT, color=C_VERT)
        h_lbl = MathTex(r"b", font_size=24, color=C_VERT)
        h_lbl.next_to(h_brace, RIGHT, buff=0.08)

        self.play(
            GrowFromCenter(w_brace), FadeIn(w_lbl),
            GrowFromCenter(h_brace), FadeIn(h_lbl),
            run_time=0.6
        )
        self.wait(0.8)
        self.play(FadeOut(w_brace), FadeOut(w_lbl),
                  FadeOut(h_brace), FadeOut(h_lbl), run_time=0.3)

        # ─ Step 3: Depth edges (45°, half) ─
        step3 = self.fixed_text("第 3 步：画深度边（45°，减半）",
                                28, C_DEPTH, np.array([0, -3.0, 0]))
        self.add_fixed_in_frame_mobjects(step3)
        self.play(Transform(step_lbl, step3), run_time=0.4)

        # Draw 4 depth edges from front to back
        depth_edges = []
        depth_pairs = [('A', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H')]
        for a, b in depth_pairs:
            line = Line(dv(a), dv(b), color=C_DEPTH, stroke_width=4)
            depth_edges.append(line)

        # Animate them one by one to show 45° direction
        depth_guide = Arrow(
            dv('A'), dv('E'),
            color=YELLOW, stroke_width=5, buff=0, tip_length=0.2
        )
        guide_lbl = self.fixed_text("45°, 长度×½", 24, YELLOW,
                                    np.array([0, -4.0, 0]))
        self.add_fixed_in_frame_mobjects(guide_lbl)
        self.play(GrowArrow(depth_guide), FadeIn(guide_lbl), run_time=0.8)
        self.wait(0.4)
        self.play(FadeOut(depth_guide), FadeOut(guide_lbl), run_time=0.3)

        self.play(
            LaggedStart(*[Create(e) for e in depth_edges],
                        lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(0.5)

        # ─ Step 4: Back face ─
        step4 = self.fixed_text("第 4 步：完成背面", 30, C_WHITE,
                                np.array([0, -3.0, 0]))
        self.add_fixed_in_frame_mobjects(step4)
        self.play(Transform(step_lbl, step4), run_time=0.4)

        # Back face visible edges: F-G, G-H, G-C (top back)
        # E is hidden (behind A), so E-F, E-H are dashed
        back_visible = VGroup(
            Line(dv('F'), dv('G'), color=C_FRONT, stroke_width=4),
            Line(dv('G'), dv('H'), color=C_FRONT, stroke_width=4),
            Line(dv('G'), dv('C'), color=C_FRONT, stroke_width=3),
            Line(dv('F'), dv('B'), color=C_FRONT, stroke_width=3),
            Line(dv('H'), dv('D'), color=C_FRONT, stroke_width=3),
        )
        back_hidden = VGroup(
            DashedLine(dv('E'), dv('F'), color=C_HIDDEN, stroke_width=3,
                       dash_length=0.12),
            DashedLine(dv('E'), dv('H'), color=C_HIDDEN, stroke_width=3,
                       dash_length=0.12),
            DashedLine(dv('E'), dv('A'), color=C_HIDDEN, stroke_width=3,
                       dash_length=0.12),
        )

        self.play(
            LaggedStart(*[Create(e) for e in back_visible], lag_ratio=0.1),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[Create(e) for e in back_hidden], lag_ratio=0.15),
            run_time=0.6
        )
        self.wait(0.5)

        # ─ Completion flash ─
        complete_lbl = self.fixed_text("✓ 完成！", 42, C_TITLE,
                                       np.array([0, -3.8, 0]))
        self.add_fixed_in_frame_mobjects(complete_lbl)
        self.play(FadeIn(complete_lbl, scale=1.3), run_time=0.5)
        self.wait(1.5)

        # Keep references for next scene
        self.all_2d_parts = VGroup(
            ax, ax_x_lbl, ax_y_lbl,
            front_face,
            *depth_edges,
            back_visible, back_hidden
        )

        # Fade out step labels
        self.play(
            FadeOut(title), FadeOut(step_lbl),
            FadeOut(complete_lbl),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 4: Summary comparison
    # ═══════════════════════════════════════════════════════════════════════
    def scene_4_summary(self):
        # Move 2D drawing to left side, show 3D cuboid on right
        sum_title = self.fixed_text("记住这三条规则！", 38, C_TITLE,
                                    np.array([0, 5.8, 0]))
        self.add_fixed_in_frame_mobjects(sum_title)
        self.play(Write(sum_title), run_time=0.5)

        # Compact rule recap
        rules = VGroup(
            Text("① 水平方向  保持原长  →", font="Noto Sans CJK SC",
                 font_size=26, color=C_HORIZ),
            Text("② 竖直方向  保持原长  ↑", font="Noto Sans CJK SC",
                 font_size=26, color=C_VERT),
            Text("③ 深度方向  减半 + 45°", font="Noto Sans CJK SC",
                 font_size=26, color=C_DEPTH),
        )
        rules.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rules.move_to(np.array([0, -4.0, 0]))

        self.add_fixed_in_frame_mobjects(rules)
        for r in rules:
            self.play(FadeIn(r, shift=RIGHT*0.3), run_time=0.4)

        # Highlight 2D drawing
        self.play(
            self.all_2d_parts.animate.set_stroke(opacity=0.9),
            run_time=0.5
        )
        self.wait(2.0)

        self.play(
            FadeOut(sum_title),
            FadeOut(rules),
            FadeOut(self.all_2d_parts),
            run_time=0.7
        )

    # ═══════════════════════════════════════════════════════════════════════
    # SCENE 5: Outro
    # ═══════════════════════════════════════════════════════════════════════
    def scene_5_outro(self):
        # Fly back to 3D view
        self.move_camera(phi=65*DEGREES, theta=-45*DEGREES,
                         zoom=0.8, run_time=1.0)

        # Final 3D cuboid
        offset = np.array([0, 0.6, 0])
        visible, hidden = self.cuboid_3d(
            color=C_TITLE, hidden_color=C_HIDDEN, offset=offset
        )
        self.play(
            LaggedStart(*[Create(l) for l in visible], lag_ratio=0.06),
            run_time=1.0
        )
        self.play(
            LaggedStart(*[Create(l) for l in hidden], lag_ratio=0.15),
            run_time=0.4
        )

        author_big = self.fixed_text(
            "上海初高中数学直通车", 40, C_WHITE, np.array([0, -3.0, 0])
        )
        author_id = self.fixed_text(
            "@emptyandcalm", 30, C_AUTHOR, np.array([0, -3.9, 0])
        )
        follow = self.fixed_text(
            "关注我，学更多数学技巧！", 30, C_TITLE, np.array([0, -5.0, 0])
        )
        self.add_fixed_in_frame_mobjects(author_big, author_id, follow)
        self.play(
            FadeIn(author_big, shift=UP*0.2),
            FadeIn(author_id, shift=UP*0.2),
            run_time=0.6
        )
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)

        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3.0)
        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(visible), FadeOut(hidden),
            FadeOut(author_big), FadeOut(author_id), FadeOut(follow),
            run_time=0.8
        )


# ─── Entry point ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # manim -qh cuboid_oblique.py CuboidObliqueDrawing
    pass