"""
因式分解——分组分解法 教学动画
Factorization - Grouping Method Teaching Animation

使用 Manim 创建的中学数学教学视频
内容: 分组分解法的定义、例题和技巧
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

运行命令:
manim -pql factorization_grouping.py FactorizationGrouping  # 快速预览
manim -qh factorization_grouping.py FactorizationGrouping   # 高质量渲染
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FactorizationGrouping(Scene):
    """
    分组分解法教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 概念介绍
    3. 例题1: ax + ay + bx + by
    4. 例题2: x² - y² + x - y
    5. 对比总结
    6. 技巧提示
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 分组标识
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮强调
        self.COLOR_SUCCESS = "#2ecc71"        # 绿色 - 成功/最终结果
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
        self.COLOR_GROUP_A = "#9b59b6"        # 紫色 - 第一组
        self.COLOR_GROUP_B = "#f39c12"        # 橙色 - 第二组
        
        # 字体大小
        self.FONT_TITLE = 40
        self.FONT_SUBTITLE = 32
        self.FONT_BODY = 26
        self.FONT_SMALL = 22
        self.FONT_AUTHOR = 20
        self.FONT_FORMULA = 32
        
        # 执行动画序列
        self.show_opening()
        self.show_concept()
        self.show_example1()
        self.show_example2()
        self.show_comparison()
        self.show_tips()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 (4秒)"""
        # 作者信息 (顶部，始终保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这个式子怎么分解?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 困难公式
        problem_eq = MathTex(
            r"ax + ay + bx + by = ?",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3)
        
        self.play(FadeIn(problem_eq), run_time=0.5)
        self.play(Flash(problem_eq, color=YELLOW, flash_radius=0.5), run_time=0.4)
        self.wait(0.4)
        
        # 提示文字
        hint_text = Text(
            "用分组分解法!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 1)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(problem_eq),
            FadeOut(hint_text),
            run_time=0.5
        )
    
    def show_concept(self):
        """场景2: 概念介绍 (8秒)"""
        # 标题
        title = Text(
            "分组分解法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "将多项式的项分组，使每组都能分解",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)
        
        # 策略要点
        strategy_1 = Text(
            "① 适当分组",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_GROUP_A
        ).move_to(UP * 2)
        
        strategy_2 = Text(
            "② 各组提取公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_GROUP_B
        ).move_to(UP * 1)
        
        strategy_3 = Text(
            "③ 继续分解共同因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0)
        
        self.play(FadeIn(strategy_1), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(strategy_2), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(strategy_3), run_time=0.6)
        self.wait(0.5)
        
        # 整体高亮
        strategies = VGroup(strategy_1, strategy_2, strategy_3)
        for strategy in strategies:
            self.play(Flash(strategy, color=YELLOW, flash_radius=0.3), run_time=0.3)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(strategies),
            run_time=0.6
        )
    
    def show_example1(self):
        """场景3: 例题1 - ax + ay + bx + by (15秒)"""
        # 例题标题
        example_title = Text(
            "例题1",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(example_title), run_time=0.6)
        
        # Step 0: 原始公式
        eq_step0 = MathTex(
            r"ax", r"+", r"ay", r"+", r"bx", r"+", r"by",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(Write(eq_step0), run_time=1.0)
        self.wait(0.5)
        
        # 高亮第一组 (ax + ay)
        self.play(
            eq_step0[0].animate.set_color(self.COLOR_GROUP_A),  # ax
            eq_step0[2].animate.set_color(self.COLOR_GROUP_A),  # ay
            run_time=0.5
        )
        self.wait(0.3)
        
        # 高亮第二组 (bx + by)
        self.play(
            eq_step0[4].animate.set_color(self.COLOR_GROUP_B),  # bx
            eq_step0[6].animate.set_color(self.COLOR_GROUP_B),  # by
            run_time=0.5
        )
        self.wait(0.3)
        
        # 说明文字
        explain_1 = Text(
            "分成两组",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(explain_1), run_time=0.4)
        self.wait(0.6)
        
        # Step 1: 添加括号
        eq_step1 = MathTex(
            r"(", r"ax", r"+", r"ay", r")", r"+", r"(", r"bx", r"+", r"by", r")",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        # 设置颜色
        eq_step1[1].set_color(self.COLOR_GROUP_A)   # ax
        eq_step1[3].set_color(self.COLOR_GROUP_A)   # ay
        eq_step1[7].set_color(self.COLOR_GROUP_B)   # bx
        eq_step1[9].set_color(self.COLOR_GROUP_B)   # by
        
        self.play(
            TransformMatchingTex(eq_step0, eq_step1),
            FadeOut(explain_1),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 提示提取公因式
        explain_2 = Text(
            "提取公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(explain_2), run_time=0.4)
        self.wait(0.6)
        
        # Step 2: 提取公因式
        eq_step2 = MathTex(
            r"a", r"(", r"x", r"+", r"y", r")", r"+", r"b", r"(", r"x", r"+", r"y", r")",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        # 设置颜色
        eq_step2[0].set_color(self.COLOR_GROUP_A)   # a
        eq_step2[7].set_color(self.COLOR_GROUP_B)   # b
        
        self.play(
            TransformMatchingTex(eq_step1, eq_step2),
            FadeOut(explain_2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 标识公因式 (x+y)
        brace_1 = Brace(eq_step2[1:6], direction=DOWN, color=self.COLOR_HIGHLIGHT)
        brace_2 = Brace(eq_step2[8:13], direction=DOWN, color=self.COLOR_HIGHLIGHT)
        
        self.play(
            FadeIn(brace_1),
            FadeIn(brace_2),
            run_time=0.5
        )
        
        # 高亮公因式
        self.play(
            eq_step2[1:6].animate.set_color(self.COLOR_HIGHLIGHT),   # (x+y)
            eq_step2[8:13].animate.set_color(self.COLOR_HIGHLIGHT),  # (x+y)
            run_time=0.6
        )
        self.wait(0.4)
        
        # 提示继续提取
        explain_3 = Text(
            "继续提取 (x+y)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(explain_3), run_time=0.4)
        self.wait(0.6)
        
        # Step 3: 最终答案
        eq_final = MathTex(
            r"(", r"a", r"+", r"b", r")", r"(", r"x", r"+", r"y", r")",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 3.5)
        
        self.play(
            TransformMatchingTex(eq_step2, eq_final),
            FadeOut(brace_1),
            FadeOut(brace_2),
            FadeOut(explain_3),
            run_time=1.0
        )
        
        # 成功特效
        self.play(Flash(eq_final, color=self.COLOR_SUCCESS, flash_radius=0.6), run_time=0.5)
        self.wait(1.0)
        
        # 清理并保留最终答案
        self.play(FadeOut(example_title), run_time=0.4)
        
        # 将最终答案移到顶部作为参考
        self.eq1_final = eq_final.copy()
        self.play(
            eq_final.animate.scale(0.7).move_to(UP * 6 + LEFT * 2),
            run_time=0.6
        )
        self.wait(0.3)
    
    def show_example2(self):
        """场景4: 例题2 - x² - y² + x - y (15秒)"""
        # 例题标题
        example_title_2 = Text(
            "例题2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(example_title_2), run_time=0.6)
        
        # Step 0: 原始公式
        eq2_step0 = MathTex(
            r"x^2", r"-", r"y^2", r"+", r"x", r"-", r"y",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(Write(eq2_step0), run_time=1.0)
        self.wait(0.5)
        
        # 高亮第一组 (x² - y²)
        self.play(
            eq2_step0[0].animate.set_color(self.COLOR_GROUP_A),  # x²
            eq2_step0[2].animate.set_color(self.COLOR_GROUP_A),  # y²
            run_time=0.5
        )
        self.wait(0.3)
        
        # 高亮第二组 (x - y)
        self.play(
            eq2_step0[4].animate.set_color(self.COLOR_GROUP_B),  # x
            eq2_step0[6].animate.set_color(self.COLOR_GROUP_B),  # y
            run_time=0.5
        )
        self.wait(0.3)
        
        # Step 1: 添加括号
        eq2_step1 = MathTex(
            r"(", r"x^2", r"-", r"y^2", r")", r"+", r"(", r"x", r"-", r"y", r")",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        # 设置颜色
        eq2_step1[1].set_color(self.COLOR_GROUP_A)   # x²
        eq2_step1[3].set_color(self.COLOR_GROUP_A)   # y²
        eq2_step1[7].set_color(self.COLOR_GROUP_B)   # x
        eq2_step1[9].set_color(self.COLOR_GROUP_B)   # y
        
        self.play(TransformMatchingTex(eq2_step0, eq2_step1), run_time=1.0)
        self.wait(0.5)
        
        # 提示平方差公式
        explain_1 = Text(
            "平方差公式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        formula_hint = MathTex(
            r"a^2 - b^2 = (a+b)(a-b)",
            font_size=self.FONT_SMALL,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1)
        
        self.play(
            FadeIn(explain_1),
            FadeIn(formula_hint),
            run_time=0.8
        )
        self.wait(1.0)
        
        # Step 2: 应用平方差公式
        eq2_step2 = MathTex(
            r"(", r"x", r"+", r"y", r")", r"(", r"x", r"-", r"y", r")", r"+", r"(", r"x", r"-", r"y", r")",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(
            TransformMatchingTex(eq2_step1, eq2_step2),
            FadeOut(explain_1),
            FadeOut(formula_hint),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 标识公因式 (x-y)
        brace_1 = Brace(eq2_step2[5:10], direction=DOWN, color=self.COLOR_HIGHLIGHT)
        brace_2 = Brace(eq2_step2[11:16], direction=DOWN, color=self.COLOR_HIGHLIGHT)
        
        self.play(
            FadeIn(brace_1),
            FadeIn(brace_2),
            run_time=0.5
        )
        
        # 高亮公因式
        self.play(
            eq2_step2[5:10].animate.set_color(self.COLOR_HIGHLIGHT),   # (x-y)
            eq2_step2[11:16].animate.set_color(self.COLOR_HIGHLIGHT),  # (x-y)
            run_time=0.6
        )
        self.wait(0.4)
        
        # 提示提取
        explain_2 = Text(
            "提取 (x-y)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 2)
        
        self.play(FadeIn(explain_2), run_time=0.4)
        self.wait(0.6)
        
        # Step 3: 最终答案
        eq2_final = MathTex(
            r"(", r"x", r"-", r"y", r")", r"(", r"x", r"+", r"y", r"+", r"1", r")",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 3.5)
        
        self.play(
            TransformMatchingTex(eq2_step2, eq2_final),
            FadeOut(brace_1),
            FadeOut(brace_2),
            FadeOut(explain_2),
            run_time=1.0
        )
        
        # 成功特效
        self.play(Flash(eq2_final, color=self.COLOR_SUCCESS, flash_radius=0.6), run_time=0.5)
        self.wait(1.0)
        
        # 清理并保留最终答案
        self.play(FadeOut(example_title_2), run_time=0.4)
        
        # 将最终答案移到顶部
        self.eq2_final = eq2_final.copy()
        self.play(
            eq2_final.animate.scale(0.7).move_to(UP * 6 + RIGHT * 2),
            run_time=0.6
        )
        self.wait(0.3)
    
    def show_comparison(self):
        """场景5: 对比总结 (10秒)"""
        # 标题
        summary_title = Text(
            "对比总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.6)
        self.wait(0.5)
        
        # 移动两个例题到中间位置
        self.play(
            self.eq1_final.animate.scale(1.2).move_to(UP * 3 + LEFT * 0),
            self.eq2_final.animate.scale(1.2).move_to(UP * 1 + LEFT * 0),
            run_time=1.0
        )
        
        # 箭头和说明
        arrow_1 = Arrow(
            start=UP * 2.5 + RIGHT * 3,
            end=UP * 3 + RIGHT * 2.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        explain_1 = Text(
            "两组都有公因式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(arrow_1, RIGHT, buff=0.2)
        
        self.play(
            Create(arrow_1),
            FadeIn(explain_1),
            run_time=0.6
        )
        self.wait(0.5)
        
        arrow_2 = Arrow(
            start=UP * 0.5 + RIGHT * 3,
            end=UP * 1 + RIGHT * 2.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        explain_2 = Text(
            "先公式法，再提取",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).next_to(arrow_2, RIGHT, buff=0.2)
        
        self.play(
            Create(arrow_2),
            FadeIn(explain_2),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 关键点
        key_point = Text(
            "分组方式很关键!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(0.5)
        
        # 高亮闪烁
        self.play(
            Flash(self.eq1_final, color=YELLOW, flash_radius=0.5),
            Flash(self.eq2_final, color=YELLOW, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(self.eq1_final),
            FadeOut(self.eq2_final),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def show_tips(self):
        """场景6: 技巧提示 (8秒)"""
        # 标题
        tips_title = Text(
            "分组技巧",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(tips_title), run_time=0.8)
        
        # 创建技巧卡片
        cards = VGroup()
        
        # 卡片1
        card_1 = self.create_tip_card(
            "1",
            "看是否有公因式可提",
            self.COLOR_GROUP_A,
            UP * 3
        )
        cards.add(card_1)
        
        # 卡片2
        card_2 = self.create_tip_card(
            "2",
            "看能否用公式分解",
            self.COLOR_GROUP_B,
            UP * 1.5
        )
        cards.add(card_2)
        
        # 卡片3
        card_3 = self.create_tip_card(
            "3",
            "尝试不同分组方式",
            self.COLOR_HIGHLIGHT,
            UP * 0
        )
        cards.add(card_3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 10)  # 初始位置在左侧外
            self.play(card.animate.shift(RIGHT * 10), run_time=0.8)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.5)
        
        # 整体高亮
        for card in cards:
            self.play(Flash(card[0], color=WHITE, flash_radius=0.3), run_time=0.3)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(tips_title),
            FadeOut(cards),
            run_time=0.6
        )
    
    def create_tip_card(self, number, content, color, position):
        """创建技巧卡片"""
        # 图标圆
        icon = Circle(
            radius=0.25,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 序号
        number_text = Text(
            number,
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(icon.get_center())
        
        icon_group = VGroup(icon, number_text)
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon_group, content_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注 (7秒)"""
        # 作者名放大
        large_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(
            Transform(self.author_info, large_name),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我，掌握更多因式分解技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标 - 数学符号
        icon_size = 0.4
        icons = VGroup(
            # 括号
            MathTex(r"()", font_size=40, color=self.COLOR_GROUP_A),
            # 加号
            MathTex(r"+", font_size=40, color=self.COLOR_GROUP_B),
            # 等号
            MathTex(r"=", font_size=40, color=self.COLOR_HIGHLIGHT),
            # 乘号
            MathTex(r"\times", font_size=40, color=self.COLOR_SUCCESS)
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        # 旋转动画
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 测试场景 - 用于快速测试单个场景
class TestScene(Scene):
    """测试单个场景"""
    
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        # 这里可以复制粘贴单个场景的代码进行测试
        # 例如：只测试例题1
        pass