"""
003_带分数加减法.py — 带分数加减法 教学动画

知识点: 整数部分和分数部分分别相加减；不够减时借1当假分数再减
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 带分数加减法 — 分开来算！
  2. 带分数结构介绍
  3. 加法例题: 2又1/3 + 1又1/3 = 3又2/3
  4. 减法例题 (够减): 3又3/4 - 1又1/4 = 2又1/2
  5. 核心难点: 不够减时借1 (3又1/4 - 1又3/4)
  6. 综合例题: 3又1/4 - 1又1/2 (通分+借位)
  7. 总结口诀
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
BG_COLOR = "#1a1a2e"
COLOR_INT = "#3b82f6"        # 蓝色 — 整数部分
COLOR_FRAC = "#f59e0b"       # 橙色 — 分数部分
COLOR_RESULT = "#22c55e"     # 绿色结果
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_BORROW = "#ef4444"     # 红色 — 借位
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class MixedNumberLesson(Scene):
    """
    带分数加减法教学动画
    场景顺序:
      1. 开场钩子
      2. 带分数结构介绍
      3. 加法例题: 2又1/3 + 1又1/3
      4. 减法例题 (够减): 3又3/4 - 1又1/4
      5. 核心难点: 不够减时借1 (3又1/4 - 1又3/4)
      6. 综合例题: 3又1/4 - 1又1/2 (通分+借位)
      7. 总结口诀
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_structure()
        self.scene_3_addition()
        self.scene_4_subtraction_easy()
        self.scene_5_borrow_one()
        self.scene_6_combined()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: 带分数加减法"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        hook1 = Text(
            "带分数加减法",
            font=FONT, font_size=48, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "整数分开算，分数分开算！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)

        # 展示预览算式
        preview = MathTex(
            r"3\frac{1}{4} - 1\frac{1}{2} = \, ?",
            font_size=64
        ).move_to(UP * 1.5)
        preview.set_color(COLOR_HL)

        self.play(FadeIn(preview, scale=0.6), run_time=0.8)
        self.wait(1.0)

        # 清理
        self.play(FadeOut(VGroup(hook1, hook2, preview)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 带分数结构介绍
    # ------------------------------------------------------------------

    def scene_2_structure(self):
        """展示带分数的结构: 整数 + 真分数"""

        title = Text(
            "带分数的结构", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.4)

        # 展示 2又3/4 的结构
        mixed_num = MathTex(
            r"2\frac{3}{4}",
            font_size=96
        ).move_to(UP * 3.5)
        mixed_num.set_color(WHITE)

        self.play(Write(mixed_num), run_time=0.8)
        self.wait(0.4)

        # 标注整数部分 (first character is "2")
        int_label = Text(
            "整数部分", font=FONT, font_size=26, color=COLOR_INT
        ).move_to(UP * 1.8 + LEFT * 2.0)
        int_arrow = Arrow(
            start=int_label.get_right() + RIGHT * 0.1,
            end=mixed_num.get_left() + LEFT * 0.05,
            color=COLOR_INT, buff=0.1, stroke_width=3
        )
        self.play(
            FadeIn(int_label),
            GrowArrow(int_arrow),
            run_time=0.6
        )
        self.wait(0.3)

        # 标注分数部分
        frac_label = Text(
            "分数部分", font=FONT, font_size=26, color=COLOR_FRAC
        ).move_to(UP * 1.8 + RIGHT * 2.0)
        frac_arrow = Arrow(
            start=frac_label.get_left() + LEFT * 0.1,
            end=mixed_num.get_right() + RIGHT * 0.05,
            color=COLOR_FRAC, buff=0.1, stroke_width=3
        )
        self.play(
            FadeIn(frac_label),
            GrowArrow(frac_arrow),
            run_time=0.6
        )
        self.wait(0.4)

        # 展示加减法核心思想
        rule_box = RoundedRectangle(
            width=7.5, height=2.5,
            corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.7,
            stroke_color=COLOR_INT, stroke_width=2
        ).move_to(DOWN * 0.3)

        rule_line1 = Text(
            "整数部分 + 整数部分", font=FONT, font_size=26, color=COLOR_INT
        ).move_to(UP * 0.2)
        rule_line2 = Text(
            "分数部分 + 分数部分", font=FONT, font_size=26, color=COLOR_FRAC
        ).move_to(DOWN * 0.7)

        self.play(Create(rule_box), run_time=0.5)
        self.play(Write(rule_line1), run_time=0.5)
        self.play(Write(rule_line2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(
                title, mixed_num, int_label, int_arrow,
                frac_label, frac_arrow,
                rule_box, rule_line1, rule_line2
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 加法例题 2又1/3 + 1又1/3
    # ------------------------------------------------------------------

    def scene_3_addition(self):
        """加法: 2又1/3 + 1又1/3 = 3又2/3"""

        title = Text(
            "加法例题", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title), run_time=0.4)

        # 原式
        expr = MathTex(
            r"2\frac{1}{3}", r"+", r"1\frac{1}{3}", r"=",
            font_size=72
        ).move_to(UP * 4.0)
        expr[0].set_color(COLOR_INT)
        expr[2].set_color(COLOR_FRAC)

        self.play(Write(expr), run_time=0.8)
        self.wait(0.5)

        # 分解提示
        decomp_label = Text(
            "分开来算：", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 2.6)
        self.play(FadeIn(decomp_label), run_time=0.4)

        # 整数部分
        int_part_label = Text(
            "整数：", font=FONT, font_size=26, color=COLOR_INT
        ).move_to(UP * 1.6 + LEFT * 2.5)
        int_calc = MathTex(
            r"2 + 1 = 3",
            font_size=52
        ).next_to(int_part_label, RIGHT, buff=0.3)
        int_calc.set_color(COLOR_INT)

        self.play(FadeIn(int_part_label), Write(int_calc), run_time=0.6)
        self.wait(0.3)

        # 分数部分
        frac_part_label = Text(
            "分数：", font=FONT, font_size=26, color=COLOR_FRAC
        ).move_to(UP * 0.4 + LEFT * 2.5)
        frac_calc = MathTex(
            r"\frac{1}{3} + \frac{1}{3} = \frac{2}{3}",
            font_size=52
        ).next_to(frac_part_label, RIGHT, buff=0.3)
        frac_calc.set_color(COLOR_FRAC)

        self.play(FadeIn(frac_part_label), Write(frac_calc), run_time=0.6)
        self.wait(0.4)

        # 结果
        result_box = RoundedRectangle(
            width=5.5, height=1.5,
            corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 1.2)

        result = MathTex(
            r"2\frac{1}{3} + 1\frac{1}{3} = 3\frac{2}{3}",
            font_size=52
        ).move_to(DOWN * 1.2)
        result.set_color(COLOR_RESULT)

        self.play(Create(result_box), run_time=0.4)
        self.play(Write(result), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(
                title, expr, decomp_label,
                int_part_label, int_calc,
                frac_part_label, frac_calc,
                result_box, result
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 减法例题 (够减的情形) 3又3/4 - 1又1/4
    # ------------------------------------------------------------------

    def scene_4_subtraction_easy(self):
        """减法 (够减): 3又3/4 - 1又1/4 = 2又2/4 = 2又1/2"""

        title = Text(
            "减法例题（够减）", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title), run_time=0.4)

        # 原式
        expr = MathTex(
            r"3\frac{3}{4}", r"-", r"1\frac{1}{4}", r"=",
            font_size=68
        ).move_to(UP * 4.0)
        expr[0].set_color(COLOR_INT)
        expr[2].set_color(COLOR_FRAC)

        self.play(Write(expr), run_time=0.7)
        self.wait(0.5)

        # 整数部分
        int_part_label = Text(
            "整数：", font=FONT, font_size=26, color=COLOR_INT
        ).move_to(UP * 2.6 + LEFT * 2.5)
        int_calc = MathTex(
            r"3 - 1 = 2",
            font_size=52
        ).next_to(int_part_label, RIGHT, buff=0.3)
        int_calc.set_color(COLOR_INT)

        self.play(FadeIn(int_part_label), Write(int_calc), run_time=0.6)
        self.wait(0.3)

        # 分数部分
        frac_part_label = Text(
            "分数：", font=FONT, font_size=26, color=COLOR_FRAC
        ).move_to(UP * 1.3 + LEFT * 2.5)
        frac_calc = MathTex(
            r"\frac{3}{4} - \frac{1}{4} = \frac{2}{4}",
            font_size=48
        ).next_to(frac_part_label, RIGHT, buff=0.3)
        frac_calc.set_color(COLOR_FRAC)

        self.play(FadeIn(frac_part_label), Write(frac_calc), run_time=0.6)
        self.wait(0.4)

        # 合并结果
        step_result = MathTex(
            r"= 2\frac{2}{4}",
            font_size=60
        ).move_to(UP * 0.1)
        step_result.set_color(WHITE)
        self.play(Write(step_result), run_time=0.5)
        self.wait(0.4)

        # 约分提示
        simplify_arrow = Arrow(
            start=step_result.get_bottom() + DOWN * 0.1,
            end=step_result.get_bottom() + DOWN * 0.9,
            color=COLOR_ACCENT, buff=0
        )
        simplify_text = Text(
            "约分", font=FONT, font_size=26, color=COLOR_ACCENT
        ).next_to(simplify_arrow, RIGHT, buff=0.2)

        self.play(GrowArrow(simplify_arrow), FadeIn(simplify_text), run_time=0.5)

        # 最终结果
        result_box = RoundedRectangle(
            width=4.5, height=1.5,
            corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 2.0)

        final_result = MathTex(
            r"= 2\frac{1}{2}",
            font_size=64
        ).move_to(DOWN * 2.0)
        final_result.set_color(COLOR_RESULT)

        self.play(Create(result_box), run_time=0.3)
        self.play(Write(final_result), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(
                title, expr,
                int_part_label, int_calc,
                frac_part_label, frac_calc,
                step_result, simplify_arrow, simplify_text,
                result_box, final_result
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 核心难点 — 借1 (3又1/4 - 1又3/4)
    # ------------------------------------------------------------------

    def scene_5_borrow_one(self):
        """核心: 分数部分不够减时，从整数部分借1"""

        title = Text(
            "分数不够减？借1！", font=FONT, font_size=38,
            color=COLOR_BORROW, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title), run_time=0.4)

        # 原式
        expr = MathTex(
            r"3\frac{1}{4}", r"-", r"1\frac{3}{4}",
            font_size=72
        ).move_to(UP * 4.0)
        expr[0].set_color(COLOR_INT)
        expr[2].set_color(COLOR_FRAC)

        self.play(Write(expr), run_time=0.7)
        self.wait(0.5)

        # 提出问题
        question = Text(
            "分数部分：", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 2.8 + LEFT * 1.8)
        frac_compare = MathTex(
            r"\frac{1}{4} < \frac{3}{4}",
            font_size=52
        ).next_to(question, RIGHT, buff=0.3)
        frac_compare.set_color(COLOR_BORROW)

        self.play(FadeIn(question), Write(frac_compare), run_time=0.6)
        self.wait(0.3)

        not_enough = Text(
            "不够减！", font=FONT, font_size=32, color=COLOR_BORROW, weight=BOLD
        ).move_to(UP * 2.0)
        self.play(
            Indicate(frac_compare, color=COLOR_BORROW, scale_factor=1.2),
            run_time=0.5
        )
        self.play(Write(not_enough), run_time=0.4)
        self.wait(0.4)

        # 借1的过程
        borrow_title = Text(
            "从整数3借1：", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 1.1)
        self.play(FadeIn(borrow_title), run_time=0.4)

        # 逐步展示借1
        borrow_line1 = MathTex(
            r"3\frac{1}{4} = 2 + 1 + \frac{1}{4}",
            font_size=44
        ).move_to(UP * 0.2)
        borrow_line1.set_color(WHITE)

        borrow_line2 = MathTex(
            r"= 2 + \frac{4}{4} + \frac{1}{4}",
            font_size=44
        ).move_to(DOWN * 0.7)
        borrow_line2.set_color(COLOR_FRAC)

        borrow_line3 = MathTex(
            r"= 2\frac{5}{4}",
            font_size=52
        ).move_to(DOWN * 1.6)
        borrow_line3.set_color(COLOR_HL)

        self.play(Write(borrow_line1), run_time=0.5)
        self.wait(0.2)
        self.play(Write(borrow_line2), run_time=0.5)
        self.wait(0.2)
        self.play(Write(borrow_line3), run_time=0.5)
        self.wait(0.4)

        # 完整计算
        full_calc = MathTex(
            r"3\frac{1}{4} - 1\frac{3}{4} = 2\frac{5}{4} - 1\frac{3}{4}",
            font_size=40
        ).move_to(DOWN * 2.8)
        full_calc.set_color(WHITE)
        self.play(Write(full_calc), run_time=0.6)
        self.wait(0.3)

        # 结果
        result_box = RoundedRectangle(
            width=5.5, height=1.5,
            corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 4.3)

        result = MathTex(
            r"= 1\frac{2}{4} = 1\frac{1}{2}",
            font_size=56
        ).move_to(DOWN * 4.3)
        result.set_color(COLOR_RESULT)

        self.play(Create(result_box), run_time=0.3)
        self.play(Write(result), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, expr, question, frac_compare, not_enough,
                borrow_title, borrow_line1, borrow_line2, borrow_line3,
                full_calc, result_box, result
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 6: 综合例题 3又1/4 - 1又1/2 (通分+借位)
    # ------------------------------------------------------------------

    def scene_6_combined(self):
        """综合例题: 3又1/4 - 1又1/2 = 1又3/4 (需通分再借位)"""

        title = Text(
            "综合例题", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title), run_time=0.4)

        # 原式
        expr = MathTex(
            r"3\frac{1}{4}", r"-", r"1\frac{1}{2}",
            font_size=72
        ).move_to(UP * 4.3)
        expr[0].set_color(COLOR_INT)
        expr[2].set_color(COLOR_FRAC)

        self.play(Write(expr), run_time=0.7)
        self.wait(0.5)

        # Step 1: 通分
        step1_label = Text(
            "第一步：通分", font=FONT, font_size=30, color=COLOR_ACCENT
        ).move_to(UP * 3.1)
        self.play(FadeIn(step1_label), run_time=0.4)

        step1_eq = MathTex(
            r"1\frac{1}{2} = 1\frac{2}{4}",
            font_size=52
        ).move_to(UP * 2.2)
        step1_eq.set_color(COLOR_FRAC)
        self.play(Write(step1_eq), run_time=0.6)
        self.wait(0.4)

        # 变成
        after_convert = MathTex(
            r"3\frac{1}{4} - 1\frac{2}{4}",
            font_size=58
        ).move_to(UP * 1.2)
        after_convert.set_color(WHITE)
        self.play(Write(after_convert), run_time=0.6)
        self.wait(0.4)

        # Step 2: 检查能否直接减
        step2_label = Text(
            "第二步：分数够减吗？", font=FONT, font_size=28, color=COLOR_ACCENT
        ).move_to(UP * 0.3)
        self.play(FadeIn(step2_label), run_time=0.4)

        check = MathTex(
            r"\frac{1}{4} < \frac{2}{4}",
            font_size=52
        ).move_to(DOWN * 0.6)
        check.set_color(COLOR_BORROW)
        self.play(Write(check), run_time=0.5)

        not_enough2 = Text(
            "不够减！需要借1", font=FONT, font_size=28, color=COLOR_BORROW, weight=BOLD
        ).move_to(DOWN * 1.5)
        self.play(
            Indicate(check, color=COLOR_BORROW, scale_factor=1.1),
            run_time=0.5
        )
        self.play(Write(not_enough2), run_time=0.4)
        self.wait(0.3)

        # Step 3: 借1
        step3_label = Text(
            "第三步：借1", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 2.4)
        borrow_result = MathTex(
            r"3\frac{1}{4} = 2\frac{5}{4}",
            font_size=52
        ).move_to(DOWN * 3.3)
        borrow_result.set_color(COLOR_HL)

        self.play(FadeIn(step3_label), run_time=0.4)
        self.play(Write(borrow_result), run_time=0.6)
        self.wait(0.4)

        # Step 4: 计算结果
        step4_eq = MathTex(
            r"2\frac{5}{4} - 1\frac{2}{4}",
            font_size=54
        ).move_to(DOWN * 4.3)
        step4_eq.set_color(WHITE)
        self.play(Write(step4_eq), run_time=0.5)
        self.wait(0.3)

        # 最终结果
        result_box = RoundedRectangle(
            width=4.5, height=1.5,
            corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 5.6)

        final_ans = MathTex(
            r"= 1\frac{3}{4}",
            font_size=68
        ).move_to(DOWN * 5.6)
        final_ans.set_color(COLOR_RESULT)

        self.play(Create(result_box), run_time=0.3)
        self.play(Write(final_ans), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, expr, step1_label, step1_eq, after_convert,
                step2_label, check, not_enough2,
                step3_label, borrow_result, step4_eq,
                result_box, final_ans
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结口诀
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        """总结带分数加减法的口诀"""

        title = Text(
            "记住这4步！", font=FONT, font_size=44,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title), run_time=0.4)

        # 大框
        summary_box = RoundedRectangle(
            width=8.0, height=8.5,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(DOWN * 0.5)
        self.play(Create(summary_box), run_time=0.4)

        # 步骤
        steps = [
            ("①", "通分（分母不同时）", COLOR_ACCENT),
            ("②", "整数部分分别算", COLOR_INT),
            ("③", "分数部分分别算", COLOR_FRAC),
            ("④", "不够减时借1，\n化为假分数再减", COLOR_BORROW),
        ]

        step_mobs = VGroup()
        for num, text, color in steps:
            num_mob = Text(
                num, font=FONT, font_size=36, color=color, weight=BOLD
            )
            text_mob = Text(
                text, font=FONT, font_size=26, color=WHITE
            )
            row = VGroup(num_mob, text_mob).arrange(RIGHT, buff=0.4, aligned_edge=UP)
            step_mobs.add(row)

        step_mobs.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        step_mobs.move_to(UP * 1.8)

        for row in step_mobs:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 提醒: 结果约分
        remind_box = RoundedRectangle(
            width=7.0, height=1.2,
            corner_radius=0.15,
            fill_color="#1e3a5f", fill_opacity=0.8,
            stroke_color=COLOR_RESULT, stroke_width=1.5
        ).move_to(DOWN * 2.7)
        remind_text = Text(
            "结果能约分要约分！", font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 2.7)

        self.play(Create(remind_box), run_time=0.3)
        self.play(Write(remind_text), run_time=0.5)
        self.wait(0.5)

        # 核心算式展示
        core_eq = MathTex(
            r"3\frac{1}{4} - 1\frac{1}{2} = 1\frac{3}{4}",
            font_size=48
        ).move_to(DOWN * 4.2)
        core_eq.set_color(COLOR_HL)
        self.play(Write(core_eq), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, summary_box, step_mobs,
                remind_box, remind_text, core_eq
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        """片尾: 作者信息 + 关注提示"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE, weight=BOLD
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=COLOR_AUTHOR
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author_mob, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)

        # 装饰: 分数符号
        deco = VGroup()
        positions = [
            LEFT * 3.0 + DOWN * 2.0,
            RIGHT * 3.0 + DOWN * 2.0,
            LEFT * 1.5 + DOWN * 3.5,
            RIGHT * 1.5 + DOWN * 3.5,
        ]
        fracs = [
            r"2\frac{1}{3}",
            r"1\frac{3}{4}",
            r"3\frac{1}{2}",
            r"4\frac{2}{5}",
        ]
        colors = [COLOR_INT, COLOR_FRAC, COLOR_ACCENT, COLOR_RESULT]

        for pos, frac, col in zip(positions, fracs, colors):
            mob = MathTex(frac, font_size=40).move_to(pos)
            mob.set_color(col)
            deco.add(mob)

        self.play(
            *[FadeIn(d, scale=0.7) for d in deco],
            run_time=0.6
        )

        self.play(
            *[d.animate.shift(UP * 0.3) for d in deco],
            run_time=1.0, rate_func=there_and_back
        )

        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                self.author_mob, author_id, follow_text, deco
            )),
            run_time=0.8
        )
