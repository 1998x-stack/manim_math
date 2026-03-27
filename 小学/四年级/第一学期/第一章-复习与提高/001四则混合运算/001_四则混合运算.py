"""
001_四则混合运算.py — 四则混合运算 教学动画

知识点: 四则混合运算的运算顺序
  - 规则1: 有括号先算括号里面
  - 规则2: 先乘除，后加减
  - 规则3: 同级运算从左到右
  - 示例题目的逐步演示

年级: 四年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
COLOR_TITLE = "#fbbf24"   # 金黄色 — 标题
COLOR_RULE1 = "#ef4444"   # 红色   — 括号规则
COLOR_RULE2 = "#3b82f6"   # 蓝色   — 乘除规则
COLOR_RULE3 = "#22c55e"   # 绿色   — 加减规则
COLOR_STEP  = "#f59e0b"   # 橙色   — 当前步骤高亮
COLOR_RESULT= "#a78bfa"   # 紫色   — 最终结果
COLOR_AUTHOR= "#6b7280"   # 灰色   — 作者信息
COLOR_BG_CARD = "#16213e" # 深蓝   — 卡片背景
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class MixedArithmeticLesson(Scene):
    """
    四则混合运算教学动画
    场景顺序:
      1. 开场钩子
      2. 三条运算顺序规则
      3. 例题1: 纯加减乘除 (无括号)
      4. 例题2: 含括号混合运算
      5. 规则对比 — 加括号 vs 不加括号
      6. 总结卡片
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识（全程保留在顶部）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        self.scene_1_opening()
        self.scene_2_three_rules()
        self.scene_3_example_no_bracket()
        self.scene_4_example_with_bracket()
        self.scene_5_contrast()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 场景 1 — 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """开场: 抛出问题，引起兴趣"""

        # 钩子问题
        hook_line1 = Text("你知道这道题", font=FONT, font_size=36, color=WHITE)
        hook_line2 = Text("该怎么算吗？", font=FONT, font_size=36, color=COLOR_TITLE)
        hook = VGroup(hook_line1, hook_line2).arrange(DOWN, buff=0.15)
        hook.move_to(UP * 5.5)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.7)
        self.wait(0.3)

        # 展示一道混合运算题
        expr = MathTex(
            r"3 + 6 \times (5 - 2) \div 2",
            font_size=52, color=COLOR_TITLE
        )
        expr.move_to(UP * 3.8)
        self.play(Write(expr), run_time=1.2)
        self.wait(0.4)

        # 三个问号暗示不同答案
        q1 = MathTex(r"= 12?", font_size=40, color="#ef4444")
        q2 = MathTex(r"= 9?",  font_size=40, color="#3b82f6")
        q3 = MathTex(r"= 21?", font_size=40, color="#22c55e")
        questions = VGroup(q1, q2, q3).arrange(RIGHT, buff=0.8)
        questions.move_to(UP * 2.5)

        self.play(FadeIn(q1, shift=UP * 0.2), run_time=0.3)
        self.play(FadeIn(q2, shift=UP * 0.2), run_time=0.3)
        self.play(FadeIn(q3, shift=UP * 0.2), run_time=0.3)
        self.wait(0.5)

        hint = Text(
            "学完今天的内容，你就知道了！",
            font=FONT, font_size=26, color=COLOR_STEP
        ).move_to(UP * 1.3)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(expr),
            FadeOut(questions), FadeOut(hint),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2 — 三条运算顺序规则
    # ------------------------------------------------------------------

    def scene_2_three_rules(self):
        """展示运算顺序三条规则"""

        section_title = Text(
            "运算顺序三条规则", font=FONT, font_size=38, color=COLOR_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(section_title), run_time=0.7)

        # ---------- 规则1: 括号优先 ----------
        icon1 = self._make_rule_icon("1", COLOR_RULE1)
        label1 = Text("有括号，先算括号里面", font=FONT, font_size=28, color=COLOR_RULE1)
        # Chinese in MathTex is forbidden — use Text only for Chinese
        example1_txt = Text("(5-2) → 先算", font=FONT, font_size=26, color=WHITE)

        rule1_row = VGroup(icon1, label1).arrange(RIGHT, buff=0.3)
        rule1_row.move_to(UP * 4.7)

        # ---------- 规则2: 乘除优先 ----------
        icon2 = self._make_rule_icon("2", COLOR_RULE2)
        label2 = Text("再算乘法和除法", font=FONT, font_size=28, color=COLOR_RULE2)

        rule2_row = VGroup(icon2, label2).arrange(RIGHT, buff=0.3)
        rule2_row.move_to(UP * 3.3)

        # ---------- 规则3: 加减最后 ----------
        icon3 = self._make_rule_icon("3", COLOR_RULE3)
        label3 = Text("最后算加法和减法", font=FONT, font_size=28, color=COLOR_RULE3)

        rule3_row = VGroup(icon3, label3).arrange(RIGHT, buff=0.3)
        rule3_row.move_to(UP * 1.9)

        # 同级补充说明
        same_level = Text(
            "★ 同级运算：从左到右依次计算",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 0.8)

        # 分隔线
        sep1 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1).move_to(UP * 4.05)
        sep2 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1).move_to(UP * 2.65)

        self.play(FadeIn(rule1_row, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(sep1), run_time=0.2)
        self.play(FadeIn(rule2_row, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(sep2), run_time=0.2)
        self.play(FadeIn(rule3_row, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(same_level, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 口诀总结
        rhyme_bg = RoundedRectangle(
            width=7.8, height=1.5,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=0.9,
            stroke_color=COLOR_TITLE, stroke_width=2
        ).move_to(DOWN * 0.8)

        rhyme = Text(
            "括号→乘除→加减，顺序莫搞错！",
            font=FONT, font_size=26, color=COLOR_TITLE
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(rhyme_bg), Write(rhyme), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(section_title), FadeOut(rule1_row), FadeOut(rule2_row),
            FadeOut(rule3_row), FadeOut(sep1), FadeOut(sep2),
            FadeOut(same_level), FadeOut(rhyme_bg), FadeOut(rhyme),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 3 — 例题1: 无括号混合运算
    # ------------------------------------------------------------------

    def scene_3_example_no_bracket(self):
        """例题1: 36 - 4 × 6 + 8 ÷ 2（先乘除后加减）"""

        # 题目标题
        eg_title = Text("例题 1", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        eg_hint  = Text("先乘除，后加减", font=FONT, font_size=24, color=COLOR_RULE2).move_to(UP * 5.9)
        self.play(Write(eg_title), FadeIn(eg_hint), run_time=0.6)

        # 原式
        expr0 = MathTex(
            r"36 - 4 \times 6 + 8 \div 2",
            font_size=46, color=WHITE
        ).move_to(UP * 4.9)
        self.play(Write(expr0), run_time=1.0)
        self.wait(0.5)

        # ---- 步骤框 ----
        steps_y = [3.5, 2.2, 0.9]  # y positions for step rows

        # Step 1: 先算 4×6=24  和  8÷2=4
        step1_label = Text("第①步：先算乘除", font=FONT, font_size=24, color=COLOR_RULE2)
        step1_label.move_to(UP * steps_y[0] + LEFT * 1.0)

        step1_a = MathTex(r"4 \times 6 = 24", font_size=36, color=COLOR_RULE2)
        step1_b = MathTex(r"8 \div 2 = 4",    font_size=36, color=COLOR_RULE2)
        step1_calcs = VGroup(step1_a, step1_b).arrange(RIGHT, buff=0.8)
        step1_calcs.move_to(UP * (steps_y[0] - 0.65))

        self.play(Write(step1_label), run_time=0.5)
        self.play(Write(step1_a), Write(step1_b), run_time=0.8)
        self.wait(0.5)

        # 把原式的乘除部分高亮 → 展示替换后的式子
        expr1 = MathTex(
            r"= 36 - 24 + 4",
            font_size=46, color=WHITE
        ).move_to(UP * steps_y[1] + UP * 0.4)

        arrow1 = Arrow(
            expr0.get_bottom() + DOWN * 0.1,
            expr1.get_top()    + UP   * 0.1,
            buff=0.05, color=COLOR_RULE2, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(Write(expr1), run_time=0.8)
        self.wait(0.4)

        # Step 2: 再算加减（从左到右）
        step2_label = Text("第②步：从左到右算加减", font=FONT, font_size=24, color=COLOR_RULE3)
        step2_label.move_to(UP * steps_y[1] + LEFT * 0.5)

        self.play(FadeIn(step2_label, shift=RIGHT * 0.2), run_time=0.4)

        # 36 - 24 = 12
        step2_a = MathTex(r"36 - 24 = 12", font_size=36, color=COLOR_RULE3)
        step2_a.move_to(UP * (steps_y[1] - 0.65))
        self.play(Write(step2_a), run_time=0.6)
        self.wait(0.3)

        # 12 + 4 = 16
        step2_b = MathTex(r"12 + 4 = 16", font_size=36, color=COLOR_RULE3)
        step2_b.move_to(UP * (steps_y[1] - 1.35))
        self.play(Write(step2_b), run_time=0.6)
        self.wait(0.3)

        # 最终结果
        result_bg = RoundedRectangle(
            width=5.5, height=1.1,
            corner_radius=0.25,
            fill_color="#1e3a5f", fill_opacity=0.95,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(UP * steps_y[2] - UP * 0.5)

        result_row = VGroup(
            Text("答：", font=FONT, font_size=34, color=WHITE),
            MathTex(r"36 - 4 \times 6 + 8 \div 2 = 16", font_size=34, color=COLOR_RESULT)
        ).arrange(RIGHT, buff=0.2).move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(Write(result_row), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(eg_title), FadeOut(eg_hint), FadeOut(expr0),
            FadeOut(step1_label), FadeOut(step1_calcs),
            FadeOut(arrow1), FadeOut(expr1),
            FadeOut(step2_label), FadeOut(step2_a), FadeOut(step2_b),
            FadeOut(result_bg), FadeOut(result_row),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 4 — 例题2: 含括号混合运算
    # ------------------------------------------------------------------

    def scene_4_example_with_bracket(self):
        """例题2: 3 + 6 × (5 - 2) ÷ 2（开场那道题）"""

        eg_title = Text("例题 2", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        eg_hint  = Text("有括号，先算括号内", font=FONT, font_size=24, color=COLOR_RULE1).move_to(UP * 5.9)
        self.play(Write(eg_title), FadeIn(eg_hint), run_time=0.6)

        # 原式
        expr0 = MathTex(
            r"3 + 6 \times (5 - 2) \div 2",
            font_size=44, color=WHITE
        ).move_to(UP * 5.0)
        self.play(Write(expr0), run_time=1.0)
        self.wait(0.4)

        # 高亮括号部分
        brace_indicator = SurroundingRectangle(
            expr0, color=COLOR_RULE1, buff=0.06, corner_radius=0.1
        )
        brace_label = Text("括号！优先算！", font=FONT, font_size=22, color=COLOR_RULE1)
        brace_label.next_to(expr0, DOWN, buff=0.25)

        self.play(Create(brace_indicator), FadeIn(brace_label), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(brace_indicator), FadeOut(brace_label), run_time=0.3)

        steps_y = [3.7, 2.4, 1.1, -0.2]

        # ---- 步骤1: 算括号 ----
        s1_label = Text("第①步：括号内 5 - 2", font=FONT, font_size=24, color=COLOR_RULE1)
        s1_label.move_to(UP * steps_y[0])
        s1_calc  = MathTex(r"5 - 2 = 3", font_size=38, color=COLOR_RULE1)
        s1_calc.move_to(UP * (steps_y[0] - 0.65))

        self.play(Write(s1_label), run_time=0.4)
        self.play(Write(s1_calc),  run_time=0.6)
        self.wait(0.4)

        expr1 = MathTex(r"= 3 + 6 \times 3 \div 2", font_size=44, color=WHITE)
        expr1.move_to(UP * steps_y[1] + UP * 0.3)

        arr1 = Arrow(
            expr0.get_bottom() + DOWN * 0.1,
            expr1.get_top() + UP * 0.1,
            buff=0.05, color=COLOR_RULE1, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(GrowArrow(arr1), run_time=0.3)
        self.play(Write(expr1), run_time=0.8)
        self.wait(0.4)

        # ---- 步骤2: 乘除 ----
        s2_label = Text("第②步：乘除从左到右", font=FONT, font_size=24, color=COLOR_RULE2)
        s2_label.move_to(UP * steps_y[1] + LEFT * 0.3)
        self.play(FadeIn(s2_label), run_time=0.4)

        s2a = MathTex(r"6 \times 3 = 18", font_size=36, color=COLOR_RULE2)
        s2a.move_to(UP * (steps_y[1] - 0.65))
        self.play(Write(s2a), run_time=0.6)
        self.wait(0.3)

        s2b = MathTex(r"18 \div 2 = 9", font_size=36, color=COLOR_RULE2)
        s2b.move_to(UP * (steps_y[1] - 1.35))
        self.play(Write(s2b), run_time=0.6)
        self.wait(0.3)

        expr2 = MathTex(r"= 3 + 9", font_size=44, color=WHITE)
        expr2.move_to(UP * steps_y[2] + UP * 0.3)
        arr2 = Arrow(
            s2b.get_bottom() + DOWN * 0.1,
            expr2.get_top()  + UP * 0.1,
            buff=0.05, color=COLOR_RULE2, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(GrowArrow(arr2), run_time=0.3)
        self.play(Write(expr2), run_time=0.6)
        self.wait(0.4)

        # ---- 步骤3: 加减 ----
        s3_label = Text("第③步：最后算加减", font=FONT, font_size=24, color=COLOR_RULE3)
        s3_label.move_to(UP * steps_y[2] + LEFT * 0.3)
        self.play(FadeIn(s3_label), run_time=0.4)

        s3_calc = MathTex(r"3 + 9 = 12", font_size=38, color=COLOR_RULE3)
        s3_calc.move_to(UP * (steps_y[2] - 0.65))
        self.play(Write(s3_calc), run_time=0.6)
        self.wait(0.4)

        # 最终结果
        result_bg = RoundedRectangle(
            width=7.0, height=1.1,
            corner_radius=0.25,
            fill_color="#1e3a5f", fill_opacity=0.95,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(UP * steps_y[3])

        result_math = MathTex(
            r"3 + 6 \times (5-2) \div 2 = 12",
            font_size=34, color=COLOR_RESULT
        ).move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(Write(result_math), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(eg_title), FadeOut(eg_hint), FadeOut(expr0),
            FadeOut(s1_label), FadeOut(s1_calc),
            FadeOut(arr1), FadeOut(expr1),
            FadeOut(s2_label), FadeOut(s2a), FadeOut(s2b),
            FadeOut(arr2), FadeOut(expr2),
            FadeOut(s3_label), FadeOut(s3_calc),
            FadeOut(result_bg), FadeOut(result_math),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 5 — 对比: 括号改变结果
    # ------------------------------------------------------------------

    def scene_5_contrast(self):
        """说明括号对计算结果的影响"""

        title = Text("括号会改变结果！", font=FONT, font_size=36, color=COLOR_TITLE)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.6)

        # 左侧：无括号
        left_head = Text("无括号", font=FONT, font_size=28, color=COLOR_RULE2)
        left_head.move_to(UP * 5.2 + LEFT * 2.3)

        left_expr = MathTex(r"3 + 2 \times 4", font_size=40, color=WHITE)
        left_expr.move_to(UP * 4.3 + LEFT * 2.3)

        left_step1 = MathTex(r"2 \times 4 = 8", font_size=32, color=COLOR_RULE2)
        left_step1.move_to(UP * 3.3 + LEFT * 2.3)

        left_step2 = MathTex(r"3 + 8", font_size=32, color=WHITE)
        left_step2.move_to(UP * 2.5 + LEFT * 2.3)

        left_result_bg = RoundedRectangle(
            width=3.2, height=0.85,
            corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.9,
            stroke_color=COLOR_RULE2, stroke_width=2
        ).move_to(UP * 1.6 + LEFT * 2.3)
        left_result = MathTex(r"= 11", font_size=38, color=COLOR_RULE2)
        left_result.move_to(left_result_bg.get_center())

        # 右侧：有括号
        right_head = Text("有括号", font=FONT, font_size=28, color=COLOR_RULE1)
        right_head.move_to(UP * 5.2 + RIGHT * 2.3)

        right_expr = MathTex(r"(3 + 2) \times 4", font_size=40, color=WHITE)
        right_expr.move_to(UP * 4.3 + RIGHT * 2.3)

        right_step1 = MathTex(r"3 + 2 = 5", font_size=32, color=COLOR_RULE1)
        right_step1.move_to(UP * 3.3 + RIGHT * 2.3)

        right_step2 = MathTex(r"5 \times 4", font_size=32, color=WHITE)
        right_step2.move_to(UP * 2.5 + RIGHT * 2.3)

        right_result_bg = RoundedRectangle(
            width=3.2, height=0.85,
            corner_radius=0.2,
            fill_color="#3b0000", fill_opacity=0.9,
            stroke_color=COLOR_RULE1, stroke_width=2
        ).move_to(UP * 1.6 + RIGHT * 2.3)
        right_result = MathTex(r"= 20", font_size=38, color=COLOR_RULE1)
        right_result.move_to(right_result_bg.get_center())

        # 中间分隔线
        sep = Line(UP * 5.8, UP * 0.8, color=GRAY_D, stroke_width=1.5)

        self.play(
            FadeIn(left_head), FadeIn(right_head),
            FadeIn(sep),
            run_time=0.5
        )
        self.play(Write(left_expr), Write(right_expr), run_time=0.8)
        self.wait(0.4)
        self.play(Write(left_step1), Write(right_step1), run_time=0.7)
        self.wait(0.3)
        self.play(Write(left_step2), Write(right_step2), run_time=0.6)
        self.wait(0.3)
        self.play(
            FadeIn(left_result_bg), FadeIn(right_result_bg),
            Write(left_result), Write(right_result),
            run_time=0.7
        )
        self.wait(0.4)

        # 差异说明
        diff_arr = Arrow(
            left_result.get_center(), right_result.get_center(),
            buff=0.15, color=COLOR_STEP, stroke_width=3,
            max_tip_length_to_length_ratio=0.12
        )
        diff_txt = Text("差了 9！", font=FONT, font_size=28, color=COLOR_STEP)
        diff_txt.move_to(UP * 0.6)

        self.play(GrowArrow(diff_arr), run_time=0.5)
        self.play(Write(diff_txt), run_time=0.5)
        self.wait(0.5)

        notice = Text(
            "括号改变了运算顺序，结果完全不同！",
            font=FONT, font_size=24, color=COLOR_TITLE
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(notice, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(left_head), FadeOut(right_head), FadeOut(sep),
            FadeOut(left_expr), FadeOut(right_expr),
            FadeOut(left_step1), FadeOut(right_step1),
            FadeOut(left_step2), FadeOut(right_step2),
            FadeOut(left_result_bg), FadeOut(right_result_bg),
            FadeOut(left_result), FadeOut(right_result),
            FadeOut(diff_arr), FadeOut(diff_txt), FadeOut(notice),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 6 — 总结卡片
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        """总结三条规则 + 口诀"""

        sum_title = Text("运算顺序总结", font=FONT, font_size=36, color=COLOR_TITLE)
        sum_title.move_to(UP * 6.4)
        self.play(Write(sum_title), run_time=0.6)

        cards_info = [
            ("①", "括号优先",   "有括号，先算括号里面",        COLOR_RULE1, UP * 4.8),
            ("②", "乘除优先",   "没有括号，先算 × 和 ÷",       COLOR_RULE2, UP * 3.2),
            ("③", "加减最后",   "最后才算 + 和 −",            COLOR_RULE3, UP * 1.6),
            ("④", "从左到右",   "同级运算，从左到右依次进行",    COLOR_STEP,  UP * 0.0),
        ]

        card_objects = []
        for num, sub, desc, color, pos in cards_info:
            card = self._make_summary_card(num, sub, desc, color, pos)
            card_objects.append(card)

        for card in card_objects:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.4)
            self.wait(0.2)

        self.wait(1.0)

        # 口诀框
        rhyme_bg = RoundedRectangle(
            width=7.8, height=1.6,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=0.95,
            stroke_color=COLOR_TITLE, stroke_width=2.5
        ).move_to(DOWN * 1.5)

        rhyme_line1 = Text("括号乘除先来算，", font=FONT, font_size=26, color=COLOR_TITLE)
        rhyme_line2 = Text("加减最后不要忘！", font=FONT, font_size=26, color=COLOR_TITLE)
        rhyme = VGroup(rhyme_line1, rhyme_line2).arrange(DOWN, buff=0.15)
        rhyme.move_to(rhyme_bg.get_center())

        self.play(FadeIn(rhyme_bg), Write(rhyme), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(sum_title),
            *[FadeOut(c) for c in card_objects],
            FadeOut(rhyme_bg), FadeOut(rhyme),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 7 — 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        """片尾: 作者信息 + 关注提示"""

        channel = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=44, color=WHITE
        ).move_to(UP * 2.0)

        handle = Text(
            "@emptyandcalm",
            font=FONT, font_size=34, color=GRAY_B
        ).move_to(UP * 1.1)

        self.play(
            FadeOut(self.author_label),
            FadeIn(channel, shift=DOWN * 0.3),
            run_time=0.7
        )
        self.play(FadeIn(handle, shift=DOWN * 0.2), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_TITLE
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰性数学符号
        ops = VGroup(
            MathTex(r"+", font_size=48, color=COLOR_RULE3),
            MathTex(r"-", font_size=48, color=COLOR_RULE3),
            MathTex(r"\times", font_size=48, color=COLOR_RULE2),
            MathTex(r"\div",   font_size=48, color=COLOR_RULE2),
        ).arrange(RIGHT, buff=0.7).move_to(DOWN * 1.5)

        for op in ops:
            self.play(FadeIn(op, scale=0.3), run_time=0.2)

        self.wait(1.5)

        self.play(
            FadeOut(channel), FadeOut(handle),
            FadeOut(follow), FadeOut(ops),
            run_time=0.8
        )

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def _make_rule_icon(self, number: str, color: str):
        """创建圆形数字图标"""
        circle = Circle(radius=0.32, fill_color=color, fill_opacity=1, stroke_width=0)
        label  = Text(number, font=FONT, font_size=24, color=WHITE, weight=BOLD)
        label.move_to(circle.get_center())
        return VGroup(circle, label)

    def _make_summary_card(self, num: str, subtitle: str, desc: str, color: str, pos):
        """创建总结卡片"""
        icon = self._make_rule_icon(num, color)

        sub_txt  = Text(subtitle, font=FONT, font_size=26, color=color, weight=BOLD)
        desc_txt = Text(desc, font=FONT, font_size=20, color=GRAY_A)

        text_col = VGroup(sub_txt, desc_txt).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        row = VGroup(icon, text_col).arrange(RIGHT, buff=0.25, aligned_edge=UP)

        bg = RoundedRectangle(
            width=7.6, height=1.0,
            corner_radius=0.2,
            fill_color=COLOR_BG_CARD, fill_opacity=0.85,
            stroke_color=color, stroke_width=1.5
        )
        bg.move_to(pos)
        row.move_to(pos)

        return VGroup(bg, row)
