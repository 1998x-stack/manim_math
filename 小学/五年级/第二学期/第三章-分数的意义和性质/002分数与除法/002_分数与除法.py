"""
002_分数与除法.py — 分数与除法 教学动画

知识点: a ÷ b = a/b (b≠0)，被除数→分子，除数→分母
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 核心关系: a ÷ b = a/b (b≠0)
  2. 被除数→分子，除数→分母
  3. 例: 1÷3 = 1/3, 2÷5 = 2/5
  4. 反过来: 3/4 = 3÷4
  5. 分数线就是除号
  6. 注意: 分母(除数)不能为0
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
COLOR_NUMER = "#3b82f6"       # 蓝色分子/被除数
COLOR_DENOM = "#ef4444"       # 红色分母/除数
COLOR_FRAC_LINE = "#22c55e"   # 绿色分数线/除号
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_EXAMPLE = "#a78bfa"     # 紫色示例
COLOR_WARN = "#f97316"        # 橙色警告
COLOR_AUTHOR = "#6b7280"      # 灰色作者
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionDivisionLesson(Scene):
    """
    分数与除法教学动画
    场景:
      1. 开场钩子
      2. 核心关系: a ÷ b = a/b
      3. 对应关系: 被除数→分子，除数→分母
      4. 实例演示
      5. 反向转换: 分数→除法
      6. 分数线就是除号
      7. 分母不能为0
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_core_relation()
        self.scene_3_mapping()
        self.scene_4_examples()
        self.scene_5_reverse()
        self.scene_6_fraction_bar()
        self.scene_7_zero_warning()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------
    def mobjects_without_author(self):
        return VGroup(*[
            m for m in self.mobjects
            if m is not self.author_mob and isinstance(m, VMobject)
        ])

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        """钩子: '1 ÷ 3 = ？' 引出分数"""

        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "分数与除法", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "它们之间有什么秘密？", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 挑战: 1 ÷ 3 = ?
        challenge = MathTex(
            r"1 \div 3 = \;?",
            font_size=64, color=WHITE
        ).move_to(UP * 1.0)
        self.play(Write(challenge), run_time=0.8)

        q = Text("?", font=FONT, font_size=80, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 1.5)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, challenge, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 核心关系 a ÷ b = a/b
    # ------------------------------------------------------------------
    def scene_2_core_relation(self):
        """展示核心公式 a ÷ b = a/b (b≠0)"""

        title = Text(
            "核心关系", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8, height=3.2,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 1.5)
        self.play(FadeIn(formula_box), run_time=0.3)

        # 核心公式: a ÷ b = a/b
        formula = MathTex(
            r"a", r"\div", r"b", r"=", r"\frac{a}{b}",
            font_size=72
        ).move_to(UP * 1.8)
        formula[0].set_color(COLOR_NUMER)   # a
        formula[1].set_color(COLOR_FRAC_LINE)  # ÷
        formula[2].set_color(COLOR_DENOM)   # b
        formula[3].set_color(WHITE)         # =
        formula[4][0].set_color(COLOR_NUMER)  # 分子a
        formula[4][1].set_color(COLOR_FRAC_LINE)  # 分数线
        formula[4][2].set_color(COLOR_DENOM)  # 分母b

        self.play(Write(formula), run_time=1.2)
        self.wait(0.5)

        # 条件: b ≠ 0
        condition = MathTex(
            r"(b \neq 0)",
            font_size=36, color=COLOR_WARN
        ).move_to(UP * 0.5)
        self.play(FadeIn(condition, shift=UP * 0.2), run_time=0.5)

        # 文字说明
        explain = Text(
            "除法可以用分数来表示！",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 1.5)
        self.play(Write(explain), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 对应关系 (被除数→分子，除数→分母)
    # ------------------------------------------------------------------
    def scene_3_mapping(self):
        """展示被除数→分子，除数→分母的对应关系"""

        title = Text(
            "对应关系", font=FONT, font_size=40,
            color=COLOR_EXAMPLE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 除法表达式: a ÷ b
        div_a = MathTex(r"a", font_size=64, color=COLOR_NUMER).move_to(UP * 3.0 + LEFT * 2.0)
        div_sign = MathTex(r"\div", font_size=64, color=COLOR_FRAC_LINE).move_to(UP * 3.0)
        div_b = MathTex(r"b", font_size=64, color=COLOR_DENOM).move_to(UP * 3.0 + RIGHT * 2.0)
        self.play(Write(div_a), Write(div_sign), Write(div_b), run_time=0.6)

        # 中文标签
        label_dividend = Text(
            "被除数", font=FONT, font_size=24, color=COLOR_NUMER
        ).next_to(div_a, UP, buff=0.3)
        label_divisor = Text(
            "除数", font=FONT, font_size=24, color=COLOR_DENOM
        ).next_to(div_b, UP, buff=0.3)
        self.play(FadeIn(label_dividend), FadeIn(label_divisor), run_time=0.4)
        self.wait(0.5)

        # 分数表达式: a/b
        frac = MathTex(r"\frac{a}{b}", font_size=80).move_to(DOWN * 0.5)
        frac[0][0].set_color(COLOR_NUMER)     # 分子 a
        frac[0][1].set_color(COLOR_FRAC_LINE)  # 分数线
        frac[0][2].set_color(COLOR_DENOM)     # 分母 b
        self.play(Write(frac), run_time=0.8)

        # 分子/分母标签
        label_numer = Text(
            "分子", font=FONT, font_size=24, color=COLOR_NUMER
        ).move_to(DOWN * 0.5 + LEFT * 2.5 + UP * 0.4)
        label_denom = Text(
            "分母", font=FONT, font_size=24, color=COLOR_DENOM
        ).move_to(DOWN * 0.5 + LEFT * 2.5 + DOWN * 0.4)
        self.play(FadeIn(label_numer), FadeIn(label_denom), run_time=0.4)

        # 箭头: 被除数 → 分子
        arrow1 = CurvedArrow(
            div_a.get_bottom() + DOWN * 0.1,
            frac.get_top() + UP * 0.1 + LEFT * 0.3,
            color=COLOR_NUMER, stroke_width=3, angle=-0.5
        )
        arrow1_text = Text(
            "被除数 → 分子", font=FONT, font_size=20, color=COLOR_NUMER
        ).move_to(UP * 1.0 + LEFT * 3.0)
        self.play(Create(arrow1), FadeIn(arrow1_text), run_time=0.6)

        # 箭头: 除数 → 分母
        arrow2 = CurvedArrow(
            div_b.get_bottom() + DOWN * 0.1,
            frac.get_bottom() + DOWN * 0.1 + RIGHT * 0.3,
            color=COLOR_DENOM, stroke_width=3, angle=0.5
        )
        arrow2_text = Text(
            "除数 → 分母", font=FONT, font_size=20, color=COLOR_DENOM
        ).move_to(UP * 1.0 + RIGHT * 3.0)
        self.play(Create(arrow2), FadeIn(arrow2_text), run_time=0.6)
        self.wait(1.5)

        # 总结
        summary = Text(
            "记住：上面是被除数，下面是除数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 实例演示
    # ------------------------------------------------------------------
    def scene_4_examples(self):
        """用具体数字举例: 1÷3 = 1/3, 2÷5 = 2/5"""

        title = Text(
            "举例验证", font=FONT, font_size=40,
            color=COLOR_EXAMPLE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 例1: 1 ÷ 3 = 1/3
        ex1_title = Text(
            "例1", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 4.0 + LEFT * 3.0)

        ex1_div = MathTex(
            r"1", r"\div", r"3",
            font_size=56
        ).move_to(UP * 2.8)
        ex1_div[0].set_color(COLOR_NUMER)
        ex1_div[1].set_color(COLOR_FRAC_LINE)
        ex1_div[2].set_color(COLOR_DENOM)

        ex1_eq = MathTex(r"=", font_size=56, color=WHITE).next_to(ex1_div, RIGHT, buff=0.4)

        ex1_frac = MathTex(
            r"\frac{1}{3}",
            font_size=56
        ).next_to(ex1_eq, RIGHT, buff=0.4)
        ex1_frac[0][0].set_color(COLOR_NUMER)
        ex1_frac[0][1].set_color(COLOR_FRAC_LINE)
        ex1_frac[0][2].set_color(COLOR_DENOM)

        self.play(FadeIn(ex1_title), Write(ex1_div), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex1_eq), Write(ex1_frac), run_time=0.6)

        # 标注说明
        ex1_note = Text(
            "1是被除数→分子，3是除数→分母",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 1.5)
        self.play(FadeIn(ex1_note), run_time=0.4)
        self.wait(0.8)

        # 例2: 2 ÷ 5 = 2/5
        ex2_title = Text(
            "例2", font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 0.5 + LEFT * 3.0)

        ex2_div = MathTex(
            r"2", r"\div", r"5",
            font_size=56
        ).move_to(DOWN * 1.7)
        ex2_div[0].set_color(COLOR_NUMER)
        ex2_div[1].set_color(COLOR_FRAC_LINE)
        ex2_div[2].set_color(COLOR_DENOM)

        ex2_eq = MathTex(r"=", font_size=56, color=WHITE).next_to(ex2_div, RIGHT, buff=0.4)

        ex2_frac = MathTex(
            r"\frac{2}{5}",
            font_size=56
        ).next_to(ex2_eq, RIGHT, buff=0.4)
        ex2_frac[0][0].set_color(COLOR_NUMER)
        ex2_frac[0][1].set_color(COLOR_FRAC_LINE)
        ex2_frac[0][2].set_color(COLOR_DENOM)

        self.play(FadeIn(ex2_title), Write(ex2_div), run_time=0.5)
        self.wait(0.3)
        self.play(Write(ex2_eq), Write(ex2_frac), run_time=0.6)

        ex2_note = Text(
            "2是被除数→分子，5是除数→分母",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(ex2_note), run_time=0.4)
        self.wait(1.5)

        # 高亮强调
        highlight_box = SurroundingRectangle(
            VGroup(ex1_div, ex1_eq, ex1_frac, ex2_div, ex2_eq, ex2_frac),
            color=COLOR_HL, stroke_width=2.5, buff=0.4, corner_radius=0.15
        )
        self.play(Create(highlight_box), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 反向转换 (分数→除法)
    # ------------------------------------------------------------------
    def scene_5_reverse(self):
        """反过来: 3/4 = 3 ÷ 4"""

        title = Text(
            "反过来也成立！", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        subtitle = Text(
            "分数也可以看成除法",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.2)
        self.play(Write(subtitle), run_time=0.5)

        # 分数 3/4
        frac = MathTex(
            r"\frac{3}{4}",
            font_size=80
        ).move_to(UP * 1.5 + LEFT * 2.0)
        frac[0][0].set_color(COLOR_NUMER)
        frac[0][1].set_color(COLOR_FRAC_LINE)
        frac[0][2].set_color(COLOR_DENOM)
        self.play(Write(frac), run_time=0.6)

        # 等号
        eq_sign = MathTex(r"=", font_size=72, color=WHITE).move_to(UP * 1.5)
        self.play(Write(eq_sign), run_time=0.3)

        # 除法 3 ÷ 4
        div_expr = MathTex(
            r"3", r"\div", r"4",
            font_size=72
        ).move_to(UP * 1.5 + RIGHT * 2.0)
        div_expr[0].set_color(COLOR_NUMER)
        div_expr[1].set_color(COLOR_FRAC_LINE)
        div_expr[2].set_color(COLOR_DENOM)
        self.play(Write(div_expr), run_time=0.6)

        # 双向箭头说明
        arrow_right = Arrow(
            LEFT * 1.0 + DOWN * 0.8,
            RIGHT * 1.0 + DOWN * 0.8,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        arrow_left = Arrow(
            RIGHT * 1.0 + DOWN * 1.2,
            LEFT * 1.0 + DOWN * 1.2,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        convert_text = Text(
            "可以互相转换", font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 1.0)
        self.play(
            Create(arrow_right), Create(arrow_left),
            FadeIn(convert_text),
            run_time=0.6
        )
        self.wait(0.8)

        # 更多例子
        more_title = Text(
            "更多例子", font=FONT, font_size=24, color=COLOR_EXAMPLE
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(more_title), run_time=0.3)

        examples = VGroup(
            MathTex(r"\frac{5}{8} = 5 \div 8", font_size=40, color=WHITE),
            MathTex(r"\frac{7}{10} = 7 \div 10", font_size=40, color=WHITE),
            MathTex(r"\frac{1}{2} = 1 \div 2", font_size=40, color=WHITE),
        ).arrange(DOWN, buff=0.6).move_to(DOWN * 4.5)

        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 分数线就是除号
    # ------------------------------------------------------------------
    def scene_6_fraction_bar(self):
        """视觉演示: 分数线 = 除号"""

        title = Text(
            "分数线就是除号", font=FONT, font_size=40,
            color=COLOR_FRAC_LINE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 大号除号
        div_symbol = MathTex(r"\div", font_size=120, color=COLOR_FRAC_LINE)
        div_symbol.move_to(UP * 2.5)
        self.play(Write(div_symbol), run_time=0.6)

        # 分解除号: 一条横线 + 上下两个点
        explain1 = Text(
            "除号由三部分组成：", font=FONT, font_size=24, color=WHITE
        ).move_to(UP * 0.5)
        explain2 = Text(
            "一条横线 + 上下各一个点", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.2)
        self.play(Write(explain1), run_time=0.4)
        self.play(Write(explain2), run_time=0.4)
        self.wait(0.5)

        # 变换: 除号 → 分数
        transition = Text(
            "把数字放到点的位置...", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(transition, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 展示变换过程
        # 左边: 3 ÷ 4
        left_expr = MathTex(
            r"3", r"\div", r"4",
            font_size=72
        ).move_to(DOWN * 3.5 + LEFT * 2.5)
        left_expr[0].set_color(COLOR_NUMER)
        left_expr[1].set_color(COLOR_FRAC_LINE)
        left_expr[2].set_color(COLOR_DENOM)

        self.play(Write(left_expr), run_time=0.5)

        # 箭头
        arrow = Arrow(
            DOWN * 3.5 + LEFT * 0.5,
            DOWN * 3.5 + RIGHT * 0.5,
            color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(Create(arrow), run_time=0.3)

        # 右边: 3/4
        right_frac = MathTex(
            r"\frac{3}{4}",
            font_size=80
        ).move_to(DOWN * 3.5 + RIGHT * 2.5)
        right_frac[0][0].set_color(COLOR_NUMER)
        right_frac[0][1].set_color(COLOR_FRAC_LINE)
        right_frac[0][2].set_color(COLOR_DENOM)
        self.play(Write(right_frac), run_time=0.6)

        # 强调框
        key_text = Text(
            "分数线 ＝ 除号",
            font=FONT, font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 5.5)
        key_box = SurroundingRectangle(
            key_text, color=COLOR_HL, stroke_width=2.5, buff=0.2, corner_radius=0.1
        )
        self.play(FadeIn(key_text), Create(key_box), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 7: 分母不能为0
    # ------------------------------------------------------------------
    def scene_7_zero_warning(self):
        """强调分母(除数)不能为0"""

        title = Text(
            "特别注意！", font=FONT, font_size=44,
            color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 警告图标
        warn_triangle = Triangle(
            fill_color=COLOR_WARN, fill_opacity=0.15,
            stroke_color=COLOR_WARN, stroke_width=3
        ).scale(1.2).move_to(UP * 3.0)
        warn_text = Text(
            "!", font=FONT, font_size=48, color=COLOR_WARN, weight=BOLD
        ).move_to(UP * 2.85)
        self.play(Create(warn_triangle), FadeIn(warn_text, scale=0.5), run_time=0.6)

        # 核心信息
        rule1 = Text(
            "分母不能为 0", font=FONT, font_size=36,
            color=WHITE, weight=BOLD
        ).move_to(UP * 0.8)
        rule2 = Text(
            "除数不能为 0", font=FONT, font_size=36,
            color=WHITE, weight=BOLD
        ).move_to(DOWN * 0.2)
        self.play(Write(rule1), run_time=0.5)
        self.play(Write(rule2), run_time=0.5)

        # 原因说明
        reason = Text(
            "因为 0 不能做除数", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(reason, shift=UP * 0.2), run_time=0.4)

        # 错误示例
        wrong = MathTex(
            r"\frac{5}{0}", font_size=72, color=COLOR_DENOM
        ).move_to(DOWN * 3.5)
        cross = Cross(wrong, stroke_color=COLOR_WARN, stroke_width=5)
        wrong_label = Text(
            "没有意义！", font=FONT, font_size=24, color=COLOR_WARN
        ).next_to(wrong, RIGHT, buff=0.5)

        self.play(Write(wrong), run_time=0.5)
        self.play(Create(cross), FadeIn(wrong_label), run_time=0.5)

        # 正确的条件
        correct_box = RoundedRectangle(
            width=7.0, height=1.5,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_FRAC_LINE, stroke_width=2.5
        ).move_to(DOWN * 5.8)
        correct_text = MathTex(
            r"a \div b = \frac{a}{b} \quad (b \neq 0)",
            font_size=38, color=COLOR_HL
        ).move_to(DOWN * 5.8)

        self.play(FadeIn(correct_box), Write(correct_text), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------
    def scene_8_outro(self):
        """作者信息放大 + 关注提示"""

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

        # 装饰: 分数和除号交替排列
        colors = [COLOR_NUMER, COLOR_DENOM, COLOR_FRAC_LINE,
                  COLOR_HL, COLOR_EXAMPLE, COLOR_WARN]
        symbols = VGroup()
        for i, c in enumerate(colors):
            if i % 2 == 0:
                sym = MathTex(r"\div", font_size=36, color=c)
            else:
                sym = MathTex(r"\frac{a}{b}", font_size=28, color=c)
            sym.move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            symbols.add(sym)

        self.play(*[FadeIn(s, scale=0.3) for s in symbols], run_time=0.5)
        self.play(Rotate(symbols, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, symbols)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 002_分数与除法.py FractionDivisionLesson
#   高质量:    manim -qh  002_分数与除法.py FractionDivisionLesson
#   4K:        manim -qk  002_分数与除法.py FractionDivisionLesson
# ======================================================================
