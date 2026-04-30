"""
三角形内角和定理动画 - Triangle Interior Angle Sum Theorem
使用 Manim 创建的中学几何教学视频

内容: 三角形三个内角和等于180°的证明（平行线法）
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ==================== 几何计算工具类 ====================
class GeometryCalculator:
    """精确几何计算工具类"""
    
    @staticmethod
    def angle_at_vertex(point1, vertex, point2):
        """
        计算∠point1-vertex-point2的角度（弧度）
        vertex: 角的顶点
        point1, point2: 角的两边上的点
        """
        v1 = np.array(point1) - np.array(vertex)
        v2 = np.array(point2) - np.array(vertex)
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    
    @staticmethod
    def normalize(vector):
        """归一化向量"""
        norm = np.linalg.norm(vector)
        return vector / norm if norm > 1e-10 else vector


# ==================== 主场景类 ====================
class TriangleAngleSum(Scene):
    """
    三角形内角和定理教学动画
    
    场景顺序:
    1. 开场钩子 (0-5s)
    2. 展示三角形与角度 (5-15s)
    3. 平行线证明法 (15-35s)
    4. 角度汇聚成平角 (35-45s)
    5. 回到原三角形 (45-52s)
    6. 推论展示 (52-62s)
    7. 片尾关注 (62-75s)
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#00D9FF"      # 青色 - 主三角形
        self.COLOR_ANGLE_A = "#FF6B6B"      # 红色 - 角A
        self.COLOR_ANGLE_B = "#4ECDC4"      # 绿松石 - 角B
        self.COLOR_ANGLE_C = "#FFE66D"      # 黄色 - 角C
        self.COLOR_AUXILIARY = "#95A5A6"    # 灰色 - 辅助线
        self.COLOR_HIGHLIGHT = YELLOW       # 高亮
        self.COLOR_TEXT = WHITE             # 文字
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_show_angles()
        self.scene_3_parallel_proof()
        self.scene_4_angle_sum()
        self.scene_5_back_to_triangle()
        self.scene_6_corollaries()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ========== 基准参数 ==========
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # ========== 主要顶点 ==========
        self.A = np.array([-2.5, 1.2, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.5, -0.8, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([-1.0, -2.0, 0]) * self.SCALE + self.OFFSET
        
        # ========== 边长计算 ==========
        self.AB = np.linalg.norm(self.B - self.A)
        self.BC = np.linalg.norm(self.C - self.B)
        self.CA = np.linalg.norm(self.A - self.C)
        
        # ========== 角度计算（弧度）==========
        self.angle_A_rad = GeometryCalculator.angle_at_vertex(self.C, self.A, self.B)
        self.angle_B_rad = GeometryCalculator.angle_at_vertex(self.A, self.B, self.C)
        self.angle_C_rad = GeometryCalculator.angle_at_vertex(self.B, self.C, self.A)
        
        # ========== 角度（度数）==========
        self.angle_A_deg = np.degrees(self.angle_A_rad)
        self.angle_B_deg = np.degrees(self.angle_B_rad)
        self.angle_C_deg = np.degrees(self.angle_C_rad)
        
        # ========== 平行线数据 ==========
        # 过C点平行于AB的直线
        AB_direction = GeometryCalculator.normalize(self.B - self.A)
        self.parallel_start = self.C - AB_direction * 3.0
        self.parallel_end = self.C + AB_direction * 3.0
        
        # ========== 验证 ==========
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-5
        
        # 验证角度和 = 180°
        angle_sum_rad = self.angle_A_rad + self.angle_B_rad + self.angle_C_rad
        angle_sum_deg = np.degrees(angle_sum_rad)
        
        if abs(angle_sum_deg - 180.0) > epsilon:
            print(f"WARNING: 角度和 = {angle_sum_deg:.6f}° (应为180°)")
        else:
            print(f"✓ 角度和验证通过: {angle_sum_deg:.2f}°")
        
        # 验证平行线
        AB_vec = self.B - self.A
        parallel_vec = self.parallel_end - self.parallel_start
        cross_product = np.cross(AB_vec[:2], parallel_vec[:2])
        
        if abs(cross_product) > epsilon:
            print(f"WARNING: 平行线不平行! 叉积 = {cross_product:.6f}")
        else:
            print("✓ 平行线验证通过")
        
        print(f"✓ 三个角度: A={self.angle_A_deg:.1f}°, B={self.angle_B_deg:.1f}°, C={self.angle_C_deg:.1f}°")
    
    # ==================== Scene 1: 开场钩子 ====================
    def scene_1_opening(self):
        """开场钩子 - 快速抓住注意力"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "三个角加起来等于多少度?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三角形快速创建
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(self.triangle), run_time=0.6)
        
        # 三个角闪烁
        angle_a_flash = Dot(self.A, color=self.COLOR_ANGLE_A, radius=0.15)
        angle_b_flash = Dot(self.B, color=self.COLOR_ANGLE_B, radius=0.15)
        angle_c_flash = Dot(self.C, color=self.COLOR_ANGLE_C, radius=0.15)
        
        self.play(
            Flash(angle_a_flash, color=self.COLOR_ANGLE_A, flash_radius=0.3),
            Flash(angle_b_flash, color=self.COLOR_ANGLE_B, flash_radius=0.3),
            Flash(angle_c_flash, color=self.COLOR_ANGLE_C, flash_radius=0.3),
            run_time=0.6
        )
        
        # 问号
        question_mark = Text(
            "?",
            font="PingFang SC",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.4)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.4
        )
    
    # ==================== Scene 2: 展示三角形与角度 ====================
    def scene_2_show_angles(self):
        """展示三角形ABC及其三个内角"""
        # 顶点标签
        self.label_A = MathTex("A", font_size=28, color=WHITE).next_to(self.A, UP + LEFT, buff=0.15)
        self.label_B = MathTex("B", font_size=28, color=WHITE).next_to(self.B, DOWN + RIGHT, buff=0.15)
        self.label_C = MathTex("C", font_size=28, color=WHITE).next_to(self.C, DOWN + LEFT, buff=0.15)
        
        self.play(FadeIn(VGroup(self.label_A, self.label_B, self.label_C)), run_time=0.6)
        
        # 角A弧线
        self.angle_arc_A = Angle.from_three_points(
            self.C, self.A, self.B,
            radius=0.5,
            color=self.COLOR_ANGLE_A,
            stroke_width=3
        )
        self.play(Create(self.angle_arc_A), run_time=0.6)
        
        # 角A度数（简化显示）
        angle_label_A = MathTex(
            r"\angle A",
            font_size=24,
            color=self.COLOR_ANGLE_A
        ).next_to(self.angle_arc_A, RIGHT, buff=0.2)
        self.play(FadeIn(angle_label_A), run_time=0.4)
        
        # 角B弧线
        self.angle_arc_B = Angle.from_three_points(
            self.A, self.B, self.C,
            radius=0.5,
            color=self.COLOR_ANGLE_B,
            stroke_width=3
        )
        self.play(Create(self.angle_arc_B), run_time=0.6)
        
        # 角B度数
        angle_label_B = MathTex(
            r"\angle B",
            font_size=24,
            color=self.COLOR_ANGLE_B
        ).next_to(self.angle_arc_B, LEFT, buff=0.2)
        self.play(FadeIn(angle_label_B), run_time=0.4)
        
        # 角C弧线
        self.angle_arc_C = Angle.from_three_points(
            self.B, self.C, self.A,
            radius=0.5,
            color=self.COLOR_ANGLE_C,
            stroke_width=3
        )
        self.play(Create(self.angle_arc_C), run_time=0.6)
        
        # 角C度数
        angle_label_C = MathTex(
            r"\angle C",
            font_size=24,
            color=self.COLOR_ANGLE_C
        ).next_to(self.angle_arc_C, UP, buff=0.2)
        self.play(FadeIn(angle_label_C), run_time=0.4)
        
        # 标题
        title = Text(
            "三角形内角和定理",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "认识这三个内角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(explain),
            FadeOut(title),
            FadeOut(angle_label_A),
            FadeOut(angle_label_B),
            FadeOut(angle_label_C),
            run_time=0.5
        )
    
    # ==================== Scene 3: 平行线证明法 ====================
    def scene_3_parallel_proof(self):
        """使用平行线和内错角证明"""
        # 说明文字1
        explain_1 = Text(
            "过点C作AB的平行线",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(Write(explain_1), run_time=0.8)
        
        # 平行线
        self.parallel_line = DashedLine(
            self.parallel_start,
            self.parallel_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(self.parallel_line), run_time=0.8)
        
        # 平行符号标记
        parallel_mark_1 = VGroup(
            Line(UP * 0.1, DOWN * 0.1),
            Line(UP * 0.1, DOWN * 0.1).shift(RIGHT * 0.1)
        ).scale(0.3).set_color(self.COLOR_AUXILIARY)
        
        # 在AB中点
        AB_mid = (self.A + self.B) / 2
        parallel_mark_1.move_to(AB_mid).rotate(
            np.arctan2((self.B - self.A)[1], (self.B - self.A)[0]) + PI/2
        )
        
        parallel_mark_2 = parallel_mark_1.copy().move_to(self.C).rotate(0)
        
        self.play(FadeIn(parallel_mark_1), FadeIn(parallel_mark_2), run_time=0.6)
        self.wait(0.8)
        
        self.play(FadeOut(explain_1), run_time=0.4)
        
        # 说明文字2 - 内错角相等
        explain_2 = Text(
            "内错角相等",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(Write(explain_2), run_time=0.8)
        
        # 高亮角A
        self.play(self.angle_arc_A.animate.set_stroke(width=6), run_time=0.4)
        
        # 复制角A到C处（左侧）
        # 计算角A在C处的位置
        CA_direction = GeometryCalculator.normalize(self.A - self.C)
        parallel_direction = GeometryCalculator.normalize(self.parallel_start - self.C)
        
        # 创建从C出发的两条线，形成与角A相等的角
        line_C_left = Line(self.C, self.C + parallel_direction * 0.5)
        line_C_up = Line(self.C, self.C + CA_direction * 0.5)
        
        self.angle_A_copy = Angle(
            line_C_left, line_C_up,
            radius=0.4,
            color=self.COLOR_ANGLE_A,
            stroke_width=3
        )
        
        self.play(TransformFromCopy(self.angle_arc_A, self.angle_A_copy), run_time=1.0)
        
        # 标记∠1 = ∠A
        label_1 = MathTex(r"\angle 1", font_size=20, color=self.COLOR_ANGLE_A).next_to(
            self.angle_A_copy, LEFT, buff=0.15
        )
        self.play(FadeIn(label_1), run_time=0.4)
        self.wait(0.6)
        
        # 恢复角A
        self.play(self.angle_arc_A.animate.set_stroke(width=3), run_time=0.4)
        
        # 高亮角B
        self.play(self.angle_arc_B.animate.set_stroke(width=6), run_time=0.4)
        
        # 复制角B到C处（右侧）
        CB_direction = GeometryCalculator.normalize(self.B - self.C)
        parallel_direction_right = GeometryCalculator.normalize(self.parallel_end - self.C)
        
        line_C_right = Line(self.C, self.C + parallel_direction_right * 0.5)
        line_C_down_right = Line(self.C, self.C + CB_direction * 0.5)
        
        self.angle_B_copy = Angle(
            line_C_down_right, line_C_right,
            radius=0.4,
            color=self.COLOR_ANGLE_B,
            stroke_width=3
        )
        
        self.play(TransformFromCopy(self.angle_arc_B, self.angle_B_copy), run_time=1.0)
        
        # 标记∠2 = ∠B
        label_2 = MathTex(r"\angle 2", font_size=20, color=self.COLOR_ANGLE_B).next_to(
            self.angle_B_copy, RIGHT, buff=0.15
        )
        self.play(FadeIn(label_2), run_time=0.4)
        self.wait(0.6)
        
        # 恢复角B
        self.play(self.angle_arc_B.animate.set_stroke(width=3), run_time=0.4)
        
        self.play(FadeOut(explain_2), run_time=0.4)
        
        # 保存标签以便后续清理
        self.label_1 = label_1
        self.label_2 = label_2
        self.parallel_marks = VGroup(parallel_mark_1, parallel_mark_2)
    
    # ==================== Scene 4: 角度汇聚成平角 ====================
    def scene_4_angle_sum(self):
        """展示三个角拼成180°"""
        # 说明文字
        explain_3 = Text(
            "三个角拼成一条直线",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(Write(explain_3), run_time=0.8)
        
        # 三个角闪烁
        self.play(
            Flash(self.angle_A_copy, color=self.COLOR_ANGLE_A),
            Flash(self.angle_arc_C, color=self.COLOR_ANGLE_C),
            Flash(self.angle_B_copy, color=self.COLOR_ANGLE_B),
            run_time=0.8
        )
        
        # 平角弧线（完整的半圆）
        straight_angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=PI,
            color=GOLD,
            stroke_width=4
        ).move_arc_center_to(self.C)
        
        self.play(Create(straight_angle_arc), run_time=1.0)
        
        # 平角标注
        straight_label = MathTex(r"180^\circ", font_size=28, color=GOLD).next_to(
            straight_angle_arc, UP, buff=0.2
        )
        self.play(FadeIn(straight_label), run_time=0.6)
        self.wait(1.0)
        
        # 公式推导
        # 步骤1: ∠1 + ∠C + ∠2 = 180°
        formula_1 = MathTex(
            r"\angle 1", r"+", r"\angle C", r"+", r"\angle 2", r"=", r"180^\circ",
            font_size=32
        ).move_to(DOWN * 3.5)
        
        formula_1[0].set_color(self.COLOR_ANGLE_A)
        formula_1[2].set_color(self.COLOR_ANGLE_C)
        formula_1[4].set_color(self.COLOR_ANGLE_B)
        
        self.play(Write(formula_1), run_time=1.0)
        self.wait(1.0)
        
        # 步骤2: ∠A + ∠C + ∠B = 180° (因为内错角相等)
        formula_2 = MathTex(
            r"\angle A", r"+", r"\angle C", r"+", r"\angle B", r"=", r"180^\circ",
            font_size=32
        ).move_to(DOWN * 3.5)
        
        formula_2[0].set_color(self.COLOR_ANGLE_A)
        formula_2[2].set_color(self.COLOR_ANGLE_C)
        formula_2[4].set_color(self.COLOR_ANGLE_B)
        
        self.play(TransformMatchingTex(formula_1, formula_2), run_time=1.2)
        self.wait(1.0)
        
        # 步骤3: 重新排列 ∠A + ∠B + ∠C = 180°
        self.formula_final = MathTex(
            r"\angle A", r"+", r"\angle B", r"+", r"\angle C", r"=", r"180^\circ",
            font_size=36
        ).move_to(DOWN * 3.5)
        
        self.formula_final[0].set_color(self.COLOR_ANGLE_A)
        self.formula_final[2].set_color(self.COLOR_ANGLE_B)
        self.formula_final[4].set_color(self.COLOR_ANGLE_C)
        
        self.play(TransformMatchingTex(formula_2, self.formula_final), run_time=1.2)
        self.wait(1.5)
        
        # 清理辅助元素
        self.play(
            FadeOut(explain_3),
            FadeOut(straight_angle_arc),
            FadeOut(straight_label),
            FadeOut(self.parallel_line),
            FadeOut(self.angle_A_copy),
            FadeOut(self.angle_B_copy),
            FadeOut(self.label_1),
            FadeOut(self.label_2),
            FadeOut(self.parallel_marks),
            run_time=0.6
        )
    
    # ==================== Scene 5: 回到原三角形 ====================
    def scene_5_back_to_triangle(self):
        """强调定理的普遍性"""
        # 公式移到顶部
        self.play(
            self.formula_final.animate.move_to(UP * 6).scale(0.9),
            run_time=0.8
        )
        
        # 三角形居中并稍微放大
        self.play(
            self.triangle.animate.scale(1.15).move_to(UP * 0.5),
            self.label_A.animate.next_to(self.A * 1.15 + UP * 0.5 - UP * 0.5 * 1.15, UP + LEFT, buff=0.15),
            self.label_B.animate.next_to(self.B * 1.15 + UP * 0.5 - UP * 0.5 * 1.15, DOWN + RIGHT, buff=0.15),
            self.label_C.animate.next_to(self.C * 1.15 + UP * 0.5 - UP * 0.5 * 1.15, DOWN + LEFT, buff=0.15),
            run_time=1.0
        )
        
        # 三角形填充
        self.play(
            self.triangle.animate.set_fill(self.COLOR_PRIMARY, opacity=0.15),
            run_time=0.8
        )
        
        # 三个角依次闪烁
        self.play(Flash(self.angle_arc_A, color=self.COLOR_ANGLE_A, flash_radius=0.4), run_time=0.4)
        self.play(Flash(self.angle_arc_B, color=self.COLOR_ANGLE_B, flash_radius=0.4), run_time=0.4)
        self.play(Flash(self.angle_arc_C, color=self.COLOR_ANGLE_C, flash_radius=0.4), run_time=0.4)
        
        # 结论文字
        conclusion = Text(
            "任意三角形都成立!",
            font="PingFang SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 4.5)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.2)
        
        # 公式加框
        formula_box = SurroundingRectangle(
            self.formula_final,
            color=GOLD,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(formula_box), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(conclusion),
            FadeOut(formula_box),
            FadeOut(self.triangle),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_C),
            FadeOut(self.angle_arc_A),
            FadeOut(self.angle_arc_B),
            FadeOut(self.angle_arc_C),
            run_time=0.6
        )
    
    # ==================== Scene 6: 推论展示 ====================
    def scene_6_corollaries(self):
        """展示重要推论"""
        # 推论标题
        corollary_title = Text(
            "重要推论",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(corollary_title), run_time=0.8)
        
        # 推论1卡片
        corollary_1_title = Text(
            "推论1:",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        
        corollary_1_content = Text(
            "直角三角形两锐角互余",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        
        corollary_1_formula = MathTex(
            r"\angle A + \angle B = 90^\circ",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        )
        
        corollary_1 = VGroup(
            corollary_1_title,
            corollary_1_content,
            corollary_1_formula
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(LEFT * 3 + UP * 1.5)
        
        self.play(FadeIn(corollary_1, shift=RIGHT * 0.5), run_time=1.0)
        
        # 推论2卡片
        corollary_2_title = Text(
            "推论2:",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        
        corollary_2_content = Text(
            "外角等于不相邻两内角之和",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        corollary_2 = VGroup(
            corollary_2_title,
            corollary_2_content
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(LEFT * 3 + DOWN * 0.5)
        
        self.play(FadeIn(corollary_2, shift=RIGHT * 0.5), run_time=1.0)
        
        # 右侧示例：直角三角形
        rt_A = np.array([1.5, 0.8, 0])
        rt_B = np.array([3.0, 0.8, 0])
        rt_C = np.array([3.0, -0.5, 0])
        
        right_triangle = Polygon(
            rt_A, rt_B, rt_C,
            color=self.COLOR_PRIMARY,
            stroke_width=2
        )
        
        # 直角标记
        right_angle_mark = RightAngle(
            Line(rt_B, rt_A),
            Line(rt_B, rt_C),
            length=0.2,
            color=YELLOW
        )
        
        # 90度标注
        right_label = MathTex(r"90^\circ", font_size=20).next_to(rt_B, DOWN + LEFT, buff=0.15)
        
        self.play(
            Create(right_triangle),
            Create(right_angle_mark),
            FadeIn(right_label),
            run_time=1.2
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(corollary_title),
            FadeOut(corollary_1),
            FadeOut(corollary_2),
            FadeOut(right_triangle),
            FadeOut(right_angle_mark),
            FadeOut(right_label),
            run_time=0.6
        )
    
    # ==================== Scene 7: 片尾关注 ====================
    def scene_7_outro(self):
        """品牌展示，引导关注"""
        # 清空保留的公式
        self.play(FadeOut(self.formula_final), run_time=0.4)
        
        # 作者名放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Transform(self.author_info, author_large), run_time=0.8)
        
        # ID
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id), run_time=0.6)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰三角形
        decorative_triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.4)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(tri, scale=0.5) for tri in decorative_triangles], run_time=0.8)
        self.play(Rotate(decorative_triangles, angle=PI, run_time=1.5))
        
        # 核心公式回顾
        formula_reminder = MathTex(
            r"\angle A + \angle B + \angle C = 180^\circ",
            font_size=38,
            color=GOLD
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(formula_reminder, scale=1.1), run_time=0.8)
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorative_triangles),
            FadeOut(formula_reminder),
            run_time=1.0
        )


# ==================== 渲染说明 ====================
"""
运行命令:

# 快速预览（低质量）
manim -pql triangle_angle_sum.py TriangleAngleSum

# 高质量渲染（推荐TikTok上传）
manim -qh triangle_angle_sum.py TriangleAngleSum

# 4K质量
manim -qk triangle_angle_sum.py TriangleAngleSum
"""