"""
百分比的意义教学动画 - The Meaning of Percentage
使用 Manim 创建的六年级数学教学视频

内容: 百分比的定义、视觉化理解、与分数小数的互化、常用百分比
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


class PercentageMeaning(Scene):
    """
    百分比的意义教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 百分比定义
    3. 视觉化理解 - 100格子
    4. 圆形图示
    5. 三者关系(核心)
    6. 常用百分比
    7. 应用场景与结尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PERCENT = "#e74c3c"       # 红色 - 百分比
        self.COLOR_FRACTION = "#3498db"      # 蓝色 - 分数
        self.COLOR_DECIMAL = "#2ecc71"       # 绿色 - 小数
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_FILLED = "#f39c12"        # 橙色 - 填充
        self.COLOR_EMPTY = "#34495e"         # 深灰 - 空白
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_PERCENT_LARGE = 60
        self.FONT_PERCENT_NORMAL = 36
        self.FONT_SMALL = 20
        self.FONT_AUTHOR = 20
        
        # 执行动画序列
        self.show_opening()
        self.show_percentage_definition()
        self.show_grid_visualization()
        self.show_circle_diagram()
        self.show_three_relationships()
        self.show_common_percentages()
        self.show_applications_and_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "考试成绩85%\n是什么意思?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 百分号85%放大显示
        percent_symbol = VGroup(
            Text("85", font_size=self.FONT_PERCENT_LARGE, color=self.COLOR_PERCENT, weight=BOLD),
            Text("%", font_size=self.FONT_PERCENT_LARGE, color=self.COLOR_PERCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 2.5)
        
        self.play(Write(percent_symbol), run_time=1.0)
        
        # 闪烁强调
        self.play(
            Flash(percent_symbol, color=self.COLOR_PERCENT, flash_radius=0.8),
            percent_symbol.animate.scale(1.1),
            run_time=0.5
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(percent_symbol),
            run_time=0.5
        )
    
    def show_percentage_definition(self):
        """场景2: 百分比定义"""
        # 标题
        title = Text(
            "什么是百分比?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义框
        definition_box = RoundedRectangle(
            width=7.5,
            height=2.5,
            corner_radius=0.2,
            color=self.COLOR_PERCENT,
            fill_opacity=0.1,
            stroke_width=3
        ).move_to(UP * 4)
        
        definition_text = VGroup(
            Text(
                "百分比(百分数)",
                font="Noto Sans CJK SC",
                font_size=self.FONT_SUBTITLE,
                color=WHITE,
                weight=BOLD
            ),
            Text(
                "表示一个数是另一个数的百分之几",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=self.COLOR_AUXILIARY
            )
        ).arrange(DOWN, buff=0.3).move_to(definition_box.get_center())
        
        self.play(
            FadeIn(definition_box, scale=0.9),
            run_time=0.6
        )
        self.play(Write(definition_text), run_time=1.4)
        
        # %符号的含义
        percent_explain = Text(
            "%的含义:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(percent_explain), run_time=0.5)
        
        # %符号分解
        percent_parts = VGroup(
            Text("%", font_size=50, color=self.COLOR_PERCENT),
            Text("=", font_size=30, color=WHITE),
            MathTex(r"\frac{}{100}", font_size=40, color=self.COLOR_PERCENT)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.8)
        
        self.play(Create(percent_parts), run_time=1.5)
        
        # 标注后项固定为100
        hundred_note = Text(
            "后项固定为100",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(percent_parts[2], DOWN, buff=0.5)
        
        arrow = Arrow(
            hundred_note.get_top(),
            percent_parts[2].get_bottom(),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=3
        )
        
        self.play(
            GrowArrow(arrow),
            FadeIn(hundred_note),
            Indicate(percent_parts[2]),
            run_time=1.5
        )
        
        # 示例25%
        example = VGroup(
            Text("例如:", font="Noto Sans CJK SC", font_size=self.FONT_BODY, color=GRAY_A),
            VGroup(
                Text("25", font_size=self.FONT_PERCENT_NORMAL, color=self.COLOR_PERCENT),
                Text("%", font_size=self.FONT_PERCENT_NORMAL, color=self.COLOR_PERCENT)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 1)
        
        self.play(Write(example), run_time=0.6)
        
        # 说明25/100
        equals = Text("=", font_size=30, color=WHITE).next_to(example, RIGHT, buff=0.3)
        fraction = MathTex(r"\frac{25}{100}", font_size=40).next_to(equals, RIGHT, buff=0.3)
        fraction[0][0:2].set_color(self.COLOR_PERCENT)  # 25
        
        self.play(
            FadeIn(equals),
            Write(fraction),
            run_time=1.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_box),
            FadeOut(definition_text),
            FadeOut(percent_explain),
            FadeOut(percent_parts),
            FadeOut(hundred_note),
            FadeOut(arrow),
            FadeOut(example),
            FadeOut(equals),
            FadeOut(fraction),
            run_time=0.6
        )
    
    def show_grid_visualization(self):
        """场景3: 视觉化理解 - 100格子"""
        # 标题
        title = Text(
            "100格图示",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建10×10网格
        grid_size = 2.5
        square_size = grid_size / 10
        
        squares = VGroup()
        for i in range(10):
            for j in range(10):
                square = Square(
                    side_length=square_size,
                    stroke_width=1.5,
                    stroke_color=WHITE,
                    fill_color=self.COLOR_EMPTY,
                    fill_opacity=0.3
                )
                square.move_to(
                    np.array([
                        (j - 4.5) * square_size,
                        (4.5 - i) * square_size + 2.5,
                        0
                    ])
                )
                squares.add(square)
        
        self.play(Create(squares), run_time=1.0)
        
        # 标注总数100
        total_label = Text(
            "总共100格",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(total_label), run_time=0.5)
        
        # 填充前25格 (左上角)
        filled_squares = VGroup()
        count = 0
        for i in range(10):
            for j in range(10):
                if count < 25:
                    filled_squares.add(squares[i * 10 + j])
                    count += 1
        
        self.play(
            LaggedStart(
                *[sq.animate.set_fill(self.COLOR_FILLED, opacity=0.8) for sq in filled_squares],
                lag_ratio=0.08
            ),
            run_time=3.0
        )
        
        # 标注25格
        filled_label = Text(
            "填充了25格",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_FILLED
        ).move_to(DOWN * 1.5)
        
        self.play(
            FadeIn(filled_label),
            Indicate(filled_squares, scale_factor=1.05),
            run_time=1.0
        )
        
        # 等式出现
        equation = VGroup(
            MathTex(r"\frac{25}{100}", font_size=40),
            Text("=", font_size=30, color=WHITE),
            VGroup(
                Text("25", font_size=36, color=self.COLOR_PERCENT),
                Text("%", font_size=36, color=self.COLOR_PERCENT)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 3)
        
        equation[0][0][0:2].set_color(self.COLOR_FILLED)
        
        self.play(Write(equation), run_time=1.0)
        
        # 高亮
        self.play(
            equation[2].animate.scale(1.2).set_color(self.COLOR_HIGHLIGHT),
            Flash(equation[2], color=self.COLOR_HIGHLIGHT),
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(squares),
            FadeOut(total_label),
            FadeOut(filled_label),
            FadeOut(equation),
            run_time=0.6
        )
    
    def show_circle_diagram(self):
        """场景4: 圆形图示"""
        # 标题
        title = Text(
            "圆形百分比图",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 完整圆形
        circle_radius = 2
        circle = Circle(
            radius=circle_radius,
            stroke_width=3,
            stroke_color=WHITE,
            fill_opacity=0
        ).shift(UP * 2)
        
        self.play(Create(circle), run_time=1.0)
        
        # 25%扇形 (从12点位置开始,顺时针90度)
        sector_25 = Sector(
            radius=circle_radius,
            angle=-90 * DEGREES,          # 顺时针90度
            start_angle=90 * DEGREES,
            color=self.COLOR_FILLED,
            fill_opacity=0,
            stroke_width=3
        ).shift(UP * 2)
        
        self.play(Create(sector_25), run_time=1.5)
        
        # 填充25%扇形
        self.play(
            sector_25.animate.set_fill(opacity=0.7),
            run_time=1.0
        )
        
        # 标注25%
        label_25 = VGroup(
            Text("25", font_size=30, color=self.COLOR_PERCENT, weight=BOLD),
            Text("%", font_size=30, color=self.COLOR_PERCENT, weight=BOLD)
        ).arrange(RIGHT, buff=0.05).move_to(UP * 3 + LEFT * 0.8)
        
        self.play(Write(label_25), run_time=0.5)
        
        # 标注75%
        label_75 = VGroup(
            Text("75", font_size=30, color=self.COLOR_AUXILIARY, weight=BOLD),
            Text("%", font_size=30, color=self.COLOR_AUXILIARY, weight=BOLD)
        ).arrange(RIGHT, buff=0.05).move_to(UP * 1.5 + RIGHT * 0.8)
        
        self.play(Write(label_75), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "25%是整体的四分之一",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 轻微旋转展示
        circle_group = VGroup(circle, sector_25, label_25, label_75)
        self.play(
            Rotate(circle_group, angle=PI/6, run_time=1.5),
            Rotate(circle_group, angle=-PI/6, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(circle_group),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_three_relationships(self):
        """场景5: 三者关系(核心)"""
        # 标题
        title = Text(
            "百分比的三种形式",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 通用公式标题
        formula_title = Text(
            "通用公式:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(formula_title), run_time=0.5)
        
        # 百分比形式
        percent_form = VGroup(
            Text("a", font_size=36, color=self.COLOR_PERCENT),
            Text("%", font_size=36, color=self.COLOR_PERCENT)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.2)
        self.play(Write(percent_form))

        # 变换为分数（旧对象被替换，自动清理）
        fraction_form = MathTex(r"\frac{a}{100}", font_size=45).move_to(UP * 4.2)
        fraction_form[0][0].set_color(self.COLOR_FRACTION)
        self.play(ReplacementTransform(percent_form, fraction_form))

        # 变换为小数（再次替换）
        decimal_form = VGroup(
            Text("0.01", font_size=36, color=self.COLOR_DECIMAL),
            Text("a", font_size=36, color=self.COLOR_DECIMAL)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.2)
        self.play(ReplacementTransform(fraction_form, decimal_form))
        self.wait(0.5)
        
        # # 变换为小数
        # decimal_form = VGroup(
        #     Text("0.01", font_size=36, color=self.COLOR_DECIMAL),
        #     Text("a", font_size=36, color=self.COLOR_DECIMAL)
        # ).arrange(RIGHT, buff=0.1).move_to(UP * 4.2)
        
        # self.play(
        #     Transform(fraction_form, decimal_form),
        #     run_time=1.5
        # )
        self.wait(0.5)
        
        # 三者并列
        percent_final = VGroup(
            Text("a", font_size=30, color=self.COLOR_PERCENT),
            Text("%", font_size=30, color=self.COLOR_PERCENT)
        ).arrange(RIGHT, buff=0.08)
        
        fraction_final = MathTex(r"\frac{a}{100}", font_size=38)
        fraction_final[0][0].set_color(self.COLOR_FRACTION)
        
        decimal_final = VGroup(
            Text("0.01", font_size=30, color=self.COLOR_DECIMAL),
            Text("a", font_size=30, color=self.COLOR_DECIMAL)
        ).arrange(RIGHT, buff=0.08)
        
        equals_1 = Text("=", font_size=30, color=WHITE)
        equals_2 = Text("=", font_size=30, color=WHITE)
        
        all_forms = VGroup(percent_final, equals_1, fraction_final, equals_2, decimal_final).move_to(UP * 3.8)
        self.play(FadeOut(decimal_form), FadeIn(all_forms))
        
        # 框选强调
        box = SurroundingRectangle(
            all_forms,
            color=self.COLOR_HIGHLIGHT,
            buff=0.25,
            stroke_width=4,
            corner_radius=0.15
        )
        
        self.play(Create(box), run_time=0.8)
        self.wait(0.5)
        
        # 具体示例标题
        example_title = Text(
            "具体示例: 25%",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 1.8)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 示例 - 25%
        ex_percent = VGroup(
            Text("25", font_size=32, color=self.COLOR_PERCENT),
            Text("%", font_size=32, color=self.COLOR_PERCENT)
        ).arrange(RIGHT, buff=0.08).move_to(UP * 0.6)
        
        self.play(Write(ex_percent), run_time=0.5)
        
        # = 25/100
        ex_eq1 = Text("=", font_size=28, color=WHITE).next_to(ex_percent, RIGHT, buff=0.25)
        ex_frac = MathTex(r"\frac{25}{100}", font_size=38).next_to(ex_eq1, RIGHT, buff=0.25)
        ex_frac[0][0:2].set_color(self.COLOR_FRACTION)
        
        self.play(
            FadeIn(ex_eq1),
            Write(ex_frac),
            run_time=1.0
        )
        
        # 化简为1/4
        ex_eq2 = Text("=", font_size=28, color=WHITE).next_to(ex_frac, RIGHT, buff=0.25)
        ex_frac_simple = MathTex(r"\frac{1}{4}", font_size=38).next_to(ex_eq2, RIGHT, buff=0.25)
        ex_frac_simple[0][0].set_color(self.COLOR_FRACTION)
        
        self.play(
            FadeIn(ex_eq2),
            Transform(ex_frac.copy(), ex_frac_simple),
            run_time=1.5
        )
        self.add(ex_frac_simple)
        
        # = 0.25
        ex_eq3 = Text("=", font_size=28, color=WHITE).next_to(ex_frac_simple, RIGHT, buff=0.25)
        ex_decimal = Text("0.25", font_size=32, color=self.COLOR_DECIMAL).next_to(ex_eq3, RIGHT, buff=0.25)
        
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
            FadeOut(formula_title),
            FadeOut(all_forms),
            FadeOut(box),
            FadeOut(example_title),
            FadeOut(ex_percent),
            FadeOut(ex_eq1),
            FadeOut(ex_frac),
            FadeOut(ex_eq2),
            FadeOut(ex_frac_simple),
            FadeOut(ex_eq3),
            FadeOut(ex_decimal),
            run_time=0.6
        )
    
    def show_common_percentages(self):
        """场景6: 常用百分比"""
        # 标题
        title = Text(
            "常用百分比",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建表格数据
        data = [
            ("50%", "1/2", "0.5"),
            ("25%", "1/4", "0.25"),
            ("75%", "3/4", "0.75"),
            ("10%", "1/10", "0.1")
        ]
        
        rows = VGroup()
        y_start = 4.5
        y_step = 1.3
        
        # 表头
        header = VGroup(
            Text("百分比", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_PERCENT),
            Text("分数", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_FRACTION),
            Text("小数", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_DECIMAL)
        ).arrange(RIGHT, buff=1.2).move_to(UP * y_start)
        
        self.play(Create(header), run_time=1.0)
        
        # 数据行
        for i, (percent, fraction, decimal) in enumerate(data):
            row = VGroup(
                Text(percent, font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                MathTex(fraction, font_size=32, color=self.COLOR_FRACTION),
                Text(decimal, font_size=28, color=self.COLOR_DECIMAL, weight=BOLD)
            ).arrange(RIGHT, buff=1.0).move_to(UP * (y_start - (i + 1) * y_step))
            
            rows.add(row)
            self.play(FadeIn(row, shift=UP * 0.2), run_time=0.8)
            if i < len(data) - 1:
                self.wait(0.2)
        
        # 全部高亮
        table_group = VGroup(header, rows)
        self.play(
            Indicate(table_group, scale_factor=1.03),
            run_time=1.0
        )
        
        # 提示记忆
        hint = Text(
            "这些是最常用的百分比,建议记住!",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(table_group),
            FadeOut(hint),
            run_time=0.6
        )
    
    def show_applications_and_outro(self):
        """场景7: 应用场景与结尾"""
        # 标题
        title = Text(
            "百分比在生活中",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=1.0)
        
        # 应用场景1: 考试成绩
        scene_1 = VGroup(
            Text("📊", font_size=40),
            Text(
                "考试成绩",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("85", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text("%", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text(" - 优秀!", font="Noto Sans CJK SC", font_size=20, color=GREEN)
            ).arrange(RIGHT, buff=0.05)
        ).arrange(DOWN, buff=0.25).move_to(UP * 3.5)
        
        self.play(FadeIn(scene_1, shift=UP * 0.3), run_time=1.0)
        
        # 应用场景2: 打折优惠
        scene_2 = VGroup(
            Text("💰", font_size=40),
            Text(
                "打折优惠",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("20", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text("% off", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text(" - 打8折", font="Noto Sans CJK SC", font_size=20, color=YELLOW)
            ).arrange(RIGHT, buff=0.05)
        ).arrange(DOWN, buff=0.25).move_to(UP * 1)
        
        self.play(FadeIn(scene_2, shift=UP * 0.3), run_time=1.0)
        
        # 应用场景3: 增长率
        scene_3 = VGroup(
            Text("📈", font_size=40),
            Text(
                "增长率",
                font="Noto Sans CJK SC",
                font_size=self.FONT_BODY,
                color=WHITE
            ),
            VGroup(
                Text("+15", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text("%", font_size=28, color=self.COLOR_PERCENT, weight=BOLD),
                Text(" - 正增长", font="Noto Sans CJK SC", font_size=20, color=BLUE)
            ).arrange(RIGHT, buff=0.05)
        ).arrange(DOWN, buff=0.25).move_to(DOWN * 1.5)
        
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
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
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
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 关键词标签
        keywords = VGroup(
            Text("#百分比", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_PERCENT),
            Text("#百分数", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_FRACTION),
            Text("#数学", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_HIGHLIGHT)
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
# manim -pql percentage_meaning.py PercentageMeaning  # 快速预览
# manim -qh percentage_meaning.py PercentageMeaning   # 高质量渲染