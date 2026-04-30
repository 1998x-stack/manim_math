"""
等腰三角形的性质 - Manim 教学动画
七年级数学 第十四章

三大性质:
  1. 等边对等角  (AB=AC → ∠B=∠C)
  2. 三线合一    (底边中线=高线=顶角平分线)
  3. 轴对称      (底边垂直平分线是对称轴)

格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== TikTok 竖屏全局配置 =====
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class IsoscelesTriangleProperties(Scene):
    """
    等腰三角形性质教学动画

    场景顺序:
      1. 开场钩子
      2. 性质一：等边对等角
      3. 性质二：三线合一
      4. 性质三：轴对称
      5. 总结 + 片尾
    """

    # ─────────────────────────────────────────────────────────
    # 配色常量
    # ─────────────────────────────────────────────────────────
    C_BG       = "#1a1a2e"
    C_WAIST    = "#e74c3c"   # 红  — 腰（等边）
    C_BASE     = "#f39c12"   # 橙  — 底边
    C_ANGLE    = "#3498db"   # 蓝  — 底角弧
    C_MEDIAN   = "#2ecc71"   # 绿  — 中线
    C_ALTITUDE = "#9b59b6"   # 紫  — 高线
    C_BISECT   = "#e67e22"   # 深橙— 顶角平分线
    C_AXIS     = "#1abc9c"   # 青  — 对称轴
    C_HIGHLIGHT= "#f1c40f"   # 金  — 高亮
    C_AUX      = "#95a5a6"   # 灰  — 辅助
    C_SUCCESS  = "#2ecc71"   # 绿  — 成功

    # ─────────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = self.C_BG

        self.setup_geometry()        # 所有几何数据统一初始化

        self.scene_1_opening()
        self.scene_2_equal_angles()
        self.scene_3_three_in_one()
        self.scene_4_symmetry()
        self.scene_5_summary_outro()

    # ═══════════════════════════════════════════════════════════
    # ① 统一初始化几何数据
    # ═══════════════════════════════════════════════════════════
    def setup_geometry(self):
        """所有坐标精确计算，后续场景只读不改"""
        SCALE  = 1.15
        OFFSET = np.array([0, 0.8, 0])

        self.A = np.array([ 0.0,  2.6, 0]) * SCALE + OFFSET   # 顶角
        self.B = np.array([-2.2, -0.8, 0]) * SCALE + OFFSET   # 左底角
        self.C = np.array([ 2.2, -0.8, 0]) * SCALE + OFFSET   # 右底角
        self.M = (self.B + self.C) / 2                         # 底边中点

        # 边长缓存
        self.AB_len = np.linalg.norm(self.B - self.A)
        self.AC_len = np.linalg.norm(self.C - self.A)
        self.BC_len = np.linalg.norm(self.C - self.B)

        # 角度缓存（弧度）
        self.ang_A   = self._angle(self.B, self.A, self.C)
        self.ang_B   = self._angle(self.A, self.B, self.C)
        self.ang_C   = self._angle(self.A, self.C, self.B)
        self.ang_BAM = self._angle(self.B, self.A, self.M)
        self.ang_CAM = self._angle(self.C, self.A, self.M)

        # 快速断言（保证等腰与三线合一）
        assert abs(self.AB_len - self.AC_len) < 1e-6
        assert abs(self.ang_B  - self.ang_C)  < 1e-6
        assert abs(self.ang_BAM - self.ang_CAM) < 1e-6
        dot_AM_BC = np.dot((self.M - self.A)[:2], (self.C - self.B)[:2])
        assert abs(dot_AM_BC) < 1e-6   # AM ⊥ BC

    # ─────────────────────────────────────────────────────────
    # 工具方法
    # ─────────────────────────────────────────────────────────
    def _angle(self, P1, vertex, P2):
        v1 = P1 - vertex
        v2 = P2 - vertex
        c  = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(c, -1.0, 1.0))

    def _cross_z(self, v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]

    def _triangle(self, color=WHITE, sw=3, fill=0.0, fc=WHITE):
        return Polygon(self.A, self.B, self.C,
                       color=color, stroke_width=sw,
                       fill_color=fc, fill_opacity=fill)

    def _tick(self, P1, P2, n=1, color=RED, size=0.20):
        """在线段 P1P2 中点处画 n 条等长刻线"""
        mid = (P1 + P2) / 2
        d   = P2 - P1;  d = d / np.linalg.norm(d)
        perp = np.array([-d[1], d[0], 0])
        offsets = {1:[0], 2:[-0.18*size*5, 0.18*size*5],
                   3:[-0.28*size*5, 0, 0.28*size*5]}[n]
        grp = VGroup()
        for off in offsets:
            grp.add(Line(mid + off*d - perp*size/2,
                         mid + off*d + perp*size/2,
                         color=color, stroke_width=3))
        return grp

    def _angle_arc(self, vertex, line1_end, line2_end,
                   radius=0.48, color=BLUE, other_angle=False,
                   double=False, sw=2.5):
        """创建角弧（已用叉积验证 other_angle）"""
        l1 = Line(vertex, line1_end)
        l2 = Line(vertex, line2_end)
        arcs = VGroup(Angle(l1, l2, radius=radius, color=color,
                            other_angle=other_angle, stroke_width=sw))
        if double:
            arcs.add(Angle(l1, l2, radius=radius + 0.13, color=color,
                           other_angle=other_angle, stroke_width=sw))
        return arcs

    def _vertex_labels(self, fa=0.15, fb=0.15, fc=0.15, sz=28):
        lA = Text("A", font="PingFang SC", font_size=sz).next_to(self.A, UP,  buff=fa)
        lB = Text("B", font="PingFang SC", font_size=sz).next_to(self.B, DL,  buff=fb)
        lC = Text("C", font="PingFang SC", font_size=sz).next_to(self.C, DR,  buff=fc)
        return lA, lB, lC

    def _label_M(self, sz=26, direction=DOWN, buff=0.18):
        return Text("M", font="PingFang SC", font_size=sz,
                    color=self.C_HIGHLIGHT).next_to(self.M, direction, buff=buff)

    def _rule_box(self, text_lines, color, pos, w=8.0, h=1.1, fsize=22):
        """创建规则文字框（圆角矩形+文字）"""
        bg = RoundedRectangle(width=w, height=h, corner_radius=0.3,
                              color=color,
                              fill_color=ManimColor(color).interpolate(BLACK, 0.85),
                              fill_opacity=0.92).move_to(pos)
        texts = VGroup()
        for i, (txt, col) in enumerate(text_lines):
            t = Text(txt, font="PingFang SC",
                     font_size=fsize, color=col)
            texts.add(t)
        texts.arrange(DOWN, buff=0.12).move_to(pos)
        return VGroup(bg, texts)

    def _section_header(self, tag, name, tag_color):
        """场景标题：序号标签 + 名称"""
        t_tag = Text(tag, font="PingFang SC",
                     font_size=26, color=tag_color).move_to(UP * 6.6)
        t_name = Text(name, font="PingFang SC",
                      font_size=40, color=tag_color).move_to(UP * 5.9)
        return t_tag, t_name

    def _property_badge(self, number, name, color, pos):
        """小属性徽章（场景过渡中显示）"""
        circ = Circle(radius=0.28, fill_color=color,
                      fill_opacity=1, stroke_width=0)
        num  = Text(str(number), font_size=22,
                    color=BLACK).move_to(circ.get_center())
        txt  = Text(name, font="PingFang SC",
                    font_size=22, color=color)
        badge = VGroup(VGroup(circ, num), txt).arrange(RIGHT, buff=0.22)
        badge.move_to(pos)
        return badge

    # ═══════════════════════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ═══════════════════════════════════════════════════════════
    def scene_1_opening(self):
        # 作者栏（固定顶部，保留全程）
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="PingFang SC", font_size=20, color=self.C_AUX
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.35)

        # 章节标签
        chap = Text("七年级 · 第十四章 · 三角形",
                    font="PingFang SC", font_size=22,
                    color=self.C_AUX).move_to(UP * 6.2)
        self.play(FadeIn(chap), run_time=0.35)

        # 主标题
        title = Text("等腰三角形的性质",
                     font="PingFang SC", font_size=50,
                     color=self.C_HIGHLIGHT).move_to(UP * 5.3)
        self.play(Write(title), run_time=0.9)

        # 钩子问句
        hook = Text("它有哪些神奇的性质？",
                    font="PingFang SC", font_size=30,
                    color=WHITE).move_to(UP * 4.4)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)

        # 绘制等腰三角形
        tri = self._triangle()
        self.play(Create(tri), run_time=0.9)

        # 标出腰相等
        lA, lB, lC = self._vertex_labels()
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        waist_AB = Line(self.A, self.B, color=self.C_WAIST, stroke_width=5)
        waist_AC = Line(self.A, self.C, color=self.C_WAIST, stroke_width=5)
        tick_AB  = self._tick(self.A, self.B, n=1, color=self.C_WAIST)
        tick_AC  = self._tick(self.A, self.C, n=1, color=self.C_WAIST)
        self.play(Create(waist_AB), Create(waist_AC), run_time=0.6)
        self.play(FadeIn(tick_AB), FadeIn(tick_AC), run_time=0.3)

        # 三个性质徽章快速浮现
        badges = VGroup(
            self._property_badge(1, "等边对等角", self.C_ANGLE,   DOWN * 3.4),
            self._property_badge(2, "三线合一",   self.C_MEDIAN,  DOWN * 4.2),
            self._property_badge(3, "轴对称",     self.C_AXIS,    DOWN * 5.0),
        )
        for b in badges:
            self.play(FadeIn(b, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(0.7)

        # 清场
        self.play(
            FadeOut(chap), FadeOut(title), FadeOut(hook),
            FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(waist_AB), FadeOut(waist_AC),
            FadeOut(tick_AB), FadeOut(tick_AC),
            FadeOut(badges),
            run_time=0.55
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 2 — 性质一：等边对等角
    # ═══════════════════════════════════════════════════════════
    def scene_2_equal_angles(self):
        t_tag, t_name = self._section_header("性质一", "等边对等角", self.C_ANGLE)
        self.play(FadeIn(t_tag, shift=DOWN * 0.15),
                  FadeIn(t_name, shift=DOWN * 0.15), run_time=0.55)

        # ── 三角形 + 标签 ──
        tri  = self._triangle()
        lA, lB, lC = self._vertex_labels()
        self.play(Create(tri), run_time=0.7)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.35)

        # ── 已知：高亮腰 AB = AC ──
        know_txt = Text("已知：AB = AC（两腰相等）",
                        font="PingFang SC", font_size=26,
                        color=WHITE).move_to(DOWN * 3.4)
        self.play(FadeIn(know_txt), run_time=0.4)

        waist_AB = Line(self.A, self.B, color=self.C_WAIST, stroke_width=6)
        waist_AC = Line(self.A, self.C, color=self.C_WAIST, stroke_width=6)
        tick_AB  = self._tick(self.A, self.B, n=1, color=self.C_WAIST)
        tick_AC  = self._tick(self.A, self.C, n=1, color=self.C_WAIST)

        self.play(Create(waist_AB), Create(waist_AC), run_time=0.7)
        self.play(FadeIn(tick_AB), FadeIn(tick_AC), run_time=0.35)

        # 条件公式
        cond = MathTex(r"AB = AC",
                       color=self.C_WAIST, font_size=36).move_to(DOWN * 4.15)
        self.play(Write(cond), run_time=0.6)
        self.wait(0.4)

        # ── 结论：∠B = ∠C 角弧出现 ──
        concl_txt = Text("∴ 两底角相等",
                         font="PingFang SC", font_size=26,
                         color=self.C_ANGLE).move_to(DOWN * 5.05)
        self.play(FadeIn(concl_txt), run_time=0.4)

        # ∠B: other_angle=True (叉积<0，顺时针)
        arc_B = self._angle_arc(self.B, self.A, self.C,
                                radius=0.52, color=self.C_ANGLE,
                                other_angle=True, double=True)
        # ∠C: other_angle=False (叉积>0，逆时针)
        arc_C = self._angle_arc(self.C, self.A, self.B,
                                radius=0.52, color=self.C_ANGLE,
                                other_angle=False, double=True)

        self.play(Create(arc_B), Create(arc_C), run_time=0.9)

        # 角度标签
        lbl_B = MathTex(r"\angle B", color=self.C_ANGLE,
                        font_size=28).move_to(self.B + np.array([0.65, 0.55, 0]))
        lbl_C = MathTex(r"\angle C", color=self.C_ANGLE,
                        font_size=28).move_to(self.C + np.array([-0.65, 0.55, 0]))
        self.play(FadeIn(lbl_B), FadeIn(lbl_C), run_time=0.4)

        # 公式
        formula = MathTex(r"\angle B = \angle C",
                          color=self.C_ANGLE, font_size=38).move_to(DOWN * 5.9)
        self.play(Write(formula), run_time=0.7)

        # 闪光强调
        self.play(
            Flash(self.B, color=self.C_ANGLE, flash_radius=0.4),
            Flash(self.C, color=self.C_ANGLE, flash_radius=0.4),
            run_time=0.6
        )

        # 规则框
        rule = self._rule_box(
            [("等边对等角：AB=AC  →  ∠B=∠C", self.C_ANGLE)],
            self.C_ANGLE, DOWN * 6.8, h=0.9
        )
        self.play(
            FadeOut(know_txt), FadeOut(cond), FadeOut(concl_txt), FadeOut(formula),
            FadeIn(rule), run_time=0.5
        )
        self.wait(1.6)

        # ── 清场 ──
        self.play(
            FadeOut(t_tag), FadeOut(t_name),
            FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(waist_AB), FadeOut(waist_AC),
            FadeOut(tick_AB), FadeOut(tick_AC),
            FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(rule),
            run_time=0.55
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 3 — 性质二：三线合一
    # ═══════════════════════════════════════════════════════════
    def scene_3_three_in_one(self):
        t_tag, t_name = self._section_header("性质二", "三线合一", self.C_MEDIAN)
        self.play(FadeIn(t_tag, shift=DOWN * 0.15),
                  FadeIn(t_name, shift=DOWN * 0.15), run_time=0.55)

        tri = self._triangle()
        lA, lB, lC = self._vertex_labels()
        self.play(Create(tri), run_time=0.7)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.35)

        # ── 先标 M 点 ──
        m_dot  = Dot(self.M, radius=0.08, color=self.C_HIGHLIGHT)
        m_lbl  = self._label_M()
        self.play(FadeIn(m_dot), FadeIn(m_lbl), run_time=0.4)

        # ─── 3a：中线 AM ───────────────────────────────────────
        step_txt = Text("① 中线 AM",
                        font="PingFang SC", font_size=28,
                        color=self.C_MEDIAN).move_to(DOWN * 3.5)
        self.play(FadeIn(step_txt), run_time=0.35)

        median = Line(self.A, self.M, color=self.C_MEDIAN, stroke_width=4)
        tick_BM = self._tick(self.B, self.M, n=2, color=self.C_MEDIAN, size=0.16)
        tick_MC = self._tick(self.M, self.C, n=2, color=self.C_MEDIAN, size=0.16)

        self.play(Create(median), run_time=0.7)
        self.play(FadeIn(tick_BM), FadeIn(tick_MC), run_time=0.35)

        # 公式：BM=MC
        f_median = MathTex(r"BM = MC",
                           color=self.C_MEDIAN, font_size=32).move_to(DOWN * 4.35)
        self.play(Write(f_median), run_time=0.55)
        self.wait(0.5)

        # ─── 3b：高线（从 A 向 BC 作垂线）─────────────────────
        self.play(FadeOut(step_txt), FadeOut(f_median), run_time=0.3)
        step_txt2 = Text("② 高线（从 A 向 BC 的垂线）",
                         font="PingFang SC", font_size=26,
                         color=self.C_ALTITUDE).move_to(DOWN * 3.5)
        self.play(FadeIn(step_txt2), run_time=0.35)

        # 高线就是 AM（因三线合一），用紫色覆盖
        altitude = Line(self.A, self.M,
                        color=self.C_ALTITUDE, stroke_width=5)

        # 直角标记（在 M 处）
        def right_angle_mark(corner, v_along, v_perp, size=0.18, color=YELLOW):
            """在 corner 处画直角标记"""
            e1 = v_along / np.linalg.norm(v_along) * size
            e2 = v_perp  / np.linalg.norm(v_perp)  * size
            sq = Polygon(
                corner,
                corner + e2,
                corner + e1 + e2,
                corner + e1,
                stroke_width=2, color=color, fill_opacity=0
            )
            return sq

        v_bc = self.C - self.B   # BC 方向（水平）
        v_am = self.A - self.M   # AM 方向（向上）
        ra   = right_angle_mark(self.M, v_bc / np.linalg.norm(v_bc),
                                v_am / np.linalg.norm(v_am),
                                size=0.20, color=YELLOW)

        self.play(Create(altitude), run_time=0.7)
        self.play(FadeIn(ra), run_time=0.35)

        f_alt = MathTex(r"AM \perp BC",
                        color=self.C_ALTITUDE, font_size=32).move_to(DOWN * 4.35)
        self.play(Write(f_alt), run_time=0.55)

        # 惊叹：和中线重合！
        overlap_txt = Text("↑ 和中线重合！",
                           font="PingFang SC", font_size=22,
                           color=self.C_HIGHLIGHT).move_to(DOWN * 5.05)
        self.play(FadeIn(overlap_txt, scale=0.8), run_time=0.45)
        self.wait(0.6)

        # ─── 3c：顶角平分线 ────────────────────────────────────
        self.play(
            FadeOut(step_txt2), FadeOut(f_alt), FadeOut(overlap_txt),
            run_time=0.3
        )
        step_txt3 = Text("③ 顶角 ∠A 的平分线",
                         font="PingFang SC", font_size=26,
                         color=self.C_BISECT).move_to(DOWN * 3.5)
        self.play(FadeIn(step_txt3), run_time=0.35)

        bisector = Line(self.A, self.M,
                        color=self.C_BISECT, stroke_width=5)

        # ∠BAM：Line(A,B)/Line(A,M) → other_angle=False（叉积>0）
        arc_BAM = self._angle_arc(self.A, self.B, self.M,
                                  radius=0.42, color=self.C_BISECT,
                                  other_angle=False, sw=2.5)
        # ∠CAM：Line(A,C)/Line(A,M) → other_angle=True（叉积<0）
        arc_CAM = self._angle_arc(self.A, self.C, self.M,
                                  radius=0.42, color=self.C_BISECT,
                                  other_angle=True, sw=2.5)

        self.play(Create(bisector), run_time=0.7)
        self.play(Create(arc_BAM), Create(arc_CAM), run_time=0.7)

        f_bis = MathTex(r"\angle BAM = \angle CAM",
                        color=self.C_BISECT, font_size=30).move_to(DOWN * 4.35)
        self.play(Write(f_bis), run_time=0.6)

        overlap_txt2 = Text("↑ 还是同一条线！",
                            font="PingFang SC", font_size=22,
                            color=self.C_HIGHLIGHT).move_to(DOWN * 5.05)
        self.play(FadeIn(overlap_txt2, scale=0.8), run_time=0.45)
        self.wait(0.6)

        # ─── 3d：三线合并动画 ────────────────────────────────────
        self.play(
            FadeOut(step_txt3), FadeOut(f_bis), FadeOut(overlap_txt2),
            run_time=0.3
        )

        # 三色线条聚合成一条彩虹线
        line_trio = VGroup(
            Line(self.A, self.M, color=self.C_MEDIAN,   stroke_width=8),
            Line(self.A, self.M, color=self.C_ALTITUDE, stroke_width=5),
            Line(self.A, self.M, color=self.C_BISECT,   stroke_width=3),
        )

        flash_txt = Text("三线合一！",
                         font="PingFang SC", font_size=46,
                         color=self.C_HIGHLIGHT).move_to(DOWN * 3.8)

        self.play(
            FadeOut(median), FadeOut(altitude), FadeOut(bisector),
            FadeIn(line_trio),
            run_time=0.5
        )
        self.play(Write(flash_txt), run_time=0.6)
        self.play(
            Flash(self.M, color=self.C_HIGHLIGHT, flash_radius=0.5),
            run_time=0.55
        )
        self.wait(0.5)

        # 三行说明
        legend = VGroup(
            Text("绿 = 中线   BM = MC",    font="PingFang SC",
                 font_size=22, color=self.C_MEDIAN),
            Text("紫 = 高线   AM ⊥ BC",   font="PingFang SC",
                 font_size=22, color=self.C_ALTITUDE),
            Text("橙 = 顶角平分线  ∠BAM = ∠CAM",
                 font="PingFang SC", font_size=22, color=self.C_BISECT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(DOWN * 5.3)

        self.play(FadeIn(legend), run_time=0.6)
        self.wait(1.8)

        # ── 清场 ──
        self.play(
            FadeOut(t_tag), FadeOut(t_name),
            FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(m_dot), FadeOut(m_lbl),
            FadeOut(tick_BM), FadeOut(tick_MC),
            FadeOut(ra),
            FadeOut(arc_BAM), FadeOut(arc_CAM),
            FadeOut(line_trio),
            FadeOut(flash_txt), FadeOut(legend),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 4 — 性质三：轴对称
    # ═══════════════════════════════════════════════════════════
    def scene_4_symmetry(self):
        t_tag, t_name = self._section_header("性质三", "轴对称图形", self.C_AXIS)
        self.play(FadeIn(t_tag, shift=DOWN * 0.15),
                  FadeIn(t_name, shift=DOWN * 0.15), run_time=0.55)

        tri = self._triangle()
        lA, lB, lC = self._vertex_labels()
        self.play(Create(tri), run_time=0.7)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.35)

        # ── 对称轴：直线 AM（延伸到上下边框）──
        axis_dir = (self.M - self.A)
        axis_dir = axis_dir / np.linalg.norm(axis_dir)
        axis_top = self.A + (-2.0) * axis_dir   # 向上延伸
        axis_bot = self.M + ( 1.5) * axis_dir   # 向下延伸

        axis = DashedLine(axis_top, axis_bot,
                          color=self.C_AXIS, stroke_width=3,
                          dash_length=0.18, dashed_ratio=0.6)

        axis_lbl = Text("对称轴",
                        font="PingFang SC", font_size=24,
                        color=self.C_AXIS).next_to(axis_top, UP, buff=0.08)

        self.play(Create(axis), run_time=0.8)
        self.play(FadeIn(axis_lbl), run_time=0.35)

        # 解释文字
        exp1 = Text("等腰三角形是轴对称图形",
                    font="PingFang SC", font_size=27,
                    color=WHITE).move_to(DOWN * 3.6)
        exp2 = Text("底边的垂直平分线是对称轴",
                    font="PingFang SC", font_size=25,
                    color=self.C_AXIS).move_to(DOWN * 4.35)
        self.play(FadeIn(exp1), run_time=0.4)
        self.play(FadeIn(exp2), run_time=0.4)
        self.wait(0.5)

        # ── 折叠动画：B 沿对称轴映射到 C ──
        fold_txt = Text("沿对称轴折叠……",
                        font="PingFang SC", font_size=26,
                        color=self.C_HIGHLIGHT).move_to(DOWN * 5.15)
        self.play(FadeIn(fold_txt), run_time=0.35)

        # 左半三角形（AB+BM）
        left_half = Polygon(
            self.A, self.B, self.M,
            fill_color=self.C_WAIST, fill_opacity=0.35,
            stroke_color=self.C_WAIST, stroke_width=3
        )
        # 右半三角形（AC+CM）
        right_half = Polygon(
            self.A, self.C, self.M,
            fill_color=self.C_AXIS, fill_opacity=0.35,
            stroke_color=self.C_AXIS, stroke_width=3
        )

        self.play(FadeIn(left_half), FadeIn(right_half), run_time=0.5)
        self.wait(0.3)

        # 右半淡出，左半 Transform 到右半位置
        right_target = Polygon(
            self.A, self.C, self.M,
            fill_color=self.C_WAIST, fill_opacity=0.55,
            stroke_color=self.C_WAIST, stroke_width=3
        )

        left_copy = left_half.copy()
        self.play(FadeOut(right_half), run_time=0.25)
        self.play(Transform(left_copy, right_target), run_time=1.1)

        # 完全重合提示
        match_txt = Text("完全重合！",
                         font="PingFang SC", font_size=38,
                         color=self.C_SUCCESS).move_to(DOWN * 6.1)
        self.play(FadeIn(match_txt, scale=0.7), run_time=0.5)
        self.play(Flash(self.M, color=self.C_AXIS, flash_radius=0.45),
                  run_time=0.5)
        self.wait(1.0)

        # B→C 对应箭头
        b_dot = Dot(self.B, radius=0.10, color=self.C_WAIST)
        c_dot = Dot(self.C, radius=0.10, color=self.C_WAIST)
        bc_arc_arrow = CurvedArrow(
            self.B, self.C,
            angle=-PI / 3,
            color=self.C_HIGHLIGHT,
            stroke_width=3, tip_length=0.22
        )
        mirror_lbl = Text("B  →  C（对称点）",
                          font="PingFang SC", font_size=22,
                          color=self.C_HIGHLIGHT).move_to(DOWN * 2.55)

        self.play(
            FadeIn(b_dot), FadeIn(c_dot),
            Create(bc_arc_arrow), FadeIn(mirror_lbl),
            run_time=0.7
        )
        self.wait(1.2)

        # ── 清场 ──
        self.play(
            FadeOut(t_tag), FadeOut(t_name),
            FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(axis), FadeOut(axis_lbl),
            FadeOut(exp1), FadeOut(exp2),
            FadeOut(fold_txt), FadeOut(match_txt),
            FadeOut(left_half), FadeOut(left_copy),
            FadeOut(b_dot), FadeOut(c_dot),
            FadeOut(bc_arc_arrow), FadeOut(mirror_lbl),
            run_time=0.6
        )

    # ═══════════════════════════════════════════════════════════
    # Scene 5 — 总结 + 片尾
    # ═══════════════════════════════════════════════════════════
    def scene_5_summary_outro(self):
        # ── 标题 ──
        sum_title = Text("知识总结",
                         font="PingFang SC", font_size=44,
                         color=self.C_HIGHLIGHT).move_to(UP * 6.5)
        self.play(Write(sum_title), run_time=0.6)

        # ── 三张卡片 ──
        cards_data = [
            ("性质一", "等边对等角",
             "AB = AC  →  ∠B = ∠C",
             self.C_ANGLE,   UP * 4.5),
            ("性质二", "三线合一",
             "中线 = 高线 = 顶角平分线",
             self.C_MEDIAN,  UP * 2.1),
            ("性质三", "轴对称图形",
             "底边垂直平分线 = 对称轴",
             self.C_AXIS,    DOWN * 0.3),
        ]

        all_cards = VGroup()
        for tag, name, content, color, pos in cards_data:
            bg = RoundedRectangle(
                width=7.8, height=1.8, corner_radius=0.32,
                color=color,
                fill_color=ManimColor(color).interpolate(BLACK, 0.82),
                fill_opacity=0.95
            ).move_to(pos)

            tag_t = Text(tag, font="PingFang SC",
                         font_size=20, color=color)
            name_t = Text(name, font="PingFang SC",
                          font_size=30, color=WHITE)
            cont_t = Text(content, font="PingFang SC",
                          font_size=22, color=color)
            inner = VGroup(tag_t, name_t, cont_t).arrange(DOWN, buff=0.12)
            inner.move_to(pos)

            card = VGroup(bg, inner)
            all_cards.add(card)

        for card in all_cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.45)
            self.wait(0.1)

        # 核心关系式
        formula_box_bg = RoundedRectangle(
            width=7.8, height=1.1, corner_radius=0.3,
            color=self.C_HIGHLIGHT,
            fill_color=ManimColor(color).interpolate(BLACK, 0.88),
            fill_opacity=0.95
        ).move_to(DOWN * 2.35)

        formula = MathTex(
            r"AB = AC \Rightarrow \angle B = \angle C",
            color=self.C_HIGHLIGHT, font_size=30
        ).move_to(DOWN * 2.35)

        self.play(FadeIn(formula_box_bg), Write(formula), run_time=0.8)
        self.wait(1.2)

        # ── 片尾：淡出卡片，放大作者信息 ──
        self.play(
            FadeOut(sum_title),
            FadeOut(all_cards),
            FadeOut(formula_box_bg), FadeOut(formula),
            run_time=0.6
        )

        outro_name = Text("上海初高中数学直通车",
                          font="PingFang SC", font_size=44,
                          color=WHITE).move_to(UP * 1.8)
        outro_id   = Text("@emptyandcalm",
                          font="PingFang SC", font_size=32,
                          color=self.C_AUX).move_to(UP * 0.8)
        cta        = Text("关注我，学更多数学技巧！",
                          font="PingFang SC", font_size=30,
                          color=self.C_HIGHLIGHT).move_to(DOWN * 0.5)

        self.play(Transform(self.author_bar, outro_name), run_time=0.65)
        self.play(FadeIn(outro_id, shift=UP * 0.25), run_time=0.4)
        self.play(FadeIn(cta, shift=UP * 0.2), run_time=0.5)

        # 装饰：三个等腰小三角旋转
        deco = VGroup()
        colors = [self.C_ANGLE, self.C_MEDIAN, self.C_AXIS]
        for i, col in enumerate(colors):
            angle_rot = i * 2 * PI / 3
            size = 0.38
            tri_d = Polygon(
                np.array([0, size * 1.1, 0]),
                np.array([-size, -size * 0.5, 0]),
                np.array([ size, -size * 0.5, 0]),
                fill_color=col, fill_opacity=0.75, stroke_width=0
            ).rotate(angle_rot).shift(
                np.array([np.cos(angle_rot) * 2.2,
                          np.sin(angle_rot) * 0.8 - 2.6, 0])
            )
            deco.add(tri_d)

        self.play(*[FadeIn(d, scale=0.3) for d in deco], run_time=0.55)
        self.play(Rotate(deco, angle=TAU / 2, run_time=1.3))
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(self.author_bar),
            FadeOut(outro_id), FadeOut(cta), FadeOut(deco),
            run_time=1.0
        )


# ═══════════════════════════════════════════════════════════════
# 渲染命令
# ═══════════════════════════════════════════════════════════════
# 快速预览:  manim -pql isosceles_properties.py IsoscelesTriangleProperties
# 高质量:    manim -qh  isosceles_properties.py IsoscelesTriangleProperties