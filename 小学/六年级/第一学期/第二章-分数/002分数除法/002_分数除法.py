"""
002_分数除法.py — 分数除法 教学动画

知识点: 分数除法法则: 除以一个数等于乘它的倒数
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子
  2. 倒数的概念
  3. 分数除法法则推导
  4. 例题1: 2/3 ÷ 3/4
  5. 例题2: 6 ÷ 2/3
  6. 应用题: 已知几分之几求原数
  7. 总结
  8. 片尾
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

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR     = "#1a1a2e"
COLOR_MAIN   = "#3b82f6"   # 蓝色主色
COLOR_RED    = "#ef4444"   # 红色
COLOR_GREEN  = "#22c55e"   # 绿色结果
COLOR_HL     = "#fbbf24"   # 黄色高亮
COLOR_PURPLE = "#a78bfa"   # 紫色强调
COLOR_ORANGE = "#f59e0b"   # 橙色
COLOR_AUTHOR = "#6b7280"   # 灰色作者信息
COLOR_FLIP   = "#f472b6"   # 粉色翻转
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionDivisionLesson(Scene):
    """
    分数除法教学动画
    场景顺序:
      1. 开场钩子
      2. 倒数的概念
      3. 分数除法法则
      4. 例题1: 2/3 ÷ 3/4
      5. 例题2: 6 ÷ 2/3
      6. 应用题
      7. 总结公式框
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_reciprocal()
        self.scene_3_division_rule()
        self.scene_4_example1()
        self.scene_5_example2()
        self.scene_6_word_problem()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 引出分数除法问题"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 主标题
        hook1 = Text(
            "分数除法",
            font=FONT, font_size=54, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "除以一个数 = 乘它的倒数！",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.7)
        self.play(Write(hook2), run_time=0.6)

        # 钩子问题
        q_text = Text(
            "你知道怎么算吗？",
            font=FONT, font_size=32, color=COLOR_PURPLE
        ).move_to(UP * 3.2)
        self.play(FadeIn(q_text, shift=UP * 0.3), run_time=0.5)

        # 预览算式
        preview = MathTex(
            r"\frac{2}{3}", r"\div", r"\frac{3}{4}", r"= \; ?",
            font_size=80
        ).move_to(UP * 1.5)
        preview[0].set_color(COLOR_MAIN)
        preview[2].set_color(COLOR_RED)
        preview[3].set_color(COLOR_HL)
        self.play(FadeIn(preview, scale=0.5), run_time=0.9)
        self.wait(1.2)

        self.play(FadeOut(VGroup(hook1, hook2, q_text, preview)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 倒数的概念
    # ------------------------------------------------------------------

    def scene_2_reciprocal(self):
        """倒数: 乘积为1的两个数互为倒数"""

        title = Text(
            "第一步：认识倒数",
            font=FONT, font_size=40, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义说明
        def_text = Text(
            "乘积是 1 的两个数互为倒数",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.9)
        self.play(Write(def_text), run_time=0.7)

        # 例: 3/4 × 4/3 = 1
        ex1 = MathTex(
            r"\frac{3}{4}", r"\times", r"\frac{4}{3}", r"=", r"1",
            font_size=68
        ).move_to(UP * 3.6)
        ex1[0].set_color(COLOR_MAIN)
        ex1[2].set_color(COLOR_ORANGE)
        ex1[4].set_color(COLOR_GREEN)

        self.play(Write(ex1), run_time=0.9)
        self.wait(0.4)

        # 双向箭头标注倒数关系
        # 箭头从 3/4 下方指向 4/3 下方
        arr_start = ex1[0].get_bottom() + DOWN * 0.12
        arr_end   = ex1[2].get_bottom() + DOWN * 0.12
        arrow_lr = CurvedArrow(arr_start, arr_end, angle=TAU / 8, color=COLOR_HL, stroke_width=2.5)
        arrow_rl = CurvedArrow(arr_end, arr_start, angle=TAU / 8, color=COLOR_HL, stroke_width=2.5)
        recip_label = Text(
            "互为倒数", font=FONT, font_size=22, color=COLOR_HL
        ).move_to((arr_start + arr_end) / 2 + DOWN * 0.55)

        self.play(Create(arrow_lr), Create(arrow_rl), run_time=0.5)
        self.play(FadeIn(recip_label), run_time=0.4)
        self.wait(0.4)

        # 求倒数方法框
        method_box = RoundedRectangle(
            width=7.0, height=1.5, corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.7,
            stroke_color=COLOR_MAIN, stroke_width=2
        ).move_to(UP * 1.6)
        method_title = Text(
            "求倒数的方法", font=FONT, font_size=26, color=COLOR_MAIN
        ).move_to(UP * 1.95)
        method_body = Text(
            "分子和分母互换位置",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 1.35)

        self.play(Create(method_box), run_time=0.4)
        self.play(Write(method_title), Write(method_body), run_time=0.6)

        # 例子列表: 几个倒数
        examples_data = [
            (r"\frac{2}{5}", r"\frac{5}{2}"),
            (r"\frac{7}{3}", r"\frac{3}{7}"),
            (r"4",           r"\frac{1}{4}"),
        ]

        ex_group = VGroup()
        for a, b in examples_data:
            row = MathTex(a, r"\longleftrightarrow", b, font_size=44)
            row[0].set_color(COLOR_MAIN)
            row[2].set_color(COLOR_ORANGE)
            ex_group.add(row)

        ex_group.arrange(DOWN, buff=0.32).move_to(DOWN * 1.1)

        self.play(LaggedStart(
            *[Write(row) for row in ex_group],
            lag_ratio=0.4
        ), run_time=1.2)
        self.wait(0.5)

        # 注意: 0 没有倒数
        note = Text(
            "注意：0 没有倒数！",
            font=FONT, font_size=26, color=COLOR_RED
        ).move_to(DOWN * 2.7)
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, def_text, ex1,
            arrow_lr, arrow_rl, recip_label,
            method_box, method_title, method_body,
            ex_group, note
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 分数除法法则推导
    # ------------------------------------------------------------------

    def scene_3_division_rule(self):
        """核心法则: a/b ÷ c/d = a/b × d/c"""

        title = Text(
            "分数除法法则",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 除法意义说明
        meaning_title = Text(
            "除法的意义：", font=FONT, font_size=30, color=COLOR_PURPLE
        ).move_to(UP * 4.9)
        self.play(FadeIn(meaning_title), run_time=0.4)

        meaning_text = Text(
            "已知积与一个因数，求另一个因数",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.25)
        self.play(Write(meaning_text), run_time=0.6)

        # 类比整数除法
        ex_int = MathTex(
            r"6 \div 2 = 3 \quad \because \quad 3 \times 2 = 6",
            font_size=44
        ).move_to(UP * 3.2)
        self.play(Write(ex_int), run_time=0.7)
        self.wait(0.4)

        transition = Text(
            "分数除法同样道理：",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 2.3)
        self.play(FadeIn(transition), run_time=0.4)

        # 核心公式大框
        rule_box = RoundedRectangle(
            width=8.2, height=3.6, corner_radius=0.3,
            fill_color="#1a2744", fill_opacity=0.85,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(Create(rule_box), run_time=0.4)

        # 公式: a/b ÷ c/d = a/b × d/c
        core_formula = MathTex(
            r"\frac{a}{b}", r"\div", r"\frac{c}{d}",
            r"=",
            r"\frac{a}{b}", r"\times", r"\frac{d}{c}",
            font_size=60
        ).move_to(UP * 1.0)
        core_formula[0].set_color(COLOR_MAIN)
        core_formula[2].set_color(COLOR_RED)
        core_formula[4].set_color(COLOR_MAIN)
        core_formula[6].set_color(COLOR_ORANGE)

        self.play(Write(core_formula), run_time=0.9)

        # 弧线箭头: c/d → d/c (倒数变换)
        flip_arrow = CurvedArrow(
            core_formula[2].get_top() + UP * 0.05,
            core_formula[6].get_top() + UP * 0.05,
            angle=-TAU / 6,
            color=COLOR_FLIP,
            stroke_width=3
        )
        flip_label = Text(
            "除数取倒数", font=FONT, font_size=22, color=COLOR_FLIP
        ).next_to(flip_arrow, UP, buff=0.08)
        self.play(Create(flip_arrow), FadeIn(flip_label), run_time=0.6)

        # 除号 → 乘号 说明
        div_note_line1 = Text("÷ 变成 ×", font=FONT, font_size=22, color=COLOR_HL).move_to(UP * 0.2)
        self.play(FadeIn(div_note_line1), run_time=0.4)

        # 口诀
        rule_text_bg = RoundedRectangle(
            width=7.5, height=0.95, corner_radius=0.15,
            fill_color="#2d1b4e", fill_opacity=0.9,
            stroke_color=COLOR_PURPLE, stroke_width=2
        ).move_to(DOWN * 0.6)
        rule_text = Text(
            "除以一个数 ＝ 乘以这个数的倒数",
            font=FONT, font_size=24, color=COLOR_PURPLE
        ).move_to(DOWN * 0.6)
        self.play(Create(rule_text_bg), Write(rule_text), run_time=0.6)
        self.wait(1.5)

        # 条件: c/d ≠ 0
        cond = MathTex(r"(c \neq 0, \; d \neq 0)", font_size=38, color=GRAY_A).move_to(DOWN * 1.7)
        self.play(FadeIn(cond), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(VGroup(
            title, meaning_title, meaning_text, ex_int,
            transition, rule_box,
            core_formula, flip_arrow, flip_label,
            div_note_line1, rule_text_bg, rule_text, cond
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 例题1 — 2/3 ÷ 3/4
    # ------------------------------------------------------------------

    def scene_4_example1(self):
        """例题1: 2/3 ÷ 3/4 = 2/3 × 4/3 = 8/9"""

        title = Text(
            "例题 1", font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 题目
        prob_label = Text(
            "计算：", font=FONT, font_size=30, color=COLOR_AUTHOR
        ).move_to(UP * 4.9 + LEFT * 2.5)
        prob = MathTex(
            r"\frac{2}{3} \div \frac{3}{4}",
            font_size=72
        ).move_to(UP * 4.9 + RIGHT * 0.8)
        self.play(FadeIn(prob_label), Write(prob), run_time=0.7)
        self.wait(0.4)

        # 步骤标题
        step1_title = Text(
            "第①步：除数变倒数，÷ 变 ×",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 3.7)
        self.play(Write(step1_title), run_time=0.6)

        # 变换过程
        step1_eq = MathTex(
            r"= \frac{2}{3}", r"\times", r"\frac{4}{3}",
            font_size=68
        ).move_to(UP * 2.8)
        step1_eq[0].set_color(COLOR_MAIN)
        step1_eq[2].set_color(COLOR_ORANGE)
        self.play(Write(step1_eq), run_time=0.7)

        # 小注: 3/4 的倒数是 4/3
        flip_note = Text(
            r"3/4 的倒数 = 4/3  （分子分母互换）",
            font=FONT, font_size=22, color=COLOR_FLIP
        ).move_to(UP * 2.05)
        flip_arr = Arrow(
            step1_eq[2].get_bottom() + DOWN * 0.05,
            UP * 2.2 + RIGHT * step1_eq[2].get_center()[0],
            buff=0.08, color=COLOR_FLIP, stroke_width=2.5
        )
        self.play(GrowArrow(flip_arr), FadeIn(flip_note), run_time=0.5)
        self.wait(0.5)

        # 步骤2: 计算
        step2_title = Text(
            "第②步：分子×分子，分母×分母",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 1.15)
        self.play(Write(step2_title), run_time=0.6)

        step2_eq = MathTex(
            r"= \frac{2 \times 4}{3 \times 3}",
            font_size=68
        ).move_to(UP * 0.25)
        self.play(Write(step2_eq), run_time=0.6)
        self.wait(0.3)

        # 结果
        step3_eq = MathTex(r"= \frac{8}{9}", font_size=82).move_to(DOWN * 0.85)
        step3_eq[0].set_color(COLOR_GREEN)
        self.play(Write(step3_eq), run_time=0.6)

        result_box = SurroundingRectangle(
            step3_eq, color=COLOR_GREEN, buff=0.2, corner_radius=0.15, stroke_width=3
        )
        self.play(Create(result_box), run_time=0.4)
        self.play(Indicate(step3_eq, color=COLOR_GREEN, scale_factor=1.15), run_time=0.6)
        self.wait(0.8)

        # 验证
        verify_label = Text("验证：", font=FONT, font_size=24, color=GRAY_A).move_to(DOWN * 2.1 + LEFT * 3.0)
        verify_eq = MathTex(
            r"\frac{8}{9} \times \frac{3}{4} = \frac{24}{36} = \frac{2}{3} \checkmark",
            font_size=44
        ).move_to(DOWN * 2.1 + RIGHT * 0.5)
        verify_eq[0].set_color(COLOR_GREEN)
        self.play(FadeIn(verify_label), Write(verify_eq), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, prob_label, prob,
            step1_title, step1_eq, flip_arr, flip_note,
            step2_title, step2_eq, step3_eq,
            result_box, verify_label, verify_eq
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 例题2 — 6 ÷ 2/3
    # ------------------------------------------------------------------

    def scene_5_example2(self):
        """例题2: 整数 ÷ 分数: 6 ÷ 2/3 = 9"""

        title = Text(
            "例题 2", font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        context = Text(
            "6 块巧克力，每次吃 2/3 块，能吃几次？",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 5.0)
        self.play(Write(context), run_time=0.7)

        # 题目算式
        prob_label = Text("计算：", font=FONT, font_size=30, color=COLOR_AUTHOR).move_to(UP * 4.1 + LEFT * 2.0)
        prob = MathTex(r"6 \div \frac{2}{3}", font_size=72).move_to(UP * 4.0 + RIGHT * 1.0)
        self.play(FadeIn(prob_label), Write(prob), run_time=0.7)
        self.wait(0.3)

        # 图形直观: 6 个矩形块
        n_blocks = 6
        block_w = 0.88
        block_h = 0.68
        blk_colors = [COLOR_ORANGE, COLOR_GREEN, COLOR_MAIN,
                      COLOR_ORANGE, COLOR_GREEN, COLOR_MAIN]
        blocks = VGroup()
        total_width = n_blocks * block_w + (n_blocks - 1) * 0.1
        start_x = -total_width / 2 + block_w / 2
        for i in range(n_blocks):
            blk = RoundedRectangle(
                width=block_w, height=block_h, corner_radius=0.08,
                fill_color=blk_colors[i // 2], fill_opacity=0.8,
                stroke_color=WHITE, stroke_width=1.5
            ).move_to(np.array([start_x + i * (block_w + 0.1), 2.75, 0]))
            blocks.add(blk)
        self.play(LaggedStart(*[FadeIn(b, scale=0.6) for b in blocks], lag_ratio=0.08), run_time=0.7)

        label_visual = Text(
            "每 2 块代表 2/3 次",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 2.05)
        self.play(FadeIn(label_visual), run_time=0.4)

        # 计算步骤
        step1_title = Text(
            "第①步：除以 2/3，变乘以倒数 3/2",
            font=FONT, font_size=25, color=GRAY_A
        ).move_to(UP * 1.35)
        self.play(Write(step1_title), run_time=0.6)

        step1_eq = MathTex(r"= 6 \times \frac{3}{2}", font_size=68).move_to(UP * 0.5)
        step1_eq[0].set_color(COLOR_ORANGE)
        self.play(Write(step1_eq), run_time=0.6)

        step2_eq = MathTex(r"= \frac{6 \times 3}{2} = \frac{18}{2}", font_size=60).move_to(DOWN * 0.45)
        self.play(Write(step2_eq), run_time=0.6)

        step3_eq = MathTex(r"= 9", font_size=82, color=COLOR_GREEN).move_to(DOWN * 1.5)
        self.play(Write(step3_eq), run_time=0.5)

        result_box = SurroundingRectangle(
            step3_eq, color=COLOR_GREEN, buff=0.2, corner_radius=0.15, stroke_width=3
        )
        self.play(Create(result_box), run_time=0.4)
        self.play(Indicate(step3_eq, scale_factor=1.2, color=COLOR_GREEN), run_time=0.5)

        answer = Text(
            "答：可以吃 9 次。",
            font=FONT, font_size=28, color=COLOR_GREEN
        ).move_to(DOWN * 2.6)
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(VGroup(
            title, context, prob_label, prob, blocks, label_visual,
            step1_title, step1_eq, step2_eq, step3_eq,
            result_box, answer
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 应用题 — 已知几分之几求原数
    # ------------------------------------------------------------------

    def scene_6_word_problem(self):
        """应用题: 一块地的 3/5 是 12 亩，求总亩数"""

        title = Text(
            "应用题", font=FONT, font_size=38, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        q1 = Text(
            "一块地的 3/5 是 12 亩，",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.9)
        q2 = Text(
            "这块地有多少亩？",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.3)
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.5)
        self.wait(0.4)

        # 图形: 长条表示全部，3/5 染绿
        bar_full = Rectangle(
            width=7.0, height=0.8,
            fill_color="#1e3a5f", fill_opacity=0.6,
            stroke_color=GRAY_A, stroke_width=2
        ).move_to(UP * 3.3)
        bar_q_label = Text(
            "? 亩（全部）",
            font=FONT, font_size=20, color=GRAY_A
        ).next_to(bar_full, RIGHT, buff=0.15)
        self.play(Create(bar_full), FadeIn(bar_q_label), run_time=0.5)

        bar_35_w = 7.0 * 3.0 / 5.0   # 4.2
        # 左对齐放置
        bar_left_x = bar_full.get_left()[0]
        bar_35 = Rectangle(
            width=bar_35_w, height=0.8,
            fill_color=COLOR_GREEN, fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([bar_left_x + bar_35_w / 2, 3.3, 0]))

        bar_35_lbl1 = Text("3/5", font=FONT, font_size=22, color=COLOR_GREEN)
        bar_35_lbl2 = Text("= 12 亩", font=FONT, font_size=22, color=COLOR_GREEN)
        bar_35_label = VGroup(bar_35_lbl1, bar_35_lbl2).arrange(DOWN, buff=0.08).next_to(bar_35, DOWN, buff=0.12)

        self.play(Create(bar_35), run_time=0.5)
        self.play(FadeIn(bar_35_label), run_time=0.4)
        self.wait(0.4)

        # 分析
        analysis = Text(
            "分析思路：",
            font=FONT, font_size=26, color=COLOR_PURPLE
        ).move_to(UP * 2.1)
        self.play(FadeIn(analysis), run_time=0.4)

        eq_setup = Text(
            "设这块地有 x 亩",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.45)
        self.play(Write(eq_setup), run_time=0.5)

        eq_rel = MathTex(
            r"x \times \frac{3}{5} = 12",
            font_size=58
        ).move_to(UP * 0.65)
        eq_rel[0][0].set_color(COLOR_MAIN)
        self.play(Write(eq_rel), run_time=0.6)
        self.wait(0.3)

        # 求解
        solve_label = Text(
            "所以：",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 0.2 + LEFT * 3.0)
        solve1 = MathTex(
            r"x = 12 \div \frac{3}{5}",
            font_size=56
        ).move_to(DOWN * 0.2 + RIGHT * 0.8)
        solve1[0][0].set_color(COLOR_MAIN)
        self.play(FadeIn(solve_label), Write(solve1), run_time=0.6)

        solve2 = MathTex(
            r"= 12 \times \frac{5}{3}",
            font_size=56
        ).move_to(DOWN * 1.1)
        solve2[0].set_color(COLOR_ORANGE)
        self.play(Write(solve2), run_time=0.6)

        solve3_num = MathTex(
            r"= \frac{60}{3} = 20",
            font_size=64, color=COLOR_GREEN
        ).move_to(DOWN * 2.1)
        solve3_unit = Text(
            "亩",
            font=FONT, font_size=42, color=COLOR_GREEN
        ).next_to(solve3_num, RIGHT, buff=0.15)

        self.play(Write(solve3_num), FadeIn(solve3_unit), run_time=0.6)

        result_box = SurroundingRectangle(
            VGroup(solve3_num, solve3_unit),
            color=COLOR_GREEN, buff=0.18, corner_radius=0.12, stroke_width=3
        )
        self.play(Create(result_box), run_time=0.4)
        self.play(Indicate(VGroup(solve3_num, solve3_unit), scale_factor=1.1), run_time=0.5)

        ans_text = Text(
            "答：这块地有 20 亩。",
            font=FONT, font_size=26, color=COLOR_GREEN
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(ans_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, q1, q2,
            bar_full, bar_q_label, bar_35, bar_35_label,
            analysis, eq_setup, eq_rel,
            solve_label, solve1, solve2,
            solve3_num, solve3_unit,
            result_box, ans_text
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        """总结: 分数除法核心要点"""

        title = Text(
            "本节总结", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 卡片1: 倒数
        card1_box = RoundedRectangle(
            width=8.2, height=1.55, corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.82,
            stroke_color=COLOR_MAIN, stroke_width=2.5
        ).move_to(UP * 4.6)
        card1_title = Text(
            "倒数", font=FONT, font_size=26, color=COLOR_MAIN, weight=BOLD
        ).move_to(UP * 5.0)
        card1_body = Text(
            "乘积为 1 的两数互为倒数（0 无倒数）",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.4)

        self.play(Create(card1_box), run_time=0.4)
        self.play(Write(card1_title), Write(card1_body), run_time=0.6)

        # 卡片2: 核心法则
        card2_box = RoundedRectangle(
            width=8.2, height=2.4, corner_radius=0.2,
            fill_color="#2d1b4e", fill_opacity=0.88,
            stroke_color=COLOR_PURPLE, stroke_width=2.5
        ).move_to(UP * 2.75)
        card2_title = Text(
            "分数除法法则", font=FONT, font_size=26, color=COLOR_PURPLE, weight=BOLD
        ).move_to(UP * 3.35)
        card2_formula = MathTex(
            r"\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}",
            font_size=50
        ).move_to(UP * 2.7)
        card2_rule = Text(
            "除以一个数  ＝  乘以它的倒数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 2.1)

        self.play(Create(card2_box), run_time=0.4)
        self.play(Write(card2_title), run_time=0.4)
        self.play(Write(card2_formula), run_time=0.7)
        self.play(Write(card2_rule), run_time=0.5)

        # 卡片3: 例子速查
        card3_box = RoundedRectangle(
            width=8.2, height=2.2, corner_radius=0.2,
            fill_color="#1a2a1a", fill_opacity=0.85,
            stroke_color=COLOR_GREEN, stroke_width=2.5
        ).move_to(UP * 0.75)
        card3_title = Text(
            "例题速查", font=FONT, font_size=26, color=COLOR_GREEN, weight=BOLD
        ).move_to(UP * 1.25)
        card3_ex1 = MathTex(
            r"\frac{2}{3} \div \frac{3}{4} = \frac{2}{3} \times \frac{4}{3} = \frac{8}{9}",
            font_size=42
        ).move_to(UP * 0.6)
        card3_ex2 = MathTex(
            r"6 \div \frac{2}{3} = 6 \times \frac{3}{2} = 9",
            font_size=42
        ).move_to(UP * 0.0)

        self.play(Create(card3_box), run_time=0.4)
        self.play(Write(card3_title), run_time=0.3)
        self.play(Write(card3_ex1), run_time=0.7)
        self.play(Write(card3_ex2), run_time=0.6)

        # 卡片4: 应用题步骤
        card4_box = RoundedRectangle(
            width=8.2, height=2.0, corner_radius=0.2,
            fill_color="#2a1a1a", fill_opacity=0.85,
            stroke_color=COLOR_RED, stroke_width=2.5
        ).move_to(DOWN * 1.5)
        card4_title = Text(
            "应用题解题思路", font=FONT, font_size=26, color=COLOR_RED, weight=BOLD
        ).move_to(DOWN * 1.05)
        card4_s1 = Text(
            "① 设未知数（设原数为 x）",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 1.55)
        card4_s2 = Text(
            "② 列方程: x × 几分之几 = 已知数 → 用除法求 x",
            font=FONT, font_size=20, color=WHITE
        ).move_to(DOWN * 2.05)

        self.play(Create(card4_box), run_time=0.4)
        self.play(Write(card4_title), run_time=0.4)
        self.play(Write(card4_s1), run_time=0.5)
        self.play(Write(card4_s2), run_time=0.5)
        self.wait(1.2)

        # 口诀条
        slogan_bg = RoundedRectangle(
            width=7.5, height=0.95, corner_radius=0.15,
            fill_color="#3b3b00", fill_opacity=0.92,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 3.2)
        slogan = Text(
            "牢记：÷ 变 ×，除数变倒数！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 3.2)
        self.play(Create(slogan_bg), Write(slogan), run_time=0.7)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title,
            card1_box, card1_title, card1_body,
            card2_box, card2_title, card2_formula, card2_rule,
            card3_box, card3_title, card3_ex1, card3_ex2,
            card4_box, card4_title, card4_s1, card4_s2,
            slogan_bg, slogan
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        """片尾: 作者信息 + 关注提示"""

        # 标志性大公式
        big_formula = MathTex(
            r"\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}",
            font_size=56
        ).move_to(UP * 2.8)
        big_formula[0].set_color(COLOR_HL)
        self.play(Write(big_formula), run_time=0.9)

        # 星形装饰环绕公式
        star_positions = [
            np.array([3.2 * np.cos(i * TAU / 6), 3.2 * np.sin(i * TAU / 6) + 2.8, 0])
            for i in range(6)
        ]
        stars = VGroup(*[
            Star(n=5, outer_radius=0.22, fill_color=COLOR_HL, fill_opacity=0.9, stroke_width=0)
            .move_to(pos)
            for pos in star_positions
        ])
        self.play(LaggedStart(*[FadeIn(s, scale=0.3) for s in stars], lag_ratio=0.12), run_time=0.8)
        self.play(Rotate(stars, angle=TAU / 12, about_point=UP * 2.8, run_time=1.0))

        # 作者信息放大到中央
        self.play(
            self.author_mob.animate
                .move_to(UP * 0.9)
                .set_color(WHITE),
            run_time=0.7
        )
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.1)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        # 关注提示
        follow_bg = RoundedRectangle(
            width=7.5, height=1.1, corner_radius=0.2,
            fill_color="#1a3a1a", fill_opacity=0.9,
            stroke_color=COLOR_GREEN, stroke_width=2.5
        ).move_to(DOWN * 1.2)
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_GREEN
        ).move_to(DOWN * 1.2)
        self.play(Create(follow_bg), Write(follow_text), run_time=0.6)

        # 彩色点装饰
        dot_colors = [COLOR_MAIN, COLOR_GREEN, COLOR_PURPLE, COLOR_HL, COLOR_RED]
        dots_row = VGroup(*[
            Dot(radius=0.12, color=dot_colors[i])
            .move_to(np.array([-2.0 + i * 1.0, -2.6, 0]))
            for i in range(5)
        ])
        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in dots_row], lag_ratio=0.12), run_time=0.6)
        self.play(dots_row.animate.shift(UP * 0.25), run_time=0.35)
        self.play(dots_row.animate.shift(DOWN * 0.25), run_time=0.35)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            big_formula, stars,
            self.author_mob, author_id,
            follow_bg, follow_text, dots_row
        )), run_time=0.8)
