"""
图形的旋转 - Rotation of Geometric Figures
使用 Manim 创建的七年级几何教学视频

内容: 旋转的定义、三要素、三大性质及综合应用
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


class RotationAnimation(Scene):
    """
    图形旋转教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 旋转定义 (三要素)
    3. 性质1 - 距离相等
    4. 性质2 - 旋转角相等
    5. 性质3 - 形状大小不变 (全等)
    6. 综合应用
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ORIGINAL = "#3498db"      # 蓝色 - 原图形
        self.COLOR_ROTATED = "#e74c3c"       # 红色 - 旋转后图形
        self.COLOR_CENTER = "#f39c12"        # 橙色 - 旋转中心
        self.COLOR_ANGLE = "#2ecc71"         # 绿色 - 旋转角
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮强调
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_property_distance()
        self.show_property_angle()
        self.show_property_congruence()
        self.show_comprehensive()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 场景2-4: 基本点旋转
        self.O = ORIGIN + UP * 0.5  # 旋转中心
        self.A = np.array([2.0, 1.5, 0]) + UP * 0.5  # 原点A
        self.B = np.array([2.0, -0.5, 0]) + UP * 0.5  # 原点B
        
        # 旋转角度 (60度 = PI/3)
        self.rotation_angle = PI / 3
        
        # 计算旋转后的点
        self.A_prime = self.rotate_point(self.A, self.O, self.rotation_angle)
        self.B_prime = self.rotate_point(self.B, self.O, self.rotation_angle)
        
        # 计算距离
        self.dist_OA = np.linalg.norm(self.A - self.O)
        self.dist_OA_prime = np.linalg.norm(self.A_prime - self.O)
        self.dist_OB = np.linalg.norm(self.B - self.O)
        self.dist_OB_prime = np.linalg.norm(self.B_prime - self.O)
        
        # 场景5: 三角形旋转
        self.O_tri = np.array([-1.5, 0, 0])
        self.tri_A = np.array([1.0, 1.5, 0])
        self.tri_B = np.array([2.5, 0.8, 0])
        self.tri_C = np.array([1.5, -0.5, 0])
        
        # 旋转90度
        self.tri_rotation_angle = PI / 2
        self.tri_A_prime = self.rotate_point(self.tri_A, self.O_tri, self.tri_rotation_angle)
        self.tri_B_prime = self.rotate_point(self.tri_B, self.O_tri, self.tri_rotation_angle)
        self.tri_C_prime = self.rotate_point(self.tri_C, self.O_tri, self.tri_rotation_angle)
        
        # 验证几何计算
        self.verify_geometry()
    
    def rotate_point(self, point, center, angle):
        """
        将点 point 绕 center 旋转 angle 弧度
        angle > 0: 逆时针
        angle < 0: 顺时针
        """
        # 平移到原点
        translated = point - center
        
        # 旋转矩阵
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        
        # 2D 旋转
        x_new = translated[0] * cos_a - translated[1] * sin_a
        y_new = translated[0] * sin_a + translated[1] * cos_a
        
        # 平移回原位置
        rotated = np.array([x_new, y_new, 0]) + center
        
        return rotated
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证距离相等
        if abs(self.dist_OA - self.dist_OA_prime) > epsilon:
            print(f"WARNING: 距离验证失败! OA={self.dist_OA:.6f}, OA'={self.dist_OA_prime:.6f}")
        
        # 验证角度
        vec_OA = self.A - self.O
        vec_OA_prime = self.A_prime - self.O
        
        angle_OA = np.arctan2(vec_OA[1], vec_OA[0])
        angle_OA_prime = np.arctan2(vec_OA_prime[1], vec_OA_prime[0])
        
        calculated_angle = angle_OA_prime - angle_OA
        if calculated_angle < 0:
            calculated_angle += 2 * PI
        
        if abs(calculated_angle - self.rotation_angle) > epsilon:
            print(f"WARNING: 角度验证失败! 期望={self.rotation_angle:.6f}, 实际={calculated_angle:.6f}")
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "如何让图形优雅地旋转？",
            font=self.FONT_CHINESE,
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简单旋转演示 - 创建一个正方形
        square = Square(side_length=2, color=self.COLOR_ORIGINAL, stroke_width=4).move_to(UP * 2)
        
        self.play(Create(square), run_time=0.6)
        
        # 旋转动画
        self.play(
            Rotate(square, angle=2*PI, about_point=square.get_center()),
            run_time=2.0,
            rate_func=smooth
        )
        
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(square),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 旋转定义"""
        # 标题
        title = Text(
            "旋转的定义",
            font=self.FONT_CHINESE,
            font_size=40,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 旋转中心
        O_dot = Dot(self.O, color=self.COLOR_CENTER, radius=0.12)
        O_label = Text("O", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_CENTER).next_to(O_dot, DOWN, buff=0.15)
        O_text = Text("旋转中心", font=self.FONT_CHINESE, font_size=18, color=GRAY_A).next_to(O_label, DOWN, buff=0.05)
        
        self.play(
            FadeIn(O_dot, scale=0.5),
            run_time=0.4
        )
        self.play(Flash(O_dot, color=self.COLOR_CENTER, flash_radius=0.3), run_time=0.3)
        self.play(FadeIn(O_label), FadeIn(O_text), run_time=0.3)
        
        # 原点 A
        A_dot = Dot(self.A, color=self.COLOR_ORIGINAL, radius=0.10)
        A_label = Text("A", font=self.FONT_CHINESE, font_size=22, color=self.COLOR_ORIGINAL).next_to(A_dot, UP, buff=0.1)
        
        self.play(FadeIn(A_dot, scale=0.5), FadeIn(A_label), run_time=0.4)
        
        # 定义文字
        def_text_1 = Text(
            "① 旋转中心: 固定不动的点",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        def_text_2 = Text(
            "② 旋转方向: 顺时针/逆时针",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.3)
        
        def_text_3 = Text(
            "③ 旋转角度: 转动的角度",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.1)
        
        self.play(FadeIn(def_text_1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(def_text_2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(def_text_3, shift=UP * 0.2), run_time=0.5)
        
        # 绘制旋转路径弧线
        arc_path = Arc(
            radius=self.dist_OA,
            start_angle=np.arctan2((self.A - self.O)[1], (self.A - self.O)[0]),
            angle=self.rotation_angle,
            color=self.COLOR_ANGLE,
            stroke_width=3
        ).shift(self.O)
        
        # 箭头指示方向
        arrow_end = self.rotate_point(self.A, self.O, self.rotation_angle * 0.95)
        arrow_direction = arrow_end - self.rotate_point(self.A, self.O, self.rotation_angle * 0.85)
        arrow_direction = arrow_direction / np.linalg.norm(arrow_direction) * 0.3
        
        arc_arrow = Arrow(
            start=arrow_end - arrow_direction,
            end=arrow_end,
            color=self.COLOR_ANGLE,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        
        self.play(Create(arc_path), run_time=0.8)
        self.play(Create(arc_arrow), run_time=0.3)
        
        # 角度标注
        angle_label = MathTex(r"60^\circ", color=self.COLOR_ANGLE, font_size=28).move_to(
            self.O + 1.5 * np.array([np.cos(self.rotation_angle/2), np.sin(self.rotation_angle/2), 0])
        )
        
        self.play(Write(angle_label), run_time=0.5)
        
        # A 点沿弧线移动到 A'
        A_prime_dot = Dot(self.A_prime, color=self.COLOR_ROTATED, radius=0.10)
        A_prime_label = Text("A'", font=self.FONT_CHINESE, font_size=22, color=self.COLOR_ROTATED).next_to(A_prime_dot, UP, buff=0.1)
        
        # 创建运动轨迹点
        moving_dot = A_dot.copy()
        
        self.play(
            MoveAlongPath(moving_dot, arc_path),
            run_time=1.5,
            rate_func=smooth
        )
        
        # 替换为 A'
        self.play(
            Transform(moving_dot, A_prime_dot),
            FadeIn(A_prime_label),
            run_time=0.4
        )
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_text_1),
            FadeOut(def_text_2),
            FadeOut(def_text_3),
            FadeOut(O_text),
            run_time=0.5
        )
        
        # 保留元素但变小
        self.O_small = Dot(self.O, color=self.COLOR_CENTER, radius=0.06, fill_opacity=0.7)
        self.A_small = Dot(self.A, color=self.COLOR_ORIGINAL, radius=0.06, fill_opacity=0.7)
        self.A_prime_small = Dot(self.A_prime, color=self.COLOR_ROTATED, radius=0.06, fill_opacity=0.7)
        
        self.play(
            Transform(O_dot, self.O_small),
            Transform(A_dot, self.A_small),
            Transform(moving_dot, self.A_prime_small),
            FadeOut(arc_path),
            FadeOut(arc_arrow),
            FadeOut(angle_label),
            FadeOut(O_label),
            FadeOut(A_label),
            FadeOut(A_prime_label),
            run_time=0.4
        )
        
        self.remove(O_dot, A_dot, moving_dot)
        self.add(self.O_small, self.A_small, self.A_prime_small)
    
    def show_property_distance(self):
        """场景3: 性质1 - 距离相等"""
        # 标题
        title = Text(
            "性质1: 对应点到中心距离相等",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 恢复点的大小
        O_dot = Dot(self.O, color=self.COLOR_CENTER, radius=0.10)
        A_dot = Dot(self.A, color=self.COLOR_ORIGINAL, radius=0.08)
        A_prime_dot = Dot(self.A_prime, color=self.COLOR_ROTATED, radius=0.08)
        
        self.play(
            Transform(self.O_small, O_dot),
            Transform(self.A_small, A_dot),
            Transform(self.A_prime_small, A_prime_dot),
            run_time=0.4
        )
        
        # 添加点 B
        B_dot = Dot(self.B, color=self.COLOR_ORIGINAL, radius=0.08)
        B_label = Text("B", font=self.FONT_CHINESE, font_size=20, color=self.COLOR_ORIGINAL).next_to(B_dot, RIGHT, buff=0.1)
        
        self.play(FadeIn(B_dot, scale=0.5), FadeIn(B_label), run_time=0.4)
        
        # 旋转 B 到 B'
        B_prime_dot = Dot(self.B_prime, color=self.COLOR_ROTATED, radius=0.08)
        B_prime_label = Text("B'", font=self.FONT_CHINESE, font_size=20, color=self.COLOR_ROTATED).next_to(B_prime_dot, RIGHT, buff=0.1)
        
        # 创建旋转动画路径
        arc_path_B = Arc(
            radius=self.dist_OB,
            start_angle=np.arctan2((self.B - self.O)[1], (self.B - self.O)[0]),
            angle=self.rotation_angle,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).shift(self.O)
        
        moving_B = B_dot.copy()
        
        self.play(
            Create(arc_path_B),
            MoveAlongPath(moving_B, arc_path_B),
            run_time=1.2
        )
        
        self.play(
            Transform(moving_B, B_prime_dot),
            FadeIn(B_prime_label),
            FadeOut(arc_path_B),
            run_time=0.4
        )
        
        # 绘制距离线 OA 和 OA'
        line_OA = DashedLine(self.O, self.A, color=self.COLOR_ORIGINAL, dash_length=0.08, stroke_width=3)
        line_OA_prime = DashedLine(self.O, self.A_prime, color=self.COLOR_ROTATED, dash_length=0.08, stroke_width=3)
        
        self.play(Create(line_OA), run_time=0.5)
        self.play(Create(line_OA_prime), run_time=0.5)
        
        # 距离标注
        dist_label_OA = MathTex(r"d", color=self.COLOR_ORIGINAL, font_size=24).move_to(
            (self.O + self.A) / 2 + LEFT * 0.3
        )
        dist_label_OA_prime = MathTex(r"d", color=self.COLOR_ROTATED, font_size=24).move_to(
            (self.O + self.A_prime) / 2 + UP * 0.3
        )
        
        self.play(Write(dist_label_OA), Write(dist_label_OA_prime), run_time=0.6)
        
        # 高亮相等
        self.play(
            Flash(line_OA, color=self.COLOR_HIGHLIGHT, line_length=0.3),
            Flash(line_OA_prime, color=self.COLOR_HIGHLIGHT, line_length=0.3),
            run_time=0.5
        )
        
        # 公式
        formula = MathTex(
            r"OA = OA', \quad OB = OB'",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "旋转不改变距离",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_OA),
            FadeOut(line_OA_prime),
            FadeOut(dist_label_OA),
            FadeOut(dist_label_OA_prime),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(B_label),
            FadeOut(B_prime_label),
            run_time=0.5
        )
        
        # 保留小点
        self.play(
            Transform(self.O_small, Dot(self.O, color=self.COLOR_CENTER, radius=0.06, fill_opacity=0.5)),
            Transform(self.A_small, Dot(self.A, color=self.COLOR_ORIGINAL, radius=0.06, fill_opacity=0.5)),
            Transform(self.A_prime_small, Dot(self.A_prime, color=self.COLOR_ROTATED, radius=0.06, fill_opacity=0.5)),
            Transform(B_dot, Dot(self.B, color=self.COLOR_ORIGINAL, radius=0.06, fill_opacity=0.5)),
            Transform(moving_B, Dot(self.B_prime, color=self.COLOR_ROTATED, radius=0.06, fill_opacity=0.5)),
            run_time=0.3
        )
        
        self.B_small = Dot(self.B, color=self.COLOR_ORIGINAL, radius=0.06, fill_opacity=0.5)
        self.B_prime_small = Dot(self.B_prime, color=self.COLOR_ROTATED, radius=0.06, fill_opacity=0.5)
        
        self.remove(B_dot, moving_B)
        self.add(self.B_small, self.B_prime_small)
    
    def show_property_angle(self):
        """场景4: 性质2 - 旋转角相等"""
        # 标题
        title = Text(
            "性质2: 旋转角相等",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 恢复点的大小
        O_dot = Dot(self.O, color=self.COLOR_CENTER, radius=0.10)
        A_dot = Dot(self.A, color=self.COLOR_ORIGINAL, radius=0.08)
        A_prime_dot = Dot(self.A_prime, color=self.COLOR_ROTATED, radius=0.08)
        B_dot = Dot(self.B, color=self.COLOR_ORIGINAL, radius=0.08)
        B_prime_dot = Dot(self.B_prime, color=self.COLOR_ROTATED, radius=0.08)
        
        self.play(
            Transform(self.O_small, O_dot),
            Transform(self.A_small, A_dot),
            Transform(self.A_prime_small, A_prime_dot),
            Transform(self.B_small, B_dot),
            Transform(self.B_prime_small, B_prime_dot),
            run_time=0.4
        )
        
        # 绘制角 ∠AOA'
        angle_AOA = Angle(
            Line(self.O, self.A),
            Line(self.O, self.A_prime),
            radius=0.6,
            color=self.COLOR_ANGLE,
            fill_opacity=0.3
        )
        
        self.play(Create(angle_AOA), run_time=0.8)
        
        # 角度标注
        angle_label_1 = MathTex(r"60^\circ", color=self.COLOR_ANGLE, font_size=26).move_to(
            self.O + 0.9 * np.array([np.cos(self.rotation_angle/2), np.sin(self.rotation_angle/2), 0])
        )
        
        self.play(Write(angle_label_1), run_time=0.5)
        
        self.wait(0.5)
        
        # 绘制角 ∠BOB'
        angle_BOB = Angle(
            Line(self.O, self.B),
            Line(self.O, self.B_prime),
            radius=0.5,
            color=self.COLOR_ANGLE,
            fill_opacity=0.3
        )
        
        self.play(Create(angle_BOB), run_time=0.8)
        
        # 第二个角度标注
        vec_OB = self.B - self.O
        angle_OB = np.arctan2(vec_OB[1], vec_OB[0])
        
        angle_label_2 = MathTex(r"60^\circ", color=self.COLOR_ANGLE, font_size=26).move_to(
            self.O + 0.75 * np.array([np.cos(angle_OB + self.rotation_angle/2), np.sin(angle_OB + self.rotation_angle/2), 0])
        )
        
        self.play(Write(angle_label_2), run_time=0.5)
        
        # 高亮两个角
        self.play(
            Flash(angle_AOA, color=self.COLOR_HIGHLIGHT, line_length=0.2),
            Flash(angle_BOB, color=self.COLOR_HIGHLIGHT, line_length=0.2),
            run_time=0.6
        )
        
        # 公式
        formula = MathTex(
            r"\angle AOA' = \angle BOB' = 60^\circ",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "所有点的旋转角度都相同",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(angle_AOA),
            FadeOut(angle_BOB),
            FadeOut(angle_label_1),
            FadeOut(angle_label_2),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(self.O_small),
            FadeOut(self.A_small),
            FadeOut(self.A_prime_small),
            FadeOut(self.B_small),
            FadeOut(self.B_prime_small),
            run_time=0.5
        )
    
    def show_property_congruence(self):
        """场景5: 性质3 - 形状大小不变 (全等)"""
        # 标题
        title = Text(
            "性质3: 图形的形状和大小不变",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建原三角形
        triangle_ABC = Polygon(
            self.tri_A, self.tri_B, self.tri_C,
            color=self.COLOR_ORIGINAL,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_ORIGINAL
        )
        
        # 顶点标签
        A_label = Text("A", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_A, UP, buff=0.1)
        B_label = Text("B", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_B, RIGHT, buff=0.1)
        C_label = Text("C", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_C, DOWN, buff=0.1)
        
        self.play(Create(triangle_ABC), run_time=1.0)
        self.play(FadeIn(A_label), FadeIn(B_label), FadeIn(C_label), run_time=0.4)
        
        # 标注边长
        side_AB = np.linalg.norm(self.tri_B - self.tri_A)
        side_BC = np.linalg.norm(self.tri_C - self.tri_B)
        side_CA = np.linalg.norm(self.tri_A - self.tri_C)
        
        side_label_AB = MathTex(f"{side_AB:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_A + self.tri_B) / 2 + UP * 0.3
        )
        side_label_BC = MathTex(f"{side_BC:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_B + self.tri_C) / 2 + RIGHT * 0.3
        )
        side_label_CA = MathTex(f"{side_CA:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_C + self.tri_A) / 2 + LEFT * 0.3
        )
        
        self.play(
            Write(side_label_AB),
            Write(side_label_BC),
            Write(side_label_CA),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 旋转中心
        O_tri_dot = Dot(self.O_tri, color=self.COLOR_CENTER, radius=0.10)
        O_tri_label = Text("O", font=self.FONT_CHINESE, font_size=22, color=self.COLOR_CENTER).next_to(O_tri_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(O_tri_dot, scale=0.5), FadeIn(O_tri_label), run_time=0.4)
        
        # 旋转三角形
        triangle_prime = Polygon(
            self.tri_A_prime, self.tri_B_prime, self.tri_C_prime,
            color=self.COLOR_ROTATED,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_ROTATED
        )
        
        # 复制原三角形用于旋转动画
        triangle_rotating = triangle_ABC.copy()
        
        self.play(
            Rotate(
                triangle_rotating,
                angle=self.tri_rotation_angle,
                about_point=self.O_tri
            ),
            run_time=2.0,
            rate_func=smooth
        )
        
        # 替换为目标三角形
        self.play(Transform(triangle_rotating, triangle_prime), run_time=0.3)
        
        # 旋转后的顶点标签
        A_prime_label = Text("A'", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_A_prime, LEFT, buff=0.1)
        B_prime_label = Text("B'", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_B_prime, UP, buff=0.1)
        C_prime_label = Text("C'", font=self.FONT_CHINESE, font_size=22, color=WHITE).next_to(self.tri_C_prime, LEFT, buff=0.1)
        
        self.play(
            FadeIn(A_prime_label),
            FadeIn(B_prime_label),
            FadeIn(C_prime_label),
            run_time=0.4
        )
        
        # 标注旋转后边长 (相同)
        side_label_AB_prime = MathTex(f"{side_AB:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_A_prime + self.tri_B_prime) / 2 + LEFT * 0.35
        )
        side_label_BC_prime = MathTex(f"{side_BC:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_B_prime + self.tri_C_prime) / 2 + UP * 0.3
        )
        side_label_CA_prime = MathTex(f"{side_CA:.1f}", font_size=20, color=GRAY_A).move_to(
            (self.tri_C_prime + self.tri_A_prime) / 2 + DOWN * 0.3
        )
        
        self.play(
            Write(side_label_AB_prime),
            Write(side_label_BC_prime),
            Write(side_label_CA_prime),
            run_time=0.8
        )
        
        # 高亮对应边
        self.play(
            Flash(Line(self.tri_A, self.tri_B), color=self.COLOR_HIGHLIGHT),
            Flash(Line(self.tri_A_prime, self.tri_B_prime), color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        # 全等符号
        congruence = MathTex(
            r"\triangle ABC \cong \triangle A'B'C'",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(congruence), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "旋转是全等变换",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(triangle_ABC),
            FadeOut(triangle_rotating),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(C_label),
            FadeOut(A_prime_label),
            FadeOut(B_prime_label),
            FadeOut(C_prime_label),
            FadeOut(side_label_AB),
            FadeOut(side_label_BC),
            FadeOut(side_label_CA),
            FadeOut(side_label_AB_prime),
            FadeOut(side_label_BC_prime),
            FadeOut(side_label_CA_prime),
            FadeOut(O_tri_dot),
            FadeOut(O_tri_label),
            FadeOut(congruence),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_comprehensive(self):
        """场景6: 综合应用"""
        # 标题
        title = Text(
            "旋转的性质总结",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建五边形
        pentagon_vertices = [
            np.array([np.cos(2*PI*i/5 + PI/2), np.sin(2*PI*i/5 + PI/2), 0]) * 1.5 + UP * 1.5
            for i in range(5)
        ]
        
        pentagon = Polygon(
            *pentagon_vertices,
            color=self.COLOR_ORIGINAL,
            stroke_width=4,
            fill_opacity=0.3,
            fill_color=self.COLOR_ORIGINAL
        )
        
        self.play(Create(pentagon), run_time=1.0)
        
        # 旋转中心
        center = UP * 1.5
        center_dot = Dot(center, color=self.COLOR_CENTER, radius=0.12)
        center_label = Text("O", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_CENTER).next_to(center_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(center_dot, scale=0.5), FadeIn(center_label), run_time=0.4)
        self.play(Flash(center_dot, color=self.COLOR_CENTER, flash_radius=0.3), run_time=0.3)
        
        # 慢速旋转动画
        pentagon_copy = pentagon.copy().set_color(self.COLOR_ROTATED)
        
        self.play(
            Rotate(
                pentagon_copy,
                angle=PI/3,
                about_point=center
            ),
            run_time=3.0,
            rate_func=smooth
        )
        
        self.wait(0.5)
        
        # 性质卡片
        card_1 = self.create_property_card(
            "距离相等",
            "对应点到中心距离相等",
            self.COLOR_ORIGINAL
        ).move_to(DOWN * 2.5 + LEFT * 10)
        
        card_2 = self.create_property_card(
            "旋转角相等",
            "所有点旋转角度相同",
            self.COLOR_ANGLE
        ).move_to(DOWN * 3.8 + LEFT * 10)
        
        card_3 = self.create_property_card(
            "全等变换",
            "形状大小保持不变",
            self.COLOR_ROTATED
        ).move_to(DOWN * 5.1 + LEFT * 10)
        
        # 卡片依次滑入
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card_3.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(pentagon),
            FadeOut(pentagon_copy),
            FadeOut(center_dot),
            FadeOut(center_label),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            run_time=0.6
        )
    
    def create_property_card(self, title, content, color):
        """创建性质卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font=self.FONT_CHINESE,
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=42,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 旋转图标装饰
        icons = VGroup(*[
            RegularPolygon(n=3, color=self.COLOR_ORIGINAL, fill_opacity=0.8)
            .scale(0.3)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * 2*PI / 6), np.sin(i * 2*PI / 6), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        # 旋转图标
        self.play(
            Rotate(icons, angle=2*PI, about_point=follow_text.get_center()),
            run_time=2.0,
            rate_func=smooth
        )
        
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql rotation_animation.py RotationAnimation  # 快速预览
# manim -qh rotation_animation.py RotationAnimation   # 高质量渲染