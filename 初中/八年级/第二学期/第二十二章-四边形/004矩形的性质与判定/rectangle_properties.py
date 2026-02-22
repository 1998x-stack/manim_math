"""
矩形的性质与判定 — 八年级数学教学动画
Rectangle: Properties & Determination — Grade 8

渲染:
  manim -pql rectangle_properties.py RectangleLesson   # 预览
  manim -qh  rectangle_properties.py RectangleLesson   # 高质量
"""

from manim import *
import numpy as np

config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 颜色 ────────────────────────────────────────
BG        = "#1a1a2e"
C_RECT    = "#4fc3f7"   # 矩形主体蓝
C_ANGLE   = "#80cbc4"   # 直角标记青
C_DIAG_A  = "#ef9a9a"   # 对角线AC 红
C_DIAG_B  = "#ce93d8"   # 对角线BD 紫
C_EQUAL   = "#ffd54f"   # 相等标记黄
C_DET1    = "#a5d6a7"   # 判定1绿
C_DET2    = "#ffb74d"   # 判定2橙
C_DET3    = "#80deea"   # 判定3青
C_CHECK   = "#69f0ae"
C_HL      = YELLOW


class RectangleLesson(Scene):

    def construct(self):
        self.camera.background_color = BG
        self._setup_geometry()

        self.scene_opening()
        self.scene_prop1_right_angles()
        self.scene_prop2_equal_diagonals()
        self.scene_det1_parallelogram_plus_angle()
        self.scene_det2_three_right_angles()
        self.scene_det3_equal_diagonals()
        self.scene_summary()
        self.scene_outro()

    # ══════════════════════════════════════════
    #  几何初始化
    # ══════════════════════════════════════════
    def _setup_geometry(self):
        cx, cy = 0.0, 1.1
        w, h   = 4.2, 2.6
        self.A = np.array([cx - w/2, cy - h/2, 0])
        self.B = np.array([cx + w/2, cy - h/2, 0])
        self.C = np.array([cx + w/2, cy + h/2, 0])
        self.D = np.array([cx - w/2, cy + h/2, 0])
        self.O = (self.A + self.C) / 2          # 对角线交点
        self.diag_len = np.linalg.norm(self.C - self.A)   # ≈ 4.94

    # ══════════════════════════════════════════
    #  工具
    # ══════════════════════════════════════════
    def _rect(self, color=C_RECT, sw=3, fill_op=0.08):
        return Polygon(self.A, self.B, self.C, self.D,
                       color=color, stroke_width=sw,
                       fill_color=color, fill_opacity=fill_op)

    def _labels(self, sz=30, color=WHITE):
        data = [("A", self.A, DL), ("B", self.B, DR),
                ("C", self.C, UR), ("D", self.D, UL)]
        return VGroup(*[
            MathTex(n, color=color, font_size=sz).next_to(p, d, buff=0.1)
            for n, p, d in data
        ])

    def _right_angle(self, corner, p1, p2, color=C_ANGLE, size=0.28):
        """精确直角符号：corner 是直角顶点，p1/p2 是两条边上的点"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        sq = Polygon(corner, corner+v1, corner+v1+v2, corner+v2,
                     color=color, stroke_width=2.0, fill_opacity=0)
        return sq

    def _dashed(self, p1, p2, color, sw=2.5):
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

        title = Text("矩形的性质与判定",
                     font="Noto Sans CJK SC", font_size=46,
                     color=GOLD, weight=BOLD).move_to(UP*6.05)
        self.play(Write(title), run_time=0.9)

        hook = Text("直角四边形的独家秘籍！",
                    font="Noto Sans CJK SC", font_size=27,
                    color=C_HL).move_to(UP*5.25)
        self.play(FadeIn(hook, shift=UP*0.2), run_time=0.5)

        self.rect   = self._rect()
        self.labels = self._labels()
        self.play(Create(self.rect), run_time=0.9)
        self.play(Write(self.labels), run_time=0.5)
        self.wait(0.7)

        self.play(FadeOut(title), FadeOut(hook), FadeOut(tag), run_time=0.4)

    # ══════════════════════════════════════════
    #  性质① — 四个直角
    # ══════════════════════════════════════════
    def scene_prop1_right_angles(self):
        title = self._sec("性质①  四个角都是直角", color=C_ANGLE)
        sub   = self._zh("矩形继承了平行四边形的所有性质", y=5.3, sz=23)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 四个直角标记依次出现
        corners = [
            (self.A, self.D, self.B),   # ∠A: 从D到A到B
            (self.B, self.A, self.C),   # ∠B: 从A到B到C
            (self.C, self.B, self.D),   # ∠C: 从B到C到D
            (self.D, self.C, self.A),   # ∠D: 从C到D到A
        ]
        names   = ["A", "B", "C", "D"]
        ra_list = []
        for (corner, p1, p2), name in zip(corners, names):
            ra = self._right_angle(corner, p1, p2, color=C_ANGLE)
            ra_list.append(ra)
            self.play(Create(ra), run_time=0.35)

        formula = self._formula(
            r"\angle A=\angle B=\angle C=\angle D=90^{\circ}",
            y=-4.2, color=C_ANGLE, sz=26
        )
        self.play(Write(formula), run_time=0.7)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            *[FadeOut(r) for r in ra_list],
            FadeOut(formula), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  性质② — 对角线相等且互相平分
    # ══════════════════════════════════════════
    def scene_prop2_equal_diagonals(self):
        title = self._sec("性质②  对角线相等", color=C_DIAG_A)
        sub   = self._zh("矩形对角线相等，且互相平分", y=5.3, sz=23)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 绘制对角线
        d_AC = self._dashed(self.A, self.C, C_DIAG_A)
        d_BD = self._dashed(self.B, self.D, C_DIAG_B)
        self.play(Create(d_AC), run_time=0.6)
        self.play(Create(d_BD), run_time=0.6)

        # 交点 O
        O_dot = Dot(self.O, radius=0.11, color=C_EQUAL)
        O_lbl = MathTex("O", color=C_EQUAL, font_size=26
                        ).next_to(self.O, UR*0.7, buff=0.12)
        self.play(FadeIn(O_dot, scale=0.3), run_time=0.35)
        self.play(Flash(O_dot, color=C_EQUAL, flash_radius=0.3), run_time=0.4)
        self.play(Write(O_lbl), run_time=0.3)

        # 等长刻度
        t_AC = self._tick(self.A, self.C, n=1, color=C_DIAG_A)
        t_BD = self._tick(self.B, self.D, n=1, color=C_DIAG_B)
        self.play(FadeIn(t_AC), FadeIn(t_BD), run_time=0.4)

        f1 = self._formula(r"AC = BD", y=-4.0, color=C_EQUAL)
        f2 = self._formula(r"OA = OB = OC = OD", y=-4.75, color=C_EQUAL, sz=25)
        self.play(Write(f1), run_time=0.5)
        self.play(Write(f2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(d_AC), FadeOut(d_BD),
            FadeOut(O_dot), FadeOut(O_lbl),
            FadeOut(t_AC), FadeOut(t_BD),
            FadeOut(f1), FadeOut(f2), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定① — 平行四边形 + 一个直角
    # ══════════════════════════════════════════
    def scene_det1_parallelogram_plus_angle(self):
        title = self._sec("判定①", color=C_DET1, y=5.9)
        sub   = self._zh("平行四边形 + 一个直角  ⟹  矩形", y=5.2,
                          color=C_DET1, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        hint = self._zh("已知是平行四边形，只需验证一个角", y=4.55, sz=21)
        self.play(FadeIn(hint), run_time=0.4)

        # 高亮平行四边形（淡色背景）
        para_bg = self._rect(color=C_DET1, sw=2, fill_op=0.06)
        self.play(FadeIn(para_bg), run_time=0.4)

        # 仅在 ∠A 处画直角符号
        ra_A = self._right_angle(self.A, self.D, self.B, color=C_DET1)
        self.play(Create(ra_A), run_time=0.5)

        f1 = self._formula(
            r"\angle A = 90^{\circ}", y=-4.2, color=C_DET1)
        self.play(Write(f1), run_time=0.5)

        # 推导箭头 + 结论
        arrow_grp = VGroup(
            Text("∴", font="Noto Sans CJK SC", font_size=28, color=C_HL),
            Text("ABCD 是矩形", font="Noto Sans CJK SC",
                 font_size=24, color=C_DET1)
        ).arrange(RIGHT, buff=0.15).move_to(UP*-5.1)
        self.play(FadeIn(arrow_grp, scale=1.05), run_time=0.5)

        badge = self._badge("平行四边形 + 一直角  ⟹  矩形", C_DET1, y=-5.9)
        self.play(FadeIn(badge), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hint),
            FadeOut(para_bg), FadeOut(ra_A),
            FadeOut(f1), FadeOut(arrow_grp), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定② — 三个直角
    # ══════════════════════════════════════════
    def scene_det2_three_right_angles(self):
        title = self._sec("判定②", color=C_DET2, y=5.9)
        sub   = self._zh("有三个角是直角的四边形  ⟹  矩形", y=5.2,
                          color=C_DET2, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        hint = self._zh("三个直角决定第四个角也是直角！", y=4.55, sz=21)
        self.play(FadeIn(hint), run_time=0.4)

        corners = [
            (self.A, self.D, self.B),
            (self.B, self.A, self.C),
            (self.C, self.B, self.D),
        ]
        ra_list = []
        for corner, p1, p2 in corners:
            ra = self._right_angle(corner, p1, p2, color=C_DET2)
            ra_list.append(ra)
            self.play(Create(ra), run_time=0.35)

        f_sum = self._formula(
            r"\angle A+\angle B+\angle C+\angle D = 360^{\circ}",
            y=-4.0, color=GRAY_A, sz=24
        )
        f_ded = self._formula(
            r"\Rightarrow \angle D = 90^{\circ}",
            y=-4.75, color=C_DET2, sz=26
        )
        self.play(Write(f_sum), run_time=0.5)
        self.play(Write(f_ded), run_time=0.5)

        # 第四个直角补全
        ra_D = self._right_angle(self.D, self.C, self.A, color=C_HL)
        self.play(Create(ra_D), run_time=0.4)
        self.wait(0.8)

        badge = self._badge("三个直角  ⟹  矩形", C_DET2, y=-5.7)
        self.play(FadeIn(badge), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hint),
            *[FadeOut(r) for r in ra_list], FadeOut(ra_D),
            FadeOut(f_sum), FadeOut(f_ded), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  判定③ — 对角线相等的平行四边形
    # ══════════════════════════════════════════
    def scene_det3_equal_diagonals(self):
        title = self._sec("判定③", color=C_DET3, y=5.9)
        sub   = self._zh("平行四边形 + 对角线相等  ⟹  矩形", y=5.2,
                          color=C_DET3, sz=24)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        d_AC = self._dashed(self.A, self.C, C_DIAG_A)
        d_BD = self._dashed(self.B, self.D, C_DIAG_B)
        self.play(Create(d_AC), Create(d_BD), run_time=0.7)

        t_AC = self._tick(self.A, self.C, n=1, color=C_DIAG_A)
        t_BD = self._tick(self.B, self.D, n=1, color=C_DIAG_B)
        self.play(FadeIn(t_AC), FadeIn(t_BD), run_time=0.4)

        f1 = self._formula(r"AC = BD", y=-4.2, color=C_DET3)
        self.play(Write(f1), run_time=0.5)

        arrow_grp = VGroup(
            Text("∴", font="Noto Sans CJK SC", font_size=28, color=C_HL),
            Text("ABCD 是矩形", font="Noto Sans CJK SC",
                 font_size=24, color=C_DET3)
        ).arrange(RIGHT, buff=0.15).move_to(UP*-5.1)
        self.play(FadeIn(arrow_grp, scale=1.05), run_time=0.5)

        badge = self._badge("平行四边形 + AC=BD  ⟹  矩形", C_DET3, y=-5.9)
        self.play(FadeIn(badge), run_time=0.4)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(d_AC), FadeOut(d_BD),
            FadeOut(t_AC), FadeOut(t_BD),
            FadeOut(f1), FadeOut(arrow_grp), FadeOut(badge), run_time=0.45
        )

    # ══════════════════════════════════════════
    #  汇总
    # ══════════════════════════════════════════
    def scene_summary(self):
        small = self._rect(sw=2, fill_op=0.05).scale(0.52).move_to(UP*4.65)
        self.play(
            Transform(self.rect, small),
            FadeOut(self.labels), run_time=0.7
        )

        title = Text("矩形 · 总览",
                     font="Noto Sans CJK SC", font_size=38,
                     color=GOLD, weight=BOLD).move_to(UP*6.05)
        self.play(Write(title), run_time=0.5)

        rows = [
            # (标签, 内容, 颜色, y中心)
            ("性质①", r"\angle A=\angle B=\angle C=\angle D=90^{\circ}",
             C_ANGLE,  3.35),
            ("性质②", r"AC = BD \quad OA=OB=OC=OD",
             C_DIAG_A, 1.85),
            ("判定①", r"\text{平行四边形} + \angle=90^{\circ}",
             C_DET1,   0.35),
            ("判定②", r"\text{三个直角} \Rightarrow \text{矩形}",
             C_DET2,  -1.15),
            ("判定③", r"\text{平行四边形} + AC=BD",
             C_DET3,  -2.65),
        ]

        cards = []
        for lab, tex, col, yc in rows:
            bg = RoundedRectangle(
                corner_radius=0.16, width=8.0, height=1.30,
                color=col, fill_opacity=0.09, stroke_width=1.5
            ).move_to(UP*yc)
            lbl = Text(lab, font="Noto Sans CJK SC",
                       font_size=24, color=col, weight=BOLD
                       ).move_to(bg.get_left() + RIGHT*0.85)
            fml = MathTex(tex, color=WHITE, font_size=21
                          ).next_to(lbl, RIGHT, buff=0.35)
            card = VGroup(bg, lbl, fml)
            cards.append(card)
            self.play(FadeIn(card, shift=RIGHT*0.2), run_time=0.4)
            self.wait(0.1)

        tip = Text("性质 + 判定，矩形拿满分！",
                   font="Noto Sans CJK SC", font_size=26,
                   color=C_HL).move_to(UP*-4.2)
        self.play(FadeIn(tip, scale=1.05), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(self.rect),
            *[FadeOut(c) for c in cards], FadeOut(tip), run_time=0.55
        )

    # ══════════════════════════════════════════
    #  片尾
    # ══════════════════════════════════════════
    def scene_outro(self):
        # 装饰：小矩形旋转飘落
        deco = VGroup()
        for pos, col, rot in [
            (UP*4.8+LEFT*3.0,  C_ANGLE, 0.1),
            (UP*2.5+RIGHT*3.6, C_DIAG_A, 0.25),
            (DOWN*0.5+LEFT*3.5, C_DET1, 0.15),
            (DOWN*3.2+RIGHT*3.1, C_DET2, 0.05),
            (UP*6.1+RIGHT*1.8,  C_DET3, 0.20),
        ]:
            mini = Rectangle(
                width=0.7, height=0.45,
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

        tagline = Text("四直角 · 对角线相等 · 三判定",
                       font="Noto Sans CJK SC", font_size=20,
                       color=GRAY_B).move_to(DOWN*1.6)
        self.play(FadeIn(tagline), run_time=0.4)

        self.play(Rotate(deco, angle=TAU/10, run_time=1.2))
        self.wait(0.8)
        self.play(
            FadeOut(self.author), FadeOut(id_txt),
            FadeOut(follow), FadeOut(tagline), FadeOut(deco), run_time=0.9
        )