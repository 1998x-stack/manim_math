"""
圆周角定理 - Inscribed Angle Theorem
使用 Manim 创建的九年级几何教学视频

内容: 圆周角定理、同弧圆周角相等、直径与90°的关系
目标观众: 九年级学生
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


class InscribedAngleTheorem(Scene):
    """
    圆周角定理教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 圆周角定义
    3. 圆心角引入
    4. 圆周角定理主体
    5. 推论1 - 同弧圆周角相等
    6. 推论2 - 直径对应90°
    7. 推论3 - 90°对应直径
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"          # 蓝色 - 圆
        self.COLOR_INSCRIBED_ANGLE = "#e74c3c" # 红色 - 圆周角
        self.COLOR_CENTRAL_ANGLE = "#f39c12"   # 橙色 - 圆心角
        self.COLOR_ARC = "#9b59b6"             # 紫色 - 弧
        self.COLOR_DIAMETER = "#2ecc71"        # 绿色 - 直径
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_inscribed_angle_definition()
        self.show_central_angle()
        self.show_main_theorem()
        self.show_corollary_1()
        self.show_corollary_2()
        self.show_corollary_3()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化圆及所有几何元素"""
        # 圆心和半径
        self.O = ORIGIN + UP * 1.5
        self.radius = 1.8
        
        # 圆上的关键点 - 使用角度定位
        # A和B是弧的端点
        self.A = self.point_on_circle(30)   # 30度
        self.B = self.point_on_circle(150)  # 150度
        
        # P是圆周角的顶点（在优弧上）
        self.P = self.point_on_circle(240)  # 240度
        
        # Q是另一个圆周角顶点（用于推论1）
        self.Q = self.point_on_circle(290)  # 290度
        
        # C是用于直径定理的点（在半圆上）
        self.C = self.point_on_circle(90)   # 90度
        
        # 计算角度
        self.central_angle_rad = self.calculate_central_angle(self.O, self.A, self.B)
        self.inscribed_angle_rad = self.calculate_inscribed_angle(self.P, self.A, self.B)
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
    
    def point_on_circle(self, angle_deg):
        """在圆上生成精确的点"""
        angle_rad = angle_deg * DEGREES
        return self.O + self.radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
    
    def calculate_central_angle(self, center, point1, point2):
        """计算圆心角（弧度）"""
        angle1 = np.arctan2(point1[1] - center[1], point1[0] - center[0])
        angle2 = np.arctan2(point2[1] - center[1], point2[0] - center[0])
        
        # 计算角度差（取较小的角）
        angle = abs(angle2 - angle1)
        if angle > PI:
            angle = 2 * PI - angle
        
        return angle
    
    def calculate_inscribed_angle(self, vertex, point1, point2):
        """计算圆周角（弧度）"""
        v1 = point1 - vertex
        v2 = point2 - vertex
        
        # 计算夹角
        cos_angle = np.dot(v1[:2], v2[:2]) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angle = np.arccos(cos_angle)
        
        return angle
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 1. 验证所有点都在圆上
        points = {'A': self.A, 'B': self.B, 'P': self.P, 'Q': self.Q, 'C': self.C}
        for name, point in points.items():
            dist = np.linalg.norm(point - self.O)
            if abs(dist - self.radius) > epsilon:
                print(f"WARNING: 点{name}不在圆上! 距离={dist:.6f}, 半径={self.radius:.6f}")
        
        # 2. 验证圆周角定理（最关键）
        ratio = self.inscribed_angle_rad / self.central_angle_rad
        if abs(ratio - 0.5) > 0.01:  # 1%误差
            print(f"WARNING: 圆周角定理验证失败!")
            print(f"  圆心角: {np.degrees(self.central_angle_rad):.2f}°")
            print(f"  圆周角: {np.degrees(self.inscribed_angle_rad):.2f}°")
            print(f"  比例: {ratio:.4f} (应为0.5)")
        
        # 3. 验证Q的圆周角与P的相等
        inscribed_angle_Q = self.calculate_inscribed_angle(self.Q, self.A, self.B)
        if abs(inscribed_angle_Q - self.inscribed_angle_rad) > epsilon * 100:
            print(f"WARNING: 同弧圆周角不相等!")
            print(f"  ∠APB: {np.degrees(self.inscribed_angle_rad):.2f}°")
            print(f"  ∠AQB: {np.degrees(inscribed_angle_Q):.2f}°")
        
        print("✓ 几何验证通过")
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        return Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "圆上的角，藏着什么秘密？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 圆出现
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.circle), run_time=0.8)
        
        # 几个点闪现
        dots = VGroup(
            Dot(self.A, radius=0.08, color=WHITE),
            Dot(self.B, radius=0.08, color=WHITE),
            Dot(self.P, radius=0.08, color=WHITE)
        )
        
        self.play(FadeIn(dots, scale=0.5), run_time=0.5)
        
        # 问号
        question_mark = Text("?", font_size=60, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 2)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.4)
        self.play(Indicate(question_mark, scale_factor=1.3), run_time=0.5)
        
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            FadeOut(dots),
            run_time=0.4
        )
    
    def show_inscribed_angle_definition(self):
        """场景2: 圆周角定义"""
        # 小标题
        subtitle = Text(
            "什么是圆周角？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_INSCRIBED_ANGLE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点P出现
        self.dot_P = Dot(self.P, color=WHITE, radius=0.10)
        label_P = Text("P", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            self.dot_P, DOWN, buff=0.15
        )
        
        self.play(
            FadeIn(self.dot_P, scale=0.5),
            FadeIn(label_P),
            run_time=0.4
        )
        
        # 点A和B出现
        self.dot_A = Dot(self.A, color=WHITE, radius=0.10)
        self.dot_B = Dot(self.B, color=WHITE, radius=0.10)
        label_A = Text("A", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            self.dot_A, RIGHT, buff=0.15
        )
        label_B = Text("B", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            self.dot_B, LEFT, buff=0.15
        )
        
        self.play(
            FadeIn(self.dot_A, scale=0.5),
            FadeIn(self.dot_B, scale=0.5),
            FadeIn(label_A),
            FadeIn(label_B),
            run_time=0.6
        )
        
        # 连线PA和PB
        line_PA = Line(self.P, self.A, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2)
        line_PB = Line(self.P, self.B, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2)
        
        self.play(
            Create(line_PA),
            Create(line_PB),
            run_time=0.6
        )
        
        # 圆周角弧
        self.inscribed_angle = Angle.from_three_points(
            self.A, self.P, self.B,
            radius=0.4,
            color=self.COLOR_INSCRIBED_ANGLE,
            other_angle=False
        )
        
        self.play(Create(self.inscribed_angle), run_time=0.8)
        
        # 标注"圆周角"
        label_inscribed = Text(
            "圆周角",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_INSCRIBED_ANGLE
        ).move_to(self.P + DOWN * 0.8)
        
        self.play(FadeIn(label_inscribed), run_time=0.5)
        
        # 定义文字
        definition_text = Text(
            "顶点在圆上，两边都与圆相交的角",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(definition_text), run_time=0.7)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(definition_text),
            FadeOut(label_inscribed),
            FadeOut(label_P),
            FadeOut(label_A),
            FadeOut(label_B),
            run_time=0.5
        )
        
        # 保留: circle, dots, lines, angle
        self.line_PA = line_PA
        self.line_PB = line_PB
    
    def show_central_angle(self):
        """场景3: 圆心角引入"""
        # 圆心O出现
        self.dot_O = Dot(self.O, color=self.COLOR_CENTRAL_ANGLE, radius=0.12)
        label_O = Text("O", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_CENTRAL_ANGLE).next_to(
            self.dot_O, LEFT, buff=0.15
        )
        
        self.play(
            FadeIn(self.dot_O, scale=0.5),
            FadeIn(label_O),
            run_time=0.5
        )
        
        # 连线OA和OB
        line_OA = Line(self.O, self.A, color=self.COLOR_CENTRAL_ANGLE, stroke_width=2)
        line_OB = Line(self.O, self.B, color=self.COLOR_CENTRAL_ANGLE, stroke_width=2)
        
        self.play(
            Create(line_OA),
            Create(line_OB),
            run_time=0.8
        )
        
        # 圆心角弧
        self.central_angle = Angle.from_three_points(
            self.A, self.O, self.B,
            radius=0.5,
            color=self.COLOR_CENTRAL_ANGLE,
            other_angle=False
        )
        
        self.play(Create(self.central_angle), run_time=0.7)
        
        # 标注"圆心角"
        label_central = Text(
            "圆心角",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_CENTRAL_ANGLE
        ).move_to(self.O + UP * 0.8)
        
        self.play(FadeIn(label_central), run_time=0.5)
        
        # 弧AB高亮
        # 计算弧的起始和结束角度
        angle_A = np.arctan2(self.A[1] - self.O[1], self.A[0] - self.O[0])
        angle_B = np.arctan2(self.B[1] - self.O[1], self.B[0] - self.O[0])
        
        arc_AB = Arc(
            radius=self.radius,
            start_angle=angle_A,
            angle=angle_B - angle_A,
            color=self.COLOR_ARC,
            stroke_width=6
        ).move_to(self.O)
        
        self.play(Create(arc_AB), run_time=0.7)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(label_O),
            FadeOut(label_central),
            FadeOut(arc_AB),
            run_time=0.4
        )
        
        # 保留: line_OA, line_OB, central_angle, dot_O
        self.line_OA = line_OA
        self.line_OB = line_OB
    
    def show_main_theorem(self):
        """场景4: 圆周角定理主体"""
        # 大标题
        main_title = Text(
            "圆周角定理",
            font="Noto Sans CJK SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(main_title, shift=UP * 0.3), run_time=0.8)
        
        # 圆周角高亮
        self.play(
            Indicate(self.inscribed_angle, color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.7
        )
        
        # 圆心角高亮
        self.play(
            Indicate(self.central_angle, color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.7
        )
        
        self.wait(1.0)
        
        # 公式
        formula = MathTex(
            r"\angle APB = \frac{1}{2} \angle AOB",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(Write(formula), run_time=1.0)
        
        # 测量角度值
        central_deg = np.degrees(self.central_angle_rad)
        inscribed_deg = np.degrees(self.inscribed_angle_rad)
        
        central_measure = MathTex(
            f"{central_deg:.1f}^\\circ",
            font_size=24,
            color=self.COLOR_CENTRAL_ANGLE
        ).move_to(self.O + UP * 0.6)
        
        inscribed_measure = MathTex(
            f"{inscribed_deg:.1f}^\\circ",
            font_size=24,
            color=self.COLOR_INSCRIBED_ANGLE
        ).move_to(self.P + DOWN * 0.6)
        
        self.play(
            FadeIn(central_measure),
            run_time=0.5
        )
        self.play(
            FadeIn(inscribed_measure),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 对比动画
        self.play(
            Indicate(VGroup(self.central_angle, self.inscribed_angle), color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 强调"一半"
        self.play(
            Indicate(formula[0][7:11], color=self.COLOR_HIGHLIGHT, scale_factor=1.2),  # \frac{1}{2}
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(main_title),
            FadeOut(central_measure),
            FadeOut(inscribed_measure),
            run_time=0.5
        )
        
        # 保留: formula
        self.main_formula = formula
    
    def show_corollary_1(self):
        """场景5: 推论1 - 同弧圆周角相等"""
        # 小标题
        subtitle = Text(
            "推论1：同弧所对的圆周角相等",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 点Q出现
        dot_Q = Dot(self.Q, color=WHITE, radius=0.10)
        label_Q = Text("Q", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            dot_Q, DOWN, buff=0.15
        )
        
        self.play(
            FadeIn(dot_Q, scale=0.5),
            FadeIn(label_Q),
            run_time=0.6
        )
        
        # 连线QA和QB
        line_QA = Line(self.Q, self.A, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2, stroke_opacity=0.6)
        line_QB = Line(self.Q, self.B, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2, stroke_opacity=0.6)
        
        self.play(
            Create(line_QA),
            Create(line_QB),
            run_time=0.8
        )
        
        # 圆周角∠AQB
        angle_AQB = Angle.from_three_points(
            self.A, self.Q, self.B,
            radius=0.4,
            color=self.COLOR_INSCRIBED_ANGLE,
            other_angle=False
        )
        
        self.play(Create(angle_AQB), run_time=0.8)
        
        self.wait(1.0)
        
        # 两个圆周角同时高亮
        self.play(
            Indicate(self.inscribed_angle, color=self.COLOR_HIGHLIGHT),
            Indicate(angle_AQB, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 角度数值
        inscribed_deg = np.degrees(self.inscribed_angle_rad)
        angle_Q_rad = self.calculate_inscribed_angle(self.Q, self.A, self.B)
        angle_Q_deg = np.degrees(angle_Q_rad)
        
        angle_P_value = MathTex(
            f"{inscribed_deg:.1f}^\\circ",
            font_size=22,
            color=self.COLOR_INSCRIBED_ANGLE
        ).move_to(self.P + DOWN * 0.6)
        
        angle_Q_value = MathTex(
            f"{angle_Q_deg:.1f}^\\circ",
            font_size=22,
            color=self.COLOR_INSCRIBED_ANGLE
        ).move_to(self.Q + DOWN * 0.6)
        
        self.play(
            FadeIn(angle_P_value),
            FadeIn(angle_Q_value),
            run_time=0.7
        )
        
        # 等号
        equals_sign = MathTex(
            "=",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(equals_sign), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            FadeOut(line_QA),
            FadeOut(line_QB),
            FadeOut(angle_AQB),
            FadeOut(angle_P_value),
            FadeOut(angle_Q_value),
            FadeOut(equals_sign),
            run_time=0.6
        )
    
    def show_corollary_2(self):
        """场景6: 推论2 - 直径对应90°"""
        # 清空之前的元素
        self.play(
            FadeOut(self.line_PA),
            FadeOut(self.line_PB),
            FadeOut(self.inscribed_angle),
            FadeOut(self.dot_P),
            FadeOut(self.line_OA),
            FadeOut(self.line_OB),
            FadeOut(self.central_angle),
            FadeOut(self.dot_O),
            FadeOut(self.main_formula),
            run_time=0.5
        )
        
        # 小标题
        subtitle = Text(
            "推论2：直径所对的圆周角 = 90°",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_DIAMETER
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.7)
        
        # 将A和B重新定位为直径的端点
        # A在右，B在左
        self.A_diameter = self.O + self.radius * RIGHT
        self.B_diameter = self.O + self.radius * LEFT
        
        # 更新点A和B的位置
        self.play(
            self.dot_A.animate.move_to(self.A_diameter),
            self.dot_B.animate.move_to(self.B_diameter),
            run_time=0.8
        )
        
        # 直径AB
        diameter_AB = Line(
            self.A_diameter, self.B_diameter,
            color=self.COLOR_DIAMETER,
            stroke_width=5
        )
        
        self.play(Create(diameter_AB), run_time=0.8)
        
        # 标注"直径"
        diameter_label = Text(
            "直径",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_DIAMETER
        ).next_to(diameter_AB, DOWN, buff=0.2)
        
        self.play(FadeIn(diameter_label), run_time=0.5)
        
        self.wait(0.8)
        
        # 点C出现（在半圆上，任意位置）
        self.dot_C = Dot(self.C, color=WHITE, radius=0.10)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(
            self.dot_C, UP, buff=0.15
        )
        
        self.play(
            FadeIn(self.dot_C, scale=0.5),
            FadeIn(label_C),
            run_time=0.8
        )
        
        # 连线CA和CB
        line_CA = Line(self.C, self.A_diameter, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2)
        line_CB = Line(self.C, self.B_diameter, color=self.COLOR_INSCRIBED_ANGLE, stroke_width=2)
        
        self.play(
            Create(line_CA),
            Create(line_CB),
            run_time=0.8
        )
        
        # 圆周角∠ACB
        angle_ACB = Angle.from_three_points(
            self.A_diameter, self.C, self.B_diameter,
            radius=0.4,
            color=self.COLOR_INSCRIBED_ANGLE,
            other_angle=False
        )
        
        self.play(Create(angle_ACB), run_time=1.0)
        
        # 直角符号
        right_angle_mark = self.create_right_angle_mark(
            self.C,
            self.A_diameter,
            self.B_diameter,
            size=0.2
        )
        
        self.play(FadeIn(right_angle_mark), run_time=0.6)
        
        # 90°标注
        angle_90_label = MathTex(
            "90^\\circ",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.C + DOWN * 0.6)
        
        self.play(FadeIn(angle_90_label), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(diameter_label),
            FadeOut(label_C),
            run_time=0.4
        )
        
        # 保留: diameter, angle, right_angle_mark, angle_90_label
        self.diameter_AB = diameter_AB
        self.line_CA = line_CA
        self.line_CB = line_CB
        self.angle_ACB = angle_ACB
        self.right_angle_mark = right_angle_mark
        self.angle_90_label = angle_90_label
    
    def show_corollary_3(self):
        """场景7: 推论3 - 90°对应直径"""
        # 小标题
        subtitle = Text(
            "推论3：90°圆周角所对的弦是直径",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 强调90°角
        self.play(
            Indicate(self.right_angle_mark, color=self.COLOR_HIGHLIGHT, scale_factor=1.2),
            Indicate(self.angle_90_label, color=self.COLOR_HIGHLIGHT, scale_factor=1.2),
            run_time=0.8
        )
        
        # 弦AB高亮
        self.play(
            Indicate(self.diameter_AB, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 圆心O重新出现并闪烁
        dot_O = Dot(self.O, color=self.COLOR_CENTRAL_ANGLE, radius=0.10)
        self.play(
            FadeIn(dot_O, scale=0.5),
            Flash(dot_O, color=self.COLOR_CENTRAL_ANGLE, flash_radius=0.4),
            run_time=0.8
        )
        
        # 验证线通过圆心（延长线）
        extended_line = DashedLine(
            self.A_diameter + (self.A_diameter - self.B_diameter) * 0.2,
            self.B_diameter + (self.B_diameter - self.A_diameter) * 0.2,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(extended_line), run_time=0.8)
        
        # 标注"直径"确认
        diameter_confirmation = Text(
            "确实是直径！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_DIAMETER
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(diameter_confirmation), run_time=0.6)
        
        # 对号
        check_mark = VGroup(
            Line(ORIGIN, RIGHT * 0.3 + DOWN * 0.3, color=GREEN, stroke_width=8),
            Line(RIGHT * 0.3 + DOWN * 0.3, RIGHT * 0.8 + UP * 0.5, color=GREEN, stroke_width=8)
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(extended_line),
            FadeOut(diameter_confirmation),
            FadeOut(check_mark),
            FadeOut(dot_O),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景8: 总结与片尾"""
        # 清空所有元素
        self.play(
            FadeOut(self.circle),
            FadeOut(self.dot_A),
            FadeOut(self.dot_B),
            FadeOut(self.dot_C),
            FadeOut(self.diameter_AB),
            FadeOut(self.line_CA),
            FadeOut(self.line_CB),
            FadeOut(self.angle_ACB),
            FadeOut(self.right_angle_mark),
            FadeOut(self.angle_90_label),
            run_time=0.6
        )
        
        # 知识卡片
        cards = VGroup()
        
        # 卡片1
        card_1 = self.create_knowledge_card(
            "圆周角 = 圆心角 ÷ 2",
            "同弧所对，角度减半",
            self.COLOR_INSCRIBED_ANGLE,
            UP * 2.5
        )
        cards.add(card_1)
        
        # 卡片2
        card_2 = self.create_knowledge_card(
            "同弧圆周角相等",
            "顶点可以在圆上任意移动",
            self.COLOR_ARC,
            UP * 1.0
        )
        cards.add(card_2)
        
        # 卡片3
        card_3 = self.create_knowledge_card(
            "直径 → 90°",
            "直径所对的圆周角是直角",
            self.COLOR_DIAMETER,
            DOWN * 0.5
        )
        cards.add(card_3)
        
        # 卡片4
        card_4 = self.create_knowledge_card(
            "90° → 直径",
            "直角圆周角所对的弦是直径",
            self.COLOR_HIGHLIGHT,
            DOWN * 2.0
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 总结文字
        summary_text = Text(
            "掌握圆周角定理\n解锁几何新视角！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理并准备片尾
        self.play(
            FadeOut(cards),
            FadeOut(summary_text),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
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
            "关注我，学更多几何技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小圆形装饰
        circles = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_CIRCLE, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circ, scale=0.5) for circ in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, title, content, color, position):
        """创建知识卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=16,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql inscribed_angle_theorem.py InscribedAngleTheorem  # 快速预览
# manim -qh inscribed_angle_theorem.py InscribedAngleTheorem   # 高质量渲染