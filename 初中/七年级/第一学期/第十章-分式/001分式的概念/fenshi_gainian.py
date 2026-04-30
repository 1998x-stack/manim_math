"""
分式的概念 - 七年级数学教学动画
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
    manim -pql fenshi_gainian.py FenshiGainian   # 快速预览
    manim -qh  fenshi_gainian.py FenshiGainian   # 高质量
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置 - TikTok 竖屏
# ══════════════════════════════════════════════════
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ══════════════════════════════════════════════════
#  颜色配置
# ══════════════════════════════════════════════════
BG_COLOR       = "#1a1a2e"
C_PRIMARY      = "#4fc3f7"   # 浅蓝 - 主色调
C_FRACTION     = "#f9a825"   # 金黄 - 分式
C_NUMERATOR    = "#81c784"   # 绿色 - 分子
C_DENOMINATOR  = "#e57373"   # 红色 - 分母
C_HIGHLIGHT    = "#fff176"   # 亮黄 - 高亮
C_CONDITION    = "#ce93d8"   # 紫色 - 条件
C_WRONG        = "#ef5350"   # 红色 - 错误/禁止
C_CORRECT      = "#66bb6a"   # 绿色 - 正确
C_CARD_BG      = "#16213e"   # 深蓝 - 卡片背景
C_SUBTITLE     = "#b0bec5"   # 灰白 - 副标题


# ══════════════════════════════════════════════════
#  字体
# ══════════════════════════════════════════════════
FONT = "PingFang SC"

# 字号规范
FS_TITLE    = 38
FS_SUBTITLE = 28
FS_BODY     = 24
FS_SMALL    = 20
FS_AUTHOR   = 20
FS_FORMULA  = 36
FS_BIG      = 52


class FenshiGainian(Scene):
    """
    分式的概念 - 七年级数学教学动画

    场景结构：
      1. 开场钩子 (0–5s)
      2. 分式的定义 (5–16s)
      3. 有意义的条件 (16–28s)
      4. 值为零的条件 (28–40s)
      5. 三规则总结 (40–51s)
      6. 片尾 (51–57s)
    """

    # ──────────────────────────────────────────────
    #  入口
    # ──────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 作者信息 - 全程保留
        self.author_bar = self._make_author_bar()
        self.add(self.author_bar)

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_definition()
        self.scene_3_meaning()
        self.scene_4_zero()
        self.scene_5_summary()
        self.scene_6_outro()

    # ══════════════════════════════════════════════
    #  SCENE 1 - 开场钩子
    # ══════════════════════════════════════════════
    def scene_1_hook(self):
        """让学生产生疑问：这些式子哪里不一样？"""

        # 钩子问题
        hook_q = Text(
            "下面这些式子，你能分辨吗？",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE
        ).move_to(UP * 5.5)

        self.play(FadeIn(hook_q, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.3)

        # 三个式子 - 整式 vs 分式
        expr1 = MathTex(r"3x^2", font_size=FS_FORMULA, color=WHITE)
        expr2 = MathTex(r"\dfrac{x}{2}", font_size=FS_FORMULA, color=WHITE)
        expr3 = MathTex(r"\dfrac{x}{x+1}", font_size=FS_FORMULA, color=C_FRACTION)

        exprs = VGroup(expr1, expr2, expr3).arrange(RIGHT, buff=1.2).move_to(UP * 4.0)

        for e in exprs:
            self.play(FadeIn(e, shift=UP * 0.2), run_time=0.4)

        self.wait(0.5)

        # 高亮第三个，打问号
        hl_rect = SurroundingRectangle(expr3, color=C_FRACTION, buff=0.15, corner_radius=0.1)
        self.play(Create(hl_rect), run_time=0.5)

        q_mark = Text("?", font=FONT, font_size=FS_BIG, color=C_FRACTION).next_to(expr3, UP, buff=0.2)
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.4)
        self.wait(0.3)

        # 标注：分母含字母！
        note_arrow = Arrow(
            start=DOWN * 0.3 + RIGHT * 2.2,
            end=expr3.get_bottom() + DOWN * 0.1,
            color=C_FRACTION, buff=0.05, stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        note_text = Text(
            "分母含有字母！",
            font=FONT, font_size=FS_SMALL, color=C_FRACTION
        ).next_to(note_arrow.get_start(), DOWN, buff=0.1)
        
        self.play(
            GrowArrow(note_arrow),
            FadeIn(note_text, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(0.5)

        # 主标题出现
        main_title = Text(
            "分式的概念", font=FONT, font_size=FS_BIG, color=C_FRACTION,
            weight=BOLD
        ).move_to(UP * 2.5)

        self.play(
            FadeOut(VGroup(hook_q, exprs, hl_rect, q_mark, note_arrow, note_text)),
            Write(main_title),
            run_time=0.8
        )
        self.wait(0.5)

        self.play(
            main_title.animate.scale(0.55).move_to(UP * 6.0).set_color(C_SUBTITLE),
            run_time=0.5
        )
        self.main_title_small = main_title  # 保留小标题

    # ══════════════════════════════════════════════
    #  SCENE 2 - 分式的定义
    # ══════════════════════════════════════════════
    def scene_2_definition(self):
        """A/B 结构 + B含字母 + 与分数对比"""

        # 场景标题
        scene_title = self._section_title("① 什么是分式？", UP * 6.8)
        self.play(FadeIn(scene_title, shift=DOWN * 0.2), run_time=0.4)

        # ── 核心公式 A/B ──
        formula = MathTex(
            r"\dfrac{A}{B}",
            font_size=70,
            color=WHITE
        ).move_to(UP * 4.8)

        self.play(Write(formula), run_time=0.8)
        self.wait(0.2)

        # 分子 Brace
        brace_A = Brace(formula, direction=UP, color=C_NUMERATOR, buff=0.05)
        label_A = Text("分子 A", font=FONT, font_size=FS_SMALL, color=C_NUMERATOR)
        label_A.next_to(brace_A, UP, buff=0.1)

        # 分母 Brace
        brace_B = Brace(formula, direction=DOWN, color=C_DENOMINATOR, buff=0.05)
        label_B = Text("分母 B", font=FONT, font_size=FS_SMALL, color=C_DENOMINATOR)
        label_B.next_to(brace_B, DOWN, buff=0.1)

        self.play(
            GrowFromCenter(brace_A), FadeIn(label_A),
            run_time=0.5
        )
        self.play(
            GrowFromCenter(brace_B), FadeIn(label_B),
            run_time=0.5
        )
        self.wait(0.3)

        # 说明文字
        cond_text = VGroup(
            Text("A, B are integral expressions", font=FONT, font_size=FS_BODY, color=C_SUBTITLE),
            Text("and B contains letters", font=FONT, font_size=FS_BODY, color=C_FRACTION),
        ).arrange(DOWN, buff=0.25).move_to(UP * 3.1)

        for t in cond_text:
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.4)
        
        # 强调 B 含字母
        self.play(
            cond_text[1].animate.scale(1.15),
            run_time=0.3
        )
        self.play(
            cond_text[1].animate.scale(1/1.15),
            run_time=0.2
        )
        self.wait(0.5)

        # ── 对比：分数 vs 分式 ──
        compare_title = Text(
            "Comparison:",
            font=FONT, font_size=FS_SMALL, color=C_SUBTITLE
        ).move_to(UP * 1.8)
        self.play(FadeIn(compare_title), run_time=0.3)

        # 左：分数（分母不含字母）
        frac_label = Text("Fraction", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE)
        frac_expr = MathTex(r"\dfrac{1}{2}", font_size=FS_FORMULA, color=C_SUBTITLE)
        frac_note = Text("denominator has no letters", font=FONT, font_size=FS_SMALL - 2, color=C_SUBTITLE)
        frac_group = VGroup(frac_label, frac_expr, frac_note).arrange(DOWN, buff=0.2)

        # 右：分式（分母含字母）
        shi_label = Text("Rational Expression", font=FONT, font_size=FS_SMALL, color=C_FRACTION)
        shi_expr = MathTex(r"\dfrac{1}{x}", font_size=FS_FORMULA, color=C_FRACTION)
        shi_note = Text("denominator contains letters ✓", font=FONT, font_size=FS_SMALL - 2, color=C_FRACTION)
        shi_group = VGroup(shi_label, shi_expr, shi_note).arrange(DOWN, buff=0.2)

        compare_group = VGroup(frac_group, shi_group).arrange(RIGHT, buff=1.5).move_to(UP * 0.5)

        self.play(FadeIn(frac_group, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(shi_group, shift=LEFT * 0.3), run_time=0.5)

        # 箭头：分数是分式的特例
        special_note = Text(
            "Fractions are special cases of rational expressions (letters = constants)",
            font=FONT, font_size=FS_SMALL - 2, color=C_SUBTITLE
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(special_note), run_time=0.4)
        self.wait(0.4)

        # ── 定义框 ──
        defn_text = Text(
            "Expressions in the form A/B (B contains letters) are called rational expressions",
            font=FONT, font_size=FS_SMALL + 1, color=WHITE
        ).move_to(DOWN * 2.0)

        defn_rect = SurroundingRectangle(
            defn_text, color=C_FRACTION, buff=0.25,
            corner_radius=0.15, stroke_width=2.5
        )
        defn_bg = defn_rect.copy().set_fill(C_CARD_BG, opacity=0.9).set_stroke(opacity=0)

        self.play(FadeIn(defn_bg), Create(defn_rect), Write(defn_text), run_time=0.8)
        self.wait(1.5)

        # 清理
        cleanup = VGroup(
            scene_title, formula, brace_A, label_A, brace_B, label_B,
            cond_text, compare_title, compare_group, special_note
        )
        self.play(FadeOut(cleanup), run_time=0.5)

        # 把定义框移到上方保留
        self.defn_group = VGroup(defn_bg, defn_rect, defn_text)
        self.play(
            self.defn_group.animate.scale(0.75).move_to(UP * 5.3),
            run_time=0.5
        )

    # ══════════════════════════════════════════════
    #  SCENE 3 - 有意义的条件
    # ══════════════════════════════════════════════
    def scene_3_meaning(self):
        """B ≠ 0 才有意义，用例子 1/(x-2) 说明"""

        scene_title = self._section_title("② 分式有意义的条件", UP * 6.8)
        self.play(FadeIn(scene_title, shift=DOWN * 0.2), run_time=0.4)

        # 示例分式
        example = MathTex(
            r"\dfrac{1}{x-2}",
            font_size=70, color=C_FRACTION
        ).move_to(UP * 5.3)

        # 先把定义框让位
        self.play(
            FadeOut(self.defn_group),
            Write(example),
            run_time=0.6
        )
        self.wait(0.3)

        # 提问
        q = Text(
            "What happens when x = 2?",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(q, shift=UP * 0.3), run_time=0.5)
        self.wait(0.4)

        # 代入计算过程
        step1 = MathTex(
            r"\dfrac{1}{2-2}",
            font_size=60, color=WHITE
        ).move_to(UP * 2.8)
        eq1 = Text("=", font=FONT, font_size=FS_FORMULA, color=WHITE).next_to(step1, RIGHT, buff=0.2)
        step2 = MathTex(
            r"\dfrac{1}{0}",
            font_size=60, color=C_WRONG
        ).next_to(eq1, RIGHT, buff=0.2)

        self.play(Write(step1), FadeIn(eq1), run_time=0.5)
        self.play(Write(step2), run_time=0.4)
        self.wait(0.3)

        # 打 × + 无意义提示
        cross = Text("×", font=FONT, font_size=80, color=C_WRONG).next_to(step2, RIGHT, buff=0.25)
        self.play(FadeIn(cross, scale=0.3), run_time=0.4)

        meaningless = Text(
            "Undefined! Denominator cannot be 0",
            font=FONT, font_size=FS_BODY, color=C_WRONG
        ).move_to(UP * 1.5)
        meaningless_rect = SurroundingRectangle(
            meaningless, color=C_WRONG, buff=0.2, corner_radius=0.1, stroke_width=2
        )
        self.play(FadeIn(meaningless), Create(meaningless_rect), run_time=0.5)
        self.wait(0.5)

        # 有意义的条件
        cond_title = Text(
            "So, condition for meaning:",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE
        ).move_to(UP * 0.3)
        self.play(FadeIn(cond_title), run_time=0.4)

        cond_specific = MathTex(
            r"x - 2 \neq 0 \quad \Longrightarrow \quad x \neq 2",
            font_size=FS_FORMULA, color=C_CONDITION
        ).move_to(DOWN * 0.6)
        self.play(Write(cond_specific), run_time=0.7)
        self.wait(0.4)

        # 通用规则大框
        rule_text = Text(
            "Rational expression meaningful ⟺ Denominator B ≠ 0",
            font=FONT, font_size=FS_BODY + 2, color=WHITE
        ).move_to(DOWN * 2.2)

        rule_bg = RoundedRectangle(
            width=rule_text.width + 0.8, height=0.85,
            corner_radius=0.2, fill_color=C_CARD_BG,
            fill_opacity=0.95, stroke_color=C_CONDITION, stroke_width=3
        ).move_to(rule_text.get_center())

        rule_formula = MathTex(
            r"B \neq 0",
            font_size=FS_FORMULA + 8, color=C_CONDITION
        ).move_to(DOWN * 3.3)

        self.play(FadeIn(rule_bg), Write(rule_text), run_time=0.6)
        self.play(Write(rule_formula), run_time=0.5)

        # 规则框
        rule_outer = SurroundingRectangle(
            VGroup(rule_bg, rule_formula), color=C_CONDITION,
            buff=0.3, corner_radius=0.2, stroke_width=2.5
        )
        self.play(Create(rule_outer), run_time=0.4)
        self.wait(1.8)

        # 保存有意义的规则组
        self.meaning_group = VGroup(rule_bg, rule_text, rule_formula, rule_outer)

        # 清理场景元素
        cleanup = VGroup(
            scene_title, example, q, step1, eq1, step2,
            cross, meaningless, meaningless_rect,
            cond_title, cond_specific
        )
        self.play(FadeOut(cleanup), run_time=0.5)
        self.play(
            self.meaning_group.animate.scale(0.7).move_to(UP * 5.0),
            run_time=0.5
        )

    # ══════════════════════════════════════════════
    #  SCENE 4 - 分式值为零的条件
    # ══════════════════════════════════════════════
    def scene_4_zero(self):
        """A=0 且 B≠0，双重条件，缺一不可"""

        scene_title = self._section_title("③ 分式值为零的条件", UP * 6.8)
        self.play(FadeIn(scene_title, shift=DOWN * 0.2), run_time=0.4)

        # 把上方内容移走
        self.play(FadeOut(self.meaning_group), run_time=0.3)

        # 示例分式
        example = MathTex(
            r"\dfrac{x-1}{x+2}",
            font_size=70, color=C_FRACTION
        ).move_to(UP * 5.3)
        self.play(Write(example), run_time=0.6)
        self.wait(0.2)

        # 分析提示
        q2 = Text(
            "When does the rational expression equal 0?",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT
        ).move_to(UP * 4.0)
        self.play(FadeIn(q2), run_time=0.4)
        self.wait(0.3)

        # 条件1：分子 = 0
        cond1_title = Text("Condition 1: Numerator = 0", font=FONT, font_size=FS_BODY, color=C_NUMERATOR).move_to(UP * 2.8)
        cond1_eq = MathTex(r"x - 1 = 0 \;\Longrightarrow\; x = 1", font_size=FS_FORMULA, color=C_NUMERATOR).move_to(UP * 2.0)
        self.play(FadeIn(cond1_title), run_time=0.3)
        self.play(Write(cond1_eq), run_time=0.5)
        self.wait(0.3)

        # 验证代入：分母不为0
        verify_title = Text("Verify substitution x = 1:", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(UP * 0.9)
        verify_calc = MathTex(
            r"\dfrac{1-1}{1+2} = \dfrac{0}{3} = 0 \quad \checkmark",
            font_size=FS_FORMULA - 4, color=C_CORRECT
        ).move_to(UP * 0.1)
        self.play(FadeIn(verify_title), run_time=0.3)
        self.play(Write(verify_calc), run_time=0.5)
        self.wait(0.4)

        # 条件2：分母 ≠ 0（且验证通过）
        cond2_title = Text("Condition 2: Denominator ≠ 0", font=FONT, font_size=FS_BODY, color=C_DENOMINATOR).move_to(DOWN * 1.0)
        cond2_eq = MathTex(r"x + 2 \neq 0 \;\Longrightarrow\; x \neq -2", font_size=FS_FORMULA, color=C_DENOMINATOR).move_to(DOWN * 1.8)
        self.play(FadeIn(cond2_title), run_time=0.3)
        self.play(Write(cond2_eq), run_time=0.5)
        self.wait(0.3)

        # "且"连接词强调
        and_text = Text(
            "Both conditions are required!",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(and_text, scale=1.1), run_time=0.4)
        self.wait(0.4)

        # 通用规则
        rule2_text = Text(
            "Rational expression = 0 ⟺ Numerator A = 0  &&  Denominator B ≠ 0",
            font=FONT, font_size=FS_SMALL + 1, color=WHITE
        ).move_to(DOWN * 4.0)
        rule2_bg = RoundedRectangle(
            width=rule2_text.width + 0.8, height=0.85,
            corner_radius=0.2, fill_color=C_CARD_BG,
            fill_opacity=0.95, stroke_color=C_CORRECT, stroke_width=3
        ).move_to(rule2_text.get_center())
        self.play(FadeIn(rule2_bg), Write(rule2_text), run_time=0.6)

        rule2_formula = MathTex(
            r"A = 0 \quad \&\& \quad B \neq 0",
            font_size=FS_FORMULA, color=C_CORRECT
        ).move_to(DOWN * 5.0)
        self.play(Write(rule2_formula), run_time=0.5)

        rule2_outer = SurroundingRectangle(
            VGroup(rule2_bg, rule2_formula), color=C_CORRECT,
            buff=0.25, corner_radius=0.2, stroke_width=2.5
        )
        self.play(Create(rule2_outer), run_time=0.4)
        self.wait(1.8)

        # 保存
        self.zero_group = VGroup(rule2_bg, rule2_text, rule2_formula, rule2_outer)

        # 清理
        cleanup = VGroup(
            scene_title, example, q2, cond1_title, cond1_eq,
            verify_title, verify_calc, cond2_title, cond2_eq, and_text
        )
        self.play(FadeOut(cleanup), run_time=0.5)
        self.play(
            self.zero_group.animate.scale(0.7).move_to(UP * 5.0),
            run_time=0.4
        )

    # ══════════════════════════════════════════════
    #  SCENE 5 - 三规则总结
    # ══════════════════════════════════════════════
    def scene_5_summary(self):
        """汇总三条核心规则"""

        # 清理之前保留的内容
        self.play(FadeOut(self.zero_group), run_time=0.3)

        # 总结标题
        summ_title = Text(
            "📝  Knowledge Summary",
            font=FONT, font_size=FS_TITLE, color=C_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(summ_title), run_time=0.5)

        # 三张卡片
        cards = VGroup(
            self._make_summary_card(
                "① Rational Expression Definition",
                r"\dfrac{A}{B}\text{ (B contains letters)}",
                C_FRACTION, UP * 4.5
            ),
            self._make_summary_card(
                "② Meaningful Condition",
                r"B \neq 0",
                C_CONDITION, UP * 1.5
            ),
            self._make_summary_card(
                "③ Equals Zero Condition",
                r"A=0 \;\&\&\; B \neq 0",
                C_CORRECT, DOWN * 1.5
            ),
        )

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.6)
            self.wait(0.3)

        self.wait(0.5)

        # 整体高亮闪烁
        self.play(
            cards[0].animate.set_color(C_FRACTION),
            cards[1].animate.set_color(C_CONDITION),
            cards[2].animate.set_color(C_CORRECT),
            run_time=0.4
        )
        self.wait(0.3)

        # 牢记口诀
        tips = Text(
            "Remember: B ≠ 0 → meaningful; A = 0 && B ≠ 0 → equals zero",
            font=FONT, font_size=FS_SMALL - 1, color=C_SUBTITLE
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(tips), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(FadeOut(VGroup(summ_title, cards, tips)), run_time=0.6)

    # ══════════════════════════════════════════════
    #  SCENE 6 - 片尾
    # ══════════════════════════════════════════════
    def scene_6_outro(self):
        """作者信息 + 关注引导"""

        # 主标题大字复现
        big_title = Text(
            "分式的概念", font=FONT, font_size=FS_BIG, color=C_FRACTION, weight=BOLD
        ).move_to(UP * 2.5)
        self.play(Write(big_title), run_time=0.7)

        # 作者大名
        author_name = Text(
            "SH Math Tutor",
            font=FONT, font_size=FS_SUBTITLE + 4, color=WHITE
        ).move_to(UP * 0.8)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE
        ).next_to(author_name, DOWN, buff=0.25)

        self.play(FadeIn(author_name, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)

        # 分隔线
        line = Line(LEFT * 3.5, RIGHT * 3.5, color=C_SUBTITLE, stroke_width=1).move_to(DOWN * 0.5)
        self.play(Create(line), run_time=0.3)

        # 关注文字
        follow_text = Text(
            "Follow me for more math tips!",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT
        ).move_to(DOWN * 1.3)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 小装饰分式们
        deco_exprs = VGroup(
            MathTex(r"\frac{x}{x+1}", font_size=24, color=C_FRACTION),
            MathTex(r"\frac{a-b}{c}", font_size=24, color=C_CONDITION),
            MathTex(r"\frac{2x}{x^2-1}", font_size=24, color=C_CORRECT),
            MathTex(r"\frac{m+n}{m-n}", font_size=24, color=C_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.7).move_to(DOWN * 2.8)

        self.play(FadeIn(deco_exprs, shift=UP * 0.2), run_time=0.5)
        self.play(
            Wiggle(deco_exprs, scale_value=1.08, rotation_angle=0.02),
            run_time=1.0
        )

        # 底部口号
        slogan = Text(
            "One problem a day keeps math anxiety away!",
            font=FONT, font_size=FS_SMALL, color=C_SUBTITLE
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(slogan), run_time=0.4)

        self.wait(1.5)

        # 整体淡出
        self.play(
            FadeOut(VGroup(big_title, author_name, author_id, line,
                           follow_text, deco_exprs, slogan)),
            FadeOut(self.author_bar),
            run_time=0.8
        )

    # ══════════════════════════════════════════════
    #  工具方法
    # ══════════════════════════════════════════════
    def _make_author_bar(self):
        """作者信息条（全程显示在顶部）"""
        author = Text(
            "SH Math Tutor  @emptyandcalm",
            font=FONT, font_size=FS_AUTHOR, color=GRAY_B
        ).move_to(UP * 7.2)
        return author

    def _section_title(self, text: str, position):
        """场景小标题（带左侧彩条）"""
        bar = Rectangle(
            width=0.1, height=0.55,
            fill_color=C_PRIMARY, fill_opacity=1,
            stroke_width=0
        )
        label = Text(text, font=FONT, font_size=FS_SUBTITLE, color=C_PRIMARY)
        group = VGroup(bar, label).arrange(RIGHT, buff=0.2)
        group.move_to(position)
        return group

    def _make_summary_card(self, title_str: str, formula_str: str, color, position):
        """创建总结卡片（背景框 + 标题 + 公式）"""
        title_mob = Text(title_str, font=FONT, font_size=FS_BODY, color=color)
        formula_mob = MathTex(formula_str, font_size=FS_FORMULA, color=WHITE)
        content = VGroup(title_mob, formula_mob).arrange(DOWN, buff=0.3)

        bg = RoundedRectangle(
            width=7.5, height=content.height + 0.8,
            corner_radius=0.25,
            fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=color, stroke_width=2.5
        )
        card = VGroup(bg, content)
        content.move_to(bg.get_center())
        card.move_to(position)
        return card