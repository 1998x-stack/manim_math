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


class SineLawAnimation(Scene):
    """
    正弦定理教学动画场景

    场景顺序:
    1. 开场介绍
    2. 三角形和外接圆
    3. 正弦定理推导
    4. 应用举例
    5. 总结回顾
    6. 片尾
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

        # 计算边长 (a=BC, b=AC, c=AB)
        self.a = np.linalg.norm(self.B - self.C)  # BC, 对应角A
        self.b = np.linalg.norm(self.C - self.A)  # AC, 对应角B
        self.c = np.linalg.norm(self.A - self.B)  # AB, 对应角C

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
            return (self.A + self.B + self.C) / 3

        ux = ((ax**2 + ay**2) * (by - cy) +
              (bx**2 + by**2) * (cy - ay) +
              (cx**2 + cy**2) * (ay - by)) / D

        uy = ((ax**2 + ay**2) * (cx - bx) +
              (bx**2 + by**2) * (ax - cx) +
              (cx**2 + cy**2) * (bx - ax)) / D

        return np.array([ux, uy, 0])

    def show_opening(self):
        """场景1: 开场介绍"""
        author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.5)

        self.play(FadeIn(author_info, shift=DOWN * 0.2), run_time=0.3)

        title = Text(
            "正弦定理",
            font="PingFang SC",
            font_size=64,
            color=GOLD
        ).move_to(UP * 6)

        subtitle = Text(
            "三角形边角关系",
            font="PingFang SC",
            font_size=36,
            color=GRAY_A
        ).move_to(UP * 5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)

        sine_law_formula = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R",
            font_size=36
        ).move_to(UP * 3.5)

        self.play(Write(sine_law_formula), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sine_law_formula),
            run_time=0.5
        )

    def show_triangle_and_circumcircle(self):
        """场景2: 三角形和外接圆"""
        self.play(Create(self.triangle), run_time=1.0)

        label_a = Text("A", font="PingFang SC", font_size=28, color=WHITE).next_to(self.A, DOWN, buff=0.15)
        label_b = Text("B", font="PingFang SC", font_size=28, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        label_c = Text("C", font="PingFang SC", font_size=28, color=WHITE).next_to(self.C, UP, buff=0.15)

        self.play(FadeIn(label_a), FadeIn(label_b), FadeIn(label_c), run_time=0.5)

        circumcircle = Circle(
            radius=self.circumradius,
            color=self.COLOR_CIRCLE,
            stroke_width=2
        ).move_to(self.circumcenter)

        circumcenter_dot = Dot(self.circumcenter, color=self.COLOR_CIRCLE, radius=0.08)
        circumcenter_label = Text("O", font="PingFang SC", font_size=24, color=self.COLOR_CIRCLE).next_to(circumcenter_dot, DOWN, buff=0.15)

        self.play(
            Create(circumcircle),
            FadeIn(circumcenter_dot),
            FadeIn(circumcenter_label),
            run_time=1.5
        )

        radii_lines = VGroup(
            DashedLine(self.circumcenter, self.A, color=self.COLOR_AUXILIARY, dash_length=0.1),
            DashedLine(self.circumcenter, self.B, color=self.COLOR_AUXILIARY, dash_length=0.1),
            DashedLine(self.circumcenter, self.C, color=self.COLOR_AUXILIARY, dash_length=0.1)
        )
        self.play(Create(radii_lines), run_time=0.8)

        r_label = Text("R", font="PingFang SC", font_size=20, color=self.COLOR_CIRCLE).move_to(
            self.circumcenter + (self.A - self.circumcenter) / 2
        )
        self.play(Write(r_label), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(radii_lines), FadeOut(r_label), run_time=0.5)

        # 存储场景2元素，供下一场景清理使用
        self.scene2_vertex_labels = VGroup(label_a, label_b, label_c)
        self.scene2_circumcircle = circumcircle
        self.scene2_circumcenter_dot = circumcenter_dot
        self.scene2_circumcenter_label = circumcenter_label

    def show_sine_law_derivation(self):
        """场景3: 正弦定理推导

        修正要点:
        1. 角D弧方向修正: Angle.from_three_points(B, D, C) 而非 (C, D, B)
           原代码逆时针扫过308°(劣弧取错)，修正后正确扫过约51°的内角
        2. 移除与顶点标签重叠的角弧文字标签
        3. 完整展示推导步骤: BD=2R → sinD=a/2R → sinA=sinD → a/sinA=2R
        4. 场景结束时清理场景2的所有残留元素
        """
        derivation_title = Text(
            "正弦定理推导",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(derivation_title), run_time=0.5)

        # 1. 高亮角A：from_three_points(B, A, C) → 顶点A，从A→B到A→C逆时针扫过内角 ✓
        angle_a_arc = Angle.from_three_points(
            self.B, self.A, self.C, radius=0.3, color=self.COLOR_ANGLE
        )
        # 边a (BC) 标签 - 放在边的外侧
        a_label = MathTex("a", color=YELLOW, font_size=28).move_to(
            (self.B + self.C) / 2 + np.array([0.28, 0.0, 0])
        )
        self.play(Create(angle_a_arc), Write(a_label), run_time=0.8)
        self.wait(0.5)

        # 2. 构造直径 BD（B的对径点D）
        diameter_end_D = self.circumcenter + (self.circumcenter - self.B)
        diameter_line = Line(self.B, diameter_end_D, color=BLUE, stroke_width=3)
        diameter_dot = Dot(diameter_end_D, color=BLUE, radius=0.08)
        diameter_label = Text(
            "D", font="PingFang SC", font_size=24, color=BLUE
        ).next_to(diameter_dot, UP, buff=0.15)

        self.play(
            Create(diameter_line),
            FadeIn(diameter_dot),
            FadeIn(diameter_label),
            run_time=1.0
        )

        # 3. 连接CD，构成直角三角形BCD
        line_CD = Line(self.C, diameter_end_D, color=PURPLE, stroke_width=2)
        self.play(Create(line_CD), run_time=0.5)

        # 4. 直角标记：∠BCD=90° (直径所对圆周角)
        right_angle = self.create_right_angle_mark(self.C, self.B, diameter_end_D, size=0.15)
        self.play(Create(right_angle), run_time=0.5)

        # 5. 高亮角D：修正后 from_three_points(B, D, C)
        #    顶点D，从D→B到D→C逆时针扫过内角 ≈51° ✓
        #    原代码 from_three_points(C, D, B) 逆时针扫308°（劣弧取错）
        angle_d_arc = Angle.from_three_points(
            self.B, diameter_end_D, self.C, radius=0.25, color=self.COLOR_ANGLE
        )
        self.play(Create(angle_d_arc), run_time=0.5)
        self.wait(0.5)

        # --- 推导步骤（完整展开） ---
        # step1: ∠A = ∠D（同弧BC圆周角）
        step1 = VGroup(
            MathTex(r"\angle A = \angle D", font_size=24),
            Text("（同弧BC圆周角）", font="PingFang SC", font_size=21, color=GRAY_A),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.0)

        # step2: ∠BCD=90°，BD=2R
        step2 = VGroup(
            MathTex(r"\angle BCD = 90^\circ", font_size=24),
            Text("，", font="PingFang SC", font_size=22),
            MathTex(r"BD = 2R", font_size=24),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.0)

        # step3: 在直角△BCD中，sinD = a/2R
        step3 = VGroup(
            Text("在直角", font="PingFang SC", font_size=22),
            MathTex(r"\triangle BCD", font_size=24),
            Text("中：", font="PingFang SC", font_size=22),
            MathTex(r"\sin D = \frac{BC}{BD} = \frac{a}{2R}", font_size=24),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.0)

        # step4: ∴ sinA = sinD = a/2R
        step4 = MathTex(
            r"\therefore\ \sin A = \sin D = \frac{a}{2R}",
            font_size=24
        ).move_to(DOWN * 4.0)

        # step5: ∴ a/sinA = 2R（加大字体突出结论）
        step5 = MathTex(
            r"\therefore\ \frac{a}{\sin A} = 2R",
            font_size=30
        ).move_to(DOWN * 5.0)

        # 同理
        similarly = VGroup(
            Text("同理可得：", font="PingFang SC", font_size=20, color=GRAY_A),
            MathTex(r"\frac{b}{\sin B} = \frac{c}{\sin C} = 2R", font_size=22),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.9)

        self.play(Write(step1), run_time=0.8)
        self.play(Write(step2), run_time=0.8)
        self.play(Write(step3), run_time=1.0)
        self.play(Write(step4), run_time=0.8)
        self.play(Write(step5), run_time=0.8)
        self.play(Write(similarly), run_time=0.8)
        self.wait(3.0)

        # 清理：推导元素 + 场景2残留元素全部 FadeOut
        self.play(
            FadeOut(derivation_title),
            FadeOut(angle_a_arc),
            FadeOut(a_label),
            FadeOut(diameter_line),
            FadeOut(diameter_dot),
            FadeOut(diameter_label),
            FadeOut(line_CD),
            FadeOut(right_angle),
            FadeOut(angle_d_arc),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            FadeOut(step5),
            FadeOut(similarly),
            # 场景2遗留元素
            FadeOut(self.triangle),
            FadeOut(self.scene2_vertex_labels),
            FadeOut(self.scene2_circumcircle),
            FadeOut(self.scene2_circumcenter_dot),
            FadeOut(self.scene2_circumcenter_label),
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
        """场景4: 正弦定理应用举例

        修正要点:
        1. 示例三角形移至屏幕上方区域（y: 3.3~4.7），与文字分离
        2. 推导文字置于中下方（y: 2.3~-1.9），消除与图形的重叠
        3. 主标题 example_title 在场景结束时统一 FadeOut
        """
        # 主标题（贯穿整个示例场景，最后统一清理）
        example_title = Text(
            "正弦定理应用",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(example_title), run_time=0.5)

        # 示例三角形顶点 - 定义在屏幕上方，与推导文字区域分离
        # 上方区域: y ≈ 3.3 ~ 4.7，文字区域: y ≈ 2.3 ~ -1.9
        ex_A = np.array([-1.0, 3.3, 0])
        ex_B = np.array([1.0, 3.3, 0])
        ex_C = np.array([0.0, 4.55, 0])

        # ===== 示例1：已知两角及一边 =====
        example_1_title = Text(
            "例1: 已知两角及一边",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(example_1_title), run_time=0.6)

        example_triangle = Polygon(ex_A, ex_B, ex_C, color=GREEN, stroke_width=3)
        example_label_a = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_A, DOWN, buff=0.12)
        example_label_b = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_B, DOWN, buff=0.12)
        example_label_c = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_C, UP, buff=0.12)

        self.play(
            Create(example_triangle),
            FadeIn(example_label_a),
            FadeIn(example_label_b),
            FadeIn(example_label_c),
            run_time=0.8
        )

        # 已知条件（中间缓冲区）
        known_condition = Text(
            "已知: ∠A=30°, ∠B=60°, a=3",
            font="PingFang SC",
            font_size=22,
            color=GREEN
        ).move_to(UP * 2.3)
        self.play(Write(known_condition), run_time=0.6)

        # 推导过程（下方区域，与三角形无重叠）
        solution_step1 = MathTex(
            r"\angle C = 180^\circ - 30^\circ - 60^\circ = 90^\circ",
            font_size=24
        ).move_to(UP * 1.2)

        solution_step2 = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B}",
            font_size=24
        ).move_to(UP * 0.2)

        solution_step3 = MathTex(
            r"\frac{3}{\sin 30^\circ} = \frac{b}{\sin 60^\circ}",
            font_size=24
        ).move_to(DOWN * 0.8)

        solution_step4 = MathTex(
            r"b = \frac{3 \cdot \frac{\sqrt{3}}{2}}{\frac{1}{2}} = 3\sqrt{3}",
            font_size=24
        ).move_to(DOWN * 1.9)

        self.play(Write(solution_step1), run_time=0.8)
        self.play(Write(solution_step2), run_time=0.8)
        self.play(Write(solution_step3), run_time=0.8)
        self.play(Write(solution_step4), run_time=1.0)
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

        # ===== 示例2：已知两边及一角 =====
        example_2_title = Text(
            "例2: 已知两边及一角",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(example_2_title), run_time=0.6)

        example_triangle_2 = Polygon(ex_A, ex_B, ex_C, color=BLUE, stroke_width=3)
        example_label_a2 = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_A, DOWN, buff=0.12)
        example_label_b2 = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_B, DOWN, buff=0.12)
        example_label_c2 = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(ex_C, UP, buff=0.12)

        self.play(
            Create(example_triangle_2),
            FadeIn(example_label_a2),
            FadeIn(example_label_b2),
            FadeIn(example_label_c2),
            run_time=0.8
        )

        known_condition_2 = Text(
            "已知: a=4, b=3, ∠A=60°",
            font="PingFang SC",
            font_size=22,
            color=BLUE
        ).move_to(UP * 2.3)
        self.play(Write(known_condition_2), run_time=0.6)

        solution_step1_2 = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B}",
            font_size=24
        ).move_to(UP * 1.2)

        solution_step2_2 = MathTex(
            r"\frac{4}{\sin 60^\circ} = \frac{3}{\sin B}",
            font_size=24
        ).move_to(UP * 0.2)

        solution_step3_2 = MathTex(
            r"\sin B = \frac{3\sin 60^\circ}{4} = \frac{3\sqrt{3}}{8} \approx 0.65",
            font_size=24
        ).move_to(DOWN * 0.8)

        # 修正原代码的计算错误: arcsin(3√3/8) ≈ 40.5°（原代码写的46.8°有误）
        # 验证: 3√3/8 = 0.6495, arcsin(0.6495) ≈ 40.5°
        # 又因 A+B < 180°, 若B=139.5°则A+B=199.5°>180°，舍去
        solution_step4_2 = VGroup(
            MathTex(r"B \approx 40.5^\circ", font_size=24),
            Text("（∵", font="PingFang SC", font_size=22, color=GRAY_A),
            MathTex(r"A+139.5^\circ > 180^\circ", font_size=22, color=GRAY_A),
            Text("舍去）", font="PingFang SC", font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 1.9)

        self.play(Write(solution_step1_2), run_time=0.8)
        self.play(Write(solution_step2_2), run_time=0.8)
        self.play(Write(solution_step3_2), run_time=0.8)
        self.play(Write(solution_step4_2), run_time=1.0)
        self.wait(2.0)

        # 清理示例2 + 主标题 example_title（修正：此前缺失对 example_title 的 FadeOut）
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
            FadeOut(example_title),  # 修正：清理整个示例场景的主标题
            run_time=0.5
        )

    def show_summary(self):
        """场景5: 总结回顾"""
        summary_title = Text(
            "正弦定理总结",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(summary_title), run_time=0.5)

        sine_law_main = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R",
            font_size=36
        ).move_to(UP * 5)
        self.play(Write(sine_law_main), run_time=1.0)

        variants_title = Text(
            "变形公式:",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)

        variant1 = MathTex(
            r"a = 2R\sin A,\quad b = 2R\sin B,\quad c = 2R\sin C",
            font_size=24
        ).move_to(UP * 2.5)

        variant2 = MathTex(
            r"\sin A = \frac{a}{2R},\quad \sin B = \frac{b}{2R},\quad \sin C = \frac{c}{2R}",
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

        applications_title = Text(
            "应用场景:",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 0.5)

        application1 = Text(
            "• 已知两角及一边，求其他边",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5)

        application2 = Text(
            "• 已知两边及其中一边的对角，求其他角",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5)

        application3 = Text(
            "• 求三角形外接圆半径",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)

        self.play(Write(applications_title), run_time=0.5)
        self.play(Write(application1), run_time=0.5)
        self.play(Write(application2), run_time=0.5)
        self.play(Write(application3), run_time=0.5)
        self.wait(3.0)

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
        final_triangle = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=2).scale(0.7)

        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.5)

        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        formula_decoration = MathTex(
            r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 2)

        self.play(Create(final_triangle), run_time=1.0)
        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.play(Write(formula_decoration), run_time=0.8)
        self.play(Rotate(final_triangle, angle=PI), run_time=2)
        self.wait(2.0)

        self.play(
            FadeOut(final_triangle),
            FadeOut(author_name),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(formula_decoration),
            run_time=1.0
        )


# 运行命令:
# manim -pql sine_law.py SineLawAnimation  # 快速预览
# manim -qh sine_law.py SineLawAnimation   # 高质量
