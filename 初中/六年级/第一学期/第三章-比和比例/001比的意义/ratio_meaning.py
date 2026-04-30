"""
比的意义教学动画 - The Meaning of Ratio
使用 Manim 创建的六年级数学教学视频

内容: 比的定义、写法、前项后项比值、与除法分数的关系
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


class RatioMeaning(Scene):
    """
    比的意义教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 比的定义
    3. 比的各部分名称
    4. 三者关系(核心)
    5. 重要提醒
    6. 实际应用与结尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 前项
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 后项
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 比值
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_RELATION = GOLD          # 金色 - 关系
        self.COLOR_WARNING = ORANGE         # 橙色 - 警告
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_RATIO_LARGE = 48
        self.FONT_RATIO_NORMAL = 32
        self.FONT_SMALL = 20
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_ratio_definition()
        self.show_ratio_components()
        self.show_three_relationships()
        self.show_important_warning()
        self.show_applications_and_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=self.FONT_AUTHOR,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "果汁:水 = 2:3\n是什么意思?",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 两个杯子(用矩形表示)
        cup_juice = VGroup(
            Rectangle(width=0.8, height=1.5, color=self.COLOR_PRIMARY, fill_opacity=0.3),
            Text("果汁", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY)
            .move_to(DOWN * 0.2)
        ).arrange(DOWN, buff=0.1).move_to(LEFT * 1.5 + UP * 3)
        
        cup_water = VGroup(
            Rectangle(width=0.8, height=1.5, color=self.COLOR_SECONDARY, fill_opacity=0.3),
            Text("水", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY)
            .move_to(DOWN * 0.2)
        ).arrange(DOWN, buff=0.1).move_to(RIGHT * 1.5 + UP * 3)
        
        self.play(
            FadeIn(cup_juice, scale=0.8),
            run_time=0.3
        )
        self.wait(0.2)
        self.play(
            FadeIn(cup_water, scale=0.8),
            run_time=0.3
        )
        
        # 比例符号
        ratio_symbol = VGroup(
            Text("2", font_size=self.FONT_RATIO_LARGE, color=self.COLOR_PRIMARY),
            Text(":", font_size=self.FONT_RATIO_LARGE, color=WHITE),
            Text("3", font_size=self.FONT_RATIO_LARGE, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1)
        
        self.play(Write(ratio_symbol), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(cup_juice),
            FadeOut(cup_water),
            FadeOut(ratio_symbol),
            run_time=0.5
        )
    
    def show_ratio_definition(self):
        """场景2: 比的定义"""
        # 标题
        title = Text(
            "什么是比?",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义框
        definition_box = RoundedRectangle(
            width=7,
            height=2.2,
            corner_radius=0.2,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 4.2)
        
        definition_text = VGroup(
            Text(
                "比",
                font="PingFang SC",
                font_size=self.FONT_SUBTITLE,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "表示两个数相除的关系",
                font="PingFang SC",
                font_size=self.FONT_BODY,
                color=self.COLOR_AUXILIARY
            )
        ).arrange(DOWN, buff=0.3).move_to(definition_box.get_center())
        
        self.play(
            FadeIn(definition_box, scale=0.9),
            run_time=0.6
        )
        self.play(Write(definition_text), run_time=1.2)
        
        # 两种写法
        format_title = Text(
            "比的写法:",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(FadeIn(format_title), run_time=0.5)
        
        # 写法1: a:b
        format_1 = VGroup(
            Text("方法1:", font="PingFang SC", font_size=self.FONT_SMALL, color=GRAY_A),
            VGroup(
                Text("a", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_PRIMARY),
                Text(":", font_size=self.FONT_RATIO_NORMAL, color=WHITE),
                Text("b", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_SECONDARY)
            ).arrange(RIGHT, buff=0.15)
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.5)
        
        self.play(Write(format_1), run_time=0.8)
        
        # 写法2: a/b - 修复这里：使用带有颜色的MathTex
        format_2 = VGroup(
            Text("方法2:", font="PingFang SC", font_size=self.FONT_SMALL, color=GRAY_A),
            MathTex(r"\frac{a}{b}", font_size=50, color=WHITE)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1)
        
        # 修复：直接设置整个分数的颜色，或者使用substrings_to_isolate
        # 更好的方法是创建单独的Text对象来构建分数
        fraction_parts = VGroup(
            Text("a", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_PRIMARY),
            Text("/", font_size=self.FONT_RATIO_NORMAL, color=WHITE),
            Text("b", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.1)
        
        # 替换format_2的第二个元素
        format_2 = VGroup(
            Text("方法2:", font="PingFang SC", font_size=self.FONT_SMALL, color=GRAY_A),
            fraction_parts
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1)
        
        self.play(Write(format_2), run_time=0.8)
        
        # 示例
        example = VGroup(
            Text("例如:", font="PingFang SC", font_size=self.FONT_SMALL, color=GRAY_A),
            VGroup(
                Text("2", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_PRIMARY),
                Text(":", font_size=self.FONT_RATIO_NORMAL, color=WHITE),
                Text("3", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_SECONDARY)
            ).arrange(RIGHT, buff=0.15)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(FadeIn(example, shift=UP * 0.3), run_time=0.5)
        
        # 标注前项和后项
        arrow_前项 = Arrow(
            example[1][0].get_bottom() + DOWN * 0.3,
            example[1][0].get_bottom() + DOWN * 0.05,
            color=self.COLOR_PRIMARY,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        
        label_前项 = Text(
            "前项",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_PRIMARY
        ).next_to(arrow_前项, DOWN, buff=0.1)
        
        arrow_后项 = Arrow(
            example[1][2].get_bottom() + DOWN * 0.3,
            example[1][2].get_bottom() + DOWN * 0.05,
            color=self.COLOR_SECONDARY,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        
        label_后项 = Text(
            "后项",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_SECONDARY
        ).next_to(arrow_后项, DOWN, buff=0.1)
        
        self.play(
            GrowArrow(arrow_前项),
            GrowArrow(arrow_后项),
            run_time=0.5
        )
        
        self.play(
            FadeIn(label_前项),
            FadeIn(label_后项),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_box),
            FadeOut(definition_text),
            FadeOut(format_title),
            FadeOut(format_1),
            FadeOut(format_2),
            FadeOut(example),
            FadeOut(arrow_前项),
            FadeOut(arrow_后项),
            FadeOut(label_前项),
            FadeOut(label_后项),
            run_time=0.6
        )
    
    def show_ratio_components(self):
        """场景3: 比的各部分名称"""
        # 标题
        title = Text(
            "比的组成",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 大号比式
        num_6 = Text("6", font_size=60, color=self.COLOR_PRIMARY, weight=BOLD)
        colon = Text(":", font_size=60, color=WHITE, weight=BOLD)
        num_3 = Text("3", font_size=60, color=self.COLOR_SECONDARY, weight=BOLD)
        
        ratio_large = VGroup(num_6, colon, num_3).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        self.play(Write(ratio_large), run_time=0.6)
        
        # 标注前项
        label_前项 = Text(
            "前项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).next_to(num_6, UP, buff=0.5)
        
        arrow_1 = Arrow(
            label_前项.get_bottom(),
            num_6.get_top(),
            color=self.COLOR_PRIMARY,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            FadeIn(label_前项, shift=DOWN * 0.2),
            GrowArrow(arrow_1),
            Indicate(num_6, scale_factor=1.2),
            run_time=0.8
        )
        
        # 标注后项
        label_后项 = Text(
            "后项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(num_3, UP, buff=0.5)
        
        arrow_2 = Arrow(
            label_后项.get_bottom(),
            num_3.get_top(),
            color=self.COLOR_SECONDARY,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            FadeIn(label_后项, shift=DOWN * 0.2),
            GrowArrow(arrow_2),
            Indicate(num_3, scale_factor=1.2),
            run_time=0.8
        )
        
        # 标注比号
        label_比号 = Text(
            "比号",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(colon, DOWN, buff=0.5)
        
        arrow_3 = Arrow(
            label_比号.get_top(),
            colon.get_bottom(),
            color=WHITE,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            FadeIn(label_比号, shift=UP * 0.2),
            GrowArrow(arrow_3),
            Indicate(colon, scale_factor=1.2),
            run_time=0.8
        )
        
        # 比值说明
        ratio_value_text = Text(
            "比值 = 前项 ÷ 后项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(ratio_value_text, shift=UP * 0.3), run_time=0.6)
        
        # 计算过程
        calculation = VGroup(
            Text("6", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_PRIMARY),
            Text("÷", font_size=self.FONT_RATIO_NORMAL, color=WHITE),
            Text("3", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_SECONDARY),
            Text("=", font_size=self.FONT_RATIO_NORMAL, color=WHITE),
            Text("2", font_size=self.FONT_RATIO_NORMAL, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        
        self.play(Write(calculation), run_time=1.5)
        
        # 结果高亮
        self.play(
            calculation[4].animate.set_color(GOLD).scale(1.3),
            Flash(calculation[4], color=GOLD, flash_radius=0.5),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ratio_large),
            FadeOut(label_前项),
            FadeOut(label_后项),
            FadeOut(label_比号),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(arrow_3),
            FadeOut(ratio_value_text),
            FadeOut(calculation),
            run_time=0.6
        )
    
    def show_three_relationships(self):
        """场景4: 三者关系(核心)"""
        # 标题
        title = Text(
            "比的三种形式",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_RELATION
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 比式
        ratio_form = VGroup(
            Text("a", font_size=40, color=self.COLOR_PRIMARY),
            Text(":", font_size=40, color=WHITE),
            Text("b", font_size=40, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.5)
        
        self.play(Write(ratio_form), run_time=1.0)
        
        # 变换为除法
        division_form = VGroup(
            Text("a", font_size=40, color=self.COLOR_PRIMARY),
            Text("÷", font_size=40, color=WHITE),
            Text("b", font_size=40, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingShapes(ratio_form, division_form),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 变换为分数 - 修复这里：使用Text对象构建分数
        fraction_parts = VGroup(
            Text("a", font_size=30, color=self.COLOR_PRIMARY),
            Text("—", font_size=40, color=WHITE).shift(UP * 0.05),
            Text("b", font_size=30, color=self.COLOR_SECONDARY)
        ).arrange(DOWN, buff=0).move_to(UP * 4.5)
        
        self.play(
            Transform(division_form, fraction_parts),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 三者并列
        ratio_final = VGroup(
            Text("a", font_size=32, color=self.COLOR_PRIMARY),
            Text(":", font_size=32, color=WHITE),
            Text("b", font_size=32, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.15)
        
        division_final = VGroup(
            Text("a", font_size=32, color=self.COLOR_PRIMARY),
            Text("÷", font_size=32, color=WHITE),
            Text("b", font_size=32, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.15)
        
        fraction_final = VGroup(
            Text("a", font_size=24, color=self.COLOR_PRIMARY),
            Text("—", font_size=32, color=WHITE).shift(UP * 0.03),
            Text("b", font_size=24, color=self.COLOR_SECONDARY)
        ).arrange(DOWN, buff=0)
        
        equals_1 = Text("=", font_size=32, color=WHITE)
        equals_2 = Text("=", font_size=32, color=WHITE)
        
        all_forms = VGroup(
            ratio_final,
            equals_1,
            division_final,
            equals_2,
            fraction_final
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        self.play(
            FadeOut(division_form),
            FadeIn(all_forms),
            run_time=1.0
        )
        
        # 框选强调
        box = SurroundingRectangle(
            all_forms,
            color=self.COLOR_RELATION,
            buff=0.3,
            stroke_width=4
        )
        
        self.play(Create(box), run_time=0.8)
        self.wait(0.8)
        
        # 示例标题
        example_title = Text(
            "例如: 4 和 5 的比",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 示例 - 逐步展开
        ex_ratio = VGroup(
            Text("4", font_size=32, color=self.COLOR_PRIMARY),
            Text(":", font_size=32, color=WHITE),
            Text("5", font_size=32, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.3)
        
        self.play(Write(ex_ratio), run_time=0.8)
        
        # 等于除法
        ex_eq1 = Text("=", font_size=32, color=WHITE).next_to(ex_ratio, RIGHT, buff=0.3)
        ex_div = VGroup(
            Text("4", font_size=32, color=self.COLOR_PRIMARY),
            Text("÷", font_size=32, color=WHITE),
            Text("5", font_size=32, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.15).next_to(ex_eq1, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(ex_eq1),
            Write(ex_div),
            run_time=1.0
        )
        
        # 等于分数
        ex_eq2 = Text("=", font_size=32, color=WHITE).next_to(ex_div, RIGHT, buff=0.3)
        ex_frac = VGroup(
            Text("4", font_size=24, color=self.COLOR_PRIMARY),
            Text("—", font_size=32, color=WHITE).shift(UP * 0.03),
            Text("5", font_size=24, color=self.COLOR_SECONDARY)
        ).arrange(DOWN, buff=0).next_to(ex_eq2, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(ex_eq2),
            Write(ex_frac),
            run_time=1.0
        )
        
        # 等于小数
        ex_eq3 = Text("=", font_size=32, color=WHITE).next_to(ex_frac, RIGHT, buff=0.3)
        ex_decimal = Text("0.8", font_size=32, color=GOLD).next_to(ex_eq3, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(ex_eq3),
            Write(ex_decimal),
            run_time=1.0
        )
        
        # 最终高亮
        self.play(
            ex_decimal.animate.scale(1.2),
            Flash(ex_decimal, color=GOLD),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_forms),
            FadeOut(box),
            FadeOut(example_title),
            FadeOut(ex_ratio),
            FadeOut(ex_eq1),
            FadeOut(ex_div),
            FadeOut(ex_eq2),
            FadeOut(ex_frac),
            FadeOut(ex_eq3),
            FadeOut(ex_decimal),
            run_time=0.6
        )
    
    def show_important_warning(self):
        """场景5: 重要提醒"""
        # 警告框
        warning_box = RoundedRectangle(
            width=7,
            height=3,
            corner_radius=0.3,
            color=self.COLOR_WARNING,
            fill_opacity=0.15,
            stroke_width=5
        ).move_to(UP * 3)
        
        self.play(FadeIn(warning_box, scale=1.2), run_time=0.5)
        
        # 警告图标
        warning_icon = Text(
            "⚠",
            font_size=60,
            color=self.COLOR_WARNING
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(warning_icon, scale=1.3), run_time=0.3)
        
        # 警告文字
        warning_text = Text(
            "重要: 比的后项不能为0",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_WARNING,
            weight=BOLD
        ).move_to(UP * 3.2)
        
        self.play(Write(warning_text), run_time=1.0)
        
        # 错误示例
        wrong_example = VGroup(
            Text("5", font_size=40, color=WHITE),
            Text(":", font_size=40, color=WHITE),
            Text("0", font_size=40, color=WHITE)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2)
        
        cross_mark = Text(
            "✗",
            font_size=60,
            color=RED
        ).next_to(wrong_example, RIGHT, buff=0.5)
        
        self.play(Write(wrong_example), run_time=0.8)
        self.play(
            Write(cross_mark),
            Flash(cross_mark, color=RED, flash_radius=0.5),
            run_time=0.7
        )
        
        # 解释原因
        explanation = Text(
            "因为除数不能为0",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.7)
        
        # 关联线
        arrow_1 = Arrow(
            wrong_example[2].get_bottom(),
            explanation.get_top() + LEFT * 0.5,
            color=self.COLOR_WARNING,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(GrowArrow(arrow_1), run_time=0.5)
        
        # 补充说明
        supplement = Text(
            "5 ÷ 0 = ? (无意义)",
            font="PingFang SC",
            font_size=self.FONT_SMALL,
            color=GRAY_B
        ).move_to(DOWN * 0.2)
        
        self.play(FadeIn(supplement), run_time=0.5)
        
        # 强调闪烁
        self.play(
            Indicate(warning_box, scale_factor=1.05),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(warning_box),
            FadeOut(warning_icon),
            FadeOut(warning_text),
            FadeOut(wrong_example),
            FadeOut(cross_mark),
            FadeOut(explanation),
            FadeOut(arrow_1),
            FadeOut(supplement),
            run_time=0.6
        )
    
    def show_applications_and_outro(self):
        """场景6: 实际应用与结尾"""
        # 标题
        title = Text(
            "比在生活中",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        
        # 应用场景1: 调配饮料
        scene_1 = VGroup(
            Text("🥤", font_size=40),
            Text(
                "调配饮料",
                font="PingFang SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("水", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY),
                Text(":", font_size=20, color=WHITE),
                Text("糖浆", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY),
                Text("=", font_size=20, color=WHITE),
                Text("3", font_size=20, color=WHITE),
                Text(":", font_size=20, color=WHITE),
                Text("1", font_size=20, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.3).move_to(UP * 3.5)
        
        self.play(FadeIn(scene_1, shift=UP * 0.3), run_time=1.0)
        
        # 应用场景2: 地图比例
        scene_2 = VGroup(
            Text("🗺", font_size=40),
            Text(
                "地图比例",
                font="PingFang SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("图上", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY),
                Text(":", font_size=20, color=WHITE),
                Text("实际", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY),
                Text("=", font_size=20, color=WHITE),
                Text("1", font_size=20, color=WHITE),
                Text(":", font_size=20, color=WHITE),
                Text("100000", font_size=20, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.3).move_to(UP * 1)
        
        self.play(FadeIn(scene_2, shift=UP * 0.3), run_time=1.0)
        
        # 应用场景3: 配方比例
        scene_3 = VGroup(
            Text("🍞", font_size=40),
            Text(
                "配方比例",
                font="PingFang SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("面粉", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY),
                Text(":", font_size=20, color=WHITE),
                Text("水", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY),
                Text("=", font_size=20, color=WHITE),
                Text("5", font_size=20, color=WHITE),
                Text(":", font_size=20, color=WHITE),
                Text("3", font_size=20, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 1.5)
        
        self.play(FadeIn(scene_3, shift=UP * 0.3), run_time=1.0)
        
        # 全部高亮
        scenes = VGroup(scene_1, scene_2, scene_3)
        self.play(
            Indicate(scenes, scale_factor=1.05),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 场景淡出
        self.play(
            FadeOut(title),
            FadeOut(scenes),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 关键词标签
        keywords = VGroup(
            Text("#比", font="PingFang SC", font_size=22, color=self.COLOR_PRIMARY),
            Text("#比例", font="PingFang SC", font_size=22, color=self.COLOR_SECONDARY),
            Text("#数学", font="PingFang SC", font_size=22, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        self.play(
            LaggedStart(*[FadeIn(kw, shift=UP * 0.2) for kw in keywords], lag_ratio=0.2),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(keywords),
            run_time=1.0
        )


# 运行命令:
# manim -pql ratio_meaning.py RatioMeaning  # 快速预览
# manim -qh ratio_meaning.py RatioMeaning   # 高质量渲染