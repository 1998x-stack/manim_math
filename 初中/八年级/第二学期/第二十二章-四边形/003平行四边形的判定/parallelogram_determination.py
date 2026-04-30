"""
平行四边形的判定 - 八年级数学教学动画
Parallelogram Determination Methods - Grade 8 Math

内容: 平行四边形的五种判定方法
目标观众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  快速预览: manim -pql parallelogram_determination.py ParallelogramDetermination
  高质量:   manim -qh  parallelogram_determination.py ParallelogramDetermination
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ─────────────────────────────────────────────
#  颜色配置
# ─────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
C_MAIN        = "#4fc3f7"   # 主图形蓝色
C_METHOD1     = "#80cbc4"   # 判定1 青绿
C_METHOD2     = "#a5d6a7"   # 判定2 绿
C_METHOD3     = "#fff176"   # 判定3 黄
C_METHOD4     = "#ef9a9a"   # 判定4 红
C_METHOD5     = "#ce93d8"   # 判定5 紫
C_CHECK       = "#69f0ae"   # 勾 绿
C_DIAG        = "#ffd54f"   # 对角线橙黄
C_AUX         = "#78909c"   # 辅助灰
C_HIGHLIGHT   = YELLOW

METHOD_COLORS = [C_METHOD1, C_METHOD2, C_METHOD3, C_METHOD4, C_METHOD5]


# ─────────────────────────────────────────────
#  主场景类
# ─────────────────────────────────────────────
class ParallelogramDetermination(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_opening()
        self.scene_method1()
        self.scene_method2()
        self.scene_method3()
        self.scene_method4()
        self.scene_method5()
        self.scene_summary()
        self.scene_outro()

    # ══════════════════════════════════════════
    #  几何数据初始化
    # ══════════════════════════════════════════
    def setup_geometry(self):
        """统一初始化平行四边形顶点及派生点"""
        OFFSET = UP * 1.0

        # 顶点（精确保证平行四边形五条判定全部成立）
        self.A = np.array([-2.2, -1.0, 0]) + OFFSET
        self.B = np.array([ 2.0, -1.0, 0]) + OFFSET
        self.C = np.array([ 2.8,  1.0, 0]) + OFFSET
        self.D = np.array([-1.4,  1.0, 0]) + OFFSET

        # 对角线交点（精确：两对角线互相平分）
        self.O = (self.A + self.C) / 2   # == (B + D) / 2

        # 边长
        self.len_AB = np.linalg.norm(self.B - self.A)   # 4.2
        self.len_AD = np.linalg.norm(self.D - self.A)   # ≈ 2.154

        # ∠A ≈ 68.2°，∠B ≈ 111.8°（验证：other_angle=True for all）
        # 对角线各半段长
        self.OA = np.linalg.norm(self.A - self.O)
        self.OB = np.linalg.norm(self.B - self.O)

    # ══════════════════════════════════════════
    #  工具方法
    # ══════════════════════════════════════════
    def make_para(self, color=C_MAIN, sw=3, fill_op=0.08):
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=color, stroke_width=sw,
            fill_color=color, fill_opacity=fill_op
        )

    def make_labels(self, size=30, color=WHITE):
        offsets = [DL*0.28, DR*0.28, UR*0.28, UL*0.28]
        names   = ["A", "B", "C", "D"]
        verts   = [self.A, self.B, self.C, self.D]
        grp = VGroup()
        for name, vert, off in zip(names, verts, offsets):
            grp.add(MathTex(name, color=color, font_size=size).next_to(vert, off, buff=0.08))
        return grp

    def make_angle_arc(self, vertex, p1, p2, color, radius=0.42):
        """
        other_angle=True：验证所有顶点叉积<0（顺时针），需要翻转。
        ∠B,∠D > 90°，使用更小半径避免溢出图形。
        """
        r = radius
        line1 = Line(vertex, p1)
        line2 = Line(vertex, p2)
        arc = Angle(line1, line2, radius=r, color=color,
                    stroke_width=2.5, other_angle=True)
        arc.set_fill(color, opacity=0.18)
        return arc

    def tick(self, p1, p2, n=1, color=WHITE, size=0.18):
        """等长刻度线"""
        mid = (p1 + p2) / 2
        d = p2 - p1
        d_n = d / np.linalg.norm(d)
        perp = np.array([-d_n[1], d_n[0], 0])
        grp = VGroup()
        sp = 0.12
        offs = np.linspace(-(n-1)*sp/2, (n-1)*sp/2, n)
        for o in offs:
            s = mid + o*d_n - perp*(size/2)
            e = mid + o*d_n + perp*(size/2)
            grp.add(Line(s, e, color=color, stroke_width=2.5))
        return grp

    def parallel_mark(self, p1, p2, n=1, color=WHITE):
        """平行箭头标记"""
        mid  = (p1 + p2) / 2
        d    = p2 - p1
        d_n  = d / np.linalg.norm(d)
        grp  = VGroup()
        sp   = 0.18
        offs = np.linspace(-(n-1)*sp/2, (n-1)*sp/2, n)
        for o in offs:
            pos = mid + o * d_n
            arr = Arrow(
                pos - d_n*0.11, pos + d_n*0.11,
                buff=0, color=color,
                stroke_width=2, tip_length=0.11,
                max_stroke_width_to_length_ratio=60
            )
            grp.add(arr)
        return grp

    def section_title(self, txt, color=YELLOW, y=5.9):
        return Text(txt, font="PingFang SC",
                    font_size=34, color=color, weight=BOLD).move_to(UP*y)

    def zh(self, txt, y, color=GRAY_A, size=22):
        return Text(txt, font="PingFang SC",
                    font_size=size, color=color).move_to(UP*y)

    def formula(self, tex, y, color=WHITE, size=28):
        return MathTex(tex, color=color, font_size=size).move_to(UP*y)

    def checkmark_badge(self, text_str, color, y):
        """带颜色勾号的判定结论小徽章"""
        check = Text("✓", font="PingFang SC",
                     font_size=28, color=C_CHECK)
        label = Text(text_str, font="PingFang SC",
                     font_size=22, color=color)
        grp = VGroup(check, label).arrange(RIGHT, buff=0.15)
        grp.move_to(UP*y)
        return grp

    def highlight_edge(self, p1, p2, color, sw=5):
        return Line(p1, p2, color=color, stroke_width=sw)

    def dashed_diag(self, p1, p2, color=C_DIAG):
        return DashedLine(p1, p2, color=color,
                          dash_length=0.14, stroke_width=2.5)

    # ══════════════════════════════════════════
    #  场景 0：开场
    # ══════════════════════════════════════════
    def scene_opening(self):
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=20, color=GRAY_B
        ).move_to(UP*7.3)
        self.play(FadeIn(self.author, shift=DOWN*0.15), run_time=0.3)

        tag = Text("八年级 · 第二十二章 · 四边形",
                   font="PingFang SC", font_size=21, color=GRAY_B
                   ).move_to(UP*6.75)
        self.play(FadeIn(tag), run_time=0.3)

        title = Text("平行四边形的判定",
                     font="PingFang SC", font_size=46,
                     color=GOLD, weight=BOLD).move_to(UP*6.0)
        self.play(Write(title), run_time=0.9)

        hook = Text("5种方法，一图看懂！",
                    font="PingFang SC", font_size=27,
                    color=C_HIGHLIGHT).move_to(UP*5.2)
        self.play(FadeIn(hook, shift=UP*0.2), run_time=0.5)

        # 展示平行四边形
        self.para = self.make_para()
        self.labels = self.make_labels()
        self.play(Create(self.para), run_time=0.9)
        self.play(Write(self.labels), run_time=0.5)
        self.wait(0.7)

        self.play(FadeOut(title), FadeOut(hook), FadeOut(tag), run_time=0.4)

    # ══════════════════════════════════════════
    #  场景 1：判定1 —— 两组对边分别平行
    # ══════════════════════════════════════════
    def scene_method1(self):
        title = self.section_title("判定1", color=C_METHOD1)
        sub   = self.zh("两组对边分别平行", y=5.3, color=C_METHOD1, size=26)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 高亮 AB 和 CD（一组）
        e_AB = self.highlight_edge(self.A, self.B, C_METHOD1)
        e_CD = self.highlight_edge(self.C, self.D, C_METHOD1)
        self.play(Create(e_AB), Create(e_CD), run_time=0.5)

        # 平行标记
        pm_AB = self.parallel_mark(self.A, self.B, n=1, color=C_METHOD1)
        pm_CD = self.parallel_mark(self.D, self.C, n=1, color=C_METHOD1)
        self.play(FadeIn(pm_AB), FadeIn(pm_CD), run_time=0.4)

        f1 = self.formula(r"AB \parallel CD", y=-4.0, color=C_METHOD1)
        self.play(Write(f1), run_time=0.5)
        self.wait(0.4)

        # 高亮 AD 和 BC（另一组）
        e_AD = self.highlight_edge(self.A, self.D, C_METHOD2)
        e_BC = self.highlight_edge(self.B, self.C, C_METHOD2)
        self.play(
            e_AB.animate.set_color(C_AUX).set_stroke(width=2),
            e_CD.animate.set_color(C_AUX).set_stroke(width=2),
        )
        self.play(Create(e_AD), Create(e_BC), run_time=0.5)

        pm_AD = self.parallel_mark(self.A, self.D, n=2, color=C_METHOD2)
        pm_BC = self.parallel_mark(self.B, self.C, n=2, color=C_METHOD2)
        self.play(FadeIn(pm_AD), FadeIn(pm_BC), run_time=0.4)

        f2 = self.formula(r"AD \parallel BC", y=-4.65, color=C_METHOD2)
        self.play(Write(f2), run_time=0.5)
        self.wait(0.4)

        badge = self.checkmark_badge("⇒ 是平行四边形", C_METHOD1, y=-5.5)
        self.play(FadeIn(badge, scale=1.05), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(e_AB), FadeOut(e_CD), FadeOut(e_AD), FadeOut(e_BC),
            FadeOut(pm_AB), FadeOut(pm_CD), FadeOut(pm_AD), FadeOut(pm_BC),
            FadeOut(f1), FadeOut(f2), FadeOut(badge),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  场景 2：判定2 —— 两组对边分别相等
    # ══════════════════════════════════════════
    def scene_method2(self):
        title = self.section_title("判定2", color=C_METHOD2)
        sub   = self.zh("两组对边分别相等", y=5.3, color=C_METHOD2, size=26)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        e_AB = self.highlight_edge(self.A, self.B, C_METHOD2)
        e_CD = self.highlight_edge(self.C, self.D, C_METHOD2)
        self.play(Create(e_AB), Create(e_CD), run_time=0.5)

        t_AB = self.tick(self.A, self.B, n=1, color=C_METHOD2)
        t_CD = self.tick(self.D, self.C, n=1, color=C_METHOD2)
        self.play(FadeIn(t_AB), FadeIn(t_CD), run_time=0.4)

        f1 = self.formula(r"AB = CD", y=-4.0, color=C_METHOD2)
        self.play(Write(f1), run_time=0.5)
        self.wait(0.4)

        e_AD = self.highlight_edge(self.A, self.D, C_METHOD3)
        e_BC = self.highlight_edge(self.B, self.C, C_METHOD3)
        self.play(
            e_AB.animate.set_color(C_AUX).set_stroke(width=2),
            e_CD.animate.set_color(C_AUX).set_stroke(width=2),
        )
        self.play(Create(e_AD), Create(e_BC), run_time=0.5)

        t_AD = self.tick(self.A, self.D, n=2, color=C_METHOD3)
        t_BC = self.tick(self.B, self.C, n=2, color=C_METHOD3)
        self.play(FadeIn(t_AD), FadeIn(t_BC), run_time=0.4)

        f2 = self.formula(r"AD = BC", y=-4.65, color=C_METHOD3)
        self.play(Write(f2), run_time=0.5)
        self.wait(0.4)

        badge = self.checkmark_badge("⇒ 是平行四边形", C_METHOD2, y=-5.5)
        self.play(FadeIn(badge, scale=1.05), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(e_AB), FadeOut(e_CD), FadeOut(e_AD), FadeOut(e_BC),
            FadeOut(t_AB), FadeOut(t_CD), FadeOut(t_AD), FadeOut(t_BC),
            FadeOut(f1), FadeOut(f2), FadeOut(badge),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  场景 3：判定3 —— 一组对边平行且相等
    # ══════════════════════════════════════════
    def scene_method3(self):
        title = self.section_title("判定3", color=C_METHOD3)
        sub   = self.zh("一组对边平行且相等", y=5.3, color=C_METHOD3, size=26)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        hint = self.zh("只需一组对边同时满足平行+相等", y=4.65, color=GRAY_A, size=21)
        self.play(FadeIn(hint), run_time=0.4)

        # 仅高亮 AB 和 CD
        e_AB = self.highlight_edge(self.A, self.B, C_METHOD3)
        e_CD = self.highlight_edge(self.C, self.D, C_METHOD3)
        self.play(Create(e_AB), Create(e_CD), run_time=0.5)

        # 平行标记 + 等长刻度
        pm_AB = self.parallel_mark(self.A, self.B, n=1, color=C_METHOD3)
        pm_CD = self.parallel_mark(self.D, self.C, n=1, color=C_METHOD3)
        t_AB  = self.tick(self.A, self.B, n=1, color=C_METHOD3)
        t_CD  = self.tick(self.D, self.C, n=1, color=C_METHOD3)

        self.play(FadeIn(pm_AB), FadeIn(pm_CD), run_time=0.4)
        self.play(FadeIn(t_AB), FadeIn(t_CD), run_time=0.4)

        f1 = self.formula(r"AB \parallel CD", y=-4.0, color=C_METHOD3)
        f2 = self.formula(r"AB = CD",         y=-4.65, color=C_METHOD3)
        self.play(Write(f1), Write(f2), run_time=0.6)
        self.wait(0.4)

        badge = self.checkmark_badge("⇒ 是平行四边形", C_METHOD3, y=-5.5)
        self.play(FadeIn(badge, scale=1.05), run_time=0.5)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(hint),
            FadeOut(e_AB), FadeOut(e_CD),
            FadeOut(pm_AB), FadeOut(pm_CD),
            FadeOut(t_AB), FadeOut(t_CD),
            FadeOut(f1), FadeOut(f2), FadeOut(badge),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  场景 4：判定4 —— 两组对角分别相等
    # ══════════════════════════════════════════
    def scene_method4(self):
        title = self.section_title("判定4", color=C_METHOD4)
        sub   = self.zh("两组对角分别相等", y=5.3, color=C_METHOD4, size=26)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # ∠A 和 ∠C（对角，红色）
        arc_A = self.make_angle_arc(self.A, self.D, self.B, C_METHOD4, radius=0.42)
        arc_C = self.make_angle_arc(self.C, self.B, self.D, C_METHOD4, radius=0.42)
        self.play(Create(arc_A), Create(arc_C), run_time=0.7)

        f1 = self.formula(r"\angle A = \angle C", y=-4.0, color=C_METHOD4)
        self.play(Write(f1), run_time=0.5)
        self.wait(0.4)

        # ∠B 和 ∠D（对角，用略深红以示区分）
        arc_B = self.make_angle_arc(self.B, self.A, self.C, "#ff7043", radius=0.38)
        arc_D = self.make_angle_arc(self.D, self.C, self.A, "#ff7043", radius=0.38)
        self.play(Create(arc_B), Create(arc_D), run_time=0.7)

        f2 = self.formula(r"\angle B = \angle D", y=-4.65, color="#ff7043")
        self.play(Write(f2), run_time=0.5)
        self.wait(0.4)

        badge = self.checkmark_badge("⇒ 是平行四边形", C_METHOD4, y=-5.5)
        self.play(FadeIn(badge, scale=1.05), run_time=0.5)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(arc_A), FadeOut(arc_C),
            FadeOut(arc_B), FadeOut(arc_D),
            FadeOut(f1), FadeOut(f2), FadeOut(badge),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  场景 5：判定5 —— 对角线互相平分
    # ══════════════════════════════════════════
    def scene_method5(self):
        title = self.section_title("判定5", color=C_METHOD5)
        sub   = self.zh("对角线互相平分", y=5.3, color=C_METHOD5, size=26)
        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 绘制两条对角线
        diag_AC = self.dashed_diag(self.A, self.C, color=C_METHOD5)
        diag_BD = self.dashed_diag(self.B, self.D, color=C_DIAG)
        self.play(Create(diag_AC), run_time=0.6)
        self.play(Create(diag_BD), run_time=0.6)

        # 交点 O
        O_dot   = Dot(self.O, radius=0.12, color=C_METHOD5)
        O_label = MathTex("O", color=C_METHOD5, font_size=28
                          ).next_to(self.O, UR*0.7, buff=0.12)
        self.play(FadeIn(O_dot, scale=0.3), run_time=0.4)
        self.play(Flash(O_dot, color=C_METHOD5, flash_radius=0.32), run_time=0.4)
        self.play(Write(O_label), run_time=0.3)

        # OA = OC
        seg_OA = Line(self.O, self.A, color=C_METHOD4, stroke_width=5)
        seg_OC = Line(self.O, self.C, color=C_METHOD4, stroke_width=5)
        self.play(Create(seg_OA), Create(seg_OC), run_time=0.5)
        t_OA = self.tick(self.O, self.A, n=1, color=C_METHOD4)
        t_OC = self.tick(self.O, self.C, n=1, color=C_METHOD4)
        self.play(FadeIn(t_OA), FadeIn(t_OC), run_time=0.4)

        f1 = self.formula(r"OA = OC", y=-4.0, color=C_METHOD4)
        self.play(Write(f1), run_time=0.5)
        self.wait(0.3)

        # OB = OD
        seg_OB = Line(self.O, self.B, color=C_DIAG, stroke_width=5)
        seg_OD = Line(self.O, self.D, color=C_DIAG, stroke_width=5)
        self.play(Create(seg_OB), Create(seg_OD), run_time=0.5)
        t_OB = self.tick(self.O, self.B, n=2, color=C_DIAG)
        t_OD = self.tick(self.O, self.D, n=2, color=C_DIAG)
        self.play(FadeIn(t_OB), FadeIn(t_OD), run_time=0.4)

        f2 = self.formula(r"OB = OD", y=-4.65, color=C_DIAG)
        self.play(Write(f2), run_time=0.5)
        self.wait(0.4)

        badge = self.checkmark_badge("⇒ 是平行四边形", C_METHOD5, y=-5.5)
        self.play(FadeIn(badge, scale=1.05), run_time=0.5)
        self.wait(1.1)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(diag_AC), FadeOut(diag_BD),
            FadeOut(O_dot), FadeOut(O_label),
            FadeOut(seg_OA), FadeOut(seg_OC),
            FadeOut(seg_OB), FadeOut(seg_OD),
            FadeOut(t_OA), FadeOut(t_OC),
            FadeOut(t_OB), FadeOut(t_OD),
            FadeOut(f1), FadeOut(f2), FadeOut(badge),
            run_time=0.45
        )

    # ══════════════════════════════════════════
    #  场景 6：五法汇总
    # ══════════════════════════════════════════
    def scene_summary(self):
        # 主图缩小居上
        small_para = self.make_para(sw=2, fill_op=0.05).scale(0.55).move_to(UP*4.6)
        self.play(
            Transform(self.para, small_para),
            FadeOut(self.labels),
            run_time=0.7
        )

        title = Text("5种判定方法", font="PingFang SC",
                     font_size=38, color=GOLD, weight=BOLD).move_to(UP*6.0)
        self.play(Write(title), run_time=0.5)

        methods = [
            ("①", "两组对边分别平行",   C_METHOD1, r"AB \!\parallel\! CD,\; AD \!\parallel\! BC"),
            ("②", "两组对边分别相等",   C_METHOD2, r"AB=CD,\; AD=BC"),
            ("③", "一组对边平行且相等", C_METHOD3, r"AB \!\parallel\! CD \text{ and } AB=CD"),
            ("④", "两组对角分别相等",   C_METHOD4, r"\angle A=\angle C,\; \angle B=\angle D"),
            ("⑤", "对角线互相平分",     C_METHOD5, r"OA=OC,\; OB=OD"),
        ]

        # 卡片起始 y
        y_start = 3.15
        dy      = 1.65
        cards   = []

        for i, (num, desc, col, tex) in enumerate(methods):
            y = y_start - i * dy

            bg = RoundedRectangle(
                corner_radius=0.18, width=8.0, height=1.45,
                color=col, fill_opacity=0.09, stroke_width=1.5
            ).move_to(UP * (y - 0.08))

            num_t  = Text(num,  font="PingFang SC",
                          font_size=26, color=col, weight=BOLD)
            desc_t = Text(desc, font="PingFang SC",
                          font_size=22, color=col)
            header = VGroup(num_t, desc_t).arrange(RIGHT, buff=0.18)
            header.move_to(UP * y)

            fml = MathTex(tex, color=WHITE, font_size=22)
            fml.next_to(header, DOWN, buff=0.10)

            card = VGroup(bg, header, fml)
            cards.append(card)
            self.play(FadeIn(card, shift=RIGHT*0.25), run_time=0.45)
            self.wait(0.12)

        # 底部口诀
        tip = Text("记住这5条，判定零失误！",
                   font="PingFang SC", font_size=26,
                   color=C_HIGHLIGHT).move_to(UP * -5.8)
        self.play(FadeIn(tip, scale=1.05), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title),
            FadeOut(self.para),
            *[FadeOut(c) for c in cards],
            FadeOut(tip),
            run_time=0.55
        )

    # ══════════════════════════════════════════
    #  场景 7：片尾
    # ══════════════════════════════════════════
    def scene_outro(self):
        # 背景装饰：5个小平行四边形，分别对应5种判定色
        deco = VGroup()
        configs = [
            (UP*4.5 + LEFT*3.2, C_METHOD1, 0.15),
            (UP*2.5 + RIGHT*3.5, C_METHOD2, 0.20),
            (DOWN*0.5 + LEFT*3.5, C_METHOD3, 0.18),
            (DOWN*3.0 + RIGHT*3.2, C_METHOD4, 0.22),
            (UP*6.0 + RIGHT*1.5, C_METHOD5, 0.14),
        ]
        for pos, col, rot in configs:
            mini = Polygon(
                np.array([-0.42, -0.18, 0]),
                np.array([ 0.32, -0.18, 0]),
                np.array([ 0.42,  0.18, 0]),
                np.array([-0.32,  0.18, 0]),
                color=col, fill_opacity=0.35, stroke_width=1.5
            ).rotate(rot).move_to(pos)
            deco.add(mini)

        self.play(*[FadeIn(d, scale=0.5) for d in deco], run_time=0.6)

        # 作者大名
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC", font_size=38,
            color=WHITE, weight=BOLD
        ).move_to(UP*1.6)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC", font_size=28, color=GRAY_B
        ).move_to(UP*0.7)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP*0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！",
                      font="PingFang SC", font_size=30,
                      color=C_HIGHLIGHT).move_to(DOWN*0.4)
        self.play(FadeIn(follow, shift=UP*0.25, scale=1.05), run_time=0.55)

        tagline = Text(
            "两平行 · 两相等 · 平行相等 · 对角相等 · 对角线分",
            font="PingFang SC", font_size=17, color=GRAY_B
        ).move_to(DOWN*1.7)
        self.play(FadeIn(tagline), run_time=0.4)

        self.play(Rotate(deco, angle=TAU/12, run_time=1.2))
        self.wait(0.8)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(tagline), FadeOut(deco),
            run_time=0.9
        )

# manim -pql parallelogram_determination.py ParallelogramDetermination  # 预览
# manim -qh  parallelogram_determination.py ParallelogramDetermination  # 高质量