"""
解直角三角形 - Solving Right Triangles
使用 Manim 创建的九年级数学教学视频

内容: 根据已知条件求解直角三角形的未知元素
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
    """几何计算工具类 - 确保所有计算精确"""
    
    @staticmethod
    def angle_at_vertex(A, B, C):
        """计算∠ABC的角度(弧度), B是顶点"""
        BA = A - B
        BC = C - B
        cos_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        return np.arccos(np.clip(cos_angle, -1.0, 1.0))


class SolvingRightTriangle(Scene):
    """
    解直角三角形教学动画
    
    场景顺序:
    1. 开场钩子
    2. 基础设置 - 建立直角三角形框架
    3. 情况1 - 已知两边
    4. 情况2 - 已知一边一角
    5. 重要提醒 - 必须至少有一边
    6. 方法总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_KNOWN = "#2ecc71"        # 绿色 - 已知条件
        self.COLOR_UNKNOWN = "#f39c12"      # 橙色 - 未知元素
        self.COLOR_ANGLE = "#9b59b6"        # 紫色 - 角度
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_setup()
        self.scene_3_case_two_sides()
        self.scene_4_case_side_angle()
        self.scene_5_warning()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何数据 - 使用标准3-4-5直角三角形"""
        # 基准参数
        self.SCALE = 1.1
        self.OFFSET = UP * 1.5
        
        # 定义直角三角形 - 使用3-4-5标准三角形
        # 直角在C点, A在左下, B在右上
        self.C = np.array([0, 0, 0]) * self.SCALE + self.OFFSET  # 直角顶点
        self.A = np.array([-4, 0, 0]) * self.SCALE + self.OFFSET  # 左侧
        self.B = np.array([0, 3, 0]) * self.SCALE + self.OFFSET   # 上方
        
        # 精确计算边长
        self.a = np.linalg.norm(self.B - self.C)  # BC (对边, opposite for angle A)
        self.b = np.linalg.norm(self.C - self.A)  # AC (邻边, adjacent for angle A)  
        self.c = np.linalg.norm(self.B - self.A)  # AB (斜边, hypotenuse)
        
        # 计算角度
        self.angle_A_rad = GeometryCalculator.angle_at_vertex(self.C, self.A, self.B)
        self.angle_A_deg = np.degrees(self.angle_A_rad)
        self.angle_B_rad = GeometryCalculator.angle_at_vertex(self.C, self.B, self.A)
        self.angle_B_deg = np.degrees(self.angle_B_rad)
        
        # 计算三角比
        self.sin_A = self.a / self.c
        self.cos_A = self.b / self.c
        self.tan_A = self.a / self.b
        
        # 验证几何关系
        self._verify_geometry()
    
    def _verify_geometry(self):
        """验证所有几何关系的正确性"""
        eps = 1e-6
        errors = []
        
        # 验证直角 (at C)
        vec_CA = self.A - self.C
        vec_CB = self.B - self.C
        dot_product = np.dot(vec_CA[:2], vec_CB[:2])
        if abs(dot_product) > eps:
            errors.append(f"不是直角! 点积={dot_product}")
        
        # 验证勾股定理
        pythagorean = self.a**2 + self.b**2 - self.c**2
        if abs(pythagorean) > eps:
            errors.append(f"勾股定理不成立! a²+b²-c²={pythagorean}")
        
        # 验证角度和
        angle_sum = self.angle_A_rad + self.angle_B_rad - np.pi/2
        if abs(angle_sum) > eps:
            errors.append(f"角度和错误! A+B={np.degrees(self.angle_A_rad + self.angle_B_rad)}°")
        
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败!")
        else:
            print("✓ 几何验证通过")
            print(f"  边长: a={self.a:.3f}, b={self.b:.3f}, c={self.c:.3f}")
            print(f"  角度: ∠A={self.angle_A_deg:.2f}°, ∠B={self.angle_B_deg:.2f}°")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息(顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "只知道两个条件\n能求出整个三角形吗?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 神秘三角形轮廓
        triangle_outline = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=2,
            fill_opacity=0
        )
        
        # 问号
        question_marks = VGroup(
            Text("?", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(self.A + RIGHT * 0.5 + UP * 0.3),
            Text("?", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(self.B + LEFT * 0.5 + DOWN * 0.3),
            Text("?", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(self.C + RIGHT * 0.5 + UP * 0.5)
        )
        
        self.play(
            Flash(triangle_outline, color=YELLOW, flash_radius=1.0),
            FadeIn(triangle_outline),
            run_time=0.8
        )
        
        for qm in question_marks:
            self.play(Flash(qm, color=YELLOW), FadeIn(qm, scale=1.5), run_time=0.3)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_marks),
            run_time=0.5
        )
        
        # 保存三角形轮廓
        self.triangle_outline = triangle_outline
    
    def scene_2_setup(self):
        """场景2: 基础设置"""
        # 三角形实体化
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Transform(self.triangle_outline, self.triangle), run_time=0.6)
        self.remove(self.triangle_outline)
        self.add(self.triangle)
        
        # 直角标记 (at C)
        right_angle_size = 0.25
        vec_CA = (self.A - self.C) / np.linalg.norm(self.A - self.C)
        vec_CB = (self.B - self.C) / np.linalg.norm(self.B - self.C)
        
        self.right_angle_mark = Polygon(
            self.C,
            self.C + vec_CA * right_angle_size,
            self.C + vec_CA * right_angle_size + vec_CB * right_angle_size,
            self.C + vec_CB * right_angle_size,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        )
        
        self.play(Create(self.right_angle_mark), run_time=0.5)
        
        # 顶点标签
        label_A = MathTex("A", font_size=28, color=WHITE).next_to(self.A, DL, buff=0.2)
        label_B = MathTex("B", font_size=28, color=WHITE).next_to(self.B, UR, buff=0.2)
        label_C = MathTex("C", font_size=28, color=WHITE).next_to(self.C, RIGHT, buff=0.2)
        
        self.vertex_labels = VGroup(label_A, label_B, label_C)
        
        self.play(Write(self.vertex_labels), run_time=0.6)
        
        # 边长标签
        side_label_a = MathTex("a", font_size=26, color=self.COLOR_SECONDARY).next_to(
            (self.B + self.C) / 2, RIGHT, buff=0.15
        )
        side_label_b = MathTex("b", font_size=26, color=self.COLOR_SECONDARY).next_to(
            (self.A + self.C) / 2, DOWN, buff=0.15
        )
        side_label_c = MathTex("c", font_size=26, color=self.COLOR_SECONDARY).next_to(
            (self.A + self.B) / 2, UL, buff=0.15
        )
        
        self.side_labels = VGroup(side_label_a, side_label_b, side_label_c)
        
        self.play(Write(self.side_labels), run_time=0.8)
        
        # 角度标记
        angle_A_arc = Arc(
            radius=0.4,
            start_angle=0,
            angle=self.angle_A_rad,
            color=self.COLOR_ANGLE,
            stroke_width=2
        ).move_arc_center_to(self.A)
        
        # 角B的起始角度需要计算
        vec_BC = self.C - self.B
        vec_BA = self.A - self.B
        start_angle_B = np.arctan2(vec_BC[1], vec_BC[0])
        
        angle_B_arc = Arc(
            radius=0.4,
            start_angle=start_angle_B,
            angle=self.angle_B_rad,
            color=self.COLOR_ANGLE,
            stroke_width=2
        ).move_arc_center_to(self.B)
        
        self.angle_arcs = VGroup(angle_A_arc, angle_B_arc)
        
        self.play(Create(self.angle_arcs), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "直角三角形有6个元素:\n3条边 + 3个角",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.0)
        
        self.play(FadeOut(explanation), run_time=0.4)
    
    def scene_3_case_two_sides(self):
        """场景3: 情况1 - 已知两边"""
        # 标题
        title = Text(
            "情况1: 已知两边",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_KNOWN
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 高亮已知边 a 和 c
        known_text = Text(
            "已知: a = 3, c = 5",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_KNOWN
        ).move_to(UP * 5)
        
        self.play(Write(known_text), run_time=0.6)
        
        # 高亮边
        self.play(
            Indicate(self.side_labels[0], color=self.COLOR_KNOWN, scale_factor=1.3),
            Indicate(self.side_labels[2], color=self.COLOR_KNOWN, scale_factor=1.3),
            run_time=0.8
        )
        
        # 步骤1: 用勾股定理求b
        step1_title = Text(
            "① 用勾股定理求边b",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(step1_title), run_time=0.6)
        
        formula1 = MathTex(
            r"b^2 = c^2 - a^2",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(Write(formula1), run_time=0.8)
        
        calculation1 = MathTex(
            r"b = \sqrt{5^2 - 3^2} = \sqrt{16} = 4",
            font_size=32,
            color=self.COLOR_UNKNOWN
        ).move_to(UP * 2.2)
        
        self.play(Write(calculation1), run_time=1.0)
        self.play(Flash(calculation1, color=YELLOW), run_time=0.4)
        
        self.wait(0.8)
        
        # 步骤2: 用三角比求角A
        step2_title = Text(
            "② 用sin求角A",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 0.8)
        
        self.play(Write(step2_title), run_time=0.6)
        
        formula2 = MathTex(
            r"\sin A = \frac{a}{c}",
            font_size=32,
            color=WHITE
        ).move_to(ORIGIN)
        
        self.play(Write(formula2), run_time=0.8)
        
        calculation2 = MathTex(
            r"A = \arcsin\left(\frac{3}{5}\right) \approx 37^\circ",
            font_size=30,
            color=self.COLOR_UNKNOWN
        ).move_to(DOWN * 0.8)
        
        self.play(Write(calculation2), run_time=1.0)
        self.play(Flash(calculation2, color=YELLOW), run_time=0.4)
        
        self.wait(0.8)
        
        # 步骤3: 互余关系求角B
        step3_title = Text(
            "③ 互余关系求角B",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(step3_title), run_time=0.6)
        
        formula3 = MathTex(
            r"B = 90^\circ - 37^\circ = 53^\circ",
            font_size=32,
            color=self.COLOR_UNKNOWN
        ).move_to(DOWN * 2.8)
        
        self.play(Write(formula3), run_time=0.8)
        self.play(Flash(formula3, color=YELLOW), run_time=0.4)
        
        # 完成标记
        checkmark = Text("✓", font_size=60, color=GREEN).move_to(DOWN * 4.5)
        completion_text = Text(
            "所有未知元素都求出了!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).next_to(checkmark, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(checkmark, scale=2),
            FadeIn(completion_text),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(known_text),
            FadeOut(step1_title),
            FadeOut(formula1),
            FadeOut(calculation1),
            FadeOut(step2_title),
            FadeOut(formula2),
            FadeOut(calculation2),
            FadeOut(step3_title),
            FadeOut(formula3),
            FadeOut(checkmark),
            FadeOut(completion_text),
            run_time=0.6
        )
    
    def scene_4_case_side_angle(self):
        """场景4: 情况2 - 已知一边一角"""
        # 标题
        title = Text(
            "情况2: 已知一边一角",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_KNOWN
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 已知条件
        known_text = Text(
            "已知: c = 5, ∠A = 37°",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_KNOWN
        ).move_to(UP * 5)
        
        self.play(Write(known_text), run_time=0.6)
        
        # 高亮
        self.play(
            Indicate(self.side_labels[2], color=self.COLOR_KNOWN, scale_factor=1.3),
            Indicate(self.angle_arcs[0], color=self.COLOR_KNOWN, scale_factor=1.3),
            run_time=0.8
        )
        
        # 步骤1: 用sin求a
        step1_title = Text(
            "① 用sin求边a",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(step1_title), run_time=0.6)
        
        formula1 = MathTex(
            r"a = c \times \sin A",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(Write(formula1), run_time=0.8)
        
        calculation1 = MathTex(
            r"a = 5 \times \sin 37^\circ \approx 3",
            font_size=32,
            color=self.COLOR_UNKNOWN
        ).move_to(UP * 2.2)
        
        self.play(Write(calculation1), run_time=1.0)
        self.play(Flash(calculation1, color=YELLOW), run_time=0.4)
        
        self.wait(0.8)
        
        # 步骤2: 用cos求b
        step2_title = Text(
            "② 用cos求边b",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 0.8)
        
        self.play(Write(step2_title), run_time=0.6)
        
        formula2 = MathTex(
            r"b = c \times \cos A",
            font_size=32,
            color=WHITE
        ).move_to(ORIGIN)
        
        self.play(Write(formula2), run_time=0.8)
        
        calculation2 = MathTex(
            r"b = 5 \times \cos 37^\circ \approx 4",
            font_size=32,
            color=self.COLOR_UNKNOWN
        ).move_to(DOWN * 0.8)
        
        self.play(Write(calculation2), run_time=1.0)
        self.play(Flash(calculation2, color=YELLOW), run_time=0.4)
        
        self.wait(0.8)
        
        # 步骤3: 互余关系求角B
        step3_title = Text(
            "③ 互余关系求角B",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(Write(step3_title), run_time=0.6)
        
        formula3 = MathTex(
            r"B = 90^\circ - 37^\circ = 53^\circ",
            font_size=32,
            color=self.COLOR_UNKNOWN
        ).move_to(DOWN * 2.8)
        
        self.play(Write(formula3), run_time=0.8)
        self.play(Flash(formula3, color=YELLOW), run_time=0.4)
        
        # 完成标记
        checkmark = Text("✓", font_size=60, color=GREEN).move_to(DOWN * 4.5)
        completion_text = Text(
            "同样全部求出!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        ).next_to(checkmark, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(checkmark, scale=2),
            FadeIn(completion_text),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(known_text),
            FadeOut(step1_title),
            FadeOut(formula1),
            FadeOut(calculation1),
            FadeOut(step2_title),
            FadeOut(formula2),
            FadeOut(calculation2),
            FadeOut(step3_title),
            FadeOut(formula3),
            FadeOut(checkmark),
            FadeOut(completion_text),
            run_time=0.6
        )
    
    def scene_5_warning(self):
        """场景5: 重要提醒"""
        # 警告图标
        warning_icon = Text("⚠", font_size=80, color=RED).move_to(UP * 4.5)
        
        self.play(FadeIn(warning_icon, scale=1.5), run_time=0.6)
        
        # 重要文字
        important_text = Text(
            "重要!",
            font="Noto Sans CJK SC",
            font_size=42,
            color=RED,
            weight=BOLD
        ).next_to(warning_icon, DOWN, buff=0.5)
        
        self.play(Write(important_text), run_time=0.6)
        
        # 核心提示
        core_message = Text(
            "至少要知道一条边!",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(Write(core_message), run_time=0.8)
        
        self.wait(0.5)
        
        # 错误示例
        wrong_example = Text(
            "错误示例:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(ORIGIN)
        
        wrong_condition = Text(
            "已知: ∠A = 30°, ∠B = 60°",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).next_to(wrong_example, DOWN, buff=0.5)
        
        self.play(
            Write(wrong_example),
            Write(wrong_condition),
            run_time=0.8
        )
        
        # 叉号
        cross_mark = Text("✗", font_size=70, color=RED).move_to(DOWN * 2.5)
        
        self.play(FadeIn(cross_mark, scale=2), run_time=0.6)
        
        # 说明
        explanation = Text(
            "只知道角度，无法确定大小\n所有角度相同的三角形都相似",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A,
            line_spacing=1.3
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(warning_icon),
            FadeOut(important_text),
            FadeOut(core_message),
            FadeOut(wrong_example),
            FadeOut(wrong_condition),
            FadeOut(cross_mark),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def scene_6_summary(self):
        """场景6: 方法总结"""
        # 先淡出三角形
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.right_angle_mark),
            FadeOut(self.vertex_labels),
            FadeOut(self.side_labels),
            FadeOut(self.angle_arcs),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "解直角三角形三大工具",
            font="Noto Sans CJK SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个工具卡片
        card1_icon = MathTex(r"a^2 + b^2 = c^2", font_size=28, color=self.COLOR_PRIMARY)
        card1_title = Text("勾股定理", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        card1_desc = Text("知两边求第三边", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        card1 = VGroup(card1_icon, card1_title, card1_desc).arrange(DOWN, buff=0.2)
        card1.move_to(UP * 3.5)
        card1.shift(LEFT * 10)
        
        card2_icon = MathTex(r"\sin, \cos, \tan", font_size=28, color=self.COLOR_PRIMARY)
        card2_title = Text("三角比", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        card2_desc = Text("边角互求", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        card2 = VGroup(card2_icon, card2_title, card2_desc).arrange(DOWN, buff=0.2)
        card2.move_to(UP * 1.5)
        card2.shift(LEFT * 10)
        
        card3_icon = MathTex(r"A + B = 90^\circ", font_size=28, color=self.COLOR_PRIMARY)
        card3_title = Text("互余关系", font="Noto Sans CJK SC", font_size=26, color=WHITE)
        card3_desc = Text("知一角求另一角", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        card3 = VGroup(card3_icon, card3_title, card3_desc).arrange(DOWN, buff=0.2)
        card3.move_to(DOWN * 0.5)
        card3.shift(LEFT * 10)
        
        # 卡片依次滑入
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 高亮卡片
        for card in [card1, card2, card3]:
            self.play(Flash(card, color=YELLOW, flash_radius=0.8), run_time=0.3)
        
        self.wait(0.5)
        
        # 核心提示
        core_tip = Text(
            "记住: 至少一边 + 一个其他条件",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(core_tip, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(core_tip),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # 账号ID
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 解题更轻松!",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰三角形
        triangles = VGroup(*[
            Polygon(
                ORIGIN, RIGHT * 0.3, UP * 0.3,
                color=GOLD,
                fill_opacity=0.8,
                stroke_width=0
            ).scale(0.5).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        
        self.play(Rotate(triangles, angle=PI, about_point=follow_text.get_center()), run_time=1.5)
        
        # 公式图标
        icon_radius = 0.25
        icons = VGroup(
            Circle(radius=icon_radius, color=self.COLOR_KNOWN, fill_opacity=0.8, stroke_width=0).shift(LEFT * 2.5),
            Circle(radius=icon_radius, color=self.COLOR_UNKNOWN, fill_opacity=0.8, stroke_width=0).shift(LEFT * 1.25),
            Circle(radius=icon_radius, color=self.COLOR_ANGLE, fill_opacity=0.8, stroke_width=0),
            Circle(radius=icon_radius, color=self.COLOR_PRIMARY, fill_opacity=0.8, stroke_width=0).shift(RIGHT * 1.25),
            Circle(radius=icon_radius, color=self.COLOR_HIGHLIGHT, fill_opacity=0.8, stroke_width=0).shift(RIGHT * 2.5)
        ).move_to(DOWN * 3.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql solving_right_triangle.py SolvingRightTriangle  # 快速预览
# manim -qh solving_right_triangle.py SolvingRightTriangle   # 高质量渲染