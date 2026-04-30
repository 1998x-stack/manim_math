"""
四种命题及其关系动画 - Four Types of Propositions Animation
使用 Manim 创建的高中数学教学视频

内容: 原命题、逆命题、否命题、逆否命题及其等价关系
目标观众: 高一学生
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


class FourPropositions(Scene):
    """
    四种命题教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 什么是命题
    3. 原命题
    4. 逆命题
    5. 否命题
    6. 逆否命题
    7. 关系图
    8. 等价关系强调
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ORIGINAL = "#e74c3c"      # 红色 - 原命题
        self.COLOR_CONVERSE = "#3498db"      # 蓝色 - 逆命题
        self.COLOR_INVERSE = "#2ecc71"       # 绿色 - 否命题
        self.COLOR_CONTRAPOSITIVE = "#f39c12"  # 橙色 - 逆否命题
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_ARROW = "#95a5a6"         # 灰色 - 箭头
        self.COLOR_EQUIV = "#9b59b6"         # 紫色 - 等价关系
        
        # 执行动画序列
        self.show_opening()
        self.show_what_is_proposition()
        self.show_original()
        self.show_converse()
        self.show_inverse()
        self.show_contrapositive()
        self.show_relationship_diagram()
        self.show_equivalence()
        self.show_outro()
    
    def create_proposition_box(self, proposition_text, condition_text, conclusion_text, 
                               box_color, title_text):
        """
        创建命题框
        
        参数:
            proposition_text: 命题符号 (如 "p → q")
            condition_text: 条件文字
            conclusion_text: 结论文字
            box_color: 边框颜色
            title_text: 标题 (如 "原命题")
        """
        # 外框
        box = Rectangle(
            width=3.5,
            height=2.0,
            color=box_color,
            stroke_width=3
        )
        
        # 标题
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=22,
            color=box_color
        ).next_to(box, UP, buff=0.2)
        
        # 命题符号
        prop_symbol = MathTex(
            proposition_text,
            font_size=36,
            color=WHITE
        ).move_to(box.get_center() + UP * 0.5)
        
        # 条件和结论说明
        condition = Text(
            condition_text,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).move_to(box.get_center() + DOWN * 0.3)
        
        conclusion = Text(
            conclusion_text,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).next_to(condition, DOWN, buff=0.1)
        
        # 组合
        group = VGroup(box, title, prop_symbol, condition, conclusion)
        
        return group, box, title, prop_symbol
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子标题
        hook = Text(
            "一个命题的四种形式",
            font="PingFang SC",
            font_size=44,
            color=GOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "它们之间有什么关系?",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 四个小框预览
        preview_boxes = VGroup()
        
        box_titles = ["原命题", "逆命题", "否命题", "逆否命题"]
        box_colors = [
            self.COLOR_ORIGINAL,
            self.COLOR_CONVERSE,
            self.COLOR_INVERSE,
            self.COLOR_CONTRAPOSITIVE
        ]
        
        for i, (title, color) in enumerate(zip(box_titles, box_colors)):
            small_box = Rectangle(
                width=1.5,
                height=1.0,
                color=color,
                stroke_width=2
            )
            small_title = Text(
                title,
                font="PingFang SC",
                font_size=16,
                color=WHITE
            ).move_to(small_box)
            
            small_group = VGroup(small_box, small_title)
            preview_boxes.add(small_group)
        
        preview_boxes.arrange_in_grid(rows=2, cols=2, buff=0.5)
        preview_boxes.move_to(UP * 1)
        
        self.play(
            *[FadeIn(box, scale=0.5) for box in preview_boxes],
            run_time=1.0
        )
        
        # 提示文字
        hint = Text(
            "看似复杂, 其实简单!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            FadeOut(preview_boxes),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_what_is_proposition(self):
        """场景2: 什么是命题"""
        # 标题
        title = Text(
            "什么是命题?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义
        definition = Text(
            "命题是可以判断真假的陈述句",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.8)
        
        # 基本形式
        form_title = Text(
            "基本形式:",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 3 + LEFT * 3)
        
        form = MathTex(
            r"\text{if } p \text{ then } q",
            font_size=36
        ).next_to(form_title, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(form_title),
            Write(form),
            run_time=1.0
        )
        
        # 示例
        example_title = Text(
            "例如:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1 + LEFT * 3.5)
        
        example = Text(
            "若 x > 0, 则 x² > 0",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(example_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        explanation = VGroup(
            Text("p: x > 0 (条件)", font="PingFang SC", font_size=20, color=GRAY_B),
            Text("q: x² > 0 (结论)", font="PingFang SC", font_size=20, color=GRAY_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.next_to(example, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(FadeIn(example_title), run_time=0.4)
        self.play(Write(example), run_time=0.8)
        self.play(FadeIn(explanation), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(form_title),
            FadeOut(form),
            FadeOut(example_title),
            FadeOut(example),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_original(self):
        """场景3: 原命题"""
        # 标题
        title = Text(
            "原命题",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_ORIGINAL
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建原命题框
        original_group, original_box, _, _ = self.create_proposition_box(
            r"p \rightarrow q",
            "条件: p",
            "结论: q",
            self.COLOR_ORIGINAL,
            "原命题"
        )
        original_group.move_to(UP * 2)
        
        self.play(
            Create(original_box),
            FadeIn(original_group[1]),  # title
            Write(original_group[2]),    # symbol
            FadeIn(original_group[3]),   # condition
            FadeIn(original_group[4]),   # conclusion
            run_time=1.5
        )
        
        # 例子
        example_title = Text(
            "例:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1 + LEFT * 3.5)
        
        example = Text(
            "若两直线平行, 则同位角相等",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).next_to(example_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(
            FadeIn(example_title),
            Write(example),
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 清理标题和例子，保留命题框
        self.play(
            FadeOut(title),
            FadeOut(example_title),
            FadeOut(example),
            run_time=0.5
        )
        
        # 保存原命题框供后续使用
        self.original_group = original_group
    
    def show_converse(self):
        """场景4: 逆命题"""
        # 标题
        title = Text(
            "逆命题 - 交换条件和结论",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CONVERSE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 原命题框移到左边
        self.play(
            self.original_group.animate.scale(0.7).move_to(LEFT * 2.5 + UP * 3),
            run_time=0.8
        )
        
        # 创建逆命题框
        converse_group, converse_box, _, _ = self.create_proposition_box(
            r"q \rightarrow p",
            "条件: q",
            "结论: p",
            self.COLOR_CONVERSE,
            "逆命题"
        )
        converse_group.scale(0.7).move_to(RIGHT * 2.5 + UP * 3)
        
        # 箭头指示变换
        arrow = Arrow(
            LEFT * 0.5 + UP * 3,
            RIGHT * 0.5 + UP * 3,
            color=self.COLOR_ARROW,
            stroke_width=4
        )
        arrow_label = Text(
            "交换",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ARROW
        ).next_to(arrow, UP, buff=0.1)
        
        self.play(
            Create(arrow),
            FadeIn(arrow_label),
            run_time=0.6
        )
        
        self.play(
            Create(converse_box),
            FadeIn(converse_group[1]),
            Write(converse_group[2]),
            FadeIn(converse_group[3]),
            FadeIn(converse_group[4]),
            run_time=1.2
        )
        
        # 高亮交换
        self.play(
            Indicate(self.original_group[2], color=self.COLOR_HIGHLIGHT),
            Indicate(converse_group[2], color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 例子
        example = Text(
            "例: 若同位角相等, 则两直线平行",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(Write(example), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(arrow_label),
            FadeOut(example),
            run_time=0.5
        )
        
        # 保存逆命题框
        self.converse_group = converse_group
    
    def show_inverse(self):
        """场景5: 否命题"""
        # 标题
        title = Text(
            "否命题 - 否定条件和结论",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_INVERSE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 重新排列：原命题移到左上
        self.play(
            self.original_group.animate.move_to(LEFT * 2.5 + UP * 3),
            self.converse_group.animate.move_to(RIGHT * 2.5 + UP * 3),
            run_time=0.6
        )
        
        # 创建否命题框
        inverse_group, inverse_box, _, _ = self.create_proposition_box(
            r"\neg p \rightarrow \neg q",
            "条件: ¬p",
            "结论: ¬q",
            self.COLOR_INVERSE,
            "否命题"
        )
        inverse_group.scale(0.7).move_to(LEFT * 2.5 + DOWN * 1)
        
        # 箭头指示变换
        arrow = Arrow(
            LEFT * 2.5 + UP * 1.8,
            LEFT * 2.5 + DOWN * 0.2,
            color=self.COLOR_ARROW,
            stroke_width=4
        )
        arrow_label = Text(
            "否定",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ARROW
        ).next_to(arrow, LEFT, buff=0.1)
        
        self.play(
            Create(arrow),
            FadeIn(arrow_label),
            run_time=0.6
        )
        
        self.play(
            Create(inverse_box),
            FadeIn(inverse_group[1]),
            Write(inverse_group[2]),
            FadeIn(inverse_group[3]),
            FadeIn(inverse_group[4]),
            run_time=1.2
        )
        
        # 高亮否定符号
        self.play(
            Indicate(inverse_group[2], color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 例子
        example = Text(
            "例: 若两直线不平行, 则同位角不相等",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(example), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(arrow_label),
            FadeOut(example),
            run_time=0.5
        )
        
        # 保存否命题框
        self.inverse_group = inverse_group
    
    def show_contrapositive(self):
        """场景6: 逆否命题"""
        # 标题
        title = Text(
            "逆否命题 - 交换并否定",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CONTRAPOSITIVE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建逆否命题框
        contrapositive_group, contrapositive_box, _, _ = self.create_proposition_box(
            r"\neg q \rightarrow \neg p",
            "条件: ¬q",
            "结论: ¬p",
            self.COLOR_CONTRAPOSITIVE,
            "逆否命题"
        )
        contrapositive_group.scale(0.7).move_to(RIGHT * 2.5 + DOWN * 1)
        
        # 箭头指示变换（从原命题到逆否命题）
        arrow = CurvedArrow(
            LEFT * 2.5 + UP * 2,
            RIGHT * 2.5 + DOWN * 0.2,
            color=self.COLOR_ARROW,
            stroke_width=3
        )
        arrow_label = Text(
            "交换+否定",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_ARROW
        ).move_to(ORIGIN + UP * 0.5)
        
        self.play(
            Create(arrow),
            FadeIn(arrow_label),
            run_time=0.6
        )
        
        self.play(
            Create(contrapositive_box),
            FadeIn(contrapositive_group[1]),
            Write(contrapositive_group[2]),
            FadeIn(contrapositive_group[3]),
            FadeIn(contrapositive_group[4]),
            run_time=1.2
        )
        
        # 高亮变换
        self.play(
            Indicate(self.original_group[2], color=self.COLOR_HIGHLIGHT),
            Indicate(contrapositive_group[2], color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 例子
        example = Text(
            "例: 若同位角不相等, 则两直线不平行",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(example), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(arrow_label),
            FadeOut(example),
            run_time=0.5
        )
        
        # 保存逆否命题框
        self.contrapositive_group = contrapositive_group
    
    def show_relationship_diagram(self):
        """场景7: 关系图"""
        # 标题
        title = Text(
            "四种命题的关系",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 7)
        
        self.play(Write(title), run_time=0.8)
        
        # 四个框排列成矩形
        positions = {
            'original': LEFT * 2.2 + UP * 2,
            'converse': RIGHT * 2.2 + UP * 2,
            'inverse': LEFT * 2.2 + DOWN * 2,
            'contrapositive': RIGHT * 2.2 + DOWN * 2
        }
        
        self.play(
            self.original_group.animate.move_to(positions['original']),
            self.converse_group.animate.move_to(positions['converse']),
            self.inverse_group.animate.move_to(positions['inverse']),
            self.contrapositive_group.animate.move_to(positions['contrapositive']),
            run_time=1.2
        )
        
        # 创建连接箭头
        # 上方互逆
        arrow_top = DoubleArrow(
            positions['original'] + RIGHT * 0.8,
            positions['converse'] + LEFT * 0.8,
            color=self.COLOR_ARROW,
            stroke_width=2,
            buff=0
        )
        label_top = Text(
            "互逆",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_ARROW
        ).next_to(arrow_top, UP, buff=0.1)
        
        # 下方互逆
        arrow_bottom = DoubleArrow(
            positions['inverse'] + RIGHT * 0.8,
            positions['contrapositive'] + LEFT * 0.8,
            color=self.COLOR_ARROW,
            stroke_width=2,
            buff=0
        )
        label_bottom = Text(
            "互逆",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_ARROW
        ).next_to(arrow_bottom, DOWN, buff=0.1)
        
        # 左侧互否
        arrow_left = DoubleArrow(
            positions['original'] + DOWN * 0.6,
            positions['inverse'] + UP * 0.6,
            color=self.COLOR_ARROW,
            stroke_width=2,
            buff=0
        )
        label_left = Text(
            "互否",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_ARROW
        ).next_to(arrow_left, LEFT, buff=0.1)
        
        # 右侧互否
        arrow_right = DoubleArrow(
            positions['converse'] + DOWN * 0.6,
            positions['contrapositive'] + UP * 0.6,
            color=self.COLOR_ARROW,
            stroke_width=2,
            buff=0
        )
        label_right = Text(
            "互否",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_ARROW
        ).next_to(arrow_right, RIGHT, buff=0.1)
        
        arrows = VGroup(arrow_top, arrow_bottom, arrow_left, arrow_right)
        labels = VGroup(label_top, label_bottom, label_left, label_right)
        
        self.play(
            *[Create(arrow) for arrow in arrows],
            run_time=1.2
        )
        
        self.play(
            *[FadeIn(label) for label in labels],
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 高亮等价关系（对角线）
        # 原命题 ⟺ 逆否命题
        equiv_line_1 = DashedLine(
            positions['original'],
            positions['contrapositive'],
            color=self.COLOR_EQUIV,
            stroke_width=4,
            dash_length=0.2
        )
        equiv_label_1 = Text(
            "等价",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_EQUIV,
            weight=BOLD
        ).move_to(ORIGIN + RIGHT * 0.3)
        
        # 逆命题 ⟺ 否命题
        equiv_line_2 = DashedLine(
            positions['converse'],
            positions['inverse'],
            color=self.COLOR_EQUIV,
            stroke_width=4,
            dash_length=0.2
        )
        equiv_label_2 = Text(
            "等价",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_EQUIV,
            weight=BOLD
        ).move_to(ORIGIN + LEFT * 0.3)
        
        self.play(
            Create(equiv_line_1),
            Create(equiv_line_2),
            run_time=1.0
        )
        
        self.play(
            Flash(self.original_group, color=self.COLOR_EQUIV, flash_radius=0.5),
            Flash(self.contrapositive_group, color=self.COLOR_EQUIV, flash_radius=0.5),
            FadeIn(equiv_label_1),
            run_time=0.8
        )
        
        self.play(
            Flash(self.converse_group, color=self.COLOR_EQUIV, flash_radius=0.5),
            Flash(self.inverse_group, color=self.COLOR_EQUIV, flash_radius=0.5),
            FadeIn(equiv_label_2),
            run_time=0.8
        )
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrows),
            FadeOut(labels),
            FadeOut(equiv_line_1),
            FadeOut(equiv_line_2),
            FadeOut(equiv_label_1),
            FadeOut(equiv_label_2),
            FadeOut(self.original_group),
            FadeOut(self.converse_group),
            FadeOut(self.inverse_group),
            FadeOut(self.contrapositive_group),
            run_time=0.8
        )
    
    def show_equivalence(self):
        """场景8: 等价关系强调"""
        # 标题
        title = Text(
            "等价关系的应用",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_EQUIV
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 等价公式
        equiv_formula_1 = MathTex(
            r"(p \rightarrow q) \Leftrightarrow (\neg q \rightarrow \neg p)",
            font_size=32,
            color=self.COLOR_EQUIV
        ).move_to(UP * 4.5)
        
        equiv_formula_2 = MathTex(
            r"(q \rightarrow p) \Leftrightarrow (\neg p \rightarrow \neg q)",
            font_size=32,
            color=self.COLOR_EQUIV
        ).move_to(UP * 3.5)
        
        self.play(Write(equiv_formula_1), run_time=1.2)
        self.play(Write(equiv_formula_2), run_time=1.2)
        
        # 说明文字
        explanation_title = Text(
            "重要性质:",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2)
        
        explanation = Text(
            "原命题与逆否命题同真同假",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(explanation_title, DOWN, buff=0.3)
        
        self.play(
            FadeIn(explanation_title),
            Write(explanation),
            run_time=1.0
        )
        
        # 应用说明
        application = VGroup(
            Text("应用: 当原命题难以直接证明时,", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("可以转而证明其逆否命题", font="PingFang SC", font_size=22, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        application.move_to(ORIGIN)
        
        self.play(FadeIn(application), run_time=1.0)
        
        # 例子
        example_box = Rectangle(
            width=7.5,
            height=2.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 3)
        
        example_title = Text(
            "例:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(example_box.get_top() + DOWN * 0.3 + LEFT * 3)
        
        example_original = Text(
            "原命题: 若 x² < 1, 则 -1 < x < 1",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(example_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        example_contra = Text(
            "逆否: 若 x≥1 或 x≤-1, 则 x²≥1",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_CONTRAPOSITIVE
        ).next_to(example_original, DOWN, buff=0.2, aligned_edge=LEFT)
        
        example_note = Text(
            "(逆否命题更容易证明)",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).next_to(example_contra, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Create(example_box), run_time=0.6)
        self.play(
            FadeIn(example_title),
            Write(example_original),
            run_time=1.0
        )
        self.play(
            Write(example_contra),
            FadeIn(example_note),
            run_time=1.0
        )
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(equiv_formula_1),
            FadeOut(equiv_formula_2),
            FadeOut(explanation_title),
            FadeOut(explanation),
            FadeOut(application),
            FadeOut(example_box),
            FadeOut(example_title),
            FadeOut(example_original),
            FadeOut(example_contra),
            FadeOut(example_note),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景9: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素 - 四个彩色小方框
        deco_boxes = VGroup()
        colors = [
            self.COLOR_ORIGINAL,
            self.COLOR_CONVERSE,
            self.COLOR_INVERSE,
            self.COLOR_CONTRAPOSITIVE
        ]
        
        for i, color in enumerate(colors):
            box = Rectangle(
                width=0.5,
                height=0.5,
                color=color,
                fill_opacity=0.6,
                stroke_width=2
            )
            deco_boxes.add(box)
        
        deco_boxes.arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(box, scale=0.5) for box in deco_boxes],
            run_time=0.6
        )
        
        # 符号旋转
        symbols = VGroup(
            MathTex(r"p \rightarrow q", font_size=30, color=self.COLOR_ORIGINAL),
            MathTex(r"q \rightarrow p", font_size=30, color=self.COLOR_CONVERSE),
            MathTex(r"\neg p \rightarrow \neg q", font_size=28, color=self.COLOR_INVERSE),
            MathTex(r"\neg q \rightarrow \neg p", font_size=28, color=self.COLOR_CONTRAPOSITIVE)
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 4.5)
        
        self.play(
            *[FadeIn(symbol, scale=0.5) for symbol in symbols],
            run_time=0.6
        )
        
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_boxes),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql four_propositions.py FourPropositions  # 快速预览
# manim -qm four_propositions.py FourPropositions   # 中等质量
# manim -qh four_propositions.py FourPropositions   # 高质量 (推荐)