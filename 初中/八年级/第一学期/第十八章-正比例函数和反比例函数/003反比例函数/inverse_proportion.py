"""
inverse_proportion.py
=====================
反比例函数 — TikTok 竖屏教学动画
格式: 1080×1920 (frame_width=9, frame_height=16)
时长: ~65s  |  年级: 八年级

运行:
    manim -pqh --resolution 1080,1920 inverse_proportion.py InverseProportion
"""

from manim import *
import numpy as np

# ── 颜色 ──────────────────────────────────────────────
BG       = "#0D1B2A"
C_WHITE  = WHITE
C_GOLD   = "#FFD700"
C_BLUE   = "#4FC3F7"
C_GREEN  = "#66BB6A"
C_RED    = "#EF5350"
C_ORANGE = "#FFA726"
C_PURPLE = "#CE93D8"
C_GRAY   = "#78909C"
C_DIM    = "#2E4A5A"
C_BOX    = "#1A2E45"


class InverseProportion(Scene):

    def construct(self):
        self.camera.background_color = BG
        self.scene1_intro()
        self.scene2_definition()
        self.scene3_k_positive()
        self.scene4_k_negative()
        self.scene5_k_size()
        self.scene6_summary()

    # ── helpers ──────────────────────────────────────
    def _title(self, txt, color=C_WHITE, size=36):
        return Text(txt, font_size=size, color=color,
                    font="PingFang SC").move_to(UP * 4.5)

    def _clear(self, *objs):
        self.play(*[FadeOut(m) for m in objs], run_time=0.45)

    def _make_axes(self, x_range=(-4, 4, 1), y_range=(-4, 4, 1),
                   x_length=6.0, y_length=6.0, center=ORIGIN):
        ax = Axes(
            x_range=list(x_range),
            y_range=list(y_range),
            x_length=x_length,
            y_length=y_length,
            axis_config={
                "color": C_GRAY, "stroke_width": 1.8,
                "include_tip": True, "tip_length": 0.18,
                "include_numbers": True,
                "font_size": 16,
            },
        ).move_to(center)
        xlbl = MathTex(r"x", font_size=22, color=C_GRAY).next_to(
            ax.x_axis.get_right(), RIGHT, buff=0.05)
        ylbl = MathTex(r"y", font_size=22, color=C_GRAY).next_to(
            ax.y_axis.get_top(), UP, buff=0.05)
        return ax, VGroup(xlbl, ylbl)

    # ══════════════════════════════════════════════════
    # Scene 1: 生活引入 (0–7s)
    # ══════════════════════════════════════════════════
    def scene1_intro(self):
        title = self._title("反比例函数", color=C_GOLD, size=44)

        # 生活场景卡片
        scene_txt = Text("速度 × 时间 = 路程（固定）",
                         font_size=26, color=C_WHITE,
                         font="PingFang SC").move_to(UP * 3.0)

        # 两列对比
        left_arrow  = Arrow(ORIGIN, UP * 0.8, color=C_GREEN,
                            stroke_width=5, buff=0).move_to(LEFT*1.8 + UP*1.4)
        right_arrow = Arrow(ORIGIN, DOWN * 0.8, color=C_RED,
                            stroke_width=5, buff=0).move_to(RIGHT*1.8 + UP*1.4)
        left_lbl  = Text("速度 ↑", font_size=26, color=C_GREEN,
                         font="PingFang SC").next_to(left_arrow, DOWN, buff=0.12)
        right_lbl = Text("时间 ↓", font_size=26, color=C_RED,
                         font="PingFang SC").next_to(right_arrow, DOWN, buff=0.12)

        # 核心关系
        xy_formula = MathTex(r"xy = k", font_size=52, color=C_GOLD)
        xy_formula.move_to(DOWN * 0.3)
        xy_box = SurroundingRectangle(xy_formula, color=C_GOLD, buff=0.22,
                                      corner_radius=0.12)

        def_text = Text("k 固定，x 越大，y 越小",
                        font_size=26, color=C_BLUE,
                        font="PingFang SC").move_to(DOWN * 1.8)
        sub_text = Text("这就是「反比例」关系！",
                        font_size=28, color=C_GREEN,
                        font="PingFang SC").move_to(DOWN * 2.8)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(scene_txt), run_time=0.5)
        self.play(Create(left_arrow), Create(right_arrow), run_time=0.4)
        self.play(FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.4)
        self.play(GrowFromCenter(xy_formula), Create(xy_box), run_time=0.6)
        self.play(FadeIn(def_text), Write(sub_text), run_time=0.6)
        self.wait(1.2)
        self._clear(title, scene_txt, left_arrow, right_arrow,
                    left_lbl, right_lbl, xy_formula, xy_box,
                    def_text, sub_text)

    # ══════════════════════════════════════════════════
    # Scene 2: 函数定义式 (7–15s)
    # ══════════════════════════════════════════════════
    def scene2_definition(self):
        title = self._title("② 反比例函数定义", color=C_GOLD, size=34)

        # 大公式
        formula = MathTex(
            r"y = \dfrac{k}{x}", font_size=72, color=C_GOLD
        ).move_to(UP * 1.5)
        f_box = SurroundingRectangle(formula, color=C_GOLD, buff=0.28,
                                     corner_radius=0.14, stroke_width=2.5)

        cond = VGroup(
            MathTex(r"k \neq 0", font_size=32, color=C_ORANGE),
            Text("，", font_size=32, color=C_WHITE, font="PingFang SC"),
            MathTex(r"x \neq 0", font_size=32, color=C_RED),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.3)

        # k>0 / k<0 说明
        k_pos = VGroup(
            MathTex(r"k > 0", font_size=30, color=C_GREEN),
            Text("：图像在 一、三 象限", font_size=26, color=C_GREEN,
                 font="PingFang SC"),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.7)

        k_neg = VGroup(
            MathTex(r"k < 0", font_size=30, color=C_RED),
            Text("：图像在 二、四 象限", font_size=26, color=C_RED,
                 font="PingFang SC"),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.7)

        # 双曲线名称
        name = Text("图像是「双曲线」",
                    font_size=28, color=C_PURPLE,
                    font="PingFang SC").move_to(DOWN * 3.8)

        self.play(Write(title), run_time=0.6)
        self.play(Write(formula), Create(f_box), run_time=0.8)
        self.play(Circumscribe(formula, color=C_GOLD, run_time=0.8))
        self.play(FadeIn(cond), run_time=0.5)
        self.play(Write(k_pos), run_time=0.5)
        self.play(Write(k_neg), run_time=0.5)
        self.play(FadeIn(name), run_time=0.4)
        self.wait(1.2)
        self._clear(title, formula, f_box, cond, k_pos, k_neg, name)

    # ══════════════════════════════════════════════════
    # Scene 3: k>0 图像 (15–30s)
    # ══════════════════════════════════════════════════
    def scene3_k_positive(self):
        title = self._title("③ k>0：一、三象限", color=C_GREEN, size=32)
        subtitle = MathTex(r"y = \dfrac{2}{x}", font_size=36, color=C_GREEN
                           ).move_to(UP * 3.5)

        ax, ax_lbls = self._make_axes(center=ORIGIN)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)
        self.play(Create(ax), FadeIn(ax_lbls), run_time=0.7)

        # 双曲线两支（避开 x=0）
        branch_r = ax.plot(
            lambda x: 2 / x,
            x_range=[0.42, 4.0, 0.02],
            color=C_GREEN, stroke_width=3,
            use_smoothing=True,
        )
        branch_l = ax.plot(
            lambda x: 2 / x,
            x_range=[-4.0, -0.42, 0.02],
            color=C_GREEN, stroke_width=3,
            use_smoothing=True,
        )

        self.play(Create(branch_r), Create(branch_l), run_time=1.2)

        # 关键点
        pts_data = [(1, 2), (2, 1), (4, 0.5), (-1, -2), (-2, -1)]
        dots = VGroup(*[Dot(ax.c2p(x, y), color=C_ORANGE, radius=0.09)
                        for x, y in pts_data])
        pt_lbls = VGroup(*[
            MathTex(f"({x},{y})" if y == int(y) else f"({x},{y:.1f})",
                    font_size=16, color=C_ORANGE
                    ).next_to(ax.c2p(x, y),
                              UR if x > 0 else DL, buff=0.07)
            for x, y in pts_data
        ])

        self.play(FadeIn(dots), run_time=0.4)
        self.play(Write(pt_lbls), run_time=0.5)

        # 增减性说明（小箭头 + 文字）
        dec_r = Arrow(ax.c2p(1, 2), ax.c2p(2.5, 0.8),
                      color=C_GOLD, stroke_width=2.5,
                      tip_length=0.18, buff=0)
        dec_l = Arrow(ax.c2p(-1, -2), ax.c2p(-2.5, -0.8),
                      color=C_GOLD, stroke_width=2.5,
                      tip_length=0.18, buff=0)
        dec_lbl = Text("x增大，y减小",
                       font_size=22, color=C_GOLD,
                       font="PingFang SC").move_to(DOWN * 3.5)

        self.play(Create(dec_r), Create(dec_l), run_time=0.5)
        self.play(FadeIn(dec_lbl), run_time=0.4)

        # 渐近线说明
        asym_txt = Text("x轴、y轴是渐近线（永不相交）",
                        font_size=22, color=C_PURPLE,
                        font="PingFang SC").move_to(DOWN * 4.4)
        # 渐近线虚线
        x_asym = DashedLine(ax.c2p(-3.8, 0), ax.c2p(3.8, 0),
                             color=C_PURPLE, stroke_width=1.5,
                             dash_length=0.12)
        y_asym = DashedLine(ax.c2p(0, -3.8), ax.c2p(0, 3.8),
                             color=C_PURPLE, stroke_width=1.5,
                             dash_length=0.12)

        self.play(Create(x_asym), Create(y_asym), run_time=0.5)
        self.play(FadeIn(asym_txt), run_time=0.4)
        self.wait(1.5)

        # 保留坐标轴，淡化曲线准备 Scene4
        self.play(
            branch_r.animate.set_color(C_DIM).set_stroke(width=1.5),
            branch_l.animate.set_color(C_DIM).set_stroke(width=1.5),
            FadeOut(dots, pt_lbls, dec_r, dec_l, dec_lbl, asym_txt,
                    x_asym, y_asym, title, subtitle),
            run_time=0.6,
        )
        # 保留 ax, ax_lbls, branch_r, branch_l 给 Scene4
        self._k_pos_curves = (ax, ax_lbls, branch_r, branch_l)

    # ══════════════════════════════════════════════════
    # Scene 4: k<0 图像 (30–42s)
    # ══════════════════════════════════════════════════
    def scene4_k_negative(self):
        ax, ax_lbls, old_r, old_l = self._k_pos_curves

        title = self._title("④ k<0：二、四象限", color=C_RED, size=32)
        subtitle = MathTex(r"y = \dfrac{-2}{x}", font_size=36, color=C_RED
                           ).move_to(UP * 3.5)
        self.play(Write(title), FadeIn(subtitle), run_time=0.5)

        branch_r2 = ax.plot(
            lambda x: -2 / x,
            x_range=[0.42, 4.0, 0.02],
            color=C_RED, stroke_width=3,
        )
        branch_l2 = ax.plot(
            lambda x: -2 / x,
            x_range=[-4.0, -0.42, 0.02],
            color=C_RED, stroke_width=3,
        )
        self.play(Create(branch_r2), Create(branch_l2), run_time=1.0)

        # 关键点 (k<0)
        pts2 = [(1, -2), (2, -1), (-1, 2), (-2, 1)]
        dots2 = VGroup(*[Dot(ax.c2p(x, y), color=C_ORANGE, radius=0.09)
                         for x, y in pts2])
        pt_lbls2 = VGroup(*[
            MathTex(f"({x},{y})", font_size=16, color=C_ORANGE
                    ).next_to(ax.c2p(x, y),
                              DR if x > 0 else UL, buff=0.07)
            for x, y in pts2
        ])
        self.play(FadeIn(dots2), Write(pt_lbls2), run_time=0.6)

        # 增减性（k<0 每象限内 x增y也增）
        inc_r = Arrow(ax.c2p(2.5, -0.8), ax.c2p(1, -2),
                      color=C_GOLD, stroke_width=2.5,
                      tip_length=0.18, buff=0)
        inc_lbl = Text("x增大，y增大",
                       font_size=22, color=C_GOLD,
                       font="PingFang SC").move_to(DOWN * 3.5)
        self.play(Create(inc_r), FadeIn(inc_lbl), run_time=0.5)

        # 对比说明
        cmp = VGroup(
            Text("绿色：k>0（一三象限）", font_size=20, color=C_GREEN,
                 font="PingFang SC"),
            Text("红色：k<0（二四象限）", font_size=20, color=C_RED,
                 font="PingFang SC"),
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 4.4)
        self.play(FadeIn(cmp), run_time=0.5)
        self.wait(1.5)

        self._clear(title, subtitle, branch_r2, branch_l2,
                    dots2, pt_lbls2, inc_r, inc_lbl,
                    old_r, old_l, cmp, ax, ax_lbls)

    # ══════════════════════════════════════════════════
    # Scene 5: |k| 大小影响图像 (42–52s)
    # ══════════════════════════════════════════════════
    def scene5_k_size(self):
        title = self._title("⑤ |k| 越大，图像越远离坐标轴", color=C_GOLD, size=28)

        ax, ax_lbls = self._make_axes(center=ORIGIN)
        self.play(Write(title), Create(ax), FadeIn(ax_lbls), run_time=0.7)

        k_configs = [
            (1, C_BLUE,   r"k=1"),
            (2, C_GOLD,   r"k=2"),
            (4, C_ORANGE, r"k=4"),
        ]

        curves = []
        for k, col, lbl_str in k_configs:
            br = ax.plot(lambda x, k=k: k/x, x_range=[0.28, 4.0, 0.02],
                         color=col, stroke_width=2.5)
            bl = ax.plot(lambda x, k=k: k/x, x_range=[-4.0, -0.28, 0.02],
                         color=col, stroke_width=2.5)
            lbl = MathTex(lbl_str, font_size=24, color=col)
            # 标注在右支右端
            lbl.next_to(ax.c2p(3.5, k/3.5), RIGHT, buff=0.08)
            curves.append((br, bl, lbl))
            self.play(Create(br), Create(bl), FadeIn(lbl), run_time=0.55)

        # 箭头说明
        arr_txt = Text("|k| 越大 → 图像越远离原点",
                       font_size=24, color=C_GOLD,
                       font="PingFang SC").move_to(DOWN * 4.0)
        self.play(FadeIn(arr_txt), run_time=0.4)
        self.wait(1.5)

        all_objs = [title, ax, ax_lbls, arr_txt]
        for br, bl, lbl in curves:
            all_objs.extend([br, bl, lbl])
        self._clear(*all_objs)

    # ══════════════════════════════════════════════════
    # Scene 6: 总结 (52–65s)
    # ══════════════════════════════════════════════════
    def scene6_summary(self):
        title = self._title("📌 核心性质总结", color=C_GOLD, size=36)

        slogans = [
            ("k>0：一、三象限，每象限内 y 减", C_GREEN),
            ("k<0：二、四象限，每象限内 y 增", C_RED),
            ("双曲线不与坐标轴相交", C_PURPLE),
        ]
        slogan_grp = VGroup(*[
            Text(s, font_size=28, color=c, font="PingFang SC")
            for s, c in slogans
        ]).arrange(DOWN, buff=0.5).move_to(UP * 1.8)

        big_f = MathTex(r"y = \dfrac{k}{x}", font_size=72, color=C_GOLD
                        ).move_to(DOWN * 1.2)
        big_box = SurroundingRectangle(big_f, color=C_GOLD, buff=0.3,
                                       corner_radius=0.14, stroke_width=3)

        bottom = Text("学会了吗？👍",
                      font_size=28, color=C_WHITE,
                      font="PingFang SC").move_to(DOWN * 3.2)

        self.play(Write(title), run_time=0.6)
        for line in slogan_grp:
            self.play(Write(line), run_time=0.55)
        self.play(GrowFromCenter(big_f), Create(big_box), run_time=0.8)
        self.play(Flash(big_f, color=C_GOLD, flash_radius=1.8,
                        line_length=0.35, num_lines=12), run_time=0.8)
        self.play(FadeIn(bottom), run_time=0.5)
        self.wait(2.5)