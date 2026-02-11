from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CosineTheoremAnimation(Scene):
    """
    余弦定理教学动画场景

    场景顺序:
    1. 开场介绍
    2. 三角形构造与标记
    3. 余弦定理公式推导
    4. 应用举例
    5. 特殊情况(勾股定理)
    6. 总结回顾
    7. 片尾关注
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_SIDES = YELLOW
        self.COLOR_ANGLE = RED
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA = BLUE
        self.COLOR_HIGHLIGHT = GOLD

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.show_opening()
        self.show_triangle_setup()
        self.show_cosine_theorem_formulas()
        self.show_application_example()
        self.show_special_case_pythagorean()
        self.show_summary()
        self.show_outro()

    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点 (创建一个合适的三角形来演示余弦定理)
        # 我们选择一个钝角三角形，这样可以清楚地看到余弦定理的作用
        self.A = np.array([-2.0, -1.0, 0])
        self.B = np.array([2.0, -1.0, 0])
        self.C = np.array([0.5, 2.0, 0])

        # 缩放和偏移以适应屏幕
        self.SCALE = 0.9
        self.OFFSET = UP * 1.0

        # 应用变换
        self.A = self.A * self.SCALE + self.OFFSET
        self.B = self.B * self.SCALE + self.OFFSET
        self.C = self.C * self.SCALE + self.OFFSET

        # 计算边长
        self.a = np.linalg.norm(self.B - self.C)  # BC 边，对应角A
        self.b = np.linalg.norm(self.C - self.A)  # CA 边，对应角B
        self.c = np.linalg.norm(self.A - self.B)  # AB 边，对应角C

        # 计算角度
        self.angle_A = self.calculate_angle_at_vertex(self.B, self.A, self.C)  # ∠BAC
        self.angle_B = self.calculate_angle_at_vertex(self.A, self.B, self.C)  # ∠ABC
        self.angle_C = self.calculate_angle_at_vertex(self.A, self.C, self.B)  # ∠ACB

        # 创建三角形对象 (但不添加到场景)
        self.triangle = Polygon(self.A, self.B, self.C, color=self.COLOR_TRIANGLE, stroke_width=3)

        # 验证几何计算
        self.verify_geometry()

        print("✓ 几何初始化完成")

    def calculate_angle_at_vertex(self, point1, vertex, point2):
        """计算顶点处的角度 (弧度)"""
        v1 = point1 - vertex
        v2 = point2 - vertex

        # 使用向量计算夹角
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)  # 防止浮点误差导致超出范围
        return np.arccos(cos_angle)

    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-5

        # 验证角度和为π (180度)
        total_angle = self.angle_A + self.angle_B + self.angle_C
        if abs(total_angle - np.pi) > epsilon:
            print(f"⚠️  角度和不等于π: {total_angle:.6f}")
        else:
            print("✓ 角度和验证通过")

        # 验证余弦定理
        # a² = b² + c² - 2bc cos(A)
        lhs_a = self.a ** 2
        rhs_a = self.b ** 2 + self.c ** 2 - 2 * self.b * self.c * np.cos(self.angle_A)
        if abs(lhs_a - rhs_a) > epsilon:
            print(f"⚠️  余弦定理 a²=b²+c²-2bc*cos(A) 验证失败: {lhs_a:.6f} vs {rhs_a:.6f}")
        else:
            print("✓ 余弦定理 a²=b²+c²-2bc*cos(A) 验证通过")

        # b² = a² + c² - 2ac cos(B)
        lhs_b = self.b ** 2
        rhs_b = self.a ** 2 + self.c ** 2 - 2 * self.a * self.c * np.cos(self.angle_B)
        if abs(lhs_b - rhs_b) > epsilon:
            print(f"⚠️  余弦定理 b²=a²+c²-2ac*cos(B) 验证失败: {lhs_b:.6f} vs {rhs_b:.6f}")
        else:
            print("✓ 余弦定理 b²=a²+c²-2ac*cos(B) 验证通过")

        # c² = a² + b² - 2ab cos(C)
        lhs_c = self.c ** 2
        rhs_c = self.a ** 2 + self.b ** 2 - 2 * self.a * self.b * np.cos(self.angle_C)
        if abs(lhs_c - rhs_c) > epsilon:
            print(f"⚠️  余弦定理 c²=a²+b²-2ab*cos(C) 验证失败: {lhs_c:.6f} vs {rhs_c:.6f}")
        else:
            print("✓ 余弦定理 c²=a²+b²-2ab*cos(C) 验证通过")

    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.5)

        # 标题
        title = Text(
            "余弦定理",
            font="Noto Sans CJK SC",
            font_size=60,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "三角形边角关系的重要定理",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5)

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 钩子问题
        hook_question = Text(
            "如何在已知两边及夹角时求第三边？",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)

        self.play(FadeIn(hook_question, shift=DOWN * 0.3), run_time=0.8)
        self.wait(1.5)

        # 清理开场元素，保留作者信息
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook_question),
            run_time=0.8
        )

    def show_triangle_setup(self):
        """场景2: 三角形构造与标记"""
        # 显示三角形
        self.play(Create(self.triangle), run_time=1.2)

        # 标记顶点
        self.label_A = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.A, DOWN, buff=0.15)
        self.label_B = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        self.label_C = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.C, UP, buff=0.15)

        self.play(
            Write(self.label_A),
            Write(self.label_B),
            Write(self.label_C),
            run_time=0.8
        )

        # 标记边长
        mid_AB = (self.A + self.B) / 2
        mid_BC = (self.B + self.C) / 2
        mid_CA = (self.C + self.A) / 2

        self.label_c = Text("c", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SIDES).move_to(mid_AB).shift(UP * 0.3)
        self.label_a = Text("a", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SIDES).move_to(mid_BC).shift(RIGHT * 0.3)
        self.label_b = Text("b", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_SIDES).move_to(mid_CA).shift(LEFT * 0.3)

        sides_group = VGroup(self.label_a, self.label_b, self.label_c)

        self.play(
            Write(self.label_c),
            Write(self.label_a),
            Write(self.label_b),
            run_time=0.8
        )

        # 高亮边
        side_a = Line(self.B, self.C, color=self.COLOR_SIDES, stroke_width=4)
        side_b = Line(self.C, self.A, color=self.COLOR_SIDES, stroke_width=4)
        side_c = Line(self.A, self.B, color=self.COLOR_SIDES, stroke_width=4)

        self.play(
            Create(side_a),
            Create(side_b),
            Create(side_c),
            run_time=1.0
        )

        # 标记角
        angle_A_arc = Angle(Line(self.A, self.B), Line(self.A, self.C), radius=0.5, color=self.COLOR_ANGLE, other_angle=False)
        angle_B_arc = Angle(Line(self.B, self.C), Line(self.B, self.A), radius=0.5, color=self.COLOR_ANGLE, other_angle=False)
        angle_C_arc = Angle(Line(self.C, self.A), Line(self.C, self.B), radius=0.5, color=self.COLOR_ANGLE, other_angle=False)

        label_angle_A = Text("A", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ANGLE).next_to(angle_A_arc, UR, buff=0.1)
        label_angle_B = Text("B", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ANGLE).next_to(angle_B_arc, LEFT, buff=0.1)
        label_angle_C = Text("C", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_ANGLE).next_to(angle_C_arc, DOWN, buff=0.1)

        angles_group = VGroup(angle_A_arc, angle_B_arc, angle_C_arc, label_angle_A, label_angle_B, label_angle_C)

        self.play(
            Create(angle_A_arc),
            Create(angle_B_arc),
            Create(angle_C_arc),
            Write(label_angle_A),
            Write(label_angle_B),
            Write(label_angle_C),
            run_time=1.0
        )

        self.wait(1.5)

        # 淡出辅助线，保留主要元素
        self.play(
            FadeOut(side_a),
            FadeOut(side_b),
            FadeOut(side_c),
            run_time=0.5
        )

        # 保存三角形和关键标签以供后续使用
        self.saved_elements = VGroup(self.triangle, self.label_A, self.label_B, self.label_C,
                                   self.label_a, self.label_b, self.label_c)

    def show_cosine_theorem_formulas(self):
        """场景3: 余弦定理公式展示"""
        # 保存三角形以便稍后恢复
        if hasattr(self, 'saved_elements'):
            self.play(FadeOut(self.saved_elements), run_time=0.5)

        # 余弦定理的主要公式
        formula_title = Text(
            "余弦定理",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)

        # 主公式
        main_formula = MathTex(
            "a^2 = b^2 + c^2 - 2bc\\cos A",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4)

        # 其他形式
        other_formulas = VGroup(
            MathTex("b^2 = a^2 + c^2 - 2ac\\cos B", font_size=32),
            MathTex("c^2 = a^2 + b^2 - 2ab\\cos C", font_size=32)
        ).arrange(DOWN, buff=0.6).move_to(UP * 1.5)

        # 推论形式
        conclusion = MathTex(
            "\\cos A = \\frac{b^2 + c^2 - a^2}{2bc}",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)

        formulas_group = VGroup(main_formula, other_formulas, conclusion)

        self.play(Write(formula_title), run_time=0.6)
        self.play(Write(main_formula), run_time=1.0)
        self.play(Write(other_formulas), run_time=1.0)
        self.play(Write(conclusion), run_time=1.0)

        # 用箭头连接公式和三角形（暂时不显示三角形）
        # 创建一个较小的三角形进行说明
        small_triangle = Polygon(
            np.array([-1, -0.5, 0]),
            np.array([1, -0.5, 0]),
            np.array([0.2, 0.8, 0]),
            color=WHITE,
            stroke_width=2
        ).scale(0.5).move_to(DOWN * 3.5)

        self.play(Create(small_triangle), run_time=0.8)

        # 强调应用说明
        application_note = Text(
            "用途: 已知两边及夹角求第三边\n或 已知三边求各角",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)

        self.play(Write(application_note), run_time=0.8)

        self.wait(2.5)

        # 清理公式部分
        self.play(
            FadeOut(formula_title),
            FadeOut(main_formula),
            FadeOut(other_formulas),
            FadeOut(conclusion),
            FadeOut(small_triangle),
            FadeOut(application_note),
            run_time=0.8
        )

    def show_application_example(self):
        """场景4: 应用举例"""
        # 如果有保存的元素，先隐藏
        if hasattr(self, 'saved_elements'):
            self.play(FadeOut(self.saved_elements), run_time=0.5)

        # 示例标题
        example_title = Text(
            "应用示例",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)

        # 示例说明
        example_text = Text(
            "在△ABC中，已知 b=5, c=7, ∠A=60°，求边a",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5)

        self.play(Write(example_title), run_time=0.5)
        self.play(Write(example_text), run_time=0.8)

        # 公式应用
        step1 = MathTex(
            "a^2 = b^2 + c^2 - 2bc\\cos A",
            font_size=32
        ).move_to(UP * 3.5)

        step2 = MathTex(
            "a^2 = 5^2 + 7^2 - 2\\cdot 5 \\cdot 7 \\cdot \\cos(60^\\circ)",
            font_size=32
        ).move_to(UP * 2.5)

        step3 = MathTex(
            "a^2 = 25 + 49 - 70 \\cdot \\frac{1}{2}",
            font_size=32
        ).move_to(UP * 1.5)

        step4 = MathTex(
            "a^2 = 74 - 35 = 39",
            font_size=32
        ).move_to(UP * 0.5)

        step5 = MathTex(
            "a = \\sqrt{39}",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(Write(step1), run_time=0.8)
        self.wait(0.8)
        self.play(Write(step2), run_time=0.8)
        self.wait(0.8)
        self.play(Write(step3), run_time=0.8)
        self.wait(0.8)
        self.play(Write(step4), run_time=0.8)
        self.wait(0.8)
        self.play(Write(step5), run_time=1.0)

        # 显示答案
        answer = Text(
            f"边 a ≈ {np.sqrt(39):.2f}",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)

        self.play(Write(answer), run_time=0.8)

        self.wait(2)

        # 清理示例部分
        self.play(
            FadeOut(example_title),
            FadeOut(example_text),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(step5),
            FadeOut(answer),
            run_time=0.8
        )

    def show_special_case_pythagorean(self):
        """场景5: 特殊情况 - 勾股定理"""
        # 清理之前的内容
        if hasattr(self, 'saved_elements'):
            self.play(FadeOut(self.saved_elements), run_time=0.5)

        # 标题
        special_title = Text(
            "特殊情况 - 勾股定理",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)

        self.play(Write(special_title), run_time=0.6)

        # 当A=90°时的情况
        right_angle_case = Text(
            "当∠A = 90° 时，cos A = cos(90°) = 0",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.5)

        self.play(Write(right_angle_case), run_time=0.8)

        # 推导过程
        derivation1 = MathTex(
            "a^2 = b^2 + c^2 - 2bc\\cos(90^\\circ)",
            font_size=32
        ).move_to(UP * 3.2)

        derivation2 = MathTex(
            "a^2 = b^2 + c^2 - 2bc \\cdot 0",
            font_size=32
        ).move_to(UP * 2.2)

        derivation3 = MathTex(
            "a^2 = b^2 + c^2",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)

        pythagorean_label = Text(
            "这就是勾股定理!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.2)

        self.play(Write(derivation1), run_time=0.8)
        self.wait(0.8)
        self.play(Write(derivation2), run_time=0.8)
        self.wait(0.8)
        self.play(Write(derivation3), run_time=1.0)
        self.wait(0.5)
        self.play(Write(pythagorean_label), run_time=0.8)

        # 强调余弦定理是勾股定理的推广
        generalization = Text(
            "余弦定理是勾股定理的推广!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GOLD
        ).move_to(DOWN * 1.5)

        self.play(Write(generalization), run_time=0.8)

        # 添加一个小的直角三角形作为例子
        right_triangle = Polygon(
            np.array([-1, -1, 0]) * 0.5 + DOWN * 3,
            np.array([1, -1, 0]) * 0.5 + DOWN * 3,
            np.array([1, 0, 0]) * 0.5 + DOWN * 3,
            color=BLUE,
            stroke_width=3
        )

        # 直角标记
        right_angle_mark = RightAngle(
            Line(right_triangle.get_vertices()[0], right_triangle.get_vertices()[1]),
            Line(right_triangle.get_vertices()[0], right_triangle.get_vertices()[2]),
            length=0.2,
            color=RED
        )

        self.play(Create(right_triangle), run_time=0.8)
        self.play(Create(right_angle_mark), run_time=0.5)

        self.wait(2.5)

        # 清理特殊情况部分
        self.play(
            FadeOut(special_title),
            FadeOut(right_angle_case),
            FadeOut(derivation1),
            FadeOut(derivation2),
            FadeOut(derivation3),
            FadeOut(pythagorean_label),
            FadeOut(generalization),
            FadeOut(right_triangle),
            FadeOut(right_angle_mark),
            run_time=0.8
        )

    def show_summary(self):
        """场景6: 总结回顾"""
        # 清理之前的内容
        existing_mobs = [m for m in self.mobjects if not isinstance(m, (Text, MathTex))]
        if existing_mobs:
            self.play(*[FadeOut(mob) for mob in existing_mobs], run_time=0.5)

        # 总结标题
        summary_title = Text(
            "余弦定理总结",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD
        ).move_to(UP * 6.5)

        self.play(Write(summary_title), run_time=0.8)

        # 要点列表
        points = VGroup(
            Text("1. 一般形式: a² = b² + c² - 2bc cos A", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("2. 用途: 已知两边及夹角求第三边", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("   或已知三边求各角", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("3. 是勾股定理的推广", font="Noto Sans CJK SC", font_size=26, color=WHITE),
            Text("4. 可用于判断三角形形状", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 2.5)

        for point in points:
            self.play(Write(point), run_time=0.8)
            self.wait(0.5)

        # 重要公式再次强调
        important_formula = MathTex(
            "a^2 = b^2 + c^2 - 2bc\\cos A",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        self.play(Write(important_formula), run_time=1.0)

        # 记忆提示
        memory_tip = Text(
            "记住: 边的平方 = 另两边平方和 - 2倍乘积×夹角余弦",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)

        self.play(Write(memory_tip), run_time=0.8)

        self.wait(2)

        # 清理总结部分
        self.play(
            FadeOut(summary_title),
            *[FadeOut(point) for point in points],
            FadeOut(important_formula),
            FadeOut(memory_tip),
            run_time=0.8
        )

    def show_outro(self):
        """场景7: 片尾关注"""
        # 清理之前的所有元素
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)

        # 最终展示完整的三角形和余弦定理
        final_formula = MathTex(
            "a^2 = b^2 + c^2 - 2bc\\cos A",
            font_size=40,
            color=GOLD
        ).move_to(UP * 2)

        # 创建新的三角形，而不是使用之前保存的
        triangle_final = Polygon(
            np.array([-2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0]) * 0.7 + DOWN * 1,
            np.array([2.0, -1.0, 0]) * 0.9 + np.array([0, 1, 0]) * 0.7 + DOWN * 1,
            np.array([0.5, 2.0, 0]) * 0.9 + np.array([0, 1, 0]) * 0.7 + DOWN * 1,
            color=WHITE,
            stroke_width=4
        )

        # 获取三角形的顶点
        vertices = triangle_final.get_vertices()

        # 标签
        label_A = Text("A", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(vertices[0], DOWN, buff=0.1)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(vertices[1], DOWN, buff=0.1)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(vertices[2], UP, buff=0.1)

        labels = VGroup(label_A, label_B, label_C)

        self.play(
            Write(final_formula),
            Create(triangle_final),
            Write(labels),
            run_time=1.0
        )

        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(DOWN * 4.5)

        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GOLD
        ).move_to(DOWN * 5.5)

        self.play(
            Write(author_name),
            Write(author_id),
            Write(follow_text),
            run_time=1.0
        )

        # 最后的装饰动画
        stars = VGroup(*[
            Star(color=YELLOW, fill_opacity=0.8).scale(0.2).move_to(
                np.array([
                    np.cos(i * 2*PI/5) * 3,
                    np.sin(i * 2*PI/5) * 3,
                    0
                ]) + DOWN * 1
            )
            for i in range(5)
        ])

        self.play(LaggedStartMap(FadeIn, stars, lag_ratio=0.2), run_time=1.5)
        self.play(Rotate(stars, angle=PI, run_time=2), rate_func=linear)

        self.wait(2)

    def perpendicular_foot(self, point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + projection * line_vec


# 运行命令示例:
# manim -pql 007_余弦定理.py CosineTheoremAnimation  # 快速预览
# manim -qh 007_余弦定理.py CosineTheoremAnimation   # 高质量