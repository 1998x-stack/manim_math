"""
全等三角形的概念与性质 - Manim教学动画
Congruent Triangles: Concept and Properties

内容: 全等三角形的定义、符号、对应边相等、对应角相等
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


class CongruentTriangles(Scene):
    """
    全等三角形教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义介绍
    3. 重合演示
    4. 全等符号
    5. 对应边相等
    6. 对应角相等
    7. 总结片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE_1 = "#3498db"      # 蓝色
        self.COLOR_TRIANGLE_2 = "#e74c3c"      # 红色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_EQUAL_MARK = "#2ecc71"      # 绿色
        
        # 字体大小
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 24,
            "small": 18,
            "author": 20,
            "formula": 32,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_overlap()
        self.scene_4_symbol()
        self.scene_5_equal_sides()
        self.scene_6_equal_angles()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        print("\n" + "="*50)
        print("初始化几何数据...")
        print("="*50)
        
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # ========== 三角形1 (ABC) - 左侧 ==========
        # 定义一个锐角三角形
        self.A1 = np.array([-3.5, -1.0, 0]) * self.SCALE + self.OFFSET
        self.B1 = np.array([-1.0, -1.0, 0]) * self.SCALE + self.OFFSET
        self.C1 = np.array([-2.0, 1.2, 0]) * self.SCALE + self.OFFSET
        
        # 计算边长
        self.AB1_length = np.linalg.norm(self.B1 - self.A1)
        self.BC1_length = np.linalg.norm(self.C1 - self.B1)
        self.CA1_length = np.linalg.norm(self.A1 - self.C1)
        
        # 计算角度（弧度）
        self.angle_A1 = self.calculate_angle(self.C1, self.A1, self.B1)
        self.angle_B1 = self.calculate_angle(self.A1, self.B1, self.C1)
        self.angle_C1 = self.calculate_angle(self.B1, self.C1, self.A1)
        
        print(f"\n三角形1 (ABC):")
        print(f"  顶点A1: {self.A1[:2]}")
        print(f"  顶点B1: {self.B1[:2]}")
        print(f"  顶点C1: {self.C1[:2]}")
        print(f"  边长: AB={self.AB1_length:.4f}, BC={self.BC1_length:.4f}, CA={self.CA1_length:.4f}")
        print(f"  角度: ∠A={np.degrees(self.angle_A1):.2f}°, ∠B={np.degrees(self.angle_B1):.2f}°, ∠C={np.degrees(self.angle_C1):.2f}°")
        
        # ========== 三角形2 (DEF) - 使用旋转+平移确保全等 ==========
        # 旋转角度和平移向量
        rotation_angle = 25 * DEGREES  # 旋转25度
        translation = np.array([4.5, 0.3, 0])
        
        # 使用旋转矩阵生成全等三角形
        vertices_1 = [self.A1, self.B1, self.C1]
        vertices_2 = self.create_congruent_triangle(vertices_1, rotation_angle, translation)
        
        self.D2, self.E2, self.F2 = vertices_2
        
        print(f"\n三角形2 (DEF):")
        print(f"  顶点D2: {self.D2[:2]}")
        print(f"  顶点E2: {self.E2[:2]}")
        print(f"  顶点F2: {self.F2[:2]}")
        
        # ========== 验证全等性 ==========
        self.verify_congruence()
        
        # ========== 创建Manim对象（但不添加到场景）==========
        self.triangle_1 = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=3
        )
        
        self.triangle_2 = Polygon(
            self.D2, self.E2, self.F2,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=3
        )
        
        print("\n✓ 几何初始化完成")
        print("="*50 + "\n")
    
    def create_congruent_triangle(self, original_vertices, rotation_angle, translation):
        """
        创建全等三角形
        
        参数:
            original_vertices: 原三角形顶点列表 [A, B, C]
            rotation_angle: 旋转角度（弧度）
            translation: 平移向量
        """
        # 计算原三角形中心
        center = np.mean(original_vertices, axis=0)
        
        # 2D旋转矩阵
        cos_a = np.cos(rotation_angle)
        sin_a = np.sin(rotation_angle)
        
        new_vertices = []
        for vertex in original_vertices:
            # 移到原点
            centered = vertex - center
            
            # 旋转（只旋转x和y）
            rotated_x = centered[0] * cos_a - centered[1] * sin_a
            rotated_y = centered[0] * sin_a + centered[1] * cos_a
            rotated = np.array([rotated_x, rotated_y, 0])
            
            # 移回并平移
            translated = rotated + center + translation
            new_vertices.append(translated)
        
        return new_vertices
    
    def calculate_angle(self, point1, vertex, point2):
        """
        计算∠point1-vertex-point2的角度（弧度）
        顶点是vertex
        """
        v1 = point1 - vertex
        v2 = point2 - vertex
        
        # 使用atan2计算角度
        cos_angle = np.dot(v1[:2], v2[:2]) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        
        return np.arccos(cos_angle)
    
    def verify_congruence(self):
        """验证两个三角形全等"""
        epsilon = 1e-5
        errors = []
        
        # 验证边长
        DE_length = np.linalg.norm(self.E2 - self.D2)
        EF_length = np.linalg.norm(self.F2 - self.E2)
        FD_length = np.linalg.norm(self.D2 - self.F2)
        
        if abs(self.AB1_length - DE_length) > epsilon:
            errors.append(f"边长AB≠DE: {self.AB1_length:.6f} vs {DE_length:.6f}")
        
        if abs(self.BC1_length - EF_length) > epsilon:
            errors.append(f"边长BC≠EF: {self.BC1_length:.6f} vs {EF_length:.6f}")
        
        if abs(self.CA1_length - FD_length) > epsilon:
            errors.append(f"边长CA≠FD: {self.CA1_length:.6f} vs {FD_length:.6f}")
        
        # 验证角度
        angle_D2 = self.calculate_angle(self.F2, self.D2, self.E2)
        angle_E2 = self.calculate_angle(self.D2, self.E2, self.F2)
        angle_F2 = self.calculate_angle(self.E2, self.F2, self.D2)
        
        if abs(self.angle_A1 - angle_D2) > epsilon:
            errors.append(f"角度A≠D: {np.degrees(self.angle_A1):.2f}° vs {np.degrees(angle_D2):.2f}°")
        
        if abs(self.angle_B1 - angle_E2) > epsilon:
            errors.append(f"角度B≠E: {np.degrees(self.angle_B1):.2f}° vs {np.degrees(angle_E2):.2f}°")
        
        if abs(self.angle_C1 - angle_F2) > epsilon:
            errors.append(f"角度C≠F: {np.degrees(self.angle_C1):.2f}° vs {np.degrees(angle_F2):.2f}°")
        
        # 输出结果
        if errors:
            print("\n❌ 全等性验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("三角形不全等！")
        else:
            print("✓ 全等性验证通过: 所有对应边和对应角相等")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        print("\n[Scene 1] 开场钩子")
        
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["author"],
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这两个三角形一样吗？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 两个三角形轮廓闪现
        tri1_outline = self.triangle_1.copy().set_fill(opacity=0.2)
        tri2_outline = self.triangle_2.copy().set_fill(opacity=0.2)
        
        self.play(
            FadeIn(tri1_outline, shift=DOWN * 0.5),
            FadeIn(tri2_outline, shift=DOWN * 0.5),
            lag_ratio=0.3,
            run_time=0.6
        )
        
        # 问号
        question_mark = Text(
            "?",
            font_size=72,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN + DOWN * 0.5)
        
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.3)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.2)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            FadeOut(tri1_outline),
            FadeOut(tri2_outline),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 定义介绍"""
        print("\n[Scene 2] 定义介绍")
        
        # 定义文字
        definition = Text(
            "能够完全重合的两个三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE
        ).move_to(UP * 5.5)
        
        definition_2 = Text(
            "叫做全等三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(definition, DOWN, buff=0.3)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.play(FadeIn(definition_2), run_time=0.5)
        
        # 三角形1
        self.play(Create(self.triangle_1), run_time=1.0)
        
        # 标签A, B, C
        label_A = Text("A", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.A1, LEFT, buff=0.15)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.B1, RIGHT, buff=0.15)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.C1, UP, buff=0.15)
        
        self.labels_1 = VGroup(label_A, label_B, label_C)
        
        self.play(Write(self.labels_1), run_time=0.6)
        
        # 三角形2
        self.play(Create(self.triangle_2), run_time=1.0)
        
        # 标签D, E, F
        label_D = Text("D", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.D2, LEFT, buff=0.15)
        label_E = Text("E", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.E2, RIGHT, buff=0.15)
        label_F = Text("F", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE).next_to(self.F2, UP, buff=0.15)
        
        self.labels_2 = VGroup(label_D, label_E, label_F)
        
        self.play(Write(self.labels_2), run_time=0.6)
        
        self.wait(0.5)
        
        # 清理定义文字
        self.play(
            FadeOut(definition),
            FadeOut(definition_2),
            run_time=0.4
        )
    
    def scene_3_overlap(self):
        """场景3: 重合演示"""
        print("\n[Scene 3] 重合演示")
        
        # 说明文字
        overlap_text = Text(
            "看！它们可以完全重合",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(overlap_text), run_time=0.4)
        
        # 高亮三角形2
        self.play(
            self.triangle_2.animate.set_stroke(self.COLOR_HIGHLIGHT, width=5),
            run_time=0.3
        )
        
        # 创建三角形2的副本用于移动
        tri2_copy = self.triangle_2.copy()
        labels_2_copy = self.labels_2.copy()
        
        self.add(tri2_copy, labels_2_copy)
        
        # 计算变换参数
        center_1 = (self.A1 + self.B1 + self.C1) / 3
        center_2 = (self.D2 + self.E2 + self.F2) / 3
        
        # Step 1: 移动到三角形1的中心
        translation = center_1 - center_2
        
        self.play(
            tri2_copy.animate.shift(translation),
            labels_2_copy.animate.shift(translation),
            run_time=1.5
        )
        
        # Step 2: 旋转对齐
        # 计算需要的旋转角度
        vec_AB = self.B1 - self.A1
        D2_new = self.D2 + translation
        E2_new = self.E2 + translation
        vec_DE = E2_new - D2_new
        
        # 计算旋转角度
        angle_AB = np.arctan2(vec_AB[1], vec_AB[0])
        angle_DE = np.arctan2(vec_DE[1], vec_DE[0])
        rotation_needed = angle_AB - angle_DE
        
        print(f"  旋转角度: {np.degrees(rotation_needed):.2f}°")
        
        self.play(
            Rotate(tri2_copy, rotation_needed, about_point=center_1),
            Rotate(labels_2_copy, rotation_needed, about_point=center_1),
            run_time=1.0
        )
        
        # Step 3: 完全重合效果
        self.play(
            Flash(tri2_copy, color=self.COLOR_HIGHLIGHT, flash_radius=0.5, line_length=0.3),
            run_time=0.4
        )
        
        # 改变副本颜色以显示重合
        self.play(
            tri2_copy.animate.set_stroke(self.COLOR_TRIANGLE_1, width=3),
            run_time=0.3
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(tri2_copy),
            FadeOut(labels_2_copy),
            FadeOut(overlap_text),
            self.triangle_2.animate.set_stroke(self.COLOR_TRIANGLE_2, width=3),
            run_time=0.6
        )
    
    def scene_4_symbol(self):
        """场景4: 全等符号"""
        print("\n[Scene 4] 全等符号")
        
        # 标题
        title = Text(
            "全等符号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 全等表达式
        congruent_expr = MathTex(
            r"\triangle", "ABC", r"\cong", r"\triangle", "DEF",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(UP * 4.2)
        
        # 分步书写
        self.play(Write(congruent_expr[0:2]), run_time=0.8)  # △ABC
        self.wait(0.2)
        self.play(Write(congruent_expr[2]), run_time=0.5)    # ≌
        self.wait(0.2)
        self.play(Write(congruent_expr[3:5]), run_time=0.8)  # △DEF
        
        # 对应关系箭头
        # 需要获取标签位置
        label_A_pos = self.labels_1[0].get_center()
        label_B_pos = self.labels_1[1].get_center()
        label_C_pos = self.labels_1[2].get_center()
        label_D_pos = self.labels_2[0].get_center()
        label_E_pos = self.labels_2[1].get_center()
        label_F_pos = self.labels_2[2].get_center()
        
        arrow_A_D = Arrow(
            label_A_pos, label_D_pos,
            buff=0.2,
            color=self.COLOR_EQUAL_MARK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow_B_E = Arrow(
            label_B_pos, label_E_pos,
            buff=0.2,
            color=self.COLOR_EQUAL_MARK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow_C_F = Arrow(
            label_C_pos, label_F_pos,
            buff=0.2,
            color=self.COLOR_EQUAL_MARK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrows = VGroup(arrow_A_D, arrow_B_E, arrow_C_F)
        
        self.play(Create(arrows), run_time=1.2)
        
        # 强调提示
        warning_text = Text(
            "注意: 对应顺序很重要！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(warning_text, shift=UP * 0.3), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理（保留全等表达式，移到顶部）
        self.play(
            FadeOut(title),
            FadeOut(arrows),
            FadeOut(warning_text),
            congruent_expr.animate.scale(0.7).move_to(UP * 6.5),
            run_time=0.6
        )
        
        # 保存表达式供后续使用
        self.congruent_expr = congruent_expr
    
    def scene_5_equal_sides(self):
        """场景5: 对应边相等"""
        print("\n[Scene 5] 对应边相等")
        
        # 标题
        property_title = Text(
            "性质1: 对应边相等",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(property_title), run_time=0.4)
        
        # 等式组（放在底部）
        equations_group = VGroup()
        
        # ===== 边AB和DE =====
        self.play(
            Indicate(Line(self.A1, self.B1), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            Indicate(Line(self.D2, self.E2), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.8
        )
        
        # 添加刻度标记
        tick_AB = self.create_tick_marks(self.A1, self.B1, num_ticks=1, color=self.COLOR_EQUAL_MARK)
        tick_DE = self.create_tick_marks(self.D2, self.E2, num_ticks=1, color=self.COLOR_EQUAL_MARK)
        
        self.play(Create(tick_AB), Create(tick_DE), run_time=0.5)
        
        # 等式
        eq1 = MathTex("AB", "=", "DE", font_size=self.FONT_SIZES["body"]).move_to(DOWN * 4.0)
        equations_group.add(eq1)
        
        self.play(Write(eq1), run_time=0.6)
        self.wait(0.3)
        
        # ===== 边BC和EF =====
        self.play(
            Indicate(Line(self.B1, self.C1), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            Indicate(Line(self.E2, self.F2), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.8
        )
        
        # 添加双刻度标记
        tick_BC = self.create_tick_marks(self.B1, self.C1, num_ticks=2, color=self.COLOR_EQUAL_MARK)
        tick_EF = self.create_tick_marks(self.E2, self.F2, num_ticks=2, color=self.COLOR_EQUAL_MARK)
        
        self.play(Create(tick_BC), Create(tick_EF), run_time=0.5)
        
        # 等式
        eq2 = MathTex("BC", "=", "EF", font_size=self.FONT_SIZES["body"]).next_to(eq1, DOWN, buff=0.3)
        equations_group.add(eq2)
        
        self.play(Write(eq2), run_time=0.6)
        self.wait(0.3)
        
        # ===== 边CA和FD =====
        self.play(
            Indicate(Line(self.C1, self.A1), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            Indicate(Line(self.F2, self.D2), color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.8
        )
        
        # 添加三刻度标记
        tick_CA = self.create_tick_marks(self.C1, self.A1, num_ticks=3, color=self.COLOR_EQUAL_MARK)
        tick_FD = self.create_tick_marks(self.F2, self.D2, num_ticks=3, color=self.COLOR_EQUAL_MARK)
        
        self.play(Create(tick_CA), Create(tick_FD), run_time=0.5)
        
        # 等式
        eq3 = MathTex("CA", "=", "FD", font_size=self.FONT_SIZES["body"]).next_to(eq2, DOWN, buff=0.3)
        equations_group.add(eq3)
        
        self.play(Write(eq3), run_time=0.6)
        
        self.wait(1.5)
        
        # 保存刻度标记
        self.tick_marks = VGroup(tick_AB, tick_DE, tick_BC, tick_EF, tick_CA, tick_FD)
        
        # 清理
        self.play(
            FadeOut(property_title),
            FadeOut(equations_group),
            run_time=0.5
        )
    
    def create_tick_marks(self, line_start, line_end, num_ticks=1, color=GREEN):
        """
        在线段上创建垂直刻度标记
        
        参数:
            line_start, line_end: 线段端点
            num_ticks: 刻度数量 (1, 2, 3)
            color: 颜色
        """
        direction = line_end - line_start
        direction_normalized = direction / np.linalg.norm(direction)
        perpendicular = np.array([-direction_normalized[1], direction_normalized[0], 0])
        
        tick_length = 0.15
        midpoint = (line_start + line_end) / 2
        
        ticks = VGroup()
        spacing = 0.12
        
        for i in range(num_ticks):
            offset = (i - (num_ticks - 1) / 2) * spacing * direction_normalized
            tick = Line(
                midpoint + offset - perpendicular * tick_length / 2,
                midpoint + offset + perpendicular * tick_length / 2,
                color=color,
                stroke_width=3
            )
            ticks.add(tick)
        
        return ticks
    
    def scene_6_equal_angles(self):
        """场景6: 对应角相等"""
        print("\n[Scene 6] 对应角相等")
        
        # 标题
        angle_title = Text(
            "性质2: 对应角相等",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(angle_title), run_time=0.4)
        
        # 等式组
        angle_equations = VGroup()
        
        # ===== 角A和角D =====
        # 创建角度弧
        arc_A, arc_D = self.create_angle_arcs_pair(
            self.C1, self.A1, self.B1,  # 角A
            self.F2, self.D2, self.E2,  # 角D
            radius=0.35,
            num_arcs=1
        )
        
        self.play(Create(arc_A), Create(arc_D), run_time=0.8)
        
        # 等式
        angle_eq1 = MathTex(r"\angle A", "=", r"\angle D", font_size=self.FONT_SIZES["body"]).move_to(DOWN * 4.0)
        angle_equations.add(angle_eq1)
        
        self.play(Write(angle_eq1), run_time=0.6)
        self.wait(0.3)
        
        # ===== 角B和角E =====
        arc_B, arc_E = self.create_angle_arcs_pair(
            self.A1, self.B1, self.C1,  # 角B
            self.D2, self.E2, self.F2,  # 角E
            radius=0.35,
            num_arcs=2
        )
        
        self.play(Create(arc_B), Create(arc_E), run_time=0.8)
        
        # 等式
        angle_eq2 = MathTex(r"\angle B", "=", r"\angle E", font_size=self.FONT_SIZES["body"]).next_to(angle_eq1, DOWN, buff=0.3)
        angle_equations.add(angle_eq2)
        
        self.play(Write(angle_eq2), run_time=0.6)
        self.wait(0.3)
        
        # ===== 角C和角F =====
        arc_C, arc_F = self.create_angle_arcs_pair(
            self.B1, self.C1, self.A1,  # 角C
            self.E2, self.F2, self.D2,  # 角F
            radius=0.35,
            num_arcs=3
        )
        
        self.play(Create(arc_C), Create(arc_F), run_time=0.8)
        
        # 等式
        angle_eq3 = MathTex(r"\angle C", "=", r"\angle F", font_size=self.FONT_SIZES["body"]).next_to(angle_eq2, DOWN, buff=0.3)
        angle_equations.add(angle_eq3)
        
        self.play(Write(angle_eq3), run_time=0.6)
        
        self.wait(1.5)
        
        # 保存角度弧
        self.angle_arcs = VGroup(arc_A, arc_D, arc_B, arc_E, arc_C, arc_F)
        
        # 清理
        self.play(
            FadeOut(angle_title),
            FadeOut(angle_equations),
            run_time=0.5
        )
    
    def create_angle_arcs_pair(self, point1_a, vertex_a, point2_a, point1_b, vertex_b, point2_b, radius=0.4, num_arcs=1):
        """
        创建一对对应角的角度弧（带多重弧标记）
        
        参数:
            point1_a, vertex_a, point2_a: 第一个角的三个点
            point1_b, vertex_b, point2_b: 第二个角的三个点
            radius: 弧半径
            num_arcs: 弧的数量 (1=单弧, 2=双弧, 3=三弧)
        """
        arc_a = self.create_angle_arc_safe(point1_a, vertex_a, point2_a, radius, self.COLOR_HIGHLIGHT)
        arc_b = self.create_angle_arc_safe(point1_b, vertex_b, point2_b, radius, self.COLOR_HIGHLIGHT)
        
        # 创建多重弧
        if num_arcs > 1:
            arc_a = self.create_multi_arc_mark(arc_a, num_arcs, spacing=0.08)
            arc_b = self.create_multi_arc_mark(arc_b, num_arcs, spacing=0.08)
        
        return arc_a, arc_b
    
    def create_angle_arc_safe(self, point1, vertex, point2, radius, color):
        """
        安全创建角度弧，自动处理方向问题
        
        ⚠️ 重点：处理大于90度和大于180度的角
        """
        # 计算两个向量
        v1 = point1 - vertex
        v2 = point2 - vertex
        
        # 计算夹角
        dot_product = np.dot(v1[:2], v2[:2])
        cross_product = v1[0] * v2[1] - v1[1] * v2[0]  # z分量
        
        angle_rad = np.arctan2(cross_product, dot_product)
        
        # 标准化到 [0, 2π)
        if angle_rad < 0:
            angle_rad += 2 * PI
        
        # 判断是否需要使用 other_angle
        use_other_angle = False
        
        if angle_rad > PI:
            # 角度大于180度
            print(f"  ⚠️ WARNING: 角度 {np.degrees(angle_rad):.1f}° > 180°，使用补角")
            use_other_angle = True
        elif angle_rad > PI / 2:
            # 角度在90-180度之间
            print(f"  INFO: 角度 {np.degrees(angle_rad):.1f}° 在90-180度之间")
            use_other_angle = False
        
        # 创建角度弧
        line1 = Line(vertex, point1)
        line2 = Line(vertex, point2)
        
        try:
            arc = Angle(
                line1, line2,
                radius=radius,
                quadrant=(1, 1),
                other_angle=use_other_angle,
                color=color,
                stroke_width=3
            )
        except Exception as e:
            print(f"  ❌ 创建角度弧失败: {e}")
            # 降级方案：使用 Arc
            start_angle = np.arctan2(v1[1], v1[0])
            arc = Arc(
                radius=radius,
                start_angle=start_angle,
                angle=angle_rad if not use_other_angle else (2*PI - angle_rad),
                color=color,
                stroke_width=3
            ).move_to(vertex)
        
        return arc
    
    def create_multi_arc_mark(self, arc, num_arcs, spacing=0.08):
        """
        创建多重弧标记
        
        参数:
            arc: 原始弧
            num_arcs: 弧的数量
            spacing: 弧之间的间距
        """
        arcs = VGroup()
        
        for i in range(num_arcs):
            arc_copy = arc.copy()
            # 缩放以创建多重效果
            scale_factor = 1 + i * spacing / 0.4  # 假设原始半径为0.4
            arc_copy.scale(scale_factor, about_point=arc.get_arc_center())
            arcs.add(arc_copy)
        
        return arcs
    
    def scene_7_outro(self):
        """场景7: 总结和片尾"""
        print("\n[Scene 7] 总结和片尾")
        
        # 三角形和标记缩小到角落
        all_elements = VGroup(
            self.triangle_1,
            self.triangle_2,
            self.labels_1,
            self.labels_2,
            self.tick_marks,
            self.angle_arcs
        )
        
        self.play(
            all_elements.animate.scale(0.4).to_corner(UL, buff=0.5),
            run_time=0.8
        )
        
        # 知识点卡片
        cards = VGroup()
        
        card_1 = self.create_summary_card(
            "定义",
            "能完全重合的两个三角形",
            self.COLOR_TRIANGLE_1,
            UP * 1.5
        )
        cards.add(card_1)
        
        card_2 = self.create_summary_card(
            "符号",
            "△ABC ≌ △DEF",
            self.COLOR_TRIANGLE_2,
            UP * 0.3
        )
        cards.add(card_2)
        
        card_3 = self.create_summary_card(
            "性质1",
            "对应边相等",
            self.COLOR_EQUAL_MARK,
            DOWN * 0.9
        )
        cards.add(card_3)
        
        card_4 = self.create_summary_card(
            "性质2",
            "对应角相等",
            self.COLOR_HIGHLIGHT,
            DOWN * 2.1
        )
        cards.add(card_4)
        
        card_5 = self.create_summary_card(
            "关键",
            "对应顺序很重要！",
            "#9b59b6",
            DOWN * 3.3
        )
        cards.add(card_5)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        # 依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 高亮每张卡片
        for card in cards:
            self.play(Indicate(card, scale_factor=1.05), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理卡片
        self.play(FadeOut(cards), FadeOut(all_elements), run_time=0.5)
        
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
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何知识！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三角形装饰
        triangles_deco = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=self.COLOR_EQUAL_MARK, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles_deco],
            run_time=0.6
        )
        self.play(Rotate(triangles_deco, angle=PI, run_time=1.5))
        
        # 全等符号闪烁
        if hasattr(self, 'congruent_expr'):
            self.play(
                self.congruent_expr.animate.scale(1.5).move_to(DOWN * 2.5),
                run_time=0.5
            )
            self.play(Flash(self.congruent_expr, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles_deco),
            FadeOut(self.congruent_expr) if hasattr(self, 'congruent_expr') else Wait(0),
            run_time=1.0
        )
        
        print("\n✓ 动画渲染完成")
    
    def create_summary_card(self, title, content, color, position):
        """创建知识点卡片"""
        # 图标
        icon = Circle(radius=0.2, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_AUXILIARY
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql congruent_triangles.py CongruentTriangles  # 快速预览
# manim -qh congruent_triangles.py CongruentTriangles   # 高质量 1080p
# manim -qk congruent_triangles.py CongruentTriangles   # 4K质量