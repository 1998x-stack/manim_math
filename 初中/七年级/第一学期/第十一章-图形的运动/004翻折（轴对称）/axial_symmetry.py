"""
轴对称（翻折）教学动画 - Axial Symmetry Teaching Animation
使用 Manim 创建的七年级几何教学视频

内容: 轴对称的定义、三大性质和生活应用
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


class AxialSymmetry(Scene):
    """
    轴对称教学动画场景
    
    场景顺序:
    1. 开场钩子 - 蝴蝶的秘密
    2. 定义讲解 - 什么是轴对称
    3. 性质1 - 对应点连线垂直于对称轴
    4. 性质2 - 对称轴平分对应点连线
    5. 性质3 - 对应线段和角相等
    6. 实际应用 - 生活中的轴对称
    7. 总结片尾 - 知识点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 原图形
        self.COLOR_SYMMETRIC = "#e74c3c"      # 红色 - 对称图形
        self.COLOR_AXIS = "#f39c12"           # 橙色 - 对称轴
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_CONNECTING = "#9b59b6"     # 紫色 - 连接线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_property_1()
        self.scene_4_property_2()
        self.scene_5_property_3()
        self.scene_6_applications()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的精确坐标"""
        # 缩放和偏移参数
        self.SCALE = 1.0
        self.OFFSET = UP * 1.0
        
        # 原三角形顶点（左侧）
        self.A = np.array([-2.0, 1.0, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([-1.0, -1.5, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([-3.0, -1.0, 0]) * self.SCALE + self.OFFSET
        
        # 对称轴（y轴，即x=0）
        self.axis_point = np.array([0, 0, 0])
        self.axis_direction = np.array([0, 1, 0])  # 竖直方向
        self.axis_start = np.array([0, -6, 0])
        self.axis_end = np.array([0, 6, 0])
        
        # 计算对称点（关于y轴对称，即x坐标取负）
        self.A_prime = self.reflect_point(self.A)
        self.B_prime = self.reflect_point(self.B)
        self.C_prime = self.reflect_point(self.C)
        
        # 计算垂足（对称轴上的点）
        self.M_A = self.calculate_foot(self.A)
        self.M_B = self.calculate_foot(self.B)
        self.M_C = self.calculate_foot(self.C)
        
        # 计算边长
        self.AB = np.linalg.norm(self.B - self.A)
        self.BC = np.linalg.norm(self.C - self.B)
        self.CA = np.linalg.norm(self.A - self.C)
        
        # 验证几何计算
        self.verify_geometry()
    
    def reflect_point(self, point):
        """计算点关于y轴（x=0）的对称点"""
        # 对于关于y轴对称：(x, y) → (-x, y)
        return np.array([-point[0], point[1], point[2]])
    
    def calculate_foot(self, point):
        """计算点到对称轴（y轴）的垂足"""
        # 对于y轴：垂足就是(0, y, 0)
        return np.array([0, point[1], point[2]])
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证对称性：AM = MA'
        dist_AM = np.linalg.norm(self.M_A - self.A)
        dist_MA_prime = np.linalg.norm(self.A_prime - self.M_A)
        
        if abs(dist_AM - dist_MA_prime) > epsilon:
            print(f"WARNING: 对称性验证失败! AM={dist_AM:.6f}, MA'={dist_MA_prime:.6f}")
        
        # 验证M是中点
        midpoint_check = (self.A + self.A_prime) / 2
        if np.linalg.norm(self.M_A - midpoint_check) > epsilon:
            print(f"WARNING: 中点验证失败!")
        
        # 验证垂直性：AA'与对称轴垂直
        vec_AA_prime = self.A_prime - self.A
        dot_product = np.dot(vec_AA_prime[:2], self.axis_direction[:2])
        
        if abs(dot_product) > epsilon:
            print(f"WARNING: 垂直性验证失败! 点积={dot_product:.6f}")
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 - 蝴蝶的秘密"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "蝴蝶为什么这么美？",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简化蝴蝶 - 左半边
        butterfly_left = VGroup(
            # 上翅膀
            Polygon(
                [-0.3, 2.5, 0],
                [-1.5, 3.5, 0],
                [-2.0, 2.8, 0],
                [-1.2, 2.0, 0],
                color=self.COLOR_PRIMARY,
                fill_opacity=0.7,
                stroke_width=2
            ),
            # 下翅膀
            Polygon(
                [-0.3, 1.5, 0],
                [-1.8, 1.2, 0],
                [-1.5, 0.5, 0],
                [-0.8, 1.0, 0],
                color=self.COLOR_PRIMARY,
                fill_opacity=0.7,
                stroke_width=2
            )
        ).move_to(UP * 2)
        
        self.play(Create(butterfly_left), run_time=1.0)
        
        # 对称轴
        axis_butterfly = DashedLine(
            UP * 4.5,
            UP * 0.5,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(axis_butterfly), run_time=0.5)
        self.play(Flash(axis_butterfly, color=self.COLOR_AXIS, flash_radius=0.5), run_time=0.4)
        
        # 右半边镜像出现
        butterfly_right = butterfly_left.copy().flip(RIGHT).set_color(self.COLOR_SYMMETRIC)
        
        self.play(Create(butterfly_right), run_time=0.8)
        
        # 提示文字
        hint_text = Text(
            "秘密在于轴对称!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(butterfly_left),
            FadeOut(butterfly_right),
            FadeOut(axis_butterfly),
            FadeOut(hint_text),
            run_time=0.6
        )
    
    def scene_2_definition(self):
        """场景2: 定义讲解"""
        # 标题
        title = Text(
            "什么是轴对称？",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        # 定义文字
        definition = Text(
            "把图形沿一条直线对折后\n能完全重合的变换",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(title), run_time=0.5)
        self.play(Write(definition), run_time=1.0)
        
        # 创建三角形
        triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=3
        )
        
        # 标注顶点
        label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(self.A, LEFT, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(self.B, DOWN, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(self.C, LEFT, buff=0.15)
        
        self.play(Create(triangle), run_time=1.0)
        self.play(FadeIn(label_A), FadeIn(label_B), FadeIn(label_C), run_time=0.4)
        
        # 对称轴
        axis = DashedLine(
            self.axis_start,
            self.axis_end,
            color=self.COLOR_AXIS,
            dash_length=0.15,
            stroke_width=3
        )
        
        axis_label = Text(
            "对称轴",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AXIS
        ).next_to(axis, UP, buff=0.2)
        
        self.play(Create(axis), FadeIn(axis_label), run_time=0.8)
        
        # 说明文字
        fold_text = Text(
            "沿对称轴对折",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(fold_text), run_time=0.5)
        
        # 折叠动画（3D旋转模拟）
        triangle_copy = triangle.copy()
        self.play(
            Rotate(
                triangle_copy,
                angle=PI,
                axis=UP,  # 绕y轴旋转
                about_point=ORIGIN,
                run_time=1.5
            )
        )
        
        overlap_text = Text(
            "能完全重合",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(overlap_text), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(triangle_copy),
            FadeOut(fold_text),
            FadeOut(overlap_text),
            FadeOut(axis_label),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            run_time=0.6
        )
        
        # 保留原三角形和对称轴
        self.triangle = triangle
        self.axis = axis
    
    def scene_3_property_1(self):
        """场景3: 性质1 - 对应点连线垂直于对称轴"""
        # 标题
        property1_title = Text(
            "性质1：垂直关系",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(property1_title), run_time=0.5)
        
        # 创建对称三角形
        triangle_prime = Polygon(
            self.A_prime, self.B_prime, self.C_prime,
            color=self.COLOR_SYMMETRIC,
            fill_opacity=0.3,
            stroke_width=3
        )
        
        self.play(Create(triangle_prime), run_time=1.0)
        
        # 标注对称点
        label_A_prime = Text("A'", font="PingFang SC", font_size=22, color=WHITE).next_to(self.A_prime, RIGHT, buff=0.15)
        label_B_prime = Text("B'", font="PingFang SC", font_size=22, color=WHITE).next_to(self.B_prime, DOWN, buff=0.15)
        label_C_prime = Text("C'", font="PingFang SC", font_size=22, color=WHITE).next_to(self.C_prime, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(label_A_prime),
            FadeIn(label_B_prime),
            FadeIn(label_C_prime),
            run_time=0.5
        )
        
        # 绘制连接线AA'
        line_AA = Line(
            self.A, self.A_prime,
            color=self.COLOR_CONNECTING,
            stroke_width=2
        )
        
        self.play(Create(line_AA), run_time=0.8)
        
        # 标记垂足M
        dot_M = Dot(self.M_A, color=YELLOW, radius=0.08)
        label_M = Text("M", font="PingFang SC", font_size=20, color=YELLOW).next_to(dot_M, DOWN, buff=0.1)
        
        self.play(FadeIn(dot_M), FadeIn(label_M), run_time=0.4)
        
        # 垂直标记
        perpendicular_mark = self.create_perpendicular_mark(
            self.M_A,
            self.A - self.M_A,
            self.axis_direction,
            size=0.18
        )
        
        self.play(Create(perpendicular_mark), run_time=0.5)
        self.play(Flash(perpendicular_mark, color=YELLOW, flash_radius=0.3), run_time=0.4)
        
        # 公式
        formula1_chinese = Text(
            "对应点连线",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        formula1_symbol = MathTex(r"\perp", font_size=32, color=YELLOW)
        formula1_chinese2 = Text(
            "对称轴",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AXIS
        )
        
        formula1 = VGroup(formula1_chinese, formula1_symbol, formula1_chinese2).arrange(RIGHT, buff=0.15).move_to(DOWN * 4)
        
        self.play(Write(formula1), run_time=1.0)
        
        # 绘制其他连接线
        line_BB = Line(self.B, self.B_prime, color=self.COLOR_CONNECTING, stroke_width=2)
        line_CC = Line(self.C, self.C_prime, color=self.COLOR_CONNECTING, stroke_width=2)
        
        self.play(
            Create(line_BB),
            Create(line_CC),
            run_time=0.8
        )
        
        explanation = Text(
            "所有对应点连线都垂直于对称轴",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(property1_title),
            FadeOut(formula1),
            FadeOut(explanation),
            FadeOut(perpendicular_mark),
            run_time=0.5
        )
        
        # 保留对称三角形、连接线、标签
        self.triangle_prime = triangle_prime
        self.line_AA = line_AA
        self.line_BB = line_BB
        self.line_CC = line_CC
        self.dot_M = dot_M
        self.label_M = label_M
        self.labels_prime = VGroup(label_A_prime, label_B_prime, label_C_prime)
    
    def create_perpendicular_mark(self, corner, direction1, direction2, size=0.15):
        """创建垂直标记（小正方形）"""
        v1 = direction1 / np.linalg.norm(direction1) * size
        v2 = direction2 / np.linalg.norm(direction2) * size
        
        square = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0
        )
        return square
    
    def scene_4_property_2(self):
        """场景4: 性质2 - 对称轴平分对应点连线"""
        # 标题
        property2_title = Text(
            "性质2：平分关系",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(property2_title), run_time=0.5)
        
        # 高亮中点M（已存在）
        self.play(
            self.dot_M.animate.set_color(YELLOW).scale(1.5),
            self.label_M.animate.set_color(YELLOW).scale(1.2),
            run_time=0.5
        )
        
        # 高亮AM段
        segment_AM = Line(self.A, self.M_A, color=YELLOW, stroke_width=4)
        self.play(Create(segment_AM), run_time=0.8)
        
        # 标注距离
        brace_AM = Brace(segment_AM, direction=UP * 0.3 + LEFT * 0.7, buff=0.1, color=YELLOW)
        label_AM = Text("d", font="PingFang SC", font_size=20, color=YELLOW).next_to(brace_AM, UP * 0.3 + LEFT * 0.7, buff=0.05)
        
        self.play(FadeIn(brace_AM), FadeIn(label_AM), run_time=0.6)
        
        # 高亮MA'段
        segment_MA_prime = Line(self.M_A, self.A_prime, color=YELLOW, stroke_width=4)
        self.play(Create(segment_MA_prime), run_time=0.8)
        
        # 标注距离
        brace_MA_prime = Brace(segment_MA_prime, direction=UP * 0.3 + RIGHT * 0.7, buff=0.1, color=YELLOW)
        label_MA_prime = Text("d", font="PingFang SC", font_size=20, color=YELLOW).next_to(brace_MA_prime, UP * 0.3 + RIGHT * 0.7, buff=0.05)
        
        self.play(FadeIn(brace_MA_prime), FadeIn(label_MA_prime), run_time=0.6)
        
        # 公式
        formula2_chinese = Text(
            "M 是",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        formula2_math = Text(
            "AA'",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_CONNECTING
        )
        formula2_chinese2 = Text(
            "的中点",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        formula2 = VGroup(formula2_chinese, formula2_math, formula2_chinese2).arrange(RIGHT, buff=0.1).move_to(DOWN * 4)
        
        self.play(Write(formula2), run_time=1.0)
        
        explanation2 = Text(
            "对称轴平分对应点连线",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation2), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(property2_title),
            FadeOut(formula2),
            FadeOut(explanation2),
            FadeOut(segment_AM),
            FadeOut(segment_MA_prime),
            FadeOut(brace_AM),
            FadeOut(label_AM),
            FadeOut(brace_MA_prime),
            FadeOut(label_MA_prime),
            self.dot_M.animate.scale(1/1.5),
            self.label_M.animate.scale(1/1.2),
            run_time=0.5
        )
    
    def scene_5_property_3(self):
        """场景5: 性质3 - 对应线段和角相等"""
        # 标题
        property3_title = Text(
            "性质3：全等性质",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(property3_title), run_time=0.5)
        
        # 高亮对应边AB和A'B'
        self.play(
            self.triangle.animate.set_stroke(color=WHITE, width=2),
            self.triangle_prime.animate.set_stroke(color=WHITE, width=2),
            run_time=0.3
        )
        
        # 高亮AB边
        ab_highlight = Line(self.A, self.B, color=YELLOW, stroke_width=5)
        ab_prime_highlight = Line(self.A_prime, self.B_prime, color=YELLOW, stroke_width=5)
        
        self.play(Create(ab_highlight), run_time=0.5)
        self.wait(0.3)
        self.play(Create(ab_prime_highlight), run_time=0.5)
        
        # 边长标注
        ab_length = np.linalg.norm(self.B - self.A)
        
        equal_sides_text = Text(
            "对应边相等",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        equal_sides_formula = MathTex(
            r"AB = A'B'",
            font_size=28,
            color=YELLOW
        )
        
        equal_sides = VGroup(equal_sides_text, equal_sides_formula).arrange(DOWN, buff=0.2).move_to(DOWN * 4)
        
        self.play(Write(equal_sides), run_time=1.0)
        
        self.wait(0.8)
        
        # 淡出边的高亮
        self.play(
            FadeOut(ab_highlight),
            FadeOut(ab_prime_highlight),
            FadeOut(equal_sides),
            run_time=0.5
        )
        
        # 标注角度
        # 角A的标记
        angle_A = self.create_angle_arc(self.A, self.B, self.C, radius=0.4, color=self.COLOR_PRIMARY)
        angle_A_prime = self.create_angle_arc(self.A_prime, self.B_prime, self.C_prime, radius=0.4, color=self.COLOR_SYMMETRIC)
        
        self.play(Create(angle_A), Create(angle_A_prime), run_time=0.8)
        
        # 角度标注
        equal_angles_text = Text(
            "对应角相等",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        equal_angles_formula = MathTex(
            r"\angle A = \angle A'",
            font_size=28,
            color=YELLOW
        )
        
        equal_angles = VGroup(equal_angles_text, equal_angles_formula).arrange(DOWN, buff=0.2).move_to(DOWN * 4)
        
        self.play(Write(equal_angles), run_time=1.0)
        
        self.wait(0.8)
        
        # 总结公式
        formula3_chinese = Text(
            "轴对称是",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        formula3_highlight = Text(
            "全等变换",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        )
        
        formula3 = VGroup(formula3_chinese, formula3_highlight).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.5)
        
        self.play(
            FadeOut(equal_angles),
            FadeIn(formula3),
            run_time=0.8
        )
        
        self.wait(1.2)
        
        # 清理场景
        self.play(
            FadeOut(property3_title),
            FadeOut(formula3),
            FadeOut(angle_A),
            FadeOut(angle_A_prime),
            FadeOut(self.triangle),
            FadeOut(self.triangle_prime),
            FadeOut(self.axis),
            FadeOut(self.line_AA),
            FadeOut(self.line_BB),
            FadeOut(self.line_CC),
            FadeOut(self.dot_M),
            FadeOut(self.label_M),
            FadeOut(self.labels_prime),
            run_time=0.6
        )
    
    def create_angle_arc(self, vertex, point1, point2, radius=0.3, color=BLUE):
        """创建角度标记的圆弧"""
        # 计算两条边的方向
        vec1 = (point1 - vertex) / np.linalg.norm(point1 - vertex)
        vec2 = (point2 - vertex) / np.linalg.norm(point2 - vertex)
        
        # 计算起始和结束角度
        angle1 = np.arctan2(vec1[1], vec1[0])
        angle2 = np.arctan2(vec2[1], vec2[0])
        
        # 创建圆弧
        arc = Arc(
            radius=radius,
            start_angle=angle1,
            angle=angle2 - angle1,
            color=color,
            stroke_width=2
        ).move_arc_center_to(vertex)
        
        return arc
    
    def scene_6_applications(self):
        """场景6: 实际应用示例"""
        # 标题
        application_title = Text(
            "轴对称在生活中",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(application_title), run_time=0.6)
        
        # 示例1: 汉字"中"（上下对称）
        chinese_char = Text(
            "中",
            font="PingFang SC",
            font_size=80,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.5)
        
        axis_horizontal = DashedLine(
            LEFT * 1.5 + UP * 3.5,
            RIGHT * 1.5 + UP * 3.5,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=2
        )
        
        example1_label = Text(
            "上下对称",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(chinese_char, DOWN, buff=0.5)
        
        self.play(Create(chinese_char), run_time=0.8)
        self.play(Create(axis_horizontal), FadeIn(example1_label), run_time=0.6)
        self.wait(0.8)
        
        # 示例2: 正方形（四条对称轴）
        square = Square(side_length=2, color=self.COLOR_SYMMETRIC, stroke_width=3).move_to(UP * 0.5)
        
        # 四条对称轴
        axis_v = DashedLine(UP * 1.5, DOWN * 0.5, color=self.COLOR_AXIS, dash_length=0.08, stroke_width=2)
        axis_h = DashedLine(LEFT * 1 + UP * 0.5, RIGHT * 1 + UP * 0.5, color=self.COLOR_AXIS, dash_length=0.08, stroke_width=2)
        axis_d1 = DashedLine(LEFT * 0.7 + UP * 1.2, RIGHT * 0.7 + DOWN * 0.2, color=self.COLOR_AXIS, dash_length=0.08, stroke_width=2)
        axis_d2 = DashedLine(LEFT * 0.7 + DOWN * 0.2, RIGHT * 0.7 + UP * 1.2, color=self.COLOR_AXIS, dash_length=0.08, stroke_width=2)
        
        four_axes = VGroup(axis_v, axis_h, axis_d1, axis_d2)
        
        example2_label = Text(
            "四条对称轴",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(square, DOWN, buff=0.5)
        
        self.play(
            FadeOut(chinese_char),
            FadeOut(axis_horizontal),
            FadeOut(example1_label),
            run_time=0.4
        )
        
        self.play(Create(square), run_time=0.8)
        self.play(Create(four_axes), FadeIn(example2_label), run_time=1.0)
        self.wait(0.8)
        
        # 示例3: 字母A（左右对称）
        letter_A = Text(
            "A",
            font="Arial",
            font_size=90,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        axis_vertical = DashedLine(
            DOWN * 1.5,
            DOWN * 3.8,
            color=self.COLOR_AXIS,
            dash_length=0.1,
            stroke_width=2
        )
        
        example3_label = Text(
            "左右对称",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(letter_A, DOWN, buff=0.5)
        
        self.play(
            FadeOut(square),
            FadeOut(four_axes),
            FadeOut(example2_label),
            run_time=0.4
        )
        
        self.play(Create(letter_A), run_time=0.8)
        self.play(Create(axis_vertical), FadeIn(example3_label), run_time=0.6)
        self.wait(0.8)
        
        # 提示
        life_hint = Text(
            "生活中处处有对称!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(life_hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(application_title),
            FadeOut(letter_A),
            FadeOut(axis_vertical),
            FadeOut(example3_label),
            FadeOut(life_hint),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结和片尾"""
        # 总结标题
        summary_title = Text(
            "轴对称三大性质",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 创建三张卡片
        card1 = self.create_property_card(
            "1",
            "对应点连线 ⊥ 对称轴",
            self.COLOR_PRIMARY,
            UP * 3.5
        )
        
        card2 = self.create_property_card(
            "2",
            "对称轴平分对应点连线",
            self.COLOR_SYMMETRIC,
            UP * 1.5
        )
        
        card3 = self.create_property_card(
            "3",
            "对应线段相等，对应角相等",
            "#2ecc71",
            DOWN * 0.5
        )
        
        # 卡片依次滑入
        self.play(card1.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card2.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card3.animate.shift(RIGHT * 0), run_time=0.6)
        
        # 关键提示
        key_tip = Text(
            "掌握轴对称，解题更轻松!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(key_tip, shift=UP * 0.3, scale=1.1), run_time=0.7)
        self.wait(1.5)
        
        # 清理并准备片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(key_tip),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画 - 对称图形
        decoration = VGroup(
            Square(side_length=0.5, color=self.COLOR_PRIMARY, fill_opacity=0.5).shift(LEFT * 1.5 + DOWN * 2),
            Square(side_length=0.5, color=self.COLOR_PRIMARY, fill_opacity=0.5).shift(RIGHT * 1.5 + DOWN * 2),
            Circle(radius=0.3, color=self.COLOR_SYMMETRIC, fill_opacity=0.5).shift(LEFT * 1.5 + DOWN * 3.5),
            Circle(radius=0.3, color=self.COLOR_SYMMETRIC, fill_opacity=0.5).shift(RIGHT * 1.5 + DOWN * 3.5),
        )
        
        self.play(*[FadeIn(d, scale=0.5) for d in decoration], run_time=0.6)
        self.play(Rotate(decoration, angle=PI/4, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration),
            run_time=1.0
        )
    
    def create_property_card(self, number, content, color, position):
        """创建性质卡片"""
        # 数字圆圈
        circle = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        number_text = Text(
            number,
            font="PingFang SC",
            font_size=28,
            color=WHITE,
            weight=BOLD
        ).move_to(circle.get_center())
        
        icon = VGroup(circle, number_text)
        
        # 内容文字
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, content_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql axial_symmetry.py AxialSymmetry  # 快速预览
# manim -qh axial_symmetry.py AxialSymmetry   # 高质量渲染（推荐用于TikTok）