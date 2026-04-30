"""
逆命题与逆定理教学动画 - Inverse Propositions and Inverse Theorems
使用 Manim 创建的八年级几何教学视频

内容: 逆命题的定义、与原命题的关系、逆定理的概念
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


class InversePropositions(Scene):
    """
    逆命题与逆定理教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义原命题与逆命题
    3. 具体示例 - 等腰三角形
    4. 关键关系 - 原命题真 ≠> 逆命题真
    5. 反例展示
    6. 逆定理的定义
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 原命题
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 逆命题
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调
        self.COLOR_TRUE = "#2ecc71"         # 绿色 - 真命题
        self.COLOR_FALSE = "#e67e22"        # 橙色 - 假命题
        self.COLOR_AUXILIARY = GRAY_B       # 辅助
        self.COLOR_ARROW = "#9b59b6"        # 紫色 - 箭头
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_example_isosceles()
        self.show_key_relationship()
        self.show_counter_example()
        self.show_inverse_theorem()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部，安全边界内)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "如果命题是真的\n反过来说还是真的吗?",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 问号动画
        question_marks = VGroup(
            Text("?", font="PingFang SC", font_size=80, color=self.COLOR_HIGHLIGHT).shift(LEFT * 1.5 + UP * 2),
            Text("?", font="PingFang SC", font_size=80, color=self.COLOR_HIGHLIGHT).shift(RIGHT * 1.5 + UP * 2)
        )
        
        self.play(FadeIn(question_marks, scale=1.5), run_time=0.5)
        self.play(
            Flash(question_marks[0], color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            Flash(question_marks[1], color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.4
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_marks),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 定义原命题与逆命题"""
        # 标题
        title = Text(
            "逆命题的定义",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 原命题框
        box_width = 6.0
        box_height = 1.5
        
        prop_box = Rectangle(
            width=box_width,
            height=box_height,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 2)
        
        prop_text = VGroup(
            Text("原命题:", font="PingFang SC", font_size=24, color=WHITE),
            VGroup(
                Text("若", font="PingFang SC", font_size=32, color=WHITE),
                MathTex(r"p", font_size=32, color=WHITE),
                Text("则", font="PingFang SC", font_size=32, color=WHITE),
                MathTex(r"q", font_size=32, color=WHITE),
            ).arrange(RIGHT, buff=0.2)
        ).arrange(RIGHT, buff=0.3).move_to(prop_box.get_center())
        
        self.play(Create(prop_box), run_time=0.5)
        self.play(Write(prop_text), run_time=0.8)
        
        # 双向箭头
        arrow_start = prop_box.get_bottom() + DOWN * 0.3
        arrow_end = DOWN * 2 + UP * (box_height/2 + 0.3)
        
        swap_arrow = DoubleArrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_ARROW,
            buff=0,
            stroke_width=4,
            tip_length=0.25
        )
        
        swap_label = Text(
            "互换条件和结论",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ARROW
        ).next_to(swap_arrow, RIGHT, buff=0.2)
        
        self.play(GrowArrow(swap_arrow), run_time=0.5)
        self.play(FadeIn(swap_label, shift=LEFT * 0.2), run_time=0.5)
        
        # 逆命题框
        inverse_box = Rectangle(
            width=box_width,
            height=box_height,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        ).move_to(DOWN * 2)
        
        inverse_text = VGroup(
            Text("逆命题:", font="PingFang SC", font_size=24, color=WHITE),
            VGroup(
                Text("若", font="PingFang SC", font_size=32, color=WHITE),
                MathTex(r"q", font_size=32, color=WHITE),
                Text("则", font="PingFang SC", font_size=32, color=WHITE),
                MathTex(r"p", font_size=32, color=WHITE),
            ).arrange(RIGHT, buff=0.2)
        ).arrange(RIGHT, buff=0.3).move_to(inverse_box.get_center())
        
        self.play(Create(inverse_box), run_time=0.5)
        self.play(Write(inverse_text), run_time=0.8)
        
        # 底部说明
        definition_text = Text(
            "把命题的条件和结论互换，得到逆命题",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(definition_text, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(prop_box),
            FadeOut(prop_text),
            FadeOut(inverse_box),
            FadeOut(inverse_text),
            FadeOut(swap_arrow),
            FadeOut(swap_label),
            FadeOut(definition_text),
            run_time=0.6
        )
    
    def show_example_isosceles(self):
        """场景3: 具体示例 - 等腰三角形"""
        # 示例标题
        example_title = Text(
            "具体例子: 等腰三角形",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # ========== 左侧: 原命题 ==========
        prop_statement = Text(
            "原命题: 若AB=AC, 则∠B=∠C",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5 + LEFT * 2.5)
        
        self.play(FadeIn(prop_statement), run_time=0.5)
        
        # 等腰三角形 (左侧) - 精确计算确保AB = AC
        scale = 0.6
        base_width = 2.0 * scale  # 底边半宽
        height = 2.5 * scale      # 高度
        
        # 计算等腰三角形顶点
        A_left = np.array([0, height, 0]) + LEFT * 2.5 + UP * 1
        B_left = np.array([-base_width, 0, 0]) + LEFT * 2.5 + UP * 1
        C_left = np.array([base_width, 0, 0]) + LEFT * 2.5 + UP * 1
        
        # 验证等腰: |AB| = |AC|
        AB_dist = np.linalg.norm(B_left - A_left)
        AC_dist = np.linalg.norm(C_left - A_left)
        assert abs(AB_dist - AC_dist) < 1e-6, f"等腰三角形不相等: AB={AB_dist}, AC={AC_dist}"
        
        triangle_left = Polygon(A_left, B_left, C_left, color=self.COLOR_PRIMARY, stroke_width=3)
        
        # 顶点标签
        label_A_left = Text("A", font="PingFang SC", font_size=18, color=WHITE).next_to(A_left, UP, buff=0.1)
        label_B_left = Text("B", font="PingFang SC", font_size=18, color=WHITE).next_to(B_left, DL, buff=0.1)
        label_C_left = Text("C", font="PingFang SC", font_size=18, color=WHITE).next_to(C_left, DR, buff=0.1)
        
        self.play(Create(triangle_left), run_time=0.5)
        self.play(FadeIn(label_A_left), FadeIn(label_B_left), FadeIn(label_C_left), run_time=0.3)
        
        # 标注相等边
        side_AB = Line(A_left, B_left, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        side_AC = Line(A_left, C_left, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        equal_mark_1 = Text("=", font="PingFang SC", font_size=16, color=YELLOW).move_to((A_left + B_left) / 2 + LEFT * 0.2)
        equal_mark_2 = Text("=", font="PingFang SC", font_size=16, color=YELLOW).move_to((A_left + C_left) / 2 + RIGHT * 0.2)
        
        self.play(
            Create(side_AB),
            Create(side_AC),
            FadeIn(equal_mark_1),
            FadeIn(equal_mark_2),
            run_time=0.5
        )
        self.play(
            side_AB.animate.set_color(self.COLOR_PRIMARY),
            side_AC.animate.set_color(self.COLOR_PRIMARY),
            run_time=0.3
        )
        
        # 标注相等角
        angle_B_arc = Arc(
            radius=0.3,
            start_angle=np.arctan2((A_left[1] - B_left[1]), (A_left[0] - B_left[0])),
            angle=np.arctan2((C_left[1] - B_left[1]), (C_left[0] - B_left[0])) - np.arctan2((A_left[1] - B_left[1]), (A_left[0] - B_left[0])),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_arc_center_to(B_left)
        
        angle_C_arc = Arc(
            radius=0.3,
            start_angle=np.arctan2((A_left[1] - C_left[1]), (A_left[0] - C_left[0])),
            angle=np.arctan2((B_left[1] - C_left[1]), (B_left[0] - C_left[0])) - np.arctan2((A_left[1] - C_left[1]), (A_left[0] - C_left[0])),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_arc_center_to(C_left)
        
        self.play(Create(angle_B_arc), Create(angle_C_arc), run_time=0.5)
        
        # ✓标记
        check_left = Text("✓", font="PingFang SC", font_size=48, color=self.COLOR_TRUE).move_to(LEFT * 2.5 + DOWN * 2)
        self.play(Flash(check_left, color=self.COLOR_TRUE, flash_radius=0.5), FadeIn(check_left, scale=1.5), run_time=0.4)
        
        self.wait(0.5)
        
        # ========== 右侧: 逆命题 ==========
        inverse_statement = Text(
            "逆命题: 若∠B=∠C, 则AB=AC",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5 + RIGHT * 2.5)
        
        self.play(FadeIn(inverse_statement), run_time=0.5)
        
        # 等腰三角形 (右侧) - 使用相同的精确计算
        A_right = np.array([0, height, 0]) + RIGHT * 2.5 + UP * 1
        B_right = np.array([-base_width, 0, 0]) + RIGHT * 2.5 + UP * 1
        C_right = np.array([base_width, 0, 0]) + RIGHT * 2.5 + UP * 1
        
        triangle_right = Polygon(A_right, B_right, C_right, color=self.COLOR_SECONDARY, stroke_width=3)
        
        # 顶点标签
        label_A_right = Text("A", font="PingFang SC", font_size=18, color=WHITE).next_to(A_right, UP, buff=0.1)
        label_B_right = Text("B", font="PingFang SC", font_size=18, color=WHITE).next_to(B_right, DL, buff=0.1)
        label_C_right = Text("C", font="PingFang SC", font_size=18, color=WHITE).next_to(C_right, DR, buff=0.1)
        
        self.play(Create(triangle_right), run_time=0.5)
        self.play(FadeIn(label_A_right), FadeIn(label_B_right), FadeIn(label_C_right), run_time=0.3)
        
        # 先标注相等角
        angle_B_arc_r = Arc(
            radius=0.3,
            start_angle=np.arctan2((A_right[1] - B_right[1]), (A_right[0] - B_right[0])),
            angle=np.arctan2((C_right[1] - B_right[1]), (C_right[0] - B_right[0])) - np.arctan2((A_right[1] - B_right[1]), (A_right[0] - B_right[0])),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_arc_center_to(B_right)
        
        angle_C_arc_r = Arc(
            radius=0.3,
            start_angle=np.arctan2((A_right[1] - C_right[1]), (A_right[0] - C_right[0])),
            angle=np.arctan2((B_right[1] - C_right[1]), (B_right[0] - C_right[0])) - np.arctan2((A_right[1] - C_right[1]), (A_right[0] - C_right[0])),
            color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_arc_center_to(C_right)
        
        self.play(Create(angle_B_arc_r), Create(angle_C_arc_r), run_time=0.5)
        
        # 再标注相等边
        side_AB_r = Line(A_right, B_right, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        side_AC_r = Line(A_right, C_right, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        equal_mark_1_r = Text("=", font="PingFang SC", font_size=16, color=YELLOW).move_to((A_right + B_right) / 2 + LEFT * 0.2)
        equal_mark_2_r = Text("=", font="PingFang SC", font_size=16, color=YELLOW).move_to((A_right + C_right) / 2 + RIGHT * 0.2)
        
        self.play(
            Create(side_AB_r),
            Create(side_AC_r),
            FadeIn(equal_mark_1_r),
            FadeIn(equal_mark_2_r),
            run_time=0.5
        )
        self.play(
            side_AB_r.animate.set_color(self.COLOR_SECONDARY),
            side_AC_r.animate.set_color(self.COLOR_SECONDARY),
            run_time=0.3
        )
        
        # ✓标记
        check_right = Text("✓", font="PingFang SC", font_size=48, color=self.COLOR_TRUE).move_to(RIGHT * 2.5 + DOWN * 2)
        self.play(Flash(check_right, color=self.COLOR_TRUE, flash_radius=0.5), FadeIn(check_right, scale=1.5), run_time=0.4)
        
        # 底部提示
        both_true = Text(
            "两个都是真命题!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_TRUE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(both_true, scale=1.1), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(example_title),
            FadeOut(prop_statement),
            FadeOut(inverse_statement),
            FadeOut(triangle_left),
            FadeOut(triangle_right),
            FadeOut(label_A_left),
            FadeOut(label_B_left),
            FadeOut(label_C_left),
            FadeOut(label_A_right),
            FadeOut(label_B_right),
            FadeOut(label_C_right),
            FadeOut(side_AB),
            FadeOut(side_AC),
            FadeOut(side_AB_r),
            FadeOut(side_AC_r),
            FadeOut(equal_mark_1),
            FadeOut(equal_mark_2),
            FadeOut(equal_mark_1_r),
            FadeOut(equal_mark_2_r),
            FadeOut(angle_B_arc),
            FadeOut(angle_C_arc),
            FadeOut(angle_B_arc_r),
            FadeOut(angle_C_arc_r),
            FadeOut(check_left),
            FadeOut(check_right),
            FadeOut(both_true),
            run_time=0.6
        )
    
    def show_key_relationship(self):
        """场景4: 关键关系 - 原命题真 ≠> 逆命题真"""
        # 大标题
        key_title = Text(
            "重要! 原命题与逆命题的关系",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(key_title), run_time=1.0)
        
        # "原命题真"
        prop_true = Text(
            "原命题真",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2 + LEFT * 2.5)
        
        self.play(FadeIn(prop_true, shift=RIGHT * 0.3), run_time=0.5)
        
        # 箭头
        arrow_center = UP * 2
        implies_arrow = Arrow(
            prop_true.get_right() + RIGHT * 0.2,
            arrow_center + RIGHT * 2.3,
            color=GRAY,
            buff=0,
            stroke_width=6,
            tip_length=0.3
        )
        
        self.play(GrowArrow(implies_arrow), run_time=0.5)
        
        # "逆命题真"
        inverse_true = Text(
            "逆命题真",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2 + RIGHT * 2.5)
        
        self.play(FadeIn(inverse_true, shift=LEFT * 0.3), run_time=0.5)
        
        # X符号划过箭头
        cross_line_1 = Line(
            implies_arrow.get_start() + UP * 0.3 + LEFT * 0.2,
            implies_arrow.get_end() + DOWN * 0.3 + RIGHT * 0.2,
            color=RED,
            stroke_width=8
        )
        
        cross_line_2 = Line(
            implies_arrow.get_start() + DOWN * 0.3 + LEFT * 0.2,
            implies_arrow.get_end() + UP * 0.3 + RIGHT * 0.2,
            color=RED,
            stroke_width=8
        )
        
        self.play(
            Create(cross_line_1),
            Create(cross_line_2),
            run_time=0.5
        )
        
        # "不一定"文字
        not_certain = Text(
            "不一定成立!",
            font="PingFang SC",
            font_size=36,
            color=RED
        ).move_to(arrow_center + DOWN * 0.8)
        
        self.play(
            Flash(not_certain, color=RED, flash_radius=0.8, num_lines=12),
            Write(not_certain),
            run_time=0.5
        )
        
        # 警告图标
        warning_icon = VGroup(
            Triangle(color=YELLOW, fill_opacity=0.3).scale(0.6),
            Text("!", font="PingFang SC", font_size=32, color=RED)
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(warning_icon, scale=1.5), run_time=0.4)
        self.play(Flash(warning_icon, color=YELLOW, flash_radius=0.6), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "原命题为真，逆命题可能真，也可能假",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(explanation, shift=UP * 0.3), run_time=0.5)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(key_title),
            FadeOut(prop_true),
            FadeOut(inverse_true),
            FadeOut(implies_arrow),
            FadeOut(cross_line_1),
            FadeOut(cross_line_2),
            FadeOut(not_certain),
            FadeOut(warning_icon),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_counter_example(self):
        """场景5: 反例展示"""
        # 反例标题
        counter_title = Text(
            "反例: 逆命题可能为假",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FALSE
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(counter_title), run_time=0.5)
        
        # ========== 左侧: 原命题 (真) ==========
        prop_text = Text(
            "原命题 (真)",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TRUE
        ).move_to(UP * 5 + LEFT * 2.5)
        
        prop_statement = Text(
            "若两直线平行\n则同位角相等",
            font="PingFang SC",
            font_size=18,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4 + LEFT * 2.5)
        
        self.play(Write(prop_text), run_time=0.5)
        self.play(FadeIn(prop_statement), run_time=0.5)
        
        # 绘制平行线和截线
        scale = 0.5
        offset_left = LEFT * 2.5 + UP * 0.5
        
        parallel_1 = Line(LEFT * 2 * scale, RIGHT * 2 * scale, color=self.COLOR_PRIMARY, stroke_width=3).shift(UP * 1.2 * scale + offset_left)
        parallel_2 = Line(LEFT * 2 * scale, RIGHT * 2 * scale, color=self.COLOR_PRIMARY, stroke_width=3).shift(DOWN * 0.8 * scale + offset_left)
        
        transversal = Line(
            LEFT * 1.5 * scale + UP * 1.5 * scale,
            RIGHT * 1.5 * scale + DOWN * 1.2 * scale,
            color=YELLOW,
            stroke_width=3
        ).shift(offset_left)
        
        self.play(Create(parallel_1), Create(parallel_2), run_time=0.5)
        self.play(Create(transversal), run_time=0.4)
        
        # 标注同位角
        angle_1_pos = LEFT * 0.5 * scale + UP * 1.2 * scale + offset_left
        angle_2_pos = RIGHT * 0.3 * scale + DOWN * 0.8 * scale + offset_left
        
        angle_arc_1 = Arc(radius=0.25, start_angle=-0.5, angle=1.0, color=self.COLOR_HIGHLIGHT, stroke_width=2).move_to(angle_1_pos)
        angle_arc_2 = Arc(radius=0.25, start_angle=-0.5, angle=1.0, color=self.COLOR_HIGHLIGHT, stroke_width=2).move_to(angle_2_pos)
        
        angle_label = Text("相等", font="PingFang SC", font_size=16, color=YELLOW).move_to(offset_left + DOWN * 2)
        
        self.play(Create(angle_arc_1), Create(angle_arc_2), run_time=0.4)
        self.play(FadeIn(angle_label), run_time=0.3)
        
        # ✓符号
        check_mark_left = Text("✓", font="PingFang SC", font_size=40, color=self.COLOR_TRUE).move_to(LEFT * 2.5 + DOWN * 3.5)
        self.play(FadeIn(check_mark_left, scale=1.3), run_time=0.3)
        
        self.wait(0.5)
        
        # ========== 右侧: 逆命题 (假) ==========
        inverse_text = Text(
            "逆命题 (假)",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_FALSE
        ).move_to(UP * 5 + RIGHT * 2.5)
        
        inverse_statement = Text(
            "若同位角相等\n则两直线平行",
            font="PingFang SC",
            font_size=18,
            color=WHITE,
            line_spacing=1.2
        ).move_to(UP * 4 + RIGHT * 2.5)
        
        self.play(Write(inverse_text), run_time=0.5)
        self.play(FadeIn(inverse_statement), run_time=0.5)
        
        # 绘制非平行线 (相交) 但同位角"看起来"相等
        offset_right = RIGHT * 2.5 + UP * 0.5
        
        # 两条相交线
        non_parallel_1 = Line(LEFT * 2 * scale, RIGHT * 2 * scale, color=self.COLOR_SECONDARY, stroke_width=3).shift(UP * 1.2 * scale + offset_right).rotate(-0.1, about_point=offset_right)
        non_parallel_2 = Line(LEFT * 2 * scale, RIGHT * 2 * scale, color=self.COLOR_SECONDARY, stroke_width=3).shift(DOWN * 0.8 * scale + offset_right).rotate(0.1, about_point=offset_right)
        
        transversal_2 = Line(
            LEFT * 1.5 * scale + UP * 1.5 * scale,
            RIGHT * 1.5 * scale + DOWN * 1.2 * scale,
            color=YELLOW,
            stroke_width=3
        ).shift(offset_right)
        
        self.play(Create(non_parallel_1), Create(non_parallel_2), run_time=0.5)
        self.play(Create(transversal_2), run_time=0.4)
        
        # 标注"相等"的同位角 (但实际不平行)
        angle_1_pos_r = LEFT * 0.5 * scale + UP * 1.2 * scale + offset_right
        angle_2_pos_r = RIGHT * 0.3 * scale + DOWN * 0.8 * scale + offset_right
        
        angle_arc_1_r = Arc(radius=0.25, start_angle=-0.5, angle=1.0, color=self.COLOR_HIGHLIGHT, stroke_width=2).move_to(angle_1_pos_r)
        angle_arc_2_r = Arc(radius=0.25, start_angle=-0.5, angle=1.0, color=self.COLOR_HIGHLIGHT, stroke_width=2).move_to(angle_2_pos_r)
        
        angle_label_r = Text("相等", font="PingFang SC", font_size=16, color=YELLOW).move_to(offset_right + DOWN * 2)
        
        self.play(Create(angle_arc_1_r), Create(angle_arc_2_r), run_time=0.4)
        self.play(FadeIn(angle_label_r), run_time=0.3)
        
        # ✗符号
        cross_mark_right = Text("✗", font="PingFang SC", font_size=40, color=RED).move_to(RIGHT * 2.5 + DOWN * 3.5)
        self.play(
            Flash(cross_mark_right, color=RED, flash_radius=0.6),
            FadeIn(cross_mark_right, scale=1.3),
            run_time=0.4
        )
        
        # 底部说明
        explanation = Text(
            "同位角相等时，直线可能相交\n(这只是特殊构造，实际很少见)",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(counter_title),
            FadeOut(prop_text),
            FadeOut(prop_statement),
            FadeOut(inverse_text),
            FadeOut(inverse_statement),
            FadeOut(parallel_1),
            FadeOut(parallel_2),
            FadeOut(transversal),
            FadeOut(non_parallel_1),
            FadeOut(non_parallel_2),
            FadeOut(transversal_2),
            FadeOut(angle_arc_1),
            FadeOut(angle_arc_2),
            FadeOut(angle_arc_1_r),
            FadeOut(angle_arc_2_r),
            FadeOut(angle_label),
            FadeOut(angle_label_r),
            FadeOut(check_mark_left),
            FadeOut(cross_mark_right),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_inverse_theorem(self):
        """场景6: 逆定理的定义"""
        # 标题
        title = Text(
            "什么是逆定理?",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义框
        definition_box = Rectangle(
            width=7.0,
            height=2.0,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        ).move_to(UP * 3.5)
        
        definition_text = Text(
            "如果一个定理的逆命题也是真命题\n则称它为逆定理",
            font="PingFang SC",
            font_size=24,
            color=WHITE,
            line_spacing=1.3
        ).move_to(definition_box.get_center())
        
        self.play(Create(definition_box), run_time=0.5)
        self.play(FadeIn(definition_text, shift=DOWN * 0.2), run_time=0.8)
        
        # 条件展示
        condition_1 = VGroup(
            Text("条件1:", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("原命题是真命题", font="PingFang SC", font_size=22, color=self.COLOR_PRIMARY),
            Text("✓", font="PingFang SC", font_size=28, color=self.COLOR_TRUE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)
        
        condition_2 = VGroup(
            Text("条件2:", font="PingFang SC", font_size=22, color=GRAY_A),
            Text("逆命题是真命题", font="PingFang SC", font_size=22, color=self.COLOR_SECONDARY),
            Text("✓", font="PingFang SC", font_size=28, color=self.COLOR_TRUE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.5)
        
        self.play(FadeIn(condition_1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(condition_2, shift=RIGHT * 0.3), run_time=0.5)
        
        # "逆定理"高亮
        theorem_word = Text(
            "逆定理",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        
        self.play(
            Flash(theorem_word, color=self.COLOR_HIGHLIGHT, flash_radius=0.8, num_lines=16),
            FadeIn(theorem_word, scale=1.2),
            run_time=0.5
        )
        
        # 示例标题
        example_title = Text(
            "经典例子:",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 2.2)
        
        self.play(FadeIn(example_title), run_time=0.5)
        
        # 示例1
        example_1 = VGroup(
            Text("•", font="PingFang SC", font_size=20, color=WHITE),
            Text("勾股定理", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY),
            Text("⟺", font="PingFang SC", font_size=24, color=self.COLOR_ARROW),
            Text("勾股定理的逆定理", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.2)
        
        self.play(FadeIn(example_1, shift=UP * 0.2), run_time=0.5)
        
        # 示例2
        example_2 = VGroup(
            Text("•", font="PingFang SC", font_size=20, color=WHITE),
            Text("等腰三角形性质", font="PingFang SC", font_size=20, color=self.COLOR_PRIMARY),
            Text("⟺", font="PingFang SC", font_size=24, color=self.COLOR_ARROW),
            Text("等腰三角形判定", font="PingFang SC", font_size=20, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.2)
        
        self.play(FadeIn(example_2, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_box),
            FadeOut(definition_text),
            FadeOut(condition_1),
            FadeOut(condition_2),
            FadeOut(theorem_word),
            FadeOut(example_title),
            FadeOut(example_1),
            FadeOut(example_2),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 总结与片尾"""
        # 总结标题
        summary_title = Text(
            "知识点总结",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点卡片
        point_1 = VGroup(
            Circle(radius=0.15, fill_color=self.COLOR_PRIMARY, fill_opacity=1, stroke_width=0),
            Text("逆命题 = 条件和结论互换", font="PingFang SC", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        point_2 = VGroup(
            Circle(radius=0.15, fill_color=self.COLOR_SECONDARY, fill_opacity=1, stroke_width=0),
            Text("原命题真 ≠> 逆命题真", font="PingFang SC", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)
        
        point_3 = VGroup(
            Circle(radius=0.15, fill_color=self.COLOR_HIGHLIGHT, fill_opacity=1, stroke_width=0),
            Text("逆命题也真 → 逆定理", font="PingFang SC", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1)
        
        # 要点依次滑入
        for point in [point_1, point_2, point_3]:
            point.shift(LEFT * 10)
        
        self.play(point_1.animate.shift(RIGHT * 10), run_time=0.4)
        self.wait(0.3)
        self.play(point_2.animate.shift(RIGHT * 10), run_time=0.4)
        self.wait(0.3)
        self.play(point_3.animate.shift(RIGHT * 10), run_time=0.4)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 2.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰圆圈
        decoration_circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_HIGHLIGHT, fill_opacity=0.5).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circle, scale=0.5) for circle in decoration_circles],
            run_time=0.6
        )
        self.play(Rotate(decoration_circles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_circles),
            run_time=1.0
        )


# 运行命令:
# manim -pql inverse_propositions.py InversePropositions  # 快速预览
# manim -qh inverse_propositions.py InversePropositions   # 高质量渲染