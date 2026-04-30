"""
对顶角与邻补角 - Vertical Angles and Adjacent Supplementary Angles
使用 Manim 创建的七年级几何教学视频

内容: 两条直线相交形成的角度关系 - 对顶角与邻补角
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from math import atan2, degrees


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class VerticalAndAdjacentAngles(Scene):
    """
    对顶角与邻补角教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 认识相交线
    3. 对顶角概念
    4. 邻补角概念
    5. 数值示例
    6. 知识总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_LINE_1 = "#3498db"        # 蓝色 - 直线1
        self.COLOR_LINE_2 = "#e74c3c"        # 红色 - 直线2
        self.COLOR_ANGLE_1 = "#f39c12"       # 橙色 - 角1
        self.COLOR_ANGLE_2 = "#2ecc71"       # 绿色 - 角2
        self.COLOR_ANGLE_3 = "#9b59b6"       # 紫色 - 角3
        self.COLOR_ANGLE_4 = "#e67e22"       # 深橙 - 角4
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_intersecting_lines()
        self.show_vertical_angles()
        self.show_adjacent_angles()
        self.show_numerical_example()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化相交线和所有角度元素"""
        # 交点位置 (主内容区域中心)
        self.O = np.array([0, 1.5, 0])
        
        # 直线1: 从左下到右上 (约30度角)
        angle_1 = 30 * DEGREES
        length = 5.0
        self.line1_direction = np.array([np.cos(angle_1), np.sin(angle_1), 0])
        self.line1_start = self.O - self.line1_direction * length / 2
        self.line1_end = self.O + self.line1_direction * length / 2
        
        # 直线2: 从左上到右下 (约-40度角)
        angle_2 = -40 * DEGREES
        self.line2_direction = np.array([np.cos(angle_2), np.sin(angle_2), 0])
        self.line2_start = self.O - self.line2_direction * length / 2
        self.line2_end = self.O + self.line2_direction * length / 2
        
        # 计算四个角的方向向量 (用于绘制角度弧线)
        # 角1: 直线1的正方向 到 直线2的正方向
        # 角2: 直线2的正方向 到 直线1的负方向
        # 角3: 直线1的负方向 到 直线2的负方向
        # 角4: 直线2的负方向 到 直线1的正方向
        
        self.angle_1_start = self.line1_direction
        self.angle_1_end = self.line2_direction
        
        self.angle_2_start = self.line2_direction
        self.angle_2_end = -self.line1_direction
        
        self.angle_3_start = -self.line1_direction
        self.angle_3_end = -self.line2_direction
        
        self.angle_4_start = -self.line2_direction
        self.angle_4_end = self.line1_direction
        
        # 计算角度值 (用于标注)
        self.angle_1_value = self.calculate_angle_between(self.angle_1_start, self.angle_1_end)
        self.angle_2_value = 180 - self.angle_1_value  # 邻补角
        self.angle_3_value = self.angle_1_value  # 对顶角
        self.angle_4_value = self.angle_2_value  # 对顶角
        
        # 验证几何关系
        self.verify_geometry()
        
        print(f"✓ 几何初始化完成")
        print(f"  角1: {self.angle_1_value:.1f}°")
        print(f"  角2: {self.angle_2_value:.1f}°")
        print(f"  角3: {self.angle_3_value:.1f}°")
        print(f"  角4: {self.angle_4_value:.1f}°")
    
    def calculate_angle_between(self, vec1, vec2):
        """计算两个向量之间的角度 (度数，0-180)"""
        # 使用atan2计算角度
        angle1 = atan2(vec1[1], vec1[0])
        angle2 = atan2(vec2[1], vec2[0])
        
        # 计算差值
        diff = angle2 - angle1
        
        # 归一化到[0, 2π)
        while diff < 0:
            diff += 2 * PI
        while diff >= 2 * PI:
            diff -= 2 * PI
        
        # 如果大于π，取补角
        if diff > PI:
            diff = 2 * PI - diff
        
        # 转换为度数
        return degrees(diff)
    
    def verify_geometry(self):
        """验证几何关系的正确性"""
        epsilon = 1.0  # 度数误差容限
        
        # 验证对顶角相等
        assert abs(self.angle_1_value - self.angle_3_value) < epsilon, \
            f"对顶角不相等! ∠1={self.angle_1_value:.1f}°, ∠3={self.angle_3_value:.1f}°"
        
        assert abs(self.angle_2_value - self.angle_4_value) < epsilon, \
            f"对顶角不相等! ∠2={self.angle_2_value:.1f}°, ∠4={self.angle_4_value:.1f}°"
        
        # 验证邻补角互补
        assert abs(self.angle_1_value + self.angle_2_value - 180) < epsilon, \
            f"邻补角不互补! ∠1+∠2={self.angle_1_value + self.angle_2_value:.1f}°"
        
        print("✓ 几何验证通过")
    
    def create_angle_arc(self, center, start_vec, end_vec, radius=0.5, color=WHITE):
        """创建角度弧线
        
        参数:
            center: 角的顶点
            start_vec: 起始方向向量
            end_vec: 终止方向向量
            radius: 弧线半径
            color: 颜色
        """
        # 计算起始和终止角度
        start_angle = atan2(start_vec[1], start_vec[0])
        end_angle = atan2(end_vec[1], end_vec[0])
        
        # 确保逆时针方向
        if end_angle < start_angle:
            end_angle += 2 * PI
        
        # 创建弧线
        arc = Arc(
            radius=radius,
            start_angle=start_angle,
            angle=end_angle - start_angle,
            color=color,
            stroke_width=3
        ).move_arc_center_to(center)
        
        return arc
    
    def get_angle_label_position(self, center, start_vec, end_vec, distance=0.7):
        """计算角度标签的位置 (在角平分线方向)"""
        # 归一化向量
        v1 = start_vec / np.linalg.norm(start_vec)
        v2 = end_vec / np.linalg.norm(end_vec)
        
        # 角平分线方向
        bisector = v1 + v2
        
        # 如果接近180度，向量和为0
        if np.linalg.norm(bisector) < 0.1:
            # 使用垂直于起始向量的方向
            bisector = np.array([-v1[1], v1[0], 0])
        
        bisector = bisector / np.linalg.norm(bisector)
        
        return center + bisector * distance
    
    def show_opening(self):
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
        hook_text = Text(
            "两条直线相交\n会形成什么有趣的角度关系?",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.5)
        
        # 两条线快速交叉
        line1_preview = Line(
            self.line1_start,
            self.line1_end,
            color=self.COLOR_LINE_1,
            stroke_width=4
        )
        
        line2_preview = Line(
            self.line2_start,
            self.line2_end,
            color=self.COLOR_LINE_2,
            stroke_width=4
        )
        
        self.play(
            Create(line1_preview),
            Create(line2_preview),
            run_time=1.0
        )
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.3)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.8), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.5
        )
        
        # 保留直线
        self.line1 = line1_preview
        self.line2 = line2_preview
    
    def show_intersecting_lines(self):
        """场景2: 认识相交线"""
        # 标题
        title = Text(
            "相交线与角",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记交点O
        dot_O = Dot(self.O, color=YELLOW, radius=0.08)
        label_O = Text(
            "O",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(dot_O, DOWN + LEFT, buff=0.15)
        
        self.play(
            FadeIn(dot_O, scale=0.5),
            FadeIn(label_O),
            run_time=0.5
        )
        
        # 依次标注四个角
        # 角1
        self.angle_1_arc = self.create_angle_arc(
            self.O,
            self.angle_1_start,
            self.angle_1_end,
            radius=0.6,
            color=self.COLOR_ANGLE_1
        )
        
        angle_1_label_pos = self.get_angle_label_position(
            self.O,
            self.angle_1_start,
            self.angle_1_end,
            distance=0.9
        )
        
        self.angle_1_label = MathTex(
            r"\angle 1",
            font_size=28,
            color=self.COLOR_ANGLE_1
        ).move_to(angle_1_label_pos)
        
        self.play(
            Create(self.angle_1_arc),
            FadeIn(self.angle_1_label),
            run_time=0.7
        )
        
        # 角2
        self.angle_2_arc = self.create_angle_arc(
            self.O,
            self.angle_2_start,
            self.angle_2_end,
            radius=0.6,
            color=self.COLOR_ANGLE_2
        )
        
        angle_2_label_pos = self.get_angle_label_position(
            self.O,
            self.angle_2_start,
            self.angle_2_end,
            distance=0.9
        )
        
        self.angle_2_label = MathTex(
            r"\angle 2",
            font_size=28,
            color=self.COLOR_ANGLE_2
        ).move_to(angle_2_label_pos)
        
        self.play(
            Create(self.angle_2_arc),
            FadeIn(self.angle_2_label),
            run_time=0.7
        )
        
        # 角3
        self.angle_3_arc = self.create_angle_arc(
            self.O,
            self.angle_3_start,
            self.angle_3_end,
            radius=0.6,
            color=self.COLOR_ANGLE_3
        )
        
        angle_3_label_pos = self.get_angle_label_position(
            self.O,
            self.angle_3_start,
            self.angle_3_end,
            distance=0.9
        )
        
        self.angle_3_label = MathTex(
            r"\angle 3",
            font_size=28,
            color=self.COLOR_ANGLE_3
        ).move_to(angle_3_label_pos)
        
        self.play(
            Create(self.angle_3_arc),
            FadeIn(self.angle_3_label),
            run_time=0.7
        )
        
        # 角4
        self.angle_4_arc = self.create_angle_arc(
            self.O,
            self.angle_4_start,
            self.angle_4_end,
            radius=0.6,
            color=self.COLOR_ANGLE_4
        )
        
        angle_4_label_pos = self.get_angle_label_position(
            self.O,
            self.angle_4_start,
            self.angle_4_end,
            distance=0.9
        )
        
        self.angle_4_label = MathTex(
            r"\angle 4",
            font_size=28,
            color=self.COLOR_ANGLE_4
        ).move_to(angle_4_label_pos)
        
        self.play(
            Create(self.angle_4_arc),
            FadeIn(self.angle_4_label),
            run_time=0.7
        )
        
        # 说明文字
        explanation = Text(
            "两条直线相交，形成四个角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(dot_O),
            FadeOut(label_O),
            run_time=0.5
        )
    
    def show_vertical_angles(self):
        """场景3: 对顶角概念"""
        # 标题
        title = Text(
            "对顶角",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "有公共顶点，但没有公共边",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(definition), run_time=0.8)
        
        # 高亮角1和角3
        self.play(
            self.angle_1_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_1_label.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.play(
            self.angle_3_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_3_label.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        # 闪烁效果
        self.play(
            Flash(self.angle_1_arc, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            Flash(self.angle_3_arc, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=0.8
        )
        
        # 说明
        explain_1 = Text(
            "∠1 和 ∠3 是对顶角",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explain_1), run_time=0.6)
        self.wait(1.2)
        
        # 性质
        property_text = Text(
            "对顶角相等!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(property_text, scale=1.2), run_time=0.8)
        
        # 等式
        equation_1 = MathTex(
            r"\angle 1 = \angle 3",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equation_1), run_time=0.8)
        self.wait(1.5)
        
        # 恢复角1和角3的颜色
        self.play(
            self.angle_1_arc.animate.set_stroke(color=self.COLOR_ANGLE_1, width=3),
            self.angle_1_label.animate.set_color(self.COLOR_ANGLE_1),
            self.angle_3_arc.animate.set_stroke(color=self.COLOR_ANGLE_3, width=3),
            self.angle_3_label.animate.set_color(self.COLOR_ANGLE_3),
            FadeOut(explain_1),
            run_time=0.5
        )
        
        # 同样展示角2和角4
        self.play(
            self.angle_2_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_2_label.animate.set_color(self.COLOR_HIGHLIGHT),
            self.angle_4_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_4_label.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.play(
            Flash(self.angle_2_arc, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            Flash(self.angle_4_arc, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=0.8
        )
        
        # 等式2
        equation_2 = MathTex(
            r"\angle 2 = \angle 4",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 6.3)
        
        self.play(Write(equation_2), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(property_text),
            FadeOut(equation_1),
            FadeOut(equation_2),
            run_time=0.6
        )
        
        # 恢复所有颜色
        self.play(
            self.angle_2_arc.animate.set_stroke(color=self.COLOR_ANGLE_2, width=3),
            self.angle_2_label.animate.set_color(self.COLOR_ANGLE_2),
            self.angle_4_arc.animate.set_stroke(color=self.COLOR_ANGLE_4, width=3),
            self.angle_4_label.animate.set_color(self.COLOR_ANGLE_4),
            run_time=0.3
        )
    
    def show_adjacent_angles(self):
        """场景4: 邻补角概念"""
        # 标题
        title = Text(
            "邻补角",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "有公共顶点和一条公共边",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(definition), run_time=0.8)
        
        # 高亮角1和角2
        self.play(
            self.angle_1_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_1_label.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.play(
            self.angle_2_arc.animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.angle_2_label.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        # 标记公共边 (直线2的正方向部分)
        common_edge_end = self.O + self.line2_direction * 1.5
        common_edge = Line(
            self.O,
            common_edge_end,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=8
        )
        
        self.play(Create(common_edge), run_time=0.8)
        
        # 说明
        explain_1 = Text(
            "∠1 和 ∠2 是邻补角",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explain_1), run_time=0.6)
        self.wait(1.5)
        
        # 性质
        property_text = Text(
            "邻补角互补 (和为180°)!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(property_text, scale=1.2), run_time=0.8)
        
        # 等式
        equation = MathTex(
            r"\angle 1 + \angle 2 = 180^\circ",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equation), run_time=0.8)
        self.wait(1.0)
        
        # 平角动画展示
        # 创建一个从角1起始方向到角2终止方向的大弧线 (180度)
        straight_angle_start = self.angle_1_start
        straight_angle_end = self.angle_2_end
        
        straight_arc = self.create_angle_arc(
            self.O,
            straight_angle_start,
            straight_angle_end,
            radius=1.0,
            color=GOLD
        )
        
        self.play(
            Create(straight_arc),
            run_time=1.2
        )
        
        straight_label = MathTex(
            r"180^\circ",
            font_size=32,
            color=GOLD
        ).move_to(self.O + UP * 1.5)
        
        self.play(FadeIn(straight_label), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(property_text),
            FadeOut(equation),
            FadeOut(common_edge),
            FadeOut(straight_arc),
            FadeOut(straight_label),
            FadeOut(explain_1),
            run_time=0.6
        )
        
        # 恢复颜色
        self.play(
            self.angle_1_arc.animate.set_stroke(color=self.COLOR_ANGLE_1, width=3),
            self.angle_1_label.animate.set_color(self.COLOR_ANGLE_1),
            self.angle_2_arc.animate.set_stroke(color=self.COLOR_ANGLE_2, width=3),
            self.angle_2_label.animate.set_color(self.COLOR_ANGLE_2),
            run_time=0.3
        )
    
    def show_numerical_example(self):
        """场景5: 数值示例"""
        # 标题
        title = Text(
            "实例验证",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 假设条件
        assumption_text = Text(
            "假设",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        )
        
        assumption_math = MathTex(
            r"\angle 1 = 60^\circ",
            font_size=32,
            color=self.COLOR_ANGLE_1
        )
        
        assumption = VGroup(assumption_text, assumption_math).arrange(RIGHT, buff=0.3).move_to(UP * 4.7)
        
        self.play(FadeIn(assumption), run_time=0.7)
        
        # 标注角1 = 60°
        value_1 = MathTex(
            r"60^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_1
        ).next_to(self.angle_1_label, RIGHT, buff=0.2)
        
        self.play(
            self.angle_1_arc.animate.set_stroke(width=5),
            FadeIn(value_1, scale=0.8),
            run_time=0.7
        )
        
        # 推导角3 (对顶角)
        deduction_3_text = Text(
            "对顶角:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        
        deduction_3_math = MathTex(
            r"\angle 3 = \angle 1 = 60^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_3
        )
        
        deduction_3 = VGroup(deduction_3_text, deduction_3_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)
        
        self.play(FadeIn(deduction_3), run_time=0.8)
        
        # 标注角3 = 60°
        value_3 = MathTex(
            r"60^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_3
        ).next_to(self.angle_3_label, LEFT, buff=0.2)
        
        self.play(
            self.angle_3_arc.animate.set_stroke(width=5),
            FadeIn(value_3, scale=0.8),
            run_time=0.7
        )
        
        self.wait(0.5)
        self.play(FadeOut(deduction_3), run_time=0.3)
        
        # 推导角2 (邻补角)
        deduction_2_text = Text(
            "邻补角:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        
        deduction_2_math = MathTex(
            r"\angle 2 = 180^\circ - 60^\circ = 120^\circ",
            font_size=26,
            color=self.COLOR_ANGLE_2
        )
        
        deduction_2 = VGroup(deduction_2_text, deduction_2_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.3)
        
        self.play(FadeIn(deduction_2), run_time=1.0)
        
        # 标注角2 = 120°
        value_2 = MathTex(
            r"120^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_2
        ).next_to(self.angle_2_label, DOWN, buff=0.2)
        
        self.play(
            self.angle_2_arc.animate.set_stroke(width=5),
            FadeIn(value_2, scale=0.8),
            run_time=0.7
        )
        
        self.wait(0.5)
        self.play(FadeOut(deduction_2), run_time=0.3)
        
        # 推导角4 (对顶角)
        deduction_4_text = Text(
            "对顶角:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        
        deduction_4_math = MathTex(
            r"\angle 4 = \angle 2 = 120^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_4
        )
        
        deduction_4 = VGroup(deduction_4_text, deduction_4_math).arrange(RIGHT, buff=0.2).move_to(DOWN * 5.2)
        
        self.play(FadeIn(deduction_4), run_time=0.8)
        
        # 标注角4 = 120°
        value_4 = MathTex(
            r"120^\circ",
            font_size=28,
            color=self.COLOR_ANGLE_4
        ).next_to(self.angle_4_label, UP, buff=0.2)
        
        self.play(
            self.angle_4_arc.animate.set_stroke(width=5),
            FadeIn(value_4, scale=0.8),
            run_time=0.7
        )
        
        self.wait(0.5)
        self.play(FadeOut(deduction_4), run_time=0.3)
        
        # 验证
        verification_text = Text(
            "验证:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        )
        
        verification_math = MathTex(
            r"60^\circ + 120^\circ = 180^\circ",
            font_size=28,
            color=WHITE
        )
        
        check_mark = Text(
            "✓",
            font_size=36,
            color=GREEN
        )
        
        verification = VGroup(
            verification_text,
            verification_math,
            check_mark
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 6)
        
        self.play(FadeIn(verification, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(assumption),
            FadeOut(value_1),
            FadeOut(value_2),
            FadeOut(value_3),
            FadeOut(value_4),
            FadeOut(verification),
            run_time=0.6
        )
        
        # 恢复角度弧线粗细
        self.play(
            self.angle_1_arc.animate.set_stroke(width=3),
            self.angle_2_arc.animate.set_stroke(width=3),
            self.angle_3_arc.animate.set_stroke(width=3),
            self.angle_4_arc.animate.set_stroke(width=3),
            run_time=0.3
        )
    
    def show_summary(self):
        """场景6: 知识总结"""
        # 标题
        title = Text(
            "知识要点",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 相交线和角缩小并上移
        all_angles = VGroup(
            self.line1,
            self.line2,
            self.angle_1_arc,
            self.angle_2_arc,
            self.angle_3_arc,
            self.angle_4_arc,
            self.angle_1_label,
            self.angle_2_label,
            self.angle_3_label,
            self.angle_4_label
        )
        
        self.play(
            all_angles.animate.scale(0.7).move_to(UP * 3.5),
            run_time=0.8
        )
        
        # 知识卡片1: 对顶角
        card_1_title = Text(
            "对顶角",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        
        card_1_content = Text(
            "相等",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        card_1_formula = MathTex(
            r"\angle 1 = \angle 3, \quad \angle 2 = \angle 4",
            font_size=24,
            color=GRAY_A
        )
        
        card_1 = VGroup(
            card_1_title,
            card_1_content,
            card_1_formula
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(UP * 0.8 + LEFT * 10)
        
        # 背景框
        card_1_bg = SurroundingRectangle(
            card_1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1,
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=self.COLOR_HIGHLIGHT
        )
        
        card_1_group = VGroup(card_1_bg, card_1)
        
        self.play(card_1_group.animate.move_to(UP * 0.8), run_time=0.8)
        
        # 知识卡片2: 邻补角
        card_2_title = Text(
            "邻补角",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        
        card_2_content = Text(
            "互补 (和为180°)",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        card_2_formula = MathTex(
            r"\angle 1 + \angle 2 = 180^\circ",
            font_size=24,
            color=GRAY_A
        )
        
        card_2 = VGroup(
            card_2_title,
            card_2_content,
            card_2_formula
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 1.5 + LEFT * 10)
        
        card_2_bg = SurroundingRectangle(
            card_2,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1,
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=self.COLOR_HIGHLIGHT
        )
        
        card_2_group = VGroup(card_2_bg, card_2)
        
        self.play(card_2_group.animate.move_to(DOWN * 1.5), run_time=0.8)
        
        # 图标闪烁
        self.play(
            Flash(all_angles, color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.8
        )
        
        # 应用提示
        tip = Text(
            "解题利器: 由一角求其他角!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(tip, shift=UP * 0.3), run_time=0.6)
        
        self.wait(3.0)
        
        # 清理所有
        self.play(
            FadeOut(title),
            FadeOut(all_angles),
            FadeOut(card_1_group),
            FadeOut(card_2_group),
            FadeOut(tip),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
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
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 角度图标装饰
        angle_icons = VGroup()
        
        for i in range(4):
            angle = i * 90 * DEGREES
            icon = VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=self.COLOR_HIGHLIGHT),
                Line(ORIGIN, UP * 0.4, color=self.COLOR_HIGHLIGHT),
                Arc(
                    radius=0.15,
                    start_angle=0,
                    angle=PI / 2,
                    color=self.COLOR_HIGHLIGHT
                )
            ).rotate(angle)
            
            pos = 2.5 * np.array([np.cos(angle + PI / 4), np.sin(angle + PI / 4), 0])
            icon.move_to(pos)
            angle_icons.add(icon)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in angle_icons],
            run_time=0.8
        )
        
        self.play(
            Rotate(angle_icons, angle=2 * PI, run_time=2.0, rate_func=linear)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(angle_icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql vertical_and_adjacent_angles.py VerticalAndAdjacentAngles  # 快速预览
# manim -qh vertical_and_adjacent_angles.py VerticalAndAdjacentAngles   # 高质量渲染 (1080×1920)