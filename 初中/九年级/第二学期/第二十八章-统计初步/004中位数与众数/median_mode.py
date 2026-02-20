"""
中位数与众数教学动画 - Median and Mode Educational Animation
使用 Manim 创建的初中统计学教学视频

内容: 中位数、众数的定义、计算和性质
目标观众: 初中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from collections import Counter
import random as rand


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class MedianAndMode(Scene):
    """
    中位数与众数教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 中位数 - 奇数情况
    3. 中位数 - 偶数情况
    4. 中位数性质（不受极端值影响）
    5. 众数概念
    6. 中位数与众数对比
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_MEDIAN = "#e74c3c"         # 红色 - 中位数
        self.COLOR_MODE = "#3498db"           # 蓝色 - 众数
        self.COLOR_DATA = "#2ecc71"           # 绿色 - 数据点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化数据
        self.setup_data()
        
        # 执行动画序列
        self.show_opening()
        self.show_median_odd()
        self.show_median_even()
        self.show_median_robustness()
        self.show_mode()
        self.show_comparison()
        self.show_outro()
    
    def setup_data(self):
        """初始化所有数据"""
        # 奇数数据集
        self.odd_data = [3, 7, 5, 9, 2]
        self.odd_sorted = sorted(self.odd_data)  # [2, 3, 5, 7, 9]
        
        # 偶数数据集
        self.even_data = [4, 8, 2, 6, 5, 9]
        self.even_sorted = sorted(self.even_data)  # [2, 4, 5, 6, 8, 9]
        
        # 众数数据集
        self.mode_data = [3, 5, 7, 5, 9, 5, 2]
        
        # 极端值数据
        self.normal_data = [5, 6, 7, 8, 9]
        self.extreme_data = [5, 6, 7, 8, 100]
        
        # 验证数据
        self.verify_data()
    
    def verify_data(self):
        """验证数据计算"""
        # 验证奇数中位数
        n_odd = len(self.odd_sorted)
        median_index_odd = (n_odd + 1) // 2 - 1
        median_odd = self.odd_sorted[median_index_odd]
        print(f"奇数中位数: {median_odd} (索引{median_index_odd})")
        
        # 验证偶数中位数
        n_even = len(self.even_sorted)
        index1 = n_even // 2 - 1
        index2 = n_even // 2
        median_even = (self.even_sorted[index1] + self.even_sorted[index2]) / 2
        print(f"偶数中位数: {median_even} (索引{index1},{index2})")
        
        # 验证众数
        freq = Counter(self.mode_data)
        mode = max(freq, key=freq.get)
        mode_count = freq[mode]
        print(f"众数: {mode} (出现{mode_count}次)")
        
        # 验证极端值
        median_normal = self.normal_data[2]
        median_extreme = self.extreme_data[2]
        print(f"正常数据中位数: {median_normal}")
        print(f"极端数据中位数: {median_extreme}")
        
        print("✓ 数据验证完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "一组数据的中心在哪?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook), run_time=0.8)
        
        # 混乱的数据点
        numbers = [3, 7, 5, 9, 2, 8, 4, 6]
        dots = VGroup()
        
        for num in numbers:
            dot_group = VGroup(
                Circle(radius=0.35, fill_opacity=1, color=self.COLOR_DATA, stroke_width=2, stroke_color=WHITE),
                Text(str(num), font="Noto Sans CJK SC", font_size=32, color=WHITE)
            )
            # 随机位置
            x = rand.uniform(-3, 3)
            y = rand.uniform(1, 4)
            dot_group.move_to([x, y, 0])
            dots.add(dot_group)
        
        self.play(FadeIn(dots, lag_ratio=0.1), run_time=1.0)
        
        # 数据点混乱移动
        animations = []
        for dot in dots:
            new_x = rand.uniform(-3, 3)
            new_y = rand.uniform(1, 4)
            animations.append(dot.animate.move_to([new_x, new_y, 0]))
        
        self.play(*animations, run_time=0.8)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(dots),
            run_time=0.5
        )
    
    def show_median_odd(self):
        """场景2: 中位数 - 奇数情况"""
        # 标题
        title = Text(
            "中位数 Median",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MEDIAN
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "数据个数为奇数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 原始数据（未排序）
        original_boxes = self.create_data_boxes(self.odd_data, color=self.COLOR_DATA)
        original_boxes.arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        original_label = Text(
            "原始数据:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(original_boxes, UP, buff=0.3)
        
        self.play(FadeIn(original_label), run_time=0.3)
        self.play(FadeIn(original_boxes, lag_ratio=0.15), run_time=0.8)
        
        # 排序提示
        sort_text = Text(
            "第一步: 从小到大排序",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(Write(sort_text), run_time=0.4)
        self.wait(0.3)
        
        # 排序后的数据
        sorted_boxes = self.create_data_boxes(self.odd_sorted, color=self.COLOR_DATA)
        sorted_boxes.arrange(RIGHT, buff=0.3).move_to(UP * 1.5)
        
        sorted_label = Text(
            "排序后:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(sorted_boxes, UP, buff=0.3)
        
        # 排序动画
        self.play(
            FadeOut(original_label),
            FadeOut(original_boxes),
            FadeOut(sort_text),
            run_time=0.3
        )
        
        self.play(FadeIn(sorted_label), run_time=0.3)
        self.play(
            *[FadeIn(box, shift=DOWN * 0.5) for box in sorted_boxes],
            lag_ratio=0.15,
            run_time=1.2
        )
        
        # 标记中间位置
        n = len(self.odd_sorted)
        middle_index = n // 2
        median_value = self.odd_sorted[middle_index]
        
        # 中间位置箭头
        arrow = Arrow(
            start=sorted_boxes[middle_index].get_bottom() + DOWN * 0.5,
            end=sorted_boxes[middle_index].get_bottom(),
            color=self.COLOR_MEDIAN,
            stroke_width=6,
            buff=0.1
        )
        
        middle_text = Text(
            "中间位置",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_MEDIAN
        ).next_to(arrow, DOWN, buff=0.1)
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(middle_text), run_time=0.3)
        
        # 高亮中位数
        self.play(
            sorted_boxes[middle_index].animate.set_fill(self.COLOR_MEDIAN, opacity=1),
            sorted_boxes[middle_index].animate.scale(1.2),
            run_time=0.4
        )
        
        # 公式
        formula_text = Text(
            "中位数 = 第",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        )
        formula_math = MathTex(
            r"\frac{n+1}{2}",
            font_size=28,
            color=WHITE
        )
        formula_rest = Text(
            "个数",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        )
        formula = VGroup(formula_text, formula_math, formula_rest).arrange(RIGHT, buff=0.1).move_to(DOWN * 1)
        
        calculation_text = Text(
            "= 第",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        calculation_math = MathTex(
            r"\frac{5+1}{2}",
            font_size=24,
            color=GRAY_A
        )
        calculation_rest = Text(
            "个数 = 第3个数 = 5",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        calculation = VGroup(calculation_text, calculation_math, calculation_rest).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.8)
        
        self.play(Write(formula), run_time=1.0)
        self.play(Write(calculation), run_time=0.8)
        
        # 结果
        result = Text(
            f"中位数 = {median_value}",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_MEDIAN,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(result, scale=1.2), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sorted_label),
            FadeOut(sorted_boxes),
            FadeOut(arrow),
            FadeOut(middle_text),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(result),
            run_time=0.6
        )
    
    def show_median_even(self):
        """场景3: 中位数 - 偶数情况"""
        # 标题
        title = Text(
            "中位数 Median",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MEDIAN
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "数据个数为偶数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 已排序的数据
        sorted_boxes = self.create_data_boxes(self.even_sorted, color=self.COLOR_DATA)
        sorted_boxes.arrange(RIGHT, buff=0.25).move_to(UP * 3.5)
        
        sorted_label = Text(
            "排序后的数据:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(sorted_boxes, UP, buff=0.3)
        
        self.play(FadeIn(sorted_label), run_time=0.3)
        self.play(FadeIn(sorted_boxes, lag_ratio=0.1), run_time=0.8)
        
        # 标记中间两个数
        n = len(self.even_sorted)
        index1 = n // 2 - 1  # 2
        index2 = n // 2      # 3
        
        # 大括号标记
        brace = Brace(
            VGroup(sorted_boxes[index1], sorted_boxes[index2]),
            direction=DOWN,
            buff=0.2,
            color=self.COLOR_MEDIAN
        )
        
        brace_text = Text(
            "中间两个数",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_MEDIAN
        ).next_to(brace, DOWN, buff=0.1)
        
        self.play(Create(brace), run_time=0.6)
        self.play(FadeIn(brace_text), run_time=0.3)
        
        # 高亮两个数
        self.play(
            sorted_boxes[index1].animate.set_fill(self.COLOR_MEDIAN, opacity=1).scale(1.15),
            sorted_boxes[index2].animate.set_fill(self.COLOR_MEDIAN, opacity=1).scale(1.15),
            run_time=0.4
        )
        
        # 计算步骤
        value1 = self.even_sorted[index1]
        value2 = self.even_sorted[index2]
        median = (value1 + value2) / 2
        
        # 加法
        addition = MathTex(
            f"{value1} + {value2}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 0.5)
        
        self.play(Write(addition), run_time=0.6)
        
        # 除法
        division = MathTex(
            r"\div 2",
            font_size=32,
            color=WHITE
        ).next_to(addition, RIGHT, buff=0.3)
        
        self.play(Write(division), run_time=0.6)
        
        # 等号和结果
        equals = MathTex(
            "=",
            font_size=32,
            color=WHITE
        ).next_to(division, RIGHT, buff=0.3)
        
        result_value = MathTex(
            f"{median}",
            font_size=32,
            color=self.COLOR_MEDIAN
        ).next_to(equals, RIGHT, buff=0.3)
        
        self.play(Write(equals), run_time=0.3)
        self.play(Write(result_value), run_time=0.5)
        
        # 公式
        formula_part1 = Text(
            "中位数 = ",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        formula_middle_text1 = Text(
            "第",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        formula_math_n2 = MathTex(
            r"\frac{n}{2}",
            font_size=24,
            color=WHITE
        )
        formula_middle_text2 = Text(
            "个数 + 第",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        formula_math_n2_plus1 = MathTex(
            r"(\frac{n}{2}+1)",
            font_size=24,
            color=WHITE
        )
        formula_end_text = Text(
            "个数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        formula_div2 = MathTex(
            r"\over 2",
            font_size=24,
            color=WHITE
        )
        
        formula = VGroup(
            formula_part1, 
            formula_middle_text1, 
            formula_math_n2, 
            formula_middle_text2, 
            formula_math_n2_plus1, 
            formula_end_text, 
            formula_div2
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 最终结果
        final_result = Text(
            f"中位数 = {median}",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_MEDIAN,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(final_result, scale=1.2), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sorted_label),
            FadeOut(sorted_boxes),
            FadeOut(brace),
            FadeOut(brace_text),
            FadeOut(addition),
            FadeOut(division),
            FadeOut(equals),
            FadeOut(result_value),
            FadeOut(formula),
            FadeOut(final_result),
            run_time=0.6
        )
    
    def show_median_robustness(self):
        """场景4: 中位数的鲁棒性"""
        # 标题
        title = Text(
            "中位数的特点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MEDIAN
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 正常数据
        normal_boxes = self.create_data_boxes(self.normal_data, color=self.COLOR_DATA)
        normal_boxes.arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        normal_label = Text(
            "正常数据:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(normal_boxes, UP, buff=0.3)
        
        self.play(FadeIn(normal_label), run_time=0.3)
        self.play(FadeIn(normal_boxes, lag_ratio=0.1), run_time=0.6)
        
        # 标记中位数
        median_index = 2
        self.play(
            normal_boxes[median_index].animate.set_fill(self.COLOR_MEDIAN, opacity=1).scale(1.2),
            run_time=0.4
        )
        
        median_1 = Text(
            "中位数 = 7",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_MEDIAN
        ).move_to(UP * 1.8)
        
        self.play(Write(median_1), run_time=0.4)
        
        # 变成极端数据
        extreme_boxes = self.create_data_boxes(self.extreme_data, color=self.COLOR_DATA)
        extreme_boxes.arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        # 保持中位数高亮
        extreme_boxes[median_index].set_fill(self.COLOR_MEDIAN, opacity=1).scale(1.2)
        
        extreme_label = Text(
            "含极端值:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(extreme_boxes, UP, buff=0.3)
        
        self.play(
            Transform(normal_label, extreme_label),
            *[Transform(normal_boxes[i], extreme_boxes[i]) for i in range(len(normal_boxes))],
            run_time=0.8
        )
        
        # 闪烁极端值
        self.play(
            Flash(normal_boxes[4], color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.3
        )
        
        # 中位数仍然是7
        median_2 = Text(
            "中位数仍 = 7",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_MEDIAN,
            weight=BOLD
        ).move_to(UP * 0.8)
        
        self.play(Write(median_2), run_time=0.5)
        
        # 对比平均数
        comparison = VGroup(
            Text("平均数: 7.0 → 25.2", font="Noto Sans CJK SC", font_size=24, color=GRAY_A),
            Text("中位数: 7 → 7", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_MEDIAN, weight=BOLD)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 1)
        
        self.play(Write(comparison), run_time=1.0)
        
        # 总结
        summary = Text(
            "中位数不受极端值影响!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(summary, shift=UP * 0.3, scale=1.1), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(normal_label),
            FadeOut(normal_boxes),
            FadeOut(median_1),
            FadeOut(median_2),
            FadeOut(comparison),
            FadeOut(summary),
            run_time=0.6
        )
    
    def show_mode(self):
        """场景5: 众数"""
        # 标题
        title = Text(
            "众数 Mode",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MODE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 数据展示
        data_boxes = self.create_data_boxes(self.mode_data, color=self.COLOR_DATA)
        data_boxes.arrange(RIGHT, buff=0.25).move_to(UP * 4.5)
        
        data_label = Text(
            "数据:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(data_boxes, UP, buff=0.3)
        
        self.play(FadeIn(data_label), run_time=0.3)
        self.play(FadeIn(data_boxes, lag_ratio=0.1), run_time=0.8)
        
        # 频数统计表
        freq = Counter(self.mode_data)
        unique_values = sorted(freq.keys())
        
        # 创建表格
        table_data = []
        for val in unique_values:
            count = freq[val]
            table_data.append([str(val), str(count)])
        
        # 表头
        header = VGroup(
            Text("数值", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("次数", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(RIGHT, buff=1.5)
        
        # 表格行
        rows = VGroup()
        for val_str, count_str in table_data:
            row = VGroup(
                Text(val_str, font="Noto Sans CJK SC", font_size=20, color=WHITE),
                Text(count_str, font="Noto Sans CJK SC", font_size=20, color=WHITE)
            ).arrange(RIGHT, buff=1.5)
            rows.add(row)
        
        # 组合表格
        freq_table = VGroup(header, *rows).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 添加边框
        table_box = SurroundingRectangle(
            freq_table,
            color=self.COLOR_AUXILIARY,
            buff=0.3,
            stroke_width=2
        )
        
        table_group = VGroup(freq_table, table_box).move_to(UP * 1)
        
        table_title = Text(
            "频数统计:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).next_to(table_group, UP, buff=0.3)
        
        self.play(FadeIn(table_title), run_time=0.3)
        self.play(Create(table_box), run_time=0.4)
        self.play(Write(header), run_time=0.5)
        
        # 逐行统计
        for row in rows:
            self.play(Write(row), run_time=0.3)
        
        self.wait(0.3)
        
        # 找出众数
        mode_value = max(freq, key=freq.get)
        mode_count = freq[mode_value]
        
        # 在表格中高亮众数
        mode_row_index = unique_values.index(mode_value)
        self.play(
            rows[mode_row_index].animate.set_color(self.COLOR_MODE).scale(1.15),
            run_time=0.4
        )
        
        # 在数据中高亮所有众数
        mode_indices = [i for i, val in enumerate(self.mode_data) if val == mode_value]
        self.play(
            *[data_boxes[i].animate.set_fill(self.COLOR_MODE, opacity=1).scale(1.1) 
              for i in mode_indices],
            run_time=0.5
        )
        
        # 标记众数
        mode_label = Text(
            f"众数 = {mode_value} (出现{mode_count}次)",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_MODE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(mode_label, scale=1.1), run_time=0.5)
        
        # 定义
        definition = Text(
            "众数: 出现次数最多的数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(definition), run_time=1.0)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(data_label),
            FadeOut(data_boxes),
            FadeOut(table_title),
            FadeOut(table_group),
            FadeOut(mode_label),
            FadeOut(definition),
            run_time=0.6
        )
    
    def show_comparison(self):
        """场景6: 中位数与众数对比"""
        # 标题
        title = Text(
            "中位数 vs 众数",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 中位数卡片
        median_card = self.create_concept_card(
            "中位数",
            "位置的中心",
            "不受极端值影响",
            self.COLOR_MEDIAN
        ).move_to(LEFT * 2 + UP * 2.5)
        
        # 众数卡片
        mode_card = self.create_concept_card(
            "众数",
            "频数的中心",
            "反映数据集中趋势",
            self.COLOR_MODE
        ).move_to(RIGHT * 2 + UP * 2.5)
        
        self.play(FadeIn(median_card, shift=RIGHT * 0.5), run_time=0.6)
        self.play(FadeIn(mode_card, shift=LEFT * 0.5), run_time=0.6)
        
        # 对比特点
        features_title = Text(
            "主要区别:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 0.2)
        
        features = VGroup(
            Text("• 中位数看位置，众数看频数", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("• 中位数需排序，众数不需要", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("• 两者可能不相等", font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(features_title, DOWN, buff=0.4)
        
        self.play(Write(features_title), run_time=0.5)
        self.play(Write(features, lag_ratio=0.3), run_time=1.5)
        
        # 应用场景
        app_title = Text(
            "应用场景:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        applications = VGroup(
            Text("工资水平 → 中位数", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_MEDIAN),
            Text("鞋码统计 → 众数", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_MODE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(app_title, DOWN, buff=0.4)
        
        self.play(Write(app_title), run_time=0.4)
        self.play(Write(applications, lag_ratio=0.3), run_time=1.2)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(median_card),
            FadeOut(mode_card),
            FadeOut(features_title),
            FadeOut(features),
            FadeOut(app_title),
            FadeOut(applications),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾"""
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
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 数字装饰
        numbers = VGroup(
            *[Text(str(i), font="Noto Sans CJK SC", font_size=40, color=self.COLOR_DATA) 
              for i in [2, 3, 5, 7, 9]]
        )
        
        positions = [
            LEFT * 3 + DOWN * 2,
            LEFT * 1.5 + DOWN * 2.5,
            ORIGIN + DOWN * 2,
            RIGHT * 1.5 + DOWN * 2.5,
            RIGHT * 3 + DOWN * 2
        ]
        
        for num, pos in zip(numbers, positions):
            num.move_to(pos)
        
        self.play(
            *[FadeIn(num, scale=0.5) for num in numbers],
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(numbers),
            run_time=1.0
        )
    
    def create_data_boxes(self, data, color=WHITE):
        """创建数据框"""
        boxes = VGroup()
        for value in data:
            box = VGroup(
                Square(side_length=0.6, fill_opacity=0.8, color=color, stroke_width=2, stroke_color=WHITE),
                Text(str(value), font="Noto Sans CJK SC", font_size=28, color=WHITE)
            )
            boxes.add(box)
        return boxes
    
    def create_concept_card(self, title_text, subtitle_text, description, color):
        """创建概念卡片"""
        # 背景
        bg = RoundedRectangle(
            width=3.5,
            height=2.5,
            corner_radius=0.2,
            fill_opacity=0.15,
            fill_color=color,
            stroke_width=3,
            stroke_color=color
        )
        
        # 标题
        title = Text(
            title_text,
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE,
            weight=BOLD
        ).move_to(bg.get_center() + UP * 0.6)
        
        # 副标题
        subtitle = Text(
            subtitle_text,
            font="Noto Sans CJK SC",
            font_size=20,
            color=color
        ).move_to(bg.get_center())
        
        # 描述
        desc = Text(
            description,
            font="Noto Sans CJK SC",
            font_size=16,
            color=GRAY_A
        ).move_to(bg.get_center() + DOWN * 0.6)
        
        return VGroup(bg, title, subtitle, desc)


# 运行命令:
# manim -pql median_mode.py MedianAndMode  # 快速预览
# manim -qh median_mode.py MedianAndMode   # 高质量渲染