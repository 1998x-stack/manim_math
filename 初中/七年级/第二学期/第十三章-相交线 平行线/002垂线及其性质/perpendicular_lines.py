"""
垂线及其性质 - Perpendicular Lines and Their Properties
使用 Manim 创建的中学几何教学视频

内容: 垂线定义、唯一性性质、最短距离性质
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


class PerpendicularLines(Scene):
    """
    垂线及其性质教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 垂线定义
    3. 性质1: 唯一性
    4. 性质2: 最短距离
    5. 实际应用示例
    6. 知识总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主直线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 垂线
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调元素
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        self.COLOR_RIGHT_ANGLE = "#2ecc71"   # 绿色 - 直角标记
        self.COLOR_DISTANCE = "#f39c12"      # 橙色 - 距离相关
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_uniqueness()
        self.show_shortest_distance()
        self.show_application()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 主直线l - 水平线
        self.line_l_start = np.array([-3.5, 0, 0])
        self.line_l_end = np.array([3.5, 0, 0])
        
        # 点P (在直线上方)
        self.P = np.array([-1.5, 2.5, 0])
        
        # 垂足H (P在直线l上的投影)
        self.H = np.array([self.P[0], 0, 0])
        
        # 点Q (另一个示例点)
        self.Q = np.array([1.8, 2.8, 0])
        
        # 垂足K (Q在直线l上的投影)
        self.K = np.array([self.Q[0], 0, 0])
        
        # 用于距离对比的点
        self.A = np.array([0.8, 0, 0])
        self.B = np.array([-3.2, 0, 0])
        
        # 计算距离
        self.dist_PH = np.linalg.norm(self.P - self.H)
        self.dist_PA = np.linalg.norm(self.P - self.A)
        self.dist_PB = np.linalg.norm(self.P - self.B)
        self.dist_QK = np.linalg.norm(self.Q - self.K)
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证垂直性: PH ⊥ l
        vec_l = self.line_l_end - self.line_l_start
        vec_PH = self.H - self.P
        dot_product = np.dot(vec_l[:2], vec_PH[:2])
        
        if abs(dot_product) > epsilon:
            print(f"WARNING: PH不垂直于l! 点积 = {dot_product:.6f}")
        
        # 验证H在直线l上
        if abs(self.H[1]) > epsilon:
            print(f"WARNING: H不在直线l上! y = {self.H[1]:.6f}")
        
        # 验证距离关系: PH < PA 且 PH < PB
        if not (self.dist_PH < self.dist_PA and self.dist_PH < self.dist_PB):
            print(f"WARNING: 距离关系不正确!")
            print(f"PH = {self.dist_PH:.3f}, PA = {self.dist_PA:.3f}, PB = {self.dist_PB:.3f}")
        
        # 检查边界
        for name, point in [("P", self.P), ("Q", self.Q), ("H", self.H), ("K", self.K)]:
            if not (-4.0 <= point[0] <= 4.0 and -7.5 <= point[1] <= 7.5):
                print(f"WARNING: 点{name}超出安全边界! {point}")
        
        print("✓ 几何验证完成")
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.25):
        """创建直角标记符号"""
        # 计算两个方向的单位向量
        vec1 = (point1 - corner)
        vec1_unit = vec1 / np.linalg.norm(vec1) * size
        
        vec2 = (point2 - corner)
        vec2_unit = vec2 / np.linalg.norm(vec2) * size
        
        # 创建直角标记的小正方形
        square = Polygon(
            corner,
            corner + vec1_unit,
            corner + vec1_unit + vec2_unit,
            corner + vec2_unit,
            color=self.COLOR_RIGHT_ANGLE,
            stroke_width=2.5,
            fill_opacity=0
        )
        return square
    
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
            "什么是垂线?\n它有什么神奇性质?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.3)
        
        # 简单示意图 - 两条相交直线
        line1 = Line([-1, 1, 0], [1, 1, 0], color=self.COLOR_PRIMARY, stroke_width=4)
        line2 = Line([0, 0, 0], [0, 2, 0], color=self.COLOR_SECONDARY, stroke_width=4)
        
        self.play(Create(line1), Create(line2), run_time=0.6)
        
        # 直角符号闪现
        right_angle_intro = self.create_right_angle_mark(
            np.array([0, 1, 0]), 
            np.array([1, 1, 0]), 
            np.array([0, 2, 0]),
            size=0.3
        )
        
        self.play(FadeIn(right_angle_intro, scale=0.5), run_time=0.4)
        self.play(Flash(right_angle_intro, color=self.COLOR_RIGHT_ANGLE, flash_radius=0.4), run_time=0.3)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(right_angle_intro),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 垂线定义"""
        # 标题
        title = Text(
            "垂线的定义",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 绘制主直线l
        self.line_l = Line(
            self.line_l_start,
            self.line_l_end,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        label_l = Text(
            "l",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(self.line_l, RIGHT, buff=0.2)
        
        self.play(Create(self.line_l), run_time=0.8)
        self.play(FadeIn(label_l), run_time=0.2)
        
        # 点P出现
        self.dot_P = Dot(self.P, color=self.COLOR_SECONDARY, radius=0.08)
        self.label_P = Text(
            "P",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(self.dot_P, UP, buff=0.15)
        
        self.play(FadeIn(self.dot_P, scale=0.5), run_time=0.3)
        self.play(FadeIn(self.label_P), run_time=0.2)
        
        self.wait(0.3)
        
        # 垂线PH绘制
        self.perpendicular = Line(
            self.P,
            self.H,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(self.perpendicular), run_time=1.0)
        
        # 垂足H
        self.dot_H = Dot(self.H, color=self.COLOR_AUXILIARY, radius=0.07)
        self.label_H = Text(
            "H",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(self.dot_H, DOWN, buff=0.15)
        
        self.play(
            FadeIn(self.dot_H),
            FadeIn(self.label_H),
            run_time=0.3
        )
        
        # 直角标记
        self.right_angle_mark = self.create_right_angle_mark(
            self.H,
            self.P,
            self.line_l_end
        )
        
        self.play(FadeIn(self.right_angle_mark), run_time=0.4)
        self.play(Flash(self.right_angle_mark, color=self.COLOR_RIGHT_ANGLE, flash_radius=0.3), run_time=0.3)
        
        # 定义文字
        definition = Text(
            "两条直线相交成直角时,\n称这两条直线互相垂直",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(DOWN * 3.5)
        
        self.play(Write(definition), run_time=1.5)
        
        # 符号表示
        symbol_chinese = Text("记作:", font="PingFang SC", font_size=22, color=GRAY_A)
        symbol_math = MathTex(r"l \perp PH", font_size=32, color=WHITE)
        symbol_group = VGroup(symbol_chinese, symbol_math).arrange(RIGHT, buff=0.3)
        symbol_group.move_to(DOWN * 5)
        
        self.play(Write(symbol_group), run_time=0.8)
        
        # 说明垂足
        footnote = Text(
            "H 叫做垂足",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(footnote), run_time=0.4)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(symbol_group),
            FadeOut(footnote),
            FadeOut(label_l),
            run_time=0.6
        )
    
    def show_uniqueness(self):
        """场景3: 性质1 - 唯一性"""
        # 副标题
        subtitle = Text(
            "性质1: 唯一性",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 尝试不同角度的线 (非垂直)
        attempt_angles = [30, -45]  # 度数
        
        for angle_deg in attempt_angles:
            # 计算尝试线的终点
            angle_rad = angle_deg * DEGREES
            direction = np.array([np.sin(angle_rad), -np.cos(angle_rad), 0])
            end_point = self.P + direction * 2.5
            
            # 找到与直线l的交点
            # 参数方程: P + t*direction, y = 0
            # P[1] + t*direction[1] = 0
            t = -self.P[1] / direction[1] if abs(direction[1]) > 0.01 else 0
            intersection = self.P + direction * t
            
            attempt_line = DashedLine(
                self.P,
                intersection,
                color=GRAY,
                dash_length=0.08,
                stroke_width=2
            )
            
            # 交叉标记 (X)
            cross_size = 0.2
            cross_mark = VGroup(
                Line(
                    intersection + np.array([-cross_size, -cross_size, 0]),
                    intersection + np.array([cross_size, cross_size, 0]),
                    color=RED,
                    stroke_width=3
                ),
                Line(
                    intersection + np.array([-cross_size, cross_size, 0]),
                    intersection + np.array([cross_size, -cross_size, 0]),
                    color=RED,
                    stroke_width=3
                )
            )
            
            self.play(Create(attempt_line), run_time=0.5)
            self.play(FadeIn(cross_mark, scale=0.5), run_time=0.2)
            self.wait(0.1)
            self.play(
                FadeOut(attempt_line),
                FadeOut(cross_mark),
                run_time=0.3
            )
        
        # 高亮唯一的垂线
        self.play(
            self.perpendicular.animate.set_color(YELLOW).set_stroke_width(5),
            run_time=0.5
        )
        
        # 对勾标记
        check_mark = VGroup(
            Line(
                self.H + np.array([-0.15, -0.1, 0]),
                self.H + np.array([-0.05, -0.2, 0]),
                color=self.COLOR_RIGHT_ANGLE,
                stroke_width=4
            ),
            Line(
                self.H + np.array([-0.05, -0.2, 0]),
                self.H + np.array([0.2, 0.1, 0]),
                color=self.COLOR_RIGHT_ANGLE,
                stroke_width=4
            )
        )
        
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.3)
        self.play(Flash(check_mark, color=self.COLOR_RIGHT_ANGLE, flash_radius=0.3), run_time=0.3)
        
        # 恢复原色
        self.play(
            self.perpendicular.animate.set_color(self.COLOR_SECONDARY).set_stroke_width(3),
            run_time=0.3
        )
        
        # 性质文字
        property_text = Text(
            "过一点有且只有一条直线\n与已知直线垂直",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 4)
        
        self.play(Write(property_text), run_time=1.5)
        
        # 强调文字
        emphasis = Text(
            "有且只有 = 存在且唯一",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(emphasis, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(property_text),
            FadeOut(emphasis),
            FadeOut(check_mark),
            run_time=0.6
        )
    
    def show_shortest_distance(self):
        """场景4: 性质2 - 最短距离"""
        # 副标题
        subtitle = Text(
            "性质2: 最短距离",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 点A和线段PA
        dot_A = Dot(self.A, color=self.COLOR_AUXILIARY, radius=0.06)
        label_A = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(dot_A, DOWN, buff=0.12)
        
        self.play(FadeIn(dot_A), run_time=0.3)
        self.play(FadeIn(label_A), run_time=0.2)
        
        line_PA = Line(self.P, self.A, color=GRAY, stroke_width=2)
        self.play(Create(line_PA), run_time=0.6)
        
        # 距离标注PA
        brace_PA = Brace(line_PA, direction=RIGHT, buff=0.1, color=self.COLOR_DISTANCE)
        label_PA = DecimalNumber(
            self.dist_PA,
            num_decimal_places=2,
            color=self.COLOR_DISTANCE,
            font_size=18
        ).next_to(brace_PA, RIGHT, buff=0.05)
        
        self.play(
            FadeIn(brace_PA),
            FadeIn(label_PA),
            run_time=0.5
        )
        
        self.wait(0.3)
        
        # 点B和线段PB
        dot_B = Dot(self.B, color=self.COLOR_AUXILIARY, radius=0.06)
        label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(dot_B, DOWN, buff=0.12)
        
        self.play(FadeIn(dot_B), FadeIn(label_B), run_time=0.3)
        
        line_PB = Line(self.P, self.B, color=GRAY, stroke_width=2)
        self.play(Create(line_PB), run_time=0.6)
        
        # 距离标注PB
        brace_PB = Brace(line_PB, direction=LEFT, buff=0.1, color=self.COLOR_DISTANCE)
        label_PB = DecimalNumber(
            self.dist_PB,
            num_decimal_places=2,
            color=self.COLOR_DISTANCE,
            font_size=18
        ).next_to(brace_PB, LEFT, buff=0.05)
        
        self.play(
            FadeIn(brace_PB),
            FadeIn(label_PB),
            run_time=0.5
        )
        
        self.wait(0.4)
        
        # 高亮垂线段PH
        self.play(
            self.perpendicular.animate.set_color(YELLOW).set_stroke_width(6),
            run_time=0.5
        )
        
        # 距离标注PH
        brace_PH = Brace(self.perpendicular, direction=LEFT, buff=0.15, color=YELLOW)
        label_PH = DecimalNumber(
            self.dist_PH,
            num_decimal_places=2,
            color=YELLOW,
            font_size=20
        ).next_to(brace_PH, LEFT, buff=0.05)
        
        self.play(
            FadeIn(brace_PH),
            FadeIn(label_PH),
            run_time=0.5
        )
        
        # 强调最短
        self.play(Indicate(label_PH, scale_factor=1.3), run_time=0.6)
        
        # 恢复颜色
        self.play(
            self.perpendicular.animate.set_color(self.COLOR_SECONDARY).set_stroke_width(3),
            run_time=0.3
        )
        
        # 定义文字
        distance_def = Text(
            "点到直线的距离\n= 垂线段的长度",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 4.5)
        
        self.play(Write(distance_def), run_time=1.5)
        
        # 强调
        emphasis = Text(
            "这是最短距离!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(emphasis, scale=1.2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(distance_def),
            FadeOut(emphasis),
            FadeOut(line_PA),
            FadeOut(line_PB),
            FadeOut(dot_A),
            FadeOut(dot_B),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(brace_PA),
            FadeOut(brace_PB),
            FadeOut(brace_PH),
            FadeOut(label_PA),
            FadeOut(label_PB),
            FadeOut(label_PH),
            run_time=0.6
        )
    
    def show_application(self):
        """场景5: 实际应用示例"""
        # 标题
        title = Text(
            "实际应用",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 问题
        question = Text(
            "求点Q到直线l的距离",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(question), run_time=1.0)
        
        # 点Q出现
        dot_Q = Dot(self.Q, color=self.COLOR_SECONDARY, radius=0.08)
        label_Q = Text("Q", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_Q, UP, buff=0.15)
        
        self.play(FadeIn(dot_Q, scale=0.5), run_time=0.3)
        self.play(FadeIn(label_Q), run_time=0.2)
        
        self.wait(0.2)
        
        # 步骤1
        step_text = Text(
            "① 过Q作l的垂线",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(step_text), run_time=0.5)
        
        # 引导虚线
        guide_line = DashedLine(
            self.Q,
            self.K,
            color=GRAY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(guide_line), run_time=0.6)
        
        # 垂足K
        dot_K = Dot(self.K, color=self.COLOR_AUXILIARY, radius=0.07)
        label_K = Text("K", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_K, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_K), run_time=0.3)
        self.play(FadeIn(label_K), run_time=0.2)
        
        # 步骤2
        step2 = Text(
            "② 标记垂足K",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Transform(step_text, step2), run_time=0.4)
        
        # 垂线实线化
        perp_QK = Line(
            self.Q,
            self.K,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(
            Transform(guide_line, perp_QK),
            run_time=0.8
        )
        
        # 直角标记
        right_angle_K = self.create_right_angle_mark(
            self.K,
            self.Q,
            self.line_l_end
        )
        
        self.play(FadeIn(right_angle_K), run_time=0.3)
        
        # 步骤3
        step3 = Text(
            "③ 测量QK长度",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Transform(step_text, step3), run_time=0.4)
        
        # 距离标注
        brace_QK = Brace(perp_QK, direction=RIGHT, buff=0.1, color=self.COLOR_DISTANCE)
        distance_value = DecimalNumber(
            self.dist_QK,
            num_decimal_places=2,
            color=self.COLOR_DISTANCE,
            font_size=22
        ).next_to(brace_QK, RIGHT, buff=0.05)
        
        self.play(
            FadeIn(brace_QK),
            FadeIn(distance_value),
            run_time=0.6
        )
        
        # 结论
        conclusion = Text(
            "距离 = QK长度 = " + f"{self.dist_QK:.2f}",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(conclusion), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理所有应用示例元素
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            FadeOut(guide_line),
            FadeOut(perp_QK),
            FadeOut(dot_K),
            FadeOut(label_K),
            FadeOut(right_angle_K),
            FadeOut(brace_QK),
            FadeOut(distance_value),
            FadeOut(step_text),
            FadeOut(conclusion),
            run_time=0.6
        )
        
        # 清理原有的P点相关元素
        self.play(
            FadeOut(self.line_l),
            FadeOut(self.dot_P),
            FadeOut(self.label_P),
            FadeOut(self.perpendicular),
            FadeOut(self.dot_H),
            FadeOut(self.label_H),
            FadeOut(self.right_angle_mark),
            run_time=0.4
        )
    
    def show_summary(self):
        """场景6: 知识总结"""
        # 标题
        title = Text(
            "知识总结",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 创建三个要点卡片
        card1 = self.create_summary_card(
            "定义",
            "两直线成直角 → 互相垂直",
            self.COLOR_PRIMARY,
            UP * 2.5
        )
        
        card2 = self.create_summary_card(
            "唯一性",
            "过一点有且只有一条垂线",
            self.COLOR_SECONDARY,
            UP * 0.5
        )
        
        card3 = self.create_summary_card(
            "最短性",
            "垂线段是最短距离",
            self.COLOR_DISTANCE,
            DOWN * 1.5
        )
        
        # 卡片依次滑入
        for card in [card1, card2, card3]:
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            self.wait(0.2)
        
        # 图标闪烁
        icons = VGroup(card1[0], card2[0], card3[0])
        self.play(
            Flash(card1[0], color=self.COLOR_PRIMARY, flash_radius=0.3),
            Flash(card2[0], color=self.COLOR_SECONDARY, flash_radius=0.3),
            Flash(card3[0], color=self.COLOR_DISTANCE, flash_radius=0.3),
            run_time=0.6
        )
        
        # 强调语
        emphasis = Text(
            "掌握垂线, 轻松解题!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(emphasis, shift=UP * 0.3, scale=1.1), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标圆
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.35)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=42,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.3)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.5)
        
        # 装饰 - 垂直线图标
        icon_group = VGroup()
        for i in range(5):
            x_pos = -2 + i
            h_line = Line([x_pos - 0.2, -2, 0], [x_pos + 0.2, -2, 0], color=self.COLOR_PRIMARY, stroke_width=2)
            v_line = Line([x_pos, -2, 0], [x_pos, -1.5, 0], color=self.COLOR_SECONDARY, stroke_width=2)
            icon_group.add(h_line, v_line)
        
        self.play(
            *[FadeIn(obj, scale=0.5) for obj in icon_group],
            run_time=0.5
        )
        
        self.play(Rotate(icon_group, angle=PI/6, run_time=1.0))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icon_group),
            run_time=0.8
        )


# 运行命令:
# manim -pql perpendicular_lines.py PerpendicularLines  # 快速预览
# manim -qh perpendicular_lines.py PerpendicularLines   # 高质量渲染