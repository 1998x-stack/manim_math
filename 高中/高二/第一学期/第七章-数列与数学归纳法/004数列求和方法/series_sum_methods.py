"""
数列求和方法教学动画 - Series Sum Methods Teaching Animation
使用 Manim 0.19.2 创建的高二数学教学视频

内容: 数列求和的五种方法（重点：裂项相消、错位相减）
目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================

# TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ==================== 主场景类 ====================

class SeriesSumMethods(Scene):
    """
    数列求和方法教学动画主场景
    
    场景顺序:
    1. 开场钩子 (5-6秒)
    2. 方法概览 (8-10秒)
    3. 裂项相消法 - 原理 (15-18秒)
    4. 裂项相消法 - 求和 (18-22秒)
    5. 错位相减法 - 原理 (15-18秒)
    6. 错位相减法 - 求和 (18-22秒)
    7. 总结与技巧 (12-15秒)
    
    总时长: 约90-110秒
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_METHOD_1 = "#3498db"      # 蓝色 - 公式法
        self.COLOR_METHOD_2 = "#9b59b6"      # 紫色 - 分组求和
        self.COLOR_METHOD_3 = "#e74c3c"      # 红色 - 裂项相消（重点）
        self.COLOR_METHOD_4 = "#f39c12"      # 橙色 - 错位相减（重点）
        self.COLOR_METHOD_5 = "#2ecc71"      # 绿色 - 倒序相加
        self.COLOR_HIGHLIGHT = "#f1c40f"     # 黄色 - 高亮
        
        # 字体大小
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "formula": 26,
            "small": 18,
        }
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_split_principle()
        self.scene_4_split_summation()
        self.scene_5_stagger_principle()
        self.scene_6_stagger_summation()
        self.scene_7_summary()
    
    # ==================== Scene 1: 开场钩子 ====================
    
    def scene_1_opening(self):
        """开场钩子 - 引出5种求和方法"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子标题
        hook_title = Text(
            "数列求和难题",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        # 示例问题
        hook_problem = MathTex(
            r"S_n = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(UP * 4.2)
        
        question_mark = Text(
            "如何求和？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(Write(hook_title), run_time=0.7)
        self.play(Write(hook_problem), run_time=0.9)
        self.play(FadeIn(question_mark, shift=UP * 0.2), run_time=0.5)
        
        # 五种方法图标
        method_names = ["公式", "分组", "裂项", "错位", "倒序"]
        colors = [
            self.COLOR_METHOD_1,
            self.COLOR_METHOD_2,
            self.COLOR_METHOD_3,
            self.COLOR_METHOD_4,
            self.COLOR_METHOD_5
        ]
        
        icons = VGroup()
        for i, (name, color) in enumerate(zip(method_names, colors)):
            # 圆圈
            circle = Circle(radius=0.35, color=color, fill_opacity=0.3, stroke_width=3)
            # 文字
            text = Text(name, font="Noto Sans CJK SC", font_size=16, color=WHITE)
            
            icon = VGroup(circle, text)
            icons.add(icon)
        
        icons.arrange(RIGHT, buff=0.5).move_to(UP * 1)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], lag_ratio=0.2),
            run_time=1.5
        )
        
        # 强调重点方法（裂项和错位）
        self.play(
            Flash(icons[2], color=self.COLOR_METHOD_3, flash_radius=0.5),
            Flash(icons[3], color=self.COLOR_METHOD_4, flash_radius=0.5),
            icons[2].animate.scale(1.2),
            icons[3].animate.scale(1.2),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_title),
            FadeOut(hook_problem),
            FadeOut(question_mark),
            FadeOut(icons),
            run_time=0.5
        )
    
    # ==================== Scene 2: 方法概览 ====================
    
    def scene_2_overview(self):
        """方法概览 - 快速介绍5种方法"""
        # 标题
        title = Text(
            "五种求和方法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 五种方法列表
        methods_data = [
            ("①公式法", "等差/等比数列", self.COLOR_METHOD_1),
            ("②分组求和", "可拆分数列", self.COLOR_METHOD_2),
            ("③裂项相消", "分式数列", self.COLOR_METHOD_3),
            ("④错位相减", "等差×等比", self.COLOR_METHOD_4),
            ("⑤倒序相加", "对称数列", self.COLOR_METHOD_5),
        ]
        
        methods = VGroup()
        for i, (name, desc, color) in enumerate(methods_data):
            method_name = Text(
                name,
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"],
                color=color,
                weight=BOLD
            )
            
            method_desc = Text(
                f"- {desc}",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"] - 2,
                color=GRAY_A
            )
            
            method_group = VGroup(method_name, method_desc).arrange(RIGHT, buff=0.3)
            methods.add(method_group)
        
        methods.arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 2)
        
        # 依次显示
        for i, method in enumerate(methods):
            self.play(FadeIn(method, shift=RIGHT * 0.3), run_time=0.6)
            if i < len(methods) - 1:
                self.wait(0.3)
        
        self.wait(0.5)
        
        # 框选重点方法
        rect_3 = SurroundingRectangle(
            methods[2],
            color=self.COLOR_METHOD_3,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3
        )
        
        rect_4 = SurroundingRectangle(
            methods[3],
            color=self.COLOR_METHOD_4,
            buff=0.15,
            corner_radius=0.1,
            stroke_width=3
        )
        
        self.play(
            Create(rect_3),
            Create(rect_4),
            run_time=0.6
        )
        
        # 说明
        note = Text(
            "今天重点讲解 ③ 和 ④",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理非重点内容
        self.play(
            FadeOut(title),
            FadeOut(methods[0]),
            FadeOut(methods[1]),
            FadeOut(methods[4]),
            FadeOut(rect_3),
            FadeOut(rect_4),
            FadeOut(note),
            methods[2].animate.scale(0.5).move_to(UP * 7 + LEFT * 2.5),
            methods[3].animate.scale(0.5).move_to(UP * 7 + RIGHT * 2.5),
            run_time=0.6
        )
        
        # 保留作为参考
        self.method_3_ref = methods[2]
        self.method_4_ref = methods[3]
    
    # ==================== Scene 3: 裂项相消法 - 原理 ====================
    
    def scene_3_split_principle(self):
        """裂项相消法原理"""
        # 标题
        title = Text(
            "裂项相消法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_METHOD_3,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 问题
        problem = MathTex(
            r"S_n = \sum_{k=1}^{n} \frac{1}{k(k+1)}",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(UP * 4)
        
        self.play(Write(problem), run_time=0.9)
        
        # 关键公式
        key_formula = MathTex(
            r"\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}",
            font_size=self.FONT_SIZES["formula"] + 2,
            color=self.COLOR_METHOD_3
        ).move_to(UP * 2.5)
        
        self.play(Write(key_formula), run_time=1.0)
        
        # 强调
        self.play(
            key_formula.animate.scale(1.15),
            Flash(key_formula, color=self.COLOR_METHOD_3),
            run_time=0.6
        )
        
        self.wait(0.8)
        
        # 验证标题
        verify_title = Text(
            "验证：通分",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(verify_title, shift=DOWN * 0.2), run_time=0.5)
        
        # 右侧
        rhs = MathTex(
            r"\frac{1}{n} - \frac{1}{n+1}",
            font_size=self.FONT_SIZES["body"]
        ).move_to(ORIGIN)
        
        self.play(Write(rhs), run_time=0.7)
        
        # 通分
        common_denom = MathTex(
            r"= \frac{n+1 - n}{n(n+1)}",
            font_size=self.FONT_SIZES["body"]
        ).next_to(rhs, DOWN, buff=0.4)
        
        self.play(Write(common_denom), run_time=0.9)
        
        # 简化
        simplified = MathTex(
            r"= \frac{1}{n(n+1)}",
            font_size=self.FONT_SIZES["body"]
        ).next_to(common_denom, DOWN, buff=0.4)
        
        self.play(TransformMatchingTex(common_denom.copy(), simplified), run_time=0.8)
        
        # 对勾
        checkmark = MathTex(
            r"\checkmark",
            font_size=self.FONT_SIZES["subtitle"],
            color=GREEN
        ).next_to(simplified, RIGHT, buff=0.2)
        
        self.play(FadeIn(checkmark, scale=1.3), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理验证部分
        self.play(
            FadeOut(verify_title),
            FadeOut(rhs),
            FadeOut(common_denom),
            FadeOut(simplified),
            FadeOut(checkmark),
            run_time=0.5
        )
        
        # 缩小保留
        self.play(
            key_formula.animate.scale(1/1.15).scale(0.6).move_to(DOWN * 6.5 + LEFT * 2),
            run_time=0.4
        )
        
        self.key_formula_ref = key_formula
        
        # 保留标题但移到参考区
        self.play(
            title.animate.scale(0.5).move_to(UP * 6.5 + LEFT * 2),
            FadeOut(problem),
            run_time=0.4
        )
        
        self.split_title_ref = title
    
    # ==================== Scene 4: 裂项相消法 - 求和 ====================
    
    def scene_4_split_summation(self):
        """裂项相消求和过程"""
        # 问题回顾
        problem = MathTex(
            r"S_4 = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \frac{1}{4 \times 5}",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 5)
        
        self.play(Write(problem), run_time=1.2)
        
        self.wait(0.5)
        
        # 裂项标题
        split_title = Text(
            "裂项：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_METHOD_3,
            weight=BOLD
        ).move_to(UP * 3.5 + LEFT * 3.5)
        
        self.play(FadeIn(split_title), run_time=0.4)
        
        # 逐项裂项
        split_terms = [
            MathTex(r"\left(1 - \frac{1}{2}\right)", font_size=self.FONT_SIZES["body"]),
            MathTex(r"\left(\frac{1}{2} - \frac{1}{3}\right)", font_size=self.FONT_SIZES["body"]),
            MathTex(r"\left(\frac{1}{3} - \frac{1}{4}\right)", font_size=self.FONT_SIZES["body"]),
            MathTex(r"\left(\frac{1}{4} - \frac{1}{5}\right)", font_size=self.FONT_SIZES["body"]),
        ]
        
        # 排列
        split_group = VGroup(*split_terms).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        split_group.next_to(split_title, DOWN, buff=0.4, aligned_edge=LEFT)
        
        # 依次显示
        for term in split_terms:
            self.play(FadeIn(term, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)
        
        # 标注相消项（用颜色和删除线）
        # 第1项的-1/2 与 第2项的1/2 相消
        cancel_animations = []
        
        # 创建删除线
        lines = []
        
        # -1/2 (第1项的第2部分)
        target_1 = split_terms[0][0][2:5]  # -1/2
        # 1/2 (第2项的第1部分)
        target_2 = split_terms[1][0][1:4]  # 1/2
        
        line_1 = Line(
            target_1.get_left(),
            target_1.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        line_2 = Line(
            target_2.get_left(),
            target_2.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        
        # -1/3 (第2项的第2部分)
        target_3 = split_terms[1][0][5:8]
        # 1/3 (第3项的第1部分)
        target_4 = split_terms[2][0][1:4]
        
        line_3 = Line(
            target_3.get_left(),
            target_3.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        line_4 = Line(
            target_4.get_left(),
            target_4.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        
        # -1/4 (第3项的第2部分)
        target_5 = split_terms[2][0][5:8]
        # 1/4 (第4项的第1部分)
        target_6 = split_terms[3][0][1:4]
        
        line_5 = Line(
            target_5.get_left(),
            target_5.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        line_6 = Line(
            target_6.get_left(),
            target_6.get_right(),
            color=self.COLOR_METHOD_3,
            stroke_width=3
        )
        
        all_lines = VGroup(line_1, line_2, line_3, line_4, line_5, line_6)
        
        self.play(
            LaggedStart(*[Create(line) for line in all_lines], lag_ratio=0.2),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # 剩余项说明
        remaining_note = Text(
            "剩余：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5 + LEFT * 3.5)
        
        remaining_formula = MathTex(
            r"1 - \frac{1}{5}",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(remaining_note, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(remaining_note),
            Write(remaining_formula),
            run_time=0.8
        )
        
        # 最终结果
        result = MathTex(
            r"S_4 = 1 - \frac{1}{5} = \frac{4}{5}",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_METHOD_3
        ).move_to(DOWN * 3)
        
        self.play(Write(result), run_time=1.0)
        
        # 一般结果
        general_result = MathTex(
            r"S_n = 1 - \frac{1}{n+1} = \frac{n}{n+1}",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(general_result, shift=UP * 0.2), run_time=0.7)
        
        # 框选
        result_box = SurroundingRectangle(
            general_result,
            color=self.COLOR_METHOD_3,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(result_box), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(problem),
            FadeOut(split_title),
            FadeOut(split_group),
            FadeOut(all_lines),
            FadeOut(remaining_note),
            FadeOut(remaining_formula),
            FadeOut(result),
            FadeOut(result_box),
            general_result.animate.scale(0.6).move_to(DOWN * 6.5 + RIGHT * 2),
            run_time=0.6
        )
        
        self.general_split_ref = general_result
    
    # ==================== Scene 5: 错位相减法 - 原理 ====================
    
    def scene_5_stagger_principle(self):
        """错位相减法原理"""
        # 标题
        title = Text(
            "错位相减法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_METHOD_4,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 适用场景
        scenario = Text(
            "适用：等差数列 × 等比数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(scenario, shift=DOWN * 0.2), run_time=0.5)
        
        # 问题
        problem = MathTex(
            r"S_n = 1 \times 2 + 2 \times 2^2 + 3 \times 2^3 + 4 \times 2^4",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 3.5)
        
        self.play(Write(problem), run_time=1.2)
        
        # 方法说明
        method_note = Text(
            "方法：乘以公比q，然后相减",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_METHOD_4
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(method_note, shift=UP * 0.2), run_time=0.6)
        
        self.wait(0.5)
        
        # 写Sₙ
        S_n = MathTex(
            r"S_n &= 1 \times 2^1 + 2 \times 2^2 + 3 \times 2^3 + 4 \times 2^4",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 1)
        
        self.play(Write(S_n), run_time=1.0)
        
        # 写2Sₙ（错位）
        two_S_n = MathTex(
            r"2S_n &=     \phantom{0}1 \times 2^2 + 2 \times 2^3 + 3 \times 2^4 + 4 \times 2^5",
            font_size=self.FONT_SIZES["body"] - 2
        ).next_to(S_n, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(two_S_n), run_time=1.2)
        
        # 画竖线连接对应项（显示错位）
        # 简化版本：画几条示意线
        line_1 = DashedLine(
            S_n.get_center() + RIGHT * 1,
            two_S_n.get_center() + RIGHT * 0.2,
            color=self.COLOR_METHOD_4,
            dash_length=0.08,
            stroke_width=2
        )
        
        line_2 = DashedLine(
            S_n.get_center() + RIGHT * 2.5,
            two_S_n.get_center() + RIGHT * 1.7,
            color=self.COLOR_METHOD_4,
            dash_length=0.08,
            stroke_width=2
        )
        
        alignment_lines = VGroup(line_1, line_2)
        
        self.play(Create(alignment_lines), run_time=0.7)
        
        self.wait(0.8)
        
        # 相减说明
        subtract_note = MathTex(
            r"S_n - 2S_n = -S_n",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(subtract_note, shift=DOWN * 0.2), run_time=0.5)
        
        # 结果
        subtraction_result = MathTex(
            r"-S_n = 2 + 2^2 + 2^3 + 2^4 - 4 \times 2^5",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(DOWN * 2.8)
        
        self.play(Write(subtraction_result), run_time=1.2)
        
        # 简化说明
        simplified_note = Text(
            "前四项是等比数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 4.2)
        
        self.play(FadeIn(simplified_note, shift=UP * 0.2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(scenario),
            FadeOut(problem),
            FadeOut(method_note),
            FadeOut(S_n),
            FadeOut(two_S_n),
            FadeOut(alignment_lines),
            FadeOut(subtract_note),
            FadeOut(subtraction_result),
            FadeOut(simplified_note),
            title.animate.scale(0.5).move_to(UP * 6.5 + RIGHT * 2),
            run_time=0.6
        )
        
        self.stagger_title_ref = title
    
    # ==================== Scene 6: 错位相减法 - 求和 ====================
    
    def scene_6_stagger_summation(self):
        """错位相减求和计算"""
        # 回顾
        recap = MathTex(
            r"-S_n = 2 + 2^2 + 2^3 + 2^4 - 4 \times 2^5",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 5)
        
        self.play(FadeIn(recap, shift=DOWN * 0.2), run_time=0.7)
        
        # 等比数列求和
        geometric_part = MathTex(
            r"2 + 2^2 + 2^3 + 2^4",
            font_size=self.FONT_SIZES["body"]
        ).move_to(UP * 3.5)
        
        self.play(Write(geometric_part), run_time=0.8)
        
        # 公式框
        geometric_box = SurroundingRectangle(
            geometric_part,
            color=self.COLOR_METHOD_4,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(geometric_box), run_time=0.5)
        
        # 等比公式
        geometric_formula = MathTex(
            r"\text{(Geometric)} = \frac{2(2^4 - 1)}{2 - 1} = 2 \times 15 = 30",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 2.3)
        
        self.play(Write(geometric_formula), run_time=1.2)
        
        self.wait(0.8)
        
        # 继续计算
        continue_calc = MathTex(
            r"-S_n = 30 - 4 \times 32 = 30 - 128 = -98",
            font_size=self.FONT_SIZES["body"]
        ).move_to(UP * 0.8)
        
        self.play(Write(continue_calc), run_time=1.2)
        
        # 最终结果
        final_step = MathTex(
            r"\therefore \quad S_n = 98",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_METHOD_4
        ).move_to(DOWN * 0.5)
        
        self.play(Write(final_step), run_time=0.9)
        
        # 框选
        result_box = SurroundingRectangle(
            final_step,
            color=self.COLOR_METHOD_4,
            buff=0.2,
            corner_radius=0.1,
            stroke_width=3
        )
        
        self.play(Create(result_box), run_time=0.5)
        
        self.wait(1.0)
        
        # 一般公式
        general_formula = MathTex(
            r"S_n = (n-1) \cdot q^{n+1} + 1",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        general_note = Text(
            "（当等差首项为1，公差为1时）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).next_to(general_formula, DOWN, buff=0.2)
        
        self.play(
            FadeIn(general_formula, shift=UP * 0.2),
            FadeIn(general_note, shift=UP * 0.2),
            run_time=0.8
        )
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(recap),
            FadeOut(geometric_part),
            FadeOut(geometric_box),
            FadeOut(geometric_formula),
            FadeOut(continue_calc),
            FadeOut(final_step),
            FadeOut(result_box),
            FadeOut(general_note),
            general_formula.animate.scale(0.6).move_to(DOWN * 6 + RIGHT * 2),
            run_time=0.6
        )
        
        self.general_stagger_ref = general_formula
    
    # ==================== Scene 7: 总结与技巧 ====================
    
    def scene_7_summary(self):
        """总结与选择技巧"""
        # 标题
        title = Text(
            "方法选择技巧",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 技巧列表
        tips = [
            "①看通项结构特点",
            "②分式→裂项相消",
            "③等差×等比→错位相减",
            "④对称性→倒序相加",
            "⑤可拆分→分组求和",
        ]
        
        tip_group = VGroup()
        for tip in tips:
            tip_text = Text(
                tip,
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"] - 2,
                color=WHITE
            )
            tip_group.add(tip_text)
        
        tip_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 2.5)
        
        # 依次显示
        for tip in tip_group:
            self.play(FadeIn(tip, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)
        
        # 重点提示
        highlight_note = Text(
            "多练习，熟能生巧！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeIn(highlight_note, scale=1.2),
            Flash(highlight_note, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理参考公式
        refs_to_clear = [
            self.method_3_ref if hasattr(self, 'method_3_ref') else None,
            self.method_4_ref if hasattr(self, 'method_4_ref') else None,
            self.split_title_ref if hasattr(self, 'split_title_ref') else None,
            self.key_formula_ref if hasattr(self, 'key_formula_ref') else None,
            self.general_split_ref if hasattr(self, 'general_split_ref') else None,
            self.stagger_title_ref if hasattr(self, 'stagger_title_ref') else None,
            self.general_stagger_ref if hasattr(self, 'general_stagger_ref') else None,
        ]
        refs_to_clear = [r for r in refs_to_clear if r is not None]
        
        self.play(
            FadeOut(title),
            FadeOut(tip_group),
            FadeOut(highlight_note),
            *[FadeOut(ref) for ref in refs_to_clear],
            run_time=0.5
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握更多求和技巧！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 点赞图标
        like_icon = Star(
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.8,
            stroke_width=2
        ).scale(0.6).move_to(DOWN * 4)
        
        self.play(
            FadeIn(like_icon, scale=0.5),
            run_time=0.4
        )
        
        self.play(
            Flash(like_icon, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            like_icon.animate.scale(1.3),
            run_time=0.5
        )
        
        self.play(like_icon.animate.scale(1/1.3), run_time=0.3)
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(like_icon),
            run_time=1.0
        )


# ==================== 渲染入口 ====================

if __name__ == "__main__":
    # 使用以下命令渲染:
    # 快速预览: manim -pql series_sum_methods.py SeriesSumMethods
    # 高质量: manim -qh series_sum_methods.py SeriesSumMethods
    # 4K质量: manim -qk series_sum_methods.py SeriesSumMethods
    pass