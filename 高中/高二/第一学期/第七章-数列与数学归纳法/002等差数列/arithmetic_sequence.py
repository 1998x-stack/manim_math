"""
等差数列教学动画 - Arithmetic Sequence Teaching Animation
使用 Manim 0.19.2 创建的高二数学教学视频

内容: 等差数列的定义、通项公式、前n项和、等差中项、图形规律
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

class ArithmeticSequenceLesson(Scene):
    """
    等差数列教学动画主场景
    
    场景顺序:
    1. 开场钩子 (3-4秒)
    2. 等差数列定义 (10-12秒)
    3. 通项公式推导 (15-18秒)
    4. 前n项和公式 (18-20秒)
    5. 等差中项 (8-10秒)
    6. 图形规律 (10-12秒)
    7. 性质与应用 (8-10秒)
    8. 总结与关注 (5-6秒)
    
    总时长: 约75-90秒
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要数列项
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调/公差
        self.COLOR_HIGHLIGHT = "#f39c12"    # 橙色 - 重点内容
        self.COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
        
        # 字体大小
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "formula": 28,
            "small": 18,
        }
        
        # 初始化数列参数和几何数据
        self.setup_sequence()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_general_term()
        self.scene_4_sum_formula()
        self.scene_5_arithmetic_mean()
        self.scene_6_graphical_pattern()
        self.scene_7_properties()
        self.scene_8_outro()
    
    def setup_sequence(self):
        """初始化等差数列的所有参数和几何数据"""
        # ========== 数列参数 ==========
        self.a1 = 2          # 首项
        self.d = 3           # 公差
        self.n_terms = 7     # 展示的项数
        
        # 计算数列各项
        self.terms = [self.a1 + (n - 1) * self.d for n in range(1, self.n_terms + 1)]
        # 结果: [2, 5, 8, 11, 14, 17, 20]
        
        # ========== NumberLine配置 ==========
        self.number_line_config = {
            "x_range": [0, 22, 2],  # [min, max, step]
            "length": 7,
            "include_numbers": True,
            "numbers_to_include": [0, 5, 10, 15, 20],
            "font_size": 18,
        }
        
        # ========== 验证数列计算 ==========
        self.verify_sequence()
    
    def verify_sequence(self):
        """验证等差数列的计算正确性"""
        epsilon = 1e-10
        
        # 验证公差一致性
        for i in range(len(self.terms) - 1):
            diff = self.terms[i + 1] - self.terms[i]
            assert abs(diff - self.d) < epsilon, f"公差不一致: {diff} ≠ {self.d}"
        
        # 验证通项公式
        for n in range(1, self.n_terms + 1):
            calculated = self.a1 + (n - 1) * self.d
            actual = self.terms[n - 1]
            assert abs(calculated - actual) < epsilon, f"通项公式错误: a_{n} = {calculated} ≠ {actual}"
        
        # 验证前n项和
        sum_terms = sum(self.terms)
        sum_formula_1 = self.n_terms * (self.terms[0] + self.terms[-1]) / 2
        sum_formula_2 = self.n_terms * self.a1 + self.n_terms * (self.n_terms - 1) * self.d / 2
        
        assert abs(sum_terms - sum_formula_1) < epsilon, "求和公式1错误"
        assert abs(sum_terms - sum_formula_2) < epsilon, "求和公式2错误"
        assert abs(sum_formula_1 - sum_formula_2) < epsilon, "两个求和公式不等价"
        
        # 验证等差中项
        for i in range(1, len(self.terms) - 1):
            middle = self.terms[i]
            mean = (self.terms[i - 1] + self.terms[i + 1]) / 2
            assert abs(middle - mean) < epsilon, f"等差中项错误: a_{i+1} = {middle} ≠ {mean}"
        
        print("✓ 数列验证通过")
    
    # ==================== Scene 1: 开场钩子 ====================
    
    def scene_1_opening(self):
        """开场钩子 - 吸引注意力"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "2, 5, 8, 11, 14, ...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"] + 4,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        question_mark = Text(
            "下一个是？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(hook_question, DOWN, buff=0.3)
        
        self.play(Write(hook_question), run_time=0.8)
        self.play(FadeIn(question_mark, shift=UP * 0.2), run_time=0.4)
        
        # 创建数轴
        number_line = NumberLine(
            **self.number_line_config,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 创建数列各项的点
        dots = VGroup()
        for term in self.terms:
            dot = Dot(
                number_line.number_to_point(term),
                radius=0.1,
                color=self.COLOR_PRIMARY,
                fill_opacity=1
            )
            dots.add(dot)
        
        # 点依次跳出
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in dots], lag_ratio=0.15),
            run_time=1.2
        )
        
        # 问号闪烁
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(question_mark),
            run_time=0.5
        )
        
        # 保留用于后续场景
        self.number_line = number_line
        self.dots = dots
    
    # ==================== Scene 2: 等差数列定义 ====================
    
    def scene_2_definition(self):
        """等差数列定义 - 强调公差"""
        # 标题
        title_cn = Text(
            "等差数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        title_en = Text(
            "Arithmetic Sequence",
            font="Arial",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title_cn, DOWN, buff=0.15)
        
        self.play(Write(title_cn), run_time=0.6)
        self.play(FadeIn(title_en), run_time=0.3)
        
        # 定义文字
        definition_text = Text(
            "从第二项起，每项与前一项的差",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 4)
        
        definition_text_2 = Text(
            "等于同一常数 d（公差）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).next_to(definition_text, DOWN, buff=0.2)
        
        self.play(FadeIn(definition_text, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(definition_text_2, shift=UP * 0.2), run_time=0.6)
        
        # 公式
        formula_definition = MathTex(
            r"a_{n+1} - a_n = d \text{ (constant)}",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(UP * 2.8)
        formula_definition.set_color_by_tex("d", self.COLOR_SECONDARY)
        
        self.play(Write(formula_definition), run_time=0.8)
        
        self.wait(0.5)
        
        # 标注公差 - 使用Brace
        braces = VGroup()
        d_labels = VGroup()
        
        for i in range(len(self.dots) - 1):
            # 创建连接两点的虚线
            line = DashedLine(
                self.dots[i].get_center(),
                self.dots[i + 1].get_center(),
                color=self.COLOR_SECONDARY,
                dash_length=0.08,
                stroke_width=2
            )
            
            brace = Brace(line, direction=UP, buff=0.1, color=self.COLOR_SECONDARY)
            label = MathTex(r"d", font_size=self.FONT_SIZES["label"], color=self.COLOR_SECONDARY)
            label.next_to(brace, UP, buff=0.05)
            
            braces.add(VGroup(line, brace))
            d_labels.add(label)
        
        # 逐个显示前3对
        for i in range(min(3, len(braces))):
            self.play(
                Indicate(VGroup(self.dots[i], self.dots[i + 1]), color=self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
            self.play(
                GrowFromCenter(braces[i]),
                FadeIn(d_labels[i], shift=DOWN * 0.2),
                run_time=0.5
            )
            self.wait(0.3)
        
        # 强调公差一致
        self.play(
            Flash(d_labels, color=self.COLOR_SECONDARY, flash_radius=0.3),
            run_time=0.6
        )
        
        # 显示公差值
        d_value = MathTex(
            r"d = 3",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 0.5)
        
        self.play(
            *[Transform(label, d_value.copy()) for label in d_labels[:3]],
            run_time=0.8
        )
        
        # 统一标签
        unified_d = Text(
            "公差 d = 3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeOut(d_labels[:3]),
            FadeIn(unified_d, scale=1.2),
            run_time=0.6
        )
        
        # 说明
        explanation = Text(
            "公差可正、可负、可为零",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title_cn),
            FadeOut(title_en),
            FadeOut(definition_text),
            FadeOut(definition_text_2),
            FadeOut(formula_definition),
            FadeOut(braces),
            FadeOut(explanation),
            unified_d.animate.scale(0.6).move_to(UP * 7 + RIGHT * 3),
            run_time=0.6
        )
        
        # 保留缩小的d标签作为参考
        self.d_reference = unified_d
    
    # ==================== Scene 3: 通项公式推导 ====================
    
    def scene_3_general_term(self):
        """通项公式推导"""
        # 标题
        title = Text(
            "通项公式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "General Term Formula",
            font="Arial",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.15)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 逐步推导
        derivation = VGroup(
            MathTex(r"a_1 = 2", font_size=self.FONT_SIZES["body"]),
            MathTex(r"a_2 = a_1 + d = 2 + 3 = 5", font_size=self.FONT_SIZES["body"]),
            MathTex(r"a_3 = a_1 + 2d = 2 + 2 \times 3 = 8", font_size=self.FONT_SIZES["body"]),
            MathTex(r"a_4 = a_1 + 3d = 2 + 3 \times 3 = 11", font_size=self.FONT_SIZES["body"]),
            MathTex(r"\vdots", font_size=self.FONT_SIZES["body"]),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        derivation.move_to(UP * 1.5)
        
        # 依次显示
        for i, formula in enumerate(derivation):
            self.play(Write(formula), run_time=0.7)
            if i < len(derivation) - 1:
                self.wait(0.3)
        
        # 框选规律
        pattern_rect = SurroundingRectangle(
            derivation[1:4],
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        pattern_note = Text(
            "系数规律: n-1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(pattern_rect, RIGHT, buff=0.3)
        
        self.play(
            Create(pattern_rect),
            FadeIn(pattern_note, shift=LEFT * 0.2),
            run_time=0.8
        )
        
        self.wait(0.8)
        
        # 通项公式
        general_formula = MathTex(
            r"a_n = a_1 + (n-1)d",
            font_size=self.FONT_SIZES["formula"] + 4,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeOut(pattern_rect),
            FadeOut(pattern_note),
            Write(general_formula),
            run_time=1.0
        )
        
        # 放大强调
        self.play(
            general_formula.animate.scale(1.2).set_color(self.COLOR_FORMULA),
            run_time=0.6
        )
        
        # 验证示例
        verification = VGroup(
            Text(
                "验证：",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SIZES["body"],
                color=WHITE
            ),
            MathTex(
                r"a_7 = 2 + (7-1) \times 3 = 2 + 18 = 20",
                font_size=self.FONT_SIZES["body"]
            ),
            MathTex(r"\checkmark", font_size=self.FONT_SIZES["subtitle"], color=GREEN)
        ).arrange(RIGHT, buff=0.2)
        verification.move_to(DOWN * 3.5)
        
        self.play(FadeIn(verification, shift=UP * 0.2), run_time=0.8)
        
        # 第7个点闪烁
        self.play(
            Flash(self.dots[6], color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
            self.dots[6].animate.scale(1.5).set_color(self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        self.play(self.dots[6].animate.scale(1/1.5).set_color(self.COLOR_PRIMARY), run_time=0.3)
        
        self.wait(2.0)  # 关键公式，多停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(derivation),
            FadeOut(verification),
            general_formula.animate.scale(1/1.2).scale(0.5).move_to(UP * 6.5 + LEFT * 2),
            run_time=0.6
        )
        
        # 保留公式作为参考
        self.general_formula_ref = general_formula
    
    # ==================== Scene 4: 前n项和公式 ====================
    
    def scene_4_sum_formula(self):
        """前n项和公式推导"""
        # 标题
        title = Text(
            "前n项和公式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Sum Formula",
            font="Arial",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.15)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 求和式
        sum_notation = MathTex(
            r"S_n = a_1 + a_2 + \cdots + a_n",
            font_size=self.FONT_SIZES["body"]
        ).move_to(UP * 4)
        
        self.play(Write(sum_notation), run_time=0.8)
        
        # 倒序相加法标题
        method_title = Text(
            "倒序相加法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(FadeIn(method_title, shift=UP * 0.2), run_time=0.5)
        
        # 正序
        forward = MathTex(
            r"S_n = a_1 + (a_1+d) + (a_1+2d) + \cdots + a_n",
            font_size=self.FONT_SIZES["body"] - 2
        ).move_to(UP * 2)
        
        self.play(Write(forward), run_time=1.0)
        
        # 倒序
        reverse = MathTex(
            r"S_n = a_n + (a_n-d) + (a_n-2d) + \cdots + a_1",
            font_size=self.FONT_SIZES["body"] - 2
        ).next_to(forward, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(reverse), run_time=1.0)
        
        # 相加
        plus_sign = MathTex(r"+", font_size=self.FONT_SIZES["subtitle"])
        plus_sign.next_to(reverse, LEFT, buff=0.2)
        
        self.play(FadeIn(plus_sign), run_time=0.3)
        
        # 画线
        line = Line(
            reverse.get_left() + LEFT * 0.5,
            reverse.get_right(),
            color=WHITE
        ).next_to(reverse, DOWN, buff=0.1)
        
        self.play(Create(line), run_time=0.5)
        
        # 结果
        result = MathTex(
            r"2S_n = (a_1+a_n) + (a_1+a_n) + \cdots + (a_1+a_n) = n(a_1+a_n)",
            font_size=self.FONT_SIZES["body"] - 2
        ).next_to(line, DOWN, buff=0.3)
        
        self.play(Write(result), run_time=1.2)
        
        self.wait(0.5)
        
        # 公式1
        formula_1 = MathTex(
            r"S_n = \frac{n(a_1 + a_n)}{2}",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1)
        
        self.play(
            FadeOut(forward),
            FadeOut(reverse),
            FadeOut(plus_sign),
            FadeOut(line),
            FadeOut(result),
            FadeOut(method_title),
            Write(formula_1),
            run_time=1.0
        )
        
        # 强调
        self.play(
            formula_1.animate.scale(1.15),
            run_time=0.4
        )
        
        self.wait(0.8)
        
        # 替换an说明
        replacement_note = Text(
            "将 aₙ = a₁+(n-1)d 代入:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(replacement_note, shift=UP * 0.2), run_time=0.5)
        
        # 公式2
        formula_2 = MathTex(
            r"S_n = na_1 + \frac{n(n-1)d}{2}",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.8)
        
        self.play(Write(formula_2), run_time=1.0)
        
        # 强调
        self.play(
            formula_2.animate.scale(1.15),
            run_time=0.4
        )
        
        self.wait(0.8)
        
        # 验证示例
        example_text = Text(
            "验证：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(DOWN * 5.5 + LEFT * 3)
        
        example_calc = MathTex(
            r"S_7 = \frac{7 \times (2+20)}{2} = \frac{154}{2} = 77",
            font_size=self.FONT_SIZES["body"] - 2
        ).next_to(example_text, RIGHT, buff=0.2)
        
        checkmark = MathTex(r"\checkmark", font_size=self.FONT_SIZES["body"], color=GREEN)
        checkmark.next_to(example_calc, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(example_text),
            Write(example_calc),
            FadeIn(checkmark, scale=1.2),
            run_time=1.0
        )
        
        self.wait(2.0)  # 关键公式，多停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(sum_notation),
            FadeOut(replacement_note),
            FadeOut(example_text),
            FadeOut(example_calc),
            FadeOut(checkmark),
            formula_1.animate.scale(1/1.15).scale(0.45).move_to(UP * 6 + RIGHT * 2.5),
            formula_2.animate.scale(1/1.15).scale(0.45).next_to(UP * 6 + RIGHT * 2.5, DOWN, buff=0.1),
            run_time=0.6
        )
        
        # 保留公式作为参考
        self.sum_formula_1_ref = formula_1
        self.sum_formula_2_ref = formula_2
    
    # ==================== Scene 5: 等差中项 ====================
    
    def scene_5_arithmetic_mean(self):
        """等差中项概念"""
        # 标题
        title = Text(
            "等差中项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Arithmetic Mean",
            font="Arial",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.15)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 定义
        definition = Text(
            "若 a, A, b 成等差数列，",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 4)
        
        definition_2 = Text(
            "则 A 为 a 和 b 的等差中项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).next_to(definition, DOWN, buff=0.2)
        
        self.play(
            FadeIn(definition, shift=UP * 0.2),
            FadeIn(definition_2, shift=UP * 0.2),
            run_time=0.9
        )
        
        # 简化数轴 - 清除原数轴
        self.play(
            FadeOut(self.number_line),
            FadeOut(self.dots),
            run_time=0.4
        )
        
        # 新数轴（简化）
        simple_line = NumberLine(
            x_range=[0, 15, 1],
            length=6,
            include_numbers=False,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1.5)
        
        self.play(Create(simple_line), run_time=0.6)
        
        # 三个点
        a_val, A_val, b_val = 5, 8, 11
        
        point_a = Dot(simple_line.number_to_point(a_val), radius=0.12, color=self.COLOR_PRIMARY)
        point_A = Dot(simple_line.number_to_point(A_val), radius=0.12, color=self.COLOR_HIGHLIGHT)
        point_b = Dot(simple_line.number_to_point(b_val), radius=0.12, color=self.COLOR_PRIMARY)
        
        label_a = MathTex("a", font_size=self.FONT_SIZES["label"]).next_to(point_a, DOWN, buff=0.2)
        label_A = MathTex("A", font_size=self.FONT_SIZES["label"], color=self.COLOR_HIGHLIGHT).next_to(point_A, DOWN, buff=0.2)
        label_b = MathTex("b", font_size=self.FONT_SIZES["label"]).next_to(point_b, DOWN, buff=0.2)
        
        self.play(
            FadeIn(point_a),
            FadeIn(point_A, scale=1.2),
            FadeIn(point_b),
            run_time=0.6
        )
        self.play(
            Write(label_a),
            Write(label_A),
            Write(label_b),
            run_time=0.4
        )
        
        # 标注距离
        brace_left = Brace(Line(point_a.get_center(), point_A.get_center()), direction=UP, buff=0.1)
        brace_label_left = MathTex("d", font_size=self.FONT_SIZES["body"], color=self.COLOR_SECONDARY)
        brace_label_left.next_to(brace_left, UP, buff=0.05)
        
        brace_right = Brace(Line(point_A.get_center(), point_b.get_center()), direction=UP, buff=0.1)
        brace_label_right = MathTex("d", font_size=self.FONT_SIZES["body"], color=self.COLOR_SECONDARY)
        brace_label_right.next_to(brace_right, UP, buff=0.05)
        
        self.play(
            GrowFromCenter(brace_left),
            FadeIn(brace_label_left),
            GrowFromCenter(brace_right),
            FadeIn(brace_label_right),
            run_time=0.8
        )
        
        # 推导
        equation_1 = MathTex(r"A - a = b - A", font_size=self.FONT_SIZES["body"]).move_to(DOWN * 1)
        self.play(Write(equation_1), run_time=0.7)
        
        equation_2 = MathTex(r"2A = a + b", font_size=self.FONT_SIZES["body"]).move_to(DOWN * 2)
        self.play(TransformMatchingTex(equation_1.copy(), equation_2), run_time=0.8)
        
        # 公式
        formula_mean = MathTex(
            r"A = \frac{a + b}{2}",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.2)
        
        self.play(Write(formula_mean), run_time=0.8)
        
        # 强调
        self.play(
            formula_mean.animate.scale(1.2),
            Flash(formula_mean, color=self.COLOR_FORMULA),
            run_time=0.6
        )
        
        # 几何意义
        geometry_note = Text(
            "A 是 a 和 b 的中点（算术平均）",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(geometry_note, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(definition),
            FadeOut(definition_2),
            FadeOut(simple_line),
            FadeOut(point_a),
            FadeOut(point_A),
            FadeOut(point_b),
            FadeOut(label_a),
            FadeOut(label_A),
            FadeOut(label_b),
            FadeOut(brace_left),
            FadeOut(brace_label_left),
            FadeOut(brace_right),
            FadeOut(brace_label_right),
            FadeOut(equation_1),
            FadeOut(equation_2),
            FadeOut(geometry_note),
            formula_mean.animate.scale(1/1.2).scale(0.5).move_to(DOWN * 6.5 + LEFT * 2),
            run_time=0.6
        )
        
        # 保留公式作为参考
        self.mean_formula_ref = formula_mean
    
    # ==================== Scene 6: 图形规律 ====================
    
    def scene_6_graphical_pattern(self):
        """用坐标系展示等差数列的线性特征"""
        # 标题
        title = Text(
            "图形特征",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "等差数列的点在一条直线上",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.15)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 22, 5],
            x_length=6,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "font_size": 16,
            },
            tips=False
        ).move_to(DOWN * 0.5)
        
        # 轴标签
        x_label = MathTex("n", font_size=self.FONT_SIZES["body"]).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("a_n", font_size=self.FONT_SIZES["body"]).next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), run_time=1.0)
        self.play(Write(x_label), Write(y_label), run_time=0.5)
        
        # 数据点
        points_data = [(n, self.a1 + (n - 1) * self.d) for n in range(1, self.n_terms + 1)]
        
        dots_graph = VGroup()
        for n, an in points_data:
            dot = Dot(
                axes.c2p(n, an),
                radius=0.08,
                color=self.COLOR_PRIMARY,
                fill_opacity=1
            )
            dots_graph.add(dot)
        
        # 点依次出现
        self.play(
            LaggedStart(*[GrowFromCenter(dot) for dot in dots_graph], lag_ratio=0.2),
            run_time=1.5
        )
        
        # 连接的直线
        line_graph = axes.plot(
            lambda n: self.a1 + (n - 1) * self.d,
            x_range=[0.5, 7.5],
            color=self.COLOR_FORMULA,
            stroke_width=3
        )
        
        self.play(Create(line_graph), run_time=1.2)
        
        # 函数标注
        function_label = MathTex(
            r"a_n = a_1 + (n-1)d",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_FORMULA
        ).move_to(UP * 5 + RIGHT * 2)
        
        self.play(FadeIn(function_label, shift=LEFT * 0.2), run_time=0.6)
        
        # 强调线性
        self.play(
            Indicate(line_graph, color=self.COLOR_HIGHLIGHT, scale_factor=1.05),
            run_time=0.8
        )
        
        # 斜率说明
        slope_explanation = Text(
            "斜率 = 公差 d = 3",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(slope_explanation, shift=UP * 0.2), run_time=0.6)
        
        # 画斜率三角形
        p1 = axes.c2p(2, self.a1 + self.d)
        p2 = axes.c2p(3, self.a1 + 2 * self.d)
        p3 = axes.c2p(3, self.a1 + self.d)
        
        slope_triangle = Polygon(p1, p2, p3, color=self.COLOR_SECONDARY, stroke_width=2)
        
        # 标注
        delta_n = MathTex(r"\Delta n = 1", font_size=14, color=self.COLOR_SECONDARY).next_to(
            Line(p1, p3).get_center(), DOWN, buff=0.1
        )
        delta_a = MathTex(r"\Delta a_n = d", font_size=14, color=self.COLOR_SECONDARY).next_to(
            Line(p3, p2).get_center(), RIGHT, buff=0.1
        )
        
        self.play(
            Create(slope_triangle),
            FadeIn(delta_n),
            FadeIn(delta_a),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(dots_graph),
            FadeOut(line_graph),
            FadeOut(function_label),
            FadeOut(slope_explanation),
            FadeOut(slope_triangle),
            FadeOut(delta_n),
            FadeOut(delta_a),
            run_time=0.6
        )
    
    # ==================== Scene 7: 性质与应用 ====================
    
    def scene_7_properties(self):
        """展示等差数列的关键性质和应用"""
        # 标题
        title = Text(
            "重要性质",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 性质1
        property_1 = MathTex(
            r"m+n = p+q \Rightarrow a_m + a_n = a_p + a_q",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(Write(property_1), run_time=1.0)
        
        # 示例
        example_indices = Text(
            "例：3 + 5 = 2 + 6 = 8",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(example_indices, shift=UP * 0.2), run_time=0.5)
        
        # 验证
        verification_text = Text(
            "验证：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 2.8 + LEFT * 3)
        
        # a3=8, a5=14, a2=5, a6=17
        calc_left = MathTex(
            r"a_3 + a_5 = 8 + 14 = 22",
            font_size=self.FONT_SIZES["body"]
        ).next_to(verification_text, RIGHT, buff=0.2)
        
        calc_right = MathTex(
            r"a_2 + a_6 = 5 + 17 = 22",
            font_size=self.FONT_SIZES["body"]
        ).move_to(UP * 1.8)
        
        checkmark = MathTex(r"\checkmark", font_size=self.FONT_SIZES["subtitle"], color=GREEN)
        checkmark.next_to(calc_right, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(verification_text),
            Write(calc_left),
            run_time=0.8
        )
        self.play(
            Write(calc_right),
            FadeIn(checkmark, scale=1.2),
            run_time=0.7
        )
        
        self.wait(0.6)
        
        # 应用题
        problem = Text(
            "应用题：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 0.5 + LEFT * 3.5)
        
        problem_text = Text(
            "某等差数列，a₃ = 7，a₇ = 15，求 a₅",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"] - 2,
            color=WHITE
        ).next_to(problem, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(problem, shift=DOWN * 0.2),
            FadeIn(problem_text, shift=DOWN * 0.2),
            run_time=0.8
        )
        
        # 解法提示
        hint = Text(
            "提示：利用等差中项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        
        # 解答
        solution = MathTex(
            r"a_5 = \frac{a_3 + a_7}{2} = \frac{7 + 15}{2} = \frac{22}{2} = 11",
            font_size=self.FONT_SIZES["body"]
        ).move_to(DOWN * 2.5)
        
        self.play(Write(solution), run_time=1.2)
        
        # 框选答案
        answer_box = SurroundingRectangle(
            solution[-2:],  # "= 11"部分
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            corner_radius=0.05
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property_1),
            FadeOut(example_indices),
            FadeOut(verification_text),
            FadeOut(calc_left),
            FadeOut(calc_right),
            FadeOut(checkmark),
            FadeOut(problem),
            FadeOut(problem_text),
            FadeOut(hint),
            FadeOut(solution),
            FadeOut(answer_box),
            run_time=0.6
        )
    
    # ==================== Scene 8: 总结与关注 ====================
    
    def scene_8_outro(self):
        """总结关键公式，引导关注"""
        # 标题
        title = Text(
            "等差数列要点总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_FORMULA,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式框
        formula_box_1 = VGroup(
            Text("通项公式:", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            MathTex(r"a_n = a_1 + (n-1)d", font_size=24, color=self.COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        formula_box_2 = VGroup(
            Text("求和公式:", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            MathTex(r"S_n = \frac{n(a_1+a_n)}{2}", font_size=24, color=self.COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
        
        formula_box_3 = VGroup(
            Text("等差中项:", font="Noto Sans CJK SC", font_size=20, color=GRAY_A),
            MathTex(r"A = \frac{a+b}{2}", font_size=24, color=self.COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1)
        
        # 依次出现
        self.play(FadeIn(formula_box_1, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(formula_box_2, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(formula_box_3, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(0.5)
        
        # 清除之前的参考公式和标题
        refs_to_clear = [
            self.d_reference if hasattr(self, 'd_reference') else None,
            self.general_formula_ref if hasattr(self, 'general_formula_ref') else None,
            self.sum_formula_1_ref if hasattr(self, 'sum_formula_1_ref') else None,
            self.sum_formula_2_ref if hasattr(self, 'sum_formula_2_ref') else None,
            self.mean_formula_ref if hasattr(self, 'mean_formula_ref') else None,
        ]
        refs_to_clear = [r for r in refs_to_clear if r is not None]
        
        self.play(
            FadeOut(title),
            *[FadeOut(ref) for ref in refs_to_clear],
            run_time=0.4
        )
        
        # 作者信息放大并移到中央
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 1)
        
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
            "关注我，掌握更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 点赞图标（使用Star代替）
        like_icon = Star(
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.8,
            stroke_width=2
        ).scale(0.6).move_to(DOWN * 5.5)
        
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
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(formula_box_1),
            FadeOut(formula_box_2),
            FadeOut(formula_box_3),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(like_icon),
            run_time=1.0
        )


# ==================== 渲染入口 ====================

if __name__ == "__main__":
    # 使用以下命令渲染:
    # 快速预览: manim -pql arithmetic_sequence.py ArithmeticSequenceLesson
    # 高质量: manim -qh arithmetic_sequence.py ArithmeticSequenceLesson
    # 4K质量: manim -qk arithmetic_sequence.py ArithmeticSequenceLesson
    pass