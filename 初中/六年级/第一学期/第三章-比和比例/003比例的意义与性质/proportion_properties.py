"""
比例的意义与性质 - Proportion Properties Teaching Animation
使用 Manim 创建的小学数学教学视频

内容: 比例的定义和基本性质（内项积等于外项积）
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


class ProportionProperties(Scene):
    """
    比例的意义与性质教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出比例概念
    2. 比例的定义
    3. 内项和外项的识别
    4. 基本性质 - 内项积等于外项积
    5. 具体验证
    6. 应用 - 判断能否组成比例
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_OUTER = "#3498db"      # 蓝色 - 外项
        self.COLOR_INNER = "#e74c3c"      # 红色 - 内项
        self.COLOR_HIGHLIGHT = YELLOW     # 黄色 - 高亮
        self.COLOR_PROPERTY = "#2ecc71"   # 绿色 - 性质
        self.COLOR_PRODUCT = "#f39c12"    # 橙色 - 乘积
        self.COLOR_AUXILIARY = GRAY_B     # 灰色 - 辅助
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_terms()
        self.show_property()
        self.show_verification()
        self.show_application()
        self.show_outro()
    
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
            "什么是比例?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 第一个比 2:3
        ratio1 = VGroup(
            Text("2", font="Noto Sans CJK SC", font_size=64, color=WHITE, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=64, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=64, color=WHITE, weight=BOLD)
        ).arrange(RIGHT, buff=0.2)
        ratio1.move_to(UP * 3 + LEFT * 2)
        
        # 等号
        equals = Text("=", font="Noto Sans CJK SC", font_size=64, color=self.COLOR_PROPERTY).move_to(UP * 3)
        
        # 第二个比 4:6
        ratio2 = VGroup(
            Text("4", font="Noto Sans CJK SC", font_size=64, color=WHITE, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=64, color=WHITE),
            Text("6", font="Noto Sans CJK SC", font_size=64, color=WHITE, weight=BOLD)
        ).arrange(RIGHT, buff=0.2)
        ratio2.move_to(UP * 3 + RIGHT * 2)
        
        self.play(FadeIn(ratio1, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(ratio2, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(equals, scale=0.5), run_time=0.3)
        
        # 组合
        proportion = VGroup(ratio1, equals, ratio2)
        
        # 闪烁
        self.play(
            Flash(proportion, color=self.COLOR_HIGHLIGHT, flash_radius=1.2),
            run_time=0.4
        )
        
        # 问题文字
        question = Text(
            "它们有什么神奇的性质?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.9)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            run_time=0.4
        )
        
        # 保存比例供后续使用
        self.proportion_example = proportion
    
    def show_definition(self):
        """场景2: 比例的定义"""
        # 标题
        title = Text(
            "比例的意义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        definition = Text(
            "表示两个比相等的式子叫做比例",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.7)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(definition), run_time=0.5)
        
        # 移动原比例到顶部
        self.play(
            self.proportion_example.animate.move_to(UP * 4.5).scale(0.8),
            run_time=0.6
        )
        
        # 一般形式
        general_label = Text(
            "一般形式:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 2.5 + LEFT * 2.5)
        
        general_form = MathTex(
            r"a:b = c:d",
            font_size=56,
            color=WHITE
        ).move_to(UP * 2.5 + RIGHT * 1)
        
        self.play(Write(general_label), run_time=0.4)
        self.play(Write(general_form), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "读作: a比b等于c比d",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.2)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(4.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(self.proportion_example),
            FadeOut(general_label),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 保留一般形式
        self.general_form = general_form
    
    def show_terms(self):
        """场景3: 内项和外项"""
        # 移动并放大一般形式
        self.play(
            self.general_form.animate.move_to(UP * 2.5).scale(1.2),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "内项与外项",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 获取公式中的各个部分 - 精确分离
        # 重新创建可以单独控制的元素
        a_text = MathTex("a", font_size=56, color=WHITE).move_to(self.general_form.get_center() + LEFT * 2.1)
        colon1 = MathTex(":", font_size=56, color=WHITE).move_to(self.general_form.get_center() + LEFT * 1.4)
        b_text = MathTex("b", font_size=56, color=WHITE).move_to(self.general_form.get_center() + LEFT * 0.7)
        equals_text = MathTex("=", font_size=56, color=WHITE).move_to(self.general_form.get_center())
        c_text = MathTex("c", font_size=56, color=WHITE).move_to(self.general_form.get_center() + RIGHT * 0.7)
        colon2 = MathTex(":", font_size=56, color=WHITE).move_to(self.general_form.get_center() + RIGHT * 1.4)
        d_text = MathTex("d", font_size=56, color=WHITE).move_to(self.general_form.get_center() + RIGHT * 2.1)
        
        # 替换原来的general_form
        new_proportion = VGroup(a_text, colon1, b_text, equals_text, c_text, colon2, d_text)
        self.play(Transform(self.general_form, new_proportion), run_time=0.3)
        self.remove(self.general_form)
        self.add(new_proportion)
        
        # === 外项 ===
        # 高亮 a
        self.play(
            a_text.animate.set_color(self.COLOR_OUTER).scale(1.2),
            run_time=0.5
        )
        
        # 高亮 d
        self.play(
            d_text.animate.set_color(self.COLOR_OUTER).scale(1.2),
            run_time=0.5
        )
        
        # 外项标签
        outer_label = Text(
            "外项 (两端)",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_OUTER,
            weight=BOLD
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(outer_label), run_time=0.4)
        
        # 外项框线
        outer_box_a = SurroundingRectangle(a_text, color=self.COLOR_OUTER, buff=0.15)
        outer_box_d = SurroundingRectangle(d_text, color=self.COLOR_OUTER, buff=0.15)
        
        self.play(Create(outer_box_a), Create(outer_box_d), run_time=0.5)
        
        # === 内项 ===
        # 高亮 b
        self.play(
            b_text.animate.set_color(self.COLOR_INNER).scale(1.2),
            run_time=0.5
        )
        
        # 高亮 c
        self.play(
            c_text.animate.set_color(self.COLOR_INNER).scale(1.2),
            run_time=0.5
        )
        
        # 内项标签
        inner_label = Text(
            "内项 (中间)",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_INNER,
            weight=BOLD
        ).move_to(ORIGIN)
        
        self.play(FadeIn(inner_label), run_time=0.4)
        
        # 内项框线
        inner_box_b = SurroundingRectangle(b_text, color=self.COLOR_INNER, buff=0.15)
        inner_box_c = SurroundingRectangle(c_text, color=self.COLOR_INNER, buff=0.15)
        
        self.play(Create(inner_box_b), Create(inner_box_c), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "两端的项叫外项，中间的项叫内项",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(3.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(outer_label),
            FadeOut(inner_label),
            FadeOut(outer_box_a),
            FadeOut(outer_box_d),
            FadeOut(inner_box_b),
            FadeOut(inner_box_c),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 保留彩色的比例式
        self.colored_proportion = new_proportion
        self.a = a_text
        self.b = b_text
        self.c = c_text
        self.d = d_text
    
    def show_property(self):
        """场景4: 基本性质 - 内项积等于外项积"""
        # 标题
        title = Text(
            "比例的基本性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        property_intro = Text(
            "内项积等于外项积",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.7)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(property_intro), run_time=0.5)
        
        # === 交叉箭头 ===
        # 从 a 到 d 的弧形箭头
        cross_arrow_1 = CurvedArrow(
            self.a.get_center() + DOWN * 0.3,
            self.d.get_center() + DOWN * 0.3,
            angle=-PI/3,
            color=self.COLOR_OUTER,
            stroke_width=4
        )
        
        # 从 b 到 c 的弧形箭头
        cross_arrow_2 = CurvedArrow(
            self.b.get_center() + UP * 0.3,
            self.c.get_center() + UP * 0.3,
            angle=PI/3,
            color=self.COLOR_INNER,
            stroke_width=4
        )
        
        self.play(GrowArrow(cross_arrow_1), run_time=0.6)
        self.play(GrowArrow(cross_arrow_2), run_time=0.6)
        
        # === 外项积 ===
        outer_product = VGroup(
            MathTex("a", font_size=40, color=self.COLOR_OUTER),
            MathTex(r"\times", font_size=36, color=WHITE),
            MathTex("d", font_size=40, color=self.COLOR_OUTER)
        ).arrange(RIGHT, buff=0.15)
        outer_product.move_to(DOWN * 1.5 + LEFT * 2)
        
        self.play(Write(outer_product), run_time=0.8)
        
        # === 等号 ===
        equals_sign = MathTex("=", font_size=48, color=self.COLOR_PROPERTY).move_to(DOWN * 1.5)
        self.play(Write(equals_sign), run_time=0.4)
        
        # === 内项积 ===
        inner_product = VGroup(
            MathTex("b", font_size=40, color=self.COLOR_INNER),
            MathTex(r"\times", font_size=36, color=WHITE),
            MathTex("c", font_size=40, color=self.COLOR_INNER)
        ).arrange(RIGHT, buff=0.15)
        inner_product.move_to(DOWN * 1.5 + RIGHT * 2)
        
        self.play(Write(inner_product), run_time=0.8)
        
        # === 完整性质公式 ===
        property_formula = MathTex(
            r"a \times d = b \times c",
            font_size=42,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(Write(property_formula), run_time=1.0)
        self.play(Indicate(property_formula, color=self.COLOR_PROPERTY, scale_factor=1.1), run_time=0.6)
        
        # 说明
        explanation = Text(
            "这是比例最重要的性质!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(4.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(property_intro),
            FadeOut(self.colored_proportion),
            FadeOut(cross_arrow_1),
            FadeOut(cross_arrow_2),
            FadeOut(outer_product),
            FadeOut(equals_sign),
            FadeOut(inner_product),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 保留性质公式
        self.property_formula = property_formula
    
    def show_verification(self):
        """场景5: 具体验证"""
        # 移动性质公式
        self.play(
            self.property_formula.animate.move_to(UP * 6).scale(0.8),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "验证性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.5)
        
        # 具体比例 2:3 = 4:6
        proportion = VGroup(
            Text("2", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_OUTER, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=52, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_INNER, weight=BOLD),
            Text("=", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_PROPERTY),
            Text("4", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_INNER, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=52, color=WHITE),
            Text("6", font="Noto Sans CJK SC", font_size=52, color=self.COLOR_OUTER, weight=BOLD)
        ).arrange(RIGHT, buff=0.15)
        proportion.move_to(UP * 3.2)
        
        self.play(Write(proportion), run_time=0.6)
        
        # 标注外项 2 和 6
        outer_terms = VGroup(proportion[0], proportion[6])
        self.play(Indicate(outer_terms, color=self.COLOR_OUTER, scale_factor=1.15), run_time=0.5)
        
        # 外项积计算
        calc_outer = VGroup(
            Text("外项积:", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            MathTex(r"2 \times 6 = 12", font_size=36, color=self.COLOR_OUTER)
        ).arrange(RIGHT, buff=0.3)
        calc_outer.move_to(UP * 1)
        
        self.play(Write(calc_outer), run_time=1.0)
        
        # 标注内项 3 和 4
        inner_terms = VGroup(proportion[2], proportion[4])
        self.play(Indicate(inner_terms, color=self.COLOR_INNER, scale_factor=1.15), run_time=0.5)
        
        # 内项积计算
        calc_inner = VGroup(
            Text("内项积:", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            MathTex(r"3 \times 4 = 12", font_size=36, color=self.COLOR_INNER)
        ).arrange(RIGHT, buff=0.3)
        calc_inner.move_to(DOWN * 0.5)
        
        self.play(Write(calc_inner), run_time=1.0)
        
        # 对比结果
        comparison_box = VGroup(calc_outer[1], calc_inner[1])
        self.play(
            comparison_box.animate.arrange(DOWN, buff=0.5).move_to(DOWN * 2.5),
            FadeOut(calc_outer[0]),
            FadeOut(calc_inner[0]),
            run_time=0.6
        )
        
        # 等号高亮
        big_equals = MathTex("=", font_size=60, color=self.COLOR_PROPERTY).move_to(DOWN * 2.5 + LEFT * 2)
        self.play(Write(big_equals), run_time=0.4)
        
        # 验证结果
        verification = MathTex(
            r"12 = 12",
            font_size=48,
            color=self.COLOR_PROPERTY
        ).move_to(DOWN * 2.5)
        
        self.play(
            Transform(comparison_box, verification),
            FadeOut(big_equals),
            run_time=0.5
        )
        
        # 成功标记
        check_mark = Text(
            "✓",
            font_size=56,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).next_to(verification, RIGHT, buff=0.3)
        
        self.play(FadeIn(check_mark, scale=0.5), run_time=0.5)
        
        # 结论
        conclusion = Text(
            "性质成立!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.5)
        self.wait(4.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(proportion),
            FadeOut(comparison_box),
            FadeOut(check_mark),
            FadeOut(conclusion),
            FadeOut(self.property_formula),
            run_time=0.5
        )
    
    def show_application(self):
        """场景6: 应用 - 判断能否组成比例"""
        # 标题
        title = Text(
            "判断能否组成比例",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.5)
        
        # 四个数
        numbers_label = Text(
            "已知四个数:",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        numbers = VGroup(
            Text("2", font="Noto Sans CJK SC", font_size=56, color=WHITE, weight=BOLD),
            Text(",", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=56, color=WHITE, weight=BOLD),
            Text(",", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            Text("4", font="Noto Sans CJK SC", font_size=56, color=WHITE, weight=BOLD),
            Text(",", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            Text("6", font="Noto Sans CJK SC", font_size=56, color=WHITE, weight=BOLD)
        ).arrange(RIGHT, buff=0.1)
        numbers.move_to(UP * 3.5)
        
        self.play(FadeIn(numbers_label), run_time=0.3)
        self.play(FadeIn(numbers, shift=DOWN * 0.3), run_time=0.6)
        
        # 问题
        question = Text(
            "它们能组成比例吗?",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(question), run_time=0.4)
        
        # 尝试排列成比例
        attempt_label = Text(
            "尝试:",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 1.3 + LEFT * 3)
        
        proportion_attempt = VGroup(
            Text("2", font="Noto Sans CJK SC", font_size=48, color=self.COLOR_OUTER, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            Text("3", font="Noto Sans CJK SC", font_size=48, color=self.COLOR_INNER, weight=BOLD),
            Text("=", font="Noto Sans CJK SC", font_size=48, color=self.COLOR_PROPERTY),
            Text("4", font="Noto Sans CJK SC", font_size=48, color=self.COLOR_INNER, weight=BOLD),
            Text(":", font="Noto Sans CJK SC", font_size=48, color=WHITE),
            Text("6", font="Noto Sans CJK SC", font_size=48, color=self.COLOR_OUTER, weight=BOLD)
        ).arrange(RIGHT, buff=0.12)
        proportion_attempt.move_to(UP * 1.3 + RIGHT * 1)
        
        self.play(
            FadeIn(attempt_label),
            Transform(numbers.copy(), proportion_attempt),
            run_time=0.8
        )
        self.add(proportion_attempt)
        
        # 验证: 外项积
        calc_outer = MathTex(
            r"2 \times 6 = 12",
            font_size=36,
            color=self.COLOR_OUTER
        ).move_to(DOWN * 0.5)
        
        self.play(Write(calc_outer), run_time=0.8)
        
        # 验证: 内项积
        calc_inner = MathTex(
            r"3 \times 4 = 12",
            font_size=36,
            color=self.COLOR_INNER
        ).move_to(DOWN * 1.8)
        
        self.play(Write(calc_inner), run_time=0.8)
        
        # 判断结果
        result = MathTex(
            r"12 = 12",
            font_size=42,
            color=self.COLOR_PROPERTY
        ).move_to(DOWN * 3.2)
        
        check = Text(
            "✓",
            font_size=48,
            color=self.COLOR_PROPERTY,
            weight=BOLD
        ).next_to(result, RIGHT, buff=0.3)
        
        self.play(Write(result), FadeIn(check, scale=0.5), run_time=0.6)
        
        # 结论
        conclusion = Text(
            "能!",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.8)
        
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.5)
        
        # 提示
        tip = Text(
            "只要内项积等于外项积，就能组成比例",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(tip), run_time=0.5)
        self.wait(3.5)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info],
            run_time=0.5
        )
    
    def show_outro(self):
        """场景7: 总结与片尾"""
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
        icon_1 = Circle(radius=0.2, fill_color=self.COLOR_PROPERTY, fill_opacity=1, stroke_width=0)
        text_1 = Text(
            "比例: 两个比相等的式子",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_1 = VGroup(icon_1, text_1).arrange(RIGHT, buff=0.3)
        card_1.move_to(UP * 3.5 + LEFT * 10)
        cards.add(card_1)
        
        # 卡片2
        icon_2 = Circle(radius=0.2, fill_color=self.COLOR_OUTER, fill_opacity=1, stroke_width=0)
        text_2 = Text(
            "基本性质: 内项积 = 外项积",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_2 = VGroup(icon_2, text_2).arrange(RIGHT, buff=0.3)
        card_2.move_to(UP * 2.5 + LEFT * 10)
        cards.add(card_2)
        
        # 卡片3
        icon_3 = Circle(radius=0.2, fill_color=self.COLOR_INNER, fill_opacity=1, stroke_width=0)
        text_3 = Text(
            "可判断四个数能否组成比例",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        card_3 = VGroup(icon_3, text_3).arrange(RIGHT, buff=0.3)
        card_3.move_to(UP * 1.5 + LEFT * 10)
        cards.add(card_3)
        
        # 卡片滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 示例回顾
        example_recap = VGroup(
            Text("例:", font="Noto Sans CJK SC", font_size=26, color=GRAY_A),
            MathTex(r"2:3 = 4:6", font_size=32, color=self.COLOR_PROPERTY),
            MathTex(r"\Rightarrow", font_size=28, color=WHITE),
            MathTex(r"2 \times 6 = 3 \times 4", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        
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
        
        # 装饰图标 - 等号符号
        icons = VGroup(*[
            Text("=", font="Noto Sans CJK SC", font_size=40, color=self.COLOR_PROPERTY, weight=BOLD)
            .shift(1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ]).move_to(follow_text.get_center() + DOWN * 1.5)
        
        self.play(
            LaggedStart(*[FadeIn(icon, scale=0.5) for icon in icons], lag_ratio=0.1),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql proportion_properties.py ProportionProperties  # 快速预览
# manim -qh proportion_properties.py ProportionProperties   # 高质量渲染