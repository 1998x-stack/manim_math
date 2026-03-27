"""
004_梯形.py — 梯形的认识 教学动画

知识点:
  - 梯形的定义: 只有一组对边平行的四边形
  - 梯形各部分名称: 上底、下底、腰、高
  - 上底 ∥ 下底，两腰不平行
  - 高: 从上底一点向下底引垂线，该点到垂足的距离

年级: 四年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR        = "#1a1a2e"
COLOR_TRAPEZOID = "#3b82f6"   # 蓝 — 梯形主体
COLOR_TOP_BASE  = "#f59e0b"   # 橙 — 上底
COLOR_BOT_BASE  = "#22c55e"   # 绿 — 下底
COLOR_LEG       = "#f472b6"   # 粉 — 腰
COLOR_HEIGHT    = "#a78bfa"   # 紫 — 高
COLOR_HL        = "#fbbf24"   # 黄 — 高亮
COLOR_AUX       = "#94a3b8"   # 灰 — 辅助
COLOR_PARALLEL  = "#06b6d4"   # 青 — 平行符号
COLOR_AUTHOR    = "#6b7280"
FONT            = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TrapezoidLesson(Scene):
    """
    梯形的认识教学动画
    场景顺序:
      1. 开场钩子
      2. 梯形定义（只有一组对边平行）
      3. 梯形各部分名称（上底、下底、腰）
      4. 梯形的高
      5. 特殊梯形（直角梯形、等腰梯形）
      6. 综合总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_parts()
        self.scene_4_height()
        self.scene_5_special()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（NumPy 精确计算）"""

        # ===== 主梯形顶点 =====
        # 下底: A(左下) → B(右下)，长度 4
        # 上底: D(左上) → C(右上)，长度 2.2，居中
        self.OFFSET = np.array([0.0, 0.5, 0.0])   # 整体上移

        # 原始坐标（未偏移）
        self.A_raw = np.array([-2.0, -1.5, 0.0])
        self.B_raw = np.array([ 2.0, -1.5, 0.0])
        self.C_raw = np.array([ 1.1,  1.5, 0.0])
        self.D_raw = np.array([-1.1,  1.5, 0.0])

        # 加偏移
        self.A = self.A_raw + self.OFFSET
        self.B = self.B_raw + self.OFFSET
        self.C = self.C_raw + self.OFFSET
        self.D = self.D_raw + self.OFFSET

        # ===== 派生点 =====
        # 高的垂足：从 D 向 AB（下底，水平线）作垂线
        # AB 是水平线，垂足 x = D[0], y = A[1]
        self.foot_D = np.array([self.D[0], self.A[1], 0.0])

        # ===== 边长缓存 =====
        self.len_top = np.linalg.norm(self.C - self.D)    # 上底
        self.len_bot = np.linalg.norm(self.B - self.A)    # 下底
        self.len_DA  = np.linalg.norm(self.A - self.D)    # 左腰
        self.len_CB  = np.linalg.norm(self.B - self.C)    # 右腰
        self.len_h   = np.linalg.norm(self.D - self.foot_D)  # 高

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-8
        # 1. 验证上下底平行（y 坐标相同）
        assert abs(self.A[1] - self.B[1]) < eps, "下底不水平"
        assert abs(self.C[1] - self.D[1]) < eps, "上底不水平"
        # 2. 上下底 y 值不同（不退化）
        assert abs(self.A[1] - self.D[1]) > 0.1, "梯形退化"
        # 3. 验证垂足在 AB 线段上
        foot_t = (self.foot_D[0] - self.A[0]) / (self.B[0] - self.A[0])
        assert 0.0 <= foot_t <= 1.0, f"垂足不在下底上: t={foot_t}"
        # 4. 验证高度计算
        h_calc = abs(self.D[1] - self.A[1])
        assert abs(h_calc - self.len_h) < eps, f"高度计算不一致: {h_calc} vs {self.len_h}"
        print("✓ 梯形几何验证通过")

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def make_author_tag(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)

    def make_main_trapezoid(self, color=COLOR_TRAPEZOID, stroke_width=3, fill=True):
        trap = Polygon(
            self.A, self.B, self.C, self.D,
            color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=0.12 if fill else 0,
        )
        return trap

    def make_parallel_arrows(self, p1, p2, color=COLOR_PARALLEL):
        """在线段中点附近画平行符号（两个小斜线标记）"""
        mid = (p1 + p2) / 2
        direction = (p2 - p1) / np.linalg.norm(p2 - p1)
        perp = np.array([-direction[1], direction[0], 0.0])
        d_off = 0.12
        marks = VGroup()
        for sign in [-1, 1]:
            center = mid + sign * d_off * direction
            tick = Line(
                center - 0.14 * perp,
                center + 0.14 * perp,
                color=color, stroke_width=2.5
            )
            marks.add(tick)
        return marks

    def make_right_angle_mark(self, corner, p1, p2, size=0.22):
        """在 corner 处（p1-corner-p2 直角）画小方块"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        sq = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=COLOR_HL, stroke_width=2.0, fill_opacity=0
        )
        return sq

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author_tag()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "什么是梯形？",
            font=FONT, font_size=42, color=COLOR_HL
        ).move_to(UP * 5.8)
        self.play(Write(hook), run_time=0.7)

        sub = Text(
            "四年级·认识梯形",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 预览梯形动画出现
        trap_preview = self.make_main_trapezoid()
        self.play(Create(trap_preview), run_time=1.2)
        self.wait(0.6)

        self.play(
            FadeOut(hook),
            FadeOut(sub),
            FadeOut(trap_preview),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2: 梯形的定义
    # ------------------------------------------------------------------

    def scene_2_definition(self):
        title = Text(
            "梯形的定义",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # -- 先展示一般四边形 --
        quad_pts = [
            np.array([-2.0, -1.0, 0.0]) + self.OFFSET,
            np.array([ 2.0, -1.0, 0.0]) + self.OFFSET,
            np.array([ 1.5,  1.8, 0.0]) + self.OFFSET,
            np.array([-0.8,  2.2, 0.0]) + self.OFFSET,
        ]
        general_quad = Polygon(*quad_pts,
                               color=GRAY_B, stroke_width=3, fill_opacity=0)
        q_label = Text(
            "一般四边形（对边不平行）",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(Create(general_quad), FadeIn(q_label), run_time=0.8)
        self.wait(0.5)

        # -- 变换成梯形 --
        trap_main = self.make_main_trapezoid()
        trap_label = Text(
            "梯形（一组对边平行）",
            font=FONT, font_size=22, color=COLOR_TRAPEZOID
        ).move_to(DOWN * 3.5)

        self.play(
            Transform(general_quad, trap_main),
            Transform(q_label, trap_label),
            run_time=1.0
        )
        self.wait(0.3)

        # -- 高亮上底、下底平行关系 --
        top_base = Line(self.D, self.C, color=COLOR_TOP_BASE, stroke_width=5)
        bot_base = Line(self.A, self.B, color=COLOR_BOT_BASE, stroke_width=5)
        self.play(Create(top_base), Create(bot_base), run_time=0.6)

        # 平行符号
        par_marks_top = self.make_parallel_arrows(self.D, self.C)
        par_marks_bot = self.make_parallel_arrows(self.A, self.B)
        self.play(FadeIn(par_marks_top), FadeIn(par_marks_bot), run_time=0.4)

        par_text = Text(
            "上底 ∥ 下底",
            font=FONT, font_size=26, color=COLOR_PARALLEL
        ).move_to(DOWN * 4.6)
        self.play(FadeIn(par_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # -- 高亮腰（不平行）--
        leg_L = Line(self.D, self.A, color=COLOR_LEG, stroke_width=5)
        leg_R = Line(self.C, self.B, color=COLOR_LEG, stroke_width=5)
        self.play(Create(leg_L), Create(leg_R), run_time=0.5)

        leg_text = Text(
            "两腰不平行",
            font=FONT, font_size=26, color=COLOR_LEG
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(leg_text, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # -- 核心定义文字 --
        defn_line1 = Text(
            "只有一组对边平行的四边形",
            font=FONT, font_size=24, color=WHITE
        )
        defn_line2 = Text(
            "叫做  梯形",
            font=FONT, font_size=24, color=COLOR_HL
        )
        defn_box = VGroup(defn_line1, defn_line2).arrange(DOWN, buff=0.25).move_to(DOWN * 2.8)

        self.play(FadeIn(defn_box, shift=UP * 0.3), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(general_quad),
            FadeOut(q_label),
            FadeOut(top_base),
            FadeOut(bot_base),
            FadeOut(par_marks_top),
            FadeOut(par_marks_bot),
            FadeOut(par_text),
            FadeOut(leg_L),
            FadeOut(leg_R),
            FadeOut(leg_text),
            FadeOut(defn_box),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 3: 各部分名称
    # ------------------------------------------------------------------

    def scene_3_parts(self):
        title = Text(
            "梯形各部分名称",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 梯形主体
        trap = self.make_main_trapezoid()
        self.play(Create(trap), run_time=0.8)

        # 顶点标注
        dot_A = Dot(self.A, color=WHITE, radius=0.08)
        dot_B = Dot(self.B, color=WHITE, radius=0.08)
        dot_C = Dot(self.C, color=WHITE, radius=0.08)
        dot_D = Dot(self.D, color=WHITE, radius=0.08)

        lbl_A = Text("A", font=FONT, font_size=22, color=WHITE).next_to(dot_A, DL, buff=0.08)
        lbl_B = Text("B", font=FONT, font_size=22, color=WHITE).next_to(dot_B, DR, buff=0.08)
        lbl_C = Text("C", font=FONT, font_size=22, color=WHITE).next_to(dot_C, UR, buff=0.08)
        lbl_D = Text("D", font=FONT, font_size=22, color=WHITE).next_to(dot_D, UL, buff=0.08)

        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C), FadeIn(dot_D),
            FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), FadeIn(lbl_D),
            run_time=0.5
        )

        # 上底
        top_hl = Line(self.D, self.C, color=COLOR_TOP_BASE, stroke_width=6)
        self.play(Create(top_hl), run_time=0.5)

        brace_top = Brace(top_hl, direction=UP, buff=0.1, color=COLOR_TOP_BASE)
        brace_top_lbl = Text(
            "上底（较短的平行边）",
            font=FONT, font_size=20, color=COLOR_TOP_BASE
        ).next_to(brace_top, UP, buff=0.1)
        self.play(FadeIn(brace_top), FadeIn(brace_top_lbl), run_time=0.5)
        self.wait(0.8)

        # 下底
        bot_hl = Line(self.A, self.B, color=COLOR_BOT_BASE, stroke_width=6)
        self.play(Create(bot_hl), run_time=0.5)

        brace_bot = Brace(bot_hl, direction=DOWN, buff=0.1, color=COLOR_BOT_BASE)
        brace_bot_lbl = Text(
            "下底（较长的平行边）",
            font=FONT, font_size=20, color=COLOR_BOT_BASE
        ).next_to(brace_bot, DOWN, buff=0.1)
        self.play(FadeIn(brace_bot), FadeIn(brace_bot_lbl), run_time=0.5)
        self.wait(0.8)

        # 两腰
        leg_L_hl = Line(self.D, self.A, color=COLOR_LEG, stroke_width=6)
        leg_R_hl = Line(self.C, self.B, color=COLOR_LEG, stroke_width=6)
        self.play(Create(leg_L_hl), Create(leg_R_hl), run_time=0.5)

        leg_lbl_L = Text("腰", font=FONT, font_size=22, color=COLOR_LEG
                         ).next_to(leg_L_hl, LEFT, buff=0.15)
        leg_lbl_R = Text("腰", font=FONT, font_size=22, color=COLOR_LEG
                         ).next_to(leg_R_hl, RIGHT, buff=0.15)
        self.play(FadeIn(leg_lbl_L), FadeIn(leg_lbl_R), run_time=0.4)

        waist_note = Text(
            "不平行的两条边叫做腰",
            font=FONT, font_size=22, color=COLOR_LEG
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(waist_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(trap),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C), FadeOut(dot_D),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C), FadeOut(lbl_D),
            FadeOut(top_hl), FadeOut(brace_top), FadeOut(brace_top_lbl),
            FadeOut(bot_hl), FadeOut(brace_bot), FadeOut(brace_bot_lbl),
            FadeOut(leg_L_hl), FadeOut(leg_R_hl),
            FadeOut(leg_lbl_L), FadeOut(leg_lbl_R),
            FadeOut(waist_note),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 4: 梯形的高
    # ------------------------------------------------------------------

    def scene_4_height(self):
        title = Text(
            "梯形的高",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        trap = self.make_main_trapezoid()
        self.play(Create(trap), run_time=0.8)

        # 顶点 D 点
        dot_D = Dot(self.D, color=COLOR_HEIGHT, radius=0.1)
        lbl_D = Text("D", font=FONT, font_size=22, color=WHITE).next_to(dot_D, UL, buff=0.08)
        self.play(FadeIn(dot_D), FadeIn(lbl_D), run_time=0.4)

        # 提示：从 D 点向下底引垂线
        note1 = Text(
            "从上底 D 点向下底引垂线",
            font=FONT, font_size=22, color=COLOR_HEIGHT
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(note1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 绘制垂线（高）
        height_line = DashedLine(
            self.D,
            self.foot_D,
            color=COLOR_HEIGHT,
            stroke_width=4,
            dash_length=0.12
        )
        self.play(Create(height_line), run_time=0.8)

        # 垂足点
        dot_foot = Dot(self.foot_D, color=COLOR_HEIGHT, radius=0.1)
        lbl_foot = Text("E", font=FONT, font_size=22, color=WHITE
                        ).next_to(dot_foot, DOWN, buff=0.1)
        self.play(FadeIn(dot_foot), FadeIn(lbl_foot), run_time=0.4)

        # 直角标记
        right_mark = self.make_right_angle_mark(self.foot_D, self.D, self.B, size=0.22)
        self.play(Create(right_mark), run_time=0.4)

        # Brace 标注高
        h_line_for_brace = Line(self.D, self.foot_D)
        brace_h = Brace(h_line_for_brace, direction=RIGHT, buff=0.12, color=COLOR_HEIGHT)
        brace_h_lbl = Text("高", font=FONT, font_size=24, color=COLOR_HEIGHT
                           ).next_to(brace_h, RIGHT, buff=0.1)
        self.play(FadeIn(brace_h), FadeIn(brace_h_lbl), run_time=0.5)

        # 说明文字
        note2 = Text(
            "D 到垂足 E 的距离就是梯形的高",
            font=FONT, font_size=22, color=COLOR_HEIGHT
        ).move_to(DOWN * 4.8)
        self.play(FadeOut(note1), FadeIn(note2, shift=UP * 0.2), run_time=0.5)

        # 强调：高垂直于底
        note3 = Text(
            "高 ⊥ 底",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(note3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(trap),
            FadeOut(dot_D), FadeOut(lbl_D),
            FadeOut(height_line),
            FadeOut(dot_foot), FadeOut(lbl_foot),
            FadeOut(right_mark),
            FadeOut(brace_h), FadeOut(brace_h_lbl),
            FadeOut(note2),
            FadeOut(note3),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 5: 特殊梯形
    # ------------------------------------------------------------------

    def scene_5_special(self):
        title = Text(
            "特殊的梯形",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # ---- 直角梯形（上半屏）----
        rA = np.array([-3.2, 2.5, 0.0])
        rB = np.array([ 1.2, 2.5, 0.0])
        rC = np.array([ 0.2, 4.5, 0.0])
        rD = np.array([-3.2, 4.5, 0.0])

        right_trap = Polygon(rA, rB, rC, rD,
                             color=COLOR_TRAPEZOID, stroke_width=3,
                             fill_color=COLOR_TRAPEZOID, fill_opacity=0.12)

        rt_title = Text(
            "直角梯形",
            font=FONT, font_size=26, color=COLOR_TRAPEZOID
        ).move_to(UP * 5.3)

        # 直角标记（rD 处）
        v1 = rA - rD
        v1_u = v1 / np.linalg.norm(v1) * 0.22
        v2 = rC - rD
        v2_u = v2 / np.linalg.norm(v2) * 0.22
        rt_mark = Polygon(
            rD, rD + v1_u, rD + v1_u + v2_u, rD + v2_u,
            color=COLOR_HL, stroke_width=2, fill_opacity=0
        )

        rt_note = Text(
            "有一个直角的梯形",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 3.8)

        self.play(FadeIn(rt_title), Create(right_trap), run_time=0.8)
        self.play(Create(rt_mark), FadeIn(rt_note), run_time=0.5)
        self.wait(0.8)

        # ---- 等腰梯形（下半屏）----
        iA = np.array([-2.2, 0.2, 0.0])
        iB = np.array([ 2.2, 0.2, 0.0])
        iC = np.array([ 1.2, 2.2, 0.0])
        iD = np.array([-1.2, 2.2, 0.0])

        iso_trap = Polygon(iA, iB, iC, iD,
                           color=COLOR_LEG, stroke_width=3,
                           fill_color=COLOR_LEG, fill_opacity=0.12)

        iso_title = Text(
            "等腰梯形",
            font=FONT, font_size=26, color=COLOR_LEG
        ).move_to(UP * 2.8)

        # 等腰标记（两腰各画两条短横线）
        def make_tick_on_segment(p1, p2, n=2, color=COLOR_HL, size=0.16):
            mid = (p1 + p2) / 2
            d = (p2 - p1) / np.linalg.norm(p2 - p1)
            perp = np.array([-d[1], d[0], 0.0])
            ticks = VGroup()
            offsets = np.linspace(-0.08 * (n - 1), 0.08 * (n - 1), n)
            for off in offsets:
                c = mid + off * d
                ticks.add(Line(c - size * perp, c + size * perp,
                               color=color, stroke_width=2.5))
            return ticks

        tick_L = make_tick_on_segment(iD, iA, n=2)
        tick_R = make_tick_on_segment(iC, iB, n=2)

        iso_note = Text(
            "两腰相等的梯形",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 1.2)

        self.play(FadeIn(iso_title), Create(iso_trap), run_time=0.8)
        self.play(Create(tick_L), Create(tick_R), FadeIn(iso_note), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rt_title), FadeOut(right_trap), FadeOut(rt_mark), FadeOut(rt_note),
            FadeOut(iso_title), FadeOut(iso_trap), FadeOut(tick_L), FadeOut(tick_R),
            FadeOut(iso_note),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 6: 综合总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text(
            "梯形知识总结",
            font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 6.8)
        self.play(Write(title), run_time=0.6)

        # 梯形示意图（略小，放在上方）
        scale = 0.72
        offset_sum = np.array([0.0, 3.5, 0.0])

        sA = self.A_raw * scale + offset_sum
        sB = self.B_raw * scale + offset_sum
        sC = self.C_raw * scale + offset_sum
        sD = self.D_raw * scale + offset_sum

        trap_s = Polygon(sA, sB, sC, sD,
                         color=COLOR_TRAPEZOID, stroke_width=3,
                         fill_color=COLOR_TRAPEZOID, fill_opacity=0.15)
        self.play(Create(trap_s), run_time=0.7)

        # 标注各部分
        top_s = Line(sD, sC, color=COLOR_TOP_BASE, stroke_width=5)
        top_lbl_s = Text("上底", font=FONT, font_size=18, color=COLOR_TOP_BASE
                         ).next_to(top_s, UP, buff=0.1)
        bot_s = Line(sA, sB, color=COLOR_BOT_BASE, stroke_width=5)
        bot_lbl_s = Text("下底", font=FONT, font_size=18, color=COLOR_BOT_BASE
                         ).next_to(bot_s, DOWN, buff=0.08)
        leg_Ls = Line(sD, sA, color=COLOR_LEG, stroke_width=4)
        leg_Rs = Line(sC, sB, color=COLOR_LEG, stroke_width=4)
        leg_Ls_lbl = Text("腰", font=FONT, font_size=18, color=COLOR_LEG
                          ).next_to(leg_Ls, LEFT, buff=0.1)
        leg_Rs_lbl = Text("腰", font=FONT, font_size=18, color=COLOR_LEG
                          ).next_to(leg_Rs, RIGHT, buff=0.1)

        # 高的垂足（相对于缩放后的梯形）
        foot_s = np.array([sD[0], sA[1], 0.0])
        h_line_s = DashedLine(sD, foot_s, color=COLOR_HEIGHT, stroke_width=3, dash_length=0.1)
        h_lbl_s = Text("高", font=FONT, font_size=18, color=COLOR_HEIGHT
                       ).next_to(h_line_s, RIGHT, buff=0.1)

        v1s = sA - foot_s
        if np.linalg.norm(v1s) > 1e-8:
            v1s_u = v1s / np.linalg.norm(v1s) * 0.16
        else:
            v1s_u = np.array([0.16, 0.0, 0.0])
        v2s = sD - foot_s
        if np.linalg.norm(v2s) > 1e-8:
            v2s_u = v2s / np.linalg.norm(v2s) * 0.16
        else:
            v2s_u = np.array([0.0, 0.16, 0.0])
        rm_s = Polygon(foot_s, foot_s + v1s_u, foot_s + v1s_u + v2s_u, foot_s + v2s_u,
                       color=COLOR_HL, stroke_width=1.8, fill_opacity=0)

        self.play(
            Create(top_s), FadeIn(top_lbl_s),
            Create(bot_s), FadeIn(bot_lbl_s),
            Create(leg_Ls), FadeIn(leg_Ls_lbl),
            Create(leg_Rs), FadeIn(leg_Rs_lbl),
            Create(h_line_s), FadeIn(h_lbl_s),
            Create(rm_s),
            run_time=1.0
        )

        # 平行符号
        par_t = self.make_parallel_arrows(sD, sC, color=COLOR_PARALLEL)
        par_b = self.make_parallel_arrows(sA, sB, color=COLOR_PARALLEL)
        self.play(FadeIn(par_t), FadeIn(par_b), run_time=0.4)
        self.wait(0.5)

        # 关键要点列表
        pts_y_start = 1.0
        pts_spacing = 1.1

        pt1_a = Text("定义：", font=FONT, font_size=22, color=COLOR_HL)
        pt1_b = Text("只有一组对边平行的四边形", font=FONT, font_size=22, color=WHITE)
        pt1 = VGroup(pt1_a, pt1_b).arrange(RIGHT, buff=0.1).move_to(
            np.array([0.0, pts_y_start, 0.0]))

        pt2_a = Text("平行：", font=FONT, font_size=22, color=COLOR_PARALLEL)
        pt2_b = Text("上底 ∥ 下底", font=FONT, font_size=22, color=WHITE)
        pt2 = VGroup(pt2_a, pt2_b).arrange(RIGHT, buff=0.1).move_to(
            np.array([0.0, pts_y_start - pts_spacing, 0.0]))

        pt3_a = Text("腰：", font=FONT, font_size=22, color=COLOR_LEG)
        pt3_b = Text("不平行的两条边", font=FONT, font_size=22, color=WHITE)
        pt3 = VGroup(pt3_a, pt3_b).arrange(RIGHT, buff=0.1).move_to(
            np.array([0.0, pts_y_start - 2 * pts_spacing, 0.0]))

        pt4_a = Text("高：", font=FONT, font_size=22, color=COLOR_HEIGHT)
        pt4_b = Text("上底到下底的垂直距离", font=FONT, font_size=22, color=WHITE)
        pt4 = VGroup(pt4_a, pt4_b).arrange(RIGHT, buff=0.1).move_to(
            np.array([0.0, pts_y_start - 3 * pts_spacing, 0.0]))

        pt5_a = Text("特殊：", font=FONT, font_size=22, color=COLOR_HL)
        pt5_b = Text("直角梯形、等腰梯形", font=FONT, font_size=22, color=GRAY_A)
        pt5 = VGroup(pt5_a, pt5_b).arrange(RIGHT, buff=0.1).move_to(
            np.array([0.0, pts_y_start - 4 * pts_spacing, 0.0]))

        for pt in [pt1, pt2, pt3, pt4, pt5]:
            self.play(FadeIn(pt, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.2)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(trap_s),
            FadeOut(top_s), FadeOut(top_lbl_s),
            FadeOut(bot_s), FadeOut(bot_lbl_s),
            FadeOut(leg_Ls), FadeOut(leg_Ls_lbl),
            FadeOut(leg_Rs), FadeOut(leg_Rs_lbl),
            FadeOut(h_line_s), FadeOut(h_lbl_s),
            FadeOut(rm_s),
            FadeOut(par_t), FadeOut(par_b),
            FadeOut(pt1), FadeOut(pt2), FadeOut(pt3),
            FadeOut(pt4), FadeOut(pt5),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰：小梯形图案
        def tiny_trap(cx, cy, scale=0.3, col=GOLD):
            a = np.array([-1.0, -0.5, 0.0]) * scale + np.array([cx, cy, 0.0])
            b = np.array([ 1.0, -0.5, 0.0]) * scale + np.array([cx, cy, 0.0])
            c = np.array([ 0.55,  0.5, 0.0]) * scale + np.array([cx, cy, 0.0])
            d = np.array([-0.55,  0.5, 0.0]) * scale + np.array([cx, cy, 0.0])
            return Polygon(a, b, c, d, color=col,
                           fill_color=col, fill_opacity=0.7,
                           stroke_width=1.5)

        traps_deco = VGroup(*[
            tiny_trap(cx, cy)
            for cx, cy in [(-3.0, -2.5), (-1.5, -3.2), (0.0, -2.5),
                           (1.5, -3.2), (3.0, -2.5)]
        ])
        self.play(*[FadeIn(t, scale=0.5) for t in traps_deco], run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(traps_deco),
            run_time=0.8
        )


# 运行命令:
# manim -qm 004_梯形.py TrapezoidLesson
