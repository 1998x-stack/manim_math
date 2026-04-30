"""
程序框图 - Flowchart Basics
使用 Manim 创建的高中数学教学视频

内容: 程序框图的五种基本符号、三种基本结构
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


class FlowchartBasics(Scene):
    """
    程序框图教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 程序框图定义
    3. 五种符号介绍
    4. 五种符号详解（5个子场景）
    5. 三种结构介绍
    6. 顺序结构详解
    7. 条件结构详解
    8. 循环结构详解
    9. 三种结构总结
    10. 片尾关注
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
        
        # 流程图符号颜色
        self.COLOR_START_END = "#9b59b6"
        self.COLOR_PROCESS = "#3498db"
        self.COLOR_DECISION = "#f39c12"
        self.COLOR_IO = "#2ecc71"
        self.COLOR_ARROW = WHITE
        
        # 结构类型颜色
        self.COLOR_SEQUENCE = "#3498db"
        self.COLOR_CONDITION = "#f39c12"
        self.COLOR_LOOP = "#9b59b6"
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 20
        self.FONT_SMALL = 16
        
        # 符号标准尺寸
        self.SYMBOL_WIDTH = 2.0
        self.SYMBOL_HEIGHT = 0.8
        self.CORNER_RADIUS = 0.3
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_five_symbols_intro()
        self.show_symbol_start_end()
        self.show_symbol_io()
        self.show_symbol_process()
        self.show_symbol_decision()
        self.show_symbol_arrow()
        self.show_three_structures_intro()
        self.show_sequence_structure()
        self.show_condition_structure()
        self.show_loop_structure()
        self.show_summary()
        self.show_outro()
    
    def create_start_end_shape(self, center, width=2.0, height=0.8):
        """创建起止框（圆角矩形）"""
        return RoundedRectangle(
            width=width,
            height=height,
            corner_radius=self.CORNER_RADIUS,
            color=self.COLOR_START_END,
            fill_opacity=0.2
        ).move_to(center)
    
    def create_io_shape(self, center, width=2.0, height=0.8):
        """创建输入输出框（平行四边形）"""
        offset = 0.3
        parallelogram = Polygon(
            center + np.array([-width/2 + offset, height/2, 0]),
            center + np.array([width/2, height/2, 0]),
            center + np.array([width/2 - offset, -height/2, 0]),
            center + np.array([-width/2, -height/2, 0]),
            color=self.COLOR_IO,
            fill_opacity=0.2
        )
        return parallelogram
    
    def create_process_shape(self, center, width=2.0, height=0.8):
        """创建处理框（矩形）"""
        return Rectangle(
            width=width,
            height=height,
            color=self.COLOR_PROCESS,
            fill_opacity=0.2
        ).move_to(center)
    
    def create_decision_shape(self, center, width=1.2, height=0.7):
        """创建判断框（菱形）"""
        diamond = Polygon(
            center + UP * height,
            center + RIGHT * width,
            center + DOWN * height,
            center + LEFT * width,
            color=self.COLOR_DECISION,
            fill_opacity=0.2
        )
        return diamond
    
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
            "如何用图形表示算法?",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 简单流程图预览（开始→处理→结束）
        preview_start = self.create_start_end_shape(UP * 3 + LEFT * 2, width=1.5, height=0.6)
        preview_start_text = Text("开始", font="PingFang SC", font_size=14, color=WHITE)
        preview_start_text.move_to(preview_start.get_center())
        
        arrow1 = Arrow(
            preview_start.get_bottom(),
            preview_start.get_bottom() + DOWN * 0.5,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        
        preview_process = self.create_process_shape(UP * 2 + LEFT * 2, width=1.5, height=0.6)
        preview_process_text = Text("处理", font="PingFang SC", font_size=14, color=WHITE)
        preview_process_text.move_to(preview_process.get_center())
        
        arrow2 = Arrow(
            preview_process.get_bottom(),
            preview_process.get_bottom() + DOWN * 0.5,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        
        preview_end = self.create_start_end_shape(UP * 1 + LEFT * 2, width=1.5, height=0.6)
        preview_end_text = Text("结束", font="PingFang SC", font_size=14, color=WHITE)
        preview_end_text.move_to(preview_end.get_center())
        
        simple_flowchart = VGroup(
            preview_start, preview_start_text,
            arrow1,
            preview_process, preview_process_text,
            arrow2,
            preview_end, preview_end_text
        ).move_to(UP * 2)
        
        self.play(FadeIn(simple_flowchart, lag_ratio=0.2), run_time=1.2)
        
        # 引导文字
        hint_text = Text(
            "答案: 程序框图",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(simple_flowchart),
            FadeOut(hint_text),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 程序框图定义"""
        # 标题
        title = Text(
            "程序框图 Flowchart",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义框
        definition_text = Text(
            "用特定图形符号表示算法步骤的图形\n也称为流程图",
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
        
        # 关键词
        keywords = VGroup(
            Text("图形符号", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT),
            Text("算法步骤", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 2)
        
        for i, word in enumerate(keywords):
            self.play(FadeIn(word, scale=1.2), run_time=0.5)
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
    
    def show_five_symbols_intro(self):
        """场景3: 五种符号介绍"""
        # 标题
        title = Text(
            "程序框图的五种基本符号",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 五个符号图标（缩小版）
        icon1 = self.create_start_end_shape(ORIGIN, width=1.0, height=0.5)
        icon2 = self.create_io_shape(ORIGIN, width=1.0, height=0.5)
        icon3 = self.create_process_shape(ORIGIN, width=1.0, height=0.5)
        icon4 = self.create_decision_shape(ORIGIN, width=0.6, height=0.4)
        icon5 = Arrow(LEFT * 0.3, RIGHT * 0.3, buff=0, stroke_width=3, color=self.COLOR_ARROW)
        
        icons = VGroup(icon1, icon2, icon3, icon4, icon5).arrange(RIGHT, buff=0.5).move_to(UP * 2)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        
        # 提示文字
        hint = Text(
            "让我们逐个认识",
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
    
    def show_symbol_start_end(self):
        """场景4.1: 起止框"""
        # 标题
        title = Text(
            "① 起止框",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_START_END
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 符号图形
        shape = self.create_start_end_shape(UP * 2.5, width=2.5, height=1.0)
        self.play(Create(shape), run_time=0.6)
        
        # 示例文字
        example1 = Text("开始", font="PingFang SC", font_size=20, color=WHITE)
        example1.move_to(UP * 2.5 + LEFT * 0.8)
        
        example2 = Text("结束", font="PingFang SC", font_size=20, color=WHITE)
        example2.move_to(UP * 2.5 + RIGHT * 0.8)
        
        self.play(FadeIn(example1), FadeIn(example2), run_time=0.4)
        
        # 说明
        explanation = Text(
            "表示算法的开始或结束",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, shape, example1, example2, explanation)),
            run_time=0.4
        )
    
    def show_symbol_io(self):
        """场景4.2: 输入输出框"""
        # 标题
        title = Text(
            "② 输入输出框",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_IO
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 符号图形
        shape = self.create_io_shape(UP * 2.5, width=2.5, height=1.0)
        self.play(Create(shape), run_time=0.6)
        
        # 示例文字
        example1 = Text("输入 x", font="PingFang SC", font_size=18, color=WHITE)
        example1.move_to(UP * 2.5 + LEFT * 0.7)
        
        example2 = Text("输出 y", font="PingFang SC", font_size=18, color=WHITE)
        example2.move_to(UP * 2.5 + RIGHT * 0.7)
        
        self.play(FadeIn(example1), FadeIn(example2), run_time=0.4)
        
        # 说明
        explanation = Text(
            "表示数据的输入或输出",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, shape, example1, example2, explanation)),
            run_time=0.4
        )
    
    def show_symbol_process(self):
        """场景4.3: 处理框"""
        # 标题
        title = Text(
            "③ 处理框",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PROCESS
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 符号图形
        shape = self.create_process_shape(UP * 2.5, width=2.5, height=1.0)
        self.play(Create(shape), run_time=0.6)
        
        # 示例文字
        example = Text("x = x + 1", font="Courier New", font_size=20, color=WHITE)
        example.move_to(UP * 2.5)
        
        self.play(FadeIn(example), run_time=0.4)
        
        # 说明
        explanation = Text(
            "表示赋值、计算等处理操作",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, shape, example, explanation)),
            run_time=0.4
        )
    
    def show_symbol_decision(self):
        """场景4.4: 判断框"""
        # 标题
        title = Text(
            "④ 判断框",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_DECISION
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 符号图形
        shape = self.create_decision_shape(UP * 2.5, width=1.5, height=1.0)
        self.play(Create(shape), run_time=0.6)
        
        # 示例文字
        example = Text("x > 0?", font="Courier New", font_size=18, color=WHITE)
        example.move_to(UP * 2.5)
        
        # 出口标签
        yes_label = Text("是", font="PingFang SC", font_size=16, color=self.COLOR_SUCCESS)
        yes_label.move_to(UP * 2.5 + DOWN * 1.2)
        
        no_label = Text("否", font="PingFang SC", font_size=16, color=self.COLOR_SECONDARY)
        no_label.move_to(UP * 2.5 + RIGHT * 1.7)
        
        # 箭头
        arrow_down = Arrow(
            UP * 2.5 + DOWN * 1.0,
            UP * 2.5 + DOWN * 1.4,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SUCCESS
        )
        
        arrow_right = Arrow(
            UP * 2.5 + RIGHT * 1.5,
            UP * 2.5 + RIGHT * 1.9,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SECONDARY
        )
        
        self.play(FadeIn(example), run_time=0.4)
        self.play(
            Create(arrow_down),
            Create(arrow_right),
            FadeIn(yes_label),
            FadeIn(no_label),
            run_time=0.5
        )
        
        # 说明
        explanation = Text(
            "表示条件判断，有两个出口",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, shape, example,
                yes_label, no_label,
                arrow_down, arrow_right,
                explanation
            )),
            run_time=0.4
        )
    
    def show_symbol_arrow(self):
        """场景4.5: 流程线"""
        # 标题
        title = Text(
            "⑤ 流程线",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_ARROW
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 四个方向的箭头
        arrow_right = Arrow(LEFT * 1.5, RIGHT * 1.5, buff=0, stroke_width=3, color=WHITE)
        arrow_down = Arrow(UP * 1.5, DOWN * 1.5, buff=0, stroke_width=3, color=WHITE)
        arrow_left = Arrow(RIGHT * 1.5, LEFT * 1.5, buff=0, stroke_width=3, color=WHITE)
        arrow_up = Arrow(DOWN * 1.5, UP * 1.5, buff=0, stroke_width=3, color=WHITE)
        
        arrows = VGroup(arrow_right, arrow_down, arrow_left, arrow_up)
        arrows.arrange_in_grid(rows=2, cols=2, buff=1.0).move_to(UP * 2)
        
        self.play(Create(arrows, lag_ratio=0.2), run_time=0.8)
        
        # 说明
        explanation = Text(
            "表示程序的执行顺序",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(VGroup(title, arrows, explanation)),
            run_time=0.4
        )
    
    def show_three_structures_intro(self):
        """场景5: 三种结构介绍"""
        # 标题
        title = Text(
            "程序框图的三种基本结构",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 三个图标
        icon1 = Text("顺序", font="PingFang SC", font_size=24, color=self.COLOR_SEQUENCE)
        icon2 = Text("条件", font="PingFang SC", font_size=24, color=self.COLOR_CONDITION)
        icon3 = Text("循环", font="PingFang SC", font_size=24, color=self.COLOR_LOOP)
        
        icons = VGroup(icon1, icon2, icon3).arrange(RIGHT, buff=1.2).move_to(UP * 2)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        
        # 提示
        hint = Text(
            "理解这三种结构是关键",
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
    
    def show_sequence_structure(self):
        """场景6: 顺序结构"""
        # 标题
        title = Text(
            "顺序结构",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_SEQUENCE
        ).move_to(UP * 7)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 流程图节点
        center_x = 0
        
        # 开始
        start_pos = np.array([center_x, 5.5, 0])
        start_shape = self.create_start_end_shape(start_pos, width=1.8, height=0.7)
        start_text = Text("开始", font="PingFang SC", font_size=16, color=WHITE)
        start_text.move_to(start_pos)
        start_node = VGroup(start_shape, start_text)
        
        self.play(FadeIn(start_node), run_time=0.4)
        
        # 箭头1
        arrow1 = Arrow(
            start_pos + DOWN * 0.35,
            start_pos + DOWN * 0.9,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        self.play(Create(arrow1), run_time=0.3)
        
        # 输入
        input_pos = np.array([center_x, 4.0, 0])
        input_shape = self.create_io_shape(input_pos, width=1.8, height=0.7)
        input_text = Text("输入 a", font="PingFang SC", font_size=16, color=WHITE)
        input_text.move_to(input_pos)
        input_node = VGroup(input_shape, input_text)
        
        self.play(FadeIn(input_node), run_time=0.4)
        
        # 箭头2
        arrow2 = Arrow(
            input_pos + DOWN * 0.35,
            input_pos + DOWN * 0.9,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        self.play(Create(arrow2), run_time=0.3)
        
        # 处理
        process_pos = np.array([center_x, 2.5, 0])
        process_shape = self.create_process_shape(process_pos, width=1.8, height=0.7)
        process_text = Text("a = a + 1", font="Courier New", font_size=14, color=WHITE)
        process_text.move_to(process_pos)
        process_node = VGroup(process_shape, process_text)
        
        self.play(FadeIn(process_node), run_time=0.4)
        
        # 箭头3
        arrow3 = Arrow(
            process_pos + DOWN * 0.35,
            process_pos + DOWN * 0.9,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        self.play(Create(arrow3), run_time=0.3)
        
        # 输出
        output_pos = np.array([center_x, 1.0, 0])
        output_shape = self.create_io_shape(output_pos, width=1.8, height=0.7)
        output_text = Text("输出 a", font="PingFang SC", font_size=16, color=WHITE)
        output_text.move_to(output_pos)
        output_node = VGroup(output_shape, output_text)
        
        self.play(FadeIn(output_node), run_time=0.4)
        
        # 箭头4
        arrow4 = Arrow(
            output_pos + DOWN * 0.35,
            output_pos + DOWN * 0.9,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        self.play(Create(arrow4), run_time=0.3)
        
        # 结束
        end_pos = np.array([center_x, -0.5, 0])
        end_shape = self.create_start_end_shape(end_pos, width=1.8, height=0.7)
        end_text = Text("结束", font="PingFang SC", font_size=16, color=WHITE)
        end_text.move_to(end_pos)
        end_node = VGroup(end_shape, end_text)
        
        self.play(FadeIn(end_node), run_time=0.4)
        
        # 说明
        explanation = Text(
            "按顺序依次执行",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        all_elements = VGroup(
            title, start_node, arrow1, input_node, arrow2,
            process_node, arrow3, output_node, arrow4, end_node, explanation
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def show_condition_structure(self):
        """场景7: 条件结构"""
        # 标题
        title = Text(
            "条件结构 IF-THEN-ELSE",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_CONDITION
        ).move_to(UP * 7)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 节点位置
        center_x = 0
        left_x = -1.5
        right_x = 1.5
        
        # 开始和输入（快速显示）
        start_pos = np.array([center_x, 6.0, 0])
        start_shape = self.create_start_end_shape(start_pos, width=1.5, height=0.6)
        start_text = Text("开始", font="PingFang SC", font_size=14, color=WHITE)
        start_text.move_to(start_pos)
        
        input_pos = np.array([center_x, 4.8, 0])
        input_shape = self.create_io_shape(input_pos, width=1.5, height=0.6)
        input_text = Text("输入 x", font="PingFang SC", font_size=14, color=WHITE)
        input_text.move_to(input_pos)
        
        arrow_start = Arrow(start_pos + DOWN * 0.3, input_pos + UP * 0.3, buff=0, stroke_width=2, color=WHITE)
        
        start_input_group = VGroup(start_shape, start_text, arrow_start, input_shape, input_text)
        self.play(FadeIn(start_input_group), run_time=0.8)
        
        # 判断节点
        decision_pos = np.array([center_x, 3.2, 0])
        decision_shape = self.create_decision_shape(decision_pos, width=1.2, height=0.8)
        decision_text = Text("x > 0?", font="Courier New", font_size=14, color=WHITE)
        decision_text.move_to(decision_pos)
        
        arrow_to_decision = Arrow(input_pos + DOWN * 0.3, decision_pos + UP * 0.8, buff=0, stroke_width=2, color=WHITE)
        
        self.play(Create(arrow_to_decision), run_time=0.3)
        self.play(FadeIn(VGroup(decision_shape, decision_text)), run_time=0.6)
        
        # 左分支（是）
        yes_label = Text("是", font="PingFang SC", font_size=14, color=self.COLOR_SUCCESS)
        yes_label.move_to(decision_pos + LEFT * 0.8 + DOWN * 0.3)
        
        process_left_pos = np.array([left_x, 1.5, 0])
        process_left_shape = self.create_process_shape(process_left_pos, width=1.4, height=0.6)
        process_left_text = Text("y = x", font="Courier New", font_size=14, color=WHITE)
        process_left_text.move_to(process_left_pos)
        
        arrow_left = Arrow(
            decision_pos + LEFT * 1.2,
            process_left_pos + UP * 0.3,
            path_arc=-0.5,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SUCCESS
        )
        
        self.play(
            FadeIn(yes_label),
            Create(arrow_left),
            run_time=0.4
        )
        self.play(FadeIn(VGroup(process_left_shape, process_left_text)), run_time=0.4)
        
        # 右分支（否）
        no_label = Text("否", font="PingFang SC", font_size=14, color=self.COLOR_SECONDARY)
        no_label.move_to(decision_pos + RIGHT * 0.8 + DOWN * 0.3)
        
        process_right_pos = np.array([right_x, 1.5, 0])
        process_right_shape = self.create_process_shape(process_right_pos, width=1.4, height=0.6)
        process_right_text = Text("y = -x", font="Courier New", font_size=14, color=WHITE)
        process_right_text.move_to(process_right_pos)
        
        arrow_right = Arrow(
            decision_pos + RIGHT * 1.2,
            process_right_pos + UP * 0.3,
            path_arc=0.5,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SECONDARY
        )
        
        self.play(
            FadeIn(no_label),
            Create(arrow_right),
            run_time=0.4
        )
        self.play(FadeIn(VGroup(process_right_shape, process_right_text)), run_time=0.4)
        
        # 汇合
        merge_pos = np.array([center_x, 0.2, 0])
        arrow_merge_left = Arrow(
            process_left_pos + DOWN * 0.3,
            merge_pos + LEFT * 0.3,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        arrow_merge_right = Arrow(
            process_right_pos + DOWN * 0.3,
            merge_pos + RIGHT * 0.3,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        
        self.play(
            Create(arrow_merge_left),
            Create(arrow_merge_right),
            run_time=0.5
        )
        
        # 输出和结束
        output_pos = np.array([center_x, -1.2, 0])
        output_shape = self.create_io_shape(output_pos, width=1.5, height=0.6)
        output_text = Text("输出 y", font="PingFang SC", font_size=14, color=WHITE)
        output_text.move_to(output_pos)
        
        end_pos = np.array([center_x, -2.5, 0])
        end_shape = self.create_start_end_shape(end_pos, width=1.5, height=0.6)
        end_text = Text("结束", font="PingFang SC", font_size=14, color=WHITE)
        end_text.move_to(end_pos)
        
        arrow_to_output = Arrow(merge_pos, output_pos + UP * 0.3, buff=0, stroke_width=2, color=WHITE)
        arrow_to_end = Arrow(output_pos + DOWN * 0.3, end_pos + UP * 0.3, buff=0, stroke_width=2, color=WHITE)
        
        self.play(
            Create(arrow_to_output),
            FadeIn(VGroup(output_shape, output_text)),
            run_time=0.5
        )
        self.play(
            Create(arrow_to_end),
            FadeIn(VGroup(end_shape, end_text)),
            run_time=0.5
        )
        
        # 说明
        explanation = Text(
            "根据条件选择不同分支执行",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        all_elements = VGroup(
            title, start_input_group,
            arrow_to_decision, decision_shape, decision_text,
            yes_label, arrow_left, process_left_shape, process_left_text,
            no_label, arrow_right, process_right_shape, process_right_text,
            arrow_merge_left, arrow_merge_right,
            arrow_to_output, output_shape, output_text,
            arrow_to_end, end_shape, end_text,
            explanation
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def show_loop_structure(self):
        """场景8: 循环结构"""
        # 标题
        title = Text(
            "循环结构 WHILE",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_LOOP
        ).move_to(UP * 7)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 节点位置
        center_x = 0
        loop_x = -1.8
        
        # 开始
        start_pos = np.array([center_x, 6.0, 0])
        start_shape = self.create_start_end_shape(start_pos, width=1.3, height=0.5)
        start_text = Text("开始", font="PingFang SC", font_size=12, color=WHITE)
        start_text.move_to(start_pos)
        
        # 初始化
        init_pos = np.array([center_x, 5.0, 0])
        init_shape = self.create_process_shape(init_pos, width=1.5, height=0.6)
        init_text = VGroup(
            Text("i = 1", font="Courier New", font_size=11, color=WHITE),
            Text("sum = 0", font="Courier New", font_size=11, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(init_pos)
        
        arrow1 = Arrow(start_pos + DOWN * 0.25, init_pos + UP * 0.3, buff=0, stroke_width=2, color=WHITE)
        
        self.play(
            FadeIn(VGroup(start_shape, start_text)),
            Create(arrow1),
            FadeIn(VGroup(init_shape, init_text)),
            run_time=0.8
        )
        
        # 判断
        decision_pos = np.array([center_x, 3.5, 0])
        decision_shape = self.create_decision_shape(decision_pos, width=1.0, height=0.7)
        decision_text = Text("i ≤ 10?", font="Courier New", font_size=12, color=WHITE)
        decision_text.move_to(decision_pos)
        
        arrow2 = Arrow(init_pos + DOWN * 0.3, decision_pos + UP * 0.7, buff=0, stroke_width=2, color=WHITE)
        
        self.play(Create(arrow2), run_time=0.3)
        self.play(FadeIn(VGroup(decision_shape, decision_text)), run_time=0.6)
        
        # 循环体（左侧）
        yes_label = Text("是", font="PingFang SC", font_size=12, color=self.COLOR_SUCCESS)
        yes_label.move_to(decision_pos + LEFT * 0.7 + DOWN * 0.2)
        
        process1_pos = np.array([loop_x, 2.0, 0])
        process1_shape = self.create_process_shape(process1_pos, width=1.6, height=0.5)
        process1_text = Text("sum=sum+i", font="Courier New", font_size=11, color=WHITE)
        process1_text.move_to(process1_pos)
        
        process2_pos = np.array([loop_x, 0.8, 0])
        process2_shape = self.create_process_shape(process2_pos, width=1.6, height=0.5)
        process2_text = Text("i = i + 1", font="Courier New", font_size=11, color=WHITE)
        process2_text.move_to(process2_pos)
        
        arrow_to_loop = Arrow(
            decision_pos + LEFT * 1.0,
            process1_pos + UP * 0.25,
            path_arc=-0.4,
            buff=0,
            stroke_width=2,
            color=self.COLOR_SUCCESS
        )
        
        arrow_loop_internal = Arrow(
            process1_pos + DOWN * 0.25,
            process2_pos + UP * 0.25,
            buff=0,
            stroke_width=2,
            color=WHITE
        )
        
        self.play(
            FadeIn(yes_label),
            Create(arrow_to_loop),
            run_time=0.4
        )
        self.play(
            FadeIn(VGroup(process1_shape, process1_text)),
            Create(arrow_loop_internal),
            FadeIn(VGroup(process2_shape, process2_text)),
            run_time=0.6
        )
        
        # 回路箭头
        loop_back_arrow = Arrow(
            process2_pos + LEFT * 0.8,
            decision_pos + LEFT * 1.0 + UP * 0.5,
            path_arc=-1.5,
            buff=0.1,
            stroke_width=2,
            color=self.COLOR_LOOP
        )
        
        loop_label = Text("循环", font="PingFang SC", font_size=10, color=self.COLOR_LOOP)
        loop_label.move_to(np.array([loop_x - 1.2, 2.5, 0]))
        
        self.play(
            Create(loop_back_arrow),
            FadeIn(loop_label),
            run_time=0.6
        )
        
        # 退出分支（右侧）
        no_label = Text("否", font="PingFang SC", font_size=12, color=self.COLOR_SECONDARY)
        no_label.move_to(decision_pos + RIGHT * 0.8 + DOWN * 0.2)
        
        output_pos = np.array([center_x, -0.5, 0])
        output_shape = self.create_io_shape(output_pos, width=1.5, height=0.5)
        output_text = Text("输出 sum", font="PingFang SC", font_size=11, color=WHITE)
        output_text.move_to(output_pos)
        
        end_pos = np.array([center_x, -1.7, 0])
        end_shape = self.create_start_end_shape(end_pos, width=1.3, height=0.5)
        end_text = Text("结束", font="PingFang SC", font_size=12, color=WHITE)
        end_text.move_to(end_pos)
        
        arrow_exit = Arrow(decision_pos + DOWN * 0.7, output_pos + UP * 0.25, buff=0, stroke_width=2, color=WHITE)
        arrow_to_end = Arrow(output_pos + DOWN * 0.25, end_pos + UP * 0.25, buff=0, stroke_width=2, color=WHITE)
        
        self.play(
            FadeIn(no_label),
            Create(arrow_exit),
            run_time=0.4
        )
        self.play(
            FadeIn(VGroup(output_shape, output_text)),
            Create(arrow_to_end),
            FadeIn(VGroup(end_shape, end_text)),
            run_time=0.4
        )
        
        # 说明
        explanation = Text(
            "重复执行直到条件不满足",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 循环动画演示（闪烁循环部分）
        loop_highlight = VGroup(
            process1_shape, process1_text,
            process2_shape, process2_text,
            loop_back_arrow
        )
        
        self.play(Indicate(loop_highlight, scale_factor=1.05), run_time=1.0)
        self.play(Indicate(loop_highlight, scale_factor=1.05), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        all_elements = VGroup(
            title,
            start_shape, start_text,
            arrow1, init_shape, init_text,
            arrow2, decision_shape, decision_text,
            yes_label, arrow_to_loop,
            process1_shape, process1_text,
            arrow_loop_internal,
            process2_shape, process2_text,
            loop_back_arrow, loop_label,
            no_label, arrow_exit,
            output_shape, output_text,
            arrow_to_end, end_shape, end_text,
            explanation
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def show_summary(self):
        """场景9: 总结"""
        # 标题
        title = Text(
            "程序框图的三种基本结构",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 三种结构
        structures = VGroup(
            Text("① 顺序结构 - 依次执行", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_SEQUENCE),
            Text("② 条件结构 - 选择分支", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_CONDITION),
            Text("③ 循环结构 - 重复执行", font="PingFang SC", font_size=self.FONT_BODY, color=self.COLOR_LOOP)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(UP * 2)
        
        self.play(FadeIn(structures, lag_ratio=0.3), run_time=1.5)
        
        # 底部提示
        bottom_note = Text(
            "掌握这三种结构是算法的基础",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(bottom_note), run_time=0.5)
        
        # 整体闪烁
        self.play(Indicate(structures, scale_factor=1.05), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(structures),
            FadeOut(bottom_note),
            run_time=0.5
        )
    
    def show_outro(self):
        """场景10: 片尾关注"""
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
        
        # 流程图符号装饰（旋转）
        deco1 = self.create_start_end_shape(follow_text.get_center() + UP * 2 + LEFT * 2, width=0.8, height=0.4)
        deco2 = self.create_process_shape(follow_text.get_center() + UP * 2 + RIGHT * 2, width=0.8, height=0.4)
        deco3 = self.create_decision_shape(follow_text.get_center() + DOWN * 2 + LEFT * 2, width=0.5, height=0.3)
        deco4 = self.create_io_shape(follow_text.get_center() + DOWN * 2 + RIGHT * 2, width=0.8, height=0.4)
        
        decorations = VGroup(deco1, deco2, deco3, deco4)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.8
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql flowchart_basics.py FlowchartBasics  # 快速预览
# manim -qh flowchart_basics.py FlowchartBasics   # 高质量渲染
# manim -qk flowchart_basics.py FlowchartBasics   # 4K质量