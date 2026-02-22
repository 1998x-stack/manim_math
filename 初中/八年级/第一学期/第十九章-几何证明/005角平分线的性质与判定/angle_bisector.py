"""
angle_bisector.py
角平分线的性质与判定 - 教学动画 (TikTok 竖屏)

目标: 八年级, 介绍角平分线性质与判定定理
格式: 1080x1920, 9x16 逻辑坐标
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===================================================
# 全局配置 — TikTok 竖屏
# ===================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT_CN = "Noto Sans CJK SC"


class AngleBisectorProperties(Scene):
    """
    角平分线性质与判定动画 (7 scenes, ~65 seconds)

    Scene 1  开场钩子
    Scene 2  引入角 ∠AOB
    Scene 3  画角平分线
    Scene 4  性质：平分线上的点到两边等距
    Scene 5  判定：等距点在平分线上
    Scene 6  总结对比（性质 ↔ 判定）
    Scene 7  片尾
    """

    # ===================================================
    # 颜色配置
    # ===================================================
    COL_RAY    = WHITE
    COL_ANGLE  = "#4fc3f7"   # 浅蓝 — 角弧
    COL_BIS    = "#ff8a65"   # 橙色 — 角平分线
    COL_DIST   = "#f48fb1"   # 粉红 — 距离线 PD / PE
    COL_PT_P   = "#ce93d8"   # 紫色 — 点 P
    COL_PT_Q   = "#80cbc4"   # 青绿 — 点 Q
    COL_EQUAL  = "#a5d6a7"   # 浅绿 — 相等标注
    COL_FORM   = GOLD        # 黄金 — 公式框
    COL_PROP   = "#4fc3f7"   # 浅蓝 — 性质标题
    COL_CRIT   = "#ffcc80"   # 浅橙 — 判定标题

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.setup_geometry()

        self.scene_opening()
        self.scene_intro_angle()
        self.scene_draw_bisector()
        self.scene_property()
        self.scene_criterion()
        self.scene_summary()
        self.scene_outro()

    # ===================================================
    # 几何数据初始化（精确计算，无臆想坐标）
    # ===================================================
    def setup_geometry(self):
        """
        角 ∠AOB：顶点 O，OA 水平向右，OB 偏上 70°
        平分线方向 35°
        """
        DEG = np.pi / 180

        # ---- 角度参数 ----
        self.ANGLE_TOTAL = 70 * DEG
        self.ANGLE_HALF  = 35 * DEG
        self.RAY_LEN     = 4.0
        self.BIS_LEN     = 3.8

        # ---- 顶点 & 方向向量 ----
        self.O = np.array([-1.0, -0.5, 0])
        self.OA_dir = np.array([1.0, 0.0, 0])
        self.OB_dir = np.array([np.cos(self.ANGLE_TOTAL),
                                 np.sin(self.ANGLE_TOTAL), 0])
        self.BIS_dir = np.array([np.cos(self.ANGLE_HALF),
                                  np.sin(self.ANGLE_HALF), 0])

        # ---- 射线端点 ----
        self.A = self.O + self.RAY_LEN * self.OA_dir
        self.B = self.O + self.RAY_LEN * self.OB_dir
        self.C = self.O + self.BIS_LEN * self.BIS_dir  # 平分线端点

        # ---- P：平分线上点（用于性质演示）----
        self.P = self.O + 2.0 * self.BIS_dir

        # ---- D = P 到 OA 的垂足（精确公式）----
        # OA 为水平线，垂足即 x=P[0], y=O[1]
        t_D = np.dot(self.P - self.O, self.OA_dir)
        self.D = self.O + t_D * self.OA_dir

        # ---- E = P 到 OB 的垂足（精确公式）----
        t_E = np.dot(self.P - self.O, self.OB_dir)
        self.E = self.O + t_E * self.OB_dir

        # ---- 距离缓存 ----
        self.PD = np.linalg.norm(self.P - self.D)
        self.PE = np.linalg.norm(self.P - self.E)

        # ---- Q：判定演示点（先在非平分线位置，动画中移动到等距位置）----
        # Q_start: 偏向 OA 一侧
        self.Q_start = self.O + 2.7 * np.array(
            [np.cos(self.ANGLE_HALF * 0.4),
             np.sin(self.ANGLE_HALF * 0.4), 0])
        # Q_end: 在平分线上（等距位置）
        self.Q_end = self.O + 2.7 * self.BIS_dir

        # ---- Q_end 的垂足 ----
        t_Dq = np.dot(self.Q_end - self.O, self.OA_dir)
        self.D_q = self.O + t_Dq * self.OA_dir
        t_Eq = np.dot(self.Q_end - self.O, self.OB_dir)
        self.E_q = self.O + t_Eq * self.OB_dir

        # ---- 验证 ----
        assert abs(self.PD - self.PE) < 1e-9, "PD ≠ PE，几何计算错误！"
        assert abs(np.linalg.norm(self.Q_end - self.D_q) -
                   np.linalg.norm(self.Q_end - self.E_q)) < 1e-9, "Q等距验证失败"
        print(f"✓ 几何验证: ∠AOB=70°, PD=PE={self.PD:.4f}")

    # ===================================================
    # 辅助：直角标记（小正方形）
    # ===================================================
    def _right_angle_mark(self, corner, toward_p, toward_line, size=0.18):
        """
        在 corner 处绘制直角标记
        toward_p   : 指向垂线方向的点（e.g. P）
        toward_line: 沿射线方向的点（e.g. A 或 B）
        """
        v1 = (toward_p    - corner)
        v2 = (toward_line - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner,
            corner + v2,
            corner + v1 + v2,
            corner + v1,
            color=YELLOW, stroke_width=1.8, fill_opacity=0
        )

    # ===================================================
    # 辅助：标注 "=" 等号标记（在线段中点旁）
    # ===================================================
    def _equal_tick(self, p1, p2, col=None, n=1):
        """
        在线段 p1-p2 中点处绘制 1 或 2 条刻度线（表示等长）
        """
        col = col or self.COL_EQUAL
        mid = (p1 + p2) / 2
        direction = p2 - p1
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])
        tick_size = 0.13
        spacing = 0.09
        ticks = VGroup()
        offsets = [0] if n == 1 else [-spacing / 2, spacing / 2]
        for off in offsets:
            center = mid + direction * off
            t = Line(
                center - perp * tick_size,
                center + perp * tick_size,
                color=col, stroke_width=2.5
            )
            ticks.add(t)
        return ticks

    # ===================================================
    # 辅助：节标题
    # ===================================================
    def _section_header(self, badge_str, title_str, badge_col=None, title_size=27):
        badge_col = badge_col or self.COL_FORM
        badge = Text(badge_str, font=FONT_CN, font_size=32, color=badge_col
                    ).move_to(UP * 5.6 + LEFT * 2.8)
        title = Text(title_str, font=FONT_CN, font_size=title_size, color=WHITE
                    ).next_to(badge, RIGHT, buff=0.22)
        return badge, title

    # ===================================================
    # Scene 1: 开场钩子 (~0-4s)
    # ===================================================
    def scene_opening(self):
        # 作者标识
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT_CN, font_size=17, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.3)

        # 大钩子
        hook1 = Text("角平分线", font=FONT_CN, font_size=56, color=self.COL_FORM
                    ).move_to(UP * 6.0)
        hook2 = Text("性质 与 判定", font=FONT_CN, font_size=38, color=WHITE
                    ).move_to(UP * 5.1)
        self.play(Write(hook1), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.4)

        # 两行预览
        prop_prev = Text(
            "性质: 平分线上的点到两边等距",
            font=FONT_CN, font_size=23, color=self.COL_PROP
        ).move_to(DOWN * 4.5)
        crit_prev = Text(
            "判定: 等距点在角平分线上",
            font=FONT_CN, font_size=23, color=self.COL_CRIT
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(prop_prev, shift=RIGHT * 0.3), run_time=0.3)
        self.play(FadeIn(crit_prev, shift=RIGHT * 0.3), run_time=0.3)
        self.wait(0.6)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(prop_prev), FadeOut(crit_prev),
            run_time=0.5
        )

    # ===================================================
    # Scene 2: 引入角 ∠AOB (~4-10s)
    # ===================================================
    def scene_intro_angle(self):
        badge, title = self._section_header("引入", "认识角 ∠AOB")
        self.play(Write(badge), FadeIn(title), run_time=0.5)

        # 画两条射线 (Manim 无 Ray 类，用 Line 代替；端点已按 RAY_LEN 延伸到位)
        self.ray_OA = Line(self.O, self.A, color=self.COL_RAY, stroke_width=3)
        self.ray_OB = Line(self.O, self.B, color=self.COL_RAY, stroke_width=3)

        # 顶点 O
        self.o_dot = Dot(self.O, color=YELLOW, radius=0.1)
        self.o_lbl = Text("O", font=FONT_CN, font_size=22, color=YELLOW
                         ).next_to(self.O, DL, buff=0.15)

        self.play(
            Create(self.ray_OA), Create(self.ray_OB),
            run_time=0.8
        )
        self.play(FadeIn(self.o_dot), Write(self.o_lbl), run_time=0.4)

        # 端点标签 A, B
        a_lbl = Text("A", font=FONT_CN, font_size=22, color=WHITE
                    ).next_to(self.A, RIGHT, buff=0.12)
        b_lbl = Text("B", font=FONT_CN, font_size=22, color=WHITE
                    ).next_to(self.B, UR, buff=0.12)
        self.play(FadeIn(a_lbl), FadeIn(b_lbl), run_time=0.4)

        # 角弧: from_three_points(A, O, B) → CCW 70° ✓ (cross_z > 0)
        self.angle_arc = Angle.from_three_points(
            self.A, self.O, self.B,
            radius=0.7, color=self.COL_ANGLE, stroke_width=2.5
        )
        # 角度标签放在角平分线方向
        ang_lbl_pos = self.O + 1.15 * self.BIS_dir
        ang_lbl = MathTex(r"70^\circ", color=self.COL_ANGLE, font_size=28
                         ).move_to(ang_lbl_pos)

        self.play(Create(self.angle_arc), run_time=0.6)
        self.play(Write(ang_lbl), run_time=0.4)

        # 说明
        explain = Text(
            "∠AOB 由两条射线 OA、OB 组成",
            font=FONT_CN, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(badge), FadeOut(title),
            FadeOut(explain), FadeOut(ang_lbl),
            run_time=0.5
        )
        # 保留: ray_OA, ray_OB, o_dot, o_lbl, angle_arc, a_lbl, b_lbl
        self.a_lbl = a_lbl
        self.b_lbl = b_lbl

    # ===================================================
    # Scene 3: 画角平分线 (~10-17s)
    # ===================================================
    def scene_draw_bisector(self):
        badge, title = self._section_header("角平分线", "把角分成两个相等的角")
        self.play(Write(badge), FadeIn(title), run_time=0.5)

        # 角弧闪烁提示
        self.play(Flash(self.angle_arc, color=self.COL_ANGLE, flash_radius=0.5),
                  run_time=0.5)

        # 画角平分线 OC（虚线 → 实线动效）
        self.bisector = Line(self.O, self.C, color=self.COL_BIS, stroke_width=3.5)
        c_lbl = Text("C", font=FONT_CN, font_size=22, color=self.COL_BIS
                    ).next_to(self.C, UR, buff=0.12)
        self.play(Create(self.bisector), run_time=1.0)
        self.play(FadeIn(c_lbl), run_time=0.3)

        # 两个半角弧（各35°）
        # 半角弧1: from_three_points(A, O, C) — CCW 35° ✓
        half_arc1 = Angle.from_three_points(
            self.A, self.O, self.C,
            radius=0.5, color=self.COL_ANGLE, stroke_width=2
        )
        # 半角弧2: from_three_points(C, O, B) — CCW 35° ✓
        half_arc2 = Angle.from_three_points(
            self.C, self.O, self.B,
            radius=0.65, color=self.COL_ANGLE, stroke_width=2
        )
        # 35° 标签
        lbl1 = MathTex(r"35^\circ", color=self.COL_ANGLE, font_size=22
                      ).move_to(self.O + 0.85 * np.array(
                          [np.cos(17.5 * np.pi/180), np.sin(17.5 * np.pi/180), 0]))
        lbl2 = MathTex(r"35^\circ", color=self.COL_ANGLE, font_size=22
                      ).move_to(self.O + 1.05 * np.array(
                          [np.cos(52.5 * np.pi/180), np.sin(52.5 * np.pi/180), 0]))

        self.play(
            ReplacementTransform(self.angle_arc, VGroup(half_arc1, half_arc2)),
            run_time=0.7
        )
        self.play(FadeIn(lbl1), FadeIn(lbl2), run_time=0.4)

        # 说明文字
        explain = Text(
            "OC 把 ∠AOB 平分为两个 35° 角",
            font=FONT_CN, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.2)
        sub_exp = Text(
            "OC 就是 ∠AOB 的角平分线",
            font=FONT_CN, font_size=24, color=self.COL_BIS
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(explain), FadeIn(sub_exp), run_time=0.5)
        self.wait(1.2)

        # 清理（保留射线、O点、O标签、平分线、A/B/C标签）
        self.play(
            FadeOut(badge), FadeOut(title),
            FadeOut(half_arc1), FadeOut(half_arc2),
            FadeOut(lbl1), FadeOut(lbl2),
            FadeOut(explain), FadeOut(sub_exp),
            FadeOut(c_lbl),
            run_time=0.5
        )

    # ===================================================
    # Scene 4: 性质 — 平分线上的点到两边等距 (~17-30s)
    # ===================================================
    def scene_property(self):
        badge, title = self._section_header(
            "性质", "平分线上的点到两边等距", badge_col=self.COL_PROP
        )
        self.play(Write(badge), FadeIn(title), run_time=0.5)

        # 1. 标记点 P 在平分线上
        p_dot = Dot(self.P, color=self.COL_PT_P, radius=0.12)
        p_lbl = Text("P", font=FONT_CN, font_size=24, color=self.COL_PT_P
                    ).next_to(self.P, RIGHT, buff=0.18)
        self.play(FadeIn(p_dot, scale=0.5), run_time=0.4)
        self.play(Flash(p_dot, color=self.COL_PT_P, flash_radius=0.3), run_time=0.3)
        self.play(FadeIn(p_lbl), run_time=0.3)

        on_line = Text(
            "P 在角平分线 OC 上",
            font=FONT_CN, font_size=22, color=GRAY_A
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(on_line), run_time=0.3)

        # 2. 画 PD（P 到 OA 的垂线）
        pd_line = DashedLine(self.P, self.D,
                             color=self.COL_DIST, stroke_width=3, dash_length=0.12)
        d_dot = Dot(self.D, color=self.COL_DIST, radius=0.08)
        d_lbl = Text("D", font=FONT_CN, font_size=20, color=self.COL_DIST
                    ).next_to(self.D, DOWN, buff=0.18)
        # 直角标记 at D：指向 P，沿 OA 方向
        ra_D = self._right_angle_mark(self.D, self.P, self.A)

        self.play(Create(pd_line), FadeIn(d_dot), run_time=0.7)
        self.play(FadeIn(ra_D), Write(d_lbl), run_time=0.3)

        pd_hint = Text(
            "PD ⊥ OA（P 到 OA 的距离）",
            font=FONT_CN, font_size=21, color=GRAY_A
        ).move_to(DOWN * 4.7)
        self.play(FadeIn(pd_hint), run_time=0.3)

        # 3. 画 PE（P 到 OB 的垂线）
        pe_line = DashedLine(self.P, self.E,
                             color=self.COL_DIST, stroke_width=3, dash_length=0.12)
        e_dot = Dot(self.E, color=self.COL_DIST, radius=0.08)
        e_lbl = Text("E", font=FONT_CN, font_size=20, color=self.COL_DIST
                    ).next_to(self.E, UR, buff=0.15)
        # 直角标记 at E：指向 P，沿 OB 方向
        ra_E = self._right_angle_mark(self.E, self.P, self.B)

        self.play(FadeOut(pd_hint), run_time=0.2)
        self.play(Create(pe_line), FadeIn(e_dot), run_time=0.7)
        self.play(FadeIn(ra_E), Write(e_lbl), run_time=0.3)

        pe_hint = Text(
            "PE ⊥ OB（P 到 OB 的距离）",
            font=FONT_CN, font_size=21, color=GRAY_A
        ).move_to(DOWN * 4.7)
        self.play(FadeIn(pe_hint), run_time=0.3)

        # 4. 刻度标注 PD = PE
        tick_PD = self._equal_tick(self.P, self.D, col=self.COL_EQUAL)
        tick_PE = self._equal_tick(self.P, self.E, col=self.COL_EQUAL)
        self.play(
            FadeOut(on_line), FadeOut(pe_hint),
            Create(tick_PD), Create(tick_PE),
            run_time=0.6
        )

        # 5. 公式框
        form_main = MathTex(
            r"PD = PE",
            color=self.COL_FORM, font_size=50
        ).move_to(DOWN * 4.8)
        self.play(Write(form_main), run_time=0.9)

        form_sub = Text(
            "P 到 ∠AOB 两边的距离相等",
            font=FONT_CN, font_size=24, color=self.COL_PROP
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(form_sub, shift=UP * 0.2), run_time=0.5)

        # 高亮闪烁
        self.play(
            Flash(form_main, color=self.COL_FORM, flash_radius=1.0), run_time=0.5
        )
        self.wait(1.5)

        # 清理（保留射线、平分线、O点）
        self.play(
            FadeOut(badge), FadeOut(title),
            FadeOut(p_dot), FadeOut(p_lbl),
            FadeOut(pd_line), FadeOut(d_dot), FadeOut(d_lbl), FadeOut(ra_D),
            FadeOut(pe_line), FadeOut(e_dot), FadeOut(e_lbl), FadeOut(ra_E),
            FadeOut(tick_PD), FadeOut(tick_PE),
            FadeOut(form_main), FadeOut(form_sub),
            run_time=0.6
        )

    # ===================================================
    # Scene 5: 判定 — 等距点在平分线上 (~30-43s)
    # ===================================================
    def scene_criterion(self):
        badge, title = self._section_header(
            "判定", "等距点在角平分线上", badge_col=self.COL_CRIT
        )
        self.play(Write(badge), FadeIn(title), run_time=0.5)

        # 1. 引入 Q（先在非等距位置）
        q_dot = Dot(self.Q_start, color=self.COL_PT_Q, radius=0.12)
        q_lbl = Text("Q", font=FONT_CN, font_size=24, color=self.COL_PT_Q
                    ).next_to(q_dot, RIGHT, buff=0.18)
        self.play(FadeIn(q_dot, scale=0.5), FadeIn(q_lbl), run_time=0.4)

        intro_q = Text(
            "角内有一点 Q，测量它到两边的距离",
            font=FONT_CN, font_size=21, color=GRAY_A
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(intro_q), run_time=0.4)

        # Q_start 的垂足（近似偏向OA）
        t_Dqs = np.dot(self.Q_start - self.O, self.OA_dir)
        D_qs = self.O + t_Dqs * self.OA_dir
        t_Eqs = np.dot(self.Q_start - self.O, self.OB_dir)
        E_qs = self.O + t_Eqs * self.OB_dir

        qdA = np.linalg.norm(self.Q_start - D_qs)
        qdB = np.linalg.norm(self.Q_start - E_qs)

        qd_line = DashedLine(self.Q_start, D_qs,
                             color=self.COL_DIST, stroke_width=2.5, dash_length=0.1)
        qe_line = DashedLine(self.Q_start, E_qs,
                             color=self.COL_DIST, stroke_width=2.5, dash_length=0.1)
        ra_Dqs = self._right_angle_mark(D_qs, self.Q_start, self.A)
        ra_Eqs = self._right_angle_mark(E_qs, self.Q_start, self.B)

        self.play(Create(qd_line), Create(qe_line),
                  FadeIn(ra_Dqs), FadeIn(ra_Eqs), run_time=0.8)

        # 不等标注
        not_equal = MathTex(
            r"QD_1 \neq QE_1", color=RED, font_size=36
        ).move_to(DOWN * 5.1)
        self.play(FadeIn(not_equal), run_time=0.4)
        self.wait(0.6)

        # 2. 移动 Q 到等距位置（滑到平分线上）
        move_hint = Text(
            "调整 Q 的位置使两边距离相等...",
            font=FONT_CN, font_size=21, color=self.COL_CRIT
        ).move_to(DOWN * 4.2)
        self.play(
            FadeOut(intro_q), FadeOut(not_equal),
            FadeIn(move_hint),
            run_time=0.4
        )

        # 移动 q_dot 到 Q_end，同时让虚线跟随（重绘）
        self.play(
            FadeOut(qd_line), FadeOut(qe_line),
            FadeOut(ra_Dqs), FadeOut(ra_Eqs),
            run_time=0.2
        )
        self.play(
            q_dot.animate.move_to(self.Q_end),
            q_lbl.animate.next_to(self.Q_end, RIGHT, buff=0.18),
            run_time=0.9,
            rate_func=smooth
        )

        # 3. Q_end 的垂线
        qd2 = DashedLine(self.Q_end, self.D_q,
                         color=self.COL_DIST, stroke_width=3, dash_length=0.12)
        qe2 = DashedLine(self.Q_end, self.E_q,
                         color=self.COL_DIST, stroke_width=3, dash_length=0.12)
        dq_dot = Dot(self.D_q, color=self.COL_DIST, radius=0.07)
        eq_dot = Dot(self.E_q, color=self.COL_DIST, radius=0.07)
        ra_Dq = self._right_angle_mark(self.D_q, self.Q_end, self.A)
        ra_Eq = self._right_angle_mark(self.E_q, self.Q_end, self.B)

        self.play(
            Create(qd2), Create(qe2),
            FadeIn(dq_dot), FadeIn(eq_dot),
            FadeIn(ra_Dq), FadeIn(ra_Eq),
            run_time=0.8
        )

        # 等距刻度
        tick_qD = self._equal_tick(self.Q_end, self.D_q, col=self.COL_EQUAL)
        tick_qE = self._equal_tick(self.Q_end, self.E_q, col=self.COL_EQUAL)
        self.play(Create(tick_qD), Create(tick_qE), run_time=0.4)

        equal_q = MathTex(
            r"QD_2 = QE_2", color=self.COL_EQUAL, font_size=40
        ).move_to(DOWN * 4.8)
        self.play(FadeOut(move_hint), Write(equal_q), run_time=0.7)

        # Q 在平分线上 → 高亮平分线
        self.play(
            self.bisector.animate.set_stroke(color=self.COL_BIS, width=6),
            run_time=0.4
        )

        # 判定结论
        crit_form = Text(
            "∴ Q 在角平分线 OC 上",
            font=FONT_CN, font_size=26, color=self.COL_CRIT
        ).move_to(DOWN * 5.7)
        self.play(FadeIn(crit_form, shift=UP * 0.2), run_time=0.5)
        self.play(Flash(q_dot, color=self.COL_PT_Q, flash_radius=0.35), run_time=0.4)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(badge), FadeOut(title),
            FadeOut(q_dot), FadeOut(q_lbl),
            FadeOut(qd2), FadeOut(qe2),
            FadeOut(dq_dot), FadeOut(eq_dot),
            FadeOut(ra_Dq), FadeOut(ra_Eq),
            FadeOut(tick_qD), FadeOut(tick_qE),
            FadeOut(equal_q), FadeOut(crit_form),
            self.bisector.animate.set_stroke(color=self.COL_BIS, width=3.5),
            run_time=0.6
        )

    # ===================================================
    # Scene 6: 总结对比 (~43-55s)
    # ===================================================
    def scene_summary(self):
        # 淡出几何图形
        self.play(
            FadeOut(self.ray_OA), FadeOut(self.ray_OB),
            FadeOut(self.bisector), FadeOut(self.o_dot),
            FadeOut(self.o_lbl), FadeOut(self.a_lbl), FadeOut(self.b_lbl),
            run_time=0.5
        )

        sum_title = Text("总结", font=FONT_CN, font_size=46, color=self.COL_FORM
                        ).move_to(UP * 5.5)
        sum_sub = Text("性质与判定 — 互为逆命题，都是真命题",
                      font=FONT_CN, font_size=21, color=GRAY_A
                      ).move_to(UP * 4.7)
        self.play(Write(sum_title), FadeIn(sum_sub), run_time=0.6)

        # ---- 性质卡片 ----
        prop_title = Text("性质", font=FONT_CN, font_size=30, color=self.COL_PROP
                         ).move_to(UP * 3.6)
        prop_cond = Text("若 P 在 ∠AOB 的角平分线上",
                        font=FONT_CN, font_size=22, color=WHITE
                        ).move_to(UP * 2.9)
        prop_arr = MathTex(r"\Downarrow", color=self.COL_PROP, font_size=36
                          ).move_to(UP * 2.15)
        prop_conc = MathTex(r"PD = PE",
                           color=self.COL_PROP, font_size=38
                           ).move_to(UP * 1.4)

        self.play(Write(prop_title), run_time=0.4)
        self.play(FadeIn(prop_cond, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(prop_arr), Write(prop_conc), run_time=0.5)

        # 分割线
        div = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_C, stroke_width=1.2
                  ).move_to(UP * 0.55)
        self.play(Create(div), run_time=0.3)

        # ---- 判定卡片 ----
        crit_title = Text("判定", font=FONT_CN, font_size=30, color=self.COL_CRIT
                         ).move_to(DOWN * 0.2)
        crit_cond = Text("若 P 到 ∠AOB 两边距离相等",
                        font=FONT_CN, font_size=22, color=WHITE
                        ).move_to(DOWN * 0.95)
        crit_arr = MathTex(r"\Downarrow", color=self.COL_CRIT, font_size=36
                          ).move_to(DOWN * 1.75)
        crit_conc = Text("P 在 ∠AOB 的角平分线上",
                        font=FONT_CN, font_size=22, color=self.COL_CRIT
                        ).move_to(DOWN * 2.5)

        self.play(Write(crit_title), run_time=0.4)
        self.play(FadeIn(crit_cond, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(crit_arr), FadeIn(crit_conc, shift=UP * 0.2), run_time=0.5)

        # ---- 互逆说明 ----
        inverse_note = Text(
            "⇔ 两者互为逆命题，均成立",
            font=FONT_CN, font_size=23, color=YELLOW
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(inverse_note, shift=UP * 0.3), run_time=0.5)

        self.wait(2.0)

        self.play(
            FadeOut(sum_title), FadeOut(sum_sub),
            FadeOut(prop_title), FadeOut(prop_cond),
            FadeOut(prop_arr), FadeOut(prop_conc),
            FadeOut(div),
            FadeOut(crit_title), FadeOut(crit_cond),
            FadeOut(crit_arr), FadeOut(crit_conc),
            FadeOut(inverse_note),
            run_time=0.5
        )

    # ===================================================
    # Scene 7: 片尾 (~55-65s)
    # ===================================================
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=38, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=28, color=GRAY_B
        ).move_to(UP * 1.0)
        follow = Text(
            "关注我，获得更多数学技巧!",
            font=FONT_CN, font_size=30, color=self.COL_FORM
        ).move_to(DOWN * 0.3)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰：旋转角符号
        def angle_deco(angle_val, pos):
            arc = Arc(radius=0.28, start_angle=0, angle=angle_val,
                      color=self.COL_BIS, stroke_width=3)
            l1 = Line(ORIGIN, RIGHT * 0.4, color=self.COL_RAY, stroke_width=2)
            l2 = Line(ORIGIN,
                      np.array([np.cos(angle_val), np.sin(angle_val), 0]) * 0.4,
                      color=self.COL_RAY, stroke_width=2)
            g = VGroup(l1, l2, arc).move_to(pos)
            return g

        decos = VGroup(
            angle_deco(70 * np.pi/180, DOWN * 1.8 + LEFT * 2.5),
            angle_deco(35 * np.pi/180, DOWN * 1.8 + LEFT * 0.5),
            angle_deco(70 * np.pi/180, DOWN * 1.8 + RIGHT * 1.5),
        )
        self.play(*[FadeIn(d, scale=0.6) for d in decos], run_time=0.5)
        self.play(Rotate(decos, angle=PI * 0.5, run_time=1.2))
        self.wait(0.8)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(decos),
            run_time=0.8
        )


# ===================================================
# 渲染命令:
# 快速预览: manim -pql angle_bisector.py AngleBisectorProperties
# 高质量:   manim -qh  angle_bisector.py AngleBisectorProperties
# ===================================================