"""
集合的运算动画 - Set Operations Animation
使用 Manim 创建的高中数学教学视频

内容: 交集、并集、补集的定义和性质
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


class SetOperations(Scene):
    """
    集合运算教学动画场景
    
    场景顺序:
    1. 开场介绍
    2. 交集演示
    3. 并集演示
    4. 补集演示
    5. 运算性质1
    6. 运算性质2
    7. 综合示例
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_SET_A = "#e74c3c"        # 红色 - 集合A
        self.COLOR_SET_B = "#3498db"        # 蓝色 - 集合B
        self.COLOR_UNIVERSAL = "#95a5a6"    # 灰色 - 全集
        self.COLOR_INTERSECTION = "#9b59b6" # 紫色 - 交集
        self.COLOR_UNION = "#2ecc71"        # 绿色 - 并集
        self.COLOR_COMPLEMENT = "#f39c12"   # 橙色 - 补集
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_intersection()
        self.show_union()
        self.show_complement()
        self.show_properties_1()
        self.show_properties_2()
        self.show_example()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化集合的几何位置"""
        # 两个圆的中心位置
        self.center_A = LEFT * 1.0 + UP * 2
        self.center_B = RIGHT * 1.0 + UP * 2
        
        # 圆的半径
        self.radius = 1.2
        
        # 全集矩形的位置和大小
        self.universal_width = 7.0
        self.universal_height = 4.5
        self.universal_center = UP * 2
        
        print("✓ 几何初始化完成")
    
    def create_venn_circles(self, with_labels=True):
        """创建文氏图的两个圆"""
        circle_A = Circle(
            radius=self.radius,
            color=self.COLOR_SET_A,
            stroke_width=3
        ).move_to(self.center_A)
        
        circle_B = Circle(
            radius=self.radius,
            color=self.COLOR_SET_B,
            stroke_width=3
        ).move_to(self.center_B)
        
        if with_labels:
            label_A = Text("A", font="PingFang SC", font_size=32, color=WHITE)\
                .move_to(self.center_A + LEFT * 0.8 + UP * 0.3)
            label_B = Text("B", font="PingFang SC", font_size=32, color=WHITE)\
                .move_to(self.center_B + RIGHT * 0.8 + UP * 0.3)
            return circle_A, circle_B, label_A, label_B
        else:
            return circle_A, circle_B
    
    def create_universal_set(self):
        """创建全集矩形"""
        rect = Rectangle(
            width=self.universal_width,
            height=self.universal_height,
            color=self.COLOR_UNIVERSAL,
            stroke_width=3
        ).move_to(self.universal_center)
        
        label = Text("U", font="PingFang SC", font_size=28, color=WHITE)\
            .move_to(rect.get_corner(UL) + DOWN * 0.3 + RIGHT * 0.3)
        
        return rect, label
    
    def show_opening(self):
        """场景1: 开场介绍"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子标题
        hook = Text(
            "集合的三大运算",
            font="PingFang SC",
            font_size=44,
            color=GOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "交集·并集·补集",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 创建两个圆形集合预览
        circle_A, circle_B, label_A, label_B = self.create_venn_circles()
        
        self.play(
            Create(circle_A),
            Create(circle_B),
            run_time=1.0
        )
        
        self.play(
            FadeIn(label_A),
            FadeIn(label_B),
            run_time=0.4
        )
        
        # 提示文字
        hint = Text(
            "三种运算, 一次掌握!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            FadeOut(hint),
            run_time=0.5
        )
        
        # 保存圆形和标签供后续使用
        self.circle_A = circle_A
        self.circle_B = circle_B
        self.label_A = label_A
        self.label_B = label_B
    
    def show_intersection(self):
        """场景2: 交集演示"""
        # 标题
        title = Text(
            "交集 Intersection",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_INTERSECTION
        ).move_to(UP * 5.5)
        
        # 数学符号
        symbol = MathTex(r"A \cap B", font_size=40, color=self.COLOR_INTERSECTION)\
            .next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(symbol), run_time=0.5)
        
        # 定义公式
        definition = MathTex(
            r"A \cap B = \{ x \mid x \in A \text{ and } x \in B \}",
            font_size=28
        ).move_to(UP * 4.2)
        
        # 中文说明
        explanation = Text(
            "既属于A又属于B的元素",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(Write(definition), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 填充圆A
        filled_A = Circle(
            radius=self.radius,
            color=self.COLOR_SET_A,
            stroke_width=3,
            fill_color=self.COLOR_SET_A,
            fill_opacity=0.3
        ).move_to(self.center_A)
        
        self.play(
            Transform(self.circle_A, filled_A),
            run_time=0.6
        )
        
        # 填充圆B
        filled_B = Circle(
            radius=self.radius,
            color=self.COLOR_SET_B,
            stroke_width=3,
            fill_color=self.COLOR_SET_B,
            fill_opacity=0.3
        ).move_to(self.center_B)
        
        self.play(
            Transform(self.circle_B, filled_B),
            run_time=0.6
        )
        
        # 创建交集区域 (使用 Intersection)
        intersection = Intersection(
            Circle(radius=self.radius).move_to(self.center_A),
            Circle(radius=self.radius).move_to(self.center_B),
            color=self.COLOR_INTERSECTION,
            fill_color=self.COLOR_INTERSECTION,
            fill_opacity=0.6,
            stroke_width=0
        )
        
        self.play(FadeIn(intersection, scale=0.8), run_time=0.8)
        
        # 示例元素
        example_title = Text(
            "示例:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 3)
        
        example_text = MathTex(
            r"A = \{1, 2, 3, 4\}",
            font_size=24
        ).next_to(example_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        example_text_2 = MathTex(
            r"B = \{3, 4, 5, 6\}",
            font_size=24
        ).next_to(example_text, DOWN, aligned_edge=LEFT, buff=0.2)
        
        example_text_3 = MathTex(
            r"A \cap B = \{3, 4\}",
            font_size=24,
            color=self.COLOR_INTERSECTION
        ).next_to(example_text_2, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(
            FadeIn(example_title),
            Write(example_text),
            run_time=0.8
        )
        self.play(Write(example_text_2), run_time=0.6)
        self.play(Write(example_text_3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(symbol),
            FadeOut(definition),
            FadeOut(explanation),
            FadeOut(intersection),
            FadeOut(example_title),
            FadeOut(example_text),
            FadeOut(example_text_2),
            FadeOut(example_text_3),
            run_time=0.6
        )
        
        # 恢复圆形为无填充
        circle_A_unfilled = Circle(
            radius=self.radius,
            color=self.COLOR_SET_A,
            stroke_width=3
        ).move_to(self.center_A)
        
        circle_B_unfilled = Circle(
            radius=self.radius,
            color=self.COLOR_SET_B,
            stroke_width=3
        ).move_to(self.center_B)
        
        self.play(
            Transform(self.circle_A, circle_A_unfilled),
            Transform(self.circle_B, circle_B_unfilled),
            run_time=0.3
        )
    
    def show_union(self):
        """场景3: 并集演示"""
        # 标题
        title = Text(
            "并集 Union",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_UNION
        ).move_to(UP * 5.5)
        
        # 数学符号
        symbol = MathTex(r"A \cup B", font_size=40, color=self.COLOR_UNION)\
            .next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(symbol), run_time=0.5)
        
        # 定义公式
        definition = MathTex(
            r"A \cup B = \{ x \mid x \in A \text{ or } x \in B \}",
            font_size=28
        ).move_to(UP * 4.2)
        
        # 中文说明
        explanation = Text(
            "属于A或属于B的所有元素",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(Write(definition), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 创建并集区域 (使用 Union)
        union = Union(
            Circle(radius=self.radius).move_to(self.center_A),
            Circle(radius=self.radius).move_to(self.center_B),
            color=self.COLOR_UNION,
            fill_color=self.COLOR_UNION,
            fill_opacity=0.3,
            stroke_width=4
        )
        
        self.play(FadeIn(union, scale=0.9), run_time=1.0)
        
        # 示例元素
        example_title = Text(
            "示例:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.5 + LEFT * 3)
        
        example_text = MathTex(
            r"A = \{1, 2, 3, 4\}",
            font_size=24
        ).next_to(example_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        example_text_2 = MathTex(
            r"B = \{3, 4, 5, 6\}",
            font_size=24
        ).next_to(example_text, DOWN, aligned_edge=LEFT, buff=0.2)
        
        example_text_3 = MathTex(
            r"A \cup B = \{1, 2, 3, 4, 5, 6\}",
            font_size=24,
            color=self.COLOR_UNION
        ).next_to(example_text_2, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(
            FadeIn(example_title),
            Write(example_text),
            run_time=0.8
        )
        self.play(Write(example_text_2), run_time=0.6)
        self.play(Write(example_text_3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(symbol),
            FadeOut(definition),
            FadeOut(explanation),
            FadeOut(union),
            FadeOut(example_title),
            FadeOut(example_text),
            FadeOut(example_text_2),
            FadeOut(example_text_3),
            run_time=0.6
        )
    
    def show_complement(self):
        """场景4: 补集演示"""
        # 创建全集矩形
        universal_rect, universal_label = self.create_universal_set()
        
        self.play(
            Create(universal_rect),
            FadeIn(universal_label),
            run_time=0.8
        )
        
        # 标题
        title = Text(
            "补集 Complement",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_COMPLEMENT
        ).move_to(UP * 5.5)
        
        # 数学符号 - 使用正确的补集符号
        symbol = MathTex(r"\complement_U A", font_size=40, color=self.COLOR_COMPLEMENT)\
            .next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        self.play(Write(symbol), run_time=0.5)
        
        # 定义公式
        definition = MathTex(
            r"\complement_U A = \{ x \mid x \in U \text{ and } x \notin A \}",
            font_size=26
        ).move_to(UP * 4.2)
        
        # 中文说明
        explanation = Text(
            "全集中不属于A的所有元素",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5)
        
        self.play(Write(definition), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 创建补集区域 (全集减去集合A)
        complement = Difference(
            Rectangle(width=self.universal_width, height=self.universal_height)\
                .move_to(self.universal_center),
            Circle(radius=self.radius).move_to(self.center_A),
            color=self.COLOR_COMPLEMENT,
            fill_color=self.COLOR_COMPLEMENT,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(FadeIn(complement), run_time=1.0)
        
        # 示例元素
        example_title = Text(
            "示例:",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5 + LEFT * 3)
        
        example_text = MathTex(
            r"U = \{1, 2, 3, 4, 5, 6\}",
            font_size=24
        ).next_to(example_title, DOWN, aligned_edge=LEFT, buff=0.3)
        
        example_text_2 = MathTex(
            r"A = \{1, 2, 3\}",
            font_size=24
        ).next_to(example_text, DOWN, aligned_edge=LEFT, buff=0.2)
        
        example_text_3 = MathTex(
            r"\complement_U A = \{4, 5, 6\}",
            font_size=24,
            color=self.COLOR_COMPLEMENT
        ).next_to(example_text_2, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(
            FadeIn(example_title),
            Write(example_text),
            run_time=0.8
        )
        self.play(Write(example_text_2), run_time=0.6)
        self.play(Write(example_text_3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(symbol),
            FadeOut(definition),
            FadeOut(explanation),
            FadeOut(complement),
            FadeOut(example_title),
            FadeOut(example_text),
            FadeOut(example_text_2),
            FadeOut(example_text_3),
            FadeOut(universal_rect),
            FadeOut(universal_label),
            run_time=0.6
        )
    
    def show_properties_1(self):
        """场景5: 运算性质1 - 基本性质"""
        # 标题
        title = Text(
            "运算性质",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "基本性质",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 性质列表
        property_1 = MathTex(
            r"A \cap \emptyset = \emptyset",
            font_size=32
        ).move_to(UP * 4.5)
        
        property_2 = MathTex(
            r"A \cup \emptyset = A",
            font_size=32
        ).move_to(UP * 3.5)
        
        property_3 = MathTex(
            r"A \cap A = A",
            font_size=32
        ).move_to(UP * 2.5)
        
        property_4 = MathTex(
            r"A \cup A = A",
            font_size=32
        ).move_to(UP * 1.5)
        
        # 中文说明
        explain_1 = Text(
            "与空集的交集为空集",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(property_1, RIGHT, buff=0.5)
        
        explain_2 = Text(
            "与空集的并集为自身",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(property_2, RIGHT, buff=0.5)
        
        self.play(Write(property_1), FadeIn(explain_1), run_time=0.8)
        self.wait(0.5)
        self.play(Write(property_2), FadeIn(explain_2), run_time=0.8)
        self.wait(0.5)
        self.play(Write(property_3), run_time=0.6)
        self.wait(0.5)
        self.play(Write(property_4), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(property_1),
            FadeOut(property_2),
            FadeOut(property_3),
            FadeOut(property_4),
            FadeOut(explain_1),
            FadeOut(explain_2),
            run_time=0.6
        )
    
    def show_properties_2(self):
        """场景6: 运算性质2 - 补集性质"""
        # 标题
        title = Text(
            "补集性质",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_COMPLEMENT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 性质列表
        property_1 = MathTex(
            r"(\complement_U A) \cup A = U",
            font_size=32
        ).move_to(UP * 4.5)
        
        property_2 = MathTex(
            r"(\complement_U A) \cap A = \emptyset",
            font_size=32
        ).move_to(UP * 3.5)
        
        property_3 = MathTex(
            r"\complement_U(\complement_U A) = A",
            font_size=32
        ).move_to(UP * 2.5)
        
        # 中文说明
        explain_1 = Text(
            "补集与原集合的并集为全集",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).next_to(property_1, DOWN, buff=0.2)
        
        explain_2 = Text(
            "补集与原集合的交集为空集",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).next_to(property_2, DOWN, buff=0.2)
        
        explain_3 = Text(
            "补集的补集是原集合",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).next_to(property_3, DOWN, buff=0.2)
        
        self.play(Write(property_1), FadeIn(explain_1), run_time=1.0)
        self.wait(0.8)
        self.play(Write(property_2), FadeIn(explain_2), run_time=1.0)
        self.wait(0.8)
        self.play(Write(property_3), FadeIn(explain_3), run_time=1.0)
        
        # 重点强调
        highlight = Text(
            "这些性质是解题的关键!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property_1),
            FadeOut(property_2),
            FadeOut(property_3),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(explain_3),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def show_example(self):
        """场景7: 综合示例"""
        # 标题
        title = Text(
            "综合应用",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 题目
        question = Text(
            "已知:",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5 + LEFT * 3.5)
        
        given_1 = MathTex(
            r"U = \{1, 2, 3, 4, 5, 6, 7, 8\}",
            font_size=28
        ).next_to(question, DOWN, aligned_edge=LEFT, buff=0.3)
        
        given_2 = MathTex(
            r"A = \{1, 3, 5, 7\}",
            font_size=28
        ).next_to(given_1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        given_3 = MathTex(
            r"B = \{2, 3, 5, 8\}",
            font_size=28
        ).next_to(given_2, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.play(
            FadeIn(question),
            Write(given_1),
            run_time=0.8
        )
        self.play(Write(given_2), run_time=0.6)
        self.play(Write(given_3), run_time=0.6)
        
        # 求解
        solve = Text(
            "求:",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 2.5 + LEFT * 3.5)
        
        result_1 = MathTex(
            r"A \cap B = \{3, 5\}",
            font_size=28,
            color=self.COLOR_INTERSECTION
        ).next_to(solve, DOWN, aligned_edge=LEFT, buff=0.3)
        
        result_2 = MathTex(
            r"A \cup B = \{1, 2, 3, 5, 7, 8\}",
            font_size=26,
            color=self.COLOR_UNION
        ).next_to(result_1, DOWN, aligned_edge=LEFT, buff=0.3)
        
        result_3 = MathTex(
            r"\complement_U A = \{2, 4, 6, 8\}",
            font_size=28,
            color=self.COLOR_COMPLEMENT
        ).next_to(result_2, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(FadeIn(solve), run_time=0.5)
        self.wait(0.5)
        
        self.play(Write(result_1), run_time=0.8)
        self.wait(0.5)
        self.play(Write(result_2), run_time=0.8)
        self.wait(0.5)
        self.play(Write(result_3), run_time=0.8)
        
        # 完成标记
        checkmark = Text(
            "✓",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        complete_text = Text(
            "完成!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(checkmark, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(checkmark, scale=1.5),
            FadeIn(complete_text),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 清理所有
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(given_1),
            FadeOut(given_2),
            FadeOut(given_3),
            FadeOut(solve),
            FadeOut(result_1),
            FadeOut(result_2),
            FadeOut(result_3),
            FadeOut(checkmark),
            FadeOut(complete_text),
            FadeOut(self.circle_A),
            FadeOut(self.circle_B),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
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
            "关注我, 掌握更多集合技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰元素 - 三个彩色圆圈
        circles_deco = VGroup(
            Circle(radius=0.4, color=self.COLOR_SET_A, fill_opacity=0.8).shift(LEFT * 2),
            Circle(radius=0.4, color=self.COLOR_UNION, fill_opacity=0.8),
            Circle(radius=0.4, color=self.COLOR_SET_B, fill_opacity=0.8).shift(RIGHT * 2)
        ).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in circles_deco],
            run_time=0.6
        )
        
        # 符号旋转
        symbols = VGroup(
            MathTex(r"\cap", font_size=40, color=self.COLOR_INTERSECTION).shift(LEFT * 1.5 + DOWN * 4),
            MathTex(r"\cup", font_size=40, color=self.COLOR_UNION).shift(DOWN * 4),
            MathTex(r"\complement", font_size=40, color=self.COLOR_COMPLEMENT).shift(RIGHT * 1.5 + DOWN * 4)
        )
        
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
            FadeOut(circles_deco),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql set_operations.py SetOperations  # 快速预览
# manim -qm set_operations.py SetOperations   # 中等质量
# manim -qh set_operations.py SetOperations   # 高质量 (推荐)