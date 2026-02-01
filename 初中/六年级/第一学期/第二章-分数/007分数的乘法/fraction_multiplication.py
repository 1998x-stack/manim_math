"""
分数的乘法 (Fraction Multiplication) - Manim 教学动画
使用 Manim 创建的中学数学教学视频

内容: 分数乘法法则、可视化理解、运算技巧
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


class FractionMultiplication(Scene):
    """
    分数乘法教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 视觉化理解 - 用网格展示
    3. 乘法法则 - 核心规则
    4. 更多例子 - 巩固练习
    5. 运算律 - 数学性质
    6. 技巧总结 - 计算技巧
    7. 结尾关注 - 总结回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_FRACTION_1 = "#3498db"    # 蓝色 - 第一个分数
        self.COLOR_FRACTION_2 = "#e74c3c"    # 红色 - 第二个分数
        self.COLOR_RESULT = "#2ecc71"        # 绿色 - 结果
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_GRID = WHITE              # 白色 - 网格
        self.COLOR_SIMPLIFY = "#9b59b6"      # 紫色 - 约分
        
        # 字体大小规范
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_FORMULA = 32
        self.FONT_LABEL = 20
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_visualization()
        self.scene_3_multiplication_rule()
        self.scene_4_more_examples()
        self.scene_5_laws()
        self.scene_6_tips()
        self.scene_7_outro()
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "分数相乘，怎么算?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE + 4,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 示例分数: 2/3 × 3/4
        frac_1 = MathTex(
            r"\frac{2}{3}",
            font_size=self.FONT_FORMULA * 1.5,
            color=self.COLOR_FRACTION_1
        ).move_to(LEFT * 1.5 + UP * 3.5)
        
        times_sign = MathTex(
            r"\times",
            font_size=self.FONT_FORMULA * 1.5,
            color=WHITE
        ).move_to(UP * 3.5)
        
        frac_2 = MathTex(
            r"\frac{3}{4}",
            font_size=self.FONT_FORMULA * 1.5,
            color=self.COLOR_FRACTION_2
        ).move_to(RIGHT * 1.5 + UP * 3.5)
        
        question = MathTex(
            r"= \ ?",
            font_size=self.FONT_FORMULA * 1.5,
            color=self.COLOR_HIGHLIGHT
        ).move_to(RIGHT * 3.2 + UP * 3.5)
        
        self.play(FadeIn(frac_1, scale=1.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(times_sign), run_time=0.3)
        self.wait(0.2)
        self.play(FadeIn(frac_2, scale=1.2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(question, scale=1.3), run_time=0.4)
        
        # 闪烁问号
        self.play(
            Flash(question, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        # 提示文字
        hint = Text(
            "很简单! 让我来教你",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 保存公式组用于后续场景
        self.formula_group = VGroup(frac_1, times_sign, frac_2)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hint),
            FadeOut(question),
            run_time=0.5
        )
    
    def scene_2_visualization(self):
        """场景2: 视觉化理解 - 用矩形网格展示"""
        # 公式移到顶部
        self.play(
            self.formula_group.animate.scale(0.7).move_to(UP * 5.5),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "视觉化理解",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建矩形网格 (3行×4列)
        grid_width = 3.0
        grid_height = 2.0
        grid_position = UP * 0.5
        
        # 外框
        rectangle = Rectangle(
            width=grid_width,
            height=grid_height,
            color=self.COLOR_GRID,
            stroke_width=3
        ).move_to(grid_position)
        
        self.play(Create(rectangle), run_time=1.0)
        
        # 水平分割线 (分成3行)
        h_lines = VGroup()
        for i in range(1, 3):
            y_pos = grid_position[1] + grid_height/2 - i * grid_height/3
            line = Line(
                start=np.array([grid_position[0] - grid_width/2, y_pos, 0]),
                end=np.array([grid_position[0] + grid_width/2, y_pos, 0]),
                color=self.COLOR_GRID,
                stroke_width=2
            )
            h_lines.add(line)
        
        self.play(Create(h_lines), run_time=1.0)
        
        # 阴影 2/3 (上面2行)
        shade_2_3_parts = VGroup()
        for i in range(2):  # 前2行
            y_pos = grid_position[1] + grid_height/2 - (i + 0.5) * grid_height/3
            shade = Rectangle(
                width=grid_width - 0.02,
                height=grid_height/3 - 0.02,
                fill_color=self.COLOR_FRACTION_1,
                fill_opacity=0.4,
                stroke_width=0
            ).move_to(np.array([grid_position[0], y_pos, 0]))
            shade_2_3_parts.add(shade)
        
        self.play(FadeIn(shade_2_3_parts), run_time=0.5)
        
        # 说明1
        explain_1 = Text(
            "先取 2/3 (上面2行)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FRACTION_1
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explain_1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 垂直分割线 (分成4列)
        v_lines = VGroup()
        for i in range(1, 4):
            x_pos = grid_position[0] - grid_width/2 + i * grid_width/4
            line = Line(
                start=np.array([x_pos, grid_position[1] + grid_height/2, 0]),
                end=np.array([x_pos, grid_position[1] - grid_height/2, 0]),
                color=self.COLOR_GRID,
                stroke_width=2
            )
            v_lines.add(line)
        
        self.play(Create(v_lines), run_time=1.0)
        
        # 阴影 3/4 (左边3列的上面2行) - 重叠部分
        shade_3_4_parts = VGroup()
        for i in range(2):  # 前2行
            for j in range(3):  # 前3列
                x_pos = grid_position[0] - grid_width/2 + (j + 0.5) * grid_width/4
                y_pos = grid_position[1] + grid_height/2 - (i + 0.5) * grid_height/3
                shade = Rectangle(
                    width=grid_width/4 - 0.02,
                    height=grid_height/3 - 0.02,
                    fill_color=self.COLOR_FRACTION_2,
                    fill_opacity=0.3,
                    stroke_width=0
                ).move_to(np.array([x_pos, y_pos, 0]))
                shade_3_4_parts.add(shade)
        
        self.play(FadeIn(shade_3_4_parts), run_time=0.5)
        
        # 说明2
        explain_2 = Text(
            "再从中取 3/4 (左边3列)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FRACTION_2
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 高亮重叠区域 (6个小格子)
        self.play(
            Indicate(shade_3_4_parts, color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        # 说明3
        explain_3_chinese = Text(
            "重叠部分 = ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        explain_3_math = MathTex(
            r"\frac{6}{12} = \frac{1}{2}",
            font_size=self.FONT_BODY + 4,
            color=self.COLOR_RESULT
        )
        explain_3 = VGroup(explain_3_chinese, explain_3_math).arrange(RIGHT, buff=0.2)
        explain_3.move_to(DOWN * 5)
        
        self.play(FadeIn(explain_3, shift=UP * 0.2), run_time=0.6)
        
        # 答案
        answer = MathTex(
            r"\frac{2}{3} \times \frac{3}{4} = \frac{1}{2}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(answer, scale=1.2), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(rectangle),
            FadeOut(h_lines),
            FadeOut(v_lines),
            FadeOut(shade_2_3_parts),
            FadeOut(shade_3_4_parts),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(explain_3),
            FadeOut(title),
            FadeOut(answer),
            self.formula_group.animate.scale(1/0.7).move_to(UP * 3.5),
            run_time=0.6
        )
    
    def scene_3_multiplication_rule(self):
        """场景3: 乘法法则"""
        # 标题
        title = Text(
            "分数乘法法则",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 原式
        step_0 = MathTex(
            r"\frac{2}{3} \times \frac{3}{4}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(TransformMatchingTex(self.formula_group, step_0), run_time=0.6)
        self.wait(0.5)
        
        # 分子相乘箭头
        arrow_num = Arrow(
            start=step_0.get_top() + UP * 0.3 + LEFT * 0.8,
            end=step_0.get_top() + UP * 0.3 + RIGHT * 0.8,
            color=self.COLOR_FRACTION_1,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        num_calc_chinese = Text(
            "分子: ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        num_calc_math = MathTex(
            r"2 \times 3 = 6",
            font_size=self.FONT_BODY + 2,
            color=self.COLOR_FRACTION_1
        )
        num_calc = VGroup(num_calc_chinese, num_calc_math).arrange(RIGHT, buff=0.2)
        num_calc.move_to(UP * 2)
        
        self.play(GrowArrow(arrow_num), run_time=0.5)
        self.play(FadeIn(num_calc, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # 分母相乘箭头
        arrow_den = Arrow(
            start=step_0.get_bottom() + DOWN * 0.3 + LEFT * 0.8,
            end=step_0.get_bottom() + DOWN * 0.3 + RIGHT * 0.8,
            color=self.COLOR_FRACTION_2,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15
        )
        
        den_calc_chinese = Text(
            "分母: ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        den_calc_math = MathTex(
            r"3 \times 4 = 12",
            font_size=self.FONT_BODY + 2,
            color=self.COLOR_FRACTION_2
        )
        den_calc = VGroup(den_calc_chinese, den_calc_math).arrange(RIGHT, buff=0.2)
        den_calc.move_to(UP * 1)
        
        self.play(GrowArrow(arrow_den), run_time=0.5)
        self.play(FadeIn(den_calc, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 计算结果
        step_1 = MathTex(
            r"= \frac{2 \times 3}{3 \times 4} = \frac{6}{12}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 0)
        
        self.play(Write(step_1), run_time=1.0)
        self.wait(0.5)
        
        # 约分
        simplify_title = Text(
            "化简 (约分)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_SIMPLIFY
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(simplify_title, shift=UP * 0.2), run_time=0.5)
        
        step_2 = MathTex(
            r"= \frac{6 \div 6}{12 \div 6} = \frac{1}{2}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2.5)
        
        self.play(Write(step_2), run_time=1.2)
        
        # 最终答案闪烁
        final_answer = MathTex(
            r"\frac{1}{2}",
            font_size=self.FONT_FORMULA * 1.5,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(final_answer, scale=1.3), run_time=0.6)
        self.play(
            Flash(final_answer, color=self.COLOR_HIGHLIGHT, flash_radius=0.6),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 法则卡片
        rule_card = Text(
            "分数乘法: 分子相乘作分子，分母相乘作分母",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        box = SurroundingRectangle(rule_card, color=self.COLOR_HIGHLIGHT, buff=0.2)
        rule_group = VGroup(box, rule_card)
        
        self.play(FadeIn(rule_group, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step_0),
            FadeOut(arrow_num),
            FadeOut(arrow_den),
            FadeOut(num_calc),
            FadeOut(den_calc),
            FadeOut(step_1),
            FadeOut(simplify_title),
            FadeOut(step_2),
            FadeOut(final_answer),
            FadeOut(rule_group),
            run_time=0.6
        )
    
    def scene_4_more_examples(self):
        """场景4: 更多例子"""
        # 例子1: 1/2 × 4/5
        ex1_title = Text(
            "例题 1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(ex1_title), run_time=0.4)
        
        ex1_problem = MathTex(
            r"\frac{1}{2} \times \frac{4}{5}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(ex1_problem), run_time=0.6)
        
        ex1_step1 = MathTex(
            r"= \frac{1 \times 4}{2 \times 5}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(ex1_step1), run_time=0.8)
        
        ex1_result = MathTex(
            r"= \frac{4}{10} = \frac{2}{5}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(UP * 0.5)
        
        self.play(Write(ex1_result), run_time=0.8)
        
        check = Text(
            "✓ 化简后得最简分数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(check, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)
        
        self.play(
            FadeOut(ex1_title),
            FadeOut(ex1_problem),
            FadeOut(ex1_step1),
            FadeOut(ex1_result),
            FadeOut(check),
            run_time=0.5
        )
        
        # 例子2: 2/3 × 9 (整数转分数)
        ex2_title = Text(
            "例题 2: 分数乘整数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(ex2_title), run_time=0.4)
        
        ex2_problem = MathTex(
            r"\frac{2}{3} \times 9",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(ex2_problem), run_time=0.6)
        
        ex2_convert_chinese = Text(
            "整数化为分数: ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        )
        ex2_convert_math = MathTex(
            r"9 = \frac{9}{1}",
            font_size=self.FONT_BODY + 2,
            color=WHITE
        )
        ex2_convert = VGroup(ex2_convert_chinese, ex2_convert_math).arrange(RIGHT, buff=0.2)
        ex2_convert.move_to(UP * 2.2)
        
        self.play(FadeIn(ex2_convert, shift=DOWN * 0.2), run_time=0.6)
        
        ex2_step1 = MathTex(
            r"= \frac{2}{3} \times \frac{9}{1} = \frac{2 \times 9}{3 \times 1}",
            font_size=self.FONT_FORMULA - 4,
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(Write(ex2_step1), run_time=0.8)
        
        ex2_step2 = MathTex(
            r"= \frac{18}{3}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(ex2_step2), run_time=0.6)
        
        ex2_simplify = MathTex(
            r"= \frac{18 \div 3}{3 \div 3} = \frac{6}{1} = 6",
            font_size=self.FONT_FORMULA - 2,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(ex2_simplify), run_time=1.0)
        self.wait(1.0)
        
        self.play(
            FadeOut(ex2_title),
            FadeOut(ex2_problem),
            FadeOut(ex2_convert),
            FadeOut(ex2_step1),
            FadeOut(ex2_step2),
            FadeOut(ex2_simplify),
            run_time=0.5
        )
        
        # 例子3: 先约分 3/4 × 8/9
        ex3_title = Text(
            "例题 3: 先约分再计算",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(ex3_title), run_time=0.4)
        
        ex3_problem = MathTex(
            r"\frac{3}{4} \times \frac{8}{9}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(ex3_problem), run_time=0.6)
        
        tip = Text(
            "技巧: 交叉约分",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SIMPLIFY
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        
        # 显示约分过程
        ex3_simplify_chinese = Text(
            "约分: ",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        ex3_simplify_math = MathTex(
            r"\frac{3}{4} \times \frac{8}{9} = \frac{3 \div 3}{4 \div 4} \times \frac{8 \div 4}{9 \div 3} = \frac{1}{1} \times \frac{2}{3}",
            font_size=self.FONT_BODY - 2,
            color=self.COLOR_SIMPLIFY
        )
        ex3_simplify_group = VGroup(ex3_simplify_chinese, ex3_simplify_math).arrange(RIGHT, buff=0.1)
        ex3_simplify_group.move_to(UP * 1)
        
        self.play(Write(ex3_simplify_group), run_time=1.2)
        
        ex3_result = MathTex(
            r"= \frac{1 \times 2}{1 \times 3} = \frac{2}{3}",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 0.5)
        
        self.play(Write(ex3_result), run_time=0.8)
        
        advantage = Text(
            "✓ 先约分，数字更小，计算更简单!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(advantage, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
        
        self.play(
            FadeOut(ex3_title),
            FadeOut(ex3_problem),
            FadeOut(tip),
            FadeOut(ex3_simplify_group),
            FadeOut(ex3_result),
            FadeOut(advantage),
            run_time=0.5
        )
    
    def scene_5_laws(self):
        """场景5: 运算律"""
        # 标题
        title = Text(
            "分数乘法的运算律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 交换律
        law1_name = Text(
            "① 交换律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_FRACTION_1
        ).move_to(UP * 4.5 + LEFT * 2.5)
        
        law1_formula = MathTex(
            r"\frac{a}{b} \times \frac{c}{d} = \frac{c}{d} \times \frac{a}{b}",
            font_size=self.FONT_BODY + 2,
            color=WHITE
        ).next_to(law1_name, RIGHT, buff=0.3)
        
        law1 = VGroup(law1_name, law1_formula)
        
        self.play(FadeIn(law1, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 结合律
        law2_name = Text(
            "② 结合律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_FRACTION_2
        ).move_to(UP * 2.5 + LEFT * 3.2)
        
        law2_formula = MathTex(
            r"(\frac{a}{b} \times \frac{c}{d}) \times \frac{e}{f} = \frac{a}{b} \times (\frac{c}{d} \times \frac{e}{f})",
            font_size=self.FONT_BODY - 4,
            color=WHITE
        ).next_to(law2_name, RIGHT, buff=0.2)
        
        law2 = VGroup(law2_name, law2_formula)
        
        self.play(FadeIn(law2, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 分配律
        law3_name = Text(
            "③ 分配律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_RESULT
        ).move_to(UP * 0.3 + LEFT * 3.2)
        
        law3_formula = MathTex(
            r"\frac{a}{b} \times (\frac{c}{d} + \frac{e}{f}) = \frac{a}{b} \times \frac{c}{d} + \frac{a}{b} \times \frac{e}{f}",
            font_size=self.FONT_BODY - 6,
            color=WHITE
        ).next_to(law3_name, RIGHT, buff=0.2)
        
        law3 = VGroup(law3_name, law3_formula)
        
        self.play(FadeIn(law3, shift=RIGHT * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 示例
        example_title = Text(
            "示例:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 2 + LEFT * 3)
        
        example_formula = MathTex(
            r"\frac{1}{2} \times \frac{3}{4} = \frac{3}{4} \times \frac{1}{2}",
            font_size=self.FONT_BODY + 2,
            color=self.COLOR_HIGHLIGHT
        ).next_to(example_title, RIGHT, buff=0.3)
        
        example = VGroup(example_title, example_formula)
        
        self.play(FadeIn(example, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 所有卡片闪烁
        all_laws = VGroup(law1, law2, law3)
        self.play(Indicate(all_laws, color=self.COLOR_HIGHLIGHT), run_time=1.0)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(law1),
            FadeOut(law2),
            FadeOut(law3),
            FadeOut(example),
            run_time=0.6
        )
    
    def scene_6_tips(self):
        """场景6: 技巧总结"""
        # 标题
        title = Text(
            "计算技巧总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 技巧列表
        tip1 = Text(
            "① 分子相乘作分子，分母相乘作分母",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(tip1, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        tip2 = Text(
            "② 整数转化为分数 (分母为1)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(tip2, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        tip3 = Text(
            "③ 能约分先约分，计算更简单",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SIMPLIFY,
            weight=BOLD
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(tip3, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        tip4 = Text(
            "④ 最后结果要化简为最简分数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(tip4, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 示例动画
        demo_title = Text(
            "快速示例:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(demo_title), run_time=0.4)
        
        demo = MathTex(
            r"\frac{5}{6} \times \frac{12}{25} = \frac{5}{6} \times \frac{12}{25} = \frac{1}{1} \times \frac{2}{5} = \frac{2}{5}",
            font_size=self.FONT_BODY - 2,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2)
        
        self.play(Write(demo), run_time=1.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(tip1),
            FadeOut(tip2),
            FadeOut(tip3),
            FadeOut(tip4),
            FadeOut(demo_title),
            FadeOut(demo),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 结尾与关注"""
        # 总结标题
        summary_title = Text(
            "分数乘法 - 知识点总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 关键点列表
        key1 = Text(
            "✓ 分子×分子，分母×分母",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 4.5)
        
        key2 = Text(
            "✓ 先约分再计算更简单",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_SIMPLIFY
        ).move_to(UP * 3.5)
        
        key3 = Text(
            "✓ 结果记得化简",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_RESULT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(key1, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(key2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(key3, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE + 4,
            color=WHITE
        ).move_to(UP * 0.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_B
        ).move_to(DOWN * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        # 装饰分数
        fractions = VGroup(
            MathTex(r"\frac{1}{2}", font_size=24, color=self.COLOR_FRACTION_1).shift(LEFT * 3 + DOWN * 4),
            MathTex(r"\frac{2}{3}", font_size=24, color=self.COLOR_FRACTION_2).shift(LEFT * 1.5 + DOWN * 4.5),
            MathTex(r"\frac{3}{4}", font_size=24, color=self.COLOR_RESULT).shift(ORIGIN + DOWN * 4),
            MathTex(r"\frac{4}{5}", font_size=24, color=self.COLOR_SIMPLIFY).shift(RIGHT * 1.5 + DOWN * 4.5),
            MathTex(r"\frac{5}{6}", font_size=24, color=self.COLOR_HIGHLIGHT).shift(RIGHT * 3 + DOWN * 4)
        )
        
        self.play(
            *[FadeIn(frac, scale=0.5) for frac in fractions],
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql fraction_multiplication.py FractionMultiplication  # 快速预览
# manim -qh fraction_multiplication.py FractionMultiplication   # 高质量渲染