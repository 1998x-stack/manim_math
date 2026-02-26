"""
全等三角形的判定——ASA 与 AAS
七年级数学 第十四章

核心内容:
  ASA (角-边-角): 两角及其夹边对应相等 → 全等
  AAS (角-角-边): 两角及其中一角对边对应相等 → 全等
  AAA 反例: 三角相等 ≠ 全等，只能说明相似

格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
from manim.utils.color.core import ManimColor
import numpy as np

# ── TikTok 竖屏配置 ────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class ASA_AAS(Scene):
    """
    场景顺序:
      1. 开场钩子
      2. "全等"回顾
      3. ASA 判定
      4. AAS 判定
      5. AAA 反例
      6. 总结 + 片尾
    """

    # ── 配色 ────────────────────────────────────────────
    C_BG        = "#1a1a2e"
    C_TRI1      = WHITE
    C_TRI2      = "#a8d8ea"
    C_ANG1      = "#e74c3c"
    C_ANG2      = "#3498db"
    C_SIDE      = "#f1c40f"
    C_CONGRUENT = "#2ecc71"
    C_WRONG     = "#e74c3c"
    C_HIGHLIGHT = "#f1c40f"
    C_AUX       = "#95a5a6"
    C_ASA       = "#9b59b6"
    C_AAS       = "#e67e22"

    def construct(self):
        self.camera.background_color = self.C_BG
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_congruence_review()
        self.scene_3_asa()
        self.scene_4_aas()
        self.scene_5_aaa_counterexample()
        self.scene_6_summary_outro()

    # ═══════════════════════════════════════════════════
    # 几何初始化
    # ═══════════════════════════════════════════════════
    def setup_geometry(self):
        self.A = np.array([-2.3,  2.8, 0.0])
        self.B = np.array([-3.5,  0.5, 0.0])
        self.C = np.array([-0.5,  0.5, 0.0])

        sh = np.array([4.4, 0.0, 0.0])
        self.D = self.A + sh
        self.E = self.B + sh
        self.F = self.C + sh

        self.AB = np.linalg.norm(self.B - self.A)
        self.AC = np.linalg.norm(self.C - self.A)
        self.BC = np.linalg.norm(self.C - self.B)

        self.aA = self._ang(self.B, self.A, self.C)
        self.aB = self._ang(self.A, self.B, self.C)
        self.aC = self._ang(self.A, self.C, self.B)

        assert abs(self.AB - np.linalg.norm(self.E - self.D)) < 1e-6
        assert abs(self.aA - self._ang(self.E, self.D, self.F)) < 1e-6

    def _ang(self, P1, v, P2):
        a = P1 - v;  b = P2 - v
        return np.arccos(np.clip(
            np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)),
            -1.0, 1.0))

    def _cross_z(self, v1, v2):
        return float(v1[0]*v2[1] - v1[1]*v2[0])

    def _tri(self, pts, color=WHITE, sw=3, fc=WHITE, fo=0.0):
        return Polygon(*pts, color=color, stroke_width=sw,
                       fill_color=fc, fill_opacity=fo)

    def _tick(self, P1, P2, n=1, color=GOLD, size=0.20):
        mid = (P1+P2)/2
        d = P2-P1;  d = d/np.linalg.norm(d)
        perp = np.array([-d[1], d[0], 0.0])
        offs = {1:[0.0], 2:[-0.28,0.28], 3:[-0.45,0.0,0.45]}[n]
        g = VGroup()
        for off in offs:
            g.add(Line(mid+off*d - perp*size/2,
                       mid+off*d + perp*size/2,
                       color=color, stroke_width=3))
        return g

    def _arc(self, vertex, end1, end2,
             radius=0.46, color=RED, other_angle=False, double=False, sw=2.5):
        l1 = Line(vertex, end1);  l2 = Line(vertex, end2)
        g = VGroup(Angle(l1, l2, radius=radius, color=color,
                         other_angle=other_angle, stroke_width=sw))
        if double:
            g.add(Angle(l1, l2, radius=radius+0.14, color=color,
                        other_angle=other_angle, stroke_width=sw))
        return g

    def _label(self, text, pt, direction, buff=0.18, sz=26, color=WHITE):
        return Text(text, font="Noto Sans CJK SC",
                    font_size=sz, color=color).next_to(pt, direction, buff=buff)

    def _header(self, tag, name, tag_col):
        tg = Text(tag,  font="Noto Sans CJK SC", font_size=25,
                  color=tag_col).move_to(UP*6.7)
        nm = Text(name, font="Noto Sans CJK SC", font_size=42,
                  color=tag_col).move_to(UP*6.0)
        return tg, nm

    def _rule_box(self, lines, color, pos, w=8.2, h=1.1):
        bg = RoundedRectangle(width=w, height=h, corner_radius=0.3,
                              color=color,
                              fill_color=ManimColor(color).interpolate(BLACK, 0.84),
                              fill_opacity=0.94).move_to(pos)
        texts = VGroup(*[
            Text(t, font="Noto Sans CJK SC", font_size=sz, color=c)
            for t, c, sz in lines
        ]).arrange(DOWN, buff=0.1).move_to(pos)
        return VGroup(bg, texts)

    def _abc_labels(self, sz=27):
        lA = self._label("A", self.A, UP,    sz=sz)
        lB = self._label("B", self.B, LEFT,  buff=0.15, sz=sz)
        lC = self._label("C", self.C, DR,    sz=sz)
        return lA, lB, lC

    def _def_labels(self, sz=27):
        lD = self._label("D", self.D, UP,   sz=sz)
        lE = self._label("E", self.E, DL,   sz=sz)
        lF = self._label("F", self.F, DOWN, buff=0.15, sz=sz)
        return lD, lE, lF

    # ═══════════════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ═══════════════════════════════════════════════════
    def scene_1_opening(self):
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC", font_size=20, color=self.C_AUX
        ).move_to(UP*7.0)
        self.play(FadeIn(self.author_bar, shift=DOWN*0.2), run_time=0.35)

        chap = Text("七年级 · 第十四章 · 三角形",
                    font="Noto Sans CJK SC", font_size=22,
                    color=self.C_AUX).move_to(UP*6.1)
        self.play(FadeIn(chap), run_time=0.35)

        title = Text("全等三角形的判定",
                     font="Noto Sans CJK SC", font_size=48,
                     color=self.C_HIGHLIGHT).move_to(UP*5.2)
        self.play(Write(title), run_time=0.85)

        hook = Text("知道两角和一条边——能判定全等吗？",
                    font="Noto Sans CJK SC", font_size=26,
                    color=WHITE).move_to(UP*4.3)
        self.play(FadeIn(hook, shift=UP*0.2), run_time=0.5)

        tri1 = self._tri([self.A, self.B, self.C], color=self.C_TRI1)
        tri2 = self._tri([self.D, self.E, self.F], color=self.C_TRI2)

        tri1.shift(LEFT*6);  tri2.shift(RIGHT*6)
        self.play(
            tri1.animate.shift(RIGHT*6),
            tri2.animate.shift(LEFT*6),
            run_time=0.9
        )

        def badge(txt, color, pos):
            bg = RoundedRectangle(width=3.6, height=0.72, corner_radius=0.24,
                                  color=color,
                                  fill_color=ManimColor(color).interpolate(BLACK, 0.8),
                                  fill_opacity=0.9).move_to(pos)
            t = Text(txt, font="Noto Sans CJK SC", font_size=26,
                     color=color).move_to(pos)
            return VGroup(bg, t)

        b1 = badge("ASA  角边角", self.C_ASA,  DOWN*3.3)
        b2 = badge("AAS  角角边", self.C_AAS,  DOWN*4.2)
        b3 = badge("AAA  反例", self.C_WRONG, DOWN*5.1)

        for b in [b1, b2, b3]:
            self.play(FadeIn(b, shift=RIGHT*0.25), run_time=0.32)
        self.wait(0.7)

        self.play(
            FadeOut(chap), FadeOut(title), FadeOut(hook),
            FadeOut(tri1), FadeOut(tri2),
            FadeOut(b1), FadeOut(b2), FadeOut(b3),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════
    # Scene 2 — "全等"概念回顾
    # ═══════════════════════════════════════════════════
    def scene_2_congruence_review(self):
        review_title = Text("什么是全等三角形？",
                            font="Noto Sans CJK SC", font_size=36,
                            color=self.C_HIGHLIGHT).move_to(UP*6.3)
        self.play(FadeIn(review_title), run_time=0.45)

        defn1 = Text("形状和大小完全相同的两个三角形",
                     font="Noto Sans CJK SC", font_size=26,
                     color=WHITE).move_to(UP*5.4)
        defn2 = Text("叫做全等三角形",
                     font="Noto Sans CJK SC", font_size=26,
                     color=WHITE).move_to(UP*4.85)
        self.play(FadeIn(defn1), FadeIn(defn2), run_time=0.5)

        tri1 = self._tri([self.A, self.B, self.C],
                         color=self.C_TRI1, fo=0.15, fc=WHITE)
        tri2 = self._tri([self.D, self.E, self.F],
                         color=self.C_TRI2, fo=0.15, fc=self.C_TRI2)
        lA, lB, lC = self._abc_labels()
        lD, lE, lF = self._def_labels()

        self.play(Create(tri1), Create(tri2), run_time=0.75)
        self.play(
            FadeIn(lA), FadeIn(lB), FadeIn(lC),
            FadeIn(lD), FadeIn(lE), FadeIn(lF),
            run_time=0.4
        )

        symbol = MathTex(r"\triangle ABC \cong \triangle DEF",
                         color=self.C_CONGRUENT, font_size=38).move_to(DOWN*3.8)
        self.play(Write(symbol), run_time=0.75)

        self.play(
            tri2.animate.set_fill(color=WHITE, opacity=0.3)
                        .set_stroke(color=WHITE),
            run_time=0.7
        )
        self.play(
            tri2.animate.set_fill(color=self.C_TRI2, opacity=0.15)
                        .set_stroke(color=self.C_TRI2),
            run_time=0.5
        )
        self.wait(0.6)

        self.play(
            FadeOut(review_title), FadeOut(defn1), FadeOut(defn2),
            FadeOut(symbol),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(lD), FadeOut(lE), FadeOut(lF),
            FadeOut(tri1), FadeOut(tri2),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════
    # Scene 3 — ASA 判定
    # ═══════════════════════════════════════════════════
    def scene_3_asa(self):
        tg, nm = self._header("判定方法一", "ASA  角-边-角", self.C_ASA)
        self.play(FadeIn(tg, shift=DOWN*0.15),
                  FadeIn(nm, shift=DOWN*0.15), run_time=0.55)

        tri1 = self._tri([self.A, self.B, self.C], color=self.C_TRI1, sw=3)
        tri2 = self._tri([self.D, self.E, self.F], color=self.C_TRI2, sw=3)
        lA, lB, lC = self._abc_labels()
        lD, lE, lF = self._def_labels()

        self.play(Create(tri1), Create(tri2), run_time=0.75)
        self.play(
            FadeIn(lA), FadeIn(lB), FadeIn(lC),
            FadeIn(lD), FadeIn(lE), FadeIn(lF),
            run_time=0.4
        )

        step1 = Text("① ∠A = ∠D",
                     font="Noto Sans CJK SC", font_size=28,
                     color=self.C_ANG1).move_to(DOWN*3.3)
        self.play(FadeIn(step1), run_time=0.35)

        arc_A = self._arc(self.A, self.B, self.C,
                          radius=0.50, color=self.C_ANG1, other_angle=False)
        arc_D = self._arc(self.D, self.E, self.F,
                          radius=0.50, color=self.C_ANG1, other_angle=False)

        self.play(Create(arc_A), Create(arc_D), run_time=0.75)

        la_A = MathTex(r"\angle A", color=self.C_ANG1,
                       font_size=26).move_to(self.A + np.array([-0.05, -0.72, 0]))
        la_D = MathTex(r"\angle D", color=self.C_ANG1,
                       font_size=26).move_to(self.D + np.array([-0.05, -0.72, 0]))
        self.play(FadeIn(la_A), FadeIn(la_D), run_time=0.35)
        self.wait(0.35)

        self.play(FadeOut(step1), run_time=0.25)
        step2 = Text("② AB = DE（夹边）",
                     font="Noto Sans CJK SC", font_size=28,
                     color=self.C_SIDE).move_to(DOWN*3.3)
        self.play(FadeIn(step2), run_time=0.35)

        side_AB = Line(self.A, self.B, color=self.C_SIDE, stroke_width=7)
        side_DE = Line(self.D, self.E, color=self.C_SIDE, stroke_width=7)
        tick_AB = self._tick(self.A, self.B, n=1, color=self.C_SIDE)
        tick_DE = self._tick(self.D, self.E, n=1, color=self.C_SIDE)

        self.play(Create(side_AB), Create(side_DE), run_time=0.65)
        self.play(FadeIn(tick_AB), FadeIn(tick_DE), run_time=0.35)

        jia_lbl = Text("← 夹边",
                       font="Noto Sans CJK SC", font_size=22,
                       color=self.C_SIDE).move_to(DOWN*4.1)
        self.play(FadeIn(jia_lbl), run_time=0.3)
        self.wait(0.35)

        self.play(FadeOut(step2), FadeOut(jia_lbl), run_time=0.25)
        step3 = Text("③ ∠B = ∠E",
                     font="Noto Sans CJK SC", font_size=28,
                     color=self.C_ANG2).move_to(DOWN*3.3)
        self.play(FadeIn(step3), run_time=0.35)

        arc_B = self._arc(self.B, self.A, self.C,
                          radius=0.50, color=self.C_ANG2, other_angle=True)
        arc_E = self._arc(self.E, self.D, self.F,
                          radius=0.50, color=self.C_ANG2, other_angle=True)

        self.play(Create(arc_B), Create(arc_E), run_time=0.75)

        lb_B = MathTex(r"\angle B", color=self.C_ANG2,
                       font_size=26).move_to(self.B + np.array([0.62, 0.48, 0]))
        lb_E = MathTex(r"\angle E", color=self.C_ANG2,
                       font_size=26).move_to(self.E + np.array([0.62, 0.48, 0]))
        self.play(FadeIn(lb_B), FadeIn(lb_E), run_time=0.35)
        self.wait(0.3)

        self.play(FadeOut(step3), run_time=0.25)

        clip_explain = Text("AB 在 ∠A 和 ∠B 之间，是夹边",
                            font="Noto Sans CJK SC", font_size=24,
                            color=self.C_SIDE).move_to(DOWN*3.5)
        self.play(FadeIn(clip_explain), run_time=0.4)
        self.wait(0.6)

        self.play(FadeOut(clip_explain), run_time=0.25)

        concl_formula = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            color=self.C_CONGRUENT, font_size=36
        ).move_to(DOWN*4.15)
        self.play(Write(concl_formula), run_time=0.65)

        asa_rule = self._rule_box(
            [("ASA（角-边-角）判定定理", self.C_ASA, 24),
             ("两角及其夹边对应相等 → 全等", WHITE, 22)],
            self.C_ASA, DOWN*5.4, h=1.35
        )
        self.play(FadeIn(asa_rule), run_time=0.5)

        self.play(
            Flash(self.A, color=self.C_ANG1, flash_radius=0.4),
            Flash(self.D, color=self.C_ANG1, flash_radius=0.4),
            Flash((self.A + self.B)/2, color=self.C_SIDE, flash_radius=0.35),
            Flash((self.D + self.E)/2, color=self.C_SIDE, flash_radius=0.35),
            run_time=0.6
        )
        self.wait(1.6)

        self.play(
            FadeOut(tg), FadeOut(nm),
            FadeOut(tri1), FadeOut(tri2),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(lD), FadeOut(lE), FadeOut(lF),
            FadeOut(arc_A), FadeOut(arc_D),
            FadeOut(arc_B), FadeOut(arc_E),
            FadeOut(la_A), FadeOut(la_D),
            FadeOut(lb_B), FadeOut(lb_E),
            FadeOut(side_AB), FadeOut(side_DE),
            FadeOut(tick_AB), FadeOut(tick_DE),
            FadeOut(concl_formula), FadeOut(asa_rule),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════
    # Scene 4 — AAS 判定
    # ═══════════════════════════════════════════════════
    def scene_4_aas(self):
        tg, nm = self._header("判定方法二", "AAS  角-角-边", self.C_AAS)
        self.play(FadeIn(tg, shift=DOWN*0.15),
                  FadeIn(nm, shift=DOWN*0.15), run_time=0.55)

        tri1 = self._tri([self.A, self.B, self.C], color=self.C_TRI1, sw=3)
        tri2 = self._tri([self.D, self.E, self.F], color=self.C_TRI2, sw=3)
        lA, lB, lC = self._abc_labels()
        lD, lE, lF = self._def_labels()

        self.play(Create(tri1), Create(tri2), run_time=0.75)
        self.play(
            FadeIn(lA), FadeIn(lB), FadeIn(lC),
            FadeIn(lD), FadeIn(lE), FadeIn(lF),
            run_time=0.4
        )

        step1 = Text("① ∠A = ∠D",
                     font="Noto Sans CJK SC", font_size=28,
                     color=self.C_ANG1).move_to(DOWN*3.3)
        self.play(FadeIn(step1), run_time=0.35)

        arc_A = self._arc(self.A, self.B, self.C,
                          radius=0.50, color=self.C_ANG1, other_angle=False)
        arc_D = self._arc(self.D, self.E, self.F,
                          radius=0.50, color=self.C_ANG1, other_angle=False)
        self.play(Create(arc_A), Create(arc_D), run_time=0.75)

        la_A = MathTex(r"\angle A", color=self.C_ANG1,
                       font_size=26).move_to(self.A + np.array([-0.05, -0.72, 0]))
        la_D = MathTex(r"\angle D", color=self.C_ANG1,
                       font_size=26).move_to(self.D + np.array([-0.05, -0.72, 0]))
        self.play(FadeIn(la_A), FadeIn(la_D), run_time=0.35)
        self.wait(0.3)

        self.play(FadeOut(step1), run_time=0.25)
        step2 = Text("② ∠B = ∠E",
                     font="Noto Sans CJK SC", font_size=28,
                     color=self.C_ANG2).move_to(DOWN*3.3)
        self.play(FadeIn(step2), run_time=0.35)

        arc_B = self._arc(self.B, self.A, self.C,
                          radius=0.50, color=self.C_ANG2, other_angle=True)
        arc_E = self._arc(self.E, self.D, self.F,
                          radius=0.50, color=self.C_ANG2, other_angle=True)
        self.play(Create(arc_B), Create(arc_E), run_time=0.75)

        lb_B = MathTex(r"\angle B", color=self.C_ANG2,
                       font_size=26).move_to(self.B + np.array([0.62, 0.48, 0]))
        lb_E = MathTex(r"\angle E", color=self.C_ANG2,
                       font_size=26).move_to(self.E + np.array([0.62, 0.48, 0]))
        self.play(FadeIn(lb_B), FadeIn(lb_E), run_time=0.35)
        self.wait(0.3)

        self.play(FadeOut(step2), run_time=0.25)
        step3 = Text("③ BC = EF（∠A 的对边）",
                     font="Noto Sans CJK SC", font_size=26,
                     color=self.C_SIDE).move_to(DOWN*3.3)
        self.play(FadeIn(step3), run_time=0.35)

        side_BC = Line(self.B, self.C, color=self.C_SIDE, stroke_width=7)
        side_EF = Line(self.E, self.F, color=self.C_SIDE, stroke_width=7)
        tick_BC = self._tick(self.B, self.C, n=2, color=self.C_SIDE)
        tick_EF = self._tick(self.E, self.F, n=2, color=self.C_SIDE)

        self.play(Create(side_BC), Create(side_EF), run_time=0.65)
        self.play(FadeIn(tick_BC), FadeIn(tick_EF), run_time=0.35)

        self.play(FadeOut(step3), run_time=0.25)

        compare_box = VGroup(
            Text("与 ASA 对比：边的位置不同！",
                 font="Noto Sans CJK SC", font_size=23,
                 color=self.C_HIGHLIGHT),
            Text("ASA → AB 是 ∠A 和 ∠B 的 夹 边",
                 font="Noto Sans CJK SC", font_size=21,
                 color=self.C_ASA),
            Text("AAS → BC 是 ∠A 的 对 边",
                 font="Noto Sans CJK SC", font_size=21,
                 color=self.C_AAS),
        ).arrange(DOWN, buff=0.15).move_to(DOWN*4.0)
        self.play(FadeIn(compare_box), run_time=0.6)
        self.wait(0.9)

        self.play(FadeOut(compare_box), run_time=0.25)

        concl_formula = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            color=self.C_CONGRUENT, font_size=36
        ).move_to(DOWN*4.05)
        self.play(Write(concl_formula), run_time=0.65)

        aas_rule = self._rule_box(
            [("AAS（角-角-边）判定定理", self.C_AAS, 24),
             ("两角及其中一角对边对应相等 → 全等", WHITE, 21)],
            self.C_AAS, DOWN*5.35, h=1.35
        )
        self.play(FadeIn(aas_rule), run_time=0.5)

        self.play(
            Flash(self.B, color=self.C_SIDE, flash_radius=0.4),
            Flash(self.C, color=self.C_SIDE, flash_radius=0.4),
            Flash(self.E, color=self.C_SIDE, flash_radius=0.4),
            Flash(self.F, color=self.C_SIDE, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(1.5)

        self.play(
            FadeOut(tg), FadeOut(nm),
            FadeOut(tri1), FadeOut(tri2),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(lD), FadeOut(lE), FadeOut(lF),
            FadeOut(arc_A), FadeOut(arc_D),
            FadeOut(arc_B), FadeOut(arc_E),
            FadeOut(la_A), FadeOut(la_D),
            FadeOut(lb_B), FadeOut(lb_E),
            FadeOut(side_BC), FadeOut(side_EF),
            FadeOut(tick_BC), FadeOut(tick_EF),
            FadeOut(concl_formula), FadeOut(aas_rule),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════
    # Scene 5 — AAA 反例
    # ═══════════════════════════════════════════════════
    def scene_5_aaa_counterexample(self):
        tg, nm = self._header("注意！", "AAA 三角对应相等", self.C_WRONG)
        self.play(FadeIn(tg, shift=DOWN*0.15),
                  FadeIn(nm, shift=DOWN*0.15), run_time=0.55)

        warn = Text("三角对应相等 ≠ 全等！",
                    font="Noto Sans CJK SC", font_size=30,
                    color=self.C_WRONG).move_to(UP*5.0)
        self.play(FadeIn(warn), run_time=0.45)

        big_A = np.array([-1.3,  3.6, 0])
        big_B = np.array([-3.0,  1.2, 0])
        big_C = np.array([ 0.4,  1.2, 0])

        center_big = (big_A + big_B + big_C) / 3
        k = 0.58
        small_A = center_big + (big_A - center_big)*k + np.array([1.6, -3.0, 0])
        small_B = center_big + (big_B - center_big)*k + np.array([1.6, -3.0, 0])
        small_C = center_big + (big_C - center_big)*k + np.array([1.6, -3.0, 0])

        tri_big   = self._tri([big_A, big_B, big_C],
                               color=WHITE, fo=0.12, fc=WHITE, sw=3)
        tri_small = self._tri([small_A, small_B, small_C],
                               color=self.C_TRI2, fo=0.12, fc=self.C_TRI2, sw=3)

        self.play(Create(tri_big), Create(tri_small), run_time=0.8)

        lg_A = self._label("A",  big_A,   UP,   sz=25)
        lg_B = self._label("B",  big_B,   LEFT, buff=0.14, sz=25)
        lg_C = self._label("C",  big_C,   DR,   sz=25)
        ls_A = self._label("A'", small_A, UP,   sz=23, color=self.C_TRI2)
        ls_B = self._label("B'", small_B, LEFT, buff=0.12, sz=23, color=self.C_TRI2)
        ls_C = self._label("C'", small_C, DR,   sz=23, color=self.C_TRI2)

        self.play(
            FadeIn(lg_A), FadeIn(lg_B), FadeIn(lg_C),
            FadeIn(ls_A), FadeIn(ls_B), FadeIn(ls_C),
            run_time=0.4
        )

        def ang3(P1, v, P2):
            a = P1-v;  b = P2-v
            return np.arccos(np.clip(
                np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)), -1,1))

        aA_big = ang3(big_B, big_A, big_C)
        aB_big = ang3(big_A, big_B, big_C)

        ang_txt = Text(
            f"∠A=∠A'≈{np.degrees(aA_big):.0f}°   ∠B=∠B'≈{np.degrees(aB_big):.0f}°",
            font="Noto Sans CJK SC", font_size=21,
            color=self.C_ANG1).move_to(DOWN*0.6)
        self.play(FadeIn(ang_txt), run_time=0.5)

        v1b = big_B - big_A;  v2b = big_C - big_A
        oa_bigA = True if (v1b[0]*v2b[1]-v1b[1]*v2b[0]) < 0 else False
        v1s = small_B - small_A;  v2s = small_C - small_A
        oa_smlA = True if (v1s[0]*v2s[1]-v1s[1]*v2s[0]) < 0 else False

        arc_bigA  = self._arc(big_A,   big_B,   big_C,
                              radius=0.42, color=self.C_ANG1, other_angle=oa_bigA)
        arc_smlA  = self._arc(small_A, small_B, small_C,
                              radius=0.28, color=self.C_ANG1, other_angle=oa_smlA)
        self.play(Create(arc_bigA), Create(arc_smlA), run_time=0.65)
        self.wait(0.4)

        but_txt = Text("但是……边长不同！",
                       font="Noto Sans CJK SC", font_size=28,
                       color=self.C_WRONG).move_to(DOWN*1.6)
        self.play(FadeIn(but_txt, scale=0.8), run_time=0.5)

        big_AB  = np.linalg.norm(big_B - big_A)
        small_AB = np.linalg.norm(small_B - small_A)

        side_big   = Line(big_A,   big_B,   color=self.C_WRONG, stroke_width=5)
        side_small = Line(small_A, small_B, color=self.C_WRONG, stroke_width=5)
        self.play(Create(side_big), Create(side_small), run_time=0.6)

        len_big_lbl = MathTex(
            f"{big_AB:.1f}",
            color=self.C_WRONG, font_size=24
        ).next_to(side_big,   LEFT, buff=0.12)
        len_sml_lbl = MathTex(
            f"{small_AB:.1f}",
            color=self.C_WRONG, font_size=24
        ).next_to(side_small, LEFT, buff=0.12)
        self.play(FadeIn(len_big_lbl), FadeIn(len_sml_lbl), run_time=0.4)
        self.wait(0.5)

        cross_mark = Text("✕",
                          font="Noto Sans CJK SC", font_size=80,
                          color=self.C_WRONG).move_to(DOWN*2.9)
        self.play(FadeIn(cross_mark, scale=0.3), run_time=0.5)

        aaa_rule = self._rule_box(
            [("AAA 三角对应相等 ≠ 全等", self.C_WRONG, 24),
             ("只能说明两三角形 相似，不能说全等！", WHITE, 21)],
            self.C_WRONG, DOWN*4.85, h=1.35
        )
        self.play(FadeIn(aaa_rule), run_time=0.5)
        self.wait(1.6)

        self.play(
            FadeOut(tg), FadeOut(nm), FadeOut(warn),
            FadeOut(tri_big), FadeOut(tri_small),
            FadeOut(lg_A), FadeOut(lg_B), FadeOut(lg_C),
            FadeOut(ls_A), FadeOut(ls_B), FadeOut(ls_C),
            FadeOut(ang_txt), FadeOut(arc_bigA), FadeOut(arc_smlA),
            FadeOut(but_txt), FadeOut(side_big), FadeOut(side_small),
            FadeOut(len_big_lbl), FadeOut(len_sml_lbl),
            FadeOut(cross_mark), FadeOut(aaa_rule),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════
    # Scene 6 — 总结 + 片尾
    # ═══════════════════════════════════════════════════
    def scene_6_summary_outro(self):
        sum_title = Text("知识总结",
                         font="Noto Sans CJK SC", font_size=44,
                         color=self.C_HIGHLIGHT).move_to(UP*6.5)
        self.play(Write(sum_title), run_time=0.6)

        asa_bg = RoundedRectangle(
            width=7.8, height=2.4, corner_radius=0.32,
            color=self.C_ASA,
            fill_color=ManimColor(self.C_ASA).interpolate(BLACK, 0.82),
            fill_opacity=0.95
        ).move_to(UP*4.6)

        asa_tag  = Text("ASA  角-边-角", font="Noto Sans CJK SC",
                        font_size=30, color=self.C_ASA)
        asa_line1 = Text("∠A=∠D，AB=DE（夹边），∠B=∠E",
                         font="Noto Sans CJK SC", font_size=22, color=WHITE)
        asa_line2 = Text("→  △ABC ≌ △DEF",
                         font="Noto Sans CJK SC", font_size=24,
                         color=self.C_CONGRUENT)
        VGroup(asa_tag, asa_line1, asa_line2)\
            .arrange(DOWN, buff=0.14).move_to(UP*4.6)

        self.play(FadeIn(asa_bg), run_time=0.3)
        self.play(
            FadeIn(asa_tag), FadeIn(asa_line1), FadeIn(asa_line2),
            run_time=0.5
        )

        aas_bg = RoundedRectangle(
            width=7.8, height=2.4, corner_radius=0.32,
            color=self.C_AAS,
            fill_color=ManimColor(self.C_AAS).interpolate(BLACK, 0.82),
            fill_opacity=0.95
        ).move_to(UP*1.8)

        aas_tag  = Text("AAS  角-角-边", font="Noto Sans CJK SC",
                        font_size=30, color=self.C_AAS)
        aas_line1 = Text("∠A=∠D，∠B=∠E，BC=EF（对边）",
                         font="Noto Sans CJK SC", font_size=22, color=WHITE)
        aas_line2 = Text("→  △ABC ≌ △DEF",
                         font="Noto Sans CJK SC", font_size=24,
                         color=self.C_CONGRUENT)
        VGroup(aas_tag, aas_line1, aas_line2)\
            .arrange(DOWN, buff=0.14).move_to(UP*1.8)

        self.play(FadeIn(aas_bg), run_time=0.3)
        self.play(
            FadeIn(aas_tag), FadeIn(aas_line1), FadeIn(aas_line2),
            run_time=0.5
        )

        aaa_bg = RoundedRectangle(
            width=7.8, height=1.5, corner_radius=0.32,
            color=self.C_WRONG,
            fill_color=ManimColor(self.C_WRONG).interpolate(BLACK, 0.85),
            fill_opacity=0.95
        ).move_to(DOWN*1.0)

        aaa_tag  = Text("✕  AAA  三角对应相等",
                        font="Noto Sans CJK SC", font_size=26,
                        color=self.C_WRONG)
        aaa_line = Text("只能说明相似，不能判定全等！",
                        font="Noto Sans CJK SC", font_size=22,
                        color=WHITE)
        VGroup(aaa_tag, aaa_line)\
            .arrange(DOWN, buff=0.14).move_to(DOWN*1.0)

        self.play(FadeIn(aaa_bg), run_time=0.3)
        self.play(FadeIn(aaa_tag), FadeIn(aaa_line), run_time=0.45)

        trick_box = RoundedRectangle(
            width=7.8, height=1.1, corner_radius=0.3,
            color=self.C_HIGHLIGHT,
            fill_color=ManimColor(self.C_HIGHLIGHT).interpolate(BLACK, 0.87),
            fill_opacity=0.95
        ).move_to(DOWN*2.6)
        trick_txt = Text("记忆：夹边→ASA，对边→AAS",
                         font="Noto Sans CJK SC", font_size=25,
                         color=self.C_HIGHLIGHT).move_to(DOWN*2.6)
        self.play(FadeIn(trick_box), FadeIn(trick_txt), run_time=0.5)

        self.wait(1.3)

        self.play(
            FadeOut(sum_title),
            FadeOut(asa_bg), FadeOut(asa_tag), FadeOut(asa_line1), FadeOut(asa_line2),
            FadeOut(aas_bg), FadeOut(aas_tag), FadeOut(aas_line1), FadeOut(aas_line2),
            FadeOut(aaa_bg), FadeOut(aaa_tag), FadeOut(aaa_line),
            FadeOut(trick_box), FadeOut(trick_txt),
            run_time=0.6
        )

        outro_name = Text("上海初高中数学直通车",
                          font="Noto Sans CJK SC", font_size=44,
                          color=WHITE).move_to(UP*1.8)
        outro_id   = Text("@emptyandcalm",
                          font="Noto Sans CJK SC", font_size=32,
                          color=self.C_AUX).move_to(UP*0.8)
        cta        = Text("关注我，学更多数学技巧！",
                          font="Noto Sans CJK SC", font_size=30,
                          color=self.C_HIGHLIGHT).move_to(DOWN*0.4)

        self.play(Transform(self.author_bar, outro_name), run_time=0.65)
        self.play(FadeIn(outro_id, shift=UP*0.25), run_time=0.4)
        self.play(FadeIn(cta, shift=UP*0.2), run_time=0.5)

        def mini_tri(offset, color, scale=0.45):
            return Polygon(
                np.array([0, scale, 0]),
                np.array([-scale*0.9, -scale*0.5, 0]),
                np.array([ scale*0.9, -scale*0.5, 0]),
                fill_color=color, fill_opacity=0.75, stroke_width=0
            ).shift(offset)

        deco = VGroup(
            mini_tri(np.array([-2.0, -2.6, 0]), self.C_ASA),
            mini_tri(np.array([ 0.0, -2.9, 0]), self.C_CONGRUENT, scale=0.35),
            mini_tri(np.array([ 2.0, -2.6, 0]), self.C_AAS),
        )
        self.play(*[FadeIn(d, scale=0.3) for d in deco], run_time=0.55)
        self.play(Rotate(deco, angle=PI, run_time=1.2))
        self.wait(0.8)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(outro_id), FadeOut(cta), FadeOut(deco),
            run_time=1.0
        )


# ═══════════════════════════════════════════════════════
# 渲染命令
# ═══════════════════════════════════════════════════════
# 快速预览:  manim -pql asa_aas.py ASA_AAS
# 高质量:    manim -qh  asa_aas.py ASA_AAS