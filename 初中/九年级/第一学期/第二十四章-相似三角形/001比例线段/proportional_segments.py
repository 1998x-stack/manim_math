"""
比例线段 - Manim 教学动画
九年级数学 | 相似三角形 | 比例线段

内容: 比例定义、内项外项、比例中项、比例性质
目标观众: 九年级学生
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


class ProportionalSegments(Scene):
    """
    比例线段教学场景
    
    场景顺序:
    1. 开场钩子
    2. 比例定义 - 四条线段成比例
    3. 内项与外项 - 基本性质
    4. 比例中项 - 特殊情况
    5. 比例性质 - 合比与等比
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"      # 红色
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色
        self.COLOR_AUXILIARY = GRAY_B         # 灰色
        self.COLOR_SEGMENT_A = "#e74c3c"      # 线段a - 红色
        self.COLOR_SEGMENT_B = "#3498db"      # 线段b - 蓝色
        self.COLOR_SEGMENT_C = "#2ecc71"      # 线段c - 绿色
        self.COLOR_SEGMENT_D = "#f39c12"      # 线段d - 橙色
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_LABEL = 24
        self.FONT_FORMULA = 28
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_proportion_definition()
        self.scene_3_inner_outer()
        self.scene_4_geometric_mean()
        self.scene_5_properties()
        self.scene_6_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据"""
        # ===== 场景2: 四条线段的长度 =====
        self.len_a = 2.0
        self.len_b = 3.0
        self.len_c = 4.0
        self.len_d = 6.0
        
        # 验证比例
        ratio_ab = self.len_a / self.len_b
        ratio_cd = self.len_c / self.len_d
        assert abs(ratio_ab - ratio_cd) < 1e-6, "比例不相等！"
        
        # 线段位置（竖直排列，左对齐）
        self.seg_a_start = np.array([-3.0, 2.5, 0])
        self.seg_a_end = self.seg_a_start + RIGHT * self.len_a
        
        self.seg_b_start = np.array([-3.0, 1.2, 0])
        self.seg_b_end = self.seg_b_start + RIGHT * self.len_b
        
        self.seg_c_start = np.array([-3.0, -0.3, 0])
        self.seg_c_end = self.seg_c_start + RIGHT * self.len_c
        
        self.seg_d_start = np.array([-3.0, -1.8, 0])
        self.seg_d_end = self.seg_d_start + RIGHT * self.len_d
        
        # ===== 场景3: 内外项积 =====
        self.product_outer = self.len_a * self.len_d  # 12
        self.product_inner = self.len_b * self.len_c  # 12
        assert abs(self.product_outer - self.product_inner) < 1e-6
        
        # ===== 场景4: 比例中项 =====
        self.len_a_mid = 2.0
        self.len_b_mid = 4.0
        self.len_c_mid = 8.0
        
        # 验证比例中项
        assert abs(self.len_b_mid ** 2 - self.len_a_mid * self.len_c_mid) < 1e-6
        
        print("✓ 几何数据初始化完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.2)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这四条线段有什么关系?",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text, run_time=0.8))
        
        # 四条不同长度的线段
        preview_y = UP * 2.5
        spacing = 1.3
        
        preview_lines = VGroup(
            Line(LEFT * 1, LEFT * 1 + RIGHT * 1.0, stroke_width=6, color=self.COLOR_SEGMENT_A),
            Line(LEFT * 1, LEFT * 1 + RIGHT * 1.5, stroke_width=6, color=self.COLOR_SEGMENT_B),
            Line(LEFT * 1, LEFT * 1 + RIGHT * 2.0, stroke_width=6, color=self.COLOR_SEGMENT_C),
            Line(LEFT * 1, LEFT * 1 + RIGHT * 3.0, stroke_width=6, color=self.COLOR_SEGMENT_D),
        ).arrange(DOWN, buff=spacing, aligned_edge=LEFT).move_to(preview_y)
        
        # 依次出现
        for line in preview_lines:
            self.play(Create(line), run_time=0.4)
        
        # 问号
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).next_to(preview_lines, RIGHT, buff=0.8)
        
        self.play(
            FadeIn(question_mark, scale=1.5),
            Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.6
        )
        
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(preview_lines),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def scene_2_proportion_definition(self):
        """场景2: 比例定义"""
        # 标题
        title = Text(
            "Proportional Segments",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6.2)
        
        subtitle = Text(
            "比例线段",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 创建四条线段
        seg_a = Line(
            self.seg_a_start, self.seg_a_end,
            stroke_width=6,
            color=self.COLOR_SEGMENT_A
        )
        label_a = Text("a", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_a.next_to(seg_a, LEFT, buff=0.3)
        
        seg_b = Line(
            self.seg_b_start, self.seg_b_end,
            stroke_width=6,
            color=self.COLOR_SEGMENT_B
        )
        label_b = Text("b", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_b.next_to(seg_b, LEFT, buff=0.3)
        
        seg_c = Line(
            self.seg_c_start, self.seg_c_end,
            stroke_width=6,
            color=self.COLOR_SEGMENT_C
        )
        label_c = Text("c", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_c.next_to(seg_c, LEFT, buff=0.3)
        
        seg_d = Line(
            self.seg_d_start, self.seg_d_end,
            stroke_width=6,
            color=self.COLOR_SEGMENT_D
        )
        label_d = Text("d", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_d.next_to(seg_d, LEFT, buff=0.3)
        
        # 依次创建
        segments = [(seg_a, label_a), (seg_b, label_b), (seg_c, label_c), (seg_d, label_d)]
        for seg, label in segments:
            self.play(
                Create(seg),
                FadeIn(label),
                run_time=0.5
            )
        
        # 标注长度
        length_labels = VGroup(
            Text("2", font="PingFang SC", font_size=20, color=GRAY_A).next_to(seg_a, RIGHT, buff=0.2),
            Text("3", font="PingFang SC", font_size=20, color=GRAY_A).next_to(seg_b, RIGHT, buff=0.2),
            Text("4", font="PingFang SC", font_size=20, color=GRAY_A).next_to(seg_c, RIGHT, buff=0.2),
            Text("6", font="PingFang SC", font_size=20, color=GRAY_A).next_to(seg_d, RIGHT, buff=0.2),
        )
        
        self.play(*[FadeIn(label) for label in length_labels], run_time=0.6)
        
        # 比例公式
        formula_y = DOWN * 4
        
        formula_1 = MathTex(
            r"\frac{a}{b} = \frac{2}{3}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(formula_y)
        formula_1[0][0].set_color(self.COLOR_SEGMENT_A)  # a
        formula_1[0][2].set_color(self.COLOR_SEGMENT_B)  # b
        
        self.play(Write(formula_1), run_time=0.8)
        self.wait(0.5)
        
        formula_2 = MathTex(
            r"\frac{c}{d} = \frac{4}{6} = \frac{2}{3}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(formula_y + DOWN * 0.8)
        formula_2[0][0].set_color(self.COLOR_SEGMENT_C)  # c
        formula_2[0][2].set_color(self.COLOR_SEGMENT_D)  # d
        
        self.play(Write(formula_2), run_time=0.8)
        self.wait(0.5)
        
        # 比例相等
        proportion_eq = MathTex(
            r"\frac{a}{b} = \frac{c}{d}",
            font_size=self.FONT_FORMULA + 2,
            color=self.COLOR_HIGHLIGHT
        ).move_to(formula_y + DOWN * 1.8)
        proportion_eq[0][0].set_color(self.COLOR_SEGMENT_A)
        proportion_eq[0][2].set_color(self.COLOR_SEGMENT_B)
        proportion_eq[0][4].set_color(self.COLOR_SEGMENT_C)
        proportion_eq[0][6].set_color(self.COLOR_SEGMENT_D)
        
        box = SurroundingRectangle(proportion_eq, color=self.COLOR_HIGHLIGHT, buff=0.15)
        
        self.play(
            Write(proportion_eq),
            Create(box),
            run_time=0.8
        )
        
        # 定义文字
        definition = Text(
            "这四条线段成比例",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(definition), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(seg_a),
            FadeOut(seg_b),
            FadeOut(seg_c),
            FadeOut(seg_d),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(label_d),
            FadeOut(length_labels),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(proportion_eq),
            FadeOut(box),
            FadeOut(definition),
            run_time=0.6
        )
    
    def scene_3_inner_outer(self):
        """场景3: 内项与外项"""
        # 标题
        title = Text(
            "Inner & Outer Terms",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6.2)
        
        subtitle = Text(
            "内项与外项",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 比例式（使用冒号表示）
        proportion = MathTex(
            r"a", r":", r"b", r"=", r"c", r":", r"d",
            font_size=self.FONT_FORMULA + 4,
            color=WHITE
        ).move_to(UP * 3.5)
        
        proportion[0].set_color(self.COLOR_SEGMENT_A)  # a
        proportion[2].set_color(self.COLOR_SEGMENT_B)  # b
        proportion[4].set_color(self.COLOR_SEGMENT_C)  # c
        proportion[6].set_color(self.COLOR_SEGMENT_D)  # d
        
        self.play(Write(proportion), run_time=0.8)
        self.wait(0.4)
        
        # 标注外项
        outer_label = Text(
            "外项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        outer_arc_1 = Arc(
            radius=0.5,
            start_angle=PI * 0.7,
            angle=PI * 0.6,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(proportion[0].get_center() + UP * 0.6)
        
        outer_arc_2 = Arc(
            radius=0.5,
            start_angle=PI * 0.7,
            angle=PI * 0.6,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(proportion[6].get_center() + UP * 0.6)
        
        self.play(
            proportion[0].animate.set_color(self.COLOR_HIGHLIGHT),
            proportion[6].animate.set_color(self.COLOR_HIGHLIGHT),
            Create(outer_arc_1),
            Create(outer_arc_2),
            Write(outer_label),
            run_time=0.8
        )
        self.wait(0.6)
        
        # 恢复颜色，标注内项
        self.play(
            proportion[0].animate.set_color(self.COLOR_SEGMENT_A),
            proportion[6].animate.set_color(self.COLOR_SEGMENT_D),
            FadeOut(outer_arc_1),
            FadeOut(outer_arc_2),
            FadeOut(outer_label),
            run_time=0.4
        )
        
        inner_label = Text(
            "内项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        inner_arc_1 = Arc(
            radius=0.5,
            start_angle=PI * 0.7,
            angle=PI * 0.6,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(proportion[2].get_center() + UP * 0.6)
        
        inner_arc_2 = Arc(
            radius=0.5,
            start_angle=PI * 0.7,
            angle=PI * 0.6,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(proportion[4].get_center() + UP * 0.6)
        
        self.play(
            proportion[2].animate.set_color(self.COLOR_HIGHLIGHT),
            proportion[4].animate.set_color(self.COLOR_HIGHLIGHT),
            Create(inner_arc_1),
            Create(inner_arc_2),
            Write(inner_label),
            run_time=0.8
        )
        self.wait(0.6)
        
        # 清理标注
        self.play(
            proportion[2].animate.set_color(self.COLOR_SEGMENT_B),
            proportion[4].animate.set_color(self.COLOR_SEGMENT_C),
            FadeOut(inner_arc_1),
            FadeOut(inner_arc_2),
            FadeOut(inner_label),
            run_time=0.4
        )
        
        # 基本性质
        property_text = Text(
            "基本性质",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 1.2)
        
        property_formula = MathTex(
            r"ad = bc",
            font_size=self.FONT_FORMULA + 2,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.3)
        
        self.play(
            Write(property_text),
            Write(property_formula),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 验证计算
        calc_left = MathTex(
            r"ad = 2 \times 6 = 12",
            font_size=self.FONT_FORMULA - 2,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        self.play(Write(calc_left), run_time=0.8)
        self.wait(0.4)
        
        calc_right = MathTex(
            r"bc = 3 \times 4 = 12",
            font_size=self.FONT_FORMULA - 2,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        self.play(Write(calc_right), run_time=0.8)
        self.wait(0.4)
        
        # 相等验证
        equal_sign = MathTex(
            r"12 = 12 \; \checkmark",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        box_verify = SurroundingRectangle(equal_sign, color=self.COLOR_HIGHLIGHT, buff=0.15)
        
        self.play(
            Write(equal_sign),
            Create(box_verify),
            run_time=0.6
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(proportion),
            FadeOut(property_text),
            FadeOut(property_formula),
            FadeOut(calc_left),
            FadeOut(calc_right),
            FadeOut(equal_sign),
            FadeOut(box_verify),
            run_time=0.6
        )
    
    def scene_4_geometric_mean(self):
        """场景4: 比例中项"""
        # 标题
        title = Text(
            "Geometric Mean",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6.2)
        
        subtitle = Text(
            "比例中项",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 三条线段
        scale_factor = 0.6
        y_pos = UP * 2.5
        spacing = 1.2
        
        seg_a_mid = Line(
            LEFT * 1.5,
            LEFT * 1.5 + RIGHT * (self.len_a_mid * scale_factor),
            stroke_width=6,
            color=self.COLOR_SEGMENT_A
        )
        label_a_mid = Text("a", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_a_mid.next_to(seg_a_mid, LEFT, buff=0.3)
        len_a_label = Text("2", font="PingFang SC", font_size=20, color=GRAY_A)
        len_a_label.next_to(seg_a_mid, RIGHT, buff=0.2)
        
        seg_b_mid = Line(
            LEFT * 1.5,
            LEFT * 1.5 + RIGHT * (self.len_b_mid * scale_factor),
            stroke_width=6,
            color=self.COLOR_SEGMENT_B
        )
        label_b_mid = Text("b", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_b_mid.next_to(seg_b_mid, LEFT, buff=0.3)
        len_b_label = Text("4", font="PingFang SC", font_size=20, color=GRAY_A)
        len_b_label.next_to(seg_b_mid, RIGHT, buff=0.2)
        
        seg_c_mid = Line(
            LEFT * 1.5,
            LEFT * 1.5 + RIGHT * (self.len_c_mid * scale_factor),
            stroke_width=6,
            color=self.COLOR_SEGMENT_C
        )
        label_c_mid = Text("c", font="PingFang SC", font_size=self.FONT_LABEL, color=WHITE)
        label_c_mid.next_to(seg_c_mid, LEFT, buff=0.3)
        len_c_label = Text("8", font="PingFang SC", font_size=20, color=GRAY_A)
        len_c_label.next_to(seg_c_mid, RIGHT, buff=0.2)
        
        segments_mid = VGroup(
            VGroup(seg_a_mid, label_a_mid, len_a_label),
            VGroup(seg_b_mid, label_b_mid, len_b_label),
            VGroup(seg_c_mid, label_c_mid, len_c_label)
        ).arrange(DOWN, buff=spacing, aligned_edge=LEFT).move_to(y_pos)
        
        for seg_group in segments_mid:
            self.play(
                Create(seg_group[0]),
                FadeIn(seg_group[1]),
                FadeIn(seg_group[2]),
                run_time=0.5
            )
        
        # 比例关系
        proportion_mid = MathTex(
            r"\frac{a}{b} = \frac{b}{c}",
            font_size=self.FONT_FORMULA,
            color=WHITE
        ).move_to(DOWN * 1.5)
        proportion_mid[0][0].set_color(self.COLOR_SEGMENT_A)
        proportion_mid[0][2].set_color(self.COLOR_SEGMENT_B)
        proportion_mid[0][4].set_color(self.COLOR_SEGMENT_B)
        proportion_mid[0][6].set_color(self.COLOR_SEGMENT_C)
        
        self.play(Write(proportion_mid), run_time=0.8)
        self.wait(0.5)
        
        # 特殊性质
        property_mid = MathTex(
            r"b^2 = ac",
            font_size=self.FONT_FORMULA + 2,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(Write(property_mid), run_time=0.8)
        self.wait(0.5)
        
        # b是比例中项
        mid_text = Text(
            "b 是 a 和 c 的比例中项",
            font="PingFang SC",
            font_size=self.FONT_BODY - 2,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(mid_text), run_time=0.6)
        self.wait(0.5)
        
        # 验证
        verify_left = MathTex(
            r"b^2 = 4^2 = 16",
            font_size=self.FONT_FORMULA - 2,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(Write(verify_left), run_time=0.7)
        self.wait(0.4)
        
        verify_right = MathTex(
            r"ac = 2 \times 8 = 16",
            font_size=self.FONT_FORMULA - 2,
            color=WHITE
        ).move_to(DOWN * 6)
        
        self.play(Write(verify_right), run_time=0.7)
        self.wait(0.4)
        
        # 相等
        equal_check = MathTex(
            r"16 = 16 \; \checkmark",
            font_size=self.FONT_FORMULA,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7.2)
        
        self.play(Write(equal_check), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(segments_mid),
            FadeOut(proportion_mid),
            FadeOut(property_mid),
            FadeOut(mid_text),
            FadeOut(verify_left),
            FadeOut(verify_right),
            FadeOut(equal_check),
            run_time=0.6
        )
    
    def scene_5_properties(self):
        """场景5: 比例性质"""
        # 标题
        title = Text(
            "Properties of Proportions",
            font="PingFang SC",
            font_size=self.FONT_TITLE - 2,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6.2)
        
        subtitle = Text(
            "比例的性质",
            font="PingFang SC",
            font_size=self.FONT_SUBTITLE,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 前提条件
        premise = MathTex(
            r"\text{If } \frac{a}{b} = \frac{c}{d}",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(UP * 4.3)
        
        self.play(Write(premise), run_time=0.6)
        
        # 性质1：合比性质
        property_1_title = Text(
            "1. Componendo",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 2.8 + LEFT * 2.5)
        
        property_1_cn = Text(
            "合比性质",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(property_1_title, RIGHT, buff=0.3)
        
        property_1_formula = MathTex(
            r"\frac{a+b}{b} = \frac{c+d}{d}",
            font_size=self.FONT_FORMULA - 2,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)
        
        card_1 = VGroup(property_1_title, property_1_cn, property_1_formula)
        card_1.shift(LEFT * 10)
        
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.8)
        
        # 性质2：等比性质
        property_2_title = Text(
            "2. Equal Ratios",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(DOWN * 0.2 + LEFT * 2.5)
        
        property_2_cn = Text(
            "等比性质",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(property_2_title, RIGHT, buff=0.3)
        
        property_2_formula = MathTex(
            r"\frac{a}{b} = \frac{c}{d} = \frac{a+c}{b+d}",
            font_size=self.FONT_FORMULA - 4,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.2)
        
        card_2 = VGroup(property_2_title, property_2_cn, property_2_formula)
        card_2.shift(LEFT * 10)
        
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.8)
        
        # 提示
        hint = Text(
            "前提条件很重要!",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(premise),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(hint),
            run_time=0.6
        )
    
    def scene_6_outro(self):
        """场景6: 总结与片尾"""
        # 标题
        title = Text(
            "核心要点",
            font="PingFang SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 卡片1：比例定义
        card1_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SEGMENT_A,
            fill_opacity=1,
            stroke_width=0
        )
        
        card1_title = Text(
            "比例定义",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card1_formula = MathTex(
            r"\frac{a}{b} = \frac{c}{d}",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card1 = VGroup(card1_icon, card1_title, card1_formula).arrange(RIGHT, buff=0.3)
        card1.move_to(UP * 3).shift(LEFT * 10)
        
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 卡片2：内外项积
        card2_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SEGMENT_B,
            fill_opacity=1,
            stroke_width=0
        )
        
        card2_title = Text(
            "基本性质",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card2_formula = MathTex(
            r"ad = bc",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card2 = VGroup(card2_icon, card2_title, card2_formula).arrange(RIGHT, buff=0.3)
        card2.move_to(UP * 1.5).shift(LEFT * 10)
        
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        
        # 卡片3：比例中项
        card3_icon = Circle(
            radius=0.15,
            fill_color=self.COLOR_SEGMENT_C,
            fill_opacity=1,
            stroke_width=0
        )
        
        card3_title = Text(
            "比例中项",
            font="PingFang SC",
            font_size=self.FONT_BODY,
            color=WHITE
        )
        
        card3_formula = MathTex(
            r"b^2 = ac",
            font_size=self.FONT_LABEL,
            color=GRAY_A
        )
        
        card3 = VGroup(card3_icon, card3_title, card3_formula).arrange(RIGHT, buff=0.3)
        card3.move_to(ORIGIN).shift(LEFT * 10)
        
        self.play(card3.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=34,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 3.5)
        
        self.play(
            Transform(self.author_info, author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多相似三角形!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰线段
        deco_segs = VGroup(*[
            Line(
                ORIGIN,
                RIGHT * 0.5,
                stroke_width=4,
                color=color
            ).rotate(i * PI / 6).move_to(
                follow_text.get_center() + 
                1.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i, color in enumerate([
                self.COLOR_SEGMENT_A,
                self.COLOR_SEGMENT_B,
                self.COLOR_SEGMENT_C,
                self.COLOR_SEGMENT_D,
                self.COLOR_HIGHLIGHT,
                self.COLOR_PRIMARY
            ])
        ])
        
        self.play(
            *[FadeIn(seg, scale=0.5) for seg in deco_segs],
            run_time=0.6
        )
        
        self.play(Rotate(deco_segs, angle=PI / 2), run_time=1.0)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(card3),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_segs),
            run_time=1.0
        )


# 运行命令示例:
# manim -pql proportional_segments.py ProportionalSegments  # 快速预览
# manim -qh proportional_segments.py ProportionalSegments   # 高质量 1080p