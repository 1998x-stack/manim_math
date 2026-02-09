"""
有理数的除法 - Rational Number Division
使用 Manim 创建的六年级数学教学视频

内容: 有理数除法法则及其应用
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


class RationalDivision(Scene):
    """
    有理数除法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 核心法则 - 除法转乘法
    3. 倒数概念
    4. 符号法则 - 同号得正
    5. 符号法则 - 异号得负
    6. 特殊情况 - 0的除法
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
        self.COLOR_RECIPROCAL = "#9b59b6"   # 紫色 - 倒数
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 36
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 22
        self.FONT_SIZE_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_core_rule()
        self.show_reciprocal_concept()
        self.show_same_sign_positive()
        self.show_different_sign_negative()
        self.show_zero_division()
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
                "你能算出来吗？",
                font=self.FONT_CHINESE,
                font_size=32,
                color=WHITE
            ),
            MathTex(
                "(-6)", r"\div", "(-2)", "=", "?",
                font_size=48
            ).shift(DOWN * 0.6)
        ).move_to(UP * 2)
        
        hook_question[1][0].set_color(self.COLOR_NEGATIVE)
        hook_question[1][2].set_color(self.COLOR_NEGATIVE)
        hook_question[1][4].set_color(self.COLOR_HIGHLIGHT)
        
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
    
    def show_core_rule(self):
        """场景2: 核心法则 - 除法转乘法"""
        # 标题
        title = Text(
            "除法的秘密",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 核心公式 - 除法形式
        division = MathTex(
            "a", r"\div", "b",
            font_size=40
        ).move_to(UP * 4)
        
        self.play(FadeIn(division, shift=UP * 0.3), run_time=0.8)
        
        # 等号和箭头
        equals_arrow = VGroup(
            MathTex("=", font_size=40),
            Arrow(
                UP * 3,
                UP * 2,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=6
            )
        )
        equals_arrow[0].next_to(division, RIGHT, buff=0.5)
        equals_arrow[1].next_to(equals_arrow[0], DOWN, buff=0.3)
        
        # 乘法形式
        multiplication = MathTex(
            "a", r"\times", r"\frac{1}{b}",
            font_size=40
        ).next_to(equals_arrow[0], RIGHT, buff=0.5)
        
        multiplication[2].set_color(self.COLOR_RECIPROCAL)
        
        # 转换动画
        self.play(Write(equals_arrow[0]), run_time=0.5)
        self.play(GrowArrow(equals_arrow[1]), run_time=0.6)
        self.play(Write(multiplication), run_time=1.0)
        
        # 说明文字
        explanation = Text(
            "除以一个数 = 乘以这个数的倒数",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.8)
        
        # 高亮倒数部分
        reciprocal_box = SurroundingRectangle(
            multiplication[2],
            color=self.COLOR_RECIPROCAL,
            buff=0.15
        )
        reciprocal_label = Text(
            "倒数",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_RECIPROCAL
        ).next_to(reciprocal_box, DOWN, buff=0.2)
        
        self.play(
            Create(reciprocal_box),
            Write(reciprocal_label),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 缩小并移至侧边
        core_formula = VGroup(
            division, equals_arrow[0], multiplication
        )
        
        self.play(
            FadeOut(title),
            FadeOut(equals_arrow[1]),
            FadeOut(explanation),
            FadeOut(reciprocal_box),
            FadeOut(reciprocal_label),
            core_formula.animate.scale(0.5).to_edge(LEFT, buff=0.3).shift(UP * 5),
            run_time=0.8
        )
        
        # 保存引用
        self.core_formula = core_formula
    
    def show_reciprocal_concept(self):
        """场景3: 倒数概念"""
        # 标题
        title = Text(
            "什么是倒数？",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_RECIPROCAL,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "两个数的乘积为1，它们互为倒数",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 5)
        
        self.play(FadeIn(definition, shift=DOWN * 0.2), run_time=0.6)
        
        # 示例1: 2的倒数
        example1 = VGroup(
            MathTex(
                "2", r"\times", r"\frac{1}{2}", "=", "1",
                font_size=32
            ),
            Text(
                "2的倒数是1/2",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_AUXILIARY
            ).shift(DOWN * 0.5)
        ).move_to(UP * 3)
        
        example1[0][2].set_color(self.COLOR_RECIPROCAL)
        
        self.play(Write(example1[0]), run_time=0.8)
        
        # 验证
        check1 = Text(
            "✓",
            font_size=40,
            color=self.COLOR_POSITIVE
        ).next_to(example1[0], RIGHT, buff=0.5)
        
        self.play(FadeIn(check1, scale=0.5), run_time=0.4)
        self.play(FadeIn(example1[1]), run_time=0.4)
        self.wait(0.5)
        
        # 示例2: -3的倒数
        example2 = VGroup(
            MathTex(
                "(-3)", r"\times", r"\left(-\frac{1}{3}\right)", "=", "1",
                font_size=32
            ),
            Text(
                "-3的倒数是-1/3",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_AUXILIARY
            ).shift(DOWN * 0.5)
        ).move_to(UP * 1)
        
        example2[0][0].set_color(self.COLOR_NEGATIVE)
        example2[0][2].set_color(self.COLOR_RECIPROCAL)
        
        self.play(Write(example2[0]), run_time=0.8)
        
        check2 = Text(
            "✓",
            font_size=40,
            color=self.COLOR_POSITIVE
        ).next_to(example2[0], RIGHT, buff=0.5)
        
        self.play(FadeIn(check2, scale=0.5), run_time=0.4)
        self.play(FadeIn(example2[1]), run_time=0.4)
        self.wait(0.5)
        
        # 示例3: 1/4的倒数
        example3 = VGroup(
            MathTex(
                r"\frac{1}{4}", r"\times", "4", "=", "1",
                font_size=32
            ),
            Text(
                "1/4的倒数是4",
                font=self.FONT_CHINESE,
                font_size=20,
                color=self.COLOR_AUXILIARY
            ).shift(DOWN * 0.5)
        ).move_to(DOWN * 1)
        
        example3[0][2].set_color(self.COLOR_RECIPROCAL)
        
        self.play(Write(example3[0]), run_time=0.8)
        
        check3 = Text(
            "✓",
            font_size=40,
            color=self.COLOR_POSITIVE
        ).next_to(example3[0], RIGHT, buff=0.5)
        
        self.play(FadeIn(check3, scale=0.5), run_time=0.4)
        self.play(FadeIn(example3[1]), run_time=0.4)
        
        # 关键提示
        key_hint = Text(
            "求倒数：分子分母互换位置",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(key_hint), run_time=0.8)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(example1),
            FadeOut(example2),
            FadeOut(example3),
            FadeOut(check1),
            FadeOut(check2),
            FadeOut(check3),
            FadeOut(key_hint),
            run_time=0.6
        )
    
    def show_same_sign_positive(self):
        """场景4: 符号法则 - 同号得正"""
        # 标题
        title = Text(
            "同号相除 → 结果为正",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_POSITIVE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 原问题
        problem = MathTex(
            "(-6)", r"\div", "(-2)",
            font_size=40
        ).move_to(UP * 4.5)
        
        problem[0].set_color(self.COLOR_NEGATIVE)
        problem[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(FadeIn(problem, shift=DOWN * 0.3), run_time=0.6)
        
        # 转换箭头
        arrow = Arrow(
            UP * 3.8,
            UP * 2.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        )
        
        conversion_text = Text(
            "转换为乘法",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).next_to(arrow, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(arrow),
            Write(conversion_text),
            run_time=0.6
        )
        
        # 乘法形式
        multiplication = MathTex(
            "(-6)", r"\times", r"\left(-\frac{1}{2}\right)",
            font_size=40
        ).move_to(UP * 2)
        
        multiplication[0].set_color(self.COLOR_NEGATIVE)
        multiplication[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(multiplication), run_time=0.8)
        
        # 符号标注
        sign_negative = Text(
            "−",
            font_size=30,
            color=self.COLOR_NEGATIVE
        ).next_to(multiplication[0], UP, buff=0.3)
        
        sign_negative2 = Text(
            "−",
            font_size=30,
            color=self.COLOR_NEGATIVE
        ).next_to(multiplication[2], UP, buff=0.3)
        
        self.play(
            FadeIn(sign_negative),
            FadeIn(sign_negative2),
            run_time=0.5
        )
        
        # 符号规则
        rule_hint = Text(
            "负 × 负 = 正",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_POSITIVE,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(Write(rule_hint), run_time=0.8)
        self.wait(0.6)
        
        # 结果
        result = MathTex(
            "=", "+3",
            font_size=48
        ).move_to(DOWN * 2.5)
        
        result[1].set_color(self.COLOR_POSITIVE)
        
        self.play(Write(result), run_time=0.8)
        
        # 高亮答案
        result_box = SurroundingRectangle(
            result[1],
            color=self.COLOR_POSITIVE,
            buff=0.2
        )
        
        self.play(
            Create(result_box),
            Flash(result[1], color=self.COLOR_POSITIVE, flash_radius=0.5),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(arrow),
            FadeOut(conversion_text),
            FadeOut(multiplication),
            FadeOut(sign_negative),
            FadeOut(sign_negative2),
            FadeOut(rule_hint),
            FadeOut(result),
            FadeOut(result_box),
            run_time=0.6
        )
    
    def show_different_sign_negative(self):
        """场景5: 符号法则 - 异号得负"""
        # 标题
        title = Text(
            "异号相除 → 结果为负",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_NEGATIVE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 原问题
        problem = MathTex(
            "(+8)", r"\div", "(-4)",
            font_size=40
        ).move_to(UP * 4.5)
        
        problem[0].set_color(self.COLOR_POSITIVE)
        problem[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(FadeIn(problem, shift=DOWN * 0.3), run_time=0.6)
        
        # 转换箭头
        arrow = Arrow(
            UP * 3.8,
            UP * 2.8,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=6
        )
        
        conversion_text = Text(
            "转换为乘法",
            font=self.FONT_CHINESE,
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).next_to(arrow, RIGHT, buff=0.2)
        
        self.play(
            GrowArrow(arrow),
            Write(conversion_text),
            run_time=0.6
        )
        
        # 乘法形式
        multiplication = MathTex(
            "(+8)", r"\times", r"\left(-\frac{1}{4}\right)",
            font_size=40
        ).move_to(UP * 2)
        
        multiplication[0].set_color(self.COLOR_POSITIVE)
        multiplication[2].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(multiplication), run_time=0.8)
        
        # 符号标注
        sign_positive = Text(
            "+",
            font_size=30,
            color=self.COLOR_POSITIVE
        ).next_to(multiplication[0], UP, buff=0.3)
        
        sign_negative = Text(
            "−",
            font_size=30,
            color=self.COLOR_NEGATIVE
        ).next_to(multiplication[2], UP, buff=0.3)
        
        self.play(
            FadeIn(sign_positive),
            FadeIn(sign_negative),
            run_time=0.5
        )
        
        # 符号规则
        rule_hint = Text(
            "正 × 负 = 负",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_NEGATIVE,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(Write(rule_hint), run_time=0.8)
        self.wait(0.6)
        
        # 结果
        result = MathTex(
            "=", "-2",
            font_size=48
        ).move_to(DOWN * 2.5)
        
        result[1].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(result), run_time=0.8)
        
        # 高亮答案
        result_box = SurroundingRectangle(
            result[1],
            color=self.COLOR_NEGATIVE,
            buff=0.2
        )
        
        self.play(
            Create(result_box),
            Flash(result[1], color=self.COLOR_NEGATIVE, flash_radius=0.5),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(problem),
            FadeOut(arrow),
            FadeOut(conversion_text),
            FadeOut(multiplication),
            FadeOut(sign_positive),
            FadeOut(sign_negative),
            FadeOut(rule_hint),
            FadeOut(result),
            FadeOut(result_box),
            run_time=0.6
        )
    
    def show_zero_division(self):
        """场景6: 特殊情况 - 0的除法"""
        # 先清理侧边公式
        self.play(FadeOut(self.core_formula), run_time=0.4)
        
        # 标题
        title = Text(
            "特殊情况：0的除法",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 规则1: 0除以任何非零数
        rule1_title = Text(
            "规则1: 0除以任何非零数都得0",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(rule1_title, shift=DOWN * 0.2), run_time=0.6)
        
        # 示例
        example1 = MathTex(
            "0", r"\div", "5", "=", "0",
            font_size=36
        ).move_to(UP * 3.5)
        
        self.play(Write(example1), run_time=0.8)
        
        # 验证标记
        check1 = Text(
            "✓",
            font_size=50,
            color=self.COLOR_POSITIVE
        ).next_to(example1, RIGHT, buff=0.5)
        
        self.play(FadeIn(check1, scale=0.5), run_time=0.4)
        self.wait(0.8)
        
        # 规则2: 除数不能为0
        rule2_title = Text(
            "规则2: 除数不能为0！",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_NEGATIVE,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(rule2_title, shift=DOWN * 0.2), run_time=0.6)
        
        # 错误示例
        example2 = MathTex(
            "5", r"\div", "0", "=", "?",
            font_size=36
        ).move_to(UP * 0.5)
        
        self.play(Write(example2), run_time=0.8)
        
        # 禁止标志（圆圈加斜杠）
        prohibition = VGroup(
            Circle(radius=0.6, color=RED, stroke_width=6),
            Line(
                0.6 * UL * 0.7,
                0.6 * DR * 0.7,
                color=RED,
                stroke_width=6
            )
        ).next_to(example2, RIGHT, buff=0.5)
        
        self.play(Create(prohibition), run_time=0.8)
        
        # 警告文字
        warning = Text(
            "无意义！",
            font=self.FONT_CHINESE,
            font_size=32,
            color=RED,
            weight=BOLD
        ).next_to(prohibition, DOWN, buff=0.5)
        
        self.play(
            Write(warning),
            Flash(prohibition, color=RED, flash_radius=0.8),
            run_time=0.8
        )
        
        # 重点强调
        key_point = VGroup(
            Text(
                "⚠️ 重要：",
                font=self.FONT_CHINESE,
                font_size=28,
                color=self.COLOR_HIGHLIGHT
            ),
            Text(
                "除数永远不能为0",
                font=self.FONT_CHINESE,
                font_size=28,
                color=self.COLOR_HIGHLIGHT,
                weight=BOLD
            ).shift(DOWN * 0.6)
        ).move_to(DOWN * 3)
        
        self.play(Write(key_point), run_time=1.0)
        
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
            ("除法转乘法", "a ÷ b = a × (1/b)", self.COLOR_PRIMARY),
            ("倒数", "分子分母互换", self.COLOR_RECIPROCAL),
            ("同号得正", "(−)÷(−)=+ 或 (+)÷(+)=+", self.COLOR_POSITIVE),
            ("异号得负", "(+)÷(−)=− 或 (−)÷(+)=−", self.COLOR_NEGATIVE),
            ("0的规则", "0÷a=0, a÷0无意义", self.COLOR_HIGHLIGHT),
        ]
        
        for i, (title, content, color) in enumerate(card_data):
            # 卡片背景
            card_bg = RoundedRectangle(
                width=7,
                height=1.0,
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
                font_size=22,
                color=WHITE,
                weight=BOLD
            )
            
            # 内容
            card_content = MathTex(
                content,
                font_size=20,
                color=color
            )
            
            # 组合
            card_text = VGroup(card_title, card_content).arrange(RIGHT, buff=0.3)
            card = VGroup(card_bg, card_text)
            card_text.move_to(card_bg.get_center())
            
            card.move_to(UP * (4.5 - i * 1.5))
            card.shift(LEFT * 10)  # 初始位置在左侧外
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.15)
        
        # 卡片闪烁
        self.play(
            *[Flash(card, color=WHITE, flash_radius=0.4) for card in cards],
            run_time=0.8
        )
        
        self.wait(1.2)
        
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车\n@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE,
            line_spacing=1.2
        ).move_to(DOWN * 4.5)
        
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
        ).move_to(DOWN * 6.5)
        
        self.play(Write(follow_text), run_time=0.8)
        
        # 装饰 - 除号和乘号围绕
        decorations = VGroup()
        symbols = ["÷", "×", "÷", "×", "÷", "×"]
        for i, symbol in enumerate(symbols):
            angle = i * PI / 3
            pos = 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            if symbol == "÷":
                deco = MathTex(r"\div", font_size=40, color=self.COLOR_PRIMARY)
            else:
                deco = MathTex(r"\times", font_size=40, color=self.COLOR_RECIPROCAL)
            
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
# manim -pql rational_division.py RationalDivision  # 快速预览
# manim -qh rational_division.py RationalDivision   # 高质量 1080p
# manim -qk rational_division.py RationalDivision   # 4K质量