"""
parallel_lines.py
平行线的判定 — 七年级数学 TikTok竖屏动画
作者: 上海初高中数学直通车 @emptyandcalm

知识点:
  (1) 同位角相等 ⟹ 两直线平行
  (2) 内错角相等 ⟹ 两直线平行
  (3) 同旁内角互补 ⟹ 两直线平行

渲染命令:
  manim -pql parallel_lines.py ParallelLineDetermination  # 预览
  manim -qh  parallel_lines.py ParallelLineDetermination  # 高质量
"""

from manim import *
import numpy as np

# ── TikTok 竖屏配置 ──────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 全局常量 ─────────────────────────────────────────────
FONT = "Noto Sans CJK SC"  # 中文字体

C_LINE1   = "#3498db"   # 蓝  — 直线 l
C_LINE2   = "#2ecc71"   # 绿  — 直线 m
C_TRANS   = "#e74c3c"   # 红  — 截线 t
C_YELLOW  = "#f1c40f"   # 黄  — 角1颜色
C_CYAN    = "#1abc9c"   # 青  — 角2颜色
C_ORANGE  = "#e67e22"   # 橙
C_GOLD    = "#f39c12"   # 金
C_GRAY    = "#bdc3c7"   # 灰
BG_COLOR  = "#1a1a2e"   # 深蓝背景


# ══════════════════════════════════════════════════════════
class ParallelLineDetermination(Scene):
    """平行线的判定方法 — 七年级数学动画"""

    # ──────────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()
        self.scene_1_opening()
        self.scene_2_diagram()
        self.scene_3_corresponding()
        self.scene_4_alternate()
        self.scene_5_cointerior()
        self.scene_6_summary()
        self.scene_7_outro()

    # ══════════════════════════════════════════════════════
    # 几何初始化
    # ══════════════════════════════════════════════════════
    def setup_geometry(self):
        """
        统一计算所有坐标，后续场景只读不写。
        截线方向: arctan(2) ≈ 63.43°（过原点）
        l1: y = 1.2  (上直线)
        l2: y = -1.5 (下直线)
        """
        # 截线角度与方向
        self.ta    = np.arctan(2)              # ≈ 1.1071 rad
        self.sin_a = np.sin(self.ta)           # 2/√5
        self.cos_a = np.cos(self.ta)           # 1/√5
        self.td    = np.array([self.cos_a, self.sin_a, 0])  # 截线单位方向

        # 两横线纵坐标
        self.Y1 =  1.2
        self.Y2 = -1.5

        # 精确计算交点（截线过原点）
        t_P = self.Y1 / self.sin_a
        t_Q = self.Y2 / self.sin_a
        self.P = np.array([t_P * self.cos_a, self.Y1, 0])   # (0.600, 1.200)
        self.Q = np.array([t_Q * self.cos_a, self.Y2, 0])   # (-0.750, -1.500)

        # 直线端点（延伸 ±3.0 单位）
        self.LINE_EXT = 3.0
        self.L1_L = np.array([self.P[0] - self.LINE_EXT, self.Y1, 0])
        self.L1_R = np.array([self.P[0] + self.LINE_EXT, self.Y1, 0])
        self.L2_L = np.array([self.Q[0] - self.LINE_EXT, self.Y2, 0])
        self.L2_R = np.array([self.Q[0] + self.LINE_EXT, self.Y2, 0])

        # 截线端点（交点外各延伸 1.5）
        self.T_START = self.Q - 1.5 * self.td
        self.T_END   = self.P + 1.5 * self.td

        # 角弧半径
        self.R = 0.42

        # 角标签位置辅助（角中线方向 + 偏移）
        def _label_pos(center, start, sweep, dist=0.72):
            mid = start + sweep / 2
            return center + dist * np.array([np.cos(mid), np.sin(mid), 0])

        self._lpos = _label_pos

        # 验证
        self._verify()

    def _verify(self):
        eps = 1e-9
        assert abs(self.P[1] - self.Y1) < eps
        assert abs(self.Q[1] - self.Y2) < eps
        # 同旁内角互补
        s4 = np.pi - self.ta  # ∠4 sweep
        s5 = self.ta           # ∠5 sweep
        assert abs(s4 + s5 - np.pi) < eps
        print("✓ 几何验证通过: P,Q,角度关系均正确")

    # ══════════════════════════════════════════════════════
    # 辅助: 扇形 & 弧线 & 平行线标记
    # ══════════════════════════════════════════════════════
    def make_sector(self, center, start, sweep, color, r=None, opacity=0.55):
        """在 center 点创建角扇形（使用 shift 而非 move_to）"""
        r = r or self.R
        return (
            Sector(radius=r, start_angle=start, angle=sweep,
                   color=color, fill_opacity=opacity, stroke_width=0)
            .shift(center)
        )

    def make_arc(self, center, start, sweep, color, r=None, sw=2.5):
        """在 center 点创建角弧线"""
        r = r or self.R
        return (
            Arc(radius=r, start_angle=start, angle=sweep,
                color=color, stroke_width=sw)
            .shift(center)
        )

    def make_tick(self, center, start, sweep, color="#ffffff"):
        """角弧上的等号小标记（两条细线表示角相等）"""
        mid = start + sweep / 2
        mid_pt = center + (self.R + 0.05) * np.array([np.cos(mid), np.sin(mid), 0])
        perp   = np.array([-np.sin(mid), np.cos(mid), 0]) * 0.12
        t1 = Line(mid_pt - perp * 0.4, mid_pt + perp * 0.4, color=color, stroke_width=2)
        t2 = t1.copy().shift(np.array([np.cos(mid), np.sin(mid), 0]) * 0.12)
        return VGroup(t1, t2)

    def make_parallel_marks(self, line_y, color=WHITE, n=1):
        """在横线上画平行标记箭头（小三角形）"""
        arrow = Arrow(
            start=np.array([0, line_y, 0]) + LEFT * 0.18,
            end  =np.array([0, line_y, 0]) + RIGHT * 0.18,
            buff=0, color=color, stroke_width=2.5,
            tip_length=0.18, max_tip_length_to_length_ratio=0.9
        )
        return arrow

    # ══════════════════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════════════════
    def scene_1_opening(self):
        # 作者信息（常驻顶部）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=20, color=C_GRAY
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.15), run_time=0.4)

        # 钩子
        hook = Text("如何判断两直线平行?", font=FONT, font_size=44, color=C_GOLD)\
               .move_to(UP * 5.5)
        sub  = Text("3种方法，一次讲清！", font=FONT, font_size=30, color=WHITE)\
               .move_to(UP * 4.6)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.9)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.4)

    # ══════════════════════════════════════════════════════
    # Scene 2: 建立三线八角图示
    # ══════════════════════════════════════════════════════
    def scene_2_diagram(self):
        title = Text("三线八角", font=FONT, font_size=38, color=C_GOLD).move_to(UP * 5.6)
        self.play(Write(title), run_time=0.6)

        # 建立图形
        l1 = Line(self.L1_L, self.L1_R, color=C_LINE1, stroke_width=3)
        l2 = Line(self.L2_L, self.L2_R, color=C_LINE2, stroke_width=3)
        t  = Line(self.T_START, self.T_END, color=C_TRANS, stroke_width=3)

        lbl_l = Text("l", font=FONT, font_size=26, color=C_LINE1)\
                .next_to(self.L1_R, RIGHT, buff=0.12)
        lbl_m = Text("m", font=FONT, font_size=26, color=C_LINE2)\
                .next_to(self.L2_R, RIGHT, buff=0.12)
        lbl_t = Text("t", font=FONT, font_size=24, color=C_TRANS)\
                .next_to(self.T_END, UR, buff=0.08)

        p_dot = Dot(self.P, color=WHITE, radius=0.07)
        q_dot = Dot(self.Q, color=WHITE, radius=0.07)

        self.play(Create(l1), Write(lbl_l), run_time=0.7)
        self.play(Create(l2), Write(lbl_m), run_time=0.7)
        self.play(Create(t),  Write(lbl_t), run_time=0.7)
        self.play(FadeIn(p_dot), FadeIn(q_dot), run_time=0.4)

        explain = Text("直线 t 截直线 l、m，形成8个角",
                       font=FONT, font_size=22, color=C_GRAY).move_to(DOWN * 4.5)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.8)

        # 存储，后续场景复用
        self.diagram = VGroup(l1, l2, t, lbl_l, lbl_m, lbl_t, p_dot, q_dot)
        self.play(FadeOut(title), FadeOut(explain), run_time=0.4)

    # ══════════════════════════════════════════════════════
    # Scene 3: 同位角相等 → 两直线平行
    # ══════════════════════════════════════════════════════
    def scene_3_corresponding(self):
        ta = self.ta
        P, Q = self.P, self.Q

        title = Text("方法一  同位角相等", font=FONT, font_size=34, color=C_YELLOW)\
                .move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # ∠1 at P (上右, start=0, sweep=ta)
        sec1 = self.make_sector(P, 0, ta, C_YELLOW)
        arc1 = self.make_arc(P, 0, ta, C_YELLOW)
        pos1 = self._lpos(P, 0, ta)
        lbl1 = Text("∠1", font=FONT, font_size=22, color=C_YELLOW).move_to(pos1)

        # ∠5 at Q (上右, start=0, sweep=ta) — 完全相同位置
        sec5 = self.make_sector(Q, 0, ta, C_CYAN)
        arc5 = self.make_arc(Q, 0, ta, C_CYAN)
        pos5 = self._lpos(Q, 0, ta)
        lbl5 = Text("∠5", font=FONT, font_size=22, color=C_CYAN).move_to(pos5)

        self.play(FadeIn(sec1), Create(arc1), FadeIn(lbl1), run_time=0.6)
        self.play(FadeIn(sec5), Create(arc5), FadeIn(lbl5), run_time=0.6)

        # 解释：位置相同
        exp1 = Text("两角相对截线位置完全相同", font=FONT, font_size=22, color=C_GRAY)\
               .move_to(DOWN * 4.2)
        exp2 = Text("→ 叫做同位角", font=FONT, font_size=24, color=C_YELLOW)\
               .move_to(DOWN * 4.9)
        self.play(FadeIn(exp1), run_time=0.5)
        self.play(FadeIn(exp2), run_time=0.4)
        self.wait(1.0)
        self.play(FadeOut(exp1), FadeOut(exp2), run_time=0.3)

        # 强调相等 → 平行
        self.play(
            sec1.animate.set_color(YELLOW).set_opacity(0.8),
            sec5.animate.set_color(YELLOW).set_opacity(0.8),
            run_time=0.5
        )

        conc = MathTex(r"\angle 1 = \angle 5 \;\Rightarrow\; l \parallel m",
                       font_size=36, color=YELLOW)
        conc.move_to(DOWN * 4.3)
        box = SurroundingRectangle(conc, color=YELLOW, buff=0.18, corner_radius=0.12)

        self.play(Write(conc), Create(box), run_time=0.9)
        self.wait(1.6)

        self.play(
            FadeOut(title), FadeOut(sec1), FadeOut(sec5),
            FadeOut(arc1), FadeOut(arc5), FadeOut(lbl1), FadeOut(lbl5),
            FadeOut(conc), FadeOut(box), run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 4: 内错角相等 → 两直线平行
    # ══════════════════════════════════════════════════════
    def scene_4_alternate(self):
        ta = self.ta
        P, Q = self.P, self.Q

        title = Text("方法二  内错角相等", font=FONT, font_size=34, color=C_CYAN)\
                .move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # ∠3 at P (下左, start=π, sweep=ta) — 在两线间，截线左侧
        sec3 = self.make_sector(P, np.pi, ta, C_YELLOW)
        arc3 = self.make_arc(P, np.pi, ta, C_YELLOW)
        pos3 = self._lpos(P, np.pi, ta, dist=0.75)
        lbl3 = Text("∠3", font=FONT, font_size=22, color=C_YELLOW).move_to(pos3)

        # ∠5 at Q (上右, start=0, sweep=ta) — 在两线间，截线右侧
        sec5 = self.make_sector(Q, 0, ta, C_CYAN)
        arc5 = self.make_arc(Q, 0, ta, C_CYAN)
        pos5 = self._lpos(Q, 0, ta)
        lbl5 = Text("∠5", font=FONT, font_size=22, color=C_CYAN).move_to(pos5)

        self.play(FadeIn(sec3), Create(arc3), FadeIn(lbl3), run_time=0.6)
        self.play(FadeIn(sec5), Create(arc5), FadeIn(lbl5), run_time=0.6)

        # 画一条虚线连接，指示"两线内侧，截线两侧"
        region_line = DashedLine(
            self.P + DOWN * 0.1, self.Q + UP * 0.1,
            color=WHITE, dash_length=0.08, stroke_width=1
        )
        self.play(Create(region_line), run_time=0.4)

        exp1 = Text("两角均在 l、m 之间", font=FONT, font_size=22, color=C_GRAY)\
               .move_to(DOWN * 4.0)
        exp2 = Text("且位于截线两侧 → 内错角", font=FONT, font_size=24, color=C_CYAN)\
               .move_to(DOWN * 4.8)
        self.play(FadeIn(exp1), run_time=0.4)
        self.play(FadeIn(exp2), run_time=0.4)
        self.wait(1.0)
        self.play(FadeOut(exp1), FadeOut(exp2), FadeOut(region_line), run_time=0.3)

        # 强调相等
        self.play(
            sec3.animate.set_color(GREEN).set_opacity(0.8),
            sec5.animate.set_color(GREEN).set_opacity(0.8),
            run_time=0.5
        )

        conc = MathTex(r"\angle 3 = \angle 5 \;\Rightarrow\; l \parallel m",
                       font_size=36, color=GREEN)
        conc.move_to(DOWN * 4.3)
        box = SurroundingRectangle(conc, color=GREEN, buff=0.18, corner_radius=0.12)

        self.play(Write(conc), Create(box), run_time=0.9)
        self.wait(1.6)

        self.play(
            FadeOut(title), FadeOut(sec3), FadeOut(sec5),
            FadeOut(arc3), FadeOut(arc5), FadeOut(lbl3), FadeOut(lbl5),
            FadeOut(conc), FadeOut(box), run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 5: 同旁内角互补 → 两直线平行
    # ══════════════════════════════════════════════════════
    def scene_5_cointerior(self):
        ta = self.ta
        P, Q = self.P, self.Q

        title = Text("方法三  同旁内角互补", font=FONT, font_size=34, color=C_ORANGE)\
                .move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # ∠4 at P (下右大角, start=π+ta, sweep=π-ta) — 同侧右，在两线间
        sweep4 = np.pi - ta
        start4 = np.pi + ta
        sec4 = self.make_sector(P, start4, sweep4, C_ORANGE)
        arc4 = self.make_arc(P, start4, sweep4, C_ORANGE)
        pos4 = self._lpos(P, start4, sweep4, dist=0.75)
        lbl4 = Text("∠4", font=FONT, font_size=22, color=C_ORANGE).move_to(pos4)

        # ∠5 at Q (上右小角, start=0, sweep=ta) — 同侧右，在两线间
        sec5 = self.make_sector(Q, 0, ta, C_YELLOW)
        arc5 = self.make_arc(Q, 0, ta, C_YELLOW)
        pos5 = self._lpos(Q, 0, ta)
        lbl5 = Text("∠5", font=FONT, font_size=22, color=C_YELLOW).move_to(pos5)

        self.play(FadeIn(sec4), Create(arc4), FadeIn(lbl4), run_time=0.6)
        self.play(FadeIn(sec5), Create(arc5), FadeIn(lbl5), run_time=0.6)

        exp1 = Text("两角在截线同侧，均在两线之间", font=FONT, font_size=22, color=C_GRAY)\
               .move_to(DOWN * 4.0)
        exp2 = Text("→ 同旁内角", font=FONT, font_size=24, color=C_ORANGE)\
               .move_to(DOWN * 4.7)
        self.play(FadeIn(exp1), run_time=0.4)
        self.play(FadeIn(exp2), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(exp1), FadeOut(exp2), run_time=0.3)

        # 和为 180° 演示：两个扇形拼合变成半圆
        sum_txt = MathTex(r"\angle 4 + \angle 5 = 180^{\circ}",
                          font_size=30, color=WHITE).move_to(DOWN * 4.0)
        self.play(Write(sum_txt), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(sum_txt), run_time=0.3)

        conc = MathTex(r"\angle 4 + \angle 5 = 180^{\circ} \;\Rightarrow\; l \parallel m",
                       font_size=30, color=C_ORANGE)
        conc.move_to(DOWN * 4.3)
        box = SurroundingRectangle(conc, color=C_ORANGE, buff=0.18, corner_radius=0.12)

        self.play(Write(conc), Create(box), run_time=0.9)
        self.wait(1.6)

        self.play(
            FadeOut(title), FadeOut(sec4), FadeOut(sec5),
            FadeOut(arc4), FadeOut(arc5), FadeOut(lbl4), FadeOut(lbl5),
            FadeOut(conc), FadeOut(box), run_time=0.5
        )

    # ══════════════════════════════════════════════════════
    # Scene 6: 总结
    # ══════════════════════════════════════════════════════
    def scene_6_summary(self):
        # 图示淡出
        self.play(FadeOut(self.diagram), run_time=0.4)

        title = Text("三种判定方法", font=FONT, font_size=40, color=C_GOLD)\
                .move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 三条方法卡片
        methods = [
            (r"\angle 1 = \angle 2", "同位角相等",   "两直线平行", C_YELLOW, 3.8),
            (r"\angle 3 = \angle 4", "内错角相等",   "两直线平行", C_CYAN,   1.8),
            (r"\angle 5 + \angle 6 = 180^{\circ}", "同旁内角互补", "两直线平行", C_ORANGE, -0.2),
        ]

        cards = []
        for formula, cond_txt, conc_txt, color, y in methods:
            # 序号圆
            idx = methods.index((formula, cond_txt, conc_txt, color, y)) + 1
            circle_bg = Circle(radius=0.28, fill_color=color, fill_opacity=1,
                               stroke_width=0).move_to(LEFT * 3.8 + UP * y)
            num = Text(str(idx), font=FONT, font_size=22, color=WHITE)\
                  .move_to(circle_bg.get_center())

            # 条件文字
            cond = Text(cond_txt, font=FONT, font_size=26, color=color)\
                   .next_to(circle_bg, RIGHT, buff=0.25)

            # 箭头
            arr = MathTex(r"\Rightarrow", font_size=28, color=WHITE)\
                  .next_to(cond, RIGHT, buff=0.25)

            # 结论
            conc = Text(conc_txt, font=FONT, font_size=26, color=WHITE)\
                   .next_to(arr, RIGHT, buff=0.25)

            # 背景条
            row = VGroup(circle_bg, num, cond, arr, conc)
            bg = RoundedRectangle(
                width=8.0, height=0.85, corner_radius=0.15,
                color=color, fill_opacity=0.1, stroke_width=1.5
            ).move_to(UP * y)

            card = VGroup(bg, circle_bg, num, cond, arr, conc)
            card.shift(LEFT * 20)   # 初始在屏幕外
            cards.append(card)

        for card in cards:
            self.play(card.animate.shift(RIGHT * 20), run_time=0.5)
            self.wait(0.2)

        self.wait(0.5)

        # 记忆口诀
        slogan = Text("记忆口诀：等等补，线平行！",
                      font=FONT, font_size=30, color=C_GOLD)\
                 .move_to(DOWN * 2.0)
        slogan_box = SurroundingRectangle(slogan, color=C_GOLD, buff=0.2, corner_radius=0.12)

        self.play(Write(slogan), Create(slogan_box), run_time=0.8)
        self.wait(1.5)

        # 补充: 平行符号动画
        para_note = Text("记住: // 表示平行", font=FONT, font_size=22, color=C_GRAY)\
                    .move_to(DOWN * 3.2)
        self.play(FadeIn(para_note), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            *[FadeOut(c) for c in cards],
            FadeOut(slogan), FadeOut(slogan_box),
            FadeOut(para_note),
            run_time=0.7
        )

    # ══════════════════════════════════════════════════════
    # Scene 7: 片尾
    # ══════════════════════════════════════════════════════
    def scene_7_outro(self):
        name = Text("上海初高中数学直通车", font=FONT, font_size=42, color=WHITE)\
               .move_to(UP * 1.8)
        uid  = Text("@emptyandcalm",       font=FONT, font_size=30, color=C_GRAY)\
               .move_to(UP * 0.8)
        cta  = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=C_GOLD)\
               .move_to(DOWN * 0.4)

        # 作者信息动画过渡
        self.play(Transform(self.author, name), run_time=0.7)
        self.play(FadeIn(uid, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(cta, shift=UP * 0.2, scale=1.05), run_time=0.5)

        # 装饰：三色小圆点
        dots = VGroup(*[
            Dot(point=np.array([1.8 * np.cos(i * 2*np.pi/6),
                                1.8 * np.sin(i * 2*np.pi/6), 0]),
                radius=0.14,
                color=[C_YELLOW, C_CYAN, C_ORANGE, C_LINE1, C_LINE2, C_TRANS][i],
                fill_opacity=0.9)
            for i in range(6)
        ]).move_to(DOWN * 2.5)

        self.play(*[GrowFromCenter(d) for d in dots], run_time=0.6)
        self.play(Rotate(dots, angle=PI, run_time=1.2))
        self.wait(0.5)

        self.play(
            FadeOut(self.author), FadeOut(uid),
            FadeOut(cta), FadeOut(dots),
            run_time=0.9
        )