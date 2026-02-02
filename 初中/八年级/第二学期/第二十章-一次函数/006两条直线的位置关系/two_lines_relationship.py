"""
两条直线的位置关系 - Two Lines Positional Relationship
使用 Manim 创建的中学数学教学视频

内容: 一次函数直线的平行、重合、相交三种位置关系
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


class TwoLinesRelationship(Scene):
    """
    两条直线位置关系教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 建立坐标系 - 展示一次函数
    3. 情况1: 平行 (k相同, b不同)
    4. 情况2: 重合 (k、b都相同)
    5. 情况3: 相交 (k不同)
    6. 总结归纳 - 三种情况对比
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_LINE1 = "#e74c3c"       # 红色 - 第一条直线
        self.COLOR_LINE2 = "#3498db"       # 蓝色 - 第二条直线
        self.COLOR_PARALLEL = "#2ecc71"    # 绿色 - 平行线
        self.COLOR_INTERSECT = "#f39c12"   # 橙色 - 交点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA = WHITE
        
        # 初始化数学参数
        self.setup_math_parameters()
        
        # 执行动画序列
        self.show_opening()
        self.show_coordinate_system()
        self.show_parallel_case()
        self.show_coincide_case()
        self.show_intersect_case()
        self.show_summary()
        self.show_outro()
    
    def setup_math_parameters(self):
        """初始化所有数学参数"""
        # 基准直线：y = 0.5x + 1
        self.k1 = 0.5
        self.b1 = 1.0
        
        # 平行直线：y = 0.5x - 1
        self.k2_parallel = 0.5
        self.b2_parallel = -1.0
        
        # 相交直线：y = -0.8x + 0.5
        self.k2_intersect = -0.8
        self.b2_intersect = 0.5
        
        # 精确计算交点
        self.intersection_x = (self.b2_intersect - self.b1) / (self.k1 - self.k2_intersect)
        self.intersection_y = self.k1 * self.intersection_x + self.b1
        self.intersection_point = np.array([self.intersection_x, self.intersection_y, 0])
        
        # 验证交点
        self.verify_intersection()
        
        print("✓ 数学参数初始化完成")
    
    def verify_intersection(self):
        """验证交点计算的正确性"""
        # 代入第一条直线方程
        y1_check = self.k1 * self.intersection_x + self.b1
        # 代入第二条直线方程
        y2_check = self.k2_intersect * self.intersection_x + self.b2_intersect
        
        epsilon = 1e-10
        if abs(y1_check - self.intersection_y) > epsilon:
            print(f"WARNING: 交点计算错误! y1={y1_check}, y={self.intersection_y}")
        if abs(y2_check - self.intersection_y) > epsilon:
            print(f"WARNING: 交点计算错误! y2={y2_check}, y={self.intersection_y}")
        if abs(y1_check - y2_check) > epsilon:
            print(f"WARNING: 两直线在交点处的y值不一致! y1={y1_check}, y2={y2_check}")
        
        print(f"✓ 交点验证通过: P({self.intersection_x:.3f}, {self.intersection_y:.3f})")
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部，持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 - 主标题
        hook_title = Text(
            "两条直线有几种关系?",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        # 副标题
        hook_subtitle = Text(
            "3种！一起来看",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_A
        ).move_to(UP * 4.6)
        
        self.play(Write(hook_title), run_time=0.8)
        self.play(FadeIn(hook_subtitle, shift=UP * 0.2), run_time=0.4)
        
        # 快速展示两条直线 (示意性，无坐标系)
        demo_line1 = Line(
            LEFT * 2 + UP * 0.5,
            RIGHT * 2 + DOWN * 0.5,
            color=self.COLOR_LINE1,
            stroke_width=6
        )
        demo_line2 = Line(
            LEFT * 2 + UP * 1.5,
            RIGHT * 2 + DOWN * 1.5,
            color=self.COLOR_LINE2,
            stroke_width=6
        )
        
        demo_group = VGroup(demo_line1, demo_line2).move_to(UP * 1)
        
        self.play(
            Create(demo_line1),
            Create(demo_line2),
            run_time=0.6
        )
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.3)
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_title),
            FadeOut(hook_subtitle),
            FadeOut(demo_group),
            FadeOut(question_mark),
            run_time=0.4
        )
    
    def show_coordinate_system(self):
        """场景2: 建立坐标系 (5-10秒)"""
        # 创建坐标轴 (适配竖屏)
        self.axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=7,
            axis_config={
                "color": GRAY_B,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18,
            },
            tips=False
        ).move_to(UP * 1.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=24, color=GRAY_A).next_to(self.axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=24, color=GRAY_A).next_to(self.axes.y_axis, UP, buff=0.2)
        
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.3)
        
        # 绘制第一条直线 y = 0.5x + 1
        self.line1_graph = self.axes.plot(
            lambda x: self.k1 * x + self.b1,
            x_range=[-3, 3],
            color=self.COLOR_LINE1,
            stroke_width=5
        )
        
        self.play(Create(self.line1_graph), run_time=1.2)
        
        # 显示公式
        self.formula1 = MathTex(
            r"y = 0.5x + 1",
            font_size=28,
            color=self.COLOR_LINE1
        ).move_to(UP * 5.5 + RIGHT * 1.5)
        
        formula1_box = SurroundingRectangle(
            self.formula1,
            color=self.COLOR_LINE1,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Write(self.formula1), run_time=0.8)
        self.play(Create(formula1_box), run_time=0.3)
        
        # 说明文字
        intro_text = Text(
            "一次函数的图像是一条直线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(intro_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理说明文字
        self.play(FadeOut(intro_text), FadeOut(x_label), FadeOut(y_label), FadeOut(formula1_box), run_time=0.3)
        
        # 将公式移到更上方
        self.play(self.formula1.animate.move_to(UP * 6.5 + LEFT * 2), run_time=0.4)
    
    def show_parallel_case(self):
        """场景3: 平行情况 (10-25秒)"""
        # 标题
        title = Text(
            "情况1: 平行",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PARALLEL,
            weight=BOLD
        ).move_to(UP * 6.5 + RIGHT * 1.8)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 条件公式
        condition = VGroup(
            MathTex(r"k_1 = k_2", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex(r"b_1 \neq b_2", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 5.8)
        
        self.play(Write(condition), run_time=1.0)
        
        # 绘制第二条平行直线 y = 0.5x - 1
        line2_parallel_graph = self.axes.plot(
            lambda x: self.k2_parallel * x + self.b2_parallel,
            x_range=[-3, 3],
            color=self.COLOR_PARALLEL,
            stroke_width=5
        )
        
        formula2_parallel = MathTex(
            r"y = 0.5x - 1",
            font_size=28,
            color=self.COLOR_PARALLEL
        ).move_to(UP * 6.5 + RIGHT * 2)
        
        self.play(Create(line2_parallel_graph), run_time=1.5)
        self.play(Write(formula2_parallel), run_time=0.6)
        
        # 高亮斜率相同
        k_highlight_box = SurroundingRectangle(
            VGroup(self.formula1[0][4:7], formula2_parallel[0][4:7]),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(Create(k_highlight_box), run_time=0.5)
        self.play(Indicate(k_highlight_box, scale_factor=1.2), run_time=0.8)
        self.play(FadeOut(k_highlight_box), run_time=0.3)
        
        # 平行符号 ∥
        parallel_symbol = MathTex(
            r"\parallel",
            font_size=40,
            color=self.COLOR_PARALLEL
        ).move_to(self.axes.c2p(2.2, 0))
        
        self.play(FadeIn(parallel_symbol, scale=1.5), run_time=0.6)
        self.play(Flash(parallel_symbol, color=self.COLOR_PARALLEL, flash_radius=0.4), run_time=0.4)
        
        # 说明文字
        explanation = VGroup(
            Text("斜率相同，截距不同", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("两直线永不相交", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_PARALLEL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition),
            FadeOut(line2_parallel_graph),
            FadeOut(formula2_parallel),
            FadeOut(parallel_symbol),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_coincide_case(self):
        """场景4: 重合情况 (25-38秒)"""
        # 标题
        title = Text(
            "情况2: 重合",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_LINE1,
            weight=BOLD
        ).move_to(UP * 6.5 + RIGHT * 1.8)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 条件公式
        condition = VGroup(
            MathTex(r"k_1 = k_2", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex(r"b_1 = b_2", font_size=24, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.5).move_to(UP * 5.8)
        
        self.play(Write(condition), run_time=1.0)
        
        # 绘制第二条直线 (临时用蓝色)
        line2_temp = self.axes.plot(
            lambda x: self.k1 * x + self.b1,  # 完全相同
            x_range=[-3, 3],
            color=self.COLOR_LINE2,
            stroke_width=5
        )
        
        formula2_temp = MathTex(
            r"y = 0.5x + 1",
            font_size=28,
            color=self.COLOR_LINE2
        ).move_to(UP * 6.5 + RIGHT * 2)
        
        self.play(Create(line2_temp), run_time=1.5)
        self.play(Write(formula2_temp), run_time=0.6)
        
        # 高亮 k 和 b 都相同
        kb_boxes = VGroup(
            SurroundingRectangle(self.formula1[0][4:7], color=self.COLOR_HIGHLIGHT, buff=0.08),
            SurroundingRectangle(self.formula1[0][8:], color=self.COLOR_HIGHLIGHT, buff=0.08)
        )
        
        self.play(Create(kb_boxes), run_time=0.5)
        self.play(Indicate(kb_boxes, scale_factor=1.15), run_time=0.8)
        self.play(FadeOut(kb_boxes), run_time=0.3)
        
        # 第二条线变色融合
        self.play(
            line2_temp.animate.set_color(self.COLOR_LINE1),
            formula2_temp.animate.set_color(self.COLOR_LINE1),
            run_time=1.0
        )
        
        # 闪烁效果
        self.play(
            Flash(self.line1_graph, color=self.COLOR_LINE1, flash_radius=0.5),
            run_time=0.4
        )
        
        # 重合符号 ≡
        coincide_symbol = MathTex(
            r"\equiv",
            font_size=40,
            color=self.COLOR_LINE1
        ).move_to(self.axes.c2p(2.2, 1))
        
        self.play(FadeIn(coincide_symbol, scale=1.5), run_time=0.6)
        
        # 说明文字
        explanation = VGroup(
            Text("斜率、截距都相同", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("实际上是同一条直线", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_LINE1)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 5.2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition),
            FadeOut(line2_temp),
            FadeOut(formula2_temp),
            FadeOut(coincide_symbol),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_intersect_case(self):
        """场景5: 相交情况 (38-55秒)"""
        # 标题
        title = Text(
            "情况3: 相交",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_INTERSECT,
            weight=BOLD
        ).move_to(UP * 6.5 + RIGHT * 1.8)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 条件公式
        condition = MathTex(
            r"k_1 \neq k_2",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.8)
        
        self.play(Write(condition), run_time=1.0)
        
        # 绘制第二条相交直线 y = -0.8x + 0.5
        self.line2_intersect_graph = self.axes.plot(
            lambda x: self.k2_intersect * x + self.b2_intersect,
            x_range=[-3, 3],
            color=self.COLOR_LINE2,
            stroke_width=5
        )
        
        formula2_intersect = MathTex(
            r"y = -0.8x + 0.5",
            font_size=28,
            color=self.COLOR_LINE2
        ).move_to(UP * 6.5 + RIGHT * 2)
        
        self.play(Create(self.line2_intersect_graph), run_time=1.5)
        self.play(Write(formula2_intersect), run_time=0.6)
        
        # 高亮斜率不同
        k_boxes = VGroup(
            SurroundingRectangle(self.formula1[0][4:7], color=self.COLOR_HIGHLIGHT, buff=0.08),
            SurroundingRectangle(formula2_intersect[0][4:8], color=self.COLOR_HIGHLIGHT, buff=0.08)
        )
        
        self.play(Create(k_boxes), run_time=0.5)
        self.play(Indicate(k_boxes, scale_factor=1.15), run_time=0.8)
        self.play(FadeOut(k_boxes), run_time=0.3)
        
        # 交点标记
        intersection_screen = self.axes.c2p(self.intersection_x, self.intersection_y)
        
        intersection_dot = Dot(
            intersection_screen,
            radius=0.15,
            color=self.COLOR_INTERSECT
        )
        
        self.play(Flash(intersection_screen, color=self.COLOR_INTERSECT, flash_radius=0.5), run_time=0.5)
        self.play(FadeIn(intersection_dot, scale=0.5), run_time=0.6)
        
        # 交点标签
        intersection_label = MathTex(
            "P",
            font_size=28,
            color=self.COLOR_INTERSECT
        ).next_to(intersection_dot, UR, buff=0.15)
        
        self.play(Write(intersection_label), run_time=0.4)
        
        # 求解过程 (分步展示)
        solution_steps = VGroup(
            Text("求交点坐标:", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            MathTex(r"0.5x + 1 = -0.8x + 0.5", font_size=18, color=GRAY_A),
            MathTex(r"1.3x = -0.5", font_size=18, color=GRAY_A),
            MathTex(r"x \approx -0.38", font_size=18, color=self.COLOR_HIGHLIGHT),
            MathTex(r"y \approx 0.81", font_size=18, color=self.COLOR_HIGHLIGHT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).scale(0.95).move_to(DOWN * 4.5 + LEFT * 1.5)
        
        for i, step in enumerate(solution_steps):
            self.play(Write(step), run_time=0.4 if i == 0 else 0.5)
            if i == 3 or i == 4:
                self.wait(0.3)
        
        # 坐标标注
        coordinates = MathTex(
            f"({self.intersection_x:.2f}, {self.intersection_y:.2f})",
            font_size=20,
            color=self.COLOR_INTERSECT
        ).next_to(intersection_label, DOWN, buff=0.1)
        
        self.play(Write(coordinates), run_time=0.6)
        self.play(Indicate(coordinates, scale_factor=1.3), run_time=0.8)
        
        # 说明文字
        explanation = VGroup(
            Text("斜率不同，必有交点", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("联立方程可求交点坐标", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 6.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        self.wait(2.5)
        
        # 清理 (保留关键元素)
        self.play(
            FadeOut(title),
            FadeOut(condition),
            FadeOut(solution_steps),
            FadeOut(explanation),
            FadeOut(formula2_intersect),
            run_time=0.6
        )
        
        # 保存交点元素供后续使用
        self.intersection_dot = intersection_dot
        self.intersection_label = intersection_label
        self.coordinates = coordinates
    
    def show_summary(self):
        """场景6: 总结归纳 (55-65秒)"""
        # 清理之前场景的剩余元素
        self.play(
            FadeOut(self.axes),
            FadeOut(self.line1_graph),
            FadeOut(self.line2_intersect_graph),
            FadeOut(self.intersection_dot),
            FadeOut(self.intersection_label),
            FadeOut(self.coordinates),
            FadeOut(self.formula1),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "三种位置关系总结",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 三张卡片
        card1 = self.create_relationship_card(
            "平行 ∥",
            r"k_1 = k_2, \, b_1 \neq b_2",
            "永不相交",
            self.COLOR_PARALLEL,
            UP * 3.5
        )
        
        card2 = self.create_relationship_card(
            "重合 ≡",
            r"k_1 = k_2, \, b_1 = b_2",
            "同一条直线",
            self.COLOR_LINE1,
            UP * 1.5
        )
        
        card3 = self.create_relationship_card(
            "相交 ×",
            r"k_1 \neq k_2",
            "有唯一交点",
            self.COLOR_INTERSECT,
            DOWN * 0.5
        )
        
        cards = VGroup(card1, card2, card3)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 判别流程图
        flowchart = self.create_flowchart().move_to(DOWN * 3.5)
        self.play(Create(flowchart), run_time=2.0)
        
        # 记忆口诀
        mnemonic = VGroup(
            Text("斜率相同看截距", font="Noto Sans CJK SC", font_size=22, color=WHITE),
            Text("截距不同就平行", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_PARALLEL),
            Text("全都相同是重合", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_LINE1),
            Text("斜率不同必相交", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_INTERSECT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(DOWN * 6.2)
        
        self.play(Write(mnemonic), run_time=1.5)
        
        # 全部高亮闪烁
        self.play(
            Flash(cards, color=self.COLOR_HIGHLIGHT, flash_radius=0.8),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(flowchart),
            FadeOut(mnemonic),
            run_time=0.6
        )
    
    def create_relationship_card(self, title_text, condition_latex, result_text, color, position):
        """创建位置关系卡片"""
        # 标题
        title = Text(
            title_text,
            font="Noto Sans CJK SC",
            font_size=28,
            color=color,
            weight=BOLD
        )
        
        # 条件
        condition = MathTex(
            condition_latex,
            font_size=20,
            color=WHITE
        )
        
        # 结果
        result = Text(
            result_text,
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card_content = VGroup(title, condition, result).arrange(DOWN, buff=0.2)
        
        # 背景框
        card_bg = RoundedRectangle(
            width=card_content.width + 0.8,
            height=card_content.height + 0.6,
            corner_radius=0.15,
            color=color,
            stroke_width=3,
            fill_opacity=0.1
        )
        
        card = VGroup(card_bg, card_content).move_to(position)
        
        return card
    
    def create_flowchart(self):
        """创建判别流程图"""
        # 主节点
        main_node = Text("比较斜率 k", font="Noto Sans CJK SC", font_size=18, color=WHITE)
        main_box = RoundedRectangle(
            width=main_node.width + 0.4,
            height=main_node.height + 0.3,
            corner_radius=0.1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        )
        main = VGroup(main_box, main_node)
        
        # 左分支 - k相同
        left_node = Text("k₁ = k₂", font="Noto Sans CJK SC", font_size=16, color=self.COLOR_PARALLEL)
        left_box = RoundedRectangle(
            width=left_node.width + 0.3,
            height=left_node.height + 0.2,
            corner_radius=0.08,
            color=self.COLOR_PARALLEL,
            stroke_width=2
        )
        left = VGroup(left_box, left_node).next_to(main, DOWN + LEFT * 1.5, buff=0.5)
        
        # 右分支 - k不同
        right_node = Text("k₁ ≠ k₂", font="Noto Sans CJK SC", font_size=16, color=self.COLOR_INTERSECT)
        right_box = RoundedRectangle(
            width=right_node.width + 0.3,
            height=right_node.height + 0.2,
            corner_radius=0.08,
            color=self.COLOR_INTERSECT,
            stroke_width=2
        )
        right = VGroup(right_box, right_node).next_to(main, DOWN + RIGHT * 1.5, buff=0.5)
        
        # 左分支细分
        parallel_node = Text("b₁ ≠ b₂ → 平行", font="Noto Sans CJK SC", font_size=14, color=self.COLOR_PARALLEL)
        coincide_node = Text("b₁ = b₂ → 重合", font="Noto Sans CJK SC", font_size=14, color=self.COLOR_LINE1)
        
        left_detail = VGroup(parallel_node, coincide_node).arrange(DOWN, buff=0.15).next_to(left, DOWN, buff=0.3)
        
        # 右分支结果
        intersect_node = Text("→ 相交", font="Noto Sans CJK SC", font_size=14, color=self.COLOR_INTERSECT)
        intersect_node.next_to(right, DOWN, buff=0.3)
        
        # 连线
        line1 = Line(main.get_bottom(), left.get_top(), color=GRAY_B, stroke_width=1.5)
        line2 = Line(main.get_bottom(), right.get_top(), color=GRAY_B, stroke_width=1.5)
        line3 = Line(left.get_bottom(), left_detail.get_top(), color=GRAY_B, stroke_width=1.5)
        line4 = Line(right.get_bottom(), intersect_node.get_top(), color=GRAY_B, stroke_width=1.5)
        
        flowchart = VGroup(
            main, left, right,
            left_detail, intersect_node,
            line1, line2, line3, line4
        )
        
        return flowchart
    
    def show_outro(self):
        """场景7: 片尾关注 (65-75秒)"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰符号 (三种关系的符号)
        symbols = VGroup(
            MathTex(r"\parallel", font_size=36, color=self.COLOR_PARALLEL),
            MathTex(r"\equiv", font_size=36, color=self.COLOR_LINE1),
            MathTex(r"\times", font_size=36, color=self.COLOR_INTERSECT)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2)
        
        self.play(*[FadeIn(sym, scale=0.5) for sym in symbols], run_time=0.6)
        
        # 符号旋转动画
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        # 函数图标装饰
        mini_graph = VGroup(
            Line(LEFT * 0.5, RIGHT * 0.5 + UP * 0.5, color=self.COLOR_LINE1, stroke_width=3),
            Line(LEFT * 0.5, RIGHT * 0.5 + DOWN * 0.5, color=self.COLOR_LINE2, stroke_width=3)
        ).scale(0.8).move_to(DOWN * 4)
        
        self.play(Create(mini_graph), run_time=1.0)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            FadeOut(mini_graph),
            run_time=1.0
        )


# 运行命令:
# manim -pql two_lines_relationship.py TwoLinesRelationship  # 快速预览
# manim -qh two_lines_relationship.py TwoLinesRelationship   # 高质量 1080p
# manim -qk two_lines_relationship.py TwoLinesRelationship   # 4K质量