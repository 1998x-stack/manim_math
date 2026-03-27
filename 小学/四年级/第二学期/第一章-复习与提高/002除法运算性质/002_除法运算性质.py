"""
除法运算性质 - Division Property Animation
使用 Manim 创建的小学数学教学视频

内容: 一个数连续除以两个数等于除以这两个数的积
知识点: a ÷ b ÷ c = a ÷ (b × c)
目标观众: 四年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DivisionPropertyLesson(Scene):
    """
    除法运算性质教学动画

    场景顺序:
    1. 开场钩子
    2. 引入问题：400 ÷ 25 ÷ 4 如何简算？
    3. 发现规律：逐步演示
    4. 归纳公式：a ÷ b ÷ c = a ÷ (b × c)
    5. 验证举例
    6. 练习巩固
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY   = "#4fc3f7"   # 浅蓝 - 主要公式
        self.COLOR_SECONDARY = "#ef5350"   # 红色 - 强调
        self.COLOR_ACCENT    = "#ffd54f"   # 金黄 - 高亮
        self.COLOR_GREEN     = "#66bb6a"   # 绿色 - 正确/结果
        self.COLOR_PURPLE    = "#ce93d8"   # 紫色 - 字母
        self.COLOR_AUX       = "#90a4ae"   # 灰蓝 - 辅助文字
        self.COLOR_ORANGE    = "#ffa726"   # 橙色 - 括号

        self.scene_1_opening()
        self.scene_2_hook_problem()
        self.scene_3_discover_pattern()
        self.scene_4_formula()
        self.scene_5_verification()
        self.scene_6_practice()
        self.scene_7_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        # 主标题
        title = Text(
            "除法运算性质",
            font="Heiti SC",
            font_size=52,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 4.5)

        subtitle = Text(
            "四年级 · 简便计算",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_AUX,
        ).move_to(UP * 3.5)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        # 钩子问题
        hook_bg = RoundedRectangle(
            width=7.5,
            height=2.2,
            corner_radius=0.3,
            fill_color="#0d1b4b",
            fill_opacity=0.85,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
        ).move_to(DOWN * 0.5)

        hook_line1 = Text(
            "你能快速算出",
            font="Heiti SC",
            font_size=30,
            color=WHITE,
        ).move_to(DOWN * 0.1)

        hook_expr = MathTex(
            r"400 \div 25 \div 4 = ?",
            font_size=46,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(hook_bg), run_time=0.3)
        self.play(Write(hook_line1), run_time=0.5)
        self.play(Write(hook_expr), run_time=0.7)
        self.wait(1.2)

        hint = Text(
            "今天学的技巧，让你秒算！",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook_bg),
            FadeOut(hook_line1),
            FadeOut(hook_expr),
            FadeOut(hint),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 2: 引入问题，逐步计算
    # ─────────────────────────────────────────────
    def scene_2_hook_problem(self):
        # 章节标题
        sec_title = Text(
            "先来试试普通算法",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # 原式
        expr0 = MathTex(r"400 \div 25 \div 4", font_size=54, color=WHITE)
        expr0.move_to(UP * 3.8)
        self.play(Write(expr0), run_time=0.7)
        self.wait(0.4)

        # 步骤1: 先算 400 ÷ 25
        step1_label = Text(
            "第一步：先算  400 ÷ 25",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_AUX,
        ).move_to(UP * 2.4)
        self.play(FadeIn(step1_label, shift=UP * 0.2), run_time=0.5)

        step1_calc = MathTex(
            r"400 \div 25 = 16",
            font_size=46,
            color=self.COLOR_GREEN,
        ).move_to(UP * 1.3)
        self.play(Write(step1_calc), run_time=0.7)
        self.wait(0.8)

        # 步骤2: 再算 16 ÷ 4
        step2_label = Text(
            "第二步：再算  16 ÷ 4",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_AUX,
        ).move_to(UP * 0.0)
        self.play(FadeIn(step2_label, shift=UP * 0.2), run_time=0.5)

        step2_calc = MathTex(
            r"16 \div 4 = 4",
            font_size=46,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 1.1)
        self.play(Write(step2_calc), run_time=0.7)
        self.wait(0.5)

        # 结果框
        result_text = Text(
            "答案 = 4",
            font="Heiti SC",
            font_size=36,
            color=self.COLOR_ACCENT,
        )
        result_box = SurroundingRectangle(
            result_text, color=self.COLOR_ACCENT, buff=0.2, corner_radius=0.15
        )
        result_group = VGroup(result_text, result_box).move_to(DOWN * 2.5)
        self.play(FadeIn(result_text), Create(result_box), run_time=0.6)
        self.wait(0.5)

        # 思考提示
        think = Text(
            "但是……400 ÷ 25 不好算！",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_SECONDARY,
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(think, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        think2 = Text(
            "有没有更简单的方法？",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 5.2)
        self.play(Write(think2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title),
            FadeOut(expr0),
            FadeOut(step1_label),
            FadeOut(step1_calc),
            FadeOut(step2_label),
            FadeOut(step2_calc),
            FadeOut(result_group),
            FadeOut(think),
            FadeOut(think2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 3: 发现规律 - 可视化演示
    # ─────────────────────────────────────────────
    def scene_3_discover_pattern(self):
        sec_title = Text(
            "发现简便方法",
            font="Heiti SC",
            font_size=36,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 6.2)
        self.play(Write(sec_title), run_time=0.6)

        # 显示原式
        original = MathTex(
            r"400 \div 25 \div 4",
            font_size=52,
            color=WHITE,
        ).move_to(UP * 4.8)
        self.play(Write(original), run_time=0.6)

        # 用大括号标注 25 × 4
        arrow_down = Text(
            "观察：25 × 4 = 100，整数！",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 3.6)
        self.play(FadeIn(arrow_down, shift=UP * 0.2), run_time=0.5)

        # 25 × 4 = 100 高亮
        mult_show = MathTex(
            r"25 \times 4 = 100",
            font_size=46,
            color=self.COLOR_ORANGE,
        ).move_to(UP * 2.5)
        self.play(Write(mult_show), run_time=0.7)
        box_mult = SurroundingRectangle(
            mult_show, color=self.COLOR_ORANGE, buff=0.15, corner_radius=0.12
        )
        self.play(Create(box_mult), run_time=0.4)
        self.wait(0.8)

        # 转换箭头
        arrow = Arrow(
            UP * 1.6, UP * 0.9,
            color=self.COLOR_ACCENT,
            buff=0.1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.25,
        )
        transform_label = Text(
            "把后两个除数合并为积！",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_ACCENT,
        ).next_to(arrow, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow), FadeIn(transform_label), run_time=0.6)

        # 新方法
        new_method = MathTex(
            r"400 \div (25 \times 4)",
            font_size=52,
            color=self.COLOR_PRIMARY,
        ).move_to(DOWN * 0.2)
        self.play(Write(new_method), run_time=0.7)
        self.wait(0.4)

        # 计算过程
        calc1 = MathTex(
            r"= 400 \div 100",
            font_size=46,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 1.4)
        self.play(Write(calc1), run_time=0.6)

        calc2 = MathTex(
            r"= 4",
            font_size=52,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 2.4)
        self.play(Write(calc2), run_time=0.5)

        # 结果对比
        compare_label = Text(
            "简单多了！只需一步除法",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(compare_label, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 两种算法对比
        self.play(
            FadeOut(arrow_down),
            FadeOut(mult_show),
            FadeOut(box_mult),
            FadeOut(arrow),
            FadeOut(transform_label),
            FadeOut(original),
            FadeOut(new_method),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(compare_label),
            run_time=0.4,
        )

        # 对比框架
        compare_title = Text(
            "两种算法对比",
            font="Heiti SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 4.5)
        self.play(Write(compare_title), run_time=0.5)

        # 左侧：普通算法
        left_title = Text(
            "普通算法",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_AUX,
        ).move_to(np.array([-2.2, 3.3, 0]))

        left_box = Rectangle(
            width=3.8,
            height=3.4,
            color=self.COLOR_AUX,
            stroke_width=1.5,
            fill_opacity=0.05,
        ).move_to(np.array([-2.2, 1.5, 0]))

        left_step1 = MathTex(r"400 \div 25", font_size=30, color=WHITE).move_to(np.array([-2.2, 2.6, 0]))
        left_eq1 = MathTex(r"= 16", font_size=30, color=self.COLOR_GREEN).move_to(np.array([-2.2, 1.9, 0]))
        left_step2 = MathTex(r"16 \div 4", font_size=30, color=WHITE).move_to(np.array([-2.2, 1.2, 0]))
        left_eq2 = MathTex(r"= 4", font_size=30, color=self.COLOR_GREEN).move_to(np.array([-2.2, 0.5, 0]))

        left_pain = Text(
            "难算！",
            font="Heiti SC",
            font_size=22,
            color=self.COLOR_SECONDARY,
        ).move_to(np.array([-2.2, -0.3, 0]))

        # 右侧：简便算法
        right_title = Text(
            "简便算法",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_PRIMARY,
        ).move_to(np.array([2.2, 3.3, 0]))

        right_box = Rectangle(
            width=3.8,
            height=3.4,
            color=self.COLOR_PRIMARY,
            stroke_width=2,
            fill_opacity=0.08,
        ).move_to(np.array([2.2, 1.5, 0]))

        right_step1 = MathTex(r"400 \div (25 \times 4)", font_size=28, color=WHITE).move_to(np.array([2.2, 2.6, 0]))
        right_eq1 = MathTex(r"= 400 \div 100", font_size=30, color=self.COLOR_GREEN).move_to(np.array([2.2, 1.8, 0]))
        right_eq2 = MathTex(r"= 4", font_size=36, color=self.COLOR_ACCENT).move_to(np.array([2.2, 0.9, 0]))

        right_good = Text(
            "轻松！",
            font="Heiti SC",
            font_size=22,
            color=self.COLOR_GREEN,
        ).move_to(np.array([2.2, 0.1, 0]))

        self.play(
            FadeIn(left_box), FadeIn(right_box),
            Write(left_title), Write(right_title),
            run_time=0.5,
        )
        self.play(
            Write(left_step1), Write(right_step1),
            run_time=0.6,
        )
        self.play(
            Write(left_eq1), Write(right_eq1),
            run_time=0.6,
        )
        self.play(
            Write(left_step2), Write(right_eq2),
            run_time=0.6,
        )
        self.play(
            Write(left_eq2),
            run_time=0.5,
        )
        self.play(
            FadeIn(left_pain), FadeIn(right_good),
            run_time=0.4,
        )

        self.wait(1.8)

        self.play(
            FadeOut(sec_title),
            FadeOut(compare_title),
            FadeOut(left_box), FadeOut(right_box),
            FadeOut(left_title), FadeOut(right_title),
            FadeOut(left_step1), FadeOut(left_eq1),
            FadeOut(left_step2), FadeOut(left_eq2),
            FadeOut(left_pain),
            FadeOut(right_step1), FadeOut(right_eq1),
            FadeOut(right_eq2), FadeOut(right_good),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 4: 归纳公式
    # ─────────────────────────────────────────────
    def scene_4_formula(self):
        sec_title = Text(
            "除法运算性质",
            font="Heiti SC",
            font_size=44,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.7)

        # 公式背景板
        formula_bg = RoundedRectangle(
            width=8.0,
            height=2.4,
            corner_radius=0.4,
            fill_color="#0d2060",
            fill_opacity=0.9,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=3,
        ).move_to(UP * 4.5)

        # 公式文字拼合（中文+数学分离）
        formula_tex = MathTex(
            r"a \div b \div c = a \div (b \times c)",
            font_size=48,
            color=WHITE,
        ).move_to(UP * 4.7)

        condition_text = Text(
            "（b、c 均不为 0）",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_AUX,
        ).move_to(UP * 4.0)

        self.play(FadeIn(formula_bg), run_time=0.4)
        self.play(Write(formula_tex), run_time=1.0)
        self.play(FadeIn(condition_text), run_time=0.4)
        self.wait(0.8)

        # 语言描述
        desc_title = Text(
            "用语言描述：",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 2.6)
        self.play(Write(desc_title), run_time=0.5)

        desc_line1 = Text(
            "一个数连续除以两个数，",
            font="Heiti SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 1.8)

        desc_line2 = Text(
            "等于这个数除以这两个数的积。",
            font="Heiti SC",
            font_size=28,
            color=WHITE,
        ).move_to(UP * 1.1)

        self.play(Write(desc_line1), run_time=0.6)
        self.play(Write(desc_line2), run_time=0.6)
        self.wait(1.0)

        # 关键词高亮
        key1 = Text("连续除以两个数", font="Heiti SC", font_size=26, color=self.COLOR_SECONDARY)
        key_arrow = Text("=", font="Heiti SC", font_size=26, color=WHITE)
        key2 = Text("除以两个数的积", font="Heiti SC", font_size=26, color=self.COLOR_GREEN)
        key_group = VGroup(key1, key_arrow, key2).arrange(RIGHT, buff=0.25).move_to(DOWN * 0.2)
        self.play(FadeIn(key_group, shift=UP * 0.2), run_time=0.6)

        # 对应标注
        # 标注 a ÷ b ÷ c 中的 ÷ b ÷ c 对应连续除以
        brace_left = Brace(
            formula_tex[0][2:9],  # 近似取 b ÷ c 范围
            direction=DOWN,
            color=self.COLOR_SECONDARY,
        )
        brace_right = Brace(
            formula_tex[0][11:],  # 近似取 (b × c) 范围
            direction=DOWN,
            color=self.COLOR_GREEN,
        )

        self.play(
            GrowFromCenter(brace_left),
            GrowFromCenter(brace_right),
            run_time=0.6,
        )
        self.wait(2.0)

        self.play(
            FadeOut(sec_title),
            FadeOut(formula_bg),
            FadeOut(formula_tex),
            FadeOut(condition_text),
            FadeOut(desc_title),
            FadeOut(desc_line1),
            FadeOut(desc_line2),
            FadeOut(key_group),
            FadeOut(brace_left),
            FadeOut(brace_right),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 5: 举例验证
    # ─────────────────────────────────────────────
    def scene_5_verification(self):
        sec_title = Text(
            "举例验证",
            font="Heiti SC",
            font_size=38,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.5)

        # 公式常驻（小版本）
        formula_small = MathTex(
            r"a \div b \div c = a \div (b \times c)",
            font_size=32,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 5.5)
        self.play(Write(formula_small), run_time=0.6)

        # 分隔线
        sep_line = Line(
            np.array([-4.0, 4.8, 0]),
            np.array([4.0, 4.8, 0]),
            color=self.COLOR_AUX,
            stroke_width=1,
        )
        self.play(Create(sep_line), run_time=0.3)

        # 例1: 400 ÷ 25 ÷ 4
        ex1_label = Text(
            "例1：",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([-3.0, 3.8, 0]))

        ex1_expr = MathTex(
            r"400 \div 25 \div 4",
            font_size=38,
            color=WHITE,
        ).next_to(ex1_label, RIGHT, buff=0.3)

        self.play(Write(ex1_label), Write(ex1_expr), run_time=0.6)

        ex1_step1 = MathTex(
            r"= 400 \div (25 \times 4)",
            font_size=36,
            color=self.COLOR_PRIMARY,
        ).move_to(np.array([0.5, 2.9, 0]))
        self.play(Write(ex1_step1), run_time=0.6)

        ex1_step2 = MathTex(
            r"= 400 \div 100 = 4",
            font_size=36,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0.5, 2.1, 0]))
        self.play(Write(ex1_step2), run_time=0.6)
        self.wait(0.6)

        # 验证标记
        check1 = Text(
            "✓ 和之前结果相同！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0, 1.3, 0]))
        self.play(FadeIn(check1, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # 分割线2
        sep2 = Line(
            np.array([-4.0, 0.8, 0]),
            np.array([4.0, 0.8, 0]),
            color=self.COLOR_AUX,
            stroke_width=1,
            stroke_opacity=0.5,
        )
        self.play(Create(sep2), run_time=0.2)

        # 例2: 600 ÷ 12 ÷ 5
        ex2_label = Text(
            "例2：",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([-3.0, 0.0, 0]))

        ex2_expr = MathTex(
            r"600 \div 12 \div 5",
            font_size=38,
            color=WHITE,
        ).next_to(ex2_label, RIGHT, buff=0.3)

        self.play(Write(ex2_label), Write(ex2_expr), run_time=0.5)

        ex2_step1 = MathTex(
            r"= 600 \div (12 \times 5)",
            font_size=36,
            color=self.COLOR_PRIMARY,
        ).move_to(np.array([0.5, -0.9, 0]))
        self.play(Write(ex2_step1), run_time=0.6)

        ex2_step2 = MathTex(
            r"= 600 \div 60 = 10",
            font_size=36,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0.5, -1.7, 0]))
        self.play(Write(ex2_step2), run_time=0.6)
        self.wait(0.5)

        check2 = Text(
            "✓ 12 × 5 = 60，更易计算！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0, -2.5, 0]))
        self.play(FadeIn(check2, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title),
            FadeOut(formula_small),
            FadeOut(sep_line),
            FadeOut(ex1_label), FadeOut(ex1_expr),
            FadeOut(ex1_step1), FadeOut(ex1_step2),
            FadeOut(check1),
            FadeOut(sep2),
            FadeOut(ex2_label), FadeOut(ex2_expr),
            FadeOut(ex2_step1), FadeOut(ex2_step2),
            FadeOut(check2),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 6: 练习巩固 + 总结
    # ─────────────────────────────────────────────
    def scene_6_practice(self):
        sec_title = Text(
            "记住这个性质",
            font="Heiti SC",
            font_size=40,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.5)

        # 核心公式大展示
        formula_bg = RoundedRectangle(
            width=8.2,
            height=2.6,
            corner_radius=0.5,
            fill_color="#061240",
            fill_opacity=0.95,
            stroke_color=self.COLOR_ACCENT,
            stroke_width=3,
        ).move_to(UP * 4.6)

        formula_main = MathTex(
            r"a \div b \div c = a \div (b \times c)",
            font_size=50,
            color=WHITE,
        ).move_to(UP * 4.8)
        formula_main.set_color_by_tex("b", self.COLOR_ORANGE)
        formula_main.set_color_by_tex("c", self.COLOR_ORANGE)

        cond = Text(
            "b ≠ 0，c ≠ 0",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_AUX,
        ).move_to(UP * 4.1)

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula_main), run_time=1.0)
        self.play(FadeIn(cond), run_time=0.4)

        # 3个关键点
        points = [
            ("①", "后两个除数相乘合并", self.COLOR_PRIMARY),
            ("②", "积通常是整十、整百", self.COLOR_GREEN),
            ("③", "使除法变得简单", self.COLOR_ACCENT),
        ]

        point_group = VGroup()
        for num, text, color in points:
            num_text = Text(num, font="Heiti SC", font_size=28, color=color)
            content_text = Text(text, font="Heiti SC", font_size=26, color=WHITE)
            row = VGroup(num_text, content_text).arrange(RIGHT, buff=0.3)
            point_group.add(row)

        point_group.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        point_group.move_to(UP * 1.8)

        for row in point_group:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.6)

        # 使用技巧
        tip_bg = RoundedRectangle(
            width=7.8,
            height=2.8,
            corner_radius=0.35,
            fill_color="#1a3300",
            fill_opacity=0.85,
            stroke_color=self.COLOR_GREEN,
            stroke_width=2,
        ).move_to(DOWN * 1.2)

        tip_title = Text(
            "使用技巧",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0, -0.3, 0]))

        tip_body1 = Text(
            "观察后两个除数能否凑成",
            font="Heiti SC",
            font_size=24,
            color=WHITE,
        ).move_to(np.array([0, -1.0, 0]))

        tip_body2 = Text(
            "整十、整百等好计算的数",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([0, -1.65, 0]))

        self.play(FadeIn(tip_bg), run_time=0.3)
        self.play(Write(tip_title), run_time=0.4)
        self.play(Write(tip_body1), run_time=0.5)
        self.play(Write(tip_body2), run_time=0.5)
        self.wait(1.2)

        # 练一练
        practice_title = Text(
            "练一练",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 3.0)

        practice_q = MathTex(
            r"3600 \div 36 \div 25 = ?",
            font_size=40,
            color=WHITE,
        ).move_to(DOWN * 4.0)

        hint_text = Text(
            "提示：36 × 25 = 900",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_AUX,
        ).move_to(DOWN * 5.0)

        self.play(Write(practice_title), run_time=0.4)
        self.play(Write(practice_q), run_time=0.7)
        self.play(FadeIn(hint_text, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)

        # 答案揭晓
        answer = MathTex(
            r"= 3600 \div 900 = 4",
            font_size=40,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 6.0)
        self.play(Write(answer), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title),
            FadeOut(formula_bg),
            FadeOut(formula_main),
            FadeOut(cond),
            FadeOut(point_group),
            FadeOut(tip_bg),
            FadeOut(tip_title),
            FadeOut(tip_body1),
            FadeOut(tip_body2),
            FadeOut(practice_title),
            FadeOut(practice_q),
            FadeOut(hint_text),
            FadeOut(answer),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 7: 片尾关注
    # ─────────────────────────────────────────────
    def scene_7_outro(self):
        # 总结框
        summary_bg = RoundedRectangle(
            width=8.0,
            height=3.8,
            corner_radius=0.5,
            fill_color="#0d1b4b",
            fill_opacity=0.9,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
        ).move_to(UP * 2.8)

        summary_title = Text(
            "今天学了什么？",
            font="Heiti SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 4.2)

        formula_recap = MathTex(
            r"a \div b \div c = a \div (b \times c)",
            font_size=42,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 3.2)

        summary_line = Text(
            "连续除以两个数 = 除以两数之积",
            font="Heiti SC",
            font_size=25,
            color=WHITE,
        ).move_to(UP * 2.3)

        example_recap = MathTex(
            r"400 \div 25 \div 4 = 400 \div 100 = 4",
            font_size=32,
            color=self.COLOR_GREEN,
        ).move_to(UP * 1.5)

        self.play(FadeIn(summary_bg), run_time=0.4)
        self.play(Write(summary_title), run_time=0.5)
        self.play(Write(formula_recap), run_time=0.7)
        self.play(Write(summary_line), run_time=0.5)
        self.play(Write(example_recap), run_time=0.7)
        self.wait(1.0)

        # 作者大名片
        author_name = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_AUX,
        ).move_to(DOWN * 2.3)

        self.play(
            Transform(self.author, author_name),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        # 关注呼吁
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 3.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.5)

        # 装饰元素 - 小星星闪烁
        stars = VGroup()
        star_positions = [
            np.array([-3.5, -5.2, 0]),
            np.array([3.5, -5.2, 0]),
            np.array([-2.0, -5.8, 0]),
            np.array([2.0, -5.8, 0]),
            np.array([0.0, -5.5, 0]),
        ]
        for pos in star_positions:
            star = Star(
                n=5,
                outer_radius=0.25,
                inner_radius=0.12,
                color=self.COLOR_ACCENT,
                fill_opacity=0.9,
                stroke_width=0,
            ).move_to(pos)
            stars.add(star)

        self.play(
            *[FadeIn(s, scale=0.3) for s in stars],
            run_time=0.6,
        )
        self.play(
            *[s.animate.scale(1.3) for s in stars],
            rate_func=there_and_back,
            run_time=0.8,
        )

        # 数学公式装饰
        deco_formula = MathTex(
            r"a \div b \div c = a \div (b \times c)",
            font_size=24,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.5,
        ).move_to(DOWN * 6.8)
        self.play(FadeIn(deco_formula), run_time=0.3)

        self.wait(2.0)

        self.play(
            FadeOut(summary_bg),
            FadeOut(summary_title),
            FadeOut(formula_recap),
            FadeOut(summary_line),
            FadeOut(example_recap),
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(stars),
            FadeOut(deco_formula),
            run_time=1.0,
        )
        self.wait(0.3)
