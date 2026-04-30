"""
002_异分母分数加减法.py — 异分母分数加减法 教学动画

知识点: 先通分，将异分母分数转化为同分母分数，再按同分母分数加减
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 分母不同怎么加？
  2. 直观演示: 为什么不能直接加（分数单位不同）
  3. 通分原理: 找最小公倍数，统一分数单位
  4. 加法例题: 1/2 + 1/3 → 通分 → 3/6 + 2/6 = 5/6
  5. 减法例题: 3/4 - 1/6 → 通分 → 9/12 - 2/12 = 7/12
  6. 步骤总结
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
BG_COLOR = "#1a1a2e"
COLOR_ADD = "#3b82f6"        # 蓝色
COLOR_SUB = "#ef4444"        # 红色
COLOR_RESULT = "#22c55e"     # 绿色
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#a78bfa"     # 紫色
COLOR_ORANGE = "#f59e0b"     # 橙色
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class UnlikeDenominatorLesson(Scene):
    """
    异分母分数加减法教学动画
    场景顺序:
      1. 开场钩子
      2. 直观图形演示: 为什么不能直接加
      3. 通分原理
      4. 加法例题 1/2 + 1/3 = 5/6
      5. 减法例题 3/4 - 1/6 = 7/12
      6. 步骤总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_why_cant_add_directly()
        self.scene_3_tongfen_principle()
        self.scene_4_addition_example()
        self.scene_5_subtraction_example()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '1/2 + 1/3 = ?' 分母不同怎么加？"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        hook1 = Text(
            "异分母分数加减法",
            font=FONT, font_size=44, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "分母不同，怎么加减？",
            font=FONT, font_size=34, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示问题算式
        preview = MathTex(
            r"\frac{1}{2}", r"+", r"\frac{1}{3}", r"= \, ?",
            font_size=80
        ).move_to(UP * 2.0)
        preview[0].set_color(COLOR_ADD)
        preview[2].set_color(COLOR_ACCENT)
        preview[3].set_color(COLOR_HL)

        self.play(FadeIn(preview, scale=0.6), run_time=0.8)
        self.wait(1.0)

        # 错误想法提示
        wrong_box = RoundedRectangle(
            width=5.5, height=1.2, corner_radius=0.2,
            fill_color="#7f1d1d", fill_opacity=0.5,
            stroke_color=COLOR_SUB, stroke_width=2
        ).move_to(DOWN * 0.3)

        wrong_label = Text(
            "直接加分子？", font=FONT, font_size=28, color=COLOR_SUB
        ).move_to(DOWN * 0.3)

        wrong_formula = MathTex(
            r"\frac{1+1}{2+3} = \frac{2}{5}", font_size=50, color=COLOR_SUB
        ).move_to(DOWN * 1.8)

        cross_text = Text(
            "X", font=FONT, font_size=60, color=COLOR_SUB
        ).move_to(DOWN * 1.8 + RIGHT * 2.5)

        self.play(FadeIn(wrong_box), Write(wrong_label), run_time=0.5)
        self.play(Write(wrong_formula), run_time=0.5)
        self.play(FadeIn(cross_text, scale=0.5), run_time=0.4)
        self.wait(0.8)

        # 清理
        self.play(FadeOut(VGroup(
            hook1, hook2, preview, wrong_box, wrong_label, wrong_formula, cross_text
        )), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 直观演示 — 为什么不能直接加（分数单位不同）
    # ------------------------------------------------------------------

    def scene_2_why_cant_add_directly(self):
        """用矩形条直观展示 1/2 和 1/3 的分数单位不同"""

        title = Text(
            "分数单位不同，不能直接加！",
            font=FONT, font_size=34, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.2)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ---- 第一行：1/2 的矩形 ----
        bar_w = 6.5
        bar_h = 1.1

        label_half = Text(
            "把1平均分成2份，每份是",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 4.8)
        frac_half = MathTex(
            r"\frac{1}{2}", font_size=44, color=COLOR_ADD
        ).next_to(label_half, RIGHT, buff=0.2)

        self.play(Write(label_half), FadeIn(frac_half), run_time=0.5)

        # 矩形条 — 分成 2 份
        parts_2 = VGroup()
        for i in range(2):
            rect = Rectangle(
                width=bar_w / 2 - 0.05, height=bar_h,
                fill_color="#334155", fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=2
            )
            x_pos = -bar_w / 4 + i * (bar_w / 2)
            rect.move_to(np.array([x_pos, 3.6, 0]))
            parts_2.add(rect)

        self.play(*[FadeIn(p, scale=0.9) for p in parts_2], run_time=0.6)

        # 高亮左边 1 份 (1/2)
        self.play(parts_2[0].animate.set_fill(COLOR_ADD, opacity=0.85), run_time=0.4)

        unit_label_2 = MathTex(
            r"\frac{1}{2}", font_size=40, color=WHITE
        ).move_to(parts_2[0].get_center())
        self.play(FadeIn(unit_label_2), run_time=0.3)
        self.wait(0.4)

        # ---- 第二行：1/3 的矩形 ----
        label_third = Text(
            "把1平均分成3份，每份是",
            font=FONT, font_size=22, color=WHITE
        ).move_to(UP * 2.5)
        frac_third = MathTex(
            r"\frac{1}{3}", font_size=44, color=COLOR_ACCENT
        ).next_to(label_third, RIGHT, buff=0.2)

        self.play(Write(label_third), FadeIn(frac_third), run_time=0.5)

        parts_3 = VGroup()
        part_w3 = bar_w / 3
        for i in range(3):
            rect = Rectangle(
                width=part_w3 - 0.05, height=bar_h,
                fill_color="#334155", fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=2
            )
            x_pos = -bar_w / 2 + part_w3 / 2 + i * part_w3
            rect.move_to(np.array([x_pos, 1.3, 0]))
            parts_3.add(rect)

        self.play(*[FadeIn(p, scale=0.9) for p in parts_3], run_time=0.6)

        # 高亮左边 1 份 (1/3)
        self.play(parts_3[0].animate.set_fill(COLOR_ACCENT, opacity=0.85), run_time=0.4)

        unit_label_3 = MathTex(
            r"\frac{1}{3}", font_size=40, color=WHITE
        ).move_to(parts_3[0].get_center())
        self.play(FadeIn(unit_label_3), run_time=0.3)
        self.wait(0.4)

        # ---- 关键说明 ----
        explain_box = RoundedRectangle(
            width=7.5, height=1.8, corner_radius=0.2,
            fill_color="#1e3a5f", fill_opacity=0.7,
            stroke_color=COLOR_ADD, stroke_width=2
        ).move_to(DOWN * 1.2)

        explain_text_1 = Text(
            "两个分数的分数单位不同！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 0.8)
        explain_text_2 = Text(
            "必须先统一分数单位才能相加",
            font=FONT, font_size=22, color=WHITE
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(explain_box), run_time=0.3)
        self.play(Write(explain_text_1), run_time=0.5)
        self.play(Write(explain_text_2), run_time=0.5)
        self.wait(1.0)

        # 解决方案提示
        solution_text = Text(
            "解决方案：通分！",
            font=FONT, font_size=30, color=COLOR_RESULT
        ).move_to(DOWN * 3.0)

        self.play(Write(solution_text), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(FadeOut(VGroup(
            title, label_half, frac_half, parts_2, unit_label_2,
            label_third, frac_third, parts_3, unit_label_3,
            explain_box, explain_text_1, explain_text_2,
            solution_text
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 通分原理 — 找最小公倍数
    # ------------------------------------------------------------------

    def scene_3_tongfen_principle(self):
        """讲解通分的原理：找最小公倍数作为公分母"""

        title = Text(
            "通分的方法",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 步骤说明框
        step_box = RoundedRectangle(
            width=7.8, height=2.6, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.8,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(UP * 4.7)

        step1 = Text(
            "第一步：找两个分母的最小公倍数",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 5.2)
        step2 = Text(
            "第二步：把各分数化成以最小公倍数",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 4.55)
        step3 = Text(
            "         为分母的同分母分数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 4.0)

        self.play(FadeIn(step_box), run_time=0.3)
        self.play(Write(step1), run_time=0.5)
        self.play(Write(step2), run_time=0.5)
        self.play(Write(step3), run_time=0.4)
        self.wait(0.5)

        # ---- 以 1/2 + 1/3 为例 ----
        example_title = Text(
            "以 1/2 + 1/3 为例：",
            font=FONT, font_size=28, color=COLOR_ACCENT
        ).move_to(UP * 2.8)
        self.play(Write(example_title), run_time=0.4)

        # 分母倍数列举
        denom_label_2 = Text(
            "2 的倍数：2, 4,  6 , 8, 10...",
            font=FONT, font_size=24, color=COLOR_ADD
        ).move_to(UP * 2.0)

        denom_label_3 = Text(
            "3 的倍数：3,  6 , 9, 12...",
            font=FONT, font_size=24, color=COLOR_ACCENT
        ).move_to(UP * 1.3)

        self.play(Write(denom_label_2), run_time=0.5)
        self.play(Write(denom_label_3), run_time=0.5)
        self.wait(0.3)

        # 最小公倍数 = 6
        lcm_box = RoundedRectangle(
            width=6.0, height=1.2, corner_radius=0.2,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=3
        ).move_to(UP * 0.2)

        lcm_text = Text(
            "最小公倍数 = 6  →  公分母 = 6",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(UP * 0.2)

        self.play(FadeIn(lcm_box), Write(lcm_text), run_time=0.6)
        self.wait(0.8)

        # 通分过程
        tongfen_title = Text(
            "通分过程：",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 0.9)
        self.play(Write(tongfen_title), run_time=0.4)

        # 1/2 → 3/6
        tf_1 = MathTex(
            r"\frac{1}{2} = \frac{1 \times 3}{2 \times 3} = \frac{3}{6}",
            font_size=46
        ).move_to(DOWN * 2.0)
        tf_1[0][0:3].set_color(COLOR_ADD)
        tf_1[0][-3:].set_color(COLOR_RESULT)

        # 1/3 → 2/6
        tf_2 = MathTex(
            r"\frac{1}{3} = \frac{1 \times 2}{3 \times 2} = \frac{2}{6}",
            font_size=46
        ).move_to(DOWN * 3.3)
        tf_2[0][0:3].set_color(COLOR_ACCENT)
        tf_2[0][-3:].set_color(COLOR_RESULT)

        self.play(Write(tf_1), run_time=0.7)
        self.play(Write(tf_2), run_time=0.7)
        self.wait(1.2)

        # 清理
        self.play(FadeOut(VGroup(
            title, step_box, step1, step2, step3,
            example_title, denom_label_2, denom_label_3,
            lcm_box, lcm_text, tongfen_title, tf_1, tf_2
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 加法例题 1/2 + 1/3 = 5/6
    # ------------------------------------------------------------------

    def scene_4_addition_example(self):
        """完整演示 1/2 + 1/3 的计算过程"""

        title = Text(
            "加法例题",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 问题
        problem = MathTex(
            r"\frac{1}{2}", r"+", r"\frac{1}{3}",
            font_size=72
        ).move_to(UP * 5.2)
        problem[0].set_color(COLOR_ADD)
        problem[2].set_color(COLOR_ACCENT)

        self.play(Write(problem), run_time=0.6)
        self.wait(0.4)

        # ---- 矩形条可视化：1/2 和 1/3 ----
        bar_w = 6.0
        bar_h = 0.9

        # 整个单位条（灰色轮廓）
        ref_bar_top = Rectangle(
            width=bar_w, height=bar_h,
            fill_opacity=0, stroke_color=GRAY, stroke_width=1.5
        ).move_to(np.array([0, 3.6, 0]))

        ref_bar_bot = Rectangle(
            width=bar_w, height=bar_h,
            fill_opacity=0, stroke_color=GRAY, stroke_width=1.5
        ).move_to(np.array([0, 2.3, 0]))

        # 1/2 填充条
        half_bar = Rectangle(
            width=bar_w / 2, height=bar_h,
            fill_color=COLOR_ADD, fill_opacity=0.75,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([-bar_w / 4, 3.6, 0]))

        half_label = MathTex(
            r"\frac{1}{2}", font_size=36, color=WHITE
        ).move_to(half_bar.get_center())

        # 1/3 填充条
        third_bar = Rectangle(
            width=bar_w / 3, height=bar_h,
            fill_color=COLOR_ACCENT, fill_opacity=0.75,
            stroke_color=WHITE, stroke_width=2
        ).move_to(np.array([-bar_w / 3, 2.3, 0]))

        third_label = MathTex(
            r"\frac{1}{3}", font_size=36, color=WHITE
        ).move_to(third_bar.get_center())

        self.play(FadeIn(ref_bar_top), FadeIn(ref_bar_bot), run_time=0.3)
        self.play(FadeIn(half_bar), FadeIn(half_label), run_time=0.5)
        self.play(FadeIn(third_bar), FadeIn(third_label), run_time=0.5)
        self.wait(0.4)

        # ---- 步骤 1：通分 ----
        step1_label = Text(
            "第一步：通分（公分母=6）",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(UP * 1.0)
        self.play(Write(step1_label), run_time=0.4)

        # ---- 步骤 2：展示通分结果 ----
        tongfen_result = MathTex(
            r"\frac{1}{2} = \frac{3}{6}",
            r"\qquad",
            r"\frac{1}{3} = \frac{2}{6}",
            font_size=50
        ).move_to(UP * 0.0)
        tongfen_result[0].set_color(COLOR_ADD)
        tongfen_result[2].set_color(COLOR_ACCENT)

        self.play(Write(tongfen_result), run_time=0.8)
        self.wait(0.4)

        # ---- 步骤 3：计算 ----
        step2_label = Text(
            "第二步：同分母分数相加",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 1.2)
        self.play(Write(step2_label), run_time=0.4)

        calc = MathTex(
            r"\frac{3}{6}", r"+", r"\frac{2}{6}",
            r"=", r"\frac{3+2}{6}", r"=", r"\frac{5}{6}",
            font_size=52
        ).move_to(DOWN * 2.5)
        calc[0].set_color(COLOR_ADD)
        calc[2].set_color(COLOR_ACCENT)
        calc[4].set_color(COLOR_HL)
        calc[6].set_color(COLOR_RESULT)

        self.play(Write(calc), run_time=1.0)
        self.wait(0.5)

        # ---- 答案高亮框 ----
        answer_box = RoundedRectangle(
            width=5.5, height=1.6, corner_radius=0.3,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=3
        ).move_to(DOWN * 4.2)

        answer = MathTex(
            r"\frac{1}{2} + \frac{1}{3} = \frac{5}{6}",
            font_size=54
        ).move_to(DOWN * 4.2)
        answer.set_color(COLOR_RESULT)

        self.play(FadeIn(answer_box), Write(answer), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(FadeOut(VGroup(
            title, problem, ref_bar_top, ref_bar_bot,
            half_bar, half_label, third_bar, third_label,
            step1_label, tongfen_result,
            step2_label, calc, answer_box, answer
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 减法例题 3/4 - 1/6 = 7/12
    # ------------------------------------------------------------------

    def scene_5_subtraction_example(self):
        """完整演示 3/4 - 1/6 的计算过程"""

        title = Text(
            "减法例题",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)

        # 问题
        problem = MathTex(
            r"\frac{3}{4}", r"-", r"\frac{1}{6}",
            font_size=72
        ).move_to(UP * 5.2)
        problem[0].set_color(COLOR_ADD)
        problem[1].set_color(COLOR_SUB)
        problem[2].set_color(COLOR_ACCENT)

        self.play(Write(problem), run_time=0.6)
        self.wait(0.4)

        # ---- 矩形条可视化 ----
        bar_w = 6.5
        bar_h = 0.9

        # 3/4 条 — 分成 4 份，高亮 3 份
        bar_y1 = 3.6
        parts_4 = VGroup()
        part_w4 = bar_w / 4
        for i in range(4):
            r = Rectangle(
                width=part_w4 - 0.04, height=bar_h,
                fill_color=COLOR_ADD if i < 3 else "#334155",
                fill_opacity=0.75 if i < 3 else 0.4,
                stroke_color=WHITE, stroke_width=2
            )
            x_pos = -bar_w / 2 + part_w4 / 2 + i * part_w4
            r.move_to(np.array([x_pos, bar_y1, 0]))
            parts_4.add(r)

        label_34 = MathTex(
            r"\frac{3}{4}", font_size=40, color=COLOR_ADD
        ).next_to(parts_4, LEFT, buff=0.3)

        # 1/6 条 — 分成 6 份，高亮 1 份
        bar_y2 = 2.3
        parts_6 = VGroup()
        part_w6 = bar_w / 6
        for i in range(6):
            r = Rectangle(
                width=part_w6 - 0.04, height=bar_h,
                fill_color=COLOR_ACCENT if i < 1 else "#334155",
                fill_opacity=0.75 if i < 1 else 0.4,
                stroke_color=WHITE, stroke_width=2
            )
            x_pos = -bar_w / 2 + part_w6 / 2 + i * part_w6
            r.move_to(np.array([x_pos, bar_y2, 0]))
            parts_6.add(r)

        label_16 = MathTex(
            r"\frac{1}{6}", font_size=40, color=COLOR_ACCENT
        ).next_to(parts_6, LEFT, buff=0.3)

        self.play(FadeIn(parts_4), FadeIn(label_34), run_time=0.5)
        self.play(FadeIn(parts_6), FadeIn(label_16), run_time=0.5)
        self.wait(0.3)

        # ---- 步骤 1：找最小公倍数 ----
        step1_label = Text(
            "第一步：找公分母",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(UP * 1.0)
        self.play(Write(step1_label), run_time=0.4)

        lcm_text = Text(
            "4 和 6 的最小公倍数 = 12",
            font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 0.3)
        self.play(Write(lcm_text), run_time=0.5)
        self.wait(0.3)

        # ---- 步骤 2：通分 ----
        step2_label = Text(
            "第二步：通分（公分母=12）",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 0.6)
        self.play(Write(step2_label), run_time=0.4)

        tf1 = MathTex(
            r"\frac{3}{4} = \frac{3 \times 3}{4 \times 3} = \frac{9}{12}",
            font_size=44
        ).move_to(DOWN * 1.8)
        tf1[0][0:3].set_color(COLOR_ADD)
        tf1[0][-4:].set_color(COLOR_RESULT)

        tf2 = MathTex(
            r"\frac{1}{6} = \frac{1 \times 2}{6 \times 2} = \frac{2}{12}",
            font_size=44
        ).move_to(DOWN * 3.0)
        tf2[0][0:3].set_color(COLOR_ACCENT)
        tf2[0][-4:].set_color(COLOR_RESULT)

        self.play(Write(tf1), run_time=0.7)
        self.play(Write(tf2), run_time=0.7)
        self.wait(0.4)

        # ---- 步骤 3：计算 ----
        step3_label = Text(
            "第三步：同分母分数相减",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 4.0)
        self.play(Write(step3_label), run_time=0.4)

        calc = MathTex(
            r"\frac{9}{12}", r"-", r"\frac{2}{12}",
            r"=", r"\frac{9-2}{12}", r"=", r"\frac{7}{12}",
            font_size=48
        ).move_to(DOWN * 5.2)
        calc[0].set_color(COLOR_ADD)
        calc[1].set_color(COLOR_SUB)
        calc[2].set_color(COLOR_ACCENT)
        calc[4].set_color(COLOR_HL)
        calc[6].set_color(COLOR_RESULT)

        self.play(Write(calc), run_time=1.0)
        self.wait(0.5)

        # 答案框
        answer_box = RoundedRectangle(
            width=5.5, height=1.6, corner_radius=0.3,
            fill_color="#14532d", fill_opacity=0.7,
            stroke_color=COLOR_RESULT, stroke_width=3
        ).move_to(DOWN * 6.4)

        answer = MathTex(
            r"\frac{3}{4} - \frac{1}{6} = \frac{7}{12}",
            font_size=52
        ).move_to(DOWN * 6.4)
        answer.set_color(COLOR_RESULT)

        self.play(FadeIn(answer_box), Write(answer), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(FadeOut(VGroup(
            title, problem, parts_4, label_34, parts_6, label_16,
            step1_label, lcm_text, step2_label, tf1, tf2,
            step3_label, calc, answer_box, answer
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 步骤总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        """异分母分数加减法的核心步骤总结"""

        title = Text(
            "解题步骤总结",
            font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)

        # ---- 三步骤卡片 ----
        def make_step_card(num_str, step_title, desc_str, card_color, y_pos):
            bg = RoundedRectangle(
                width=7.8, height=1.9, corner_radius=0.25,
                fill_color="#0f172a", fill_opacity=0.85,
                stroke_color=card_color, stroke_width=2.5
            ).move_to(np.array([0, y_pos, 0]))

            circle = Circle(
                radius=0.38, fill_color=card_color, fill_opacity=1, stroke_width=0
            ).move_to(np.array([-3.3, y_pos, 0]))

            num = Text(
                num_str, font=FONT, font_size=28, color=WHITE, weight=BOLD
            ).move_to(circle.get_center())

            step_t = Text(
                step_title, font=FONT, font_size=26, color=card_color, weight=BOLD
            ).move_to(np.array([-0.8, y_pos + 0.42, 0]))

            desc_t = Text(
                desc_str, font=FONT, font_size=22, color=WHITE
            ).move_to(np.array([-0.5, y_pos - 0.42, 0]))

            return VGroup(bg, circle, num, step_t, desc_t)

        card1 = make_step_card("1", "通  分", "找最小公倍数作公分母", COLOR_ADD, 4.8)
        card2 = make_step_card("2", "化  分", "把各分数化成同分母分数", COLOR_ACCENT, 2.5)
        card3 = make_step_card("3", "计  算", "分母不变，分子相加减", COLOR_RESULT, 0.2)

        self.play(FadeIn(card1, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(card2, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(card3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)

        # ---- 公式框 ----
        formula_box = RoundedRectangle(
            width=7.5, height=2.8, corner_radius=0.3,
            fill_color="#1e1b4b", fill_opacity=0.8,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 2.8)

        formula_title = Text(
            "核心步骤", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 1.8)

        # 异分母 → 通分 → 同分母 → 计算
        flow_1 = Text("异分母", font=FONT, font_size=26, color=COLOR_ADD).move_to(DOWN * 2.7 + LEFT * 2.8)
        arrow_1 = Arrow(
            start=np.array([-1.6, -2.7, 0]),
            end=np.array([-0.6, -2.7, 0]),
            color=WHITE, stroke_width=3, buff=0
        )
        flow_2 = Text("通分", font=FONT, font_size=26, color=COLOR_ACCENT).move_to(DOWN * 2.7 + RIGHT * 0.2)
        arrow_2 = Arrow(
            start=np.array([0.9, -2.7, 0]),
            end=np.array([1.9, -2.7, 0]),
            color=WHITE, stroke_width=3, buff=0
        )
        flow_3 = Text("计算", font=FONT, font_size=26, color=COLOR_RESULT).move_to(DOWN * 2.7 + RIGHT * 2.8)

        formula_note = Text(
            "分母变为公分母，分子相应变化",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 3.6)

        self.play(FadeIn(formula_box), Write(formula_title), run_time=0.4)
        self.play(
            FadeIn(flow_1), GrowArrow(arrow_1), FadeIn(flow_2),
            GrowArrow(arrow_2), FadeIn(flow_3),
            run_time=0.8
        )
        self.play(Write(formula_note), run_time=0.5)
        self.wait(0.5)

        # 重点提示
        key_note = Text(
            "记住：先通分，再计算！",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 4.8)

        self.play(Write(key_note), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(FadeOut(VGroup(
            title, card1, card2, card3,
            formula_box, formula_title,
            flow_1, arrow_1, flow_2, arrow_2, flow_3,
            formula_note, key_note
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        """片尾：作者信息 + 关注提示"""

        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE, weight=BOLD
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=COLOR_AUTHOR
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)

        self.play(Write(follow_text), run_time=0.6)

        # 装饰：展示完整算式
        deco_left = MathTex(
            r"\frac{1}{2} + \frac{1}{3}",
            font_size=38
        ).move_to(DOWN * 2.5 + LEFT * 2.5)
        deco_left.set_color(COLOR_ADD)

        deco_arrow_label = Text(
            "通分", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 2.1)
        deco_arrow = Arrow(
            start=DOWN * 2.5 + LEFT * 0.8,
            end=DOWN * 2.5 + RIGHT * 0.8,
            color=WHITE, stroke_width=3, buff=0
        )

        deco_right = MathTex(
            r"\frac{3}{6} + \frac{2}{6} = \frac{5}{6}",
            font_size=38
        ).move_to(DOWN * 2.5 + RIGHT * 2.5)
        deco_right.set_color(COLOR_RESULT)

        deco_eq = VGroup(deco_left, deco_arrow, deco_arrow_label, deco_right)

        self.play(Write(deco_eq), run_time=1.0)

        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_eq),
            run_time=1.0
        )
