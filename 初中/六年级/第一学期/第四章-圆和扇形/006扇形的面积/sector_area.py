"""
扇形的面积 - Sector Area Animation
使用 Manim 创建的六年级数学教学视频

内容: 扇形的定义、圆心角、面积公式推导 (两种形式)、实例计算
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


class SectorAreaAnimation(Scene):
    """
    扇形面积教学动画场景
    
    场景顺序:
    1. 开场钩子 (披萨问题)
    2. 认识扇形 (定义、组成)
    3. 圆心角概念 (角度与面积关系)
    4. 面积公式推导 - 第一形式 S=(nπr²)/360
    5. 面积公式推导 - 第二形式 S=(1/2)lr
    6. 实例计算 (具体数字演示)
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"        # 蓝色 - 圆
        self.COLOR_SECTOR = "#e74c3c"        # 红色 - 扇形
        self.COLOR_RADIUS = "#2ecc71"        # 绿色 - 半径
        self.COLOR_ARC = "#f39c12"           # 橙色 - 弧
        self.COLOR_ANGLE = "#9b59b6"         # 紫色 - 角度
        self.COLOR_FORMULA = YELLOW          # 黄色 - 公式
        self.COLOR_HIGHLIGHT = GOLD          # 金色 - 强调
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_central_angle()
        self.scene_4_formula_one()
        self.scene_5_formula_two()
        self.scene_6_example()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # 主几何参数
        self.center = UP * 1.5
        self.radius = 2.0
        self.angle = 90 * DEGREES  # 主示例使用90度
        
        # 计算关键点
        self.O = self.center
        self.A = self.center + self.radius * RIGHT
        self.B = self.center + self.radius * np.array([
            np.cos(self.angle),
            np.sin(self.angle),
            0
        ])
        
        # 圆弧中点 (用于标注)
        mid_angle = self.angle / 2
        self.arc_mid = self.center + (self.radius + 0.4) * np.array([
            np.cos(mid_angle),
            np.sin(mid_angle),
            0
        ])
        
        # 计算弧长和面积 (用于验证)
        self.arc_length = (self.angle / TAU) * (2 * PI * self.radius)
        self.sector_area = (self.angle / TAU) * (PI * self.radius ** 2)
        
        print(f"✓ 几何初始化完成:")
        print(f"  圆心: {self.O}")
        print(f"  半径: {self.radius}")
        print(f"  角度: {self.angle / DEGREES}")
        print(f"  弧长: {self.arc_length:.4f}")
        print(f"  面积: {self.sector_area:.4f}")
    
    def scene_1_opening(self):
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
            "披萨切一块，面积怎么算?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 披萨扇形 (大角度，120度)
        pizza_center = UP * 2.5
        pizza_radius = 1.8
        pizza_angle = 120 * DEGREES
        
        pizza_sector = Sector(
            radius=pizza_radius,
            angle=pizza_angle,
            start_angle=-pizza_angle/2,  # 居中对称
            arc_center=pizza_center,
            color=self.COLOR_SECTOR,
            fill_opacity=0.4,
            stroke_width=3
        )
        
        # 披萨装饰线 (芝士效果)
        cheese_lines = VGroup(*[
            Line(
                pizza_center,
                pizza_center + pizza_radius * np.array([
                    np.cos(-pizza_angle/2 + i * pizza_angle / 5),
                    np.sin(-pizza_angle/2 + i * pizza_angle / 5),
                    0
                ]),
                color=YELLOW,
                stroke_width=1.5
            )
            for i in range(6)
        ])
        
        self.play(
            Create(pizza_sector),
            Create(cheese_lines),
            run_time=1.0
        )
        
        self.play(
            Flash(pizza_sector, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 过渡文字
        transition = Text(
            "这就是扇形!",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(pizza_sector),
            FadeOut(cheese_lines),
            FadeOut(transition),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 认识扇形"""
        # 标题
        title = Text(
            "什么是扇形?",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 绘制完整的圆
        circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=2,
            stroke_opacity=0.5
        ).move_to(self.center)
        
        self.play(Create(circle), run_time=1.2)
        
        # 标记圆心O
        dot_O = Dot(self.O, radius=0.08, color=WHITE)
        label_O = Text("O", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_O, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dot_O, scale=0.5),
            FadeIn(label_O),
            run_time=0.5
        )
        
        # 绘制半径OA
        radius_1 = Line(
            self.O,
            self.A,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        self.play(Create(radius_1), run_time=0.6)
        
        # 标注点A
        dot_A = Dot(self.A, radius=0.08, color=self.COLOR_RADIUS)
        label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_A, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(label_A),
            run_time=0.3
        )
        
        # 绘制半径OB
        radius_2 = Line(
            self.O,
            self.B,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        self.play(Create(radius_2), run_time=0.6)
        
        # 标注点B
        dot_B = Dot(self.B, radius=0.08, color=self.COLOR_RADIUS)
        label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_B, UP + LEFT, buff=0.15)
        
        self.play(
            FadeIn(dot_B, scale=0.5),
            FadeIn(label_B),
            run_time=0.3
        )
        
        # 高亮圆弧AB
        arc = Arc(
            radius=self.radius,
            start_angle=0,
            angle=self.angle,
            arc_center=self.center,
            color=self.COLOR_ARC,
            stroke_width=6
        )
        
        self.play(Create(arc), run_time=0.8)
        
        # 扇形填充
        sector_fill = Sector(
            radius=self.radius,
            angle=self.angle,
            start_angle=0,
            arc_center=self.center,
            color=self.COLOR_SECTOR,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(FadeIn(sector_fill), run_time=0.6)
        
        # 定义文字
        definition = Text(
            "两条半径 + 圆弧 = 扇形",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        self.wait(1.0)
        
        # 清理 (保留核心元素)
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.4
        )
        
        # 存储元素供后续使用
        self.circle = circle
        self.sector_fill = sector_fill
        self.radius_1 = radius_1
        self.radius_2 = radius_2
        self.arc = arc
        self.dot_O = dot_O
        self.label_O = label_O
        self.dot_A = dot_A
        self.label_A = label_A
        self.dot_B = dot_B
        self.label_B = label_B
    
    def scene_3_central_angle(self):
        """场景3: 圆心角概念"""
        # 标题
        title = Text(
            "圆心角",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ANGLE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 角度弧线标记
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=self.angle,
            arc_center=self.center,
            color=self.COLOR_ANGLE,
            stroke_width=3
        )
        
        self.play(Create(angle_arc), run_time=0.6)
        
        # 角度标注
        angle_label = MathTex(
            r"n",  # 修复：去掉度数符号
            font_size=32,
            color=self.COLOR_ANGLE
        ).move_to(
            self.center + 0.9 * np.array([
                np.cos(self.angle / 2),
                np.sin(self.angle / 2),
                0
            ])
        )
        
        self.play(Write(angle_label), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "圆心角决定扇形大小",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        # 演示不同角度
        angles_demo = [60, 120, 180, 90]  # 最后回到90度
        
        for target_angle_deg in angles_demo:
            target_angle = target_angle_deg * DEGREES
            
            # 目标点B
            target_B = self.center + self.radius * np.array([
                np.cos(target_angle),
                np.sin(target_angle),
                0
            ])
            
            # 创建目标元素
            target_sector = Sector(
                radius=self.radius,
                angle=target_angle,
                start_angle=0,
                arc_center=self.center,
                color=self.COLOR_SECTOR,
                fill_opacity=0.3,
                stroke_width=0
            )
            
            target_arc = Arc(
                radius=self.radius,
                start_angle=0,
                angle=target_angle,
                arc_center=self.center,
                color=self.COLOR_ARC,
                stroke_width=6
            )
            
            target_radius_2 = Line(
                self.O,
                target_B,
                color=self.COLOR_RADIUS,
                stroke_width=4
            )
            
            target_angle_arc = Arc(
                radius=0.6,
                start_angle=0,
                angle=target_angle,
                arc_center=self.center,
                color=self.COLOR_ANGLE,
                stroke_width=3
            )
            
            target_angle_label = MathTex(
                f"{target_angle_deg}",
                font_size=32,
                color=self.COLOR_ANGLE
            ).move_to(
                self.center + 0.9 * np.array([
                    np.cos(target_angle / 2),
                    np.sin(target_angle / 2),
                    0
                ])
            )
            
            # 动画变换
            self.play(
                Transform(self.sector_fill, target_sector),
                Transform(self.arc, target_arc),
                Transform(self.radius_2, target_radius_2),
                Transform(self.dot_B, Dot(target_B, radius=0.08, color=self.COLOR_RADIUS)),
                Transform(self.label_B, Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(target_B, UP + LEFT, buff=0.15)),
                Transform(angle_arc, target_angle_arc),
                Transform(angle_label, target_angle_label),
                run_time=0.8
            )
            
            if target_angle_deg != 90:
                self.wait(0.2)
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            run_time=0.4
        )
        
        # 保存当前角度弧线
        self.angle_arc = angle_arc
        self.angle_label = angle_label
    
    def scene_4_formula_one(self):
        """场景4: 面积公式推导 - 第一形式"""
        # 标题
        title = Text(
            "扇形面积公式",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 问题引入
        question = Text(
            "扇形是圆的一部分",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(question), run_time=0.8)
        
        # 整圆面积公式
        circle_formula = MathTex(
            r"S_{\text{circle}} = \pi r^2",
            font_size=32,
            color=self.COLOR_CIRCLE
        ).move_to(UP * 3.8)
        
        self.play(Write(circle_formula), run_time=1.0)
        self.wait(0.5)
        
        # 圆分割动画 (简化版 - 12等分)
        division_lines = VGroup(*[
            Line(
                self.center,
                self.center + self.radius * np.array([
                    np.cos(i * TAU / 12),
                    np.sin(i * TAU / 12),
                    0
                ]),
                color=self.COLOR_AUXILIARY,
                stroke_width=1
            )
            for i in range(12)
        ])
        
        self.play(
            Create(division_lines),
            self.circle.animate.set_stroke(opacity=1),
            run_time=1.2
        )
        
        # 强调360度
        full_angle_text = Text(
            "360",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(self.center + DOWN * 0.3)
        
        self.play(FadeIn(full_angle_text, scale=1.2), run_time=0.5)
        self.wait(0.7)
        
        # 清除分割线
        self.play(
            FadeOut(division_lines),
            FadeOut(full_angle_text),
            self.circle.animate.set_stroke(opacity=0.5),
            run_time=0.4
        )
        
        # 扇形占比问题
        ratio_question = Text(
            "圆心角n占360的几分之几?",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(ratio_question), run_time=1.0)
        self.wait(0.5)
        
        # 分数表示
        ratio_formula = MathTex(
            r"\text{ratio} = \frac{n}{360}",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(Write(ratio_formula), run_time=0.8)
        
        # 高亮分数
        self.play(
            Indicate(ratio_formula, color=self.COLOR_HIGHLIGHT, scale_factor=1.15),
            run_time=0.6
        )
        
        # 公式组合
        combined = Text(
            "扇形面积 = 比例 × 圆面积",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(combined), run_time=1.0)
        
        # 最终公式推导
        formula_step = MathTex(
            r"S_{\text{sector}} = \frac{n}{360} \times \pi r^2",
            font_size=36
        ).move_to(DOWN * 0.8)
        
        self.play(Write(formula_step), run_time=1.2)
        
        # 简化为最终形式
        formula_final = MathTex(
            r"S = \frac{n\pi r^2}{360}",
            font_size=42,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2.2)
        
        self.play(
            TransformFromCopy(formula_step, formula_final),
            run_time=1.0
        )
        
        # 框住强调
        formula_box = SurroundingRectangle(
            formula_final,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(formula_box), run_time=0.6)
        self.play(
            Flash(formula_final, color=self.COLOR_FORMULA, flash_radius=0.8),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理 (保留最终公式，移到顶部)
        formula_small = MathTex(
            r"S = \frac{n\pi r^2}{360}",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5 + LEFT * 2)
        
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(circle_formula),
            FadeOut(ratio_question),
            FadeOut(ratio_formula),
            FadeOut(combined),
            FadeOut(formula_step),
            FadeOut(formula_box),
            Transform(formula_final, formula_small),
            run_time=0.6
        )
        
        self.formula_1 = formula_final  # 保存引用
    
    def scene_5_formula_two(self):
        """场景5: 面积公式推导 - 第二形式"""
        # 标题
        title = Text(
            "另一个公式",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ARC
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 高亮圆弧
        self.play(
            Indicate(self.arc, color=self.COLOR_ARC, scale_factor=1.1),
            run_time=0.8
        )
        
        # 弧长公式
        arc_length_intro = Text(
            "弧长公式:",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        arc_length_formula = MathTex(
            r"l = \frac{n}{360} \times 2\pi r",
            font_size=32,
            color=self.COLOR_ARC
        ).move_to(UP * 3.5)
        
        self.play(
            FadeIn(arc_length_intro),
            Write(arc_length_formula),
            run_time=1.2
        )
        
        # 提示
        hint = Text(
            "用弧长代替角度",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(hint), run_time=0.8)
        
        # 从第一公式开始
        deriv_1 = MathTex(
            r"S = \frac{n}{360} \times \pi r^2",
            font_size=30
        ).move_to(UP * 1.3)
        
        self.play(Write(deriv_1), run_time=0.8)
        
        # 变形
        deriv_2 = MathTex(
            r"S = \frac{n}{360} \times 2\pi r \times \frac{r}{2}",
            font_size=28
        ).move_to(UP * 0.3)
        
        self.play(
            TransformMatchingTex(deriv_1.copy(), deriv_2),
            run_time=1.2
        )
        
        # 替换弧长 (高亮对应部分)
        arc_part_highlight = SurroundingRectangle(
            deriv_2[0][2:14],  # n/360 × 2πr 部分
            color=self.COLOR_ARC,
            buff=0.05
        )
        
        self.play(Create(arc_part_highlight), run_time=0.5)
        self.play(FadeOut(arc_part_highlight), run_time=0.3)
        
        deriv_3 = MathTex(
            r"S = l \times \frac{r}{2}",
            font_size=32
        ).move_to(DOWN * 0.7)
        
        self.play(Write(deriv_3), run_time=1.0)
        
        # 最终形式
        formula_final_2 = MathTex(
            r"S = \frac{1}{2}lr",
            font_size=42,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2.0)
        
        self.play(
            TransformFromCopy(deriv_3, formula_final_2),
            run_time=1.0
        )
        
        # 框住强调
        formula_box_2 = SurroundingRectangle(
            formula_final_2,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(formula_box_2), run_time=0.6)
        self.play(
            Flash(formula_final_2, color=self.COLOR_FORMULA, flash_radius=0.8),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 两公式并列对比
        formula_small_2 = MathTex(
            r"S = \frac{1}{2}lr",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5 + RIGHT * 2)
        
        self.play(
            Transform(formula_final_2, formula_small_2),
            run_time=0.8
        )
        
        comparison_text = Text(
            "两个公式,任选其一",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(comparison_text), run_time=0.5)
        self.wait(0.7)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arc_length_intro),
            FadeOut(arc_length_formula),
            FadeOut(hint),
            FadeOut(deriv_1),
            FadeOut(deriv_2),
            FadeOut(deriv_3),
            FadeOut(formula_box_2),
            FadeOut(comparison_text),
            run_time=0.6
        )
        
        self.formula_2 = formula_final_2  # 保存引用
    
    def scene_6_example(self):
        """场景6: 实例计算"""
        # 清除之前的几何图形 (腾出空间)
        self.play(
            FadeOut(self.circle),
            FadeOut(self.sector_fill),
            FadeOut(self.radius_1),
            FadeOut(self.radius_2),
            FadeOut(self.arc),
            FadeOut(self.dot_O),
            FadeOut(self.label_O),
            FadeOut(self.dot_A),
            FadeOut(self.label_A),
            FadeOut(self.dot_B),
            FadeOut(self.label_B),
            FadeOut(self.angle_arc),
            FadeOut(self.angle_label),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "例题",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 题目
        problem = Text(
            "已知: r = 6cm,  n = 60",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        
        question_mark = Text(
            "求: 扇形面积",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(
            FadeIn(problem),
            FadeIn(question_mark),
            run_time=1.0
        )
        
        # 绘制示例扇形 (左侧)
        example_center = LEFT * 2.5 + UP * 2
        example_radius = 1.5
        example_angle = 60 * DEGREES
        
        example_sector = Sector(
            radius=example_radius,
            angle=example_angle,
            start_angle=0,
            arc_center=example_center,
            color=self.COLOR_SECTOR,
            fill_opacity=0.4,
            stroke_width=3
        )
        
        example_O = example_center
        example_A = example_center + example_radius * RIGHT
        example_B = example_center + example_radius * np.array([
            np.cos(example_angle),
            np.sin(example_angle),
            0
        ])
        
        example_radius_1 = Line(example_O, example_A, color=self.COLOR_RADIUS, stroke_width=3)
        example_radius_2 = Line(example_O, example_B, color=self.COLOR_RADIUS, stroke_width=3)
        
        # 标注尺寸
        radius_label = MathTex(
            "r=6",
            font_size=24,
            color=self.COLOR_RADIUS
        ).next_to(example_radius_1, DOWN, buff=0.1)
        
        angle_arc_ex = Arc(
            radius=0.5,
            start_angle=0,
            angle=example_angle,
            arc_center=example_center,
            color=self.COLOR_ANGLE,
            stroke_width=2
        )
        
        angle_label_ex = MathTex(
            r"60",
            font_size=24,
            color=self.COLOR_ANGLE
        ).move_to(
            example_center + 0.7 * np.array([
                np.cos(example_angle / 2),
                np.sin(example_angle / 2),
                0
            ])
        )
        
        self.play(
            Create(example_sector),
            Create(example_radius_1),
            Create(example_radius_2),
            run_time=1.0
        )
        
        self.play(
            FadeIn(radius_label),
            Create(angle_arc_ex),
            FadeIn(angle_label_ex),
            run_time=0.8
        )
        
        # 选择公式
        formula_choice = MathTex(
            r"S = \frac{n\pi r^2}{360}",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 3 + RIGHT * 2.5)
        
        self.play(Write(formula_choice), run_time=0.8)
        
        # 计算步骤 (右侧)
        step_1 = MathTex(
            r"S = \frac{60 \times \pi \times 6^2}{360}",
            font_size=28
        ).move_to(UP * 1.8 + RIGHT * 2.5)
        
        self.play(Write(step_1), run_time=1.0)
        
        step_2 = MathTex(
            r"= \frac{60 \times \pi \times 36}{360}",
            font_size=28
        ).move_to(UP * 0.9 + RIGHT * 2.5)
        
        self.play(Write(step_2), run_time=0.8)
        
        step_3 = MathTex(
            r"= \frac{\pi \times 36}{6}",
            font_size=28
        ).move_to(UP * 0.0 + RIGHT * 2.5)
        
        self.play(Write(step_3), run_time=0.8)
        
        step_4 = MathTex(
            r"= 6\pi \text{ cm}^2",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0 + RIGHT * 2.5)
        
        self.play(Write(step_4), run_time=0.8)
        
        # 近似值
        step_5 = MathTex(
            r"\approx 18.84 \text{ cm}^2",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 2.0 + RIGHT * 2.5)
        
        self.play(FadeIn(step_5), run_time=0.6)
        
        # 答案框
        answer_box = SurroundingRectangle(
            step_4,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        # 对勾
        checkmark = Text("✓", font_size=40, color=GREEN).next_to(answer_box, RIGHT, buff=0.2)
        self.play(FadeIn(checkmark, scale=1.3), run_time=0.4)
        
        self.wait(1.0)
        
        # 快速验证公式2
        verify_text = Text(
            "验证公式2:",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(DOWN * 3.5)
        
        # 计算弧长: l = (60/360) × 2π × 6 = 2π
        # 修复这里：移除对勾符号，或者使用LaTeX命令
        verify_calc = MathTex(
            r"l = 2\pi, \quad S = \frac{1}{2} \times 2\pi \times 6 = 6\pi",
            font_size=22,
            color=GRAY_B
        ).move_to(DOWN * 4.2)
        
        self.play(
            FadeIn(verify_text),
            FadeIn(verify_calc),
            run_time=1.5
        )
        
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(question_mark),
            FadeOut(example_sector),
            FadeOut(example_radius_1),
            FadeOut(example_radius_2),
            FadeOut(radius_label),
            FadeOut(angle_arc_ex),
            FadeOut(angle_label_ex),
            FadeOut(formula_choice),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(step_3),
            FadeOut(step_4),
            FadeOut(step_5),
            FadeOut(answer_box),
            FadeOut(checkmark),
            FadeOut(verify_text),
            FadeOut(verify_calc),
            FadeOut(self.formula_1),
            FadeOut(self.formula_2),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "扇形面积 - 核心要点",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点1
        point_1_icon = Sector(
            radius=0.3,
            angle=PI/2,
            color=self.COLOR_SECTOR,
            fill_opacity=0.8
        ).move_to(UP * 3 + LEFT * 3)
        
        point_1_text = Text(
            "扇形 = 两半径 + 圆弧",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(point_1_icon, RIGHT, buff=0.4)
        
        point_1 = VGroup(point_1_icon, point_1_text)
        
        self.play(
            FadeIn(point_1_icon, scale=0.5),
            FadeIn(point_1_text, shift=RIGHT * 0.3),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 要点2
        point_2_icon = MathTex(
            r"\frac{n}{360}",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(UP * 1.5 + LEFT * 3.3)
        
        point_2_text = Text(
            "公式1:  S = (nπr²)/360",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(point_2_icon, RIGHT, buff=0.6)
        
        point_2 = VGroup(point_2_icon, point_2_text)
        
        self.play(
            FadeIn(point_2_icon, scale=0.5),
            FadeIn(point_2_text, shift=RIGHT * 0.3),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 要点3
        point_3_icon = MathTex(
            r"\frac{1}{2}lr",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(ORIGIN + LEFT * 3.2)
        
        point_3_text = Text(
            "公式2:  S = (1/2)lr",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(point_3_icon, RIGHT, buff=0.6)
        
        point_3 = VGroup(point_3_icon, point_3_text)
        
        self.play(
            FadeIn(point_3_icon, scale=0.5),
            FadeIn(point_3_text, shift=RIGHT * 0.3),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 所有要点闪烁
        all_points = VGroup(point_1, point_2, point_3)
        self.play(
            Flash(point_1, color=self.COLOR_HIGHLIGHT),
            Flash(point_2, color=self.COLOR_HIGHLIGHT),
            Flash(point_3, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # 清空
        self.play(
            FadeOut(summary_title),
            FadeOut(all_points),
            run_time=0.5
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小扇形装饰旋转
        decoration_sectors = VGroup(*[
            Sector(
                radius=0.4,
                angle=60 * DEGREES,
                start_angle=i * 60 * DEGREES,
                color=self.COLOR_SECTOR,
                fill_opacity=0.6
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([
                    np.cos(i * TAU / 6),
                    np.sin(i * TAU / 6),
                    0
                ])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(sector, scale=0.5) for sector in decoration_sectors],
            run_time=0.6
        )
        
        self.play(
            Rotate(decoration_sectors, angle=PI, run_time=1.5)
        )
        
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_sectors),
            run_time=1.0
        )


# ===== 运行说明 =====
# 快速预览 (480p, 15fps):
#   manim -pql sector_area.py SectorAreaAnimation
#
# 高质量渲染 (1080p, 60fps):
#   manim -qh sector_area.py SectorAreaAnimation
#
# 4K质量 (2160p, 60fps):
#   manim -qk sector_area.py SectorAreaAnimation