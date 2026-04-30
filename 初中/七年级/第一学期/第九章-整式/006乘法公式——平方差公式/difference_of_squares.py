"""
平方差公式教学动画 - Difference of Squares Formula Animation
使用 Manim 创建的初中数学教学视频

内容: (a+b)(a-b) = a² - b²
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


class DifferenceOfSquares(Scene):
    """
    平方差公式教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 公式引入
    3. 几何证明 - 构建大正方形
    4. 几何证明 - 减去小正方形
    5. 几何证明 - 重组为矩形
    6. 具体例子
    7. 逆用公式 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要公式
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调部分
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数/加法
        self.COLOR_NEGATIVE = "#e67e22"     # 橙色 - 负数/减法
        self.COLOR_SQUARE_A = "#9b59b6"     # 紫色 - a² 区域
        self.COLOR_SQUARE_B = "#1abc9c"     # 青色 - b² 区域
        self.COLOR_AUXILIARY = GRAY_B       # 辅助线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_formula_intro()
        self.scene_3_build_square_a()
        self.scene_4_subtract_square_b()
        self.scene_5_rearrange_rectangles()
        self.scene_6_concrete_example()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素和参数"""
        # 正方形参数
        self.a = 2.5  # 大正方形边长
        self.b = 1.0  # 小正方形边长
        
        # 位置偏移
        self.square_center = UP * 1.5
        
        # 大正方形的四个顶点
        self.A_TL = self.square_center + np.array([-self.a/2, self.a/2, 0])   # 左上
        self.A_TR = self.square_center + np.array([self.a/2, self.a/2, 0])    # 右上
        self.A_BL = self.square_center + np.array([-self.a/2, -self.a/2, 0])  # 左下
        self.A_BR = self.square_center + np.array([self.a/2, -self.a/2, 0])   # 右下
        
        # 小正方形中心（右上角对齐）
        self.square_b_center = self.A_TR + np.array([-self.b/2, -self.b/2, 0])
        
        # 小正方形的四个顶点
        self.B_TL = self.square_b_center + np.array([-self.b/2, self.b/2, 0])
        self.B_TR = self.square_b_center + np.array([self.b/2, self.b/2, 0])
        self.B_BL = self.square_b_center + np.array([-self.b/2, -self.b/2, 0])
        self.B_BR = self.square_b_center + np.array([self.b/2, -self.b/2, 0])
        
        # L形区域的关键点
        # 上方矩形：从大正方形左上到小正方形左下的区域
        self.top_rect_TL = self.A_TL
        self.top_rect_TR = self.A_TR
        self.top_rect_BL = np.array([self.A_TL[0], self.B_BL[1], 0])
        self.top_rect_BR = self.B_BL
        
        # 右侧矩形：从小正方形左下到大正方形右下的区域
        self.right_rect_TL = self.B_BL
        self.right_rect_TR = self.B_BR
        self.right_rect_BL = np.array([self.B_BL[0], self.A_BL[1], 0])
        self.right_rect_BR = self.A_BR
        
        # 重组后的矩形位置（下方）
        self.final_rect_center = DOWN * 3
        
        print("✓ 几何参数初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "快速计算",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5)
        
        hook_formula = MathTex(
            r"(x+2)(x-2) = \,?",
            font_size=56,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.5)
        
        # 问号特别高亮
        question_mark = hook_formula[-1]
        
        self.play(Write(hook_question), run_time=0.6)
        self.play(Write(hook_formula), run_time=0.8)
        self.play(
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            question_mark.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.2),
            run_time=0.5
        )
        
        # 思考时间
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hook_formula),
            run_time=0.5
        )
    
    def scene_2_formula_intro(self):
        """场景2: 公式引入"""
        # 标题
        title = Text(
            "平方差公式",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式 - 分步出现
        formula_left = MathTex(
            r"(a+b)(a-b)",
            font_size=44,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        equals = MathTex(
            r"=",
            font_size=44,
            color=WHITE
        ).next_to(formula_left, RIGHT, buff=0.3)
        
        formula_right = MathTex(
            r"a^2 - b^2",
            font_size=44,
            color=self.COLOR_SECONDARY
        ).next_to(equals, RIGHT, buff=0.3)
        
        # 组合完整公式
        full_formula = VGroup(formula_left, equals, formula_right)
        
        self.play(Write(formula_left), run_time=0.8)
        self.play(Write(equals), run_time=0.3)
        self.play(Write(formula_right), run_time=0.8)
        
        # 高亮整个公式
        self.play(Indicate(full_formula, color=self.COLOR_HIGHLIGHT), run_time=0.8)
        
        # 文字解释
        explanation = Text(
            "两数和 × 两数差 = 两数平方差",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理并移动公式到顶部作为参考
        self.play(FadeOut(title), FadeOut(explanation), run_time=0.4)
        
        # 创建小号参考公式
        self.reference_formula = MathTex(
            r"(a+b)(a-b) = a^2 - b^2",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(full_formula, self.reference_formula),
            run_time=0.6
        )
        self.remove(full_formula)
        self.add(self.reference_formula)
    
    def scene_3_build_square_a(self):
        """场景3: 构建大正方形"""
        # 引导文字
        guide_text = Text(
            "让我们用面积来理解这个公式",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(guide_text, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 创建大正方形
        square_a = Polygon(
            self.A_TL, self.A_TR, self.A_BR, self.A_BL,
            color=self.COLOR_SQUARE_A,
            stroke_width=3,
            fill_opacity=0
        )
        
        self.play(Create(square_a), run_time=1.2)
        
        # 标注边长
        label_a_top = MathTex(r"a", font_size=32, color=WHITE).next_to(
            Line(self.A_TL, self.A_TR), UP, buff=0.15
        )
        label_a_right = MathTex(r"a", font_size=32, color=WHITE).next_to(
            Line(self.A_TR, self.A_BR), RIGHT, buff=0.15
        )
        label_a_bottom = MathTex(r"a", font_size=32, color=WHITE).next_to(
            Line(self.A_BL, self.A_BR), DOWN, buff=0.15
        )
        label_a_left = MathTex(r"a", font_size=32, color=WHITE).next_to(
            Line(self.A_TL, self.A_BL), LEFT, buff=0.15
        )
        
        labels_a = VGroup(label_a_top, label_a_right, label_a_bottom, label_a_left)
        
        self.play(Write(labels_a), run_time=0.8)
        
        # 填充颜色
        self.play(
            square_a.animate.set_fill(self.COLOR_SQUARE_A, opacity=0.3),
            run_time=0.6
        )
        
        # 面积标注
        area_a_label = MathTex(
            r"a^2",
            font_size=48,
            color=WHITE
        ).move_to(self.square_center)
        
        area_a_text = Text(
            "面积 =",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(area_a_label, LEFT, buff=0.2)
        
        area_a_group = VGroup(area_a_text, area_a_label)
        
        self.play(FadeIn(area_a_group, scale=0.8), run_time=0.6)
        self.wait(1.0)
        
        # 清理引导文字和面积标注，保留正方形
        self.play(
            FadeOut(guide_text),
            FadeOut(area_a_group),
            run_time=0.4
        )
        
        # 保存元素供后续使用
        self.square_a = square_a
        self.labels_a = labels_a
    
    def scene_4_subtract_square_b(self):
        """场景4: 减去小正方形"""
        # 引导文字
        guide_text = Text(
            "从中减去一个边长为 b 的正方形",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(guide_text, shift=UP * 0.3), run_time=0.6)
        
        # 创建小正方形 - 从中心缩放出现
        square_b = Polygon(
            self.B_TL, self.B_TR, self.B_BR, self.B_BL,
            color=self.COLOR_SQUARE_B,
            stroke_width=3,
            fill_opacity=0
        )
        
        square_b.scale(0.1).move_to(self.square_b_center)
        
        self.play(
            square_b.animate.scale(10).set_fill(self.COLOR_SQUARE_B, opacity=0.5),
            run_time=1.0
        )
        
        # 标注边长 b
        label_b_top = MathTex(r"b", font_size=28, color=WHITE).next_to(
            Line(self.B_TL, self.B_TR), UP, buff=0.1
        )
        label_b_right = MathTex(r"b", font_size=28, color=WHITE).next_to(
            Line(self.B_TR, self.B_BR), RIGHT, buff=0.1
        )
        
        labels_b = VGroup(label_b_top, label_b_right)
        
        self.play(Write(labels_b), run_time=0.6)
        
        # 面积标注 b²
        area_b_label = MathTex(
            r"b^2",
            font_size=36,
            color=WHITE
        ).move_to(self.square_b_center)
        
        self.play(FadeIn(area_b_label, scale=0.8), run_time=0.5)
        self.wait(0.5)
        
        # 高亮剩余的L形区域
        # 创建L形区域的轮廓
        l_shape = VGroup(
            # 上方矩形轮廓
            Polygon(
                self.top_rect_TL, self.top_rect_TR, self.top_rect_BR, self.top_rect_BL,
                color=self.COLOR_POSITIVE,
                stroke_width=4,
                fill_opacity=0
            ),
            # 右侧矩形轮廓
            Polygon(
                self.right_rect_TL, self.right_rect_TR, self.right_rect_BR, self.right_rect_BL,
                color=self.COLOR_POSITIVE,
                stroke_width=4,
                fill_opacity=0
            )
        )
        
        self.play(Create(l_shape), run_time=0.8)
        self.play(
            Flash(l_shape, color=self.COLOR_POSITIVE, flash_radius=0.5),
            run_time=0.5
        )
        
        # 剩余面积标注
        remaining_area = MathTex(
            r"a^2 - b^2",
            font_size=32,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 4.5)
        
        remaining_text = Text(
            "剩余面积 =",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(remaining_area, LEFT, buff=0.2)
        
        remaining_group = VGroup(remaining_text, remaining_area)
        
        self.play(FadeIn(remaining_group, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(guide_text),
            FadeOut(area_b_label),
            FadeOut(remaining_group),
            FadeOut(l_shape),
            run_time=0.4
        )
        
        # 保存元素
        self.square_b = square_b
        self.labels_b = labels_b
    
    def scene_5_rearrange_rectangles(self):
        """场景5: 重组为矩形"""
        # 引导文字
        guide_text = Text(
            "将剩余部分重新排列",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(guide_text, shift=UP * 0.3), run_time=0.6)
        
        # 创建分割线（虚线）
        division_line = DashedLine(
            self.B_BL, np.array([self.B_BL[0], self.A_BL[1], 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(division_line), run_time=0.6)
        self.wait(0.3)
        
        # 创建两个矩形
        # 上方矩形：宽 a, 高 b
        top_rect = Polygon(
            self.top_rect_TL, self.top_rect_TR, self.top_rect_BR, self.top_rect_BL,
            color=self.COLOR_POSITIVE,
            stroke_width=3,
            fill_color=self.COLOR_POSITIVE,
            fill_opacity=0.4
        )
        
        # 右侧矩形：宽 (a-b), 高 (a-b)
        right_rect = Polygon(
            self.right_rect_TL, self.right_rect_TR, self.right_rect_BR, self.right_rect_BL,
            color=self.COLOR_NEGATIVE,
            stroke_width=3,
            fill_color=self.COLOR_NEGATIVE,
            fill_opacity=0.4
        )
        
        # 高亮上方矩形
        self.play(
            FadeIn(top_rect, scale=1.05),
            run_time=0.6
        )
        
        # 标注上方矩形尺寸
        top_label_width = MathTex(r"a", font_size=26, color=WHITE).next_to(
            Line(self.top_rect_TL, self.top_rect_TR), UP, buff=0.1
        )
        top_label_height = MathTex(r"b", font_size=26, color=WHITE).next_to(
            Line(self.top_rect_TR, self.top_rect_BR), RIGHT, buff=0.1
        )
        
        self.play(Write(VGroup(top_label_width, top_label_height)), run_time=0.5)
        self.wait(0.4)
        
        # 高亮右侧矩形
        self.play(
            FadeIn(right_rect, scale=1.05),
            run_time=0.6
        )
        
        # 标注右侧矩形尺寸
        right_label_width = MathTex(r"a-b", font_size=24, color=WHITE).next_to(
            Line(self.right_rect_BL, self.right_rect_BR), DOWN, buff=0.1
        )
        right_label_height = MathTex(r"a-b", font_size=24, color=WHITE).next_to(
            Line(self.right_rect_TR, self.right_rect_BR), RIGHT, buff=0.1
        )
        
        self.play(Write(VGroup(right_label_width, right_label_height)), run_time=0.5)
        self.wait(0.5)
        
        # 淡出原始正方形和标签
        self.play(
            FadeOut(self.square_a),
            FadeOut(self.square_b),
            FadeOut(self.labels_a),
            FadeOut(self.labels_b),
            FadeOut(division_line),
            run_time=0.4
        )
        
        # 移动下方矩形到上方矩形下方
        # 计算目标位置
        target_y = self.top_rect_BL[1] - (self.a - self.b) / 2
        target_center = np.array([self.top_rect_BL[0] + (self.a - self.b) / 2, target_y, 0])
        
        self.play(
            right_rect.animate.move_to(target_center),
            right_label_width.animate.shift(DOWN * (self.top_rect_BL[1] - target_y - (self.a - self.b) / 2)),
            right_label_height.animate.shift(DOWN * (self.top_rect_BL[1] - target_y - (self.a - self.b) / 2)),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # 组合成大矩形并标注总尺寸
        # 淡出旧标签
        self.play(
            FadeOut(top_label_width),
            FadeOut(top_label_height),
            FadeOut(right_label_width),
            FadeOut(right_label_height),
            run_time=0.3
        )
        
        # 创建组合矩形的标注
        combined_width_label = MathTex(r"a+b", font_size=32, color=WHITE).next_to(
            Line(self.top_rect_TL, self.top_rect_TR), UP, buff=0.15
        )
        combined_height_label = MathTex(r"a-b", font_size=32, color=WHITE).next_to(
            Line(self.top_rect_TR, self.top_rect_BR), RIGHT, buff=0.15
        ).shift(DOWN * (self.a - self.b) / 2)
        
        self.play(
            Write(combined_width_label),
            Write(combined_height_label),
            run_time=0.8
        )
        
        # 最终面积公式
        final_area = MathTex(
            r"(a+b)(a-b)",
            font_size=40,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 4.5)
        
        final_text = Text(
            "面积 =",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).next_to(final_area, LEFT, buff=0.2)
        
        final_group = VGroup(final_text, final_area)
        
        self.play(FadeIn(final_group, shift=UP * 0.2), run_time=0.8)
        
        # 连接到参考公式
        equals_sign = MathTex(r"=", font_size=36, color=WHITE).next_to(final_area, RIGHT, buff=0.2)
        result_formula = MathTex(r"a^2 - b^2", font_size=40, color=self.COLOR_SECONDARY).next_to(
            equals_sign, RIGHT, buff=0.2
        )
        
        self.play(
            Write(equals_sign),
            Write(result_formula),
            run_time=0.8
        )
        
        # 高亮完整等式
        complete_formula = VGroup(final_text, final_area, equals_sign, result_formula)
        self.play(
            Indicate(complete_formula, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        self.wait(2.0)  # 关键理解时间
        
        # 清理
        self.play(
            FadeOut(guide_text),
            FadeOut(top_rect),
            FadeOut(right_rect),
            FadeOut(combined_width_label),
            FadeOut(combined_height_label),
            FadeOut(complete_formula),
            run_time=0.6
        )
    
    def scene_6_concrete_example(self):
        """场景6: 具体例子"""
        # 例子标题
        example_title = Text(
            "让我们计算开头的问题",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(example_title, shift=UP * 0.3), run_time=0.6)
        
        # 原题
        original_problem = MathTex(
            r"(x+2)(x-2)",
            font_size=48,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        self.play(Write(original_problem), run_time=0.8)
        self.wait(0.5)
        
        # 标识 a 和 b
        a_label = Text(
            "a = x",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 2.5 + LEFT * 2)
        
        b_label = Text(
            "b = 2",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 2.5 + RIGHT * 2)
        
        self.play(
            FadeIn(a_label, shift=RIGHT * 0.3),
            FadeIn(b_label, shift=LEFT * 0.3),
            run_time=0.6
        )
        
        # 高亮对应部分
        self.play(
            original_problem[0][1].animate.set_color(self.COLOR_POSITIVE),  # x in (x+2)
            original_problem[0][4].animate.set_color(self.COLOR_POSITIVE),  # x in (x-2)
            original_problem[0][2].animate.set_color(self.COLOR_NEGATIVE),  # 2 in (x+2)
            original_problem[0][5].animate.set_color(self.COLOR_NEGATIVE),  # 2 in (x-2)
            run_time=0.8
        )
        
        self.wait(0.6)
        
        # 套用公式
        arrow = MathTex(r"\Downarrow", font_size=48, color=WHITE).move_to(UP * 1)
        
        formula_hint = Text(
            "套用公式",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(arrow, RIGHT, buff=0.3)
        
        self.play(
            Write(arrow),
            FadeIn(formula_hint),
            run_time=0.6
        )
        
        # 中间步骤
        step_1 = MathTex(
            r"= x^2 - 2^2",
            font_size=44,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(step_1), run_time=0.8)
        self.wait(0.5)
        
        # 最终结果
        equals_2 = MathTex(r"=", font_size=44, color=WHITE).move_to(DOWN * 2)
        result = MathTex(
            r"x^2 - 4",
            font_size=52,
            color=self.COLOR_SECONDARY
        ).next_to(equals_2, RIGHT, buff=0.3)
        
        result_group = VGroup(equals_2, result)
        
        self.play(Write(result_group), run_time=0.8)
        
        # 高亮结果
        self.play(
            Indicate(result, color=self.COLOR_HIGHLIGHT, scale_factor=1.15),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(original_problem),
            FadeOut(a_label),
            FadeOut(b_label),
            FadeOut(arrow),
            FadeOut(formula_hint),
            FadeOut(step_1),
            FadeOut(result_group),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 逆用公式 + 片尾"""
        # 逆用提示
        reverse_title = Text(
            "公式也可以反过来用!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(reverse_title, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 逆向公式
        reverse_formula = MathTex(
            r"a^2 - b^2 = (a+b)(a-b)",
            font_size=44,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        self.play(Write(reverse_formula), run_time=1.0)
        
        # 应用场景
        application = Text(
            "用于因式分解",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(application), run_time=0.5)
        
        # 快速例子
        example = MathTex(
            r"x^2 - 9 = (x+3)(x-3)",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.2)
        
        self.play(Write(example), run_time=0.8)
        self.wait(1.2)
        
        # 淡出所有内容（包括参考公式）
        self.play(
            FadeOut(self.reference_formula),
            FadeOut(reverse_title),
            FadeOut(reverse_formula),
            FadeOut(application),
            FadeOut(example),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图案 - 小正方形围成一圈
        decorations = VGroup(*[
            Square(side_length=0.3, color=GOLD, fill_opacity=0.6)
            .move_to(follow_text.get_center() + 2.2 * np.array([np.cos(i * TAU / 8), np.sin(i * TAU / 8), 0]))
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI/4, run_time=1.5))
        
        # 公式图标快闪
        formula_icons = VGroup(
            MathTex(r"a^2", font_size=24, color=self.COLOR_SQUARE_A),
            MathTex(r"-", font_size=24, color=WHITE),
            MathTex(r"b^2", font_size=24, color=self.COLOR_SQUARE_B),
            MathTex(r"=", font_size=24, color=WHITE),
            MathTex(r"(a\!+\!b)(a\!-\!b)", font_size=24, color=self.COLOR_PRIMARY)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in formula_icons], run_time=0.6)
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            FadeOut(formula_icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql difference_of_squares.py DifferenceOfSquares  # 快速预览
# manim -qh difference_of_squares.py DifferenceOfSquares   # 高质量渲染