"""
正弦定理 - 三角形边角关系教学动画
使用 Manim 创建的中学数学教学视频

内容: 正弦定理 a/sin A = b/sin B = c/sin C = 2R 的证明和应用
目标观众: 高中学生
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


class 正弦定理Animation(Scene):
    """
    正弦定理教学动画场景

    场景顺序:
    1. 开场介绍
    2. 三角形和外接圆
    3. 正弦定理推导
    4. 应用举例
    5. 总结回顾
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_CIRCLE = YELLOW
        self.COLOR_HIGHLIGHT = "#f1c40f"
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_ANGLE = RED

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_triangle_and_circumcircle()
        self.show_sine_law_derivation()
        self.show_examples()
        self.show_summary()
        self.show_outro()

    def setup_geometry(self):
        """初始化三角形和相关几何元素"""
        # 定义三角形顶点 (使用锐角三角形便于展示)
        self.A = np.array([-2, -1, 0])
        self.B = np.array([2, -1, 0])
        self.C = np.array([0, 1.5, 0])

        # 应用缩放和偏移
        self.SCALE = 0.8
        self.OFFSET = UP * 1.5
        self.A = self.A * self.SCALE + self.OFFSET
        self.B = self.B * self.SCALE + self.OFFSET
        self.C = self.C * self.SCALE + self.OFFSET

        # 计算边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB

        # 计算角度
        self.angle_A = self.calculate_angle_at_vertex(self.A, self.B, self.C)
        self.angle_B = self.calculate_angle_at_vertex(self.B, self.A, self.C)
        self.angle_C = self.calculate_angle_at_vertex(self.C, self.A, self.B)

        # 计算外心和外接圆半径
        self.circumcenter = self.calculate_circumcenter()
        self.circumradius = np.linalg.norm(self.A - self.circumcenter)

        # 创建三角形对象
        self.triangle = Polygon(self.A, self.B, self.C, color=self.COLOR_TRIANGLE, stroke_width=3)

        # 验证几何计算
        self.verify_geometry()

    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6

        # 验证外心到三顶点距离相等
        dist_A = np.linalg.norm(self.circumcenter - self.A)
        dist_B = np.linalg.norm(self.circumcenter - self.B)
        dist_C = np.linalg.norm(self.circumcenter - self.C)

        if not (abs(dist_A - dist_B) < epsilon and abs(dist_B - dist_C) < epsilon):
            print(f"WARNING: 外心计算可能有误! 距离: {dist_A:.6f}, {dist_B:.6f}, {dist_C:.6f}")

        # 验证角度和为180度
        total_angle = np.degrees(self.angle_A + self.angle_B + self.angle_C)
        if abs(total_angle - 180) > epsilon:
            print(f"WARNING: 角度和不等于180°! 实际: {total_angle:.6f}")

        print("✓ 几何验证完成")

    def calculate_angle_at_vertex(self, vertex, point1, point2):
        """计算顶点处的角度（弧度）"""
        vec1 = point1 - vertex
        vec2 = point2 - vertex
        cos_angle = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 数值稳定性
        return np.arccos(cos_angle)

    def calculate_circumcenter(self):
        """计算外心 - 使用解析公式精确计算"""
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]

        # 计算D值 (行列式)
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

        if abs(D) < 1e-10:
            # 三点共线，退化情况
            return (self.A + self.B + self.C) / 3

        # 计算外心坐标
        ux = ((ax**2 + ay**2) * (by - cy) +
              (bx**2 + by**2) * (cy - ay) +
              (cx**2 + cy**2) * (ay - by)) / D

        uy = ((ax**2 + ay**2) * (cx - bx) +
              (bx**2 + by**2) * (ax - cx) +
              (cx**2 + cy**2) * (bx - ax)) / D

        return np.array([ux, uy, 0])

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)

        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "正弦定理",
            font="Noto Sans CJK SC",
            font_size=64,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "三角形边角关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GRAY_A
        ).move_to(UP * 5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 三角形边角关系的视觉示意
        sine_law_formula = MathTex(
            r"{a \over \sin A} = {b \over \sin B} = {c \over \sin C} = 2R",
            font_size=36
        ).move_to(UP * 3.5)

        self.play(Write(sine_law_formula), run_time=1.0)

        # 等待
        self.wait(1.5)

        # 清理部分元素
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sine_law_formula),
            run_time=0.5
        )

    def show_triangle_and_circumcircle(self):
        """场景2: 三角形和外接圆"""
        # 显示三角形
        self.play(Create(self.triangle), run_time=1.0)

        # 添加顶点标签
        label_a = Text("A", font="Noto Sans CJK SC", font_size=28, color=WHITE).next_to(self.A, DOWN, buff=0.15)
        label_b = Text("B", font="Noto Sans CJK SC", font_size=28, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        label_c = Text("C", font="Noto Sans CJK SC", font_size=28, color=WHITE).next_to(self.C, UP, buff=0.15)

        self.play(
            FadeIn(label_a),
            FadeIn(label_b),
            FadeIn(label_c),
            run_time=0.5
        )

        # 显示外接圆
        circumcircle = Circle(
            radius=self.circumradius,
            color=self.COLOR_CIRCLE,
            stroke_width=2
        ).move_to(self.circumcenter)

        circumcenter_dot = Dot(self.circumcenter, color=self.COLOR_CIRCLE, radius=0.08)
        circumcenter_label = Text("O", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CIRCLE).next_to(circumcenter_dot, DOWN, buff=0.15)

        self.play(
            Create(circumcircle),
            FadeIn(circumcenter_dot),
            FadeIn(circumcenter_label),
            run_time=1.5
        )

        # 从外心到顶点的连线
        radii_lines = VGroup(
            DashedLine(self.circumcenter, self.A, color=self.COLOR_AUXILIARY, dash_length=0.1),
            DashedLine(self.circumcenter, self.B, color=self.COLOR_AUXILIARY, dash_length=0.1),
            DashedLine(self.circumcenter, self.C, color=self.COLOR_AUXILIARY, dash_length=0.1)
        )

        self.play(Create(radii_lines), run_time=0.8)

        # 外接圆半径文字说明
        r_label = Text("R", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_CIRCLE).move_to(
            self.circumcenter + (self.A - self.circumcenter) / 2
        )
        self.play(Write(r_label), run_time=0.5)

        # 等待
        self.wait(2.0)

        # 清理部分元素
        self.play(
            FadeOut(radii_lines),
            FadeOut(r_label),
            run_time=0.5
        )

    def show_sine_law_derivation(self):
        """场景3: 正弦定理推导"""
        # 标题
        derivation_title = Text(
            "正弦定理推导",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)

        self.play(Write(derivation_title), run_time=0.5)

        # 选择直径的一端和另一顶点构成直角三角形来推导
        # 将顶点C连接到外心，并继续延长到圆上形成直径
        diameter_end = self.circumcenter + (self.circumcenter - self.A)  # A对面的点
        extended_triangle = Polygon(self.B, self.C, diameter_end, color=PURPLE, stroke_width=2)

        # 高亮三角形ABC中边a的对角A
        angle_a_arc = Angle.from_three_points(self.B, self.A, self.C, radius=0.3, color=self.COLOR_ANGLE)
        angle_a_label = Text("A", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ANGLE).next_to(angle_a_arc, LEFT, buff=0.2)

        # 标注边长
        a_label = MathTex("a", color=self.COLOR_TRIANGLE).move_to(
            (self.B + self.C) / 2 + np.array([0, 0.3, 0])
        )

        self.play(
            Create(angle_a_arc),
            Write(angle_a_label),
            Write(a_label),
            run_time=0.8
        )

        # 绘制直径及其对应的圆周角
        diameter_line = Line(self.A, diameter_end, color=BLUE, stroke_width=3)
        diameter_dot = Dot(diameter_end, color=BLUE, radius=0.08)
        diameter_label = Text("A'", font="Noto Sans CJK SC", font_size=24, color=BLUE).next_to(diameter_dot, DOWN, buff=0.15)

        self.play(
            Create(diameter_line),
            FadeIn(diameter_dot),
            FadeIn(diameter_label),
            run_time=1.0
        )

        # 构造三角形BCA'，其中角BCA'是直角（圆周角对直径）
        right_angle = self.create_right_angle_mark(self.C, self.B, diameter_end, size=0.15)

        self.play(Create(right_angle), run_time=0.5)

        # 说明角A = 角A'（同弧所对的圆周角相等）
        angle_ap_arc = Angle.from_three_points(self.B, diameter_end, self.C, radius=0.25, color=self.COLOR_ANGLE)
        angle_ap_label = Text("A'", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ANGLE).next_to(angle_ap_arc, LEFT, buff=0.2)

        self.play(
            Create(angle_ap_arc),
            Write(angle_ap_label),
            run_time=0.5
        )

        # 推导过程
        step1 = MathTex(
            r"\because \angle A = \angle A' \text{ (同弧所对圆周角)}",
            font_size=24
        ).move_to(DOWN * 1)

        step2 = MathTex(
            r"\text{且 } \angle BCA' = 90^\circ \text{ (直径所对圆周角)}",
            font_size=24
        ).move_to(DOWN * 2)

        step3 = MathTex(
            r"\therefore \sin A' = \sin A = {a \over 2R}",
            font_size=24
        ).move_to(DOWN * 3)

        step4 = MathTex(
            r"\Rightarrow {a \over \sin A} = 2R",
            font_size=28
        ).move_to(DOWN * 4.5)

        self.play(Write(step1), run_time=0.8)
        self.play(Write(step2), run_time=0.8)
        self.play(Write(step3), run_time=0.8)
        self.play(Write(step4), run_time=1.0)

        # 总结公式
        sine_law_full = MathTex(
            r"{a \over \sin A} = {b \over \sin B} = {c \over \sin C} = 2R",
            font_size=32
        ).move_to(DOWN * 6.5)

        self.play(Write(sine_law_full), run_time=1.0)

        # 等待
        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(derivation_title),
            FadeOut(angle_a_arc),
            FadeOut(angle_a_label),
            FadeOut(a_label),
            FadeOut(diameter_line),
            FadeOut(diameter_dot),
            FadeOut(diameter_label),
            FadeOut(right_angle),
            FadeOut(angle_ap_arc),
            FadeOut(angle_ap_label),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(sine_law_full),
            run_time=0.6
        )

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

    def show_examples(self):
        """场景4: 正弦定理应用举例"""
        # 标题
        example_title = Text(
            "正弦定理应用",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)

        self.play(Write(example_title), run_time=0.5)

        # 示例1：已知两角及一边，求其他边
        example_1_title = Text(
            "例1: 已知两角及一边",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.2)

        self.play(Write(example_1_title), run_time=0.6)

        # 重新绘制一个清晰的三角形用于示例
        example_triangle = Polygon(self.A, self.B, self.C, color=GREEN, stroke_width=3)
        example_label_a = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.A, DOWN, buff=0.15)
        example_label_b = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        example_label_c = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.C, UP, buff=0.15)

        self.play(
            Create(example_triangle),
            FadeIn(example_label_a),
            FadeIn(example_label_b),
            FadeIn(example_label_c),
            run_time=0.8
        )

        # 标注已知条件
        known_condition = Text(
            "已知: ∠A=30°, ∠B=60°, a=3",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GREEN
        ).move_to(UP * 3.5)

        self.play(Write(known_condition), run_time=0.6)

        # 求解过程
        solution_step1 = MathTex(
            r"\angle C = 180^\circ - 30^\circ - 60^\circ = 90^\circ",
            font_size=24
        ).move_to(UP * 2.5)

        solution_step2 = MathTex(
            r"{a \over \sin A} = {b \over \sin B}",
            font_size=24
        ).move_to(UP * 1.5)

        solution_step3 = MathTex(
            r"{3 \over \sin 30^\circ} = {b \over \sin 60^\circ}",
            font_size=24
        ).move_to(UP * 0.5)

        solution_step4 = MathTex(
            r"b = {3 \cdot \sin 60^\circ \over \sin 30^\circ} = {3 \cdot {\sqrt{3} \over 2} \over {1 \over 2}} = 3\sqrt{3}",
            font_size=24
        ).move_to(DOWN * 0.5)

        self.play(Write(solution_step1), run_time=0.8)
        self.play(Write(solution_step2), run_time=0.8)
        self.play(Write(solution_step3), run_time=0.8)
        self.play(Write(solution_step4), run_time=1.0)

        # 等待
        self.wait(2.0)

        # 清理示例1
        self.play(
            FadeOut(example_1_title),
            FadeOut(example_triangle),
            FadeOut(example_label_a),
            FadeOut(example_label_b),
            FadeOut(example_label_c),
            FadeOut(known_condition),
            FadeOut(solution_step1),
            FadeOut(solution_step2),
            FadeOut(solution_step3),
            FadeOut(solution_step4),
            run_time=0.5
        )

        # 示例2：已知两边及其中一边的对角
        example_2_title = Text(
            "例2: 已知两边及一角",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.2)

        self.play(Write(example_2_title), run_time=0.6)

        # 重新绘制示例三角形
        example_triangle_2 = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        example_label_a2 = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.A, DOWN, buff=0.15)
        example_label_b2 = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        example_label_c2 = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.C, UP, buff=0.15)

        self.play(
            Create(example_triangle_2),
            FadeIn(example_label_a2),
            FadeIn(example_label_b2),
            FadeIn(example_label_c2),
            run_time=0.8
        )

        # 标注已知条件
        known_condition_2 = Text(
            "已知: a=4, b=3, ∠A=60°",
            font="Noto Sans CJK SC",
            font_size=22,
            color=BLUE
        ).move_to(UP * 3.5)

        self.play(Write(known_condition_2), run_time=0.6)

        # 求解过程
        solution_step1_2 = MathTex(
            r"{a \over \sin A} = {b \over \sin B}",
            font_size=24
        ).move_to(UP * 2.5)

        solution_step2_2 = MathTex(
            r"{4 \over \sin 60^\circ} = {3 \over \sin B}",
            font_size=24
        ).move_to(UP * 1.5)

        solution_step3_2 = MathTex(
            r"\sin B = {3 \cdot \sin 60^\circ \over 4} = {3 \cdot {\sqrt{3} \over 2} \over 4} = {3\sqrt{3} \over 8}",
            font_size=24
        ).move_to(UP * 0.5)

        solution_step4_2 = Text(
            "B = arcsin(3√3/8) ≈ 46.8° 或 133.2°",
            font="Noto Sans CJK SC",
            font_size=22
        ).move_to(DOWN * 0.5)

        self.play(Write(solution_step1_2), run_time=0.8)
        self.play(Write(solution_step2_2), run_time=0.8)
        self.play(Write(solution_step3_2), run_time=0.8)
        self.play(Write(solution_step4_2), run_time=1.0)

        # 等待
        self.wait(2.0)

        # 清理示例2
        self.play(
            FadeOut(example_2_title),
            FadeOut(example_triangle_2),
            FadeOut(example_label_a2),
            FadeOut(example_label_b2),
            FadeOut(example_label_c2),
            FadeOut(known_condition_2),
            FadeOut(solution_step1_2),
            FadeOut(solution_step2_2),
            FadeOut(solution_step3_2),
            FadeOut(solution_step4_2),
            run_time=0.5
        )

    def show_summary(self):
        """场景5: 总结回顾"""
        # 标题
        summary_title = Text(
            "正弦定理总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)

        self.play(Write(summary_title), run_time=0.5)

        # 正弦定理主要形式
        sine_law_main = MathTex(
            r"{a \over \sin A} = {b \over \sin B} = {c \over \sin C} = 2R",
            font_size=36
        ).move_to(UP * 5)

        self.play(Write(sine_law_main), run_time=1.0)

        # 变形公式
        variants_title = Text(
            "变形公式:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)

        variant1 = MathTex(
            r"a = 2R \sin A,\quad b = 2R \sin B,\quad c = 2R \sin C",
            font_size=24
        ).move_to(UP * 2.5)

        variant2 = MathTex(
            r"\sin A = {a \over 2R},\quad \sin B = {b \over 2R},\quad \sin C = {c \over 2R}",
            font_size=24
        ).move_to(UP * 1.5)

        variant3 = MathTex(
            r"\sin A : \sin B : \sin C = a : b : c",
            font_size=24
        ).move_to(UP * 0.5)

        self.play(Write(variants_title), run_time=0.5)
        self.play(Write(variant1), run_time=0.8)
        self.play(Write(variant2), run_time=0.8)
        self.play(Write(variant3), run_time=0.8)

        # 应用场景
        applications_title = Text(
            "应用场景:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 0.5)

        application1 = Text(
            "• 已知两角及一边，求其他边",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)

        application2 = Text(
            "• 已知两边及其中一边的对角，求其他角",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5)

        application3 = Text(
            "• 求三角形外接圆半径",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(Write(applications_title), run_time=0.5)
        self.play(Write(application1), run_time=0.5)
        self.play(Write(application2), run_time=0.5)
        self.play(Write(application3), run_time=0.5)

        # 等待
        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(sine_law_main),
            FadeOut(variants_title),
            FadeOut(variant1),
            FadeOut(variant2),
            FadeOut(variant3),
            FadeOut(applications_title),
            FadeOut(application1),
            FadeOut(application2),
            FadeOut(application3),
            run_time=0.6
        )

    def show_outro(self):
        """场景6: 片尾关注"""
        # 三角形作为装饰元素
        final_triangle = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=2).scale(0.7)

        # 作者信息
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.5)

        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        # 正弦定理公式作为装饰
        formula_decoration = MathTex(
            r"{a \over \sin A} = {b \over \sin B} = {c \over \sin C}",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 2)

        # 动画序列
        self.play(
            Create(final_triangle),
            run_time=1.0
        )
        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.play(Write(formula_decoration), run_time=0.8)

        # 让三角形旋转
        self.play(Rotate(final_triangle, angle=PI, run_time=2))

        # 等待
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(final_triangle),
            FadeOut(author_name),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(formula_decoration),
            run_time=1.0
        )


# 运行命令:
# manim -pql 006_正弦定理.py 正弦定理Animation  # 快速预览
# manim -qh 006_正弦定理.py 正弦定理Animation   # 高质量