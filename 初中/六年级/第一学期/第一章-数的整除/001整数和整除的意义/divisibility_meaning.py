"""
整数和整除的意义 教学动画
Integers and Divisibility Meaning Teaching Animation

使用 Manim 创建的小学数学教学视频
内容: 整除的概念、因数与倍数、整除符号
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

运行命令:
manim -pql divisibility_meaning.py DivisibilityMeaning  # 快速预览
manim -qh divisibility_meaning.py DivisibilityMeaning   # 高质量渲染
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DivisibilityMeaning(Scene):
    """
    整除的意义教学动画场景
    
    场景顺序:
    1. 开场钩子 - 生活场景
    2. 整除概念 - 定义和条件
    3. 视觉演示1 - 12÷3能整除
    4. 视觉演示2 - 12÷5不能整除
    5. 因数与倍数 - 概念引入
    6. 符号记法 - b|a的含义
    7. 片尾总结 - 关注引导
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要概念
        self.COLOR_DIVISIBLE = "#2ecc71"      # 绿色 - 能整除
        self.COLOR_NOT_DIVISIBLE = "#e74c3c"  # 红色 - 不能整除
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮强调
        self.COLOR_FACTOR = "#9b59b6"         # 紫色 - 因数
        self.COLOR_MULTIPLE = "#f39c12"       # 橙色 - 倍数
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助元素
        
        # 字体大小
        self.FONT_TITLE = 40
        self.FONT_SUBTITLE = 32
        self.FONT_BODY = 26
        self.FONT_SMALL = 22
        self.FONT_AUTHOR = 20
        self.FONT_FORMULA = 32
        
        # 方块大小
        self.SQUARE_SIZE = 0.35
        
        # 执行动画序列
        self.show_opening()
        self.show_concept()
        self.show_example_divisible()
        self.show_example_not_divisible()
        self.show_factor_multiple()
        self.show_notation()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 (5秒)"""
        # 作者信息（顶部，始终保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "12个苹果，怎么分?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.3)
        
        # 场景描述
        scenario = Text(
            "平均分给3个同学",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(scenario, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 问题
        question = Text(
            "每人能分到几个?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2)
        
        self.play(FadeIn(question), run_time=0.5)
        self.play(Flash(question, color=YELLOW, flash_radius=0.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(scenario),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_concept(self):
        """场景2: 整除概念介绍 (10秒)"""
        # 标题
        title = Text(
            "整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义
        definition = Text(
            "整数a除以不为零的整数b",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=1.0)
        self.wait(0.5)
        
        # 除法公式
        formula_text = Text(
            "a ÷ b =",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(UP * 2.5 + LEFT * 1.5)
        
        quotient = Text(
            "q",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula_text, RIGHT, buff=0.3)
        
        dots = Text(
            "...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).next_to(quotient, RIGHT, buff=0.3)
        
        remainder = Text(
            "r",
            font="Noto Sans CJK SC",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_DIVISIBLE
        ).next_to(dots, RIGHT, buff=0.3)
        
        formula = VGroup(formula_text, quotient, dots, remainder)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.5)
        
        # 条件1：商为整数
        condition_1 = Text(
            "① 商为整数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1)
        
        self.play(FadeIn(condition_1), run_time=0.6)
        self.play(quotient.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.4)
        self.wait(0.3)
        
        # 条件2：余数为零
        condition_2 = Text(
            "② 余数为零",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_DIVISIBLE
        ).move_to(UP * 0)
        
        self.play(FadeIn(condition_2), run_time=0.6)
        self.play(remainder.animate.set_color(self.COLOR_DIVISIBLE), run_time=0.4)
        self.wait(0.5)
        
        # 整体强调
        self.play(
            Flash(condition_1, color=YELLOW, flash_radius=0.4),
            Flash(condition_2, color=GREEN, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(formula),
            FadeOut(condition_1),
            FadeOut(condition_2),
            run_time=0.6
        )
    
    def show_example_divisible(self):
        """场景3: 视觉演示 - 12÷3能整除 (12秒)"""
        # 例题标题
        example_title = MathTex(
            r"12 \div 3 = \,?",
            font_size=self.FONT_TITLE
        ).move_to(UP * 5.5)
        
        self.play(Write(example_title), run_time=0.6)
        
        # 创建12个方块（4行3列）
        squares = VGroup()
        for i in range(3):  # 3列
            for j in range(4):  # 4行
                x = (i - 1) * 0.5
                y = 3 + (1.5 - j) * 0.5
                square = Square(
                    side_length=self.SQUARE_SIZE,
                    fill_color=self.COLOR_PRIMARY,
                    fill_opacity=0.7,
                    stroke_color=WHITE,
                    stroke_width=2
                ).move_to(np.array([x, y, 0]))
                squares.add(square)
        
        # 方块逐个出现
        self.play(
            *[FadeIn(square, scale=0.5) for square in squares],
            run_time=2.0,
            lag_ratio=0.1
        )
        
        # 说明文字
        explain_1 = Text(
            "12个方块",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(0.5)
        
        # 分组提示
        explain_2 = Text(
            "分成3组",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(Transform(explain_1, explain_2), run_time=0.5)
        self.wait(0.5)
        
        # 分组动画 - 移动到3个位置
        group_colors = [self.COLOR_FACTOR, self.COLOR_MULTIPLE, self.COLOR_PRIMARY]
        group_centers = [LEFT * 2.5, ORIGIN, RIGHT * 2.5]
        
        animations = []
        for i in range(3):  # 3组
            for j in range(4):  # 每组4个
                idx = i * 4 + j
                # 计算该组内的位置
                local_x = (j % 2 - 0.5) * 0.5
                local_y = 2.5 + (1 - j // 2) * 0.5
                target_pos = group_centers[i] + np.array([local_x, local_y, 0])
                
                animations.append(
                    squares[idx].animate.move_to(target_pos).set_fill(
                        group_colors[i], opacity=0.8
                    )
                )
        
        self.play(*animations, run_time=2.0)
        self.wait(0.5)
        
        # 每组计数
        group_labels = VGroup()
        for i, center in enumerate(group_centers):
            label = Text(
                "4",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SUBTITLE,
                color=group_colors[i]
            ).move_to(center + DOWN * 1.2)
            group_labels.add(label)
            
            # 该组的方块闪烁
            group_squares = squares[i*4:(i+1)*4]
            self.play(
                *[Flash(sq, color=WHITE, flash_radius=0.2) for sq in group_squares],
                FadeIn(label, scale=1.5),
                run_time=0.5
            )
        
        self.wait(0.5)
        
        # 结果公式
        result = MathTex(
            r"12 \div 3 = 4",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 0.5)
        
        self.play(
            FadeOut(explain_1),
            Write(result),
            run_time=0.8
        )
        
        # 余数显示
        remainder_text = Text(
            "余数 = 0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_DIVISIBLE
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(remainder_text), run_time=0.6)
        self.wait(0.3)
        
        # 成功标记
        success = VGroup(
            Text(
                "能整除!",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SUBTITLE,
                color=self.COLOR_DIVISIBLE
            ),
            Text(
                "✓",
                font="Noto Sans CJK SC",
                font_size=self.FONT_TITLE,
                color=self.COLOR_DIVISIBLE
            ).shift(RIGHT * 0.8)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2)
        
        self.play(
            FadeIn(success, shift=UP * 0.3, scale=1.2),
            Flash(success, color=GREEN, flash_radius=0.6),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(squares),
            FadeOut(group_labels),
            FadeOut(result),
            FadeOut(remainder_text),
            FadeOut(success),
            run_time=0.6
        )
    
    def show_example_not_divisible(self):
        """场景4: 视觉演示 - 12÷5不能整除 (12秒)"""
        # 例题标题
        example_title = MathTex(
            r"12 \div 5 = \,?",
            font_size=self.FONT_TITLE
        ).move_to(UP * 5.5)
        
        self.play(Write(example_title), run_time=0.6)
        
        # 创建12个方块
        squares = VGroup()
        for i in range(3):
            for j in range(4):
                x = (i - 1) * 0.5
                y = 3 + (1.5 - j) * 0.5
                square = Square(
                    side_length=self.SQUARE_SIZE,
                    fill_color=self.COLOR_PRIMARY,
                    fill_opacity=0.7,
                    stroke_color=WHITE,
                    stroke_width=2
                ).move_to(np.array([x, y, 0]))
                squares.add(square)
        
        self.play(
            *[FadeIn(square, scale=0.5) for square in squares],
            run_time=2.0,
            lag_ratio=0.1
        )
        
        # 分组提示
        explain = Text(
            "分成5组",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(0.5)
        
        # 分组 - 前10个分成5组，每组2个
        group_colors = [
            "#9b59b6", "#e74c3c", "#3498db", "#2ecc71", "#f39c12"
        ]
        group_x_positions = [-3, -1.5, 0, 1.5, 3]
        
        # 前10个方块分组
        animations = []
        for i in range(5):  # 5组
            for j in range(2):  # 每组2个
                idx = i * 2 + j
                local_y = 2.3 + (1 - j) * 0.5
                target_pos = np.array([group_x_positions[i], local_y, 0])
                
                animations.append(
                    squares[idx].animate.move_to(target_pos).set_fill(
                        group_colors[i], opacity=0.8
                    )
                )
        
        # 剩余2个方块位置
        for idx in [10, 11]:
            target_pos = np.array([group_x_positions[idx-10] + 0.6, 0.8, 0])
            animations.append(
                squares[idx].animate.move_to(target_pos)
            )
        
        self.play(*animations, run_time=2.0)
        self.wait(0.5)
        
        # 剩余方块闪烁（红色边框）
        remaining = VGroup(squares[10], squares[11])
        self.play(
            *[sq.animate.set_stroke(self.COLOR_NOT_DIVISIBLE, width=4) for sq in remaining],
            *[Flash(sq, color=RED, flash_radius=0.3) for sq in remaining],
            run_time=0.8
        )
        self.wait(0.4)
        
        # 结果公式
        result = MathTex(
            r"12 \div 5 = 2 \cdots 2",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 0.5)
        
        self.play(
            FadeOut(explain),
            Write(result),
            run_time=0.8
        )
        
        # 商和余数标注
        quotient_label = Text(
            "商 = 2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.5)
        
        remainder_label = Text(
            "余数 = 2",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_NOT_DIVISIBLE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(quotient_label), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(remainder_label), run_time=0.5)
        self.wait(0.3)
        
        # 失败标记
        failure = VGroup(
            Text(
                "不能整除!",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SUBTITLE,
                color=self.COLOR_NOT_DIVISIBLE
            ),
            Text(
                "✗",
                font="Noto Sans CJK SC",
                font_size=self.FONT_TITLE,
                color=self.COLOR_NOT_DIVISIBLE
            ).shift(RIGHT * 1)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(
            FadeIn(failure, shift=UP * 0.3),
            Flash(failure, color=RED, flash_radius=0.6),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(squares),
            FadeOut(result),
            FadeOut(quotient_label),
            FadeOut(remainder_label),
            FadeOut(failure),
            run_time=0.6
        )
    
    def show_factor_multiple(self):
        """场景5: 因数与倍数 (12秒)"""
        # 标题
        title = Text(
            "因数与倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 回顾例子
        example = MathTex(
            r"12 \div 3 = 4",
            font_size=self.FONT_FORMULA
        ).move_to(UP * 3.5)
        
        self.play(Write(example), run_time=0.8)
        self.wait(0.5)
        
        # 指向12和3的箭头
        arrow_to_3 = Arrow(
            start=example.get_left() + DOWN * 0.8,
            end=example.get_left() + LEFT * 0.3,
            color=self.COLOR_FACTOR,
            buff=0.1
        )
        
        arrow_to_12 = Arrow(
            start=example.get_left() + DOWN * 0.8 + RIGHT * 0.8,
            end=example.get_left() + RIGHT * 0.5,
            color=self.COLOR_MULTIPLE,
            buff=0.1
        )
        
        self.play(
            Create(arrow_to_3),
            run_time=0.6
        )
        
        # 因数定义
        factor_def = Text(
            "3 是 12 的因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FACTOR
        ).move_to(UP * 2)
        
        self.play(FadeIn(factor_def, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        self.play(Create(arrow_to_12), run_time=0.6)
        
        # 倍数定义
        multiple_def = Text(
            "12 是 3 的倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_MULTIPLE
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(multiple_def, shift=UP * 0.3), run_time=0.8)
        self.wait(0.5)
        
        # 双向关系
        relation_arrow_1 = Arrow(
            start=factor_def.get_right() + RIGHT * 0.2,
            end=multiple_def.get_right() + RIGHT * 0.2,
            color=YELLOW,
            buff=0.1
        )
        
        relation_arrow_2 = Arrow(
            start=multiple_def.get_left() + LEFT * 0.2,
            end=factor_def.get_left() + LEFT * 0.2,
            color=YELLOW,
            buff=0.1
        )
        
        self.play(
            Create(relation_arrow_1),
            Create(relation_arrow_2),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 关键提示
        key_point = Text(
            "因数 ≤ 倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeIn(key_point, shift=UP * 0.3, scale=1.1),
            Flash(key_point, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example),
            FadeOut(arrow_to_3),
            FadeOut(arrow_to_12),
            FadeOut(factor_def),
            FadeOut(multiple_def),
            FadeOut(relation_arrow_1),
            FadeOut(relation_arrow_2),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def show_notation(self):
        """场景6: 符号记法 b|a (10秒)"""
        # 标题
        title = Text(
            "整除的符号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 符号展示
        symbol = MathTex(
            r"b \mid a",
            font_size=60
        ).move_to(UP * 3.5)
        
        self.play(Write(symbol), run_time=1.0)
        self.wait(0.5)
        
        # 读法
        pronunciation = Text(
            "读作：b 整除 a",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 2)
        
        self.play(FadeIn(pronunciation), run_time=0.6)
        self.wait(0.4)
        
        # 含义
        meaning = Text(
            "表示：a 能被 b 整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 1)
        
        self.play(FadeIn(meaning), run_time=0.6)
        self.wait(0.5)
        
        # 例子1
        example_1 = MathTex(
            r"3 \mid 12",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_DIVISIBLE
        ).move_to(DOWN * 0.5)
        
        self.play(Write(example_1), run_time=0.6)
        
        explain_1 = Text(
            "12 能被 3 整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(0.4)
        
        # 例子2
        example_2 = MathTex(
            r"4 \mid 12",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_DIVISIBLE
        ).move_to(DOWN * 3)
        
        self.play(Write(example_2), run_time=0.6)
        
        explain_2 = Text(
            "12 能被 4 整除",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_2), run_time=0.5)
        self.wait(0.5)
        
        # 整体高亮
        self.play(
            Flash(symbol, color=YELLOW, flash_radius=0.6),
            Flash(example_1, color=GREEN, flash_radius=0.4),
            Flash(example_2, color=GREEN, flash_radius=0.4),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(symbol),
            FadeOut(pronunciation),
            FadeOut(meaning),
            FadeOut(example_1),
            FadeOut(explain_1),
            FadeOut(example_2),
            FadeOut(explain_2),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾总结 (9秒)"""
        # 总结标题
        summary_title = Text(
            "记住这些!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点1
        point_1 = Text(
            "整除 = 商为整数 + 余数为0",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(point_1, shift=UP * 0.3), run_time=0.6)
        self.wait(0.2)
        
        # 要点2
        point_2_text = Text(
            "因数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FACTOR
        )
        
        point_2_symbol = MathTex(
            r"\leq",
            font_size=self.FONT_BODY
        )
        
        point_2_text2 = Text(
            "倍数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_MULTIPLE
        )
        
        point_2 = VGroup(point_2_text, point_2_symbol, point_2_text2).arrange(
            RIGHT, buff=0.3
        ).move_to(UP * 2)
        
        self.play(FadeIn(point_2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.2)
        
        # 要点3
        point_3_math = MathTex(
            r"b \mid a",
            font_size=self.FONT_BODY
        )
        
        point_3_text = Text(
            "表示 b 整除 a",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        point_3 = VGroup(point_3_math, point_3_text).arrange(
            RIGHT, buff=0.4
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(point_3, shift=UP * 0.3), run_time=0.6)
        self.wait(0.4)
        
        # 要点闪烁
        self.play(
            Flash(point_1, color=YELLOW, flash_radius=0.4),
            run_time=0.4
        )
        self.play(
            Flash(point_2, color=YELLOW, flash_radius=0.4),
            run_time=0.4
        )
        self.play(
            Flash(point_3, color=YELLOW, flash_radius=0.4),
            run_time=0.4
        )
        self.wait(0.3)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeOut(summary_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_B
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰数字和符号
        decorations = VGroup(
            MathTex(r"3", font_size=30, color=self.COLOR_FACTOR),
            MathTex(r"\div", font_size=30, color=WHITE),
            MathTex(r"12", font_size=30, color=self.COLOR_MULTIPLE),
            MathTex(r"\mid", font_size=30, color=self.COLOR_HIGHLIGHT),
            MathTex(r"4", font_size=30, color=self.COLOR_DIVISIBLE)
        ).arrange(RIGHT, buff=0.6).move_to(DOWN * 5.5)
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# 测试场景 - 用于快速测试单个场景
class TestDivisibility(Scene):
    """测试单个场景"""
    
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        
        # 这里可以复制粘贴单个场景的代码进行测试
        pass