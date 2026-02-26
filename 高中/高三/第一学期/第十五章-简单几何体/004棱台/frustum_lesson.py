"""
frustum_lesson.py — 棱台教学动画（正四棱台）
格式: TikTok 竖屏 1080×1920  |  引擎: Manim 0.19.2 ThreeDScene

渲染命令:
    manim -pql frustum_lesson.py FrustumLesson   # 快速预览 480p
    manim -qh  frustum_lesson.py FrustumLesson   # 高质量 1080p

几何参数:
    a1 = 1.2  (上底边长)    a2 = 2.4  (下底边长)
    h  = 2.0  (棱台高)      h_pyr = 4.0  (原棱锥总高)
    slant ≈ 2.088  (斜高)   V ≈ 6.72   S侧 ≈ 15.03
"""

from manim import *
import numpy as np

# ── 全局视频配置 ──────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 配色方案 ─────────────────────────────────────────────
BG_COLOR     = "#1a1a2e"
BOT_COLOR    = "#4ecdc4"    # 下底面
TOP_COLOR    = "#a8e6cf"    # 上底面
FACE1_COLOR  = "#ff6b6b"    # 侧面 ABB'A'
FACE2_COLOR  = "#ffd93d"    # 侧面 BCC'B'
FACE3_COLOR  = "#6bcb77"    # 侧面 DCC'D' → 实为 CDD'C'
FACE4_COLOR  = "#a29bfe"    # 侧面 DAA'D'
EDGE_COLOR   = "#ecf0f1"
HEIGHT_COLOR = "#74b9ff"
SLANT_COLOR  = "#fd79a8"
ACCENT       = "#ffd93d"
PHANTOM_COL  = "#636e72"
AUTHOR_COLOR = "#636e72"

# ── 精确几何参数（已由 verify_geometry_frustum.py 验证）──
a1 = 1.2 ; a2 = 2.4 ; h = 2.0
k  = a1 / a2            # = 0.5
h_pyr = h / (1 - k)    # = 4.0
s1 = a1 / 2             # = 0.6
s2 = a2 / 2             # = 1.2

# 下底顶点（z = 0）
A_pt  = np.array([-s2, -s2, 0.0])
B_pt  = np.array([ s2, -s2, 0.0])
C_pt  = np.array([ s2,  s2, 0.0])
D_pt  = np.array([-s2,  s2, 0.0])

# 上底顶点（z = h）
Ap_pt = np.array([-s1, -s1, h])
Bp_pt = np.array([ s1, -s1, h])
Cp_pt = np.array([ s1,  s1, h])
Dp_pt = np.array([-s1,  s1, h])

# 原棱锥顶点
APEX  = np.array([0.0, 0.0, h_pyr])

# 斜高端点
M_AB   = (A_pt + B_pt)   / 2   # (0, -1.2, 0)
M_ApBp = (Ap_pt + Bp_pt) / 2   # (0, -0.6, 2)
slant_h = float(np.linalg.norm(M_ApBp - M_AB))  # ≈ 2.088

# 公式数值
S1      = a1 ** 2
S2      = a2 ** 2
C1      = 4 * a1
C2      = 4 * a2
S_lat   = 0.5 * (C1 + C2) * slant_h
S_total = S1 + S2 + S_lat
volume  = (h / 3) * (S1 + S2 + np.sqrt(S1 * S2))


# ════════════════════════════════════════════════════════════
class FrustumLesson(ThreeDScene):
    """正四棱台教学动画 — 总时长约 75 秒"""

    # ═══════════════════════════════
    # CONSTRUCT
    # ═══════════════════════════════
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.78)

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_components()
        self.scene_4_properties()
        self.scene_5_volume()
        self.scene_6_surface()
        self.scene_7_outro()

    # ═══════════════════════════════
    # HELPERS
    # ═══════════════════════════════
    def _frustum(self, face_op=0.42, base_op=0.65, stroke_w=2.5):
        """构建棱台所有几何面 + 棱。返回 dict。"""
        A, B, C, D = A_pt, B_pt, C_pt, D_pt
        Ap, Bp, Cp, Dp = Ap_pt, Bp_pt, Cp_pt, Dp_pt

        bot = Polygon(A, B, C, D,
                      fill_color=BOT_COLOR, fill_opacity=base_op,
                      stroke_color=EDGE_COLOR, stroke_width=stroke_w)
        top = Polygon(Ap, Bp, Cp, Dp,
                      fill_color=TOP_COLOR, fill_opacity=base_op,
                      stroke_color=EDGE_COLOR, stroke_width=stroke_w)

        face_specs = [
            (A,  B,  Bp, Ap, FACE1_COLOR),   # front
            (B,  C,  Cp, Bp, FACE2_COLOR),   # right
            (C,  D,  Dp, Cp, FACE3_COLOR),   # back
            (D,  A,  Ap, Dp, FACE4_COLOR),   # left
        ]
        faces = [
            Polygon(p1, p2, p3, p4,
                    fill_color=col, fill_opacity=face_op,
                    stroke_color=EDGE_COLOR, stroke_width=stroke_w)
            for p1, p2, p3, p4, col in face_specs
        ]

        bot_edges = VGroup(
            Line(A, B, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(B, C, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(C, D, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(D, A, stroke_color=EDGE_COLOR, stroke_width=3),
        )
        top_edges = VGroup(
            Line(Ap, Bp, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(Bp, Cp, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(Cp, Dp, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(Dp, Ap, stroke_color=EDGE_COLOR, stroke_width=3),
        )
        lat_edges = VGroup(
            Line(A, Ap, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(B, Bp, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(C, Cp, stroke_color=EDGE_COLOR, stroke_width=3),
            Line(D, Dp, stroke_color=EDGE_COLOR, stroke_width=3),
        )

        return dict(
            bot=bot, top=top, faces=faces, faces_group=VGroup(*faces),
            bot_edges=bot_edges, top_edges=top_edges, lat_edges=lat_edges,
            A=A, B=B, C=C, D=D,
            Ap=Ap_pt, Bp=Bp_pt, Cp=Cp_pt, Dp=Dp_pt,
        )

    def ft(self, txt, size=26, color=WHITE):
        return Text(txt, font="Noto Sans CJK SC", font_size=size, color=color)

    def add_ft(self, *mobs):
        self.add_fixed_in_frame_mobjects(*mobs)

    def rm_ft(self, *mobs, rt=0.45):
        self.play(*[FadeOut(m) for m in mobs], run_time=rt)
        for m in mobs:
            self.remove(m)

    # ═══════════════════════════════
    # SCENE 1 — Opening Hook  (≈6 s)
    # ═══════════════════════════════
    def scene_1_opening(self):
        # Author watermark
        wm = self.ft("上海初高中数学直通车 @emptyandcalm", size=18, color=AUTHOR_COLOR)
        wm.move_to(UP * 7.2)
        self.add_ft(wm)
        self.play(FadeIn(wm, shift=DOWN * 0.1), run_time=0.3)

        # Hook headline
        hook = self.ft("你见过被截断的棱锥吗？", size=42, color=ACCENT)
        hook.move_to(UP * 6.0)
        self.add_ft(hook)
        self.play(Write(hook), run_time=0.8)

        sub = self.ft("今天搞定 棱台！", size=36, color=WHITE)
        sub.move_to(UP * 5.0)
        self.add_ft(sub)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # Build frustum progressively
        F = self._frustum()
        self._F = F

        self.play(DrawBorderThenFill(F["bot"]), Create(F["bot_edges"]), run_time=0.7)
        self.play(Create(F["lat_edges"]), run_time=0.5)
        self.play(
            DrawBorderThenFill(F["top"]), Create(F["top_edges"]), run_time=0.5
        )
        self.play(
            *[DrawBorderThenFill(face) for face in F["faces"]], run_time=0.8
        )

        # Dramatic camera sweep
        self.move_camera(theta=-100 * DEGREES, run_time=1.2, rate_func=smooth)
        self.move_camera(theta=-45  * DEGREES, run_time=0.9, rate_func=smooth)
        self.wait(0.3)

        self.rm_ft(hook, sub, rt=0.4)

    # ═══════════════════════════════
    # SCENE 2 — Definition  (≈11 s)
    # ═══════════════════════════════
    def scene_2_definition(self):
        F = self._F

        title = self.ft("棱台的定义", size=44, color=ACCENT).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # ── Step 1: Show the original full pyramid (phantom) ──
        info1 = self.ft("从一个棱锥出发……", size=30, color=PHANTOM_COL).move_to(UP * 5.5)
        self.add_ft(info1)
        self.play(FadeIn(info1, shift=UP * 0.2), run_time=0.4)

        # Phantom lateral edges from bottom to apex
        phantom_edges = VGroup(
            DashedLine(A_pt, APEX, color=PHANTOM_COL, stroke_width=2, dash_length=0.12),
            DashedLine(B_pt, APEX, color=PHANTOM_COL, stroke_width=2, dash_length=0.12),
            DashedLine(C_pt, APEX, color=PHANTOM_COL, stroke_width=2, dash_length=0.12),
            DashedLine(D_pt, APEX, color=PHANTOM_COL, stroke_width=2, dash_length=0.12),
        )
        apex_dot = Dot3D(APEX, radius=0.08, color=PHANTOM_COL)
        self.play(Create(phantom_edges), FadeIn(apex_dot), run_time=0.8)
        self.wait(0.5)

        # ── Step 2: Cutting plane descends ──
        self.rm_ft(info1, rt=0.3)
        info2 = self.ft("用平行于底面的平面来截……", size=28, color=ACCENT).move_to(UP * 5.5)
        self.add_ft(info2)
        self.play(FadeIn(info2), run_time=0.4)

        # Cutting plane: a square slightly larger than the top base
        cut_size = s1 * 1.6
        cut_plane = Polygon(
            [-cut_size, -cut_size, h],
            [ cut_size, -cut_size, h],
            [ cut_size,  cut_size, h],
            [-cut_size,  cut_size, h],
            fill_color=YELLOW, fill_opacity=0.35,
            stroke_color=YELLOW, stroke_width=3
        )
        self.play(FadeIn(cut_plane, shift=DOWN * 0.3), run_time=0.8)
        self.wait(0.7)

        # ── Step 3: Fade out top + cutting plane + phantom ──
        self.rm_ft(info2, rt=0.3)
        info3 = self.ft("截面以上的部分去掉……", size=28, color=WHITE).move_to(UP * 5.5)
        self.add_ft(info3)
        self.play(FadeIn(info3), run_time=0.3)

        # Phantom top pyramid (from apex down to cut)
        top_pyr_edges = VGroup(
            Line(APEX, Ap_pt, stroke_color=PHANTOM_COL, stroke_width=2),
            Line(APEX, Bp_pt, stroke_color=PHANTOM_COL, stroke_width=2),
            Line(APEX, Cp_pt, stroke_color=PHANTOM_COL, stroke_width=2),
            Line(APEX, Dp_pt, stroke_color=PHANTOM_COL, stroke_width=2),
        )
        top_pyr_base = Polygon(
            Ap_pt, Bp_pt, Cp_pt, Dp_pt,
            fill_color=PHANTOM_COL, fill_opacity=0.5,
            stroke_color=PHANTOM_COL, stroke_width=2
        )
        self.play(Create(top_pyr_edges), DrawBorderThenFill(top_pyr_base), run_time=0.6)
        self.wait(0.4)
        self.play(
            FadeOut(top_pyr_edges),
            FadeOut(top_pyr_base),
            FadeOut(apex_dot),
            FadeOut(phantom_edges),
            FadeOut(cut_plane),
            run_time=0.8
        )

        # ── Step 4: Definition card ──
        self.rm_ft(info3, rt=0.3)
        d1 = self.ft("棱台 = 棱锥被截面截断后", size=26, color=WHITE).move_to(UP * 5.4)
        d2 = self.ft("底部剩余的几何体", size=26, color=ACCENT).move_to(UP * 4.7)
        d3 = self.ft("两个平行底面  +  梯形侧面", size=24, color=GRAY_A).move_to(UP * 3.9)
        self.add_ft(d1, d2, d3)
        self.play(FadeIn(d1, shift=UP*0.15), run_time=0.4)
        self.play(FadeIn(d2, shift=UP*0.15), run_time=0.4)
        self.play(FadeIn(d3, shift=UP*0.15), run_time=0.4)
        self.wait(1.0)

        self.rm_ft(title, d1, d2, d3, rt=0.4)

    # ═══════════════════════════════
    # SCENE 3 — Components  (≈14 s)
    # ═══════════════════════════════
    def scene_3_components(self):
        F = self._F

        title = self.ft("各部分名称", size=44, color=ACCENT).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.4)

        # ─── (a) 下底面 ────────────────────────────────
        info = self.ft("ABCD  ——  下底面（较大）", size=28, color=BOT_COLOR).move_to(UP * 5.5)
        self.add_ft(info)
        self.play(
            F["bot"].animate.set_stroke(YELLOW, 5).set_fill(BOT_COLOR, 0.9),
            Write(info), run_time=0.6
        )
        self.wait(0.8)
        self.play(F["bot"].animate.set_stroke(EDGE_COLOR, 2.5).set_fill(BOT_COLOR, 0.65), run_time=0.3)
        self.rm_ft(info, rt=0.3)

        # ─── (b) 上底面 ────────────────────────────────
        info = self.ft("A'B'C'D'  ——  上底面（较小）", size=28, color=TOP_COLOR).move_to(UP * 5.5)
        self.add_ft(info)
        self.play(
            F["top"].animate.set_stroke(YELLOW, 5).set_fill(TOP_COLOR, 0.9),
            Write(info), run_time=0.6
        )
        self.wait(0.8)
        self.play(F["top"].animate.set_stroke(EDGE_COLOR, 2.5).set_fill(TOP_COLOR, 0.65), run_time=0.3)
        self.rm_ft(info, rt=0.3)

        # ─── (c) 侧面（梯形）─────────────────────────
        face_front = F["faces"][0]   # ABB'A'
        info = self.ft("ABB'A'  ——  侧面（等腰梯形）", size=27, color=FACE1_COLOR).move_to(UP * 5.5)
        self.add_ft(info)
        self.play(
            face_front.animate.set_fill(FACE1_COLOR, 0.9).set_stroke(YELLOW, 5),
            Write(info), run_time=0.6
        )
        self.wait(0.8)
        self.play(face_front.animate.set_fill(FACE1_COLOR, 0.42).set_stroke(EDGE_COLOR, 2.5), run_time=0.3)
        self.rm_ft(info, rt=0.3)

        # ─── (d) 侧棱 AA' ──────────────────────────────
        edge_aa = Line(A_pt, Ap_pt, stroke_color=YELLOW, stroke_width=6)
        dot_a   = Dot3D(A_pt,  radius=0.09, color=YELLOW)
        dot_ap  = Dot3D(Ap_pt, radius=0.09, color=YELLOW)
        info = self.ft("AA'  ——  侧棱（斜向连接两底）", size=27, color=YELLOW).move_to(UP * 5.5)
        self.add_ft(info)
        self.play(Create(edge_aa), FadeIn(dot_a, dot_ap), Write(info), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(edge_aa), FadeOut(dot_a), FadeOut(dot_ap), run_time=0.3)
        self.rm_ft(info, rt=0.3)

        # ─── (e) 高 h ─────────────────────────────────
        O_bot = np.array([0, 0, 0])
        O_top = np.array([0, 0, h])
        h_line = DashedLine(O_bot, O_top, color=HEIGHT_COLOR, stroke_width=5, dash_length=0.14)

        # Right-angle mark at O_bot
        sz = 0.2
        ra = Polygon(
            O_bot,
            O_bot + np.array([sz, 0, 0]),
            O_bot + np.array([sz, 0, sz]),
            O_bot + np.array([0,  0, sz]),
            stroke_color=HEIGHT_COLOR, stroke_width=2, fill_opacity=0
        )
        info = self.ft("h  ——  棱台的高（垂直两底面）", size=27, color=HEIGHT_COLOR).move_to(UP * 5.5)
        h_label = MathTex(r"h \perp \text{base}", font_size=30, color=HEIGHT_COLOR).move_to(UP * 4.7)
        self.add_ft(info, h_label)
        self.play(Create(h_line), FadeIn(ra), Write(info), run_time=0.7)
        self.play(Write(h_label), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(h_line), FadeOut(ra), run_time=0.3)
        self.rm_ft(info, h_label, rt=0.3)

        # ─── (f) 斜高 l' ──────────────────────────────
        sl_line  = Line(M_AB, M_ApBp, stroke_color=SLANT_COLOR, stroke_width=5)
        dot_mab  = Dot3D(M_AB,   radius=0.07, color=SLANT_COLOR)
        dot_mapbp = Dot3D(M_ApBp, radius=0.07, color=SLANT_COLOR)

        info = self.ft("l'  ——  斜高（两底边中点连线）", size=27, color=SLANT_COLOR).move_to(UP * 5.5)
        sl_tex = MathTex(
            r"l' = \sqrt{h^2 + \left(\frac{a_2 - a_1}{2}\right)^2}",
            font_size=28, color=SLANT_COLOR
        ).move_to(UP * 4.6)
        self.add_ft(info, sl_tex)
        self.play(Create(sl_line), FadeIn(dot_mab, dot_mapbp), Write(info), run_time=0.7)
        self.play(Write(sl_tex), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(sl_line), FadeOut(dot_mab), FadeOut(dot_mapbp), run_time=0.3)
        self.rm_ft(info, sl_tex, rt=0.3)

        self.rm_ft(title, rt=0.4)

    # ═══════════════════════════════
    # SCENE 4 — Properties  (≈8 s)
    # ═══════════════════════════════
    def scene_4_properties(self):
        F = self._F

        title = self.ft("正棱台的性质", size=44, color=ACCENT).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        props = [
            ("① 两底面是相似的正多边形", BOT_COLOR,   UP * 5.6),
            ("② 侧面是全等的等腰梯形",   FACE1_COLOR, UP * 4.7),
            ("③ 侧棱长度相等",            YELLOW,      UP * 3.8),
        ]
        prop_mobs = []
        for txt, col, pos in props:
            m = self.ft(txt, size=28, color=col).move_to(pos)
            self.add_ft(m)
            self.play(FadeIn(m, shift=RIGHT * 0.25), run_time=0.45)
            prop_mobs.append(m)
            self.wait(0.35)

        # ① Highlight both bases simultaneously
        self.play(
            F["bot"].animate.set_stroke(YELLOW, 5).set_fill(BOT_COLOR, 0.9),
            F["top"].animate.set_stroke(YELLOW, 5).set_fill(TOP_COLOR, 0.9),
            run_time=0.5
        )
        self.wait(0.4)
        self.play(
            F["bot"].animate.set_stroke(EDGE_COLOR, 2.5).set_fill(BOT_COLOR, 0.65),
            F["top"].animate.set_stroke(EDGE_COLOR, 2.5).set_fill(TOP_COLOR, 0.65),
            run_time=0.3
        )

        # ② Highlight all four side faces
        self.play(
            *[f.animate.set_fill(f.get_fill_color(), 0.9).set_stroke(YELLOW, 4)
              for f in F["faces"]],
            run_time=0.5
        )
        self.wait(0.4)
        self.play(
            *[f.animate.set_fill(f.get_fill_color(), 0.42).set_stroke(EDGE_COLOR, 2.5)
              for f in F["faces"]],
            run_time=0.3
        )

        # ③ Highlight all lateral edges
        lat_hl = VGroup(
            Line(A_pt, Ap_pt, stroke_color=YELLOW, stroke_width=6),
            Line(B_pt, Bp_pt, stroke_color=YELLOW, stroke_width=6),
            Line(C_pt, Cp_pt, stroke_color=YELLOW, stroke_width=6),
            Line(D_pt, Dp_pt, stroke_color=YELLOW, stroke_width=6),
        )
        self.play(Create(lat_hl), run_time=0.5)

        # Slow rotation to show symmetry
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(lat_hl), run_time=0.4)
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=0.8)
        self.rm_ft(title, *prop_mobs, rt=0.4)

    # ═══════════════════════════════
    # SCENE 5 — Volume  (≈15 s)
    # ═══════════════════════════════
    def scene_5_volume(self):
        F = self._F

        title = self.ft("体积公式推导", size=44, color=ACCENT).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.5)

        # ── Step 1: Show big pyramid (phantom) ──────────────
        idea = self.ft("棱台 = 大棱锥  −  小棱锥", size=30, color=WHITE).move_to(UP * 5.7)
        self.add_ft(idea)
        self.play(FadeIn(idea, shift=UP * 0.2), run_time=0.5)

        big_pyr_lat = VGroup(
            DashedLine(A_pt, APEX, color=PHANTOM_COL, stroke_width=2.5, dash_length=0.12),
            DashedLine(B_pt, APEX, color=PHANTOM_COL, stroke_width=2.5, dash_length=0.12),
            DashedLine(C_pt, APEX, color=PHANTOM_COL, stroke_width=2.5, dash_length=0.12),
            DashedLine(D_pt, APEX, color=PHANTOM_COL, stroke_width=2.5, dash_length=0.12),
        )
        apex_dot = Dot3D(APEX, radius=0.08, color=PHANTOM_COL)
        self.play(Create(big_pyr_lat), FadeIn(apex_dot), run_time=0.7)

        # Small pyramid on top (solid)
        small_lat = VGroup(
            Line(Ap_pt, APEX, stroke_color=YELLOW, stroke_width=3),
            Line(Bp_pt, APEX, stroke_color=YELLOW, stroke_width=3),
            Line(Cp_pt, APEX, stroke_color=YELLOW, stroke_width=3),
            Line(Dp_pt, APEX, stroke_color=YELLOW, stroke_width=3),
        )
        small_base = Polygon(
            Ap_pt, Bp_pt, Cp_pt, Dp_pt,
            fill_color=YELLOW, fill_opacity=0.5,
            stroke_color=YELLOW, stroke_width=2
        )
        self.play(Create(small_lat), DrawBorderThenFill(small_base), run_time=0.7)
        self.wait(0.5)

        # ── Step 2: Height labeling ─────────────────────────
        # h_pyr line
        h_big_line = DashedLine(
            np.array([0, 0, 0]), APEX,
            color=HEIGHT_COLOR, stroke_width=3, dash_length=0.14
        )
        self.play(Create(h_big_line), run_time=0.4)

        # Brace labels via fixed-frame text
        V_big_tex = MathTex(
            rf"V_{{大}} = \frac{{1}}{{3}} \cdot {S2:.2f} \times {h_pyr:.1f} = {(S2*h_pyr/3):.2f}",
            font_size=28, color=PHANTOM_COL
        ).move_to(UP * 4.9)
        self.add_ft(V_big_tex)
        self.play(Write(V_big_tex), run_time=0.7)
        self.wait(0.4)

        V_small_tex = MathTex(
            rf"V_{{小}} = \frac{{1}}{{3}} \cdot {S1:.2f} \times {h_pyr - h:.1f} = {(S1*(h_pyr-h)/3):.2f}",
            font_size=28, color=YELLOW
        ).move_to(UP * 4.1)
        self.add_ft(V_small_tex)
        self.play(Write(V_small_tex), run_time=0.7)
        self.wait(0.5)

        # ── Step 3: Fade phantom, show derivation ───────────
        self.play(
            FadeOut(big_pyr_lat), FadeOut(apex_dot),
            FadeOut(small_lat), FadeOut(small_base),
            FadeOut(h_big_line),
            run_time=0.5
        )

        V_diff = MathTex(
            r"V = V_{大} - V_{小}",
            font_size=36, color=WHITE
        ).move_to(UP * 3.3)
        self.add_ft(V_diff)
        self.play(Write(V_diff), run_time=0.5)
        self.wait(0.4)

        # ── Step 4: Final clean formula ─────────────────────
        form_final = MathTex(
            r"V = \frac{h}{3}\left(S_{\text{上}} + S_{\text{下}} + \sqrt{S_{\text{上}} \cdot S_{\text{下}}}\right)",
            font_size=32, color=ACCENT
        ).move_to(UP * 2.4)
        box = SurroundingRectangle(form_final, color=ACCENT, buff=0.18, corner_radius=0.12)
        self.add_ft(form_final, box)
        self.play(Write(form_final), Create(box), run_time=1.2)
        self.play(Indicate(form_final, scale_factor=1.08, color=YELLOW), run_time=0.6)
        self.wait(0.5)

        # ── Step 5: Substitute numbers ──────────────────────
        num_tex = MathTex(
            rf"V = \frac{{{h:.1f}}}{{3}} \times ({S1:.2f} + {S2:.2f} + {np.sqrt(S1*S2):.2f})",
            font_size=30, color=WHITE
        ).move_to(UP * 1.4)
        self.add_ft(num_tex)
        self.play(Write(num_tex), run_time=0.8)

        result_v = MathTex(
            rf"V = {volume:.2f}",
            font_size=52, color=ACCENT
        ).move_to(UP * 0.5)
        self.add_ft(result_v)
        self.play(Write(result_v), run_time=0.6)
        self.play(Indicate(result_v, scale_factor=1.12), run_time=0.5)
        self.wait(0.8)

        self.rm_ft(title, idea, V_big_tex, V_small_tex, V_diff, form_final, box, num_tex, result_v, rt=0.5)

    # ═══════════════════════════════
    # SCENE 6 — Surface Area  (≈10 s)
    # ═══════════════════════════════
    def scene_6_surface(self):
        F = self._F

        title = self.ft("侧面积公式", size=44, color=ACCENT).move_to(UP * 6.5)
        self.add_ft(title)
        self.play(Write(title), run_time=0.4)

        # Highlight all trapezoidal faces
        for f in F["faces"]:
            f.set_fill(f.get_fill_color(), 0.80)
        self.wait(0.3)

        # Key idea: unfold one face
        key_idea = self.ft("每个侧面都是等腰梯形", size=28, color=WHITE).move_to(UP * 5.6)
        self.add_ft(key_idea)
        self.play(FadeIn(key_idea, shift=UP * 0.2), run_time=0.4)

        # Slant height line
        sl_line  = Line(M_AB, M_ApBp, stroke_color=SLANT_COLOR, stroke_width=6)
        dot_m1   = Dot3D(M_AB,   radius=0.08, color=SLANT_COLOR)
        dot_m2   = Dot3D(M_ApBp, radius=0.08, color=SLANT_COLOR)
        self.play(Create(sl_line), FadeIn(dot_m1, dot_m2), run_time=0.5)

        # Formula
        form = MathTex(
            r"S_{\text{侧}} = \frac{1}{2} (C_{\text{上}} + C_{\text{下}}) \cdot l'",
            font_size=38, color=SLANT_COLOR
        ).move_to(UP * 4.7)
        self.add_ft(form)
        self.play(Write(form), run_time=0.9)
        self.wait(0.5)

        note = self.ft("C上 = 上底周长    C下 = 下底周长    l' = 斜高", size=21, color=GRAY_A).move_to(UP * 3.9)
        self.add_ft(note)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.5)

        # Numbers
        c_sum = C1 + C2
        num_tex = MathTex(
            rf"S_{{侧}} = \frac{{1}}{{2}} \times ({C1:.1f} + {C2:.1f}) \times {slant_h:.3f}",
            font_size=30, color=WHITE
        ).move_to(UP * 3.1)
        self.add_ft(num_tex)
        self.play(Write(num_tex), run_time=0.7)

        result_s = MathTex(
            rf"S_{{侧}} \approx {S_lat:.2f}",
            font_size=50, color=ACCENT
        ).move_to(UP * 2.1)
        self.add_ft(result_s)
        self.play(Write(result_s), run_time=0.5)
        self.play(Indicate(result_s, scale_factor=1.12), run_time=0.5)

        # Total
        total_txt = self.ft(f"全面积 S = {S_total:.2f}", size=28, color=GRAY_A).move_to(UP * 1.2)
        self.add_ft(total_txt)
        self.play(FadeIn(total_txt), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(sl_line), FadeOut(dot_m1), FadeOut(dot_m2), run_time=0.3)
        for f in F["faces"]:
            f.set_fill(f.get_fill_color(), 0.42)
        self.rm_ft(title, key_idea, form, note, num_tex, result_s, total_txt, rt=0.5)

    # ═══════════════════════════════
    # SCENE 7 — Recap + Outro  (≈8 s)
    # ═══════════════════════════════
    def scene_7_outro(self):
        F = self._F

        # ── Formula recap card ──────────────────────────────
        recap = self.ft("公式速记", size=42, color=ACCENT).move_to(UP * 6.5)
        fv = MathTex(
            r"V = \frac{h}{3}\!\left(S_1 + S_2 + \sqrt{S_1 S_2}\right)",
            font_size=34, color=HEIGHT_COLOR
        ).move_to(UP * 5.5)
        fs = MathTex(
            r"S_{\text{侧}} = \tfrac{1}{2}(C_1 + C_2)\,l'",
            font_size=34, color=SLANT_COLOR
        ).move_to(UP * 4.7)
        fl = MathTex(
            r"l' = \sqrt{h^2 + \left(\tfrac{a_2 - a_1}{2}\right)^2}",
            font_size=30, color=GRAY_A
        ).move_to(UP * 3.9)
        note_a = self.ft("a₁=上底边长，a₂=下底边长", size=20, color=GRAY_B).move_to(UP * 3.1)

        self.add_ft(recap, fv, fs, fl, note_a)
        self.play(Write(recap), run_time=0.4)
        for m in [fv, fs, fl, note_a]:
            self.play(Write(m) if isinstance(m, MathTex) else FadeIn(m, shift=UP*0.1),
                      run_time=0.5)

        # Ambient rotation while formulas are visible
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(2.8)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=70 * DEGREES, theta=-45 * DEGREES, run_time=0.8)

        # ── Fade out everything ─────────────────────────────
        F_all = VGroup(
            F["bot"], F["top"], F["faces_group"],
            F["bot_edges"], F["top_edges"], F["lat_edges"]
        )
        self.play(
            FadeOut(F_all),
            FadeOut(recap), FadeOut(fv), FadeOut(fs), FadeOut(fl), FadeOut(note_a),
            run_time=0.7
        )
        for m in [recap, fv, fs, fl, note_a]:
            self.remove(m)

        # ── Outro card ──────────────────────────────────────
        auth_big = self.ft("上海初高中数学直通车", size=42, color=WHITE).move_to(UP * 2.0)
        auth_id  = self.ft("@emptyandcalm",  size=30, color=GRAY_B).move_to(UP * 0.9)
        follow   = self.ft("关注我，获得更多数学技巧！", size=30, color=ACCENT).move_to(DOWN * 0.3)

        self.add_ft(auth_big, auth_id, follow)
        self.play(FadeIn(auth_big, scale=1.05), FadeIn(auth_id, shift=UP*0.2), run_time=0.8)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # Small decorative frustum
        mini_F = self._frustum(face_op=0.65, base_op=0.80)
        mini_all = VGroup(
            mini_F["bot"], mini_F["top"], mini_F["faces_group"],
            mini_F["bot_edges"], mini_F["top_edges"], mini_F["lat_edges"]
        ).scale(0.32).move_to(np.array([0, -3.0, 0]))
        self.play(
            DrawBorderThenFill(mini_F["bot"]),
            DrawBorderThenFill(mini_F["top"]),
            *[DrawBorderThenFill(f) for f in mini_F["faces"]],
            Create(mini_F["bot_edges"]),
            Create(mini_F["top_edges"]),
            Create(mini_F["lat_edges"]),
            run_time=1.0
        )

        self.begin_ambient_camera_rotation(rate=0.20)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()