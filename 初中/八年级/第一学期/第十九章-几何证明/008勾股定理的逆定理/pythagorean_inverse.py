"""
pythagorean_inverse.py
======================
勾股定理的逆定理 — TikTok 竖屏教学动画
格式: 1080×1920 (9:16)
时长: ~60s
受众: 八年级学生

运行命令:
    manim -pqh pythagorean_inverse.py PythagoreanInverse
    # 竖屏需要配置:
    manim -pqh --resolution 1080,1920 pythagorean_inverse.py PythagoreanInverse
"""

from manim import *
import numpy as np

# ── 颜色主题 ─────────────────────────────────────────────
BG_COLOR       = "#0D1B2A"   # 深蓝背景
TITLE_COLOR    = WHITE
ACCENT_GOLD    = "#FFD700"   # 金色强调
ACCENT_GREEN   = "#4CAF50"   # 验证成功绿
ACCENT_BLUE    = "#4FC3F7"   # 浅蓝（三角形）
ACCENT_RED     = "#EF5350"   # 错误/对比红
STEP_COLOR     = "#E0E0E0"   # 计算步骤文字
BOX_COLOR      = "#1E3A5F"   # 文字框背景


# ── 竖屏配置 ─────────────────────────────────────────────
# 在 manim.cfg 中设置或通过命令行传入:
#   frame_height = 16
#   frame_width  = 9
# 本文件内坐标基于 frame_height=16 / frame_width=9
# 若使用默认配置(8×14.2)，坐标会等比缩放

class PythagoreanInverse(Scene):
    """勾股定理的逆定理 — 完整教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene1_intro()
        self.scene2_forward()
        self.scene3_inverse_concept()
        self.scene4_example_345()
        self.scene5_pythagorean_triples()
        self.scene6_summary()

    # ══════════════════════════════════════════════════════
    # Scene 1: 片头引入 (0–5s)
    # ══════════════════════════════════════════════════════
    def scene1_intro(self):
        # 标题
        title = Text(
            "如何判断直角三角形？",
            font_size=38,
            color=WHITE,
            font="PingFang SC",
        ).move_to(UP * 3.5)

        # 三个不同三角形（直角/锐角/钝角）
        tri_right = Polygon(
            [-0.8, -0.8, 0], [0.8, -0.8, 0], [-0.8, 0.8, 0],
            color=ACCENT_BLUE, fill_opacity=0.35,
        ).scale(0.9).move_to(LEFT * 2.2 + UP * 0.5)

        tri_acute = Polygon(
            [-0.6, -0.7, 0], [0.6, -0.7, 0], [0.0, 0.7, 0],
            color=WHITE, fill_opacity=0.25,
        ).scale(0.9).move_to(UP * 0.5)

        tri_obtuse = Polygon(
            [-0.9, -0.5, 0], [0.9, -0.5, 0], [0.6, 0.7, 0],
            color=ACCENT_RED, fill_opacity=0.25,
        ).scale(0.9).move_to(RIGHT * 2.2 + UP * 0.5)

        # 问号
        q1 = Text("?", font_size=44, color=ACCENT_GOLD).next_to(tri_right, UP, buff=0.2)
        q2 = Text("?", font_size=44, color=ACCENT_GOLD).next_to(tri_acute, UP, buff=0.2)
        q3 = Text("?", font_size=44, color=ACCENT_GOLD).next_to(tri_obtuse, UP, buff=0.2)

        self.play(Write(title), run_time=1.2)
        self.play(
            GrowFromCenter(tri_right),
            GrowFromCenter(tri_acute),
            GrowFromCenter(tri_obtuse),
            run_time=1.0,
        )
        self.play(FadeIn(q1), FadeIn(q2), FadeIn(q3), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(tri_right), FadeOut(tri_acute),
            FadeOut(tri_obtuse), FadeOut(q1), FadeOut(q2), FadeOut(q3),
            run_time=0.6,
        )

    # ══════════════════════════════════════════════════════
    # Scene 2: 回顾勾股定理正向 (5–13s)
    # ══════════════════════════════════════════════════════
    def scene2_forward(self):
        title = Text("① 回顾：勾股定理", font_size=34, color=ACCENT_BLUE).move_to(UP * 4.3)

        # 等腰直角三角形
        # A=(-1.5,-1.5) 直角顶点, B=(1.5,-1.5), C=(-1.5,1.5)
        A = np.array([-1.5, -1.5, 0])
        B = np.array([ 1.5, -1.5, 0])
        C = np.array([-1.5,  1.5, 0])

        triangle = Polygon(A, B, C,
            color=ACCENT_BLUE, fill_color=ACCENT_BLUE, fill_opacity=0.25,
            stroke_width=2.5,
        ).move_to(UP * 0.5)
        # 偏移后实际顶点（triangle已移动，用参考偏移量）
        offset = UP * 0.5

        # 直角标记
        right_mark = RightAngle(
            Line(B + offset, A + offset),
            Line(A + offset, C + offset),
            length=0.25, color=WHITE,
        )

        # 边标注（紧贴三角形，留0.3 buff）
        lbl_a = MathTex("a", color=ACCENT_GOLD, font_size=32).move_to(
            np.array([-2.05, -0.0, 0]) + offset  # 左边 AC 中点左侧
        )
        lbl_b = MathTex("b", color=ACCENT_GOLD, font_size=32).move_to(
            np.array([0.0, -2.05, 0]) + offset  # 底边 AB 下方
        )
        lbl_c = MathTex("c", color=ACCENT_GOLD, font_size=32).move_to(
            np.array([0.45, 0.15, 0]) + offset  # 斜边 BC 旁
        )

        # 条件文字
        cond = Text("已知 ∠A = 90°", font_size=28, color=WHITE).move_to(DOWN * 2.5 + offset)

        # 公式框
        formula = MathTex(r"a^2 + b^2 = c^2", font_size=42, color=ACCENT_GOLD)
        formula_box = SurroundingRectangle(formula, color=ACCENT_GOLD, buff=0.2, corner_radius=0.1)
        formula_grp = VGroup(formula, formula_box).move_to(DOWN * 3.5)

        self.play(FadeIn(title), run_time=0.5)
        self.play(DrawBorderThenFill(triangle), run_time=1.0)
        self.play(Create(right_mark), run_time=0.4)
        self.play(Write(lbl_a), Write(lbl_b), run_time=0.5)
        self.play(Write(lbl_c), run_time=0.4)
        self.play(FadeIn(cond), run_time=0.4)
        self.play(Write(formula), Create(formula_box), run_time=0.8)
        self.wait(1.2)

        scene2_objs = VGroup(
            title, triangle, right_mark, lbl_a, lbl_b, lbl_c, cond, formula, formula_box
        )
        self.play(FadeOut(scene2_objs), run_time=0.5)

    # ══════════════════════════════════════════════════════
    # Scene 3: 逆定理核心概念 (13–23s)
    # ══════════════════════════════════════════════════════
    def scene3_inverse_concept(self):
        title = Text("② 逆定理：反过来也成立！", font_size=34, color=ACCENT_GOLD).move_to(UP * 4.3)

        # 正向框
        fwd_text = MathTex(
            r"\angle C = 90°", r"\Rightarrow", r"a^2+b^2=c^2",
            font_size=30,
        )
        fwd_text[0].set_color(ACCENT_BLUE)
        fwd_text[2].set_color(ACCENT_GOLD)
        fwd_box = SurroundingRectangle(fwd_text, color=ACCENT_BLUE, buff=0.18, corner_radius=0.08)
        fwd_grp = VGroup(fwd_text, fwd_box).move_to(UP * 2.0)

        # 大反向箭头
        flip_arrow = Arrow(
            start=LEFT * 1.2, end=RIGHT * 1.2,
            color=ACCENT_GOLD, stroke_width=4, tip_length=0.3,
        ).move_to(UP * 0.8)
        flip_label = Text("逆定理 ↩", font_size=26, color=ACCENT_GOLD).next_to(flip_arrow, UP, buff=0.1)

        # 逆向框
        inv_text = MathTex(
            r"a^2+b^2=c^2", r"\Rightarrow", r"\angle C = 90°",
            font_size=30,
        )
        inv_text[0].set_color(ACCENT_GOLD)
        inv_text[2].set_color(ACCENT_GREEN)
        inv_box = SurroundingRectangle(inv_text, color=ACCENT_GREEN, buff=0.18, corner_radius=0.08)
        inv_grp = VGroup(inv_text, inv_box).move_to(DOWN * 0.3)

        # 核心定理大框
        core_lines = VGroup(
            Text("勾股定理的逆定理", font_size=30, color=ACCENT_GOLD),
            MathTex(r"a^2 + b^2 = c^2", font_size=34, color=WHITE),
            Text("则 △ABC 是直角三角形", font_size=28, color=ACCENT_GREEN),
            MathTex(r"\Rightarrow \angle C = 90^\circ", font_size=34, color=ACCENT_GREEN),
        ).arrange(DOWN, buff=0.22).move_to(DOWN * 2.8)
        core_box = SurroundingRectangle(
            core_lines, color=ACCENT_GREEN, buff=0.28,
            corner_radius=0.15, stroke_width=2.5,
        )
        core_grp = VGroup(core_lines, core_box)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(fwd_grp), run_time=0.6)
        self.play(GrowArrow(flip_arrow), Write(flip_label), run_time=0.7)
        self.play(FadeIn(inv_grp), run_time=0.6)
        self.wait(0.5)
        self.play(GrowFromCenter(core_grp), run_time=1.0)
        self.play(Indicate(core_grp, color=ACCENT_GOLD, scale_factor=1.04), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, fwd_grp, flip_arrow, flip_label, inv_grp, core_grp)),
            run_time=0.6,
        )

    # ══════════════════════════════════════════════════════
    # Scene 4: 3-4-5 例题验证 (23–43s)
    # ══════════════════════════════════════════════════════
    def scene4_example_345(self):
        # 题目说明
        prob_title = Text("③ 例题验证", font_size=34, color=WHITE).move_to(UP * 4.3)
        prob_sub   = Text(
            "三角形三边为 3、4、5，是直角三角形吗？",
            font_size=26, color=STEP_COLOR,
        ).move_to(UP * 3.5)

        self.play(Write(prob_title), FadeIn(prob_sub), run_time=0.8)

        # ── 三角形 ──────────────────────────────────────
        # A=(-2,-2) 直角顶点, B=(2,-2), C=(-2,1)，整体上移 1 单位
        off = np.array([0.0, 1.0, 0.0])
        A = np.array([-2.0, -2.0, 0.0]) + off
        B = np.array([ 2.0, -2.0, 0.0]) + off
        C = np.array([-2.0,  1.0, 0.0]) + off

        # 初始灰色（未证明）
        tri = Polygon(A, B, C,
            color=GRAY, fill_color=GRAY, fill_opacity=0.2,
            stroke_width=2.5,
        )

        # 边标注
        mid_AC = (A + C) / 2
        mid_AB = (A + B) / 2
        mid_BC = (B + C) / 2

        lbl_a = MathTex("a=3", font_size=28, color=ACCENT_GOLD).move_to(mid_AC + np.array([-0.55, 0, 0]))
        lbl_b = MathTex("b=4", font_size=28, color=ACCENT_GOLD).move_to(mid_AB + np.array([0, -0.45, 0]))
        lbl_c = MathTex("c=5", font_size=28, color=ACCENT_GOLD).move_to(mid_BC + np.array([0.5, 0.1, 0]))

        self.play(DrawBorderThenFill(tri), run_time=1.0)
        self.play(Write(lbl_a), Write(lbl_b), Write(lbl_c), run_time=0.7)

        # ── 计算步骤（下方区域）───────────────────────
        step_y_start = -2.2  # 三角形下方
        step_gap = 0.62
        steps = [
            (r"a^2 + b^2 = 3^2 + 4^2 = 9 + 16 = 25", WHITE),
            (r"c^2 = 5^2 = 25",                         WHITE),
            (r"\therefore\ a^2 + b^2 = c^2 \checkmark", ACCENT_GREEN),
        ]
        step_mobjs = []
        for i, (tex, col) in enumerate(steps):
            s = MathTex(tex, font_size=28, color=col).move_to(
                np.array([0.0, step_y_start - i * step_gap, 0.0])
            )
            step_mobjs.append(s)

        for s in step_mobjs[:2]:
            self.play(Write(s), run_time=0.7)
        self.play(Write(step_mobjs[2]), run_time=0.8)

        # ── 三角形变绿，出现直角标记 ─────────────────
        tri_green = Polygon(A, B, C,
            color=ACCENT_GREEN, fill_color=ACCENT_GREEN, fill_opacity=0.3,
            stroke_width=2.5,
        )
        right_mark = RightAngle(
            Line(B, A), Line(A, C),
            length=0.28, color=WHITE,
        )

        self.play(
            Transform(tri, tri_green),
            run_time=0.6,
        )
        self.play(Create(right_mark), run_time=0.5)

        # ── 结论文字 ──────────────────────────────────
        conclusion = Text(
            "△ABC 是直角三角形！",
            font_size=32, color=ACCENT_GREEN,
        ).move_to(np.array([0.0, step_y_start - 3 * step_gap, 0.0]))
        conc_box = SurroundingRectangle(conclusion, color=ACCENT_GREEN, buff=0.15, corner_radius=0.1)
        conc_grp = VGroup(conclusion, conc_box)

        self.play(GrowFromCenter(conc_grp), run_time=0.7)
        self.play(Indicate(conc_grp, color=ACCENT_GOLD, scale_factor=1.06), run_time=0.7)
        self.wait(1.5)

        scene4_objs = VGroup(
            prob_title, prob_sub, tri, lbl_a, lbl_b, lbl_c,
            right_mark, conc_grp, *step_mobjs
        )
        self.play(FadeOut(scene4_objs), run_time=0.6)

    # ══════════════════════════════════════════════════════
    # Scene 5: 常见勾股数表 (43–53s)
    # ══════════════════════════════════════════════════════
    def scene5_pythagorean_triples(self):
        title = Text("④ 常用勾股数组", font_size=34, color=ACCENT_GOLD).move_to(UP * 4.3)
        subtitle = Text("记住它们，判题更快！", font_size=26, color=STEP_COLOR).move_to(UP * 3.5)

        # 表格数据
        triples = [
            ("3", "4", "5"),
            ("5", "12", "13"),
            ("8", "15", "17"),
        ]
        col_x = {"a": -2.0, "b": -0.3, "c": 1.4, "check": 2.6}
        row_y = [2.0, 0.6, -0.8]

        # 表头
        hdr_a = MathTex("a", font_size=30, color=ACCENT_BLUE).move_to([col_x["a"], 3.0, 0])
        hdr_b = MathTex("b", font_size=30, color=ACCENT_BLUE).move_to([col_x["b"], 3.0, 0])
        hdr_c = MathTex("c", font_size=30, color=ACCENT_BLUE).move_to([col_x["c"], 3.0, 0])
        hdr_v = Text("验证", font_size=26, color=ACCENT_BLUE).move_to([col_x["check"], 3.0, 0])
        hdr_line = Line(
            start=[-2.8, 2.65, 0], end=[3.0, 2.65, 0],
            color=ACCENT_BLUE, stroke_width=1.5,
        )
        headers = VGroup(hdr_a, hdr_b, hdr_c, hdr_v, hdr_line)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)
        self.play(FadeIn(headers), run_time=0.5)

        row_objs = []
        for i, (a, b, c) in enumerate(triples):
            y = row_y[i]
            ma = MathTex(a, font_size=32, color=WHITE).move_to([col_x["a"], y, 0])
            mb = MathTex(b, font_size=32, color=WHITE).move_to([col_x["b"], y, 0])
            mc = MathTex(c, font_size=32, color=WHITE).move_to([col_x["c"], y, 0])
            check = Text("✓", font_size=30, color=ACCENT_GREEN).move_to([col_x["check"], y, 0])
            # 验证公式（右侧小字）
            formula_str = f"{a}^2+{b}^2={c}^2"
            vf = MathTex(formula_str, font_size=20, color=GRAY).move_to(
                [col_x["check"] + 1.5, y, 0]
            )
            row_grp = VGroup(ma, mb, mc)
            self.play(FadeIn(row_grp), run_time=0.5)
            self.play(FadeIn(check), run_time=0.3)
            row_objs.extend([ma, mb, mc, check])

        # 提示
        tip = Text(
            "💡 整数倍也是勾股数：6-8-10, 9-12-15…",
            font_size=22, color=ACCENT_GOLD,
        ).move_to(DOWN * 2.3)
        self.play(Write(tip), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, subtitle, headers, tip, *row_objs)),
            run_time=0.6,
        )

    # ══════════════════════════════════════════════════════
    # Scene 6: 总结 (53–60s)
    # ══════════════════════════════════════════════════════
    def scene6_summary(self):
        # 核心公式
        formula = MathTex(
            r"a^2 + b^2 = c^2",
            r"\Longrightarrow",
            r"\angle C = 90^\circ",
            font_size=40,
        )
        formula[0].set_color(ACCENT_GOLD)
        formula[1].set_color(WHITE)
        formula[2].set_color(ACCENT_GREEN)
        f_box = SurroundingRectangle(formula, color=ACCENT_GOLD, buff=0.25, corner_radius=0.12, stroke_width=2.5)
        f_grp = VGroup(formula, f_box).move_to(UP * 1.5)

        # 小三角形示意
        off = np.array([0.0, -1.0, 0.0])
        tA = np.array([-1.5, -0.8, 0.0]) + off
        tB = np.array([ 1.5, -0.8, 0.0]) + off
        tC = np.array([-1.5,  0.5, 0.0]) + off
        sum_tri = Polygon(tA, tB, tC,
            color=ACCENT_GREEN, fill_color=ACCENT_GREEN, fill_opacity=0.3,
            stroke_width=2.5,
        )
        sum_right = RightAngle(
            Line(tB, tA), Line(tA, tC),
            length=0.25, color=WHITE,
        )

        # 底部口诀
        slogan = Text(
            "判定直角三角形的秘密武器 🎯",
            font_size=28, color=WHITE,
        ).move_to(DOWN * 3.5)

        self.play(Write(formula), Create(f_box), run_time=1.0)
        self.play(Circumscribe(f_grp, color=ACCENT_GOLD, run_time=1.0))
        self.play(GrowFromCenter(sum_tri), run_time=0.7)
        self.play(Create(sum_right), run_time=0.4)
        self.play(
            Rotate(sum_tri, angle=TAU, about_point=sum_tri.get_center()),
            run_time=2.0,
        )
        self.play(FadeIn(slogan), run_time=0.6)
        self.play(Flash(f_grp, color=ACCENT_GOLD, flash_radius=1.8, line_length=0.4), run_time=0.8)
        self.wait(1.5)