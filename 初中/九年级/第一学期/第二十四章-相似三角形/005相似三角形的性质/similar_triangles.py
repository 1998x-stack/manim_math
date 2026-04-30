"""
相似三角形的性质 - Similar Triangles Properties
使用 Manim 创建的九年级数学教学视频

知识点: 相似三角形的性质
- 对应角相等，对应边成比例
- 对应高、中线、角平分线之比 = 相似比 k
- 周长比 = k
- 面积比 = k²

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from manim.utils.unit import *

from manim import *
import numpy as np
from manim.utils.unit import *


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SimilarTrianglesProperties(Scene):
    """
    相似三角形性质教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义相似三角形
    3. 性质1: 对应边成比例
    4. 性质2: 对应高之比
    5. 性质3: 对应中线/角平分线之比
    6. 性质4: 周长比和面积比
    7. 总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 原三角形
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 相似三角形
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_FORMULA = WHITE          # 白色 - 公式
        
        # 相似比
        self.k = 0.6
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_edge_ratios()
        self.show_altitude_ratio()
        self.show_median_bisector_ratio()
        self.show_perimeter_area_ratio()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ========== 原三角形 ABC ==========
        self.SCALE = 0.85
        self.OFFSET = np.array([0, 1.5, 0])
        
        A_base = np.array([-2.5, 1, 0])
        B_base = np.array([2.5, -1, 0])
        C_base = np.array([0, 2.5, 0])
        
        self.A = A_base * self.SCALE + self.OFFSET
        self.B = B_base * self.SCALE + self.OFFSET
        self.C = C_base * self.SCALE + self.OFFSET
        
        # 边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # 周长和面积
        self.perimeter = self.a + self.b + self.c
        s = self.perimeter / 2
        self.area = np.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        
        # 高
        self.foot_A = self.foot_of_perpendicular(self.A, self.B, self.C)
        self.h_A = np.linalg.norm(self.A - self.foot_A)
        
        # 中线
        self.M_BC = (self.B + self.C) / 2
        self.m_A = np.linalg.norm(self.A - self.M_BC)
        
        # 角平分线交点
        t = self.c / (self.b + self.c)
        self.D_bisector = self.B + t * (self.C - self.B)
        self.l_A = np.linalg.norm(self.A - self.D_bisector)
        
        # ========== 相似三角形 A'B'C' ==========
        # 调整位置以确保在边界内
        centroid_ABC = (self.A + self.B + self.C) / 3
        
        # 中心化、缩放、旋转
        A_centered = self.A - centroid_ABC
        B_centered = self.B - centroid_ABC
        C_centered = self.C - centroid_ABC
        
        A_scaled = A_centered * self.k
        B_scaled = B_centered * self.k
        C_scaled = C_centered * self.k
        
        rotation_angle = np.radians(15)
        rotation_matrix = np.array([
            [np.cos(rotation_angle), -np.sin(rotation_angle), 0],
            [np.sin(rotation_angle), np.cos(rotation_angle), 0],
            [0, 0, 1]
        ])
        
        A_rotated = rotation_matrix @ A_scaled
        B_rotated = rotation_matrix @ B_scaled
        C_rotated = rotation_matrix @ C_scaled
        
        # 调整到安全位置（向左移动以避免超出边界）
        target_position = np.array([0.5, -3.8, 0])  # 调整后的位置
        offset_prime = target_position - A_rotated
        
        self.A_prime = A_rotated + offset_prime
        self.B_prime = B_rotated + offset_prime
        self.C_prime = C_rotated + offset_prime
        
        # 边长
        self.a_prime = np.linalg.norm(self.B_prime - self.C_prime)
        self.b_prime = np.linalg.norm(self.C_prime - self.A_prime)
        self.c_prime = np.linalg.norm(self.A_prime - self.B_prime)
        
        # 周长和面积
        self.perimeter_prime = self.a_prime + self.b_prime + self.c_prime
        s_prime = self.perimeter_prime / 2
        self.area_prime = np.sqrt(s_prime * (s_prime - self.a_prime) * 
                                   (s_prime - self.b_prime) * (s_prime - self.c_prime))
        
        # 高
        self.foot_A_prime = self.foot_of_perpendicular(self.A_prime, self.B_prime, self.C_prime)
        self.h_A_prime = np.linalg.norm(self.A_prime - self.foot_A_prime)
        
        # 中线
        self.M_BC_prime = (self.B_prime + self.C_prime) / 2
        self.m_A_prime = np.linalg.norm(self.A_prime - self.M_BC_prime)
        
        # 角平分线交点
        t_prime = self.c_prime / (self.b_prime + self.c_prime)
        self.D_bisector_prime = self.B_prime + t_prime * (self.C_prime - self.B_prime)
        self.l_A_prime = np.linalg.norm(self.A_prime - self.D_bisector_prime)
        
        # 验证
        self.verify_geometry()
    
    @staticmethod
    def foot_of_perpendicular(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + projection * line_vec
    
    def verify_geometry(self):
        """验证几何关系"""
        eps = 1e-6
        
        # 验证边长比
        ratio_a = self.a_prime / self.a
        ratio_b = self.b_prime / self.b
        ratio_c = self.c_prime / self.c
        
        assert abs(ratio_a - self.k) < eps, f"Edge ratio error: a'/a={ratio_a:.6f}"
        assert abs(ratio_b - self.k) < eps, f"Edge ratio error: b'/b={ratio_b:.6f}"
        assert abs(ratio_c - self.k) < eps, f"Edge ratio error: c'/c={ratio_c:.6f}"
        
        # 验证面积比
        ratio_area = self.area_prime / self.area
        assert abs(ratio_area - self.k**2) < eps, f"面积比错误: S'/S={ratio_area:.6f}"
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
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
            "两个形状一样的三角形\n有什么神奇的关系？",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 创建两个三角形
        self.triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.triangle_A_prime = Polygon(
            self.A_prime, self.B_prime, self.C_prime,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        self.play(Create(self.triangle_ABC), run_time=0.8)
        self.play(Create(self.triangle_A_prime), run_time=0.8)
        
        # 闪烁
        self.play(
            Flash(self.triangle_ABC.get_center(), color=self.COLOR_PRIMARY, flash_radius=1.5),
            Flash(self.triangle_A_prime.get_center(), color=self.COLOR_SECONDARY, flash_radius=1.0),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.5)
    
    def show_definition(self):
        """场景2: 定义相似三角形"""
        # 标题
        title = Text(
            "相似三角形",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.2)
        
        definition = Text(
            "形状相同，大小可以不同",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        self.play(Write(definition), run_time=1.0)
        
        # 相似符号
        similarity_symbol = MathTex(
            r"\triangle ABC \sim \triangle A'B'C'",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.7)
        
        self.play(Write(similarity_symbol), run_time=0.8)
        
        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(self.A, LEFT, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(self.B, RIGHT, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(self.C, UP, buff=0.15)
        
        label_A_prime = Text("A'", font="PingFang SC", font_size=20, color=WHITE).next_to(self.A_prime, LEFT, buff=0.12)
        label_B_prime = Text("B'", font="PingFang SC", font_size=20, color=WHITE).next_to(self.B_prime, RIGHT, buff=0.12)
        label_C_prime = Text("C'", font="PingFang SC", font_size=20, color=WHITE).next_to(self.C_prime, UP, buff=0.12)
        
        self.play(
            Write(label_A), Write(label_B), Write(label_C),
            Write(label_A_prime), Write(label_B_prime), Write(label_C_prime),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(similarity_symbol),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(label_A_prime), FadeOut(label_B_prime), FadeOut(label_C_prime),
            run_time=0.6
        )
    
    def show_edge_ratios(self):
        """场景3: 对应边成比例"""
        # 标题
        title = Text(
            "性质1：对应边成比例",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 标注边长 - 使用 Brace
        # BC边
        brace_BC = Brace(Line(self.B, self.C), direction=RIGHT, buff=0.08, color=self.COLOR_PRIMARY)
        label_BC = DecimalNumber(self.a, num_decimal_places=1, font_size=20, color=WHITE).next_to(brace_BC, RIGHT, buff=0.05)
        
        # AB边
        brace_AB = Brace(Line(self.A, self.B), direction=DOWN, buff=0.08, color=self.COLOR_PRIMARY)
        label_AB = DecimalNumber(self.c, num_decimal_places=1, font_size=20, color=WHITE).next_to(brace_AB, DOWN, buff=0.05)
        
        self.play(
            FadeIn(brace_BC), FadeIn(label_BC),
            FadeIn(brace_AB), FadeIn(label_AB),
            run_time=1.2
        )
        
        # B'C'边
        brace_BC_prime = Brace(Line(self.B_prime, self.C_prime), direction=RIGHT, buff=0.08, color=self.COLOR_SECONDARY)
        label_BC_prime = DecimalNumber(self.a_prime, num_decimal_places=1, font_size=18, color=WHITE).next_to(brace_BC_prime, RIGHT, buff=0.05)
        
        # A'B'边
        brace_AB_prime = Brace(Line(self.A_prime, self.B_prime), direction=DOWN, buff=0.08, color=self.COLOR_SECONDARY)
        label_AB_prime = DecimalNumber(self.c_prime, num_decimal_places=1, font_size=18, color=WHITE).next_to(brace_AB_prime, DOWN, buff=0.05)
        
        self.play(
            FadeIn(brace_BC_prime), FadeIn(label_BC_prime),
            FadeIn(brace_AB_prime), FadeIn(label_AB_prime),
            run_time=1.2
        )
        
        # 公式
        formula = MathTex(
            r"\frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(formula), run_time=0.8)
        
        # 数值计算
        ratio_text = Text(
            f"{self.a_prime:.1f} ÷ {self.a:.1f} = {self.k:.1f}",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.3)
        
        self.play(Write(ratio_text), run_time=1.0)
        
        # 结论
        conclusion = Text(
            f"相似比 k = {self.k}",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 7.0)
        
        self.play(Write(conclusion), run_time=1.0)
        self.play(Flash(conclusion.get_center(), color=GOLD, flash_radius=0.8), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(brace_BC), FadeOut(label_BC),
            FadeOut(brace_AB), FadeOut(label_AB),
            FadeOut(brace_BC_prime), FadeOut(label_BC_prime),
            FadeOut(brace_AB_prime), FadeOut(label_AB_prime),
            FadeOut(formula),
            FadeOut(ratio_text),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_altitude_ratio(self):
        """场景4: 对应高之比"""
        # 标题
        title = Text(
            "性质2：对应高之比 = k",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # BC边高亮
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(bc_line), run_time=0.4)
        
        # 绘制高线
        altitude_A = DashedLine(
            self.A, self.foot_A,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(altitude_A), run_time=1.0)
        
        # 垂直符号
        right_angle_mark = self.create_right_angle_mark(
            self.foot_A, self.A, self.B, size=0.15
        )
        self.play(FadeIn(right_angle_mark), run_time=0.4)
        
        # 高度标注
        brace_h = Brace(altitude_A, direction=LEFT, buff=0.08, color=self.COLOR_PRIMARY)
        label_h = MathTex(r"h_A", font_size=22, color=WHITE).next_to(brace_h, LEFT, buff=0.05)
        
        self.play(FadeIn(brace_h), FadeIn(label_h), run_time=0.8)
        self.play(bc_line.animate.set_color(self.COLOR_PRIMARY), run_time=0.3)
        
        # B'C'边高亮
        bc_prime_line = Line(self.B_prime, self.C_prime, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(bc_prime_line), run_time=0.4)
        
        # 绘制高线
        altitude_A_prime = DashedLine(
            self.A_prime, self.foot_A_prime,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(altitude_A_prime), run_time=1.0)
        
        # 高度标注
        brace_h_prime = Brace(altitude_A_prime, direction=LEFT, buff=0.08, color=self.COLOR_SECONDARY)
        label_h_prime = MathTex(r"h_{A'}", font_size=20, color=WHITE).next_to(brace_h_prime, LEFT, buff=0.05)
        
        self.play(FadeIn(brace_h_prime), FadeIn(label_h_prime), run_time=0.8)
        self.play(bc_prime_line.animate.set_color(self.COLOR_SECONDARY), run_time=0.3)
        
        # 公式
        formula = MathTex(
            r"\frac{h_{A'}}{h_A} = k",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(formula), run_time=0.8)
        
        # 数值验证
        verification = Text(
            f"{self.h_A_prime:.2f} ÷ {self.h_A:.2f} = {self.k:.1f} ✓",
            font="PingFang SC",
            font_size=24,
            color=GOLD
        ).move_to(DOWN * 6.6)
        
        self.play(Write(verification), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(bc_line),
            FadeOut(bc_prime_line),
            FadeOut(altitude_A),
            FadeOut(altitude_A_prime),
            FadeOut(right_angle_mark),
            FadeOut(brace_h), FadeOut(label_h),
            FadeOut(brace_h_prime), FadeOut(label_h_prime),
            FadeOut(formula),
            FadeOut(verification),
            run_time=0.6
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = point1 - corner
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = point2 - corner
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
        return square
    
    def show_median_bisector_ratio(self):
        """场景5: 对应中线/角平分线之比"""
        # 标题
        title = Text(
            "对应中线之比 = k",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # BC中点
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        m_bc_label = Text("M", font="PingFang SC", font_size=18, color=WHITE).next_to(m_bc_dot, RIGHT, buff=0.08)
        
        self.play(FadeIn(m_bc_dot), FadeIn(m_bc_label), run_time=0.5)
        
        # 中线AM
        median_A = Line(self.A, self.M_BC, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(median_A), run_time=0.8)
        
        # B'C'中点
        m_bc_prime_dot = Dot(self.M_BC_prime, color=self.COLOR_AUXILIARY, radius=0.05)
        self.play(FadeIn(m_bc_prime_dot), run_time=0.5)
        
        # 中线A'M'
        median_A_prime = Line(self.A_prime, self.M_BC_prime, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(median_A_prime), run_time=0.8)
        
        # 公式
        formula = MathTex(
            r"\frac{m_{A'}}{m_A} = k",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(formula), run_time=1.0)
        
        # 补充说明
        note = Text(
            "同样地，角平分线之比也等于 k",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6.3)
        
        self.play(FadeIn(note), run_time=1.0)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(m_bc_dot), FadeOut(m_bc_label),
            FadeOut(m_bc_prime_dot),
            FadeOut(median_A),
            FadeOut(median_A_prime),
            FadeOut(formula),
            FadeOut(note),
            run_time=0.6
        )
    
    def show_perimeter_area_ratio(self):
        """场景6: 周长比和面积比"""
        # 标题
        title = Text(
            "周长比 = k，面积比 = k²",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 周长公式
        perimeter_formula = MathTex(
            r"L = a + b + c",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.3)
        
        self.play(Write(perimeter_formula), run_time=1.0)
        
        # 周长比
        ratio_perimeter = MathTex(
            rf"\frac{{L'}}{{L}} = \frac{{{self.perimeter_prime:.1f}}}{{{self.perimeter:.1f}}} = {self.k:.1f}",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(ratio_perimeter), run_time=1.0)
        
        # 过渡
        transition = Text(
            "而面积呢？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.7)
        
        self.play(FadeIn(transition), run_time=0.8)
        self.wait(0.5)
        
        # 填充面积
        fill_ABC = self.triangle_ABC.copy().set_fill(self.COLOR_PRIMARY, opacity=0.3)
        fill_A_prime = self.triangle_A_prime.copy().set_fill(self.COLOR_SECONDARY, opacity=0.3)
        
        self.play(FadeIn(fill_ABC), run_time=0.8)
        self.play(FadeIn(fill_A_prime), run_time=0.8)
        
        # 面积比公式
        area_formula = MathTex(
            rf"\frac{{S'}}{{S}} = k^2 = {self.k}^2 = {self.k**2:.2f}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5.5)
        
        self.play(Write(area_formula), run_time=1.2)
        
        # 强调
        emphasis = Text(
            "注意是平方！",
            font="PingFang SC",
            font_size=30,
            color=GOLD
        ).move_to(DOWN * 6.5)
        
        self.play(
            Write(emphasis),
            Flash(area_formula.get_center(), color=YELLOW, flash_radius=1.0),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(perimeter_formula),
            FadeOut(ratio_perimeter),
            FadeOut(transition),
            FadeOut(fill_ABC),
            FadeOut(fill_A_prime),
            FadeOut(area_formula),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结 + 片尾"""
        # 清除现有对象
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.triangle_A_prime),
            run_time=0.8
        )
        
        # 创建两个对比三角形作为视觉辅助
        triangle_left = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.5).move_to(LEFT * 3.5 + UP * 5)
        
        triangle_right = Polygon(
            self.A_prime, self.B_prime, self.C_prime,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).scale(0.5).move_to(RIGHT * 3.5 + UP * 5)
        
        # 显示两个三角形
        self.play(
            Create(triangle_left),
            Create(triangle_right),
            run_time=0.8
        )
        
        # 标题
        title = Text(
            "相似三角形性质总结", 
            font="PingFang SC", 
            font_size=40, 
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 创建一个清晰的网格布局来展示性质
        # 使用VGroup来组织内容
        summary_items = [
            (r"\text{Side ratios}\ \frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c} = k", "k"),
            (r"\text{Altitudes ratio}", "k"),
            (r"\text{Medians ratio}", "k"),
            (r"\text{Angle bisectors ratio}", "k"),
            (r"\text{Perimeter ratio}", "k"),
            (r"\text{Area ratio}", r"k^2")
        ]
        
        # 计算网格位置
        positions = [
            UP * 4 + LEFT * 3,    # 边长比
            UP * 4 + RIGHT * 3,   # k
            UP * 2.5 + LEFT * 3,  # 高之比
            UP * 2.5 + RIGHT * 3, # k
            UP * 1 + LEFT * 3,    # 中线比
            UP * 1 + RIGHT * 3,   # k
            DOWN * 0.5 + LEFT * 3, # 角平分线比
            DOWN * 0.5 + RIGHT * 3, # k
            DOWN * 2 + LEFT * 3,   # 周长比
            DOWN * 2 + RIGHT * 3,  # k
            DOWN * 3.5 + LEFT * 3, # Area ratio
            DOWN * 3.5 + RIGHT * 3 # k²
        ]
        
        # 存储所有文本对象
        all_texts = []
        
        # 动画展示每一对性质
        for i in range(len(summary_items)):
            prop_text = MathTex(summary_items[i][0], font_size=28, color=WHITE).move_to(positions[i * 2])
            value_text = MathTex(summary_items[i][1], font_size=32, color=GOLD).move_to(positions[i * 2 + 1])
            
            all_texts.extend([prop_text, value_text])
            
            if i == 0:
                # 第一对同时出现
                self.play(Write(prop_text), Write(value_text), run_time=0.8)
            else:
                # 后续对依次出现
                self.play(Write(prop_text), run_time=0.6)
                self.play(Write(value_text), run_time=0.6)
                
            self.wait(0.3)
        
        # 高亮面积比这一项（因为它最重要）
        area_prop = all_texts[10]  # Area ratio text
        area_value = all_texts[11]  # k² text
        
        highlight_box = SurroundingRectangle(
            VGroup(area_prop, area_value),
            color=YELLOW,
            buff=0.2,
            stroke_width=3
        )
        
        self.play(Create(highlight_box), run_time=0.8)
        self.play(Indicate(area_value, color=GOLD, scale_factor=1.2), run_time=1.0)
        
        # 添加说明文字
        reminder_text = Text(
            "Key Point: Area ratio is the square of similarity ratio!", 
            font="PingFang SC", 
            font_size=24, 
            color=GOLD
        ).move_to(DOWN * 5.5)
        
        self.play(Write(reminder_text), run_time=1.0)
        
        # 最后的强调
        emphasis = MathTex(
            "k^2",
            font_size=60,
            color=YELLOW
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(emphasis), run_time=0.8)
        self.play(Flash(emphasis.get_center(), color=YELLOW, flash_radius=1.2), run_time=1.0)
        
        # 作者信息
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 7.5)
        
        self.play(FadeIn(author_name, shift=UP * 0.3), run_time=0.8)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 8.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.8)
        
        # 装饰动画
        decorations = VGroup(*[
            Star(color=GOLD, fill_color=GOLD, fill_opacity=0.8)
            .scale(0.2)
            .move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(*[GrowFromCenter(dec) for dec in decorations], run_time=0.8)
        self.play(Rotate(decorations, angle=TAU/8, run_time=1.0))
        
        self.wait(2.0)
        
        # 渐次消失
        all_mobjects = [triangle_left, triangle_right, title, highlight_box, reminder_text, emphasis, author_name, follow_text, decorations] + all_texts
        self.play(*[FadeOut(obj) for obj in all_mobjects], run_time=1.5)
    
    def create_summary_card(self, content, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=self.COLOR_HIGHLIGHT, fill_opacity=1, stroke_width=0)
        
        # 内容
        text = Text(
            content,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql similar_triangles.py SimilarTrianglesProperties  # 快速预览
# manim -qh similar_triangles.py SimilarTrianglesProperties   # 高质量渲染