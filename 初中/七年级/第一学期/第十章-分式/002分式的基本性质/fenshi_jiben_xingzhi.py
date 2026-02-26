"""分式的基本性质 - 七年级数学教学动画
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
    manim -pql fenshi_jiben_xingzhi.py FenshiJibenXingzhi   # 快速预览
    manim -qh  fenshi_jiben_xingzhi.py FenshiJibenXingzhi   # 高质量
"""

from manim import *
import numpy as np

# ══════════════════════════════════════════════════
#  全局配置 - TikTok 竖屏
# ══════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ══════════════════════════════════════════════════
#  调色板
# ══════════════════════════════════════════════════
BG_COLOR    = "#1a1a2e"
C_PRIMARY   = "#4fc3f7"   # 浅蓝
C_MULTIPLY  = "#f9a825"   # 金黄  - 乘变换
C_DIVIDE    = "#81c784"   # 绿色  - 除变换
C_HIGHLIGHT = "#fff176"   # 亮黄
C_EQUAL     = "#ce93d8"   # 紫色  - 等号/不变
C_WRONG     = "#ef5350"   # 红色
C_CORRECT   = "#66bb6a"   # 绿色
C_CARD_BG   = "#16213e"   # 深蓝卡片背景
C_SUBTITLE  = "#b0bec5"   # 灰白

# ══════════════════════════════════════════════════
#  字体 & 字号
# ══════════════════════════════════════════════════
FONT     = "Noto Sans CJK SC"
FS_TITLE = 38
FS_SUB   = 28
FS_BODY  = 24
FS_SMALL = 20
FS_FORM  = 36
FS_BIG   = 52
FS_AUTH  = 20

# ══════════════════════════════════════════════════
#  主场景
# ══════════════════════════════════════════════════
class FenshiJibenXingzhi(Scene):
    """
    分式的基本性质
    Scene 1 : 开场钩子          (0–6s)
    Scene 2 : 性质一 — 同乘     (6–19s)
    Scene 3 : 性质二 — 同除(约分)(19–31s)
    Scene 4 : 完整规则大卡      (31–41s)
    Scene 5 : 应用 约分/通分    (41–53s)
    Scene 6 : 总结 + 片尾       (53–60s)
    """

    # ──────────────────────────────────────────
    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_bar = self._make_author_bar()
        self.add(self.author_bar)

        self.scene_1_hook()
        self.scene_2_multiply()
        self.scene_3_divide()
        self.scene_4_combined_rule()
        self.scene_5_applications()
        self.scene_6_outro()

    # ══════════════════════════════════════════
    #  SCENE 1 — 开场钩子
    # ══════════════════════════════════════════
    def scene_1_hook(self):
        hook_q = Text(
            "还记得分数的基本性质吗？",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).move_to(UP * 5.5)
        self.play(FadeIn(hook_q, shift=DOWN * 0.3), run_time=0.5)

        # 1/2 = 2/4 = 3/6
        f1 = MathTex(r"\dfrac{1}{2}", font_size=FS_FORM, color=WHITE)
        eq1 = Text("=", font=FONT, font_size=FS_FORM, color=C_SUBTITLE)
        f2 = MathTex(r"\dfrac{2}{4}", font_size=FS_FORM, color=WHITE)
        eq2 = Text("=", font=FONT, font_size=FS_FORM, color=C_SUBTITLE)
        f3 = MathTex(r"\dfrac{3}{6}", font_size=FS_FORM, color=WHITE)
        frac_row = VGroup(f1, eq1, f2, eq2, f3).arrange(RIGHT, buff=0.35).move_to(UP * 4.1)

        self.play(FadeIn(frac_row, shift=UP * 0.2), run_time=0.7)
        self.wait(0.3)

        # 说明：分子分母同乘同数
        note = Text(
            "分子、分母同乘（或同除）同一个不为零的数，分数值不变",
            font=FONT, font_size=FS_SMALL - 1, color=C_HIGHLIGHT,
        ).move_to(UP * 3.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # 过渡语
        bridge = Text(
            "分式也有完全类似的性质！",
            font=FONT, font_size=FS_BODY + 2, color=C_PRIMARY,
        ).move_to(UP * 1.8)
        self.play(Write(bridge), run_time=0.5)
        self.wait(0.3)

        # 主标题
        main_title = Text(
            "分式的基本性质",
            font=FONT, font_size=FS_BIG, color=C_MULTIPLY, weight=BOLD,
        ).move_to(UP * 0.6)
        self.play(Write(main_title), run_time=0.7)
        self.wait(0.4)

        # 把标题缩小移顶留用
        self.play(
            FadeOut(VGroup(hook_q, frac_row, note, bridge)),
            main_title.animate.scale(0.5).move_to(UP * 6.0).set_color(C_SUBTITLE),
            run_time=0.5,
        )
        self.small_title = main_title

    # ══════════════════════════════════════════
    #  SCENE 2 — 性质一：同乘不为零的整式
    # ══════════════════════════════════════════
    def scene_2_multiply(self):
        sec_title = self._section_title("性质一：同乘不为零的整式", UP * 6.8)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # ── 通用公式展示 ──
        # 左：A/B
        lhs = MathTex(r"\dfrac{A}{B}", font_size=68, color=WHITE).move_to(UP * 5.2 + LEFT * 3.0)

        # 箭头
        arr = Arrow(
            LEFT * 0.6, RIGHT * 0.6,
            color=C_MULTIPLY, buff=0,
            stroke_width=5, max_tip_length_to_length_ratio=0.25,
        ).move_to(UP * 5.2)

        # 右：(A×C)/(B×C)
        rhs = MathTex(
            r"\dfrac{A \times C}{B \times C}",
            font_size=56, color=WHITE,
        ).move_to(UP * 5.2 + RIGHT * 2.5)

        self.play(Write(lhs), run_time=0.5)
        self.play(GrowArrow(arr), run_time=0.4)
        self.play(Write(rhs), run_time=0.6)
        self.wait(0.2)

        # 分子 C 标色
        rhs_copy = rhs.copy()
        
        successful_animation = False
        
        c_elements = []
        for i, mob in enumerate(rhs[0]):
            # Try to get the tex_string attribute safely
            if hasattr(mob, 'tex_string') and mob.tex_string:
                if 'C' in mob.tex_string:
                    c_elements.append(mob)
            elif hasattr(mob, 'get_tex_string'):
                try:
                    if mob.get_tex_string() == 'C':
                        c_elements.append(mob)
                except (AttributeError, TypeError):
                    # Some objects might not have get_tex_string implemented or may raise errors
                    continue
        
        if c_elements:
            self.play(*[mob.animate.set_color(C_MULTIPLY) for mob in c_elements], run_time=0.4)
            successful_animation = True
        elif len(rhs[0]) > 4 and len(rhs[0]) > 9:
            try:
                self.play(
                    rhs[0][4].animate.set_color(C_MULTIPLY),
                    rhs[0][9].animate.set_color(C_MULTIPLY),
                    run_time=0.4,
                )
                successful_animation = True
            except IndexError:
                pass
        elif len(rhs[0]) > 4:
            try:
                self.play(rhs[0][4].animate.set_color(C_MULTIPLY), run_time=0.4)
                successful_animation = True
            except IndexError:
                pass
        
        if not successful_animation:
            self.wait(0.4)

        # 条件框：C ≠ 0
        cond = MathTex(r"C \neq 0", font_size=FS_FORM, color=C_WRONG).move_to(UP * 4.0)
        cond_rect = SurroundingRectangle(cond, color=C_WRONG, buff=0.2, corner_radius=0.12, stroke_width=2.5)
        cond_label = Text("重要条件", font=FONT, font_size=FS_SMALL - 2, color=C_WRONG).next_to(cond_rect, LEFT, buff=0.15)
        self.play(Write(cond), Create(cond_rect), FadeIn(cond_label), run_time=0.5)
        self.wait(0.3)

        # ── 具体例子 1：x/(x+1), C=2 ──
        ex1_label = Text("例1：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(UP * 2.8 + LEFT * 3.5)

        ex1_lhs = MathTex(r"\dfrac{x}{x+1}", font_size=50, color=WHITE)
        ex1_eq  = Text("=", font=FONT, font_size=FS_FORM, color=C_SUBTITLE)
        ex1_rhs = MathTex(r"\dfrac{x \cdot 2}{(x+1) \cdot 2}", font_size=44, color=WHITE)
        ex1_row = VGroup(ex1_lhs, ex1_eq, ex1_rhs).arrange(RIGHT, buff=0.35).move_to(UP * 2.8)

        self.play(FadeIn(ex1_label), run_time=0.2)
        self.play(Write(ex1_lhs), run_time=0.4)
        self.play(FadeIn(ex1_eq), run_time=0.2)
        self.play(Write(ex1_rhs), run_time=0.5)

        # 乘以2 标记
        c2_top = MathTex(r"\times 2", font_size=FS_SMALL, color=C_MULTIPLY).next_to(ex1_rhs[0][1], UP, buff=0.05)
        c2_bot = MathTex(r"\times 2", font_size=FS_SMALL, color=C_MULTIPLY).next_to(ex1_rhs[0][4], DOWN, buff=0.05)
        self.play(FadeIn(c2_top), FadeIn(c2_bot), run_time=0.3)
        self.wait(0.3)

        # 简化结果
        ex1_eq2  = Text("=", font=FONT, font_size=FS_FORM, color=C_SUBTITLE)
        ex1_rhs2 = MathTex(r"\dfrac{2x}{2(x+1)}", font_size=50, color=C_CORRECT)
        ex1_ext  = VGroup(ex1_eq2, ex1_rhs2).arrange(RIGHT, buff=0.3).next_to(ex1_row, DOWN, buff=0.3)
        self.play(Write(ex1_ext), run_time=0.5)

        check1 = Text("✓ 分式的值不变", font=FONT, font_size=FS_SMALL, color=C_CORRECT).next_to(ex1_ext, RIGHT, buff=0.3)
        self.play(FadeIn(check1, scale=0.8), run_time=0.3)
        self.wait(0.4)

        # ── 具体例子 2：a/b, C=b+1 ──
        ex2_label = Text("例2：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(UP * 0.5 + LEFT * 3.5)
        ex2_lhs = MathTex(r"\dfrac{a}{b}", font_size=50, color=WHITE)
        ex2_eq  = Text("=", font=FONT, font_size=FS_FORM, color=C_SUBTITLE)
        ex2_rhs = MathTex(r"\dfrac{a(b+1)}{b(b+1)}", font_size=44, color=WHITE)
        ex2_row = VGroup(ex2_lhs, ex2_eq, ex2_rhs).arrange(RIGHT, buff=0.35).move_to(UP * 0.5)

        c_label = Text("（这里 C = b+1，需保证 b+1 ≠ 0）", font=FONT, font_size=FS_SMALL - 2, color=C_SUBTITLE).move_to(DOWN * 0.6)

        self.play(FadeIn(ex2_label), run_time=0.2)
        self.play(Write(ex2_row), run_time=0.6)
        self.play(FadeIn(c_label), run_time=0.3)
        self.wait(1.0)

        # 清理 Scene 2
        scene2_all = VGroup(
            sec_title, lhs, arr, rhs, cond, cond_rect, cond_label,
            ex1_label, ex1_row, c2_top, c2_bot, ex1_ext, check1,
            ex2_label, ex2_row, c_label,
        )
        self.play(FadeOut(scene2_all), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 3 — 性质二：同除 (约分)
    # ══════════════════════════════════════════
    def scene_3_divide(self):
        sec_title = self._section_title("性质二：同除不为零的整式", UP * 6.8)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # 通用公式（逆向展示）
        lhs_gen = MathTex(r"\dfrac{A \times C}{B \times C}", font_size=56, color=WHITE).move_to(UP * 5.3 + LEFT * 2.8)
        arr_gen = Arrow(
            LEFT * 0.6, RIGHT * 0.6,
            color=C_DIVIDE, buff=0,
            stroke_width=5, max_tip_length_to_length_ratio=0.25,
        ).move_to(UP * 5.3)
        rhs_gen = MathTex(r"\dfrac{A}{B}", font_size=68, color=WHITE).move_to(UP * 5.3 + RIGHT * 2.8)

        div_label = Text(
            "÷ C（即去掉公因式）",
            font=FONT, font_size=FS_SMALL, color=C_DIVIDE,
        ).move_to(UP * 4.2)

        self.play(Write(lhs_gen), GrowArrow(arr_gen), Write(rhs_gen), run_time=0.7)
        self.play(FadeIn(div_label, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)

        # ── 具体例子：2x² / (4x) ──
        ex_label = Text("例：约分", font=FONT, font_size=FS_BODY, color=C_SUBTITLE).move_to(UP * 3.0)
        self.play(FadeIn(ex_label), run_time=0.3)

        orig = MathTex(r"\dfrac{2x^2}{4x}", font_size=60, color=C_MULTIPLY).move_to(UP * 2.0)
        self.play(Write(orig), run_time=0.5)
        self.wait(0.2)

        # 拆解公因式
        step1_label = Text("提取公因式 2x：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(UP * 0.8)
        step1 = MathTex(
            r"\dfrac{2x \cdot x}{2x \cdot 2}",
            font_size=56, color=WHITE,
        ).move_to(UP * 0.0)

        self.play(FadeIn(step1_label), run_time=0.3)
        self.play(Write(step1), run_time=0.5)

        # 标记公因式
        common_box = SurroundingRectangle(
            VGroup(step1), color=C_DIVIDE, buff=0.1, corner_radius=0.1, stroke_width=2
        )
        self.play(Create(common_box), run_time=0.3)
        self.wait(0.2)

        # 约去公因式 → 结果
        result_label = Text("÷ 2x 得：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(DOWN * 1.3)
        result = MathTex(r"\dfrac{x}{2}", font_size=64, color=C_CORRECT).move_to(DOWN * 2.2)
        self.play(FadeIn(result_label), run_time=0.3)
        self.play(Write(result), run_time=0.5)

        # 最简分式标注
        simplest_rect = SurroundingRectangle(result, color=C_CORRECT, buff=0.25, corner_radius=0.15, stroke_width=2.5)
        simplest_label = Text(
            "最简分式（分子分母无公因式）",
            font=FONT, font_size=FS_SMALL - 2, color=C_CORRECT,
        ).next_to(simplest_rect, DOWN, buff=0.2)

        self.play(Create(simplest_rect), FadeIn(simplest_label), run_time=0.5)
        self.wait(1.2)

        scene3_all = VGroup(
            sec_title, lhs_gen, arr_gen, rhs_gen, div_label,
            ex_label, orig, step1_label, step1, common_box,
            result_label, result, simplest_rect, simplest_label,
        )
        self.play(FadeOut(scene3_all), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 4 — 完整规则大卡
    # ══════════════════════════════════════════
    def scene_4_combined_rule(self):
        sec_title = self._section_title("完整性质总览", UP * 6.8)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # 大公式块
        rule_title = Text("分式的基本性质", font=FONT, font_size=FS_BODY, color=C_MULTIPLY).move_to(UP * 5.5)
        self.play(FadeIn(rule_title), run_time=0.3)

        formula_main = MathTex(
            r"\dfrac{A}{B} = \dfrac{A \times C}{B \times C} = \dfrac{A \div C}{B \div C}",
            font_size=46, color=WHITE,
        ).move_to(UP * 4.3)
        formula_bg = RoundedRectangle(
            width=formula_main.width + 1.0, height=1.6,
            corner_radius=0.25, fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=C_MULTIPLY, stroke_width=3,
        ).move_to(formula_main.get_center())
        self.play(FadeIn(formula_bg), Write(formula_main), run_time=0.8)
        self.wait(0.2)

        # 两个箭头说明：乘 / 除
        arrow_mul = Arrow(
            formula_main.get_right() + LEFT * 0.1,
            formula_main.get_right() + RIGHT * 0.1,
            color=C_MULTIPLY, buff=0, stroke_width=4,
        )
        lbl_mul = Text("同乘 C", font=FONT, font_size=FS_SMALL, color=C_MULTIPLY).next_to(UP * 3.0 + LEFT * 1.5)

        # 用简单文本替代箭头
        explain_mul = Text(
            "← 分子分母同乘 C（扩分）",
            font=FONT, font_size=FS_SMALL + 1, color=C_MULTIPLY,
        ).move_to(UP * 3.1)
        explain_div = Text(
            "← 分子分母同除 C（约分）",
            font=FONT, font_size=FS_SMALL + 1, color=C_DIVIDE,
        ).move_to(UP * 2.4)

        self.play(FadeIn(explain_mul, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(explain_div, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.3)

        # C ≠ 0 大字强调
        c_big = MathTex(r"C \neq 0", font_size=FS_BIG, color=C_WRONG).move_to(UP * 1.2)
        c_rect = SurroundingRectangle(c_big, color=C_WRONG, buff=0.3, corner_radius=0.15, stroke_width=3)
        c_note = Text(
            "C 为不等于零的整式",
            font=FONT, font_size=FS_SMALL, color=C_WRONG,
        ).next_to(c_rect, DOWN, buff=0.2)
        self.play(Write(c_big), Create(c_rect), run_time=0.6)
        self.play(FadeIn(c_note), run_time=0.3)
        self.wait(0.4)

        # 类比提示
        analogy = VGroup(
            Text("类比分数的基本性质：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE),
            MathTex(r"\dfrac{a}{b} = \dfrac{a \times c}{b \times c}", font_size=38, color=C_SUBTITLE),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 0.8)
        analogy_rect = SurroundingRectangle(
            analogy, color=C_SUBTITLE, buff=0.25, corner_radius=0.15,
            stroke_width=1.5, stroke_opacity=0.6,
        )
        self.play(FadeIn(analogy), Create(analogy_rect), run_time=0.6)
        self.wait(1.5)

        scene4_all = VGroup(
            sec_title, rule_title, formula_bg, formula_main,
            explain_mul, explain_div, c_big, c_rect, c_note,
            analogy, analogy_rect,
        )
        self.play(FadeOut(scene4_all), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 5 — 应用：约分 & 通分
    # ══════════════════════════════════════════
    def scene_5_applications(self):
        sec_title = self._section_title("实际应用", UP * 6.8)
        self.play(FadeIn(sec_title, shift=DOWN * 0.2), run_time=0.4)

        # ── 应用1：约分 ──
        app1_title = self._mini_title("应用1：约分", UP * 5.8, C_MULTIPLY)
        self.play(FadeIn(app1_title), run_time=0.3)

        # (x²-x) / (x²-1)
        frac_orig = MathTex(
            r"\dfrac{x^2 - x}{x^2 - 1}",
            font_size=58, color=WHITE,
        ).move_to(UP * 4.6)
        self.play(Write(frac_orig), run_time=0.5)
        self.wait(0.2)

        # 因式分解步骤
        step_label = Text("因式分解：", font=FONT, font_size=FS_SMALL, color=C_SUBTITLE).move_to(UP * 3.5)
        step1 = MathTex(
            r"= \dfrac{x(x-1)}{(x+1)(x-1)}",
            font_size=52, color=WHITE,
        ).move_to(UP * 2.8)
        self.play(FadeIn(step_label), Write(step1), run_time=0.6)

        # 公因式 (x-1) 高亮
        factor_box = SurroundingRectangle(step1, color=C_DIVIDE, buff=0.1, corner_radius=0.1, stroke_width=2)
        factor_note = Text("公因式：(x-1)", font=FONT, font_size=FS_SMALL - 2, color=C_DIVIDE).next_to(factor_box, RIGHT, buff=0.2)
        self.play(Create(factor_box), FadeIn(factor_note), run_time=0.4)
        self.wait(0.2)

        # 约去 → 结果
        result1 = MathTex(r"= \dfrac{x}{x+1}", font_size=58, color=C_CORRECT).move_to(UP * 1.7)
        cond1   = Text("（x ≠ 1，x ≠ -1）", font=FONT, font_size=FS_SMALL - 2, color=C_SUBTITLE).next_to(result1, RIGHT, buff=0.2)
        self.play(Write(result1), FadeIn(cond1), run_time=0.5)
        self.wait(0.5)

        # ── 应用2：通分 ──
        app2_title = self._mini_title("应用2：通分", UP * 0.5, C_DIVIDE)
        self.play(FadeIn(app2_title), run_time=0.3)

        # 两个分式
        frac_a = MathTex(r"\dfrac{1}{x+1}", font_size=50, color=WHITE)
        comm   = Text("和", font=FONT, font_size=FS_BODY, color=C_SUBTITLE)
        frac_b = MathTex(r"\dfrac{1}{x-1}", font_size=50, color=WHITE)
        pair   = VGroup(frac_a, comm, frac_b).arrange(RIGHT, buff=0.4).move_to(DOWN * 0.5)
        self.play(Write(pair), run_time=0.5)
        self.wait(0.2)

        # 公分母
        denom_label = Text("公分母：(x+1)(x-1)", font=FONT, font_size=FS_SMALL, color=C_MULTIPLY).move_to(DOWN * 1.6)
        result2a = MathTex(r"\dfrac{x-1}{(x+1)(x-1)}", font_size=40, color=C_CORRECT)
        result2b = MathTex(r"\dfrac{x+1}{(x+1)(x-1)}", font_size=40, color=C_CORRECT)
        result2_row = VGroup(result2a, Text("和", font=FONT, font_size=FS_BODY, color=C_SUBTITLE), result2b).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.8)

        self.play(FadeIn(denom_label), run_time=0.3)
        self.play(Write(result2_row), run_time=0.6)
        self.wait(1.0)

        scene5_all = VGroup(
            sec_title, app1_title, frac_orig, step_label, step1,
            factor_box, factor_note, result1, cond1,
            app2_title, pair, denom_label, result2_row,
        )
        self.play(FadeOut(scene5_all), run_time=0.5)

    # ══════════════════════════════════════════
    #  SCENE 6 — 总结 + 片尾
    # ══════════════════════════════════════════
    def scene_6_outro(self):
        # 三条记忆卡
        summ_title = Text(
            "记住这三点！",
            font=FONT, font_size=FS_TITLE, color=C_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(summ_title), run_time=0.5)

        cards = VGroup(
            self._summary_card("同乘不为零的整式", r"\dfrac{A}{B} = \dfrac{A \times C}{B \times C}", C_MULTIPLY, UP * 4.5),
            self._summary_card("同除不为零的整式", r"\dfrac{A \times C}{B \times C} = \dfrac{A}{B}", C_DIVIDE,  UP * 1.8),
            self._summary_card("C 必须不等于零",    r"C \neq 0", C_WRONG, DOWN * 0.9),
        )
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.55)
            self.wait(0.2)

        self.wait(0.5)

        # 口诀
        tip = Text(
            "口诀：同乘同除不为零，分式的值永不变",
            font=FONT, font_size=FS_SMALL, color=C_SUBTITLE,
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(VGroup(summ_title, cards, tip, self.small_title)), run_time=0.5)

        # ── 片尾 ──
        main_big = Text(
            "分式的基本性质",
            font=FONT, font_size=FS_BIG, color=C_MULTIPLY, weight=BOLD,
        ).move_to(UP * 2.5)
        self.play(Write(main_big), run_time=0.6)

        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=FS_SUB + 4, color=WHITE,
        ).move_to(UP * 0.8)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_BODY, color=C_SUBTITLE,
        ).next_to(author_name, DOWN, buff=0.25)

        self.play(FadeIn(author_name, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)

        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=C_SUBTITLE, stroke_width=1).move_to(DOWN * 0.4)
        self.play(Create(divider), run_time=0.3)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=FS_BODY, color=C_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰分式
        deco = VGroup(
            MathTex(r"\frac{a}{b}=\frac{ac}{bc}", font_size=22, color=C_MULTIPLY),
            MathTex(r"\frac{2x}{4}=\frac{x}{2}", font_size=22, color=C_DIVIDE),
            MathTex(r"C\neq 0", font_size=22, color=C_WRONG),
            MathTex(r"\frac{x}{x+1}", font_size=22, color=C_EQUAL),
        ).arrange(RIGHT, buff=0.7).move_to(DOWN * 2.8)
        self.play(FadeIn(deco, shift=UP * 0.2), run_time=0.5)
        self.play(Wiggle(deco, scale_value=1.07), run_time=0.8)

        slogan = Text(
            "每天一道题，数学不再难！",
            font=FONT, font_size=FS_SMALL, color=C_SUBTITLE,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(slogan), run_time=0.4)

        self.wait(1.5)
        self.play(
            FadeOut(VGroup(main_big, author_name, author_id, divider,
                           follow, deco, slogan)),
            FadeOut(self.author_bar),
            run_time=0.8,
        )

    # ══════════════════════════════════════════
    #  工具方法
    # ══════════════════════════════════════════
    def _make_author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=FS_AUTH, color=GRAY_B,
        ).move_to(UP * 6.9)

    def _section_title(self, text: str, pos):
        bar = Rectangle(
            width=0.12, height=0.55,
            fill_color=C_PRIMARY, fill_opacity=1, stroke_width=0,
        )
        lbl = Text(text, font=FONT, font_size=FS_SUB, color=C_PRIMARY)
        grp = VGroup(bar, lbl).arrange(RIGHT, buff=0.2)
        grp.move_to(pos)
        return grp

    def _mini_title(self, text: str, pos, color=C_SUBTITLE):
        bar = Rectangle(
            width=0.08, height=0.42,
            fill_color=color, fill_opacity=1, stroke_width=0,
        )
        lbl = Text(text, font=FONT, font_size=FS_BODY, color=color)
        grp = VGroup(bar, lbl).arrange(RIGHT, buff=0.15)
        grp.move_to(pos)
        return grp

    def _summary_card(self, title_str: str, formula_str: str, color, pos):
        title_mob   = Text(title_str, font=FONT, font_size=FS_BODY, color=color)
        formula_mob = MathTex(formula_str, font_size=FS_FORM, color=WHITE)
        content     = VGroup(title_mob, formula_mob).arrange(DOWN, buff=0.25)
        bg = RoundedRectangle(
            width=7.6, height=content.height + 0.7,
            corner_radius=0.25,
            fill_color=C_CARD_BG, fill_opacity=0.95,
            stroke_color=color, stroke_width=2.5,
        )
        card = VGroup(bg, content)
        content.move_to(bg.get_center())
        card.move_to(pos)
        return card