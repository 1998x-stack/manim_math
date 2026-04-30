"""
基本算法语句 - Basic Algorithm Statements
使用 Manim 创建的高中数学教学视频

内容: 五种基本算法语句（赋值、输入、输出、条件、循环）
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


class AlgorithmStatements(Scene):
    """
    基本算法语句教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 基本语句定义
    3. 五种语句介绍
    4. 五种语句详解（5个子场景）
    5. 综合示例
    6. 五种语句回顾
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"
        self.COLOR_SECONDARY = "#e74c3c"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_SUCCESS = "#2ecc71"
        
        # 语句类型颜色
        self.COLOR_ASSIGNMENT = "#3498db"
        self.COLOR_INPUT = "#2ecc71"
        self.COLOR_OUTPUT = "#2ecc71"
        self.COLOR_CONDITION = "#f39c12"
        self.COLOR_LOOP = "#9b59b6"
        
        # 代码颜色
        self.COLOR_CODE_BG = "#2c3e50"
        self.COLOR_CODE_TEXT = WHITE
        self.COLOR_CODE_KEYWORD = "#e74c3c"
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_CODE = 18
        self.FONT_LABEL = 16
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_five_statements_intro()
        self.show_assignment_statement()
        self.show_input_statement()
        self.show_output_statement()
        self.show_conditional_statement()
        self.show_loop_statement()
        self.show_comprehensive_example()
        self.show_summary()
        self.show_outro()
    
    def create_code_line(self, text, font_size=18, color=WHITE):
        """创建代码行"""
        return Text(text, font="Courier New", font_size=font_size, color=color)
    
    def create_variable_box(self, var_name, value, color=None):
        """创建变量框"""
        if color is None:
            color = self.COLOR_PRIMARY
        
        box = Rectangle(width=2.2, height=0.8, color=color, stroke_width=2)
        
        label = Text(f"{var_name}:", font="Courier New", font_size=16, color=WHITE)
        label.next_to(box.get_left(), RIGHT, buff=0.2)
        
        val_text = Text(str(value), font="Courier New", font_size=16, color=color)
        val_text.next_to(label, RIGHT, buff=0.2)
        
        group = VGroup(box, label, val_text)
        return group
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何让计算机执行算法?",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 代码片段
        code_snippet = VGroup(
            self.create_code_line("x = 5", color=self.COLOR_ASSIGNMENT),
            self.create_code_line("IF x > 0 THEN", color=self.COLOR_CONDITION),
            self.create_code_line("FOR i = 1 TO 10", color=self.COLOR_LOOP)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 2)
        
        for line in code_snippet:
            self.play(FadeIn(line, shift=UP * 0.2), run_time=0.4)
        
        # 引导文字
        hint_text = Text(
            "答案: 基本算法语句",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(code_snippet),
            FadeOut(hint_text),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 基本语句定义"""
        # 标题
        title = Text(
            "基本算法语句",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义框
        definition_text = Text(
            "用特定语法描述算法步骤的代码语句\n是编写程序的基础",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 3)
        
        definition_box = SurroundingRectangle(
            definition_text,
            color=self.COLOR_PRIMARY,
            buff=0.5
        )
        
        definition_group = VGroup(definition_box, definition_text)
        
        self.play(FadeIn(definition_group, shift=UP * 0.5), run_time=0.8)
        
        # 五种语句图标
        icons = VGroup(
            Text("=", font="Courier New", font_size=28, color=self.COLOR_ASSIGNMENT),
            Text("IN", font="Courier New", font_size=24, color=self.COLOR_INPUT),
            Text("OUT", font="Courier New", font_size=24, color=self.COLOR_OUTPUT),
            Text("IF", font="Courier New", font_size=24, color=self.COLOR_CONDITION),
            Text("FOR", font="Courier New", font_size=24, color=self.COLOR_LOOP)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_group),
            FadeOut(icons),
            run_time=0.5
        )
    
    def show_five_statements_intro(self):
        """场景3: 五种语句介绍"""
        # 标题
        title = Text(
            "五种基本算法语句",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 五个标签
        labels = VGroup(
            Text("① 赋值", font="PingFang SC", font_size=22, color=self.COLOR_ASSIGNMENT),
            Text("② 输入", font="PingFang SC", font_size=22, color=self.COLOR_INPUT),
            Text("③ 输出", font="PingFang SC", font_size=22, color=self.COLOR_OUTPUT),
            Text("④ 条件", font="PingFang SC", font_size=22, color=self.COLOR_CONDITION),
            Text("⑤ 循环", font="PingFang SC", font_size=22, color=self.COLOR_LOOP)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 1)
        
        self.play(FadeIn(labels, lag_ratio=0.2), run_time=1.0)
        
        # 提示
        hint = Text(
            "让我们逐个学习",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(hint), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(labels),
            FadeOut(hint),
            run_time=0.4
        )
    
    def show_assignment_statement(self):
        """场景4.1: 赋值语句"""
        # 标题
        title = Text(
            "① 赋值语句",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_ASSIGNMENT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 代码
        code1 = self.create_code_line("x = 3", font_size=20)
        code2 = self.create_code_line("y = x + 5", font_size=20)
        code_group = VGroup(code1, code2).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 3)
        
        self.play(FadeIn(code1), run_time=0.5)
        
        # 变量框
        var_x = self.create_variable_box("x", "3", self.COLOR_ASSIGNMENT)
        var_x.move_to(ORIGIN + LEFT * 1.5)
        
        # 演示 x = 3
        value_3 = Text("3", font="Courier New", font_size=18, color=self.COLOR_ASSIGNMENT)
        value_3.next_to(code1, RIGHT, buff=0.5)
        
        self.play(FadeIn(value_3), run_time=0.3)
        self.play(
            Create(Arrow(value_3.get_center(), var_x.get_center(), buff=0.2, color=self.COLOR_ASSIGNMENT)),
            FadeIn(var_x),
            FadeOut(value_3),
            run_time=0.8
        )
        
        # 演示 y = x + 5
        self.play(FadeIn(code2), run_time=0.5)
        
        # 计算过程
        calc = Text("3 + 5 = 8", font="Courier New", font_size=16, color=WHITE)
        calc.next_to(code2, RIGHT, buff=0.5)
        self.play(FadeIn(calc), run_time=0.5)
        
        var_y = self.create_variable_box("y", "8", self.COLOR_ASSIGNMENT)
        var_y.move_to(ORIGIN + RIGHT * 1.5)
        
        self.play(
            FadeIn(var_y),
            FadeOut(calc),
            run_time=0.6
        )
        
        # 说明
        explanation = Text(
            "将值赋给变量，存储在内存中",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, code_group, var_x, var_y, explanation)),
            run_time=0.5
        )
    
    def show_input_statement(self):
        """场景4.2: 输入语句"""
        # 标题
        title = Text(
            "② 输入语句 INPUT",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_INPUT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 代码
        code = self.create_code_line("INPUT x", font_size=20)
        code.move_to(UP * 3)
        
        self.play(FadeIn(code), run_time=0.5)
        
        # 键盘图标（用文字代替）
        keyboard_icon = Text("⌨", font_size=40, color=GRAY_A)
        keyboard_icon.move_to(UP * 1 + LEFT * 2)
        
        self.play(FadeIn(keyboard_icon, scale=0.8), run_time=0.4)
        
        # 输入框
        input_box = Rectangle(width=2.0, height=0.8, color=self.COLOR_INPUT, stroke_width=2)
        input_box.move_to(UP * 1)
        input_label = Text("输入", font="PingFang SC", font_size=16, color=GRAY_A)
        input_label.next_to(input_box, UP, buff=0.1)
        
        self.play(Create(input_box), FadeIn(input_label), run_time=0.4)
        
        # 输入值
        input_value = Text("10", font="Courier New", font_size=18, color=self.COLOR_INPUT)
        input_value.move_to(input_box.get_center())
        
        self.play(FadeIn(input_value), run_time=0.4)
        
        # 变量框
        var_x = self.create_variable_box("x", "10", self.COLOR_INPUT)
        var_x.move_to(DOWN * 1)
        
        # 数据流动
        arrow = Arrow(input_box.get_bottom(), var_x.get_top(), buff=0.2, color=self.COLOR_INPUT)
        
        self.play(
            Create(arrow),
            FadeIn(var_x),
            run_time=0.8
        )
        
        # 说明
        explanation = Text(
            "从外部读取数据到变量",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, code, keyboard_icon, input_box, input_label,
                input_value, arrow, var_x, explanation
            )),
            run_time=0.5
        )
    
    def show_output_statement(self):
        """场景4.3: 输出语句"""
        # 标题
        title = Text(
            "③ 输出语句 PRINT",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_OUTPUT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 代码
        code1 = self.create_code_line("x = 100", font_size=20)
        code2 = self.create_code_line("PRINT x", font_size=20)
        code_group = VGroup(code1, code2).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 3)
        
        self.play(FadeIn(code_group), run_time=0.6)
        
        # 变量框
        var_x = self.create_variable_box("x", "100", self.COLOR_OUTPUT)
        var_x.move_to(UP * 0.5)
        
        self.play(FadeIn(var_x), run_time=0.5)
        
        # 输出框
        output_box = Rectangle(width=2.5, height=0.8, color=self.COLOR_OUTPUT, stroke_width=2)
        output_box.move_to(DOWN * 1.5)
        output_label = Text("输出", font="PingFang SC", font_size=16, color=GRAY_A)
        output_label.next_to(output_box, UP, buff=0.1)
        
        output_value = Text("100", font="Courier New", font_size=18, color=self.COLOR_OUTPUT)
        output_value.move_to(output_box.get_center())
        
        # 数据流动
        arrow = Arrow(var_x.get_bottom(), output_box.get_top(), buff=0.2, color=self.COLOR_OUTPUT)
        
        self.play(
            Create(arrow),
            Create(output_box),
            FadeIn(output_label),
            run_time=0.6
        )
        
        self.play(FadeIn(output_value), run_time=0.4)
        
        # 屏幕显示
        screen = Rectangle(width=3.5, height=1.2, color=GRAY_A, stroke_width=1, fill_opacity=0.1)
        screen.move_to(DOWN * 3.5)
        screen_value = Text("100", font="Courier New", font_size=24, color=self.COLOR_OUTPUT)
        screen_value.move_to(screen.get_center())
        
        self.play(
            FadeIn(screen),
            TransformFromCopy(output_value, screen_value),
            run_time=0.6
        )
        
        # 说明
        explanation = Text(
            "将变量值输出到屏幕",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, code_group, var_x, arrow, output_box,
                output_label, output_value, screen, screen_value, explanation
            )),
            run_time=0.5
        )
    
    def show_conditional_statement(self):
        """场景4.4: 条件语句"""
        # 标题
        title = Text(
            "④ 条件语句 IF-THEN-ELSE",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_CONDITION
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 代码（缩小）
        code_lines = VGroup(
            self.create_code_line("x = 5", font_size=16),
            self.create_code_line("IF x > 0 THEN", font_size=16),
            self.create_code_line("    y = 1", font_size=16),
            self.create_code_line("ELSE", font_size=16),
            self.create_code_line("    y = -1", font_size=16),
            self.create_code_line("END IF", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(UP * 3)
        
        self.play(FadeIn(code_lines), run_time=0.8)
        
        # 执行：x = 5
        var_x = self.create_variable_box("x", "5", self.COLOR_CONDITION)
        var_x.scale(0.8).move_to(UP * 0.5 + LEFT * 1.5)
        
        self.play(
            code_lines[0].animate.set_color(self.COLOR_HIGHLIGHT),
            FadeIn(var_x),
            run_time=0.5
        )
        self.play(code_lines[0].animate.set_color(WHITE), run_time=0.2)
        
        # 判断：x > 0?
        condition = Text("x > 0?", font="Courier New", font_size=16, color=self.COLOR_CONDITION)
        condition.move_to(ORIGIN + LEFT * 1.5)
        
        self.play(
            code_lines[1].animate.set_color(self.COLOR_HIGHLIGHT),
            FadeIn(condition),
            run_time=0.5
        )
        
        # 判断结果：是
        result = Text("是", font="PingFang SC", font_size=18, color=self.COLOR_SUCCESS)
        result.next_to(condition, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(result, scale=1.2),
            run_time=0.4
        )
        
        # 执行 THEN 分支
        self.play(
            code_lines[1].animate.set_color(WHITE),
            code_lines[2].animate.set_color(self.COLOR_SUCCESS),
            run_time=0.5
        )
        
        var_y = self.create_variable_box("y", "1", self.COLOR_SUCCESS)
        var_y.scale(0.8).move_to(UP * 0.5 + RIGHT * 1.5)
        
        self.play(
            FadeIn(var_y),
            run_time=0.5
        )
        
        self.play(code_lines[2].animate.set_color(WHITE), run_time=0.2)
        
        # 说明
        explanation = Text(
            "根据条件执行不同代码",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, code_lines, var_x, var_y,
                condition, result, explanation
            )),
            run_time=0.5
        )
    
    def show_loop_statement(self):
        """场景4.5: 循环语句"""
        # 标题
        title = Text(
            "⑤ 循环语句 FOR",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_LOOP
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 代码
        code_lines = VGroup(
            self.create_code_line("sum = 0", font_size=16),
            self.create_code_line("FOR i = 1 TO 3", font_size=16),
            self.create_code_line("    sum = sum + i", font_size=16),
            self.create_code_line("NEXT i", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(UP * 3.5)
        
        self.play(FadeIn(code_lines), run_time=0.8)
        
        # 初始化 sum = 0
        var_sum = self.create_variable_box("sum", "0", self.COLOR_LOOP)
        var_sum.scale(0.7).move_to(UP * 0.8 + LEFT * 1.8)
        
        self.play(
            code_lines[0].animate.set_color(self.COLOR_HIGHLIGHT),
            FadeIn(var_sum),
            run_time=0.5
        )
        self.play(code_lines[0].animate.set_color(WHITE), run_time=0.2)
        
        # 循环 i = 1, 2, 3
        var_i = self.create_variable_box("i", "1", self.COLOR_LOOP)
        var_i.scale(0.7).move_to(UP * 0.8 + RIGHT * 1.8)
        
        # 执行过程显示
        process = VGroup()
        
        for iteration in range(1, 4):
            # 更新 i
            var_i_new = self.create_variable_box("i", str(iteration), self.COLOR_LOOP)
            var_i_new.scale(0.7).move_to(var_i.get_center())
            
            if iteration == 1:
                self.play(
                    code_lines[1].animate.set_color(self.COLOR_HIGHLIGHT),
                    FadeIn(var_i_new),
                    run_time=0.4
                )
                var_i = var_i_new
            else:
                self.play(
                    Transform(var_i, var_i_new),
                    run_time=0.3
                )
            
            self.play(code_lines[1].animate.set_color(WHITE), run_time=0.1)
            
            # 执行 sum = sum + i
            self.play(
                code_lines[2].animate.set_color(self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
            
            # 计算新值
            old_val = (iteration - 1) * iteration // 2
            new_val = old_val + iteration
            
            # 显示计算过程
            calc_text = Text(
                f"{old_val}+{iteration}={new_val}",
                font="Courier New",
                font_size=14,
                color=YELLOW
            )
            calc_text.move_to(DOWN * 0.5)
            
            self.play(FadeIn(calc_text), run_time=0.3)
            
            # 更新 sum
            var_sum_new = self.create_variable_box("sum", str(new_val), self.COLOR_LOOP)
            var_sum_new.scale(0.7).move_to(var_sum.get_center())
            
            self.play(
                Transform(var_sum, var_sum_new),
                FadeOut(calc_text),
                run_time=0.4
            )
            
            self.play(code_lines[2].animate.set_color(WHITE), run_time=0.1)
        
        # 说明
        explanation = Text(
            "重复执行指定次数",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, code_lines, var_sum, var_i, explanation
            )),
            run_time=0.5
        )
    
    def show_comprehensive_example(self):
        """场景5: 综合示例"""
        # 标题
        title = Text(
            "综合示例: 求和程序",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 7)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 代码（左侧，缩小）
        code_lines = VGroup(
            self.create_code_line("INPUT n", font_size=14),
            self.create_code_line("sum = 0", font_size=14),
            self.create_code_line("FOR i=1 TO n", font_size=14),
            self.create_code_line("  sum=sum+i", font_size=14),
            self.create_code_line("NEXT i", font_size=14),
            self.create_code_line("PRINT sum", font_size=14)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(UP * 2.5 + LEFT * 2)
        
        self.play(FadeIn(code_lines), run_time=0.8)
        
        # 变量区（右侧）
        var_label = Text("变量:", font="PingFang SC", font_size=16, color=GRAY_A)
        var_label.move_to(UP * 4 + RIGHT * 2)
        self.play(FadeIn(var_label), run_time=0.3)
        
        # INPUT n
        self.play(code_lines[0].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        var_n = self.create_variable_box("n", "3", self.COLOR_INPUT)
        var_n.scale(0.6).move_to(UP * 3 + RIGHT * 2)
        self.play(FadeIn(var_n), run_time=0.4)
        self.play(code_lines[0].animate.set_color(WHITE), run_time=0.2)
        
        # sum = 0
        self.play(code_lines[1].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        var_sum = self.create_variable_box("sum", "0", self.COLOR_PRIMARY)
        var_sum.scale(0.6).move_to(UP * 2.2 + RIGHT * 2)
        self.play(FadeIn(var_sum), run_time=0.4)
        self.play(code_lines[1].animate.set_color(WHITE), run_time=0.2)
        
        # 循环 i = 1, 2, 3
        var_i = self.create_variable_box("i", "1", self.COLOR_LOOP)
        var_i.scale(0.6).move_to(UP * 1.4 + RIGHT * 2)
        
        # 快速执行循环
        for iteration in [1, 2, 3]:
            # FOR i
            self.play(code_lines[2].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.2)
            
            var_i_new = self.create_variable_box("i", str(iteration), self.COLOR_LOOP)
            var_i_new.scale(0.6).move_to(var_i.get_center())
            
            if iteration == 1:
                self.play(FadeIn(var_i_new), run_time=0.3)
                var_i = var_i_new
            else:
                self.play(Transform(var_i, var_i_new), run_time=0.2)
            
            self.play(code_lines[2].animate.set_color(WHITE), run_time=0.1)
            
            # sum = sum + i
            self.play(code_lines[3].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.2)
            
            old_val = (iteration - 1) * iteration // 2
            new_val = old_val + iteration
            
            var_sum_new = self.create_variable_box("sum", str(new_val), self.COLOR_PRIMARY)
            var_sum_new.scale(0.6).move_to(var_sum.get_center())
            
            self.play(Transform(var_sum, var_sum_new), run_time=0.3)
            self.play(code_lines[3].animate.set_color(WHITE), run_time=0.1)
        
        # PRINT sum
        self.play(code_lines[5].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        output = Text("输出: 6", font="Courier New", font_size=18, color=self.COLOR_SUCCESS)
        output.move_to(DOWN * 2)
        
        self.play(FadeIn(output, scale=1.2), run_time=0.5)
        self.play(code_lines[5].animate.set_color(WHITE), run_time=0.2)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, code_lines, var_label,
                var_n, var_sum, var_i, output
            )),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景6: 总结"""
        # 标题
        title = Text(
            "五种基本算法语句",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 五种语句
        statements = VGroup(
            Text("① 赋值语句  x = 表达式", font="PingFang SC", font_size=20, color=self.COLOR_ASSIGNMENT),
            Text("② 输入语句  INPUT 变量", font="PingFang SC", font_size=20, color=self.COLOR_INPUT),
            Text("③ 输出语句  PRINT 变量", font="PingFang SC", font_size=20, color=self.COLOR_OUTPUT),
            Text("④ 条件语句  IF...THEN...ELSE", font="PingFang SC", font_size=20, color=self.COLOR_CONDITION),
            Text("⑤ 循环语句  FOR / WHILE", font="PingFang SC", font_size=20, color=self.COLOR_LOOP)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 1)
        
        self.play(FadeIn(statements, lag_ratio=0.3), run_time=2.0)
        
        # 整体闪烁
        self.play(Indicate(statements, scale_factor=1.05), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(statements),
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
            "关注我, 学更多编程技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 代码符号装饰
        symbols = VGroup(
            Text("{", font="Courier New", font_size=40, color=self.COLOR_PRIMARY),
            Text("}", font="Courier New", font_size=40, color=self.COLOR_PRIMARY),
            Text("[", font="Courier New", font_size=40, color=self.COLOR_LOOP),
            Text("]", font="Courier New", font_size=40, color=self.COLOR_LOOP),
            Text("(", font="Courier New", font_size=40, color=self.COLOR_CONDITION),
            Text(")", font="Courier New", font_size=40, color=self.COLOR_CONDITION)
        )
        
        positions = [
            follow_text.get_center() + UP * 2.5 + LEFT * 2.5,
            follow_text.get_center() + UP * 2.5 + RIGHT * 2.5,
            follow_text.get_center() + DOWN * 2.5 + LEFT * 2.5,
            follow_text.get_center() + DOWN * 2.5 + RIGHT * 2.5,
            follow_text.get_center() + UP * 2 + LEFT * 3.5,
            follow_text.get_center() + UP * 2 + RIGHT * 3.5
        ]
        
        for i, symbol in enumerate(symbols):
            symbol.move_to(positions[i])
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in symbols],
            run_time=0.8
        )
        
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql algorithm_statements.py AlgorithmStatements  # 快速预览
# manim -qh algorithm_statements.py AlgorithmStatements   # 高质量渲染
# manim -qk algorithm_statements.py AlgorithmStatements   # 4K质量