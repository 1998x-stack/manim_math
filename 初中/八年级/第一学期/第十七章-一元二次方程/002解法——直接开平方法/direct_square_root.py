"""
直接开平方法 - Manim 教学动画
Direct Square Root Method for Solving Quadratic Equations

目标受众: 八年级学生
视频格式: TikTok 竖屏 (1080×1920)
时长: 60-75秒

作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DirectSquareRootMethod(Scene):
    """
    直接开平方法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 引入方法名称
    3. 基本公式推导 (x² = 9)
    4. 通用公式展示
    5. 实例演示1 - (x+2)² = 16
    6. 实例演示2 - x² + 6x + 9 = 25
    7. 总结与关注
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
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 40
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 24
        self.FONT_SIZE_SMALL = 20
        self.FONT_SIZE_FORMULA = 32
        
        # 执行动画序列
        self.show_opening()
        self.show_method_introduction()
        self.show_basic_derivation()
        self.show_general_formula()
        self.show_example_1()
        self.show_example_2()
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
        
        # 钩子问题
        hook_question = MathTex(
            r"x^2 = 9",
            font_size=56,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        hook_text = Text(
            "x 等于多少？",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=WHITE
        ).next_to(hook_question, DOWN, buff=0.5)
        
        self.play(Write(hook_question), run_time=0.8)
        self.play(FadeIn(hook_text, shift=UP * 0.2), run_time=0.5)
        
        # 思考气泡
        thinking_bubble = VGroup(
            Circle(radius=0.3, color=WHITE, fill_opacity=0.1).shift(RIGHT * 2 + UP * 2),
            Circle(radius=0.2, color=WHITE, fill_opacity=0.1).shift(RIGHT * 2.5 + UP * 1.5),
            Circle(radius=0.15, color=WHITE, fill_opacity=0.1).shift(RIGHT * 2.8 + UP * 1.2),
        )
        
        question_mark = Text(
            "?",
            font=self.FONT_CHINESE,
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(RIGHT * 2 + UP * 2)
        
        self.play(
            FadeIn(thinking_bubble, scale=0.5),
            FadeIn(question_mark, scale=0.5),
            run_time=0.5
        )
        
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.4), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hook_text),
            FadeOut(thinking_bubble),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_method_introduction(self):
        """场景2: 引入方法名称 (5-10秒)"""
        # 标题
        title = Text(
            "直接开平方法",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5)
        
        # 副标题
        subtitle = Text(
            "Direct Square Root Method",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.3)
        
        # 说明文字
        description = Text(
            "快速解决特殊形式的一元二次方程",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_B
        ).move_to(UP * 3)
        
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.play(FadeIn(description, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(description),
            run_time=0.5
        )
    
    def show_basic_derivation(self):
        """场景3: 基本公式推导 (10-25秒)"""
        # 起始公式
        eq1 = MathTex(
            r"x^2 = 9",
            font_size=self.FONT_SIZE_FORMULA + 8,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4)
        
        self.play(Write(eq1), run_time=1.0)
        self.wait(0.5)
        
        # 箭头和提示
        arrow1 = Arrow(
            start=UP * 3,
            end=UP * 2,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        hint1 = Text(
            "两边开平方",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(arrow1, RIGHT, buff=0.3)
        
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(hint1, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 开平方后
        eq2 = MathTex(
            r"x = {{ \pm }} \sqrt{9}",
            font_size=self.FONT_SIZE_FORMULA + 8,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1)
        
        self.play(
            TransformMatchingTex(eq1.copy(), eq2),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 强调 ± 符号
        plus_minus = eq2.get_part_by_tex(r"\pm")
        self.play(
            Indicate(plus_minus, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 解释框
        explanation_box = VGroup(
            RoundedRectangle(
                width=3.5,
                height=1.0,
                corner_radius=0.1,
                color=self.COLOR_HIGHLIGHT,
                fill_opacity=0.1
            ),
            Text(
                "正负两个解",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=self.COLOR_HIGHLIGHT
            )
        ).arrange(DOWN, buff=0.1).next_to(eq2, RIGHT, buff=0.8)
        
        self.play(FadeIn(explanation_box, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.8)
        
        # 计算结果
        eq3 = MathTex(
            r"x = {{ \pm }} 3",
            font_size=self.FONT_SIZE_FORMULA + 8,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 1)
        
        self.play(
            TransformMatchingTex(eq2.copy(), eq3),
            run_time=1.0
        )
        
        # 答案框高亮
        answer_rect = SurroundingRectangle(
            eq3,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(answer_rect), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(eq1),
            FadeOut(arrow1),
            FadeOut(hint1),
            FadeOut(eq2),
            FadeOut(explanation_box),
            FadeOut(eq3),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_general_formula(self):
        """场景4: 通用公式展示 (25-35秒)"""
        # 公式框
        formula_box = RoundedRectangle(
            width=7.5,
            height=2.5,
            corner_radius=0.15,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 3.5)
        
        self.play(Create(formula_box), run_time=0.8)
        
        # 通用公式
        general_formula = MathTex(
            r"(x+m)^2 = n",
            font_size=self.FONT_SIZE_FORMULA + 4,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.2)
        
        self.play(Write(general_formula), run_time=1.0)
        
        # 双箭头
        double_arrow = DoubleArrow(
            start=UP * 3.5 + LEFT * 2,
            end=UP * 3.5 + RIGHT * 2,
            color=self.COLOR_SECONDARY,
            stroke_width=4,
            buff=0
        ).move_to(UP * 3.3)
        
        self.play(GrowArrow(double_arrow), run_time=0.8)
        
        # 解的形式
        solution_form = MathTex(
            r"x = -m \pm \sqrt{n}",
            font_size=self.FONT_SIZE_FORMULA + 4,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.6)
        
        self.play(Write(solution_form), run_time=1.2)
        self.wait(0.5)
        
        # 条件框
        condition_box = RoundedRectangle(
            width=3.0,
            height=0.8,
            corner_radius=0.1,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.1
        ).move_to(UP * 1.5)
        
        condition_text = MathTex(
            r"n \geq 0",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(condition_box.get_center())
        
        condition_label = Text(
            "重要条件:",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(condition_box, UP, buff=0.2)
        
        self.play(
            FadeIn(condition_box),
            FadeIn(condition_label),
            run_time=0.5
        )
        self.play(Write(condition_text), run_time=0.8)
        self.wait(0.8)
        
        # 整体闪烁强调
        emphasis_group = VGroup(formula_box, general_formula, double_arrow, solution_form)
        self.play(
            Flash(emphasis_group, color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(formula_box),
            FadeOut(general_formula),
            FadeOut(double_arrow),
            FadeOut(solution_form),
            FadeOut(condition_box),
            FadeOut(condition_text),
            FadeOut(condition_label),
            run_time=0.6
        )
    
    def show_example_1(self):
        """场景5: 实例演示1 - (x+2)² = 16 (35-48秒)"""
        # 例题标签
        example_label = Text(
            "例题 1",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 问题
        problem = MathTex(
            r"(x+2)^2 = 16",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(Write(problem), run_time=0.8)
        self.wait(0.5)
        
        # 步骤1: 开平方
        step1_label = Text(
            "步骤1: 开平方",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 3.2)
        
        step1 = MathTex(
            r"x+2 = \pm 4",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(step1_label, shift=DOWN * 0.2), run_time=0.4)
        self.play(
            TransformMatchingTex(problem.copy(), step1),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 步骤2: 移项
        step2_label = Text(
            "步骤2: 移项",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 1.2)
        
        step2 = MathTex(
            r"x = -2 \pm 4",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(step2_label, shift=DOWN * 0.2), run_time=0.4)
        self.play(
            TransformMatchingTex(step1.copy(), step2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 分离两解
        step3_label = Text(
            "步骤3: 计算",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(DOWN * 0.8)
        
        solutions = MathTex(
            r"x_1 = 2, \quad x_2 = -6",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(step3_label, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(solutions), run_time=1.0)
        
        # 答案框
        answer_rect = SurroundingRectangle(
            solutions,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Create(answer_rect), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(problem),
            FadeOut(step1_label),
            FadeOut(step1),
            FadeOut(step2_label),
            FadeOut(step2),
            FadeOut(step3_label),
            FadeOut(solutions),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景6: 实例演示2 - x² + 6x + 9 = 25 (48-60秒)"""
        # 例题标签
        example_label = Text(
            "例题 2",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 原始方程
        original_eq = MathTex(
            r"{{ x^2 + 6x + 9 }} = 25",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(Write(original_eq), run_time=0.8)
        self.wait(0.3)
        
        # 高亮左侧
        left_side = original_eq.get_part_by_tex(r"x^2 + 6x + 9")
        self.play(
            Indicate(left_side, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 提示完全平方式
        hint_perfect = Text(
            "识别: 完全平方式",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.2)
        
        self.play(FadeIn(hint_perfect, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 变换为完全平方形式
        transformed = MathTex(
            r"(x+3)^2 = 25",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.3)
        
        self.play(
            TransformMatchingTex(original_eq.copy(), transformed),
            run_time=1.0
        )
        self.play(FadeOut(hint_perfect), run_time=0.3)
        self.wait(0.5)
        
        # 开平方
        sqrt_step = MathTex(
            r"x+3 = \pm 5",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.0)
        
        self.play(
            TransformMatchingTex(transformed.copy(), sqrt_step),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 移项
        solve_step = MathTex(
            r"x = -3 \pm 5",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.2)
        
        self.play(
            TransformMatchingTex(sqrt_step.copy(), solve_step),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 最终答案
        final_answers = MathTex(
            r"x_1 = 2, \quad x_2 = -8",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.5)
        
        self.play(Write(final_answers), run_time=1.0)
        
        # 答案框
        answer_rect = SurroundingRectangle(
            final_answers,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Create(answer_rect), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(original_eq),
            FadeOut(transformed),
            FadeOut(sqrt_step),
            FadeOut(solve_step),
            FadeOut(final_answers),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与关注 (60-75秒)"""
        # 总结标题
        summary_title = Text(
            "方法要点",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点1
        point1 = VGroup(
            Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "形式: (x+m)² = n",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        point1.shift(LEFT * 10)
        
        # 要点2
        point2 = VGroup(
            Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "步骤: 开平方 → 移项",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.0)
        point2.shift(LEFT * 10)
        
        # 要点3
        point3 = VGroup(
            Circle(radius=0.15, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "注意: n ≥ 0, 两个解",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        point3.shift(LEFT * 10)
        
        # 依次滑入
        self.play(point1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(point2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(point3.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.5)
        
        # 要点闪烁
        all_points = VGroup(point1, point2, point3)
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
        ).move_to(DOWN * 2)
        
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
            "关注我, 学更多数学技巧!",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰元素 - 小圆圈旋转
        decorations = VGroup(*[
            Circle(
                radius=0.2,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0])
            )
            for i in range(8)
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
manim -pql direct_square_root.py DirectSquareRootMethod

高质量渲染 (1080p):
manim -qh direct_square_root.py DirectSquareRootMethod

4K质量 (2160p):
manim -qk direct_square_root.py DirectSquareRootMethod

GIF格式:
manim -pql --format gif direct_square_root.py DirectSquareRootMethod
"""