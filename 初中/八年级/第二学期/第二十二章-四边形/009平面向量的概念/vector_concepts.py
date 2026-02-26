"""
平面向量的概念
Plane Vector Concepts - Manim Animation

年级: 八年级第二学期
章节: 第二十二章 四边形（向量基础）
内容: 向量定义、表示、模、相等/相反/零向量

TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 — TikTok竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PlaneVectorConcepts(Scene):
    """
    平面向量的概念教学动画
    场景顺序：
      1. 开场 Hook
      2. 向量的定义
      3. 向量的表示方法
      4. 向量的模
      5. 相等向量 vs 相反向量
      6. 零向量
      7. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 颜色配置 ──────────────────────────────────────
        self.C_TITLE    = YELLOW
        self.C_MAIN     = "#00CED1"   # 主向量 青色
        self.C_RED      = "#FF6B6B"   # 对比 红色
        self.C_GREEN    = "#2ECC71"   # 第三 绿色
        self.C_EQUAL    = "#FFD700"   # 相等 金色
        self.C_OPPOSITE = "#FF4500"   # 相反 橙红
        self.C_MODULE   = "#DA70D6"   # 模   紫色
        self.C_CARD_BG  = "#16213e"   # 卡片背景

        # ── 初始化几何数据 ────────────────────────────────
        self.setup_geometry()

        # ── 场景执行 ──────────────────────────────────────
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_notation()
        self.scene_4_modulus()
        self.scene_5_equal_opposite()
        self.scene_6_zero_vector()
        self.scene_7_summary()

    # =========================================================
    # § 几何初始化
    # =========================================================
    def setup_geometry(self):
        """精确计算所有向量坐标，统一管理"""

        # ── 主向量 (Scene 2/3/4) ──────────────────────────
        # 斜向右上，清晰展示方向+长度
        self.VA_START = np.array([-2.5, -0.5, 0])
        self.VA_END   = np.array([ 1.5,  2.0, 0])
        self.VA_VEC   = self.VA_END - self.VA_START        # 方向向量
        self.VA_LEN   = float(np.linalg.norm(self.VA_VEC))  # 模长

        # ── Scene 3 向量 b（水平向右，用 \vec{a} 表示）────
        self.VB_START = np.array([-2.0, -1.5, 0])
        self.VB_END   = np.array([ 1.0, -1.5, 0])
        self.VB_VEC   = self.VB_END - self.VB_START
        self.VB_LEN   = float(np.linalg.norm(self.VB_VEC))

        # ── 相等向量组 (Scene 5) — 4条平行等长 ───────────
        # 基础方向向量（统一）
        self.EQ_DIR = np.array([2.0, 1.2, 0])
        self.EQ_LEN = float(np.linalg.norm(self.EQ_DIR))

        # 4条起点（错落分布在画面中）
        self.EQ_STARTS = [
            np.array([-3.2,  0.5, 0]),
            np.array([-1.0,  1.5, 0]),
            np.array([-2.5, -1.5, 0]),
            np.array([ 0.5, -0.8, 0]),
        ]
        self.EQ_ENDS = [s + self.EQ_DIR for s in self.EQ_STARTS]

        # ── 相反向量组 (Scene 5) — 2条反向等长 ───────────
        self.OPP_DIR_POS = np.array([2.5, 0.0, 0])   # 正向
        self.OPP_DIR_NEG = -self.OPP_DIR_POS           # 反向

        self.OPP_A_START = np.array([-2.8, 0.0, 0])
        self.OPP_A_END   = self.OPP_A_START + self.OPP_DIR_POS

        self.OPP_B_START = np.array([ 2.8, 0.0, 0])
        self.OPP_B_END   = self.OPP_B_START + self.OPP_DIR_NEG

        # ── 验证 ──────────────────────────────────────────
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何计算"""
        eps = 1e-10

        # 相等向量：方向和长度一致
        for i, (s, e) in enumerate(zip(self.EQ_STARTS, self.EQ_ENDS)):
            vec = e - s
            assert abs(np.linalg.norm(vec) - self.EQ_LEN) < eps, f"相等向量{i}长度不一致"
            cos_angle = np.dot(vec[:2], self.EQ_DIR[:2]) / (np.linalg.norm(vec[:2]) * np.linalg.norm(self.EQ_DIR[:2]))
            assert abs(cos_angle - 1.0) < eps, f"相等向量{i}方向不一致"

        # 相反向量：长度相等，方向相反
        len_a = np.linalg.norm(self.OPP_DIR_POS)
        len_b = np.linalg.norm(self.OPP_DIR_NEG)
        assert abs(len_a - len_b) < eps, "相反向量长度不一致"
        dot = np.dot(self.OPP_DIR_POS[:2], self.OPP_DIR_NEG[:2])
        assert dot < -1e-6, "相反向量方向应相反（点积<0）"

        # 边界检查：所有端点在 x∈[-4,4], y∈[-7,7]
        all_points = (
            [self.VA_START, self.VA_END,
             self.VB_START, self.VB_END,
             self.OPP_A_START, self.OPP_A_END,
             self.OPP_B_START, self.OPP_B_END]
            + self.EQ_STARTS + self.EQ_ENDS
        )
        for p in all_points:
            assert abs(p[0]) <= 4.0, f"点 {p} x超界"
            assert abs(p[1]) <= 7.0, f"点 {p} y超界"

        print(f"✓ 几何验证通过")
        print(f"  主向量 |VA| = {self.VA_LEN:.4f}")
        print(f"  相等向量 |EQ| = {self.EQ_LEN:.4f}")
        print(f"  相反向量 |OPP| = {float(np.linalg.norm(self.OPP_DIR_POS)):.4f}")

    # =========================================================
    # § 工具方法
    # =========================================================
    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 6.8)

    def make_scene_title(self, text, color=None, y=6.0):
        color = color or self.C_TITLE
        return Text(
            text,
            font="Noto Sans CJK SC",
            font_size=38,
            color=color,
        ).move_to(UP * y)

    def make_card(self, w, h, pos, border_color, fill="#16213e"):
        return RoundedRectangle(
            width=w, height=h,
            corner_radius=0.28,
            fill_color=fill,
            fill_opacity=0.92,
            stroke_color=border_color,
            stroke_width=2,
        ).move_to(pos)

    def make_arrow(self, start, end, color, stroke=5, tip=0.22):
        return Arrow(
            start, end,
            color=color,
            stroke_width=stroke,
            max_tip_length_to_length_ratio=tip,
            buff=0,
        )

    # =========================================================
    # § Scene 1: 开场 Hook
    # =========================================================
    def scene_1_opening(self):
        self.author_info = self.make_author()
        self.play(FadeIn(self.author_info, shift=DOWN * 0.15), run_time=0.3)

        # ── 主问句 ────────────────────────────────────────
        hook = Text(
            "什么是向量？",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.C_TITLE,
        ).move_to(UP * 5.2)
        self.play(Write(hook), run_time=0.7)

        # ── 6条方向各异的箭头（射线式汇聚）────────────────
        # 从圆周各方向指向中心附近，角度精确计算
        angles_deg = [0, 60, 120, 180, 240, 300]
        radius = 3.0
        center = np.array([0, 1.5, 0])

        arrows_hook = VGroup()
        for deg in angles_deg:
            theta = np.radians(deg)
            direction = np.array([np.cos(theta), np.sin(theta), 0])
            start = center + radius * direction
            end   = center + 0.6 * direction
            color = [self.C_MAIN, self.C_RED, self.C_GREEN,
                     self.C_EQUAL, self.C_OPPOSITE, self.C_MODULE][angles_deg.index(deg)]
            arr = self.make_arrow(start, end, color, stroke=4, tip=0.28)
            arrows_hook.add(arr)

        self.play(
            LaggedStart(
                *[GrowArrow(a) for a in arrows_hook],
                lag_ratio=0.12,
            ),
            run_time=1.2,
        )
        self.play(
            LaggedStart(
                *[Flash(a.get_end(), color=a.get_color(), flash_radius=0.25)
                  for a in arrows_hook],
                lag_ratio=0.08,
            ),
            run_time=0.6,
        )
        self.wait(0.5)

        self.play(
            FadeOut(hook),
            FadeOut(arrows_hook),
            run_time=0.45,
        )

    # =========================================================
    # § Scene 2: 向量的定义
    # =========================================================
    def scene_2_definition(self):
        title = self.make_scene_title("向量的定义", color=self.C_MAIN, y=6.0)
        self.play(FadeIn(title), run_time=0.4)

        # ── 主向量箭头 ───────────────────────────────────
        main_arrow = self.make_arrow(
            self.VA_START, self.VA_END, self.C_MAIN, stroke=6,
        )
        self.play(GrowArrow(main_arrow), run_time=0.9)

        # ── 端点 ─────────────────────────────────────────
        dot_start = Dot(self.VA_START, radius=0.1, color=WHITE)
        dot_end   = Dot(self.VA_END,   radius=0.1, color=WHITE)
        self.play(FadeIn(dot_start), FadeIn(dot_end), run_time=0.3)

        # ── 方向标注 — 弧线箭头 + "方向"文字 ─────────────
        # 在箭头终点附近标注方向
        direction_label = Text(
            "方  向",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_TITLE,
        ).move_to(self.VA_END + RIGHT * 1.2 + UP * 0.3)

        direction_arrow = Arrow(
            direction_label.get_left() + LEFT * 0.15,
            self.VA_END + UP * 0.18,
            color=self.C_TITLE,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3,
            buff=0.05,
        )

        self.play(FadeIn(direction_label), GrowArrow(direction_arrow), run_time=0.6)

        # ── 大小标注 — Brace ─────────────────────────────
        # 沿向量方向创建 Brace（用Line做底边投影到画面）
        mid_point = (self.VA_START + self.VA_END) / 2
        size_label = Text(
            "大  小",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_MODULE,
        ).move_to(mid_point + LEFT * 1.4 + DOWN * 0.4)

        size_arrow = Arrow(
            size_label.get_right() + RIGHT * 0.1,
            mid_point + LEFT * 0.3,
            color=self.C_MODULE,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.3,
            buff=0.05,
        )

        # 向量长度的虚线覆盖
        vec_underline = DashedLine(
            self.VA_START, self.VA_END,
            color=self.C_MODULE,
            stroke_width=3,
            dash_length=0.12,
        )
        self.play(
            Create(vec_underline),
            FadeIn(size_label),
            GrowArrow(size_arrow),
            run_time=0.7,
        )

        # ── 定义卡片 ─────────────────────────────────────
        def_card = self.make_card(7.8, 2.2, DOWN * 2.5, self.C_MAIN)

        def_line1 = Text(
            "向量：既有大小，又有方向的量",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
        ).move_to(DOWN * 2.1)

        def_line2 = Text(
            "用有向线段来表示",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(def_card), run_time=0.3)
        self.play(FadeIn(def_line1, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(def_line2, shift=UP * 0.2), run_time=0.4)

        # ── 对比卡片：标量 vs 向量 ─────────────────────────
        cmp_card = self.make_card(7.8, 2.4, DOWN * 5.0, GRAY_B, "#0d0d1a")
        cmp_title = Text(
            "对比",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B,
        ).move_to(DOWN * 4.1)

        scalar_text = Text(
            "标量（如温度）：只有大小",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
        ).move_to(DOWN * 4.7)

        vector_text = Text(
            "向量（如速度）：大小 + 方向",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_MAIN,
        ).move_to(DOWN * 5.4)

        self.play(FadeIn(cmp_card), FadeIn(cmp_title), run_time=0.3)
        self.play(FadeIn(scalar_text), run_time=0.4)
        self.play(FadeIn(vector_text), run_time=0.4)
        self.wait(1.5)

        # ── 清场 ─────────────────────────────────────────
        self.play(
            FadeOut(title),
            FadeOut(main_arrow),
            FadeOut(dot_start),
            FadeOut(dot_end),
            FadeOut(direction_label),
            FadeOut(direction_arrow),
            FadeOut(size_label),
            FadeOut(size_arrow),
            FadeOut(vec_underline),
            FadeOut(def_card),
            FadeOut(def_line1),
            FadeOut(def_line2),
            FadeOut(cmp_card),
            FadeOut(cmp_title),
            FadeOut(scalar_text),
            FadeOut(vector_text),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 3: 向量的表示方法
    # =========================================================
    def scene_3_notation(self):
        title = self.make_scene_title("向量的表示方法", color="#FF6B6B", y=6.0)
        self.play(FadeIn(title), run_time=0.4)

        # ── 方法一：\overrightarrow{AB} ──────────────────
        label_m1 = Text(
            "方法一：用端点字母",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_TITLE,
        ).move_to(UP * 5.0)
        self.play(FadeIn(label_m1), run_time=0.35)

        # 点A和点B + 箭头
        A_pos = np.array([-2.5, 3.0, 0])
        B_pos = np.array([ 1.5, 4.0, 0])

        dot_A = Dot(A_pos, radius=0.12, color=self.C_MAIN)
        dot_B = Dot(B_pos, radius=0.12, color=self.C_MAIN)
        lbl_A = Text("A", font="Noto Sans CJK SC", font_size=28,
                     color=self.C_MAIN).next_to(dot_A, DL, buff=0.12)
        lbl_B = Text("B", font="Noto Sans CJK SC", font_size=28,
                     color=self.C_MAIN).next_to(dot_B, UR, buff=0.12)
        arrow_AB = self.make_arrow(A_pos, B_pos, self.C_MAIN, stroke=5)

        self.play(FadeIn(dot_A), FadeIn(lbl_A), run_time=0.3)
        self.play(FadeIn(dot_B), FadeIn(lbl_B), run_time=0.3)
        self.play(GrowArrow(arrow_AB), run_time=0.7)

        # 符号
        sym_AB = MathTex(
            r"\overrightarrow{AB}",
            font_size=52,
            color=self.C_MAIN,
        ).move_to(UP * 1.8)

        box_AB = SurroundingRectangle(sym_AB, color=self.C_MAIN,
                                      buff=0.2, corner_radius=0.1)
        self.play(Write(sym_AB), run_time=0.7)
        self.play(Create(box_AB), run_time=0.3)
        self.wait(0.4)

        # ── 方法二：\vec{a} ───────────────────────────────
        label_m2 = Text(
            "方法二：用小写字母",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_TITLE,
        ).move_to(UP * 0.8)
        self.play(FadeIn(label_m2), run_time=0.35)

        # 第二条向量（水平）
        arrow_a = self.make_arrow(
            self.VB_START, self.VB_END, self.C_GREEN, stroke=5
        )
        self.play(GrowArrow(arrow_a), run_time=0.6)

        sym_a = MathTex(
            r"\vec{a}",
            font_size=52,
            color=self.C_GREEN,
        ).move_to(DOWN * 0.5)
        box_a = SurroundingRectangle(sym_a, color=self.C_GREEN,
                                     buff=0.2, corner_radius=0.1)
        self.play(Write(sym_a), run_time=0.6)
        self.play(Create(box_a), run_time=0.3)

        # ── 提示：起点不同，向量可以相同 ─────────────────
        note_card = self.make_card(7.8, 1.5, DOWN * 2.4, GRAY_B, "#0d0d1a")
        note_text = Text(
            "向量只关注：大小 + 方向",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(DOWN * 2.2)
        note_text2 = Text(
            "起点位置不影响向量本身！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B,
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(note_card), run_time=0.3)
        self.play(FadeIn(note_text), FadeIn(note_text2), run_time=0.5)
        self.wait(1.5)

        # ── 清场 ─────────────────────────────────────────
        self.play(
            FadeOut(title), FadeOut(label_m1),
            FadeOut(dot_A), FadeOut(dot_B),
            FadeOut(lbl_A), FadeOut(lbl_B),
            FadeOut(arrow_AB), FadeOut(sym_AB), FadeOut(box_AB),
            FadeOut(label_m2), FadeOut(arrow_a),
            FadeOut(sym_a), FadeOut(box_a),
            FadeOut(note_card), FadeOut(note_text), FadeOut(note_text2),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 4: 向量的模
    # =========================================================
    def scene_4_modulus(self):
        title = self.make_scene_title("向量的模（大小）", color=self.C_MODULE, y=6.0)
        self.play(FadeIn(title), run_time=0.4)

        # ── 向量箭头（竖屏中部）─────────────────────────
        mod_start = np.array([-2.5, 2.5, 0])
        mod_end   = np.array([ 2.0, 4.0, 0])
        mod_vec   = mod_end - mod_start
        mod_len   = float(np.linalg.norm(mod_vec))

        arrow_mod = self.make_arrow(mod_start, mod_end, self.C_MODULE, stroke=6)
        dot_s = Dot(mod_start, radius=0.11, color=WHITE)
        dot_e = Dot(mod_end, radius=0.11, color=WHITE)
        lbl_P = Text("P", font="Noto Sans CJK SC", font_size=26,
                     color=WHITE).next_to(dot_s, DL, buff=0.1)
        lbl_Q = Text("Q", font="Noto Sans CJK SC", font_size=26,
                     color=WHITE).next_to(dot_e, UR, buff=0.1)

        self.play(GrowArrow(arrow_mod), run_time=0.8)
        self.play(FadeIn(dot_s), FadeIn(dot_e), run_time=0.3)
        self.play(FadeIn(lbl_P), FadeIn(lbl_Q), run_time=0.3)

        # ── 长度 Brace（沿向量方向）─────────────────────
        # 计算向量方向的垂直偏移，将Brace放在向量下方
        perp_unit = np.array([-mod_vec[1], mod_vec[0], 0])
        perp_unit /= np.linalg.norm(perp_unit)
        offset = -perp_unit * 0.35

        brace_line = Line(
            mod_start + offset,
            mod_end + offset,
            color=self.C_MODULE,
            stroke_width=2,
        )
        brace_tick_s = Line(
            mod_start + offset * 0.5,
            mod_start + offset * 1.5,
            color=self.C_MODULE, stroke_width=2
        )
        brace_tick_e = Line(
            mod_end + offset * 0.5,
            mod_end + offset * 1.5,
            color=self.C_MODULE, stroke_width=2
        )
        brace_group = VGroup(brace_line, brace_tick_s, brace_tick_e)

        mid_mod = (mod_start + mod_end) / 2 + offset * 2.5
        len_label = MathTex(
            r"|\overrightarrow{PQ}|",
            font_size=38,
            color=self.C_MODULE,
        ).move_to(mid_mod + DOWN * 0.4)

        self.play(Create(brace_group), run_time=0.5)
        self.play(Write(len_label), run_time=0.6)

        # ── 公式卡片 ─────────────────────────────────────
        formula_card = self.make_card(7.8, 2.8, UP * 0.3, self.C_MODULE)

        # 用两部分拼接：MathTex + Text（避免 MathTex 含中文）
        part1 = MathTex(
            r"|\overrightarrow{PQ}| \;=",
            font_size=38,
            color=self.C_MODULE,
        )
        part2 = Text(
            "向量的长度",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE,
        )
        formula_row = VGroup(part1, part2).arrange(RIGHT, buff=0.25).move_to(UP * 0.7)

        also_label = VGroup(
            Text("也写作", font="Noto Sans CJK SC", font_size=28, color=GRAY_A),
            MathTex(r"|\vec{a}|", font_size=38, color=self.C_MODULE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.0)

        self.play(FadeIn(formula_card), run_time=0.3)
        self.play(FadeIn(formula_row), run_time=0.5)
        self.play(FadeIn(also_label), run_time=0.4)

        # ── 特殊说明：|a| ≥ 0 ────────────────────────────
        nonneg_card = self.make_card(7.5, 1.4, DOWN * 1.3, GRAY_B, "#0d0d1a")
        nonneg_row = VGroup(
            Text("模的性质：", font="Noto Sans CJK SC",
                 font_size=24, color=GRAY_A),
            MathTex(r"|\vec{a}| \geq 0", font_size=36, color=self.C_MODULE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.3)

        self.play(FadeIn(nonneg_card), FadeIn(nonneg_row), run_time=0.5)
        self.wait(1.8)

        # ── 清场 ─────────────────────────────────────────
        self.play(
            FadeOut(title),
            FadeOut(arrow_mod), FadeOut(dot_s), FadeOut(dot_e),
            FadeOut(lbl_P), FadeOut(lbl_Q),
            FadeOut(brace_group), FadeOut(len_label),
            FadeOut(formula_card), FadeOut(formula_row), FadeOut(also_label),
            FadeOut(nonneg_card), FadeOut(nonneg_row),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 5: 相等向量 vs 相反向量
    # =========================================================
    def scene_5_equal_opposite(self):

        # ── 第一段：相等向量 ─────────────────────────────
        title_eq = self.make_scene_title("相等向量", color=self.C_EQUAL, y=6.0)
        self.play(FadeIn(title_eq), run_time=0.4)

        # 4条平行等长箭头，依次出现
        eq_colors = [self.C_EQUAL, self.C_MAIN, self.C_RED, self.C_GREEN]
        eq_arrows = VGroup()
        eq_labels = VGroup()

        label_names = [
            r"\vec{a}",
            r"\vec{b}",
            r"\vec{c}",
            r"\vec{d}",
        ]

        for i, (start, end, color, sym) in enumerate(
            zip(self.EQ_STARTS, self.EQ_ENDS, eq_colors, label_names)
        ):
            arr = self.make_arrow(start, end, color, stroke=5)
            eq_arrows.add(arr)
            # 标签放在箭头中点上方
            mid = (start + end) / 2
            lbl = MathTex(sym, font_size=30, color=color).move_to(
                mid + np.array([0, 0.45, 0])
            )
            eq_labels.add(lbl)

        # 逐一绘制
        for arr, lbl in zip(eq_arrows, eq_labels):
            self.play(GrowArrow(arr), FadeIn(lbl), run_time=0.45)

        # 强调"方向相同、大小相同"
        eq_cond_card = self.make_card(7.8, 2.0, DOWN * 4.5, self.C_EQUAL)
        eq_cond1 = Text(
            "方向相同  且  大小相等",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_EQUAL,
        ).move_to(DOWN * 4.2)
        eq_cond2 = VGroup(
            Text("即", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            MathTex(r"\vec{a} = \vec{b} = \vec{c} = \vec{d}",
                    font_size=32, color=self.C_EQUAL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.9)

        self.play(FadeIn(eq_cond_card), run_time=0.3)
        self.play(FadeIn(eq_cond1), run_time=0.4)
        self.play(FadeIn(eq_cond2), run_time=0.4)

        # 关键提示：起点不同也可以相等
        eq_note = Text(
            "起点不同，仍可以是相等向量！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B,
        ).move_to(DOWN * 5.7)
        self.play(FadeIn(eq_note), run_time=0.4)
        self.wait(1.8)

        # 清除相等向量内容
        self.play(
            FadeOut(title_eq),
            FadeOut(eq_arrows),
            FadeOut(eq_labels),
            FadeOut(eq_cond_card),
            FadeOut(eq_cond1),
            FadeOut(eq_cond2),
            FadeOut(eq_note),
            run_time=0.5,
        )

        # ── 第二段：相反向量 ─────────────────────────────
        title_opp = self.make_scene_title("相反向量", color=self.C_OPPOSITE, y=6.0)
        self.play(FadeIn(title_opp), run_time=0.4)

        # 正向箭头 \vec{a}（左→右，橙红）
        opp_arr_a = self.make_arrow(
            self.OPP_A_START, self.OPP_A_END,
            self.C_OPPOSITE, stroke=6
        )
        # 反向箭头 \vec{b}（右→左，青色）
        opp_arr_b = self.make_arrow(
            self.OPP_B_START, self.OPP_B_END,
            self.C_MAIN, stroke=6
        )

        self.play(GrowArrow(opp_arr_a), run_time=0.7)

        lbl_a_opp = MathTex(r"\vec{a}", font_size=36, color=self.C_OPPOSITE).move_to(
            (self.OPP_A_START + self.OPP_A_END) / 2 + UP * 0.5
        )
        self.play(FadeIn(lbl_a_opp), run_time=0.3)

        self.play(GrowArrow(opp_arr_b), run_time=0.7)
        lbl_b_opp = MathTex(r"\vec{b}", font_size=36, color=self.C_MAIN).move_to(
            (self.OPP_B_START + self.OPP_B_END) / 2 + DOWN * 0.6
        )
        self.play(FadeIn(lbl_b_opp), run_time=0.3)

        # 等长标记（两条竖线）
        mid_a = (self.OPP_A_START + self.OPP_A_END) / 2
        mid_b = (self.OPP_B_START + self.OPP_B_END) / 2

        tick_a = Line(mid_a + DOWN * 0.18, mid_a + UP * 0.18,
                      color=WHITE, stroke_width=3)
        tick_b1 = Line(mid_b + DOWN * 0.18 + LEFT * 0.08,
                       mid_b + UP * 0.18 + LEFT * 0.08,
                       color=WHITE, stroke_width=3)
        tick_b2 = Line(mid_b + DOWN * 0.18 + RIGHT * 0.08,
                       mid_b + UP * 0.18 + RIGHT * 0.08,
                       color=WHITE, stroke_width=3)

        self.play(Create(tick_a), Create(tick_b1), Create(tick_b2), run_time=0.4)

        # 结论公式
        opp_card = self.make_card(7.8, 2.8, DOWN * 4.0, self.C_OPPOSITE)

        opp_cond = Text(
            "大小相等  方向相反",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_OPPOSITE,
        ).move_to(DOWN * 3.5)

        opp_formula = VGroup(
            MathTex(r"\vec{b} = -\vec{a}", font_size=44, color=self.C_OPPOSITE),
        ).move_to(DOWN * 4.3)

        opp_note = Text(
            "互为相反向量",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
        ).move_to(DOWN * 5.0)

        self.play(FadeIn(opp_card), run_time=0.3)
        self.play(FadeIn(opp_cond), run_time=0.4)
        self.play(Write(opp_formula), run_time=0.6)
        self.play(FadeIn(opp_note), run_time=0.3)
        self.wait(2.0)

        # ── 清场 ─────────────────────────────────────────
        self.play(
            FadeOut(title_opp),
            FadeOut(opp_arr_a), FadeOut(opp_arr_b),
            FadeOut(lbl_a_opp), FadeOut(lbl_b_opp),
            FadeOut(tick_a), FadeOut(tick_b1), FadeOut(tick_b2),
            FadeOut(opp_card), FadeOut(opp_cond),
            FadeOut(opp_formula), FadeOut(opp_note),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 6: 零向量
    # =========================================================
    def scene_6_zero_vector(self):
        title = self.make_scene_title("零向量", color=GRAY_A, y=6.0)
        self.play(FadeIn(title), run_time=0.4)

        # ── 动画：箭头从有到无，收缩为点 ─────────────────
        zero_center = np.array([0.0, 2.5, 0])

        # 初始：一条短向量
        start_vec_s = zero_center + np.array([-1.2, 0, 0])
        start_vec_e = zero_center + np.array([ 1.2, 0, 0])
        arrow_shrink = self.make_arrow(start_vec_s, start_vec_e,
                                       GRAY_A, stroke=5)
        self.play(GrowArrow(arrow_shrink), run_time=0.6)

        # 收缩动画 → 变成点
        zero_dot = Dot(zero_center, radius=0.15, color=GRAY_B)
        self.play(
            Transform(arrow_shrink, zero_dot),
            run_time=1.0,
        )
        self.remove(arrow_shrink)
        self.add(zero_dot)

        # Flash 强调
        self.play(Flash(zero_dot, color=GRAY_A, flash_radius=0.3), run_time=0.4)

        # 符号 \vec{0}
        sym_zero = MathTex(r"\vec{0}", font_size=56, color=GRAY_A).move_to(
            zero_center + DOWN * 0.9
        )
        self.play(Write(sym_zero), run_time=0.6)

        # ── 定义卡片 ─────────────────────────────────────
        zero_card = self.make_card(7.8, 3.0, UP * 0.5, GRAY_B, "#0d0d1a")

        zero_def1 = Text(
            "零向量：模为 0 的向量",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE,
        ).move_to(UP * 0.9)

        zero_def2 = MathTex(
            r"|\vec{0}| = 0",
            font_size=38,
            color=GRAY_A,
        ).move_to(UP * 0.3)

        zero_def3 = Text(
            "方向：任意（特殊规定）",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B,
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(zero_card), run_time=0.3)
        self.play(FadeIn(zero_def1), run_time=0.4)
        self.play(Write(zero_def2), run_time=0.5)
        self.play(FadeIn(zero_def3), run_time=0.4)

        # 对比提示
        cmp_zero = Text(
            "只有零向量的模为 0",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_TITLE,
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(cmp_zero), run_time=0.4)
        self.wait(1.8)

        # ── 清场 ─────────────────────────────────────────
        self.play(
            FadeOut(title), FadeOut(zero_dot), FadeOut(sym_zero),
            FadeOut(zero_card), FadeOut(zero_def1),
            FadeOut(zero_def2), FadeOut(zero_def3),
            FadeOut(cmp_zero),
            run_time=0.5,
        )

    # =========================================================
    # § Scene 7: 总结 + 片尾
    # =========================================================
    def scene_7_summary(self):
        sum_title = Text(
            "核心知识总结",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.C_TITLE,
        ).move_to(UP * 5.8)
        self.play(Write(sum_title), run_time=0.5)

        # ── 4张概念卡片，逐一滑入 ────────────────────────
        card_data = [
            (
                "向量", "既有大小，又有方向的量", self.C_MAIN,
                r"\overrightarrow{AB} \; \text{or} \; \vec{a}", UP * 4.5,
            ),
            (
                "向量的模", "有向线段的长度（≥ 0）", self.C_MODULE,
                r"|\vec{a}| \geq 0", UP * 3.2,
            ),
            (
                "相等向量", "大小相等，方向相同", self.C_EQUAL,
                r"\vec{a} = \vec{b}", UP * 1.9,
            ),
            (
                "相反向量", "大小相等，方向相反", self.C_OPPOSITE,
                r"\vec{b} = -\vec{a}", UP * 0.6,
            ),
        ]

        all_cards = []
        for cname, cdesc, color, formula_str, ypos in card_data:
            card_bg = self.make_card(8.0, 1.1, ypos, color)

            row_left = VGroup(
                Text(cname, font="Noto Sans CJK SC",
                     font_size=24, color=color),
                Text(cdesc, font="Noto Sans CJK SC",
                     font_size=18, color=GRAY_A),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.05).move_to(
                ypos + LEFT * 2.0
            )

            row_right = MathTex(formula_str, font_size=30, color=color).move_to(
                ypos + RIGHT * 2.0
            )

            grp = VGroup(card_bg, row_left, row_right)
            grp.shift(LEFT * 11)   # 初始在画面外
            all_cards.append(grp)

        for grp in all_cards:
            self.play(grp.animate.shift(RIGHT * 11), run_time=0.35)

        # 零向量条
        zero_row = VGroup(
            Text("零向量", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
            Text("模为0的特殊向量", font="Noto Sans CJK SC", font_size=18, color=GRAY_B),
            MathTex(r"|\vec{0}| = 0", font_size=30, color=GRAY_A),
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 0.8)
        zero_row.shift(LEFT * 11)
        self.play(zero_row.animate.shift(RIGHT * 11), run_time=0.3)

        self.wait(1.2)

        # ── 清除总结，进入片尾 ────────────────────────────
        self.play(
            FadeOut(sum_title),
            *[FadeOut(g) for g in all_cards],
            FadeOut(zero_row),
            run_time=0.6,
        )

        # ── 片尾：作者信息 ────────────────────────────────
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=42,
            color=WHITE,
            weight=BOLD,
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B,
        ).move_to(UP * 1.1)

        divider = Line(LEFT * 3.5, RIGHT * 3.5,
                       color=GRAY_B, stroke_width=1).move_to(UP * 0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_TITLE,
        ).move_to(ORIGIN)

        # 装饰：多个小箭头旋转
        deco_arrows = VGroup(*[
            Arrow(
                ORIGIN,
                np.array([np.cos(i * TAU / 8), np.sin(i * TAU / 8), 0]) * 0.5,
                color=[self.C_MAIN, self.C_RED, self.C_GREEN,
                       self.C_EQUAL, self.C_OPPOSITE, self.C_MODULE,
                       YELLOW, WHITE][i],
                stroke_width=3,
                max_tip_length_to_length_ratio=0.4,
                buff=0,
            )
            for i in range(8)
        ]).move_to(DOWN * 2.0)

        self.play(Transform(self.author_info, author_large), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in deco_arrows], lag_ratio=0.06),
            run_time=0.7,
        )
        self.play(Rotate(deco_arrows, angle=TAU / 8, run_time=1.0))
        self.wait(1.5)

        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(divider),
            FadeOut(follow_text),
            FadeOut(deco_arrows),
            run_time=0.8,
        )


# ============================================================
# 渲染命令:
# manim -pql vector_concepts.py PlaneVectorConcepts   # 快速预览
# manim -qh  vector_concepts.py PlaneVectorConcepts   # 高质量
# ============================================================