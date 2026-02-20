"""
配方法 - Manim 教学动画
Completing the Square Method for Solving Quadratic Equations

目标受众: 八年级学生
视频格式: TikTok 竖屏 (1080×1920)
时长: 75-90秒

作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CompletingTheSquare(Scene):
    """
    配方法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 复习完全平方公式
    3. 配方的几何意义（重点）
    4. 配方法步骤讲解
    5. 例题1 - x² + 6x + 5 = 0
    6. 例题2 - 2x² - 8x + 3 = 0
    7. 配方法的应用
    8. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 关键步骤
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_SUCCESS = "#2ecc71"        # 绿色 - 正确答案
        self.COLOR_GEOMETRY = "#9b59b6"       # 紫色 - 几何图形
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 40
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 24
        self.FONT_SIZE_SMALL = 20
        self.FONT_SIZE_FORMULA = 32
        
        # 执行动画序列
        self.show_opening()
        self.show_perfect_square_review()
        self.show_geometry_visualization()
        self.show_method_steps()
        self.show_example_1()
        self.show_example_2()
        self.show_applications()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部固定)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 问题方程
        problem_eq = MathTex(
            r"x^2 + 6x + 5 = 0",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        self.play(Write(problem_eq), run_time=0.8)
        self.wait(0.3)
        
        # 问号
        question_mark = Text(
            "?",
            font=self.FONT_CHINESE,
            font_size=56,
            color=self.COLOR_HIGHLIGHT
        ).next_to(problem_eq, RIGHT, buff=0.5)
        
        question_text = Text(
            "不能直接开平方，怎么办？",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(
            FadeIn(question_mark, scale=0.5),
            run_time=0.4
        )
        self.play(Write(question_text), run_time=0.8)
        
        # 闪烁强调
        self.play(
            Flash(problem_eq, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(problem_eq),
            FadeOut(question_mark),
            FadeOut(question_text),
            run_time=0.5
        )
    
    def show_perfect_square_review(self):
        """场景2: 复习完全平方公式 (5-12秒)"""
        # 标题
        title = Text(
            "回顾：完全平方公式",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式
        formula = MathTex(
            r"(a+b)^2 = a^2 + 2ab + b^2",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)
        
        # 箭头
        arrow = Arrow(
            start=UP * 3,
            end=UP * 2,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 示例
        example = MathTex(
            r"{{ (x+3) }}^2 = {{ x^2 }} + {{ 6x }} + {{ 9 }}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1)
        
        self.play(Write(example), run_time=1.2)
        self.wait(0.5)
        
        # 高亮对应项
        x2_term = example.get_part_by_tex(r"x^2")
        six_x_term = example.get_part_by_tex(r"6x")
        nine_term = example.get_part_by_tex(r"9")
        
        self.play(
            Indicate(x2_term, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        self.play(
            Indicate(six_x_term, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        self.play(
            Indicate(nine_term, color=self.COLOR_HIGHLIGHT),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(arrow),
            FadeOut(example),
            run_time=0.5
        )
    
    def show_geometry_visualization(self):
        """场景3: 配方的几何意义 (12-25秒)"""
        # 标题
        geo_title = Text(
            "几何理解：x² + 6x",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_GEOMETRY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(geo_title), run_time=0.8)
        
        # 几何中心位置
        center = np.array([0, 2.5, 0])
        square_size = 1.2
        
        # 1. x² 正方形（蓝色）
        square_x2 = Square(
            side_length=square_size,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=3
        ).move_to(center + LEFT * square_size / 2 + UP * square_size / 2)
        
        label_x2 = MathTex(
            r"x^2",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(square_x2.get_center())
        
        self.play(FadeIn(square_x2), run_time=0.5)
        self.play(Write(label_x2), run_time=0.5)
        self.wait(0.3)
        
        # 提示 6x
        hint_6x = Text(
            "6x = 3x + 3x",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(hint_6x, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)
        
        # 2. 第一个 3x 矩形（右侧）
        rect1 = Rectangle(
            width=square_size,
            height=square_size,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.3,
            stroke_width=3
        ).next_to(square_x2, RIGHT, buff=0)
        
        label_3x_1 = MathTex(
            r"3x",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(rect1.get_center())
        
        self.play(
            FadeIn(rect1, shift=LEFT * 0.3),
            run_time=0.7
        )
        self.play(Write(label_3x_1), run_time=0.4)
        self.wait(0.3)
        
        # 3. 第二个 3x 矩形（下方）
        rect2 = Rectangle(
            width=square_size,
            height=square_size,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.3,
            stroke_width=3
        ).next_to(square_x2, DOWN, buff=0)
        
        label_3x_2 = MathTex(
            r"3x",
            font_size=self.FONT_SIZE_SMALL,
            color=WHITE
        ).move_to(rect2.get_center())
        
        self.play(
            FadeIn(rect2, shift=UP * 0.3),
            run_time=0.7
        )
        self.play(Write(label_3x_2), run_time=0.4)
        self.play(FadeOut(hint_6x), run_time=0.3)
        self.wait(0.5)
        
        # 4. 提示缺少的部分
        missing_hint = Text(
            "缺少什么？",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(missing_hint, shift=DOWN * 0.2), run_time=0.5)
        
        # 虚线框标记缺口
        dotted_square_pos = rect1.get_center() + DOWN * square_size
        dotted_square = DashedVMobject(
            Square(
                side_length=square_size,
                color=self.COLOR_GEOMETRY,
                stroke_width=3
            ).move_to(dotted_square_pos),
            num_dashes=20
        )
        
        self.play(Create(dotted_square), run_time=0.6)
        self.play(
            Flash(dotted_square, color=self.COLOR_GEOMETRY, flash_radius=0.4),
            run_time=0.4
        )
        self.wait(0.5)
        
        # 5. 补充小正方形 3² = 9（紫色）
        square_9 = Square(
            side_length=square_size,
            color=self.COLOR_GEOMETRY,
            fill_opacity=0.5,
            stroke_width=3
        ).move_to(dotted_square_pos)
        
        label_9 = MathTex(
            r"9",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(square_9.get_center())
        
        self.play(
            FadeOut(dotted_square),
            FadeIn(square_9, scale=0.8),
            run_time=0.7
        )
        self.play(Write(label_9), run_time=0.4)
        self.play(FadeOut(missing_hint), run_time=0.3)
        self.wait(0.5)
        
        # 6. 整体大正方形边框
        all_shapes = VGroup(square_x2, rect1, rect2, square_9)
        big_square_outline = SurroundingRectangle(
            all_shapes,
            color=self.COLOR_SUCCESS,
            buff=0.05,
            stroke_width=5
        )
        
        self.play(Create(big_square_outline), run_time=0.8)
        
        # 标注 (x+3)²
        label_total = MathTex(
            r"(x+3)^2",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).next_to(big_square_outline, RIGHT, buff=0.5)
        
        self.play(Write(label_total), run_time=0.8)
        self.wait(0.5)
        
        # 公式对照
        formula_correspondence = MathTex(
            r"x^2 + 6x {{ + 9 }} = (x+3)^2",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        formula_correspondence.get_part_by_tex(r"+ 9").set_color(self.COLOR_GEOMETRY)
        
        self.play(Write(formula_correspondence), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(geo_title),
            FadeOut(square_x2),
            FadeOut(rect1),
            FadeOut(rect2),
            FadeOut(square_9),
            FadeOut(label_x2),
            FadeOut(label_3x_1),
            FadeOut(label_3x_2),
            FadeOut(label_9),
            FadeOut(big_square_outline),
            FadeOut(label_total),
            FadeOut(formula_correspondence),
            run_time=0.6
        )
    
    def show_method_steps(self):
        """场景4: 配方法步骤讲解 (25-38秒)"""
        # 标题
        title = Text(
            "配方法步骤",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建步骤卡片
        def create_step_card(number, text, color):
            circle = Circle(
                radius=0.25,
                color=color,
                fill_opacity=1,
                stroke_width=0
            )
            num_text = Text(
                str(number),
                font=self.FONT_CHINESE,
                font_size=20,
                color=WHITE,
                weight=BOLD
            ).move_to(circle.get_center())
            
            content = Text(
                text,
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_SMALL,
                color=WHITE
            )
            
            card = VGroup(circle, num_text, content).arrange(RIGHT, buff=0.4)
            card.shift(LEFT * 10)  # 初始在屏幕外
            return card
        
        step1 = create_step_card(1, "移项（常数→右边）", self.COLOR_PRIMARY)
        step2 = create_step_card(2, "二次项系数化为1", self.COLOR_PRIMARY)
        step3 = create_step_card(3, "两边加 (p/2)²", self.COLOR_SECONDARY)
        step4 = create_step_card(4, "配成完全平方式", self.COLOR_PRIMARY)
        
        step1.move_to(UP * 3.5)
        step2.move_to(UP * 2.0)
        step3.move_to(UP * 0.5)
        step4.move_to(DOWN * 1.0)
        
        # 依次滑入
        for step in [step1, step2, step3, step4]:
            self.play(step.animate.shift(RIGHT * 10), run_time=0.6)
            self.wait(0.2)
        
        # 强调关键步骤
        self.play(
            Flash(step3, color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(step4),
            run_time=0.5
        )
    
    def show_example_1(self):
        """场景5: 例题1 - x² + 6x + 5 = 0 (38-53秒)"""
        # 例题标签
        example_label = Text(
            "例题 1",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 原方程
        eq0 = MathTex(
            r"x^2 + 6x + 5 = 0",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(eq0), run_time=0.8)
        self.wait(0.5)
        
        # 步骤1：移项
        eq1 = MathTex(
            r"x^2 + 6x = -5",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.5)
        
        step1_label = Text(
            "① 移项",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(eq1, LEFT, buff=0.5)
        
        self.play(
            TransformMatchingTex(eq0.copy(), eq1),
            FadeIn(step1_label),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 标注左侧
        left_highlight = SurroundingRectangle(
            eq1[0:3],  # x² + 6x
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(Create(left_highlight), run_time=0.5)
        self.wait(0.3)
        
        # 提示计算 (6/2)² = 9
        hint_calc = MathTex(
            r"\left(\frac{6}{2}\right)^2 = 9",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(eq1, RIGHT, buff=0.8)
        
        self.play(
            Write(hint_calc),
            FadeOut(left_highlight),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 步骤2：两边加9
        eq2 = MathTex(
            r"x^2 + 6x {{ + 9 }} = -5 {{ + 9 }}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.0)
        
        eq2.get_part_by_tex(r"+ 9").set_color(self.COLOR_GEOMETRY)
        
        step2_label = Text(
            "② 两边+9",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(eq2, LEFT, buff=0.5)
        
        self.play(
            TransformMatchingTex(eq1.copy(), eq2),
            FadeIn(step2_label),
            FadeOut(hint_calc),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 步骤3：配成完全平方
        eq3 = MathTex(
            r"{{ (x+3)^2 }} = 4",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.5)
        
        step3_label = Text(
            "③ 配方",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(eq3, LEFT, buff=0.5)
        
        self.play(
            TransformMatchingTex(eq2.copy(), eq3),
            FadeIn(step3_label),
            run_time=1.2
        )
        self.wait(0.3)
        
        # 高亮完全平方
        perfect_square = eq3.get_part_by_tex(r"(x+3)^2")
        self.play(
            Indicate(perfect_square, scale_factor=1.2, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 步骤4：开平方
        eq4 = MathTex(
            r"x + 3 = \pm 2",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 1.0)
        
        step4_label = Text(
            "④ 开平方",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(eq4, LEFT, buff=0.5)
        
        self.play(
            TransformMatchingTex(eq3.copy(), eq4),
            FadeIn(step4_label),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 步骤5：解出x
        eq5 = MathTex(
            r"x = -3 \pm 2",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 2.5)
        
        step5_label = Text(
            "⑤ 移项",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(eq5, LEFT, buff=0.5)
        
        self.play(
            TransformMatchingTex(eq4.copy(), eq5),
            FadeIn(step5_label),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 最终答案
        answer = MathTex(
            r"x_1 = -1, \quad x_2 = -5",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 4.0)
        
        answer_rect = SurroundingRectangle(
            answer,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Write(answer), run_time=1.0)
        self.play(Create(answer_rect), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(eq0),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3),
            FadeOut(eq4),
            FadeOut(eq5),
            FadeOut(step1_label),
            FadeOut(step2_label),
            FadeOut(step3_label),
            FadeOut(step4_label),
            FadeOut(step5_label),
            FadeOut(answer),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景6: 例题2 - 2x² - 8x + 3 = 0 (53-68秒)"""
        # 例题标签
        example_label = Text(
            "例题 2：系数 ≠ 1",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 原方程
        eq0 = MathTex(
            r"{{ 2 }}x^2 - 8x + 3 = 0",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(eq0), run_time=0.8)
        self.wait(0.3)
        
        # 高亮系数2
        coeff = eq0.get_part_by_tex(r"2")
        self.play(
            Indicate(coeff, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 提示先除以2
        hint_divide = Text(
            "先除以 2",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(eq0, RIGHT, buff=0.5)
        
        self.play(FadeIn(hint_divide, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.5)
        
        # 化简
        eq1 = MathTex(
            r"x^2 - 4x + \frac{3}{2} = 0",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.0)
        
        self.play(
            TransformMatchingTex(eq0.copy(), eq1),
            FadeOut(hint_divide),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 移项
        eq2 = MathTex(
            r"x^2 - 4x = -\frac{3}{2}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.5)
        
        self.play(
            TransformMatchingTex(eq1.copy(), eq2),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 提示计算
        hint_calc = MathTex(
            r"\left(\frac{-4}{2}\right)^2 = 4",
            font_size=self.FONT_SIZE_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(eq2, RIGHT, buff=0.5)
        
        self.play(Write(hint_calc), run_time=0.8)
        self.wait(0.5)
        
        # 两边加4
        eq3 = MathTex(
            r"x^2 - 4x {{ + 4 }} = -\frac{3}{2} {{ + 4 }}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.0)
        
        eq3.get_part_by_tex(r"+ 4").set_color(self.COLOR_GEOMETRY)
        
        self.play(
            TransformMatchingTex(eq2.copy(), eq3),
            FadeOut(hint_calc),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 配方
        eq4 = MathTex(
            r"(x-2)^2 = \frac{5}{2}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.5)
        
        self.play(
            TransformMatchingTex(eq3.copy(), eq4),
            run_time=1.2
        )
        self.wait(0.5)
        
        # 开平方
        eq5 = MathTex(
            r"x - 2 = \pm\sqrt{\frac{5}{2}}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 2.0)
        
        self.play(
            TransformMatchingTex(eq4.copy(), eq5),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 最终答案
        answer = MathTex(
            r"x = 2 \pm \sqrt{\frac{5}{2}}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3.5)
        
        answer_rect = SurroundingRectangle(
            answer,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Write(answer), run_time=1.0)
        self.play(Create(answer_rect), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(eq0),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3),
            FadeOut(eq4),
            FadeOut(eq5),
            FadeOut(answer),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_applications(self):
        """场景7: 配方法的应用 (68-75秒)"""
        # 标题
        title = Text(
            "配方法的意义",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 应用卡片
        app1 = VGroup(
            Text("①", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_SECONDARY),
            Text(
                "推导求根公式",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        app2 = VGroup(
            Text("②", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_SECONDARY),
            Text(
                "化为顶点式 y=a(x-h)²+k",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        
        app3 = VGroup(
            Text("③", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_SECONDARY),
            Text(
                "求二次函数最值",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            )
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        
        self.play(FadeIn(app1, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(app2, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(app3, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.5)
        
        # 闪烁强调
        all_apps = VGroup(app1, app2, app3)
        self.play(
            Flash(all_apps, color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(app1),
            FadeOut(app2),
            FadeOut(app3),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景8: 总结与关注 (75-90秒)"""
        # 总结标题
        summary_title = Text(
            "配方法要点",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点
        def create_point(icon, text):
            circle = Circle(radius=0.18, color=self.COLOR_PRIMARY, fill_opacity=1)
            icon_text = Text(
                icon,
                font=self.FONT_CHINESE,
                font_size=18,
                color=WHITE
            ).move_to(circle.get_center())
            content = Text(
                text,
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_SMALL,
                color=WHITE
            )
            point = VGroup(circle, icon_text, content).arrange(RIGHT, buff=0.3)
            point.shift(LEFT * 10)
            return point
        
        point1 = create_point("1", "移项 → 系数化1")
        point2 = create_point("2", "关键：加 (p/2)²")
        point3 = create_point("3", "配成 (x+m)² 形式")
        point4 = create_point("4", "开平方求解")
        
        point1.move_to(UP * 3.5)
        point2.move_to(UP * 2.0)
        point3.move_to(UP * 0.5)
        point4.move_to(DOWN * 1.0)
        
        # 依次滑入
        for point in [point1, point2, point3, point4]:
            self.play(point.animate.shift(RIGHT * 10), run_time=0.6)
            self.wait(0.2)
        
        # 闪烁
        all_points = VGroup(point1, point2, point3, point4)
        self.play(
            Flash(all_points, color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我, 掌握解题技巧!",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰 - 正方形旋转
        decorations = VGroup(*[
            Square(
                side_length=0.3,
                color=self.COLOR_GEOMETRY,
                fill_opacity=0.6
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([
                    np.cos(i * PI / 3),
                    np.sin(i * PI / 3),
                    0
                ])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(
            Rotate(decorations, angle=PI, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(all_points),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# ==================== 渲染命令 ====================
"""
快速预览 (480p):
manim -pql completing_the_square.py CompletingTheSquare

高质量渲染 (1080p):
manim -qh completing_the_square.py CompletingTheSquare

4K质量 (2160p):
manim -qk completing_the_square.py CompletingTheSquare

GIF格式:
manim -pql --format gif completing_the_square.py CompletingTheSquare
"""