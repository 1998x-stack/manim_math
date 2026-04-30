"""
分类计数原理与分步计数原理 - Classification and Step Counting Principles
使用 Manim 创建的高中数学教学视频

内容: 加法原理（分类计数）vs 乘法原理（分步计数）
目标观众: 高三学生
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


class CountingPrinciples(Scene):
    """
    分类计数原理与分步计数原理教学动画
    
    场景顺序:
    1. 开场钩子 - 生活实例引入
    2. 分类计数原理介绍（加法原理）
    3. 分类计数实例
    4. 分步计数原理介绍（乘法原理）
    5. 分步计数实例（回到开场问题）
    6. 对比总结
    7. 记忆口诀 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CLASSIFICATION = "#3498db"  # 蓝色 - 分类计数
        self.COLOR_STEP = "#e74c3c"           # 红色 - 分步计数
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_SUCCESS = "#2ecc71"
        
        # 字体配置
        self.FONT = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_classification_intro()
        self.show_classification_example()
        self.show_step_intro()
        self.show_step_example()
        self.show_comparison()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 - 用生活实例吸引注意"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=20,
            color=GRAY_B
        ).to_edge(UP, buff=0.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_title = Text(
            "思考题",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        hook_q1 = Text(
            "从A地到B地，有3条路",
            font=self.FONT,
            font_size=28,
            color=WHITE
        ).move_to(UP * 5)
        
        hook_q2 = Text(
            "从B地到C地，有2条路",
            font=self.FONT,
            font_size=28,
            color=WHITE
        ).move_to(UP * 4.2)
        
        hook_q3 = Text(
            "问：从A到C有几种走法？",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 3)
        
        self.play(Write(hook_title), run_time=0.5)
        self.play(Write(hook_q1), run_time=0.6)
        self.play(Write(hook_q2), run_time=0.6)
        self.play(Write(hook_q3), run_time=0.7)
        
        # 简单路径示意图
        # A点
        point_A = Dot(LEFT * 3 + UP * 0.5, radius=0.15, color=self.COLOR_SUCCESS)
        label_A = Text("A", font=self.FONT, font_size=28, color=WHITE).next_to(point_A, LEFT, buff=0.2)
        
        # B点
        point_B = Dot(ORIGIN + UP * 0.5, radius=0.15, color=BLUE)
        label_B = Text("B", font=self.FONT, font_size=28, color=WHITE).next_to(point_B, UP, buff=0.2)
        
        # C点
        point_C = Dot(RIGHT * 3 + UP * 0.5, radius=0.15, color=RED)
        label_C = Text("C", font=self.FONT, font_size=28, color=WHITE).next_to(point_C, RIGHT, buff=0.2)
        
        # A到B的3条路（简化表示）
        path_AB_1 = Arrow(point_A.get_center(), point_B.get_center() + UP * 0.4, 
                          color=self.COLOR_AUXILIARY, buff=0.2, stroke_width=3)
        path_AB_2 = Arrow(point_A.get_center(), point_B.get_center(), 
                          color=self.COLOR_AUXILIARY, buff=0.2, stroke_width=3)
        path_AB_3 = Arrow(point_A.get_center(), point_B.get_center() + DOWN * 0.4, 
                          color=self.COLOR_AUXILIARY, buff=0.2, stroke_width=3)
        
        # B到C的2条路
        path_BC_1 = Arrow(point_B.get_center(), point_C.get_center() + UP * 0.3, 
                          color=self.COLOR_AUXILIARY, buff=0.2, stroke_width=3)
        path_BC_2 = Arrow(point_B.get_center(), point_C.get_center() + DOWN * 0.3, 
                          color=self.COLOR_AUXILIARY, buff=0.2, stroke_width=3)
        
        paths = VGroup(path_AB_1, path_AB_2, path_AB_3, path_BC_1, path_BC_2)
        points = VGroup(point_A, point_B, point_C, label_A, label_B, label_C)
        
        diagram = VGroup(points, paths).move_to(DOWN * 1)
        
        self.play(
            FadeIn(points, scale=0.8),
            *[Create(path) for path in paths],
            run_time=1.2
        )
        
        # 疑问标记
        question = Text("?", font=self.FONT, font_size=60, color=self.COLOR_HIGHLIGHT)
        question.move_to(DOWN * 3.5)
        
        self.play(Write(question, run_time=0.5), Flash(question, color=YELLOW))
        self.wait(1.0)
        
        # 清理（保留作者信息和问题暂存）
        self.hook_group = VGroup(hook_title, hook_q1, hook_q2, hook_q3)
        self.diagram_group = VGroup(diagram, question)
        
        self.play(
            FadeOut(self.hook_group),
            FadeOut(self.diagram_group),
            run_time=0.5
        )
    
    def show_classification_intro(self):
        """场景2: 分类计数原理介绍（加法原理）"""
        # 标题
        title = Text(
            "分类计数原理",
            font=self.FONT,
            font_size=40,
            color=self.COLOR_CLASSIFICATION,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "加法原理",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_AUXILIARY
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 定义
        definition = Text(
            "完成一件事有n类不同方案\n第i类有mᵢ种方法\n则完成这件事共有：",
            font=self.FONT,
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(definition), run_time=1.2)
        
        # 核心公式
        formula = MathTex(
            r"N = m_1 + m_2 + \cdots + m_n",
            font_size=44,
            color=self.COLOR_CLASSIFICATION
        ).move_to(UP * 2.8)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)
        
        # 可视化：3个并列的盒子
        box_width = 1.8
        box_height = 1.2
        
        box1 = Rectangle(width=box_width, height=box_height, 
                        color=self.COLOR_CLASSIFICATION, stroke_width=3)
        box1_label = Text("第1类", font=self.FONT, font_size=22, color=WHITE)
        box1_count = MathTex(r"m_1", font_size=36, color=self.COLOR_CLASSIFICATION)
        box1_content = VGroup(box1_label, box1_count).arrange(DOWN, buff=0.2)
        box1_group = VGroup(box1, box1_content)
        
        box2 = Rectangle(width=box_width, height=box_height, 
                        color=self.COLOR_CLASSIFICATION, stroke_width=3)
        box2_label = Text("第2类", font=self.FONT, font_size=22, color=WHITE)
        box2_count = MathTex(r"m_2", font_size=36, color=self.COLOR_CLASSIFICATION)
        box2_content = VGroup(box2_label, box2_count).arrange(DOWN, buff=0.2)
        box2_group = VGroup(box2, box2_content)
        
        box3 = Rectangle(width=box_width, height=box_height, 
                        color=self.COLOR_CLASSIFICATION, stroke_width=3)
        box3_label = Text("第n类", font=self.FONT, font_size=22, color=WHITE)
        box3_count = MathTex(r"m_n", font_size=36, color=self.COLOR_CLASSIFICATION)
        box3_content = VGroup(box3_label, box3_count).arrange(DOWN, buff=0.2)
        box3_group = VGroup(box3, box3_content)
        
        boxes = VGroup(box1_group, box2_group, box3_group).arrange(RIGHT, buff=0.8).move_to(UP * 0.5)
        
        # 盒子依次出现
        for i, box_group in enumerate([box1_group, box2_group, box3_group]):
            self.play(
                FadeIn(box_group[0], scale=0.8),
                Write(box_group[1]),
                run_time=0.5
            )
            self.wait(0.2)
        
        # 加号
        plus1 = MathTex(r"+", font_size=48, color=YELLOW).move_to((box1_group.get_center() + box2_group.get_center()) / 2)
        plus2 = MathTex(r"\cdots", font_size=48, color=YELLOW).move_to((box2_group.get_center() + box3_group.get_center()) / 2)
        
        self.play(Write(plus1), Write(plus2), run_time=0.6)
        
        # 关键特征
        key_point = Text(
            "关键：任一类都能独立完成任务",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        key_word = Text(
            "（并列关系）",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).next_to(key_point, DOWN, buff=0.2)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(key_word), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(key_point),
            FadeOut(key_word),
            run_time=0.5
        )
        
        # 缩小并移到上方
        small_group = VGroup(title, subtitle, formula, boxes, plus1, plus2)
        self.play(
            small_group.animate.scale(0.5).to_edge(UP, buff=1.5),
            run_time=0.6
        )
        
        self.classification_ref = small_group
    
    def show_classification_example(self):
        """场景3: 分类计数实例"""
        # 问题
        problem = Text(
            "例题",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        problem_text = Text(
            "从北京到上海：\n坐飞机4种航班\n坐火车3种车次\n坐汽车2种路线\n问：共有多少种方式？",
            font=self.FONT,
            font_size=24,
            color=WHITE,
            line_spacing=1.3
        ).move_to(UP * 3.5)
        
        self.play(Write(problem), run_time=0.5)
        self.play(Write(problem_text), run_time=1.5)
        self.wait(0.5)
        
        # 三个类别框
        box_width = 2.2
        box_height = 1.0
        
        # 飞机
        plane_box = RoundedRectangle(width=box_width, height=box_height, 
                                     corner_radius=0.1, color=self.COLOR_CLASSIFICATION, stroke_width=3)
        plane_icon = Text("✈️", font_size=32)
        plane_text = Text("飞机", font=self.FONT, font_size=22, color=WHITE)
        plane_count = Text("4种", font=self.FONT, font_size=28, color=self.COLOR_CLASSIFICATION, weight=BOLD)
        plane_content = VGroup(plane_icon, plane_text, plane_count).arrange(DOWN, buff=0.1)
        plane_group = VGroup(plane_box, plane_content)
        
        # 火车
        train_box = RoundedRectangle(width=box_width, height=box_height, 
                                     corner_radius=0.1, color=self.COLOR_CLASSIFICATION, stroke_width=3)
        train_icon = Text("🚄", font_size=32)
        train_text = Text("火车", font=self.FONT, font_size=22, color=WHITE)
        train_count = Text("3种", font=self.FONT, font_size=28, color=self.COLOR_CLASSIFICATION, weight=BOLD)
        train_content = VGroup(train_icon, train_text, train_count).arrange(DOWN, buff=0.1)
        train_group = VGroup(train_box, train_content)
        
        # 汽车
        car_box = RoundedRectangle(width=box_width, height=box_height, 
                                   corner_radius=0.1, color=self.COLOR_CLASSIFICATION, stroke_width=3)
        car_icon = Text("🚌", font_size=32)
        car_text = Text("汽车", font=self.FONT, font_size=22, color=WHITE)
        car_count = Text("2种", font=self.FONT, font_size=28, color=self.COLOR_CLASSIFICATION, weight=BOLD)
        car_content = VGroup(car_icon, car_text, car_count).arrange(DOWN, buff=0.1)
        car_group = VGroup(car_box, car_content)
        
        categories = VGroup(plane_group, train_group, car_group).arrange(RIGHT, buff=0.6).move_to(UP * 1)
        
        # 依次出现
        for cat in categories:
            self.play(FadeIn(cat, scale=0.8), run_time=0.5)
        
        # 加号
        plus1 = MathTex(r"+", font_size=40, color=YELLOW).move_to((plane_group.get_center() + train_group.get_center()) / 2 + DOWN * 0.05)
        plus2 = MathTex(r"+", font_size=40, color=YELLOW).move_to((train_group.get_center() + car_group.get_center()) / 2 + DOWN * 0.05)
        
        self.play(Write(plus1), Write(plus2), run_time=0.5)
        
        # 计算过程
        calc_step1 = MathTex(r"4", r"+", r"3", r"+", r"2", font_size=40, color=WHITE).move_to(DOWN * 1)
        calc_step1[0].set_color(self.COLOR_CLASSIFICATION)
        calc_step1[2].set_color(self.COLOR_CLASSIFICATION)
        calc_step1[4].set_color(self.COLOR_CLASSIFICATION)
        
        self.play(Write(calc_step1), run_time=0.8)
        
        # 等号和答案
        equals = MathTex(r"=", font_size=40, color=WHITE).next_to(calc_step1, RIGHT, buff=0.3)
        answer = MathTex(r"9", font_size=48, color=self.COLOR_SUCCESS).next_to(equals, RIGHT, buff=0.3)
        
        self.play(Write(equals), run_time=0.3)
        self.play(Write(answer), Flash(answer, color=YELLOW), run_time=0.6)
        
        # 答案文字
        answer_text = Text(
            "共9种方式",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_SUCCESS
        ).next_to(answer, DOWN, buff=0.4)
        
        self.play(FadeIn(answer_text), run_time=0.5)
        
        # 关键提示
        hint = Text(
            "任选其一即可完成旅程",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(problem),
            FadeOut(problem_text),
            FadeOut(categories),
            FadeOut(plus1),
            FadeOut(plus2),
            FadeOut(calc_step1),
            FadeOut(equals),
            FadeOut(answer),
            FadeOut(answer_text),
            FadeOut(hint),
            FadeOut(self.classification_ref),
            run_time=0.6
        )
    
    def show_step_intro(self):
        """场景4: 分步计数原理介绍（乘法原理）"""
        # 标题
        title = Text(
            "分步计数原理",
            font=self.FONT,
            font_size=40,
            color=self.COLOR_STEP,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "乘法原理",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_AUXILIARY
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 定义
        definition = Text(
            "完成一件事需要n个步骤\n第i步有mᵢ种方法\n则完成这件事共有：",
            font=self.FONT,
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(definition), run_time=1.2)
        
        # 核心公式
        formula = MathTex(
            r"N = m_1 \times m_2 \times \cdots \times m_n",
            font_size=40,
            color=self.COLOR_STEP
        ).move_to(UP * 2.8)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)
        
        # 可视化：步骤链（箭头连接）
        step_width = 1.5
        step_height = 1.0
        
        step1 = RoundedRectangle(width=step_width, height=step_height, 
                                corner_radius=0.1, color=self.COLOR_STEP, stroke_width=3)
        step1_label = Text("第1步", font=self.FONT, font_size=20, color=WHITE)
        step1_count = MathTex(r"m_1", font_size=32, color=self.COLOR_STEP)
        step1_content = VGroup(step1_label, step1_count).arrange(DOWN, buff=0.15)
        step1_group = VGroup(step1, step1_content)
        
        arrow1 = Arrow(ORIGIN, RIGHT * 0.8, color=YELLOW, stroke_width=6, buff=0)
        
        step2 = RoundedRectangle(width=step_width, height=step_height, 
                                corner_radius=0.1, color=self.COLOR_STEP, stroke_width=3)
        step2_label = Text("第2步", font=self.FONT, font_size=20, color=WHITE)
        step2_count = MathTex(r"m_2", font_size=32, color=self.COLOR_STEP)
        step2_content = VGroup(step2_label, step2_count).arrange(DOWN, buff=0.15)
        step2_group = VGroup(step2, step2_content)
        
        arrow2 = Arrow(ORIGIN, RIGHT * 0.8, color=YELLOW, stroke_width=6, buff=0)
        dots = MathTex(r"\cdots", font_size=40, color=YELLOW)
        arrow3 = Arrow(ORIGIN, RIGHT * 0.8, color=YELLOW, stroke_width=6, buff=0)
        
        step3 = RoundedRectangle(width=step_width, height=step_height, 
                                corner_radius=0.1, color=self.COLOR_STEP, stroke_width=3)
        step3_label = Text("第n步", font=self.FONT, font_size=20, color=WHITE)
        step3_count = MathTex(r"m_n", font_size=32, color=self.COLOR_STEP)
        step3_content = VGroup(step3_label, step3_count).arrange(DOWN, buff=0.15)
        step3_group = VGroup(step3, step3_content)
        
        chain = VGroup(step1_group, arrow1, step2_group, arrow2, dots, arrow3, step3_group)
        chain.arrange(RIGHT, buff=0.25).move_to(UP * 0.5)
        
        # 步骤依次出现
        self.play(FadeIn(step1_group, scale=0.8), run_time=0.5)
        self.play(GrowArrow(arrow1), run_time=0.4)
        self.play(FadeIn(step2_group, scale=0.8), run_time=0.5)
        self.play(GrowArrow(arrow2), run_time=0.4)
        self.play(Write(dots), run_time=0.3)
        self.play(GrowArrow(arrow3), run_time=0.4)
        self.play(FadeIn(step3_group, scale=0.8), run_time=0.5)
        
        # 乘号
        times1 = MathTex(r"\times", font_size=36, color=YELLOW).next_to(arrow1, DOWN, buff=0.3)
        times2 = MathTex(r"\times", font_size=36, color=YELLOW).next_to(arrow2, DOWN, buff=0.3)
        times3 = MathTex(r"\times", font_size=36, color=YELLOW).next_to(arrow3, DOWN, buff=0.3)
        
        self.play(Write(times1), Write(times2), Write(times3), run_time=0.6)
        
        # 关键特征
        key_point = Text(
            "关键：每步都要完成",
            font=self.FONT,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.8)
        
        key_word = Text(
            "（递进关系）",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).next_to(key_point, DOWN, buff=0.2)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(key_word), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(key_point),
            FadeOut(key_word),
            run_time=0.5
        )
        
        # 缩小并移到上方
        small_group = VGroup(title, subtitle, formula, chain, times1, times2, times3)
        self.play(
            small_group.animate.scale(0.5).to_edge(UP, buff=1.5),
            run_time=0.6
        )
        
        self.step_ref = small_group
    
    def show_step_example(self):
        """场景5: 分步计数实例（回到开场问题）"""
        # 回顾问题
        problem = Text(
            "回到开场问题",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        problem_text = Text(
            "从A地经B地到C地：\nA→B有3条路\nB→C有2条路\n问：A→C共有多少种走法？",
            font=self.FONT,
            font_size=24,
            color=WHITE,
            line_spacing=1.3
        ).move_to(UP * 3.8)
        
        self.play(Write(problem), run_time=0.5)
        self.play(Write(problem_text), run_time=1.2)
        self.wait(0.5)
        
        # 分步分析
        step_label_1 = Text(
            "第1步：A→B",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_STEP
        ).move_to(UP * 2)
        
        step_count_1 = Text(
            "3种选择",
            font=self.FONT,
            font_size=28,
            color=YELLOW,
            weight=BOLD
        ).next_to(step_label_1, RIGHT, buff=0.5)
        
        self.play(Write(step_label_1), run_time=0.5)
        self.play(FadeIn(step_count_1, scale=1.2), run_time=0.4)
        
        # 第1步可视化
        point_A = Dot(LEFT * 2.5, radius=0.12, color=self.COLOR_SUCCESS)
        label_A = Text("A", font=self.FONT, font_size=24, color=WHITE).next_to(point_A, LEFT, buff=0.15)
        
        point_B = Dot(RIGHT * 0.5, radius=0.12, color=BLUE)
        label_B = Text("B", font=self.FONT, font_size=24, color=WHITE).next_to(point_B, UP, buff=0.15)
        
        paths_AB = VGroup(
            Arrow(point_A.get_center(), point_B.get_center() + UP * 0.3, color=self.COLOR_AUXILIARY, buff=0.15, stroke_width=4),
            Arrow(point_A.get_center(), point_B.get_center(), color=self.COLOR_AUXILIARY, buff=0.15, stroke_width=4),
            Arrow(point_A.get_center(), point_B.get_center() + DOWN * 0.3, color=self.COLOR_AUXILIARY, buff=0.15, stroke_width=4)
        )
        
        step1_diagram = VGroup(point_A, label_A, point_B, label_B, paths_AB).move_to(UP * 0.5)
        
        self.play(FadeIn(step1_diagram), run_time=0.8)
        self.wait(0.3)
        
        # 第2步
        step_label_2 = Text(
            "第2步：B→C",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_STEP
        ).move_to(DOWN * 0.8)
        
        step_count_2 = Text(
            "2种选择",
            font=self.FONT,
            font_size=28,
            color=YELLOW,
            weight=BOLD
        ).next_to(step_label_2, RIGHT, buff=0.5)
        
        self.play(Write(step_label_2), run_time=0.5)
        self.play(FadeIn(step_count_2, scale=1.2), run_time=0.4)
        
        # 第2步可视化（添加C点和BC路径）
        point_C = Dot(RIGHT * 3.5 + DOWN * 1.5, radius=0.12, color=RED)
        label_C = Text("C", font=self.FONT, font_size=24, color=WHITE).next_to(point_C, RIGHT, buff=0.15)
        
        # 将B点位置用于第2步展示
        point_B_for_step2 = Dot(LEFT * 1.5 + DOWN * 1.5, radius=0.12, color=BLUE)
        label_B_2 = Text("B", font=self.FONT, font_size=24, color=WHITE).next_to(point_B_for_step2, LEFT, buff=0.15)
        
        paths_BC = VGroup(
            Arrow(point_B_for_step2.get_center(), point_C.get_center() + UP * 0.2, color=self.COLOR_AUXILIARY, buff=0.15, stroke_width=4),
            Arrow(point_B_for_step2.get_center(), point_C.get_center() + DOWN * 0.2, color=self.COLOR_AUXILIARY, buff=0.15, stroke_width=4)
        )
        
        step2_diagram = VGroup(point_B_for_step2, label_B_2, point_C, label_C, paths_BC)
        
        self.play(FadeIn(step2_diagram), run_time=0.8)
        self.wait(0.5)
        
        # 树状展开说明
        tree_hint = Text(
            "每条第1步路径后，都有2种第2步选择",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(tree_hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        # 计算
        calc = MathTex(
            r"3", r"\times", r"2", r"=", r"6",
            font_size=44
        ).move_to(DOWN * 4.2)
        calc[0].set_color(YELLOW)
        calc[2].set_color(YELLOW)
        calc[4].set_color(self.COLOR_SUCCESS)
        
        self.play(Write(calc), run_time=0.8)
        self.play(Flash(calc[4], color=YELLOW), run_time=0.5)
        
        # 答案
        answer_text = Text(
            "共6种走法",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(answer_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(problem),
            FadeOut(problem_text),
            FadeOut(step_label_1),
            FadeOut(step_count_1),
            FadeOut(step1_diagram),
            FadeOut(step_label_2),
            FadeOut(step_count_2),
            FadeOut(step2_diagram),
            FadeOut(tree_hint),
            FadeOut(calc),
            FadeOut(answer_text),
            FadeOut(self.step_ref),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 对比总结"""
        # 标题
        title = Text(
            "两种原理对比",
            font=self.FONT,
            font_size=40,
            color=YELLOW,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 对比表格
        table_y_start = 4.5
        row_height = 1.2
        
        # 表头
        header_classification = Text(
            "分类计数原理",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_CLASSIFICATION,
            weight=BOLD
        ).move_to(LEFT * 2.2 + UP * table_y_start)
        
        header_step = Text(
            "分步计数原理",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_STEP,
            weight=BOLD
        ).move_to(RIGHT * 2.2 + UP * table_y_start)
        
        divider = Line(UP * (table_y_start + 0.5), DOWN * 4, color=GRAY_B, stroke_width=2)
        
        self.play(
            Write(header_classification),
            Write(header_step),
            Create(divider),
            run_time=0.8
        )
        
        # 第1行：关系
        row1_y = table_y_start - row_height
        
        relation_left = Text(
            "并列关系",
            font=self.FONT,
            font_size=26,
            color=WHITE
        ).move_to(LEFT * 2.2 + UP * row1_y)
        
        relation_right = Text(
            "递进关系",
            font=self.FONT,
            font_size=26,
            color=WHITE
        ).move_to(RIGHT * 2.2 + UP * row1_y)
        
        self.play(FadeIn(relation_left), FadeIn(relation_right), run_time=0.6)
        
        # 第2行：符号
        row2_y = row1_y - row_height
        
        symbol_left = MathTex(r"+", font_size=60, color=self.COLOR_CLASSIFICATION).move_to(LEFT * 2.2 + UP * row2_y)
        symbol_right = MathTex(r"\times", font_size=60, color=self.COLOR_STEP).move_to(RIGHT * 2.2 + UP * row2_y)
        
        self.play(Write(symbol_left), Write(symbol_right), run_time=0.6)
        
        # 第3行：条件
        row3_y = row2_y - row_height
        
        condition_left = Text(
            "任一类即可\n完成任务",
            font=self.FONT,
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        ).move_to(LEFT * 2.2 + UP * row3_y)
        
        condition_right = Text(
            "每步都要\n完成",
            font=self.FONT,
            font_size=22,
            color=WHITE,
            line_spacing=1.2
        ).move_to(RIGHT * 2.2 + UP * row3_y)
        
        self.play(FadeIn(condition_left), FadeIn(condition_right), run_time=0.6)
        
        # 第4行：公式
        row4_y = row3_y - row_height
        
        formula_left = MathTex(
            r"m_1 + m_2 + \cdots + m_n",
            font_size=24,
            color=self.COLOR_CLASSIFICATION
        ).move_to(LEFT * 2.2 + UP * row4_y)
        
        formula_right = MathTex(
            r"m_1 \times m_2 \times \cdots \times m_n",
            font_size=20,
            color=self.COLOR_STEP
        ).move_to(RIGHT * 2.2 + UP * row4_y)
        
        self.play(Write(formula_left), Write(formula_right), run_time=0.8)
        
        # 关键差异闪烁
        self.play(
            Flash(relation_left, color=YELLOW),
            Flash(relation_right, color=YELLOW),
            run_time=0.6
        )
        self.play(
            Indicate(symbol_left, scale_factor=1.3),
            Indicate(symbol_right, scale_factor=1.3),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(header_classification),
            FadeOut(header_step),
            FadeOut(divider),
            FadeOut(relation_left),
            FadeOut(relation_right),
            FadeOut(symbol_left),
            FadeOut(symbol_right),
            FadeOut(condition_left),
            FadeOut(condition_right),
            FadeOut(formula_left),
            FadeOut(formula_right),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 记忆口诀 + 片尾关注"""
        # 记忆口诀标题
        title = Text(
            "记忆口诀",
            font=self.FONT,
            font_size=40,
            color=YELLOW,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 口诀1
        slogan1 = Text(
            "分类加，分步乘",
            font=self.FONT,
            font_size=48,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 4)
        
        self.play(FadeIn(slogan1, shift=DOWN * 0.3, scale=1.2), run_time=0.8)
        self.wait(0.5)
        
        # 口诀2
        slogan2 = Text(
            "并列加，递进乘",
            font=self.FONT,
            font_size=48,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        self.play(FadeIn(slogan2, shift=DOWN * 0.3, scale=1.2), run_time=0.8)
        self.wait(0.5)
        
        # 口诀3
        slogan3 = Text(
            "独立加，依赖乘",
            font=self.FONT,
            font_size=48,
            color=WHITE,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(slogan3, shift=DOWN * 0.3, scale=1.2), run_time=0.8)
        self.wait(0.8)
        
        # 口诀组合闪烁
        slogans = VGroup(slogan1, slogan2, slogan3)
        self.play(
            Flash(slogans, color=YELLOW, flash_radius=1.5),
            slogans.animate.set_color(YELLOW),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 口诀淡出
        self.play(FadeOut(title), FadeOut(slogans), run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=44,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
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
            "关注我，学更多数学技巧！",
            font=self.FONT,
            font_size=34,
            color=YELLOW
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素：加号和乘号旋转
        plus_icon = MathTex(r"+", font_size=80, color=self.COLOR_CLASSIFICATION).move_to(LEFT * 3 + DOWN * 3)
        times_icon = MathTex(r"\times", font_size=80, color=self.COLOR_STEP).move_to(RIGHT * 3 + DOWN * 3)
        
        self.play(
            FadeIn(plus_icon, scale=0.5),
            FadeIn(times_icon, scale=0.5),
            run_time=0.5
        )
        self.play(
            Rotate(plus_icon, angle=2*PI, run_time=1.5, rate_func=linear),
            Rotate(times_icon, angle=-2*PI, run_time=1.5, rate_func=linear)
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(plus_icon),
            FadeOut(times_icon),
            run_time=1.0
        )


# 运行命令:
# manim -pql counting_principles.py CountingPrinciples  # 快速预览
# manim -qh counting_principles.py CountingPrinciples   # 高质量渲染