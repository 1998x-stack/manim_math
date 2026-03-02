"""
待定系数法求一次函数解析式 - Finding Linear Function Formula Using Undetermined Coefficients
使用 Manim 创建的中学数学教学视频

内容: 通过两点求一次函数解析式 (待定系数法)
目标观众: 八年级学生
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


class LinearFunctionUndeterminedCoefficients(Scene):
    """
    待定系数法求一次函数解析式教学动画
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 建立坐标系并标注点
    3. 引入待定系数法
    4. 代入点A建立方程
    5. 代入点B建立方程
    6. 解方程组并绘制函数
    7. 总结和关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主函数线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 重点标注
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
        self.COLOR_POINT_A = "#2ecc71"      # 绿色 - 点A
        self.COLOR_POINT_B = "#9b59b6"      # 紫色 - 点B
        
        # 字体大小规范
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "small": 18,
            "author": 20,
            "formula": 28,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_setup_axes()
        self.scene_3_introduce_method()
        self.scene_4_substitute_point_a()
        self.scene_5_substitute_point_b()
        self.scene_6_solve_and_draw()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化所有几何数据和坐标"""
        # 已知点坐标（数学坐标）
        self.x_A = 1
        self.y_A = 3
        self.x_B = 3
        self.y_B = 7
        
        # 函数参数（k=2, b=1）
        self.k = 2
        self.b = 1
        
        # 坐标系配置
        self.x_range = [-1, 5, 1]
        self.y_range = [-1, 9, 1]
        
        # 坐标系缩放和位置
        self.axes_scale = 0.7
        self.axes_offset = UP * 1.0
        
        # 作者信息（全局保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["author"],
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7.5)
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息淡入
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 标题
        title = Text(
            "两点确定一条直线",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题文字
        question = Text(
            "知道两个点的坐标",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)
        
        # 创建两个神秘的点（初始位置）
        self.dot_A_initial = Dot(
            UP * 2 + LEFT * 1.5,
            color=self.COLOR_POINT_A,
            radius=0.12
        )
        self.dot_B_initial = Dot(
            UP * 2 + RIGHT * 1.5,
            color=self.COLOR_POINT_B,
            radius=0.12
        )
        
        # 点闪烁出现
        self.play(
            Flash(self.dot_A_initial, color=self.COLOR_POINT_A, flash_radius=0.3),
            FadeIn(self.dot_A_initial, scale=0.5),
            run_time=0.5
        )
        self.play(
            Flash(self.dot_B_initial, color=self.COLOR_POINT_B, flash_radius=0.3),
            FadeIn(self.dot_B_initial, scale=0.5),
            run_time=0.5
        )
        
        # 提示文字
        hint = Text(
            "能求出函数解析式吗?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(hint),
            run_time=0.5
        )
        
        # 点变半透明
        self.play(
            self.dot_A_initial.animate.set_opacity(0.3),
            self.dot_B_initial.animate.set_opacity(0.3),
            run_time=0.3
        )
    
    def scene_2_setup_axes(self):
        """场景2: 建立坐标系并标注点"""
        # 创建坐标系
        self.axes = Axes(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=6 * self.axes_scale,
            y_length=10 * self.axes_scale,
            axis_config={
                "include_numbers": True,
                "font_size": 16,
                "include_tip": True,
            }
        ).move_to(self.axes_offset)
        
        # 坐标轴标签
        x_label = Text("x", font_size=20).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = Text("y", font_size=20).next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
        
        self.play(Create(self.axes), run_time=1.2)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 计算点在坐标系中的实际位置
        point_A_pos = self.axes.c2p(self.x_A, self.y_A)
        point_B_pos = self.axes.c2p(self.x_B, self.y_B)
        
        # 移动点到正确位置并恢复不透明度
        self.play(
            self.dot_A_initial.animate.move_to(point_A_pos).set_opacity(1),
            run_time=0.8
        )
        
        # 点A标签
        label_A = VGroup(
            Text("A", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=self.COLOR_POINT_A),
            MathTex(r"(1, 3)", font_size=self.FONT_SIZES["label"], color=WHITE)
        ).arrange(RIGHT, buff=0.1).next_to(self.dot_A_initial, UL, buff=0.15)
        
        self.play(FadeIn(label_A), run_time=0.5)
        
        # 移动点B
        self.play(
            self.dot_B_initial.animate.move_to(point_B_pos).set_opacity(1),
            run_time=0.8
        )
        
        # 点B标签
        label_B = VGroup(
            Text("B", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=self.COLOR_POINT_B),
            MathTex(r"(3, 7)", font_size=self.FONT_SIZES["label"], color=WHITE)
        ).arrange(RIGHT, buff=0.1).next_to(self.dot_B_initial, UR, buff=0.15)
        
        self.play(FadeIn(label_B), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "已知两点坐标",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理说明
        self.play(FadeOut(explain), run_time=0.4)
        
        # 保存元素供后续使用
        self.dot_A = self.dot_A_initial
        self.dot_B = self.dot_B_initial
        self.label_A = label_A
        self.label_B = label_B
        self.x_label = x_label
        self.y_label = y_label
    
    def scene_3_introduce_method(self):
        """场景3: 引入待定系数法"""
        # 方法标题
        method_title = Text(
            "待定系数法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5)
        
        self.play(Write(method_title), run_time=0.8)
        
        # 核心公式 y = kx + b（使用分组便于高亮）
        formula_general = MathTex(
            r"y = {{ k }}x + {{ b }}",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(UP * 4.2)
        
        self.play(Write(formula_general), run_time=1.0)
        self.wait(0.5)
        
        # 高亮 k
        k_index = 1
        self.play(formula_general[k_index].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        k_explain = Text(
            "斜率(待定)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 3.2 + LEFT * 1.5)
        
        self.play(FadeIn(k_explain, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.8)
        
        # 恢复k颜色
        self.play(
            formula_general[k_index].animate.set_color(WHITE),
            FadeOut(k_explain),
            run_time=0.3
        )
        
        # 高亮 b
        b_index = 3
        self.play(formula_general[b_index].animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        
        b_explain = Text(
            "截距(待定)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 3.2 + RIGHT * 1.5)
        
        self.play(FadeIn(b_explain, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.8)
        
        # 恢复b颜色
        self.play(
            formula_general[b_index].animate.set_color(WHITE),
            FadeOut(b_explain),
            run_time=0.3
        )
        
        # 核心思想
        core_idea = Text(
            "代入已知点求出k和b",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(core_idea, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)
        
        # 清理，保留公式
        self.play(
            FadeOut(method_title),
            FadeOut(core_idea),
            run_time=0.5
        )
        
        # 公式移到顶部并缩小
        formula_general_small = MathTex(
            r"y = kx + b",
            font_size=22
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(formula_general, formula_general_small),
            run_time=0.5
        )
        
        self.formula_general = formula_general
    
    def scene_4_substitute_point_a(self):
        """场景4: 代入点A建立方程"""
        # 提示文字
        hint_step1 = Text(
            "代入点A(1, 3)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_POINT_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(hint_step1), run_time=0.5)
        
        # 点A放大脉冲
        self.play(
            self.dot_A.animate.scale(1.5),
            Flash(self.dot_A, color=self.COLOR_POINT_A, flash_radius=0.4),
            run_time=0.5
        )
        self.play(self.dot_A.animate.scale(1/1.5), run_time=0.3)
        
        # 代入公式
        substitute_A = MathTex(
            r"3 = k \cdot 1 + b",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(DOWN * 4.8)
        
        self.play(Write(substitute_A), run_time=1.0)
        self.wait(0.8)
        
        # 箭头
        arrow_1 = Arrow(
            substitute_A.get_bottom() + DOWN * 0.2,
            substitute_A.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_1), run_time=0.4)
        
        # 方程1
        equation_1 = MathTex(
            r"k + b = 3",
            font_size=self.FONT_SIZES["formula"],
            color=WHITE
        ).next_to(arrow_1, DOWN, buff=0.2)
        
        self.play(Write(equation_1), run_time=0.8)
        self.wait(0.8)
        
        # 移动到左侧
        equation_1_final = MathTex(
            r"k + b = 3",
            font_size=24
        ).move_to(LEFT * 1.5 + DOWN * 1.5)
        
        self.play(
            FadeOut(hint_step1),
            FadeOut(substitute_A),
            FadeOut(arrow_1),
            Transform(equation_1, equation_1_final),
            run_time=0.6
        )
        
        # 添加编号
        num_1 = Text("①", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(equation_1, LEFT, buff=0.2)
        self.play(FadeIn(num_1), run_time=0.3)
        
        self.wait(0.5)
        
        self.equation_1 = equation_1
        self.num_1 = num_1
    
    def scene_5_substitute_point_b(self):
        """场景5: 代入点B建立方程"""
        # 提示文字
        hint_step2 = Text(
            "代入点B(3, 7)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_POINT_B
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(hint_step2), run_time=0.5)
        
        # 点B放大脉冲
        self.play(
            self.dot_B.animate.scale(1.5),
            Flash(self.dot_B, color=self.COLOR_POINT_B, flash_radius=0.4),
            run_time=0.5
        )
        self.play(self.dot_B.animate.scale(1/1.5), run_time=0.3)
        
        # 代入公式
        substitute_B = MathTex(
            r"7 = k \cdot 3 + b",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(DOWN * 4.8)
        
        self.play(Write(substitute_B), run_time=1.0)
        self.wait(0.8)
        
        # 箭头
        arrow_2 = Arrow(
            substitute_B.get_bottom() + DOWN * 0.2,
            substitute_B.get_bottom() + DOWN * 0.6,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_2), run_time=0.4)
        
        # 方程2
        equation_2 = MathTex(
            r"3k + b = 7",
            font_size=self.FONT_SIZES["formula"],
            color=WHITE
        ).next_to(arrow_2, DOWN, buff=0.2)
        
        self.play(Write(equation_2), run_time=0.8)
        self.wait(0.8)
        
        # 移动到左侧（在方程1下方）
        equation_2_final = MathTex(
            r"3k + b = 7",
            font_size=24
        ).move_to(LEFT * 1.5 + DOWN * 2.3)
        
        self.play(
            FadeOut(hint_step2),
            FadeOut(substitute_B),
            FadeOut(arrow_2),
            Transform(equation_2, equation_2_final),
            run_time=0.6
        )
        
        # 添加编号
        num_2 = Text("②", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(equation_2, LEFT, buff=0.2)
        self.play(FadeIn(num_2), run_time=0.3)
        
        # 大括号
        brace = Brace(
            VGroup(self.equation_1, equation_2),
            LEFT,
            buff=0.5,
            color=self.COLOR_HIGHLIGHT
        )
        
        self.play(Create(brace), run_time=0.5)
        
        # "方程组"标注
        system_label = Text(
            "方程组",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_HIGHLIGHT
        ).next_to(brace, LEFT, buff=0.1)
        
        self.play(FadeIn(system_label), run_time=0.4)
        self.wait(1.0)
        
        self.equation_2 = equation_2
        self.num_2 = num_2
        self.brace = brace
        self.system_label = system_label
    
    def scene_6_solve_and_draw(self):
        """场景6: 解方程组并绘制函数"""
        # 提示：相减消元
        solve_hint = Text(
            "②-①消元",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(RIGHT * 2 + DOWN * 1.5)
        
        self.play(FadeIn(solve_hint, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 计算过程：3k + b - (k + b) = 7 - 3
        calc_subtract = MathTex(
            r"2k = 4",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(RIGHT * 2 + DOWN * 2.3)
        
        self.play(Write(calc_subtract), run_time=0.8)
        self.wait(0.6)
        
        # 结果 k = 2
        result_k = MathTex(
            r"k = 2",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(RIGHT * 2 + DOWN * 3.3)
        
        self.play(Write(result_k), run_time=0.6)
        self.play(result_k.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        self.wait(0.8)
        
        # 恢复颜色
        self.play(result_k.animate.set_color(WHITE), run_time=0.2)
        
        # 代入求b
        calc_b_text = Text(
            "代入①求b:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_AUXILIARY
        ).move_to(RIGHT * 2 + DOWN * 4.0)
        
        calc_b = MathTex(
            r"2 + b = 3",
            font_size=22
        ).next_to(calc_b_text, DOWN, buff=0.15)
        
        self.play(FadeIn(calc_b_text), run_time=0.4)
        self.play(Write(calc_b), run_time=0.6)
        
        # 结果 b = 1
        result_b = MathTex(
            r"b = 1",
            font_size=self.FONT_SIZES["formula"]
        ).move_to(RIGHT * 2 + DOWN * 5.2)
        
        self.play(Write(result_b), run_time=0.6)
        self.play(result_b.animate.set_color(self.COLOR_HIGHLIGHT), run_time=0.3)
        self.wait(0.8)
        
        # 恢复颜色
        self.play(result_b.animate.set_color(WHITE), run_time=0.2)
        
        # 清理方程组和计算步骤
        self.play(
            FadeOut(self.equation_1),
            FadeOut(self.equation_2),
            FadeOut(self.num_1),
            FadeOut(self.num_2),
            FadeOut(self.brace),
            FadeOut(self.system_label),
            FadeOut(solve_hint),
            FadeOut(calc_subtract),
            FadeOut(calc_b_text),
            FadeOut(calc_b),
            run_time=0.6
        )
        
        # 最终公式出现
        final_formula = MathTex(
            r"y = 2x + 1",
            font_size=self.FONT_SIZES["formula"] + 4,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 1.8)
        
        # 先显示 k=2, b=1 移动到公式位置
        k_b_group = VGroup(result_k, result_b).copy()
        
        self.play(
            k_b_group.animate.arrange(RIGHT, buff=0.5).move_to(DOWN * 1.8),
            run_time=0.6
        )
        
        self.play(
            FadeOut(k_b_group),
            FadeIn(final_formula, scale=1.2),
            run_time=0.8
        )
        
        # 清理原来的 k=2, b=1
        self.play(
            FadeOut(result_k),
            FadeOut(result_b),
            run_time=0.3
        )
        
        self.wait(0.5)
        
        # 绘制函数线
        function_line = self.axes.plot(
            lambda x: 2 * x + 1,
            x_range=[0, 4],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(function_line), run_time=1.8)
        
        # 验证：线过A和B
        self.play(
            Flash(self.dot_A, color=self.COLOR_POINT_A, flash_radius=0.4),
            Flash(self.dot_B, color=self.COLOR_POINT_B, flash_radius=0.4),
            run_time=0.8
        )
        
        # 添加"验证通过"提示
        check_text = Text(
            "✓ 直线经过A和B",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(check_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(FadeOut(check_text), run_time=0.4)
        
        self.final_formula = final_formula
        self.function_line = function_line
    
    def scene_7_summary(self):
        """场景7: 总结和关注"""
        # 清空坐标系和点
        self.play(
            FadeOut(self.axes),
            FadeOut(self.dot_A),
            FadeOut(self.dot_B),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            FadeOut(self.function_line),
            FadeOut(self.formula_general),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "待定系数法四步骤",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 创建步骤卡片
        steps = [
            ("① 设",  r"y = kx + b",  "math"),
            ("② 代入", "两点坐标",     "text"),
            ("③ 建立", "方程组",       "text"),
            ("④ 求解", None,           "mixed"),   # k 和 b
        ]

        step_cards = VGroup()
        for i, (num, content, mode) in enumerate(steps):   # ← 3-tuple unpack
            icon = Circle(
                radius=0.15,
                fill_color=self.COLOR_PRIMARY,
                fill_opacity=1,
                stroke_width=0
            )
            num_text = Text(num, font="Noto Sans CJK SC", font_size=20, color=WHITE)

            if mode == "math":
                content_text = MathTex(content, font_size=22)
            elif mode == "mixed":
                content_text = VGroup(
                    MathTex(r"k", font_size=22),
                    Text("和", font="Noto Sans CJK SC", font_size=22, color=WHITE),
                    MathTex(r"b", font_size=22),
                ).arrange(RIGHT, buff=0.15)
            else:
                content_text = Text(content, font="Noto Sans CJK SC", font_size=22, color=WHITE)

            card = VGroup(icon, num_text, content_text).arrange(RIGHT, buff=0.3)
            card.move_to(UP * (3.5 - i * 1.0))
            card.shift(LEFT * 10)
            step_cards.add(card)

        for i, card in enumerate(step_cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(step_cards) - 1:
                self.wait(0.2)
        
        self.wait(0.5)
        
        # 最终公式放大居中
        self.play(
            self.final_formula.animate.scale(1.4).move_to(DOWN * 1.5),
            run_time=0.8
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_hint = Text(
            "关注我，学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(follow_hint, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰：小圆圈围绕公式旋转
        circles = VGroup(*[
            Circle(
                radius=0.12,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6
            ).move_to(
                self.final_formula.get_center() + 1.8 * np.array([
                    np.cos(i * TAU / 5),
                    np.sin(i * TAU / 5),
                    0
                ])
            )
            for i in range(5)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in circles],
            run_time=0.6
        )
        
        self.play(Rotate(circles, angle=PI, run_time=1.5, rate_func=smooth))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(step_cards),
            FadeOut(self.final_formula),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_hint),
            FadeOut(circles),
            run_time=1.0
        )


# 运行命令:
# manim -pql linear_function_undetermined_coefficients.py LinearFunctionUndeterminedCoefficients  # 快速预览
# manim -qh linear_function_undetermined_coefficients.py LinearFunctionUndeterminedCoefficients   # 高质量（推荐）
# manim -qk linear_function_undetermined_coefficients.py LinearFunctionUndeterminedCoefficients   # 4K质量