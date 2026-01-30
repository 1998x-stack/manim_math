"""
因式分解——十字相乘法 教学动画
Cross Multiplication Factorization Method Educational Animation

使用 Manim 创建的七年级数学教学视频
内容: 十字相乘法的原理、步骤和应用
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


class CrossMultiplicationMethod(Scene):
    """
    十字相乘法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 方法介绍
    3. 简单例题1 (x²+5x+6)
    4. 验证过程
    5. 例题2 (x²-5x+6) - 负号
    6. 复杂例题 (2x²+7x+3)
    7. 技巧总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"      # 红色
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色
        self.COLOR_SUCCESS = "#2ecc71"        # 绿色
        self.COLOR_AUXILIARY = GRAY_B         # 灰色
        self.COLOR_CROSS_LINE = "#e67e22"     # 橙色 - 十字线
        self.COLOR_BOX_BG = "#2c3e50"         # 深蓝灰
        
        # 字体大小
        self.FONT_SIZE_TITLE = 38
        self.FONT_SIZE_SUBTITLE = 30
        self.FONT_SIZE_FORMULA = 32
        self.FONT_SIZE_BODY = 24
        self.FONT_SIZE_SMALL = 20
        self.FONT_SIZE_AUTHOR = 20
        
        # 十字图尺寸
        self.CELL_WIDTH = 1.2
        self.CELL_HEIGHT = 0.8
        self.GRID_LINE_WIDTH = 3
        
        # 执行动画序列
        self.show_opening()
        self.show_method_intro()
        self.show_example_1()
        self.show_verification()
        self.show_example_2()
        self.show_challenge_example()
        self.show_tips_summary()
        self.show_outro()
    
    def create_cross_grid(self, position=ORIGIN):
        """创建十字图网格框架"""
        # 垂直线
        v_line = Line(
            position + UP * self.CELL_HEIGHT,
            position + DOWN * self.CELL_HEIGHT,
            color=self.COLOR_CROSS_LINE,
            stroke_width=self.GRID_LINE_WIDTH
        )
        
        # 水平线
        h_line = Line(
            position + LEFT * self.CELL_WIDTH,
            position + RIGHT * self.CELL_WIDTH,
            color=self.COLOR_CROSS_LINE,
            stroke_width=self.GRID_LINE_WIDTH
        )
        
        # X符号（装饰用）
        x_mark = VGroup(
            Line(
                position + UL * 0.15,
                position + DR * 0.15,
                color=self.COLOR_CROSS_LINE,
                stroke_width=2
            ),
            Line(
                position + UR * 0.15,
                position + DL * 0.15,
                color=self.COLOR_CROSS_LINE,
                stroke_width=2
            )
        )
        
        return VGroup(v_line, h_line, x_mark)
    
    def create_cross_arrows(self, center, cell_w, cell_h):
        """创建交叉箭头（对角线）"""
        # 左上到右下
        arrow_1 = Arrow(
            center + UP * cell_h/2 + LEFT * cell_w/2,
            center + DOWN * cell_h/2 + RIGHT * cell_w/2,
            color=self.COLOR_SECONDARY,
            stroke_width=4,
            buff=0.15,
            max_tip_length_to_length_ratio=0.15
        )
        
        # 左下到右上
        arrow_2 = Arrow(
            center + DOWN * cell_h/2 + LEFT * cell_w/2,
            center + UP * cell_h/2 + RIGHT * cell_w/2,
            color=self.COLOR_SECONDARY,
            stroke_width=4,
            buff=0.15,
            max_tip_length_to_length_ratio=0.15
        )
        
        return VGroup(arrow_1, arrow_2)
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5s)"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何快速分解这个式子?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        problem_expr = MathTex(
            r"2x^2 + 7x + 3",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        question_mark = Text(
            "?",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).next_to(problem_expr, RIGHT, buff=0.3)
        
        self.play(Write(hook_question), run_time=0.8)
        self.play(Write(problem_expr), run_time=0.9)
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.3)
        self.play(Flash(question_mark, color=YELLOW), run_time=0.4)
        
        # 神秘的十字符号
        cross_symbol = VGroup(
            Line(UP * 0.5, DOWN * 0.5, color=self.COLOR_CROSS_LINE, stroke_width=6),
            Line(LEFT * 0.5, RIGHT * 0.5, color=self.COLOR_CROSS_LINE, stroke_width=6)
        ).move_to(UP * 2)
        
        self.play(FadeIn(cross_symbol, scale=2), run_time=0.6)
        self.play(Rotate(cross_symbol, angle=PI/4, run_time=0.4))
        
        # 提示
        hint_text = Text(
            "用十字相乘法!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(problem_expr),
            FadeOut(question_mark),
            FadeOut(hint_text),
            cross_symbol.animate.scale(0.4).move_to(UP * 6.5 + RIGHT * 3),
            run_time=0.8
        )
        
        self.cross_symbol = cross_symbol
    
    def show_method_intro(self):
        """场景2: 方法介绍 (5-13s)"""
        # 标题
        title = Text(
            "十字相乘法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 通用公式
        general_formula = MathTex(
            r"x^2 + (p+q)x + pq = (x+p)(x+q)",
            font_size=self.FONT_SIZE_FORMULA,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(general_formula), run_time=1.2)
        
        # 十字图示
        grid_center = UP * 1.5
        cross_grid = self.create_cross_grid(grid_center)
        
        self.play(Create(cross_grid), run_time=1.0)
        
        # 填入标签
        label_tl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        label_tl.move_to(grid_center + UP * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        label_tr = MathTex("p", font_size=32, color=self.COLOR_SECONDARY)
        label_tr.move_to(grid_center + UP * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        label_bl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        label_bl.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        label_br = MathTex("q", font_size=32, color=self.COLOR_SECONDARY)
        label_br.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        labels = VGroup(label_tl, label_tr, label_bl, label_br)
        
        self.play(FadeIn(labels, lag_ratio=0.2), run_time=0.8)
        
        # 交叉箭头
        cross_arrows = self.create_cross_arrows(grid_center, self.CELL_WIDTH, self.CELL_HEIGHT)
        
        self.play(Create(cross_arrows), run_time=0.8)
        
        # 步骤说明
        step_1 = Text(
            "① 找p,q使 p×q = 常数项",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        step_2 = Text(
            "② 验证 p+q = 一次项系数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 2.3)
        
        step_3 = Text(
            "③ 结果为 (x+p)(x+q)",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3.1)
        
        self.play(FadeIn(step_1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(step_2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(step_3, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(general_formula),
            FadeOut(cross_grid),
            FadeOut(labels),
            FadeOut(cross_arrows),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(step_3),
            title.animate.scale(0.7).move_to(UP * 6.2),
            run_time=0.8
        )
        
        self.method_title = title
    
    def show_example_1(self):
        """场景3: 简单例题1 - x²+5x+6 (13-28s)"""
        # 例题标题
        example_title = Text(
            "例题1",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(FadeIn(example_title, scale=1.2), run_time=0.5)
        
        # 原式
        original_text = Text("因式分解:", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        original_expr = MathTex(r"x^2 + 5x + 6", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 分析
        analysis = Text(
            "分析: 6 = 2 × 3",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(analysis), run_time=0.6)
        
        # 显示6的分解
        six_decomp = MathTex(r"6 = 2 \times 3", font_size=26, color=self.COLOR_HIGHLIGHT)
        six_decomp.next_to(analysis, DOWN, buff=0.3)
        
        self.play(Write(six_decomp), run_time=0.8)
        self.wait(0.5)
        
        # 十字图
        grid_center = ORIGIN
        cross_grid = self.create_cross_grid(grid_center)
        
        self.play(Create(cross_grid), run_time=0.8)
        
        # 填入数字
        num_tl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        num_tl.move_to(grid_center + UP * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_tr = MathTex("2", font_size=32, color=self.COLOR_SECONDARY)
        num_tr.move_to(grid_center + UP * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        num_bl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        num_bl.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_br = MathTex("3", font_size=32, color=self.COLOR_SECONDARY)
        num_br.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        # 先填左列
        self.play(FadeIn(num_tl), FadeIn(num_bl), run_time=0.6)
        
        # 再填右列
        self.play(FadeIn(num_tr), FadeIn(num_br), run_time=0.6)
        
        # 交叉箭头
        cross_arrows = self.create_cross_arrows(grid_center, self.CELL_WIDTH, self.CELL_HEIGHT)
        
        self.play(Create(cross_arrows), run_time=0.8)
        
        # 交叉乘积
        product_1 = MathTex(r"x \times 3 = 3x", font_size=24, color=self.COLOR_HIGHLIGHT)
        product_1.move_to(DOWN * 2.2 + LEFT * 1.5)
        
        product_2 = MathTex(r"x \times 2 = 2x", font_size=24, color=self.COLOR_HIGHLIGHT)
        product_2.move_to(DOWN * 2.2 + RIGHT * 1.5)
        
        self.play(Write(product_1), run_time=0.7)
        self.play(Write(product_2), run_time=0.7)
        
        # 相加验证
        sum_calc = MathTex(r"3x + 2x = 5x", font_size=26, color=WHITE)
        sum_calc.move_to(DOWN * 3.2)
        
        self.play(Write(sum_calc), run_time=0.8)
        
        # 验证标记
        check = Text("✓", font_size=36, color=self.COLOR_SUCCESS)
        check.next_to(sum_calc, RIGHT, buff=0.3)
        
        self.play(FadeIn(check, scale=1.5), run_time=0.5)
        self.wait(0.5)
        
        # 结果
        result = MathTex(
            r"(x+2)(x+3)",
            font_size=40,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 4.5)
        
        result_box = SurroundingRectangle(
            result,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(result), run_time=1.0)
        self.play(Create(result_box), run_time=0.5)
        
        # 对号
        big_check = Text("✓", font_size=60, color=self.COLOR_SUCCESS)
        big_check.next_to(result_box, RIGHT, buff=0.3)
        
        self.play(FadeIn(big_check, scale=2), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(original_group),
            FadeOut(analysis),
            FadeOut(six_decomp),
            FadeOut(cross_grid),
            FadeOut(num_tl),
            FadeOut(num_tr),
            FadeOut(num_bl),
            FadeOut(num_br),
            FadeOut(cross_arrows),
            FadeOut(product_1),
            FadeOut(product_2),
            FadeOut(sum_calc),
            FadeOut(check),
            FadeOut(result_box),
            FadeOut(big_check),
            result.animate.scale(0.6).move_to(UP * 5.8 + LEFT * 2),
            run_time=0.8
        )
        
        self.example_1_result = result
    
    def show_verification(self):
        """场景4: 验证过程 (28-36s)"""
        # 验证标题
        verify_title = Text(
            "验证",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(Write(verify_title), run_time=0.5)
        
        # 展开过程
        step_1 = MathTex(r"(x+2)(x+3)", font_size=32, color=WHITE)
        step_1.move_to(UP * 3)
        
        self.play(Write(step_1), run_time=0.8)
        
        # FOIL展开
        step_2 = MathTex(r"= x \cdot x + x \cdot 3 + 2 \cdot x + 2 \cdot 3", font_size=28, color=WHITE)
        step_2.move_to(UP * 1.8)
        
        self.play(Write(step_2), run_time=1.2)
        
        # 计算
        step_3 = MathTex(r"= x^2 + 3x + 2x + 6", font_size=30, color=WHITE)
        step_3.move_to(UP * 0.5)
        
        self.play(Write(step_3), run_time=1.0)
        
        # 合并同类项
        step_4 = MathTex(r"= x^2 + 5x + 6", font_size=32, color=self.COLOR_SUCCESS)
        step_4.move_to(DOWN * 0.8)
        
        self.play(
            TransformMatchingTex(step_3.copy(), step_4),
            run_time=1.0
        )
        
        # 对比原式
        original_ref = MathTex(r"x^2 + 5x + 6", font_size=32, color=self.COLOR_HIGHLIGHT)
        original_ref.move_to(DOWN * 2.2)
        
        compare_text = Text(
            "与原式相同!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(original_ref), run_time=0.6)
        
        # 连接箭头
        arrow = Arrow(
            step_4.get_bottom(),
            original_ref.get_top(),
            color=self.COLOR_SUCCESS,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(Create(arrow), run_time=0.5)
        self.play(FadeIn(compare_text, shift=UP * 0.2), run_time=0.5)
        
        # 闪烁效果
        self.play(
            Flash(step_4, color=self.COLOR_SUCCESS),
            Flash(original_ref, color=self.COLOR_SUCCESS),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(verify_title),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(step_3),
            FadeOut(step_4),
            FadeOut(original_ref),
            FadeOut(arrow),
            FadeOut(compare_text),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景5: 例题2 - x²-5x+6 (36-48s)"""
        # 例题标题
        example_title = Text(
            "例题2",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5)
        
        self.play(FadeIn(example_title, scale=1.2), run_time=0.5)
        
        # 原式
        original_text = Text("因式分解:", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        original_expr = MathTex(r"x^2 - 5x + 6", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 强调负号
        minus_sign = original_expr[0][3]  # 负号位置
        self.play(
            Indicate(minus_sign, color=self.COLOR_SECONDARY, scale_factor=1.5),
            run_time=0.8
        )
        
        # 分析
        analysis = Text(
            "注意: 两数积=6, 和=-5",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(analysis), run_time=0.7)
        
        # 十字图
        grid_center = UP * 0.3
        cross_grid = self.create_cross_grid(grid_center)
        
        self.play(Create(cross_grid), run_time=0.8)
        
        # 填入数字（负数）
        num_tl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        num_tl.move_to(grid_center + UP * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_tr = MathTex("-2", font_size=32, color=self.COLOR_SECONDARY)
        num_tr.move_to(grid_center + UP * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        num_bl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        num_bl.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_br = MathTex("-3", font_size=32, color=self.COLOR_SECONDARY)
        num_br.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        self.play(FadeIn(num_tl), FadeIn(num_bl), run_time=0.5)
        self.play(FadeIn(num_tr), FadeIn(num_br), run_time=0.6)
        
        # 交叉箭头
        cross_arrows = self.create_cross_arrows(grid_center, self.CELL_WIDTH, self.CELL_HEIGHT)
        
        self.play(Create(cross_arrows), run_time=0.7)
        
        # 交叉乘积
        product_calc = MathTex(
            r"(-3x) + (-2x) = -5x",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(product_calc), run_time=1.0)
        
        # 验证标记
        check = Text("✓", font_size=36, color=self.COLOR_SUCCESS)
        check.next_to(product_calc, RIGHT, buff=0.3)
        
        self.play(FadeIn(check, scale=1.5), run_time=0.5)
        
        # 结果
        result = MathTex(
            r"(x-2)(x-3)",
            font_size=40,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3)
        
        result_box = SurroundingRectangle(
            result,
            color=self.COLOR_SUCCESS,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(result), run_time=1.0)
        self.play(Create(result_box), run_time=0.5)
        
        # 符号提示
        tip_text = Text(
            "提示: 负负得正!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        tip_formula = MathTex(r"(-2) \times (-3) = 6", font_size=24, color=self.COLOR_HIGHLIGHT)
        tip_formula.next_to(tip_text, DOWN, buff=0.2)
        
        self.play(FadeIn(tip_text), FadeIn(tip_formula), run_time=0.8)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(original_group),
            FadeOut(analysis),
            FadeOut(cross_grid),
            FadeOut(num_tl),
            FadeOut(num_tr),
            FadeOut(num_bl),
            FadeOut(num_br),
            FadeOut(cross_arrows),
            FadeOut(product_calc),
            FadeOut(check),
            FadeOut(result_box),
            FadeOut(tip_text),
            FadeOut(tip_formula),
            result.animate.scale(0.6).move_to(UP * 5.8),
            run_time=0.8
        )
        
        self.example_2_result = result
    
    def show_challenge_example(self):
        """场景6: 复杂例题 - 2x²+7x+3 (48-68s)"""
        # 挑战题标题
        challenge_title = Text(
            "挑战题",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.2)
        
        star_1 = Text("⭐", font_size=28, color=GOLD).next_to(challenge_title, LEFT, buff=0.3)
        star_2 = Text("⭐", font_size=28, color=GOLD).next_to(challenge_title, RIGHT, buff=0.3)
        
        title_group = VGroup(star_1, challenge_title, star_2)
        
        self.play(FadeIn(title_group, scale=1.3), run_time=0.7)
        
        # 原式
        original_text = Text("因式分解:", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        original_expr = MathTex(r"2x^2 + 7x + 3", font_size=36, color=WHITE)
        original_group = VGroup(original_text, original_expr).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(Write(original_group), run_time=1.0)
        
        # 分析
        analysis = Text(
            "分析: 需要分解2和3",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(analysis), run_time=0.7)
        
        # 显示分解
        decomp_1 = MathTex(r"2x^2 = 2x \cdot x", font_size=24, color=self.COLOR_PRIMARY)
        decomp_1.move_to(UP * 2.1 + LEFT * 1.5)
        
        decomp_2 = MathTex(r"3 = 1 \cdot 3", font_size=24, color=self.COLOR_SECONDARY)
        decomp_2.move_to(UP * 2.1 + RIGHT * 1.5)
        
        self.play(Write(decomp_1), run_time=0.8)
        self.play(Write(decomp_2), run_time=0.8)
        
        self.wait(0.5)
        
        # 十字图
        grid_center = UP * 0.2
        cross_grid = self.create_cross_grid(grid_center)
        
        self.play(Create(cross_grid), run_time=0.8)
        
        # 填入数字
        num_tl = MathTex("2x", font_size=30, color=self.COLOR_PRIMARY)
        num_tl.move_to(grid_center + UP * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_tr = MathTex("1", font_size=32, color=self.COLOR_SECONDARY)
        num_tr.move_to(grid_center + UP * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        num_bl = MathTex("x", font_size=32, color=self.COLOR_PRIMARY)
        num_bl.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + LEFT * self.CELL_WIDTH/2)
        
        num_br = MathTex("3", font_size=32, color=self.COLOR_SECONDARY)
        num_br.move_to(grid_center + DOWN * self.CELL_HEIGHT/2 + RIGHT * self.CELL_WIDTH/2)
        
        self.play(FadeIn(num_tl), FadeIn(num_bl), run_time=0.6)
        self.play(FadeIn(num_tr), FadeIn(num_br), run_time=0.6)
        
        # 交叉箭头
        cross_arrows = self.create_cross_arrows(grid_center, self.CELL_WIDTH, self.CELL_HEIGHT)
        
        self.play(Create(cross_arrows), run_time=0.8)
        
        # 交叉乘积
        product_1 = MathTex(r"2x \times 3 = 6x", font_size=24, color=self.COLOR_HIGHLIGHT)
        product_1.move_to(DOWN * 1.8 + LEFT * 1.5)
        
        product_2 = MathTex(r"x \times 1 = x", font_size=24, color=self.COLOR_HIGHLIGHT)
        product_2.move_to(DOWN * 1.8 + RIGHT * 1.5)
        
        self.play(Write(product_1), run_time=0.7)
        self.play(Write(product_2), run_time=0.7)
        
        # 相加验证
        sum_calc = MathTex(r"6x + x = 7x", font_size=26, color=WHITE)
        sum_calc.move_to(DOWN * 2.8)
        
        self.play(Write(sum_calc), run_time=0.8)
        
        # 验证标记
        check = Text("✓", font_size=36, color=self.COLOR_SUCCESS)
        check.next_to(sum_calc, RIGHT, buff=0.3)
        
        self.play(FadeIn(check, scale=1.5), run_time=0.5)
        self.wait(0.5)
        
        # 结果
        result = MathTex(
            r"(2x+1)(x+3)",
            font_size=42,
            color=GOLD
        ).move_to(DOWN * 4.2)
        
        result_box = SurroundingRectangle(
            result,
            color=GOLD,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=4
        )
        
        self.play(Write(result), run_time=1.2)
        self.play(Create(result_box), run_time=0.6)
        
        # 庆祝效果
        stars = VGroup(*[
            Text("⭐", font_size=30, color=GOLD)
            .move_to(result_box.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            Flash(result, color=GOLD, flash_radius=0.8, num_lines=12),
            *[FadeIn(star, scale=0.5) for star in stars],
            run_time=1.0
        )
        
        # 技巧提示
        tip = Text(
            "技巧: 首项系数≠1时,同时分解首项和常数项",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(tip), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title_group),
            FadeOut(original_group),
            FadeOut(analysis),
            FadeOut(decomp_1),
            FadeOut(decomp_2),
            FadeOut(cross_grid),
            FadeOut(num_tl),
            FadeOut(num_tr),
            FadeOut(num_bl),
            FadeOut(num_br),
            FadeOut(cross_arrows),
            FadeOut(product_1),
            FadeOut(product_2),
            FadeOut(sum_calc),
            FadeOut(check),
            FadeOut(result_box),
            FadeOut(stars),
            FadeOut(tip),
            result.animate.scale(0.5).move_to(UP * 5.8 + RIGHT * 2.5),
            run_time=0.8
        )
        
        self.challenge_result = result
    
    def show_tips_summary(self):
        """场景7: 技巧总结 (68-80s)"""
        # 总结标题
        summary_title = Text(
            "技巧总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZE_TITLE,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 技巧卡片
        tips = [
            "① 列出因数对: 找所有p,q组合",
            "② 验证和: p+q=一次项系数",
            "③ 注意符号: 正负搭配要小心",
            "④ 复杂情况: 同时分解首项和常数",
            "⑤ 多次尝试: 找到正确组合"
        ]
        
        tip_cards = VGroup()
        
        for i, tip_text in enumerate(tips):
            # 创建卡片
            tip = Text(
                tip_text,
                font="Noto Sans CJK SC",
                font_size=20,
                color=WHITE
            )
            
            bg = RoundedRectangle(
                width=tip.width + 0.6,
                height=tip.height + 0.3,
                fill_color=self.COLOR_BOX_BG,
                fill_opacity=0.8,
                stroke_color=self.COLOR_PRIMARY,
                stroke_width=2,
                corner_radius=0.1
            )
            
            card = VGroup(bg, tip)
            card.move_to(UP * (3 - i * 1.3) + LEFT * 10)  # 初始在左侧外
            
            tip_cards.add(card)
        
        # 卡片依次滑入
        for card in tip_cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.15)
        
        # 全部闪烁
        self.play(*[Flash(card, color=self.COLOR_PRIMARY) for card in tip_cards], run_time=0.6)
        
        # 口诀
        slogan = Text(
            "十字交叉乘，相加要相等!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(slogan, shift=UP * 0.3, scale=1.2), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(tip_cards),
            FadeOut(slogan),
            FadeOut(self.method_title),
            FadeOut(self.example_1_result),
            FadeOut(self.example_2_result),
            FadeOut(self.challenge_result),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景8: 片尾关注 (80-88s)"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握更多因式分解技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 十字符号装饰（环绕动画）
        cross_decorations = VGroup(*[
            VGroup(
                Line(UP * 0.3, DOWN * 0.3, color=self.COLOR_CROSS_LINE, stroke_width=4),
                Line(LEFT * 0.3, RIGHT * 0.3, color=self.COLOR_CROSS_LINE, stroke_width=4)
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0])
            )
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(cross, scale=0.5) for cross in cross_decorations],
            run_time=0.8
        )
        
        # 旋转动画
        self.play(Rotate(cross_decorations, angle=PI, run_time=1.5, rate_func=smooth))
        
        # 示例公式快闪
        formulas = VGroup(
            MathTex(r"x^2+5x+6", font_size=20, color=self.COLOR_PRIMARY),
            MathTex(r"x^2-5x+6", font_size=20, color=self.COLOR_PRIMARY),
            MathTex(r"2x^2+7x+3", font_size=20, color=GOLD)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.8)
        
        self.play(*[FadeIn(f, scale=0.8) for f in formulas], run_time=0.6)
        
        self.wait(1.2)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(cross_decorations),
            FadeOut(formulas),
            FadeOut(self.cross_symbol),
            run_time=1.0
        )


# 运行命令:
# manim -pql cross_multiplication.py CrossMultiplicationMethod  # 快速预览 (480p 15fps)
# manim -qm cross_multiplication.py CrossMultiplicationMethod   # 中等质量 (720p 30fps)
# manim -qh cross_multiplication.py CrossMultiplicationMethod   # 高质量 (1080p 60fps)