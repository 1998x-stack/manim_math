"""
余角与补角 - Complementary and Supplementary Angles
使用 Manim 创建的六年级几何教学视频

内容: 余角(α+β=90°)和补角(α+β=180°)的定义、实例和性质
目标观众: 六年级学生
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


class ComplementarySupplementaryAngles(Scene):
    """
    余角与补角教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引起注意
    2. 余角定义 - α + β = 90°
    3. 余角实例 - 30° + 60°
    4. 补角定义 - α + β = 180°
    5. 补角实例 - 120° + 60°
    6. 性质总结 - 重要性质
    7. 结尾关注 - 总结 + 关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_COMPLEMENTARY = "#3498db"    # 蓝色 - 余角
        self.COLOR_SUPPLEMENTARY = "#e74c3c"    # 红色 - 补角
        self.COLOR_RIGHT_ANGLE = "#2ecc71"      # 绿色 - 直角
        self.COLOR_STRAIGHT_ANGLE = "#f39c12"   # 橙色 - 平角
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 36
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 22
        self.FONT_SIZE_SMALL = 18
        
        # 作者信息 (全程保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_complementary_definition()
        self.show_complementary_example()
        self.show_supplementary_definition()
        self.show_supplementary_example()
        self.show_properties()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ===== 余角场景几何 =====
        self.O_comp = ORIGIN + UP * 1.5  # 余角顶点
        
        # 余角的角度设置
        self.alpha_angle_comp = 30 * DEGREES  # 30度
        self.beta_angle_comp = 60 * DEGREES   # 60度
        
        # 验证余角和为90度
        assert abs((self.alpha_angle_comp + self.beta_angle_comp) - PI/2) < 1e-6, \
            "余角和必须为90度!"
        
        # 射线端点（精确计算）
        self.A_comp = self.O_comp + RIGHT * 2.5  # 水平向右
        self.B_comp = self.O_comp + np.array([
            2.5 * np.cos(self.alpha_angle_comp),
            2.5 * np.sin(self.alpha_angle_comp),
            0
        ])
        self.C_comp = self.O_comp + UP * 2.5  # 垂直向上（确保90度）
        
        # 弧的半径
        self.arc_radius_alpha_comp = 0.8
        self.arc_radius_beta_comp = 1.2
        
        # ===== 补角场景几何 =====
        self.O_supp = ORIGIN + UP * 1.5  # 补角顶点
        
        # 补角的角度设置
        self.alpha_angle_supp = 120 * DEGREES  # 120度
        self.beta_angle_supp = 60 * DEGREES    # 60度
        
        # 验证补角和为180度
        assert abs((self.alpha_angle_supp + self.beta_angle_supp) - PI) < 1e-6, \
            "补角和必须为180度!"
        
        # 射线端点（精确计算）
        self.A_supp = self.O_supp + LEFT * 3   # 平角左端
        self.B_supp = self.O_supp + RIGHT * 3  # 平角右端
        self.C_supp = self.O_supp + np.array([
            2.5 * np.cos(self.alpha_angle_supp),
            2.5 * np.sin(self.alpha_angle_supp),
            0
        ])
        
        # 弧的半径
        self.arc_radius_alpha_supp = 0.9
        self.arc_radius_beta_supp = 1.3
        
        print("✓ 几何验证完成")
    
    def create_right_angle_mark(self, corner, p1, p2, size=0.2, color=None):
        """创建直角标记（小方块）"""
        if color is None:
            color = self.COLOR_RIGHT_ANGLE
        
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        
        square = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=2,
            fill_opacity=0
        )
        return square
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息淡入
        self.play(FadeIn(self.author_info, shift=DOWN*0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "两个角相加会怎样?",
            font=self.FONT_CHINESE,
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 创建两个神秘角度
        angle1_center = LEFT * 1.5 + UP * 2
        angle2_center = RIGHT * 1.5 + UP * 2
        
        # 角1: 30度
        line1_1 = Line(angle1_center, angle1_center + RIGHT * 1.5, color=WHITE, stroke_width=3)
        line1_2 = Line(
            angle1_center,
            angle1_center + np.array([1.5 * np.cos(30*DEGREES), 1.5 * np.sin(30*DEGREES), 0]),
            color=WHITE,
            stroke_width=3
        )
        arc1 = Arc(
            radius=0.6,
            start_angle=0,
            angle=30*DEGREES,
            color=self.COLOR_COMPLEMENTARY,
            stroke_width=3,
            arc_center=angle1_center
        )
        label1 = MathTex(r"30^\circ", font_size=28, color=WHITE).next_to(arc1, RIGHT, buff=0.15)
        angle1_group = VGroup(line1_1, line1_2, arc1, label1)
        
        # 角2: 60度
        line2_1 = Line(angle2_center, angle2_center + RIGHT * 1.5, color=WHITE, stroke_width=3)
        line2_2 = Line(
            angle2_center,
            angle2_center + np.array([1.5 * np.cos(60*DEGREES), 1.5 * np.sin(60*DEGREES), 0]),
            color=WHITE,
            stroke_width=3
        )
        arc2 = Arc(
            radius=0.6,
            start_angle=0,
            angle=60*DEGREES,
            color=self.COLOR_COMPLEMENTARY,
            stroke_width=3,
            arc_center=angle2_center
        )
        label2 = MathTex(r"60^\circ", font_size=28, color=WHITE).next_to(arc2, RIGHT, buff=0.15)
        angle2_group = VGroup(line2_1, line2_2, arc2, label2)
        
        # 角度闪现
        self.play(
            Create(angle1_group),
            Create(angle2_group),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 角度闪烁
        self.play(
            Flash(arc1, color=self.COLOR_COMPLEMENTARY, flash_radius=0.4),
            Flash(arc2, color=self.COLOR_COMPLEMENTARY, flash_radius=0.4),
            run_time=0.7
        )
        
        # 提示文字
        hint = Text(
            "竟然有特殊名称?",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint, shift=UP*0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(angle1_group),
            FadeOut(angle2_group),
            FadeOut(hint),
            run_time=0.6
        )
    
    def show_complementary_definition(self):
        """场景2: 余角定义"""
        # 标题
        title = Text(
            "余角 Complementary Angles",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_COMPLEMENTARY
        ).move_to(UP * 5.5)
        
        # 定义
        definition = Text(
            "两角之和等于90°",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.6)
        
        # 绘制射线OA（水平向右）
        ray_OA = Line(self.O_comp, self.A_comp, color=WHITE, stroke_width=3)
        self.play(Create(ray_OA), run_time=0.5)
        
        # 绘制射线OB（旋转30度）
        ray_OB = Line(self.O_comp, self.B_comp, color=WHITE, stroke_width=3)
        self.play(Create(ray_OB), run_time=0.5)
        
        # 绘制角α的弧
        arc_alpha = Arc(
            radius=self.arc_radius_alpha_comp,
            start_angle=0,
            angle=self.alpha_angle_comp,
            color=self.COLOR_COMPLEMENTARY,
            stroke_width=3,
            arc_center=self.O_comp
        )
        self.play(Create(arc_alpha), run_time=0.5)
        
        # 标注α
        label_alpha = MathTex(r"\alpha", font_size=32, color=WHITE).move_to(
            self.O_comp + np.array([1.2, 0.3, 0])
        )
        self.play(FadeIn(label_alpha), run_time=0.3)
        
        # 绘制射线OC（垂直向上）
        ray_OC = Line(self.O_comp, self.C_comp, color=WHITE, stroke_width=3)
        self.play(Create(ray_OC), run_time=0.5)
        
        # 绘制角β的弧
        arc_beta = Arc(
            radius=self.arc_radius_beta_comp,
            start_angle=self.alpha_angle_comp,
            angle=self.beta_angle_comp,
            color=self.COLOR_COMPLEMENTARY,
            stroke_width=3,
            arc_center=self.O_comp
        )
        self.play(Create(arc_beta), run_time=0.5)
        
        # 标注β
        label_beta = MathTex(r"\beta", font_size=32, color=WHITE).move_to(
            self.O_comp + np.array([0.5, 1.5, 0])
        )
        self.play(FadeIn(label_beta), run_time=0.3)
        
        # 直角标记
        right_angle_mark = self.create_right_angle_mark(
            self.O_comp, self.A_comp, self.C_comp, size=0.25
        )
        self.play(FadeIn(right_angle_mark), run_time=0.4)
        
        # 公式
        formula1 = MathTex(
            r"\alpha", r"+", r"\beta", r"=", r"90^\circ",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3.5)
        formula1[0].set_color(self.COLOR_COMPLEMENTARY)
        formula1[2].set_color(self.COLOR_COMPLEMENTARY)
        formula1[4].set_color(self.COLOR_RIGHT_ANGLE)
        
        self.play(Write(formula1), run_time=1.0)
        self.wait(1.5)
        
        # 清理（保留图形但移除文字）
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 保存元素以便下一场景使用
        self.comp_elements = VGroup(
            ray_OA, ray_OB, ray_OC,
            arc_alpha, arc_beta,
            label_alpha, label_beta,
            right_angle_mark,
            formula1
        )
    
    def show_complementary_example(self):
        """场景3: 余角实例"""
        # 说明文字
        example_text = Text(
            "举个例子",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(example_text, shift=DOWN*0.3), run_time=0.5)
        
        # 标注具体度数
        angle_30 = MathTex(r"30^\circ", font_size=36, color=YELLOW).move_to(
            self.O_comp + np.array([1.3, 0.2, 0])
        )
        angle_60 = MathTex(r"60^\circ", font_size=36, color=YELLOW).move_to(
            self.O_comp + np.array([0.6, 1.7, 0])
        )
        
        self.play(FadeIn(angle_30), FadeIn(angle_60), run_time=0.7)
        
        # 计算式
        calc = MathTex(
            r"30^\circ", r"+", r"60^\circ", r"=", r"90^\circ",
            font_size=38,
            color=WHITE
        ).move_to(DOWN * 4.5)
        calc[0].set_color(YELLOW)
        calc[2].set_color(YELLOW)
        calc[4].set_color(self.COLOR_RIGHT_ANGLE)
        
        self.play(Write(calc), run_time=0.8)
        
        # 高亮显示角α
        arc_alpha = self.comp_elements[3]
        self.play(arc_alpha.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(arc_alpha.animate.set_color(self.COLOR_COMPLEMENTARY), run_time=0.3)
        
        # 高亮显示角β
        arc_beta = self.comp_elements[4]
        self.play(arc_beta.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(arc_beta.animate.set_color(self.COLOR_COMPLEMENTARY), run_time=0.3)
        
        # 结论 - 使用 Text 和 MathTex 组合，避免中文在 MathTex 中
        conclusion_text = VGroup(
            MathTex(r"\therefore \ 30^\circ", font_size=28, color=WHITE),
            Text("与", font=self.FONT_CHINESE, font_size=24, color=WHITE),
            MathTex(r"60^\circ", font_size=28, color=WHITE),
            Text("互为余角", font=self.FONT_CHINESE, font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.8)
        
        self.play(FadeIn(conclusion_text), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_text),
            FadeOut(angle_30),
            FadeOut(angle_60),
            FadeOut(calc),
            FadeOut(conclusion_text),
            FadeOut(self.comp_elements),
            run_time=0.6
        )
    
    def show_supplementary_definition(self):
        """场景4: 补角定义"""
        # 标题
        title = Text(
            "补角 Supplementary Angles",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_SUPPLEMENTARY
        ).move_to(UP * 5.5)
        
        # 定义
        definition = Text(
            "两角之和等于180°",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(definition), run_time=0.6)
        
        # 绘制基准线（平角）
        base_line = Line(self.A_supp, self.B_supp, color=WHITE, stroke_width=3)
        self.play(Create(base_line), run_time=0.6)
        
        # 绘制射线OC
        ray_OC_supp = Line(self.O_supp, self.C_supp, color=WHITE, stroke_width=3)
        self.play(Create(ray_OC_supp), run_time=0.5)
        
        # 绘制角α的弧（120度）
        arc_alpha_supp = Arc(
            radius=self.arc_radius_alpha_supp,
            start_angle=PI,  # 从左边开始
            angle=self.alpha_angle_supp,
            color=self.COLOR_SUPPLEMENTARY,
            stroke_width=3,
            arc_center=self.O_supp
        )
        self.play(Create(arc_alpha_supp), run_time=0.5)
        
        # 标注α
        label_alpha_supp = MathTex(r"\alpha", font_size=32, color=WHITE).move_to(
            self.O_supp + np.array([-1.2, 0.8, 0])
        )
        self.play(FadeIn(label_alpha_supp), run_time=0.3)
        
        # 绘制角β的弧（60度）
        arc_beta_supp = Arc(
            radius=self.arc_radius_beta_supp,
            start_angle=self.alpha_angle_supp + PI,
            angle=self.beta_angle_supp,
            color=self.COLOR_SUPPLEMENTARY,
            stroke_width=3,
            arc_center=self.O_supp
        )
        self.play(Create(arc_beta_supp), run_time=0.5)
        
        # 标注β
        label_beta_supp = MathTex(r"\beta", font_size=32, color=WHITE).move_to(
            self.O_supp + np.array([1.5, 0.5, 0])
        )
        self.play(FadeIn(label_beta_supp), run_time=0.3)
        
        # 平角标注（双箭头）
        straight_angle_mark = DoubleArrow(
            self.A_supp + DOWN*0.3,
            self.B_supp + DOWN*0.3,
            color=self.COLOR_STRAIGHT_ANGLE,
            stroke_width=3,
            buff=0,
            max_tip_length_to_length_ratio=0.08
        )
        straight_label = MathTex(r"180^\circ", font_size=24, color=self.COLOR_STRAIGHT_ANGLE).next_to(
            straight_angle_mark, DOWN, buff=0.1
        )
        
        self.play(FadeIn(straight_angle_mark), FadeIn(straight_label), run_time=0.4)
        
        # 公式
        formula2 = MathTex(
            r"\alpha", r"+", r"\beta", r"=", r"180^\circ",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 4.5)
        formula2[0].set_color(self.COLOR_SUPPLEMENTARY)
        formula2[2].set_color(self.COLOR_SUPPLEMENTARY)
        formula2[4].set_color(self.COLOR_STRAIGHT_ANGLE)
        
        self.play(Write(formula2), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 保存元素
        self.supp_elements = VGroup(
            base_line, ray_OC_supp,
            arc_alpha_supp, arc_beta_supp,
            label_alpha_supp, label_beta_supp,
            straight_angle_mark, straight_label,
            formula2
        )
    
    def show_supplementary_example(self):
        """场景5: 补角实例"""
        # 说明文字
        example_text = Text(
            "举个例子",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(example_text, shift=DOWN*0.3), run_time=0.5)
        
        # 标注具体度数
        angle_120 = MathTex(r"120^\circ", font_size=36, color=YELLOW).move_to(
            self.O_supp + np.array([-1.3, 0.7, 0])
        )
        angle_60 = MathTex(r"60^\circ", font_size=36, color=YELLOW).move_to(
            self.O_supp + np.array([1.6, 0.4, 0])
        )
        
        self.play(FadeIn(angle_120), FadeIn(angle_60), run_time=0.7)
        
        # 计算式
        calc = MathTex(
            r"120^\circ", r"+", r"60^\circ", r"=", r"180^\circ",
            font_size=38,
            color=WHITE
        ).move_to(DOWN * 5.5)
        calc[0].set_color(YELLOW)
        calc[2].set_color(YELLOW)
        calc[4].set_color(self.COLOR_STRAIGHT_ANGLE)
        
        self.play(Write(calc), run_time=0.8)
        
        # 高亮显示角α
        arc_alpha = self.supp_elements[2]
        self.play(arc_alpha.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(arc_alpha.animate.set_color(self.COLOR_SUPPLEMENTARY), run_time=0.3)
        
        # 高亮显示角β
        arc_beta = self.supp_elements[3]
        self.play(arc_beta.animate.set_color(YELLOW), run_time=0.5)
        self.wait(0.3)
        self.play(arc_beta.animate.set_color(self.COLOR_SUPPLEMENTARY), run_time=0.3)
        
        # 结论
        conclusion_text = VGroup(
            MathTex(r"\therefore \ 120^\circ", font_size=28, color=WHITE),
            Text("与", font=self.FONT_CHINESE, font_size=24, color=WHITE),
            MathTex(r"60^\circ", font_size=28, color=WHITE),
            Text("互为补角", font=self.FONT_CHINESE, font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 6.5)
        
        self.play(FadeIn(conclusion_text), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_text),
            FadeOut(angle_120),
            FadeOut(angle_60),
            FadeOut(calc),
            FadeOut(conclusion_text),
            FadeOut(self.supp_elements),
            run_time=0.6
        )
    
    def show_properties(self):
        """场景6: 性质总结"""
        # 标题
        property_title = Text(
            "重要性质",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(property_title), run_time=0.6)
        
        # 性质1卡片
        property1_title = Text(
            "性质1",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_COMPLEMENTARY
        )
        property1_content = Text(
            "同角(或等角)的\n余角相等",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        )
        property1_card = VGroup(property1_title, property1_content).arrange(DOWN, buff=0.3)
        property1_card.move_to(UP * 4)
        
        # 性质1图示
        diagram1_center = UP * 1.5
        
        # α角
        alpha_line1 = Line(diagram1_center, diagram1_center + RIGHT*1, color=GRAY_B, stroke_width=2)
        alpha_line2 = Line(diagram1_center, diagram1_center + np.array([0.8, 0.5, 0]), color=GRAY_B, stroke_width=2)
        alpha_arc = Arc(0.4, 0, 30*DEGREES, color=YELLOW, stroke_width=2, arc_center=diagram1_center)
        alpha_label = MathTex(r"\alpha", font_size=20).move_to(diagram1_center + np.array([0.6, 0.15, 0]))
        
        # β1角
        beta1_center = diagram1_center + LEFT * 2
        beta1_line1 = Line(beta1_center, beta1_center + np.array([0.8, 0.5, 0]), color=self.COLOR_COMPLEMENTARY, stroke_width=2)
        beta1_line2 = Line(beta1_center, beta1_center + UP, color=self.COLOR_COMPLEMENTARY, stroke_width=2)
        beta1_arc = Arc(0.5, 30*DEGREES, 60*DEGREES, color=self.COLOR_COMPLEMENTARY, stroke_width=2, arc_center=beta1_center)
        beta1_label = MathTex(r"\beta_1", font_size=20).move_to(beta1_center + np.array([0.3, 0.6, 0]))
        
        # β2角
        beta2_center = diagram1_center + RIGHT * 2
        beta2_line1 = Line(beta2_center, beta2_center + np.array([0.8, 0.5, 0]), color=self.COLOR_COMPLEMENTARY, stroke_width=2)
        beta2_line2 = Line(beta2_center, beta2_center + UP, color=self.COLOR_COMPLEMENTARY, stroke_width=2)
        beta2_arc = Arc(0.5, 30*DEGREES, 60*DEGREES, color=self.COLOR_COMPLEMENTARY, stroke_width=2, arc_center=beta2_center)
        beta2_label = MathTex(r"\beta_2", font_size=20).move_to(beta2_center + np.array([0.3, 0.6, 0]))
        
        diagram1 = VGroup(
            alpha_line1, alpha_line2, alpha_arc, alpha_label,
            beta1_line1, beta1_line2, beta1_arc, beta1_label,
            beta2_line1, beta2_line2, beta2_arc, beta2_label
        )
        
        # 等号
        equals1 = MathTex(r"\beta_1 = \beta_2", font_size=24, color=self.COLOR_COMPLEMENTARY).move_to(UP * 0.2)
        
        self.play(FadeIn(property1_card, shift=LEFT*0.3), run_time=0.8)
        self.play(Create(diagram1), run_time=1.2)
        self.play(Write(equals1), run_time=0.5)
        self.wait(1.0)
        
        # 性质2卡片
        property2_title = Text(
            "性质2",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_SUPPLEMENTARY
        )
        property2_content = Text(
            "同角(或等角)的\n补角相等",
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        )
        property2_card = VGroup(property2_title, property2_content).arrange(DOWN, buff=0.3)
        property2_card.move_to(DOWN * 1.5)
        
        # 性质2图示
        diagram2_center = DOWN * 3.5
        
        # α角（与上面相同）
        alpha2_line1 = Line(diagram2_center + LEFT*1.2, diagram2_center + RIGHT*1.2, color=GRAY_B, stroke_width=2)
        alpha2_line2 = Line(diagram2_center, diagram2_center + np.array([-0.8, 0.6, 0]), color=GRAY_B, stroke_width=2)
        alpha2_arc = Arc(0.4, PI, 120*DEGREES, color=YELLOW, stroke_width=2, arc_center=diagram2_center)
        alpha2_label = MathTex(r"\alpha", font_size=20).move_to(diagram2_center + np.array([-0.5, 0.3, 0]))
        
        # β角
        beta2_arc_supp = Arc(0.5, 120*DEGREES+PI, 60*DEGREES, color=self.COLOR_SUPPLEMENTARY, stroke_width=2, arc_center=diagram2_center)
        beta2_label_supp = MathTex(r"\beta", font_size=20).move_to(diagram2_center + np.array([0.5, 0.4, 0]))
        
        diagram2 = VGroup(
            alpha2_line1, alpha2_line2, alpha2_arc, alpha2_label,
            beta2_arc_supp, beta2_label_supp
        )
        
        # 说明
        equals2_text = VGroup(
            Text("若", font=self.FONT_CHINESE, font_size=20, color=WHITE),
            MathTex(r"\alpha", font_size=20, color=WHITE),
            Text("相同", font=self.FONT_CHINESE, font_size=20, color=WHITE),
            Text("则", font=self.FONT_CHINESE, font_size=20, color=WHITE),
            MathTex(r"\beta", font_size=20, color=WHITE),
            Text("相等", font=self.FONT_CHINESE, font_size=20, color=WHITE)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property2_card, shift=LEFT*0.3), run_time=0.8)
        self.play(Create(diagram2), run_time=1.0)
        self.play(FadeIn(equals2_text), run_time=0.5)
        self.wait(1.0)
        
        # 强调文字
        emphasis = Text(
            "必须掌握!",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.8)
        
        self.play(FadeIn(emphasis, scale=1.2), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(property_title),
            FadeOut(property1_card),
            FadeOut(diagram1),
            FadeOut(equals1),
            FadeOut(property2_card),
            FadeOut(diagram2),
            FadeOut(equals2_text),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 结尾关注"""
        # 核心公式回顾
        formula_comp = MathTex(
            r"\alpha + \beta = 90^\circ",
            font_size=38,
            color=self.COLOR_COMPLEMENTARY
        ).move_to(UP * 3)
        
        formula_supp = MathTex(
            r"\alpha + \beta = 180^\circ",
            font_size=38,
            color=self.COLOR_SUPPLEMENTARY
        ).move_to(UP * 1.5)
        
        formulas = VGroup(formula_comp, formula_supp)
        
        self.play(FadeIn(formulas, shift=DOWN*0.5), run_time=0.8)
        self.wait(0.3)
        
        # 公式闪烁
        self.play(Indicate(formulas, scale_factor=1.1), run_time=0.8)
        
        # 作者信息放大并移到中心
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=38,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=30,
            color=GRAY_B
        ).move_to(DOWN * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP*0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我,获得更多数学技巧!",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)
        
        # 装饰元素（6个角图标）
        decorations = VGroup()
        for i in range(6):
            angle_val = 30 if i % 2 == 0 else 60
            color = self.COLOR_COMPLEMENTARY if i % 2 == 0 else self.COLOR_SUPPLEMENTARY
            
            center = follow_text.get_center() + 2.2 * np.array([
                np.cos(i * PI / 3),
                np.sin(i * PI / 3),
                0
            ])
            
            # 简单的角图标
            line1 = Line(center, center + RIGHT*0.3, color=color, stroke_width=2)
            line2 = Line(center, center + np.array([0.3*np.cos(angle_val*DEGREES), 0.3*np.sin(angle_val*DEGREES), 0]), color=color, stroke_width=2)
            arc = Arc(0.15, 0, angle_val*DEGREES, color=color, stroke_width=2, arc_center=center)
            
            icon = VGroup(line1, line2, arc)
            decorations.add(icon)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in decorations],
            run_time=0.6
        )
        
        # 旋转装饰
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(formulas),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 渲染命令:
# manim -pql complementary_supplementary.py ComplementarySupplementaryAngles  # 快速预览
# manim -qh complementary_supplementary.py ComplementarySupplementaryAngles   # 高质量渲染