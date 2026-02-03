"""
圆的切线性质与判定 - Circle Tangent Properties and Criteria
使用 Manim 创建的中学几何教学视频

内容: 切线性质、切线判定、切线长定理
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


class TangentProperties(Scene):
    """
    圆的切线性质与判定教学动画
    
    场景顺序:
    1. 开场钩子
    2. 切线性质 - 引入
    3. 切线性质 - 证明垂直
    4. 切线判定 - 引入
    5. 切线判定 - 动画验证
    6. 切线长定理 - 引入
    7. 切线长定理 - 证明
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"      # 蓝色 - 圆
        self.COLOR_TANGENT = "#e74c3c"     # 红色 - 切线
        self.COLOR_RADIUS = "#2ecc71"      # 绿色 - 半径
        self.COLOR_HIGHLIGHT = YELLOW      # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B      # 灰色 - 辅助线
        self.COLOR_POINT = "#f39c12"       # 橙色 - 切点
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_tangent_property_intro()
        self.scene_3_perpendicular_proof()
        self.scene_4_tangent_criteria_intro()
        self.scene_5_tangent_criteria_demo()
        self.scene_6_tangent_length_intro()
        self.scene_7_tangent_length_proof()
        self.scene_8_summary_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的坐标"""
        # ========== 基础参数 ==========
        self.SCALE = 1.0
        self.MAIN_Y_OFFSET = 1.0  # 主图形区域的y偏移
        
        # ========== Scene 1-3: 切线性质 ==========
        # 圆心O和半径
        self.O = np.array([0, self.MAIN_Y_OFFSET, 0])
        self.radius = 2.0
        
        # 切点P (在圆的右侧)
        angle_P = 30 * DEGREES
        self.P = self.O + self.radius * np.array([np.cos(angle_P), np.sin(angle_P), 0])
        
        # 切线方向 (垂直于OP)
        OP_vec = self.P - self.O
        self.tangent_dir = np.array([-OP_vec[1], OP_vec[0], 0])
        self.tangent_dir = self.tangent_dir / np.linalg.norm(self.tangent_dir)
        
        # 切线端点
        tangent_extend = 2.5
        self.tangent_start = self.P - self.tangent_dir * tangent_extend
        self.tangent_end = self.P + self.tangent_dir * tangent_extend
        
        # ========== Scene 4-5: 切线判定 ==========
        # 半径外端点Q (用于判定演示)
        angle_Q = -20 * DEGREES
        self.Q = self.O + self.radius * np.array([np.cos(angle_Q), np.sin(angle_Q), 0])
        
        # OQ方向
        OQ_vec = self.Q - self.O
        self.perp_to_OQ = np.array([-OQ_vec[1], OQ_vec[0], 0])
        self.perp_to_OQ = self.perp_to_OQ / np.linalg.norm(self.perp_to_OQ)
        
        # ========== Scene 6-7: 切线长定理 ==========
        # 圆外点P (不同于Scene 1的切点P，这里重命名)
        self.P_external = np.array([-2.5, self.MAIN_Y_OFFSET + 2.0, 0])
        
        # 计算两个切点A和B
        self.A, self.B = self.calculate_tangent_points(
            self.P_external, self.O, self.radius
        )
        
        # 切线长
        self.tangent_length_PA = np.linalg.norm(self.A - self.P_external)
        self.tangent_length_PB = np.linalg.norm(self.B - self.P_external)
        
        # ========== 验证几何关系 ==========
        self.verify_geometry()
    
    def calculate_tangent_points(self, P, O, radius):
        """
        从圆外点P到圆O(半径radius)的两个切点
        
        精确几何计算方法:
        1. 计算PO距离d
        2. 计算切线长 l = sqrt(d^2 - r^2)
        3. 使用投影方法找到切点
        
        Returns: (A, B) 两个切点坐标
        """
        # PO向量和距离
        PO_vec = O - P
        d = np.linalg.norm(PO_vec)
        
        if d <= radius:
            raise ValueError(f"点P必须在圆外! d={d:.3f}, r={radius:.3f}")
        
        # 切线长
        tangent_length = np.sqrt(d**2 - radius**2)
        
        # PO方向单位向量
        u = PO_vec / d
        
        # 垂直方向
        v = np.array([-u[1], u[0], 0])
        
        # 使用角度关系计算
        # cos(theta) = r/d, 其中theta是∠OPA (或∠OPB)
        cos_theta = radius / d
        sin_theta = tangent_length / d
        
        # 从P到切点的向量长度就是tangent_length
        # 方向是: u旋转±theta角度
        
        # 切点A (逆时针旋转)
        # PA方向 = cos(theta)*u + sin(theta)*v (但长度是tangent_length)
        # 不对，应该从O出发
        
        # 更简单的方法: 
        # M是PO上距离O为h的点，其中h = r^2/d
        # 从M垂直于PO的方向距离sqrt(r^2-h^2)到达切点
        
        h = radius**2 / d  # O到切线的垂直距离在PO上的投影长度
        M = O - h * u  # 垂足点M
        
        # 从M到切点的距离
        m_to_tangent = np.sqrt(radius**2 - h**2)
        
        # 两个切点
        A = M + m_to_tangent * v
        B = M - m_to_tangent * v
        
        return A, B
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        errors = []
        
        # ===== 验证切线性质 (Scene 1-3) =====
        # 1. P在圆上
        dist_OP = np.linalg.norm(self.P - self.O)
        if abs(dist_OP - self.radius) > epsilon:
            errors.append(f"P不在圆上: |OP|={dist_OP:.6f}, r={self.radius:.6f}")
        
        # 2. 切线垂直于半径
        OP_vec = self.P - self.O
        dot_product = np.dot(OP_vec[:2], self.tangent_dir[:2])
        if abs(dot_product) > epsilon:
            errors.append(f"切线不垂直于半径: OP·tangent_dir={dot_product:.6f}")
        
        # ===== 验证切线判定 (Scene 4-5) =====
        # Q在圆上
        dist_OQ = np.linalg.norm(self.Q - self.O)
        if abs(dist_OQ - self.radius) > epsilon:
            errors.append(f"Q不在圆上: |OQ|={dist_OQ:.6f}, r={self.radius:.6f}")
        
        # perp_to_OQ确实垂直于OQ
        OQ_vec = self.Q - self.O
        dot_product_2 = np.dot(OQ_vec[:2], self.perp_to_OQ[:2])
        if abs(dot_product_2) > epsilon:
            errors.append(f"perp_to_OQ不垂直于OQ: OQ·perp={dot_product_2:.6f}")
        
        # ===== 验证切线长定理 (Scene 6-7) =====
        # 1. P_external在圆外
        dist_PO = np.linalg.norm(self.P_external - self.O)
        if dist_PO <= self.radius:
            errors.append(f"P_external不在圆外: |PO|={dist_PO:.6f}, r={self.radius:.6f}")
        
        # 2. A和B在圆上
        dist_OA = np.linalg.norm(self.A - self.O)
        dist_OB = np.linalg.norm(self.B - self.O)
        if abs(dist_OA - self.radius) > epsilon:
            errors.append(f"A不在圆上: |OA|={dist_OA:.6f}, r={self.radius:.6f}")
        if abs(dist_OB - self.radius) > epsilon:
            errors.append(f"B不在圆上: |OB|={dist_OB:.6f}, r={self.radius:.6f}")
        
        # 3. PA垂直于OA
        PA_vec = self.A - self.P_external
        OA_vec = self.A - self.O
        dot_PA_OA = np.dot(PA_vec[:2], OA_vec[:2])
        if abs(dot_PA_OA) > epsilon:
            errors.append(f"PA不垂直于OA: PA·OA={dot_PA_OA:.6f}")
        
        # 4. PB垂直于OB
        PB_vec = self.B - self.P_external
        OB_vec = self.B - self.O
        dot_PB_OB = np.dot(PB_vec[:2], OB_vec[:2])
        if abs(dot_PB_OB) > epsilon:
            errors.append(f"PB不垂直于OB: PB·OB={dot_PB_OB:.6f}")
        
        # 5. PA = PB (切线长相等)
        if abs(self.tangent_length_PA - self.tangent_length_PB) > epsilon:
            errors.append(
                f"切线长不相等: PA={self.tangent_length_PA:.6f}, "
                f"PB={self.tangent_length_PB:.6f}"
            )
        
        # 6. 勾股定理: PA^2 + r^2 = PO^2
        expected_PO_sq = self.tangent_length_PA**2 + self.radius**2
        actual_PO_sq = dist_PO**2
        if abs(expected_PO_sq - actual_PO_sq) > epsilon:
            errors.append(
                f"勾股定理不成立: PA²+r²={expected_PO_sq:.6f}, "
                f"PO²={actual_PO_sq:.6f}"
            )
        
        # ===== 输出结果 =====
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败!")
        else:
            print("✓ 几何验证通过")
            print(f"  - 切点P: {self.P}")
            print(f"  - 圆外点P_external: {self.P_external}")
            print(f"  - 切点A: {self.A}")
            print(f"  - 切点B: {self.B}")
            print(f"  - 切线长PA: {self.tangent_length_PA:.4f}")
            print(f"  - 切线长PB: {self.tangent_length_PB:.4f}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "切线有什么神奇性质?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=0.8)
        
        # 神秘图形: 圆和切线
        circle_preview = Circle(
            radius=self.radius * 0.6,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(UP * 2)
        
        tangent_preview = Line(
            LEFT * 2, RIGHT * 2,
            color=self.COLOR_TANGENT,
            stroke_width=4
        ).move_to(circle_preview.get_center() + UP * (self.radius * 0.6))
        
        self.play(Create(circle_preview), run_time=0.5)
        self.play(Create(tangent_preview, run_time=0.5))
        
        # 问号
        question = Text("?", font_size=60, color=YELLOW).move_to(DOWN * 1)
        self.play(FadeIn(question, scale=1.5), run_time=0.3)
        self.play(Flash(question, color=YELLOW, flash_radius=0.8), run_time=0.4)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(circle_preview),
            FadeOut(tangent_preview),
            FadeOut(question),
            run_time=0.5
        )
    
    def scene_2_tangent_property_intro(self):
        """场景2: 切线性质 - 引入"""
        # 标题
        title = Text(
            "切线性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TANGENT
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "切线垂直于过切点的半径",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 绘制圆
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.circle), run_time=1.0)
        
        # 标记圆心O
        o_dot = Dot(self.O, color=WHITE, radius=0.08)
        o_label = MathTex("O", font_size=24).next_to(o_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(o_dot), Write(o_label), run_time=0.5)
        
        # 标记切点P
        p_dot = Dot(self.P, color=self.COLOR_POINT, radius=0.10)
        p_label = MathTex("P", font_size=24).next_to(p_dot, UR, buff=0.15)
        
        self.play(FadeIn(p_dot), Write(p_label), run_time=0.5)
        
        # 绘制半径OP
        radius_line = Line(self.O, self.P, color=self.COLOR_RADIUS, stroke_width=3)
        
        self.play(Create(radius_line), run_time=0.5)
        
        # 绘制切线
        tangent_line = Line(
            self.tangent_start,
            self.tangent_end,
            color=self.COLOR_TANGENT,
            stroke_width=3
        )
        
        # 切线标签
        tangent_label_text = Text("l", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_TANGENT)
        tangent_label_text.next_to(self.tangent_end, UP, buff=0.1)
        
        self.play(Create(tangent_line), Write(tangent_label_text), run_time=0.8)
        
        self.wait(1.0)
        
        # 保存对象供下一场景使用
        self.title_property = title
        self.subtitle_property = subtitle
        self.o_dot = o_dot
        self.o_label = o_label
        self.p_dot = p_dot
        self.p_label = p_label
        self.radius_line = radius_line
        self.tangent_line = tangent_line
        self.tangent_label_text = tangent_label_text
    
    def scene_3_perpendicular_proof(self):
        """场景3: 切线性质 - 证明垂直"""
        # 添加直角标记
        right_angle = RightAngle(
            Line(self.O, self.P),
            Line(self.P, self.tangent_end),
            length=0.3,
            quadrant=(1, 1),
            color=YELLOW,
            stroke_width=2
        )
        
        self.play(Create(right_angle), run_time=0.5)
        self.play(Flash(right_angle, color=YELLOW, flash_radius=0.5), run_time=0.4)
        
        # 公式
        formula_label = Text(
            "切线性质:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        formula_math = MathTex(
            r"l \perp OP",
            font_size=28
        )
        formula = VGroup(formula_label, formula_math).arrange(RIGHT, buff=0.2)
        formula.move_to(DOWN * 4)
        
        self.play(Write(formula_label), Write(formula_math), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "圆的切线垂直于过切点的半径",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 动画演示: 旋转半径和切线
        # 创建可旋转的半径和切线 (使用always_redraw)
        angle_tracker = ValueTracker(30 * DEGREES)
        
        rotating_P = always_redraw(lambda: Dot(
            self.O + self.radius * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()),
                0
            ]),
            color=self.COLOR_POINT,
            radius=0.10
        ))
        
        rotating_radius = always_redraw(lambda: Line(
            self.O,
            self.O + self.radius * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()),
                0
            ]),
            color=self.COLOR_RADIUS,
            stroke_width=3
        ))
        
        rotating_tangent = always_redraw(lambda: Line(
            self.O + self.radius * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()),
                0
            ]) + 2 * np.array([
                -np.sin(angle_tracker.get_value()),
                np.cos(angle_tracker.get_value()),
                0
            ]),
            self.O + self.radius * np.array([
                np.cos(angle_tracker.get_value()),
                np.sin(angle_tracker.get_value()),
                0
            ]) - 2 * np.array([
                -np.sin(angle_tracker.get_value()),
                np.cos(angle_tracker.get_value()),
                0
            ]),
            color=self.COLOR_TANGENT,
            stroke_width=3
        ))
        
        rotating_right_angle = always_redraw(lambda: RightAngle(
            Line(
                self.O,
                self.O + self.radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ])
            ),
            Line(
                self.O + self.radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ]),
                self.O + self.radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ]) + np.array([
                    -np.sin(angle_tracker.get_value()),
                    np.cos(angle_tracker.get_value()),
                    0
                ])
            ),
            length=0.3,
            quadrant=(1, 1),
            color=YELLOW,
            stroke_width=2
        ))
        
        # 替换静态元素
        self.play(
            FadeOut(self.p_dot),
            FadeOut(self.radius_line),
            FadeOut(self.tangent_line),
            FadeOut(right_angle),
            run_time=0.3
        )
        
        self.add(rotating_P, rotating_radius, rotating_tangent, rotating_right_angle)
        
        # 旋转动画
        self.play(
            angle_tracker.animate.set_value(30 * DEGREES + PI * 2 / 3),
            run_time=2.5,
            rate_func=smooth
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(self.title_property),
            FadeOut(self.subtitle_property),
            FadeOut(formula),
            FadeOut(explanation),
            FadeOut(rotating_P),
            FadeOut(rotating_radius),
            FadeOut(rotating_tangent),
            FadeOut(rotating_right_angle),
            FadeOut(self.o_dot),
            FadeOut(self.o_label),
            FadeOut(self.p_label),
            FadeOut(self.tangent_label_text),
            FadeOut(self.circle),
            run_time=0.6
        )
    
    def scene_4_tangent_criteria_intro(self):
        """场景4: 切线判定 - 引入"""
        # 标题
        title = Text(
            "切线判定",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "如何判断一条直线是否为切线?",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 三个判定条件卡片
        card1_icon = Circle(radius=0.15, fill_color=self.COLOR_RADIUS, fill_opacity=1, stroke_width=0)
        card1_text = Text("① 过半径外端", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card1 = VGroup(card1_icon, card1_text).arrange(RIGHT, buff=0.3)
        card1.move_to(UP * 1.5 + LEFT * 10)  # 初始在左侧外
        
        card2_icon = Circle(radius=0.15, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
        card2_text = Text("② 垂直于半径", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card2 = VGroup(card2_icon, card2_text).arrange(RIGHT, buff=0.3)
        card2.move_to(UP * 0.5 + LEFT * 10)
        
        card3_icon = Circle(radius=0.15, fill_color=self.COLOR_CIRCLE, fill_opacity=1, stroke_width=0)
        card3_text = Text("③ 只有一个交点", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card3 = VGroup(card3_icon, card3_text).arrange(RIGHT, buff=0.3)
        card3.move_to(DOWN * 0.5 + LEFT * 10)
        
        # 卡片滑入
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(subtitle),
            run_time=0.5
        )
        
        self.title_criteria = title
    
    def scene_5_tangent_criteria_demo(self):
        """场景5: 切线判定 - 动画验证"""
        # 重新绘制圆
        circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(circle), run_time=0.8)
        
        # 圆心和半径
        o_dot = Dot(self.O, color=WHITE, radius=0.08)
        o_label = MathTex("O", font_size=24).next_to(o_dot, DOWN, buff=0.15)
        
        radius_to_Q = Line(self.O, self.Q, color=self.COLOR_RADIUS, stroke_width=3)
        q_dot = Dot(self.Q, color=self.COLOR_POINT, radius=0.10)
        q_label = MathTex("Q", font_size=24).next_to(q_dot, DR, buff=0.15)
        
        self.play(
            FadeIn(o_dot), Write(o_label),
            Create(radius_to_Q),
            FadeIn(q_dot), Write(q_label),
            run_time=1.0
        )
        
        # 测试1: 不过外端 (在Q内侧的平行线)
        test_line_1_start = self.Q - 0.5 * (self.Q - self.O) / np.linalg.norm(self.Q - self.O) - 1.5 * self.perp_to_OQ
        test_line_1_end = self.Q - 0.5 * (self.Q - self.O) / np.linalg.norm(self.Q - self.O) + 1.5 * self.perp_to_OQ
        test_line_1 = Line(test_line_1_start, test_line_1_end, color=GRAY_B, stroke_width=3)
        
        explain_1 = Text(
            "不过半径外端 ✗",
            font="Noto Sans CJK SC",
            font_size=22,
            color=RED
        ).move_to(DOWN * 4.5)
        
        self.play(Create(test_line_1), run_time=0.6)
        self.play(FadeIn(explain_1, shift=UP * 0.3), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(explain_1), run_time=0.3)
        
        # 测试2: 不垂直 (过Q但不垂直)
        # 方向与OQ成45度
        non_perp_dir = (self.perp_to_OQ + (self.Q - self.O) / np.linalg.norm(self.Q - self.O)) / np.sqrt(2)
        test_line_2_start = self.Q - 1.8 * non_perp_dir
        test_line_2_end = self.Q + 1.8 * non_perp_dir
        test_line_2 = Line(test_line_2_start, test_line_2_end, color=GRAY_B, stroke_width=3)
        
        explain_2 = Text(
            "不垂直于半径 ✗",
            font="Noto Sans CJK SC",
            font_size=22,
            color=RED
        ).move_to(DOWN * 4.5)
        
        self.play(Transform(test_line_1, test_line_2), run_time=0.6)
        self.play(FadeIn(explain_2, shift=UP * 0.3), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(explain_2), run_time=0.3)
        
        # 测试3: 满足条件 (过Q且垂直)
        test_line_3_start = self.Q - 2.0 * self.perp_to_OQ
        test_line_3_end = self.Q + 2.0 * self.perp_to_OQ
        test_line_3 = Line(test_line_3_start, test_line_3_end, color=self.COLOR_TANGENT, stroke_width=4)
        
        self.play(Transform(test_line_1, test_line_3), run_time=0.6)
        
        # 添加直角标记
        right_angle = RightAngle(
            Line(self.O, self.Q),
            Line(self.Q, test_line_3_end),
            length=0.3,
            quadrant=(1, 1),
            color=YELLOW,
            stroke_width=2
        )
        
        self.play(Create(right_angle), run_time=0.5)
        
        explain_3 = Text(
            "满足条件! 这是切线 ✓",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_3, shift=UP * 0.3), run_time=0.5)
        self.play(Flash(right_angle, color=YELLOW), run_time=0.4)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(self.title_criteria),
            FadeOut(circle),
            FadeOut(o_dot),
            FadeOut(o_label),
            FadeOut(radius_to_Q),
            FadeOut(q_dot),
            FadeOut(q_label),
            FadeOut(test_line_1),
            FadeOut(right_angle),
            FadeOut(explain_3),
            run_time=0.6
        )
    
    def scene_6_tangent_length_intro(self):
        """场景6: 切线长定理 - 引入"""
        # 标题
        title = Text(
            "切线长定理",
            font="Noto Sans CJK SC",
            font_size=36,
            color="#9b59b6"  # 紫色
        ).move_to(UP * 5.5)
        
        definition = Text(
            "从圆外一点引两条切线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.5)
        
        # 绘制圆
        circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(circle), run_time=0.8)
        
        # 圆心O
        o_dot = Dot(self.O, color=WHITE, radius=0.08)
        o_label = MathTex("O", font_size=24).next_to(o_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(o_dot), Write(o_label), run_time=0.5)
        
        # 圆外点P
        p_ext_dot = Dot(self.P_external, color="#9b59b6", radius=0.12)
        p_ext_label = MathTex("P", font_size=24, color="#9b59b6").next_to(p_ext_dot, UP, buff=0.15)
        
        self.play(FadeIn(p_ext_dot), Write(p_ext_label), run_time=0.5)
        
        # 绘制切线PA
        tangent_PA = Line(self.P_external, self.A, color=self.COLOR_TANGENT, stroke_width=3)
        self.play(Create(tangent_PA), run_time=1.0)
        
        # 标记切点A
        a_dot = Dot(self.A, color=self.COLOR_POINT, radius=0.10)
        a_label = MathTex("A", font_size=24).next_to(a_dot, LEFT, buff=0.15)
        
        self.play(FadeIn(a_dot), Write(a_label), run_time=0.5)
        
        # 绘制切线PB
        tangent_PB = Line(self.P_external, self.B, color=self.COLOR_TANGENT, stroke_width=3)
        self.play(Create(tangent_PB), run_time=1.0)
        
        # 标记切点B
        b_dot = Dot(self.B, color=self.COLOR_POINT, radius=0.10)
        b_label = MathTex("B", font_size=24).next_to(b_dot, RIGHT, buff=0.15)
        
        self.play(FadeIn(b_dot), Write(b_label), run_time=0.5)
        
        # 标注切线长PA
        brace_PA = Brace(Line(self.P_external, self.A), direction=LEFT, buff=0.1, color=YELLOW)
        label_PA = brace_PA.get_text("PA", buff=0.1).set_color(YELLOW).scale(0.8)
        
        self.play(FadeIn(brace_PA), Write(label_PA), run_time=0.6)
        
        # 标注切线长PB
        brace_PB = Brace(Line(self.P_external, self.B), direction=RIGHT, buff=0.1, color=YELLOW)
        label_PB = brace_PB.get_text("PB", buff=0.1).set_color(YELLOW).scale(0.8)
        
        self.play(FadeIn(brace_PB), Write(label_PB), run_time=0.6)
        
        self.wait(1.0)
        
        # 保存对象
        self.title_length = title
        self.definition_length = definition
        self.circle_length = circle
        self.o_dot_length = o_dot
        self.o_label_length = o_label
        self.p_ext_dot = p_ext_dot
        self.p_ext_label = p_ext_label
        self.tangent_PA = tangent_PA
        self.tangent_PB = tangent_PB
        self.a_dot = a_dot
        self.a_label = a_label
        self.b_dot = b_dot
        self.b_label = b_label
        self.brace_PA = brace_PA
        self.label_PA = label_PA
        self.brace_PB = brace_PB
        self.label_PB = label_PB
    
    def scene_7_tangent_length_proof(self):
        """场景7: 切线长定理 - 证明"""
        # 连接半径OA, OB
        radius_OA = Line(self.O, self.A, color=self.COLOR_RADIUS, stroke_width=2, stroke_opacity=0.6)
        radius_OB = Line(self.O, self.B, color=self.COLOR_RADIUS, stroke_width=2, stroke_opacity=0.6)
        
        self.play(Create(radius_OA), Create(radius_OB), run_time=0.8)
        
        # 连接OP
        line_OP = DashedLine(self.O, self.P_external, color=GRAY_B, dash_length=0.1)
        
        self.play(Create(line_OP), run_time=0.6)
        
        # 添加直角标记
        # ∠OAP
        right_angle_A = RightAngle(
            Line(self.O, self.A),
            Line(self.A, self.P_external),
            length=0.25,
            quadrant=(-1, -1),
            other_angle=False,
            color=YELLOW,
            stroke_width=2
        )
        
        # ∠OBP
        right_angle_B = RightAngle(
            Line(self.O, self.B),
            Line(self.B, self.P_external),
            length=0.25,
            quadrant=(1, -1),
            other_angle=False,
            color=YELLOW,
            stroke_width=2
        )
        
        self.play(Create(right_angle_A), Create(right_angle_B), run_time=0.6)
        
        # 说明文字1
        explain_1_text = Text(
            "切线性质:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        explain_1_formula = MathTex(
            r"PA \perp OA,\ PB \perp OB",
            font_size=22
        )
        explain_1 = VGroup(explain_1_text, explain_1_formula).arrange(RIGHT, buff=0.2)
        explain_1.move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(explain_1), run_time=0.3)
        
        # 高亮三角形OAP
        triangle_OAP = Polygon(
            self.O, self.A, self.P_external,
            color=YELLOW,
            fill_opacity=0.15,
            stroke_width=3
        )
        
        self.play(FadeIn(triangle_OAP), run_time=0.4)
        self.wait(0.3)
        
        # 高亮三角形OBP
        triangle_OBP = Polygon(
            self.O, self.B, self.P_external,
            color=YELLOW,
            fill_opacity=0.15,
            stroke_width=3
        )
        
        self.play(Transform(triangle_OAP, triangle_OBP), run_time=0.5)
        
        # 全等标记
        congruent_text = Text(
            "全等:",
            font="Noto Sans CJK SC",
            font_size=20,
            color=WHITE
        )
        congruent_formula = MathTex(
            r"\triangle OAP \cong \triangle OBP",
            font_size=22
        )
        congruent = VGroup(congruent_text, congruent_formula).arrange(RIGHT, buff=0.2)
        congruent.move_to(DOWN * 4.5)
        
        self.play(Write(congruent), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(congruent), FadeOut(triangle_OAP), run_time=0.3)
        
        # 最终结论公式
        conclusion_text = Text(
            "切线长定理:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        conclusion_formula = MathTex(
            r"PA = PB",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        )
        conclusion = VGroup(conclusion_text, conclusion_formula).arrange(RIGHT, buff=0.3)
        conclusion.move_to(DOWN * 5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.8)
        self.play(Flash(conclusion_formula, color=YELLOW, flash_radius=1.0), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(self.title_length),
            FadeOut(self.definition_length),
            FadeOut(self.circle_length),
            FadeOut(self.o_dot_length),
            FadeOut(self.o_label_length),
            FadeOut(self.p_ext_dot),
            FadeOut(self.p_ext_label),
            FadeOut(self.tangent_PA),
            FadeOut(self.tangent_PB),
            FadeOut(self.a_dot),
            FadeOut(self.a_label),
            FadeOut(self.b_dot),
            FadeOut(self.b_label),
            FadeOut(self.brace_PA),
            FadeOut(self.label_PA),
            FadeOut(self.brace_PB),
            FadeOut(self.label_PB),
            FadeOut(radius_OA),
            FadeOut(radius_OB),
            FadeOut(line_OP),
            FadeOut(right_angle_A),
            FadeOut(right_angle_B),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_8_summary_outro(self):
        """场景8: 总结与片尾"""
        # 三个知识卡片
        card1_title = Text("切线性质", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_TANGENT)
        card1_content = Text(
            "切线垂直于过切点的半径",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        card1 = VGroup(card1_title, card1_content).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card1.move_to(UP * 2.5 + LEFT * 10)
        
        card2_title = Text("切线判定", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_HIGHLIGHT)
        card2_content = Text(
            "过半径外端且垂直于半径",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        card2 = VGroup(card2_title, card2_content).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card2.move_to(UP * 1 + LEFT * 10)
        
        card3_title = Text("切线长定理", font="Noto Sans CJK SC", font_size=22, color="#9b59b6")
        card3_content = Text(
            "从圆外一点的切线长相等",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        card3 = VGroup(card3_title, card3_content).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card3.move_to(DOWN * 0.5 + LEFT * 10)
        
        # 卡片依次滑入
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 4)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我, 学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小装饰
        circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_CIRCLE, fill_opacity=0.6)
            .move_to(follow.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(*[FadeIn(c, scale=0.5) for c in circles], run_time=0.5)
        self.play(Rotate(circles, angle=PI, run_time=1.2))
        
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(VGroup(*self.mobjects)),
            run_time=1.0
        )


# 运行命令:
# manim -pql tangent_properties.py TangentProperties  # 快速预览
# manim -qh tangent_properties.py TangentProperties   # 高质量渲染