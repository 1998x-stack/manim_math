"""
幂的运算法则动画 - Power Operation Laws Animation
使用 Manim 创建的七年级数学教学视频

内容: 同底数幂相乘、幂的乘方、积的乘方、同底数幂相除
目标观众: 七年级学生
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


class PowerOperationLaws(Scene):
    """
    幂的运算法则教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 法则一 - 同底数幂相乘
    3. 法则二 - 幂的乘方
    4. 法则三 - 积的乘方
    5. 法则四 - 同底数幂相除
    6. 四法则总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要公式
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 底数
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_EXPONENT = "#2ecc71"     # 绿色 - 指数
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 位置配置
        self.TITLE_Y = 5.5
        self.FORMULA_Y = 2.0
        self.EXAMPLE_Y = -0.5
        self.EXPLAIN_Y = -3.5
        
        # 执行动画序列
        self.show_opening()
        self.show_law_1_same_base_multiply()
        self.show_law_2_power_of_power()
        self.show_law_3_product_power()
        self.show_law_4_same_base_divide()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_chinese = Text(
            "你会算吗?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        hook_question = MathTex(
            r"2^3 \times 2^5 = \,?",
            font_size=60,
            color=WHITE
        ).move_to(UP * 2)
        
        # 分别着色
        hook_question.set_color_by_tex("2", self.COLOR_SECONDARY)
        hook_question.set_color_by_tex("?", self.COLOR_HIGHLIGHT)
        
        self.play(Write(hook_chinese), run_time=0.8)
        self.play(Write(hook_question), run_time=1.0)
        
        # 思考提示
        hint = Text(
            "别急着展开计算!",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        
        # 问号闪烁
        question_mark = hook_question[-1]
        self.play(
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_chinese),
            FadeOut(hook_question),
            FadeOut(hint),
            run_time=0.5
        )
    
    def show_law_1_same_base_multiply(self):
        """场景2: 法则一 - 同底数幂相乘"""
        # 标题
        title = Text(
            "法则一：同底数幂相乘",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 通用公式
        formula = MathTex(
            r"a^m \times a^n = a^{m+n}",
            font_size=48
        ).move_to(UP * self.FORMULA_Y)
        
        # 着色
        formula.set_color_by_tex("a", self.COLOR_SECONDARY)
        formula.set_color_by_tex("m", self.COLOR_EXPONENT)
        formula.set_color_by_tex("n", self.COLOR_EXPONENT)
        
        self.play(Write(formula), run_time=1.2)
        
        # 关键提示
        key_point = Text(
            "底数不变，指数相加",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(key_point), run_time=0.6)
        self.wait(1.0)
        
        # 具体例子
        example_label = Text(
            "例子:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * self.EXAMPLE_Y + LEFT * 3)
        
        example = MathTex(
            r"2^3 \times 2^5 = 2^{3+5} = 2^8",
            font_size=40
        ).next_to(example_label, RIGHT, buff=0.3)
        
        example.set_color_by_tex("2", self.COLOR_SECONDARY)
        example.set_color_by_tex("3", self.COLOR_EXPONENT)
        example.set_color_by_tex("5", self.COLOR_EXPONENT)
        example.set_color_by_tex("8", self.COLOR_EXPONENT)
        
        self.play(
            FadeIn(example_label),
            Write(example),
            run_time=1.5
        )
        
        # 可视化解释
        explain_1 = MathTex(
            r"2^3 = 2 \times 2 \times 2",
            font_size=32
        ).move_to(UP * self.EXPLAIN_Y)
        explain_1.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        explain_2 = MathTex(
            r"2^5 = 2 \times 2 \times 2 \times 2 \times 2",
            font_size=32
        ).next_to(explain_1, DOWN, buff=0.3)
        explain_2.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        self.play(
            FadeIn(explain_1, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(
            FadeIn(explain_2, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 合并说明
        merge_text = Text(
            "共有 3+5=8 个底数相乘",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(explain_2, DOWN, buff=0.5)
        
        self.play(FadeIn(merge_text), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(key_point),
            FadeOut(example_label),
            FadeOut(example),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(merge_text),
            run_time=0.6
        )
    
    def show_law_2_power_of_power(self):
        """场景3: 法则二 - 幂的乘方"""
        # 标题
        title = Text(
            "法则二：幂的乘方",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 通用公式
        formula = MathTex(
            r"(a^m)^n = a^{mn}",
            font_size=48
        ).move_to(UP * self.FORMULA_Y)
        
        formula.set_color_by_tex("a", self.COLOR_SECONDARY)
        formula.set_color_by_tex("m", self.COLOR_EXPONENT)
        formula.set_color_by_tex("n", self.COLOR_EXPONENT)
        
        self.play(Write(formula), run_time=1.2)
        
        # 关键提示
        key_point = Text(
            "底数不变，指数相乘",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(key_point), run_time=0.6)
        self.wait(0.8)
        
        # 具体例子
        example_label = Text(
            "例子:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * self.EXAMPLE_Y + LEFT * 3)
        
        example = MathTex(
            r"(2^3)^2 = 2^{3 \times 2} = 2^6",
            font_size=40
        ).next_to(example_label, RIGHT, buff=0.3)
        
        example.set_color_by_tex("2", self.COLOR_SECONDARY)
        example.set_color_by_tex("3", self.COLOR_EXPONENT)
        example.set_color_by_tex("6", self.COLOR_EXPONENT)
        
        self.play(
            FadeIn(example_label),
            Write(example),
            run_time=1.5
        )
        
        # 可视化解释
        explain_1 = MathTex(
            r"(2^3)^2 = 2^3 \times 2^3",
            font_size=32
        ).move_to(UP * self.EXPLAIN_Y)
        explain_1.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        explain_2 = MathTex(
            r"= (2 \times 2 \times 2) \times (2 \times 2 \times 2)",
            font_size=28
        ).next_to(explain_1, DOWN, buff=0.3)
        explain_2.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        self.play(FadeIn(explain_1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(explain_2, shift=UP * 0.2), run_time=0.8)
        
        # 合并说明
        merge_text = Text(
            "共有 3×2=6 个底数相乘",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(explain_2, DOWN, buff=0.5)
        
        self.play(FadeIn(merge_text), run_time=0.6)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(key_point),
            FadeOut(example_label),
            FadeOut(example),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(merge_text),
            run_time=0.6
        )
    
    def show_law_3_product_power(self):
        """场景4: 法则三 - 积的乘方"""
        # 标题
        title = Text(
            "法则三：积的乘方",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 通用公式
        formula = MathTex(
            r"(ab)^n = a^n b^n",
            font_size=48
        ).move_to(UP * self.FORMULA_Y)
        
        formula.set_color_by_tex("a", self.COLOR_SECONDARY)
        formula.set_color_by_tex("b", "#f39c12")  # 橙色
        formula.set_color_by_tex("n", self.COLOR_EXPONENT)
        
        self.play(Write(formula), run_time=1.2)
        
        # 关键提示
        key_point = Text(
            "每个因数分别乘方",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(key_point), run_time=0.6)
        self.wait(0.8)
        
        # 具体例子
        example_label = Text(
            "例子:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * self.EXAMPLE_Y + LEFT * 3.2)
        
        example = MathTex(
            r"(2 \times 3)^2 = 2^2 \times 3^2",
            font_size=40
        ).next_to(example_label, RIGHT, buff=0.3)
        
        example[0][1].set_color(self.COLOR_SECONDARY)  # 2
        example[0][3].set_color("#f39c12")  # 3
        example[0][7].set_color(self.COLOR_SECONDARY)  # 2
        example[0][10].set_color("#f39c12")  # 3
        
        self.play(
            FadeIn(example_label),
            Write(example),
            run_time=1.5
        )
        
        # 计算验证
        verify_1 = MathTex(
            r"= 4 \times 9 = 36",
            font_size=36
        ).next_to(example, DOWN, buff=0.5)
        
        verify_2_chinese = Text(
            "验证：",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * self.EXPLAIN_Y + LEFT * 3.2)
        
        verify_2 = MathTex(
            r"(2 \times 3)^2 = 6^2 = 36",
            font_size=32
        ).next_to(verify_2_chinese, RIGHT, buff=0.3)
        
        verify_2[0][1].set_color(self.COLOR_SECONDARY)
        verify_2[0][3].set_color("#f39c12")
        
        self.play(Write(verify_1), run_time=0.8)
        self.wait(0.5)
        self.play(
            FadeIn(verify_2_chinese),
            Write(verify_2),
            run_time=1.0
        )
        
        # 正确标记
        check_mark = Text(
            "✓ 结果一致!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EXPONENT
        ).next_to(verify_2, DOWN, buff=0.5)
        
        self.play(FadeIn(check_mark, scale=1.2), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(key_point),
            FadeOut(example_label),
            FadeOut(example),
            FadeOut(verify_1),
            FadeOut(verify_2_chinese),
            FadeOut(verify_2),
            FadeOut(check_mark),
            run_time=0.6
        )
    
    def show_law_4_same_base_divide(self):
        """场景5: 法则四 - 同底数幂相除"""
        # 标题
        title = Text(
            "法则四：同底数幂相除",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * self.TITLE_Y)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.8)
        
        # 通用公式（带条件）
        formula = MathTex(
            r"a^m \div a^n = a^{m-n}",
            font_size=48
        ).move_to(UP * (self.FORMULA_Y + 0.5))
        
        formula.set_color_by_tex("a", self.COLOR_SECONDARY)
        formula.set_color_by_tex("m", self.COLOR_EXPONENT)
        formula.set_color_by_tex("n", self.COLOR_EXPONENT)
        
        condition = MathTex(
            r"(a \neq 0)",
            font_size=32,
            color="#f39c12"
        ).next_to(formula, RIGHT, buff=0.3)
        
        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(condition), run_time=0.4)
        
        # 关键提示
        key_point = Text(
            "底数不变，指数相减",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(key_point), run_time=0.6)
        self.wait(1.0)
        
        # 具体例子
        example_label = Text(
            "例子:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * self.EXAMPLE_Y + LEFT * 3)
        
        example = MathTex(
            r"2^5 \div 2^3 = 2^{5-3} = 2^2 = 4",
            font_size=40
        ).next_to(example_label, RIGHT, buff=0.3)
        
        example.set_color_by_tex("2", self.COLOR_SECONDARY)
        example.set_color_by_tex("5", self.COLOR_EXPONENT)
        example.set_color_by_tex("3", self.COLOR_EXPONENT)
        
        self.play(
            FadeIn(example_label),
            Write(example),
            run_time=1.5
        )
        
        # 可视化解释
        explain_1 = MathTex(
            r"2^5 = 2 \times 2 \times 2 \times 2 \times 2",
            font_size=28
        ).move_to(UP * (self.EXPLAIN_Y + 0.5))
        explain_1.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        explain_2 = MathTex(
            r"2^3 = 2 \times 2 \times 2",
            font_size=28
        ).next_to(explain_1, DOWN, buff=0.3)
        explain_2.set_color_by_tex("2", self.COLOR_SECONDARY)
        
        self.play(FadeIn(explain_1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(explain_2, shift=UP * 0.2), run_time=0.8)
        
        # 约分说明
        cancel_text = Text(
            "约去3个2，剩余 5-3=2 个",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).next_to(explain_2, DOWN, buff=0.5)
        
        self.play(FadeIn(cancel_text), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(condition),
            FadeOut(key_point),
            FadeOut(example_label),
            FadeOut(example),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(cancel_text),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 四法则总结"""
        # 标题
        title = Text(
            "幂的运算四大法则",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        
        # 创建四个法则卡片
        cards = VGroup()
        
        # 卡片1: 同底数幂相乘
        card_1 = self.create_law_card(
            "法则1",
            r"a^m \times a^n = a^{m+n}",
            "底数不变，指数相加",
            self.COLOR_PRIMARY,
            UP * 3
        )
        cards.add(card_1)
        
        # 卡片2: 幂的乘方
        card_2 = self.create_law_card(
            "法则2",
            r"(a^m)^n = a^{mn}",
            "底数不变，指数相乘",
            self.COLOR_EXPONENT,
            UP * 1
        )
        cards.add(card_2)
        
        # 卡片3: 积的乘方
        card_3 = self.create_law_card(
            "法则3",
            r"(ab)^n = a^n b^n",
            "每个因数分别乘方",
            "#9b59b6",
            DOWN * 1
        )
        cards.add(card_3)
        
        # 卡片4: 同底数幂相除
        card_4 = self.create_law_card(
            "法则4",
            r"a^m \div a^n = a^{m-n}",
            "底数不变，指数相减",
            self.COLOR_SECONDARY,
            DOWN * 3
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 10)  # 初始位置在左侧外
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.6
            )
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 记忆口诀
        mnemonic = Text(
            "同底数看运算，乘加除减乘方乘",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(mnemonic, shift=UP * 0.3), run_time=0.8)
        
        # 所有卡片闪烁
        self.play(
            *[Flash(card, color=YELLOW, flash_radius=0.5) for card in cards],
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(mnemonic),
            run_time=0.6
        )
    
    def create_law_card(self, number, formula_tex, description, color, position):
        """创建法则卡片"""
        # 法则编号
        number_text = Text(
            number,
            font="PingFang SC",
            font_size=24,
            color=color,
            weight=BOLD
        )
        
        # 公式
        formula = MathTex(
            formula_tex,
            font_size=32
        )
        
        # 描述
        desc = Text(
            description,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card_content = VGroup(number_text, formula, desc).arrange(DOWN, buff=0.15)
        
        # 背景框
        box = SurroundingRectangle(
            card_content,
            color=color,
            buff=0.25,
            corner_radius=0.1,
            stroke_width=2
        )
        
        card = VGroup(box, card_content)
        card.move_to(position)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
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
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 装饰 - 小公式环绕
        decorations = VGroup()
        formulas_deco = [
            r"a^m",
            r"a^n",
            r"a^{m+n}",
            r"(a^m)^n",
        ]
        
        for i, formula in enumerate(formulas_deco):
            deco = MathTex(formula, font_size=28, color=self.COLOR_PRIMARY)
            angle = i * TAU / len(formulas_deco)
            deco.move_to(follow_text.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            decorations.add(deco)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.6
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 运行命令:
# manim -pql power_operation_laws.py PowerOperationLaws  # 快速预览
# manim -qh power_operation_laws.py PowerOperationLaws   # 高质量渲染