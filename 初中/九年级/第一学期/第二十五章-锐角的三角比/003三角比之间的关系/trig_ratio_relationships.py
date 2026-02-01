"""
三角比之间的关系 - Trigonometric Ratio Relationships
使用 Manim 创建的九年级数学教学视频

内容: sin²A+cos²A=1, tanA=sinA/cosA, 互余角关系
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


class TrigRatioRelationships(Scene):
    """
    三角比关系教学动画
    
    场景顺序:
    1. 开场钩子
    2. 建立直角三角形
    3. 关系1: sin²A + cos²A = 1
    4. 关系2: tanA = sinA/cosA
    5. 关系3: 互余角关系
    6. 总结回顾
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
        self.COLOR_SIN = "#2ecc71"          # 绿色 - sin
        self.COLOR_COS = "#9b59b6"          # 紫色 - cos
        self.COLOR_TAN = "#f39c12"          # 橙色 - tan
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_triangle_setup()
        self.scene_3_pythagorean_identity()
        self.scene_4_tangent_quotient()
        self.scene_5_complementary_angles()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何数据 - 所有坐标通过精确计算获得"""
        # 基准参数
        self.SCALE = 1.2
        self.OFFSET = UP * 1.0
        
        # 定义直角三角形 - 使用标准3-4-5直角三角形
        # 直角在C点, 角A在A点, 角B在B点
        # 放置: C在原点, A在左侧, B在上方
        # 这样形成：BC=3.6 (对边), AC=4.8 (邻边), AB=6.0 (斜边)
        
        self.C = np.array([0, 0, 0]) * self.SCALE + self.OFFSET  # 直角顶点
        self.A = np.array([-4, 0, 0]) * self.SCALE + self.OFFSET  # 左侧
        self.B = np.array([0, 3, 0]) * self.SCALE + self.OFFSET   # 上方
        
        # 精确计算边长
        self.a = np.linalg.norm(self.C - self.B)  # BC (对边, opposite) - 对于角A
        self.b = np.linalg.norm(self.C - self.A)  # AC (邻边, adjacent) - 对于角A  
        self.c = np.linalg.norm(self.B - self.A)  # AB (斜边, hypotenuse)
        
        # 计算三角比 (角A的三角比)
        self.sin_A = self.a / self.c  # 对边/斜边
        self.cos_A = self.b / self.c  # 邻边/斜边
        self.tan_A = self.a / self.b  # 对边/邻边
        
        # 计算角度(用于显示) - 角A在顶点A
        vec_AB = self.B - self.A
        vec_AC = self.C - self.A
        self.angle_A_rad = GeometryCalculator.angle_at_vertex(self.B, self.A, self.C)
        self.angle_A_deg = np.degrees(self.angle_A_rad)
        
        # 互余角 (角B) - 直角在C
        self.angle_B_rad = np.pi/2 - self.angle_A_rad
        self.sin_B = self.b / self.c  # 对于角B，AC是对边
        self.cos_B = self.a / self.c  # 对于角B，BC是邻边
        self.tan_B = self.b / self.a
        
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
        
        # 验证勾股定理 (a² + b² = c², where c is the hypotenuse AB)
        pythagorean = self.a**2 + self.b**2 - self.c**2
        if abs(pythagorean) > eps:
            errors.append(f"勾股定理不成立! a²+b²-c²={pythagorean}")
        
        # 验证 sin²A + cos²A = 1
        identity1 = self.sin_A**2 + self.cos_A**2 - 1.0
        if abs(identity1) > eps:
            errors.append(f"sin²+cos²≠1! 差值={identity1}")
        
        # 验证 tanA = sinA/cosA
        tan_quotient = self.sin_A / self.cos_A - self.tan_A
        if abs(tan_quotient) > eps:
            errors.append(f"tan≠sin/cos! 差值={tan_quotient}")
        
        # 验证互余关系 (角A和角B互余)
        complementary1 = self.sin_A - self.cos_B
        if abs(complementary1) > eps:
            errors.append(f"sinA≠cosB! 差值={complementary1}")
        
        complementary2 = self.cos_A - self.sin_B
        if abs(complementary2) > eps:
            errors.append(f"cosA≠sinB! 差值={complementary2}")
        
        complementary3 = self.tan_A * self.tan_B - 1.0
        if abs(complementary3) > eps:
            errors.append(f"tanA·tanB≠1! 差值={complementary3}")
        
        if errors:
            print("❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败!")
        else:
            print("✓ 几何验证通过")
            print(f"  三角形边长: a={self.a:.3f}, b={self.b:.3f}, c={self.c:.3f}")
            print(f"  三角比: sin={self.sin_A:.3f}, cos={self.cos_A:.3f}, tan={self.tan_A:.3f}")
    
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
            "同一个角的三角比\n有什么关系?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 三个公式快闪
        formula1 = MathTex(
            r"\sin^2 A + \cos^2 A = 1",
            font_size=32,
            color=self.COLOR_SIN
        ).move_to(UP * 3)
        
        formula2 = MathTex(
            r"\tan A = \frac{\sin A}{\cos A}",
            font_size=32,
            color=self.COLOR_TAN
        ).move_to(UP * 2)
        
        formula3 = MathTex(
            r"\sin A = \cos(90^\circ - A)",
            font_size=32,
            color=self.COLOR_COS
        ).move_to(UP * 1)
        
        formulas = VGroup(formula1, formula2, formula3)
        
        for formula in formulas:
            self.play(Flash(formula, color=YELLOW, flash_radius=0.3), FadeIn(formula), run_time=0.4)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(formulas),
            run_time=0.5
        )
    
    def scene_2_triangle_setup(self):
        """场景2: 建立直角三角形"""
        # 创建三角形
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(self.triangle), run_time=1.0)
        
        # 直角标记 (at C)
        right_angle_size = 0.25
        # 计算从C出发的两条边的方向向量
        vec_CA = (self.A - self.C) / np.linalg.norm(self.A - self.C)
        vec_CB = (self.B - self.C) / np.linalg.norm(self.B - self.C)
        
        right_angle_square = Polygon(
            self.C,
            self.C + vec_CA * right_angle_size,
            self.C + vec_CA * right_angle_size + vec_CB * right_angle_size,
            self.C + vec_CB * right_angle_size,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        )
        
        self.play(Create(right_angle_square), run_time=0.5)
        
        # 顶点标签
        label_A = MathTex("A", font_size=28, color=WHITE).next_to(self.A, DL, buff=0.2)
        label_B = MathTex("B", font_size=28, color=WHITE).next_to(self.B, DR, buff=0.2)
        label_C = MathTex("C", font_size=28, color=WHITE).next_to(self.C, UP, buff=0.2)
        
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            run_time=0.6
        )
        
        # 边长标签
        side_label_a = MathTex("a", font_size=24, color=self.COLOR_SECONDARY).next_to(
            (self.B + self.C) / 2, RIGHT, buff=0.15
        )
        side_label_b = MathTex("b", font_size=24, color=self.COLOR_SECONDARY).next_to(
            (self.A + self.B) / 2, DOWN, buff=0.15
        )
        side_label_c = MathTex("c", font_size=24, color=self.COLOR_SECONDARY).next_to(
            (self.A + self.C) / 2, LEFT, buff=0.15
        )
        
        self.side_labels = VGroup(side_label_a, side_label_b, side_label_c)
        
        self.play(Write(self.side_labels), run_time=0.8)
        
        # 标记角A (at vertex A)
        # 角A is from AB to AC
        angle_arc = Arc(
            radius=0.5,
            start_angle=0,  # From AB (horizontal right)
            angle=self.angle_A_rad,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_arc_center_to(self.A)
        
        # Position angle label
        mid_angle = self.angle_A_rad / 2
        angle_label = MathTex("A", font_size=22, color=self.COLOR_HIGHLIGHT).move_to(
            self.A + 0.7 * (np.cos(mid_angle) * RIGHT + np.sin(mid_angle) * UP)
        )
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.6)
        
        self.wait(1.0)
        
        # 保存元素引用
        self.right_angle_mark = right_angle_square
        self.vertex_labels = VGroup(label_A, label_B, label_C)
        self.angle_A_arc = angle_arc
        self.angle_A_label = angle_label
    
    def scene_3_pythagorean_identity(self):
        """场景3: sin²A + cos²A = 1"""
        # 标题
        title = Text(
            "关系一: 平方和关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SIN
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 勾股定理
        step1 = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.2)
        
        explanation = Text(
            "(勾股定理)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(step1, RIGHT, buff=0.3)
        
        self.play(Write(step1), FadeIn(explanation), run_time=0.8)
        
        # 高亮三条边
        self.play(
            Indicate(self.triangle, color=self.COLOR_HIGHLIGHT, scale_factor=1.05),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 两边同除c²
        step2 = MathTex(
            r"\frac{a^2}{c^2} + \frac{b^2}{c^2} = \frac{c^2}{c^2}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(
            TransformMatchingTex(step1, step2),
            FadeOut(explanation),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 化简
        step3 = MathTex(
            r"\left(\frac{a}{c}\right)^2 + \left(\frac{b}{c}\right)^2 = 1",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3)
        
        self.play(TransformMatchingTex(step2, step3), run_time=1.0)
        self.wait(0.5)
        
        # 替换为sin和cos
        step4 = MathTex(
            r"\sin^2 A + \cos^2 A = 1",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        # 标注定义
        sin_def = MathTex(
            r"\sin A = \frac{a}{c}",
            font_size=24,
            color=self.COLOR_SIN
        ).move_to(DOWN * 4)
        
        cos_def = MathTex(
            r"\cos A = \frac{b}{c}",
            font_size=24,
            color=self.COLOR_COS
        ).next_to(sin_def, RIGHT, buff=0.8)
        
        self.play(
            TransformMatchingTex(step3, step4),
            FadeIn(sin_def, shift=UP * 0.2),
            FadeIn(cos_def, shift=UP * 0.2),
            run_time=1.0
        )
        
        # 矩形框高亮
        box = SurroundingRectangle(step4, color=self.COLOR_HIGHLIGHT, buff=0.2)
        self.play(Create(box), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step4),
            FadeOut(box),
            FadeOut(sin_def),
            FadeOut(cos_def),
            run_time=0.6
        )
    
    def scene_4_tangent_quotient(self):
        """场景4: tanA = sinA/cosA"""
        # 标题
        title = Text(
            "关系二: 商的关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_TAN
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 三角比定义
        sin_def = MathTex(
            r"\sin A = \frac{a}{c}",
            font_size=32,
            color=self.COLOR_SIN
        ).move_to(UP * 4)
        
        cos_def = MathTex(
            r"\cos A = \frac{b}{c}",
            font_size=32,
            color=self.COLOR_COS
        ).next_to(sin_def, DOWN, buff=0.5, aligned_edge=LEFT)
        
        tan_def = MathTex(
            r"\tan A = \frac{a}{b}",
            font_size=32,
            color=self.COLOR_TAN
        ).next_to(cos_def, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(sin_def), run_time=0.6)
        self.play(Write(cos_def), run_time=0.6)
        self.play(Write(tan_def), run_time=0.6)
        
        self.wait(0.5)
        
        # 计算 sinA/cosA
        step1 = MathTex(
            r"\frac{\sin A}{\cos A} = \frac{\frac{a}{c}}{\frac{b}{c}}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Write(step1), run_time=1.0)
        self.wait(0.5)
        
        # 化简
        step2 = MathTex(
            r"\frac{\sin A}{\cos A} = \frac{a}{c} \times \frac{c}{b}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(TransformMatchingTex(step1, step2), run_time=1.0)
        self.wait(0.5)
        
        # 约分
        step3 = MathTex(
            r"\frac{\sin A}{\cos A} = \frac{a}{b}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(TransformMatchingTex(step2, step3), run_time=1.0)
        self.wait(0.5)
        
        # 最终结论
        conclusion = MathTex(
            r"\tan A = \frac{\sin A}{\cos A}",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(Write(conclusion), run_time=1.0)
        
        # 矩形框
        box = SurroundingRectangle(conclusion, color=self.COLOR_HIGHLIGHT, buff=0.2)
        self.play(Create(box), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sin_def),
            FadeOut(cos_def),
            FadeOut(tan_def),
            FadeOut(step3),
            FadeOut(conclusion),
            FadeOut(box),
            run_time=0.6
        )
    
    def scene_5_complementary_angles(self):
        """场景5: 互余角关系"""
        # 标题
        title = Text(
            "关系三: 互余角关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_COS
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 标记角B (the complementary angle to A)
        # 角B is at vertex B, from BC to BA
        vec_BC = self.C - self.B
        vec_BA = self.A - self.B
        # Calculate the starting angle for the arc
        start_angle_B = np.arctan2(vec_BC[1], vec_BC[0])
        
        angle_B_arc = Arc(
            radius=0.5,
            start_angle=start_angle_B,
            angle=self.angle_B_rad,
            color=self.COLOR_COS,
            stroke_width=2
        ).move_arc_center_to(self.B)
        
        mid_angle_B = start_angle_B + self.angle_B_rad / 2
        angle_B_label = MathTex("B", font_size=22, color=self.COLOR_COS).move_to(
            self.B + 0.65 * (np.cos(mid_angle_B) * RIGHT + np.sin(mid_angle_B) * UP)
        )
        
        self.play(Create(angle_B_arc), Write(angle_B_label), run_time=0.6)
        
        # 互余说明
        complementary_text = Text(
            "互余: ∠A + ∠B = 90°",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.2)
        
        angle_equation = MathTex(
            r"\angle B = 90^\circ - \angle A",
            font_size=28,
            color=self.COLOR_COS
        ).move_to(UP * 3.5)
        
        self.play(Write(complementary_text), run_time=0.8)
        self.play(Write(angle_equation), run_time=0.6)
        
        self.wait(0.8)
        
        # 三组关系
        relation1 = MathTex(
            r"\sin A = \cos(90^\circ - A)",
            font_size=32,
            color=self.COLOR_SIN
        ).move_to(UP * 2.3)
        
        relation2 = MathTex(
            r"\cos A = \sin(90^\circ - A)",
            font_size=32,
            color=self.COLOR_COS
        ).move_to(UP * 1.3)
        
        relation3 = MathTex(
            r"\tan A \cdot \tan(90^\circ - A) = 1",
            font_size=32,
            color=self.COLOR_TAN
        ).move_to(UP * 0.3)
        
        # 依次显示
        self.play(Write(relation1), run_time=0.8)
        self.wait(0.5)
        
        # 高亮对应的边 - For angle A: opposite is BC
        side_BC = Line(self.B, self.C, color=self.COLOR_SIN, stroke_width=5)
        self.play(Create(side_BC), run_time=0.5)
        self.play(FadeOut(side_BC), run_time=0.3)
        
        self.play(Write(relation2), run_time=0.8)
        self.wait(0.5)
        
        self.play(Write(relation3), run_time=0.8)
        
        # 框选三组关系
        relations_group = VGroup(relation1, relation2, relation3)
        box = SurroundingRectangle(relations_group, color=self.COLOR_HIGHLIGHT, buff=0.25)
        self.play(Create(box), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(angle_B_arc),
            FadeOut(angle_B_label),
            FadeOut(complementary_text),
            FadeOut(angle_equation),
            FadeOut(relations_group),
            FadeOut(box),
            run_time=0.6
        )
    
    def scene_6_summary(self):
        """场景6: 总结回顾"""
        # 三角形移到右上角并缩小
        triangle_group = VGroup(
            self.triangle,
            self.right_angle_mark,
            self.vertex_labels,
            self.side_labels,
            self.angle_A_arc,
            self.angle_A_label
        )
        
        self.play(
            triangle_group.animate.scale(0.4).to_corner(UR, buff=0.5),
            run_time=0.8
        )
        
        # 标题
        title = Text(
            "三角比的三大关系",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个卡片
        card1_title = Text("平方和关系", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        card1_formula = MathTex(r"\sin^2 A + \cos^2 A = 1", font_size=28, color=self.COLOR_SIN)
        card1 = VGroup(card1_title, card1_formula).arrange(DOWN, buff=0.2)
        card1.move_to(UP * 3.5)
        card1.shift(LEFT * 10)  # 初始位置在屏幕外
        
        card2_title = Text("商的关系", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        card2_formula = MathTex(r"\tan A = \frac{\sin A}{\cos A}", font_size=28, color=self.COLOR_TAN)
        card2 = VGroup(card2_title, card2_formula).arrange(DOWN, buff=0.2)
        card2.move_to(UP * 1.5)
        card2.shift(LEFT * 10)
        
        card3_title = Text("互余角关系", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        card3_formula = MathTex(r"\sin A = \cos(90^\circ - A)", font_size=28, color=self.COLOR_COS)
        card3 = VGroup(card3_title, card3_formula).arrange(DOWN, buff=0.2)
        card3.move_to(DOWN * 0.5)
        card3.shift(LEFT * 10)
        
        # 卡片依次滑入
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 三卡片高亮
        for card in [card1, card2, card3]:
            self.play(Flash(card, color=YELLOW, flash_radius=0.5), run_time=0.3)
        
        # 强调文字
        emphasis = Text(
            "记住这三个, 解题无忧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(emphasis, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(emphasis),
            FadeOut(triangle_group),
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
            "关注我, 数学更简单!",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰三角形 (围绕旋转)
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
        
        # 公式图标闪烁
        icon_radius = 0.25
        icons = VGroup(
            Circle(radius=icon_radius, color=self.COLOR_SIN, fill_opacity=0.8, stroke_width=0).shift(LEFT * 2.5),
            Circle(radius=icon_radius, color=self.COLOR_COS, fill_opacity=0.8, stroke_width=0).shift(LEFT * 1.25),
            Circle(radius=icon_radius, color=self.COLOR_TAN, fill_opacity=0.8, stroke_width=0),
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
# manim -pql trig_ratio_relationships.py TrigRatioRelationships  # 快速预览
# manim -qh trig_ratio_relationships.py TrigRatioRelationships   # 高质量渲染