"""
平行线的性质动画 - Parallel Lines Properties Animation
使用 Manim 创建的初中几何教学视频

内容: 平行线的性质 - 同位角相等、内错角相等、同旁内角互补
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


class ParallelLinesProperties(Scene):
    """
    平行线性质教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 同位角相等
    3. 内错角相等  
    4. 同旁内角互补
    5. 动态验证
    6. 非平行线对比
    7. 总结回顾
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 平行线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 截线
        self.COLOR_HIGHLIGHT = "#f1c40f"    # 黄色 - 角度标记
        self.COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
        self.COLOR_TEXT = WHITE
        self.COLOR_EQUAL = GREEN              # 绿色 - 相等标记
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_corresponding_angles()
        self.show_alternate_angles()
        self.show_co_interior_angles()
        self.dynamic_verification()
        self.compare_non_parallel()
        self.summary_review()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化平行线和截线的几何数据"""
        # 基准平行线位置
        self.line_y_pos_1 = 1.0
        self.line_y_pos_2 = -1.0
        
        # 平行线的起始和结束点
        self.line1_start = np.array([-4, self.line_y_pos_1, 0])
        self.line1_end = np.array([4, self.line_y_pos_1, 0])
        self.line2_start = np.array([-4, self.line_y_pos_2, 0])
        self.line2_end = np.array([4, self.line_y_pos_2, 0])
        
        # 截线的起始和结束点 (斜线)
        self.transversal_start = np.array([-2.5, 3, 0])
        self.transversal_end = np.array([2.5, -3, 0])
        
        # 计算截线与平行线的交点
        # 由于平行线是水平的，截线是一条斜线，我们可以解析计算交点
        # 截线方程: y = mx + c
        # 斜率 m = (self.transversal_end[1] - self.transversal_start[1]) / (self.transversal_end[0] - self.transversal_start[0])
        self.slope = (self.transversal_end[1] - self.transversal_start[1]) / (self.transversal_end[0] - self.transversal_start[0])
        self.intercept = self.transversal_start[1] - self.slope * self.transversal_start[0]
        
        # 交点计算：对于水平线 y = y0，与截线的交点为 (x, y0)，其中 x = (y0 - intercept) / slope
        self.intersection1_x = (self.line_y_pos_1 - self.intercept) / self.slope
        self.intersection1 = np.array([self.intersection1_x, self.line_y_pos_1, 0])
        
        self.intersection2_x = (self.line_y_pos_2 - self.intercept) / self.slope
        self.intersection2 = np.array([self.intersection2_x, self.line_y_pos_2, 0])
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        # 验证交点确实在平行线上
        tolerance = 1e-6
        if abs(self.intersection1[1] - self.line_y_pos_1) > tolerance:
            print(f"WARNING: 交点1不在第一条平行线上! y={self.intersection1[1]}, expected={self.line_y_pos_1}")
        
        if abs(self.intersection2[1] - self.line_y_pos_2) > tolerance:
            print(f"WARNING: 交点2不在第二条平行线上! y={self.intersection2[1]}, expected={self.line_y_pos_2}")
        
        # 验证交点确实在截线上
        expected_y1 = self.slope * self.intersection1[0] + self.intercept
        expected_y2 = self.slope * self.intersection2[0] + self.intercept
        
        if abs(self.intersection1[1] - expected_y1) > tolerance:
            print(f"WARNING: 交点1不在截线上! y={self.intersection1[1]}, expected={expected_y1}")
        
        if abs(self.intersection2[1] - expected_y2) > tolerance:
            print(f"WARNING: 交点2不在截线上! y={self.intersection2[1]}, expected={expected_y2}")
        
        print("✓ 几何验证完成")
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 标题
        title = Text(
            "平行线的性质",
            font="PingFang SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "由线推角的秘密",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 5.7)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 创建平行线
        self.parallel_line1 = Line(
            self.line1_start, 
            self.line1_end, 
            color=self.COLOR_PRIMARY, 
            stroke_width=4
        )
        self.parallel_line2 = Line(
            self.line2_start, 
            self.line2_end, 
            color=self.COLOR_PRIMARY, 
            stroke_width=4
        )
        
        self.play(
            Create(self.parallel_line1),
            Create(self.parallel_line2),
            run_time=1.0
        )
        
        # 添加截线
        self.transversal_line = Line(
            self.transversal_start,
            self.transversal_end,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(self.transversal_line), run_time=1.0)
        
        # 交点
        self.point_A = Dot(self.intersection1, color=RED, radius=0.08)
        self.label_A = Text("A", font="PingFang SC", font_size=20, color=RED).next_to(self.point_A, UP, buff=0.1)
        self.point_B = Dot(self.intersection2, color=RED, radius=0.08)
        self.label_B = Text("B", font="PingFang SC", font_size=20, color=RED).next_to(self.point_B, DOWN, buff=0.1)
        
        self.play(
            FadeIn(self.point_A),
            FadeIn(self.label_A),
            FadeIn(self.point_B),
            FadeIn(self.label_B),
            run_time=0.5
        )
        
        # 问题提示
        question = Text(
            "当两直线平行时，\n截线形成的角有什么关系？",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_corresponding_angles(self):
        """场景2: 同位角相等"""
        # 标题
        title = Text(
            "同位角相等",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        definition = Text(
            "两直线平行 → 同位角相等",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 创建同位角标记 - 使用精确的几何计算
        # 以点A为中心的左上角角
        arc_radius = 0.5
        
        # 计算截线和上线在点A处的角度
        upper_line_left = Line(self.intersection1 + LEFT*0.5, self.intersection1)
        transversal_part1 = Line(self.transversal_start, self.intersection1)
        
        # 使用Angle.from_three_points创建角度
        # 对于左上角的同位角，我们考虑从水平线向右，再到截线向下
        point_on_upper_line = self.intersection1 + RIGHT * 0.5
        point_on_transversal = self.transversal_start
        
        # 创建第一个同位角
        self.corner_angle1 = Angle(
            Line(self.intersection1, point_on_upper_line),
            Line(self.intersection1, point_on_transversal),
            radius=arc_radius * 0.8,
            quadrant=(-1, -1),  # 左下角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 对于点B处的同位角，同样考虑从水平线向右，再到截线向下
        point_on_lower_line = self.intersection2 + RIGHT * 0.5
        point_on_transversal_B = self.transversal_end
        
        # 创建第二个同位角
        self.corner_angle2 = Angle(
            Line(self.intersection2, point_on_lower_line),
            Line(self.intersection2, point_on_transversal_B),
            radius=arc_radius * 0.8,
            quadrant=(-1, -1),  # 左下角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 显示两个同位角
        self.play(
            Create(self.corner_angle1),
            Create(self.corner_angle2),
            run_time=1.0
        )
        
        # 闪烁角度
        self.play(
            Flash(self.corner_angle1, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            Flash(self.corner_angle2, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            run_time=1.0
        )
        
        # 显示角度值和等式
        angle_value1 = MathTex(r"\alpha", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection1 + UL * 0.7)
        angle_value2 = MathTex(r"\alpha", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection2 + UL * 0.7)
        
        self.play(
            Write(angle_value1),
            Write(angle_value2),
            run_time=0.8
        )
        
        # 等式
        equation = Text(
            "同位角相等", 
            font="PingFang SC",
            color=self.COLOR_EQUAL,
            font_size=36
        ).move_to(DOWN * 4.5)
        self.play(Write(equation), run_time=0.8)
        
        # 强调相等关系
        equality = MathTex(
            r"\angle 1 = \angle 2", 
            color=self.COLOR_EQUAL,
            font_size=40
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equality), run_time=0.8)
        self.wait(1.5)
        
        # 保留图形，清理文字
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(equation),
            FadeOut(equality),
            FadeOut(angle_value1),
            FadeOut(angle_value2),
            run_time=0.5
        )
    
    def show_alternate_angles(self):
        """场景3: 内错角相等"""
        # 标题
        title = Text(
            "内错角相等",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        definition = Text(
            "两直线平行 → 内错角相等",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 隐藏之前的同位角
        self.play(
            FadeOut(self.corner_angle1),
            FadeOut(self.corner_angle2),
            run_time=0.3
        )
        
        # 创建内错角 - 位于截线两侧的内部角度
        arc_radius = 0.6
        
        # 左侧内错角：在点A处，上方平行线与截线形成的右侧角度
        # 在点A处的右下角
        self.alternate_angle1 = Angle(
            Line(self.intersection1, self.intersection1 + RIGHT * 0.5),  # 水平向右
            Line(self.intersection1, self.transversal_start),  # 斜向上
            radius=arc_radius * 0.8,
            quadrant=(1, -1),  # 右下角
            other_angle=True,  # 使用另一个角
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 在点B处的左上角（与上面的角相对）
        self.alternate_angle2 = Angle(
            Line(self.intersection2, self.intersection2 + LEFT * 0.5),  # 水平向左
            Line(self.intersection2, self.transversal_end),  # 斜向下
            radius=arc_radius * 0.8,
            quadrant=(-1, 1),  # 左上角
            other_angle=True,  # 使用另一个角
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 显示两个内错角
        self.play(
            Create(self.alternate_angle1),
            Create(self.alternate_angle2),
            run_time=1.0
        )
        
        # 闪烁角度
        self.play(
            Flash(self.alternate_angle1, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            Flash(self.alternate_angle2, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            run_time=1.0
        )
        
        # 显示角度值和等式
        angle_value1_alt = MathTex(r"\beta", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection1 + DR * 0.7)
        angle_value2_alt = MathTex(r"\beta", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection2 + UL * 0.7)
        
        self.play(
            Write(angle_value1_alt),
            Write(angle_value2_alt),
            run_time=0.8
        )
        
        # 等式
        equation_alt = Text(
            "内错角相等", 
            font="PingFang SC",
            color=self.COLOR_EQUAL,
            font_size=36
        ).move_to(DOWN * 4.5)
        self.play(Write(equation_alt), run_time=0.8)
        
        # 强调相等关系
        equality_alt = MathTex(
            r"\angle 3 = \angle 4", 
            color=self.COLOR_EQUAL,
            font_size=40
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equality_alt), run_time=0.8)
        self.wait(1.5)
        
        # 保留图形，清理文字
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(equation_alt),
            FadeOut(equality_alt),
            FadeOut(angle_value1_alt),
            FadeOut(angle_value2_alt),
            run_time=0.5
        )
    
    def show_co_interior_angles(self):
        """场景4: 同旁内角互补"""
        # 标题
        title = Text(
            "同旁内角互补",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        definition = Text(
            "两直线平行 → 同旁内角互补 (和为180°)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 隐藏之前的内错角
        self.play(
            FadeOut(self.alternate_angle1),
            FadeOut(self.alternate_angle2),
            run_time=0.3
        )
        
        # 创建同旁内角 - 位于截线同侧的内部角度
        arc_radius = 0.6
        
        # 在点A处的右侧内部角度（右上角）
        self.co_interior_angle1 = Angle(
            Line(self.intersection1, self.intersection1 + RIGHT * 0.5),  # 水平向右
            Line(self.intersection1, self.transversal_start),  # 斜向上
            radius=arc_radius * 0.8,
            quadrant=(1, 1),  # 右上角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 在点B处的左侧内部角度（左下角）
        self.co_interior_angle2 = Angle(
            Line(self.intersection2, self.intersection2 + LEFT * 0.5),  # 水平向左
            Line(self.intersection2, self.transversal_end),  # 斜向下
            radius=arc_radius * 0.8,
            quadrant=(-1, -1),  # 左下角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        # 显示两个同旁内角
        self.play(
            Create(self.co_interior_angle1),
            Create(self.co_interior_angle2),
            run_time=1.0
        )
        
        # 闪烁角度
        self.play(
            Flash(self.co_interior_angle1, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            Flash(self.co_interior_angle2, color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            run_time=1.0
        )
        
        # 显示角度值
        angle_gamma1 = MathTex(r"\gamma", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection1 + UR * 0.7)
        angle_gamma2 = MathTex(r"\delta", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection2 + DL * 0.7)
        
        self.play(
            Write(angle_gamma1),
            Write(angle_gamma2),
            run_time=0.8
        )
        
        # 显示互补关系
        complement_relation = Text(
            "同旁内角互补", 
            font="PingFang SC",
            color=self.COLOR_EQUAL,
            font_size=32
        ).move_to(DOWN * 4.5)
        self.play(Write(complement_relation), run_time=0.8)
        
        # 显示求和等于180度
        sum_equation = MathTex(
            r"\gamma + \delta = 180^\circ", 
            color=self.COLOR_EQUAL,
            font_size=40
        ).move_to(DOWN * 5.5)
        
        self.play(Write(sum_equation), run_time=0.8)
        
        # 动画展示两个角度拼成平角
        # 创建两个角的副本用于演示拼接
        gamma_copy = MathTex(r"\gamma", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(DOWN * 2 + LEFT * 2)
        plus_sign = MathTex("+", color=WHITE, font_size=40).next_to(gamma_copy, RIGHT, buff=0.3)
        delta_copy = MathTex(r"\delta", color=self.COLOR_HIGHLIGHT, font_size=32).next_to(plus_sign, RIGHT, buff=0.3)
        equals_sign = MathTex("=", color=WHITE, font_size=40).next_to(delta_copy, RIGHT, buff=0.3)
        straight_angle = MathTex(r"180^\circ", color=GREEN, font_size=40).next_to(equals_sign, RIGHT, buff=0.3)
        
        sum_display = VGroup(gamma_copy, plus_sign, delta_copy, equals_sign, straight_angle).move_to(DOWN * 2)
        
        self.play(
            ReplacementTransform(angle_gamma1.copy(), gamma_copy),
            ReplacementTransform(angle_gamma2.copy(), delta_copy),
            Write(plus_sign),
            Write(equals_sign),
            Write(straight_angle),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 保留图形，清理文字
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(complement_relation),
            FadeOut(sum_equation),
            FadeOut(sum_display),
            run_time=0.5
        )
    
    def dynamic_verification(self):
        """场景5: 动态验证"""
        # 标题
        title = Text(
            "动态验证",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        explanation = Text(
            "改变截线角度，性质依然成立",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(explanation), run_time=0.8)
        
        # 先恢复到原始状态，隐藏之前的角标记
        self.play(
            FadeOut(self.co_interior_angle1),
            FadeOut(self.co_interior_angle2),
            run_time=0.3
        )
        
        # 创建一个可以旋转的截线
        # 新的截线位置
        new_transversal_start = np.array([-2, 3, 0])
        new_transversal_end = np.array([2, -3, 0])
        
        new_transversal = Line(
            new_transversal_start,
            new_transversal_end,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        # 计算新的交点
        new_slope = (new_transversal_end[1] - new_transversal_start[1]) / (new_transversal_end[0] - new_transversal_start[0])
        new_intercept = new_transversal_start[1] - new_slope * new_transversal_start[0]
        
        new_intersection1_x = (self.line_y_pos_1 - new_intercept) / new_slope
        new_intersection1 = np.array([new_intersection1_x, self.line_y_pos_1, 0])
        
        new_intersection2_x = (self.line_y_pos_2 - new_intercept) / new_slope
        new_intersection2 = np.array([new_intersection2_x, self.line_y_pos_2, 0])
        
        # 变换到新截线
        self.play(
            Transform(self.transversal_line, new_transversal),
            Transform(self.point_A, Dot(new_intersection1, color=RED, radius=0.08)),
            Transform(self.label_A, Text("A", font="PingFang SC", font_size=20, color=RED).next_to(new_intersection1, UP, buff=0.1)),
            Transform(self.point_B, Dot(new_intersection2, color=RED, radius=0.08)),
            Transform(self.label_B, Text("B", font="PingFang SC", font_size=20, color=RED).next_to(new_intersection2, DOWN, buff=0.1)),
            run_time=1.5
        )
        
        # 更新当前交点
        self.intersection1 = new_intersection1
        self.intersection2 = new_intersection2
        
        # 显示新的同位角
        arc_radius = 0.5
        new_corner_angle1 = Angle(
            Line(self.intersection1, self.intersection1 + RIGHT * 0.5),
            Line(self.intersection1, new_transversal_start),
            radius=arc_radius * 0.8,
            quadrant=(1, 1),  # 右上角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        new_corner_angle2 = Angle(
            Line(self.intersection2, self.intersection2 + RIGHT * 0.5),
            Line(self.intersection2, new_transversal_end),
            radius=arc_radius * 0.8,
            quadrant=(1, 1),  # 右上角
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        self.play(
            Create(new_corner_angle1),
            Create(new_corner_angle2),
            run_time=1.0
        )
        
        # 显示角度值
        new_angle_value1 = MathTex(r"\alpha'", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection1 + UR * 0.7)
        new_angle_value2 = MathTex(r"\alpha'", color=self.COLOR_HIGHLIGHT, font_size=32).move_to(self.intersection2 + UR * 0.7)
        
        self.play(
            Write(new_angle_value1),
            Write(new_angle_value2),
            run_time=0.8
        )
        
        # 显示相等关系
        still_equal = Text(
            "同位角仍然相等!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 4.5)
        
        self.play(Write(still_equal), run_time=0.6)
        
        # 旋转截线到另一个位置
        newer_transversal_start = np.array([-3, 2, 0])
        newer_transversal_end = np.array([3, -2, 0])
        
        newer_transversal = Line(
            newer_transversal_start,
            newer_transversal_end,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        # 计算更新后的交点
        newer_slope = (newer_transversal_end[1] - newer_transversal_start[1]) / (newer_transversal_end[0] - newer_transversal_start[0])
        newer_intercept = newer_transversal_start[1] - newer_slope * newer_transversal_start[0]
        
        # 保存这些值以备后用
        self.newer_slope = newer_slope
        self.newer_intercept = newer_intercept
        self.last_transversal_start = newer_transversal_start
        self.last_transversal_end = newer_transversal_end
        newer_intersection1_x = (self.line_y_pos_1 - newer_intercept) / newer_slope
        newer_intersection1 = np.array([newer_intersection1_x, self.line_y_pos_1, 0])
        
        newer_intersection2_x = (self.line_y_pos_2 - newer_intercept) / newer_slope
        newer_intersection2 = np.array([newer_intersection2_x, self.line_y_pos_2, 0])
        
        self.play(
            Transform(self.transversal_line, newer_transversal),
            Transform(self.point_A, Dot(newer_intersection1, color=RED, radius=0.08)),
            Transform(self.label_A, Text("A", font="PingFang SC", font_size=20, color=RED).next_to(newer_intersection1, UP, buff=0.1)),
            Transform(self.point_B, Dot(newer_intersection2, color=RED, radius=0.08)),
            Transform(self.label_B, Text("B", font="PingFang SC", font_size=20, color=RED).next_to(newer_intersection2, DOWN, buff=0.1)),
            FadeOut(new_corner_angle1),
            FadeOut(new_corner_angle2),
            FadeOut(new_angle_value1),
            FadeOut(new_angle_value2),
            run_time=1.5
        )
        
        # 更新当前交点
        self.intersection1 = newer_intersection1
        self.intersection2 = newer_intersection2
        
        # 显示最终确认
        final_confirmation = Text(
            "无论截线如何变化，\n平行线性质始终成立！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 3)
        
        self.play(Write(final_confirmation), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(still_equal),
            FadeOut(final_confirmation),
            run_time=0.5
        )
    
    def compare_non_parallel(self):
        """场景6: 对比非平行线"""
        # 标题
        title = Text(
            "非平行线的情况",
            font="PingFang SC",
            font_size=36,
            color=RED
        ).move_to(UP * 6.5)
        
        explanation = Text(
            "如果不平行，这些性质还成立吗？",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(explanation), run_time=0.8)
        
        # 变换平行线为非平行线
        # 移动第二条线使其不再平行于第一条
        skewed_line2_start = np.array([-4, -2.0, 0])
        skewed_line2_end = np.array([4, 0.5, 0])
        
        skewed_line2 = Line(
            skewed_line2_start,
            skewed_line2_end,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        # 计算新的交点（因为第二条线不再是水平的）
        # 第二条线的新斜率和截距
        skewed_slope = (skewed_line2_end[1] - skewed_line2_start[1]) / (skewed_line2_end[0] - skewed_line2_start[0])
        skewed_intercept = skewed_line2_start[1] - skewed_slope * skewed_line2_start[0]
        
        # 新的交点
        # 新的交点 - 用当前截线参数
        current_transversal_start = self.last_transversal_start
        current_transversal_end = self.last_transversal_end
        
        # 重新计算当前截线的斜率和截距
        current_slope = (current_transversal_end[1] - current_transversal_start[1]) / (current_transversal_end[0] - current_transversal_start[0])
        current_intercept = current_transversal_start[1] - current_slope * current_transversal_start[0]
        
        new_int2_x = (current_intercept - skewed_intercept) / (skewed_slope - current_slope)
        new_int2_y = skewed_slope * new_int2_x + skewed_intercept
        new_intersection2_skewed = np.array([new_int2_x, new_int2_y, 0])
        
        self.play(
            Transform(self.parallel_line2, skewed_line2),
            Transform(self.point_B, Dot(new_intersection2_skewed, color=RED, radius=0.08)),
            Transform(self.label_B, Text("B", font="PingFang SC", font_size=20, color=RED).next_to(new_intersection2_skewed, DOWN, buff=0.1)),
            run_time=1.5
        )
        
        # 显示同位角（现在不相等）
        non_parallel_angle1 = Angle(
            Line(self.intersection1, self.intersection1 + RIGHT * 0.5),
            Line(self.intersection1, self.last_transversal_start),
            radius=0.5,
            quadrant=(1, 1),
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        non_parallel_angle2 = Angle(
            Line(new_intersection2_skewed, new_intersection2_skewed + RIGHT * 0.5),
            Line(new_intersection2_skewed, self.last_transversal_end),
            radius=0.5,
            quadrant=(1, 1),
            other_angle=False,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        
        self.play(
            Create(non_parallel_angle1),
            Create(non_parallel_angle2),
            run_time=1.0
        )
        
        # 显示不等符号
        not_equal = MathTex(r"\neq", color=RED, font_size=40).move_to((self.intersection1 + new_intersection2_skewed)/2 + RIGHT * 0.5)
        
        self.play(Write(not_equal), run_time=0.6)
        
        # 解释文本
        explanation2 = Text(
            "非平行线时，同位角不相等！",
            font="PingFang SC",
            font_size=24,
            color=RED
        ).move_to(DOWN * 4.5)
        
        self.play(Write(explanation2), run_time=0.6)
        
        # 恢复平行线
        self.play(
            Transform(self.parallel_line2, Line(self.line2_start, self.line2_end, color=self.COLOR_PRIMARY, stroke_width=4)),
            Transform(self.point_B, Dot(self.intersection2, color=RED, radius=0.08)),
            Transform(self.label_B, Text("B", font="PingFang SC", font_size=20, color=RED).next_to(self.intersection2, DOWN, buff=0.1)),
            FadeOut(non_parallel_angle1),
            FadeOut(non_parallel_angle2),
            FadeOut(not_equal),
            FadeOut(explanation2),
            run_time=1.5
        )
        
        # 强调条件
        condition = Text(
            "重要条件：两直线必须平行！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 4.5)
        
        self.play(Write(condition), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(condition),
            run_time=0.5
        )
    
    def summary_review(self):
        """场景7: 总结回顾"""
        # 标题
        title = Text(
            "总结：平行线的性质",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 展示三个性质卡片
        property1 = self.create_property_card(
            "同位角相等",
            "两直线平行 ⟹ 同位角相等",
            self.COLOR_HIGHLIGHT,
            UP * 2
        )
        
        property2 = self.create_property_card(
            "内错角相等", 
            "两直线平行 ⟹ 内错角相等",
            self.COLOR_HIGHLIGHT,
            ORIGIN
        )
        
        property3 = self.create_property_card(
            "同旁内角互补",
            "两直线平行 ⟹ 同旁内角互补",
            self.COLOR_HIGHLIGHT,
            DOWN * 2
        )
        
        properties = VGroup(property1, property2, property3)
        
        # 卡片依次出现
        self.play(FadeIn(property1), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(property2), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(property3), run_time=0.8)
        self.wait(1.0)
        
        # 最终强调
        emphasis = Text(
            "记住：由线的关系推断角的关系",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 5)
        
        self.play(Write(emphasis), run_time=0.6)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property1),
            FadeOut(property2),
            FadeOut(property3),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def create_property_card(self, title, content, color, position):
        """创建性质卡片"""
        # 卡片背景
        card_bg = Rectangle(
            width=6,
            height=1.2,
            color=color,
            fill_color=color,
            fill_opacity=0.2,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=24,
            color=color
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=18,
            color=WHITE
        )
        
        # 组合
        card_content = VGroup(title_text, content_text).arrange(DOWN, buff=0.2)
        card = VGroup(card_bg, card_content).move_to(position)
        
        # 初始位置在屏幕外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何知识!",
            font="PingFang SC",
            font_size=30,
            color="#f1c40f"
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 几何图案装饰
        # 平行线图标
        parallel_icons = VGroup(
            Line(LEFT*0.5, RIGHT*0.5, color=self.COLOR_PRIMARY, stroke_width=4),
            Line(LEFT*0.5, RIGHT*0.5, color=self.COLOR_PRIMARY, stroke_width=4).shift(DOWN*0.3)
        ).move_to(DOWN * 2.5)
        
        self.play(Create(parallel_icons), run_time=0.6)
        
        # 旋转动画
        self.play(Rotate(parallel_icons, angle=PI, run_time=1.5))
        
        self.wait(1)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(parallel_icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql parallel_lines_properties.py ParallelLinesProperties  # 快速预览
# manim -qh parallel_lines_properties.py ParallelLinesProperties   # 高质量