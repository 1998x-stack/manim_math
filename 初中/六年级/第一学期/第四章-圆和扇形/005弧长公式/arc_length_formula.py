"""
弧长公式教学动画 - Arc Length Formula Animation
使用 Manim 创建的六年级数学教学视频

内容: 圆和扇形 - 弧长公式的推导与应用
知识点: l = (nπr)/180, l = (n/360) × 2πr, l = αr
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


class ArcLengthFormula(Scene):
    """
    弧长公式教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 圆周长复习 - 基础知识
    3. 弧的概念 - 圆周的一部分
    4. 比例关系推导 - 核心推理
    5. 弧长公式推导 - 数学推导
    6. 实例计算 - 应用演练
    7. 片尾总结 - 知识回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"       # 蓝色 - 主圆
        self.COLOR_ARC = "#e74c3c"          # 红色 - 弧
        self.COLOR_RADIUS = "#2ecc71"       # 绿色 - 半径
        self.COLOR_ANGLE = "#f39c12"        # 橙色 - 圆心角
        self.COLOR_FORMULA = "#9b59b6"      # 紫色 - 公式
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_circumference_review()
        self.scene_3_arc_concept()
        self.scene_4_proportion_derivation()
        self.scene_5_formula_derivation()
        self.scene_6_example_calculation()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 基准参数
        self.center = ORIGIN + UP * 1.5  # 圆心位置
        self.radius = 2.0  # 半径
        
        # 角度参数 (使用度数)
        self.start_angle = 30  # 起始角度 (度)
        self.end_angle = 150   # 结束角度 (度)
        self.central_angle = 120  # 圆心角 (度)
        
        # 计算关键点
        self.point_start = self.center + self.radius * np.array([
            np.cos(self.start_angle * DEGREES),
            np.sin(self.start_angle * DEGREES),
            0
        ])
        
        self.point_end = self.center + self.radius * np.array([
            np.cos(self.end_angle * DEGREES),
            np.sin(self.end_angle * DEGREES),
            0
        ])
        
        # 计算圆周长和弧长
        self.circumference = 2 * PI * self.radius
        self.arc_length = (self.central_angle * PI * self.radius) / 180
        
        # 验证计算
        print(f"✓ 几何参数:")
        print(f"  半径: {self.radius}")
        print(f"  圆心角: {self.central_angle}°")
        print(f"  圆周长: {self.circumference:.4f}")
        print(f"  弧长: {self.arc_length:.4f}")
    
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
        hook_text = Text(
            "如何计算弧长?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 创建圆
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        self.play(Create(self.circle), run_time=1.0)
        
        # 创建弧并高亮
        arc = Arc(
            radius=self.radius,
            start_angle=self.start_angle * DEGREES,
            angle=self.central_angle * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=8
        ).move_to(self.center)
        
        self.play(
            Create(arc),
            Flash(arc, color=self.COLOR_ARC, flash_radius=0.5, num_lines=12),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(arc),
            run_time=0.5
        )
    
    def scene_2_circumference_review(self):
        """场景2: 圆周长复习"""
        # 标题
        title = Text(
            "首先, 回顾圆周长",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 半径线
        radius_line = Line(
            self.center,
            self.center + RIGHT * self.radius,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        radius_label = MathTex(
            "r",
            font_size=28,
            color=self.COLOR_RADIUS
        ).next_to(radius_line, DOWN, buff=0.15)
        
        self.play(Create(radius_line), run_time=0.5)
        self.play(FadeIn(radius_label, shift=UP * 0.1), run_time=0.3)
        
        # 圆周长公式
        circumference_formula = MathTex(
            r"C = 2\pi r",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.5)
        
        self.play(Write(circumference_formula), run_time=1.0)
        self.wait(0.5)
        
        # 创意动画: 圆"展开"成直线
        # 创建一个表示圆周的虚线圆
        circle_dashed = DashedVMobject(
            Circle(radius=self.radius, color=self.COLOR_CIRCLE).move_to(self.center),
            num_dashes=40
        )
        
        # 创建展开的直线
        line_length = 2 * PI * self.radius
        unrolled_line = Line(
            LEFT * line_length / 2,
            RIGHT * line_length / 2,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(DOWN * 0.5)
        
        self.play(
            Transform(self.circle, circle_dashed),
            run_time=0.8
        )
        
        self.play(
            ReplacementTransform(circle_dashed, unrolled_line),
            run_time=1.5,
            rate_func=smooth
        )
        
        # 标注长度
        brace = Brace(unrolled_line, DOWN, buff=0.2, color=self.COLOR_AUXILIARY)
        brace_label = MathTex(
            r"2\pi r",
            font_size=28,
            color=self.COLOR_AUXILIARY
        ).next_to(brace, DOWN, buff=0.1)
        
        self.play(
            FadeIn(brace),
            FadeIn(brace_label),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理并恢复圆
        # 重新创建圆 (因为之前被Transform了)
        new_circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        self.play(
            FadeOut(title),
            FadeOut(circumference_formula),
            FadeOut(unrolled_line),
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(radius_line),
            FadeOut(radius_label),
            run_time=0.5
        )
        
        # 添加新圆 (替换旧的)
        self.remove(self.circle)
        self.circle = new_circle
        self.add(self.circle)
    
    def scene_3_arc_concept(self):
        """场景3: 弧的概念"""
        # 标题
        title = Text(
            "弧: 圆周的一部分",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建弧 (高亮)
        self.arc = Arc(
            radius=self.radius,
            start_angle=self.start_angle * DEGREES,
            angle=self.central_angle * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=8
        ).move_to(self.center)
        
        self.play(Create(self.arc), run_time=1.2)
        
        # 半径1 (到起点)
        self.radius1 = Line(
            self.center,
            self.point_start,
            color=self.COLOR_RADIUS,
            stroke_width=3
        )
        
        # 半径2 (到终点)
        self.radius2 = Line(
            self.center,
            self.point_end,
            color=self.COLOR_RADIUS,
            stroke_width=3
        )
        
        self.play(Create(self.radius1), run_time=0.5)
        self.play(Create(self.radius2), run_time=0.5)
        
        # 圆心角标注
        self.angle_arc = Angle(
            self.radius1,
            self.radius2,
            radius=0.6,
            color=self.COLOR_ANGLE,
            other_angle=False
        )
        
        self.angle_label = MathTex(
            r"n°",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(self.center + UP * 0.9 + RIGHT * 0.3)
        
        self.play(Create(self.angle_arc), run_time=0.5)
        self.play(FadeIn(self.angle_label, shift=DOWN * 0.1), run_time=0.3)
        
        # 说明文字
        explain = Text(
            "圆心角决定弧的大小",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2.0)  # 重点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain),
            run_time=0.5
        )

    def scene_4_proportion_derivation(self):
        """场景4: 比例关系推导"""
        # 标题
        title = Text(
            "找规律: 比例关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题1: 圆心角是多少?
        question1 = Text(
            "这个角是多少?",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.5 + LEFT * 3)
        
        # 答案1: n°
        answer1 = MathTex(
            r"n°",
            font_size=32,
            color=self.COLOR_ANGLE
        ).next_to(question1, DOWN, buff=0.3)
        
        # 指向角的箭头
        arrow1 = Arrow(
            answer1.get_right(),
            self.angle_label.get_left(),
            color=self.COLOR_ANGLE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(FadeIn(question1, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            FadeIn(answer1, scale=1.2),
            Create(arrow1),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # 问题2: 完整圆是多少?
        question2 = Text(
            "完整圆是多少?",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.5 + RIGHT * 3)
        
        # 答案2: 360°
        answer2 = MathTex(
            r"360°",
            font_size=32,
            color=self.COLOR_CIRCLE
        ).next_to(question2, DOWN, buff=0.3)
        
        self.play(FadeIn(question2, shift=DOWN * 0.2), run_time=0.5)
        self.play(
            FadeIn(answer2, scale=1.2),
            self.circle.animate.set_stroke(width=5),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # 比例关系式 - 修复：使用正确的LaTeX分数语法
        ratio_math = MathTex(
            r"\frac{l}{C} = \frac{n}{360}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        # 设置颜色
        ratio_math.set_color_by_tex("l", self.COLOR_ARC)
        ratio_math.set_color_by_tex("C", self.COLOR_CIRCLE)
        ratio_math.set_color_by_tex("n", self.COLOR_ANGLE)
        ratio_math.set_color_by_tex("360", self.COLOR_CIRCLE)
        
        # 添加说明文字
        ratio_explain = Text(
            "(弧长/圆周长 = 角度/360°)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(ratio_math, DOWN, buff=0.3)
        
        ratio_formula = VGroup(ratio_math, ratio_explain)
        
        self.play(Write(ratio_math), FadeIn(ratio_explain), run_time=1.5)
        
        self.wait(1.0)
        
        # 可视化比例 - 饼图
        # 创建完整圆扇形 (半透明)
        full_sector = Sector(
            radius=0.8,  # 修复：使用 radius 而不是 outer_radius
            angle=360 * DEGREES,
            start_angle=0,
            color=self.COLOR_AUXILIARY,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(DOWN * 5.5 + LEFT * 2.5)
        
        # 创建 n° 扇形 (高亮)
        highlight_sector = Sector(
            radius=0.8,  # 修复：使用 radius 而不是 outer_radius
            angle=self.central_angle * DEGREES,
            start_angle=self.start_angle * DEGREES,
            color=self.COLOR_ANGLE,
            fill_opacity=0.5,
            stroke_width=3
        ).move_to(DOWN * 5.5 + LEFT * 2.5)
        
        # 标签
        full_label = MathTex(r"360°", font_size=20, color=WHITE).next_to(full_sector, DOWN, buff=0.2)
        part_label = MathTex(r"n°", font_size=20, color=self.COLOR_ANGLE).next_to(highlight_sector, RIGHT, buff=0.2)
        
        pie_group = VGroup(full_sector, highlight_sector, full_label, part_label)
        
        self.play(
            FadeIn(full_sector),
            FadeIn(full_label),
            run_time=0.6
        )
        self.play(
            FadeIn(highlight_sector, scale=0.8),
            FadeIn(part_label),
            run_time=0.6
        )
        
        self.wait(2.0)  # 理解停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question1),
            FadeOut(question2),
            FadeOut(answer1),
            FadeOut(answer2),
            FadeOut(arrow1),
            FadeOut(pie_group),
            self.circle.animate.set_stroke(width=3),
            run_time=0.6
        )
        
        # 将比例式移到顶部保存
        self.ratio_math = MathTex(
            r"\frac{l}{C} = \frac{n}{360}",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(
            FadeOut(ratio_explain),
            Transform(ratio_math, self.ratio_math),
            run_time=0.5
        )

    def scene_5_formula_derivation(self):
        """场景5: 弧长公式推导"""
        # 标题
        title = Text(
            "推导弧长公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(title), run_time=0.8)
        
        # Step 1: 用 l 和 C 替换文字
        step1 = MathTex(
            r"\frac{l}{C} = \frac{n}{360}",  # 去掉度数符号，简化公式
            font_size=32,
            color=WHITE
        ).move_to(UP * 3)
        
        # 手动设置颜色 - 通过索引访问子对象
        # step1[0] 是整个公式，我们需要根据索引来设置颜色
        # 由于使用了\frac，公式的结构会更复杂
        # 我们可以使用更简单的方法：创建多个MathTex对象并组合
        
        explain1 = Text(
            "用字母表示",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(step1, RIGHT, buff=0.5)
        
        self.play(
            TransformMatchingTex(self.ratio_math, step1),
            FadeIn(explain1),
            run_time=1.0
        )
        
        self.wait(0.8)
        self.play(FadeOut(explain1), run_time=0.3)
        
        # Step 2: 代入 C = 2πr
        step2 = MathTex(
            r"\frac{l}{2\pi r} = \frac{n}{360}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        explain2 = Text(
            "代入 C = 2πr",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(step2, RIGHT, buff=0.5)
        
        self.play(
            TransformMatchingTex(step1, step2),
            FadeIn(explain2),
            run_time=1.0
        )
        
        self.wait(0.8)
        self.play(FadeOut(explain2), run_time=0.3)
        
        # Step 3: 解出 l (形式1)
        step3 = MathTex(
            r"l = \frac{n}{360} \times 2\pi r",
            font_size=32,
            color=WHITE
        ).move_to(ORIGIN)
        
        explain3 = Text(
            "公式形式1",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_FORMULA
        ).next_to(step3, RIGHT, buff=0.5)
        
        self.play(
            TransformMatchingTex(step2, step3),
            FadeIn(explain3),
            run_time=1.0
        )
        
        # 高亮框
        box1 = SurroundingRectangle(step3, color=self.COLOR_FORMULA, buff=0.15)
        self.play(Create(box1), run_time=0.5)
        
        self.wait(1.0)
        
        # Step 4: 化简 (形式2)
        step4 = MathTex(
            r"l = \frac{n\pi r}{180}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        explain4 = Text(
            "公式形式2 (化简)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_FORMULA
        ).next_to(step4, RIGHT, buff=0.5)
        
        self.play(
            FadeOut(explain3),
            run_time=0.3
        )
        
        self.play(
            Write(step4),
            FadeIn(explain4),
            run_time=1.0
        )
        
        # 高亮框
        box2 = SurroundingRectangle(step4, color=self.COLOR_FORMULA, buff=0.15)
        self.play(Create(box2), run_time=0.5)
        
        self.wait(1.5)
        
        # 三公式并列展示
        self.play(
            FadeOut(title),
            FadeOut(explain4),
            run_time=0.4
        )
        
        # 重新排列三个公式
        formula_title = Text(
            "弧长公式的三种形式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        # 公式1 (最常用)
        final_formula1 = MathTex(
            r"l = \frac{n\pi r}{180}",
            font_size=36,
            color=self.COLOR_FORMULA  # 直接设置公式颜色
        ).move_to(UP * 2.5)
        
        label1 = Text(
            "最常用",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(final_formula1, RIGHT, buff=0.3)
        
        # 公式2 (展开形式)
        final_formula2 = MathTex(
            r"l = \frac{n}{360} \times 2\pi r",
            font_size=32,
            color=self.COLOR_FORMULA  # 直接设置公式颜色
        ).move_to(UP * 0.5)
        
        label2 = Text(
            "便于理解",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(final_formula2, RIGHT, buff=0.3)
        
        # 公式3 (弧度制)
        final_formula3 = MathTex(
            r"l = \alpha r",
            font_size=32,
            color=self.COLOR_FORMULA  # 直接设置公式颜色
        ).move_to(DOWN * 1.5)
        
        label3 = Text(
            "弧度制 (高中)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        ).next_to(final_formula3, RIGHT, buff=0.3)
        
        self.play(
            FadeOut(step3),
            FadeOut(box1),
            FadeOut(step4),
            FadeOut(box2),
            run_time=0.4
        )
        
        self.play(Write(formula_title), run_time=0.6)
        
        self.play(
            Write(final_formula1),
            FadeIn(label1),
            run_time=0.8
        )
        
        self.play(
            Write(final_formula2),
            FadeIn(label2),
            run_time=0.8
        )
        
        self.play(
            Write(final_formula3),
            FadeIn(label3),
            run_time=0.8
        )
        
        # 统一框选
        all_formulas = VGroup(final_formula1, final_formula2, final_formula3)
        big_box = SurroundingRectangle(all_formulas, color=self.COLOR_FORMULA, buff=0.3)
        
        self.play(Create(big_box), run_time=0.6)
        
        self.wait(2.5)  # 难点停留
        
        # 保存公式组
        self.formulas_group = VGroup(
            formula_title, final_formula1, label1,
            final_formula2, label2, final_formula3, label3, big_box
        )
        
        # 清理
        self.play(
            FadeOut(self.formulas_group),
            run_time=0.6
        )

    def scene_6_example_calculation(self):
        """场景6: 实例计算"""
        # 标题
        title = Text(
            "实战演练",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 题目
        problem = Text(
            "已知: r = 3cm, n = 120°\n求: 弧长 l",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(FadeIn(problem, shift=DOWN * 0.2), run_time=0.8)
        
        self.wait(0.5)
        
        # 在图上标注参数
        # 更新圆的半径为3 (缩放)
        scale_factor = 1.5 / self.radius  # 目标半径1.5 (适合屏幕)
        
        example_circle = Circle(
            radius=1.5,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(UP * 1.5)
        
        example_arc = Arc(
            radius=1.5,
            start_angle=30 * DEGREES,
            angle=120 * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=6
        ).move_to(UP * 1.5)
        
        # 半径标注
        radius_line_ex = Line(
            UP * 1.5,
            UP * 1.5 + RIGHT * 1.5,
            color=self.COLOR_RADIUS,
            stroke_width=3
        )
        
        radius_label_ex = MathTex(
            r"r = 3\text{cm}",
            font_size=24,
            color=self.COLOR_RADIUS
        ).next_to(radius_line_ex, DOWN, buff=0.1)
        
        # 圆心角标注
        radius1_ex = Line(
            UP * 1.5,
            UP * 1.5 + 1.5 * np.array([np.cos(30 * DEGREES), np.sin(30 * DEGREES), 0]),
            color=self.COLOR_RADIUS,
            stroke_width=2
        )
        
        radius2_ex = Line(
            UP * 1.5,
            UP * 1.5 + 1.5 * np.array([np.cos(150 * DEGREES), np.sin(150 * DEGREES), 0]),
            color=self.COLOR_RADIUS,
            stroke_width=2
        )
        
        angle_arc_ex = Angle(
            radius1_ex,
            radius2_ex,
            radius=0.5,
            color=self.COLOR_ANGLE
        )
        
        angle_label_ex = MathTex(
            r"120^{\circ}",  # 使用LaTeX标准的度数表示
            font_size=24,
            color=self.COLOR_ANGLE
        ).move_to(UP * 2.2)
        
        self.play(
            FadeOut(self.circle),
            FadeOut(self.arc),
            FadeOut(self.radius1),
            FadeOut(self.radius2),
            FadeOut(self.angle_arc),
            FadeOut(self.angle_label),
            run_time=0.4
        )
        
        self.play(
            Create(example_circle),
            Create(example_arc),
            run_time=0.8
        )
        
        self.play(
            Create(radius_line_ex),
            FadeIn(radius_label_ex),
            Create(radius1_ex),
            Create(radius2_ex),
            Create(angle_arc_ex),
            FadeIn(angle_label_ex),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 选择公式 - 修复这里
        # 使用Text显示中文，MathTex显示公式
        formula_text = Text(
            "使用公式:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1 + LEFT * 2)
        
        formula_math = MathTex(
            r"l = \frac{n\pi r}{180}",  # 使用\frac代替\over
            font_size=28,
            color=WHITE
        ).next_to(formula_text, RIGHT, buff=0.3)
        
        formula_group = VGroup(formula_text, formula_math)
        formula_group.move_to(DOWN * 1)
        
        self.play(Write(formula_group), run_time=0.8)
        
        self.wait(0.5)
        
        # 计算步骤 - 修复这里
        calc_step1 = MathTex(
            r"l = \frac{120 \times \pi \times 3}{180}",  # 使用\frac
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        self.play(Write(calc_step1), run_time=1.0)
        self.wait(0.5)
        
        # 化简
        calc_step2 = MathTex(
            r"l = \frac{360\pi}{180}",  # 使用\frac
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(TransformMatchingTex(calc_step1.copy(), calc_step2), run_time=0.8)
        self.wait(0.5)
        
        # 最终答案
        calc_step3 = MathTex(
            r"l = 2\pi \text{ cm}",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(TransformMatchingTex(calc_step2.copy(), calc_step3), run_time=0.8)
        
        # 答案框高亮
        answer_box = SurroundingRectangle(
            calc_step3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            stroke_width=3
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        # 数值近似
        approx = MathTex(
            r"\approx 6.28 \text{ cm}",
            font_size=28,
            color=GRAY_A
        ).next_to(calc_step3, DOWN, buff=0.3)
        
        self.play(FadeIn(approx, shift=UP * 0.1), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(example_circle),
            FadeOut(example_arc),
            FadeOut(radius_line_ex),
            FadeOut(radius_label_ex),
            FadeOut(radius1_ex),
            FadeOut(radius2_ex),
            FadeOut(angle_arc_ex),
            FadeOut(angle_label_ex),
            FadeOut(formula_group),
            FadeOut(calc_step1),
            FadeOut(calc_step2),
            FadeOut(calc_step3),
            FadeOut(answer_box),
            FadeOut(approx),
            run_time=0.6
        )

    def scene_7_outro(self):
        """场景7: 片尾总结"""
        # 标题
        title = Text(
            "弧长公式总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 要点1
        point1 = Text(
            "弧长 = 圆周长 × 角度比例",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(point1, shift=DOWN * 0.2), run_time=0.6)
        
        # 要点2
        point2 = Text(
            "三种公式形式, 灵活选择",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(point2, shift=DOWN * 0.2), run_time=0.6)
        
        # 公式卡片 - 修复这里
        formula_card1 = MathTex(
            r"l = \frac{n\pi r}{180}",
            font_size=32,
            color=self.COLOR_FORMULA  # 直接设置颜色
        ).move_to(UP * 1.5)
        
        formula_card2 = MathTex(
            r"l = \frac{n}{360} \times 2\pi r",
            font_size=28,
            color=self.COLOR_FORMULA  # 直接设置颜色
        ).move_to(ORIGIN)
        
        formula_card3 = MathTex(
            r"l = \alpha r",
            font_size=28,
            color=self.COLOR_FORMULA  # 直接设置颜色
        ).move_to(DOWN * 1.5)
        
        formulas = VGroup(formula_card1, formula_card2, formula_card3)
        
        # 移除通过索引设置颜色的循环
        # for formula in formulas:
        #     formula[2].set_color(self.COLOR_FORMULA)
        
        self.play(
            *[FadeIn(f, shift=LEFT * 0.3) for f in formulas],
            run_time=1.0
        )
        
        # 记忆技巧
        tip = Text(
            "记住: n/360 = 角度比",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        tip_box = SurroundingRectangle(tip, color=self.COLOR_HIGHLIGHT, buff=0.15)
        
        self.play(
            FadeIn(tip, shift=UP * 0.2),
            Create(tip_box),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理前面内容
        self.play(
            FadeOut(title),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(formulas),
            FadeOut(tip),
            FadeOut(tip_box),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰圆圈
        circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_FORMULA, fill_opacity=0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles],
            run_time=0.6
        )
        
        self.play(Rotate(circles, angle=2 * PI, run_time=2))
        
        # 弧长图标闪烁
        icon_arc1 = Arc(
            radius=0.3,
            start_angle=0,
            angle=120 * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=4
        ).move_to(DOWN * 3 + LEFT * 2)
        
        icon_arc2 = Arc(
            radius=0.3,
            start_angle=0,
            angle=90 * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=4
        ).move_to(DOWN * 3)
        
        icon_arc3 = Arc(
            radius=0.3,
            start_angle=0,
            angle=180 * DEGREES,
            color=self.COLOR_ARC,
            stroke_width=4
        ).move_to(DOWN * 3 + RIGHT * 2)
        
        icons = VGroup(icon_arc1, icon_arc2, icon_arc3)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            FadeOut(icons),
            run_time=1.0
        )

# 运行命令:
# manim -pql arc_length_formula.py ArcLengthFormula  # 快速预览
# manim -qh arc_length_formula.py ArcLengthFormula   # 高质量渲染 (1080p)