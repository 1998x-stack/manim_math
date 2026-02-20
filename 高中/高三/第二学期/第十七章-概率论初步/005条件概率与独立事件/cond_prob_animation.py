"""
条件概率与独立事件 - 高三数学教学动画
概率论初步: 条件概率、乘法公式、独立事件、二项分布
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from math import comb as math_comb

# ===== TikTok 竖屏配置 =====
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

FONT = "Noto Sans CJK SC"

# ===== 颜色方案 =====
BG      = "#1a1a2e"
C_A     = "#e74c3c"   # 红  — 事件 A
C_B     = "#3498db"   # 蓝  — 事件 B
C_AB    = "#9b59b6"   # 紫  — 交集 AB
C_COND  = "#2ecc71"   # 绿  — 条件概率高亮
C_IND   = "#f1c40f"   # 金  — 独立事件
C_BINOM = "#e67e22"   # 橙  — 二项分布
C_TREE  = "#1abc9c"   # 青  — 树形图
C_OMEGA = "#7f8c8d"   # 灰  — 样本空间
C_HL    = "#f1c40f"   # 高亮
C_CARD  = "#16213e"   # 深蓝卡片
C_DIM   = "#2c3e50"   # 灰暗（淡出时用）


# ================================================================
class CondProbAnimation(Scene):
    """
    Scene 1  开场钩子
    Scene 2  条件概率定义（韦恩图）
    Scene 3  乘法公式（概率树）
    Scene 4  独立事件
    Scene 5  n 次独立重复 & 二项分布
    Scene 6  全概率公式（简述）
    Scene 7  总结 & 片尾
    """

    # ── 韦恩图公共参数 ──────────────────────────────────────────
    R   = 1.35
    DX  = 1.0          # 两圆各偏离坐标原点的 x 距离
    VENN_OFF = UP * 0.5

    def construct(self):
        self.camera.background_color = BG
        self.scene_1_opening()
        self.scene_2_conditional_prob()
        self.scene_3_multiplication_rule()
        self.scene_4_independence()
        self.scene_5_binomial()
        self.scene_6_total_prob()
        self.scene_7_summary()

    # ================================================================
    #  工具方法
    # ================================================================

    def _venn_base(self, opacity_a=0.35, opacity_b=0.35,
                   color_a=None, color_b=None, offset=None):
        """构建 Ω矩形 + 圆A + 圆B + 标签"""
        ca = color_a or C_A
        cb = color_b or C_B
        off = offset if offset is not None else self.VENN_OFF

        omega = RoundedRectangle(
            width=6.2, height=3.2, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.7
        ).move_to(off)

        cir_a = Circle(radius=self.R, stroke_color=ca, stroke_width=2.5,
                       fill_color=ca, fill_opacity=opacity_a
                       ).move_to(off + LEFT * self.DX)
        cir_b = Circle(radius=self.R, stroke_color=cb, stroke_width=2.5,
                       fill_color=cb, fill_opacity=opacity_b
                       ).move_to(off + RIGHT * self.DX)

        lω = Text("Ω", font=FONT, font_size=22, color=C_OMEGA
                  ).next_to(omega, UR, buff=-0.5)
        la = Text("A", font=FONT, font_size=30, color=ca
                  ).move_to(off + LEFT * (self.DX + self.R * 0.55))
        lb = Text("B", font=FONT, font_size=30, color=cb
                  ).move_to(off + RIGHT * (self.DX + self.R * 0.55))
        return omega, cir_a, cir_b, lω, la, lb

    def _inter_fill(self, ca, cb, color=C_AB, opacity=0.85):
        return Intersection(ca, cb,
                            fill_color=color, fill_opacity=opacity,
                            stroke_width=0)

    def _title(self, main, sub=None, mc=C_HL, sc=GRAY_A, ms=40, ss=26):
        t = Text(main, font=FONT, font_size=ms, color=mc).move_to(UP * 6.0)
        if sub:
            s = Text(sub, font=FONT, font_size=ss, color=sc
                     ).next_to(t, DOWN, buff=0.25)
            return VGroup(t, s)
        return t

    def _fbox(self, tex, color=C_HL, fs=38):
        f = MathTex(tex, font_size=fs, color=color)
        b = SurroundingRectangle(f, color=color, buff=0.22, corner_radius=0.12)
        return VGroup(f, b)

    # ================================================================
    #  Scene 1: 开场钩子
    # ================================================================
    def scene_1_opening(self):
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_OMEGA
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.1), run_time=0.4)

        # 钩子问题
        q1 = Text("明天下雨的概率是 30%", font=FONT, font_size=40, color=WHITE)
        q1.move_to(UP * 5.2)
        self.play(Write(q1), run_time=0.6)

        q2 = Text("但今天是阴天…", font=FONT, font_size=36, color=C_B)
        q2.move_to(UP * 4.2)
        self.play(FadeIn(q2, shift=UP * 0.2), run_time=0.5)

        q3 = Text("概率变成 70%！", font=FONT, font_size=48, color=C_A)
        q3.move_to(UP * 3.1)
        self.play(FadeIn(q3, scale=1.15), run_time=0.5)
        self.wait(0.3)

        explain = Text("这就是——条件概率", font=FONT, font_size=36, color=C_HL)
        explain.move_to(UP * 1.9)
        self.play(Write(explain), run_time=0.6)

        # 公式预告
        prev_f = MathTex(r"P(A \mid B) = \frac{P(AB)}{P(B)}",
                         font_size=52, color=WHITE).move_to(UP * 0.7)
        self.play(Write(prev_f), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(VGroup(q1, q2, q3, explain, prev_f)), run_time=0.5)

    # ================================================================
    #  Scene 2: 条件概率 —— 韦恩图动画
    # ================================================================
    def scene_2_conditional_prob(self):
        title = self._title("条件概率  P(A|B)",
                            sub="B 发生后，A 的概率是多少？",
                            mc=C_COND)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        # ── Step 1: 普通韦恩图 ──
        omega, ca, cb, lω, la, lb = self._venn_base()
        self.play(Create(omega), Write(lω), run_time=0.4)
        self.play(GrowFromCenter(ca), Write(la), run_time=0.5)
        self.play(GrowFromCenter(cb), Write(lb), run_time=0.5)

        inter = self._inter_fill(ca, cb)
        self.play(FadeIn(inter, scale=0.7), run_time=0.4)

        desc_normal = Text("完整样本空间 Ω", font=FONT,
                           font_size=26, color=C_OMEGA).move_to(DOWN * 2.3)
        self.play(FadeIn(desc_normal), run_time=0.3)
        self.wait(0.4)

        # ── Step 2: "B 发生了！" → 灰化 B 外区域 ──
        # 用遮罩：把 Ω-B 区域盖灰
        grey_mask = Difference(
            omega.copy().set_stroke(width=0),
            cb.copy().set_stroke(width=0),
            fill_color="#1a1a2e", fill_opacity=0.78, stroke_width=0
        )

        b_new_label = Text("B 发生了！\n现在 Ω → B", font=FONT,
                            font_size=28, color=C_B).move_to(DOWN * 2.3)

        self.play(
            FadeOut(desc_normal),
            FadeIn(grey_mask),
            cb.animate.set_stroke(color=C_B, width=4),
            run_time=0.6
        )
        self.play(Write(b_new_label), run_time=0.5)
        self.wait(0.4)

        # ── Step 3: 高亮 AB 交叉，说明 P(A|B) ──
        inter_bright = self._inter_fill(ca, cb, color=C_COND, opacity=0.95)
        self.play(FadeOut(inter), FadeIn(inter_bright), run_time=0.4)

        arrow = Arrow(
            self.VENN_OFF + LEFT * 0.15 + DOWN * 0.5,
            self.VENN_OFF + RIGHT * 0.05,
            buff=0, color=C_COND, stroke_width=2.5
        )
        cond_hint = Text("这部分就是 P(A|B)", font=FONT,
                         font_size=26, color=C_COND
                         ).next_to(arrow.get_start(), DOWN, buff=0.1)
        self.play(GrowArrow(arrow), FadeIn(cond_hint), run_time=0.5)
        self.wait(0.4)

        # ── Step 4: 核心公式 ──
        self.play(FadeOut(VGroup(b_new_label, arrow, cond_hint)), run_time=0.3)

        formula = self._fbox(
            r"P(A \mid B) = \frac{P(AB)}{P(B)}",
            color=C_COND, fs=42
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(formula), run_time=0.6)

        # 面积比直观
        area_hint = Text("= AB 面积 ÷ B 面积", font=FONT,
                         font_size=24, color=GRAY_A).move_to(DOWN * 3.6)
        self.play(FadeIn(area_hint), run_time=0.4)

        # ── Step 5: 数值例子 ──
        eg_title = Text("例：P(AB)=0.12，P(B)=0.4", font=FONT,
                        font_size=26, color=GRAY_A).move_to(DOWN * 4.5)
        eg_ans   = MathTex(r"P(A \mid B) = \frac{0.12}{0.4} = 0.3",
                           font_size=34, color=C_COND).move_to(DOWN * 5.4)
        self.play(FadeIn(eg_title), run_time=0.4)
        self.play(Write(eg_ans), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, omega, ca, cb, lω, la, lb,
            grey_mask, inter_bright,
            formula, area_hint, eg_title, eg_ans
        )), run_time=0.5)

    # ================================================================
    #  Scene 3: 乘法公式 —— 概率树
    # ================================================================
    def scene_3_multiplication_rule(self):
        title = self._title("乘法公式", sub="用树形图理解 P(AB)",
                            mc=C_TREE)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        # ── 坐标系（树形图逻辑坐标，整体居中偏上）──
        off = DOWN * 0.2   # 整棵树的纵向偏移

        # 节点位置（屏幕坐标）
        root_pos  = LEFT * 3.8 + off
        b_pos     = LEFT * 1.0 + UP * 1.8 + off
        bc_pos    = LEFT * 1.0 + DOWN * 1.8 + off
        ab_pos    = RIGHT * 2.4 + UP * 2.8 + off
        acb_pos   = RIGHT * 2.4 + UP * 0.8 + off
        abc_pos   = RIGHT * 2.4 + DOWN * 0.8 + off
        acbc_pos  = RIGHT * 2.4 + DOWN * 2.8 + off

        # 节点样式
        def node(pos, label_str, color, radius=0.18):
            dot = Circle(radius=radius, fill_color=color, fill_opacity=1,
                         stroke_width=0).move_to(pos)
            lbl = Text(label_str, font=FONT, font_size=22, color=WHITE
                       ).move_to(pos)
            return VGroup(dot, lbl)

        root_node = node(root_pos, "·", C_OMEGA, 0.15)
        b_node    = node(b_pos,  "B",  C_B)
        bc_node   = node(bc_pos, "B̄", "#7f8c8d")
        ab_node   = node(ab_pos,   "A",  C_A)
        acb_node  = node(acb_pos,  "Ā", "#7f8c8d")
        abc_node  = node(abc_pos,  "A",  C_A)
        acbc_node = node(acbc_pos, "Ā", "#7f8c8d")

        # 分支线
        def branch(p1, p2, color=C_OMEGA):
            return Line(p1, p2, stroke_color=color, stroke_width=2.5,
                        buff=0.22)

        br_b   = branch(root_pos, b_pos,   C_B)
        br_bc  = branch(root_pos, bc_pos,  C_DIM)
        br_ab  = branch(b_pos,  ab_pos,   C_A)
        br_acb = branch(b_pos,  acb_pos,  C_DIM)
        br_abc = branch(bc_pos, abc_pos,  C_A)
        br_acbc= branch(bc_pos, acbc_pos, C_DIM)

        # 概率标签（放在枝干中点旁）
        def edge_label(p1, p2, text_str, color, side=UP):
            mid = (np.array(p1) + np.array(p2)) / 2
            lbl = Text(text_str, font=FONT, font_size=20, color=color
                       ).move_to(mid + side * 0.28)
            return lbl

        pb  = edge_label(root_pos, b_pos,  "P(B)=0.6",    C_B,    UP)
        pbc = edge_label(root_pos, bc_pos, "P(B̄)=0.4",   C_DIM,  DOWN)
        pab  = edge_label(b_pos, ab_pos,  "P(A|B)=0.5",  C_A,    UP)
        pacb = edge_label(b_pos, acb_pos, "P(Ā|B)=0.5",  C_DIM,  DOWN)
        pabc = edge_label(bc_pos, abc_pos, "P(A|B̄)=0.3", C_A,    UP)
        pacbc= edge_label(bc_pos, acbc_pos,"P(Ā|B̄)=0.7",C_DIM,  DOWN)

        # 依次出现
        self.play(FadeIn(root_node), run_time=0.3)
        self.play(Create(br_b),  FadeIn(b_node),  Write(pb),  run_time=0.5)
        self.play(Create(br_bc), FadeIn(bc_node), Write(pbc), run_time=0.4)
        self.play(
            Create(br_ab),  FadeIn(ab_node),  Write(pab),
            Create(br_acb), FadeIn(acb_node), Write(pacb),
            run_time=0.5
        )
        self.play(
            Create(br_abc),  FadeIn(abc_node),  Write(pabc),
            Create(br_acbc), FadeIn(acbc_node), Write(pacbc),
            run_time=0.4
        )
        self.wait(0.3)

        # ── 高亮路径 B → A，P(AB) = P(B)·P(A|B) ──
        br_b_hl  = br_b.copy().set_stroke(color=C_COND, width=5)
        br_ab_hl = br_ab.copy().set_stroke(color=C_COND, width=5)
        self.play(
            Create(br_b_hl), Create(br_ab_hl),
            b_node.animate.set_color(C_COND),
            ab_node.animate.set_color(C_COND),
            run_time=0.5
        )

        path_eq = MathTex(
            r"P(AB) = P(B) \cdot P(A \mid B) = 0.6 \times 0.5 = 0.3",
            font_size=30, color=C_COND
        ).move_to(DOWN * 4.5)
        self.play(Write(path_eq), run_time=0.7)
        self.wait(0.5)

        # 核心公式
        mult_formula = self._fbox(
            r"P(AB) = P(B) \cdot P(A \mid B) = P(A) \cdot P(B \mid A)",
            color=C_TREE, fs=28
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(mult_formula), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, root_node, b_node, bc_node, ab_node, acb_node,
            abc_node, acbc_node,
            br_b, br_bc, br_ab, br_acb, br_abc, br_acbc,
            pb, pbc, pab, pacb, pabc, pacbc,
            br_b_hl, br_ab_hl, path_eq, mult_formula
        )), run_time=0.5)

    # ================================================================
    #  Scene 4: 独立事件
    # ================================================================
    def scene_4_independence(self):
        title = self._title("独立事件", sub="A 的发生不受 B 影响",
                            mc=C_IND)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        # ── 对比展示：非独立 vs 独立 ──
        # 非独立（B发生后，A区域面积占比变了）
        non_title = Text("普通情况（非独立）", font=FONT,
                         font_size=26, color=GRAY_A).move_to(UP * 4.8)
        self.play(FadeIn(non_title), run_time=0.3)

        off = UP * 2.8
        omega, ca, cb, lω, la, lb = self._venn_base(offset=off)
        self.play(Create(omega), Write(lω), run_time=0.3)
        self.play(GrowFromCenter(ca), GrowFromCenter(cb),
                  Write(la), Write(lb), run_time=0.5)

        inter = self._inter_fill(ca, cb)
        self.play(FadeIn(inter), run_time=0.3)

        # 箭头 + 问题：B发生后，A的概率变了吗？
        q_arrow = Arrow(RIGHT * 3.2 + UP * 2.8, RIGHT * 1.5 + UP * 2.8,
                        buff=0.05, color=C_B, stroke_width=2)
        q_label = Text("B 发生后\nA 的概率变了", font=FONT,
                       font_size=22, color=C_B
                       ).next_to(q_arrow, RIGHT, buff=0.1)
        self.play(GrowArrow(q_arrow), FadeIn(q_label), run_time=0.4)

        # 用不等号表达非独立
        non_eq = MathTex(r"P(A \mid B) \neq P(A)", font_size=36,
                         color=C_A).move_to(UP * 1.2)
        self.play(Write(non_eq), run_time=0.5)
        self.wait(0.5)

        # ── 独立事件：韦恩图按比例铺满 ──
        self.play(FadeOut(VGroup(non_title, omega, ca, cb, lω, la, lb,
                                  inter, q_arrow, q_label, non_eq)),
                  run_time=0.4)

        ind_title = Text("独立事件", font=FONT, font_size=28,
                         color=C_IND).move_to(UP * 4.8)
        self.play(FadeIn(ind_title), run_time=0.3)

        # 独立示意：用等式说明
        ind_eq = MathTex(r"P(A \mid B) = P(A)", font_size=50,
                         color=C_IND).move_to(UP * 3.2)
        sub_eq = Text("B 发生与否，不影响 A 的概率", font=FONT,
                      font_size=26, color=GRAY_A).move_to(UP * 2.3)
        self.play(Write(ind_eq), run_time=0.6)
        self.play(FadeIn(sub_eq), run_time=0.4)

        # 等价定义
        equiv = self._fbox(r"P(AB) = P(A) \cdot P(B)",
                           color=C_IND, fs=46).move_to(UP * 1.0)
        self.play(FadeIn(equiv), run_time=0.6)
        self.wait(0.4)

        # 判定方法卡片
        judge = VGroup(
            Text("判定方法:", font=FONT, font_size=28, color=C_IND),
            Text("验证 P(AB) = P(A)·P(B) 是否成立",
                 font=FONT, font_size=26, color=WHITE),
            Text("若相等 → 独立；不等 → 不独立",
                 font=FONT, font_size=24, color=GRAY_A),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 0.8)

        bg_judge = RoundedRectangle(
            width=judge.width + 0.7, height=judge.height + 0.5,
            corner_radius=0.15, fill_color=C_CARD, fill_opacity=0.95,
            stroke_color=C_IND, stroke_width=2
        ).move_to(judge.get_center())
        judge_card = VGroup(bg_judge, judge)
        self.play(FadeIn(judge_card, shift=UP * 0.2), run_time=0.5)

        # 投硬币例子
        coin_eg = VGroup(
            Text("例: 两次独立投硬币", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"P(H_1 H_2) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}",
                    font_size=34, color=WHITE),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 3.2)
        self.play(FadeIn(coin_eg, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(title, ind_title, ind_eq, sub_eq,
                                  equiv, judge_card, coin_eg)),
                  run_time=0.5)

    # ================================================================
    #  Scene 5: 二项分布
    # ================================================================
    def scene_5_binomial(self):
        title = self._title("n 次独立重复试验",
                            sub="二项概率公式",
                            mc=C_BINOM)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        # ── 引入：3次投硬币，恰好2次正面 ──
        setup = Text("3 次投硬币，正面概率 p = 0.5", font=FONT,
                     font_size=30, color=WHITE).move_to(UP * 4.7)
        question = Text("恰好 2 次正面 的概率？", font=FONT,
                        font_size=34, color=C_BINOM).move_to(UP * 4.0)
        self.play(FadeIn(setup), run_time=0.4)
        self.play(Write(question), run_time=0.5)

        # ── 列举所有路径（HHT / HTH / THH）──
        path_title = Text("满足条件的路径:", font=FONT,
                          font_size=26, color=GRAY_A).move_to(UP * 2.9)
        self.play(FadeIn(path_title), run_time=0.3)

        paths = [
            ("H H T", r"p \cdot p \cdot (1-p)"),
            ("H T H", r"p \cdot (1-p) \cdot p"),
            ("T H H", r"(1-p) \cdot p \cdot p"),
        ]

        path_objs = VGroup()
        for i, (label, formula_str) in enumerate(paths):
            label_t = Text(label, font=FONT, font_size=30,
                           color=C_A if "H" in label[0] else "#7f8c8d")
            eq_sign = Text("→", font=FONT, font_size=26, color=C_OMEGA)
            formula_t = MathTex(formula_str, font_size=28, color=WHITE)
            row = VGroup(label_t, eq_sign, formula_t).arrange(RIGHT, buff=0.3)
            row.move_to(UP * (2.1 - i * 0.7))
            path_objs.add(row)

        for row in path_objs:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.3)

        # ── 每条路径概率相等 = p²(1-p) ──
        each = MathTex(r"\text{each} = p^2(1-p)",
                       font_size=32, color=C_BINOM).move_to(UP * 0.2)

        # 用 Text 替代 \text{} 内的中文
        each_cn = Text("每条路径概率 =", font=FONT,
                       font_size=26, color=C_BINOM).move_to(UP * 0.2 + LEFT * 1.2)
        each_fml = MathTex(r"p^2(1-p)", font_size=34, color=C_BINOM
                           ).next_to(each_cn, RIGHT, buff=0.2)
        each_row = VGroup(each_cn, each_fml)

        self.play(Write(each_row), run_time=0.5)

        # ── C(3,2) = 3 种组合 ──
        comb_text = VGroup(
            Text("共", font=FONT, font_size=30, color=WHITE),
            MathTex(r"C_3^2 = 3", font_size=38, color=C_HL),
            Text("种路径", font=FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.8)
        self.play(FadeIn(comb_text), run_time=0.4)

        # ── 二项公式推导 ──
        arrow_derive = Arrow(DOWN * 0.4, DOWN * 1.5,
                             buff=0, color=C_BINOM, stroke_width=2.5)
        self.play(GrowArrow(arrow_derive), run_time=0.3)

        binom_derive = MathTex(
            r"P(X=2) = C_3^2 \cdot p^2 \cdot (1-p)^1 = 3 \times 0.25 \times 0.5 = 0.375",
            font_size=27, color=WHITE
        ).move_to(DOWN * 2.2)
        self.play(Write(binom_derive), run_time=0.7)
        self.wait(0.4)

        # ── 一般公式 ──
        gen_formula = self._fbox(
            r"P(X=k) = C_n^k \cdot p^k \cdot (1-p)^{n-k}",
            color=C_BINOM, fs=36
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(gen_formula), run_time=0.6)
        self.wait(0.4)

        # 参数注解
        param_note = VGroup(
            Text("n : 独立重复次数", font=FONT, font_size=22, color=GRAY_A),
            Text("p : 每次成功概率", font=FONT, font_size=22, color=GRAY_A),
            Text("k : 恰好成功次数", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(DOWN * 5.4)
        self.play(FadeIn(param_note), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, setup, question, path_title, path_objs,
            each_row, comb_text, arrow_derive,
            binom_derive, gen_formula, param_note
        )), run_time=0.5)

    # ================================================================
    #  Scene 6: 全概率公式（简述）
    # ================================================================
    def scene_6_total_prob(self):
        title = self._title("全概率公式", sub="将样本空间划分后求 P(A)",
                            mc=C_TREE, ms=38)
        self.play(Write(title[0]), FadeIn(title[1]), run_time=0.5)

        off = UP * 1.5
        # Ω 矩形
        omega = RoundedRectangle(
            width=6.2, height=2.8, corner_radius=0.15,
            stroke_color=C_OMEGA, stroke_width=2,
            fill_color="#0d0d1a", fill_opacity=0.7
        ).move_to(off)
        lω = Text("Ω", font=FONT, font_size=22, color=C_OMEGA
                  ).next_to(omega, UR, buff=-0.5)
        self.play(Create(omega), Write(lω), run_time=0.4)

        # 三列分区 B₁, B₂, B₃
        colors_b = ["#2980b9", "#8e44ad", "#16a085"]
        widths   = [1.8, 2.0, 2.4]   # 各列宽度，总和 = 6.2
        labels_b = ["B₁", "B₂", "B₃"]
        labels_p = ["P(B₁)=0.3", "P(B₂)=0.4", "P(B₃)=0.3"]
        parts    = VGroup()

        x_cursor = -3.1
        rects_bi = []
        for w, col, lbl, plbl in zip(widths, colors_b, labels_b, labels_p):
            rect = Rectangle(
                width=w, height=2.8,
                fill_color=col, fill_opacity=0.30,
                stroke_color=col, stroke_width=1.5
            ).move_to(off + RIGHT * (x_cursor + w/2))
            t = Text(lbl, font=FONT, font_size=24, color=col
                     ).move_to(rect.get_center() + UP * 0.6)
            pt = Text(plbl, font=FONT, font_size=18, color=col
                      ).move_to(rect.get_center() + DOWN * 0.8)
            parts.add(VGroup(rect, t, pt))
            rects_bi.append(rect)
            x_cursor += w

        self.play(*[FadeIn(p, shift=UP * 0.2) for p in parts], run_time=0.5)
        self.wait(0.3)

        # A 圆（跨越三列）
        cir_a = Circle(radius=1.1, fill_color=C_A, fill_opacity=0.45,
                       stroke_color=C_A, stroke_width=2.5
                       ).move_to(off + RIGHT * 0.2)
        la_label = Text("A", font=FONT, font_size=26, color=C_A
                        ).move_to(cir_a.get_center())
        self.play(GrowFromCenter(cir_a), Write(la_label), run_time=0.5)

        # 三个交叉填充
        fills = VGroup(*[
            Intersection(cir_a.copy(), r.copy(),
                         fill_color=C_A, fill_opacity=0.80,
                         stroke_width=0)
            for r in rects_bi
        ])
        self.play(FadeIn(fills), run_time=0.4)
        self.wait(0.3)

        # 公式
        total_formula = self._fbox(
            r"P(A) = \sum_{i} P(B_i) \cdot P(A \mid B_i)",
            color=C_TREE, fs=34
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(total_formula), run_time=0.6)

        eg_total = MathTex(
            r"= 0.3 \times 0.8 + 0.4 \times 0.5 + 0.3 \times 0.3 = 0.52",
            font_size=30, color=GRAY_A
        ).move_to(DOWN * 2.7)
        self.play(Write(eg_total), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, omega, lω, parts, cir_a, la_label,
            fills, total_formula, eg_total
        )), run_time=0.5)

    # ================================================================
    #  Scene 7: 总结 & 片尾
    # ================================================================
    def scene_7_summary(self):
        sum_title = Text("本节核心公式", font=FONT, font_size=40,
                         color=C_HL).move_to(UP * 6.2)
        self.play(Write(sum_title), run_time=0.5)

        # 公式卡
        formulas = [
            ("条件概率",
             r"P(A \mid B) = \frac{P(AB)}{P(B)}",
             C_COND, UP * 4.8),
            ("乘法公式",
             r"P(AB) = P(B) \cdot P(A \mid B)",
             C_TREE, UP * 3.5),
            ("独立事件",
             r"P(AB) = P(A) \cdot P(B)",
             C_IND, UP * 2.2),
            ("二项分布",
             r"P(X=k) = C_n^k p^k (1-p)^{n-k}",
             C_BINOM, UP * 0.9),
            ("全概率",
             r"P(A) = \textstyle\sum P(B_i) P(A \mid B_i)",
             C_TREE, DOWN * 0.4),
        ]

        card_group = VGroup()
        for cn, tex, col, pos in formulas:
            lbl = Text(cn, font=FONT, font_size=20, color=col)
            fml = MathTex(tex, font_size=28, color=WHITE)
            row = VGroup(lbl, fml).arrange(RIGHT, buff=0.3)
            bg = RoundedRectangle(
                width=max(row.width + 0.7, 7.5),
                height=row.height + 0.45,
                corner_radius=0.12,
                fill_color=C_CARD, fill_opacity=0.94,
                stroke_color=col, stroke_width=2
            )
            row.move_to(bg.get_center())
            card = VGroup(bg, row).move_to(pos)
            card_group.add(card)

        for card in card_group:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.32)

        # 记忆口诀
        motto_bg = RoundedRectangle(
            width=7.8, height=1.1, corner_radius=0.2,
            fill_color="#0a0a1a", fill_opacity=0.95,
            stroke_color=C_HL, stroke_width=2
        ).move_to(DOWN * 1.9)
        motto = Text("「条件除交积·独立可相乘·重复用二项」",
                     font=FONT, font_size=23, color=C_HL
                     ).move_to(DOWN * 1.9)
        self.play(FadeIn(motto_bg), Write(motto), run_time=0.6)
        self.wait(0.8)

        # ── 片尾 ──
        self.play(FadeOut(VGroup(sum_title, card_group, motto_bg, motto)),
                  run_time=0.5)

        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=44, color=WHITE)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=32, color=C_OMEGA)
        VGroup(author_big, author_id).arrange(DOWN, buff=0.3).move_to(UP * 0.8)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，高考概率不失分！",
                      font=FONT, font_size=32, color=C_HL).move_to(DOWN * 0.8)
        fbox = SurroundingRectangle(follow, color=C_HL,
                                    buff=0.2, corner_radius=0.12)
        self.play(FadeIn(follow, scale=1.1), Create(fbox), run_time=0.6)

        # 小装饰：公式闪烁
        deco = MathTex(r"P(A \mid B) \xrightarrow{\text{indep.}} P(A)",
                       font_size=34, color=GRAY_A).move_to(DOWN * 2.4)
        self.play(Write(deco), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(self.author, author_id,
                                  follow, fbox, deco)), run_time=1.0)


# ================================================================
#  渲染命令:
#   预览: manim -pql cond_prob_animation.py CondProbAnimation
#   高清: manim -qh  cond_prob_animation.py CondProbAnimation
# ================================================================