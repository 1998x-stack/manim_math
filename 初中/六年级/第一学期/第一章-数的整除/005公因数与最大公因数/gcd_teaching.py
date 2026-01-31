"""
最大公因数 (Greatest Common Divisor) 教学动画
使用 Manim 创建的小学数学教学视频

内容: 公因数与最大公因数的概念，短除法求解
目标观众: 六年级学生
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


class GCDTeaching(Scene):
    """
    最大公因数教学动画场景
    
    场景顺序:
    1. 开场钩子 - 提出问题
    2. 因数概念回顾
    3. 公因数展示 - Venn图
    4. 最大公因数概念
    5. 短除法演示
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 数字12
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 数字18
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_COMMON = "#2ecc71"       # 绿色 - 公因数
        self.COLOR_GCD = GOLD               # 金色 - 最大公因数
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_positions()
        
        # 执行动画序列
        self.show_opening()
        self.show_factors_review()
        self.show_common_factors_venn()
        self.show_gcd_concept()
        self.show_short_division()
        self.show_outro()
    
    def setup_positions(self):
        """初始化所有位置常量"""
        # Scene 1 & 2 位置
        self.pos_12_initial = UP * 3 + LEFT * 2
        self.pos_18_initial = UP * 3 + RIGHT * 2
        self.pos_12_left = UP * 3 + LEFT * 3
        self.pos_18_right = UP * 3 + RIGHT * 3
        
        # Venn图位置
        self.venn_left = LEFT * 1.5 + UP * 0.5
        self.venn_right = RIGHT * 1.5 + UP * 0.5
        self.venn_radius = 1.8
        
        # 短除法位置
        self.division_top = UP * 4
        self.row_spacing = 1.2
        self.col_spacing = 1.5
        
        # 数据
        self.factors_12 = [1, 2, 3, 4, 6, 12]
        self.factors_18 = [1, 2, 3, 6, 9, 18]
        self.common_factors = [1, 2, 3, 6]
        self.unique_12 = [4, 12]
        self.unique_18 = [9, 18]
    
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
        hook_text = Text(
            "12和18有什么共同点?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 数字12和18
        num_12 = Text(
            "12",
            font="Noto Sans CJK SC",
            font_size=72,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(self.pos_12_initial)
        
        num_18 = Text(
            "18",
            font="Noto Sans CJK SC",
            font_size=72,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(self.pos_18_initial)
        
        self.play(FadeIn(num_12, scale=0.5), run_time=0.4)
        self.play(FadeIn(num_18, scale=0.5), run_time=0.4)
        
        # 闪烁高亮
        self.play(
            Flash(num_12, color=self.COLOR_PRIMARY, flash_radius=0.8),
            Flash(num_18, color=self.COLOR_SECONDARY, flash_radius=0.8),
            run_time=0.5
        )
        
        # 问题文字
        question = Text(
            "它们的最大公因数是多少?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.9)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            run_time=0.4
        )
        
        # 保存数字对象供后续使用
        self.num_12 = num_12
        self.num_18 = num_18
    
    def show_factors_review(self):
        """场景2: 因数概念回顾"""
        # 标题
        title = Text(
            "什么是因数?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        definition = Text(
            "能整除一个数的数叫做它的因数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(definition), run_time=0.5)
        
        # 数字移动到左右两侧
        self.play(
            self.num_12.animate.move_to(self.pos_12_left),
            self.num_18.animate.move_to(self.pos_18_right),
            run_time=0.6
        )
        
        # 12的因数标签
        label_12 = Text(
            "12的因数:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(self.num_12, DOWN, buff=0.5)
        
        # 创建12的因数
        factors_12_group = VGroup()
        for i, factor in enumerate(self.factors_12):
            f_text = Text(
                str(factor),
                font="Noto Sans CJK SC",
                font_size=28,
                color=self.COLOR_PRIMARY
            )
            factors_12_group.add(f_text)
        
        # 水平排列
        factors_12_group.arrange(RIGHT, buff=0.3)
        factors_12_group.next_to(label_12, DOWN, buff=0.3)
        
        # 逐个出现
        self.play(FadeIn(label_12), run_time=0.3)
        self.play(
            LaggedStart(*[FadeIn(f, shift=DOWN * 0.2) for f in factors_12_group], lag_ratio=0.15),
            run_time=1.5
        )
        
        # 18的因数标签
        label_18 = Text(
            "18的因数:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(self.num_18, DOWN, buff=0.5)
        
        # 创建18的因数
        factors_18_group = VGroup()
        for factor in self.factors_18:
            f_text = Text(
                str(factor),
                font="Noto Sans CJK SC",
                font_size=28,
                color=self.COLOR_SECONDARY
            )
            factors_18_group.add(f_text)
        
        # 水平排列
        factors_18_group.arrange(RIGHT, buff=0.3)
        factors_18_group.next_to(label_18, DOWN, buff=0.3)
        
        # 逐个出现
        self.play(FadeIn(label_18), run_time=0.3)
        self.play(
            LaggedStart(*[FadeIn(f, shift=DOWN * 0.2) for f in factors_18_group], lag_ratio=0.15),
            run_time=1.5
        )
        
        # 说明文字
        explanation = Text(
            "找出它们共有的因数!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)
        
        # 保存因数组供后续使用
        self.factors_12_group = factors_12_group
        self.factors_18_group = factors_18_group
        self.label_12 = label_12
        self.label_18 = label_18
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explanation),
            run_time=0.4
        )
    
    def show_common_factors_venn(self):
        """场景3: 公因数展示 - Venn图"""
        # 标题
        title = Text(
            "公因数",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_COMMON,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "两个数共有的因数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)
        
        # 移动数字到Venn图上方
        self.play(
            self.num_12.animate.scale(0.6).move_to(self.venn_left + UP * 2.5),
            self.num_18.animate.scale(0.6).move_to(self.venn_right + UP * 2.5),
            FadeOut(self.label_12),
            FadeOut(self.label_18),
            run_time=0.6
        )
        
        # 创建Venn图圆
        circle_12 = Circle(
            radius=self.venn_radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=self.COLOR_PRIMARY
        ).move_to(self.venn_left)
        
        circle_18 = Circle(
            radius=self.venn_radius,
            color=self.COLOR_SECONDARY,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=self.COLOR_SECONDARY
        ).move_to(self.venn_right)
        
        self.play(Create(circle_12), run_time=0.8)
        self.play(Create(circle_18), run_time=0.8)
        
        # 圆标签
        label_12_venn = Text(
            "12",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_PRIMARY
        ).move_to(self.venn_left + UP * (self.venn_radius + 0.4))
        
        label_18_venn = Text(
            "18",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(self.venn_right + UP * (self.venn_radius + 0.4))
        
        self.play(FadeIn(label_12_venn), FadeIn(label_18_venn), run_time=0.3)
        
        # 移动因数到Venn图
        # 12的独有因数: 4, 12
        unique_12_group = VGroup()
        for i, val in enumerate(self.unique_12):
            # 找到对应的文本对象
            for f in self.factors_12_group:
                if f.text == str(val):
                    unique_12_group.add(f)
                    break
        
        # 定位在左圆
        unique_12_group.arrange(DOWN, buff=0.3)
        unique_12_group.move_to(self.venn_left + LEFT * 0.8)
        
        # 18的独有因数: 9, 18
        unique_18_group = VGroup()
        for val in self.unique_18:
            for f in self.factors_18_group:
                if f.text == str(val):
                    unique_18_group.add(f)
                    break
        
        unique_18_group.arrange(DOWN, buff=0.3)
        unique_18_group.move_to(self.venn_right + RIGHT * 0.8)
        
        # 公因数: 1, 2, 3, 6
        common_group = VGroup()
        for val in self.common_factors:
            # 从12的因数中取一个
            for f in self.factors_12_group:
                if f.text == str(val) and f not in unique_12_group:
                    common_group.add(f)
                    break
        
        # 定位在交集
        common_group.arrange(DOWN, buff=0.25)
        intersection_center = (self.venn_left + self.venn_right) / 2
        common_group.move_to(intersection_center)
        
        # 移除18的因数（因为我们只需要一份公因数）
        factors_18_to_remove = VGroup()
        for f in self.factors_18_group:
            if f not in unique_18_group:
                factors_18_to_remove.add(f)
        
        # 动画: 移动到各自区域
        self.play(
            *[f.animate.move_to(unique_12_group[i].get_center()) 
              for i, f in enumerate(unique_12_group)],
            run_time=1.0
        )
        
        self.play(
            *[f.animate.move_to(unique_18_group[i].get_center()) 
              for i, f in enumerate(unique_18_group)],
            FadeOut(factors_18_to_remove),
            run_time=1.0
        )
        
        self.play(
            *[f.animate.move_to(common_group[i].get_center()).set_color(self.COLOR_COMMON) 
              for i, f in enumerate(common_group)],
            run_time=1.2
        )
        
        # 高亮交集区域
        # 创建交集形状 (使用Intersection)
        intersection = Intersection(circle_12, circle_18, 
                                   fill_color=self.COLOR_COMMON, 
                                   fill_opacity=0.3,
                                   stroke_width=0)
        
        self.play(FadeIn(intersection), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "公因数: 1, 2, 3, 6",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_COMMON,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 圈出公因数
        highlight_box = SurroundingRectangle(
            common_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Create(highlight_box), run_time=0.6)
        self.wait(1.5)
        
        # 保存公因数组
        self.common_group = common_group
        
        # 清理
        self.play(
            FadeOut(circle_12),
            FadeOut(circle_18),
            FadeOut(label_12_venn),
            FadeOut(label_18_venn),
            FadeOut(unique_12_group),
            FadeOut(unique_18_group),
            FadeOut(intersection),
            FadeOut(highlight_box),
            FadeOut(self.num_12),
            FadeOut(self.num_18),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 将标题变换
        self.venn_title = title
        self.venn_subtitle = subtitle
    
    def show_gcd_concept(self):
        """场景4: 最大公因数概念"""
        # 标题变换
        new_title = Text(
            "最大公因数",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_GCD,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        new_subtitle = Text(
            "Greatest Common Divisor (GCD)",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(
            Transform(self.venn_title, new_title),
            Transform(self.venn_subtitle, new_subtitle),
            run_time=0.6
        )
        
        # 公因数水平排列到中央
        self.common_group.generate_target()
        self.common_group.target.arrange(RIGHT, buff=0.5)
        self.common_group.target.move_to(UP * 2)
        
        self.play(MoveToTarget(self.common_group), run_time=0.8)
        
        # 逐个淡入（重新强调）
        for f in self.common_group:
            self.play(
                f.animate.scale(1.2).set_color(self.COLOR_COMMON),
                run_time=0.2
            )
            self.play(f.animate.scale(1/1.2), run_time=0.1)
        
        # "最大"文字强调
        max_text = Text(
            "最大的公因数",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(max_text, scale=1.2), run_time=0.5)
        
        # 找到数字6
        num_6 = None
        for f in self.common_group:
            if f.text == "6":
                num_6 = f
                break
        
        # 6放大并变金色
        self.play(
            num_6.animate.scale(1.5).set_color(self.COLOR_GCD),
            run_time=0.8
        )
        
        # 其他数字变暗
        others = VGroup(*[f for f in self.common_group if f != num_6])
        self.play(others.animate.set_opacity(0.3), run_time=0.4)
        
        # 公式书写
        gcd_formula = MathTex(
            r"\gcd(12, 18) = 6",
            font_size=36,
            color=WHITE
        ).move_to(ORIGIN)
        
        # 设置颜色
        gcd_formula.set_color_by_tex("6", self.COLOR_GCD)
        
        self.play(Write(gcd_formula), run_time=1.0)
        
        # 箭头指向6
        arrow = Arrow(
            gcd_formula.get_right() + RIGHT * 0.3,
            num_6.get_center(),
            color=self.COLOR_GCD,
            buff=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 结论文字
        conclusion = Text(
            "12和18的最大公因数是6",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(conclusion), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(self.venn_title),
            FadeOut(self.venn_subtitle),
            FadeOut(max_text),
            FadeOut(self.common_group),
            FadeOut(gcd_formula),
            FadeOut(arrow),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_short_division(self):
        """场景5: 短除法演示"""
        # 标题
        title = Text(
            "短除法求最大公因数",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 7)
        
        instruction = Text(
            "用公因数连续除，直到互质",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 6.3)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(instruction), run_time=0.5)
        
        # 初始数字
        num_12_text = Text("12", font="Noto Sans CJK SC", font_size=36, 
                          color=self.COLOR_PRIMARY)
        num_18_text = Text("18", font="Noto Sans CJK SC", font_size=36, 
                          color=self.COLOR_SECONDARY)
        
        # 位置
        num_12_pos = self.division_top + LEFT * 0.8
        num_18_pos = self.division_top + RIGHT * 0.8
        
        num_12_text.move_to(num_12_pos)
        num_18_text.move_to(num_18_pos)
        
        # 绘制框架
        frame_width = 4
        frame_height = 4.5
        division_frame = Rectangle(
            width=frame_width,
            height=frame_height,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).move_to(self.division_top + DOWN * (frame_height/2 - 0.3))
        
        self.play(Create(division_frame), run_time=0.6)
        self.play(Write(num_12_text), Write(num_18_text), run_time=0.6)
        
        # 步骤1: 除以2
        step1_text = Text(
            "步骤1: 找公因数2",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(step1_text), run_time=0.5)
        
        # 除数2
        divisor_2 = Text(
            "2",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_GCD
        ).move_to(self.division_top + LEFT * 2.5)
        
        self.play(FadeIn(divisor_2, shift=LEFT * 0.3), run_time=0.5)
        
        # 横线1
        h_line_1 = Line(
            self.division_top + LEFT * 2 + DOWN * 0.4,
            self.division_top + RIGHT * 2 + DOWN * 0.4,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        self.play(Create(h_line_1), run_time=0.4)
        
        # 计算结果
        result_6 = Text("6", font="Noto Sans CJK SC", font_size=36, 
                       color=self.COLOR_PRIMARY)
        result_9 = Text("9", font="Noto Sans CJK SC", font_size=36, 
                       color=self.COLOR_SECONDARY)
        
        result_6_pos = num_12_pos + DOWN * self.row_spacing
        result_9_pos = num_18_pos + DOWN * self.row_spacing
        
        result_6.move_to(result_6_pos)
        result_9.move_to(result_9_pos)
        
        self.play(Write(result_6), run_time=0.6)
        self.play(Write(result_9), run_time=0.6)
        
        # 步骤2: 除以3
        step2_text = Text(
            "步骤2: 找公因数3",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeIn(step2_text),
            FadeOut(step1_text),
            run_time=0.5
        )
        
        # 除数3
        divisor_3 = Text(
            "3",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_GCD
        ).move_to(divisor_2.get_center() + DOWN * self.row_spacing)
        
        self.play(FadeIn(divisor_3, shift=LEFT * 0.3), run_time=0.5)
        
        # 横线2
        h_line_2 = Line(
            h_line_1.get_start() + DOWN * self.row_spacing,
            h_line_1.get_end() + DOWN * self.row_spacing,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        self.play(Create(h_line_2), run_time=0.4)
        
        # 最终结果
        final_2 = Text("2", font="Noto Sans CJK SC", font_size=36, 
                      color=self.COLOR_PRIMARY)
        final_3 = Text("3", font="Noto Sans CJK SC", font_size=36, 
                      color=self.COLOR_SECONDARY)
        
        final_2_pos = result_6_pos + DOWN * self.row_spacing
        final_3_pos = result_9_pos + DOWN * self.row_spacing
        
        final_2.move_to(final_2_pos)
        final_3.move_to(final_3_pos)
        
        self.play(Write(final_2), run_time=0.6)
        self.play(Write(final_3), run_time=0.6)
        
        # 互质说明
        coprime_text = Text(
            "2和3互质，停止",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeIn(coprime_text),
            FadeOut(step2_text),
            run_time=0.5
        )
        
        # 圈出公因数
        highlight_2 = Circle(
            radius=0.35,
            color=self.COLOR_GCD,
            stroke_width=3
        ).move_to(divisor_2)
        
        highlight_3 = Circle(
            radius=0.35,
            color=self.COLOR_GCD,
            stroke_width=3
        ).move_to(divisor_3)
        
        self.play(
            Create(highlight_2),
            Create(highlight_3),
            run_time=0.8
        )
        
        # 乘法公式
        multiply_formula = MathTex(
            r"\text{GCD} = 2 \times 3",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(multiply_formula), run_time=1.0)
        
        # 计算过程
        calculation = MathTex(
            r"= 6",
            font_size=32,
            color=self.COLOR_GCD
        ).next_to(multiply_formula, RIGHT, buff=0.3)
        
        self.play(Write(calculation), run_time=1.2)
        
        # 答案高亮
        answer = VGroup(multiply_formula, calculation)
        self.play(
            answer.animate.scale(1.3).set_color(self.COLOR_GCD),
            run_time=0.6
        )
        
        # 庆祝动画
        self.play(
            Flash(answer, color=self.COLOR_GCD, flash_radius=1.0),
            run_time=0.5
        )
        
        # 最终答案文字
        final_answer = Text(
            "所以 gcd(12, 18) = 6",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_GCD,
            weight=BOLD
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(final_answer, shift=UP * 0.3), run_time=0.5)
        
        self.wait(4.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(instruction),
            FadeOut(division_frame),
            FadeOut(num_12_text),
            FadeOut(num_18_text),
            FadeOut(divisor_2),
            FadeOut(divisor_3),
            FadeOut(h_line_1),
            FadeOut(h_line_2),
            FadeOut(result_6),
            FadeOut(result_9),
            FadeOut(final_2),
            FadeOut(final_3),
            FadeOut(highlight_2),
            FadeOut(highlight_3),
            FadeOut(coprime_text),
            FadeOut(answer),
            FadeOut(final_answer),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景6: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "知识点总结",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 总结卡片
        cards = VGroup()
        
        # 卡片1
        icon_1 = Circle(radius=0.2, fill_color=self.COLOR_COMMON, 
                       fill_opacity=1, stroke_width=0)
        text_1 = Text(
            "公因数: 两个数共有的因数",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_1 = VGroup(icon_1, text_1).arrange(RIGHT, buff=0.3)
        card_1.move_to(UP * 3)
        cards.add(card_1)
        
        # 卡片2
        icon_2 = Circle(radius=0.2, fill_color=self.COLOR_GCD, 
                       fill_opacity=1, stroke_width=0)
        text_2 = Text(
            "最大公因数: 公因数中最大的",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_2 = VGroup(icon_2, text_2).arrange(RIGHT, buff=0.3)
        card_2.move_to(UP * 2)
        cards.add(card_2)
        
        # 卡片3
        icon_3 = Circle(radius=0.2, fill_color=self.COLOR_HIGHLIGHT, 
                       fill_opacity=1, stroke_width=0)
        text_3 = Text(
            "短除法: 公因数连除再相乘",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_3 = VGroup(icon_3, text_3).arrange(RIGHT, buff=0.3)
        card_3.move_to(UP * 1)
        cards.add(card_3)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 示例回顾
        example_recap = VGroup(
            Text("示例:", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            MathTex(r"\gcd(12, 18) = 2 \times 3 = 6", font_size=28, color=self.COLOR_GCD)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.5)
        
        self.play(FadeIn(example_recap), run_time=0.6)
        self.wait(0.8)
        
        # 淡出总结
        summary_group = VGroup(summary_title, cards, example_recap)
        self.play(FadeOut(summary_group), run_time=0.5)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.5)
        
        # 装饰图标
        icons = VGroup(*[
            Circle(radius=0.25, color=self.COLOR_GCD, fill_opacity=0.8)
            .shift(2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ]).move_to(follow_text.get_center() + DOWN * 1.5)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], lag_ratio=0.1),
            run_time=0.8
        )
        
        self.wait(0.6)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql gcd_teaching.py GCDTeaching  # 快速预览
# manim -qh gcd_teaching.py GCDTeaching   # 高质量渲染