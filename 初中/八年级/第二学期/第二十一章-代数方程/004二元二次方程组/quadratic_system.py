"""
二元二次方程组教学动画 - Quadratic System of Equations
使用 Manim 创建的八年级代数教学视频

内容: 二元二次方程组的代入消元法
目标观众: 八年级学生
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


class QuadraticSystemSolver(Scene):
    """
    二元二次方程组求解动画场景
    
    示例题目:
    { x² + y² = 25
    { x + y = 7
    
    场景顺序:
    1. 开场钩子
    2. 识别方程组特征
    3. 代入消元 - 解出y
    4. 代入消元 - 代入并化简
    5. 求解一元二次方程
    6. 回代求y并总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主方程
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 次方程
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键步骤
        self.COLOR_SOLUTION = "#2ecc71"     # 绿色 - 解
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助说明
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_identification()
        self.show_solve_for_y()
        self.show_substitution()
        self.show_solve_quadratic()
        self.show_back_substitution()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 引出问题"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "两个未知数，两个方程，怎么解？",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        
        # 副标题
        subtitle = Text(
            "二元二次方程组",
            font=self.FONT_CHINESE,
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 方程组 - 使用大括号
        eq1 = MathTex(
            r"x^2 + y^2 = 25",
            font_size=36,
            color=self.COLOR_PRIMARY
        )
        eq2 = MathTex(
            r"x + y = 7",
            font_size=36,
            color=self.COLOR_SECONDARY
        )
        
        # 左大括号
        brace = MathTex(r"\left\{", font_size=60)
        
        # 组合方程组
        eq1.next_to(brace, RIGHT, buff=0.3)
        eq2.next_to(eq1, DOWN, aligned_edge=LEFT, buff=0.4)
        brace.next_to(eq1, LEFT, buff=0.2)
        
        self.equation_system = VGroup(brace, eq1, eq2).move_to(UP * 2)
        
        self.play(Write(self.equation_system), run_time=1.5)
        
        # 高亮二次项
        self.wait(0.5)
        quadratic_terms = VGroup(
            eq1[0][0:2],  # x^2
            eq1[0][3:5]   # y^2
        )
        self.play(Indicate(quadratic_terms, scale_factor=1.2, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        
        self.wait(1.0)
        
        # 清理钩子
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            run_time=0.5
        )
        
        # 保存方程以便后续使用
        self.eq1 = eq1
        self.eq2 = eq2
        self.brace = brace
    
    def show_identification(self):
        """场景2: 识别方程组特征"""
        # 标题
        title = Text(
            "识别特征",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        
        # 圈出第一个方程的二次项
        rect1 = SurroundingRectangle(
            self.eq1,
            color=self.COLOR_PRIMARY,
            buff=0.15,
            corner_radius=0.1
        )
        
        label1 = Text(
            "二次方程 (最高次数为2)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(rect1, DOWN, buff=0.3)
        
        self.play(Create(rect1), run_time=0.6)
        self.play(FadeIn(label1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 圈出第二个方程
        rect2 = SurroundingRectangle(
            self.eq2,
            color=self.COLOR_SECONDARY,
            buff=0.15,
            corner_radius=0.1
        )
        
        label2 = Text(
            "一次方程 (更简单)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(rect2, DOWN, buff=0.3)
        
        self.play(
            FadeOut(rect1),
            FadeOut(label1),
            run_time=0.3
        )
        self.play(Create(rect2), run_time=0.6)
        self.play(FadeIn(label2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 策略说明
        strategy = Text(
            "策略: 从简单方程入手!",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(strategy, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rect2),
            FadeOut(label2),
            FadeOut(strategy),
            run_time=0.5
        )
    
    def show_solve_for_y(self):
        """场景3: 代入消元 - 解出y"""
        # 步骤标题
        step_title = Text(
            "Step 1: 解出一个未知数",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 高亮第二个方程
        self.play(
            Indicate(self.eq2, scale_factor=1.15, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 说明
        explanation = Text(
            "从 x + y = 7 解出 y",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.5)
        
        # 移项过程
        eq2_copy = self.eq2.copy()
        self.play(eq2_copy.animate.move_to(DOWN * 0.5), run_time=0.8)
        
        # 箭头
        arrow = Arrow(
            eq2_copy.get_bottom() + DOWN * 0.2,
            eq2_copy.get_bottom() + DOWN * 0.8,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 移项后的结果
        y_expr = MathTex(
            r"y = 7 - x",
            font_size=36,
            color=self.COLOR_SOLUTION
        ).move_to(DOWN * 1.8)
        
        self.play(TransformMatchingTex(eq2_copy, y_expr), run_time=1.0)
        
        # 框住结果
        box = SurroundingRectangle(
            y_expr,
            color=self.COLOR_SOLUTION,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(box), run_time=0.6)
        self.wait(1.5)
        
        # 移动到侧边保存
        saved_y = VGroup(y_expr, box).copy()
        self.play(
            saved_y.animate.scale(0.7).move_to(RIGHT * 3 + UP * 4),
            FadeOut(arrow),
            FadeOut(explanation),
            FadeOut(step_title),
            run_time=0.8
        )
        
        # 清理原位置的y表达式
        self.play(
            FadeOut(y_expr),
            FadeOut(box),
            run_time=0.3
        )
        
        # 保存以供后续使用
        self.saved_y_expr = saved_y
    
    def show_substitution(self):
        """场景4: 代入消元 - 代入并化简"""
        # 步骤标题
        step_title = Text(
            "Step 2: 代入第一个方程",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 高亮第一个方程
        self.play(
            Indicate(self.eq1, scale_factor=1.15, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 高亮保存的y表达式
        self.play(
            Indicate(self.saved_y_expr, scale_factor=1.2, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 复制第一个方程到中心
        eq1_work = self.eq1.copy()
        self.play(eq1_work.animate.move_to(UP * 0.5), run_time=0.8)
        
        # 说明代入
        sub_text = Text(
            "将 y = 7 - x 代入",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(sub_text), run_time=0.5)
        self.wait(0.5)
        
        # 箭头指示
        arrow = Arrow(
            UP * 0.2,
            DOWN * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        self.play(GrowArrow(arrow), run_time=0.4)
        
        # 代入后的方程
        substituted = MathTex(
            r"x^2 + (7-x)^2 = 25",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1.8)
        
        self.play(
            TransformMatchingTex(eq1_work, substituted),
            FadeOut(arrow),
            FadeOut(sub_text),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 展开 (7-x)²
        expand_text = Text(
            "展开 (7-x)²",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(expand_text), run_time=0.5)
        
        expanded = MathTex(
            r"x^2 + 49 - 14x + x^2 = 25",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 2.8)
        
        self.play(
            TransformMatchingTex(substituted, expanded),
            run_time=1.2
        )
        self.wait(1.0)
        
        # 合并同类项
        self.play(
            FadeOut(expand_text),
            run_time=0.3
        )
        
        combine_text = Text(
            "合并同类项",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(combine_text), run_time=0.5)
        
        # 高亮x²项
        x2_terms = VGroup(
            expanded[0][0:2],   # 第一个x^2
            expanded[0][12:14]  # 第二个x^2
        )
        self.play(Indicate(x2_terms, color=YELLOW), run_time=0.8)
        
        combined = MathTex(
            r"2x^2 - 14x + 49 = 25",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 3.8)
        
        self.play(
            TransformMatchingTex(expanded, combined),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 移项
        self.play(FadeOut(combine_text), run_time=0.3)
        
        simplified1 = MathTex(
            r"2x^2 - 14x + 24 = 0",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 4.8)
        
        self.play(
            TransformMatchingTex(combined, simplified1),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 化简（除以2）
        divide_text = Text(
            "÷ 2",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(simplified1, RIGHT, buff=0.3)
        
        self.play(FadeIn(divide_text, shift=LEFT * 0.2), run_time=0.4)
        
        self.quadratic_eq = MathTex(
            r"x^2 - 7x + 12 = 0",
            font_size=36,
            color=self.COLOR_SOLUTION
        ).move_to(DOWN * 5.8)
        
        self.play(
            TransformMatchingTex(simplified1, self.quadratic_eq),
            FadeOut(divide_text),
            run_time=1.0
        )
        
        # 框住最终方程
        final_box = SurroundingRectangle(
            self.quadratic_eq,
            color=self.COLOR_SOLUTION,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(final_box), run_time=0.6)
        
        # 庆祝文字
        success_text = Text(
            "降次成功！一元二次方程",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(FadeIn(success_text, scale=1.1), run_time=0.6)
        self.wait(2.0)
        
        # 清理并准备下一场景
        self.play(
            FadeOut(step_title),
            FadeOut(success_text),
            FadeOut(final_box),
            run_time=0.5
        )
        
        # 将方程移到中心
        self.play(
            self.quadratic_eq.animate.move_to(UP * 1.5),
            run_time=0.8
        )
    
    def show_solve_quadratic(self):
        """场景5: 求解一元二次方程"""
        # 步骤标题
        step_title = Text(
            "Step 3: 因式分解",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 提示寻找因数
        hint = Text(
            "寻找两数: 和为 -7，积为 12",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint), run_time=0.6)
        self.wait(1.0)
        
        # 闪现 -3 和 -4
        factors = MathTex(
            r"-3, \quad -4",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(factors, scale=1.2), run_time=0.6)
        self.wait(0.8)
        
        # 验证
        check1 = MathTex(
            r"(-3) + (-4) = -7 \quad \checkmark",
            font_size=24,
            color=GREEN
        ).move_to(DOWN * 2.5)
        
        check2 = MathTex(
            r"(-3) \times (-4) = 12 \quad \checkmark",
            font_size=24,
            color=GREEN
        ).move_to(DOWN * 3.2)
        
        self.play(
            FadeIn(check1, shift=UP * 0.2),
            FadeIn(check2, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hint),
            FadeOut(factors),
            FadeOut(check1),
            FadeOut(check2),
            run_time=0.5
        )
        
        # 因式分解
        factored = MathTex(
            r"(x - 3)(x - 4) = 0",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(TransformMatchingTex(self.quadratic_eq.copy(), factored), run_time=1.2)
        self.wait(0.8)
        
        # 箭头
        arrow = Arrow(
            DOWN * 1,
            DOWN * 2,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 解
        solution_x = MathTex(
            r"x = 3 \text{ or } x = 4",
            font_size=36,
            color=self.COLOR_SOLUTION
        ).move_to(DOWN * 2.8)
        
        self.play(Write(solution_x), run_time=1.0)
        
        # 框住解
        sol_box = SurroundingRectangle(
            solution_x,
            color=self.COLOR_SOLUTION,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(sol_box), run_time=0.6)
        self.wait(1.5)
        
        # 移到侧边保存
        self.saved_x_sols = VGroup(solution_x, sol_box).copy()
        self.play(
            self.saved_x_sols.animate.scale(0.65).move_to(RIGHT * 3 + UP * 1.5),
            FadeOut(step_title),
            FadeOut(self.quadratic_eq),
            FadeOut(factored),
            FadeOut(arrow),
            FadeOut(solution_x),
            FadeOut(sol_box),
            run_time=0.8
        )
    
    def show_back_substitution(self):
        """场景6: 回代求y并总结"""
        # 步骤标题
        step_title = Text(
            "Step 4: 回代求 y",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 回忆 y = 7 - x
        self.play(
            Indicate(self.saved_y_expr, scale_factor=1.2, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 提取 y = 7 - x 到中心
        y_formula = MathTex(
            r"y = 7 - x",
            font_size=32,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(TransformFromCopy(self.saved_y_expr, y_formula), run_time=0.8)
        
        # 当 x = 3
        case1_title = Text(
            "当 x = 3:",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.8 + LEFT * 2)
        
        self.play(FadeIn(case1_title, shift=RIGHT * 0.2), run_time=0.5)
        
        # 箭头
        arrow1 = Arrow(
            self.saved_x_sols.get_left() + LEFT * 0.3,
            case1_title.get_right() + RIGHT * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=3
        )
        self.play(GrowArrow(arrow1), run_time=0.5)
        
        calc1 = MathTex(
            r"y = 7 - 3 = 4",
            font_size=28,
            color=WHITE
        ).next_to(case1_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(calc1), run_time=0.8)
        
        sol1 = MathTex(
            r"(3, 4)",
            font_size=32,
            color=self.COLOR_SOLUTION
        ).next_to(calc1, DOWN, buff=0.4)
        
        sol1_box = SurroundingRectangle(
            sol1,
            color=self.COLOR_SOLUTION,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(sol1, scale=1.1),
            Create(sol1_box),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 当 x = 4
        case2_title = Text(
            "当 x = 4:",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 2 + LEFT * 2)
        
        self.play(
            FadeIn(case2_title, shift=RIGHT * 0.2),
            FadeOut(arrow1),
            run_time=0.5
        )
        
        arrow2 = Arrow(
            self.saved_x_sols.get_left() + LEFT * 0.3,
            case2_title.get_right() + RIGHT * 0.3,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=3
        )
        self.play(GrowArrow(arrow2), run_time=0.5)
        
        calc2 = MathTex(
            r"y = 7 - 4 = 3",
            font_size=28,
            color=WHITE
        ).next_to(case2_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(calc2), run_time=0.8)
        
        sol2 = MathTex(
            r"(4, 3)",
            font_size=32,
            color=self.COLOR_SOLUTION
        ).next_to(calc2, DOWN, buff=0.4)
        
        sol2_box = SurroundingRectangle(
            sol2,
            color=self.COLOR_SOLUTION,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(
            FadeIn(sol2, scale=1.1),
            Create(sol2_box),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 最终解集
        final_title = Text(
            "解集:",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        final_sols = MathTex(
            r"\{(3, 4), \quad (4, 3)\}",
            font_size=36,
            color=self.COLOR_SOLUTION
        ).next_to(final_title, RIGHT, buff=0.3)
        
        final_box = SurroundingRectangle(
            VGroup(final_title, final_sols),
            color=self.COLOR_SOLUTION,
            buff=0.25,
            corner_radius=0.15
        )
        
        self.play(
            FadeIn(final_title),
            FadeIn(final_sols),
            Create(final_box),
            run_time=1.0
        )
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(y_formula),
            FadeOut(case1_title),
            FadeOut(calc1),
            FadeOut(sol1),
            FadeOut(sol1_box),
            FadeOut(case2_title),
            FadeOut(calc2),
            FadeOut(sol2),
            FadeOut(sol2_box),
            FadeOut(arrow2),
            FadeOut(self.saved_y_expr),
            FadeOut(self.saved_x_sols),
            FadeOut(self.equation_system),
            FadeOut(final_title),
            FadeOut(final_sols),
            FadeOut(final_box),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 方法总结
        summary_title = Text(
            "代入消元三步走",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(FadeIn(summary_title, scale=1.1), run_time=0.8)
        
        # 步骤卡片
        steps = VGroup(
            Text("① 解出一个未知数", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("② 代入另一个方程", font=self.FONT_CHINESE, font_size=26, color=WHITE),
            Text("③ 回代求另一个未知数", font=self.FONT_CHINESE, font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 1)
        
        for i, step in enumerate(steps):
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.4)
            if i < len(steps) - 1:
                self.wait(0.2)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(steps),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=44,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多解题技巧！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 装饰 - 小方程式旋转
        decorations = VGroup()
        equations_deco = [
            r"x + y",
            r"x^2",
            r"y^2",
            r"xy"
        ]
        
        for i, eq in enumerate(equations_deco):
            deco = MathTex(eq, font_size=28, color=self.COLOR_PRIMARY)
            angle = i * PI / 2
            deco.move_to(2.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 3)
            decorations.add(deco)
        
        self.play(
            *[FadeIn(d, scale=0.5) for d in decorations],
            run_time=0.6
        )
        
        self.play(
            Rotate(decorations, angle=2*PI, run_time=2, rate_func=linear),
            run_time=2
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql quadratic_system.py QuadraticSystemSolver  # 快速预览
# manim -qh quadratic_system.py QuadraticSystemSolver   # 高质量渲染