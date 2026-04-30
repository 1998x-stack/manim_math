"""
代数方程的应用 - 增长率问题教学动画
使用 Manim 创建的八年级代数应用题教学视频

内容: 增长率问题的完整解题流程
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


class AlgebraApplication(Scene):
    """
    代数方程应用题动画场景
    
    示例题目:
    某商店去年的销售额为100万元，今年的销售额为121万元。
    如果每年的增长率相同，求这个增长率。
    
    场景顺序:
    1. 开场钩子
    2. 问题展示
    3. 解题步骤总览
    4. 审题分析
    5. 设未知数
    6. 找等量关系
    7. 列方程并解方程
    8. 检验作答
    9. 方法总结
    10. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PROBLEM = "#3498db"      # 蓝色 - 题目
        self.COLOR_ANALYSIS = "#e74c3c"     # 红色 - 分析
        self.COLOR_EQUATION = "#9b59b6"     # 紫色 - 方程
        self.COLOR_SOLUTION = "#2ecc71"     # 绿色 - 解答
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键步骤
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助说明
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_problem()
        self.show_steps_overview()
        self.show_analysis()
        self.show_set_variable()
        self.show_find_relation()
        self.show_solve_equation()
        self.show_verification()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 实际场景引入"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 店铺图标（用圆圈和矩形模拟）
        shop = VGroup(
            Rectangle(width=1.5, height=1.2, color=self.COLOR_PROBLEM, fill_opacity=0.3),
            Triangle(color=self.COLOR_PROBLEM, fill_opacity=0.5).scale(0.8).shift(UP * 0.8)
        ).move_to(UP * 4 + LEFT * 1.5)
        
        # 钱袋图标
        money_bag = VGroup(
            Circle(radius=0.5, color=self.COLOR_SOLUTION, fill_opacity=0.3),
            Text("¥", font=self.FONT_CHINESE, font_size=36, color=self.COLOR_SOLUTION)
        ).move_to(UP * 4 + RIGHT * 1.5)
        
        self.play(FadeIn(shop, scale=0.8), run_time=0.5)
        self.play(FadeIn(money_bag, scale=0.8), run_time=0.5)
        
        # 钩子问题
        hook = Text(
            "销售额大增！增长率是多少？",
            font=self.FONT_CHINESE,
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(Write(hook), run_time=1.2)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(shop),
            FadeOut(money_bag),
            FadeOut(hook),
            run_time=0.6
        )
    
    def show_problem(self):
        """场景2: 问题展示"""
        # 标题
        title = Text(
            "实际应用题",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 题目内容（分段显示）
        line1 = Text(
            "去年销售额: 100万元",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_PROBLEM
        ).move_to(UP * 3.5)
        
        line2 = Text(
            "今年销售额: 121万元",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_SOLUTION
        ).move_to(UP * 2.5)
        
        line3 = Text(
            "每年增长率相同",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_ANALYSIS
        ).move_to(UP * 1.5)
        
        question = Text(
            "求: 增长率是多少？",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.2)
        
        self.play(FadeIn(line1, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(line2, shift=RIGHT * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 高亮"相同增长率"
        rect = SurroundingRectangle(
            line3,
            color=self.COLOR_ANALYSIS,
            buff=0.15,
            corner_radius=0.1
        )
        self.play(
            FadeIn(line3, shift=RIGHT * 0.3),
            Create(rect),
            run_time=0.8
        )
        self.wait(0.8)
        self.play(FadeOut(rect), run_time=0.3)
        
        self.play(FadeIn(question, scale=1.1), run_time=0.8)
        self.wait(1.5)
        
        # 保存题目，缩小移到顶部
        self.problem_group = VGroup(line1, line2, line3, question)
        
        self.play(
            FadeOut(title),
            self.problem_group.animate.scale(0.5).move_to(UP * 6.5),
            run_time=0.8
        )
    
    def show_steps_overview(self):
        """场景3: 解题步骤总览"""
        # 标题
        title = Text(
            "解题六步法",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 六个步骤
        steps = [
            "① 审题",
            "② 设未知数",
            "③ 找等量关系",
            "④ 列方程",
            "⑤ 解方程",
            "⑥ 检验作答"
        ]
        
        step_objs = []
        for i, step_text in enumerate(steps):
            step = Text(
                step_text,
                font=self.FONT_CHINESE,
                font_size=26,
                color=WHITE
            ).move_to(UP * (3 - i * 0.9))
            step_objs.append(step)
        
        # 依次显示步骤
        for step in step_objs:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.4)
        
        self.wait(0.5)
        
        # 添加箭头
        arrows = []
        for i in range(len(step_objs) - 1):
            arrow = Arrow(
                step_objs[i].get_bottom() + DOWN * 0.1,
                step_objs[i+1].get_top() + UP * 0.1,
                color=self.COLOR_AUXILIARY,
                buff=0,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            arrows.append(arrow)
            self.play(GrowArrow(arrow), run_time=0.3)
        
        self.wait(1.5)
        
        # 保存步骤对象以便后续高亮
        self.steps_objs = step_objs
        self.steps_arrows = arrows
        self.steps_title = title
        
        # 移到侧边
        steps_group = VGroup(title, *step_objs, *arrows)
        self.play(
            steps_group.animate.scale(0.6).move_to(RIGHT * 3.2 + UP * 2),
            run_time=0.8
        )
    
    def show_analysis(self):
        """场景4: 审题分析"""
        # 高亮步骤1
        self.play(
            Indicate(self.steps_objs[0], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 标题
        step_title = Text(
            "Step 1: 审题 - 理解题意",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5 + LEFT * 1)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 时间轴
        timeline = Arrow(
            LEFT * 2.5,
            RIGHT * 2.5,
            color=self.COLOR_AUXILIARY,
            buff=0,
            stroke_width=4
        ).move_to(UP * 2)
        
        year_last = Text(
            "去年",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).next_to(timeline.get_start(), UP, buff=0.3)
        
        year_this = Text(
            "今年",
            font=self.FONT_CHINESE,
            font_size=24,
            color=WHITE
        ).next_to(timeline.get_end(), UP, buff=0.3)
        
        self.play(
            GrowArrow(timeline),
            FadeIn(year_last),
            FadeIn(year_this),
            run_time=1.0
        )
        
        # 去年数据
        data_last = Text(
            "100万",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_PROBLEM
        ).next_to(timeline.get_start(), DOWN, buff=0.5)
        
        self.play(FadeIn(data_last, scale=1.1), run_time=0.6)
        
        # 增长箭头
        growth_arrow = CurvedArrow(
            timeline.get_start() + DOWN * 0.3,
            timeline.get_end() + DOWN * 0.3,
            color=self.COLOR_ANALYSIS,
            angle=-TAU/4
        )
        
        growth_label = Text(
            "增长率 x",
            font=self.FONT_CHINESE,
            font_size=22,
            color=self.COLOR_ANALYSIS
        ).next_to(growth_arrow, DOWN, buff=0.1)
        
        self.play(
            Create(growth_arrow),
            FadeIn(growth_label),
            run_time=0.8
        )
        
        # 今年数据
        data_this = Text(
            "121万",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_SOLUTION
        ).next_to(timeline.get_end(), DOWN, buff=0.5)
        
        self.play(FadeIn(data_this, scale=1.1), run_time=0.6)
        
        # 关键信息
        key_info = Text(
            "关键: 连续两年，相同增长率",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(key_info, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(timeline),
            FadeOut(year_last),
            FadeOut(year_this),
            FadeOut(data_last),
            FadeOut(data_this),
            FadeOut(growth_arrow),
            FadeOut(growth_label),
            FadeOut(key_info),
            run_time=0.6
        )
    
    def show_set_variable(self):
        """场景5: 设未知数"""
        # 高亮步骤2
        self.play(
            Indicate(self.steps_objs[1], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 标题
        step_title = Text(
            "Step 2: 设未知数",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5 + LEFT * 1)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 设未知数
        set_var = Text(
            "设: 增长率为 x",
            font=self.FONT_CHINESE,
            font_size=30,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(Write(set_var), run_time=1.0)
        
        # 说明
        explanation = Text(
            "(x 表示每年的增长率)",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).next_to(set_var, DOWN, buff=0.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 移到侧边保存
        var_group = VGroup(set_var, explanation)
        self.play(
            FadeOut(step_title),
            var_group.animate.scale(0.7).move_to(LEFT * 3 + UP * 5),
            run_time=0.6
        )
        
        self.saved_variable = var_group
    
    def show_find_relation(self):
        """场景6: 找等量关系"""
        # 高亮步骤3
        self.play(
            Indicate(self.steps_objs[2], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 标题
        step_title = Text(
            "Step 3: 找等量关系",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5 + LEFT * 1)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 增长过程可视化
        process_title = Text(
            "增长过程:",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).move_to(UP * 3 + LEFT * 2)
        
        self.play(FadeIn(process_title), run_time=0.5)
        
        # 第一年
        year1_label = Text(
            "第一年:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.8 + LEFT * 2.5)
        
        year1_eq = MathTex(
            r"100 \times (1+x)",
            font_size=30,
            color=WHITE
        ).next_to(year1_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(year1_label),
            Write(year1_eq),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 箭头
        arrow1 = Arrow(
            year1_eq.get_bottom() + DOWN * 0.1,
            year1_eq.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4
        )
        
        continue_text = Text(
            "继续增长",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow1, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(arrow1),
            FadeIn(continue_text),
            run_time=0.6
        )
        
        # 第二年
        year2_label = Text(
            "第二年:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.2 + LEFT * 2.5)
        
        year2_eq = MathTex(
            r"100 \times (1+x) \times (1+x)",
            font_size=28,
            color=WHITE
        ).next_to(year2_label, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(year2_label),
            Write(year2_eq),
            run_time=1.2
        )
        self.wait(0.8)
        
        # 化简
        arrow2 = Arrow(
            year2_eq.get_bottom() + DOWN * 0.1,
            year2_eq.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow2), run_time=0.5)
        
        simplified = MathTex(
            r"100(1+x)^2",
            font_size=32,
            color=self.COLOR_EQUATION
        ).move_to(DOWN * 1.5)
        
        self.play(
            TransformMatchingTex(year2_eq.copy(), simplified),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 等量关系
        relation_arrow = Arrow(
            simplified.get_bottom() + DOWN * 0.1,
            simplified.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4
        )
        
        self.play(GrowArrow(relation_arrow), run_time=0.5)
        
        final_eq = MathTex(
            r"100(1+x)^2 = 121",
            font_size=36,
            color=self.COLOR_SOLUTION
        ).move_to(DOWN * 3)
        
        self.play(Write(final_eq), run_time=1.0)
        
        # 框住关键式
        eq_box = SurroundingRectangle(
            final_eq,
            color=self.COLOR_SOLUTION,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(eq_box), run_time=0.6)
        self.wait(1.5)
        
        # 保存方程
        self.saved_equation = VGroup(final_eq, eq_box)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(process_title),
            FadeOut(year1_label),
            FadeOut(year1_eq),
            FadeOut(arrow1),
            FadeOut(continue_text),
            FadeOut(year2_label),
            FadeOut(year2_eq),
            FadeOut(arrow2),
            FadeOut(simplified),
            FadeOut(relation_arrow),
            run_time=0.6
        )
        
        # 移动方程到中心
        self.play(
            self.saved_equation.animate.move_to(UP * 2),
            run_time=0.6
        )
    
    def show_solve_equation(self):
        """场景7: 列方程并解方程"""
        # 高亮步骤4和5
        self.play(
            Indicate(self.steps_objs[3], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            Indicate(self.steps_objs[4], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 标题
        step_title = Text(
            "Step 4 & 5: 列方程 & 解方程",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5 + LEFT * 0.5)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 提取方程
        equation = self.saved_equation[0].copy()
        
        # 除以100
        divide_text = Text(
            "两边同除以100",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(divide_text), run_time=0.5)
        
        arrow = Arrow(
            self.saved_equation.get_bottom() + DOWN * 0.1,
            self.saved_equation.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        eq_step1 = MathTex(
            r"(1+x)^2 = 1.21",
            font_size=34,
            color=WHITE
        ).move_to(DOWN * 0.2)
        
        self.play(
            TransformMatchingTex(equation, eq_step1),
            FadeOut(arrow),
            FadeOut(divide_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 开平方
        sqrt_text = Text(
            "两边开平方",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.2)
        
        self.play(FadeIn(sqrt_text), run_time=0.5)
        
        eq_step2 = MathTex(
            r"1+x = \pm 1.1",
            font_size=34,
            color=WHITE
        ).move_to(DOWN * 2)
        
        self.play(
            Write(eq_step2),
            FadeOut(sqrt_text),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 分支求解
        branch_title = Text(
            "分两种情况:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.2)
        
        self.play(FadeIn(branch_title), run_time=0.5)
        
        # 情况1: 正数
        case1 = MathTex(
            r"1+x = 1.1",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 4.2 + LEFT * 1.5)
        
        arrow1 = Arrow(
            case1.get_bottom() + DOWN * 0.1,
            case1.get_bottom() + DOWN * 0.5,
            color=self.COLOR_SOLUTION,
            buff=0,
            stroke_width=3
        )
        
        sol1 = MathTex(
            r"x_1 = 0.1 = 10\%",
            font_size=30,
            color=self.COLOR_SOLUTION
        ).next_to(arrow1, DOWN, buff=0.1)
        
        self.play(
            Write(case1),
            GrowArrow(arrow1),
            Write(sol1),
            run_time=1.2
        )
        
        # 情况2: 负数
        case2 = MathTex(
            r"1+x = -1.1",
            font_size=30,
            color=WHITE
        ).move_to(DOWN * 4.2 + RIGHT * 1.5)
        
        arrow2 = Arrow(
            case2.get_bottom() + DOWN * 0.1,
            case2.get_bottom() + DOWN * 0.5,
            color=RED,
            buff=0,
            stroke_width=3
        )
        
        sol2 = MathTex(
            r"x_2 = -2.1 = -210\%",
            font_size=28,
            color=RED
        ).next_to(arrow2, DOWN, buff=0.1)
        
        self.play(
            Write(case2),
            GrowArrow(arrow2),
            Write(sol2),
            run_time=1.2
        )
        
        self.wait(2.0)
        
        # 保存解
        self.solutions = VGroup(
            VGroup(case1, arrow1, sol1),
            VGroup(case2, arrow2, sol2)
        )
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(self.saved_equation),
            FadeOut(eq_step1),
            FadeOut(eq_step2),
            FadeOut(branch_title),
            run_time=0.6
        )
    
    def show_verification(self):
        """场景8: 检验作答"""
        # 高亮步骤6
        self.play(
            Indicate(self.steps_objs[5], scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 标题
        step_title = Text(
            "Step 6: 检验作答",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5 + LEFT * 1)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 移动解到上方
        self.play(
            self.solutions.animate.move_to(UP * 3),
            run_time=0.8
        )
        
        # 检验 x₁ = 10%
        verify1_title = Text(
            "检验 x₁ = 10%:",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_SOLUTION
        ).move_to(UP * 0.8 + LEFT * 2)
        
        self.play(FadeIn(verify1_title), run_time=0.5)
        
        calc1 = MathTex(
            r"100 \times 1.1^2 = 100 \times 1.21 = 121",
            font_size=26,
            color=WHITE
        ).next_to(verify1_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Write(calc1), run_time=1.0)
        
        check1 = Text(
            "✓ 计算正确",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_SOLUTION
        ).next_to(calc1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        meaning1 = Text(
            "✓ 增长10%，符合实际",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_SOLUTION
        ).next_to(check1, DOWN, aligned_edge=LEFT, buff=0.1)
        
        self.play(
            FadeIn(check1, shift=UP * 0.2),
            FadeIn(meaning1, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 检验 x₂ = -210%
        verify2_title = Text(
            "检验 x₂ = -210%:",
            font=self.FONT_CHINESE,
            font_size=26,
            color=RED
        ).move_to(DOWN * 2 + LEFT * 2)
        
        self.play(FadeIn(verify2_title), run_time=0.5)
        
        meaning2 = Text(
            "✗ 增长-210%不合实际",
            font=self.FONT_CHINESE,
            font_size=24,
            color=RED
        ).next_to(verify2_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        reason = Text(
            "(销售额不可能变为负数)",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_A
        ).next_to(meaning2, DOWN, aligned_edge=LEFT, buff=0.1)
        
        self.play(
            FadeIn(meaning2, shift=UP * 0.2),
            FadeIn(reason),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 最终答案
        final_box = Rectangle(
            width=6,
            height=1.2,
            color=self.COLOR_SOLUTION,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(DOWN * 4.5)
        
        final_answer = Text(
            "答: 增长率为 10%",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_SOLUTION
        ).move_to(final_box.get_center())
        
        self.play(
            Create(final_box),
            FadeIn(final_answer, scale=1.1),
            run_time=1.0
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(self.solutions),
            FadeOut(verify1_title),
            FadeOut(calc1),
            FadeOut(check1),
            FadeOut(meaning1),
            FadeOut(verify2_title),
            FadeOut(meaning2),
            FadeOut(reason),
            FadeOut(final_box),
            FadeOut(final_answer),
            run_time=0.8
        )
    
    def show_summary(self):
        """场景9: 方法总结"""
        # 清空侧边步骤
        steps_group = VGroup(
            self.steps_title,
            *self.steps_objs,
            *self.steps_arrows
        )
        self.play(FadeOut(steps_group), FadeOut(self.problem_group), FadeOut(self.saved_variable), run_time=0.5)
        
        # 标题
        title = Text(
            "解题方法总结",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        self.play(FadeIn(title, scale=1.1), run_time=0.8)
        
        # 六步法卡片
        steps_summary = [
            "① 审题: 理解题意，找关键信息",
            "② 设未知数: 选择合适的未知数",
            "③ 找等量关系: 建立数学模型",
            "④ 列方程: 写出方程",
            "⑤ 解方程: 求解未知数",
            "⑥ 检验作答: 验证实际意义"
        ]
        
        cards = VGroup()
        for i, step in enumerate(steps_summary):
            card = Text(
                step,
                font=self.FONT_CHINESE,
                font_size=22,
                color=WHITE
            ).move_to(UP * (3 - i * 0.9))
            cards.add(card)
        
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
        
        self.wait(1.0)
        
        # 关键提示
        key_tip = Text(
            "关键: 审题和检验最重要！",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(key_tip, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 适用范围
        scope = Text(
            "适用于: 增长率、工程、行程等问题",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(scope), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(key_tip),
            FadeOut(scope),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景10: 片尾关注"""
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
            "关注我，学更多应用题技巧！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 装饰元素 - 小公式
        decorations = VGroup()
        formulas = [
            r"x + y",
            r"x^2",
            r"(1+x)^2",
            r"\%"
        ]
        
        for i, formula in enumerate(formulas):
            deco = MathTex(formula, font_size=28, color=self.COLOR_PROBLEM)
            angle = i * PI / 2
            deco.move_to(2.5 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 3.5)
            decorations.add(deco)
        
        self.play(
            *[FadeIn(d, scale=0.5) for d in decorations],
            run_time=0.6
        )
        
        self.play(
            Rotate(decorations, angle=2*PI, run_time=2, rate_func=linear),
            run_time=2
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql algebra_application.py AlgebraApplication  # 快速预览
# manim -qh algebra_application.py AlgebraApplication   # 高质量渲染