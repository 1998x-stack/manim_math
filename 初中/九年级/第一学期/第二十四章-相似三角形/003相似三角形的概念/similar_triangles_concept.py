"""
相似三角形的概念 - Similar Triangles Concept
使用 Manim 创建的九年级几何教学视频

内容:
1. 相似三角形的定义
2. 对应角相等
3. 对应边成比例
4. 相似比的含义
5. 全等是特殊情况

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


class GeometryCalculator:
    """几何计算工具类"""
    
    @staticmethod
    def angle_between_vectors(v1, v2):
        """计算两向量夹角（弧度）"""
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    
    @staticmethod
    def angle_at_vertex(P1, vertex, P2):
        """计算顶点处的角度（弧度），vertex是顶点"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        return GeometryCalculator.angle_between_vectors(v1, v2)


class SimilarTrianglesConcept(Scene):
    """
    相似三角形概念教学动画
    
    场景顺序:
    1. 开场钩子
    2. 定义展示
    3. 对应角相等
    4. 对应边成比例
    5. 相似比的含义
    6. 全等是特殊情况
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE_1 = "#3498db"    # 蓝色 - 小三角形
        self.COLOR_TRIANGLE_2 = "#e74c3c"    # 红色 - 大三角形
        self.COLOR_ANGLE = "#2ecc71"         # 绿色 - 角度
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA = "#f39c12"
        
        # 作者信息（始终显示在顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.author_info)
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_corresponding_angles()
        self.show_corresponding_sides()
        self.show_similarity_ratio()
        self.show_congruence_special_case()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化两个相似三角形的几何数据"""
        # 相似比
        self.k = 2.0
        
        # ========== 三角形1（小）- 基准三角形 ==========
        # 使用一个不等边三角形，便于展示
        self.A1 = np.array([-1.5, 0.5, 0])
        self.B1 = np.array([0.5, -1, 0])
        self.C1 = np.array([1, 1.2, 0])
        
        # 计算边长
        self.ab1 = np.linalg.norm(self.B1 - self.A1)
        self.bc1 = np.linalg.norm(self.C1 - self.B1)
        self.ca1 = np.linalg.norm(self.A1 - self.C1)
        
        # 计算角度（弧度）
        calc = GeometryCalculator
        self.angle_A1 = calc.angle_at_vertex(self.B1, self.A1, self.C1)  # Angle at A between BA and AC
        self.angle_B1 = calc.angle_at_vertex(self.C1, self.B1, self.A1)  # Angle at B between CB and BA
        self.angle_C1 = calc.angle_at_vertex(self.A1, self.C1, self.B1)  # Angle at C between AC and CB
        
        # ========== 三角形2（大）- 相似三角形 ==========
        # 通过缩放得到，确保相似
        # 放置在不同位置
        offset = np.array([0, -1.5, 0])
        center1 = (self.A1 + self.B1 + self.C1) / 3
        
        self.D2 = offset + self.k * (self.A1 - center1)  # Corresponds to A1 -> D
        self.E2 = offset + self.k * (self.B1 - center1)  # Corresponds to B1 -> E
        self.F2 = offset + self.k * (self.C1 - center1)  # Corresponds to C1 -> F
        
        # 计算边长
        self.de2 = np.linalg.norm(self.E2 - self.D2)
        self.ef2 = np.linalg.norm(self.F2 - self.E2)
        self.fd2 = np.linalg.norm(self.D2 - self.F2)
        
        # 计算角度（弧度）
        self.angle_D2 = calc.angle_at_vertex(self.E2, self.D2, self.F2)  # Corresponds to A1 - Angle at D between ED and DF
        self.angle_E2 = calc.angle_at_vertex(self.F2, self.E2, self.D2)  # Corresponds to B1 - Angle at E between FE and ED
        self.angle_F2 = calc.angle_at_vertex(self.D2, self.F2, self.E2)  # Corresponds to C1 - Angle at F between DF and FE
        
        # 验证
        self.verify_similarity()
        
        print(f"✓ 几何初始化完成")
        print(f"  三角形1边长: AB={self.ab1:.2f}, BC={self.bc1:.2f}, CA={self.ca1:.2f}")
        print(f"  三角形2边长: DE={self.de2:.2f}, EF={self.ef2:.2f}, FD={self.fd2:.2f}")
        print(f"  相似比 k={self.k:.2f}")
    
    def verify_similarity(self):
        """验证两个三角形的相似性"""
        epsilon_angle = 0.01  # 角度误差（弧度）
        epsilon_ratio = 0.01  # 比例误差
        
        # 验证角度相等
        angle_diff_A = abs(self.angle_A1 - self.angle_D2)
        angle_diff_B = abs(self.angle_B1 - self.angle_E2)
        angle_diff_C = abs(self.angle_C1 - self.angle_F2)
        
        if angle_diff_A > epsilon_angle:
            print(f"WARNING: 角A不相等! 差值 = {np.degrees(angle_diff_A):.2f}°")
        if angle_diff_B > epsilon_angle:
            print(f"WARNING: 角B不相等! 差值 = {np.degrees(angle_diff_B):.2f}°")
        if angle_diff_C > epsilon_angle:
            print(f"WARNING: 角C不相等! 差值 = {np.degrees(angle_diff_C):.2f}°")
        
        # 验证比例相等
        ratio1 = self.de2 / self.ab1
        ratio2 = self.ef2 / self.bc1
        ratio3 = self.fd2 / self.ca1
        
        if abs(ratio1 - self.k) > epsilon_ratio:
            print(f"WARNING: AB比例错误! {ratio1:.3f} vs {self.k:.3f}")
        if abs(ratio2 - self.k) > epsilon_ratio:
            print(f"WARNING: BC比例错误! {ratio2:.3f} vs {self.k:.3f}")
        if abs(ratio3 - self.k) > epsilon_ratio:
            print(f"WARNING: CA比例错误! {ratio3:.3f} vs {self.k:.3f}")
        
        print(f"✓ 相似性验证: 角度相等, 比例={ratio1:.3f}, {ratio2:.3f}, {ratio3:.3f}")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 钩子问题
        hook = Text(
            "两个形状'相似'意味着什么?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.3)
        
        # 快速展示两个三角形
        tri1_demo = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=4
        ).shift(LEFT * 1.5 + DOWN * 0.5)
        
        tri2_demo = Polygon(
            self.D2, self.E2, self.F2,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=4
        ).shift(RIGHT * 0.5 + DOWN * 0.5)
        
        self.play(
            FadeIn(tri1_demo, scale=0.5),
            run_time=0.6
        )
        self.play(
            FadeIn(tri2_demo, scale=0.5),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(tri1_demo),
            FadeOut(tri2_demo),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 定义展示"""
        # 标题
        title = Text(
            "什么是相似三角形?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建两个三角形（分开放置）
        self.tri1 = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=3
        ).shift(LEFT * 2 + UP * 2.5)
        
        self.tri2 = Polygon(
            self.D2, self.E2, self.F2,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=3
        ).shift(RIGHT * 1.5 + UP * 1)
        
        self.play(Create(self.tri1), run_time=0.8)
        self.play(Create(self.tri2), run_time=0.8)
        
        # 顶点标签
        # 三角形1
        pos_A1 = self.tri1.get_vertices()[0]
        pos_B1 = self.tri1.get_vertices()[1]
        pos_C1 = self.tri1.get_vertices()[2]
        
        label_A = Text("A", font="Noto Sans CJK SC", font_size=22).next_to(pos_A1, LEFT, buff=0.12)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=22).next_to(pos_B1, DOWN, buff=0.12)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=22).next_to(pos_C1, UP, buff=0.12)
        
        # 三角形2 - 对应顶点对应关系：A->D, B->E, C->F
        pos_D2 = self.tri2.get_vertices()[0]
        pos_E2 = self.tri2.get_vertices()[1]
        pos_F2 = self.tri2.get_vertices()[2]
        
        label_D = Text("D", font="Noto Sans CJK SC", font_size=22).next_to(pos_D2, LEFT, buff=0.12)
        label_E = Text("E", font="Noto Sans CJK SC", font_size=22).next_to(pos_E2, DOWN, buff=0.12)
        label_F = Text("F", font="Noto Sans CJK SC", font_size=22).next_to(pos_F2, UP, buff=0.12)
        
        self.labels1 = VGroup(label_A, label_B, label_C)
        self.labels2 = VGroup(label_D, label_E, label_F)
        
        self.play(
            Write(self.labels1),
            Write(self.labels2),
            run_time=0.6
        )
        
        # 定义文字
        def1 = Text(
            "① 对应角相等",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(DOWN * 1)
        
        def2 = Text(
            "② 对应边成比例",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(def1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(def2, shift=UP * 0.2), run_time=0.6)
        
        # 相似符号
        similar_symbol = MathTex(
            r"\triangle ABC \sim \triangle DEF",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(similar_symbol), run_time=1.0)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def1),
            FadeOut(def2),
            FadeOut(similar_symbol),
            run_time=0.5
        )
    
    def show_corresponding_angles(self):
        """场景3: 对应角相等"""
        # 副标题
        subtitle = Text(
            "条件1: 对应角相等",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 获取当前三角形顶点位置
        pos_A1 = self.tri1.get_vertices()[0]
        pos_B1 = self.tri1.get_vertices()[1]
        pos_C1 = self.tri1.get_vertices()[2]
        
        pos_D2 = self.tri2.get_vertices()[0]
        pos_E2 = self.tri2.get_vertices()[1]
        pos_F2 = self.tri2.get_vertices()[2]
        
        # 预先定义所有角度对象
        angle_A = Angle.from_three_points(
            pos_B1, pos_A1, pos_C1,
            radius=0.4,
            color=GREEN,
            other_angle=False
        )
        
        angle_D = Angle.from_three_points(
            pos_E2, pos_D2, pos_F2,
            radius=0.6,
            color=GREEN,
            other_angle=False
        )
        
        angle_B = Angle.from_three_points(
            pos_C1, pos_B1, pos_A1,
            radius=0.4,
            color=YELLOW,
            other_angle=False
        )
        
        angle_E = Angle.from_three_points(
            pos_F2, pos_E2, pos_D2,
            radius=0.6,
            color=YELLOW,
            other_angle=False
        )
        
        angle_C = Angle.from_three_points(
            pos_A1, pos_C1, pos_B1,
            radius=0.4,
            color=ORANGE,
            other_angle=False
        )
        
        angle_F = Angle.from_three_points(
            pos_D2, pos_F2, pos_E2,
            radius=0.6,
            color=ORANGE,
            other_angle=False
        )
        
        # 显示角A和角D（绿色）
        self.play(Create(angle_A), Create(angle_D), run_time=0.5)
        
        # 角度值
        angle_val_A = Text(
            f"∠A = ∠D = {np.degrees(self.angle_A1):.0f}°",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).move_to(DOWN * 3.5)
        
        self.play(Write(angle_val_A), run_time=0.6)
        self.play(Flash(angle_A, color=GREEN), Flash(angle_D, color=GREEN), run_time=0.4)
        self.wait(0.5)
        
        # 显示角B和角E（黄色）
        self.play(Create(angle_B), Create(angle_E), run_time=0.5)
        
        angle_val_B = Text(
            f"∠B = ∠E = {np.degrees(self.angle_B1):.0f}°",
            font="Noto Sans CJK SC",
            font_size=24,
            color=YELLOW
        ).move_to(DOWN * 4.3)
        
        self.play(
            Write(angle_val_B),
            FadeOut(angle_val_A),
            run_time=0.6
        )
        self.wait(0.3)
        
        # 显示角C和角F（橙色）
        self.play(Create(angle_C), Create(angle_F), run_time=0.5)
        
        angle_val_C = Text(
            f"∠C = ∠F = {np.degrees(self.angle_C1):.0f}°",
            font="Noto Sans CJK SC",
            font_size=24,
            color=ORANGE
        ).move_to(DOWN * 5.1)
        
        self.play(
            Write(angle_val_C),
            FadeOut(angle_val_B),
            run_time=0.6
        )
        
        angle_E = Angle.from_three_points(
            pos_D2, pos_E2, pos_F2,
            radius=0.6,
            color=YELLOW,
            other_angle=False
        )
        
        self.play(Create(angle_B), run_time=0.5)
        self.play(Create(angle_E), run_time=0.5)
        
        angle_val_B = Text(
            f"∠B = ∠E = {np.degrees(self.angle_B1):.0f}°",
            font="Noto Sans CJK SC",
            font_size=24,
            color=YELLOW
        ).move_to(DOWN * 4.3)
        
        self.play(
            Write(angle_val_B),
            FadeOut(angle_val_A),
            run_time=0.6
        )
        self.wait(0.3)
        
        # 角C和角F（橙色）
        angle_C = Angle.from_three_points(
            pos_B1, pos_C1, pos_A1,
            radius=0.4,
            color=ORANGE,
            other_angle=False
        )
        
        angle_F = Angle.from_three_points(
            pos_E2, pos_F2, pos_D2,
            radius=0.6,
            color=ORANGE,
            other_angle=False
        )
        
        self.play(Create(angle_C), run_time=0.5)
        self.play(Create(angle_F), run_time=0.5)
        
        angle_val_C = Text(
            f"∠C = ∠F = {np.degrees(self.angle_C1):.0f}°",
            font="Noto Sans CJK SC",
            font_size=24,
            color=ORANGE
        ).move_to(DOWN * 5.1)
        
        self.play(
            Write(angle_val_C),
            FadeOut(angle_val_B),
            run_time=0.6
        )
        
        # 总结公式
        formula = MathTex(
            r"\angle A = \angle D, \, \angle B = \angle E, \, \angle C = \angle F",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 6)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(VGroup(angle_A, angle_B, angle_C, angle_D, angle_E, angle_F)),
            FadeOut(angle_val_C),
            FadeOut(formula),
            run_time=0.5
        )
    
    def show_corresponding_sides(self):
        """场景4: 对应边成比例"""
        # 副标题
        subtitle = Text(
            "条件2: 对应边成比例",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.8)
        
        # 获取顶点
        pos_A1 = self.tri1.get_vertices()[0]
        pos_B1 = self.tri1.get_vertices()[1]
        pos_C1 = self.tri1.get_vertices()[2]
        
        pos_D2 = self.tri2.get_vertices()[0]
        pos_E2 = self.tri2.get_vertices()[1]
        pos_F2 = self.tri2.get_vertices()[2]
        
        # AB 和 DE
        line_AB = Line(pos_A1, pos_B1, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        line_DE = Line(pos_D2, pos_E2, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        
        self.play(Create(line_AB), Create(line_DE), run_time=0.6)
        
        label_AB = Text(
            f"AB={self.ab1:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_AB, LEFT, buff=0.1)
        
        label_DE = Text(
            f"DE={self.de2:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_DE, LEFT, buff=0.1)
        
        self.play(Write(label_AB), Write(label_DE), run_time=0.5)
        
        ratio1 = MathTex(
            rf"\frac{{DE}}{{AB}} = \frac{{{self.de2:.1f}}}{{{self.ab1:.1f}}} = {self.k:.1f}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3)
        
        self.play(Write(ratio1), run_time=0.8)
        self.wait(0.8)
        
        # 清除第一组
        self.play(
            FadeOut(VGroup(line_AB, line_DE, label_AB, label_DE)),
            run_time=0.3
        )
        
        # BC 和 EF
        line_BC = Line(pos_B1, pos_C1, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        line_EF = Line(pos_E2, pos_F2, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        
        self.play(Create(line_BC), Create(line_EF), run_time=0.6)
        
        label_BC = Text(
            f"BC={self.bc1:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_BC, DOWN, buff=0.1)
        
        label_EF = Text(
            f"EF={self.ef2:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_EF, DOWN, buff=0.1)
        
        self.play(Write(label_BC), Write(label_EF), run_time=0.5)
        
        ratio2 = MathTex(
            rf"\frac{{EF}}{{BC}} = \frac{{{self.ef2:.1f}}}{{{self.bc1:.1f}}} = {self.k:.1f}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 4)
        
        self.play(Write(ratio2), run_time=0.8)
        self.wait(0.8)
        
        # 清除第二组
        self.play(
            FadeOut(VGroup(line_BC, line_EF, label_BC, label_EF)),
            run_time=0.3
        )
        
        # CA 和 FD
        line_CA = Line(pos_C1, pos_A1, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        line_FD = Line(pos_F2, pos_D2, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        
        self.play(Create(line_CA), Create(line_FD), run_time=0.6)
        
        label_CA = Text(
            f"CA={self.ca1:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_CA, RIGHT, buff=0.1)
        
        label_FD = Text(
            f"FD={self.fd2:.1f}",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        ).next_to(line_FD, RIGHT, buff=0.1)
        
        self.play(Write(label_CA), Write(label_FD), run_time=0.5)
        
        ratio3 = MathTex(
            rf"\frac{{FD}}{{CA}} = \frac{{{self.fd2:.1f}}}{{{self.ca1:.1f}}} = {self.k:.1f}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5)
        
        self.play(Write(ratio3), run_time=0.8)
        self.wait(1.0)
        
        # 总结
        summary = Text(
            f"相似比 k = {self.k:.1f}",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.2)
        
        self.play(Write(summary), run_time=0.8)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(VGroup(line_CA, line_FD, label_CA, label_FD)),
            FadeOut(VGroup(ratio1, ratio2, ratio3)),
            FadeOut(summary),
            run_time=0.5
        )
    
    def show_similarity_ratio(self):
        """场景5: 相似比的含义"""
        # 清除之前的三角形
        self.play(
            FadeOut(self.tri1),
            FadeOut(self.tri2),
            FadeOut(self.labels1),
            FadeOut(self.labels2),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "相似比的几何意义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 说明
        explanation = Text(
            "相似比 = 对应边长度的比值",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 创建小三角形在中心
        tri_small = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_TRIANGLE_1
        ).move_to(UP * 1)
        
        self.play(Create(tri_small), run_time=0.8)
        
        # 标注 k=2
        k_label = Text(
            "k = 2",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(Write(k_label), run_time=0.6)
        
        # 缩放动画
        tri_large = tri_small.copy().set_color(self.COLOR_TRIANGLE_2)
        
        self.play(
            Transform(tri_small, tri_large.scale(2)),
            run_time=2.0,
            rate_func=there_and_back
        )
        
        self.play(Flash(tri_small, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # k值说明
        k_explanation = VGroup(
            Text("k > 1: 放大", font="Noto Sans CJK SC", font_size=24, color=GREEN),
            Text("k = 1: 全等", font="Noto Sans CJK SC", font_size=24, color=YELLOW),
            Text("k < 1: 缩小", font="Noto Sans CJK SC", font_size=24, color=ORANGE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 3.5)
        
        self.play(FadeIn(k_explanation, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(tri_small),
            FadeOut(k_label),
            FadeOut(k_explanation),
            run_time=0.6
        )
    
    def show_congruence_special_case(self):
        """场景6: 全等是特殊情况"""
        # 标题
        title = Text(
            "特殊情况: 全等三角形",
            font="Noto Sans CJK SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建两个相同的三角形
        tri1 = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_1,
            stroke_width=3
        ).shift(LEFT * 1.8 + UP * 2)
        
        tri2 = Polygon(
            self.A1, self.B1, self.C1,
            color=self.COLOR_TRIANGLE_2,
            stroke_width=3
        ).shift(RIGHT * 1.8 + UP * 2)
        
        self.play(Create(tri1), Create(tri2), run_time=1.0)
        
        # k=1 标注
        k_equals_1 = Text(
            "k = 1",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(Write(k_equals_1), run_time=0.8)
        
        # 说明
        explanation = Text(
            "相似比为 1 的相似三角形",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 符号
        congruent = MathTex(
            r"\triangle ABC \cong \triangle DEF",
            font_size=32,
            color=GREEN
        ).move_to(DOWN * 2)
        
        similar = MathTex(
            r"\triangle ABC \sim \triangle DEF",
            font_size=32,
            color=YELLOW
        ).move_to(DOWN * 3)
        
        self.play(Write(congruent), run_time=0.8)
        self.play(Write(similar), run_time=0.8)
        
        # 关系说明
        relation = Text(
            "全等 ⊂ 相似",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        arrow = Arrow(
            congruent.get_right() + RIGHT * 0.3,
            similar.get_right() + RIGHT * 0.3,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(
            Write(relation),
            Create(arrow),
            run_time=1.0
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, tri1, tri2, k_equals_1, explanation, congruent, similar, relation, arrow)),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何知识!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 相似三角形图标装饰
        icon1 = Polygon(
            ORIGIN, RIGHT * 0.6, UP * 0.6,
            color=self.COLOR_TRIANGLE_1,
            fill_opacity=0.6,
            stroke_width=2
        ).shift(LEFT * 2.5 + DOWN * 2.5)
        
        icon2 = Polygon(
            ORIGIN, RIGHT * 1.2, UP * 1.2,
            color=self.COLOR_TRIANGLE_2,
            fill_opacity=0.6,
            stroke_width=2
        ).shift(RIGHT * 2.5 + DOWN * 3)
        
        icons = VGroup(icon1, icon2)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.8
        )
        
        # 旋转缩放
        self.play(
            Rotate(icons, angle=PI/4),
            icons.animate.scale(1.2),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql similar_triangles_concept.py SimilarTrianglesConcept  # 快速预览
# manim -qh similar_triangles_concept.py SimilarTrianglesConcept   # 高质量渲染