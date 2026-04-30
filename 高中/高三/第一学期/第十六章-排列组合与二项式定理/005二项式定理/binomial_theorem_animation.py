"""
binomial_theorem_animation.py - 二项式定理 教学动画
高三数学第十六章：二项式定理 + 通项公式 + 杨辉三角 + 推论

manim -qh binomial_theorem_animation.py BinomialTheorem


格式: TikTok 竖屏 (1080×1920)，约 68 秒
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================== 全局配置 ========================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================== 颜色常量 ========================
BG_COLOR = "#1a1a2e"
C_HL     = "#f6c90e"   # 黄 - 高亮/答案
C_FMT    = "#4ecdc4"   # 青 - 公式框
C_A      = "#ff6b6b"   # 红 - a 项
C_B      = "#45b7d1"   # 蓝 - b 项
C_K      = "#96ceb4"   # 绿 - 指数/k
C_COEF   = "#c084fc"   # 紫 - 系数 C(n,k)
C_ORANGE = "#f4a261"
C_GRAY   = "#a0a0b0"
FONT_CN  = "PingFang SC"

# 杨辉三角布局常量
PASCAL_ROW_H  = 0.70
PASCAL_COL_W  = 0.82
PASCAL_CTR_Y  = 2.5   # 第0行 y 坐标

def pascal_pos(n, k):
    """返回杨辉三角第 n 行第 k 列的坐标（numpy array）"""
    x = (k - n / 2) * PASCAL_COL_W
    y = PASCAL_CTR_Y - n * PASCAL_ROW_H
    return np.array([x, y, 0])


def make_section_tag(text_str, color, width=5.0):
    """创建场景标题标签"""
    box = RoundedRectangle(
        width=width, height=0.72, corner_radius=0.18,
        color=color, fill_color=color, fill_opacity=0.22, stroke_width=2
    )
    label = Text(text_str, font=FONT_CN, font_size=34, color=color, weight=BOLD)
    return VGroup(box, label)


def make_formula_box(formula_str, color, width=7.5, fs=30):
    """创建公式高亮框"""
    box = RoundedRectangle(
        width=width, height=1.0, corner_radius=0.18,
        color=color, fill_color=color, fill_opacity=0.1, stroke_width=2
    )
    f = MathTex(formula_str, font_size=fs, color=color)
    return VGroup(box, f)


# ======================== 主场景 ========================
class BinomialTheorem(Scene):
    """二项式定理完整教学动画（约68秒）"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 全程作者栏
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.0)
        self.add(self.author_bar)

        self.scene1_hook()
        self.scene2_main_formula()
        self.scene3_general_term()
        self.scene4_pascal()
        self.scene5_corollaries()
        self.scene6_outro()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场钩子 (0~6s)
    # ─────────────────────────────────────────────────
    def scene1_hook(self):
        title = Text("(a+b)ⁿ 怎么展开？",
                     font=FONT_CN, font_size=40, color=C_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # (a+b)^2 展开
        f2 = MathTex(
            r"(a+b)^2 = a^2 + 2ab + b^2",
            font_size=30, color=WHITE
        ).move_to(UP * 4.8)
        self.play(Write(f2), run_time=0.8)

        # (a+b)^3 展开
        f3 = MathTex(
            r"(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
            font_size=28, color=WHITE
        ).move_to(UP * 3.5)
        self.play(Write(f3), run_time=0.9)

        # 规律提示 + 挑战
        pattern = Text("系数：1,2,1  /  1,3,3,1  → 有规律！",
                       font=FONT_CN, font_size=22, color=C_K
                       ).move_to(UP * 2.3)
        self.play(FadeIn(pattern, shift=UP * 0.2), run_time=0.5)

        challenge = Text("n=10 时，能快速展开吗？",
                         font=FONT_CN, font_size=26, color=C_ORANGE
                         ).move_to(UP * 1.2)
        self.play(FadeIn(challenge), run_time=0.4)
        self.wait(1.3)

        self.play(FadeOut(VGroup(title, f2, f3, pattern, challenge)), run_time=0.4)

    # ─────────────────────────────────────────────────
    # Scene 2: 主公式 (6~20s)
    # ─────────────────────────────────────────────────
    def scene2_main_formula(self):
        tag = make_section_tag("二项式定理", C_FMT, width=5.2)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 第一行：展开式
        intro = Text("展开式（逐项写出）：",
                     font=FONT_CN, font_size=22, color=C_GRAY
                     ).move_to(UP * 5.1)
        self.play(FadeIn(intro), run_time=0.3)

        # 逐项展开（分色标注）
        expand = MathTex(
            r"(a+b)^n = ",
            r"C(n,0)", r"a^n",
            r"+",
            r"C(n,1)", r"a^{n-1}b",
            r"+ \cdots +",
            r"C(n,n)", r"b^n",
            font_size=26
        ).move_to(UP * 4.0)

        # 分色
        expand[1].set_color(C_COEF)   # C(n,0)
        expand[2].set_color(C_A)      # a^n
        expand[4].set_color(C_COEF)   # C(n,1)
        expand[5].set_color(WHITE)    # a^{n-1}b
        expand[7].set_color(C_COEF)   # C(n,n)
        expand[8].set_color(C_B)      # b^n

        self.play(Write(expand), run_time=1.2)
        self.wait(0.4)

        # 高亮系数
        coef_label = Text("系数 C(n,k) — 紫色",
                          font=FONT_CN, font_size=20, color=C_COEF
                          ).move_to(UP * 2.9)
        self.play(
            Indicate(expand[1], color=C_COEF, scale_factor=1.2),
            Indicate(expand[4], color=C_COEF, scale_factor=1.2),
            Indicate(expand[7], color=C_COEF, scale_factor=1.2),
            run_time=0.6
        )
        self.play(FadeIn(coef_label), run_time=0.3)

        # a 幂次递减
        a_label = Text("a 的指数递减：n, n-1, ..., 0",
                       font=FONT_CN, font_size=20, color=C_A
                       ).move_to(UP * 2.1)
        self.play(
            expand[2].animate.set_color(C_A),
            FadeIn(a_label),
            run_time=0.5
        )

        # b 幂次递增
        b_label = Text("b 的指数递增：0, 1, ..., n",
                       font=FONT_CN, font_size=20, color=C_B
                       ).move_to(UP * 1.3)
        expand[5].set_color(C_B)
        self.play(FadeIn(b_label), run_time=0.4)
        self.wait(0.4)

        # 紧凑求和形式
        arrow = Text("↓  紧凑写法：",
                     font=FONT_CN, font_size=22, color=C_GRAY
                     ).move_to(UP * 0.3)
        self.play(FadeIn(arrow), run_time=0.3)

        sum_box, sum_f = make_formula_box(
            r"\sum_{k=0}^{n} C(n,k)\, a^{n-k} b^k",
            C_FMT, width=6.5, fs=32
        )
        sum_f.move_to(sum_box.get_center())
        sum_group = VGroup(sum_box, sum_f).move_to(DOWN * 0.7)
        self.play(FadeIn(sum_box), Write(sum_f), run_time=0.8)

        # 共 n+1 项
        n_terms = Text("展开共 n+1 项",
                       font=FONT_CN, font_size=24, color=C_HL
                       ).move_to(DOWN * 1.9)
        self.play(FadeIn(n_terms, shift=UP * 0.2), run_time=0.4)
        self.play(Indicate(n_terms, scale_factor=1.05), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            tag, intro, expand, coef_label, a_label, b_label,
            arrow, sum_group, n_terms
        )), run_time=0.45)

    # ─────────────────────────────────────────────────
    # Scene 3: 通项公式 (20~34s)
    # ─────────────────────────────────────────────────
    def scene3_general_term(self):
        tag = make_section_tag("通项公式", C_ORANGE, width=4.5)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 通项公式框
        gt_box, gt_f = make_formula_box(
            r"T_{k+1} = C(n,k) \cdot a^{n-k} \cdot b^k",
            C_HL, width=7.2, fs=32
        )
        gt_f.move_to(gt_box.get_center())
        gt_group = VGroup(gt_box, gt_f).move_to(UP * 4.8)
        self.play(FadeIn(gt_box), Write(gt_f), run_time=0.9)

        # 三组大括号：分别标注系数/a/b
        # 使用 Brace 对公式子部分标注
        brace_note = Text("k = 0, 1, 2, ..., n",
                          font=FONT_CN, font_size=22, color=C_K
                          ).move_to(UP * 3.7)
        self.play(FadeIn(brace_note), run_time=0.35)

        note_coef = VGroup(
            Text("①系数", font=FONT_CN, font_size=20, color=C_COEF),
            Text("C(n,k)", font=FONT_CN, font_size=18, color=C_COEF)
        ).arrange(DOWN, buff=0.05).move_to(UP * 3.0 + LEFT * 2.5)

        note_a = VGroup(
            Text("② a 的幂", font=FONT_CN, font_size=20, color=C_A),
            Text("n-k 次", font=FONT_CN, font_size=18, color=C_A)
        ).arrange(DOWN, buff=0.05).move_to(UP * 3.0)

        note_b = VGroup(
            Text("③ b 的幂", font=FONT_CN, font_size=20, color=C_B),
            Text("k 次", font=FONT_CN, font_size=18, color=C_B)
        ).arrange(DOWN, buff=0.05).move_to(UP * 3.0 + RIGHT * 2.5)

        self.play(
            LaggedStart(
                FadeIn(note_coef), FadeIn(note_a), FadeIn(note_b),
                lag_ratio=0.3
            ),
            run_time=0.9
        )
        self.wait(0.5)

        # 示例计算 (a+b)^5 第3项
        eg_title = Text("例：(a+b)⁵ 的第 3 项",
                        font=FONT_CN, font_size=24, color=WHITE
                        ).move_to(UP * 1.7)
        self.play(FadeIn(eg_title), run_time=0.35)

        # 第3项 → k=2（注意从k=0开始）
        k_note = Text("第 3 项 → k = 2（k 从 0 计）",
                      font=FONT_CN, font_size=20, color=C_K
                      ).move_to(UP * 0.9)
        self.play(FadeIn(k_note), run_time=0.35)

        calc1 = MathTex(
            r"T_3 = C(5,2) \cdot a^{5-2} \cdot b^2",
            font_size=30, color=WHITE
        ).move_to(UP * 0.0)
        self.play(Write(calc1), run_time=0.7)

        calc2 = MathTex(
            r"C(5,2) = \frac{5!}{2!\cdot 3!} = 10",
            font_size=28, color=C_COEF
        ).move_to(DOWN * 1.1)
        self.play(Write(calc2), run_time=0.7)

        # 结果高亮
        res_box = RoundedRectangle(
            width=5.5, height=1.0, corner_radius=0.2,
            color=C_HL, stroke_width=2.5,
            fill_color=C_HL, fill_opacity=0.12
        ).move_to(DOWN * 2.4)
        res_f = MathTex(r"T_3 = 10a^3b^2",
                        font_size=38, color=C_HL).move_to(DOWN * 2.4)
        self.play(FadeIn(res_box), Write(res_f), run_time=0.7)
        self.play(Flash(res_box, color=C_HL, flash_radius=0.6), run_time=0.5)
        self.wait(1.4)

        self.play(FadeOut(VGroup(
            tag, gt_group, brace_note, note_coef, note_a, note_b,
            eg_title, k_note, calc1, calc2, res_box, res_f
        )), run_time=0.45)

    # ─────────────────────────────────────────────────
    # Scene 4: 杨辉三角 (34~48s)
    # ─────────────────────────────────────────────────
    def scene4_pascal(self):
        tag = make_section_tag("杨辉三角 = 二项式系数", C_COEF, width=6.5)
        tag.move_to(UP * 6.5)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 构建杨辉三角
        from math import comb
        pascal_vals = [[comb(n, k) for k in range(n + 1)] for n in range(6)]

        # 行颜色
        row_colors = [C_GRAY, C_GRAY, C_GRAY, C_ORANGE, C_GRAY, C_COEF]

        all_cells = []
        for n, row in enumerate(pascal_vals):
            row_cells = []
            for k, val in enumerate(row):
                pos = pascal_pos(n, k)
                fs = 24 if val < 10 else 20
                cell = Text(str(val), font=FONT_CN, font_size=fs,
                            color=row_colors[n]).move_to(pos)
                row_cells.append(cell)
            all_cells.append(row_cells)

        # 行标签 n= 放在左侧
        row_labels = VGroup(*[
            Text(f"n={n}", font=FONT_CN, font_size=16, color=C_GRAY
                 ).move_to(pascal_pos(n, 0) + LEFT * 1.5)
            for n in range(6)
        ])

        # 逐行淡入
        for n, row_cells in enumerate(all_cells):
            self.play(
                LaggedStart(
                    *[FadeIn(c, shift=DOWN * 0.12) for c in row_cells],
                    lag_ratio=0.08
                ),
                FadeIn(row_labels[n]),
                run_time=0.4
            )

        self.wait(0.4)

        # 高亮 n=3 行 (橙色) → (a+b)³
        n3_note = Text("n=3 行  →  (a+b)³ 的系数",
                       font=FONT_CN, font_size=21, color=C_ORANGE
                       ).move_to(DOWN * 1.8)
        n3_rects = VGroup(*[
            SurroundingRectangle(all_cells[3][k], color=C_ORANGE, buff=0.1)
            for k in range(4)
        ])
        self.play(Create(n3_rects), FadeIn(n3_note), run_time=0.6)
        self.wait(0.6)

        # 高亮 n=5 行 (紫色) → (a+b)^5
        n5_note = Text("n=5 行  →  (a+b)⁵ 的系数",
                       font=FONT_CN, font_size=21, color=C_COEF
                       ).move_to(DOWN * 2.6)
        n5_rects = VGroup(*[
            SurroundingRectangle(all_cells[5][k], color=C_COEF, buff=0.1)
            for k in range(6)
        ])
        self.play(
            FadeOut(n3_rects),
            Create(n5_rects),
            FadeIn(n5_note),
            run_time=0.6
        )

        # 对称性高亮: C(5,2)=C(5,3)=10
        sym_note = Text("对称：C(5,2) = C(5,3) = 10",
                        font=FONT_CN, font_size=21, color=C_HL
                        ).move_to(DOWN * 3.5)
        self.play(
            Indicate(all_cells[5][2], color=C_HL, scale_factor=1.3),
            Indicate(all_cells[5][3], color=C_HL, scale_factor=1.3),
            FadeIn(sym_note),
            run_time=0.7
        )
        self.wait(1.4)

        # 清场
        all_tri = VGroup(*[c for row in all_cells for c in row])
        self.play(FadeOut(VGroup(
            tag, row_labels, all_tri, n3_note, n5_rects, n5_note, sym_note
        )), run_time=0.5)

    # ─────────────────────────────────────────────────
    # Scene 5: 重要推论 (48~60s)
    # ─────────────────────────────────────────────────
    def scene5_corollaries(self):
        tag = make_section_tag("妙用代入法", C_HL, width=4.8)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 基础公式
        base = MathTex(
            r"(a+b)^n = \sum_{k=0}^{n} C(n,k)\, a^{n-k} b^k",
            font_size=26, color=C_GRAY
        ).move_to(UP * 5.0)
        self.play(Write(base), run_time=0.7)

        # ── 推论1: a=b=1 ──
        sub1_lbl = Text("令 a=b=1：",
                        font=FONT_CN, font_size=24, color=C_K
                        ).move_to(UP * 3.9)
        self.play(FadeIn(sub1_lbl), run_time=0.3)

        res1_f = MathTex(
            r"2^n = C(n,0) + C(n,1) + \cdots + C(n,n)",
            font_size=26, color=WHITE
        ).move_to(UP * 3.1)
        self.play(Write(res1_f), run_time=0.7)

        box1 = RoundedRectangle(
            width=7.0, height=0.85, corner_radius=0.18,
            color=C_FMT, stroke_width=2, fill_color=C_FMT, fill_opacity=0.1
        ).move_to(UP * 2.1)
        res1_compact = MathTex(
            r"\sum_{k=0}^{n} C(n,k) = 2^n",
            font_size=32, color=C_FMT
        ).move_to(UP * 2.1)
        self.play(FadeIn(box1), Write(res1_compact), run_time=0.6)
        self.wait(0.5)

        # ── 推论2: a=1, b=-1 ──
        sub2_lbl = Text("令 a=1, b=−1：",
                        font=FONT_CN, font_size=24, color=C_A
                        ).move_to(UP * 0.9)
        self.play(FadeIn(sub2_lbl), run_time=0.3)

        res2_f = MathTex(
            r"0 = C(n,0) - C(n,1) + C(n,2) - \cdots",
            font_size=24, color=WHITE
        ).move_to(UP * 0.0)
        self.play(Write(res2_f), run_time=0.7)

        # 奇偶分离
        sep_note = Text("→ 偶数项之和 = 奇数项之和",
                        font=FONT_CN, font_size=22, color=C_A
                        ).move_to(DOWN * 0.9)
        self.play(FadeIn(sep_note), run_time=0.4)

        box2 = RoundedRectangle(
            width=7.0, height=0.85, corner_radius=0.18,
            color=C_HL, stroke_width=2, fill_color=C_HL, fill_opacity=0.1
        ).move_to(DOWN * 2.0)
        res2_compact = MathTex(
            r"C(n,0)+C(n,2)+\cdots = C(n,1)+C(n,3)+\cdots = 2^{n-1}",
            font_size=22, color=C_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(box2), Write(res2_compact), run_time=0.8)
        self.play(Indicate(res2_compact, scale_factor=1.03), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            tag, base, sub1_lbl, res1_f, box1, res1_compact,
            sub2_lbl, res2_f, sep_note, box2, res2_compact
        )), run_time=0.5)

    # ─────────────────────────────────────────────────
    # Scene 6: 片尾 (60~68s)
    # ─────────────────────────────────────────────────
    def scene6_outro(self):
        # 公式总结三行
        summary = VGroup(
            MathTex(r"(a+b)^n = \sum C(n,k)a^{n-k}b^k",
                    font_size=26, color=C_FMT),
            MathTex(r"T_{k+1} = C(n,k)a^{n-k}b^k",
                    font_size=26, color=C_HL),
            MathTex(r"\sum C(n,k) = 2^n",
                    font_size=26, color=C_COEF),
        ).arrange(DOWN, buff=0.55).move_to(UP * 3.5)

        for f in summary:
            self.play(FadeIn(f, shift=LEFT * 0.2), run_time=0.35)

        self.wait(0.3)

        # 作者信息
        author_big = Text("上海初高中数学直通车",
                          font=FONT_CN, font_size=40, color=WHITE
                          ).move_to(DOWN * 1.5)
        author_id  = Text("@emptyandcalm",
                          font=FONT_CN, font_size=28, color=C_GRAY
                          ).move_to(DOWN * 2.5)
        cta = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=28, color=C_HL
                   ).move_to(DOWN * 3.7)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(cta, scale=1.08), run_time=0.5)

        # 装饰彩点
        dots = VGroup(*[
            Dot(np.array([np.cos(i * 2 * np.pi / 6) * 1.8,
                           -3.7 + np.sin(i * 2 * np.pi / 6) * 0.45, 0]),
                radius=0.1,
                color=[C_A, C_B, C_K, C_COEF, C_HL, C_FMT][i],
                fill_opacity=0.9)
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Rotate(dots, angle=2 * np.pi / 3,
                         about_point=np.array([0, -3.7, 0]),
                         run_time=1.0))
        self.wait(0.8)
        self.play(FadeOut(VGroup(summary, author_big, author_id, cta, dots)),
                  run_time=0.7)