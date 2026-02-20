"""
算法初步 - 经典算法案例动画
Classic Algorithm Cases for High School Mathematics

内容: 辗转相除法、秦九韶算法、进制转换
目标观众: 高二学生
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


class ClassicAlgorithms(Scene):
    """
    经典算法案例教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 辗转相除法 - 介绍
    3. 辗转相除法 - 演示
    4. 秦九韶算法 - 介绍
    5. 秦九韶算法 - 演示
    6. 进制转换 - 介绍
    7. 进制转换 - 演示
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"    # 红色
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色
        self.COLOR_AUXILIARY = GRAY_B       # 灰色
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色
        self.COLOR_ALGORITHM_1 = "#e74c3c"  # 辗转相除法
        self.COLOR_ALGORITHM_2 = "#3498db"  # 秦九韶算法
        self.COLOR_ALGORITHM_3 = "#9b59b6"  # 进制转换
        
        # 字体配置
        self.FONT = "Noto Sans CJK SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_euclidean_intro()
        self.show_euclidean_demo()
        self.show_horner_intro()
        self.show_horner_demo()
        self.show_conversion_intro()
        self.show_conversion_demo()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook = Text(
            "这三个古老算法",
            font=self.FONT,
            font_size=42,
            color=WHITE
        ).move_to(UP * 5.5)
        
        hook2 = Text(
            "至今仍在计算机中使用！",
            font=self.FONT,
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)
        
        # 三个算法图标
        icon1 = self.create_algorithm_icon(
            "辗转相除法",
            "GCD",
            self.COLOR_ALGORITHM_1,
            UP * 2
        )
        
        icon2 = self.create_algorithm_icon(
            "秦九韶算法",
            "Horner",
            self.COLOR_ALGORITHM_2,
            ORIGIN
        )
        
        icon3 = self.create_algorithm_icon(
            "进制转换",
            "Base",
            self.COLOR_ALGORITHM_3,
            DOWN * 2
        )
        
        icons = VGroup(icon1, icon2, icon3)
        
        for i, icon in enumerate(icons):
            self.play(
                FadeIn(icon, scale=0.5),
                Flash(icon[0], color=self.COLOR_HIGHLIGHT, flash_radius=0.4),
                run_time=0.6
            )
            if i < len(icons) - 1:
                self.wait(0.2)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(hook2),
            run_time=0.5
        )
        
        # 图标移到侧边栏（缩小）
        side_icons = icons.copy().scale(0.4).arrange(DOWN, buff=0.3).to_edge(RIGHT, buff=0.5).shift(UP * 2)
        self.play(Transform(icons, side_icons), run_time=0.6)
        self.side_icons = icons
    
    def create_algorithm_icon(self, chinese, english, color, position):
        """创建算法图标卡片"""
        # 圆形图标
        circle = Circle(radius=0.5, fill_color=color, fill_opacity=0.8, stroke_width=2, stroke_color=WHITE)
        
        # 英文缩写
        en_text = Text(english, font="Arial", font_size=24, color=WHITE)
        
        icon_group = VGroup(circle, en_text)
        
        # 中文标签
        cn_text = Text(chinese, font=self.FONT, font_size=28, color=WHITE)
        
        full_group = VGroup(icon_group, cn_text).arrange(RIGHT, buff=0.4)
        full_group.move_to(position)
        
        return full_group
    
    def show_euclidean_intro(self):
        """场景2: 辗转相除法 - 介绍"""
        # 标题
        title = Text(
            "辗转相除法",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_ALGORITHM_1
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "欧几里得算法 · 求最大公约数",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 核心公式
        formula = MathTex(
            r"\gcd(a, b) = \gcd(b, a \bmod b)",
            font_size=32
        ).move_to(UP * 3)
        
        self.play(Write(formula), run_time=1.0)
        
        # 示例
        example_label = Text(
            "示例:",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.5 + LEFT * 2)
        
        example = MathTex(
            r"\gcd(48, 18) = \, ?",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1 + RIGHT * 0.5)
        
        self.play(FadeIn(example_label), FadeIn(example, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1.2)
        
        # 保存标题引用
        self.euclidean_title = title
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(formula),
            FadeOut(example_label),
            FadeOut(example),
            run_time=0.5
        )
    
    def show_euclidean_demo(self):
        """场景3: 辗转相除法 - 演示"""
        # 创建表格
        table_data = [
            ["步骤", "a", "b", "a ÷ b", "余数"],
        ]
        
        steps = [
            ["1", "48", "18", "2", "12"],
            ["2", "18", "12", "1", "6"],
            ["3", "12", "6", "2", "0"],
        ]
        
        # 表头
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": self.COLOR_AUXILIARY}
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(table), run_time=0.5)
        
        # 逐步添加行
        current_a = 48
        current_b = 18
        y_offset = UP * 1.2
        
        for i, step in enumerate(steps):
            # 步骤行
            step_row = self.create_table_row(step, y_offset - DOWN * (i * 0.8))
            
            self.play(FadeIn(step_row, shift=UP * 0.2), run_time=0.5)
            
            # 计算说明
            if i < len(steps) - 1:
                next_gcd = MathTex(
                    f"\\gcd({current_a}, {current_b}) = \\gcd({current_b}, {int(step[4])})",
                    font_size=24,
                    color=self.COLOR_PRIMARY
                ).move_to(DOWN * 2)
                
                self.play(Write(next_gcd), run_time=0.8)
                self.wait(0.7)
                self.play(FadeOut(next_gcd), run_time=0.3)
                
                current_a = current_b
                current_b = int(step[4])
            else:
                # 最后一步 - 高亮结果
                result_box = SurroundingRectangle(
                    step_row,
                    color=self.COLOR_SUCCESS,
                    buff=0.1,
                    stroke_width=3
                )
                
                self.play(Create(result_box), run_time=0.5)
                
                result_text = Text(
                    f"答案: gcd(48, 18) = 6",
                    font=self.FONT,
                    font_size=28,
                    color=self.COLOR_SUCCESS
                ).move_to(DOWN * 3)
                
                self.play(Write(result_text), run_time=0.8)
                self.play(
                    Flash(result_text, color=self.COLOR_SUCCESS, flash_radius=0.5),
                    run_time=0.4
                )
                
                self.wait(2.0)
                
                # 清理
                self.play(
                    FadeOut(table),
                    FadeOut(step_row),
                    FadeOut(result_box),
                    FadeOut(result_text),
                    run_time=0.6
                )
        
        # 缩小标题
        small_title = self.euclidean_title.copy().scale(0.5).to_corner(UL, buff=0.5)
        self.play(Transform(self.euclidean_title, small_title), run_time=0.4)
    
    def create_table_row(self, data, position):
        """创建表格行"""
        cells = VGroup()
        x_positions = [-3, -1.5, 0, 1.5, 3]
        
        for i, value in enumerate(data):
            cell_text = Text(
                value,
                font=self.FONT if i == 0 else "Arial",
                font_size=22,
                color=WHITE if i == 0 else self.COLOR_PRIMARY
            ).move_to(position + RIGHT * x_positions[i])
            
            cells.add(cell_text)
        
        return cells
    
    def show_horner_intro(self):
        """场景4: 秦九韶算法 - 介绍"""
        # 标题
        title = Text(
            "秦九韶算法",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_ALGORITHM_2
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Horner方法 · 高效计算多项式",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 普通形式
        normal_form = MathTex(
            r"f(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0",
            font_size=24
        ).move_to(UP * 2.5)
        
        self.play(Write(normal_form), run_time=1.2)
        
        # 箭头
        arrow = Arrow(
            UP * 1.5,
            UP * 0.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=6
        )
        
        transform_text = Text(
            "嵌套形式",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow, RIGHT, buff=0.2)
        
        self.play(Create(arrow), FadeIn(transform_text), run_time=0.5)
        
        # 嵌套形式
        nested_form = MathTex(
            r"f(x) = (\cdots((a_n x + a_{n-1})x + a_{n-2})x + \cdots + a_1)x + a_0",
            font_size=22
        ).move_to(DOWN * 0.5)
        
        self.play(Write(nested_form), run_time=1.0)
        
        # 优势说明
        advantage = Text(
            "优势: 减少乘法次数，提高效率",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(advantage), run_time=0.8)
        
        self.wait(1.3)
        
        # 保存标题引用
        self.horner_title = title
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(normal_form),
            FadeOut(arrow),
            FadeOut(transform_text),
            FadeOut(nested_form),
            FadeOut(advantage),
            run_time=0.6
        )
    
    def show_horner_demo(self):
        """场景5: 秦九韶算法 - 演示"""
        # 示例多项式
        poly = MathTex(
            r"f(x) = 2x^3 + 3x^2 - 5x + 1",
            font_size=28
        ).move_to(UP * 3.5)
        
        x_value = MathTex(
            r"x = 2",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8)
        
        self.play(Write(poly), run_time=0.8)
        self.play(FadeIn(x_value), run_time=0.5)
        
        # 计算步骤
        steps = [
            (r"v_0 = a_3 = 2", 2),
            (r"v_1 = v_0 \times 2 + 3 = 7", 7),
            (r"v_2 = v_1 \times 2 - 5 = 9", 9),
            (r"v_3 = v_2 \times 2 + 1 = 19", 19),
        ]
        
        y_pos = UP * 1.5
        
        for i, (step_tex, value) in enumerate(steps):
            # 步骤公式
            step = MathTex(
                step_tex,
                font_size=26
            ).move_to(y_pos - DOWN * (i * 0.7))
            
            # 高亮当前步骤
            if i == 0:
                step.set_color(self.COLOR_PRIMARY)
            
            self.play(Write(step), run_time=0.8)
            
            # 显示中间结果
            if i < len(steps) - 1:
                result = MathTex(
                    f"= {value}",
                    font_size=26,
                    color=self.COLOR_SUCCESS
                ).next_to(step, RIGHT, buff=0.3)
                
                self.play(FadeIn(result, shift=LEFT * 0.2), run_time=0.5)
                self.wait(0.7)
            else:
                # 最终结果
                result_box = SurroundingRectangle(
                    step,
                    color=self.COLOR_SUCCESS,
                    buff=0.15,
                    stroke_width=3
                )
                
                self.play(Create(result_box), run_time=0.5)
                
                final_result = Text(
                    "f(2) = 19",
                    font=self.FONT,
                    font_size=32,
                    color=self.COLOR_SUCCESS
                ).move_to(DOWN * 3)
                
                self.play(Write(final_result), run_time=1.0)
                self.play(
                    Flash(final_result, color=self.COLOR_SUCCESS, flash_radius=0.5),
                    run_time=0.4
                )
        
        # 对比说明
        comparison = Text(
            "仅需 3 次乘法！",
            font=self.FONT,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(comparison), run_time=0.8)
        
        self.wait(1.8)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info and mob != self.side_icons],
            run_time=0.6
        )
    
    def show_conversion_intro(self):
        """场景6: 进制转换 - 介绍"""
        # 标题
        title = Text(
            "进制转换算法",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_ALGORITHM_3
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 左右两个卡片
        left_card = self.create_conversion_card(
            "十进制 → k进制",
            "除k取余，逆序排列",
            self.COLOR_ALGORITHM_3,
            LEFT * 2 + UP * 2
        )
        
        right_card = self.create_conversion_card(
            "k进制 → 十进制",
            "按权展开，求和",
            self.COLOR_PRIMARY,
            RIGHT * 2 + UP * 2
        )
        
        self.play(FadeIn(left_card, shift=RIGHT * 0.5), run_time=0.7)
        self.play(FadeIn(right_card, shift=LEFT * 0.5), run_time=0.7)
        
        # 公式
        left_formula = MathTex(
            r"\text{Repeat: } n \div k \rightarrow \text{quotient, remainder}",
            font_size=20
        ).move_to(LEFT * 2 + UP * 0.5)
        
        right_formula = MathTex(
            r"\sum_{i=0}^{n} a_i k^i",
            font_size=28
        ).move_to(RIGHT * 2 + UP * 0.5)
        
        self.play(Write(left_formula), run_time=1.0)
        self.play(Write(right_formula), run_time=1.0)
        
        self.wait(1.8)
        
        # 保存标题和卡片引用
        self.conversion_title = title
        self.conversion_cards = VGroup(left_card, right_card)
        
        # 清理公式
        self.play(
            FadeOut(left_formula),
            FadeOut(right_formula),
            run_time=0.5
        )
        
        # 卡片缩小移到顶部
        small_cards = self.conversion_cards.copy().scale(0.5).arrange(RIGHT, buff=0.5).move_to(UP * 4)
        self.play(Transform(self.conversion_cards, small_cards), run_time=0.5)
    
    def create_conversion_card(self, title_text, subtitle_text, color, position):
        """创建进制转换卡片"""
        # 背景矩形
        rect = RoundedRectangle(
            width=3.5,
            height=1.5,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title = Text(
            title_text,
            font=self.FONT,
            font_size=24,
            color=WHITE
        ).move_to(rect.get_center() + UP * 0.3)
        
        # 副标题
        subtitle = Text(
            subtitle_text,
            font=self.FONT,
            font_size=18,
            color=GRAY_A
        ).move_to(rect.get_center() + DOWN * 0.3)
        
        card = VGroup(rect, title, subtitle)
        card.move_to(position)
        
        return card
    
    def show_conversion_demo(self):
        """场景7: 进制转换 - 演示"""
        # Part A: 十进制转二进制
        demo_title_1 = Text(
            "示例1: 十进制 → 二进制",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_ALGORITHM_3
        ).move_to(UP * 2.5 + LEFT * 2)
        
        self.play(FadeIn(demo_title_1), run_time=0.5)
        
        # 示例
        example_1 = MathTex(
            r"25_{10} \rightarrow \, ?_2",
            font_size=26
        ).move_to(UP * 1.8 + LEFT * 2)
        
        self.play(Write(example_1), run_time=0.5)
        
        # 计算步骤
        steps_1 = [
            (r"25 \div 2 = 12 \cdots 1", LEFT * 2 + UP * 1),
            (r"12 \div 2 = 6 \cdots 0", LEFT * 2 + UP * 0.3),
            (r"6 \div 2 = 3 \cdots 0", LEFT * 2 + DOWN * 0.4),
            (r"3 \div 2 = 1 \cdots 1", LEFT * 2 + DOWN * 1.1),
            (r"1 \div 2 = 0 \cdots 1", LEFT * 2 + DOWN * 1.8),
        ]
        
        remainders = []
        for step_tex, pos in steps_1:
            step = MathTex(step_tex, font_size=22).move_to(pos)
            self.play(Write(step), run_time=0.7)
            
            # 提取余数
            remainder = step_tex.split("cdots")[1].strip()
            remainders.append(remainder)
            
            self.wait(0.5)
        
        # 逆序排列
        arrow_up = Arrow(
            LEFT * 2 + DOWN * 2.5,
            LEFT * 2 + DOWN * 3.5,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        )
        
        reverse_text = Text(
            "逆序排列",
            font=self.FONT,
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).next_to(arrow_up, RIGHT, buff=0.2)
        
        self.play(Create(arrow_up), FadeIn(reverse_text), run_time=0.5)
        
        # 结果
        result_1 = MathTex(
            r"25_{10} = 11001_2",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(LEFT * 2 + DOWN * 4.5)
        
        self.play(Write(result_1), run_time=1.0)
        self.wait(0.5)
        
        # Part B: 二进制转十进制
        demo_title_2 = Text(
            "示例2: 二进制 → 十进制",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.5 + RIGHT * 2)
        
        self.play(FadeIn(demo_title_2), run_time=0.5)
        
        # 示例
        example_2 = MathTex(
            r"1101_2 \rightarrow \, ?_{10}",
            font_size=26
        ).move_to(UP * 1.8 + RIGHT * 2)
        
        self.play(Write(example_2), run_time=0.5)
        
        # 展开公式
        expansion = MathTex(
            r"1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0",
            font_size=20
        ).move_to(UP * 0.8 + RIGHT * 2)
        
        self.play(Write(expansion), run_time=1.5)
        
        # 逐项计算
        calc_steps = MathTex(
            r"= 8 + 4 + 0 + 1",
            font_size=24
        ).move_to(DOWN * 0.2 + RIGHT * 2)
        
        self.play(Write(calc_steps), run_time=1.5)
        
        # 求和
        sum_result = MathTex(
            r"= 13_{10}",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.2 + RIGHT * 2)
        
        self.play(Write(sum_result), run_time=1.0)
        
        # 高亮结果
        result_box = SurroundingRectangle(
            sum_result,
            color=self.COLOR_SUCCESS,
            buff=0.15,
            stroke_width=3
        )
        
        self.play(Create(result_box), run_time=0.5)
        self.play(
            Flash(sum_result, color=self.COLOR_SUCCESS, flash_radius=0.4),
            run_time=0.4
        )
        
        self.wait(1.6)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info and mob != self.side_icons],
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结与片尾"""
        # 三大算法卡片重现
        summary_title = Text(
            "三大经典算法",
            font=self.FONT,
            font_size=40,
            color=GOLD
        ).move_to(UP * 5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 精简卡片
        card_1 = self.create_summary_card(
            "辗转相除法",
            "高效求最大公约数",
            self.COLOR_ALGORITHM_1,
            UP * 2.5
        )
        
        card_2 = self.create_summary_card(
            "秦九韶算法",
            "快速计算多项式值",
            self.COLOR_ALGORITHM_2,
            UP * 0.8
        )
        
        card_3 = self.create_summary_card(
            "进制转换",
            "不同进制间灵活转换",
            self.COLOR_ALGORITHM_3,
            DOWN * 0.9
        )
        
        cards = VGroup(card_1, card_2, card_3)
        
        # 卡片滑入
        for card in cards:
            card.shift(LEFT * 10)
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
        
        # 核心要点
        key_point = Text(
            "高效 · 精确 · 实用",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.8)
        
        # 应用场景
        application = Text(
            "广泛应用于: 计算机科学、密码学、人工智能",
            font=self.FONT,
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(application), run_time=0.8)
        
        self.wait(1.0)
        
        # 清理上半部分
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(key_point),
            FadeOut(application),
            FadeOut(self.side_icons),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多算法技巧！",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰小图标
        icons = VGroup(*[
            Circle(radius=0.2, fill_color=c, fill_opacity=0.8, stroke_width=0)
            for c in [self.COLOR_ALGORITHM_1, self.COLOR_ALGORITHM_2, self.COLOR_ALGORITHM_3]
        ]).arrange(RIGHT, buff=0.5).move_to(DOWN * 2)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.play(icons.animate.scale(1.2), run_time=0.5)
        self.play(icons.animate.scale(1/1.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(icons),
            run_time=1.0
        )
    
    def create_summary_card(self, title_text, subtitle_text, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(radius=0.3, fill_color=color, fill_opacity=0.8, stroke_width=0)
        
        # 文字
        title = Text(title_text, font=self.FONT, font_size=28, color=WHITE)
        subtitle = Text(subtitle_text, font=self.FONT, font_size=18, color=GRAY_A)
        
        text_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15)
        
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card


# 运行命令示例:
# manim -pql classic_algorithms.py ClassicAlgorithms  # 快速预览
# manim -qh classic_algorithms.py ClassicAlgorithms   # 高质量输出