"""
对数的概念与运算 - Manim 教学动画
Logarithm Concepts and Operations

内容: 对数定义、恒等式、运算法则、换底公式
目标观众: 高一学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场钩子
2. 对数定义
3. 常用对数与自然对数
4. 对数恒等式
5. 对数运算法则（上）
6. 对数运算法则（下）
7. 总结与片尾
"""

from manim import *
import numpy as np

# ===== 全局配置 - TikTok竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 品牌信息 =====
AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "Noto Sans CJK SC"

# ===== 配色方案 =====
COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要概念
COLOR_SECONDARY = "#e74c3c"    # 红色 - 重点强调
COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式框
COLOR_EXPONENT = "#9b59b6"     # 紫色 - 指数
COLOR_LOGARITHM = "#e67e22"    # 橙色 - 对数

# ===== 字体大小 =====
FONT_SIZE_TITLE = 36
FONT_SIZE_SUBTITLE = 28
FONT_SIZE_BODY = 22
FONT_SIZE_FORMULA = 28
FONT_SIZE_LABEL = 20
FONT_SIZE_SMALL = 18


class LogarithmConcepts(Scene):
    """对数的概念与运算教学动画主场景"""
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 作者信息（全程显示）
        self.author_info = Text(
            f"{AUTHOR_NAME} {AUTHOR_ID}",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_LABEL,
            color=GRAY_B
        ).move_to(UP * 7.5)
        
        self.add(self.author_info)
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_special_logs()
        self.scene_4_identities()
        self.scene_5_operations_part1()
        self.scene_6_operations_part2()
        self.scene_7_outro()
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (3-4秒)"""
        # 钩子问题
        hook_text = Text(
            "2的几次方等于8？",
            font=AUTHOR_FONT,
            font_size=42,
            color=WHITE
        ).move_to(UP * 3)
        
        # 答案
        answer = VGroup(
            MathTex(r"2^3 = 8", font_size=38, color=COLOR_EXPONENT),
            Text(
                "这就是对数！",
                font=AUTHOR_FONT,
                font_size=36,
                color=COLOR_HIGHLIGHT
            )
        ).arrange(DOWN, buff=0.5).move_to(UP * 0.5)
        
        # 动画
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(answer[0], shift=UP*0.3), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(answer[1], scale=1.2), run_time=0.5)
        self.play(Flash(answer[1], color=COLOR_HIGHLIGHT, flash_radius=1.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(answer),
            run_time=0.5
        )
    
    def scene_2_definition(self):
        """场景2: 对数定义 (10-12秒)"""
        # 标题
        title = Text(
            "对数的定义",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 指数式
        exponent_form = MathTex(
            r"2^3 = 8",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_EXPONENT
        ).move_to(UP * 4)
        
        # 双向箭头
        double_arrow = MathTex(
            r"\Updownarrow",
            font_size=48,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        # 对数式
        log_form = MathTex(
            r"\log_2 8 = 3",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_LOGARITHM
        ).move_to(UP * 1)
        
        # 标注
        base_label = Text("底数", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=GRAY_A).next_to(log_form, DOWN, buff=1.2).shift(LEFT * 1.5)
        true_label = Text("真数", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=GRAY_A).next_to(log_form, DOWN, buff=1.2)
        result_label = Text("对数", font=AUTHOR_FONT, font_size=FONT_SIZE_SMALL, color=GRAY_A).next_to(log_form, DOWN, buff=1.2).shift(RIGHT * 1.5)
        
        # 箭头指向
        base_arrow = Arrow(base_label.get_top(), log_form.get_bottom() + LEFT * 0.8, buff=0.1, color=GRAY_A, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        true_arrow = Arrow(true_label.get_top(), log_form.get_bottom() + RIGHT * 0.3, buff=0.1, color=GRAY_A, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        result_arrow = Arrow(result_label.get_top(), log_form.get_bottom() + RIGHT * 1.2, buff=0.1, color=GRAY_A, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        
        labels = VGroup(base_label, true_label, result_label, base_arrow, true_arrow, result_arrow)
        
        # 一般形式
        general_form = MathTex(
            r"a^x = N \Leftrightarrow x = \log_a N",
            font_size=FONT_SIZE_FORMULA,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        general_box = SurroundingRectangle(
            general_form,
            color=COLOR_FORMULA,
            buff=0.3,
            corner_radius=0.1
        )
        
        # 条件
        condition = MathTex(
            r"(a > 0, a \neq 1, N > 0)",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        ).next_to(general_form, DOWN, buff=0.3)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.play(Write(exponent_form), run_time=0.8)
        self.wait(0.2)
        
        # 箭头摆动效果
        self.play(
            FadeIn(double_arrow, shift=DOWN*0.2),
            run_time=0.6
        )
        
        self.play(Write(log_form), run_time=1.0)
        self.wait(0.3)
        
        # 标注说明
        self.play(
            *[FadeIn(obj, shift=UP*0.2) for obj in labels],
            run_time=1.2
        )
        self.wait(0.8)
        
        # 淡出标注
        self.play(FadeOut(labels), run_time=0.4)
        
        # 一般形式
        self.play(
            Create(general_box),
            Write(general_form),
            run_time=1.5
        )
        self.play(Write(condition), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(exponent_form),
            FadeOut(double_arrow),
            FadeOut(log_form),
            FadeOut(general_box),
            FadeOut(general_form),
            FadeOut(condition),
            run_time=0.6
        )
    
    def scene_3_special_logs(self):
        """场景3: 常用对数与自然对数 (8-10秒)"""
        # 标题
        title = Text(
            "特殊对数",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 常用对数卡片
        common_log_title = Text(
            "常用对数",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SUBTITLE,
            color=WHITE
        )
        
        common_log_def = MathTex(
            r"\lg N = \log_{10} N",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_LOGARITHM
        )
        
        common_log_example = MathTex(
            r"\lg 100 = 2",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        )
        
        common_log_card = VGroup(
            common_log_title,
            common_log_def,
            common_log_example
        ).arrange(DOWN, buff=0.3)
        
        common_log_bg = SurroundingRectangle(
            common_log_card,
            color=COLOR_PRIMARY,
            buff=0.4,
            corner_radius=0.2,
            stroke_width=2,
            fill_opacity=0.05
        )
        
        common_log_group = VGroup(common_log_bg, common_log_card).move_to(UP * 2.5 + LEFT * 0)
        
        # 自然对数卡片
        natural_log_title = Text(
            "自然对数",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SUBTITLE,
            color=WHITE
        )
        
        natural_log_def = MathTex(
            r"\ln N = \log_e N",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_LOGARITHM
        )
        
        natural_log_e = MathTex(
            r"e \approx 2.718",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        )
        
        natural_log_example = MathTex(
            r"\ln e = 1",
            font_size=FONT_SIZE_BODY,
            color=GRAY_A
        )
        
        natural_log_card = VGroup(
            natural_log_title,
            natural_log_def,
            natural_log_e,
            natural_log_example
        ).arrange(DOWN, buff=0.25)
        
        natural_log_bg = SurroundingRectangle(
            natural_log_card,
            color=COLOR_SECONDARY,
            buff=0.4,
            corner_radius=0.2,
            stroke_width=2,
            fill_opacity=0.05
        )
        
        natural_log_group = VGroup(natural_log_bg, natural_log_card).move_to(DOWN * 1 + LEFT * 0)
        
        # 应用说明
        application = Text(
            "广泛用于科学计算与工程应用",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_BODY,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        # 动画序列
        self.play(Write(title), run_time=0.5)
        
        # 常用对数从左滑入
        common_log_group.shift(LEFT * 10)
        self.play(common_log_group.animate.shift(RIGHT * 10), run_time=0.8)
        self.wait(0.6)
        
        # 自然对数从右滑入
        natural_log_group.shift(RIGHT * 10)
        self.play(natural_log_group.animate.shift(LEFT * 10), run_time=0.8)
        self.wait(0.6)
        
        # 应用说明
        self.play(FadeIn(application, shift=UP*0.3), run_time=1.0)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(common_log_group),
            FadeOut(natural_log_group),
            FadeOut(application),
            run_time=0.6
        )
    
    def scene_4_identities(self):
        """场景4: 对数恒等式 (8-10秒)"""
        # 标题
        title = Text(
            "对数恒等式",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 核心恒等式
        core_identity = MathTex(
            r"a^{\log_a N} = N",
            font_size=FONT_SIZE_FORMULA + 4,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        core_box = SurroundingRectangle(
            core_identity,
            color=COLOR_FORMULA,
            buff=0.4,
            corner_radius=0.1,
            stroke_width=3
        )
        
        # 数值验证
        verification = VGroup(
            MathTex(r"2^{\log_2 8}", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"= 2^3", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 8", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT),
            MathTex(r"\checkmark", font_size=FONT_SIZE_BODY + 4, color=COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.8)
        
        # 特殊情况
        special_cases = VGroup(
            MathTex(r"\log_a a^n = n", font_size=FONT_SIZE_BODY + 2, color=WHITE),
            MathTex(r"\log_a 1 = 0", font_size=FONT_SIZE_BODY + 2, color=WHITE),
            MathTex(r"\log_a a = 1", font_size=FONT_SIZE_BODY + 2, color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(DOWN * 0.5)
        
        # 每个公式的框
        special_boxes = VGroup(*[
            SurroundingRectangle(
                formula,
                color=COLOR_AUXILIARY,
                buff=0.2,
                corner_radius=0.05,
                stroke_width=1.5
            )
            for formula in special_cases
        ])
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        
        self.play(
            Create(core_box),
            Write(core_identity),
            run_time=1.0
        )
        self.wait(0.6)
        
        # 逐个显示验证步骤
        for i, part in enumerate(verification):
            self.play(FadeIn(part, shift=RIGHT*0.3), run_time=0.4)
            if i < len(verification) - 1:
                self.wait(0.2)
        
        self.wait(0.8)
        
        # 特殊情况依次出现
        for formula, box in zip(special_cases, special_boxes):
            self.play(
                Write(formula),
                Create(box),
                run_time=0.6
            )
            self.wait(0.2)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(core_box),
            FadeOut(core_identity),
            FadeOut(verification),
            FadeOut(special_cases),
            FadeOut(special_boxes),
            run_time=0.6
        )
    
    def scene_5_operations_part1(self):
        """场景5: 对数运算法则（上）- 乘除法 (10-12秒)"""
        # 标题
        title = Text(
            "对数运算法则",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        subtitle = Text(
            "乘法与除法",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        # 乘法法则
        multiply_rule = MathTex(
            r"\log_a(MN) = \log_a M + \log_a N",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        multiply_box = SurroundingRectangle(
            multiply_rule,
            color=COLOR_FORMULA,
            buff=0.3,
            corner_radius=0.1
        )
        
        # 乘法示例
        multiply_example = VGroup(
            MathTex(r"\log_2(4 \times 8)", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"= \log_2 4 + \log_2 8", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 2 + 3", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 5", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(UP * 2)
        
        # 验证
        multiply_verify = VGroup(
            MathTex(r"\log_2 32 = 5", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"\checkmark", font_size=FONT_SIZE_BODY + 4, color=COLOR_FORMULA)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        
        # 除法法则
        divide_rule = MathTex(
            r"\log_a \left(\frac{M}{N}\right) = \log_a M - \log_a N",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        divide_box = SurroundingRectangle(
            divide_rule,
            color=COLOR_SECONDARY,
            buff=0.3,
            corner_radius=0.1
        )
        
        # 除法示例
        divide_example = VGroup(
            MathTex(r"\log_2 \left(\frac{8}{4}\right)", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"= \log_2 8 - \log_2 4", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 3 - 2", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 1", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 3.5)
        
        # 动画序列
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)
        
        # 乘法法则
        self.play(
            Create(multiply_box),
            Write(multiply_rule),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 乘法示例逐行
        for line in multiply_example:
            self.play(Write(line), run_time=0.4)
            self.wait(0.15)
        
        # 验证
        self.play(
            *[FadeIn(obj, scale=1.1) for obj in multiply_verify],
            run_time=0.8
        )
        self.wait(0.5)
        
        # 除法法则
        self.play(
            Create(divide_box),
            Write(divide_rule),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 除法示例逐行
        for line in divide_example:
            self.play(Write(line), run_time=0.4)
            self.wait(0.15)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(multiply_box),
            FadeOut(multiply_rule),
            FadeOut(multiply_example),
            FadeOut(multiply_verify),
            FadeOut(divide_box),
            FadeOut(divide_rule),
            FadeOut(divide_example),
            run_time=0.6
        )
    
    def scene_6_operations_part2(self):
        """场景6: 对数运算法则（下）- 幂运算与换底 (10-12秒)"""
        # 标题
        title = Text(
            "幂运算与换底公式",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        # 幂运算法则
        power_rule = MathTex(
            r"\log_a M^n = n \log_a M",
            font_size=FONT_SIZE_FORMULA,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        power_box = SurroundingRectangle(
            power_rule,
            color=COLOR_FORMULA,
            buff=0.3,
            corner_radius=0.1
        )
        
        # 幂运算示例
        power_example = VGroup(
            MathTex(r"\log_2 8^2", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"= 2 \log_2 8", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= 2 \times 3 = 6", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 2.8)
        
        # 换底公式标题强调
        change_base_title = Text(
            "万能公式",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_SUBTITLE,
            color=GOLD
        ).move_to(UP * 0.8)
        
        # 换底公式
        change_base_formula = MathTex(
            r"\log_a b = \frac{\log_c b}{\log_c a}",
            font_size=FONT_SIZE_FORMULA + 2,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        change_base_box = SurroundingRectangle(
            change_base_formula,
            color=GOLD,
            buff=0.4,
            corner_radius=0.1,
            stroke_width=3
        )
        
        # 换底应用示例
        change_base_example = VGroup(
            MathTex(r"\log_2 8", font_size=FONT_SIZE_BODY, color=WHITE),
            MathTex(r"= \frac{\lg 8}{\lg 2}", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"= \frac{0.903}{0.301}", font_size=FONT_SIZE_BODY, color=GRAY_A),
            MathTex(r"\approx 3", font_size=FONT_SIZE_BODY, color=COLOR_HIGHLIGHT)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 3)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        
        # 幂运算法则
        self.play(
            Create(power_box),
            Write(power_rule),
            run_time=1.0
        )
        self.wait(0.3)
        
        # 幂运算示例
        for line in power_example:
            self.play(Write(line), run_time=0.4)
            self.wait(0.15)
        
        self.wait(0.6)
        
        # 换底公式
        self.play(Write(change_base_title), run_time=0.6)
        self.play(
            Create(change_base_box),
            Write(change_base_formula),
            run_time=1.2
        )
        self.wait(0.3)
        
        # 换底示例
        for line in change_base_example:
            self.play(Write(line), run_time=0.4)
            self.wait(0.15)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(power_box),
            FadeOut(power_rule),
            FadeOut(power_example),
            FadeOut(change_base_title),
            FadeOut(change_base_box),
            FadeOut(change_base_formula),
            FadeOut(change_base_example),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 总结与片尾 (8-10秒)"""
        # 标题
        title = Text(
            "对数四要素",
            font=AUTHOR_FONT,
            font_size=FONT_SIZE_TITLE,
            color=GOLD
        ).move_to(UP * 6.5)
        
        # 四大要点卡片
        cards_data = [
            ("定义", r"a^x = N \Leftrightarrow x = \log_a N", COLOR_PRIMARY),
            ("恒等式", r"a^{\log_a N} = N", COLOR_FORMULA),
            ("运算", r"\log_a(MN) = \log_a M + \log_a N", COLOR_SECONDARY),
            ("换底", r"\log_a b = \frac{\log_c b}{\log_c a}", GOLD)
        ]
        
        cards = VGroup()
        
        for i, (title_text, formula_text, color) in enumerate(cards_data):
            # 标题
            card_title = Text(
                title_text,
                font=AUTHOR_FONT,
                font_size=FONT_SIZE_BODY,
                color=WHITE
            )
            
            # 公式
            card_formula = MathTex(
                formula_text,
                font_size=FONT_SIZE_SMALL + 2,
                color=GRAY_A
            )
            
            # 组合
            card_content = VGroup(card_title, card_formula).arrange(DOWN, buff=0.2)
            
            # 背景框
            card_bg = SurroundingRectangle(
                card_content,
                color=color,
                buff=0.3,
                corner_radius=0.1,
                stroke_width=2,
                fill_opacity=0.05
            )
            
            card = VGroup(card_bg, card_content)
            card.move_to(UP * (3 - i * 1.8))
            
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            
            cards.add(card)
        
        # 动画序列
        self.play(Write(title), run_time=0.6)
        self.wait(0.4)
        
        # 卡片依次滑入
        for card in cards:
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.4
            )
            self.wait(0.1)
        
        # 整体闪烁强调
        for card in cards:
            self.play(
                card[0].animate.set_stroke(width=4),
                run_time=0.15
            )
        
        self.wait(0.6)
        
        # 清除卡片
        self.play(
            FadeOut(title),
            FadeOut(cards),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            AUTHOR_NAME,
            font=AUTHOR_FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            AUTHOR_ID,
            font=AUTHOR_FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP*0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font=AUTHOR_FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP*0.3, scale=1.1), run_time=0.6)
        
        # 对数符号装饰
        log_symbols = VGroup(*[
            MathTex(r"\log", font_size=32, color=color)
            for color in [COLOR_PRIMARY, COLOR_SECONDARY, COLOR_FORMULA, GOLD]
        ]).arrange(RIGHT, buff=0.8).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(symbol, scale=0.5) for symbol in log_symbols],
            run_time=0.6
        )
        
        # 旋转动画
        self.play(
            Rotate(log_symbols, angle=PI/4),
            run_time=1.5,
            rate_func=there_and_back
        )
        
        self.wait(0.5)
        
        # 总结文字
        summary = Text(
            "掌握对数，解题更轻松！",
            font=AUTHOR_FONT,
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary, shift=UP*0.3), run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(log_symbols),
            FadeOut(summary),
            run_time=1.0
        )


# ===== 运行说明 =====
"""
渲染命令:

快速预览（低质量）:
manim -pql logarithm_concepts.py LogarithmConcepts

中等质量:
manim -qm logarithm_concepts.py LogarithmConcepts

高质量（1080p）:
manim -qh logarithm_concepts.py LogarithmConcepts

4K质量:
manim -qk logarithm_concepts.py LogarithmConcepts

透明背景:
manim -qh -t logarithm_concepts.py LogarithmConcepts

GIF格式:
manim -qm --format gif logarithm_concepts.py LogarithmConcepts
"""