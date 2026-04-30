"""
整式方程 - 因式分解法教学动画
Integral Equations - Factorization Method Teaching Animation

目标受众: 八年级学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
内容: 以 x³ - 4x = 0 为例，展示高次方程降次解法

渲染命令:
  manim -pql integral_equation_animation.py IntegralEquation   # 快速预览
  manim -qh  integral_equation_animation.py IntegralEquation   # 高质量
"""

from manim import *
import numpy as np

# ── 全局配置 TikTok 竖屏 ──────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ── 字体 ──────────────────────────────────────────────────────
CJK_FONT = "PingFang SC"

# ── 配色方案 ──────────────────────────────────────────────────
BG_COLOR        = "#1a1a2e"
COLOR_TITLE     = GOLD
COLOR_EQUATION  = "#00d4ff"   # 主方程蓝
COLOR_HIGHLIGHT = "#ff6b6b"   # 警示红
COLOR_STEP      = "#a8e6cf"   # 步骤绿
COLOR_RESULT    = "#ffeaa7"   # 结果黄
COLOR_FACTOR    = "#fd79a8"   # 因式粉
COLOR_ARROW     = "#74b9ff"   # 箭头蓝
COLOR_SUBTITLE  = GRAY_A
COLOR_AUTHOR    = GRAY_B
COLOR_BOX_BG    = "#16213e"


class IntegralEquation(Scene):
    """
    整式方程教学动画 - 七个场景
    Scene 1: 开场钩子
    Scene 2: 整式方程定义
    Scene 3: 核心思想 - 降次
    Scene 4: 例题解法 (x³ - 4x = 0)
    Scene 5: 零乘积定理
    Scene 6: 另一类型 (x³ = 8)
    Scene 7: 总结与片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 常驻作者信息
        self.author_bar = self._make_author_bar()
        self.add(self.author_bar)

        # 执行各场景
        self.scene1_hook()
        self.scene2_definition()
        self.scene3_core_idea()
        self.scene4_example()
        self.scene5_zero_product()
        self.scene6_cube_type()
        self.scene7_outro()

    # ─────────────────────────────────────────────────────────
    # 辅助函数
    # ─────────────────────────────────────────────────────────

    def _make_author_bar(self):
        """创建顶部作者信息条"""
        txt = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=CJK_FONT,
            font_size=18,
            color=COLOR_AUTHOR
        ).move_to(UP * 7.2)
        return txt

    def _make_title(self, text, font_size=38, color=COLOR_TITLE):
        """创建带下划线的标题"""
        label = Text(text, font=CJK_FONT, font_size=font_size, color=color)
        underline = Line(
            label.get_left() + DOWN * 0.08,
            label.get_right() + DOWN * 0.08,
            color=color, stroke_width=2
        )
        return VGroup(label, underline)

    def _make_rounded_box(self, mobject, color=COLOR_STEP, buff=0.25, fill_opacity=0.12):
        """为 mobject 创建圆角高亮框"""
        return RoundedRectangle(
            width=mobject.get_width() + buff * 2,
            height=mobject.get_height() + buff * 2,
            corner_radius=0.18,
            color=color,
            fill_color=color,
            fill_opacity=fill_opacity,
            stroke_width=2
        ).move_to(mobject.get_center())

    def _fade_out_all_except(self, *keep):
        """淡出除 keep 之外的所有 mobject"""
        to_fade = [m for m in self.mobjects if m not in keep]
        if to_fade:
            self.play(*[FadeOut(m) for m in to_fade], run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────────────

    def scene1_hook(self):
        # 钩子问题
        hook = Text(
            "你能解出这个方程吗？",
            font=CJK_FONT,
            font_size=32,
            color=COLOR_SUBTITLE
        ).move_to(UP * 5.5)

        # 主方程
        eq = MathTex(
            r"x^3 - 4x = 0",
            font_size=68,
            color=COLOR_EQUATION
        ).move_to(UP * 3.5)

        # 学年标签
        grade_label = Text(
            "八年级 · 第二十一章",
            font=CJK_FONT,
            font_size=22,
            color=GRAY_B
        ).move_to(UP * 2.2)

        # 装饰框
        eq_box = self._make_rounded_box(eq, color=COLOR_EQUATION, buff=0.35, fill_opacity=0.1)

        # 动画
        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.6)
        self.play(Write(eq), run_time=1.2)
        self.play(Create(eq_box), run_time=0.5)
        self.play(FadeIn(grade_label), run_time=0.4)
        self.wait(0.5)

        # 挑战感 - 闪烁问号
        self.play(
            eq.animate.set_color(COLOR_HIGHLIGHT),
            run_time=0.3
        )
        self.play(
            eq.animate.set_color(COLOR_EQUATION),
            run_time=0.3
        )
        self.wait(0.5)

        # 引出解法文字
        solve_text = Text(
            "用因式分解法来解！",
            font=CJK_FONT,
            font_size=30,
            color=COLOR_STEP
        ).move_to(UP * 0.5)

        self.play(FadeIn(solve_text, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook),
            FadeOut(eq),
            FadeOut(eq_box),
            FadeOut(grade_label),
            FadeOut(solve_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 2: 整式方程定义
    # ─────────────────────────────────────────────────────────

    def scene2_definition(self):
        # 标题
        title = self._make_title("整式方程", font_size=40)
        title.move_to(UP * 6.0)

        # 定义说明
        def_line1 = Text(
            "分母中不含未知数的方程",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_SUBTITLE
        ).move_to(UP * 4.8)

        # 包含类型
        types_title = Text(
            "包括:",
            font=CJK_FONT,
            font_size=24,
            color=COLOR_RESULT
        ).move_to(UP * 3.5 + LEFT * 2.8)

        types = VGroup(
            Text("• 一元一次方程", font=CJK_FONT, font_size=24, color=COLOR_SUBTITLE),
            Text("• 一元二次方程", font=CJK_FONT, font_size=24, color=COLOR_SUBTITLE),
            Text("• 一元高次方程", font=CJK_FONT, font_size=24, color=COLOR_HIGHLIGHT),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).move_to(UP * 2.5 + LEFT * 0.5)

        # 示例方程
        ex1 = MathTex(r"2x + 1 = 0", font_size=32, color=COLOR_SUBTITLE).move_to(UP * 0.8 + LEFT * 2.0)
        ex2 = MathTex(r"x^2 - 5x + 6 = 0", font_size=32, color=COLOR_SUBTITLE).move_to(UP * 0.8 + RIGHT * 1.5)
        ex3 = MathTex(r"x^3 - 4x = 0", font_size=36, color=COLOR_HIGHLIGHT).move_to(DOWN * 0.6)

        label1 = Text("一次", font=CJK_FONT, font_size=18, color=GRAY_B).next_to(ex1, DOWN, buff=0.1)
        label2 = Text("二次", font=CJK_FONT, font_size=18, color=GRAY_B).next_to(ex2, DOWN, buff=0.1)
        label3 = Text("← 三次！今天的主角", font=CJK_FONT, font_size=20, color=COLOR_HIGHLIGHT).next_to(ex3, RIGHT, buff=0.2)

        # 动画
        self.play(Write(title[0]), Create(title[1]), run_time=0.7)
        self.play(FadeIn(def_line1, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)

        self.play(FadeIn(types_title), run_time=0.3)
        for t in types:
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(0.3)
        self.play(FadeIn(ex1), FadeIn(label1), run_time=0.4)
        self.play(FadeIn(ex2), FadeIn(label2), run_time=0.4)
        self.play(Write(ex3), FadeIn(label3), run_time=0.6)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(def_line1),
            FadeOut(types_title),
            FadeOut(types),
            FadeOut(ex1), FadeOut(label1),
            FadeOut(ex2), FadeOut(label2),
            FadeOut(ex3), FadeOut(label3),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 3: 核心思想 - 降次
    # ─────────────────────────────────────────────────────────

    def scene3_core_idea(self):
        # 核心概念大字
        core_title = Text(
            "核心思想：",
            font=CJK_FONT,
            font_size=34,
            color=COLOR_RESULT
        ).move_to(UP * 5.5)

        # 降次大字
        reduce_text = Text(
            "降次",
            font=CJK_FONT,
            font_size=72,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.0)

        # 高次 → 低次
        high = Text("高次", font=CJK_FONT, font_size=40, color=COLOR_EQUATION).move_to(UP * 2.0 + LEFT * 2.5)
        arrow = Arrow(
            LEFT * 0.8 + UP * 2.0,
            RIGHT * 0.8 + UP * 2.0,
            color=COLOR_ARROW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.25
        )
        low = Text("低次", font=CJK_FONT, font_size=40, color=COLOR_STEP).move_to(UP * 2.0 + RIGHT * 2.5)

        # 方法框
        method_label = Text(
            "方法：因式分解",
            font=CJK_FONT,
            font_size=30,
            color=COLOR_SUBTITLE
        ).move_to(UP * 0.5)

        method_box = self._make_rounded_box(method_label, color=COLOR_STEP, buff=0.3)

        # 关键公式
        key_formula_txt = Text(
            "将方程化为  A·B·C = 0  的形式",
            font=CJK_FONT,
            font_size=24,
            color=COLOR_RESULT
        ).move_to(DOWN * 0.8)

        # 动画
        self.play(FadeIn(core_title), run_time=0.4)
        self.play(
            FadeIn(reduce_text, scale=0.7),
            run_time=0.6
        )
        self.play(
            Flash(reduce_text, color=COLOR_HIGHLIGHT, flash_radius=1.2, num_lines=12),
            run_time=0.5
        )
        self.wait(0.3)

        self.play(FadeIn(high, shift=RIGHT * 0.3), run_time=0.4)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(low, shift=LEFT * 0.3), run_time=0.4)
        self.wait(0.3)

        self.play(Create(method_box), FadeIn(method_label), run_time=0.6)
        self.play(FadeIn(key_formula_txt), run_time=0.4)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(core_title),
            FadeOut(reduce_text),
            FadeOut(high),
            FadeOut(arrow),
            FadeOut(low),
            FadeOut(method_box),
            FadeOut(method_label),
            FadeOut(key_formula_txt),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 4: 例题解法
    # ─────────────────────────────────────────────────────────

    def scene4_example(self):
        # 例题标题
        example_title = self._make_title("例题", font_size=36, color=COLOR_TITLE)
        example_title.move_to(UP * 6.5)

        # 原方程
        eq_orig = MathTex(
            r"x^3 - 4x = 0",
            font_size=52,
            color=COLOR_EQUATION
        ).move_to(UP * 5.0)

        orig_box = self._make_rounded_box(eq_orig, color=COLOR_EQUATION, buff=0.3, fill_opacity=0.08)

        self.play(Write(example_title[0]), Create(example_title[1]), run_time=0.5)
        self.play(Write(eq_orig), Create(orig_box), run_time=0.8)
        self.wait(0.4)

        # ── 步骤一: 提公因式 ──────────────────────────────────
        step1_label = Text(
            "第一步：提公因式",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_STEP
        ).move_to(UP * 3.5 + LEFT * 0.0)

        step1_indicator = Line(
            step1_label.get_left() + LEFT * 0.15,
            step1_label.get_left() + LEFT * 0.15 + UP * step1_label.get_height(),
            color=COLOR_STEP,
            stroke_width=4
        )

        eq_step1 = MathTex(
            r"x(x^2 - 4) = 0",
            font_size=52,
            color=COLOR_SUBTITLE
        ).move_to(UP * 2.3)

        # 高亮 x 因子
        eq_step1.set_color_by_tex("x", COLOR_FACTOR)

        # 解释箭头
        arrow1 = Arrow(
            eq_orig.get_bottom() + DOWN * 0.05,
            eq_step1.get_top() + UP * 0.05,
            color=COLOR_ARROW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
            buff=0.15
        )

        hint1 = Text(
            "共同因子 x",
            font=CJK_FONT,
            font_size=20,
            color=COLOR_FACTOR
        ).next_to(arrow1, RIGHT, buff=0.2)

        self.play(FadeIn(step1_label, shift=RIGHT * 0.3), run_time=0.5)
        self.play(GrowArrow(arrow1), FadeIn(hint1), run_time=0.5)
        self.play(Write(eq_step1), run_time=0.8)
        self.wait(0.8)

        # ── 步骤二: 平方差公式 ───────────────────────────────
        step2_label = Text(
            "第二步：平方差公式",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_STEP
        ).move_to(UP * 0.8)

        eq_step2 = MathTex(
            r"x(x+2)(x-2) = 0",
            font_size=48,
            color=COLOR_SUBTITLE
        ).move_to(DOWN * 0.5)

        # 注意: set_color_by_tex 对简单字符效果最好
        # 不使用脆弱的索引方式

        step2_formula = MathTex(
            r"a^2 - b^2 = (a+b)(a-b)",
            font_size=26,
            color=GRAY_B
        ).move_to(UP * 0.2)

        step2_formula_box = self._make_rounded_box(step2_formula, color=GRAY_B, buff=0.2, fill_opacity=0.05)

        arrow2 = Arrow(
            eq_step1.get_bottom() + DOWN * 0.05,
            eq_step2.get_top() + UP * 0.05,
            color=COLOR_ARROW,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
            buff=0.12
        )

        self.play(FadeOut(arrow1), FadeOut(hint1), run_time=0.3)
        self.play(FadeIn(step2_label, shift=RIGHT * 0.3), run_time=0.4)
        self.play(
            Create(step2_formula_box),
            FadeIn(step2_formula),
            run_time=0.5
        )
        self.play(GrowArrow(arrow2), run_time=0.4)
        self.play(Write(eq_step2), run_time=0.8)
        self.wait(0.8)

        # ── 步骤三: 零乘积定理 ────────────────────────────────
        self.play(
            FadeOut(step2_formula_box),
            FadeOut(step2_formula),
            FadeOut(step1_label),
            FadeOut(step2_label),
            FadeOut(arrow2),
            run_time=0.4
        )

        step3_label = Text(
            "第三步：令每个因式 = 0",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_STEP
        ).move_to(DOWN * 1.8)

        # 三个方程
        eq_a = MathTex(r"x = 0", font_size=40, color=COLOR_RESULT).move_to(DOWN * 3.0 + LEFT * 2.8)
        eq_b = MathTex(r"x + 2 = 0", font_size=40, color=COLOR_RESULT).move_to(DOWN * 3.0)
        eq_c = MathTex(r"x - 2 = 0", font_size=40, color=COLOR_RESULT).move_to(DOWN * 3.0 + RIGHT * 2.8)

        or_ab = Text("或", font=CJK_FONT, font_size=24, color=GRAY_B).move_to(DOWN * 3.0 + LEFT * 1.4)
        or_bc = Text("或", font=CJK_FONT, font_size=24, color=GRAY_B).move_to(DOWN * 3.0 + RIGHT * 1.4)

        # 解
        sol_a = MathTex(r"x = 0", font_size=38, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.2 + LEFT * 2.8)
        sol_b = MathTex(r"x = -2", font_size=38, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.2)
        sol_c = MathTex(r"x = 2", font_size=38, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.2 + RIGHT * 2.8)

        self.play(FadeIn(step3_label), run_time=0.4)
        self.play(
            FadeIn(eq_a), FadeIn(or_ab), FadeIn(eq_b), FadeIn(or_bc), FadeIn(eq_c),
            run_time=0.7
        )
        self.wait(0.5)

        arrow_a = Arrow(eq_a.get_bottom() + DOWN * 0.05, sol_a.get_top() + UP * 0.05,
                        color=COLOR_ARROW, stroke_width=2.5, max_tip_length_to_length_ratio=0.25, buff=0.1)
        arrow_b = Arrow(eq_b.get_bottom() + DOWN * 0.05, sol_b.get_top() + UP * 0.05,
                        color=COLOR_ARROW, stroke_width=2.5, max_tip_length_to_length_ratio=0.25, buff=0.1)
        arrow_c = Arrow(eq_c.get_bottom() + DOWN * 0.05, sol_c.get_top() + UP * 0.05,
                        color=COLOR_ARROW, stroke_width=2.5, max_tip_length_to_length_ratio=0.25, buff=0.1)

        self.play(
            GrowArrow(arrow_a), GrowArrow(arrow_b), GrowArrow(arrow_c),
            run_time=0.5
        )
        self.play(Write(sol_a), Write(sol_b), Write(sol_c), run_time=0.7)
        self.wait(0.5)

        # 最终答案框 - 竖排防止溢出
        answer_label = Text(
            "答：",
            font=CJK_FONT,
            font_size=24,
            color=COLOR_RESULT
        )
        answer_formula = MathTex(
            r"x_1 = 0,\quad x_2 = -2,\quad x_3 = 2",
            font_size=30,
            color=COLOR_RESULT
        )
        answer_group = VGroup(answer_label, answer_formula).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        answer_group.move_to(DOWN * 5.5)
        answer_box = self._make_rounded_box(answer_group, color=COLOR_RESULT, buff=0.3, fill_opacity=0.1)

        self.play(
            Create(answer_box),
            FadeIn(answer_label),
            Write(answer_formula),
            run_time=0.8
        )
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(example_title),
            FadeOut(eq_orig), FadeOut(orig_box),
            FadeOut(eq_step1),
            FadeOut(eq_step2),
            FadeOut(step3_label),
            FadeOut(eq_a), FadeOut(or_ab), FadeOut(eq_b), FadeOut(or_bc), FadeOut(eq_c),
            FadeOut(arrow_a), FadeOut(arrow_b), FadeOut(arrow_c),
            FadeOut(sol_a), FadeOut(sol_b), FadeOut(sol_c),
            FadeOut(answer_box), FadeOut(answer_label), FadeOut(answer_formula),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────
    # Scene 5: 零乘积定理
    # ─────────────────────────────────────────────────────────

    def scene5_zero_product(self):
        # 标题
        title = self._make_title("零乘积定理", font_size=38, color=COLOR_TITLE)
        title.move_to(UP * 6.0)

        # 核心公式
        formula = MathTex(
            r"A \cdot B \cdot C = 0",
            font_size=64,
            color=COLOR_EQUATION
        ).move_to(UP * 4.2)
        formula_box = self._make_rounded_box(formula, color=COLOR_EQUATION, buff=0.4, fill_opacity=0.08)

        # 推导
        implies = MathTex(r"\Downarrow", font_size=48, color=COLOR_ARROW).move_to(UP * 2.8)

        result_text = Text(
            "至少有一个因式等于零",
            font=CJK_FONT,
            font_size=28,
            color=COLOR_SUBTITLE
        ).move_to(UP * 2.0)

        # 三个条件
        cond_a = MathTex(r"A = 0", font_size=40, color=COLOR_RESULT).move_to(UP * 0.8 + LEFT * 3.0)
        cond_b = MathTex(r"B = 0", font_size=40, color=COLOR_RESULT).move_to(UP * 0.8)
        cond_c = MathTex(r"C = 0", font_size=40, color=COLOR_RESULT).move_to(UP * 0.8 + RIGHT * 3.0)

        or1 = Text("或", font=CJK_FONT, font_size=22, color=GRAY_B).move_to(UP * 0.8 + LEFT * 1.5)
        or2 = Text("或", font=CJK_FONT, font_size=22, color=GRAY_B).move_to(UP * 0.8 + RIGHT * 1.5)

        # 说明
        note = Text(
            "这是解高次方程的关键！",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(Write(title[0]), Create(title[1]), run_time=0.5)
        self.play(Create(formula_box), Write(formula), run_time=0.7)
        self.play(FadeIn(implies, shift=DOWN * 0.2), run_time=0.4)
        self.play(FadeIn(result_text), run_time=0.5)
        self.play(
            FadeIn(cond_a), FadeIn(or1), FadeIn(cond_b), FadeIn(or2), FadeIn(cond_c),
            run_time=0.6
        )
        self.play(FadeIn(note, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(formula), FadeOut(formula_box),
            FadeOut(implies), FadeOut(result_text),
            FadeOut(cond_a), FadeOut(or1), FadeOut(cond_b), FadeOut(or2), FadeOut(cond_c),
            FadeOut(note),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 6: 另一类型 x³ = a
    # ─────────────────────────────────────────────────────────

    def scene6_cube_type(self):
        # 标题
        title = self._make_title("另一类型", font_size=38, color=COLOR_TITLE)
        title.move_to(UP * 6.0)

        # x³ = 8
        eq_cube = MathTex(
            r"x^3 = 8",
            font_size=60,
            color=COLOR_EQUATION
        ).move_to(UP * 4.5)
        eq_cube_box = self._make_rounded_box(eq_cube, color=COLOR_EQUATION, buff=0.3, fill_opacity=0.08)

        self.play(Write(title[0]), Create(title[1]), run_time=0.5)
        self.play(Write(eq_cube), Create(eq_cube_box), run_time=0.7)

        # 解法: 开立方
        method_text = Text(
            "两边开立方",
            font=CJK_FONT,
            font_size=28,
            color=COLOR_STEP
        ).move_to(UP * 3.0)

        arrow_down = MathTex(r"\Downarrow", font_size=44, color=COLOR_ARROW).move_to(UP * 2.3)

        eq_solution = MathTex(
            r"x = \sqrt[3]{8} = 2",
            font_size=56,
            color=COLOR_RESULT
        ).move_to(UP * 1.3)
        sol_box = self._make_rounded_box(eq_solution, color=COLOR_RESULT, buff=0.35, fill_opacity=0.1)

        self.play(FadeIn(method_text), run_time=0.4)
        self.play(FadeIn(arrow_down, shift=DOWN * 0.2), run_time=0.3)
        self.play(Write(eq_solution), Create(sol_box), run_time=0.8)
        self.wait(0.5)

        # 验证
        verify_text = MathTex(
            r"2^3 = 8 \checkmark",
            font_size=32,
            color=COLOR_STEP
        ).move_to(UP * 0.0)

        self.play(FadeIn(verify_text), run_time=0.4)
        self.wait(0.5)

        # 一般公式
        general_title = Text(
            "一般公式：",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_SUBTITLE
        ).move_to(DOWN * 1.2 + LEFT * 1.0)

        general_formula = MathTex(
            r"x^n = a \Rightarrow x = \sqrt[n]{a}",
            font_size=36,
            color=COLOR_EQUATION
        ).move_to(DOWN * 2.2)

        gen_box = self._make_rounded_box(general_formula, color=COLOR_EQUATION, buff=0.3, fill_opacity=0.08)

        self.play(FadeIn(general_title), run_time=0.4)
        self.play(Create(gen_box), Write(general_formula), run_time=0.7)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(eq_cube), FadeOut(eq_cube_box),
            FadeOut(method_text),
            FadeOut(arrow_down),
            FadeOut(eq_solution), FadeOut(sol_box),
            FadeOut(verify_text),
            FadeOut(general_title),
            FadeOut(general_formula), FadeOut(gen_box),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 7: 总结与片尾
    # ─────────────────────────────────────────────────────────

    def scene7_outro(self):
        # 解题三步法标题
        summary_title = Text(
            "解题三步法",
            font=CJK_FONT,
            font_size=38,
            color=COLOR_TITLE
        ).move_to(UP * 5.8)

        underline = Line(
            summary_title.get_left() + DOWN * 0.08,
            summary_title.get_right() + DOWN * 0.08,
            color=COLOR_TITLE,
            stroke_width=2
        )

        # 三步骤
        step_items = [
            ("① 提公因式",   r"x(x^2 - 4) = 0",        COLOR_STEP),
            ("② 因式分解",   r"x(x+2)(x-2) = 0",       COLOR_STEP),
            ("③ 令各因式=0", r"x=0,\; x=-2,\; x=2",    COLOR_RESULT),
        ]

        step_group = VGroup()
        for txt_cn, tex_str, clr in step_items:
            label = Text(txt_cn, font=CJK_FONT, font_size=28, color=clr)
            eq_txt = MathTex(tex_str, font_size=28, color=GRAY_A)
            row = VGroup(label, eq_txt).arrange(RIGHT, buff=0.5)
            step_group.add(row)

        step_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        step_group.move_to(UP * 3.5)

        # 核心口诀
        mantra = Text(
            "高次方程不要慌，因式分解来帮忙！",
            font=CJK_FONT,
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)
        mantra_box = self._make_rounded_box(mantra, color=COLOR_HIGHLIGHT, buff=0.25, fill_opacity=0.08)

        self.play(Write(summary_title), Create(underline), run_time=0.6)

        for row in step_group:
            self.play(FadeIn(row, shift=RIGHT * 0.4), run_time=0.4)

        self.play(Create(mantra_box), FadeIn(mantra), run_time=0.6)
        self.wait(1.0)

        # 清场，保留作者信息并放大
        self.play(
            FadeOut(summary_title), FadeOut(underline),
            FadeOut(step_group),
            FadeOut(mantra), FadeOut(mantra_box),
            run_time=0.5
        )

        # 作者信息放大居中
        self.play(FadeOut(self.author_bar), run_time=0.2)

        author_big = Text(
            "上海初高中数学直通车",
            font=CJK_FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=CJK_FONT,
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=CJK_FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)

        # 装饰小方程组
        deco_eqs = VGroup(
            MathTex(r"x^3 - 4x = 0", font_size=24, color=GRAY_B),
            MathTex(r"x(x+2)(x-2) = 0", font_size=24, color=GRAY_B),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)

        self.play(
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco_eqs), run_time=0.4)
        self.wait(1.5)

        # 最终淡出
        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_eqs),
            run_time=1.0
        )