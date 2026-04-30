"""
pyramid_lesson.py — 棱锥教学动画
格式: TikTok 竖屏 1080×1920
引擎: Manim 0.19.2 ThreeDScene

渲染命令:
    manim -pql pyramid_lesson.py PyramidLesson   # 快速预览 480p
    manim -qh  pyramid_lesson.py PyramidLesson   # 高质量 1080p
"""

from manim import *
import numpy as np

# ── 全局配置 ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 颜色方案 ─────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
BASE_COLOR    = "#4ecdc4"    # 底面
FACE1_COLOR   = "#ff6b6b"    # 侧面 PAB
FACE2_COLOR   = "#ffd93d"    # 侧面 PBC
FACE3_COLOR   = "#6bcb77"    # 侧面 PCD
FACE4_COLOR   = "#a29bfe"    # 侧面 PDA
EDGE_COLOR    = "#ffffff"
APEX_COLOR    = "#ffd93d"
HEIGHT_COLOR  = "#74b9ff"
SLANT_COLOR   = "#fd79a8"
ACCENT_COLOR  = "#ffd93d"
AUTHOR_COLOR  = "#636e72"

# ── 几何参数（精确计算，与 verify_geometry.py 保持一致）──
a = 2.4          # 底面边长
h = 2.0          # 棱锥高
s = a / 2        # 半边长（= 1.2）

# 底面顶点（正方形，z = 0）
A_pt = np.array([-s, -s, 0.0])
B_pt = np.array([ s, -s, 0.0])
C_pt = np.array([ s,  s, 0.0])
D_pt = np.array([-s,  s, 0.0])
P_pt = np.array([0.0, 0.0, h])   # 顶点（正上方）
O_pt = np.array([0.0, 0.0, 0.0]) # 底面中心
M_AB = (A_pt + B_pt) / 2         # AB 中点 (0, -1.2, 0)

slant_h  = float(np.linalg.norm(P_pt - M_AB))  # 斜高 ≈ 2.332
edge_len = float(np.linalg.norm(P_pt - A_pt))  # 侧棱长 ≈ 2.623
S_base   = a ** 2                               # 底面积 = 5.76
S_side   = 0.5 * 4 * a * slant_h               # 侧面积 ≈ 11.20
S_total  = S_base + S_side                      # 全面积 ≈ 16.96
volume   = S_base * h / 3                       # 体积 ≈ 3.84


# ════════════════════════════════════════════════════════════
class PyramidLesson(ThreeDScene):
    """正四棱锥教学动画 — 总时长约 70 秒"""

    # ════════════════════════════════
    # CONSTRUCT
    # ════════════════════════════════
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            zoom=0.75
        )

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_components()
        self.scene_4_regular_pyramid()
        self.scene_5_volume()
        self.scene_6_surface_area()
        self.scene_7_outro()

    # ════════════════════════════════
    # HELPER: Build pyramid
    # ════════════════════════════════
    def make_pyramid_mobs(self, face_opacity=0.40, base_opacity=0.60):
        """
        构建正四棱锥所有几何元素。
        返回 dict，键名即 mobject 名称。
        """
        A, B, C, D, P = A_pt, B_pt, C_pt, D_pt, P_pt

        base = Polygon(A, B, C, D,
                       fill_color=BASE_COLOR, fill_opacity=base_opacity,
                       stroke_color=EDGE_COLOR, stroke_width=2.5)

        face_defs = [
            (P, A, B, FACE1_COLOR),
            (P, B, C, FACE2_COLOR),
            (P, C, D, FACE3_COLOR),
            (P, D, A, FACE4_COLOR),
        ]
        faces = [
            Polygon(p1, p2, p3,
                    fill_color=col, fill_opacity=face_opacity,
                    stroke_color=EDGE_COLOR, stroke_width=2.5)
            for p1, p2, p3, col in face_defs
        ]
        faces_group = VGroup(*faces)

        # Base edges (stroked on top for clarity)
        base_edges = VGroup(
            Line(A, B, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(B, C, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(C, D, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(D, A, stroke_color=EDGE_COLOR, stroke_width=3),
        )
        lat_edges = VGroup(
            Line(P, A, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(P, B, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(P, C, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(P, D, stroke_color=EDGE_COLOR, stroke_width=3),
        )

        apex_dot = Dot3D(P, color=APEX_COLOR, radius=0.09)
        base_dot = Dot3D(O_pt, color=WHITE, radius=0.05)

        return dict(
            base=base, faces=faces, faces_group=faces_group,
            base_edges=base_edges, lat_edges=lat_edges,
            apex_dot=apex_dot, base_dot=base_dot,
            A=A, B=B, C=C, D=D, P=P,
        )

    # ════════════════════════════════
    # HELPER: Fixed-frame text
    # ════════════════════════════════
    def ft(self, txt, size=26, color=WHITE):
        """Short helper: create a fixed-frame Chinese Text mobject."""
        return Text(txt, font="PingFang SC", font_size=size, color=color)

    def add_ft(self, *mobs):
        """add_fixed_in_frame_mobjects shortcut."""
        self.add_fixed_in_frame_mobjects(*mobs)

    def fade_ft(self, *mobs, rt=0.4):
        """FadeOut fixed-frame mobs and remove them."""
        self.play(*[FadeOut(m) for m in mobs], run_time=rt)
        for m in mobs:
            self.remove(m)

    # ════════════════════════════════
    # SCENE 1 — Opening Hook  (≈5s)
    # ════════════════════════════════
    def scene_1_opening(self):
        # ── Author watermark (top) ────────────────────
        author_wm = self.ft("上海初高中数学直通车 @emptyandcalm", size=18, color=AUTHOR_COLOR)
        author_wm.move_to(UP * 7.2)
        self.add_ft(author_wm)
        self.play(FadeIn(author_wm, shift=DOWN * 0.15), run_time=0.4)

        # ── Hook title ───────────────────────────────
        hook = self.ft("一分钟搞懂棱锥！", size=54, color=ACCENT_COLOR)
        hook.move_to(UP * 5.8)
        self.add_ft(hook)
        self.play(Write(hook), run_time=0.8)

        sub = self.ft("定义 · 性质 · 体积 · 表面积", size=26, color=GRAY_A)
        sub.move_to(UP * 4.7)
        self.add_ft(sub)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # ── Build pyramid 3D ─────────────────────────
        pyr = self.make_pyramid_mobs()
        self._pyr = pyr  # store for other scenes

        # Base grows first
        self.play(DrawBorderThenFill(pyr["base"]), run_time=0.8)
        # Base edges
        self.play(Create(pyr["base_edges"]), run_time=0.4)
        # Lateral edges
        self.play(Create(pyr["lat_edges"]), run_time=0.5)
        # Side faces
        self.play(
            *[DrawBorderThenFill(f) for f in pyr["faces"]],
            FadeIn(pyr["apex_dot"]),
            run_time=1.0
        )

        # Dramatic rotation
        self.move_camera(theta=-90 * DEGREES, run_time=1.2, rate_func=smooth)
        self.move_camera(theta=-45 * DEGREES, run_time=0.8, rate_func=smooth)
        self.wait(0.4)

        self.fade_ft(hook, sub, rt=0.4)

    # ════════════════════════════════
    # SCENE 2 — Definition  (≈8s)
    # ════════════════════════════════
    def scene_2_definition(self):
        pyr = self._pyr

        title = self.ft("棱锥的定义", size=44, color=ACCENT_COLOR).move_to(UP * 6.3)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # ── Definition line 1: 底面
        def1 = self.ft("① 底面是多边形", size=30, color=BASE_COLOR).move_to(UP * 5.2)
        self.add_ft(def1)
        self.play(
            pyr["base"].animate.set_fill(BASE_COLOR, 0.9).set_stroke(YELLOW, 4),
            Write(def1),
            run_time=0.6
        )
        self.wait(0.6)
        self.play(
            pyr["base"].animate.set_fill(BASE_COLOR, 0.6).set_stroke(EDGE_COLOR, 2.5),
            run_time=0.3
        )

        # ── Definition line 2: 侧面
        def2 = self.ft("② 侧面都是三角形", size=30, color=FACE1_COLOR).move_to(UP * 4.2)
        self.add_ft(def2)
        face_pab = pyr["faces"][0]
        self.play(
            face_pab.animate.set_fill(FACE1_COLOR, 0.9).set_stroke(YELLOW, 4),
            Write(def2),
            run_time=0.6
        )
        self.wait(0.6)
        self.play(face_pab.animate.set_fill(FACE1_COLOR, 0.40).set_stroke(EDGE_COLOR, 2.5), run_time=0.3)

        # ── Definition line 3: 公共顶点
        def3 = self.ft("③ 共享公共顶点 P", size=30, color=APEX_COLOR).move_to(UP * 3.2)
        self.add_ft(def3)
        self.play(
            Flash(pyr["apex_dot"], color=APEX_COLOR, flash_radius=0.4, line_length=0.15),
            Write(def3),
            run_time=0.7
        )
        self.wait(0.8)

        # ── Type intro
        tip = self.ft("底面有几条边 → 几棱锥", size=24, color=GRAY_A).move_to(UP * 2.1)
        self.add_ft(tip)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)
        self.wait(0.7)

        self.fade_ft(title, def1, def2, def3, tip, rt=0.4)

    # ════════════════════════════════
    # SCENE 3 — Components  (≈14s)
    # ════════════════════════════════
    def scene_3_components(self):
        pyr = self._pyr
        P, A, B, C, D = pyr["P"], pyr["A"], pyr["B"], pyr["C"], pyr["D"]

        title = self.ft("各部分名称", size=44, color=ACCENT_COLOR).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # ─── (a) 顶点 P ───────────────────────────────
        info = self.ft("P  ——  顶点（公共顶点）", size=28, color=APEX_COLOR).move_to(UP * 5.3)
        self.add_ft(info)
        self.play(Flash(pyr["apex_dot"], color=APEX_COLOR, flash_radius=0.5), Write(info), run_time=0.6)
        self.wait(0.8)
        self.fade_ft(info, rt=0.3)

        # ─── (b) 底面 ABCD ─────────────────────────────
        info = self.ft("ABCD  ——  底面（多边形）", size=28, color=BASE_COLOR).move_to(UP * 5.3)
        self.add_ft(info)
        self.play(
            pyr["base"].animate.set_stroke(YELLOW, 5).set_fill(BASE_COLOR, 0.9),
            Write(info), run_time=0.6
        )
        self.wait(0.8)
        self.play(pyr["base"].animate.set_stroke(EDGE_COLOR, 2.5).set_fill(BASE_COLOR, 0.60), run_time=0.3)
        self.fade_ft(info, rt=0.3)

        # ─── (c) 侧面 △PAB ─────────────────────────────
        face_pab = pyr["faces"][0]
        info = self.ft("△PAB  ——  侧面（三角形）", size=28, color=FACE1_COLOR).move_to(UP * 5.3)
        self.add_ft(info)
        self.play(
            face_pab.animate.set_fill(FACE1_COLOR, 0.9).set_stroke(YELLOW, 5),
            Write(info), run_time=0.6
        )
        self.wait(0.8)
        self.play(face_pab.animate.set_fill(FACE1_COLOR, 0.40).set_stroke(EDGE_COLOR, 2.5), run_time=0.3)
        self.fade_ft(info, rt=0.3)

        # ─── (d) 侧棱 PA ────────────────────────────────
        edge_PA = Line(P, A, stroke_color=YELLOW, stroke_width=6)
        info = self.ft("PA  ——  侧棱（顶点→底面顶点）", size=27, color=YELLOW).move_to(UP * 5.3)
        self.add_ft(info)
        self.play(Create(edge_PA), Write(info), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(edge_PA), run_time=0.3)
        self.fade_ft(info, rt=0.3)

        # ─── (e) 高 h ────────────────────────────────────
        # h_line: P → O (vertical dashed)
        h_line = DashedLine(P, O_pt, color=HEIGHT_COLOR, stroke_width=5, dash_length=0.14)
        ra_size = 0.22
        # Right-angle mark at O_pt (in XY plane)
        ra_mark = Polygon(
            O_pt,
            O_pt + np.array([ra_size, 0, 0]),
            O_pt + np.array([ra_size, 0, ra_size]),
            O_pt + np.array([0,       0, ra_size]),
            stroke_color=HEIGHT_COLOR, stroke_width=2, fill_opacity=0
        )
        info = self.ft("h  ——  棱锥的高（垂直底面）", size=27, color=HEIGHT_COLOR).move_to(UP * 5.3)
        h_tex = MathTex(r"h \perp \text{base}", font_size=32, color=HEIGHT_COLOR).move_to(UP * 4.5)
        h_note = self.ft("（高垂直底面）", size=22, color=HEIGHT_COLOR).move_to(UP * 3.8)
        self.add_ft(info, h_tex, h_note)
        self.play(Create(h_line), FadeIn(ra_mark), Write(info), run_time=0.7)
        self.play(Write(h_tex), run_time=0.4)
        self.play(FadeIn(h_note), run_time=0.3)
        self.wait(1.0)
        self.play(FadeOut(h_line), FadeOut(ra_mark), run_time=0.3)
        self.fade_ft(info, h_tex, h_note, rt=0.3)

        # ─── (f) 斜高 l ─────────────────────────────────
        m_ab = M_AB.copy()
        slant_line = Line(P, m_ab, stroke_color=SLANT_COLOR, stroke_width=5)
        m_dot = Dot3D(m_ab, color=SLANT_COLOR, radius=0.07)
        info = self.ft("l  ——  斜高（顶点→底边中点）", size=27, color=SLANT_COLOR).move_to(UP * 5.3)
        slant_tex = MathTex(
            r"l = \sqrt{h^2 + \left(\frac{a}{2}\right)^2}",
            font_size=30, color=SLANT_COLOR
        ).move_to(UP * 4.3)
        self.add_ft(info, slant_tex)
        self.play(Create(slant_line), FadeIn(m_dot), Write(info), run_time=0.7)
        self.play(Write(slant_tex), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(slant_line), FadeOut(m_dot), run_time=0.3)
        self.fade_ft(info, slant_tex, rt=0.3)

        self.fade_ft(title, rt=0.4)

    # ════════════════════════════════
    # SCENE 4 — 正棱锥 Properties  (≈9s)
    # ════════════════════════════════
    def scene_4_regular_pyramid(self):
        pyr = self._pyr
        P = pyr["P"]
        A, B, C, D = pyr["A"], pyr["B"], pyr["C"], pyr["D"]

        title = self.ft("正棱锥", size=52, color=ACCENT_COLOR).move_to(UP * 6.5)
        sub   = self.ft("底面正多边形 + 顶点在正上方", size=24, color=GRAY_A).move_to(UP * 5.6)
        self.add_ft(title, sub)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        props = [
            ("① 所有侧棱相等", FACE1_COLOR, UP * 4.6),
            ("② 侧面都是等腰三角形", FACE2_COLOR, UP * 3.7),
            ("③ 所有斜高相等", SLANT_COLOR,  UP * 2.8),
        ]
        prop_mobs = []
        for txt, col, pos in props:
            m = self.ft(txt, size=28, color=col).move_to(pos)
            self.add_ft(m)
            self.play(FadeIn(m, shift=RIGHT * 0.3), run_time=0.4)
            prop_mobs.append(m)
            self.wait(0.4)

        # Slow rotation to show symmetry
        self.move_camera(theta=-90 * DEGREES, run_time=1.5, rate_func=smooth)

        # Highlight all lateral edges equally
        lat_highlight = VGroup(
            Line(P, A, stroke_color=YELLOW, stroke_width=5),
            Line(P, B, stroke_color=YELLOW, stroke_width=5),
            Line(P, C, stroke_color=YELLOW, stroke_width=5),
            Line(P, D, stroke_color=YELLOW, stroke_width=5),
        )
        self.play(Create(lat_highlight), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(lat_highlight), run_time=0.4)

        self.move_camera(theta=-45 * DEGREES, run_time=1.0, rate_func=smooth)
        self.wait(0.3)

        self.fade_ft(title, sub, *prop_mobs, rt=0.4)

    # ════════════════════════════════
    # SCENE 5 — Volume Formula  (≈14s)
    # ════════════════════════════════
    def scene_5_volume(self):
        pyr = self._pyr
        P = pyr["P"]

        title = self.ft("体积公式", size=48, color=ACCENT_COLOR).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # ── Show height visually ─────────────────────
        h_line = DashedLine(P, O_pt, color=HEIGHT_COLOR, stroke_width=5, dash_length=0.14)
        base_hl = pyr["base"].copy().set_fill(BASE_COLOR, 0.9)
        self.play(Create(h_line), run_time=0.6)
        self.play(base_hl.animate.set_stroke(YELLOW, 4), run_time=0.3)

        # ── Analogy text ────────────────────────────
        analogy = self.ft("棱锥 = ⅓ × 同底等高的棱柱", size=26, color=WHITE).move_to(UP * 5.4)
        self.add_ft(analogy)
        self.play(FadeIn(analogy, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # ── Core formula ────────────────────────────
        form_core = MathTex(
            r"V = \frac{1}{3} \cdot S_{\text{base}} \cdot h",
            font_size=50, color=ACCENT_COLOR
        ).move_to(UP * 4.3)
        self.add_ft(form_core)
        self.play(Write(form_core), run_time=1.0)
        self.play(Indicate(form_core, scale_factor=1.1, color=YELLOW), run_time=0.6)
        self.wait(0.6)

        # ── Substitution ────────────────────────────
        sub_txt = self.ft("代入数值：", size=24, color=GRAY_A).move_to(UP * 3.3)
        self.add_ft(sub_txt)
        self.play(FadeIn(sub_txt), run_time=0.3)

        form_sub = MathTex(
            rf"V = \frac{{1}}{{3}} \times {a:.1f}^2 \times {h:.1f}",
            font_size=36, color=WHITE
        ).move_to(UP * 2.6)
        self.add_ft(form_sub)
        self.play(Write(form_sub), run_time=0.7)
        self.wait(0.4)

        form_sub2 = MathTex(
            rf"V = \frac{{1}}{{3}} \times {S_base:.2f} \times {h:.1f}",
            font_size=36, color=WHITE
        ).move_to(UP * 1.8)
        self.add_ft(form_sub2)
        self.play(Write(form_sub2), run_time=0.6)
        self.wait(0.3)

        result_v = MathTex(
            rf"V = {volume:.2f}",
            font_size=52, color=ACCENT_COLOR
        ).move_to(UP * 0.9)
        self.add_ft(result_v)
        self.play(Write(result_v), run_time=0.6)
        self.play(Indicate(result_v, scale_factor=1.15), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(h_line), FadeOut(base_hl), run_time=0.3)
        self.fade_ft(title, analogy, form_core, sub_txt, form_sub, form_sub2, result_v, rt=0.5)

    # ════════════════════════════════
    # SCENE 6 — Surface Area  (≈10s)
    # ════════════════════════════════
    def scene_6_surface_area(self):
        pyr = self._pyr
        P = pyr["P"]

        title = self.ft("表面积公式", size=46, color=ACCENT_COLOR).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # Highlight all faces
        for f in pyr["faces"]:
            f.set_fill(opacity=0.8)
        self.wait(0.3)

        # ── Total area ──────────────────────────────
        form_total = MathTex(
            r"S = S_{\text{base}} + S_{\text{lateral}}",
            font_size=48, color=WHITE
        ).move_to(UP * 5.4)
        self.add_ft(form_total)
        self.play(Write(form_total), run_time=0.7)
        self.wait(0.5)

        # ── Lateral area formula ─────────────────────
        # Show slant height line
        slant_vis = Line(P, M_AB, stroke_color=SLANT_COLOR, stroke_width=5)
        self.play(Create(slant_vis), run_time=0.4)

        form_lateral = MathTex(
            r"S_{\text{lateral}} = \frac{1}{2} \cdot C \cdot l",
            font_size=40, color=SLANT_COLOR
        ).move_to(UP * 4.3)
        note_cl = self.ft("C = 底面周长，l = 斜高", size=22, color=GRAY_A).move_to(UP * 3.5)
        self.add_ft(form_lateral, note_cl)
        self.play(Write(form_lateral), FadeIn(note_cl), run_time=0.7)
        self.wait(0.6)

        # ── Numbers ─────────────────────────────────
        form_nums = MathTex(
            rf"S = ({a:.1f})^2 + \frac{{1}}{{2}} \times 4 \times {a:.1f} \times {slant_h:.2f}",
            font_size=28, color=WHITE
        ).move_to(UP * 2.6)
        self.add_ft(form_nums)
        self.play(Write(form_nums), run_time=0.8)
        self.wait(0.4)

        result_s = MathTex(
            rf"S \approx {S_total:.2f}",
            font_size=50, color=ACCENT_COLOR
        ).move_to(UP * 1.7)
        self.add_ft(result_s)
        self.play(Write(result_s), run_time=0.6)
        self.play(Indicate(result_s, scale_factor=1.15), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(slant_vis), run_time=0.3)
        for f in pyr["faces"]:
            f.set_fill(opacity=0.40)
        self.fade_ft(title, form_total, form_lateral, note_cl, form_nums, result_s, rt=0.5)

    # ════════════════════════════════
    # SCENE 7 — Summary + Outro  (≈8s)
    # ════════════════════════════════
    def scene_7_outro(self):
        pyr = self._pyr

        # ── Formula recap ────────────────────────────
        recap_title = self.ft("公式速记卡", size=40, color=ACCENT_COLOR).move_to(UP * 6.5)
        box_v = MathTex(
            r"V = \frac{1}{3} S_{\text{base}} h",
            font_size=40, color=HEIGHT_COLOR
        ).move_to(UP * 5.4)
        box_sl = MathTex(
            r"S_{\text{lateral}} = \frac{1}{2} C \cdot l",
            font_size=40, color=SLANT_COLOR
        ).move_to(UP * 4.4)
        box_st = MathTex(
            r"S = S_{\text{base}} + S_{\text{lateral}}",
            font_size=40, color=FACE1_COLOR
        ).move_to(UP * 3.4)
        slant_eq = MathTex(
            r"l = \sqrt{h^2 + \left(\frac{a}{2}\right)^2}",
            font_size=34, color=GRAY_A
        ).move_to(UP * 2.4)

        self.add_ft(recap_title, box_v, box_sl, box_st, slant_eq)
        self.play(Write(recap_title), run_time=0.4)
        self.play(Write(box_v), run_time=0.5)
        self.play(Write(box_sl), run_time=0.5)
        self.play(Write(box_st), run_time=0.5)
        self.play(Write(slant_eq), run_time=0.5)

        # Slow ambient rotation while formulas are shown
        self.begin_ambient_camera_rotation(rate=0.20)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        # ── Fade out pyramid ─────────────────────────
        pyr_all = VGroup(
            pyr["base"], pyr["faces_group"],
            pyr["base_edges"], pyr["lat_edges"],
            pyr["apex_dot"]
        )
        self.play(
            FadeOut(pyr_all),
            FadeOut(recap_title), FadeOut(box_v), FadeOut(box_sl),
            FadeOut(box_st), FadeOut(slant_eq),
            run_time=0.7
        )
        for m in [recap_title, box_v, box_sl, box_st, slant_eq]:
            self.remove(m)

        # ── Outro card ───────────────────────────────
        author_big = self.ft("上海初高中数学直通车", size=42, color=WHITE).move_to(UP * 2.0)
        author_id  = self.ft("@emptyandcalm", size=30, color=GRAY_B).move_to(UP * 0.9)
        follow_txt = self.ft("关注我，获得更多数学技巧！", size=30, color=ACCENT_COLOR).move_to(ORIGIN + DOWN * 0.3)

        self.add_ft(author_big, author_id, follow_txt)
        self.play(
            FadeIn(author_big, scale=1.05),
            FadeIn(author_id, shift=UP * 0.2),
            run_time=0.8
        )
        self.play(FadeIn(follow_txt, shift=UP * 0.3), run_time=0.5)

        # Decorative pyramid icon (small)
        small_pyr = self.make_pyramid_mobs(face_opacity=0.6, base_opacity=0.7)
        sp_all = VGroup(
            small_pyr["base"], small_pyr["faces_group"],
            small_pyr["base_edges"], small_pyr["lat_edges"],
            small_pyr["apex_dot"]
        ).scale(0.35).move_to(np.array([0, -3.0, 0]))
        self.play(
            DrawBorderThenFill(small_pyr["base"]),
            Create(small_pyr["base_edges"]),
            Create(small_pyr["lat_edges"]),
            *[DrawBorderThenFill(f) for f in small_pyr["faces"]],
            FadeIn(small_pyr["apex_dot"]),
            run_time=1.0
        )

        self.move_camera(theta=45 * DEGREES, run_time=2.0, rate_func=smooth)
        self.wait(1.5)