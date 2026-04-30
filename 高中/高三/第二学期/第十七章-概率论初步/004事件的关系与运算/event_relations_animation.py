"""
事件的关系与运算 - 高三数学教学动画
概率论初步: 并事件、交事件、互斥事件、对立事件
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== TikTok 竖屏配置 =====
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

FONT = "PingFang SC"

# ===== 颜色方案 =====
BG      = "#1a1a2e"
C_A     = "#e74c3c"   # 红 - 事件A
C_B     = "#3498db"   # 蓝 - 事件B
C_AB    = "#9b59b6"   # 紫 - 交集
C_UNI   = "#2ecc71"   # 绿 - 并集
C_OMEGA = "#7f8c8d"   # 灰 - 样本空间
C_HL    = "#f1c40f"   # 金 - 高亮
C_COMP  = "#e67e22"   # 橙 - 补事件
C_CARD  = "#16213e"   # 深蓝卡片
C_EX    = "#1abc9c"   # 青 - 互斥


# ================================================================
class EventRelations(Scene):
    """
    事件关系与运算教学动画
    Scene 1  开场钩子
    Scene 2  样本空间 & 基础韦恩图
    Scene 3  包含关系 A⊆B
    Scene 4  并事件 A∪B
    Scene 5  交事件 A∩B
    Scene 6  互斥事件 & 对立事件
    Scene 7  总结 & 片尾
    """

    # ── 韦恩图参数 ───────────────────────────────────────────────
    R = 1.35          # 标准圆半径（等圆场景）
    DX = 1.0          # 两圆圆心各偏离原点的 x 距离
    # 圆心: A = (-DX, 0), B = (+DX, 0)
    # 圆心距 d = 2*DX = 2.0   |r1-r2|=0 < d < r1+r2=2.7  ✓相交
    VENN_OFFSET = UP * 0.5   # 韦恩图整体偏移（主内容区中央偏上）

    # ── 互斥场景参数 ─────────────────────────────────────────────
    R_EX  = 1.0
    DX_EX = 1.8    # d = 3.6 > 2.0 = r1+r2  ✓ 不相交

    # ── 包含场景参数 ─────────────────────────────────────────────
    R_INNER = 0.75
    R_OUTER = 1.4
    # 小圆圆心偏移: (-0.3, 0)  大圆圆心: (0, 0)
    # dist + R_INNER = 0.3+0.75 = 1.05 ≤ 1.4 = R_OUTER  ✓ 内含

    def construct(self):
        self.camera.background_color = BG
        self.scene_1_opening()
        self.scene_2_sample_space()
        self.scene_3_containment()
        self.scene_4_union()
        self.scene_5_intersection()
        self.scene_6_exclusive_and_complementary()
        self.scene_7_summary()

    # ================================================================
    #  工具函数
    # ================================================================

    def _make_venn_base(self, r=None, dx=None, offset=None,
                        opacity_a=0.35, opacity_b=0.35,
                        color_a=None, color_b=None):
        """
        创建基础韦恩图（样本空间矩形 + 两圆）。
        返回 (omega_rect, circle_a, circle_b, label_omega, label_a, label_b)
        """
        r      = r      if r      is not None else self.R
        dx     = dx     if dx     is not None else self.DX
        offset = offset if offset is not None else self.VENN_OFFSET
        ca     = color_a if color_a else C_A
        cb     = color_b if color_b else C_B

        omega_rect = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.6
        ).move_to(offset)

        circle_a = Circle(radius=r, stroke_color=ca, stroke_width=2.5,
                          fill_color=ca, fill_opacity=opacity_a
                          ).move_to(offset + LEFT * dx)

        circle_b = Circle(radius=r, stroke_color=cb, stroke_width=2.5,
                          fill_color=cb, fill_opacity=opacity_b
                          ).move_to(offset + RIGHT * dx)

        label_omega = Text("Ω", font=FONT, font_size=24, color=C_OMEGA
                           ).next_to(omega_rect, UR, buff=-0.5)
        label_a = Text("A", font=FONT, font_size=32, color=ca
                       ).move_to(offset + LEFT * (dx + r * 0.55))
        label_b = Text("B", font=FONT, font_size=32, color=cb
                       ).move_to(offset + RIGHT * (dx + r * 0.55))

        return omega_rect, circle_a, circle_b, label_omega, label_a, label_b

    def _make_intersection_fill(self, circle_a, circle_b, color=C_AB, opacity=0.85):
        """用 Intersection 生成 A∩B 填充区域"""
        fill = Intersection(circle_a, circle_b,
                            fill_color=color, fill_opacity=opacity,
                            stroke_width=0)
        return fill

    def _title_block(self, main_text, sub_text=None, main_color=C_HL,
                     sub_color=GRAY_A, main_size=42, sub_size=26):
        """生成标题 + 副标题组"""
        title = Text(main_text, font=FONT, font_size=main_size, color=main_color)
        title.move_to(UP * 6.0)
        if sub_text:
            sub = Text(sub_text, font=FONT, font_size=sub_size, color=sub_color)
            sub.next_to(title, DOWN, buff=0.3)
            return VGroup(title, sub)
        return title

    def _formula_box(self, tex_str, color=C_HL, font_size=40):
        """公式 + 外框"""
        f = MathTex(tex_str, font_size=font_size, color=color)
        box = SurroundingRectangle(f, color=color, buff=0.22, corner_radius=0.12)
        return VGroup(f, box)

    def _card(self, lines, width=7.0, color=C_HL):
        """多行文字卡片"""
        texts = VGroup(*[
            Text(l, font=FONT, font_size=24, color=WHITE) for l in lines
        ]).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        bg = RoundedRectangle(
            width=max(texts.width + 0.8, width),
            height=texts.height + 0.5,
            corner_radius=0.15,
            fill_color=C_CARD, fill_opacity=0.95,
            stroke_color=color, stroke_width=2
        )
        texts.move_to(bg.get_center())
        return VGroup(bg, texts)

    # ================================================================
    #  Scene 1: 开场钩子
    # ================================================================
    def scene_1_opening(self):
        # 作者信息（常驻顶部）
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_OMEGA
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.15), run_time=0.4)

        # 大钩子
        hook_q = Text("掷一颗骰子", font=FONT, font_size=52, color=WHITE)
        hook_q.move_to(UP * 5.3)
        self.play(Write(hook_q), run_time=0.5)

        # 事件定义
        evt_a = Text("A = 出现奇数  {1, 3, 5}", font=FONT,
                     font_size=30, color=C_A).move_to(UP * 4.1)
        evt_b = Text("B = 出现质数  {2, 3, 5}", font=FONT,
                     font_size=30, color=C_B).move_to(UP * 3.3)
        self.play(FadeIn(evt_a, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(evt_b, shift=RIGHT * 0.3), run_time=0.4)

        # 六面骰子点数
        nums = VGroup(*[
            Text(str(i), font=FONT, font_size=36,
                 color=C_A if i % 2 == 1 else WHITE)
            .move_to(LEFT * (2.5 - (i - 1) * 1.0) + UP * 2.2)
            for i in range(1, 7)
        ])
        # 质数染蓝（2,3,5）
        for obj, val in zip(nums, range(1, 7)):
            if val in (2, 3, 5):
                obj.set_color(C_B)
            if val in (3, 5):    # 既是奇数又是质数 → 紫
                obj.set_color(C_AB)
        self.play(FadeIn(nums, shift=UP * 0.2), run_time=0.5)

        question = Text("它们有什么关系？", font=FONT,
                        font_size=38, color=C_HL).move_to(UP * 1.1)
        self.play(Write(question), run_time=0.6)

        answer = Text("用韦恩图来看！", font=FONT,
                      font_size=34, color=C_UNI).move_to(UP * 0.2)
        self.play(FadeIn(answer, scale=1.1), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook_q, evt_a, evt_b, nums, question, answer)),
                  run_time=0.5)

    # ================================================================
    #  Scene 2: 样本空间 & 基础韦恩图
    # ================================================================
    def scene_2_sample_space(self):
        title = self._title_block("样本空间与事件",
                                  sub_text="韦恩图直观表示", main_size=40)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        omega, ca, cb, lω, la, lb = self._make_venn_base()

        # 样本空间矩形
        self.play(Create(omega), run_time=0.5)
        self.play(Write(lω), run_time=0.3)

        # 圆A
        self.play(GrowFromCenter(ca), run_time=0.6)
        self.play(Write(la), run_time=0.3)

        # 圆B
        self.play(GrowFromCenter(cb), run_time=0.6)
        self.play(Write(lb), run_time=0.3)

        # 交叠区域提示
        inter_fill = self._make_intersection_fill(ca, cb)
        self.play(FadeIn(inter_fill, scale=0.8), run_time=0.5)

        desc_ab = Text("重叠部分 = A 和 B 都发生", font=FONT,
                       font_size=26, color=C_AB).move_to(DOWN * 2.5)
        self.play(FadeIn(desc_ab, shift=UP * 0.2), run_time=0.5)

        desc_out = Text("矩形外没有 = 不可能事件", font=FONT,
                        font_size=24, color=C_OMEGA).move_to(DOWN * 3.3)
        self.play(FadeIn(desc_out), run_time=0.4)
        self.wait(0.8)

        self.play(FadeOut(VGroup(title, omega, ca, cb, lω, la, lb,
                                 inter_fill, desc_ab, desc_out)),
                  run_time=0.5)

    # ================================================================
    #  Scene 3: 包含关系 A⊆B
    # ================================================================
    def scene_3_containment(self):
        title = self._title_block("包含关系  A ⊆ B",
                                  sub_text="A 发生必然导致 B 发生",
                                  main_color=C_B, main_size=40)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        off = self.VENN_OFFSET
        omega = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.6
        ).move_to(off)

        # 大圆 B
        circle_b_big = Circle(radius=self.R_OUTER,
                              stroke_color=C_B, stroke_width=2.5,
                              fill_color=C_B, fill_opacity=0.25
                              ).move_to(off + RIGHT * 0.2)

        # 小圆 A（在 B 内部）
        circle_a_small = Circle(radius=self.R_INNER,
                                stroke_color=C_A, stroke_width=2.5,
                                fill_color=C_A, fill_opacity=0.55
                                ).move_to(off + LEFT * 0.3)

        label_b = Text("B", font=FONT, font_size=36, color=C_B
                       ).move_to(off + RIGHT * (0.2 + self.R_OUTER * 0.65))
        label_a = Text("A", font=FONT, font_size=28, color=C_A
                       ).move_to(circle_a_small.get_center() + LEFT * 0.1)

        lω = Text("Ω", font=FONT, font_size=24, color=C_OMEGA
                  ).next_to(omega, UR, buff=-0.5)

        self.play(Create(omega), Write(lω), run_time=0.4)
        self.play(GrowFromCenter(circle_b_big), Write(label_b), run_time=0.6)
        self.play(GrowFromCenter(circle_a_small), Write(label_a), run_time=0.5)
        self.wait(0.3)

        # 箭头说明
        arrow = Arrow(
            circle_a_small.get_center() + DOWN * 0.5,
            circle_b_big.get_center() + DOWN * 1.1,
            buff=0.1, color=C_HL, stroke_width=2.5
        )
        desc = Text("A 发生 → B 必然发生", font=FONT,
                    font_size=28, color=C_HL).move_to(DOWN * 2.5)
        self.play(GrowArrow(arrow), FadeIn(desc, shift=UP * 0.2), run_time=0.6)

        # 数学符号
        sub_formula = MathTex(r"A \subseteq B", font_size=52, color=C_B
                              ).move_to(DOWN * 3.6)
        self.play(Write(sub_formula), run_time=0.6)

        # 小例子
        eg = Text("例: A={3} ⊆ B={2,3,5}  ✓", font=FONT,
                  font_size=24, color=GRAY_A).move_to(DOWN * 4.6)
        self.play(FadeIn(eg), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, omega, lω, circle_b_big, circle_a_small,
                                 label_a, label_b, arrow, desc,
                                 sub_formula, eg)),
                  run_time=0.5)

    # ================================================================
    #  Scene 4: 并事件 A∪B
    # ================================================================
    def scene_4_union(self):
        title = self._title_block("并事件  A ∪ B",
                                  sub_text="A 或 B 至少一个发生",
                                  main_color=C_UNI, main_size=42)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        omega, ca, cb, lω, la, lb = self._make_venn_base(
            opacity_a=0.15, opacity_b=0.15)
        self.play(Create(omega), Write(lω), run_time=0.4)
        self.play(GrowFromCenter(ca), Write(la), run_time=0.4)
        self.play(GrowFromCenter(cb), Write(lb), run_time=0.4)

        # ── 高亮整个 A∪B（两圆各自高亮填充）──
        union_a = ca.copy().set_fill(C_UNI, opacity=0.65).set_stroke(width=0)
        union_b = cb.copy().set_fill(C_UNI, opacity=0.65).set_stroke(width=0)
        inter_cover = self._make_intersection_fill(ca, cb, color=C_UNI, opacity=0.75)

        union_label = MathTex(r"A \cup B", font_size=40, color=C_UNI
                              ).move_to(self.VENN_OFFSET)

        self.play(
            FadeIn(union_a), FadeIn(union_b), FadeIn(inter_cover),
            run_time=0.6
        )
        self.play(Write(union_label), run_time=0.4)
        self.wait(0.3)

        # ── 一般加法公式 ──
        formula_gen = self._formula_box(
            r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
            color=C_UNI, font_size=34
        ).move_to(DOWN * 2.6)
        self.play(FadeIn(formula_gen), run_time=0.6)

        # ── 解释: 为什么减去交集 ──
        explain = Text("防止 A∩B 被重复计算", font=FONT,
                       font_size=26, color=C_OMEGA).move_to(DOWN * 3.7)
        inter_highlight = self._make_intersection_fill(
            ca, cb, color=C_HL, opacity=0.9)
        self.play(FadeIn(explain), FadeIn(inter_highlight), run_time=0.5)

        # 箭头指向交集
        arrow_int = Arrow(
            self.VENN_OFFSET + UP * 0.05,
            self.VENN_OFFSET + DOWN * 0.35,
            buff=0, color=C_HL, stroke_width=2
        )
        self.play(GrowArrow(arrow_int), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, omega, ca, cb, lω, la, lb,
            union_a, union_b, inter_cover, union_label,
            formula_gen, explain, inter_highlight, arrow_int
        )), run_time=0.5)

    # ================================================================
    #  Scene 5: 交事件 A∩B
    # ================================================================
    def scene_5_intersection(self):
        title = self._title_block("交事件  A ∩ B",
                                  sub_text="A 和 B 同时发生",
                                  main_color=C_AB, main_size=42)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        omega, ca, cb, lω, la, lb = self._make_venn_base(
            opacity_a=0.15, opacity_b=0.15)
        self.play(Create(omega), Write(lω), run_time=0.4)
        self.play(GrowFromCenter(ca), Write(la), run_time=0.4)
        self.play(GrowFromCenter(cb), Write(lb), run_time=0.4)

        # ── 只高亮交集 ──
        inter_fill = self._make_intersection_fill(ca, cb, color=C_AB, opacity=0.90)
        inter_label = MathTex(r"A \cap B", font_size=36, color=C_AB
                              ).move_to(self.VENN_OFFSET)

        self.play(FadeIn(inter_fill, scale=0.6), run_time=0.6)
        self.play(Write(inter_label), run_time=0.4)
        self.wait(0.3)

        # ── 不等式性质 ──
        ineq_1 = MathTex(r"P(A \cap B) \leq P(A)", font_size=38, color=WHITE
                         ).move_to(DOWN * 2.4)
        ineq_2 = MathTex(r"P(A \cap B) \leq P(B)", font_size=38, color=WHITE
                         ).move_to(DOWN * 3.2)
        self.play(Write(ineq_1), run_time=0.5)
        self.play(Write(ineq_2), run_time=0.5)

        desc_ineq = Text("交集不可能比单个事件更大", font=FONT,
                         font_size=25, color=GRAY_A).move_to(DOWN * 4.2)
        self.play(FadeIn(desc_ineq), run_time=0.4)

        # 骰子例子
        eg = Text("例: A={1,3,5}  B={2,3,5}  A∩B={3,5}", font=FONT,
                  font_size=24, color=GRAY_A).move_to(DOWN * 5.2)
        self.play(FadeIn(eg), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, omega, ca, cb, lω, la, lb,
            inter_fill, inter_label,
            ineq_1, ineq_2, desc_ineq, eg
        )), run_time=0.5)

    # ================================================================
    #  Scene 6: 互斥事件 & 对立事件
    # ================================================================
    def scene_6_exclusive_and_complementary(self):
        self._scene_6a_exclusive()
        self._scene_6b_complementary()

    def _scene_6a_exclusive(self):
        """互斥事件：两圆不相交"""
        title = self._title_block("互斥事件（不相容事件）",
                                  sub_text="不能同时发生",
                                  main_color=C_EX, main_size=38)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        off = self.VENN_OFFSET
        omega = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.6
        ).move_to(off)

        # 两圆不相交（互斥）
        ex_a = Circle(radius=self.R_EX,
                      stroke_color=C_A, stroke_width=2.5,
                      fill_color=C_A, fill_opacity=0.45
                      ).move_to(off + LEFT * self.DX_EX)
        ex_b = Circle(radius=self.R_EX,
                      stroke_color=C_B, stroke_width=2.5,
                      fill_color=C_B, fill_opacity=0.45
                      ).move_to(off + RIGHT * self.DX_EX)

        lω = Text("Ω", font=FONT, font_size=24, color=C_OMEGA
                  ).next_to(omega, UR, buff=-0.5)
        la = Text("A", font=FONT, font_size=32, color=C_A).move_to(ex_a.get_center())
        lb = Text("B", font=FONT, font_size=32, color=C_B).move_to(ex_b.get_center())

        self.play(Create(omega), Write(lω), run_time=0.4)
        self.play(GrowFromCenter(ex_a), Write(la), run_time=0.5)
        self.play(GrowFromCenter(ex_b), Write(lb), run_time=0.5)

        # A∩B = ∅
        empty_formula = MathTex(r"A \cap B = \varnothing", font_size=48,
                                color=C_EX).move_to(DOWN * 2.4)
        self.play(Write(empty_formula), run_time=0.6)

        # 加法公式（互斥时无需减交集）
        add_formula = self._formula_box(
            r"P(A \cup B) = P(A) + P(B)",
            color=C_EX, font_size=38
        ).move_to(DOWN * 3.6)
        self.play(FadeIn(add_formula), run_time=0.5)

        hint = Text("互斥 → 加法公式不需要减交集！", font=FONT,
                    font_size=26, color=C_HL).move_to(DOWN * 4.8)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.4)

        # 骰子例子
        eg = Text("例: A={奇数}  B={偶数}  → 互斥", font=FONT,
                  font_size=24, color=GRAY_A).move_to(DOWN * 5.7)
        self.play(FadeIn(eg), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, omega, lω, ex_a, ex_b, la, lb,
            empty_formula, add_formula, hint, eg
        )), run_time=0.5)

    def _scene_6b_complementary(self):
        """对立事件：互斥 + 覆盖全集"""
        title = self._title_block("对立事件（互为对立）",
                                  sub_text="互斥 且 合起来等于 Ω",
                                  main_color=C_COMP, main_size=38)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        off = self.VENN_OFFSET
        omega_rect = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.6
        ).move_to(off)

        # A 占左半，Ā 占右半（用 Rectangle 表示两半覆盖 Ω）
        half_w = 3.1
        rect_a = Rectangle(
            width=half_w, height=3.2,
            stroke_width=0,
            fill_color=C_A, fill_opacity=0.45
        ).move_to(off + LEFT * half_w / 2)
        # 圆角遮罩：直接用圆角矩形叠加实现视觉
        rect_comp = Rectangle(
            width=half_w, height=3.2,
            stroke_width=0,
            fill_color=C_COMP, fill_opacity=0.45
        ).move_to(off + RIGHT * half_w / 2)

        # 用 Intersection / Difference 来精确裁剪（视觉效果）
        fill_a = Intersection(
            rect_a, omega_rect,
            fill_color=C_A, fill_opacity=0.5, stroke_width=0
        )
        fill_comp = Intersection(
            rect_comp, omega_rect,
            fill_color=C_COMP, fill_opacity=0.5, stroke_width=0
        )

        lω = Text("Ω", font=FONT, font_size=24, color=C_OMEGA
                  ).next_to(omega_rect, UR, buff=-0.5)
        la = Text("A", font=FONT, font_size=34, color=C_A
                  ).move_to(off + LEFT * 1.5)
        lb = Text("Ā", font=FONT, font_size=34, color=C_COMP
                  ).move_to(off + RIGHT * 1.5)
        sep = DashedLine(
            off + UP * 1.6, off + DOWN * 1.6,
            color=WHITE, stroke_width=2.5, dash_length=0.15
        )

        self.play(Create(omega_rect), Write(lω), run_time=0.4)
        self.play(FadeIn(fill_a), FadeIn(fill_comp), run_time=0.5)
        self.play(Create(sep), Write(la), Write(lb), run_time=0.5)

        # 两个条件
        cond_1 = MathTex(r"A \cap \bar{A} = \varnothing", font_size=42,
                         color=WHITE).move_to(DOWN * 2.4)
        cond_2 = MathTex(r"A \cup \bar{A} = \Omega", font_size=42,
                         color=WHITE).move_to(DOWN * 3.2)
        self.play(Write(cond_1), run_time=0.5)
        self.play(Write(cond_2), run_time=0.5)

        # 核心公式
        core = self._formula_box(
            r"P(\bar{A}) = 1 - P(A)",
            color=C_COMP, font_size=46
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(core), run_time=0.6)
        self.wait(0.5)

        # 对比小结
        compare = VGroup(
            Text("互斥：不能同时发生，但可以都不发生",
                 font=FONT, font_size=22, color=C_EX),
            Text("对立：不能同时，也不能都不发生",
                 font=FONT, font_size=22, color=C_COMP),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 6.0)
        self.play(FadeIn(compare[0], shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(compare[1], shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, omega_rect, lω, fill_a, fill_comp, sep,
            la, lb, cond_1, cond_2, core, compare
        )), run_time=0.5)

    # ================================================================
    #  Scene 7: 总结 & 片尾
    # ================================================================
    def scene_7_summary(self):
        # 公式汇总标题
        sum_title = Text("知识点总结", font=FONT, font_size=42,
                         color=C_HL).move_to(UP * 6.0)
        self.play(Write(sum_title), run_time=0.5)

        # 五张知识卡依次滑入
        cards_data = [
            ("并事件  A∪B",
             r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
             C_UNI, UP * 4.2),
            ("互斥时",
             r"P(A \cup B) = P(A) + P(B)",
             C_EX, UP * 2.8),
            ("交事件  A∩B",
             r"P(A \cap B) \leq \min\{P(A), P(B)\}",
             C_AB, UP * 1.4),
            ("对立事件",
             r"P(\bar{A}) = 1 - P(A)",
             C_COMP, ORIGIN),
            ("包含关系",
             r"A \subseteq B \Rightarrow P(A) \leq P(B)",
             C_B, DOWN * 1.4),
        ]

        card_objs = VGroup()
        for cn_label, tex, color, pos in cards_data:
            lbl = Text(cn_label, font=FONT, font_size=22, color=color)
            fml = MathTex(tex, font_size=30, color=WHITE)
            row = VGroup(lbl, fml).arrange(RIGHT, buff=0.35)
            bg = RoundedRectangle(
                width=max(row.width + 0.7, 7.5),
                height=row.height + 0.5,
                corner_radius=0.12,
                fill_color=C_CARD, fill_opacity=0.92,
                stroke_color=color, stroke_width=2
            )
            row.move_to(bg.get_center())
            card = VGroup(bg, row).move_to(pos)
            card_objs.add(card)

        for card in card_objs:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.35)

        # 记忆口诀
        motto_bg = RoundedRectangle(
            width=7.6, height=1.1, corner_radius=0.2,
            fill_color="#0a0a1a", fill_opacity=0.95,
            stroke_color=C_HL, stroke_width=2
        ).move_to(DOWN * 3.1)
        motto = Text("「互斥不重叠 · 对立无遗漏 · 并交用公式」",
                     font=FONT, font_size=24, color=C_HL
                     ).move_to(DOWN * 3.1)
        self.play(FadeIn(motto_bg), Write(motto), run_time=0.6)
        self.wait(1.0)

        # ── 片尾 ──
        self.play(
            FadeOut(sum_title), FadeOut(card_objs),
            FadeOut(motto_bg), FadeOut(motto),
            run_time=0.5
        )

        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=42, color=WHITE)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=32, color=C_OMEGA)
        VGroup(author_big, author_id).arrange(DOWN, buff=0.3).move_to(UP * 1.0)

        self.play(
            Transform(self.author_bar, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多概率技巧！",
                      font=FONT, font_size=32, color=C_HL).move_to(DOWN * 0.8)
        follow_box = SurroundingRectangle(
            follow, color=C_HL, buff=0.2, corner_radius=0.12)
        self.play(FadeIn(follow, scale=1.1), Create(follow_box), run_time=0.6)

        # 装饰：三个韦恩图小图标
        icon_venn = self._make_mini_venn_icon(DOWN * 2.8)
        self.play(FadeIn(icon_venn, scale=0.5), run_time=0.5)

        # 最终公式
        final = MathTex(
            r"P(A \cup B) = P(A) + P(B) - P(A \cap B)",
            font_size=36, color=WHITE
        ).move_to(DOWN * 4.8)
        self.play(Write(final), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                self.author_bar, author_id,
                follow, follow_box, icon_venn, final
            )),
            run_time=1.0
        )

    def _make_mini_venn_icon(self, center):
        """小型韦恩图装饰图标"""
        r = 0.45
        dx = 0.35
        ca = Circle(radius=r, fill_color=C_A, fill_opacity=0.5,
                    stroke_color=C_A, stroke_width=1.5).move_to(center + LEFT * dx)
        cb = Circle(radius=r, fill_color=C_B, fill_opacity=0.5,
                    stroke_color=C_B, stroke_width=1.5).move_to(center + RIGHT * dx)
        inter = Intersection(ca, cb,
                             fill_color=C_AB, fill_opacity=0.8, stroke_width=0)
        return VGroup(ca, cb, inter)


# ================================================================
#  渲染命令:
#   预览: manim -pql event_relations_animation.py EventRelations
#   高清: manim -qh  event_relations_animation.py EventRelations
# ================================================================