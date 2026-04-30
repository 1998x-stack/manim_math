"""
切线的性质与判定 - Tangent Properties and Theorems
使用 Manim 创建的初中几何教学视频

内容: 切线性质、切线判定、切线长定理
目标观众: 初中生
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


class TangentTheorems(Scene):
    """
    切线的性质与判定教学动画
    
    场景顺序:
    1. 开场钩子
    2. 切线性质 (切线⊥半径)
    3. 切线判定定理
    4. 切线长定理准备
    5. 切线长定理演示
    6. 知识总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"        # 蓝色 - 圆
        self.COLOR_TANGENT = "#e74c3c"       # 红色 - 切线
        self.COLOR_RADIUS = "#2ecc71"        # 绿色 - 半径
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_EQUAL = "#f39c12"         # 橙色 - 相等标记
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_tangent_property()
        self.scene_3_tangent_criterion()
        self.scene_4_tangent_length_prep()
        self.scene_5_tangent_length_theorem()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 圆的基本参数
        self.O = np.array([0, 1.5, 0])  # 圆心位置
        self.r = 2.0                     # 半径
        
        # 切点T的位置 (在圆的右侧,方便演示)
        # 选择角度 30度
        angle_T = np.radians(30)
        self.T = self.O + self.r * np.array([np.cos(angle_T), np.sin(angle_T), 0])
        
        # 切线方向 (垂直于半径OT)
        radius_dir = self.T - self.O
        # 逆时针旋转90度得到切线方向
        self.tangent_dir = np.array([-radius_dir[1], radius_dir[0], 0])
        self.tangent_dir = self.tangent_dir / np.linalg.norm(self.tangent_dir)
        
        # 圆外点P的位置 (用于切线长定理)
        # P点位置要确保在圆外,且两条切线在视野内
        self.P = np.array([3.0, 3.5, 0])
        
        # 验证P在圆外
        dist_OP = np.linalg.norm(self.P - self.O)
        assert dist_OP > self.r, f"P点必须在圆外! 距离={dist_OP:.2f}, 半径={self.r}"
        
        # 计算从P到圆的两个切点A和B
        self.A, self.B = self.calculate_tangent_points(self.P)
        
        # 计算切线长
        self.tangent_length = np.linalg.norm(self.P - self.A)
        
        # 验证几何关系
        self.verify_geometry()
        
        # 创建圆对象
        self.circle = Circle(
            radius=self.r,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
    
    def calculate_tangent_points(self, P):
        """
        计算从圆外点P到圆的两个切点
        
        方法: 使用几何关系
        - 切点在圆上: ||切点-O|| = r
        - 切线垂直于半径: (P-切点)·(O-切点) = 0
        - 在直角三角形OTP中: OP² = OT² + TP²
        - 因此: ∠TOP = arcsin(TP/OP) = arcsin(l/d)
        - 其中 l = √(d²-r²) 是切线长
        
        正确的角度关系:
        - 从O看P的角度 θ_OP
        - 切点偏移角度 α = arccos(r/d)
        """
        O = self.O
        r = self.r
        
        # OP向量和距离
        OP = P - O
        d = np.linalg.norm(OP)
        
        # 切线长
        l = np.sqrt(d**2 - r**2)
        
        # OP的角度
        theta_OP = np.arctan2(OP[1], OP[0])
        
        # 关键: ∠POT (从OP到OT的角度)
        # 在直角三角形中，sin(∠OPT) = r/d
        # 所以 ∠OPT = arcsin(r/d)
        # ∠POT = π/2 - ∠OPT = π/2 - arcsin(r/d) = arccos(r/d)
        angle_offset = np.arccos(r / d)
        
        # 两个切点的角度
        angle_A = theta_OP - angle_offset
        angle_B = theta_OP + angle_offset
        
        # 计算切点位置
        A = O + r * np.array([np.cos(angle_A), np.sin(angle_A), 0])
        B = O + r * np.array([np.cos(angle_B), np.sin(angle_B), 0])
        
        return A, B
    
    def verify_geometry(self):
        """验证所有几何关系"""
        epsilon = 1e-6
        errors = []
        
        # 验证T在圆上
        dist_OT = np.linalg.norm(self.T - self.O)
        if abs(dist_OT - self.r) > epsilon:
            errors.append(f"T不在圆上: 距离={dist_OT:.6f}, 半径={self.r}")
        
        # 验证切线方向垂直于半径
        radius_vec = self.T - self.O
        dot_product = np.dot(radius_vec[:2], self.tangent_dir[:2])
        if abs(dot_product) > epsilon:
            errors.append(f"切线不垂直于半径: 点积={dot_product:.6f}")
        
        # 验证P在圆外
        dist_OP = np.linalg.norm(self.P - self.O)
        if dist_OP <= self.r:
            errors.append(f"P不在圆外: 距离={dist_OP:.2f}, 半径={self.r}")
        
        # 验证A和B在圆上
        dist_OA = np.linalg.norm(self.A - self.O)
        dist_OB = np.linalg.norm(self.B - self.O)
        
        if abs(dist_OA - self.r) > epsilon:
            errors.append(f"A不在圆上: 距离={dist_OA:.6f}")
        if abs(dist_OB - self.r) > epsilon:
            errors.append(f"B不在圆上: 距离={dist_OB:.6f}")
        
        # 验证PA垂直于OA
        vec_PA = self.A - self.P
        vec_OA = self.A - self.O
        dot_PA_OA = np.dot(vec_PA[:2], vec_OA[:2])
        if abs(dot_PA_OA) > epsilon:
            errors.append(f"PA不垂直于OA: 点积={dot_PA_OA:.6f}")
        
        # 验证PB垂直于OB
        vec_PB = self.B - self.P
        vec_OB = self.B - self.O
        dot_PB_OB = np.dot(vec_PB[:2], vec_OB[:2])
        if abs(dot_PB_OB) > epsilon:
            errors.append(f"PB不垂直于OB: 点积={dot_PB_OB:.6f}")
        
        # 验证切线长相等
        length_PA = np.linalg.norm(self.P - self.A)
        length_PB = np.linalg.norm(self.P - self.B)
        if abs(length_PA - length_PB) > epsilon:
            errors.append(f"切线长不相等: PA={length_PA:.6f}, PB={length_PB:.6f}")
        
        # 验证边界
        # 检查所有关键点是否在安全范围内
        points_to_check = [
            ("O", self.O),
            ("T", self.T),
            ("P", self.P),
            ("A", self.A),
            ("B", self.B)
        ]
        
        for name, point in points_to_check:
            if point[0] < -4 or point[0] > 4:
                errors.append(f"{name}点x坐标溢出: x={point[0]:.2f}")
            if point[1] < -6 or point[1] > 6:
                errors.append(f"{name}点y坐标溢出: y={point[1]:.2f}")
        
        # 输出结果
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败!")
        else:
            print("✓ 几何验证通过")
            print(f"  圆心O: {self.O}")
            print(f"  半径r: {self.r}")
            print(f"  切点T: {self.T}")
            print(f"  圆外点P: {self.P}")
            print(f"  切点A: {self.A}")
            print(f"  切点B: {self.B}")
            print(f"  切线长: {self.tangent_length:.4f}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "什么是切线?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 圆淡入
        self.play(FadeIn(self.circle, scale=0.8), run_time=0.6)
        
        # 直线从远处移动到相切位置
        # 创建一条移动的直线
        tangent_length_display = 3.0
        moving_line = Line(
            self.T - self.tangent_dir * tangent_length_display,
            self.T + self.tangent_dir * tangent_length_display,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        # 初始位置: 远离圆
        moving_line.shift(DOWN * 4)
        
        self.play(Create(moving_line), run_time=0.5)
        
        # 移动到相切位置
        self.play(
            moving_line.animate.shift(UP * 4),
            run_time=2.0,
            rate_func=smooth
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(moving_line),
            run_time=0.4
        )
    
    def scene_2_tangent_property(self):
        """场景2: 切线性质 - 切线垂直于过切点的半径"""
        # 标题
        title = Text(
            "切线性质",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记圆心O
        O_dot = Dot(self.O, color=self.COLOR_RADIUS, radius=0.08)
        O_label = MathTex("O", font_size=28, color=self.COLOR_RADIUS).next_to(
            O_dot, DOWN, buff=0.15
        )
        
        self.play(FadeIn(O_dot, scale=0.5), run_time=0.3)
        self.play(Write(O_label), run_time=0.3)
        
        # 标记切点T
        T_dot = Dot(self.T, color=self.COLOR_HIGHLIGHT, radius=0.10)
        T_label = MathTex("T", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            T_dot, UR, buff=0.15
        )
        
        self.play(FadeIn(T_dot, scale=0.5), run_time=0.4)
        self.play(Flash(T_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.3)
        self.play(Write(T_label), run_time=0.3)
        
        # 绘制半径OT
        radius_OT = Line(
            self.O, self.T,
            color=self.COLOR_RADIUS,
            stroke_width=3
        )
        
        self.play(Create(radius_OT), run_time=0.8)
        
        # 绘制切线l
        tangent_length = 3.0
        tangent_line = Line(
            self.T - self.tangent_dir * tangent_length,
            self.T + self.tangent_dir * tangent_length,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        l_label = MathTex("l", font_size=28, color=self.COLOR_TANGENT).move_to(
            self.T + self.tangent_dir * (tangent_length + 0.3)
        )
        
        self.play(Create(tangent_line), run_time=0.8)
        self.play(Write(l_label), run_time=0.3)
        
        # 添加垂直符号
        right_angle = self.create_right_angle_mark(
            self.T, self.O, self.T + self.tangent_dir, size=0.25
        )
        
        self.play(FadeIn(right_angle), run_time=0.5)
        
        # 公式
        formula = MathTex(
            "l", r"\perp", "OT",
            font_size=32
        ).move_to(DOWN * 3.5)
        formula[0].set_color(self.COLOR_TANGENT)
        formula[2].set_color(self.COLOR_RADIUS)
        
        self.play(Write(formula), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "切线垂直于过切点的半径",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(explain), run_time=0.6)
        
        # 强调垂直关系
        self.play(
            Indicate(right_angle, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(tangent_line),
            FadeOut(l_label),
            FadeOut(right_angle),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.5
        )
        
        # 保留用于下一场景
        self.O_dot = O_dot
        self.O_label = O_label
        self.T_dot = T_dot
        self.T_label = T_label
        self.radius_OT = radius_OT
    
    def scene_3_tangent_criterion(self):
        """场景3: 切线判定定理"""
        # 标题
        title = Text(
            "切线判定",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 强调T点是半径外端
        self.play(
            Indicate(self.T_dot, color=self.COLOR_HIGHLIGHT, scale_factor=1.5),
            run_time=0.8
        )
        
        # 条件1: 直线过T点
        condition_1 = Text(
            "条件1: 直线过半径外端T",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(condition_1, shift=RIGHT * 0.3), run_time=0.6)
        
        # 绘制过T的直线
        tangent_length = 3.0
        perpendicular_line = Line(
            self.T - self.tangent_dir * tangent_length,
            self.T + self.tangent_dir * tangent_length,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        self.play(Create(perpendicular_line), run_time=0.8)
        
        # 条件2: 垂直于半径
        condition_2 = Text(
            "条件2: 且垂直于这条半径",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(condition_2, shift=RIGHT * 0.3), run_time=0.6)
        
        # 添加垂直符号
        right_angle = self.create_right_angle_mark(
            self.T, self.O, self.T + self.tangent_dir, size=0.25
        )
        
        self.play(FadeIn(right_angle), run_time=0.5)
        
        # 推导箭头
        arrow = Arrow(
            UP * 3.2, UP * 2.4,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.6)
        
        # 结论
        conclusion = Text(
            "则此直线是圆的切线",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)
        
        self.play(Write(conclusion), run_time=0.8)
        
        # 关键提示
        key_hint = Text(
            "两个条件缺一不可!",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(key_hint, scale=1.1), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition_1),
            FadeOut(condition_2),
            FadeOut(perpendicular_line),
            FadeOut(right_angle),
            FadeOut(arrow),
            FadeOut(conclusion),
            FadeOut(key_hint),
            FadeOut(self.radius_OT),
            FadeOut(self.T_dot),
            FadeOut(self.T_label),
            run_time=0.6
        )
    
    def scene_4_tangent_length_prep(self):
        """场景4: 切线长定理准备"""
        # 标题
        title = Text(
            "切线长定理",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标记圆外点P
        P_dot = Dot(self.P, color=self.COLOR_EQUAL, radius=0.10)
        P_label = MathTex("P", font_size=28, color=self.COLOR_EQUAL).next_to(
            P_dot, UR, buff=0.15
        )
        
        self.play(FadeIn(P_dot, scale=0.5), run_time=0.4)
        self.play(Flash(P_dot, color=self.COLOR_EQUAL, flash_radius=0.3), run_time=0.3)
        self.play(Write(P_label), run_time=0.3)
        
        # 连接PO (虚线)
        line_PO = DashedLine(
            self.P, self.O,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(line_PO), run_time=0.8)
        
        # 提示文字
        hint = Text(
            "从P引两条切线到圆...",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint), run_time=0.6)
        self.wait(1.5)
        
        # 清理提示
        self.play(FadeOut(hint), run_time=0.3)
        
        # 保留元素
        self.title_tangent_length = title
        self.P_dot = P_dot
        self.P_label = P_label
        self.line_PO = line_PO
    
    def scene_5_tangent_length_theorem(self):
        """场景5: 切线长定理演示"""
        # 绘制第一条切线PA
        tangent_PA = Line(
            self.P, self.A,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        self.play(Create(tangent_PA), run_time=1.0)
        
        # 标记切点A
        A_dot = Dot(self.A, color=self.COLOR_HIGHLIGHT, radius=0.09)
        A_label = MathTex("A", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            A_dot, LEFT, buff=0.15
        )
        
        self.play(FadeIn(A_dot, scale=0.5), run_time=0.3)
        self.play(Flash(A_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.3)
        self.play(Write(A_label), run_time=0.3)
        
        # 绘制第二条切线PB
        tangent_PB = Line(
            self.P, self.B,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        self.play(Create(tangent_PB), run_time=1.0)
        
        # 标记切点B
        B_dot = Dot(self.B, color=self.COLOR_HIGHLIGHT, radius=0.09)
        B_label = MathTex("B", font_size=24, color=self.COLOR_HIGHLIGHT).next_to(
            B_dot, RIGHT, buff=0.15
        )
        
        self.play(FadeIn(B_dot, scale=0.5), run_time=0.3)
        self.play(Flash(B_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.25), run_time=0.3)
        self.play(Write(B_label), run_time=0.3)
        
        # 绘制半径OA和OB (虚线)
        radius_OA = DashedLine(
            self.O, self.A,
            color=self.COLOR_RADIUS,
            dash_length=0.08,
            stroke_width=2
        )
        
        radius_OB = DashedLine(
            self.O, self.B,
            color=self.COLOR_RADIUS,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(radius_OA), run_time=0.6)
        self.play(Create(radius_OB), run_time=0.6)
        
        # 标注切线长PA
        brace_PA = Brace(tangent_PA, direction=tangent_PA.copy().rotate(-PI/2).get_unit_vector(), buff=0.05)
        PA_label = MathTex("PA", font_size=20).next_to(brace_PA, LEFT, buff=0.05)
        
        self.play(FadeIn(brace_PA), Write(PA_label), run_time=0.6)
        
        # 标注切线长PB
        brace_PB = Brace(tangent_PB, direction=tangent_PB.copy().rotate(PI/2).get_unit_vector(), buff=0.05)
        PB_label = MathTex("PB", font_size=20).next_to(brace_PB, RIGHT, buff=0.05)
        
        self.play(FadeIn(brace_PB), Write(PB_label), run_time=0.6)
        
        # 相等公式
        equal_formula = MathTex(
            "PA", "=", "PB",
            font_size=32,
            color=self.COLOR_EQUAL
        ).move_to(DOWN * 4)
        
        self.play(Write(equal_formula), run_time=0.8)
        
        # 添加双等号标记在两条切线上
        # PA中点
        mid_PA = (self.P + self.A) / 2
        equal_mark_1 = MathTex(r"\parallel", font_size=20, color=self.COLOR_EQUAL).move_to(mid_PA).rotate(
            np.arctan2((self.A - self.P)[1], (self.A - self.P)[0])
        )
        
        # PB中点
        mid_PB = (self.P + self.B) / 2
        equal_mark_2 = MathTex(r"\parallel", font_size=20, color=self.COLOR_EQUAL).move_to(mid_PB).rotate(
            np.arctan2((self.B - self.P)[1], (self.B - self.P)[0])
        )
        
        self.play(
            FadeIn(equal_mark_1),
            FadeIn(equal_mark_2),
            run_time=0.5
        )
        
        # 说明文字
        explain = Text(
            "切线长相等!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explain, scale=1.1), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理所有元素
        self.play(
            FadeOut(self.title_tangent_length),
            FadeOut(self.P_dot),
            FadeOut(self.P_label),
            FadeOut(self.line_PO),
            FadeOut(tangent_PA),
            FadeOut(tangent_PB),
            FadeOut(A_dot),
            FadeOut(B_dot),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(radius_OA),
            FadeOut(radius_OB),
            FadeOut(brace_PA),
            FadeOut(brace_PB),
            FadeOut(PA_label),
            FadeOut(PB_label),
            FadeOut(equal_formula),
            FadeOut(equal_mark_1),
            FadeOut(equal_mark_2),
            FadeOut(explain),
            FadeOut(self.circle),
            FadeOut(self.O_dot),
            FadeOut(self.O_label),
            run_time=0.6
        )
    
    def scene_6_summary(self):
        """场景6: 知识总结"""
        # 标题
        title = Text(
            "切线三要素",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个知识卡片
        card_y_positions = [2.5, 0.5, -1.5]
        
        # 卡片1: 切线性质
        card_1 = self.create_knowledge_card(
            "1. 切线性质",
            "切线 ⊥ 过切点的半径",
            self.COLOR_CIRCLE,
            UP * card_y_positions[0]
        )
        
        # 卡片2: 切线判定
        card_2 = self.create_knowledge_card(
            "2. 切线判定",
            "过半径外端且垂直 ⟹ 切线",
            self.COLOR_TANGENT,
            UP * card_y_positions[1]
        )
        
        # 卡片3: 切线长定理
        card_3 = self.create_knowledge_card(
            "3. 切线长定理",
            "从圆外一点引两条切线,切线长相等",
            self.COLOR_EQUAL,
            UP * card_y_positions[2],
            font_size_content=18
        )
        
        cards = VGroup(card_1, card_2, card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 依次闪烁强调
        for card in cards:
            self.play(Indicate(card, color=self.COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.6)
            self.wait(0.3)
        
        # 重点提示
        key_point = Text(
            "掌握三要素, 轻松解题!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(key_point), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def create_knowledge_card(self, title_text, content_text, color, position, font_size_content=20):
        """创建知识卡片"""
        # 图标圆
        icon = Circle(radius=0.18, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content = Text(
            content_text,
            font="PingFang SC",
            font_size=font_size_content,
            color=self.COLOR_AUXILIARY
        )
        
        # 组合
        card = VGroup(icon, title, content).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
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
    
    def scene_7_outro(self):
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
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        circles = VGroup(*[
            Circle(radius=0.22, color=self.COLOR_CIRCLE, stroke_width=2, fill_opacity=0.3)
            .move_to(follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )


# 运行命令:
# manim -pql tangent_theorems.py TangentTheorems  # 快速预览
# manim -qh tangent_theorems.py TangentTheorems   # 高质量渲染