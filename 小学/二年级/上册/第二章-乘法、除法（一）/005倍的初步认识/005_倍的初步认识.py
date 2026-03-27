"""
005_倍的初步认识.py — 倍的初步认识 教学动画

知识点: 倍的概念 — 比较两个数量时，如果较大数里有几个较小数，
        就说较大数是较小数的"几倍"。
        求一个数的几倍用乘法；求一个数是另一个数的几倍用除法。
年级: 二年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  1. 开场钩子
  2. 认识"倍" — 图形直观理解（草莓例子）
  3. 求"几倍是多少" — 乘法（5的3倍=15）
  4. 求"是几倍" — 除法（15是5的几倍）
  5. 方法总结
  6. 小练习
  7. 片尾
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
BG_COLOR    = "#1a1a2e"
COLOR_A     = "#3b82f6"   # 蓝 — 基准数量
COLOR_B     = "#f59e0b"   # 橙 — 倍数后数量
COLOR_HL    = "#fbbf24"   # 黄高亮
COLOR_MULT  = "#22c55e"   # 绿 — 乘法
COLOR_DIV   = "#a78bfa"   # 紫 — 除法
COLOR_RULE  = "#f472b6"   # 粉 — 规则
COLOR_CARD  = "#0f172a"
COLOR_AUTHOR = "#6b7280"
FONT        = "Noto Sans CJK SC"


class MultipleIntroLesson(Scene):
    """
    倍的初步认识 教学动画
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_concept()
        self.scene_3_mult()
        self.scene_4_div()
        self.scene_5_summary()
        self.scene_6_practice()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "倍的初步认识", font=FONT, font_size=52,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)

        hook2 = Text(
            '什么是"倍"？', font=FONT, font_size=38,
            color=COLOR_HL
        ).move_to(UP * 4.2)

        self.play(Write(hook1), run_time=0.7)
        self.play(Write(hook2), run_time=0.6)

        # 展示核心问题
        question_line1 = Text(
            "3的2倍是多少？", font=FONT, font_size=32, color=COLOR_A
        ).move_to(UP * 2.2)
        question_line2 = Text(
            "6是3的几倍？", font=FONT, font_size=32, color=COLOR_B
        ).move_to(UP * 1.2)

        self.play(FadeIn(question_line1, shift=LEFT * 0.3), run_time=0.6)
        self.play(FadeIn(question_line2, shift=LEFT * 0.3), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(hook1, hook2, question_line1, question_line2)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 认识"倍" — 直观图形
    # ------------------------------------------------------------------
    def scene_2_concept(self):
        title = Text(
            '认识"倍"', font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # --- 第1行：草莓基准组（3个） ---
        intro1 = Text(
            "第一行放了 3 个草莓：", font=FONT,
            font_size=26, color=GRAY_A
        ).move_to(UP * 4.8)
        self.play(FadeIn(intro1, shift=RIGHT * 0.2), run_time=0.5)

        row1 = self._make_berry_row(count=3, color=COLOR_A, y=3.5)
        self.play(FadeIn(row1, lag_ratio=0.25), run_time=0.8)
        self.wait(0.3)

        # 花括号 + 标注
        brace1 = Brace(row1, DOWN, buff=0.12, color=COLOR_A)
        label1 = Text("3 个", font=FONT, font_size=24, color=COLOR_A
                      ).next_to(brace1, DOWN, buff=0.12)
        self.play(FadeIn(brace1), FadeIn(label1), run_time=0.4)
        self.wait(0.3)

        # --- 第2行：2倍行（6个 = 2组×3个） ---
        intro2 = Text(
            '第二行放了 2 个"3"，即 2 倍：',
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 2.2)
        self.play(FadeIn(intro2, shift=RIGHT * 0.2), run_time=0.5)

        row2_g1 = self._make_berry_row(count=3, color=COLOR_B, y=1.3, x_offset=-1.55)
        row2_g2 = self._make_berry_row(count=3, color=COLOR_B, y=1.3, x_offset=1.55)

        # 先画分组框
        box_g1 = RoundedRectangle(
            width=2.8, height=0.85, corner_radius=0.18,
            stroke_color=COLOR_B, stroke_width=2,
            fill_color=COLOR_B, fill_opacity=0.12
        ).move_to(np.array([-1.55, 1.3, 0]))
        box_g2 = RoundedRectangle(
            width=2.8, height=0.85, corner_radius=0.18,
            stroke_color=COLOR_B, stroke_width=2,
            fill_color=COLOR_B, fill_opacity=0.12
        ).move_to(np.array([1.55, 1.3, 0]))

        self.play(FadeIn(box_g1), run_time=0.3)
        self.play(FadeIn(row2_g1, lag_ratio=0.25), run_time=0.6)
        self.play(FadeIn(box_g2), run_time=0.3)
        self.play(FadeIn(row2_g2, lag_ratio=0.25), run_time=0.6)

        # 花括号 + 标注
        row2_all = VGroup(row2_g1, row2_g2, box_g1, box_g2)
        brace2 = Brace(VGroup(row2_g1, row2_g2), DOWN, buff=0.12, color=COLOR_B)
        label2 = Text("6 个 = 2个3", font=FONT, font_size=24, color=COLOR_B
                      ).next_to(brace2, DOWN, buff=0.12)
        self.play(FadeIn(brace2), FadeIn(label2), run_time=0.4)
        self.wait(0.4)

        # --- 核心结论 ---
        conclusion_box = RoundedRectangle(
            width=8.0, height=1.8, corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(conclusion_box), run_time=0.3)

        concl = Text(
            "6 是 3 的 2 倍",
            font=FONT, font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(conclusion_box.get_center() + UP * 0.22)
        concl_sub = Text(
            "6 里面有 2 个 3",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(conclusion_box.get_center() + DOWN * 0.38)
        self.play(Write(concl), run_time=0.7)
        self.play(FadeIn(concl_sub), run_time=0.4)
        self.play(Indicate(concl, scale_factor=1.08, color=COLOR_HL), run_time=0.5)
        self.wait(1.5)

        # --- 推广：3倍的情形 ---
        expand_title = Text(
            "如果放 3 倍呢？", font=FONT, font_size=26,
            color=COLOR_RULE
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(expand_title, shift=UP * 0.2), run_time=0.5)

        row3_g1 = self._make_berry_row(count=3, color=COLOR_RULE, y=-4.6, x_offset=-3.1)
        row3_g2 = self._make_berry_row(count=3, color=COLOR_RULE, y=-4.6, x_offset=0.0)
        row3_g3 = self._make_berry_row(count=3, color=COLOR_RULE, y=-4.6, x_offset=3.1)
        for rg in [row3_g1, row3_g2, row3_g3]:
            self.play(FadeIn(rg, lag_ratio=0.25), run_time=0.4)

        row3_label = Text(
            "9 个 = 3个3  →  9是3的3倍",
            font=FONT, font_size=22, color=COLOR_RULE
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(row3_label), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, intro1, intro2,
                row1, brace1, label1,
                row2_all, brace2, label2,
                conclusion_box, concl, concl_sub,
                expand_title,
                row3_g1, row3_g2, row3_g3, row3_label
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 求"几倍是多少" — 乘法
    # ------------------------------------------------------------------
    def scene_3_mult(self):
        title = Text(
            "求几倍是多少 → 用乘法",
            font=FONT, font_size=34, color=COLOR_MULT, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # 问题呈现
        q_lead = Text(
            "问：5 的 3 倍是多少？",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(q_lead), run_time=0.6)
        self.wait(0.3)

        # --- 直观图：3组，每组5个方块 ---
        group_label_y = 3.4
        blocks_y = 2.7
        colors_3 = ["#3b82f6", "#f59e0b", "#22c55e"]
        all_block_groups = VGroup()
        group_braces = VGroup()
        group_labels = VGroup()

        x_starts = [-3.0, -0.15, 2.7]   # 每组起始x

        for g in range(3):
            grp = VGroup()
            for k in range(5):
                sq = Square(
                    side_length=0.48,
                    fill_color=colors_3[g], fill_opacity=0.85,
                    stroke_color=WHITE, stroke_width=1.2
                ).move_to(np.array([x_starts[g] + k * 0.52, blocks_y, 0]))
                grp.add(sq)
            all_block_groups.add(grp)

            # 括弧 + 数字标注
            br = Brace(grp, DOWN, buff=0.08, color=colors_3[g])
            lbl = Text("5", font=FONT, font_size=22, color=colors_3[g]
                       ).next_to(br, DOWN, buff=0.08)
            group_braces.add(br)
            group_labels.add(lbl)

        # 组编号
        group_nums = VGroup(*[
            Text(f"第{['一','二','三'][g]}组", font=FONT, font_size=20, color=colors_3[g]
                 ).move_to(np.array([x_starts[g] + 1.04, group_label_y, 0]))
            for g in range(3)
        ])

        for g in range(3):
            self.play(
                FadeIn(group_nums[g]),
                FadeIn(all_block_groups[g], lag_ratio=0.2),
                run_time=0.6
            )
        self.play(
            FadeIn(group_braces), FadeIn(group_labels),
            run_time=0.4
        )
        self.wait(0.3)

        # 大括号：全部 = 3组
        big_brace = Brace(all_block_groups, DOWN, buff=0.55, color=COLOR_HL)
        big_label = Text("3 组（3倍）", font=FONT, font_size=24, color=COLOR_HL
                         ).next_to(big_brace, DOWN, buff=0.1)
        self.play(FadeIn(big_brace), FadeIn(big_label), run_time=0.4)
        self.wait(0.3)

        # 思考框：5 × 3 = ?
        think_box = RoundedRectangle(
            width=8.0, height=3.5, corner_radius=0.25,
            fill_color=COLOR_CARD, fill_opacity=0.95,
            stroke_color=COLOR_MULT, stroke_width=2
        ).move_to(DOWN * 0.6)
        self.play(FadeIn(think_box), run_time=0.3)

        think_lead = Text(
            "3倍 就是 3个5 相加：",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(think_box.get_top() + DOWN * 0.6)
        self.play(FadeIn(think_lead), run_time=0.4)

        # 加法先写
        add_eq = MathTex(
            r"5 + 5 + 5 = 15",
            font_size=38, color=WHITE
        ).move_to(think_box.get_center() + UP * 0.25)
        self.play(Write(add_eq), run_time=0.8)
        self.wait(0.3)

        # 转为乘法
        arrow_to_mult = Arrow(
            start=add_eq.get_bottom() + DOWN * 0.05,
            end=add_eq.get_bottom() + DOWN * 0.75,
            color=COLOR_MULT, stroke_width=4, buff=0.0
        )
        self.play(GrowArrow(arrow_to_mult), run_time=0.4)

        mult_eq = MathTex(
            r"5 \times 3 = 15",
            font_size=44, color=COLOR_MULT
        ).move_to(think_box.get_bottom() + UP * 0.65)
        self.play(Write(mult_eq), run_time=0.7)
        self.play(Indicate(mult_eq, scale_factor=1.08, color=COLOR_HL), run_time=0.5)
        self.wait(0.5)

        # 结论框
        ans_box = RoundedRectangle(
            width=8.0, height=1.5, corner_radius=0.2,
            fill_color="#064e3b", fill_opacity=0.9,
            stroke_color=COLOR_MULT, stroke_width=2.5
        ).move_to(DOWN * 3.2)
        self.play(FadeIn(ans_box), run_time=0.3)
        ans_text = Text(
            "5 的 3 倍 = 5 × 3 = 15",
            font=FONT, font_size=30, color=COLOR_MULT, weight=BOLD
        ).move_to(ans_box.get_center())
        self.play(Write(ans_text), run_time=0.6)
        self.wait(0.4)

        # 规则说明
        rule = Text(
            "求一个数的几倍  →  用乘法",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(VGroup(
                title, q_lead,
                all_block_groups, group_braces, group_labels, group_nums,
                big_brace, big_label,
                think_box, think_lead, add_eq, arrow_to_mult, mult_eq,
                ans_box, ans_text, rule
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 求"是几倍" — 除法
    # ------------------------------------------------------------------
    def scene_4_div(self):
        title = Text(
            "求是几倍 → 用除法",
            font=FONT, font_size=34, color=COLOR_DIV, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        q_lead = Text(
            "问：15 是 5 的几倍？",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(q_lead), run_time=0.6)
        self.wait(0.3)

        # 直观图：15个方块，每5个一组
        blocks_y = 3.6
        colors_div = ["#3b82f6", "#f59e0b", "#22c55e"]
        x_starts_div = [-3.0, -0.15, 2.7]
        all_div_groups = VGroup()
        div_braces = VGroup()

        for g in range(3):
            grp = VGroup()
            for k in range(5):
                sq = Square(
                    side_length=0.48,
                    fill_color=colors_div[g], fill_opacity=0.85,
                    stroke_color=WHITE, stroke_width=1.2
                ).move_to(np.array([x_starts_div[g] + k * 0.52, blocks_y, 0]))
                grp.add(sq)
            all_div_groups.add(grp)
            br = Brace(grp, UP, buff=0.06, color=colors_div[g])
            div_braces.add(br)

        for g in range(3):
            self.play(FadeIn(all_div_groups[g], lag_ratio=0.2), run_time=0.4)
        self.play(FadeIn(div_braces), run_time=0.3)

        total_brace = Brace(all_div_groups, UP, buff=0.48, color=COLOR_HL)
        total_label = Text("15 个", font=FONT, font_size=24, color=COLOR_HL
                           ).next_to(total_brace, UP, buff=0.1)
        self.play(FadeIn(total_brace), FadeIn(total_label), run_time=0.4)
        self.wait(0.3)

        # 思考框
        think_box2 = RoundedRectangle(
            width=8.0, height=3.8, corner_radius=0.25,
            fill_color=COLOR_CARD, fill_opacity=0.95,
            stroke_color=COLOR_DIV, stroke_width=2
        ).move_to(DOWN * 0.4)
        self.play(FadeIn(think_box2), run_time=0.3)

        think_lead2 = Text(
            "每组 5 个，一共能分几组？",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(think_box2.get_top() + DOWN * 0.6)
        self.play(FadeIn(think_lead2), run_time=0.4)

        # 数数框
        count_row = VGroup()
        for g in range(3):
            mini_box = RoundedRectangle(
                width=1.6, height=0.9, corner_radius=0.15,
                fill_color=colors_div[g], fill_opacity=0.25,
                stroke_color=colors_div[g], stroke_width=2
            ).move_to(think_box2.get_center() + UP * 0.55 + RIGHT * (g - 1) * 2.0)
            num_t = Text(
                f"第{['1','2','3'][g]}组", font=FONT, font_size=20, color=colors_div[g]
            ).move_to(mini_box.get_center())
            count_row.add(VGroup(mini_box, num_t))
        self.play(FadeIn(count_row, lag_ratio=0.3), run_time=0.8)
        self.wait(0.3)

        # 除法算式
        arrow_div = Arrow(
            start=think_box2.get_center() + UP * 0.0,
            end=think_box2.get_center() + DOWN * 0.65,
            color=COLOR_DIV, stroke_width=4, buff=0.0
        )
        self.play(GrowArrow(arrow_div), run_time=0.4)

        div_eq = MathTex(
            r"15 \div 5 = 3",
            font_size=46, color=COLOR_DIV
        ).move_to(think_box2.get_bottom() + UP * 0.7)
        self.play(Write(div_eq), run_time=0.7)
        self.play(Indicate(div_eq, scale_factor=1.08, color=COLOR_HL), run_time=0.5)
        self.wait(0.5)

        # 结论框
        ans_box2 = RoundedRectangle(
            width=8.0, height=1.6, corner_radius=0.2,
            fill_color="#2e1065", fill_opacity=0.9,
            stroke_color=COLOR_DIV, stroke_width=2.5
        ).move_to(DOWN * 3.4)
        self.play(FadeIn(ans_box2), run_time=0.3)
        ans_text2 = Text(
            "15 ÷ 5 = 3，所以 15 是 5 的 3 倍",
            font=FONT, font_size=24, color=COLOR_DIV, weight=BOLD
        ).move_to(ans_box2.get_center())
        self.play(Write(ans_text2), run_time=0.7)
        self.wait(0.4)

        rule2 = Text(
            "求一个数是另一个数的几倍  →  用除法",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(rule2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(VGroup(
                title, q_lead,
                all_div_groups, div_braces, total_brace, total_label,
                think_box2, think_lead2, count_row, arrow_div, div_eq,
                ans_box2, ans_text2, rule2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 方法总结
    # ------------------------------------------------------------------
    def scene_5_summary(self):
        card = RoundedRectangle(
            width=8.5, height=11.0, corner_radius=0.35,
            fill_color=COLOR_CARD, fill_opacity=0.97,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(card), run_time=0.3)

        sum_title = Text(
            "倍的知识总结", font=FONT,
            font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(sum_title), run_time=0.5)

        # 定义块
        def_box = RoundedRectangle(
            width=7.8, height=2.2, corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=COLOR_A, stroke_width=1.5
        ).move_to(UP * 4.0)
        def_title = Text(
            '什么是"倍"？', font=FONT, font_size=24, color=COLOR_A, weight=BOLD
        ).move_to(def_box.get_top() + DOWN * 0.45)
        def_body = Text(
            "一个数里有几个另一个数，\n就说这个数是那个数的几倍",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(def_box.get_center() + DOWN * 0.15)
        self.play(FadeIn(def_box), run_time=0.3)
        self.play(FadeIn(def_title), FadeIn(def_body), run_time=0.5)
        self.wait(0.3)

        # 乘法块
        mult_box = RoundedRectangle(
            width=7.8, height=3.2, corner_radius=0.2,
            fill_color="#052e16", fill_opacity=0.9,
            stroke_color=COLOR_MULT, stroke_width=1.5
        ).move_to(UP * 1.3)
        mult_title_t = Text(
            "求几倍是多少  →  乘法",
            font=FONT, font_size=24, color=COLOR_MULT, weight=BOLD
        ).move_to(mult_box.get_top() + DOWN * 0.48)

        mult_ex_line1 = Text(
            "例：5的3倍是多少？",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(mult_box.get_center() + UP * 0.38)

        mult_eq = MathTex(
            r"5 \times 3 = 15",
            font_size=36, color=COLOR_MULT
        ).move_to(mult_box.get_center() + DOWN * 0.35)

        self.play(FadeIn(mult_box), run_time=0.3)
        self.play(FadeIn(mult_title_t), FadeIn(mult_ex_line1), run_time=0.4)
        self.play(Write(mult_eq), run_time=0.5)
        self.wait(0.3)

        # 除法块
        div_box = RoundedRectangle(
            width=7.8, height=3.2, corner_radius=0.2,
            fill_color="#2e1065", fill_opacity=0.9,
            stroke_color=COLOR_DIV, stroke_width=1.5
        ).move_to(DOWN * 1.9)
        div_title_t = Text(
            "求是几倍  →  除法",
            font=FONT, font_size=24, color=COLOR_DIV, weight=BOLD
        ).move_to(div_box.get_top() + DOWN * 0.48)

        div_ex_line1 = Text(
            "例：15是5的几倍？",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(div_box.get_center() + UP * 0.38)

        div_eq = MathTex(
            r"15 \div 5 = 3",
            font_size=36, color=COLOR_DIV
        ).move_to(div_box.get_center() + DOWN * 0.35)

        self.play(FadeIn(div_box), run_time=0.3)
        self.play(FadeIn(div_title_t), FadeIn(div_ex_line1), run_time=0.4)
        self.play(Write(div_eq), run_time=0.5)
        self.wait(0.3)

        # 关键提示
        key_tip = Text(
            "乘法和除法互为逆运算！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(key_tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                card, sum_title,
                def_box, def_title, def_body,
                mult_box, mult_title_t, mult_ex_line1, mult_eq,
                div_box, div_title_t, div_ex_line1, div_eq,
                key_tip
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 小练习
    # ------------------------------------------------------------------
    def scene_6_practice(self):
        title = Text(
            "试一试！", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 练习数据：(问题文字, 计算式文本, LaTeX答案式, 答案颜色)
        practices = [
            (
                "2 的 4 倍是多少？",
                "求几倍是多少  →  乘法",
                r"2 \times 4 = 8",
                COLOR_MULT,
                "答：8"
            ),
            (
                "12 是 3 的几倍？",
                "求是几倍  →  除法",
                r"12 \div 3 = 4",
                COLOR_DIV,
                "答：4 倍"
            ),
            (
                "6 的 5 倍是多少？",
                "求几倍是多少  →  乘法",
                r"6 \times 5 = 30",
                COLOR_MULT,
                "答：30"
            ),
        ]

        y_centers = [UP * 4.5, UP * 0.5, DOWN * 3.5]
        all_prac_mobs = VGroup()

        for i, (q_txt, method_txt, eq_tex, eq_color, ans_txt) in enumerate(practices):
            yc = y_centers[i]

            # 问题框
            p_box = RoundedRectangle(
                width=8.2, height=3.6, corner_radius=0.2,
                fill_color=COLOR_CARD, fill_opacity=0.95,
                stroke_color=eq_color, stroke_width=1.5
            ).move_to(yc)

            q_label = Text(
                f"第{['一','二','三'][i]}题：{q_txt}",
                font=FONT, font_size=24, color=WHITE
            ).move_to(yc + UP * 1.1)

            method_label = Text(
                method_txt,
                font=FONT, font_size=20, color=GRAY_A
            ).move_to(yc + UP * 0.3)

            eq_mob = MathTex(eq_tex, font_size=36, color=eq_color
                             ).move_to(yc + DOWN * 0.45)

            ans_mob = Text(ans_txt, font=FONT, font_size=22,
                           color=eq_color, weight=BOLD
                           ).move_to(yc + DOWN * 1.15)

            group = VGroup(p_box, q_label, method_label, eq_mob, ans_mob)
            all_prac_mobs.add(group)

            self.play(FadeIn(p_box), run_time=0.25)
            self.play(Write(q_label), run_time=0.5)
            self.play(FadeIn(method_label, shift=RIGHT * 0.2), run_time=0.4)
            self.play(Write(eq_mob), run_time=0.5)
            self.play(FadeIn(ans_mob, scale=1.1), run_time=0.4)
            self.wait(0.4)

        cheer = Text(
            "你都答对了吗？", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 7.0)
        all_prac_mobs.add(cheer)
        self.play(FadeIn(cheer, scale=1.1), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(VGroup(title, all_prac_mobs)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------
    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：彩色"倍"字环绕
        deco = VGroup(*[
            Text(
                "倍",
                font=FONT, font_size=24,
                color=[COLOR_A, COLOR_B, COLOR_MULT, COLOR_DIV, COLOR_RULE,
                       COLOR_HL][i % 6]
            ).move_to(
                follow.get_center()
                + 2.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        for d in deco:
            self.play(FadeIn(d, scale=0.5), run_time=0.15)

        self.play(Rotate(deco, angle=PI, run_time=1.2))
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, deco)),
            run_time=0.8
        )

    # ------------------------------------------------------------------
    # 工具函数
    # ------------------------------------------------------------------
    def _make_berry_row(self, count: int, color: str, y: float,
                        x_offset: float = 0.0) -> VGroup:
        """创建一行草莓形状（用圆形代替）"""
        row = VGroup()
        spacing = 0.68
        total_width = (count - 1) * spacing
        for i in range(count):
            x = x_offset + (-total_width / 2 + i * spacing)
            circle = Circle(
                radius=0.25,
                fill_color=color, fill_opacity=0.88,
                stroke_color=WHITE, stroke_width=1.5
            ).move_to(np.array([x, y, 0]))
            # 小叶子（三角形装饰）
            leaf = Triangle(
                fill_color=COLOR_MULT, fill_opacity=0.7,
                stroke_width=0
            ).scale(0.12).move_to(np.array([x, y + 0.28, 0]))
            row.add(VGroup(circle, leaf))
        return row


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 005_倍的初步认识.py MultipleIntroLesson
#   中等质量:  manim -qm  005_倍的初步认识.py MultipleIntroLesson
#   高质量:    manim -qh  005_倍的初步认识.py MultipleIntroLesson
# ======================================================================
