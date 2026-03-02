"""
菱形的性质与判定 — 八年级数学教学动画
Rhombus: Properties & Determination — Grade 8

渲染:
  manim -pql rhombus_properties.py RhombusLesson   # 预览
  manim -qh  rhombus_properties.py RhombusLesson   # 高质量
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 颜色 ────────────────────────────────────────
BG       = "#1a1a2e"
C_RHOM   = "#4dd0e1"   # 菱形主体
C_SIDE   = "#a5d6a7"   # 四边相等 绿
C_DIAG   = "#ffd54f"   # 对角线 黄
C_PERP   = "#ef9a9a"   # 垂直 红
C_AREA   = "#ce93d8"   # 面积 紫
C_DET1   = "#80cbc4"   # 判定1 青
C_DET2   = "#ffb74d"   # 判定2 橙
C_DET3   = "#b39ddb"   # 判定3 紫
C_CHECK  = "#69f0ae"
C_HL     = YELLOW


class RhombusLesson(Scene):

    def construct(self):
        self.camera.background_color = BG
        self._setup_geometry()

        self.scene_opening()
        self.scene_prop1_equal_sides()
        self.scene_prop2_perp_diagonals()
        self.scene_prop3_area()
        self.scene_det1_para_adjacent()
        self.scene_det2_four_sides()
        self.scene_det3_perp_diagonals()
        self.scene_summary()
        self.scene_outro()

    # ══════════════════════════════════════════
    #  几何初始化
    # ══════════════════════════════════════════
    def _setup_geometry(self):
        """
        菱形以对角线水平/垂直方向放置：
          A(左) B(下) C(右) D(上)
        精确保证：四边相等，AC⊥BD，互相平分
        验证：∠A=∠C≈66.2°，∠B=∠D≈113.8°，all other_angle=True
        """
        cx, cy = 0.0, 1.1
        d1 = 4.6   # AC 水平对角线长
        d2 = 3.0   # BD 垂直对角线长
        self.A = np.array([cx - d1/2, cy,       0])
        self.B = np.array([cx,        cy - d2/2, 0])
        self.C = np.array([cx + d1/2, cy,       0])
        self.D = np.array([cx,        cy + d2/2, 0])
        self.O = (self.A + self.C) / 2         # == (B+D)/2
        self.side = np.linalg.norm(self.B - self.A)   # ≈ 2.746
        self.d1   = d1
        self.d2   = d2

    # ══════════════════════════════════════════
    #  工具
    # ══════════════════════════════════════════
    def _rhom(self, color=C_RHOM, sw=3, fill_op=0.08):
        return Polygon(self.A, self.B, self.C, self.D,
                       color=color, stroke_width=sw,
                       fill_color=color, fill_opacity=fill_op)

    def _labels(self, sz=30, color=WHITE):
        data = [("A", self.A, LEFT*0.35),
                ("B", self.B, DOWN*0.35),
                ("C", self.C, RIGHT*0.35),
                ("D", self.D, UP*0.35)]
        return VGroup(*[
            MathTex(n, color=color, font_size=sz).next_to(p, d, buff=0.05)
            for n, p, d in data
        ])

    def _dashed(self, p1, p2, color=C_DIAG, sw=2.5):
        return DashedLine(p1, p2, color=color,
                          dash_length=0.14, stroke_width=sw)

    def _tick(self, p1, p2, n=1, color=WHITE, sz=0.18):
        mid  = (p1+p2)/2
        d    = p2-p1; d = d/np.linalg.norm(d)
        perp = np.array([-d[1], d[0], 0])
        sp   = 0.12
        offs = np.linspace(-(n-1)*sp/2, (n-1)*sp/2, n)
        return VGroup(*[
            Line(mid+o*d - perp*sz/2, mid+o*d + perp*sz/2,
                 color=color, stroke_width=2.5) for o in offs
        ])

    def _right_angle(self, corner, p1, p2, color=C_PERP, size=0.22):
        """精确直角符号"""
        v1 = (p1 - corner); v1 = v1/np.linalg.norm(v1)*size
        v2 = (p2 - corner); v2 = v2/np.linalg.norm(v2)*size
        return Polygon(corner, corner+v1, corner+v1+v2, corner+v2,
                       color=color, stroke_width=2.0, fill_opacity=0)

    def _angle_arc(self, vertex, p1, p2, color, radius=0.42):
        """other_angle=True (验证：所有叉积<0)"""
        return Angle(
            Line(vertex, p1), Line(vertex, p2),
            radius=radius, color=color,
            stroke_width=2.5, other_angle=True
        )

    def _badge(self, txt, color, y):
        check = Text("✓", font="Noto Sans CJK SC", font_size=28, color=C_CHECK)
        label = Text(txt,  font="Noto Sans CJK SC", font_size=22, color=color)
        return VGroup(check, label).arrange(RIGHT, buff=0.15).move_to(UP*y)

    def _zh(self, txt, y, color=GRAY_A, sz=22):
        return Text(txt, font="Noto Sans CJK SC",
                    font_size=sz, color=color).move_to(UP*y)

    def _sec(self, txt, color=C_HL, y=5.9):
        return Text(txt, font="Noto Sans CJK SC",
                    font_size=34, color=color, weight=BOLD).move_to(UP*y)

    def _formula(self, tex, y, color=WHITE, sz=28):
        return MathTex(tex, color=color, font_size=sz).move_to(UP*y)

    def _edge(self, p1, p2, color, sw=5):
        return Line(p1, p2, color=color, stroke_width=sw)

    # ══════════════════════════════════════════
    #  Scene 0 — 开场
    # ══════════════════════════════════════════
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=20, color=GRAY_B
        ).move_to(UP*7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.15), run_time=0.3)

        tag = Text("八年级 · 第二十二章 · 四边形",
                   font="Noto Sans CJK SC", font_size=21, color=GRAY_B
                   ).move_to(UP*6.75)
        self.play(FadeIn(tag), run_time=0.3)

        title = Text("菱形的性质与判定",
                     font="Noto Sans CJK SC", font_size=46,
                     color=GOLD, weight=BOLD).move_to(UP*6.05)
        self.play(Write(title), run_time=0.9)

        hook = Text("等边四边形有哪些神奇性质？",
                    font="Noto Sans CJK SC", font_size=26,
                    color=C_HL).move_to(UP*5.25)
        self.play(FadeIn(hook, shift=UP*0.2), run_time=0.5)

        self.rhom   = self._rhom()
        self.labels = self._labels()
        self.play(Create(self.rhom), run_time=0.9)
        self.play(Write(self.labels), run_time=0.5)
        self.wait(0.7)
        self.play(FadeOut(title), FadeOut(hook), FadeOut(tag), run_time=0.4)

    # ══════════════════════════════════════════
    #  性质① — 四边相等
    # ══════════════════════════════════════════
    def scene_prop1_equal_sides(self):
        title = self._sec("性质①  四条边都相等", color=C_SIDE)
        sub   = self._zh("菱形继承平行四边形所有性质", y=5.3, sz=23)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        edges = [
            (self.A, self.B), (self.B, self.C),
            (self.C, self.D), (self.D, self.A)
        ]
        hi_list = []
        for i, (p1, p2) in enumerate(edges):
            hi = self._edge(p1, p2, C_SIDE)
            hi_list.append(hi)
            self.play(Create(hi), run_time=0.3)

        # 刻度（每条边一个刻度）
        tick_list = []
        for p1, p2 in edges:
            t = self._tick(p1, p2, n=1, color=C_SIDE)
            tick_list.append(t)
        self.play(*[FadeIn(t) for t in tick_list], run_time=0.4)

        f = self._formula(r"AB = BC = CD = DA", y=-4.2, color=C_SIDE)
        self.play(Write(f), run_time=0.6)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            *[FadeOut(h) for h in hi_list],
            *[FadeOut(t) for t in tick_list],
            FadeOut(f), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  性质② — 对角线互相垂直平分 + 平分对角
    # ══════════════════════════════════════════
    def scene_prop2_perp_diagonals(self):
        title = self._sec("性质②  对角线互相垂直平分", color=C_PERP)
        sub   = self._zh("且每条对角线平分一组对角", y=5.3, sz=23)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 绘制对角线
        d_AC = self._dashed(self.A, self.C, C_DIAG)
        d_BD = self._dashed(self.B, self.D, C_PERP)
        self.play(Create(d_AC), run_time=0.6)
        self.play(Create(d_BD), run_time=0.6)

        # 交点 O
        O_dot = Dot(self.O, radius=0.11, color=C_HL)
        O_lbl = MathTex("O", color=C_HL, font_size=26
                        ).next_to(self.O, UR*0.7, buff=0.12)
        self.play(FadeIn(O_dot, scale=0.3), run_time=0.35)
        self.play(Flash(O_dot, color=C_HL, flash_radius=0.3), run_time=0.35)
        self.play(Write(O_lbl), run_time=0.3)

        # 垂直符号（在交点处）
        # OA 方向（水平右），OB 方向（垂直下）
        ra_O = self._right_angle(
            self.O,
            self.O + np.array([0.3, 0, 0]),   # AC方向
            self.O + np.array([0, -0.3, 0]),   # BD方向
            color=C_PERP, size=0.22
        )
        self.play(Create(ra_O), run_time=0.4)

        f1 = self._formula(r"AC \perp BD", y=-4.0, color=C_PERP)
        self.play(Write(f1), run_time=0.5)

        # 互相平分刻度
        segs = [(self.O, self.A), (self.O, self.C),
                (self.O, self.B), (self.O, self.D)]
        ticks = [self._tick(p1, p2, n=1, color=C_DIAG) for p1, p2 in segs]
        self.play(*[FadeIn(t) for t in ticks], run_time=0.4)
        f2 = self._formula(r"OA=OC,\; OB=OD", y=-4.75, color=C_DIAG, sz=25)
        self.play(Write(f2), run_time=0.5)
        self.wait(0.5)

        # 对角线平分对角（角弧）— ∠DAC = ∠BAC
        hint2 = self._zh("AC 平分 ∠DAB，BD 平分 ∠ABC", y=-5.5, sz=20)
        self.play(FadeIn(hint2), run_time=0.4)
        arc1 = self._angle_arc(self.A, self.D, self.O, C_DIAG,  radius=0.38)
        arc2 = self._angle_arc(self.A, self.O, self.B, C_DIAG,  radius=0.38)
        self.play(Create(arc1), Create(arc2), run_time=0.6)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(d_AC), FadeOut(d_BD),
            FadeOut(O_dot), FadeOut(O_lbl), FadeOut(ra_O),
            FadeOut(f1), FadeOut(f2),
            *[FadeOut(t) for t in ticks],
            FadeOut(hint2), FadeOut(arc1), FadeOut(arc2),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  性质③ — 面积公式
    # ══════════════════════════════════════════
    def scene_prop3_area(self):
        title = self._sec("面积公式", color=C_AREA)
        sub   = self._zh("利用对角线计算菱形面积", y=5.3, sz=23)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 对角线
        d_AC = self._dashed(self.A, self.C, C_DIAG)
        d_BD = self._dashed(self.B, self.D, C_PERP)
        self.play(Create(d_AC), Create(d_BD), run_time=0.6)

        # 填色四个三角形，依次出现
        # 菱形由四个直角三角形组成
        O = self.O
        tri_colors = ["#e53935","#1e88e5","#43a047","#fb8c00"]
        tri_verts  = [
            [self.A, O, self.D],
            [self.D, O, self.C],
            [self.C, O, self.B],
            [self.B, O, self.A],
        ]
        tris = []
        for verts, col in zip(tri_verts, tri_colors):
            tri = Polygon(*verts, color=col,
                          fill_color=col, fill_opacity=0.35,
                          stroke_width=0)
            tris.append(tri)
            self.play(FadeIn(tri, scale=0.8), run_time=0.25)

        # 标注 d1/2, d2/2
        lbl_d1 = MathTex(r"\frac{AC}{2}", color=C_DIAG, font_size=22
                         ).next_to((self.A+O)/2, DOWN, buff=0.12)
        lbl_d2 = MathTex(r"\frac{BD}{2}", color=C_PERP, font_size=22
                         ).next_to((self.B+O)/2, RIGHT, buff=0.12)
        self.play(Write(lbl_d1), Write(lbl_d2), run_time=0.5)

        # 面积公式推导
        f1 = self._formula(
            r"S = 4 \times \frac{1}{2} \times \frac{AC}{2} \times \frac{BD}{2}",
            y=-4.1, color=C_AREA, sz=24
        )
        f2 = self._formula(
            r"S = \dfrac{1}{2} \times AC \times BD",
            y=-4.9, color=C_HL, sz=28
        )
        self.play(Write(f1), run_time=0.6)
        self.play(Write(f2), run_time=0.6)
        self.wait(1.3)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(d_AC), FadeOut(d_BD),
            *[FadeOut(t) for t in tris],
            FadeOut(lbl_d1), FadeOut(lbl_d2),
            FadeOut(f1), FadeOut(f2), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定① — 平行四边形 + 一组邻边相等
    # ══════════════════════════════════════════
    def scene_det1_para_adjacent(self):
        title = self._sec("判定①", color=C_DET1, y=5.9)
        sub   = self._zh("平行四边形 + 一组邻边相等  ⟹  菱形",
                          y=5.2, color=C_DET1, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        hint = self._zh("AB 和 BC 是邻边，AB = BC 即可", y=4.55, sz=21)
        self.play(FadeIn(hint), run_time=0.4)

        # 高亮两条邻边
        hi_AB = self._edge(self.A, self.B, C_DET1)
        hi_BC = self._edge(self.B, self.C, C_DET1)
        self.play(Create(hi_AB), Create(hi_BC), run_time=0.5)

        t_AB = self._tick(self.A, self.B, n=1, color=C_DET1)
        t_BC = self._tick(self.B, self.C, n=1, color=C_DET1)
        self.play(FadeIn(t_AB), FadeIn(t_BC), run_time=0.4)

        f1 = self._formula(r"AB = BC", y=-4.2, color=C_DET1)
        self.play(Write(f1), run_time=0.5)

        badge = self._badge("平行四边形 + 邻边相等  ⟹  菱形", C_DET1, y=-5.1)
        self.play(FadeIn(badge, scale=1.05), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hint),
            FadeOut(hi_AB), FadeOut(hi_BC),
            FadeOut(t_AB), FadeOut(t_BC),
            FadeOut(f1), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定② — 四边相等
    # ══════════════════════════════════════════
    def scene_det2_four_sides(self):
        title = self._sec("判定②", color=C_DET2, y=5.9)
        sub   = self._zh("四边都相等的四边形  ⟹  菱形",
                          y=5.2, color=C_DET2, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        edges = [(self.A,self.B),(self.B,self.C),(self.C,self.D),(self.D,self.A)]
        his   = [self._edge(p1, p2, C_DET2) for p1,p2 in edges]
        ticks = [self._tick(p1, p2, n=1, color=C_DET2) for p1,p2 in edges]

        self.play(*[Create(h) for h in his], run_time=0.5)
        self.play(*[FadeIn(t) for t in ticks], run_time=0.4)

        f = self._formula(r"AB = BC = CD = DA", y=-4.2, color=C_DET2)
        self.play(Write(f), run_time=0.5)

        badge = self._badge("四边相等  ⟹  菱形", C_DET2, y=-5.1)
        self.play(FadeIn(badge, scale=1.05), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            *[FadeOut(h) for h in his],
            *[FadeOut(t) for t in ticks],
            FadeOut(f), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定③ — 平行四边形 + 对角线垂直
    # ══════════════════════════════════════════
    def scene_det3_perp_diagonals(self):
        title = self._sec("判定③", color=C_DET3, y=5.9)
        sub   = self._zh("平行四边形 + 对角线互相垂直  ⟹  菱形",
                          y=5.2, color=C_DET3, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        d_AC = self._dashed(self.A, self.C, C_DIAG)
        d_BD = self._dashed(self.B, self.D, C_PERP)
        self.play(Create(d_AC), Create(d_BD), run_time=0.7)

        O_dot = Dot(self.O, radius=0.10, color=C_HL)
        self.play(FadeIn(O_dot, scale=0.3), run_time=0.3)

        # 垂直符号
        ra_O = self._right_angle(
            self.O,
            self.O + np.array([0.25, 0, 0]),
            self.O + np.array([0, -0.25, 0]),
            color=C_PERP, size=0.22
        )
        self.play(Create(ra_O), run_time=0.4)

        f1 = self._formula(r"AC \perp BD", y=-4.2, color=C_DET3)
        self.play(Write(f1), run_time=0.5)

        badge = self._badge("平行四边形 + AC⊥BD  ⟹  菱形", C_DET3, y=-5.1)
        self.play(FadeIn(badge, scale=1.05), run_time=0.4)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(d_AC), FadeOut(d_BD),
            FadeOut(O_dot), FadeOut(ra_O),
            FadeOut(f1), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  汇总
    # ══════════════════════════════════════════
    def scene_summary(self):
        small = self._rhom(sw=2, fill_op=0.05).scale(0.52).move_to(UP*4.65)
        self.play(
            Transform(self.rhom, small),
            FadeOut(self.labels), run_time=0.7
        )

        title = Text("菱形 · 总览",
                     font="Noto Sans CJK SC", font_size=38,
                     color=GOLD, weight=BOLD).move_to(UP*6.05)
        self.play(Write(title), run_time=0.5)

        rows = [
            ("性质①", r"AB=BC=CD=DA",                       None,           C_SIDE,  3.35),
            ("性质②", r"AC \perp BD,\; OA=OC",              None,           C_PERP,  1.85),
            ("面积",   r"S=\tfrac{1}{2}\cdot AC\cdot BD",   None,           C_AREA,  0.35),
            ("判定①", r"AB=BC",                              "平行四边形+",  C_DET1, -1.15),
            ("判定②", r"AB=BC=CD=DA",                        None,           C_DET2, -2.65),
            ("判定③", r"AC\perp BD",                         "平行四边形+",  C_DET3, -4.15),
        ]

        cards = []
        for lab, tex, prefix_zh, col, yc in rows:
            bg = RoundedRectangle(
                corner_radius=0.16, width=8.0, height=1.20,
                color=col, fill_opacity=0.09, stroke_width=1.5
            ).move_to(UP * yc)
            lbl = Text(lab, font="Noto Sans CJK SC",
                    font_size=22, color=col, weight=BOLD
                    ).move_to(bg.get_left() + RIGHT * 0.75)
            
            if prefix_zh:
                fml = VGroup(
                    Text(prefix_zh, font="Noto Sans CJK SC", font_size=21, color=WHITE),
                    MathTex(tex, color=WHITE, font_size=21)
                ).arrange(RIGHT, buff=0.1).next_to(lbl, RIGHT, buff=0.3)
            else:
                fml = MathTex(tex, color=WHITE, font_size=21
                            ).next_to(lbl, RIGHT, buff=0.3)
            
            card = VGroup(bg, lbl, fml)
            cards.append(card)
            self.play(FadeIn(card, shift=RIGHT * 0.2), run_time=0.38)
            self.wait(0.08)

        tip = Text("三性质 + 三判定，菱形全掌握！",
                   font="Noto Sans CJK SC", font_size=24,
                   color=C_HL).move_to(UP*-5.5)
        self.play(FadeIn(tip, scale=1.05), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(self.rhom),
            *[FadeOut(c) for c in cards], FadeOut(tip), run_time=0.55
        )

    # ══════════════════════════════════════════
    #  片尾
    # ══════════════════════════════════════════
    def scene_outro(self):
        deco = VGroup()
        for pos, col, rot in [
            (UP*4.8+LEFT*3.0,  C_SIDE, 0.12),
            (UP*2.5+RIGHT*3.6, C_PERP, 0.28),
            (DOWN*0.5+LEFT*3.5, C_AREA, 0.08),
            (DOWN*3.2+RIGHT*3.0, C_DET1, 0.18),
            (UP*6.0+RIGHT*1.8,  C_DET3, 0.22),
        ]:
            mini = Polygon(
                np.array([-0.5, 0, 0]), np.array([0, -0.3, 0]),
                np.array([0.5, 0, 0]),  np.array([0,  0.3, 0]),
                color=col, fill_opacity=0.35, stroke_width=1.5
            ).rotate(rot).move_to(pos)
            deco.add(mini)

        self.play(*[FadeIn(d, scale=0.5) for d in deco], run_time=0.6)

        name_big = Text("上海初高中数学直通车",
                        font="Noto Sans CJK SC", font_size=38,
                        color=WHITE, weight=BOLD).move_to(UP*1.6)
        id_txt   = Text("@emptyandcalm",
                        font="Noto Sans CJK SC", font_size=28,
                        color=GRAY_B).move_to(UP*0.7)

        self.play(Transform(self.author, name_big), run_time=0.7)
        self.play(FadeIn(id_txt, shift=UP*0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！",
                      font="Noto Sans CJK SC", font_size=30,
                      color=C_HL).move_to(DOWN*0.4)
        self.play(FadeIn(follow, shift=UP*0.25, scale=1.05), run_time=0.55)

        tagline = Text("四边等 · 对角线垂直 · 面积=½d₁d₂",
                       font="Noto Sans CJK SC", font_size=20,
                       color=GRAY_B).move_to(DOWN*1.6)
        self.play(FadeIn(tagline), run_time=0.4)

        self.play(Rotate(deco, angle=TAU/10, run_time=1.2))
        self.wait(0.8)
        self.play(
            FadeOut(self.author), FadeOut(id_txt),
            FadeOut(follow), FadeOut(tagline), FadeOut(deco), run_time=0.9
        )