"""
因数与倍数 - Factors and Multiples Animation
使用 Manim 创建的六年级数学教学视频

内容: 因数与倍数的定义、性质和特殊规律
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


class FactorsAndMultiples(Scene):
    """
    因数与倍数教学动画场景
    
    场景顺序:
    1. 开场引入
    2. 因数与倍数定义
    3. 找因数 - 有限性
    4. 找倍数 - 无限性
    5. 特殊规律
    6. 总结与巩固
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要概念
        self.COLOR_FACTOR = "#e74c3c"        # 红色 - 因数
        self.COLOR_MULTIPLE = "#2ecc71"      # 绿色 - 倍数
        self.COLOR_HIGHLIGHT = "#f39c12"     # 橙色 - 高亮
        self.COLOR_SPECIAL = "#9b59b6"       # 紫色 - 特殊
        self.COLOR_AUXILIARY = "#95a5a6"     # 灰色 - 辅助
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_FORMULA = 32
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_find_factors()
        self.show_find_multiples()
        self.show_special_rules()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场引入 (4-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "12个糖果，可以平均分给几个人？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 糖果图标（用圆点代替）
        candy_group = VGroup()
        for i in range(12):
            row = i // 6
            col = i % 6
            candy = Circle(
                radius=0.15,
                fill_color=GOLD,
                fill_opacity=1,
                stroke_color=YELLOW,
                stroke_width=2
            ).move_to(np.array([col * 0.6 - 1.5, 3 - row * 0.6, 0]))
            candy_group.add(candy)
        
        self.play(FadeIn(candy_group, scale=0.5), run_time=0.8)
        self.wait(0.5)
        
        # 分组示意 - 分成3组
        hint = Text(
            "可以分成：2人、3人、4人、6人...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 1)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(candy_group),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 因数与倍数定义 (8-10秒)"""
        # 标题
        title = Text(
            "因数与倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 定义公式
        if_text = Text(
            "如果",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4 + LEFT * 3)
        
        formula = MathTex(
            r"a = b \times q",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).next_to(if_text, RIGHT, buff=0.3)
        
        condition = Text(
            "(q为正整数)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(formula, RIGHT, buff=0.2)
        
        def_group1 = VGroup(if_text, formula, condition)
        
        self.play(Write(def_group1), run_time=1.0)
        
        # 则的说明
        then_text = Text(
            "则：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 2.5 + LEFT * 3.5)
        
        factor_def = Text(
            "b 是 a 的因数（约数）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FACTOR
        ).next_to(then_text, RIGHT, buff=0.3)
        
        multiple_def = Text(
            "a 是 b 的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_MULTIPLE
        ).move_to(UP * 1.5 + LEFT * 0.5)
        
        self.play(FadeIn(then_text), run_time=0.3)
        self.play(FadeIn(factor_def, shift=LEFT * 0.2), run_time=0.5)
        self.play(Indicate(factor_def, color=self.COLOR_FACTOR), run_time=0.6)
        
        self.play(FadeIn(multiple_def, shift=LEFT * 0.2), run_time=0.5)
        self.play(Indicate(multiple_def, color=self.COLOR_MULTIPLE), run_time=0.6)
        
        # 具体例子
        example_title = Text(
            "例如：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(ORIGIN + LEFT * 3.2)
        
        example_formula = MathTex(
            r"12 = 3 \times 4",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).next_to(example_title, RIGHT, buff=0.3)
        
        example_group = VGroup(example_title, example_formula)
        
        self.play(FadeIn(example_group, shift=UP * 0.2), run_time=0.6)
        
        # 标注关系
        arrow1 = Arrow(
            start=example_formula.get_bottom() + LEFT * 0.5,
            end=example_formula.get_bottom() + LEFT * 0.5 + DOWN * 0.8,
            color=self.COLOR_MULTIPLE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        label1 = Text(
            "倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_MULTIPLE
        ).next_to(arrow1, DOWN, buff=0.1)
        
        arrow2 = Arrow(
            start=example_formula.get_bottom(),
            end=example_formula.get_bottom() + DOWN * 0.8,
            color=self.COLOR_FACTOR,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        label2 = Text(
            "因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_FACTOR
        ).next_to(arrow2, DOWN, buff=0.1)
        
        arrow3 = Arrow(
            start=example_formula.get_bottom() + RIGHT * 0.5,
            end=example_formula.get_bottom() + RIGHT * 0.5 + DOWN * 0.8,
            color=self.COLOR_FACTOR,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        label3 = Text(
            "因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_FACTOR
        ).next_to(arrow3, DOWN, buff=0.1)
        
        self.play(
            GrowArrow(arrow1),
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            run_time=0.6
        )
        self.play(
            FadeIn(label1),
            FadeIn(label2),
            FadeIn(label3),
            run_time=0.4
        )
        
        # 强调相互依存
        note = Text(
            "因数和倍数是相互依存的关系",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_group1),
            FadeOut(then_text),
            FadeOut(factor_def),
            FadeOut(multiple_def),
            FadeOut(example_group),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(label3),
            FadeOut(note),
            run_time=0.5
        )
    
    def show_find_factors(self):
        """场景3: 找因数 - 有限性 (12-15秒)"""
        # 标题
        title = Text(
            "找12的所有因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_FACTOR
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 方法说明
        method = Text(
            "方法：从1到12逐个检查",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(method), run_time=0.5)
        
        # 检查过程
        check_y = 3
        factors_found = []
        
        # 检查1-12
        checks = [
            (1, True, "12÷1=12"),
            (2, True, "12÷2=6"),
            (3, True, "12÷3=4"),
            (4, True, "12÷4=3"),
            (5, False, "12÷5=?"),
            (6, True, "12÷6=2"),
        ]
        
        for num, is_factor, expr in checks:
            # 显示检查
            check_text = Text(
                expr,
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ).move_to(UP * check_y + LEFT * 2)
            
            result = Text(
                "✓" if is_factor else "✗",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=self.COLOR_FACTOR if is_factor else GRAY
            ).next_to(check_text, RIGHT, buff=0.5)
            
            if is_factor:
                label = Text(
                    f"{num}是因数",
                    font="Noto Sans CJK SC",
                    font_size=self.FONT_SMALL,
                    color=self.COLOR_FACTOR
                ).next_to(result, RIGHT, buff=0.3)
                factors_found.append(num)
            else:
                label = Text(
                    "不是因数",
                    font="Noto Sans CJK SC",
                    font_size=self.FONT_SMALL,
                    color=GRAY
                ).next_to(result, RIGHT, buff=0.3)
            
            check_group = VGroup(check_text, result, label)
            
            self.play(FadeIn(check_group, shift=LEFT * 0.2), run_time=0.4)
            
            if num <= 4:  # 只显示前几个
                check_y -= 0.8
            else:
                # 快速淡出前面的，显示后面的
                self.play(FadeOut(check_group), run_time=0.2)
                if num == 5:
                    dots_text = Text(
                        "...",
                        font="Noto Sans CJK SC",
                        font_size=self.FONT_BODY,
                        color=GRAY_A
                    ).move_to(UP * check_y)
                    self.play(FadeIn(dots_text), run_time=0.3)
                    self.wait(0.3)
                    self.play(FadeOut(dots_text), run_time=0.2)
        
        # 结果表格
        result_title = Text(
            "12的所有因数：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FACTOR
        ).move_to(UP * 0.5)
        
        factors_text = MathTex(
            r"1, 2, 3, 4, 6, 12",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_FACTOR
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(result_title), run_time=0.5)
        self.play(FadeIn(factors_text, scale=1.1), run_time=0.6)
        
        # 框选强调
        box = SurroundingRectangle(
            factors_text,
            color=self.COLOR_FACTOR,
            buff=0.2,
            corner_radius=0.1
        )
        self.play(Create(box), run_time=0.5)
        
        # 强调有限性
        finite_note = Text(
            "共6个（有限的）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(finite_note, shift=UP * 0.2), run_time=0.6)
        self.play(Flash(finite_note, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        conclusion = Text(
            "一个数的因数是有限的",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(conclusion), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(method),
            FadeOut(result_title),
            FadeOut(factors_text),
            FadeOut(box),
            FadeOut(finite_note),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_find_multiples(self):
        """场景4: 找倍数 - 无限性 (12-15秒)"""
        # 标题
        title = Text(
            "找3的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_MULTIPLE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式提示
        formulas = VGroup(
            MathTex(r"3 \times 1 = 3", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"3 \times 2 = 6", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"3 \times 3 = 9", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"3 \times 4 = 12", font_size=self.FONT_BODY, color=WHITE),
            Text("...", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=GRAY_A)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 3 + LEFT * 2)
        
        self.play(FadeIn(formulas, shift=RIGHT * 0.3), run_time=1.0)
        
        # 数轴展示
        number_line = NumberLine(
            x_range=[0, 21, 3],
            length=7,
            include_numbers=True,
            font_size=20,
            label_direction=DOWN
        ).move_to(UP * 0.5)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 标记倍数
        multiples = [3, 6, 9, 12, 15, 18]
        dots = VGroup()
        
        for m in multiples:
            dot = Dot(
                number_line.n2p(m),
                color=self.COLOR_MULTIPLE,
                radius=0.12
            )
            dots.add(dot)
        
        self.play(FadeIn(dots, scale=0.5, lag_ratio=0.2), run_time=1.5)
        
        # 延伸箭头
        arrow = Arrow(
            start=number_line.get_right(),
            end=number_line.get_right() + RIGHT * 1.5,
            color=self.COLOR_MULTIPLE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        ellipsis = Text(
            "...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_MULTIPLE
        ).next_to(arrow, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(ellipsis), run_time=0.4)
        
        # 强调无限性
        infinite_note = Text(
            "永远写不完（无限的）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(infinite_note, shift=UP * 0.2), run_time=0.6)
        self.play(Flash(infinite_note, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        conclusion = Text(
            "一个数的倍数是无限的",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(conclusion), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formulas),
            FadeOut(number_line),
            FadeOut(dots),
            FadeOut(arrow),
            FadeOut(ellipsis),
            FadeOut(infinite_note),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def show_special_rules(self):
        """场景5: 特殊规律 (10-12秒)"""
        # 标题
        title = Text(
            "特殊规律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SPECIAL
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 规律1
        rule1_title = Text(
            "规律①：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5 + LEFT * 3)
        
        rule1_content = Text(
            "1 是所有正整数的因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FACTOR
        ).next_to(rule1_title, RIGHT, buff=0.3)
        
        rule1_box = SurroundingRectangle(
            VGroup(rule1_title, rule1_content),
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        rule1_group = VGroup(rule1_box, rule1_title, rule1_content)
        
        self.play(FadeIn(rule1_group, shift=LEFT * 0.3), run_time=0.7)
        
        # 示例1
        examples1 = VGroup(
            MathTex(r"1 \times 5 = 5", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"1 \times 12 = 12", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"1 \times 99 = 99", font_size=self.FONT_BODY, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(UP * 1.5 + LEFT * 1)
        
        self.play(FadeIn(examples1, shift=RIGHT * 0.2, lag_ratio=0.3), run_time=1.0)
        
        # 高亮1
        for example in examples1:
            self.play(Indicate(example, scale_factor=1.1), run_time=0.4)
        
        # 规律2
        rule2_title = Text(
            "规律②：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1 + LEFT * 2.5)
        
        rule2_content = Text(
            "0 是所有非零整数的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_MULTIPLE
        ).next_to(rule2_title, RIGHT, buff=0.3)
        
        rule2_box = SurroundingRectangle(
            VGroup(rule2_title, rule2_content),
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        rule2_group = VGroup(rule2_box, rule2_title, rule2_content)
        
        self.play(FadeIn(rule2_group, shift=LEFT * 0.3), run_time=0.7)
        
        # 示例2
        examples2 = VGroup(
            MathTex(r"3 \times 0 = 0", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"7 \times 0 = 0", font_size=self.FONT_BODY, color=WHITE),
            MathTex(r"15 \times 0 = 0", font_size=self.FONT_BODY, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 2.8 + LEFT * 1)
        
        self.play(FadeIn(examples2, shift=RIGHT * 0.2, lag_ratio=0.3), run_time=1.0)
        
        # 高亮0
        for example in examples2:
            self.play(Indicate(example, scale_factor=1.1), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule1_group),
            FadeOut(examples1),
            FadeOut(rule2_group),
            FadeOut(examples2),
            run_time=0.5
        )
    
    def show_summary(self):
        """场景6: 总结与巩固 (10-12秒)"""
        # 标题
        title = Text(
            "知识总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 对比表格 - 使用VGroup而不是Table（更简单）
        table_title = Text(
            "因数 vs 倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(table_title), run_time=0.5)
        
        # 手动创建表格
        row1 = VGroup(
            Text("", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("因数", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_FACTOR),
            Text("倍数", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_MULTIPLE)
        ).arrange(RIGHT, buff=1.0).move_to(UP * 3)
        
        row2 = VGroup(
            Text("数量", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("有限", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("无限", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(RIGHT, buff=1.0).move_to(UP * 2.2)
        
        row3 = VGroup(
            Text("最小", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            Text("1", font="Noto Sans CJK SC", font_size=20, color=WHITE),
            Text("本身", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(RIGHT, buff=1.0).move_to(UP * 1.4)
        
        comparison_table = VGroup(row1, row2, row3)
        
        self.play(FadeIn(comparison_table, shift=UP * 0.2, lag_ratio=0.3), run_time=1.0)
        
        # 总结要点
        point1_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_PRIMARY,
            fill_opacity=1,
            stroke_width=0
        ).move_to(DOWN * 0.3 + LEFT * 3.5)
        
        point1_text = Text(
            "定义：a = b × q，b是a的因数，a是b的倍数",
            font="Noto Sans CJK SC",
            font_size=18,
            color=WHITE
        ).next_to(point1_icon, RIGHT, buff=0.2)
        
        point1 = VGroup(point1_icon, point1_text)
        point1.shift(LEFT * 10)
        
        point2_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_FACTOR,
            fill_opacity=1,
            stroke_width=0
        ).move_to(DOWN * 1.3 + LEFT * 3.5)
        
        point2_text = Text(
            "数量：因数有限，倍数无限",
            font="Noto Sans CJK SC",
            font_size=18,
            color=WHITE
        ).next_to(point2_icon, RIGHT, buff=0.2)
        
        point2 = VGroup(point2_icon, point2_text)
        point2.shift(LEFT * 10)
        
        point3_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SPECIAL,
            fill_opacity=1,
            stroke_width=0
        ).move_to(DOWN * 2.3 + LEFT * 3.5)
        
        point3_text = Text(
            "特殊：1是所有正整数的因数，0是所有非零整数的倍数",
            font="Noto Sans CJK SC",
            font_size=16,
            color=WHITE
        ).next_to(point3_icon, RIGHT, buff=0.2)
        
        point3 = VGroup(point3_icon, point3_text)
        point3.shift(LEFT * 10)
        
        # 要点依次滑入
        self.play(point1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(point2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.3)
        self.play(point3.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.8)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰星星
        stars = VGroup(*[
            Star(
                n=5,
                outer_radius=0.2,
                color=GOLD,
                fill_opacity=0.8
            ).move_to(follow_text.get_center() + 1.5 * np.array([np.cos(i * PI / 2), np.sin(i * PI / 2), 0]))
            for i in range(4)
        ])
        
        self.play(
            *[FadeIn(star, scale=0.5) for star in stars],
            run_time=0.5
        )
        self.play(
            *[Flash(star, color=GOLD) for star in stars],
            run_time=0.5
        )
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(table_title),
            FadeOut(comparison_table),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            FadeOut(follow_text),
            FadeOut(stars),
            FadeOut(self.author_info),
            run_time=1.0
        )


# 运行命令:
# manim -pql factors_multiples.py FactorsAndMultiples  # 快速预览
# manim -qh factors_multiples.py FactorsAndMultiples   # 高质量渲染