"""
线段垂直平分线的性质与判定
八年级数学动画教学 - TikTok竖屏版 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局视频配置 ──────────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ─────────────────────────────────────────────────────────────
class PerpendicularBisector(Scene):
    """
    场景顺序:
      1. 开场钩子
      2. 认识垂直平分线
      3. 性质演示 (PA=PB)
      4. 简洁证明
      5. 判定定理
      6. 互逆总结
      7. 片尾关注
    """

    # ── 颜色常量 ─────────────────────────────────────────────
    COL_BG        = "#1a1a2e"
    COL_SEGMENT   = WHITE
    COL_BISECTOR  = "#3498db"   # 蓝：垂直平分线
    COL_POINT_P   = "#e74c3c"   # 红：动点P
    COL_EQUAL     = "#2ecc71"   # 绿：相等距离
    COL_MIDPOINT  = YELLOW      # 黄：中点M
    COL_AUX       = GRAY_B      # 灰：辅助线
    COL_HIGHLIGHT = GOLD        # 金：重点
    COL_PROOF     = "#9b59b6"   # 紫：证明用

    def construct(self):
        self.camera.background_color = self.COL_BG
        self.setup_geometry()

        self.scene_1_hook()
        self.scene_2_definition()
        self.scene_3_property()
        self.scene_4_proof()
        self.scene_5_criterion()
        self.scene_6_summary()
        self.scene_7_outro()

    # ═══════════════════════════════════════════════════════════
    # 几何初始化（所有坐标统一在此计算）
    # ═══════════════════════════════════════════════════════════
    def setup_geometry(self):
        # ── 主线段端点 ──────────────────────────────────────
        self.A = np.array([-2.2,  0.0, 0])
        self.B = np.array([ 2.2,  0.0, 0])

        # ── 派生点（精确计算，不猜坐标）──────────────────────
        self.M = (self.A + self.B) / 2            # 中点 M = [0, 0, 0]

        AB_vec = self.B - self.A
        AB_dir = AB_vec / np.linalg.norm(AB_vec)  # AB单位方向
        # 垂直方向（逆时针旋转90°）
        self.perp_dir = np.array([-AB_dir[1], AB_dir[0], 0])

        # 垂直平分线端点（延伸4个单位）
        self.bsect_top    = self.M + 3.8 * self.perp_dir
        self.bsect_bottom = self.M - 3.8 * self.perp_dir

        # 性质演示用P点（在垂直平分线上，两侧各一个）
        self.P1 = self.M + 2.5 * self.perp_dir   # 上方
        self.P2 = self.M - 1.8 * self.perp_dir   # 下方

        # 证明用P点
        self.P_proof = self.M + 2.0 * self.perp_dir

        # 距离缓存（用于标注）
        self.PA1 = np.linalg.norm(self.P1 - self.A)   # 3.33
        self.PB1 = np.linalg.norm(self.P1 - self.B)   # 3.33

        # ── 验证 ──────────────────────────────────────────
        self._verify()

    def _verify(self):
        eps = 1e-9
        # 中点验证
        assert abs(np.linalg.norm(self.M - self.A) -
                   np.linalg.norm(self.M - self.B)) < eps, "中点错误"
        # 垂直验证
        AB_v = self.B - self.A
        assert abs(np.dot(AB_v[:2], self.perp_dir[:2])) < eps, "垂直关系错误"
        # PA=PB验证
        for P, name in [(self.P1, "P1"), (self.P2, "P2"), (self.P_proof, "P_proof")]:
            diff = abs(np.linalg.norm(P - self.A) - np.linalg.norm(P - self.B))
            assert diff < eps, f"{name}: PA≠PB, diff={diff}"
        print("✓ 几何验证通过")

    # ─────────────────────────────────────────────────────────
    # 工具函数
    # ─────────────────────────────────────────────────────────
    def _right_angle_mark(self, corner, p1, p2, size=0.22, color=YELLOW):
        """手动绘制直角标记（小方块）"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=2.0,
            fill_opacity=0
        )

    def _tick_mark(self, p1, p2, color=YELLOW, size=0.15):
        """在线段中间绘制等长刻度符号"""
        mid = (p1 + p2) / 2
        direction = p2 - p1
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])
        return Line(
            mid - perp * size,
            mid + perp * size,
            color=color,
            stroke_width=2.5
        )

    def _text(self, s, size=22, color=WHITE, **kwargs):
        return Text(s, font="Noto Sans CJK SC", font_size=size, color=color, **kwargs)

    # ═══════════════════════════════════════════════════════════
    # Scene 1: 开场钩子
    # ═══════════════════════════════════════════════════════════
    def scene_1_hook(self):
        # 作者信息（顶部，常驻）
        self.author = self._text(
            "上海初高中数学直通车 @emptyandcalm",
            size=18, color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = self._text("哪里的点到 A、B", size=34, color=self.COL_HIGHLIGHT)
        hook_line2 = self._text("距离相等？", size=34, color=self.COL_HIGHLIGHT)
        hook = VGroup(hook_line1, hook_line2).arrange(DOWN, buff=0.15)
        hook.move_to(UP * 5.5)

        self.play(Write(hook), run_time=1.0)

        # A、B 两点出现（在主内容区）
        a_dot = Dot(self.A + UP * 2, color=WHITE, radius=0.12)
        b_dot = Dot(self.B + UP * 2, color=WHITE, radius=0.12)
        a_lbl = MathTex("A", color=WHITE, font_size=28).next_to(a_dot, DL, buff=0.12)
        b_lbl = MathTex("B", color=WHITE, font_size=28).next_to(b_dot, DR, buff=0.12)
        ab_seg = Line(self.A + UP * 2, self.B + UP * 2, color=WHITE, stroke_width=3)

        self.play(Create(ab_seg), FadeIn(a_dot), FadeIn(b_dot),
                  Write(a_lbl), Write(b_lbl), run_time=0.8)

        # 一个游荡的"问号点"
        question_dot = Dot(UP * 4.0, color=self.COL_POINT_P, radius=0.14)
        question_mark = self._text("?", size=30, color=self.COL_POINT_P)
        question_mark.next_to(question_dot, UR, buff=0.08)
        self.play(FadeIn(question_dot), Write(question_mark), run_time=0.4)
        self.play(question_dot.animate.move_to(UP * 3.5 + LEFT * 0.3),
                  question_mark.animate.move_to(UP * 3.9 + LEFT * 0.1),
                  run_time=0.8, rate_func=smooth)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(ab_seg), FadeOut(a_dot), FadeOut(b_dot),
            FadeOut(a_lbl), FadeOut(b_lbl),
            FadeOut(question_dot), FadeOut(question_mark),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 2: 认识垂直平分线（定义）
    # ═══════════════════════════════════════════════════════════
    def scene_2_definition(self):
        title = self._text("垂直平分线", size=38, color=self.COL_BISECTOR)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.7)

        subtitle = self._text("也叫「中垂线」", size=24, color=GRAY_A)
        subtitle.move_to(UP * 5.0)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ── 绘制线段 AB（偏上区域）──────────────────────────
        offset = UP * 1.5
        A = self.A + offset
        B = self.B + offset
        M = self.M + offset

        seg = Line(A, B, color=self.COL_SEGMENT, stroke_width=4)
        a_dot = Dot(A, color=WHITE, radius=0.11)
        b_dot = Dot(B, color=WHITE, radius=0.11)
        a_lbl = MathTex("A", color=WHITE, font_size=28).next_to(a_dot, DL, buff=0.10)
        b_lbl = MathTex("B", color=WHITE, font_size=28).next_to(b_dot, DR, buff=0.10)

        self.play(Create(seg), FadeIn(a_dot), FadeIn(b_dot),
                  Write(a_lbl), Write(b_lbl), run_time=0.9)

        # ── 标记中点 M ──────────────────────────────────────
        m_dot = Dot(M, color=self.COL_MIDPOINT, radius=0.11)
        m_lbl = MathTex("M", color=self.COL_MIDPOINT, font_size=26).next_to(m_dot, DOWN, buff=0.12)

        step1 = self._text("① 找到中点 M，使 AM = MB", size=22, color=GRAY_A)
        step1.move_to(DOWN * 2.8)

        self.play(FadeIn(m_dot, scale=0.5), Write(m_lbl), run_time=0.5)
        self.play(FadeIn(step1), run_time=0.4)

        # 刻度符号
        tick_am = self._tick_mark(A, M, color=self.COL_MIDPOINT)
        tick_mb = self._tick_mark(M, B, color=self.COL_MIDPOINT)
        self.play(Create(tick_am), Create(tick_mb), run_time=0.4)
        self.wait(0.4)

        # ── 绘制垂直平分线 ──────────────────────────────────
        bsect_top    = M + 3.2 * self.perp_dir
        bsect_bottom = M - 2.8 * self.perp_dir

        bisector = Line(bsect_bottom, bsect_top,
                        color=self.COL_BISECTOR, stroke_width=3)
        l_lbl = MathTex("l", color=self.COL_BISECTOR, font_size=28)
        l_lbl.next_to(bsect_top, UR, buff=0.12)

        step2 = self._text("② 过 M 作 AB 的垂线 → 垂直平分线 l", size=20, color=GRAY_A)
        step2.move_to(DOWN * 3.5)

        self.play(FadeOut(step1), run_time=0.2)
        self.play(Create(bisector), Write(l_lbl), FadeIn(step2), run_time=1.0)

        # ── 直角符号 ────────────────────────────────────────
        # P_for_mark 在垂直平分线上稍微高一点的位置
        P_mark = M + 0.5 * self.perp_dir
        ra_mark = self._right_angle_mark(M, A, P_mark, size=0.22, color=YELLOW)
        self.play(Create(ra_mark), run_time=0.4)
        self.wait(0.5)

        # ── 定义文字 ────────────────────────────────────────
        self.play(FadeOut(step2), run_time=0.2)
        def_text = self._text(
            "l ⊥ AB 且过中点 M\n这就是 AB 的垂直平分线",
            size=22, color=WHITE
        )
        def_text.move_to(DOWN * 3.2)
        self.play(FadeIn(def_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)

        # 保存到实例供后续场景使用
        self._def_seg   = seg
        self._def_a_dot = a_dot
        self._def_b_dot = b_dot
        self._def_a_lbl = a_lbl
        self._def_b_lbl = b_lbl
        self._def_m_dot = m_dot
        self._def_m_lbl = m_lbl
        self._def_bisector = bisector
        self._def_l_lbl = l_lbl
        self._def_ra  = ra_mark
        self._def_ticks = VGroup(tick_am, tick_mb)
        self._scene2_offset = offset

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(def_text),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 3: 性质演示 PA = PB
    # ═══════════════════════════════════════════════════════════
    def scene_3_property(self):
        offset = self._scene2_offset
        A = self.A + offset
        B = self.B + offset
        M = self.M + offset
        P1 = self.P1 + offset
        P2 = self.P2 + offset

        # 标题
        prop_title = self._text("性质", size=38, color=self.COL_HIGHLIGHT)
        prop_title.move_to(UP * 5.8)
        self.play(Write(prop_title), run_time=0.5)

        prop_sub = self._text("垂直平分线上的点到两端点等距", size=22, color=GRAY_A)
        prop_sub.move_to(UP * 5.1)
        self.play(FadeIn(prop_sub), run_time=0.4)

        # ── P1 点出现（在垂直平分线上）──────────────────────
        p_dot = Dot(P1, color=self.COL_POINT_P, radius=0.13)
        p_lbl = MathTex("P", color=self.COL_POINT_P, font_size=28).next_to(p_dot, RIGHT, buff=0.12)

        step = self._text("取垂直平分线上一点 P", size=22, color=GRAY_A)
        step.move_to(DOWN * 3.0)

        self.play(FadeIn(p_dot, scale=0.5), Write(p_lbl), FadeIn(step), run_time=0.7)

        # ── 连接 PA、PB（绿色虚线）──────────────────────────
        pa_line = DashedLine(P1, A, color=self.COL_EQUAL,
                             dash_length=0.12, stroke_width=2.5)
        pb_line = DashedLine(P1, B, color=self.COL_EQUAL,
                             dash_length=0.12, stroke_width=2.5)

        self.play(Create(pa_line), Create(pb_line), run_time=0.8)

        # PA、PB 标注
        pa_mid = (P1 + A) / 2
        pb_mid = (P1 + B) / 2
        pa_label = MathTex("PA", color=self.COL_EQUAL, font_size=22)
        pa_label.move_to(pa_mid + LEFT * 0.5)
        pb_label = MathTex("PB", color=self.COL_EQUAL, font_size=22)
        pb_label.move_to(pb_mid + RIGHT * 0.5)

        self.play(Write(pa_label), Write(pb_label), run_time=0.5)
        self.play(FadeOut(step), run_time=0.2)

        # 强调相等
        eq_text = self._text("测量一下……", size=22, color=GRAY_A)
        eq_text.move_to(DOWN * 3.0)
        self.play(FadeIn(eq_text), run_time=0.4)
        self.wait(0.5)

        eq_formula = MathTex("PA = PB", color=self.COL_EQUAL, font_size=44)
        eq_formula.move_to(DOWN * 3.6)
        self.play(
            FadeOut(eq_text),
            Write(eq_formula),
            pa_line.animate.set_color(YELLOW),
            pb_line.animate.set_color(YELLOW),
            run_time=0.8
        )
        self.play(Flash(p_dot, color=self.COL_EQUAL, flash_radius=0.35), run_time=0.5)
        self.wait(0.8)

        # ── 换一个P2点，再次验证 ─────────────────────────────
        swap_text = self._text("换一个点试试？", size=22, color=GRAY_A)
        swap_text.move_to(DOWN * 4.5)
        self.play(
            FadeOut(eq_formula), FadeOut(pa_label), FadeOut(pb_label),
            FadeIn(swap_text), run_time=0.5
        )

        # P移动到P2
        pa_line2 = DashedLine(P2, A, color=self.COL_EQUAL,
                              dash_length=0.12, stroke_width=2.5)
        pb_line2 = DashedLine(P2, B, color=self.COL_EQUAL,
                              dash_length=0.12, stroke_width=2.5)

        self.play(
            p_dot.animate.move_to(P2),
            p_lbl.animate.next_to(P2, RIGHT, buff=0.12),
            FadeOut(pa_line), FadeOut(pb_line),
            run_time=0.8
        )
        self.play(Create(pa_line2), Create(pb_line2), run_time=0.6)

        eq_formula2 = MathTex("PA = PB", color=self.COL_EQUAL, font_size=40)
        eq_formula2.move_to(DOWN * 3.8)
        self.play(
            FadeOut(swap_text),
            Write(eq_formula2),
            run_time=0.6
        )
        self.play(Flash(p_dot, color=self.COL_EQUAL, flash_radius=0.35), run_time=0.4)
        self.wait(0.8)

        # ── 性质结论框 ──────────────────────────────────────
        self.play(
            FadeOut(pa_line2), FadeOut(pb_line2),
            FadeOut(eq_formula2), FadeOut(p_dot), FadeOut(p_lbl),
            run_time=0.4
        )

        prop_box_text = self._text("若 P 在 AB 的垂直平分线上", size=22, color=WHITE)
        prop_arrow = MathTex(r"\Rightarrow", color=self.COL_HIGHLIGHT, font_size=38)
        prop_result = MathTex("PA = PB", color=self.COL_EQUAL, font_size=38)

        prop_group = VGroup(prop_box_text, prop_arrow, prop_result).arrange(DOWN, buff=0.2)
        prop_group.move_to(DOWN * 3.5)

        prop_rect = SurroundingRectangle(prop_group, color=self.COL_HIGHLIGHT,
                                         corner_radius=0.15, buff=0.2)
        self.play(FadeIn(prop_group), Create(prop_rect), run_time=0.8)
        self.wait(1.5)

        # 保存并清理
        self._prop_group = prop_group
        self._prop_rect = prop_rect
        self.play(
            FadeOut(prop_title), FadeOut(prop_sub),
            FadeOut(prop_group), FadeOut(prop_rect),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 4: 简洁证明
    # ═══════════════════════════════════════════════════════════
    def scene_4_proof(self):
        offset = self._scene2_offset
        A = self.A + offset
        B = self.B + offset
        M = self.M + offset
        P = self.P_proof + offset

        # 标题
        pf_title = self._text("为什么 PA = PB？", size=34, color=self.COL_HIGHLIGHT)
        pf_title.move_to(UP * 5.8)
        self.play(Write(pf_title), run_time=0.6)

        # ── P点出现 ──────────────────────────────────────────
        p_dot = Dot(P, color=self.COL_POINT_P, radius=0.12)
        p_lbl = MathTex("P", color=self.COL_POINT_P, font_size=26).next_to(p_dot, RIGHT, buff=0.10)
        self.play(FadeIn(p_dot), Write(p_lbl), run_time=0.4)

        # ── 连MA、MB (以便展示刻度) ──────────────────────────
        ma_line = Line(M, A, color=self.COL_PROOF, stroke_width=2.5)
        mb_line = Line(M, B, color=self.COL_PROOF, stroke_width=2.5)

        step1 = self._text("① 已知: AM = MB (M 是中点)", size=22, color=GRAY_A)
        step1.move_to(DOWN * 2.8)
        self.play(Create(ma_line), Create(mb_line), FadeIn(step1), run_time=0.7)

        tick_a = self._tick_mark(M, A, color=self.COL_PROOF)
        tick_b = self._tick_mark(M, B, color=self.COL_PROOF)
        self.play(Create(tick_a), Create(tick_b), run_time=0.3)
        self.wait(0.4)

        # ── 连PM ─────────────────────────────────────────────
        pm_line = Line(P, M, color=self.COL_PROOF, stroke_width=2.5)

        step2 = self._text("② PM 是公共边", size=22, color=GRAY_A)
        step2.move_to(DOWN * 3.3)
        self.play(FadeOut(step1), Create(pm_line), FadeIn(step2), run_time=0.6)

        # ── 直角符号 ─────────────────────────────────────────
        P_above = M + 0.5 * self.perp_dir   # 稍微在垂直平分线上方
        ra = self._right_angle_mark(M, A, P_above, size=0.22, color=YELLOW)

        step3_a = self._text("③ ∠PMA = ∠PMB = 90°", size=22, color=GRAY_A)
        step3_a.move_to(DOWN * 3.8)
        self.play(FadeOut(step2), Create(ra), FadeIn(step3_a), run_time=0.6)
        self.wait(0.5)

        # ── 全等结论 ──────────────────────────────────────────
        step4 = self._text("SAS全等: △PMA ≅ △PMB", size=22, color=self.COL_HIGHLIGHT)
        step4.move_to(DOWN * 4.4)

        tri_PMA = Polygon(P, M, A, color=self.COL_PROOF,
                          fill_color=self.COL_PROOF, fill_opacity=0.15,
                          stroke_width=2)
        tri_PMB = Polygon(P, M, B, color=self.COL_EQUAL,
                          fill_color=self.COL_EQUAL, fill_opacity=0.15,
                          stroke_width=2)

        self.play(FadeOut(step3_a), run_time=0.2)
        self.play(Create(tri_PMA), Create(tri_PMB), FadeIn(step4), run_time=0.8)
        self.wait(0.6)

        # ── 最终结论 PA=PB ─────────────────────────────────
        final = MathTex(r"\therefore PA = PB", color=self.COL_EQUAL, font_size=42)
        final.move_to(DOWN * 5.2)
        self.play(Write(final), run_time=0.6)
        self.play(Flash(final, color=self.COL_EQUAL, flash_radius=1.2), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(pf_title),
            FadeOut(p_dot), FadeOut(p_lbl),
            FadeOut(ma_line), FadeOut(mb_line),
            FadeOut(pm_line),
            FadeOut(tick_a), FadeOut(tick_b),
            FadeOut(ra),
            FadeOut(step4),
            FadeOut(tri_PMA), FadeOut(tri_PMB),
            FadeOut(final),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 5: 判定定理（逆命题）
    # ═══════════════════════════════════════════════════════════
    def scene_5_criterion(self):
        offset = self._scene2_offset
        A = self.A + offset
        B = self.B + offset
        M = self.M + offset

        crit_title = self._text("判定", size=38, color=ORANGE)
        crit_title.move_to(UP * 5.8)
        self.play(Write(crit_title), run_time=0.5)

        crit_sub = self._text("等距的点在哪里？", size=26, color=GRAY_A)
        crit_sub.move_to(UP * 5.1)
        self.play(FadeIn(crit_sub), run_time=0.4)

        # ── 展示所有等距点（轨迹）──────────────────────────
        locus_dots = VGroup()
        locus_lines = VGroup()

        t_vals = np.linspace(-2.6, 2.6, 9)
        for t in t_vals:
            p = M + t * self.perp_dir
            d = Dot(p + UP * 0, color=self.COL_POINT_P, radius=0.08, fill_opacity=0.7)
            la = DashedLine(p, A, color=self.COL_EQUAL, stroke_width=1.5,
                            dash_length=0.1)
            lb = DashedLine(p, B, color=self.COL_EQUAL, stroke_width=1.5,
                            dash_length=0.1)
            locus_dots.add(d)
            locus_lines.add(la, lb)

        step_c1 = self._text("到 A、B 等距的点有无数多个…", size=21, color=GRAY_A)
        step_c1.move_to(DOWN * 3.0)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in locus_dots], lag_ratio=0.1),
            FadeIn(step_c1),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[Create(l) for l in locus_lines], lag_ratio=0.05),
            run_time=1.0
        )
        self.wait(0.6)

        # ── 连成一线，正好是垂直平分线！──────────────────────
        step_c2 = self._text("它们连成一条线……正好是垂直平分线！", size=20, color=self.COL_HIGHLIGHT)
        step_c2.move_to(DOWN * 3.6)

        self.play(FadeOut(step_c1), FadeOut(locus_lines), run_time=0.4)
        self.play(FadeIn(step_c2), run_time=0.4)

        # 垂直平分线高亮闪烁
        self.play(
            self._def_bisector.animate.set_color(self.COL_HIGHLIGHT).set_stroke(width=5),
            run_time=0.5
        )
        self.play(
            self._def_bisector.animate.set_color(self.COL_BISECTOR).set_stroke(width=3),
            run_time=0.4
        )
        self.wait(0.6)

        # ── 判定公式 ─────────────────────────────────────────
        self.play(FadeOut(step_c2), FadeOut(locus_dots), run_time=0.3)

        crit_box1 = self._text("若 PA = PB", size=22, color=WHITE)
        crit_arrow = MathTex(r"\Rightarrow", color=ORANGE, font_size=38)
        crit_result = self._text("P 在 AB 的垂直平分线上", size=22, color=ORANGE)

        crit_group = VGroup(crit_box1, crit_arrow, crit_result).arrange(DOWN, buff=0.2)
        crit_group.move_to(DOWN * 3.8)
        crit_rect = SurroundingRectangle(crit_group, color=ORANGE,
                                          corner_radius=0.15, buff=0.2)

        self.play(FadeIn(crit_group), Create(crit_rect), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(crit_title), FadeOut(crit_sub),
            FadeOut(crit_group), FadeOut(crit_rect),
            run_time=0.5
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 6: 互逆总结
    # ═══════════════════════════════════════════════════════════
    def scene_6_summary(self):
        # 淡出主图形
        self.play(
            FadeOut(self._def_seg),
            FadeOut(self._def_a_dot), FadeOut(self._def_b_dot),
            FadeOut(self._def_a_lbl), FadeOut(self._def_b_lbl),
            FadeOut(self._def_m_dot), FadeOut(self._def_m_lbl),
            FadeOut(self._def_bisector), FadeOut(self._def_l_lbl),
            FadeOut(self._def_ra), FadeOut(self._def_ticks),
            run_time=0.5
        )

        sum_title = self._text("总结记忆", size=38, color=self.COL_HIGHLIGHT)
        sum_title.move_to(UP * 6.5)
        self.play(Write(sum_title), run_time=0.5)

        # ── 两条结论横幅 ──────────────────────────────────────
        # 性质（上方）
        prop_header = self._text("【性质】", size=26, color=self.COL_EQUAL)
        prop_body1  = self._text("P 在垂直平分线上", size=22, color=WHITE)
        prop_arrow  = MathTex(r"\Rightarrow", color=self.COL_EQUAL, font_size=36)
        prop_body2  = MathTex("PA = PB", color=self.COL_EQUAL, font_size=34)

        prop_row = VGroup(prop_body1, prop_arrow, prop_body2).arrange(RIGHT, buff=0.3)
        prop_block = VGroup(prop_header, prop_row).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        prop_block.move_to(UP * 4.0)
        prop_bg = SurroundingRectangle(prop_block, color=self.COL_EQUAL,
                                        corner_radius=0.2, buff=0.25, fill_opacity=0.07)

        # 判定（下方）
        crit_header = self._text("【判定】", size=26, color=ORANGE)
        crit_body1  = MathTex("PA = PB", color=ORANGE, font_size=34)
        crit_arrow  = MathTex(r"\Rightarrow", color=ORANGE, font_size=36)
        crit_body2  = self._text("P 在垂直平分线上", size=22, color=WHITE)

        crit_row = VGroup(crit_body1, crit_arrow, crit_body2).arrange(RIGHT, buff=0.3)
        crit_block = VGroup(crit_header, crit_row).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        crit_block.move_to(UP * 2.0)
        crit_bg = SurroundingRectangle(crit_block, color=ORANGE,
                                        corner_radius=0.2, buff=0.25, fill_opacity=0.07)

        self.play(
            FadeIn(prop_bg), FadeIn(prop_block),
            run_time=0.7
        )
        self.play(
            FadeIn(crit_bg), FadeIn(crit_block),
            run_time=0.7
        )

        # ── 互为逆命题说明 ────────────────────────────────────
        reverse_note = self._text("互为逆命题，都是真命题！", size=26, color=self.COL_HIGHLIGHT)
        reverse_note.move_to(DOWN * 0.2)
        self.play(Write(reverse_note), run_time=0.6)

        # 双向箭头装饰
        double_arrow = MathTex(r"\Leftrightarrow", color=self.COL_HIGHLIGHT, font_size=52)
        double_arrow.move_to(DOWN * 1.2)
        self.play(FadeIn(double_arrow, scale=0.5), run_time=0.4)
        self.play(double_arrow.animate.scale(1.2), run_time=0.3)
        self.play(double_arrow.animate.scale(1/1.2), run_time=0.3)

        # ── 轴对称联系 ────────────────────────────────────────
        axis_note = self._text("💡 与轴对称密切相关！", size=22, color=TEAL)
        axis_note.move_to(DOWN * 2.3)
        self.play(FadeIn(axis_note, shift=UP * 0.2), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(sum_title),
            FadeOut(prop_block), FadeOut(prop_bg),
            FadeOut(crit_block), FadeOut(crit_bg),
            FadeOut(reverse_note), FadeOut(double_arrow),
            FadeOut(axis_note),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 7: 片尾
    # ═══════════════════════════════════════════════════════════
    def scene_7_outro(self):
        author_big = self._text("上海初高中数学直通车", size=38, color=WHITE)
        author_big.move_to(UP * 1.5)

        author_id = self._text("@emptyandcalm", size=30, color=GRAY_B)
        author_id.move_to(UP * 0.5)

        follow_text = self._text("关注我，学更多数学技巧！", size=28, color=self.COL_HIGHLIGHT)
        follow_text.move_to(DOWN * 0.8)

        # 小几何装饰：几个小线段和等号
        deco = VGroup(
            MathTex("PA = PB", color=self.COL_EQUAL, font_size=24).move_to(DOWN * 2.2),
            MathTex(r"l \perp AB", color=self.COL_BISECTOR, font_size=24).move_to(DOWN * 3.0),
        )

        self.play(
            Transform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in deco], lag_ratio=0.3),
            run_time=0.8
        )
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects.copy()], run_time=0.8)

# # 快速预览
# manim -pql perpendicular_bisector.py PerpendicularBisector

# # 高清正式版
# manim -qh perpendicular_bisector.py PerpendicularBisector