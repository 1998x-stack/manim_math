"""
binom_coef_properties_animation.py - 二项式系数的性质 教学动画
高三数学第十六章：5大性质——对称/递推/系数和/奇偶和/最大系数

manim -qh  binom_coef_properties_animation.py BinomCoefProperties  # 高质量

格式: TikTok 竖屏 (1080×1920)，约 70 秒
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from math import comb

# ======================== 全局配置 ========================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================== 颜色常量 ========================
BG_COLOR = "#1a1a2e"
C_HL     = "#f6c90e"   # 黄 - 高亮 / 答案
C_SYM    = "#45b7d1"   # 蓝 - 对称性
C_REC    = "#96ceb4"   # 绿 - 递推性
C_SUM    = "#c084fc"   # 紫 - 系数和
C_ODD    = "#ff6b6b"   # 红 - 奇偶和
C_MAX    = "#f4a261"   # 橙 - 最大系数
C_GRAY   = "#a0a0b0"
C_FMT    = "#4ecdc4"   # 青 - 公式框
FONT_CN  = "Noto Sans CJK SC"

# ======================== 杨辉三角布局 ========================
PASCAL_ROW_H = 0.70
PASCAL_COL_W = 0.82
PASCAL_CTR_Y = 3.5   # 第0行 y 坐标（6行时，第5行在 y=0.0）

def pascal_pos(n, k):
    """返回杨辉三角第 n 行第 k 列中心坐标"""
    x = (k - n / 2) * PASCAL_COL_W
    y = PASCAL_CTR_Y - n * PASCAL_ROW_H
    return np.array([x, y, 0])

PASCAL_VALS = [[comb(n, k) for k in range(n + 1)] for n in range(7)]

# ======================== 辅助函数 ========================
def make_tag(text_str, color, width=5.5):
    """圆角背景标签"""
    box = RoundedRectangle(
        width=width, height=0.72, corner_radius=0.18,
        color=color, fill_color=color, fill_opacity=0.22, stroke_width=2
    )
    lbl = Text(text_str, font=FONT_CN, font_size=32, color=color, weight=BOLD)
    lbl.move_to(box.get_center())
    return VGroup(box, lbl)


def make_fbox(formula_str, color=C_FMT, width=7.2, fs=28):
    """公式高亮框"""
    box = RoundedRectangle(
        width=width, height=0.95, corner_radius=0.18,
        color=color, fill_color=color, fill_opacity=0.10, stroke_width=2
    )
    f = MathTex(formula_str, font_size=fs, color=color)
    f.move_to(box.get_center())
    return VGroup(box, f)


def build_pascal(n_rows=6, row_colors=None, font_sizes=None):
    """
    构建 n_rows 行杨辉三角（Text 对象）。
    row_colors: list of colors per row (默认 C_GRAY)
    返回: list of list of Text
    """
    if row_colors is None:
        row_colors = [C_GRAY] * n_rows
    cells = []
    for n in range(n_rows):
        row = []
        for k in range(n + 1):
            val = PASCAL_VALS[n][k]
            fs = 22 if val < 10 else 18
            c = Text(str(val), font=FONT_CN, font_size=fs,
                     color=row_colors[n]).move_to(pascal_pos(n, k))
            row.append(c)
        cells.append(row)
    return cells


# ======================== 主场景 ========================
class BinomCoefProperties(Scene):
    """二项式系数5大性质 完整教学动画（约70秒）"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=C_GRAY
        ).move_to(UP * 7.0)
        self.add(self.author_bar)

        self.scene1_hook()
        self.scene2_symmetry()
        self.scene3_recurrence()
        self.scene4_sum()
        self.scene5_oddeven_max()
        self.scene6_outro()

    # ─────────────────────────────────────────────────
    # Scene 1: 开场 (0~6s)
    # ─────────────────────────────────────────────────
    def scene1_hook(self):
        title = Text("二项式系数 5 大性质",
                     font=FONT_CN, font_size=38, color=C_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 5个性质 bullet
        props = [
            ("① 对称性",  "C(n,k) = C(n,n-k)",        C_SYM),
            ("② 递推性",  "C(n,k) = C(n-1,k)+C(n-1,k-1)", C_REC),
            ("③ 系数和",  "∑C(n,k) = 2ⁿ",              C_SUM),
            ("④ 奇偶和",  "各 = 2^(n-1)",              C_ODD),
            ("⑤ 最大系数", "中间项最大",                C_MAX),
        ]
        ys = [4.9, 3.95, 3.0, 2.05, 1.1]
        bullets = VGroup()
        for (label, desc, col), y in zip(props, ys):
            lt = Text(label, font=FONT_CN, font_size=22, color=col, weight=BOLD
                      ).move_to(UP * y + LEFT * 1.8)
            dt = Text(desc,  font=FONT_CN, font_size=19, color=C_GRAY
                      ).move_to(UP * y + RIGHT * 1.0)
            row = VGroup(lt, dt)
            bullets.add(row)
            self.play(FadeIn(row, shift=LEFT * 0.3), run_time=0.35)

        self.wait(0.8)
        self.play(FadeOut(VGroup(title, bullets)), run_time=0.4)

    # ─────────────────────────────────────────────────
    # Scene 2: 对称性 (6~18s)
    # ─────────────────────────────────────────────────
    def scene2_symmetry(self):
        tag = make_tag("① 对称性", C_SYM, width=4.5)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 6行杨辉三角
        n_rows = 6
        row_colors = [C_GRAY] * n_rows
        cells = build_pascal(n_rows, row_colors)

        # 逐行淡入
        for n, row in enumerate(cells):
            self.play(
                LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in row],
                            lag_ratio=0.07),
                run_time=0.35
            )

        self.wait(0.4)

        # 对称轴：从 y=PASCAL_CTR_Y 到 y=0
        sym_line = DashedLine(
            start=np.array([0, PASCAL_CTR_Y + 0.2, 0]),
            end  =np.array([0, PASCAL_CTR_Y - 5 * PASCAL_ROW_H - 0.2, 0]),
            color=C_SYM, stroke_width=2, dash_length=0.15
        )
        sym_text = Text("对称轴", font=FONT_CN, font_size=18, color=C_SYM
                        ).move_to(np.array([0.6, PASCAL_CTR_Y + 0.35, 0]))
        self.play(Create(sym_line), FadeIn(sym_text), run_time=0.7)

        # 高亮第5行对称对 C(5,1)=C(5,4)=5 (蓝) & C(5,2)=C(5,3)=10 (黄)
        hl_rects = VGroup(
            SurroundingRectangle(cells[5][1], color=C_SYM, buff=0.08),
            SurroundingRectangle(cells[5][4], color=C_SYM, buff=0.08),
        )
        hl_rects2 = VGroup(
            SurroundingRectangle(cells[5][2], color=C_HL, buff=0.08),
            SurroundingRectangle(cells[5][3], color=C_HL, buff=0.08),
        )
        self.play(Create(hl_rects), run_time=0.5)
        self.play(Create(hl_rects2), run_time=0.4)

        eq1 = Text("C(5,1) = C(5,4) = 5",
                   font=FONT_CN, font_size=20, color=C_SYM
                   ).move_to(DOWN * 1.3)
        eq2 = Text("C(5,2) = C(5,3) = 10",
                   font=FONT_CN, font_size=20, color=C_HL
                   ).move_to(DOWN * 2.0)
        self.play(FadeIn(eq1), FadeIn(eq2), run_time=0.5)
        self.wait(0.4)

        # 主公式
        fb = make_fbox(r"C(n,k) = C(n,\, n-k)", C_SYM, width=6.0)
        fb.move_to(DOWN * 3.1)
        self.play(FadeIn(fb[0]), Write(fb[1]), run_time=0.7)

        # 直觉说明
        intuition = Text("选 k 个 ≡ 排除 n-k 个",
                         font=FONT_CN, font_size=20, color=C_GRAY
                         ).move_to(DOWN * 4.2)
        self.play(FadeIn(intuition), run_time=0.4)
        self.wait(1.3)

        # 存储三角形供 Scene 3 复用
        self._pascal_cells   = cells
        self._pascal_tri_grp = VGroup(*[c for row in cells for c in row])

        self.play(FadeOut(VGroup(
            tag, sym_line, sym_text, hl_rects, hl_rects2,
            eq1, eq2, fb, intuition
        )), run_time=0.4)

    # ─────────────────────────────────────────────────
    # Scene 3: 递推性 (18~30s)
    # ─────────────────────────────────────────────────
    def scene3_recurrence(self):
        # 三角形已在画面上
        cells = self._pascal_cells

        tag = make_tag("② 递推性", C_REC, width=4.5)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 暗化整个三角，只保留关键节点
        full = VGroup(*[c for row in cells for c in row])
        self.play(full.animate.set_opacity(0.25), run_time=0.4)

        # 高亮 C(4,1)=4, C(4,2)=6, C(5,2)=10
        cells[4][1].set_opacity(1).set_color(C_REC)
        cells[4][2].set_opacity(1).set_color(C_REC)
        cells[5][2].set_opacity(1).set_color(C_HL)
        self.play(
            cells[4][1].animate.set_opacity(1),
            cells[4][2].animate.set_opacity(1),
            cells[5][2].animate.set_opacity(1),
            run_time=0.4
        )

        # 高亮框
        box41 = SurroundingRectangle(cells[4][1], color=C_REC, buff=0.1)
        box42 = SurroundingRectangle(cells[4][2], color=C_REC, buff=0.1)
        box52 = SurroundingRectangle(cells[5][2], color=C_HL,  buff=0.1)
        self.play(Create(box41), Create(box42), Create(box52), run_time=0.5)

        # 箭头 C(4,1)→C(5,2) 和 C(4,2)→C(5,2)
        arr1 = Arrow(
            start=pascal_pos(4, 1) + DOWN * 0.25,
            end  =pascal_pos(5, 2) + UP   * 0.25,
            color=C_REC, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )
        arr2 = Arrow(
            start=pascal_pos(4, 2) + DOWN * 0.25,
            end  =pascal_pos(5, 2) + UP   * 0.25,
            color=C_REC, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )
        self.play(Create(arr1), Create(arr2), run_time=0.6)

        # 计算展示
        calc = VGroup(
            Text("C(4,1)", font=FONT_CN, font_size=22, color=C_REC),
            Text("+", font=FONT_CN, font_size=22, color=WHITE),
            Text("C(4,2)", font=FONT_CN, font_size=22, color=C_REC),
            Text("=", font=FONT_CN, font_size=22, color=WHITE),
            Text("C(5,2)", font=FONT_CN, font_size=22, color=C_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.5)
        sub_calc = MathTex(r"4 + 6 = 10",
                           font_size=28, color=WHITE).move_to(DOWN * 2.3)
        self.play(FadeIn(calc), run_time=0.5)
        self.play(Write(sub_calc), run_time=0.5)
        self.wait(0.4)

        # 通用公式框
        fb = make_fbox(r"C(n,k) = C(n-1,k) + C(n-1,k-1)", C_REC, width=7.5, fs=26)
        fb.move_to(DOWN * 3.5)
        self.play(FadeIn(fb[0]), Write(fb[1]), run_time=0.7)

        # 直觉：k项中"包含第n个"和"不含第n个"
        hint = Text("含第n个：C(n-1,k-1)  不含：C(n-1,k)",
                    font=FONT_CN, font_size=19, color=C_GRAY
                    ).move_to(DOWN * 4.6)
        self.play(FadeIn(hint), run_time=0.35)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            tag, self._pascal_tri_grp,
            box41, box42, box52, arr1, arr2,
            calc, sub_calc, fb, hint
        )), run_time=0.4)

    # ─────────────────────────────────────────────────
    # Scene 4: 系数和 = 2^n (30~43s)
    # ─────────────────────────────────────────────────
    def scene4_sum(self):
        tag = make_tag("③ 系数和 = 2ⁿ", C_SUM, width=5.2)
        tag.move_to(UP * 6.1)
        self.play(FadeIn(tag[0]), Write(tag[1]), run_time=0.5)

        # 基础：(1+x)^n 展开
        base = MathTex(
            r"(1+x)^n = \sum_{k=0}^{n} C(n,k)\, x^k",
            font_size=28, color=C_GRAY
        ).move_to(UP * 5.0)
        self.play(Write(base), run_time=0.7)

        # 代入 x=1
        sub_lbl = Text("令 x = 1：",
                       font=FONT_CN, font_size=24, color=C_SUM
                       ).move_to(UP * 3.9)
        self.play(FadeIn(sub_lbl), run_time=0.35)

        deriv = MathTex(
            r"(1+1)^n = C(n,0) + C(n,1) + \cdots + C(n,n)",
            font_size=24, color=WHITE
        ).move_to(UP * 3.0)
        self.play(Write(deriv), run_time=0.7)

        # 公式框
        fb = make_fbox(r"\sum_{k=0}^{n} C(n,k) = 2^n", C_SUM, width=6.0, fs=32)
        fb.move_to(UP * 1.8)
        self.play(FadeIn(fb[0]), Write(fb[1]), run_time=0.7)
        self.play(Flash(fb[0], color=C_SUM, flash_radius=0.55), run_time=0.4)

        # 具体例子 n=4
        sep = Line(start=LEFT * 3.5, end=RIGHT * 3.5,
                   color=C_GRAY, stroke_width=1.2
                   ).move_to(UP * 0.8)
        self.play(Create(sep), run_time=0.3)

        eg_title = Text("例：n = 4",
                        font=FONT_CN, font_size=22, color=C_GRAY
                        ).move_to(UP * 0.2)
        self.play(FadeIn(eg_title), run_time=0.3)

        # n=4 行方块（显示 1 4 6 4 1）
        row4_vals = PASCAL_VALS[4]   # [1, 4, 6, 4, 1]
        row4_cells = VGroup()
        xs = [i * 1.1 - 2.2 for i in range(5)]
        for i, (val, x) in enumerate(zip(row4_vals, xs)):
            box = RoundedRectangle(
                width=0.72, height=0.55, corner_radius=0.1,
                color=C_SUM, fill_color=C_SUM, fill_opacity=0.25, stroke_width=1.5
            ).move_to(np.array([x, -0.7, 0]))
            num = Text(str(val), font=FONT_CN, font_size=22, color=WHITE
                       ).move_to(np.array([x, -0.7, 0]))
            row4_cells.add(VGroup(box, num))

        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in row4_cells], lag_ratio=0.12),
            run_time=0.6
        )

        sum_eq = MathTex(r"1+4+6+4+1 = 16 = 2^4",
                         font_size=28, color=C_HL).move_to(DOWN * 1.8)
        self.play(Write(sum_eq), run_time=0.7)

        # 直觉：每个元素选/不选
        intuit = Text("每个元素只有「选」或「不选」两种状态",
                      font=FONT_CN, font_size=19, color=C_GRAY
                      ).move_to(DOWN * 2.9)
        intuit2 = Text("→ 共 2ⁿ 种组合",
                       font=FONT_CN, font_size=21, color=C_SUM
                       ).move_to(DOWN * 3.7)
        self.play(FadeIn(intuit), run_time=0.35)
        self.play(FadeIn(intuit2), run_time=0.35)
        self.wait(1.3)

        self.play(FadeOut(VGroup(
            tag, base, sub_lbl, deriv, fb, sep,
            eg_title, row4_cells, sum_eq, intuit, intuit2
        )), run_time=0.45)

    # ─────────────────────────────────────────────────
    # Scene 5: 奇偶和 + 最大系数 (43~58s)
    # ─────────────────────────────────────────────────
    def scene5_oddeven_max(self):
        # ── Part A: 奇偶和 ──
        tag_a = make_tag("④ 奇偶项和 = 2^(n-1)", C_ODD, width=6.0)
        tag_a.move_to(UP * 6.1)
        self.play(FadeIn(tag_a[0]), Write(tag_a[1]), run_time=0.5)

        sub_lbl = Text("令 x = -1 代入 (1+x)ⁿ：",
                       font=FONT_CN, font_size=22, color=C_ODD
                       ).move_to(UP * 5.0)
        self.play(FadeIn(sub_lbl), run_time=0.35)

        zero_eq = MathTex(
            r"0 = C(n,0) - C(n,1) + C(n,2) - \cdots",
            font_size=25, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(zero_eq), run_time=0.7)

        # 奇偶分离图示
        even_row = VGroup(
            Text("偶项：C(n,0)+C(n,2)+…", font=FONT_CN, font_size=20, color=C_SUM),
            MathTex(r"= 2^{n-1}", font_size=24, color=C_HL)
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.8)
        odd_row = VGroup(
            Text("奇项：C(n,1)+C(n,3)+…", font=FONT_CN, font_size=20, color=C_ODD),
            MathTex(r"= 2^{n-1}", font_size=24, color=C_HL)
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.0)
        self.play(FadeIn(even_row), run_time=0.4)
        self.play(FadeIn(odd_row),  run_time=0.4)

        fb_odd = make_fbox(
            r"C(n,0)+C(n,2)+\cdots = C(n,1)+C(n,3)+\cdots = 2^{n-1}",
            C_ODD, width=7.5, fs=20
        )
        fb_odd.move_to(UP * 0.8)
        self.play(FadeIn(fb_odd[0]), Write(fb_odd[1]), run_time=0.7)
        self.wait(0.7)

        # 清除 Part A，进入 Part B
        self.play(FadeOut(VGroup(
            tag_a, sub_lbl, zero_eq, even_row, odd_row, fb_odd
        )), run_time=0.4)

        # ── Part B: 最大系数 ──
        tag_b = make_tag("⑤ 最大系数在中间", C_MAX, width=5.8)
        tag_b.move_to(UP * 6.1)
        self.play(FadeIn(tag_b[0]), Write(tag_b[1]), run_time=0.5)

        # 展示 n=6 行（7个数）水平排列，高亮 C(6,3)=20
        n6_vals = PASCAL_VALS[6]   # [1,6,15,20,15,6,1]
        n6_width = 0.82
        n6_xs = [(i - 3) * n6_width for i in range(7)]
        n6_cells = VGroup()
        for i, (val, x) in enumerate(zip(n6_vals, n6_xs)):
            is_max = (i == 3)
            col = C_MAX if is_max else C_GRAY
            bg_col = C_MAX if is_max else "#2a2a4a"
            box = RoundedRectangle(
                width=0.68, height=0.58, corner_radius=0.1,
                color=col, fill_color=bg_col, fill_opacity=0.85 if is_max else 0.4,
                stroke_width=2 if is_max else 1.2
            ).move_to(np.array([x, 4.8, 0]))
            num = Text(str(val), font=FONT_CN, font_size=19,
                       color=WHITE if is_max else C_GRAY,
                       weight=BOLD if is_max else NORMAL
                       ).move_to(np.array([x, 4.8, 0]))
            n6_cells.add(VGroup(box, num))

        n6_label = Text("n=6 行：", font=FONT_CN, font_size=20, color=C_GRAY
                        ).move_to(UP * 4.8 + LEFT * 4.2)
        self.play(FadeIn(n6_label), run_time=0.3)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in n6_cells], lag_ratio=0.1),
            run_time=0.7
        )

        # 指向中间最大值
        max_arrow = Arrow(
            start=np.array([0, 5.6, 0]),
            end  =np.array([0, 5.15, 0]),
            color=C_MAX, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25
        )
        max_lbl = Text("最大值 20", font=FONT_CN, font_size=20, color=C_MAX
                       ).move_to(np.array([0, 5.85, 0]))
        self.play(FadeIn(max_lbl), Create(max_arrow), run_time=0.5)

        # n 偶数结论
        even_rule = VGroup(
            Text("n 为偶数：", font=FONT_CN, font_size=21, color=C_MAX),
            Text("中间项 C(n, n/2) 最大",
                 font=FONT_CN, font_size=21, color=WHITE)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.5)
        self.play(FadeIn(even_rule), run_time=0.4)

        # n=5 行 (奇数) 展示两个最大中间项
        n5_vals = PASCAL_VALS[5]   # [1,5,10,10,5,1]
        n5_xs = [(i - 2.5) * n6_width for i in range(6)]
        n5_cells = VGroup()
        for i, (val, x) in enumerate(zip(n5_vals, n5_xs)):
            is_max = (i in [2, 3])
            col = C_HL if is_max else C_GRAY
            bg_col = "#2d2d4a" if is_max else "#1f1f35"
            box = RoundedRectangle(
                width=0.68, height=0.58, corner_radius=0.1,
                color=col, fill_color=bg_col, fill_opacity=0.9 if is_max else 0.4,
                stroke_width=2 if is_max else 1.2
            ).move_to(np.array([x, 2.5, 0]))
            num = Text(str(val), font=FONT_CN, font_size=19,
                       color=col, weight=BOLD if is_max else NORMAL
                       ).move_to(np.array([x, 2.5, 0]))
            n5_cells.add(VGroup(box, num))

        n5_label = Text("n=5 行：", font=FONT_CN, font_size=20, color=C_GRAY
                        ).move_to(UP * 2.5 + LEFT * 4.0)
        self.play(FadeIn(n5_label), run_time=0.3)
        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in n5_cells], lag_ratio=0.1),
            run_time=0.6
        )

        # n 奇数结论
        odd_rule = VGroup(
            Text("n 为奇数：", font=FONT_CN, font_size=21, color=C_HL),
            Text("中间两项 C(n, ⌊n/2⌋) 相等且最大",
                 font=FONT_CN, font_size=21, color=WHITE)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.4)
        self.play(FadeIn(odd_rule), run_time=0.4)
        self.wait(1.3)

        self.play(FadeOut(VGroup(
            tag_b, n6_label, n6_cells, max_arrow, max_lbl,
            even_rule, n5_label, n5_cells, odd_rule
        )), run_time=0.45)

    # ─────────────────────────────────────────────────
    # Scene 6: 速查总结 + 片尾 (58~70s)
    # ─────────────────────────────────────────────────
    def scene6_outro(self):
        sum_title = Text("5 大性质速查",
                         font=FONT_CN, font_size=38, color=C_HL
                         ).move_to(UP * 6.2)
        self.play(Write(sum_title), run_time=0.5)

        # 5张卡片
        cards_data = [
            ("① 对称",   r"C(n,k) = C(n,n-k)",                         C_SYM, UP * 4.9),
            ("② 递推",   r"C(n,k) = C(n-1,k)+C(n-1,k-1)",             C_REC, UP * 3.4),
            ("③ 系数和", r"\sum C(n,k) = 2^n",                          C_SUM, UP * 1.9),
            ("④ 奇偶和", r"C_{\text{偶}} = C_{\text{奇}} = 2^{n-1}",  C_ODD, UP * 0.4),
            ("⑤ 最大",   r"C\!\left(n,\left\lfloor\tfrac{n}{2}\right\rfloor\right)",
             C_MAX, DOWN * 1.1),
        ]

        # Card ④ 用纯文本避免中文混入 MathTex
        card_group = VGroup()
        for i, (label, fmla, col, pos) in enumerate(cards_data):
            box = RoundedRectangle(
                width=7.5, height=1.2, corner_radius=0.2,
                color=col, fill_color=col, fill_opacity=0.10, stroke_width=1.8
            ).move_to(pos)
            lbl_t = Text(label, font=FONT_CN, font_size=22, color=col,
                         weight=BOLD).move_to(pos + LEFT * 2.3)
            # Card ④ 特殊处理：纯文字代替 MathTex
            if i == 3:
                fmla_obj = Text("偶项和 = 奇项和 = 2^(n-1)",
                                font=FONT_CN, font_size=19, color=WHITE
                                ).move_to(pos + RIGHT * 1.0)
            else:
                fmla_obj = MathTex(fmla, font_size=22, color=WHITE
                                   ).move_to(pos + RIGHT * 1.0)
            card = VGroup(box, lbl_t, fmla_obj)
            card_group.add(card)
            self.play(FadeIn(card, shift=LEFT * 0.4), run_time=0.38)

        self.wait(0.5)

        # 作者信息 + CTA
        author_big = Text("上海初高中数学直通车",
                          font=FONT_CN, font_size=36, color=WHITE
                          ).move_to(DOWN * 3.0)
        author_id  = Text("@emptyandcalm",
                          font=FONT_CN, font_size=26, color=C_GRAY
                          ).move_to(DOWN * 3.9)
        cta = Text("关注我，获得更多数学技巧！",
                   font=FONT_CN, font_size=26, color=C_HL
                   ).move_to(DOWN * 4.8)

        self.play(FadeIn(author_big, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.35)
        self.play(FadeIn(cta, scale=1.06), run_time=0.45)

        # 彩色装饰点旋转
        sparkle_colors = [C_SYM, C_REC, C_SUM, C_ODD, C_MAX, C_HL]
        dots = VGroup(*[
            Dot(
                np.array([np.cos(i * 2 * np.pi / 6) * 1.6,
                           -4.8 + np.sin(i * 2 * np.pi / 6) * 0.4, 0]),
                radius=0.11, color=sparkle_colors[i], fill_opacity=0.9
            )
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Rotate(dots, angle=PI,
                         about_point=np.array([0, -4.8, 0]),
                         run_time=1.2))
        self.wait(0.8)

        self.play(FadeOut(VGroup(
            sum_title, card_group, author_big, author_id, cta, dots
        )), run_time=0.7)