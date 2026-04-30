"""
因式分解——公式法 教学动画
Factorization - Formula Method Educational Animation

使用 Manim 创建的七年级数学教学视频
内容: 平方差公式和完全平方公式的因式分解
目标观众: 七年级学生
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


class FactorizationFormulas(Scene):
    """
    因式分解公式法教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 平方差公式讲解
    3. 平方差公式例题
    4. 完全平方公式讲解
    5. 完全平方公式例题
    6. 综合例题
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调项
        self.COLOR_HIGHLIGHT = YELLOW          # 黄色 - 高亮
        self.COLOR_SUCCESS = "#2ecc71"         # 绿色 - 成功/正确
        self.COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助说明
        self.COLOR_FORMULA_BG = "#2c3e50"      # 深蓝灰 - 公式背景
        
        # 字体大小
        self.FONT_SIZE_TITLE = 38
        self.FONT_SIZE_FORMULA = 32
        self.FONT_SIZE_BODY = 24
        self.FONT_SIZE_SMALL = 20
        self.FONT_SIZE_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_difference_of_squares_theory()
        self.show_difference_of_squares_example()
        self.show_perfect_square_theory()
        self.show_perfect_square_example()
        self.show_challenge_example()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5s)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_SIZE_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何快速分解",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 5.5)
        
        hook_expr = MathTex(
            r"x^2 - 100",
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).next_to(hook_question, DOWN, buff=0.4)
        
        question_mark = Text(
            "?",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).next_to(hook_expr, RIGHT, buff=0.3)
        
        self.play(Write(hook_question), run_time=0.8)
        self.play(Write(hook_expr), run_time=0.7)
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.3)
        self.play(Flash(question_mark, color=YELLOW, flash_radius=0.5), run_time=0.4)
        
        # 三个公式卡片预告
        card_1_cn = Text("平方差公式", font="PingFang SC", font_size=24, color=WHITE)
        card_1_formula = MathTex(r"a^2-b^2", font_size=28, color=self.COLOR_PRIMARY)
        card_1 = VGroup(card_1_cn, card_1_formula).arrange(DOWN, buff=0.15)
        card_1.move_to(UP * 1.5 + LEFT * 10)
        
        card_2_cn = Text("完全平方(+)", font="PingFang SC", font_size=24, color=WHITE)
        card_2_formula = MathTex(r"a^2+2ab+b^2", font_size=24, color=self.COLOR_PRIMARY)
        card_2 = VGroup(card_2_cn, card_2_formula).arrange(DOWN, buff=0.15)
        card_2.move_to(ORIGIN + LEFT * 10)
        
        card_3_cn = Text("完全平方(-)", font="PingFang SC", font_size=24, color=WHITE)
        card_3_formula = MathTex(r"a^2-2ab+b^2", font_size=24, color=self.COLOR_PRIMARY)
        card_3 = VGroup(card_3_cn, card_3_formula).arrange(DOWN, buff=0.15)
        card_3.move_to(DOWN * 1.5 + LEFT * 10)
        
        self.add(card_1, card_2, card_3)
        
        # 卡片依次滑入
        self.play(
            card_1.animate.shift(RIGHT * 10),
            run_time=0.6
        )
        self.play(
            card_2.animate.shift(RIGHT * 10),
            run_time=0.6
        )
        self.play(
            card_3.animate.shift(RIGHT * 10),
            run_time=0.6
        )
        
        # 提示文字
        hint_text = Text(
            "掌握这三个公式就够了!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hook_expr),
            FadeOut(question_mark),
            FadeOut(hint_text),
            card_1.animate.scale(0.6).move_to(UP * 6.5 + LEFT * 2),
            card_2.animate.scale(0.6).move_to(UP * 6.5),
            card_3.animate.scale(0.6).move_to(UP * 6.5 + RIGHT * 2),
            run_time=0.8
        )
        
        # 保存卡片引用
        self.formula_cards = VGroup(card_1, card_2, card_3)
    
    def show_difference_of_squares_theory(self):
        """场景2: 平方差公式讲解 (5-18s)"""
        # 标题
        title = Text(
            "平方差公式",
            font="PingFang SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式: a² - b² = (a+b)(a-b)
        formula_left = MathTex(
            r"a^2 - b^2",
            font_size=self.FONT_SIZE_FORMULA,
            color=WHITE
        )
        
        equal_sign = MathTex(r"=", font_size=self.FONT_SIZE_FORMULA)
        
        formula_right = MathTex(
            r"(a+b)(a-b)",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        )
        
        formula_group = VGroup(formula_left, equal_sign, formula_right).arrange(RIGHT, buff=0.3)
        formula_group.move_to(UP * 3.5)
        
        # 分步展示公式
        self.play(Write(formula_left), run_time=1.0)
        
        # 高亮 a² 和 b²
        a_squared = formula_left[0][0:2]  # a^2
        b_squared = formula_left[0][4:6]  # b^2
        
        self.play(
            Indicate(a_squared, color=self.COLOR_SECONDARY, scale_factor=1.3),
            run_time=0.7
        )
        self.play(
            Indicate(b_squared, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=0.7
        )
        
        self.play(FadeIn(equal_sign), run_time=0.3)
        self.play(Write(formula_right), run_time=1.2)
        
        # 几何可视化 - 两个正方形
        square_scale = 0.8
        square_large = Square(side_length=2 * square_scale, color=self.COLOR_SECONDARY, fill_opacity=0.3)
        square_large.move_to(UP * 0.5 + LEFT * 1.5)
        
        square_small = Square(side_length=1.2 * square_scale, color=self.COLOR_HIGHLIGHT, fill_opacity=0.5)
        square_small.move_to(square_large.get_center())
        
        label_a = MathTex("a", font_size=24, color=self.COLOR_SECONDARY).next_to(square_large, UP, buff=0.1)
        label_b = MathTex("b", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(square_small, UP, buff=0.1)
        
        self.play(
            Create(square_large),
            FadeIn(label_a),
            run_time=1.0
        )
        self.play(
            Create(square_small),
            FadeIn(label_b),
            run_time=1.0
        )
        
        # 面积差说明
        area_text = Text(
            "面积差",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(square_large, RIGHT, buff=0.5)
        
        area_formula = MathTex(
            r"a^2 - b^2",
            font_size=26,
            color=WHITE
        ).next_to(area_text, DOWN, buff=0.2)
        
        self.play(FadeIn(area_text), FadeIn(area_formula), run_time=0.8)
        
        self.wait(0.8)
        
        # 清除几何图形
        self.play(
            FadeOut(square_large),
            FadeOut(square_small),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(area_text),
            FadeOut(area_formula),
            run_time=0.6
        )
        
        # 识别要点
        points_title = Text(
            "识别要点:",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        point_1 = Text(
            "① 两项相减",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        point_2 = Text(
            "② 都是平方项",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(DOWN * 1.2)
        
        # point_3 = MathTex(
        #     r"\text{③ 结构: } \square^2 - \triangle^2",
        #     font_size=self.FONT_SIZE_SMALL,
        #     color=WHITE
        # ).move_to(DOWN * 1.9)
        
        # 修正：使用Text代替MathTex中的中文
        point_3_cn = Text("③ 结构:", font="PingFang SC", font_size=self.FONT_SIZE_SMALL, color=WHITE)
        point_3_formula = MathTex(r"\square^2 - \triangle^2", font_size=self.FONT_SIZE_SMALL, color=WHITE)
        point_3 = VGroup(point_3_cn, point_3_formula).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.9)
        
        self.play(FadeIn(points_title), run_time=0.4)
        self.play(FadeIn(point_1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(point_2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(point_3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 公式整体强调
        formula_box = SurroundingRectangle(
            formula_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(formula_box), run_time=0.8)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(points_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            FadeOut(formula_box),
            formula_group.animate.scale(0.7).move_to(UP * 5.8),
            FadeOut(title),
            run_time=0.8
        )
        
        # 保存公式引用
        self.diff_squares_formula = formula_group
    
    def show_difference_of_squares_example(self):
        """场景3: 平方差公式例题 (18-30s)"""
        # 例题标题
        example_title = Text(
            "例题1",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(FadeIn(example_title, scale=1.2), run_time=0.5)
        
        # 原式
        original_text = Text("因式分解:", font="PingFang SC", font_size=self.FONT_SIZE_BODY, color=WHITE)
        original_expr = MathTex(r"x^2 - 9", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 分析步骤1: 识别平方项
        step_1 = Text(
            "识别平方项:",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2)
        
        identify_x = MathTex(r"x^2 = x^2", font_size=26, color=self.COLOR_SECONDARY)
        identify_9 = MathTex(r"9 = 3^2", font_size=26, color=self.COLOR_HIGHLIGHT)
        identify_group = VGroup(identify_x, identify_9).arrange(RIGHT, buff=0.8).next_to(step_1, DOWN, buff=0.3)
        
        self.play(FadeIn(step_1), run_time=0.5)
        self.wait(0.3)
        
        # 高亮 x²
        self.play(
            original_expr[0][0:2].animate.set_color(self.COLOR_SECONDARY),
            run_time=0.5
        )
        self.play(Write(identify_x), run_time=0.6)
        
        # 高亮 9 并变换为 3²
        self.play(
            original_expr[0][3].animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        nine_to_square = MathTex(r"3^2", font_size=36, color=self.COLOR_HIGHLIGHT)
        nine_to_square.move_to(original_expr[0][3].get_center())
        
        self.play(
            Transform(original_expr[0][3], nine_to_square),
            run_time=0.8
        )
        self.play(Write(identify_9), run_time=0.6)
        
        # 分析步骤2: 应用公式
        step_2 = Text(
            "应用公式:",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(ORIGIN)
        
        formula_ref_cn = Text("根据", font="PingFang SC", font_size=20, color=GRAY)
        formula_ref = MathTex(r"a^2-b^2=(a+b)(a-b)", font_size=22, color=self.COLOR_PRIMARY)
        formula_ref_group = VGroup(formula_ref_cn, formula_ref).arrange(RIGHT, buff=0.1).next_to(step_2, DOWN, buff=0.3)
        
        self.play(FadeIn(step_2), run_time=0.5)
        self.play(FadeIn(formula_ref_group), run_time=0.6)
        
        # 对应关系箭头
        correspond_a = MathTex(r"a = x", font_size=20, color=self.COLOR_SECONDARY).move_to(DOWN * 1.5 + LEFT * 1.5)
        correspond_b = MathTex(r"b = 3", font_size=20, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 1.5 + RIGHT * 1.5)
        
        arrow_1 = Arrow(
            correspond_a.get_right(),
            correspond_a.get_right() + RIGHT * 0.5,
            color=self.COLOR_SECONDARY,
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3
        )
        arrow_2 = Arrow(
            correspond_b.get_left(),
            correspond_b.get_left() + LEFT * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play(
            FadeIn(correspond_a),
            FadeIn(correspond_b),
            Create(arrow_1),
            Create(arrow_2),
            run_time=1.0
        )
        
        self.wait(0.8)
        
        # 结果出现
        result_expr = MathTex(
            r"(x+3)(x-3)",
            font_size=40,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3)
        
        result_box = SurroundingRectangle(
            result_expr,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(result_expr), run_time=1.0)
        self.play(Create(result_box), run_time=0.5)
        
        # 对号确认
        checkmark = Text(
            "✓",
            font_size=60,
            color=self.COLOR_SUCCESS
        ).next_to(result_box, RIGHT, buff=0.3)
        
        self.play(FadeIn(checkmark, scale=2), run_time=0.5)
        self.wait(0.8)
        
        # 验证 (快速展示)
        verify_text = Text(
            "验证:",
            font="PingFang SC",
            font_size=20,
            color=GRAY
        ).move_to(DOWN * 4.5 + LEFT * 3)
        
        verify_expr = MathTex(
            r"(x+3)(x-3) = x^2 - 9",
            font_size=22,
            color=GRAY
        ).next_to(verify_text, RIGHT, buff=0.2)
        
        verify_group = VGroup(verify_text, verify_expr)
        
        self.play(FadeIn(verify_group), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(original_group),
            FadeOut(step_1),
            FadeOut(identify_group),
            FadeOut(step_2),
            FadeOut(formula_ref_group),
            FadeOut(correspond_a),
            FadeOut(correspond_b),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(result_box),
            FadeOut(checkmark),
            FadeOut(verify_group),
            result_expr.animate.scale(0.6).move_to(UP * 5.8 + RIGHT * 3),
            run_time=0.8
        )
        
        self.example_1_result = result_expr
    
    def show_perfect_square_theory(self):
        """场景4: 完全平方公式讲解 (30-45s)"""
        # 标题
        title = Text(
            "完全平方公式",
            font="PingFang SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式1: a² + 2ab + b² = (a+b)²
        formula_1_left = MathTex(
            r"a^2 + 2ab + b^2",
            font_size=30,
            color=WHITE
        )
        equal_1 = MathTex(r"=", font_size=30)
        formula_1_right = MathTex(
            r"(a+b)^2",
            font_size=30,
            color=self.COLOR_SUCCESS
        )
        formula_1 = VGroup(formula_1_left, equal_1, formula_1_right).arrange(RIGHT, buff=0.25)
        formula_1.move_to(UP * 3.5)
        
        # 公式2: a² - 2ab + b² = (a-b)²
        formula_2_left = MathTex(
            r"a^2 - 2ab + b^2",
            font_size=30,
            color=WHITE
        )
        equal_2 = MathTex(r"=", font_size=30)
        formula_2_right = MathTex(
            r"(a-b)^2",
            font_size=30,
            color=self.COLOR_SUCCESS
        )
        formula_2 = VGroup(formula_2_left, equal_2, formula_2_right).arrange(RIGHT, buff=0.25)
        formula_2.move_to(UP * 2.3)
        
        # 展示公式1
        self.play(Write(formula_1_left), run_time=1.2)
        
        # 高亮三项 (彩虹渐变效果)
        term_a2 = formula_1_left[0][0:2]   # a²
        term_2ab = formula_1_left[0][3:6]  # 2ab
        term_b2 = formula_1_left[0][7:9]   # b²
        
        self.play(
            term_a2.animate.set_color(self.COLOR_SECONDARY),
            term_2ab.animate.set_color(self.COLOR_HIGHLIGHT),
            term_b2.animate.set_color(BLUE),
            run_time=1.0
        )
        
        self.play(FadeIn(equal_1), run_time=0.3)
        self.play(Write(formula_1_right), run_time=0.8)
        
        self.wait(0.5)
        
        # 展示公式2
        self.play(Write(formula_2_left), run_time=1.2)
        self.play(FadeIn(equal_2), run_time=0.3)
        self.play(Write(formula_2_right), run_time=0.8)
        
        # 双箭头对比
        comparison_arrow = DoubleArrow(
            formula_1.get_left() + LEFT * 0.3,
            formula_2.get_left() + LEFT * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=3,
            tip_length=0.2
        )
        
        diff_label = Text(
            "注意符号!",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_HIGHLIGHT
        ).next_to(comparison_arrow, LEFT, buff=0.2)
        
        self.play(Create(comparison_arrow), FadeIn(diff_label), run_time=0.8)
        self.wait(0.5)
        
        # 识别要点
        points_title = Text(
            "识别关键:",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.8)
        
        point_1 = Text(
            "① 三项式",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(UP * 0.1)
        
        point_2 = Text(
            "② 首末是平方项",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(DOWN * 0.6)
        
        point_3_cn = Text(
            "③ 中间项",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        )
        point_3_formula = MathTex(
            r"= \pm 2ab",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        )
        point_3 = VGroup(point_3_cn, point_3_formula).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.3)
        
        point_4_cn = Text(
            "④ + 号",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        )
        point_4_arrow = MathTex(r"\rightarrow", font_size=self.FONT_SIZE_SMALL)
        point_4_result = MathTex(r"(a+b)^2", font_size=self.FONT_SIZE_SMALL, color=self.COLOR_SUCCESS)
        point_4 = VGroup(point_4_cn, point_4_arrow, point_4_result).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.1)
        
        point_5_cn = Text(
            "   - 号",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        )
        point_5_arrow = MathTex(r"\rightarrow", font_size=self.FONT_SIZE_SMALL)
        point_5_result = MathTex(r"(a-b)^2", font_size=self.FONT_SIZE_SMALL, color=self.COLOR_SUCCESS)
        point_5 = VGroup(point_5_cn, point_5_arrow, point_5_result).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.8)
        
        self.play(FadeIn(points_title), run_time=0.4)
        self.play(FadeIn(point_1, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(point_2, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(point_3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(point_4, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(point_5, shift=UP * 0.2), run_time=0.5)
        
        # 强调符号的重要性
        self.play(
            Indicate(formula_1_left[0][2], color=self.COLOR_SUCCESS, scale_factor=1.5),  # + 号
            Indicate(formula_2_left[0][2], color=self.COLOR_SECONDARY, scale_factor=1.5),  # - 号
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(comparison_arrow),
            FadeOut(diff_label),
            FadeOut(points_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            FadeOut(point_4),
            FadeOut(point_5),
            formula_1.animate.scale(0.6).move_to(UP * 5.8 + LEFT * 2.5),
            formula_2.animate.scale(0.6).move_to(UP * 5.8 + RIGHT * 2.5),
            run_time=0.8
        )
        
        # 保存公式引用
        self.perfect_square_formulas = VGroup(formula_1, formula_2)
    
    def show_perfect_square_example(self):
        """场景5: 完全平方公式例题 (45-60s)"""
        # 例题标题
        example_title = Text(
            "例题2",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(FadeIn(example_title, scale=1.2), run_time=0.5)
        
        # 原式
        original_text = Text("因式分解:", font="PingFang SC", font_size=self.FONT_SIZE_BODY, color=WHITE)
        original_expr = MathTex(r"x^2 + 6x + 9", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 步骤1: 检查首项
        step_1 = Text(
            "① 检查首项:",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.2)
        
        check_1 = MathTex(r"x^2 = x^2 \quad \checkmark", font_size=24, color=self.COLOR_SECONDARY)
        check_1.next_to(step_1, DOWN, buff=0.2)
        
        self.play(FadeIn(step_1), run_time=0.4)
        
        # 高亮首项
        x_squared_circle = Circle(
            radius=0.3,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(original_expr[0][0:2].get_center())
        
        self.play(Create(x_squared_circle), run_time=0.5)
        self.play(FadeOut(x_squared_circle), FadeIn(check_1), run_time=0.6)
        
        # 步骤2: 检查末项
        step_2 = Text(
            "② 检查末项:",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.9)
        
        check_2 = MathTex(r"9 = 3^2 \quad \checkmark", font_size=24, color=BLUE)
        check_2.next_to(step_2, DOWN, buff=0.2)
        
        self.play(FadeIn(step_2), run_time=0.4)
        
        # 高亮末项
        nine_circle = Circle(
            radius=0.3,
            color=BLUE,
            stroke_width=3
        ).move_to(original_expr[0][6:7].get_center())
        
        self.play(Create(nine_circle), run_time=0.5)
        self.play(FadeOut(nine_circle), FadeIn(check_2), run_time=0.6)
        
        # 步骤3: 检查中间项
        step_3 = Text(
            "③ 检查中间项:",
            font="PingFang SC",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.4)
        
        check_3_1 = MathTex(r"6x = 2 \cdot x \cdot 3", font_size=24, color=self.COLOR_HIGHLIGHT)
        check_3_2 = Text("✓", font_size=30, color=self.COLOR_SUCCESS)
        check_3 = VGroup(check_3_1, check_3_2).arrange(RIGHT, buff=0.2).next_to(step_3, DOWN, buff=0.2)
        
        self.play(FadeIn(step_3), run_time=0.4)
        
        # 高亮中间项
        six_x_circle = Circle(
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(original_expr[0][3:5].get_center())
        
        self.play(Create(six_x_circle), run_time=0.5)
        self.play(FadeOut(six_x_circle), FadeIn(check_3), run_time=0.8)
        
        self.wait(0.5)
        
        # 公式对应
        correspond_text = Text(
            "对应公式:",
            font="PingFang SC",
            font_size=22,
            color=GRAY
        ).move_to(DOWN * 2)
        
        correspond_a = MathTex(r"a = x", font_size=22, color=self.COLOR_SECONDARY)
        correspond_b = MathTex(r"b = 3", font_size=22, color=BLUE)
        correspond_group = VGroup(correspond_a, correspond_b).arrange(RIGHT, buff=1.2).next_to(correspond_text, DOWN, buff=0.3)
        
        self.play(FadeIn(correspond_text), FadeIn(correspond_group), run_time=0.8)
        
        self.wait(0.6)
        
        # 结果出现
        result_expr = MathTex(
            r"(x+3)^2",
            font_size=40,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3.8)
        
        result_box = SurroundingRectangle(
            result_expr,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(result_expr), run_time=1.0)
        self.play(Create(result_box), run_time=0.5)
        
        # 对号确认
        checkmark = Text(
            "✓",
            font_size=60,
            color=self.COLOR_SUCCESS
        ).next_to(result_box, RIGHT, buff=0.3)
        
        self.play(FadeIn(checkmark, scale=2), run_time=0.5)
        
        # 技巧提示
        tip_text = Text(
            "技巧: 中间项是关键!",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(tip_text, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(original_group),
            FadeOut(step_1),
            FadeOut(check_1),
            FadeOut(step_2),
            FadeOut(check_2),
            FadeOut(step_3),
            FadeOut(check_3),
            FadeOut(correspond_text),
            FadeOut(correspond_group),
            FadeOut(result_box),
            FadeOut(checkmark),
            FadeOut(tip_text),
            result_expr.animate.scale(0.6).move_to(UP * 5.3 + RIGHT * 3),
            run_time=0.8
        )
        
        self.example_2_result = result_expr
    
    def show_challenge_example(self):
        """场景6: 综合挑战例题 (60-72s)"""
        # 挑战题标题
        challenge_title = Text(
            "挑战题",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5)
        
        star_1 = Text("⭐", font_size=30, color=GOLD).next_to(challenge_title, LEFT, buff=0.3)
        star_2 = Text("⭐", font_size=30, color=GOLD).next_to(challenge_title, RIGHT, buff=0.3)
        
        challenge_group = VGroup(star_1, challenge_title, star_2)
        
        self.play(FadeIn(challenge_group, scale=1.3), run_time=0.7)
        
        # 原式
        original_text = Text("因式分解:", font="PingFang SC", font_size=self.FONT_SIZE_BODY, color=WHITE)
        original_expr = MathTex(r"4x^2 - 9y^2", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 提示: 平方差结构
        hint = Text(
            "这是平方差结构!",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 分解 4x²
        step_1 = MathTex(
            r"4x^2 = (2x)^2",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.2)
        
        self.play(
            original_expr[0][0:3].animate.set_color(self.COLOR_SECONDARY),
            run_time=0.5
        )
        self.play(Write(step_1), run_time=0.8)
        
        # 分解 9y²
        step_2 = MathTex(
            r"9y^2 = (3y)^2",
            font_size=28,
            color=BLUE
        ).move_to(UP * 0.4)
        
        self.play(
            original_expr[0][4:7].animate.set_color(BLUE),
            run_time=0.5
        )
        self.play(Write(step_2), run_time=0.8)
        
        # 重写表达式
        rewritten_expr = MathTex(
            r"(2x)^2 - (3y)^2",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        rewritten_label = Text(
            "改写为:",
            font="PingFang SC",
            font_size=22,
            color=GRAY
        ).next_to(rewritten_expr, LEFT, buff=0.3)
        
        self.play(Write(rewritten_label), Write(rewritten_expr), run_time=1.0)
        
        # 应用公式指示
        formula_arrow = Arrow(
            rewritten_expr.get_bottom(),
            rewritten_expr.get_bottom() + DOWN * 0.8,
            color=self.COLOR_PRIMARY,
            buff=0.1,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        
        formula_label_cn = Text(
            "应用",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_PRIMARY
        )
        formula_label_math = MathTex(
            r"a^2-b^2=(a+b)(a-b)",
            font_size=22,
            color=self.COLOR_PRIMARY
        )
        formula_label = VGroup(formula_label_cn, formula_label_math).arrange(RIGHT, buff=0.1)
        formula_label.next_to(formula_arrow, DOWN, buff=0.1)
        
        self.play(Create(formula_arrow), FadeIn(formula_label), run_time=1.0)
        
        # 对应关系
        correspond_text = MathTex(
            r"a = 2x, \quad b = 3y",
            font_size=22,
            color=GRAY
        ).next_to(formula_label, DOWN, buff=0.3)
        
        self.play(FadeIn(correspond_text), run_time=0.6)
        
        self.wait(0.6)
        
        # 最终结果
        result_expr = MathTex(
            r"(2x+3y)(2x-3y)",
            font_size=42,
            color=GOLD
        ).move_to(DOWN * 4)
        
        result_box = SurroundingRectangle(
            result_expr,
            color=GOLD,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=4
        )
        
        self.play(Write(result_expr), run_time=1.2)
        self.play(Create(result_box), run_time=0.6)
        
        # 庆祝动画
        stars = VGroup(*[
            Text("⭐", font_size=40, color=GOLD)
            .move_to(result_box.get_center() + 1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            Flash(result_expr, color=GOLD, flash_radius=0.8, num_lines=12),
            *[FadeIn(star, scale=0.5) for star in stars],
            run_time=1.0
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(challenge_group),
            FadeOut(original_group),
            FadeOut(hint),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(rewritten_label),
            FadeOut(rewritten_expr),
            FadeOut(formula_arrow),
            FadeOut(formula_label),
            FadeOut(correspond_text),
            FadeOut(result_box),
            FadeOut(stars),
            result_expr.animate.scale(0.5).move_to(UP * 4.8),
            run_time=0.8
        )
        
        self.challenge_result = result_expr
    
    def show_summary(self):
        """场景7: 总结与关注 (72-80s)"""
        # 总结标题
        summary_title = Text(
            "三大公式助你快速分解!",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title, run_time=1.0))
        
        # 三个公式卡片重新整理
        # 平方差公式卡片
        card_1_title = Text(
            "平方差公式",
            font="PingFang SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )
        card_1_formula = MathTex(
            r"a^2-b^2=(a+b)(a-b)",
            font_size=26,
            color=self.COLOR_PRIMARY
        )
        card_1 = VGroup(card_1_title, card_1_formula).arrange(DOWN, buff=0.2)
        card_1_bg = RoundedRectangle(
            width=card_1.width + 0.6,
            height=card_1.height + 0.4,
            fill_color=self.COLOR_FORMULA_BG,
            fill_opacity=0.8,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
            corner_radius=0.15
        )
        card_1_group = VGroup(card_1_bg, card_1).move_to(UP * 3)
        
        # 完全平方公式(+)卡片
        card_2_title = Text(
            "完全平方 (+)",
            font="PingFang SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )
        card_2_formula = MathTex(
            r"a^2+2ab+b^2=(a+b)^2",
            font_size=24,
            color=self.COLOR_PRIMARY
        )
        card_2 = VGroup(card_2_title, card_2_formula).arrange(DOWN, buff=0.2)
        card_2_bg = RoundedRectangle(
            width=card_2.width + 0.6,
            height=card_2.height + 0.4,
            fill_color=self.COLOR_FORMULA_BG,
            fill_opacity=0.8,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
            corner_radius=0.15
        )
        card_2_group = VGroup(card_2_bg, card_2).move_to(UP * 1.2)
        
        # 完全平方公式(-)卡片
        card_3_title = Text(
            "完全平方 (-)",
            font="PingFang SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )
        card_3_formula = MathTex(
            r"a^2-2ab+b^2=(a-b)^2",
            font_size=24,
            color=self.COLOR_PRIMARY
        )
        card_3 = VGroup(card_3_title, card_3_formula).arrange(DOWN, buff=0.2)
        card_3_bg = RoundedRectangle(
            width=card_3.width + 0.6,
            height=card_3.height + 0.4,
            fill_color=self.COLOR_FORMULA_BG,
            fill_opacity=0.8,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
            corner_radius=0.15
        )
        card_3_group = VGroup(card_3_bg, card_3).move_to(DOWN * 0.6)
        
        formula_cards = VGroup(card_1_group, card_2_group, card_3_group)
        
        # 卡片依次出现
        for card in formula_cards:
            self.play(FadeIn(card, scale=0.9), run_time=0.5)
            self.wait(0.2)
        
        # 公式闪烁强调
        self.play(
            Flash(card_1_group, color=self.COLOR_PRIMARY, flash_radius=0.8),
            run_time=0.4
        )
        self.play(
            Flash(card_2_group, color=self.COLOR_PRIMARY, flash_radius=0.8),
            run_time=0.4
        )
        self.play(
            Flash(card_3_group, color=self.COLOR_PRIMARY, flash_radius=0.8),
            run_time=0.4
        )
        
        # 记忆口诀
        mnemonic_1 = Text(
            "两平方相减 → 平方差",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        mnemonic_2 = Text(
            "三项式中间2ab → 完全平方",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.3)
        
        self.play(FadeIn(mnemonic_1, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(mnemonic_2, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.0)
        
        # 清除上方内容，准备片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(formula_cards),
            FadeOut(mnemonic_1),
            FadeOut(mnemonic_2),
            run_time=0.6
        )
        
        # 作者信息放大居中
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 公式图标环绕装饰
        icon_radius = 2.5
        icons = VGroup(*[
            Circle(
                radius=0.25,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.8,
                stroke_width=0
            ).move_to(
                follow_text.get_center() + icon_radius * np.array([np.cos(i * 2 * PI / 8), np.sin(i * 2 * PI / 8), 0])
            )
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.8
        )
        
        # 旋转动画
        self.play(Rotate(icons, angle=PI, run_time=1.5, rate_func=smooth))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql factorization_formulas.py FactorizationFormulas  # 快速预览 (480p 15fps)
# manim -qm factorization_formulas.py FactorizationFormulas   # 中等质量 (720p 30fps)
# manim -qh factorization_formulas.py FactorizationFormulas   # 高质量 (1080p 60fps)