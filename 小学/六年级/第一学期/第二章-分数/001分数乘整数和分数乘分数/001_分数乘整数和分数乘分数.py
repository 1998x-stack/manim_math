"""
001_分数乘整数和分数乘分数.py — 分数乘整数和分数乘分数 教学动画

知识点: 分数乘整数、分数乘分数、算理、约分
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 算理理解: 求一个数的几分之几是多少
  3. 分数乘整数: 3/4 × 2
  4. 分数乘分数规则: a/b × c/d = (a×c)/(b×d)
  5. 例题1: 2/3 × 3/4 (先约分)
  6. 例题2: 3/5 × 5/6 (交叉约分)
  7. 应用题
  8. 总结
  9. 片尾
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# TeX template with cancel package
myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{cancel}")

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_FRAC_A = "#3b82f6"      # 蓝色 第一个分数
COLOR_FRAC_B = "#f59e0b"      # 橙色 第二个分数
COLOR_RESULT = "#22c55e"      # 绿色 结果
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_ACCENT = "#a78bfa"      # 紫色强调
COLOR_SUB = "#ef4444"         # 红色
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_NUMERATOR = "#f472b6"   # 粉色 分子
COLOR_DENOMINATOR = "#38bdf8" # 天蓝色 分母
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionMultiplicationLesson(Scene):
    """
    分数乘整数和分数乘分数教学动画
    场景顺序:
      1. 开场钩子
      2. 算理: 求一个数的几分之几
      3. 分数乘整数 (3/4 × 2)
      4. 分数乘分数规则
      5. 例题1: 2/3 × 3/4 (先约分)
      6. 例题2: 3/5 × 5/6 (交叉约分)
      7. 应用题
      8. 总结公式框
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_rationale()
        self.scene_3_fraction_times_int()
        self.scene_4_fraction_rule()
        self.scene_5_example_1()
        self.scene_6_example_2_cross_cancel()
        self.scene_7_word_problem()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 分数乘法，你真的会吗？"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook1 = Text(
            "分数乘分数",
            font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "你真的会算吗？",
            font=FONT, font_size=38, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)

        # 预览算式
        preview = MathTex(
            r"\frac{2}{3}", r"\times", r"\frac{3}{4}", r"= \ ?",
            font_size=80
        ).move_to(UP * 2.2)
        preview[0].set_color(COLOR_FRAC_A)
        preview[2].set_color(COLOR_FRAC_B)
        preview[3].set_color(COLOR_HL)

        self.play(FadeIn(preview, scale=0.5), run_time=0.8)
        self.wait(0.8)

        hint = Text(
            "分子×分子，分母×分母！",
            font=FONT, font_size=30, color=COLOR_ACCENT
        ).move_to(DOWN * 0.4)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, preview, hint)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 算理理解 — 求一个数的几分之几
    # ------------------------------------------------------------------

    def scene_2_rationale(self):
        """用矩形直观演示算理"""

        title = Text(
            "理解算理", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        subtitle = Text(
            "求一个数的几分之几是多少",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 问题文字
        p1 = Text("一根绳子长", font=FONT, font_size=26, color=WHITE)
        p_frac1 = MathTex(r"\frac{3}{4}", font_size=48, color=COLOR_FRAC_A)
        p2 = Text("米，用了它的", font=FONT, font_size=26, color=WHITE)
        row1 = VGroup(p1, p_frac1, p2).arrange(RIGHT, buff=0.15)

        p_frac2 = MathTex(r"\frac{2}{3}", font_size=48, color=COLOR_FRAC_B)
        p3 = Text("，用了多少米？", font=FONT, font_size=26, color=WHITE)
        row2 = VGroup(p_frac2, p3).arrange(RIGHT, buff=0.15)

        q_group = VGroup(row1, row2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        q_group.move_to(UP * 4.3)
        self.play(FadeIn(q_group), run_time=0.5)

        # 矩形条: 4等分，代表整体1米
        bar_total_w = 6.4
        bar_h = 1.0
        n_total = 4
        part_w = bar_total_w / n_total
        bar_cx = 0.0
        bar_cy = 2.6

        # 4格背景
        all_parts = VGroup()
        for i in range(n_total):
            rect = Rectangle(
                width=part_w - 0.06, height=bar_h,
                fill_color="#1e3a5f", fill_opacity=0.8,
                stroke_color="#4b5563", stroke_width=1.5
            )
            x_pos = bar_cx - bar_total_w / 2 + part_w / 2 + i * part_w
            rect.move_to(np.array([x_pos, bar_cy, 0]))
            all_parts.add(rect)

        self.play(Create(all_parts), run_time=0.5)

        # 标注 "1 米"
        brace_full = Brace(all_parts, direction=DOWN, buff=0.05, color=GRAY_A)
        label_1m = Text("1 米", font=FONT, font_size=22, color=GRAY_A)
        label_1m.next_to(brace_full, DOWN, buff=0.08)
        self.play(FadeIn(brace_full), FadeIn(label_1m), run_time=0.3)

        # 高亮前3份 (3/4)
        highlight_34 = VGroup()
        for i in range(3):
            rect = Rectangle(
                width=part_w - 0.06, height=bar_h,
                fill_color=COLOR_FRAC_A, fill_opacity=0.7,
                stroke_color=COLOR_FRAC_A, stroke_width=2
            )
            x_pos = bar_cx - bar_total_w / 2 + part_w / 2 + i * part_w
            rect.move_to(np.array([x_pos, bar_cy, 0]))
            highlight_34.add(rect)

        self.play(FadeIn(highlight_34), run_time=0.5)

        brace_34 = Brace(highlight_34, direction=UP, buff=0.05, color=COLOR_FRAC_A)
        label_34 = MathTex(r"\frac{3}{4}", font_size=36, color=COLOR_FRAC_A)
        label_34.next_to(brace_34, UP, buff=0.08)
        self.play(FadeIn(brace_34), FadeIn(label_34), run_time=0.3)
        self.wait(0.3)

        # 3/4 范围内再3等分，每小格宽度
        sub_w = (part_w * 3) / 3  # = part_w
        start_x = bar_cx - bar_total_w / 2

        explain = Text(
            "再把 3/4 分成 3 等份，取 2 份",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 1.4)
        self.play(FadeIn(explain), run_time=0.3)

        # 在3/4内画2条竖线（3等分界）
        dividers = VGroup()
        for k in range(1, 3):
            x = start_x + k * sub_w
            dline = DashedLine(
                np.array([x, bar_cy - bar_h / 2, 0]),
                np.array([x, bar_cy + bar_h / 2, 0]),
                color=WHITE, dash_length=0.08, stroke_width=1.5
            )
            dividers.add(dline)
        self.play(Create(dividers), run_time=0.3)

        # 高亮前2格 (2/3 of 3/4)
        sub_highlight = VGroup()
        for k in range(2):
            rect2 = Rectangle(
                width=sub_w - 0.06, height=bar_h,
                fill_color=COLOR_FRAC_B, fill_opacity=0.75,
                stroke_color=COLOR_FRAC_B, stroke_width=2
            )
            x_pos2 = start_x + sub_w / 2 + k * sub_w
            rect2.move_to(np.array([x_pos2, bar_cy, 0]))
            sub_highlight.add(rect2)

        self.play(FadeIn(sub_highlight), run_time=0.4)
        self.wait(0.5)

        # 结果
        result_t = Text("共用了", font=FONT, font_size=26, color=WHITE)
        result_f = MathTex(r"\frac{2}{4} = \frac{1}{2}", font_size=46, color=COLOR_RESULT)
        result_u = Text("米", font=FONT, font_size=26, color=WHITE)
        result_row = VGroup(result_t, result_f, result_u).arrange(RIGHT, buff=0.2)
        result_row.move_to(UP * 0.4)
        self.play(FadeIn(result_row), run_time=0.5)

        # 连接算式
        link_eq = MathTex(
            r"\frac{3}{4} \times \frac{2}{3} = \frac{6}{12} = \frac{1}{2}",
            font_size=46, color=COLOR_RESULT
        ).move_to(DOWN * 0.8)
        self.play(Write(link_eq), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, subtitle, q_group,
            all_parts, brace_full, label_1m,
            highlight_34, brace_34, label_34,
            explain, dividers, sub_highlight,
            result_row, link_eq
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 分数乘整数
    # ------------------------------------------------------------------

    def scene_3_fraction_times_int(self):
        """分数乘整数: 3/4 × 2，分子乘整数，分母不变"""

        title = Text(
            "分数 × 整数",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 算式
        eq1 = MathTex(r"\frac{3}{4} \times 2", font_size=76, color=WHITE).move_to(UP * 5.0)
        self.play(Write(eq1), run_time=0.6)

        # 解释文字
        expl_t = Text("就是 2 个", font=FONT, font_size=28, color=WHITE)
        expl_f = MathTex(r"\frac{3}{4}", font_size=52, color=COLOR_FRAC_A)
        expl_row = VGroup(expl_t, expl_f).arrange(RIGHT, buff=0.2)
        expl_row.move_to(UP * 3.8)
        self.play(FadeIn(expl_row), run_time=0.4)

        # 矩形条演示: 2行每行4格，前3格高亮
        bar_w = 6.0
        bar_h = 0.9
        n_cols = 4
        pw = bar_w / n_cols
        row_ys = [2.8, 1.7]

        bar_group = VGroup()
        for row_idx, ry in enumerate(row_ys):
            for col_idx in range(n_cols):
                x_pos = -bar_w / 2 + pw / 2 + col_idx * pw
                rect = Rectangle(
                    width=pw - 0.05, height=bar_h,
                    fill_color=COLOR_FRAC_A if col_idx < 3 else "#2d3748",
                    fill_opacity=0.75 if col_idx < 3 else 0.45,
                    stroke_color=WHITE, stroke_width=1.5
                )
                rect.move_to(np.array([x_pos, ry, 0]))
                bar_group.add(rect)

        self.play(Create(bar_group), run_time=0.7)

        # 大括号标注每行为 3/4
        row1_highlighted = VGroup(*[bar_group[i] for i in range(3)])
        row2_highlighted = VGroup(*[bar_group[n_cols + i] for i in range(3)])
        b1 = Brace(row1_highlighted, direction=LEFT, buff=0.05, color=COLOR_FRAC_A)
        b2 = Brace(row2_highlighted, direction=LEFT, buff=0.05, color=COLOR_FRAC_A)
        bl1 = MathTex(r"\frac{3}{4}", font_size=30, color=COLOR_FRAC_A).next_to(b1, LEFT, buff=0.08)
        bl2 = MathTex(r"\frac{3}{4}", font_size=30, color=COLOR_FRAC_A).next_to(b2, LEFT, buff=0.08)
        self.play(FadeIn(b1), FadeIn(bl1), FadeIn(b2), FadeIn(bl2), run_time=0.4)
        self.wait(0.4)

        # 步骤推导
        step1 = MathTex(
            r"\frac{3}{4} \times 2 = \frac{3 \times 2}{4} = \frac{6}{4} = \frac{3}{2}",
            font_size=50, color=WHITE
        ).move_to(DOWN * 0.2)
        self.play(Write(step1), run_time=1.0)

        # 法则框
        rule_box = Rectangle(
            width=7.5, height=1.4,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 2.0)
        rule_t1 = Text("分数 × 整数:", font=FONT, font_size=26, color=COLOR_HL)
        rule_t2 = Text("分子乘整数，分母不变", font=FONT, font_size=26, color=WHITE)
        rule_content = VGroup(rule_t1, rule_t2).arrange(RIGHT, buff=0.3)
        rule_content.move_to(DOWN * 2.0)
        self.play(Create(rule_box), FadeIn(rule_content), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, eq1, expl_row, bar_group,
            b1, bl1, b2, bl2, step1, rule_box, rule_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 分数乘分数规则
    # ------------------------------------------------------------------

    def scene_4_fraction_rule(self):
        """核心公式: a/b × c/d = (a×c)/(b×d)"""

        title = Text(
            "分数 × 分数",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        subtitle = Text("计算法则", font=FONT, font_size=32, color=WHITE).move_to(UP * 5.4)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 核心公式
        formula = MathTex(
            r"\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}",
            font_size=64, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(formula), run_time=1.0)
        self.wait(0.3)

        # 标注分子
        label_num = Text("分子相乘", font=FONT, font_size=24, color=COLOR_NUMERATOR)
        label_num.move_to(UP * 5.1)
        self.play(FadeIn(label_num), run_time=0.4)

        # 标注分母
        label_den = Text("分母相乘", font=FONT, font_size=24, color=COLOR_DENOMINATOR)
        label_den.move_to(UP * 2.7)
        self.play(FadeIn(label_den), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(VGroup(label_num, label_den)), run_time=0.3)

        # 具体例子: 1/2 × 1/3
        ex_title = Text("例：", font=FONT, font_size=28, color=GRAY_A)
        ex_eq = MathTex(
            r"\frac{1}{2} \times \frac{1}{3} = \frac{1 \times 1}{2 \times 3} = \frac{1}{6}",
            font_size=52, color=WHITE
        )
        ex_row = VGroup(ex_title, ex_eq).arrange(RIGHT, buff=0.2)
        ex_row.move_to(UP * 2.4)
        self.play(Write(ex_row), run_time=0.8)

        # 面积图示: 大矩形 = 1，竖线分成2，横线分成3，高亮1/6
        big_w = 4.8
        big_h = 3.6
        big_rect = Rectangle(
            width=big_w, height=big_h,
            fill_color="#1e293b", fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        ).move_to(DOWN * 1.9)

        self.play(Create(big_rect), run_time=0.4)

        # 竖线 (1/2)
        v_x = big_rect.get_center()[0]  # x=0, split at center
        v_line = Line(
            np.array([v_x, big_rect.get_top()[1], 0]),
            np.array([v_x, big_rect.get_bottom()[1], 0]),
            color=COLOR_FRAC_A, stroke_width=2.5
        )
        self.play(Create(v_line), run_time=0.3)
        lbl_half = MathTex(r"\frac{1}{2}", font_size=26, color=COLOR_FRAC_A)
        lbl_half.next_to(big_rect, DOWN, buff=0.1).shift(LEFT * big_w / 4)
        self.play(FadeIn(lbl_half), run_time=0.2)

        # 水平线 (1/3, 2/3)
        h_lines = VGroup()
        for k in range(1, 3):
            hy = big_rect.get_bottom()[1] + big_h * k / 3
            hl = Line(
                np.array([big_rect.get_left()[0], hy, 0]),
                np.array([big_rect.get_right()[0], hy, 0]),
                color=COLOR_FRAC_B, stroke_width=2.0
            )
            h_lines.add(hl)
        self.play(Create(h_lines), run_time=0.3)
        lbl_third = MathTex(r"\frac{1}{3}", font_size=26, color=COLOR_FRAC_B)
        lbl_third.next_to(big_rect, LEFT, buff=0.1).shift(UP * big_h / 6)
        self.play(FadeIn(lbl_third), run_time=0.2)

        # 高亮左上角 1/6 区域
        small_w = big_w / 2
        small_h = big_h / 3
        small_rect = Rectangle(
            width=small_w - 0.04,
            height=small_h - 0.04,
            fill_color=COLOR_RESULT, fill_opacity=0.65,
            stroke_color=COLOR_RESULT, stroke_width=2
        )
        small_cx = big_rect.get_left()[0] + small_w / 2
        small_cy = big_rect.get_top()[1] - small_h / 2
        small_rect.move_to(np.array([small_cx, small_cy, 0]))
        self.play(FadeIn(small_rect), run_time=0.4)

        lbl_16 = MathTex(r"\frac{1}{6}", font_size=28, color=COLOR_RESULT)
        lbl_16.move_to(small_rect.get_center())
        self.play(FadeIn(lbl_16), run_time=0.3)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, subtitle, formula, ex_row,
            big_rect, v_line, lbl_half, h_lines, lbl_third,
            small_rect, lbl_16
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 例题1 — 2/3 × 3/4
    # ------------------------------------------------------------------

    def scene_5_example_1(self):
        """例题1: 2/3 × 3/4，展示先约分方法"""

        title = Text(
            "例题 1", font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.3)

        # 题目
        problem = MathTex(
            r"\frac{2}{3} \times \frac{3}{4}",
            font_size=82, color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(problem), run_time=0.7)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 4.1)
        self.play(Create(sep), run_time=0.2)

        # 方法1: 直接计算
        m1_lbl = Text("方法一：直接计算", font=FONT, font_size=28, color=GRAY_A).move_to(UP * 3.5)
        self.play(FadeIn(m1_lbl), run_time=0.3)

        s1 = MathTex(r"= \frac{2 \times 3}{3 \times 4}", font_size=64, color=WHITE).move_to(UP * 2.5)
        self.play(Write(s1), run_time=0.6)

        s2 = MathTex(r"= \frac{6}{12}", font_size=64, color=WHITE).move_to(UP * 1.3)
        self.play(Write(s2), run_time=0.5)

        s3 = MathTex(r"= \frac{1}{2}", font_size=72, color=COLOR_RESULT).move_to(UP * 0.0)
        simp_note = Text("（约分）", font=FONT, font_size=24, color=COLOR_HL).next_to(s3, RIGHT, buff=0.2)
        self.play(Write(s3), FadeIn(simp_note), run_time=0.5)
        self.wait(0.8)

        # 切换：方法2 先约分
        self.play(FadeOut(VGroup(m1_lbl, s1, s2, s3, simp_note)), run_time=0.3)

        m2_lbl = Text(
            "方法二：先约分，更简便！",
            font=FONT, font_size=26, color=COLOR_ACCENT
        ).move_to(UP * 3.5)
        self.play(FadeIn(m2_lbl), run_time=0.3)

        # 重新显示原式
        orig = MathTex(
            r"\frac{2}{3} \times \frac{3}{4}",
            font_size=74, color=WHITE
        ).move_to(UP * 2.4)
        self.play(FadeIn(orig), run_time=0.4)

        # 说明约分:  分子2和分母4 → 各除2；分子3和分母3 → 各除3
        ann_box = Rectangle(
            width=7.5, height=2.0,
            fill_color="#1e293b", fill_opacity=0.85,
            stroke_color=COLOR_ACCENT, stroke_width=1.5
        ).move_to(UP * 1.0)

        ann_t1 = Text("2 和 4 有公因数 2", font=FONT, font_size=24, color=COLOR_FRAC_A)
        ann_t2 = Text("3 和 3 有公因数 3", font=FONT, font_size=24, color=COLOR_FRAC_B)
        ann_group = VGroup(ann_t1, ann_t2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        ann_group.move_to(UP * 1.0)
        self.play(Create(ann_box), FadeIn(ann_group), run_time=0.5)
        self.wait(0.4)

        # 约分后的结果 (用颜色高亮约分，不用\cancel)
        after_cancel = MathTex(
            r"\frac{2}{3} \times \frac{3}{4}",
            font_size=70, color=WHITE
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(after_cancel), run_time=0.4)

        # 箭头指向约分说明
        arrow_ann = Text(
            "2÷2→1, 4÷2→2, 3÷3→1",
            font=FONT, font_size=22, color=COLOR_RESULT
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(arrow_ann), run_time=0.4)

        final_result = MathTex(
            r"= \frac{1 \times 1}{1 \times 2} = \frac{1}{2}",
            font_size=60, color=COLOR_RESULT
        ).move_to(DOWN * 2.0)
        self.play(Write(final_result), run_time=0.7)
        self.wait(0.8)

        # 技巧提示框
        tip_box = RoundedRectangle(
            width=7.5, height=1.3, corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.85,
            stroke_color=COLOR_RESULT, stroke_width=2
        ).move_to(DOWN * 3.3)
        tip_text = Text(
            "先约分，计算更简便！",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 3.3)
        self.play(Create(tip_box), FadeIn(tip_text), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, problem, sep, m2_lbl,
            orig, ann_box, ann_group,
            after_cancel, arrow_ann, final_result,
            tip_box, tip_text
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 例题2 — 3/5 × 5/6 (交叉约分)
    # ------------------------------------------------------------------

    def scene_6_example_2_cross_cancel(self):
        """例题2: 3/5 × 5/6，交叉约分"""

        title = Text(
            "例题 2  交叉约分",
            font=FONT, font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.3)

        # 题目
        problem = MathTex(
            r"\frac{3}{5} \times \frac{5}{6}",
            font_size=82, color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(problem), run_time=0.6)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 4.1)
        self.play(Create(sep), run_time=0.2)

        hint = Text(
            "能约分先约分！", font=FONT, font_size=28, color=COLOR_ACCENT
        ).move_to(UP * 3.5)
        self.play(FadeIn(hint), run_time=0.3)

        # 注解1: 5 和 5
        ann1 = Text("分子5 和 分母5 约分 ÷5", font=FONT, font_size=24, color=COLOR_FRAC_B)
        ann1.move_to(UP * 2.8)
        self.play(FadeIn(ann1), run_time=0.4)

        # 注解2: 3 和 6
        ann2 = Text("分子3 和 分母6 约分 ÷3", font=FONT, font_size=24, color=COLOR_FRAC_A)
        ann2.move_to(UP * 2.2)
        self.play(FadeIn(ann2), run_time=0.4)
        self.wait(0.4)

        # 约分后 (直接展示约分结果)
        after = MathTex(
            r"\frac{3}{5} \times \frac{5}{6}",
            font_size=70, color=WHITE
        ).move_to(UP * 1.0)
        after2 = MathTex(
            r"= \frac{1}{1} \times \frac{1}{2}",
            font_size=62, color=WHITE
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(after), run_time=0.6)
        self.play(FadeIn(after2), run_time=0.5)

        # 最终结果
        final = MathTex(
            r"= \frac{1}{2}",
            font_size=80, color=COLOR_RESULT
        ).move_to(DOWN * 1.8)
        self.play(Write(final), run_time=0.5)
        self.wait(0.5)

        # 验证框
        check_box = Rectangle(
            width=7.5, height=2.0,
            fill_color="#1e1b4b", fill_opacity=0.85,
            stroke_color=COLOR_ACCENT, stroke_width=2
        ).move_to(DOWN * 3.6)
        check_title = Text("不约分直接算（验证）:", font=FONT, font_size=22, color=COLOR_ACCENT)
        check_eq = MathTex(
            r"\frac{3 \times 5}{5 \times 6} = \frac{15}{30} = \frac{1}{2}",
            font_size=44, color=WHITE
        )
        check_content = VGroup(check_title, check_eq).arrange(DOWN, buff=0.2)
        check_content.move_to(DOWN * 3.6)
        self.play(Create(check_box), FadeIn(check_content), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, problem, sep, hint,
            ann1, ann2, after, after2, final,
            check_box, check_content
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 应用题
    # ------------------------------------------------------------------

    def scene_7_word_problem(self):
        """应用题: 一块布3/4米，送给朋友2/3，送了多少米？"""

        title = Text(
            "应用题", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title), run_time=0.3)

        # 题目
        p1 = Text("一块布长", font=FONT, font_size=28, color=WHITE)
        pf1 = MathTex(r"\frac{3}{4}", font_size=52, color=COLOR_FRAC_A)
        p2 = Text("米，送给朋友", font=FONT, font_size=28, color=WHITE)
        row1 = VGroup(p1, pf1, p2).arrange(RIGHT, buff=0.15)

        p3 = Text("其中的", font=FONT, font_size=28, color=WHITE)
        pf2 = MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_FRAC_B)
        p4 = Text("，送了多少米？", font=FONT, font_size=28, color=WHITE)
        row2 = VGroup(p3, pf2, p4).arrange(RIGHT, buff=0.15)

        problem_grp = VGroup(row1, row2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        problem_grp.move_to(UP * 4.8)
        self.play(FadeIn(problem_grp), run_time=0.6)

        sep = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1).move_to(UP * 3.7)
        self.play(Create(sep), run_time=0.2)

        # 解题思路
        think_t = Text("思路：", font=FONT, font_size=26, color=COLOR_ACCENT)
        think_c = Text("求 3/4 的 2/3 是多少", font=FONT, font_size=26, color=WHITE)
        think_row = VGroup(think_t, think_c).arrange(RIGHT, buff=0.2)
        think_row.move_to(UP * 3.1)
        self.play(FadeIn(think_row), run_time=0.4)

        # 列式
        eq_lbl = Text("列式：", font=FONT, font_size=26, color=GRAY_A)
        eq_formula = MathTex(r"\frac{3}{4} \times \frac{2}{3}", font_size=68, color=WHITE)
        eq_row = VGroup(eq_lbl, eq_formula).arrange(RIGHT, buff=0.3)
        eq_row.move_to(UP * 2.0)
        self.play(Write(eq_row), run_time=0.6)

        # 计算过程
        c1 = MathTex(
            r"= \frac{3 \times 2}{4 \times 3}",
            font_size=62, color=WHITE
        ).move_to(UP * 0.7)
        self.play(Write(c1), run_time=0.6)

        c2 = MathTex(r"= \frac{2}{4} = \frac{1}{2}", font_size=62, color=COLOR_RESULT).move_to(DOWN * 0.6)
        self.play(Write(c2), run_time=0.6)
        self.wait(0.5)

        # 答语框
        ans_box = RoundedRectangle(
            width=7.5, height=1.5, corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.85,
            stroke_color=COLOR_RESULT, stroke_width=2
        ).move_to(DOWN * 2.3)
        ans_t = Text("答：送了", font=FONT, font_size=28, color=WHITE)
        ans_f = MathTex(r"\frac{1}{2}", font_size=48, color=COLOR_RESULT)
        ans_u = Text("米。", font=FONT, font_size=28, color=WHITE)
        ans_row = VGroup(ans_t, ans_f, ans_u).arrange(RIGHT, buff=0.15)
        ans_row.move_to(DOWN * 2.3)
        self.play(Create(ans_box), FadeIn(ans_row), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, problem_grp, sep, think_row,
            eq_row, c1, c2, ans_box, ans_row
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 8: 总结公式框
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        """总结: 核心法则 + 注意事项"""

        title = Text(
            "总结", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.4)

        # 卡片1: 核心公式
        card1 = Rectangle(
            width=7.8, height=2.0,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=COLOR_FRAC_A, stroke_width=2.5
        ).move_to(UP * 4.7)
        c1_t = Text("计算法则", font=FONT, font_size=28, color=COLOR_FRAC_A)
        c1_f = MathTex(
            r"\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}",
            font_size=50, color=WHITE
        )
        c1_content = VGroup(c1_t, c1_f).arrange(DOWN, buff=0.15)
        c1_content.move_to(UP * 4.7)
        self.play(Create(card1), FadeIn(c1_content), run_time=0.5)

        # 卡片2: 先约分技巧
        card2 = Rectangle(
            width=7.8, height=2.2,
            fill_color="#14532d", fill_opacity=0.9,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(UP * 2.3)
        c2_t = Text("关键技巧：先约分", font=FONT, font_size=28, color=COLOR_RESULT)
        c2_eq = MathTex(
            r"\frac{2}{3} \times \frac{3}{4} = \frac{1 \times 1}{1 \times 2} = \frac{1}{2}",
            font_size=42, color=WHITE
        )
        c2_note = Text("减小数字，运算更简便", font=FONT, font_size=22, color=GRAY_A)
        c2_content = VGroup(c2_t, c2_eq, c2_note).arrange(DOWN, buff=0.12)
        c2_content.move_to(UP * 2.3)
        self.play(Create(card2), FadeIn(c2_content), run_time=0.5)

        # 卡片3: 算理
        card3 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#3b1f6e", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=2.5
        ).move_to(UP * 0.1)
        c3_t = Text("算理", font=FONT, font_size=28, color=COLOR_ACCENT)
        c3_c = Text(
            "求一个数的几分之几是多少",
            font=FONT, font_size=26, color=WHITE
        )
        c3_content = VGroup(c3_t, c3_c).arrange(DOWN, buff=0.15)
        c3_content.move_to(UP * 0.1)
        self.play(Create(card3), FadeIn(c3_content), run_time=0.5)

        # 卡片4: 分数乘整数
        card4 = Rectangle(
            width=7.8, height=1.8,
            fill_color="#422006", fill_opacity=0.9,
            stroke_color=COLOR_FRAC_B, stroke_width=2.5
        ).move_to(DOWN * 1.8)
        c4_t = Text("分数 × 整数", font=FONT, font_size=26, color=COLOR_FRAC_B)
        c4_f = MathTex(
            r"\frac{a}{b} \times n = \frac{a \times n}{b}",
            font_size=44, color=WHITE
        )
        c4_content = VGroup(c4_t, c4_f).arrange(DOWN, buff=0.14)
        c4_content.move_to(DOWN * 1.8)
        self.play(Create(card4), FadeIn(c4_content), run_time=0.5)

        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title,
            card1, c1_content,
            card2, c2_content,
            card3, c3_content,
            card4, c4_content
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        """片尾: 关注提示"""

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(Transform(self.author_mob, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.5)

        # 装饰: 分数符号
        deco = VGroup(
            MathTex(r"\frac{1}{2}", font_size=46, color=COLOR_FRAC_A).shift(LEFT * 3.0 + DOWN * 2.6),
            MathTex(r"\times", font_size=46, color=COLOR_HL).shift(LEFT * 1.2 + DOWN * 2.6),
            MathTex(r"\frac{2}{3}", font_size=46, color=COLOR_FRAC_B).shift(RIGHT * 0.6 + DOWN * 2.6),
            MathTex(r"=\frac{1}{3}", font_size=46, color=COLOR_RESULT).shift(RIGHT * 2.8 + DOWN * 2.6),
        )
        self.play(*[FadeIn(f, scale=0.5) for f in deco], run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=0.8
        )
