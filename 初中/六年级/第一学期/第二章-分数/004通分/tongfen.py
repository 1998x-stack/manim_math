"""
通分 (Finding Common Denominators) - Manim教学动画
使用 Manim 创建的六年级数学教学视频

内容: 通分的概念、方法和应用
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

修复说明:
  AnnularSector 以坐标原点为弧心创建，
  .move_to() 移动的是包围盒中心（≠ 弧心），导致扇形与圆错位。
  修复方案：统一改为 .shift(center)，确保弧心精确对齐圆心。
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TongFenAnimation(Scene):
    """
    通分教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 问题可视化 - 饼图展示
    3. 引入通分概念
    4. 寻找最小公倍数
    5. 通分过程 - 1/3
    6. 通分过程 - 1/4
    7. 总结与加法
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要分数
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 第二个分数
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_COMMON = "#2ecc71"       # 绿色 - 公分母/结果
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线/说明
        self.COLOR_STEP = "#f39c12"         # 橙色 - 步骤标记
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_visual_problem()
        self.show_tongfen_concept()
        self.show_lcm_finding()
        self.show_convert_1_3()
        self.show_convert_1_4()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有位置参数"""
        # 饼图参数
        self.pie_radius = 1.2
        self.pie1_center = np.array([-2.5, 2, 0])
        self.pie2_center = np.array([2.5, 2, 0])
        
        # 位置参数
        self.formula_y = 5.5
        self.explanation_y = -4.5
        
        print("✓ 几何设置完成")

    # ------------------------------------------------------------------ #
    #  辅助方法：创建对齐圆心的扇形                                         #
    # ------------------------------------------------------------------ #
    def make_sector(self, center, radius, angle, start_angle, color, opacity=0.6):
        """
        创建一个以 center 为弧心的扇形。
        
        关键修复：AnnularSector 默认弧心在原点，必须用 .shift() 而非
        .move_to()，否则移动的是包围盒中心，造成扇形与圆错位。
        """
        sector = AnnularSector(
            inner_radius=0,
            outer_radius=radius,
            angle=angle,
            start_angle=start_angle,
            color=color,
            fill_opacity=opacity,
            stroke_width=0
        ).shift(center)          # ← 核心修复：shift 而非 move_to
        return sector

    def make_divisions(self, center, radius, n, color, stroke_width=2):
        """创建 n 等分分割线"""
        divisions = VGroup()
        for i in range(n):
            angle = i * 2 * PI / n
            line = Line(
                center,
                center + radius * np.array([np.cos(angle), np.sin(angle), 0]),
                color=color,
                stroke_width=stroke_width
            )
            divisions.add(line)
        return divisions

    # ------------------------------------------------------------------ #

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
            "这两个分数能直接相加吗？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 显示分数 1/3 + 1/4
        frac_1 = MathTex(
            r"\frac{1}{3}",
            font_size=60,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 2 + UP * 4)
        
        plus_sign = MathTex(
            r"+",
            font_size=60,
            color=WHITE
        ).move_to(UP * 4)
        
        frac_2 = MathTex(
            r"\frac{1}{4}",
            font_size=60,
            color=self.COLOR_SECONDARY
        ).move_to(RIGHT * 2 + UP * 4)
        
        self.play(FadeIn(frac_1, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(plus_sign), run_time=0.3)
        self.play(FadeIn(frac_2, shift=DOWN * 0.3), run_time=0.5)
        
        # 疑问标记
        question_mark = Text(
            "?",
            font="Noto Sans CJK SC",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.4)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.5
        )
        
        # 保存分数对象供后续使用
        self.frac_1_original = frac_1
        self.frac_2_original = frac_2
        self.plus_sign = plus_sign
    
    def show_visual_problem(self):
        """场景2: 问题可视化 - 饼图展示"""
        self.play(
            self.frac_1_original.animate.move_to(self.pie1_center + UP * 2),
            self.frac_2_original.animate.move_to(self.pie2_center + UP * 2),
            FadeOut(self.plus_sign),
            run_time=0.8
        )
        
        # ── 饼图1: 1/3 ──────────────────────────────────────────────── #
        pie1_full = Circle(
            radius=self.pie_radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.pie1_center)
        
        self.play(Create(pie1_full), run_time=0.6)
        
        pie1_divisions = self.make_divisions(
            self.pie1_center, self.pie_radius, 3, self.COLOR_PRIMARY
        )
        self.play(Create(pie1_divisions), run_time=0.5)
        
        # 修复：shift 保证弧心对齐圆心
        pie1_fill = self.make_sector(
            center=self.pie1_center,
            radius=self.pie_radius,
            angle=2 * PI / 3,        # 1/3 圆
            start_angle=PI / 2,
            color=self.COLOR_PRIMARY
        )
        self.play(FadeIn(pie1_fill), run_time=0.4)
        
        # ── 饼图2: 1/4 ──────────────────────────────────────────────── #
        pie2_full = Circle(
            radius=self.pie_radius,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(self.pie2_center)
        
        self.play(Create(pie2_full), run_time=0.6)
        
        pie2_divisions = self.make_divisions(
            self.pie2_center, self.pie_radius, 4, self.COLOR_SECONDARY
        )
        self.play(Create(pie2_divisions), run_time=0.5)
        
        # 修复：shift 保证弧心对齐圆心
        pie2_fill = self.make_sector(
            center=self.pie2_center,
            radius=self.pie_radius,
            angle=PI / 2,            # 1/4 圆
            start_angle=PI / 2,
            color=self.COLOR_SECONDARY
        )
        self.play(FadeIn(pie2_fill), run_time=0.4)
        
        # 说明
        explain_text = Text(
            "分母不同，不能直接相加！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(explain_text), run_time=0.4)
        
        # 保存饼图对象
        self.pie1_group = VGroup(pie1_full, pie1_divisions, pie1_fill)
        self.pie2_group = VGroup(pie2_full, pie2_divisions, pie2_fill)
    
    def show_tongfen_concept(self):
        """场景3: 引入通分概念"""
        title = Text(
            "通分",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_COMMON,
            weight=BOLD
        ).move_to(UP * 0.5)
        
        self.play(Write(title), run_time=0.8)
        
        definition_parts = Text(
            "把异分母分数化成同分母分数",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(definition_parts, shift=UP * 0.2), run_time=0.6)
        
        self.wait(0.3)
        same_denom_text = Text(
            "同分母",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(definition_parts.get_center() + RIGHT * 1.2)
        
        underline = Line(
            same_denom_text.get_left() + DOWN * 0.2,
            same_denom_text.get_right() + DOWN * 0.2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(FadeIn(underline), run_time=0.4)
        
        goal_text = Text(
            "找到公分母: 3和4的最小公倍数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_STEP
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(goal_text, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)
        
        self.play(
            FadeOut(title),
            FadeOut(definition_parts),
            FadeOut(underline),
            FadeOut(same_denom_text),
            run_time=0.5
        )
        
        self.goal_text = goal_text
    
    def show_lcm_finding(self):
        """场景4: 寻找最小公倍数"""
        label_3 = Text(
            "3的倍数:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 3 + UP * 0.5)
        
        self.play(Write(label_3), run_time=0.5)
        
        nums_3_list = [3, 6, 9, 12, 15, 18]
        nums_3 = VGroup()
        for i, num in enumerate(nums_3_list):
            num_text = Text(
                str(num),
                font="Noto Sans CJK SC",
                font_size=22,
                color=self.COLOR_PRIMARY if num != 12 else self.COLOR_HIGHLIGHT
            ).move_to(LEFT * 3 + RIGHT * (i * 0.8) + DOWN * 0.3)
            nums_3.add(num_text)
        
        self.play(
            LaggedStart(*[FadeIn(n, shift=DOWN * 0.2) for n in nums_3], lag_ratio=0.15),
            run_time=1.5
        )
        
        label_4 = Text(
            "4的倍数:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).move_to(LEFT * 3 + DOWN * 1.5)
        
        self.play(Write(label_4), run_time=0.5)
        
        nums_4_list = [4, 8, 12, 16, 20]
        nums_4 = VGroup()
        for i, num in enumerate(nums_4_list):
            num_text = Text(
                str(num),
                font="Noto Sans CJK SC",
                font_size=22,
                color=self.COLOR_SECONDARY if num != 12 else self.COLOR_HIGHLIGHT
            ).move_to(LEFT * 3 + RIGHT * (i * 0.8) + DOWN * 2.3)
            nums_4.add(num_text)
        
        self.play(
            LaggedStart(*[FadeIn(n, shift=DOWN * 0.2) for n in nums_4], lag_ratio=0.15),
            run_time=1.5
        )
        
        twelve_3 = nums_3[3]
        twelve_4 = nums_4[2]
        
        self.play(
            Flash(twelve_3, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            Flash(twelve_4, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        
        circle_3 = Circle(radius=0.3, color=self.COLOR_HIGHLIGHT, stroke_width=3).move_to(twelve_3)
        circle_4 = Circle(radius=0.3, color=self.COLOR_HIGHLIGHT, stroke_width=3).move_to(twelve_4)
        
        self.play(Create(circle_3), Create(circle_4), run_time=0.5)
        
        conclusion = Text(
            "最小公倍数 = 12",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_COMMON,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.6)
        self.wait(1.5)
        
        self.play(
            FadeOut(label_3), FadeOut(label_4),
            FadeOut(nums_3), FadeOut(nums_4),
            FadeOut(circle_3), FadeOut(circle_4),
            FadeOut(self.goal_text),
            run_time=0.6
        )
        
        self.lcm_conclusion = conclusion
    
    def show_convert_1_3(self):
        """场景5: 通分过程 - 1/3 → 4/12"""
        self.play(
            self.frac_1_original.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.2),
            run_time=0.3
        )
        self.play(
            self.frac_1_original.animate.set_color(self.COLOR_PRIMARY).scale(1/1.2),
            run_time=0.3
        )
        
        step_1_text = Text(
            "分子分母同乘 4",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_STEP
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(step_1_text, shift=UP * 0.2), run_time=0.5)
        
        multiply_formula = MathTex(
            r"\frac{1 \times 4}{3 \times 4}",
            font_size=50,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 0.5)
        
        self.play(Write(multiply_formula), run_time=1.0)
        
        # 饼图1 重新分割成12份
        pie1_12_divisions = self.make_divisions(
            self.pie1_center, self.pie_radius, 12, self.COLOR_COMMON
        )

        # 修复：shift 保证弧心对齐圆心
        pie1_12_fill = self.make_sector(
            center=self.pie1_center,
            radius=self.pie_radius,
            angle=4 * 2 * PI / 12,   # 4/12
            start_angle=PI / 2,
            color=self.COLOR_COMMON
        )
        
        self.play(
            FadeOut(self.pie1_group[1]),   # 旧分割线
            FadeOut(self.pie1_group[2]),   # 旧填充
            run_time=0.3
        )
        self.play(Create(pie1_12_divisions), run_time=1.2)
        self.play(FadeIn(pie1_12_fill), run_time=0.6)
        
        self.pie1_group = VGroup(self.pie1_group[0], pie1_12_divisions, pie1_12_fill)
        
        result_4_12 = MathTex(
            r"= \frac{4}{12}",
            font_size=50,
            color=self.COLOR_COMMON
        ).next_to(multiply_formula, RIGHT, buff=0.3)
        
        self.play(Write(result_4_12), run_time=0.8)
        
        equals_verification = Text(
            "分数的值不变！",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(equals_verification), run_time=0.3)
        self.wait(1.5)
        
        self.play(
            FadeOut(step_1_text),
            FadeOut(multiply_formula),
            FadeOut(equals_verification),
            run_time=0.5
        )
        
        self.result_4_12 = result_4_12
    
    def show_convert_1_4(self):
        """场景6: 通分过程 - 1/4 → 3/12"""
        self.play(
            self.frac_2_original.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.2),
            run_time=0.3
        )
        self.play(
            self.frac_2_original.animate.set_color(self.COLOR_SECONDARY).scale(1/1.2),
            run_time=0.3
        )
        
        step_2_text = Text(
            "分子分母同乘 3",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_STEP
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(step_2_text, shift=UP * 0.2), run_time=0.5)
        
        multiply_formula_2 = MathTex(
            r"\frac{1 \times 3}{4 \times 3}",
            font_size=50,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 0.5)
        
        self.play(Write(multiply_formula_2), run_time=1.0)
        
        # 饼图2 重新分割成12份
        pie2_12_divisions = self.make_divisions(
            self.pie2_center, self.pie_radius, 12, self.COLOR_COMMON
        )

        # 修复：shift 保证弧心对齐圆心
        pie2_12_fill = self.make_sector(
            center=self.pie2_center,
            radius=self.pie_radius,
            angle=3 * 2 * PI / 12,   # 3/12
            start_angle=PI / 2,
            color=self.COLOR_COMMON
        )
        
        self.play(
            FadeOut(self.pie2_group[1]),   # 旧分割线
            FadeOut(self.pie2_group[2]),   # 旧填充
            run_time=0.3
        )
        self.play(Create(pie2_12_divisions), run_time=1.2)
        self.play(FadeIn(pie2_12_fill), run_time=0.6)
        
        self.pie2_group = VGroup(self.pie2_group[0], pie2_12_divisions, pie2_12_fill)
        
        result_3_12 = MathTex(
            r"= \frac{3}{12}",
            font_size=50,
            color=self.COLOR_COMMON
        ).next_to(multiply_formula_2, RIGHT, buff=0.3)
        
        self.play(Write(result_3_12), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(step_2_text),
            FadeOut(multiply_formula_2),
            run_time=0.5
        )
        
        self.result_3_12 = result_3_12
    
    def show_summary(self):
        """场景7: 总结与加法"""
        self.play(
            self.pie1_group.animate.move_to(LEFT * 1.5 + DOWN * 1),
            self.pie2_group.animate.move_to(RIGHT * 1.5 + DOWN * 1),
            self.frac_1_original.animate.move_to(LEFT * 3 + UP * 5.5),
            self.frac_2_original.animate.move_to(RIGHT * 3 + UP * 5.5),
            FadeOut(self.result_4_12),
            FadeOut(self.result_3_12),
            FadeOut(self.lcm_conclusion),
            run_time=1.0
        )
        
        final_equation = MathTex(
            r"\frac{1}{3} + \frac{1}{4} = \frac{4}{12} + \frac{3}{12}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(final_equation), run_time=1.2)
        
        final_result = MathTex(
            r"= \frac{7}{12}",
            font_size=40,
            color=self.COLOR_COMMON
        ).next_to(final_equation, DOWN, buff=0.3)
        
        self.play(Write(final_result), run_time=0.8)
        
        # 合并饼图显示7/12 (创建在原点)
        combined_pie_circle = Circle(
            radius=self.pie_radius,
            color=self.COLOR_COMMON,
            stroke_width=3
        ).move_to(ORIGIN)
        
        combined_pie_divisions = self.make_divisions(
            ORIGIN, self.pie_radius, 12, self.COLOR_COMMON
        )

        # 修复：ORIGIN 处使用 shift(ORIGIN) = no-op，与 move_to 等价，但保持一致
        combined_pie_fill = self.make_sector(
            center=ORIGIN,
            radius=self.pie_radius,
            angle=7 * 2 * PI / 12,   # 7/12
            start_angle=PI / 2,
            color=self.COLOR_COMMON,
            opacity=0.7
        )
        
        self.play(
            FadeOut(self.pie1_group),
            FadeOut(self.pie2_group),
            run_time=0.3
        )
        
        self.play(
            Create(combined_pie_circle),
            Create(combined_pie_divisions),
            FadeIn(combined_pie_fill),
            run_time=1.0
        )
        
        summary_title = Text(
            "通分三步骤:",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        self.play(Write(summary_title), run_time=0.6)
        
        point_1 = Text(
            "① 找最小公倍数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.3 + LEFT * 0.5)
        
        point_2 = Text(
            "② 分子分母同乘",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.0 + LEFT * 0.5)
        
        point_3 = Text(
            "③ 分数值不变",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.7 + LEFT * 0.5)
        
        self.play(FadeIn(point_1, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(point_2, shift=LEFT * 0.3), run_time=0.5)
        self.play(FadeIn(point_3, shift=LEFT * 0.3), run_time=0.5)
        
        self.wait(2.0)
        
        self.play(
            FadeOut(VGroup(
                self.frac_1_original,
                self.frac_2_original,
                final_equation,
                final_result,
                combined_pie_circle,
                combined_pie_divisions,
                combined_pie_fill,
                summary_title,
                point_1,
                point_2,
                point_3
            )),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        fraction_icons = VGroup()
        fractions_display = [
            (r"\frac{1}{2}", self.COLOR_PRIMARY),
            (r"\frac{1}{3}", self.COLOR_SECONDARY),
            (r"\frac{1}{4}", self.COLOR_COMMON),
            (r"\frac{2}{3}", self.COLOR_STEP),
        ]
        
        for i, (frac, color) in enumerate(fractions_display):
            icon = MathTex(frac, font_size=40, color=color)
            angle = i * 2 * PI / 4
            icon.move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            )
            fraction_icons.add(icon)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in fraction_icons], run_time=0.6)
        self.play(Rotate(fraction_icons, angle=PI, run_time=1.5))
        self.wait(1.0)
        
        self.play(
            FadeOut(VGroup(self.author_info, author_id, follow_text, fraction_icons)),
            run_time=1.0
        )


# 运行命令:
# manim -pql tongfen.py TongFenAnimation  # 快速预览
# manim -qh tongfen.py TongFenAnimation   # 高质量渲染