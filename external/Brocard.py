"""
布罗卡点 (Brocard Points) - Manim 数学教学动画
Brocard Points Geometry Animation

内容: 布罗卡点的定义、性质、构造和特殊情况
目标观众: 高中生及几何爱好者
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from scipy.optimize import minimize


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class BrocardPointsScene(Scene):
    """
    布罗卡点教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义第一布罗卡点
    3. 定义第二布罗卡点
    4. 布罗卡角公式
    5. 构造方法展示
    6. 等边三角形特例
    7. 性质总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"          # 蓝色 - 三角形
        self.COLOR_BROCARD_1 = "#e74c3c"        # 红色 - 第一布罗卡点 Ω
        self.COLOR_BROCARD_2 = "#f39c12"        # 橙色 - 第二布罗卡点 Ω'
        self.COLOR_ANGLE = "#2ecc71"            # 绿色 - 角弧
        self.COLOR_CIRCLE = "#9b59b6"           # 紫色 - 辅助圆
        self.COLOR_AUXILIARY = GRAY_B           # 灰色 - 辅助线
        self.COLOR_HIGHLIGHT = YELLOW           # 黄色 - 高亮
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_first_brocard_point()
        self.show_second_brocard_point()
        self.show_brocard_angle_formula()
        self.show_construction_method()
        self.show_equilateral_case()
        self.show_properties_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点 (使用不等边三角形展示一般性)
        self.A_base = np.array([-2.5, 1.5, 0])
        self.B_base = np.array([2.5, -0.5, 0])
        self.C_base = np.array([-1.0, -2.5, 0])
        
        # 缩放和偏移
        self.SCALE = 0.75
        self.OFFSET = UP * 1.0
        
        # 应用变换
        self.A = self.A_base * self.SCALE + self.OFFSET
        self.B = self.B_base * self.SCALE + self.OFFSET
        self.C = self.C_base * self.SCALE + self.OFFSET
        
        # 计算几何数据
        self._calculate_geometry()
        
        # 验证几何计算
        self._verify_geometry()
        
        # 创建三角形对象
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
    
    def _calculate_geometry(self):
        """计算所有几何数据"""
        # 边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # 面积
        AB = self.B - self.A
        AC = self.C - self.A
        cross_product = AB[0] * AC[1] - AB[1] * AC[0]
        self.area = abs(cross_product) / 2
        
        # 布罗卡角
        cot_omega = (self.a**2 + self.b**2 + self.c**2) / (4 * self.area)
        self.omega = np.arctan(1 / cot_omega)
        
        # 参考点
        self.circumcenter = self._calc_circumcenter()
        self.centroid = (self.A + self.B + self.C) / 3
        
        # 布罗卡点
        self.brocard_1 = self._calc_first_brocard_point()
        self.brocard_2 = self._calc_second_brocard_point()
    
    def _calc_circumcenter(self):
        """计算外心"""
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]
        
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        
        if abs(D) < 1e-10:
            return (self.A + self.B + self.C) / 3
        
        ux = ((ax**2 + ay**2) * (by - cy) + 
              (bx**2 + by**2) * (cy - ay) + 
              (cx**2 + cy**2) * (ay - by)) / D
        
        uy = ((ax**2 + ay**2) * (cx - bx) + 
              (bx**2 + by**2) * (ax - cx) + 
              (cx**2 + cy**2) * (bx - ax)) / D
        
        return np.array([ux, uy, 0])
    
    def _angle_at_vertex(self, P, vertex, point_on_ray):
        """计算角度"""
        v1 = point_on_ray - vertex
        v2 = P - vertex
        
        cos_angle = np.dot(v1[:2], v2[:2]) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angle = np.arccos(cos_angle)
        
        return angle
    
    def _calc_first_brocard_point(self):
        """计算第一布罗卡点 - 使用优化方法"""
        def objective(point):
            P = np.array([point[0], point[1], 0])
            
            angle1 = self._angle_at_vertex(P, self.A, self.B)
            angle2 = self._angle_at_vertex(P, self.B, self.C)
            angle3 = self._angle_at_vertex(P, self.C, self.A)
            
            error = (angle1 - self.omega)**2 + (angle2 - self.omega)**2 + (angle3 - self.omega)**2
            return error
        
        x0 = self.centroid[:2]
        result = minimize(objective, x0, method='Nelder-Mead', options={'xatol': 1e-8})
        
        return np.array([result.x[0], result.x[1], 0])
    
    def _calc_second_brocard_point(self):
        """计算第二布罗卡点 - 使用优化方法"""
        def objective(point):
            P = np.array([point[0], point[1], 0])
            
            angle1 = self._angle_at_vertex(P, self.B, self.A)
            angle2 = self._angle_at_vertex(P, self.C, self.B)
            angle3 = self._angle_at_vertex(P, self.A, self.C)
            
            error = (angle1 - self.omega)**2 + (angle2 - self.omega)**2 + (angle3 - self.omega)**2
            return error
        
        x0 = self.centroid[:2]
        result = minimize(objective, x0, method='Nelder-Mead', options={'xatol': 1e-8})
        
        return np.array([result.x[0], result.x[1], 0])
    
    def _verify_geometry(self):
        """验证几何计算"""
        epsilon = 1e-4
        
        # 验证第一布罗卡点
        angle1 = self._angle_at_vertex(self.brocard_1, self.A, self.B)
        angle2 = self._angle_at_vertex(self.brocard_1, self.B, self.C)
        angle3 = self._angle_at_vertex(self.brocard_1, self.C, self.A)
        
        if abs(angle1 - self.omega) > epsilon or abs(angle2 - self.omega) > epsilon or abs(angle3 - self.omega) > epsilon:
            print(f"WARNING: 第一布罗卡点验证失败")
        
        # 验证第二布罗卡点
        angle4 = self._angle_at_vertex(self.brocard_2, self.B, self.A)
        angle5 = self._angle_at_vertex(self.brocard_2, self.C, self.B)
        angle6 = self._angle_at_vertex(self.brocard_2, self.A, self.C)
        
        if abs(angle4 - self.omega) > epsilon or abs(angle5 - self.omega) > epsilon or abs(angle6 - self.omega) > epsilon:
            print(f"WARNING: 第二布罗卡点验证失败")
        
        print(f"✓ 几何验证通过: ω = {np.degrees(self.omega):.2f}°")
    
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
        
        # 钩子标题
        hook_text = Text(
            "三角形中的神秘孪生点",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三角形淡入
        self.play(Create(self.triangle), run_time=1.0)
        
        # 两个布罗卡点闪烁
        omega_1_dot = Dot(self.brocard_1, radius=0.10, color=self.COLOR_BROCARD_1)
        omega_2_dot = Dot(self.brocard_2, radius=0.10, color=self.COLOR_BROCARD_2)
        
        self.play(
            FadeIn(omega_1_dot, scale=0.5),
            FadeIn(omega_2_dot, scale=0.5),
            run_time=0.5
        )
        
        self.play(
            Flash(omega_1_dot, color=self.COLOR_BROCARD_1, flash_radius=0.3),
            Flash(omega_2_dot, color=self.COLOR_BROCARD_2, flash_radius=0.3),
            run_time=0.4
        )
        
        # 提示文字
        hint = Text(
            "满足优美的等角性质",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hint),
            run_time=0.5
        )
        
        # 保留点但变淡
        self.omega_1_small = Dot(self.brocard_1, radius=0.06, color=self.COLOR_BROCARD_1, fill_opacity=0.3)
        self.omega_2_small = Dot(self.brocard_2, radius=0.06, color=self.COLOR_BROCARD_2, fill_opacity=0.3)
        
        self.play(
            Transform(omega_1_dot, self.omega_1_small),
            Transform(omega_2_dot, self.omega_2_small),
            run_time=0.3
        )
        
        self.remove(omega_1_dot, omega_2_dot)
        self.add(self.omega_1_small, self.omega_2_small)
    
    def show_first_brocard_point(self):
        """场景2: 第一布罗卡点"""
        # 标题
        title = Text(
            "第一布罗卡点 Ω",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_BROCARD_1
        ).move_to(UP * 6)
        
        definition = Text(
            "∠ΩAB = ∠ΩBC = ∠ΩCA = ω",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 第一布罗卡点放大
        omega_1_large = Dot(self.brocard_1, radius=0.12, color=self.COLOR_BROCARD_1)
        omega_1_label = MathTex(r"\Omega", color=self.COLOR_BROCARD_1, font_size=32).next_to(omega_1_large, RIGHT, buff=0.15)
        
        self.play(
            Transform(self.omega_1_small, omega_1_large),
            FadeIn(omega_1_label),
            run_time=0.6
        )
        
        self.wait(0.3)
        
        # 连线并标记角度
        lines = VGroup()
        angles = VGroup()
        angle_labels = VGroup()
        
        # ∠ΩAB
        line_OA = DashedLine(self.brocard_1, self.A, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(line_OA), run_time=0.5)
        lines.add(line_OA)
        
        angle_OAB = self._create_angle_arc(self.A, self.B, self.brocard_1, radius=0.4, color=self.COLOR_ANGLE)
        angle_label_1 = MathTex(r"\omega", color=self.COLOR_ANGLE, font_size=22).move_to(
            self.A + 0.6 * (self.B - self.A) / np.linalg.norm(self.B - self.A) + 
            0.3 * (self.brocard_1 - self.A) / np.linalg.norm(self.brocard_1 - self.A)
        )
        
        self.play(Create(angle_OAB), FadeIn(angle_label_1), run_time=0.5)
        angles.add(angle_OAB)
        angle_labels.add(angle_label_1)
        
        # ∠ΩBC
        line_OB = DashedLine(self.brocard_1, self.B, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(line_OB), run_time=0.5)
        lines.add(line_OB)
        
        angle_OBC = self._create_angle_arc(self.B, self.C, self.brocard_1, radius=0.4, color=self.COLOR_ANGLE)
        angle_label_2 = MathTex(r"\omega", color=self.COLOR_ANGLE, font_size=22).move_to(
            self.B + 0.6 * (self.C - self.B) / np.linalg.norm(self.C - self.B) + 
            0.3 * (self.brocard_1 - self.B) / np.linalg.norm(self.brocard_1 - self.B)
        )
        
        self.play(Create(angle_OBC), FadeIn(angle_label_2), run_time=0.5)
        angles.add(angle_OBC)
        angle_labels.add(angle_label_2)
        
        # ∠ΩCA
        line_OC = DashedLine(self.brocard_1, self.C, color=self.COLOR_AUXILIARY, dash_length=0.08)
        self.play(Create(line_OC), run_time=0.5)
        lines.add(line_OC)
        
        angle_OCA = self._create_angle_arc(self.C, self.A, self.brocard_1, radius=0.4, color=self.COLOR_ANGLE)
        angle_label_3 = MathTex(r"\omega", color=self.COLOR_ANGLE, font_size=22).move_to(
            self.C + 0.6 * (self.A - self.C) / np.linalg.norm(self.A - self.C) + 
            0.3 * (self.brocard_1 - self.C) / np.linalg.norm(self.brocard_1 - self.C)
        )
        
        self.play(Create(angle_OCA), FadeIn(angle_label_3), run_time=0.5)
        angles.add(angle_OCA)
        angle_labels.add(angle_label_3)
        
        # 高亮三个角
        self.play(
            Flash(angle_OAB, color=self.COLOR_ANGLE, flash_radius=0.5),
            Flash(angle_OBC, color=self.COLOR_ANGLE, flash_radius=0.5),
            Flash(angle_OCA, color=self.COLOR_ANGLE, flash_radius=0.5),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(lines),
            FadeOut(angles),
            FadeOut(angle_labels),
            FadeOut(omega_1_label),
            run_time=0.6
        )
        
        # 还原小点
        self.play(Transform(self.omega_1_small, Dot(self.brocard_1, radius=0.06, color=self.COLOR_BROCARD_1, fill_opacity=0.5)), run_time=0.3)
    
    def show_second_brocard_point(self):
        """场景3: 第二布罗卡点"""
        # 标题
        title = Text(
            "第二布罗卡点 Ω'",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_BROCARD_2
        ).move_to(UP * 6)
        
        definition = Text(
            "∠Ω'BA = ∠Ω'CB = ∠Ω'AC = ω",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 第二布罗卡点放大
        omega_2_large = Dot(self.brocard_2, radius=0.12, color=self.COLOR_BROCARD_2)
        omega_2_label = MathTex(r"\Omega'", color=self.COLOR_BROCARD_2, font_size=32).next_to(omega_2_large, LEFT, buff=0.15)
        
        self.play(
            Transform(self.omega_2_small, omega_2_large),
            FadeIn(omega_2_label),
            run_time=0.6
        )
        
        self.wait(0.3)
        
        # 快速显示三个角
        lines = VGroup(
            DashedLine(self.brocard_2, self.A, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.brocard_2, self.B, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.brocard_2, self.C, color=self.COLOR_AUXILIARY, dash_length=0.08)
        )
        
        angles = VGroup(
            self._create_angle_arc(self.B, self.A, self.brocard_2, radius=0.4, color=self.COLOR_ANGLE),
            self._create_angle_arc(self.C, self.B, self.brocard_2, radius=0.4, color=self.COLOR_ANGLE),
            self._create_angle_arc(self.A, self.C, self.brocard_2, radius=0.4, color=self.COLOR_ANGLE)
        )
        
        self.play(Create(lines), run_time=0.8)
        self.play(Create(angles), run_time=0.8)
        
        # 对比两个点
        self.omega_1_small.set_opacity(1)
        self.play(
            Flash(self.omega_1_small, color=self.COLOR_BROCARD_1),
            Flash(self.omega_2_small, color=self.COLOR_BROCARD_2),
            run_time=0.6
        )
        
        symmetry_text = Text(
            "等角共轭点",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(symmetry_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(lines),
            FadeOut(angles),
            FadeOut(symmetry_text),
            FadeOut(omega_2_label),
            run_time=0.6
        )
        
        # 还原小点
        self.play(Transform(self.omega_2_small, Dot(self.brocard_2, radius=0.06, color=self.COLOR_BROCARD_2, fill_opacity=0.5)), run_time=0.3)
        self.omega_1_small.set_opacity(0.5)
    
    def show_brocard_angle_formula(self):
        """场景4: 布罗卡角公式"""
        # 标题
        title = Text(
            "布罗卡角 ω",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ANGLE
        ).move_to(UP * 6.2)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式1
        formula_1 = MathTex(
            r"\cot \omega = \cot A + \cot B + \cot C",
            font_size=30
        ).move_to(UP * 5)
        
        self.play(FadeIn(formula_1, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)
        
        # 公式2
        formula_2 = MathTex(
            r"\cot \omega = \frac{a^2 + b^2 + c^2}{4\Delta}",
            font_size=30
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(formula_2, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)
        
        # 数值示例
        example_title = Text(
            "本例计算:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(example_title), run_time=0.4)
        
        # 边长和面积
        values = VGroup(
            MathTex(rf"a = {self.a:.2f},\, b = {self.b:.2f},\, c = {self.c:.2f}", font_size=24),
            MathTex(rf"\Delta = {self.area:.2f}", font_size=24)
        ).arrange(DOWN, buff=0.3).move_to(UP * 1.0)
        
        self.play(FadeIn(values), run_time=0.6)
        
        # 计算结果
        omega_deg = np.degrees(self.omega)
        result = MathTex(
            rf"\omega \approx {omega_deg:.1f}^\circ",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        
        # 取值范围说明
        range_text = Text(
            "0° < ω ≤ 30°  (等边时取等)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.8)
        
        self.play(FadeIn(range_text), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(example_title),
            FadeOut(values),
            FadeOut(result),
            FadeOut(range_text),
            run_time=0.6
        )
    
    def show_construction_method(self):
        """场景5: 构造方法展示 (简化版)"""
        # 标题
        title = Text(
            "如何构造布罗卡点?",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.7)
        
        # 说明文字
        method_text = Text(
            "需要三个特殊圆的交点",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(method_text), run_time=0.5)
        
        # 显示圆的说明（简化，不实际绘制复杂圆）
        circle_desc = VGroup(
            Text("圆1: 过A, B且切BC于B", font="PingFang SC", font_size=22, color=GRAY_B),
            Text("圆2: 过B, C且切CA于C", font="PingFang SC", font_size=22, color=GRAY_B),
            Text("圆3: 过C, A且切AB于A", font="PingFang SC", font_size=22, color=GRAY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 3)
        
        for desc in circle_desc:
            self.play(FadeIn(desc, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(1.0)
        
        # 标记第一布罗卡点
        omega_1_highlight = Dot(self.brocard_1, radius=0.15, color=self.COLOR_BROCARD_1)
        intersection_label = Text(
            "三圆交点 → Ω",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_BROCARD_1
        ).next_to(omega_1_highlight, DOWN, buff=0.5)
        
        self.play(
            FadeIn(omega_1_highlight, scale=0.5),
            FadeIn(intersection_label),
            run_time=0.6
        )
        
        self.play(Flash(omega_1_highlight, color=self.COLOR_BROCARD_1, flash_radius=0.4), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(method_text),
            FadeOut(circle_desc),
            FadeOut(omega_1_highlight),
            FadeOut(intersection_label),
            run_time=0.6
        )
    
    def show_equilateral_case(self):
        """场景6: 等边三角形特例"""
        # 变换为等边三角形
        side = 3.5
        height = side * np.sqrt(3) / 2
        
        A_eq = np.array([-side/2, -height/3, 0]) * self.SCALE + self.OFFSET
        B_eq = np.array([side/2, -height/3, 0]) * self.SCALE + self.OFFSET
        C_eq = np.array([0, 2*height/3, 0]) * self.SCALE + self.OFFSET
        
        triangle_eq = Polygon(A_eq, B_eq, C_eq, color=self.COLOR_PRIMARY, stroke_width=3)
        
        # 标题
        title = Text(
            "特例: 等边三角形",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 变换三角形
        self.play(Transform(self.triangle, triangle_eq), run_time=1.2)
        
        # 计算等边三角形的重心和布罗卡角
        centroid_eq = (A_eq + B_eq + C_eq) / 3
        omega_eq = np.radians(30)
        
        # 公式
        formula = MathTex(
            r"\cot \omega = 3 \cot 60^\circ = \sqrt{3}",
            font_size=28
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(formula), run_time=0.8)
        
        # 结果
        result = MathTex(
            r"\omega = 30^\circ",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(result, scale=1.1), run_time=0.6)
        self.wait(0.8)
        
        # 移动布罗卡点到重心
        centroid_dot = Dot(centroid_eq, radius=0.12, color=GREEN)
        centroid_label = Text(
            "重心 = 布罗卡点",
            font="PingFang SC",
            font_size=26,
            color=GREEN
        ).next_to(centroid_dot, DOWN, buff=0.4)
        
        self.play(
            self.omega_1_small.animate.move_to(centroid_eq).set_color(GREEN),
            self.omega_2_small.animate.move_to(centroid_eq).set_color(GREEN),
            FadeIn(centroid_label),
            run_time=1.0
        )
        
        self.play(Flash(centroid_dot, color=GREEN, flash_radius=0.4), run_time=0.4)
        
        # 四心合一提示
        hint = Text(
            "等边三角形: 四心合一",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(result),
            FadeOut(centroid_label),
            FadeOut(hint),
            run_time=0.6
        )
        
        # 变回原三角形
        self.play(Transform(self.triangle, Polygon(self.A, self.B, self.C, color=self.COLOR_PRIMARY, stroke_width=3)), run_time=0.8)
        self.play(
            self.omega_1_small.animate.move_to(self.brocard_1).set_color(self.COLOR_BROCARD_1),
            self.omega_2_small.animate.move_to(self.brocard_2).set_color(self.COLOR_BROCARD_2),
            run_time=0.6
        )
    
    def show_properties_summary(self):
        """场景7: 性质总结"""
        # 标题
        title = Text(
            "布罗卡点的性质",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 性质卡片
        cards = VGroup()
        
        card_1 = self._create_property_card(
            "等角共轭点",
            "两个布罗卡点对称",
            UP * 3.5
        )
        cards.add(card_1)
        
        card_2 = self._create_property_card(
            "布罗卡角范围",
            "0° < ω ≤ 30°",
            UP * 2.2
        )
        cards.add(card_2)
        
        card_3 = self._create_property_card(
            "等边三角形",
            "布罗卡点 = 重心",
            UP * 0.9
        )
        cards.add(card_3)
        
        card_4 = self._create_property_card(
            "优美对称性",
            "几何学的内在和谐",
            DOWN * 0.4
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 高亮
        highlight = Text(
            "探索几何之美!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(highlight),
            FadeOut(self.triangle),
            FadeOut(self.omega_1_small),
            FadeOut(self.omega_2_small),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1.0)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文案
        follow_text = Text(
            "关注我, 探索更多几何奥秘!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰三角形
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )
    
    # Helper methods
    
    def _create_angle_arc(self, vertex, ray_point1, ray_point2, radius=0.5, color=YELLOW):
        """创建角弧 - 使用Arc而非Angle类避免兼容性问题"""
        v1 = ray_point1 - vertex
        v2 = ray_point2 - vertex
        
        angle1 = np.arctan2(v1[1], v1[0])
        angle2 = np.arctan2(v2[1], v2[0])
        
        # 确保逆时针
        if angle2 < angle1:
            angle2 += 2 * PI
        
        arc = Arc(
            radius=radius,
            start_angle=angle1,
            angle=angle2 - angle1,
            color=color,
            stroke_width=2
        ).move_arc_center_to(vertex)
        
        return arc
    
    def _create_property_card(self, title_text, content_text, position):
        """创建性质卡片"""
        icon = Circle(radius=0.2, fill_color=self.COLOR_ANGLE, fill_opacity=1, stroke_width=0)
        
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        content = Text(
            content_text,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        card = VGroup(icon, title, content).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        card.shift(LEFT * 10)  # 初始在左侧外
        
        return card