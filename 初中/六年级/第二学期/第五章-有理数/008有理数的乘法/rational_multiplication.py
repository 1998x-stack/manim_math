"""
有理数的乘法 - Rational Number Multiplication
使用 Manim 创建的六年级数学教学视频

内容: 有理数乘法法则及其应用
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


class RationalMultiplication(Scene):
    """
    有理数乘法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 法则总览
    3. 同号得正 - 正×正
    4. 同号得正 - 负×负
    5. 异号得负 - 正×负
    6. 多个数相乘规律
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主题色
        self.COLOR_POSITIVE = "#2ecc71"     # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e74c3c"     # 红色 - 负数
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 36
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 22
        self.FONT_SIZE_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_rules_overview()
        self.show_positive_times_positive()
        self.show_negative_times_negative()
        self.show_positive_times_negative()
        self.show_multiple_multiplication()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部常驻）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).to_edge(UP, buff=0.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = VGroup(
            Text(
                "你知道吗？",
                font=self.FONT_CHINESE,
                font_size=32,
                color=WHITE
            ),
            Text(
                "负数 × 负数 = ？",
                font=self.FONT_CHINESE,
                font_size=48,
                color=self.COLOR_HIGHLIGHT,
                weight=BOLD
            ).shift(DOWN * 0.6)
        ).move_to(UP * 2)
        
        self.play(Write(hook_question[0]), run_time=0.6)
        self.play(Write(hook_question[1]), run_time=0.8)
        
        # 大问号动画
        question_mark = Text(
            "?",
            font_size=120,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.5)
        self.play(
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=1.5),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_rules_overview(self):
        """场景2: 法则总览"""
        # 标题
        title = Text(
            "有理数乘法法则",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 四条法则
        rules = VGroup()
        
        rule_data = [
            ("(+) × (+) = ", "+", self.COLOR_POSITIVE),
            ("(-) × (-) = ", "+", self.COLOR_POSITIVE),
            ("(+) × (-) = ", "-", self.COLOR_NEGATIVE),
            ("(-) × (+) = ", "-", self.COLOR_NEGATIVE),
        ]
        
        for i, (formula, result, color) in enumerate(rule_data):
            rule_text = MathTex(
                formula, result,
                font_size=32
            )
            rule_text[1].set_color(color)
            rule_text.shift(DOWN * (i - 1.5) * 1.2 + UP * 3)
            rules.add(rule_text)
        
        # 逐条淡入
        for i, rule in enumerate(rules):
            self.play(FadeIn(rule, shift=RIGHT * 0.3), run_time=0.4)
            if i < len(rules) - 1:
                self.wait(0.2)
        
        # 高亮关键规律
        key_box_1 = SurroundingRectangle(
            VGroup(rules[0], rules[1]),
            color=self.COLOR_POSITIVE,
            buff=0.2
        )
        key_label_1 = Text(
            "同号得正",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_POSITIVE
        ).next_to(key_box_1, RIGHT, buff=0.3)
        
        key_box_2 = SurroundingRectangle(
            VGroup(rules[2], rules[3]),
            color=self.COLOR_NEGATIVE,
            buff=0.2
        )
        key_label_2 = Text(
            "异号得负",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_NEGATIVE
        ).next_to(key_box_2, RIGHT, buff=0.3)
        
        self.play(
            Create(key_box_1),
            Write(key_label_1),
            run_time=0.6
        )
        self.wait(0.4)
        
        self.play(
            Create(key_box_2),
            Write(key_label_2),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 缩小并移至侧边
        rules_summary = VGroup(title, rules, key_box_1, key_label_1, key_box_2, key_label_2)
        
        self.play(
            rules_summary.animate.scale(0.5).to_edge(LEFT, buff=0.3).shift(UP * 3),
            run_time=0.8
        )
        
        # 保存引用以便后续清理
        self.rules_summary = rules_summary
    
    def show_positive_times_positive(self):
        """场景3: 同号得正 - 正×正"""
        # 示例公式
        formula = MathTex(
            "(+3)", r"\times", "(+2)", "=", "?",
            font_size=40
        ).move_to(UP * 5)
        formula[0].set_color(self.COLOR_POSITIVE)
        formula[2].set_color(self.COLOR_POSITIVE)
        
        self.play(Write(formula), run_time=0.8)
        
        # 数轴
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=20,
            include_tip=True
        ).move_to(UP * 1.5)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 说明文字
        explanation = Text(
            "从0开始，向右跳3个单位，跳2次",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 起点
        dot = Dot(number_line.n2p(0), color=self.COLOR_POSITIVE, radius=0.12)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)
        
        # 第一次跳跃
        arc1 = Arc(
            radius=0.8,
            start_angle=0,
            angle=PI,
            color=self.COLOR_POSITIVE
        ).shift(number_line.n2p(1.5) + DOWN * 0.8)
        
        arrow1 = Arrow(
            number_line.n2p(0),
            number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            buff=0,
            stroke_width=6
        ).shift(UP * 0.5)
        
        label1 = Text(
            "+3",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_POSITIVE
        ).next_to(arrow1, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow1),
            Write(label1),
            run_time=0.6
        )
        self.play(
            MoveAlongPath(dot, arc1),
            run_time=0.8
        )
        
        # 第二次跳跃
        arc2 = Arc(
            radius=0.8,
            start_angle=0,
            angle=PI,
            color=self.COLOR_POSITIVE
        ).shift(number_line.n2p(4.5) + DOWN * 0.8)
        
        arrow2 = Arrow(
            number_line.n2p(3),
            number_line.n2p(6),
            color=self.COLOR_POSITIVE,
            buff=0,
            stroke_width=6
        ).shift(UP * 0.5)
        
        label2 = Text(
            "+3",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_POSITIVE
        ).next_to(arrow2, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow2),
            Write(label2),
            run_time=0.6
        )
        self.play(
            MoveAlongPath(dot, arc2),
            run_time=0.8
        )
        
        # 终点标记
        end_dot = Dot(number_line.n2p(6), color=YELLOW, radius=0.15)
        self.play(
            Transform(dot, end_dot),
            Flash(end_dot, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        
        # 结果
        result = MathTex(
            "(+3)", r"\times", "(+2)", "=", "+6",
            font_size=40
        ).move_to(DOWN * 3)
        result[0].set_color(self.COLOR_POSITIVE)
        result[2].set_color(self.COLOR_POSITIVE)
        result[4].set_color(self.COLOR_POSITIVE)
        
        self.play(
            TransformMatchingTex(formula.copy(), result),
            run_time=0.8
        )
        
        # 高亮结果
        box = SurroundingRectangle(result[4], color=self.COLOR_POSITIVE, buff=0.15)
        self.play(Create(box), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(number_line),
            FadeOut(dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(result),
            FadeOut(box),
            run_time=0.6
        )
    
    def show_negative_times_negative(self):
        """场景4: 同号得正 - 负×负"""
        # 示例公式
        formula = MathTex(
            "(-3)", r"\times", "(-2)", "=", "?",
            font_size=40
        ).move_to(UP * 5)
        formula[0].set_color(self.COLOR_NEGATIVE)
        formula[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(formula), run_time=0.8)
        
        # 双向数轴
        number_line = NumberLine(
            x_range=[-10, 10, 2],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=20,
            include_tip=True,
            tip_width=0.2,
            tip_height=0.2
        ).move_to(UP * 1)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 理解提示
        hint = Text(
            "负数×负数 = 反向的反向 = 正向",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint), run_time=0.6)
        
        # 起点
        dot = Dot(number_line.n2p(0), color=self.COLOR_NEGATIVE, radius=0.12)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)
        
        # 说明反向
        explanation = Text(
            "反向跳-3，跳2次（负的负 = 正）",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.5)
        
        # 第一次反向跳
        arrow1 = Arrow(
            number_line.n2p(0),
            number_line.n2p(3),
            color=self.COLOR_POSITIVE,
            buff=0,
            stroke_width=6
        ).shift(UP * 0.5)
        
        label1 = Text(
            "反向-3 = +3",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_POSITIVE
        ).next_to(arrow1, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow1),
            Write(label1),
            run_time=0.7
        )
        self.play(dot.animate.move_to(number_line.n2p(3)), run_time=0.8)
        
        # 第二次反向跳
        arrow2 = Arrow(
            number_line.n2p(3),
            number_line.n2p(6),
            color=self.COLOR_POSITIVE,
            buff=0,
            stroke_width=6
        ).shift(UP * 0.5)
        
        label2 = Text(
            "再反向-3 = +3",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_POSITIVE
        ).next_to(arrow2, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow2),
            Write(label2),
            run_time=0.7
        )
        self.play(dot.animate.move_to(number_line.n2p(6)), run_time=0.8)
        
        # 终点标记
        end_dot = Dot(number_line.n2p(6), color=YELLOW, radius=0.15)
        self.play(
            Transform(dot, end_dot),
            Flash(end_dot, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        
        # 结果
        result = MathTex(
            "(-3)", r"\times", "(-2)", "=", "+6",
            font_size=40
        ).move_to(DOWN * 3)
        result[0].set_color(self.COLOR_NEGATIVE)
        result[2].set_color(self.COLOR_NEGATIVE)
        result[4].set_color(self.COLOR_POSITIVE)
        
        self.play(
            TransformMatchingTex(formula.copy(), result),
            run_time=0.8
        )
        
        # 关键洞察
        insight = Text(
            "负负得正！",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        box = SurroundingRectangle(result[4], color=self.COLOR_POSITIVE, buff=0.15)
        
        self.play(
            Create(box),
            Write(insight),
            run_time=0.8
        )
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(number_line),
            FadeOut(dot),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(hint),
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(result),
            FadeOut(box),
            FadeOut(insight),
            run_time=0.6
        )
    
    def show_positive_times_negative(self):
        """场景5: 异号得负 - 正×负"""
        # 示例公式
        formula = MathTex(
            "(+3)", r"\times", "(-2)", "=", "?",
            font_size=40
        ).move_to(UP * 5)
        formula[0].set_color(self.COLOR_POSITIVE)
        formula[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(formula), run_time=0.8)
        
        # 数轴
        number_line = NumberLine(
            x_range=[-10, 4, 2],
            length=7,
            include_numbers=True,
            label_direction=DOWN,
            font_size=20,
            include_tip=True
        ).move_to(UP * 1.5)
        
        self.play(Create(number_line), run_time=1.0)
        
        # 说明
        explanation = Text(
            "从0开始，向左跳2个单位，跳3次",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        # 起点
        dot = Dot(number_line.n2p(0), color=self.COLOR_NEGATIVE, radius=0.12)
        self.play(FadeIn(dot, scale=0.5), run_time=0.3)
        
        # 三次跳跃
        positions = [0, -2, -4, -6]
        for i in range(3):
            arrow = Arrow(
                number_line.n2p(positions[i]),
                number_line.n2p(positions[i + 1]),
                color=self.COLOR_NEGATIVE,
                buff=0,
                stroke_width=6
            ).shift(UP * (0.5 + i * 0.3))
            
            label = Text(
                "−2",
                font=self.FONT_CHINESE,
                font_size=24,
                color=self.COLOR_NEGATIVE
            ).next_to(arrow, UP, buff=0.1)
            
            self.play(
                GrowArrow(arrow),
                Write(label),
                run_time=0.5
            )
            self.play(
                dot.animate.move_to(number_line.n2p(positions[i + 1])),
                run_time=0.6
            )
        
        # 终点标记
        end_dot = Dot(number_line.n2p(-6), color=YELLOW, radius=0.15)
        self.play(
            Transform(dot, end_dot),
            Flash(end_dot, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        
        # 结果
        result = MathTex(
            "(+3)", r"\times", "(-2)", "=", "-6",
            font_size=40
        ).move_to(DOWN * 3)
        result[0].set_color(self.COLOR_POSITIVE)
        result[2].set_color(self.COLOR_NEGATIVE)
        result[4].set_color(self.COLOR_NEGATIVE)
        
        self.play(
            TransformMatchingTex(formula.copy(), result),
            run_time=0.8
        )
        
        box = SurroundingRectangle(result[4], color=self.COLOR_NEGATIVE, buff=0.15)
        self.play(Create(box), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info and mob != self.rules_summary],
            run_time=0.6
        )
    
    def show_multiple_multiplication(self):
        """场景6: 多个数相乘规律"""
        # 清理之前的规则总览
        self.play(FadeOut(self.rules_summary), run_time=0.4)
        
        # 标题
        title = Text(
            "负因数个数决定符号",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 示例1: 2个负数（偶数）
        example1 = VGroup(
            MathTex(
                "(-2)", r"\times", "(-3)", "=", "+6",
                font_size=32
            ),
            Text(
                "2个负数（偶数）→ 正",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_POSITIVE
            ).shift(DOWN * 0.5)
        ).move_to(UP * 4)
        
        example1[0][0].set_color(self.COLOR_NEGATIVE)
        example1[0][2].set_color(self.COLOR_NEGATIVE)
        example1[0][4].set_color(self.COLOR_POSITIVE)
        
        self.play(FadeIn(example1[0]), run_time=0.6)
        
        # 计数动画
        count_1 = VGroup(
            Circle(radius=0.15, color=YELLOW).move_to(example1[0][0].get_center() + UP * 0.5),
            Text("1", font_size=16, color=YELLOW).move_to(example1[0][0].get_center() + UP * 0.5)
        )
        count_2 = VGroup(
            Circle(radius=0.15, color=YELLOW).move_to(example1[0][2].get_center() + UP * 0.5),
            Text("2", font_size=16, color=YELLOW).move_to(example1[0][2].get_center() + UP * 0.5)
        )
        
        self.play(FadeIn(count_1), run_time=0.3)
        self.play(FadeIn(count_2), run_time=0.3)
        self.play(FadeIn(example1[1]), run_time=0.4)
        
        box1 = SurroundingRectangle(example1[0][4], color=self.COLOR_POSITIVE, buff=0.1)
        self.play(Create(box1), run_time=0.4)
        self.wait(0.5)
        
        self.play(FadeOut(count_1), FadeOut(count_2), run_time=0.3)
        
        # 示例2: 3个负数（奇数）
        example2 = VGroup(
            MathTex(
                "(-2)", r"\times", "(-3)", r"\times", "(-1)", "=", "-6",
                font_size=32
            ),
            Text(
                "3个负数（奇数）→ 负",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_NEGATIVE
            ).shift(DOWN * 0.5)
        ).move_to(UP * 1.5)
        
        example2[0][0].set_color(self.COLOR_NEGATIVE)
        example2[0][2].set_color(self.COLOR_NEGATIVE)
        example2[0][4].set_color(self.COLOR_NEGATIVE)
        example2[0][6].set_color(self.COLOR_NEGATIVE)
        
        self.play(FadeIn(example2[0]), run_time=0.6)
        
        # 计数动画
        count_positions = [example2[0][0], example2[0][2], example2[0][4]]
        counts = VGroup()
        for i, pos in enumerate(count_positions):
            count = VGroup(
                Circle(radius=0.15, color=YELLOW).move_to(pos.get_center() + UP * 0.5),
                Text(str(i + 1), font_size=16, color=YELLOW).move_to(pos.get_center() + UP * 0.5)
            )
            counts.add(count)
            self.play(FadeIn(count), run_time=0.2)
        
        self.play(FadeIn(example2[1]), run_time=0.4)
        
        box2 = SurroundingRectangle(example2[0][6], color=self.COLOR_NEGATIVE, buff=0.1)
        self.play(Create(box2), run_time=0.4)
        self.wait(0.5)
        
        self.play(FadeOut(counts), run_time=0.3)
        
        # 示例3: 4个负数（偶数）
        example3 = VGroup(
            MathTex(
                "(-1)", r"\times", "(-1)", r"\times", "(-1)", r"\times", "(-1)", "=", "+1",
                font_size=28
            ),
            Text(
                "4个负数（偶数）→ 正",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_POSITIVE
            ).shift(DOWN * 0.5)
        ).move_to(DOWN * 1)
        
        example3[0][0].set_color(self.COLOR_NEGATIVE)
        example3[0][2].set_color(self.COLOR_NEGATIVE)
        example3[0][4].set_color(self.COLOR_NEGATIVE)
        example3[0][6].set_color(self.COLOR_NEGATIVE)
        example3[0][8].set_color(self.COLOR_POSITIVE)
        
        self.play(FadeIn(example3[0]), run_time=0.6)
        self.play(FadeIn(example3[1]), run_time=0.4)
        
        box3 = SurroundingRectangle(example3[0][8], color=self.COLOR_POSITIVE, buff=0.1)
        self.play(Create(box3), run_time=0.4)
        
        # 核心规律总结
        summary = VGroup(
            Text(
                "★ 偶数个负因数 → 结果为正",
                font=self.FONT_CHINESE,
                font_size=24,
                color=self.COLOR_POSITIVE
            ),
            Text(
                "★ 奇数个负因数 → 结果为负",
                font=self.FONT_CHINESE,
                font_size=24,
                color=self.COLOR_NEGATIVE
            ).shift(DOWN * 0.6)
        ).move_to(DOWN * 3.5)
        
        self.play(Write(summary), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 核心规律卡片
        cards = VGroup()
        
        card_data = [
            ("同号相乘", "结果为正", self.COLOR_POSITIVE, "(+)×(+)=+ 或 (−)×(−)=+"),
            ("异号相乘", "结果为负", self.COLOR_NEGATIVE, "(+)×(−)=− 或 (−)×(+)=−"),
            ("偶数个负因数", "结果为正", self.COLOR_POSITIVE, "负负得正"),
            ("奇数个负因数", "结果为负", self.COLOR_NEGATIVE, "一负留负"),
        ]
        
        for i, (title, conclusion, color, detail) in enumerate(card_data):
            # 卡片背景
            card_bg = RoundedRectangle(
                width=7,
                height=1.2,
                corner_radius=0.2,
                fill_color=color,
                fill_opacity=0.2,
                stroke_color=color,
                stroke_width=2
            )
            
            # 标题
            card_title = Text(
                title,
                font=self.FONT_CHINESE,
                font_size=24,
                color=WHITE,
                weight=BOLD
            )
            
            # 结论
            card_conclusion = Text(
                conclusion,
                font=self.FONT_CHINESE,
                font_size=20,
                color=color
            )
            
            # 详情
            card_detail = Text(
                detail,
                font=self.FONT_CHINESE,
                font_size=16,
                color=GRAY_A
            )
            
            # 组合
            card_content = VGroup(card_title, card_conclusion, card_detail).arrange(RIGHT, buff=0.3)
            card = VGroup(card_bg, card_content)
            card_content.move_to(card_bg.get_center())
            
            card.move_to(UP * (3 - i * 1.8))
            card.shift(LEFT * 10)  # 初始位置在左侧外
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 卡片闪烁
        self.play(
            *[Flash(card, color=WHITE, flash_radius=0.5) for card in cards],
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车\n@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 4)
        
        self.play(
            FadeOut(cards),
            Transform(self.author_info, author_big),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰 - 小加号和减号围绕
        decorations = VGroup()
        symbols = ["+", "−", "+", "−", "+", "−"]
        for i, symbol in enumerate(symbols):
            angle = i * PI / 3
            pos = 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            if symbol == "+":
                deco = Text(symbol, font_size=40, color=self.COLOR_POSITIVE)
            else:
                deco = Text(symbol, font_size=40, color=self.COLOR_NEGATIVE)
            
            deco.move_to(follow_text.get_center() + pos)
            decorations.add(deco)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.6
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql rational_multiplication.py RationalMultiplication  # 快速预览
# manim -qh rational_multiplication.py RationalMultiplication   # 高质量 1080p
# manim -qk rational_multiplication.py RationalMultiplication   # 4K质量