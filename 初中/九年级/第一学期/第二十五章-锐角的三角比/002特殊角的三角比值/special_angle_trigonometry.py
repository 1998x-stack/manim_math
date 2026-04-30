"""
特殊角的三角比值动画 - Special Angle Trigonometric Values Animation
使用 Manim 创建的九年级数学教学视频

内容: 30°、45°、60°的三角比值推导和记忆
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


class SpecialAngleTrigonometry(Scene):
    """
    特殊角三角比值教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 30°角构造 (等边三角形)
    3. 30°角三角比计算
    4. 45°角构造 (等腰直角三角形)
    5. 45°角三角比计算
    6. 60°角构造
    7. 60°角三角比计算
    8. 汇总表格
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主三角形
        self.COLOR_30 = "#e74c3c"           # 红色 - 30°
        self.COLOR_45 = "#2ecc71"           # 绿色 - 45°
        self.COLOR_60 = "#f39c12"           # 橙色 - 60°
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_30_degree_construction()
        self.show_30_degree_calculation()
        self.show_45_degree_construction()
        self.show_45_degree_calculation()
        self.show_60_degree_construction()
        self.show_60_degree_calculation()
        self.show_summary_table()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 基准参数
        self.SCALE = 1.2
        self.OFFSET = UP * 1.5
        
        # ===== 30°角 - 等边三角形的一半 =====
        self.side_30 = 2.0 * self.SCALE
        
        # 等边三角形顶点
        self.A_30 = np.array([-1, 0, 0]) * self.SCALE + self.OFFSET
        self.B_30 = np.array([1, 0, 0]) * self.SCALE + self.OFFSET
        self.C_30 = np.array([0, np.sqrt(3), 0]) * self.SCALE + self.OFFSET
        
        # AB的中点D (高线的垂足)
        self.D_30 = (self.A_30 + self.B_30) / 2
        
        # 验证计算
        self.height_30 = np.sqrt(3) * self.SCALE
        assert abs(np.linalg.norm(self.C_30 - self.D_30) - self.height_30) < 1e-6, "30°高线长度错误"
        
        # ===== 45°角 - 等腰直角三角形 =====
        self.leg_45 = np.sqrt(2) * self.SCALE
        
        # 等腰直角三角形顶点 (P为直角顶点)
        self.P_45 = np.array([0, 0, 0]) + self.OFFSET
        self.Q_45 = np.array([np.sqrt(2), 0, 0]) * self.SCALE + self.OFFSET
        self.R_45 = np.array([0, np.sqrt(2), 0]) * self.SCALE + self.OFFSET
        
        # 验证计算
        hypotenuse_45 = np.linalg.norm(self.Q_45 - self.R_45)
        expected_hypotenuse = 2 * self.SCALE
        assert abs(hypotenuse_45 - expected_hypotenuse) < 1e-6, "45°斜边长度错误"
        
        # ===== 60°角 - 使用30°的等边三角形 =====
        # 60°角在点A，对边是CD，邻边是AD
        # 与30°共用几何数据
        
        print("✓ 几何数据初始化完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "30°、45°、60°的三角比值",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        hook_question = Text(
            "你能记住吗?",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(hook_text), run_time=0.8)
        self.play(FadeIn(hook_question, shift=UP * 0.2), run_time=0.5)
        
        # 三个角度符号快闪
        angle_30_symbol = MathTex(r"30^\circ", font_size=60, color=self.COLOR_30).move_to(UP * 2)
        angle_45_symbol = MathTex(r"45^\circ", font_size=60, color=self.COLOR_45).move_to(ORIGIN)
        angle_60_symbol = MathTex(r"60^\circ", font_size=60, color=self.COLOR_60).move_to(DOWN * 2)
        
        angles_group = VGroup(angle_30_symbol, angle_45_symbol, angle_60_symbol)
        
        for angle in angles_group:
            self.play(FadeIn(angle, scale=0.5), run_time=0.2)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hook_question),
            FadeOut(angles_group),
            run_time=0.5
        )
    
    def show_30_degree_construction(self):
        """场景2: 30°角构造"""
        # 标题
        title = Text(
            "30° 角的推导",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_30
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "等边三角形的一半",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        
        # 绘制等边三角形ABC
        triangle_30 = Polygon(
            self.A_30, self.B_30, self.C_30,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_30), run_time=1.0)
        
        # 标注顶点
        label_A = Text("A", font="PingFang SC", font_size=20).next_to(self.A_30, DL, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=20).next_to(self.B_30, DR, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=20).next_to(self.C_30, UP, buff=0.15)
        
        self.play(Write(label_A), Write(label_B), Write(label_C), run_time=0.5)
        
        # 绘制高线CD
        altitude_CD = DashedLine(
            self.C_30, self.D_30,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        point_D = Dot(self.D_30, color=self.COLOR_AUXILIARY, radius=0.06)
        label_D = Text("D", font="PingFang SC", font_size=20).next_to(self.D_30, DOWN, buff=0.15)
        
        self.play(
            Create(altitude_CD),
            FadeIn(point_D),
            Write(label_D),
            run_time=0.8
        )
        
        # 添加直角符号
        right_angle = self.create_right_angle_mark(self.D_30, self.C_30, self.A_30, size=0.15)
        self.play(FadeIn(right_angle), run_time=0.3)
        
        # 标注边长
        label_AC = MathTex("2", font_size=24, color=YELLOW).next_to(
            (self.A_30 + self.C_30) / 2, LEFT, buff=0.1
        )
        label_AD = MathTex("1", font_size=24, color=YELLOW).next_to(
            (self.A_30 + self.D_30) / 2, DOWN, buff=0.1
        )
        label_CD = MathTex(r"\sqrt{3}", font_size=24, color=YELLOW).next_to(
            (self.C_30 + self.D_30) / 2, RIGHT, buff=0.1
        )
        
        self.play(
            Write(label_AC),
            Write(label_AD),
            Write(label_CD),
            run_time=1.0
        )
        
        # 高亮30°角 (在点C，等边三角形被高线分割后的角度)
        angle_30 = Angle.from_three_points(
            self.A_30, self.C_30, self.D_30,
            radius=0.4,
            color=self.COLOR_30
        )
        angle_label = MathTex(r"30^\circ", font_size=20, color=self.COLOR_30).next_to(
            self.C_30 + 0.3 * (self.A_30 - self.C_30) / np.linalg.norm(self.A_30 - self.C_30) + 0.3 * (self.D_30 - self.C_30) / np.linalg.norm(self.D_30 - self.C_30),
            LEFT,
            buff=0.05
        )
        
        self.play(Create(angle_30), Write(angle_label), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "等边三角形高线平分底边",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 保存元素供下一场景使用
        self.triangle_30_elements = VGroup(
            triangle_30, altitude_CD, point_D, right_angle,
            label_A, label_B, label_C, label_D,
            label_AC, label_AD, label_CD,
            angle_30, angle_label
        )
        
        # 清理标题和说明
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(explanation), run_time=0.4)
    
    def show_30_degree_calculation(self):
        """场景3: 30°角三角比计算"""
        # 标题
        title = Text(
            "30° 的三角比值",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_30
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 公式位置 (底部区域)
        formula_y_start = DOWN * 3.5
        formula_spacing = 0.8
        
        # sin30°
        # 修正：MathTex中不能有中文，需要分离
        sin_label = Text("sin 30° = 对边/斜边 = ", font="PingFang SC", font_size=20)
        sin_calc = MathTex(r"\frac{1}{2}", font_size=26)
        sin_group = VGroup(sin_label, sin_calc).arrange(RIGHT, buff=0.1).move_to(formula_y_start)
        
        self.play(Write(sin_group), run_time=0.8)
        
        # 高亮对边和斜边
        ad_highlight = Line(self.A_30, self.D_30, color=self.COLOR_30, stroke_width=5)
        ac_highlight = Line(self.A_30, self.C_30, color=self.COLOR_30, stroke_width=5)
        
        self.play(ShowPassingFlash(ad_highlight), ShowPassingFlash(ac_highlight), run_time=0.6)
        self.wait(0.3)
        
        # cos30°
        cos_label = Text("cos 30° = 邻边/斜边 = ", font="PingFang SC", font_size=20)
        cos_calc = MathTex(r"\frac{\sqrt{3}}{2}", font_size=26)
        cos_group = VGroup(cos_label, cos_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing
        )
        
        self.play(Write(cos_group), run_time=0.8)
        
        # 高亮邻边和斜边
        cd_highlight = DashedLine(self.C_30, self.D_30, color=self.COLOR_30, stroke_width=5)
        
        self.play(ShowPassingFlash(cd_highlight), ShowPassingFlash(ac_highlight), run_time=0.6)
        self.wait(0.3)
        
        # tan30°
        tan_label = Text("tan 30° = 对边/邻边 = ", font="PingFang SC", font_size=20)
        tan_calc = MathTex(r"\frac{\sqrt{3}}{3}", font_size=26)
        tan_group = VGroup(tan_label, tan_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing * 2
        )
        
        self.play(Write(tan_group), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sin_group),
            FadeOut(cos_group),
            FadeOut(tan_group),
            FadeOut(self.triangle_30_elements),
            run_time=0.6
        )
    
    def show_45_degree_construction(self):
        """场景4: 45°角构造"""
        # 标题
        title = Text(
            "45° 角的推导",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_45
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "等腰直角三角形",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        
        # 绘制等腰直角三角形PQR
        triangle_45 = Polygon(
            self.P_45, self.Q_45, self.R_45,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_45), run_time=1.0)
        
        # 标注顶点
        label_P = Text("P", font="PingFang SC", font_size=20).next_to(self.P_45, DL, buff=0.15)
        label_Q = Text("Q", font="PingFang SC", font_size=20).next_to(self.Q_45, DR, buff=0.15)
        label_R = Text("R", font="PingFang SC", font_size=20).next_to(self.R_45, UP, buff=0.15)
        
        self.play(Write(label_P), Write(label_Q), Write(label_R), run_time=0.5)
        
        # 添加直角符号 (在P点)
        right_angle_P = self.create_right_angle_mark(self.P_45, self.Q_45, self.R_45, size=0.15)
        self.play(FadeIn(right_angle_P), run_time=0.3)
        
        # 标注边长
        label_PQ = MathTex(r"\sqrt{2}", font_size=24, color=YELLOW).next_to(
            (self.P_45 + self.Q_45) / 2, DOWN, buff=0.1
        )
        label_PR = MathTex(r"\sqrt{2}", font_size=24, color=YELLOW).next_to(
            (self.P_45 + self.R_45) / 2, LEFT, buff=0.1
        )
        label_QR = MathTex("2", font_size=24, color=YELLOW).next_to(
            (self.Q_45 + self.R_45) / 2, UR, buff=0.1
        )
        
        self.play(
            Write(label_PQ),
            Write(label_PR),
            Write(label_QR),
            run_time=1.0
        )
        
        # 高亮45°角
        angle_45 = Angle.from_three_points(
            self.R_45, self.Q_45, self.P_45,
            radius=0.4,
            color=self.COLOR_45
        )
        angle_label = MathTex(r"45^\circ", font_size=20, color=self.COLOR_45).next_to(
            self.Q_45 + 0.5 * UP + 0.3 * LEFT,
            UP,
            buff=0
        )
        
        self.play(Create(angle_45), Write(angle_label), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "两条直角边相等",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 保存元素
        self.triangle_45_elements = VGroup(
            triangle_45, right_angle_P,
            label_P, label_Q, label_R,
            label_PQ, label_PR, label_QR,
            angle_45, angle_label
        )
        
        # 清理标题和说明
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(explanation), run_time=0.4)
    
    def show_45_degree_calculation(self):
        """场景5: 45°角三角比计算"""
        # 标题
        title = Text(
            "45° 的三角比值",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_45
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 公式位置
        formula_y_start = DOWN * 3.5
        formula_spacing = 0.8
        
        # sin45°
        sin_label = Text("sin 45° = ", font="PingFang SC", font_size=20)
        sin_calc = MathTex(r"\frac{\sqrt{2}}{2}", font_size=26)
        sin_group = VGroup(sin_label, sin_calc).arrange(RIGHT, buff=0.1).move_to(formula_y_start)
        
        self.play(Write(sin_group), run_time=0.8)
        
        # 高亮对边和斜边
        pr_highlight = Line(self.P_45, self.R_45, color=self.COLOR_45, stroke_width=5)
        qr_highlight = Line(self.Q_45, self.R_45, color=self.COLOR_45, stroke_width=5)
        
        self.play(ShowPassingFlash(pr_highlight), ShowPassingFlash(qr_highlight), run_time=0.6)
        self.wait(0.3)
        
        # cos45°
        cos_label = Text("cos 45° = ", font="PingFang SC", font_size=20)
        cos_calc = MathTex(r"\frac{\sqrt{2}}{2}", font_size=26)
        cos_group = VGroup(cos_label, cos_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing
        )
        
        self.play(Write(cos_group), run_time=0.8)
        
        # 高亮邻边和斜边
        pq_highlight = Line(self.P_45, self.Q_45, color=self.COLOR_45, stroke_width=5)
        
        self.play(ShowPassingFlash(pq_highlight), ShowPassingFlash(qr_highlight), run_time=0.6)
        self.wait(0.3)
        
        # tan45°
        tan_label = Text("tan 45° = ", font="PingFang SC", font_size=20)
        tan_calc = MathTex("1", font_size=26)
        tan_group = VGroup(tan_label, tan_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing * 2
        )
        
        self.play(Write(tan_group), run_time=0.8)
        
        # 强调tan45°=1
        self.play(Flash(tan_calc, color=self.COLOR_45), Indicate(tan_calc), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sin_group),
            FadeOut(cos_group),
            FadeOut(tan_group),
            FadeOut(self.triangle_45_elements),
            run_time=0.6
        )
    
    def show_60_degree_construction(self):
        """场景6: 60°角构造"""
        # 标题
        title = Text(
            "60° 角的推导",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_60
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "与30°互为余角",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.4)
        
        # 重新绘制等边三角形 (复用几何数据)
        triangle_60 = Polygon(
            self.A_30, self.B_30, self.C_30,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_60), run_time=1.0)
        
        # 绘制高线
        altitude_CD = DashedLine(
            self.C_30, self.D_30,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(altitude_CD), run_time=0.8)
        
        # 高亮60°角 (在点A，由AD和AC形成的角)
        angle_60 = Angle.from_three_points(
            self.D_30, self.A_30, self.C_30,
            radius=0.4,
            color=self.COLOR_60
        )
        angle_label = MathTex(r"60^\circ", font_size=20, color=self.COLOR_60).next_to(
            self.A_30 + 0.3 * (self.D_30 - self.A_30) / np.linalg.norm(self.D_30 - self.A_30) + 0.3 * (self.C_30 - self.A_30) / np.linalg.norm(self.C_30 - self.A_30),
            LEFT,
            buff=0.05
        )
        
        self.play(Create(angle_60), Write(angle_label), run_time=0.8)
        
        # 标注边长
        label_AD = MathTex("1", font_size=24, color=YELLOW).next_to(
            (self.A_30 + self.D_30) / 2, DOWN, buff=0.1
        )
        label_CD = MathTex(r"\sqrt{3}", font_size=24, color=YELLOW).next_to(
            (self.C_30 + self.D_30) / 2, RIGHT, buff=0.1
        )
        label_AC = MathTex("2", font_size=24, color=YELLOW).next_to(
            (self.A_30 + self.C_30) / 2, LEFT, buff=0.1
        )
        
        self.play(
            Write(label_AD),
            Write(label_CD),
            Write(label_AC),
            run_time=1.0
        )
        
        # 说明文字
        explanation = Text(
            "60°角的对边和邻边与30°互换",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 保存元素
        self.triangle_60_elements = VGroup(
            triangle_60, altitude_CD,
            label_AD, label_CD, label_AC,
            angle_60, angle_label
        )
        
        # 清理标题和说明
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(explanation), run_time=0.4)
    
    def show_60_degree_calculation(self):
        """场景7: 60°角三角比计算"""
        # 标题
        title = Text(
            "60° 的三角比值",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_60
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 公式位置
        formula_y_start = DOWN * 3.5
        formula_spacing = 0.8
        
        # sin60°
        sin_label = Text("sin 60° = ", font="PingFang SC", font_size=20)
        sin_calc = MathTex(r"\frac{\sqrt{3}}{2}", font_size=26)
        sin_group = VGroup(sin_label, sin_calc).arrange(RIGHT, buff=0.1).move_to(formula_y_start)
        
        self.play(Write(sin_group), run_time=0.8)
        
        # 高亮对边和斜边
        cd_highlight = DashedLine(self.C_30, self.D_30, color=self.COLOR_60, stroke_width=5)
        ac_highlight = Line(self.A_30, self.C_30, color=self.COLOR_60, stroke_width=5)
        
        self.play(ShowPassingFlash(cd_highlight), ShowPassingFlash(ac_highlight), run_time=0.6)
        self.wait(0.3)
        
        # cos60°
        cos_label = Text("cos 60° = ", font="PingFang SC", font_size=20)
        cos_calc = MathTex(r"\frac{1}{2}", font_size=26)
        cos_group = VGroup(cos_label, cos_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing
        )
        
        self.play(Write(cos_group), run_time=0.8)
        
        # 高亮邻边和斜边
        ad_highlight = Line(self.A_30, self.D_30, color=self.COLOR_60, stroke_width=5)
        
        self.play(ShowPassingFlash(ad_highlight), ShowPassingFlash(ac_highlight), run_time=0.6)
        self.wait(0.3)
        
        # tan60°
        tan_label = Text("tan 60° = ", font="PingFang SC", font_size=20)
        tan_calc = MathTex(r"\sqrt{3}", font_size=26)
        tan_group = VGroup(tan_label, tan_calc).arrange(RIGHT, buff=0.1).move_to(
            formula_y_start + DOWN * formula_spacing * 2
        )
        
        self.play(Write(tan_group), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sin_group),
            FadeOut(cos_group),
            FadeOut(tan_group),
            FadeOut(self.triangle_60_elements),
            run_time=0.6
        )
    
    def show_summary_table(self):
        """场景8: 汇总表格"""
        # 标题
        title = Text(
            "特殊角三角比值汇总",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 创建表格 - 使用 Table 类的 element_to_mobject 参数处理文本和公式
        from manim import Table, MathTex
        
        # 表头
        headers = ["角度", "sin", "cos", "tan"]
        
        # 数据 - 使用字符串 and let Table handle conversion
        table_raw_data = [
            headers,
            [r"30^\circ", r"\frac{1}{2}", r"\frac{\sqrt{3}}{2}", r"\frac{\sqrt{3}}{3}"],
            [r"45^\circ", r"\frac{\sqrt{2}}{2}", r"\frac{\sqrt{2}}{2}", "1"],
            [r"60^\circ", r"\frac{\sqrt{3}}{2}", r"\frac{1}{2}", r"\sqrt{3}"],
        ]
        
        # 自定义元素转换函数
        def element_to_mobject(element):
            # 如果包含LaTeX特殊字符，使用MathTex，否则使用Text
            if any(char in element for char in ['^', '_', '\\', '{', '}']) and ('\\' in element or '^' in element or '_' in element):
                return MathTex(element, font_size=24)
            elif element == "角度":
                return Text(element, font="PingFang SC", font_size=24)
            else:
                return MathTex(element, font_size=24)
        
        table = Table(
            table_raw_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": WHITE},
            element_to_mobject=element_to_mobject
        ).scale(0.7).move_to(UP * 1.5)
        
        # 表格框架
        self.play(Create(table), run_time=1.0)
        
        # 逐行填充数据
        self.wait(0.4)
        
        # 高亮特殊规律
        # sin30° = cos60°
        sin_30_cell = table.get_entries((2, 2))  # 第2行第2列
        cos_60_cell = table.get_entries((4, 3))  # 第4行第3列
        
        self.play(
            Indicate(sin_30_cell, color=self.COLOR_HIGHLIGHT),
            Indicate(cos_60_cell, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 记忆提示
        tip_1 = Text(
            "sin和cos互换: sin30°=cos60°",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        tip_2 = Text(
            "45°的sin和cos相等",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.2)
        
        tip_3 = Text(
            "tan45°=1 最好记!",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.9)
        
        self.play(FadeIn(tip_1), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(tip_2), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(tip_3), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(table),
            FadeOut(tip_1),
            FadeOut(tip_2),
            FadeOut(tip_3),
            run_time=0.5
        )
    
    def show_outro(self):
        """场景9: 片尾关注"""
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
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三角形装饰
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
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
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


# 运行命令:
# manim -pql special_angle_trigonometry.py SpecialAngleTrigonometry  # 快速预览
# manim -qh special_angle_trigonometry.py SpecialAngleTrigonometry   # 高质量渲染