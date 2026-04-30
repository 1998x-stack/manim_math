"""
算法的概念 - Algorithm Concept
使用 Manim 创建的高中数学教学视频

内容: 算法的定义、算法五要素、流程图示例
目标观众: 高二学生
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


class AlgorithmConcept(Scene):
    """
    算法概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 算法定义
    3. 五要素介绍
    4. 五要素详解（5个子场景）
    5. 流程图示例
    6. 五要素回顾
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要概念
        self.COLOR_SECONDARY = "#e74c3c"     # 红色 - 重要标记
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        self.COLOR_SUCCESS = "#2ecc71"       # 绿色 - 成功/输出
        
        # 流程图元素颜色
        self.COLOR_START_END = "#9b59b6"     # 紫色 - 开始/结束
        self.COLOR_PROCESS = "#3498db"       # 蓝色 - 处理框
        self.COLOR_DECISION = "#f39c12"      # 橙色 - 判断框
        self.COLOR_IO = "#2ecc71"            # 绿色 - 输入输出
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_five_features_intro()
        self.show_feature_finiteness()
        self.show_feature_determinacy()
        self.show_feature_feasibility()
        self.show_feature_input()
        self.show_feature_output()
        self.show_flowchart_example()
        self.show_summary()
        self.show_outro()
    
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
        hook_question = Text(
            "计算机是如何解决问题的?",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 代码滚动效果
        code_lines = VGroup(
            Text("if (condition) {", font="Courier New", font_size=18, color=self.COLOR_PRIMARY),
            Text("    process();", font="Courier New", font_size=18, color=self.COLOR_PRIMARY),
            Text("    return result;", font="Courier New", font_size=18, color=self.COLOR_PRIMARY),
            Text("}", font="Courier New", font_size=18, color=self.COLOR_PRIMARY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 2)
        
        for i, line in enumerate(code_lines):
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.3)
            if i < len(code_lines) - 1:
                self.wait(0.1)
        
        # 引导文字
        hint_text = Text(
            "答案就是: 算法",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.9)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(code_lines),
            FadeOut(hint_text),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 算法定义"""
        # 标题
        title = Text(
            "算法 Algorithm",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义框
        definition_text = Text(
            "按照一定规则解决某一类问题的\n明确和有限的步骤",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 3)
        
        definition_box = SurroundingRectangle(
            definition_text,
            color=self.COLOR_PRIMARY,
            buff=0.5,
            corner_radius=0.2
        )
        
        definition_group = VGroup(definition_box, definition_text)
        
        self.play(FadeIn(definition_group, shift=UP * 0.5), run_time=0.8)
        
        # 关键词高亮
        keywords = VGroup(
            Text("规则", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT),
            Text("明确", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT),
            Text("有限", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT),
            Text("步骤", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2)
        
        for i, word in enumerate(keywords):
            self.play(
                FadeIn(word, scale=1.2),
                run_time=0.3
            )
            if i < len(keywords) - 1:
                self.wait(0.2)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_group),
            FadeOut(keywords),
            run_time=0.5
        )
    
    def show_five_features_intro(self):
        """场景3: 五要素介绍"""
        # 标题
        title = Text(
            "算法的五个基本特征",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 五个图标（圆圈编号）
        icons = VGroup()
        for i in range(1, 6):
            circle = Circle(radius=0.4, color=self.COLOR_PRIMARY, stroke_width=3)
            number = Text(
                str(i),
                font="PingFang SC",
                font_size=28,
                color=self.COLOR_PRIMARY
            )
            icon = VGroup(circle, number)
            icons.add(icon)
        
        icons.arrange(RIGHT, buff=0.6).move_to(UP * 2)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        
        # 提示文字
        hint = Text(
            "让我们逐个了解",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(hint), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(icons),
            FadeOut(hint),
            run_time=0.4
        )
    
    def show_feature_finiteness(self):
        """场景4.1: 有穷性"""
        # 标题
        title = Text(
            "① 有穷性 Finiteness",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 图示 - 步骤序列
        steps = VGroup()
        for i in range(1, 6):
            if i < 5:
                step = Text(
                    f"Step{i}",
                    font="Courier New",
                    font_size=18,
                    color=WHITE
                )
            else:
                step = Text(
                    "END",
                    font="Courier New",
                    font_size=18,
                    color=self.COLOR_SUCCESS
                )
            steps.add(step)
        
        # 添加箭头
        diagram = VGroup()
        for i, step in enumerate(steps):
            diagram.add(step)
            if i < len(steps) - 1:
                arrow = Arrow(
                    ORIGIN,
                    RIGHT * 0.8,
                    buff=0.1,
                    stroke_width=3,
                    color=self.COLOR_AUXILIARY
                )
                diagram.add(arrow)
        
        diagram.arrange(RIGHT, buff=0.2).move_to(UP * 2)
        
        self.play(Create(diagram), run_time=1.2)
        
        # 说明文字
        explanation = Text(
            "算法必须在有限步骤内结束",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, diagram, explanation)),
            run_time=0.4
        )
    
    def show_feature_determinacy(self):
        """场景4.2: 确定性"""
        # 标题
        title = Text(
            "② 确定性 Determinacy",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 图示 - 相同输入产生相同输出
        # 第一行
        input1 = Text("输入A", font="PingFang SC", font_size=18, color=self.COLOR_IO)
        process1 = Rectangle(width=1.5, height=0.8, color=self.COLOR_PROCESS)
        process1_text = Text("处理", font="PingFang SC", font_size=16, color=WHITE)
        output1 = Text("输出B", font="PingFang SC", font_size=18, color=self.COLOR_SUCCESS)
        
        arrow1_1 = Arrow(ORIGIN, RIGHT * 0.8, buff=0.1, stroke_width=2, color=self.COLOR_AUXILIARY)
        arrow1_2 = Arrow(ORIGIN, RIGHT * 0.8, buff=0.1, stroke_width=2, color=self.COLOR_AUXILIARY)
        
        line1 = VGroup(input1, arrow1_1, process1, process1_text, arrow1_2, output1)
        line1.arrange(RIGHT, buff=0.2)
        process1_text.move_to(process1.get_center())
        
        # 第二行
        input2 = Text("输入A", font="PingFang SC", font_size=18, color=self.COLOR_IO)
        process2 = Rectangle(width=1.5, height=0.8, color=self.COLOR_PROCESS)
        process2_text = Text("处理", font="PingFang SC", font_size=16, color=WHITE)
        output2 = Text("输出B", font="PingFang SC", font_size=18, color=self.COLOR_SUCCESS)
        
        arrow2_1 = Arrow(ORIGIN, RIGHT * 0.8, buff=0.1, stroke_width=2, color=self.COLOR_AUXILIARY)
        arrow2_2 = Arrow(ORIGIN, RIGHT * 0.8, buff=0.1, stroke_width=2, color=self.COLOR_AUXILIARY)
        
        line2 = VGroup(input2, arrow2_1, process2, process2_text, arrow2_2, output2)
        line2.arrange(RIGHT, buff=0.2)
        process2_text.move_to(process2.get_center())
        
        diagram = VGroup(line1, line2).arrange(DOWN, buff=0.6).move_to(UP * 1.5)
        
        self.play(Create(diagram), run_time=1.2)
        
        # 说明文字
        explanation = Text(
            "相同输入必产生相同输出",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, diagram, explanation)),
            run_time=0.4
        )
    
    def show_feature_feasibility(self):
        """场景4.3: 可行性"""
        # 标题
        title = Text(
            "③ 可行性 Feasibility",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 图示 - 可执行 vs 不可执行
        feasible = VGroup(
            Text("✓", font_size=36, color=self.COLOR_SUCCESS),
            Text("可执行的操作", font="PingFang SC", font_size=18, color=WHITE)
        ).arrange(RIGHT, buff=0.3)
        
        infeasible = VGroup(
            Text("✗", font_size=36, color=self.COLOR_SECONDARY),
            Text("不可执行的操作", font="PingFang SC", font_size=18, color=GRAY_A)
        ).arrange(RIGHT, buff=0.3)
        
        diagram = VGroup(feasible, infeasible).arrange(DOWN, buff=0.8).move_to(UP * 2)
        
        self.play(FadeIn(feasible), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(infeasible), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "每一步都必须可执行",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, diagram, explanation)),
            run_time=0.4
        )
    
    def show_feature_input(self):
        """场景4.4: 输入"""
        # 标题
        title = Text(
            "④ 输入 Input",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 图示 - 输入到算法
        input_box = Rectangle(width=1.8, height=0.8, color=self.COLOR_IO)
        input_text = Text("Input", font="Courier New", font_size=18, color=WHITE)
        input_text.move_to(input_box.get_center())
        
        arrow = Arrow(ORIGIN, RIGHT * 1.2, buff=0.1, stroke_width=3, color=self.COLOR_AUXILIARY)
        
        algo_box = Rectangle(width=2.0, height=0.8, color=self.COLOR_PROCESS)
        algo_text = Text("算法", font="PingFang SC", font_size=18, color=WHITE)
        algo_text.move_to(algo_box.get_center())
        
        diagram = VGroup(input_box, input_text, arrow, algo_box, algo_text).arrange(RIGHT, buff=0.2).move_to(UP * 2)
        
        self.play(Create(diagram), run_time=1.0)
        
        # 注释
        note = Text(
            "可以有0个或多个",
            font="PingFang SC",
            font_size=16,
            color=GRAY_A
        ).next_to(diagram, DOWN, buff=0.5)
        
        self.play(FadeIn(note), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "算法接收外部数据",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, diagram, note, explanation)),
            run_time=0.4
        )
    
    def show_feature_output(self):
        """场景4.5: 输出"""
        # 标题
        title = Text(
            "⑤ 输出 Output",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 图示 - 算法到输出
        algo_box = Rectangle(width=2.0, height=0.8, color=self.COLOR_PROCESS)
        algo_text = Text("算法", font="PingFang SC", font_size=18, color=WHITE)
        algo_text.move_to(algo_box.get_center())
        
        arrow = Arrow(ORIGIN, RIGHT * 1.2, buff=0.1, stroke_width=3, color=self.COLOR_AUXILIARY)
        
        output_box = Rectangle(width=1.8, height=0.8, color=self.COLOR_SUCCESS)
        output_text = Text("Output", font="Courier New", font_size=18, color=WHITE)
        output_text.move_to(output_box.get_center())
        
        diagram = VGroup(algo_box, algo_text, arrow, output_box, output_text).arrange(RIGHT, buff=0.2).move_to(UP * 2)
        
        self.play(Create(diagram), run_time=1.0)
        
        # 注释
        note = Text(
            "至少有1个",
            font="PingFang SC",
            font_size=16,
            color=GRAY_A
        ).next_to(diagram, DOWN, buff=0.5)
        
        self.play(FadeIn(note), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "算法必须产生结果",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, diagram, note, explanation)),
            run_time=0.4
        )
    
    def show_flowchart_example(self):
        """场景5: 流程图示例 - 求两数最大值"""
        # 标题
        title = Text(
            "流程图示例: 求最大值",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 7)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # 流程图节点坐标
        start_pos = np.array([0, 5.5, 0])
        input_pos = np.array([0, 4.0, 0])
        decision_pos = np.array([0, 2.3, 0])
        process_left_pos = np.array([-1.8, 0.5, 0])
        process_right_pos = np.array([1.8, 0.5, 0])
        merge_pos = np.array([0, -1.0, 0])
        output_pos = np.array([0, -2.5, 0])
        end_pos = np.array([0, -4.0, 0])
        
        # 1. 开始节点（椭圆）
        start_ellipse = Ellipse(width=1.8, height=0.8, color=self.COLOR_START_END, fill_opacity=0.2)
        start_ellipse.move_to(start_pos)
        start_text = Text("开始", font="PingFang SC", font_size=18, color=WHITE)
        start_text.move_to(start_pos)
        start_node = VGroup(start_ellipse, start_text)
        
        self.play(FadeIn(start_node), run_time=0.5)
        
        # 箭头1
        arrow1 = Arrow(start_pos + DOWN * 0.4, input_pos + UP * 0.5, buff=0, stroke_width=2, color=WHITE)
        self.play(Create(arrow1), run_time=0.3)
        
        # 2. 输入节点（平行四边形）
        input_para = Polygon(
            input_pos + np.array([-1.2, 0.4, 0]),
            input_pos + np.array([1.0, 0.4, 0]),
            input_pos + np.array([1.2, -0.4, 0]),
            input_pos + np.array([-1.0, -0.4, 0]),
            color=self.COLOR_IO,
            fill_opacity=0.2
        )
        input_text = Text("输入 a, b", font="PingFang SC", font_size=16, color=WHITE)
        input_text.move_to(input_pos)
        input_node = VGroup(input_para, input_text)
        
        self.play(FadeIn(input_node), run_time=0.8)
        
        # 箭头2
        arrow2 = Arrow(input_pos + DOWN * 0.5, decision_pos + UP * 0.7, buff=0, stroke_width=2, color=WHITE)
        self.play(Create(arrow2), run_time=0.3)
        
        # 3. 判断节点（菱形）
        decision_diamond = Polygon(
            decision_pos + UP * 0.7,
            decision_pos + RIGHT * 1.2,
            decision_pos + DOWN * 0.7,
            decision_pos + LEFT * 1.2,
            color=self.COLOR_DECISION,
            fill_opacity=0.2
        )
        decision_text = Text("a > b ?", font="Courier New", font_size=16, color=WHITE)
        decision_text.move_to(decision_pos)
        decision_node = VGroup(decision_diamond, decision_text)
        
        self.play(FadeIn(decision_node), run_time=1.0)
        
        # 左分支（是）
        yes_label = Text("是", font="PingFang SC", font_size=14, color=self.COLOR_SUCCESS)
        yes_label.move_to(decision_pos + LEFT * 0.8 + DOWN * 0.3)
        
        arrow3_left = Arrow(
            decision_pos + LEFT * 1.2,
            process_left_pos + UP * 0.5,
            path_arc=-0.5,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SUCCESS
        )
        
        process_left_rect = Rectangle(width=2.0, height=0.8, color=self.COLOR_PROCESS, fill_opacity=0.2)
        process_left_rect.move_to(process_left_pos)
        process_left_text = Text("max = a", font="Courier New", font_size=16, color=WHITE)
        process_left_text.move_to(process_left_pos)
        process_left_node = VGroup(process_left_rect, process_left_text)
        
        self.play(
            FadeIn(yes_label),
            Create(arrow3_left),
            run_time=0.5
        )
        self.play(FadeIn(process_left_node), run_time=0.5)
        
        # 右分支（否）
        no_label = Text("否", font="PingFang SC", font_size=14, color=self.COLOR_SECONDARY)
        no_label.move_to(decision_pos + RIGHT * 0.8 + DOWN * 0.3)
        
        arrow3_right = Arrow(
            decision_pos + RIGHT * 1.2,
            process_right_pos + UP * 0.5,
            path_arc=0.5,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SECONDARY
        )
        
        process_right_rect = Rectangle(width=2.0, height=0.8, color=self.COLOR_PROCESS, fill_opacity=0.2)
        process_right_rect.move_to(process_right_pos)
        process_right_text = Text("max = b", font="Courier New", font_size=16, color=WHITE)
        process_right_text.move_to(process_right_pos)
        process_right_node = VGroup(process_right_rect, process_right_text)
        
        self.play(
            FadeIn(no_label),
            Create(arrow3_right),
            run_time=0.5
        )
        self.play(FadeIn(process_right_node), run_time=0.5)
        
        # 汇合箭头
        arrow4_left = Arrow(process_left_pos + DOWN * 0.4, merge_pos + LEFT * 0.5 + UP * 0.2, buff=0, stroke_width=2, color=WHITE)
        arrow4_right = Arrow(process_right_pos + DOWN * 0.4, merge_pos + RIGHT * 0.5 + UP * 0.2, buff=0, stroke_width=2, color=WHITE)
        
        self.play(
            Create(arrow4_left),
            Create(arrow4_right),
            run_time=0.6
        )
        
        # 箭头5（从汇合点到输出）
        arrow5 = Arrow(merge_pos, output_pos + UP * 0.5, buff=0, stroke_width=2, color=WHITE)
        self.play(Create(arrow5), run_time=0.3)
        
        # 4. 输出节点
        output_para = Polygon(
            output_pos + np.array([-1.2, 0.4, 0]),
            output_pos + np.array([1.0, 0.4, 0]),
            output_pos + np.array([1.2, -0.4, 0]),
            output_pos + np.array([-1.0, -0.4, 0]),
            color=self.COLOR_IO,
            fill_opacity=0.2
        )
        output_text = Text("输出 max", font="PingFang SC", font_size=16, color=WHITE)
        output_text.move_to(output_pos)
        output_node = VGroup(output_para, output_text)
        
        self.play(FadeIn(output_node), run_time=0.8)
        
        # 箭头6
        arrow6 = Arrow(output_pos + DOWN * 0.5, end_pos + UP * 0.4, buff=0, stroke_width=2, color=WHITE)
        self.play(Create(arrow6), run_time=0.3)
        
        # 5. 结束节点
        end_ellipse = Ellipse(width=1.8, height=0.8, color=self.COLOR_START_END, fill_opacity=0.2)
        end_ellipse.move_to(end_pos)
        end_text = Text("结束", font="PingFang SC", font_size=18, color=WHITE)
        end_text.move_to(end_pos)
        end_node = VGroup(end_ellipse, end_text)
        
        self.play(FadeIn(end_node), run_time=0.5)
        
        # 整体闪烁
        all_elements = VGroup(
            start_node, arrow1, input_node, arrow2, decision_node,
            yes_label, arrow3_left, process_left_node,
            no_label, arrow3_right, process_right_node,
            arrow4_left, arrow4_right, arrow5, output_node, arrow6, end_node
        )
        
        self.play(Indicate(all_elements, scale_factor=1.02), run_time=0.7)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_elements),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景6: 五要素回顾"""
        # 标题
        title = Text(
            "算法五要素",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 五要素列表
        features = VGroup(
            Text("① 有穷性 - 有限步骤", font="PingFang SC", font_size=self.FONT_BODY, color=WHITE),
            Text("② 确定性 - 明确无歧义", font="PingFang SC", font_size=self.FONT_BODY, color=WHITE),
            Text("③ 可行性 - 可执行", font="PingFang SC", font_size=self.FONT_BODY, color=WHITE),
            Text("④ 输入 - 0个或多个", font="PingFang SC", font_size=self.FONT_BODY, color=WHITE),
            Text("⑤ 输出 - 1个或多个", font="PingFang SC", font_size=self.FONT_BODY, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 1)
        
        self.play(FadeIn(features, lag_ratio=0.2), run_time=2.0)
        
        # 整体闪烁
        self.play(Indicate(features, scale_factor=1.05), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(features),
            run_time=0.5
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车\n@emptyandcalm",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多算法技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素（小三角形旋转）
        triangles = VGroup(*[
            RegularPolygon(n=3, color=GOLD, fill_opacity=0.8)
            .scale(0.4)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.8
        )
        
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )


# 运行命令:
# manim -pql algorithm_concept.py AlgorithmConcept  # 快速预览
# manim -qh algorithm_concept.py AlgorithmConcept   # 高质量渲染
# manim -qk algorithm_concept.py AlgorithmConcept   # 4K质量