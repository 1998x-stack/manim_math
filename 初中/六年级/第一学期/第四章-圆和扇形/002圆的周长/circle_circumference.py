"""
圆的周长 - Circle Circumference Animation
使用 Manim 创建的六年级数学教学视频

内容: 周长定义、π的意义、周长公式 C=πd=2πr
目标观众: 六年级学生
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


class CircleCircumference(Scene):
    """
    圆的周长教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 周长定义
    3. 神奇的π
    4. 公式 C=πd
    5. 公式 C=2πr
    6. 视觉验证 - 展开圆
    7. 实际应用
    8. 总结回顾
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"         # 蓝色 - 圆
        self.COLOR_CIRCUMFERENCE = "#e74c3c"  # 红色 - 周长
        self.COLOR_DIAMETER = "#f39c12"       # 橙色 - 直径
        self.COLOR_RADIUS = "#2ecc71"         # 绿色 - 半径
        self.COLOR_PI = "#9b59b6"             # 紫色 - π
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_pi()
        self.show_formula_pi_d()
        self.show_formula_2pi_r()
        self.show_unroll_verification()
        self.show_application()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化圆和所有几何元素"""
        # 主圆参数
        self.O = ORIGIN + UP * 1.0  # 圆心位置
        self.radius = 2.0  # 半径
        self.diameter = 2 * self.radius  # 直径
        
        # 创建主圆
        self.main_circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        # 圆心点
        self.center_dot = Dot(
            self.O,
            color=self.COLOR_CIRCLE,
            radius=0.08
        )
        
        # 直径端点
        self.D1 = self.O + LEFT * self.radius
        self.D2 = self.O + RIGHT * self.radius
        
        # 半径端点（右侧）
        self.P_right = self.O + RIGHT * self.radius
        
        # 周长（用于计算）
        self.circumference = 2 * PI * self.radius
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "圆一周有多长？",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 圆形创建
        self.play(Create(self.main_circle), run_time=1.0)
        
        # 圆周高亮闪烁
        self.play(
            self.main_circle.animate.set_color(self.COLOR_CIRCUMFERENCE).set_stroke(width=6),
            Flash(self.main_circle, color=self.COLOR_CIRCUMFERENCE, flash_radius=self.radius + 0.5),
            run_time=0.8
        )
        
        self.play(
            self.main_circle.animate.set_color(self.COLOR_CIRCLE).set_stroke(width=3),
            run_time=0.4
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.5)
    
    def show_definition(self):
        """场景2: 周长定义"""
        # 标题
        title = Text(
            "什么是周长？",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 定义文字
        definition = Text(
            "周长是圆一周的长度",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(Write(definition), run_time=1.5)
        
        # 小点沿圆运动
        # 起点在圆的右侧
        start_point = self.O + RIGHT * self.radius
        moving_dot = Dot(start_point, color=self.COLOR_CIRCUMFERENCE, radius=0.12)
        
        self.play(FadeIn(moving_dot, scale=0.5), run_time=0.4)
        
        # 使用 MoveAlongPath 让点沿圆运动
        circle_path = self.main_circle.copy()
        
        self.play(
            MoveAlongPath(moving_dot, circle_path, rate_func=linear),
            self.main_circle.animate.set_color(self.COLOR_CIRCUMFERENCE).set_stroke(width=5),
            run_time=2.5
        )
        
        # 圆周加粗后恢复
        self.play(
            self.main_circle.animate.set_color(self.COLOR_CIRCLE).set_stroke(width=3),
            run_time=0.4
        )
        
        # 公式提示
        formula_hint = Text(
            "如何计算这个长度呢？",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula_hint), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(formula_hint),
            FadeOut(moving_dot),
            run_time=0.6
        )
    
    def show_pi(self):
        """场景3: 神奇的π"""
        # 标题
        title = Text(
            "神奇的常数 π",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_PI
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 直径线段
        diameter = Line(
            self.D1,
            self.D2,
            color=self.COLOR_DIAMETER,
            stroke_width=4
        )
        
        self.play(Create(diameter), run_time=0.6)
        
        # 标注直径
        label_d = MathTex("d", font_size=32, color=self.COLOR_DIAMETER).next_to(diameter, DOWN, buff=0.15)
        
        self.play(FadeIn(label_d), run_time=0.4)
        
        # 比值公式
        ratio_formula = MathTex(
            r"\frac{C}{d} = ?",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(ratio_formula), run_time=1.0)
        
        # π符号闪亮登场
        pi_symbol = MathTex(
            r"\pi",
            font_size=72,
            color=self.COLOR_PI
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeIn(pi_symbol, scale=0.5),
            Flash(pi_symbol, color=self.COLOR_PI, flash_radius=1.0),
            run_time=0.8
        )
        
        # 更新公式
        ratio_formula_complete = MathTex(
            r"\frac{C}{d} = \pi",
            font_size=36,
            color=self.COLOR_PI
        ).move_to(UP * 4.5)
        
        self.play(Transform(ratio_formula, ratio_formula_complete), run_time=0.6)
        
        # π的值
        pi_value = MathTex(
            r"\pi \approx 3.14159...",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 1.8)
        
        self.play(Write(pi_value), run_time=1.0)
        
        # 说明文字
        explanation = Text(
            "圆周长是直径的π倍",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(explanation), run_time=1.5)
        
        self.wait(2.0)
        
        # 清理，保留π符号但缩小移到角落
        pi_small = MathTex(r"\pi", font_size=28, color=self.COLOR_PI).move_to(UP * 6.5 + RIGHT * 3.5)
        
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(diameter),
            FadeOut(label_d),
            FadeOut(ratio_formula),
            FadeOut(pi_value),
            Transform(pi_symbol, pi_small),
            run_time=0.6
        )
        
        # 保存小π符号的引用
        self.pi_small = pi_symbol
    
    def show_formula_pi_d(self):
        """场景4: 周长公式 C=πd"""
        # 标题
        title = Text(
            "周长公式",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 直径重新出现
        diameter = Line(
            self.D1,
            self.D2,
            color=self.COLOR_DIAMETER,
            stroke_width=4
        )
        
        label_d = MathTex("d", font_size=28, color=self.COLOR_DIAMETER).next_to(diameter, DOWN, buff=0.15)
        
        self.play(
            Create(diameter),
            FadeIn(label_d),
            run_time=0.6
        )
        
        # 公式 C = πd
        formula_1 = MathTex(
            r"C = \pi d",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.2)
        
        self.play(Write(formula_1), run_time=1.0)
        
        # 公式分解说明
        c_label = Text("周长", font="PingFang SC", font_size=20, color=self.COLOR_CIRCUMFERENCE).next_to(formula_1, LEFT, buff=1.5).shift(UP * 0.05)
        pi_label = Text("圆周率", font="PingFang SC", font_size=20, color=self.COLOR_PI).next_to(formula_1, DOWN, buff=0.3).shift(LEFT * 0.5)
        d_label = Text("直径", font="PingFang SC", font_size=20, color=self.COLOR_DIAMETER).next_to(formula_1, DOWN, buff=0.3).shift(RIGHT * 0.7)
        
        arrows_c = Arrow(c_label.get_right(), formula_1.get_left() + LEFT * 0.05, buff=0.05, color=self.COLOR_CIRCUMFERENCE, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        arrow_pi = Arrow(pi_label.get_top(), formula_1.get_bottom() + DOWN * 0.05 + LEFT * 0.3, buff=0.05, color=self.COLOR_PI, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        arrow_d = Arrow(d_label.get_top(), formula_1.get_bottom() + DOWN * 0.05 + RIGHT * 0.4, buff=0.05, color=self.COLOR_DIAMETER, stroke_width=2, max_tip_length_to_length_ratio=0.15)
        
        self.play(
            FadeIn(c_label),
            FadeIn(pi_label),
            FadeIn(d_label),
            Create(arrows_c),
            Create(arrow_pi),
            Create(arrow_d),
            run_time=1.5
        )
        
        # 数值示例
        example_text = Text(
            "例如：直径 d = 4",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 2)
        
        calculation = MathTex(
            r"C = \pi \times 4 \approx 3.14 \times 4 = 12.56",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(
            FadeIn(example_text),
            run_time=0.8
        )
        
        self.play(
            Write(calculation),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(diameter),
            FadeOut(label_d),
            FadeOut(c_label),
            FadeOut(pi_label),
            FadeOut(d_label),
            FadeOut(arrows_c),
            FadeOut(arrow_pi),
            FadeOut(arrow_d),
            FadeOut(example_text),
            FadeOut(calculation),
            run_time=0.6
        )
        
        # 公式移到上方
        formula_1_small = MathTex(r"C = \pi d", font_size=32, color=WHITE).move_to(UP * 5.5 + LEFT * 1.5)
        self.play(Transform(formula_1, formula_1_small), run_time=0.5)
        
        # 保存引用
        self.formula_1 = formula_1
    
    def show_formula_2pi_r(self):
        """场景5: 第二个公式 C=2πr"""
        # 标题
        title = Text(
            "另一种表达",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 半径线段
        radius = Line(
            self.O,
            self.P_right,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        label_r = MathTex("r", font_size=28, color=self.COLOR_RADIUS).next_to(radius, DOWN, buff=0.1)
        
        self.play(
            Create(radius),
            FadeIn(label_r),
            run_time=0.6
        )
        
        # 标注 d = 2r
        relation = MathTex(
            r"d = 2r",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(Write(relation), run_time=0.8)
        
        # 公式变换
        transform_text = Text(
            "代入公式:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3)
        
        self.play(FadeIn(transform_text), run_time=0.5)
        
        step_1 = MathTex(r"C = \pi {{ d }}", font_size=36).move_to(UP * 2)
        step_2 = MathTex(r"C = \pi \cdot {{ 2r }}", font_size=36).move_to(UP * 2)
        step_3 = MathTex(r"C = 2\pi r", font_size=36).move_to(UP * 2)
        
        self.play(Write(step_1), run_time=0.6)
        self.wait(0.4)
        self.play(TransformMatchingTex(step_1, step_2), run_time=0.8)
        self.wait(0.4)
        self.play(TransformMatchingTex(step_2, step_3), run_time=0.8)
        
        # 强调最终公式
        formula_2 = MathTex(
            r"C = 2\pi r",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(
            ReplacementTransform(step_3, formula_2),
            run_time=0.6
        )
        
        # 说明
        explanation = Text(
            "两个公式都正确，可根据已知条件选用",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(Write(explanation), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(radius),
            FadeOut(label_r),
            FadeOut(relation),
            FadeOut(transform_text),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 公式移到右上方
        formula_2_small = MathTex(r"C = 2\pi r", font_size=32, color=WHITE).move_to(UP * 5.5 + RIGHT * 1.8)
        self.play(Transform(formula_2, formula_2_small), run_time=0.5)
        
        # 保存引用
        self.formula_2 = formula_2
    
    def show_unroll_verification(self):
        """场景6: 视觉验证 - 展开圆"""
        # 标题
        title = Text(
            "验证：展开圆周",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 圆周高亮
        self.play(
            self.main_circle.animate.set_color(self.COLOR_CIRCUMFERENCE).set_stroke(width=5),
            run_time=0.4
        )
        
        # 标记起点
        start_point = self.O + RIGHT * self.radius
        start_dot = Dot(start_point, color=self.COLOR_HIGHLIGHT, radius=0.12)
        start_label = Text("起点", font="PingFang SC", font_size=20, color=self.COLOR_HIGHLIGHT).next_to(start_dot, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(start_dot, scale=0.5),
            FadeIn(start_label),
            run_time=0.3
        )
        
        # "展开"动画 - 使用 Arc 逐渐变平
        # 创建展开的目标位置
        unroll_y = DOWN * 2
        unroll_start = LEFT * (PI * self.radius) + unroll_y
        unroll_end = RIGHT * (PI * self.radius) + unroll_y
        
        # 创建展开的线段（周长）
        unrolled_line = Line(
            unroll_start,
            unroll_end,
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=5
        )
        
        # 说明文字
        unroll_text = Text(
            "将圆周拉直...",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(unroll_text), run_time=0.6)
        
        # 圆周变形为直线（使用变换）
        self.play(
            Transform(self.main_circle.copy(), unrolled_line),
            FadeOut(start_dot),
            FadeOut(start_label),
            run_time=3.0
        )
        
        # 创建展开线的副本以便操作
        unrolled_copy = Line(
            unroll_start,
            unroll_end,
            color=self.COLOR_CIRCUMFERENCE,
            stroke_width=5
        )
        self.add(unrolled_copy)
        
        self.play(FadeOut(unroll_text), run_time=0.3)
        
        # 恢复原圆
        self.play(
            self.main_circle.animate.set_color(self.COLOR_CIRCLE).set_stroke(width=3),
            run_time=0.4
        )
        
        # 直径线段对比
        diameter_length = 2 * self.radius
        
        # 创建多个直径副本来对比
        num_diameters = 3  # 显示3个直径长度
        diameter_copies = VGroup()
        
        for i in range(num_diameters):
            d_copy = Line(
                unroll_start + RIGHT * i * diameter_length,
                unroll_start + RIGHT * (i + 1) * diameter_length,
                color=self.COLOR_DIAMETER,
                stroke_width=4
            )
            diameter_copies.add(d_copy)
        
        # 添加超出部分的虚线
        extra_length = self.circumference - num_diameters * diameter_length
        extra_line = DashedLine(
            unroll_start + RIGHT * num_diameters * diameter_length,
            unroll_end,
            color=self.COLOR_DIAMETER,
            stroke_width=3,
            dash_length=0.08
        )
        
        self.play(
            Create(diameter_copies),
            Create(extra_line),
            run_time=1.5
        )
        
        # 标注π倍关系
        brace = Brace(unrolled_copy, direction=DOWN, buff=0.2, color=WHITE)
        brace_label = MathTex(r"C = \pi d", font_size=28, color=WHITE).next_to(brace, DOWN, buff=0.1)
        
        # 标注直径
        d_brace = Brace(diameter_copies[0], direction=UP, buff=0.1, color=self.COLOR_DIAMETER)
        d_label = MathTex("d", font_size=24, color=self.COLOR_DIAMETER).next_to(d_brace, UP, buff=0.05)
        
        self.play(
            FadeIn(brace),
            FadeIn(brace_label),
            FadeIn(d_brace),
            FadeIn(d_label),
            run_time=1.5
        )
        
        # 强调π ≈ 3.14
        pi_text = Text(
            "周长约等于3.14个直径",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(pi_text, shift=UP * 0.3), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(unrolled_copy),
            FadeOut(diameter_copies),
            FadeOut(extra_line),
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(d_brace),
            FadeOut(d_label),
            FadeOut(pi_text),
            run_time=0.6
        )
    
    def show_application(self):
        """场景7: 实际应用示例"""
        # 标题
        title = Text(
            "实际应用",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 问题
        problem = Text(
            "一个圆的半径为 3 厘米，\n求周长是多少？",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(problem), run_time=1.2)
        
        # 圆的参数标注
        radius_line = Line(
            self.O,
            self.O + RIGHT * self.radius,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        radius_label = MathTex(r"r = 3 \text{ cm}", font_size=28, color=self.COLOR_RADIUS).next_to(radius_line, DOWN, buff=0.15)
        
        self.play(
            Create(radius_line),
            FadeIn(radius_label),
            run_time=0.8
        )
        
        # 解题步骤
        solution_title = Text(
            "解：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 2.5 + LEFT * 3.5)
        
        step_1 = MathTex(
            r"C = 2\pi r",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.8)
        
        step_2 = MathTex(
            r"= 2 \times \pi \times 3",
            font_size=32,
            color=WHITE
        ).move_to(UP * 0.8)
        
        step_3 = MathTex(
            r"= 6\pi",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.2)
        
        step_4 = MathTex(
            r"\approx 6 \times 3.14 = 18.84 \text{ cm}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1.2)
        
        self.play(FadeIn(solution_title), run_time=0.3)
        self.play(Write(step_1), run_time=0.8)
        self.play(Write(step_2), run_time=1.0)
        self.play(Write(step_3), run_time=1.0)
        self.play(Write(step_4), run_time=1.0)
        
        # 答案高亮
        answer = Text(
            "答：周长约为 18.84 厘米",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(
            FadeIn(answer, scale=1.1),
            Flash(answer, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(solution_title),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(step_3),
            FadeOut(step_4),
            FadeOut(answer),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 总结回顾"""
        # 标题
        title = Text(
            "周长知识要点",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 清除之前的公式
        if hasattr(self, 'formula_1'):
            self.play(FadeOut(self.formula_1), FadeOut(self.formula_2), FadeOut(self.pi_small), run_time=0.3)
        
        # 圆缩小移到上方
        self.play(
            self.main_circle.animate.scale(0.6).move_to(UP * 3.5),
            self.center_dot.animate.scale(0.6).move_to(UP * 3.5),
            run_time=0.8
        )
        
        # 知识卡片
        cards_data = [
            ("周长定义", "圆一周的长度", self.COLOR_CIRCUMFERENCE, UP * 1.8),
            ("圆周率 π", "周长与直径的比值 ≈ 3.14", self.COLOR_PI, UP * 0.8),
            ("公式1", "C = πd (已知直径)", self.COLOR_DIAMETER, DOWN * 0.2),
            ("公式2", "C = 2πr (已知半径)", self.COLOR_RADIUS, DOWN * 1.2),
        ]
        
        cards = VGroup()
        
        for name, desc, color, pos in cards_data:
            # 图标圆
            icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
            
            # 名称
            name_text = Text(
                name,
                font="PingFang SC",
                font_size=22,
                color=WHITE,
                weight=BOLD
            )
            
            # 描述
            desc_text = Text(
                desc,
                font="PingFang SC",
                font_size=18,
                color=GRAY_A
            )
            
            # 组合
            card = VGroup(icon, name_text, desc_text).arrange(RIGHT, buff=0.2)
            card.move_to(pos)
            
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.6
            )
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight_text = Text(
            "掌握公式，轻松计算圆周长！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.main_circle),
            FadeOut(self.center_dot),
            FadeOut(cards),
            FadeOut(highlight_text),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景9: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID出现
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        circles_deco = VGroup(*[
            Circle(
                radius=0.3,
                color=self.COLOR_CIRCLE,
                fill_opacity=0.6,
                stroke_width=2
            ).move_to(
                follow_text.get_center() + 
                2.0 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles_deco],
            run_time=0.6
        )
        
        self.play(
            Rotate(circles_deco, angle=PI, about_point=follow_text.get_center()),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles_deco),
            run_time=1.0
        )


# 运行命令:
# manim -pql circle_circumference.py CircleCircumference  # 快速预览
# manim -qh circle_circumference.py CircleCircumference   # 高质量渲染