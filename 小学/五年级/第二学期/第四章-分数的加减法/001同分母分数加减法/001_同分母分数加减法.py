"""
001_同分母分数加减法.py — 同分母分数加减法 教学动画

知识点: 同分母分数相加减，分母不变，分子相加减
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 分数单位相同，直接算！
  2. 直观演示: 矩形分成 7 份，颜色展示 2/7 + 3/7
  3. 加法法则: a/c + b/c = (a+b)/c
  4. 加法例题: 2/7 + 3/7 = 5/7
  5. 减法例题: 5/8 - 2/8 = 3/8
  6. 约分例题: 3/6 + 1/6 = 4/6 = 2/3
  7. 假分数转换: 5/8 + 7/8 = 12/8 = 3/2 = 1½
  8. 总结公式框
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

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR = "#1a1a2e"
COLOR_ADD = "#3b82f6"        # 蓝色加法
COLOR_SUB = "#ef4444"        # 红色减法
COLOR_RESULT = "#22c55e"     # 绿色结果
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#a78bfa"     # 紫色强调
COLOR_ORANGE = "#f59e0b"     # 橙色
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class SameDenominatorLesson(Scene):
    """
    同分母分数加减法教学动画
    场景顺序:
      1. 开场钩子
      2. 直观图形演示: 矩形分 7 份
      3. 加法法则推导
      4. 加法例题 2/7 + 3/7
      5. 减法例题 5/8 - 2/8
      6. 约分例题 3/6 + 1/6 = 4/6 = 2/3
      7. 假分数转换 5/8 + 7/8
      8. 总结公式框
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_visual_intro()
        self.scene_3_addition_rule()
        self.scene_4_addition_example()
        self.scene_5_subtraction_example()
        self.scene_6_simplification()
        self.scene_7_improper_fraction()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '同分母分数加减法 — 分数单位相同，直接算！'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        hook1 = Text(
            "同分母分数加减法",
            font=FONT, font_size=44, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "分数单位相同，直接算！",
            font=FONT, font_size=34, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示一个快速预览算式
        preview = MathTex(
            r"\frac{2}{7}", r"+", r"\frac{3}{7}", r"=", r"?",
            font_size=72
        ).move_to(UP * 1.5)
        preview[0].set_color(COLOR_ADD)
        preview[2].set_color(COLOR_ACCENT)
        preview[4].set_color(COLOR_HL)

        self.play(FadeIn(preview, scale=0.5), run_time=0.8)
        self.wait(1.0)

        # 清理
        self.play(FadeOut(VGroup(hook1, hook2, preview)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 直观图形演示 — 矩形分成 7 份
    # ------------------------------------------------------------------

    def scene_2_visual_intro(self):
        """用矩形分成 7 份来直观展示 2/7 + 3/7 = 5/7"""

        title = Text(
            "用图形来理解", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 矩形条: 7 等分
        bar_width = 7.0
        bar_height = 1.2
        n_parts = 7
        part_w = bar_width / n_parts

        parts = VGroup()
        for i in range(n_parts):
            rect = RoundedRectangle(
                width=part_w - 0.04, height=bar_height,
                corner_radius=0.05,
                fill_color="#334155", fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=2
            )
            rect.move_to(
                LEFT * (bar_width / 2 - part_w / 2) + RIGHT * i * part_w
                + UP * 3.0
            )
            parts.add(rect)

        self.play(
            *[FadeIn(p, scale=0.8) for p in parts],
            run_time=0.8
        )

        # 标注: 每一份是 1/7
        unit_label = Text(
            "每一份是", font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 1.5 + LEFT * 1.5)
        unit_frac = MathTex(
            r"\frac{1}{7}", font_size=48, color=COLOR_HL
        ).next_to(unit_label, RIGHT, buff=0.3)
        self.play(Write(unit_label), FadeIn(unit_frac), run_time=0.6)
        self.wait(0.5)

        # 涂色前 2 份 — 代表 2/7
        for i in range(2):
            self.play(
                parts[i].animate.set_fill(COLOR_ADD, opacity=0.85),
                run_time=0.3
            )

        label_2 = MathTex(
            r"\frac{2}{7}", font_size=48, color=COLOR_ADD
        ).move_to(UP * 0.3 + LEFT * 2.0)
        self.play(FadeIn(label_2, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)

        # 再涂色 3 份 — 代表 3/7
        for i in range(2, 5):
            self.play(
                parts[i].animate.set_fill(COLOR_ACCENT, opacity=0.85),
                run_time=0.3
            )

        plus_sign = MathTex(r"+", font_size=48, color=WHITE).move_to(UP * 0.3)
        label_3 = MathTex(
            r"\frac{3}{7}", font_size=48, color=COLOR_ACCENT
        ).move_to(UP * 0.3 + RIGHT * 2.0)
        self.play(FadeIn(plus_sign), FadeIn(label_3, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 结果: 一共涂了 5 份 = 5/7
        count_text = Text(
            "一共涂了 5 份", font=FONT, font_size=28, color=COLOR_RESULT
        ).move_to(DOWN * 1.0)
        self.play(Write(count_text), run_time=0.5)

        equals = MathTex(r"=", font_size=48, color=WHITE).move_to(DOWN * 2.3 + LEFT * 1.0)
        label_5 = MathTex(
            r"\frac{5}{7}", font_size=64, color=COLOR_RESULT
        ).move_to(DOWN * 2.3 + RIGHT * 0.5)
        result_box = SurroundingRectangle(
            label_5, color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )

        self.play(
            FadeIn(equals), FadeIn(label_5, scale=0.6),
            run_time=0.5
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(0.5)

        # 关键理解
        insight = Text(
            "分数单位相同，直接数格子！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(insight, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, parts, unit_label, unit_frac,
                label_2, plus_sign, label_3,
                count_text, equals, label_5, result_box, insight
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 加法法则推导
    # ------------------------------------------------------------------

    def scene_3_addition_rule(self):
        """推导公式: a/c + b/c = (a+b)/c"""

        title = Text(
            "加法法则", font=FONT, font_size=42,
            color=COLOR_ADD, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 法则框
        rule_box = RoundedRectangle(
            width=7.8, height=4.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_ADD, stroke_width=3
        ).move_to(UP * 2.5)
        self.play(FadeIn(rule_box), run_time=0.3)

        # 文字描述
        r1 = Text(
            "同分母分数相加", font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 3.8)
        r2 = Text(
            "分母不变", font=FONT, font_size=34,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 2.8)
        r3 = Text(
            "分子相加", font=FONT, font_size=34,
            color=COLOR_RESULT, weight=BOLD
        ).move_to(UP * 1.8)

        self.play(Write(r1), run_time=0.5)
        self.play(Write(r2), run_time=0.5)
        self.play(Write(r3), run_time=0.5)
        self.wait(0.5)

        # 公式
        formula = MathTex(
            r"\frac{a}{c}", r"+", r"\frac{b}{c}", r"=",
            r"\frac{a+b}{c}",
            font_size=56
        ).move_to(DOWN * 0.3)
        formula[0].set_color(COLOR_ADD)
        formula[2].set_color(COLOR_ACCENT)
        formula[4].set_color(COLOR_RESULT)

        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)

        # 高亮分母不变
        denom_note = Text(
            "分母 c 不变", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.8 + LEFT * 2.0)
        numer_note = Text(
            "分子 a + b", font=FONT, font_size=24, color=COLOR_RESULT
        ).move_to(DOWN * 1.8 + RIGHT * 2.0)

        arrow_d = Arrow(
            denom_note.get_top(), formula[4].get_bottom() + DOWN * 0.1 + LEFT * 0.3,
            color=COLOR_HL, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )
        arrow_n = Arrow(
            numer_note.get_top(), formula[4].get_top() + UP * 0.1 + RIGHT * 0.1,
            color=COLOR_RESULT, stroke_width=2, max_tip_length_to_length_ratio=0.15
        )

        self.play(
            FadeIn(denom_note), Create(arrow_d),
            FadeIn(numer_note), Create(arrow_n),
            run_time=0.7
        )
        self.wait(0.5)

        # 减法同理
        sub_title = Text(
            "减法同理", font=FONT, font_size=34,
            color=COLOR_SUB, weight=BOLD
        ).move_to(DOWN * 3.3)
        self.play(FadeIn(sub_title, shift=UP * 0.3), run_time=0.5)

        sub_formula = MathTex(
            r"\frac{a}{c}", r"-", r"\frac{b}{c}", r"=",
            r"\frac{a-b}{c}",
            font_size=56
        ).move_to(DOWN * 4.8)
        sub_formula[0].set_color(COLOR_ADD)
        sub_formula[1].set_color(COLOR_SUB)
        sub_formula[2].set_color(COLOR_ACCENT)
        sub_formula[4].set_color(COLOR_RESULT)

        self.play(Write(sub_formula), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, rule_box, r1, r2, r3,
                formula, denom_note, numer_note, arrow_d, arrow_n,
                sub_title, sub_formula
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 加法例题 2/7 + 3/7
    # ------------------------------------------------------------------

    def scene_4_addition_example(self):
        """加法例题: 2/7 + 3/7 = 5/7"""

        title = Text(
            "例题一：加法", font=FONT, font_size=40,
            color=COLOR_ADD, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 题目
        problem = MathTex(
            r"\frac{2}{7}", r"+", r"\frac{3}{7}",
            font_size=72
        ).move_to(UP * 3.5)
        problem[0].set_color(COLOR_ADD)
        problem[2].set_color(COLOR_ACCENT)

        self.play(Write(problem), run_time=0.7)
        self.wait(0.5)

        # Step 1: 分母相同
        step1_text = Text(
            "第一步：分母相同吗？",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 1.8)
        self.play(Write(step1_text), run_time=0.5)

        check_yes = Text(
            "相同！都是 7",
            font=FONT, font_size=28, color=COLOR_RESULT, weight=BOLD
        ).move_to(UP * 0.8)
        self.play(FadeIn(check_yes, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # Step 2: 分母不变，分子相加
        step2_text = Text(
            "第二步：分母不变，分子相加",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 0.3)
        self.play(Write(step2_text), run_time=0.5)

        # 计算过程
        calc = MathTex(
            r"=", r"\frac{2+3}{7}",
            font_size=68
        ).move_to(DOWN * 1.8)
        calc[1].set_color(COLOR_RESULT)

        self.play(Write(calc), run_time=0.6)
        self.wait(0.3)

        # Step 3: 得出结果
        step3_text = Text(
            "第三步：计算分子",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 3.2)
        self.play(Write(step3_text), run_time=0.5)

        result = MathTex(
            r"=", r"\frac{5}{7}",
            font_size=72
        ).move_to(DOWN * 4.6)
        result[1].set_color(COLOR_HL)

        self.play(Write(result), run_time=0.6)

        # 高亮结果
        result_box = SurroundingRectangle(
            result[1], color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, problem, step1_text, check_yes,
                step2_text, calc, step3_text, result, result_box
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 减法例题 5/8 - 2/8
    # ------------------------------------------------------------------

    def scene_5_subtraction_example(self):
        """减法例题: 5/8 - 2/8 = 3/8"""

        title = Text(
            "例题二：减法", font=FONT, font_size=40,
            color=COLOR_SUB, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 矩形条 8 等分 — 直观演示减法
        bar_width = 7.0
        bar_height = 1.0
        n_parts = 8
        part_w = bar_width / n_parts

        parts = VGroup()
        for i in range(n_parts):
            rect = RoundedRectangle(
                width=part_w - 0.04, height=bar_height,
                corner_radius=0.04,
                fill_color="#334155", fill_opacity=0.6,
                stroke_color=WHITE, stroke_width=2
            )
            rect.move_to(
                LEFT * (bar_width / 2 - part_w / 2) + RIGHT * i * part_w
                + UP * 3.5
            )
            parts.add(rect)

        self.play(
            *[FadeIn(p, scale=0.8) for p in parts],
            run_time=0.6
        )

        # 先涂色 5 份 (5/8)
        for i in range(5):
            self.play(
                parts[i].animate.set_fill(COLOR_ADD, opacity=0.85),
                run_time=0.2
            )

        label_5 = MathTex(
            r"\frac{5}{8}", font_size=44, color=COLOR_ADD
        ).move_to(UP * 2.2 + LEFT * 2.0)
        self.play(FadeIn(label_5), run_time=0.3)

        # 去掉 2 份 (减去 2/8) — 用划线标记
        minus_sign = MathTex(r"-", font_size=44, color=COLOR_SUB).move_to(UP * 2.2)
        label_2 = MathTex(
            r"\frac{2}{8}", font_size=44, color=COLOR_SUB
        ).move_to(UP * 2.2 + RIGHT * 2.0)
        self.play(FadeIn(minus_sign), FadeIn(label_2), run_time=0.3)

        for i in range(3, 5):
            cross = VGroup(
                Line(
                    parts[i].get_corner(UL) + np.array([0.05, -0.05, 0]),
                    parts[i].get_corner(DR) + np.array([-0.05, 0.05, 0]),
                    color=COLOR_SUB, stroke_width=3
                ),
                Line(
                    parts[i].get_corner(DL) + np.array([0.05, 0.05, 0]),
                    parts[i].get_corner(UR) + np.array([-0.05, -0.05, 0]),
                    color=COLOR_SUB, stroke_width=3
                )
            )
            self.play(Create(cross), run_time=0.3)
            parts[i].animate.set_fill("#334155", opacity=0.3)

        self.wait(0.5)

        # 题目 + 计算
        problem = MathTex(
            r"\frac{5}{8}", r"-", r"\frac{2}{8}",
            font_size=64
        ).move_to(UP * 0.3)
        problem[0].set_color(COLOR_ADD)
        problem[1].set_color(COLOR_SUB)
        problem[2].set_color(COLOR_SUB)

        self.play(Write(problem), run_time=0.6)
        self.wait(0.3)

        # 过程
        step_note = Text(
            "分母不变，分子相减",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(Write(step_note), run_time=0.5)

        calc = MathTex(
            r"=", r"\frac{5-2}{8}",
            font_size=64
        ).move_to(DOWN * 2.4)
        calc[1].set_color(COLOR_RESULT)
        self.play(Write(calc), run_time=0.6)

        result = MathTex(
            r"=", r"\frac{3}{8}",
            font_size=68
        ).move_to(DOWN * 4.0)
        result[1].set_color(COLOR_HL)
        self.play(Write(result), run_time=0.6)

        result_box = SurroundingRectangle(
            result[1], color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)

        remain_text = Text(
            "还剩 3 份！",
            font=FONT, font_size=26, color=COLOR_RESULT
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(remain_text, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects
              if mob != self.author_mob and isinstance(mob, VMobject)],
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 约分例题 3/6 + 1/6 = 4/6 = 2/3
    # ------------------------------------------------------------------

    def scene_6_simplification(self):
        """约分: 3/6 + 1/6 = 4/6 = 2/3"""

        title = Text(
            "例题三：结果要约分", font=FONT, font_size=40,
            color=COLOR_ORANGE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 提醒
        remind = Text(
            "计算结果能约分的要约分！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 4.2)
        self.play(Write(remind), run_time=0.5)

        # 题目
        problem = MathTex(
            r"\frac{3}{6}", r"+", r"\frac{1}{6}",
            font_size=72
        ).move_to(UP * 2.5)
        problem[0].set_color(COLOR_ADD)
        problem[2].set_color(COLOR_ACCENT)

        self.play(Write(problem), run_time=0.7)
        self.wait(0.5)

        # Step 1: 分母不变，分子相加
        s1 = Text(
            "分母不变，分子相加",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 0.8)
        self.play(Write(s1), run_time=0.5)

        calc1 = MathTex(
            r"=", r"\frac{3+1}{6}",
            font_size=64
        ).move_to(DOWN * 0.3)
        calc1[1].set_color(COLOR_RESULT)
        self.play(Write(calc1), run_time=0.6)

        calc2 = MathTex(
            r"=", r"\frac{4}{6}",
            font_size=64
        ).move_to(DOWN * 1.8)
        calc2[1].set_color(COLOR_RESULT)
        self.play(Write(calc2), run_time=0.5)
        self.wait(0.5)

        # Step 2: 约分
        s2 = Text(
            "4 和 6 的最大公因数是 2，要约分！",
            font=FONT, font_size=24, color=COLOR_ORANGE
        ).move_to(DOWN * 3.2)
        self.play(Write(s2), run_time=0.6)

        # 约分箭头
        frac_46 = MathTex(r"\frac{4}{6}", font_size=64, color=COLOR_RESULT)
        arrow = MathTex(r"\longrightarrow", font_size=48, color=COLOR_HL)
        frac_23 = MathTex(r"\frac{2}{3}", font_size=64, color=COLOR_HL)

        chain = VGroup(frac_46, arrow, frac_23).arrange(RIGHT, buff=0.6)
        chain.move_to(DOWN * 4.8)

        self.play(FadeIn(frac_46), run_time=0.3)

        # 弧线标注: ÷2
        div2_top = MathTex(r"\div 2", font_size=28, color=COLOR_ORANGE)
        arr_top = CurvedArrow(
            frac_46.get_top() + UP * 0.15 + LEFT * 0.1,
            frac_23.get_top() + UP * 0.15 + RIGHT * 0.1,
            color=COLOR_ORANGE, stroke_width=2.5, angle=-0.5
        )
        div2_top.next_to(arr_top, UP, buff=0.08)

        div2_bot = MathTex(r"\div 2", font_size=28, color=COLOR_ORANGE)
        arr_bot = CurvedArrow(
            frac_46.get_bottom() + DOWN * 0.15 + LEFT * 0.1,
            frac_23.get_bottom() + DOWN * 0.15 + RIGHT * 0.1,
            color=COLOR_ORANGE, stroke_width=2.5, angle=0.5
        )
        div2_bot.next_to(arr_bot, DOWN, buff=0.08)

        self.play(
            FadeIn(arrow), FadeIn(frac_23),
            Create(arr_top), FadeIn(div2_top),
            Create(arr_bot), FadeIn(div2_bot),
            run_time=0.8
        )

        # 高亮最终结果
        result_box = SurroundingRectangle(
            frac_23, color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, remind, problem, s1, calc1, calc2, s2,
                frac_46, arrow, frac_23,
                arr_top, div2_top, arr_bot, div2_bot,
                result_box
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 假分数转换 5/8 + 7/8 = 12/8 = 3/2 = 1½
    # ------------------------------------------------------------------

    def scene_7_improper_fraction(self):
        """假分数: 5/8 + 7/8 = 12/8，要化简"""

        title = Text(
            "例题四：假分数要化简", font=FONT, font_size=40,
            color=COLOR_ACCENT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        remind = Text(
            "结果是假分数，要化成带分数！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 4.2)
        self.play(Write(remind), run_time=0.5)

        # 题目
        problem = MathTex(
            r"\frac{5}{8}", r"+", r"\frac{7}{8}",
            font_size=68
        ).move_to(UP * 2.5)
        problem[0].set_color(COLOR_ADD)
        problem[2].set_color(COLOR_ACCENT)

        self.play(Write(problem), run_time=0.7)
        self.wait(0.5)

        # Step 1: 分子相加
        s1 = Text(
            "分母不变，分子相加",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.0)
        self.play(Write(s1), run_time=0.4)

        calc1 = MathTex(
            r"=", r"\frac{5+7}{8}",
            font_size=60
        ).move_to(UP * 0.0)
        calc1[1].set_color(COLOR_RESULT)
        self.play(Write(calc1), run_time=0.5)

        calc2 = MathTex(
            r"=", r"\frac{12}{8}",
            font_size=60
        ).move_to(DOWN * 1.2)
        calc2[1].set_color(COLOR_RESULT)
        self.play(Write(calc2), run_time=0.5)
        self.wait(0.3)

        # 标注: 12 > 8，这是假分数
        flag = Text(
            "12 > 8，这是假分数！",
            font=FONT, font_size=24, color=COLOR_SUB
        ).move_to(DOWN * 2.4)
        self.play(FadeIn(flag, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # Step 2: 先约分 12/8 ÷4 = 3/2
        s2 = Text(
            "先约分：12 和 8 的最大公因数是 4",
            font=FONT, font_size=24, color=COLOR_ORANGE
        ).move_to(DOWN * 3.4)
        self.play(Write(s2), run_time=0.5)

        calc3 = MathTex(
            r"=", r"\frac{12 \div 4}{8 \div 4}",
            r"=", r"\frac{3}{2}",
            font_size=52
        ).move_to(DOWN * 4.6)
        calc3[1].set_color(COLOR_ORANGE)
        calc3[3].set_color(COLOR_RESULT)
        self.play(Write(calc3), run_time=0.7)
        self.wait(0.3)

        # Step 3: 化成带分数
        s3 = Text(
            "再化成带分数：3 ÷ 2 = 1 余 1",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.8)

        calc4 = MathTex(
            r"=", r"1\frac{1}{2}",
            font_size=64
        ).move_to(DOWN * 6.8)
        calc4[1].set_color(COLOR_HL)

        self.play(Write(s3), run_time=0.5)
        self.play(Write(calc4), run_time=0.6)

        result_box = SurroundingRectangle(
            calc4[1], color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, remind, problem, s1, calc1, calc2,
                flag, s2, calc3, s3, calc4, result_box
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 总结公式框
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        """总结同分母分数加减法的法则和注意事项"""

        title = Text(
            "总结", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 加法公式框 =====
        box_add = RoundedRectangle(
            width=7.8, height=2.6,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_ADD, stroke_width=3
        ).move_to(UP * 3.2)
        self.play(FadeIn(box_add), run_time=0.3)

        add_label = Text(
            "加法", font=FONT, font_size=26, color=COLOR_ADD
        ).move_to(UP * 4.2)
        add_formula = MathTex(
            r"\frac{a}{c}", r"+", r"\frac{b}{c}", r"=",
            r"\frac{a+b}{c}",
            font_size=50
        ).move_to(UP * 3.0)
        add_formula[0].set_color(COLOR_ADD)
        add_formula[2].set_color(COLOR_ACCENT)
        add_formula[4].set_color(COLOR_RESULT)

        self.play(Write(add_label), run_time=0.3)
        self.play(Write(add_formula), run_time=0.7)

        # ===== 减法公式框 =====
        box_sub = RoundedRectangle(
            width=7.8, height=2.6,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_SUB, stroke_width=3
        ).move_to(UP * 0.2)
        self.play(FadeIn(box_sub), run_time=0.3)

        sub_label = Text(
            "减法", font=FONT, font_size=26, color=COLOR_SUB
        ).move_to(UP * 1.2)
        sub_formula = MathTex(
            r"\frac{a}{c}", r"-", r"\frac{b}{c}", r"=",
            r"\frac{a-b}{c}",
            font_size=50
        ).move_to(DOWN * 0.0)
        sub_formula[0].set_color(COLOR_ADD)
        sub_formula[1].set_color(COLOR_SUB)
        sub_formula[2].set_color(COLOR_ACCENT)
        sub_formula[4].set_color(COLOR_RESULT)

        self.play(Write(sub_label), run_time=0.3)
        self.play(Write(sub_formula), run_time=0.7)
        self.wait(0.5)

        # ===== 注意事项 =====
        points_data = [
            ("1. 分母不变，分子相加减", COLOR_HL),
            ("2. 结果能约分的要约分", COLOR_ORANGE),
            ("3. 假分数要化成带分数", COLOR_ACCENT),
        ]

        notes_title = Text(
            "注意事项", font=FONT, font_size=28, color=WHITE, weight=BOLD
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(notes_title, shift=UP * 0.2), run_time=0.4)

        points = VGroup()
        for i, (text, color) in enumerate(points_data):
            pt = Text(
                text, font=FONT, font_size=24, color=color
            ).move_to(DOWN * (3.0 + i * 0.9))
            points.add(pt)

        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.5)

        # 核心口诀
        motto_box = RoundedRectangle(
            width=7.0, height=1.4,
            corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(DOWN * 6.0)
        self.play(FadeIn(motto_box), run_time=0.3)

        motto = Text(
            "口诀：分母不变分子算，约分化简别偷懒！",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 6.0)
        self.play(Write(motto), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                box_add, add_label, add_formula,
                box_sub, sub_label, sub_formula,
                notes_title, points,
                motto_box, motto
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        """作者信息放大 + 关注提示 + 装饰"""

        # 作者名放大居中
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

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 小分数围绕
        deco_colors = [
            COLOR_ADD, COLOR_RESULT, COLOR_ACCENT,
            COLOR_HL, COLOR_SUB, COLOR_ORANGE
        ]
        deco_fracs = [
            r"\frac{2}{7}", r"\frac{5}{7}", r"\frac{3}{8}",
            r"\frac{2}{3}", r"1\frac{1}{2}", r"\frac{a+b}{c}"
        ]
        mini = VGroup(*[
            MathTex(f, font_size=30, color=c).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.5,
                    np.sin(i * PI / 3) * 0.8,
                    0.0
                ])
            )
            for i, (f, c) in enumerate(zip(deco_fracs, deco_colors))
        ])
        self.play(*[FadeIn(t, scale=0.3) for t in mini], run_time=0.5)
        self.play(
            Rotate(mini, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql 001_同分母分数加减法.py SameDenominatorLesson
#   高质量:   manim -qh  001_同分母分数加减法.py SameDenominatorLesson
#   4K:       manim -qk  001_同分母分数加减法.py SameDenominatorLesson
# ======================================================================
