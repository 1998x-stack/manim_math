"""
绝对值 (Absolute Value) 教学动画
使用 Manim 创建的六年级数学教学视频

内容: 绝对值的定义、几何意义、性质和应用
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


class AbsoluteValueConcept(Scene):
    """
    绝对值教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 引入绝对值概念 - 几何意义
    3. 绝对值符号与计算 - 基本运算
    4. 数学规则展示 - 分段函数
    5. 对称性展示 - 对称性质
    6. 实际应用示例 - 生活应用
    7. 总结与片尾 - 回顾要点
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 强调
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_POSITIVE = "#2ecc71"       # 绿色 - 正数
        self.COLOR_NEGATIVE = "#e67e22"       # 橙色 - 负数
        self.COLOR_ZERO = "#95a5a6"           # 灰色 - 零
        self.COLOR_DISTANCE = "#9b59b6"       # 紫色 - 距离
        self.COLOR_AUXILIARY = GRAY_B         # 辅助线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduce_concept()
        self.scene_3_absolute_value_notation()
        self.scene_4_mathematical_rules()
        self.scene_5_symmetry()
        self.scene_6_real_world_applications()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化数轴和所有几何元素"""
        # 数轴配置
        self.x_range = [-5, 5, 1]  # 范围和步长
        self.unit_length = 0.8     # 每个整数间距
        self.numberline_center = UP * 2  # 垂直偏移
        
        # 创建数轴
        self.numberline = NumberLine(
            x_range=self.x_range,
            length=8,  # 总长度
            color=WHITE,
            include_numbers=True,
            numbers_to_include=range(-5, 6),
            font_size=24,
            tick_size=0.1,
            stroke_width=2
        ).move_to(self.numberline_center)
        
        # 关键点位置（精确计算）
        self.origin_point = self.numberline.n2p(0)
        self.point_A = self.numberline.n2p(3)
        self.point_B = self.numberline.n2p(-3)
        self.point_C = self.numberline.n2p(-4)
        self.point_D = self.numberline.n2p(1.5)
        
        # 距离计算
        self.dist_3 = np.linalg.norm(self.point_A - self.origin_point)
        self.dist_neg3 = np.linalg.norm(self.point_B - self.origin_point)
        self.dist_neg4 = np.linalg.norm(self.point_C - self.origin_point)
        
        # 验证几何
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证对称性：3和-3到原点距离相等
        if abs(self.dist_3 - self.dist_neg3) > epsilon:
            print(f"WARNING: 距离不相等! |3|={self.dist_3:.6f}, |-3|={self.dist_neg3:.6f}")
        
        # 验证单位长度一致性
        unit_check = np.linalg.norm(self.numberline.n2p(1) - self.origin_point)
        expected_unit = self.dist_3 / 3
        
        if abs(unit_check - expected_unit) > epsilon:
            print(f"WARNING: 单位长度不一致! 实际={unit_check:.6f}, 期望={expected_unit:.6f}")
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-4秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "3 和 -3，谁离原点更远？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=0.8)
        self.wait(0.9)
        
        # 数轴淡入
        self.play(Create(self.numberline), run_time=1.0)
        self.wait(0.9)
        
        # 清理
        self.play(FadeOut(hook_question), run_time=0.4)
    
    def scene_2_introduce_concept(self):
        """场景2: 引入绝对值概念 (4-10秒)"""
        # 标记原点
        origin_dot = Dot(self.origin_point, color=self.COLOR_SECONDARY, radius=0.12)
        origin_label = MathTex("0", font_size=32, color=WHITE).next_to(origin_dot, DOWN, buff=0.2)
        
        self.play(FadeIn(origin_dot, scale=0.5), run_time=0.4)
        self.play(Write(origin_label), run_time=0.3)
        
        # 点A(3) 和 点B(-3)
        dot_A = Dot(self.point_A, color=self.COLOR_POSITIVE, radius=0.1)
        dot_B = Dot(self.point_B, color=self.COLOR_NEGATIVE, radius=0.1)
        
        label_A = MathTex("3", font_size=28, color=self.COLOR_POSITIVE).next_to(dot_A, UP, buff=0.15)
        label_B = MathTex("-3", font_size=28, color=self.COLOR_NEGATIVE).next_to(dot_B, UP, buff=0.15)
        
        self.play(FadeIn(dot_A), FadeIn(label_A), run_time=0.4)
        self.play(FadeIn(dot_B), FadeIn(label_B), run_time=0.4)
        
        # 距离箭头（双向）
        arrow_A = DoubleArrow(
            start=self.origin_point,
            end=self.point_A,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.15
        ).shift(DOWN * 0.3)
        
        arrow_B = DoubleArrow(
            start=self.origin_point,
            end=self.point_B,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.15
        ).shift(DOWN * 0.3)
        
        self.play(Create(arrow_A), run_time=0.6)
        self.play(Create(arrow_B), run_time=0.6)
        
        # 距离标注（Brace）
        brace_A = Brace(Line(self.origin_point, self.point_A), direction=DOWN, buff=0.5)
        brace_label_A = Text("3", font="PingFang SC", font_size=24, color=WHITE).next_to(brace_A, DOWN, buff=0.1)
        
        brace_B = Brace(Line(self.point_B, self.origin_point), direction=DOWN, buff=0.5)
        brace_label_B = Text("3", font="PingFang SC", font_size=24, color=WHITE).next_to(brace_B, DOWN, buff=0.1)
        
        self.play(
            FadeIn(brace_A),
            FadeIn(brace_label_A),
            FadeIn(brace_B),
            FadeIn(brace_label_B),
            run_time=0.5
        )
        
        # 显示"距离相等！"
        equal_text = Text(
            "距离相等！",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(equal_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 定义文字
        definition = VGroup(
            Text("绝对值：", font="PingFang SC", font_size=32, color=WHITE),
            Text("一个数到原点的距离", font="PingFang SC", font_size=28, color=GRAY_A)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(DOWN * 4)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(equal_text),
            FadeOut(brace_A),
            FadeOut(brace_label_A),
            FadeOut(brace_B),
            FadeOut(brace_label_B),
            FadeOut(arrow_A),
            FadeOut(arrow_B),
            FadeOut(dot_A),
            FadeOut(dot_B),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(origin_dot),
            FadeOut(origin_label),
            FadeOut(definition),
            run_time=0.6
        )
    
    def scene_3_absolute_value_notation(self):
        """场景3: 绝对值符号与计算 (10-18秒)"""
        # 标题
        title = Text(
            "绝对值符号",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式组（垂直排列）
        formula_1 = MathTex(r"|3| = 3", font_size=40).move_to(UP * 3.5)
        formula_2 = MathTex(r"|-3| = 3", font_size=40).move_to(UP * 2)
        formula_3 = MathTex(r"|0| = 0", font_size=40).move_to(UP * 0.5)
        
        # 颜色标记
        formula_1.set_color_by_tex("3", self.COLOR_POSITIVE)
        formula_2.set_color_by_tex("-3", self.COLOR_NEGATIVE)
        formula_2.set_color_by_tex("= 3", self.COLOR_POSITIVE)
        formula_3.set_color_by_tex("0", self.COLOR_ZERO)
        
        # 动画：公式1
        self.play(Write(formula_1), run_time=0.5)
        self.wait(0.5)
        
        # 动画：公式2
        self.play(Write(formula_2), run_time=0.5)
        self.wait(0.5)
        
        # 动画：公式3
        self.play(Write(formula_3), run_time=0.5)
        self.wait(0.4)
        
        # 重点：非负性
        highlight = VGroup(
            Text("重点：", font="PingFang SC", font_size=32, color=self.COLOR_HIGHLIGHT),
            MathTex(r"|a| \geq 0", font_size=36, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        
        # 高亮非负性
        self.play(Indicate(highlight[1], scale_factor=1.2, color=YELLOW), run_time=0.7)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_1),
            FadeOut(formula_2),
            FadeOut(formula_3),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def scene_4_mathematical_rules(self):
        """场景4: 数学规则展示 (18-28秒)"""
        # 标题
        title = Text(
            "数学定义",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 分段函数
        piecewise_formula = MathTex(
            r"|a| = \begin{cases} a, & a \geq 0 \\ -a, & a < 0 \end{cases}",
            font_size=44
        ).move_to(UP * 5)
        
        # 颜色标记
        piecewise_formula[0][4].set_color(self.COLOR_POSITIVE)  # a (positive case)
        piecewise_formula[0][6:9].set_color(self.COLOR_POSITIVE)  # a >= 0
        piecewise_formula[0][9:11].set_color(self.COLOR_NEGATIVE)  # -a
        piecewise_formula[0][11:14].set_color(self.COLOR_NEGATIVE)  # a < 0
        
        self.play(Write(piecewise_formula), run_time=1.2)
        
        # 数轴正半轴高亮
        positive_region = Rectangle(
            width=4.0,
            height=0.4,
            fill_color=self.COLOR_POSITIVE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(self.numberline.n2p(2.5))
        
        label_pos = Text(
            "a≥0时，|a|=a",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_POSITIVE
        ).move_to(UP * 3)
        
        self.play(Create(positive_region), run_time=0.6)
        self.play(FadeIn(label_pos, shift=DOWN * 0.2), run_time=0.6)
        
        # 示例
        example_pos = MathTex(r"|5| = 5", font_size=32, color=self.COLOR_POSITIVE).move_to(UP * 2.2)
        self.play(FadeIn(example_pos), run_time=0.5)
        self.wait(0.8)
        
        # 数轴负半轴高亮
        negative_region = Rectangle(
            width=4.0,
            height=0.4,
            fill_color=self.COLOR_NEGATIVE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(self.numberline.n2p(-2.5))
        
        label_neg = Text(
            "a<0时，|a|=-a",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_NEGATIVE
        ).move_to(UP * 0.8)
        
        self.play(Create(negative_region), run_time=0.6)
        self.play(FadeIn(label_neg, shift=DOWN * 0.2), run_time=0.6)
        
        # 示例
        example_neg = MathTex(r"|-5| = -(-5) = 5", font_size=32, color=self.COLOR_NEGATIVE).move_to(ORIGIN)
        self.play(FadeIn(example_neg), run_time=0.7)
        self.wait(1.0)
        
        # 零点高亮
        origin_dot = Dot(self.origin_point, color=self.COLOR_ZERO, radius=0.15)
        self.play(Flash(origin_dot, color=self.COLOR_ZERO, flash_radius=0.4), run_time=0.5)
        
        label_zero = MathTex(r"|0| = 0", font_size=32, color=self.COLOR_ZERO).move_to(DOWN * 1.2)
        self.play(FadeIn(label_zero), run_time=0.4)
        self.wait(1.9)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(piecewise_formula),
            FadeOut(positive_region),
            FadeOut(negative_region),
            FadeOut(label_pos),
            FadeOut(label_neg),
            FadeOut(example_pos),
            FadeOut(example_neg),
            FadeOut(origin_dot),
            FadeOut(label_zero),
            run_time=0.6
        )
    
    def scene_5_symmetry(self):
        """场景5: 对称性展示 (28-36秒)"""
        # 标题
        title = Text(
            "对称性",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式
        symmetry_formula = MathTex(r"|-a| = |a|", font_size=44, color=self.COLOR_HIGHLIGHT).move_to(UP * 5.5)
        self.play(Write(symmetry_formula), run_time=0.7)
        
        # 示例1：3和-3
        value_1 = 3
        point_pos_1 = self.numberline.n2p(value_1)
        point_neg_1 = self.numberline.n2p(-value_1)
        
        dot_pos_1 = Dot(point_pos_1, color=self.COLOR_POSITIVE, radius=0.1)
        dot_neg_1 = Dot(point_neg_1, color=self.COLOR_NEGATIVE, radius=0.1)
        
        label_pos_1 = MathTex(f"{value_1}", font_size=28, color=self.COLOR_POSITIVE).next_to(dot_pos_1, UP, buff=0.15)
        label_neg_1 = MathTex(f"{-value_1}", font_size=28, color=self.COLOR_NEGATIVE).next_to(dot_neg_1, UP, buff=0.15)
        
        self.play(FadeIn(dot_pos_1), FadeIn(label_pos_1), run_time=0.4)
        self.play(FadeIn(dot_neg_1), FadeIn(label_neg_1), run_time=0.4)
        
        # 对称虚线（原点处）
        symmetry_line = DashedLine(
            start=self.origin_point + DOWN * 1.0,
            end=self.origin_point + UP * 0.8,
            color=self.COLOR_HIGHLIGHT,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(symmetry_line), run_time=0.5)
        
        # 距离箭头
        arrow_pos_1 = DoubleArrow(
            start=self.origin_point,
            end=point_pos_1,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        arrow_neg_1 = DoubleArrow(
            start=self.origin_point,
            end=point_neg_1,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        self.play(Create(arrow_pos_1), Create(arrow_neg_1), run_time=0.8)
        
        # 标注"距离相等"
        equal_dist = Text(
            "距离相等",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(equal_dist), run_time=0.5)
        self.wait(0.6)
        
        # 更换示例：4和-4
        value_2 = 4
        point_pos_2 = self.numberline.n2p(value_2)
        point_neg_2 = self.numberline.n2p(-value_2)
        
        dot_pos_2 = Dot(point_pos_2, color=self.COLOR_POSITIVE, radius=0.1)
        dot_neg_2 = Dot(point_neg_2, color=self.COLOR_NEGATIVE, radius=0.1)
        
        label_pos_2 = MathTex(f"{value_2}", font_size=28, color=self.COLOR_POSITIVE).next_to(dot_pos_2, UP, buff=0.15)
        label_neg_2 = MathTex(f"{-value_2}", font_size=28, color=self.COLOR_NEGATIVE).next_to(dot_neg_2, UP, buff=0.15)
        
        arrow_pos_2 = DoubleArrow(
            start=self.origin_point,
            end=point_pos_2,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        arrow_neg_2 = DoubleArrow(
            start=self.origin_point,
            end=point_neg_2,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        self.play(
            Transform(dot_pos_1, dot_pos_2),
            Transform(dot_neg_1, dot_neg_2),
            Transform(label_pos_1, label_pos_2),
            Transform(label_neg_1, label_neg_2),
            Transform(arrow_pos_1, arrow_pos_2),
            Transform(arrow_neg_1, arrow_neg_2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 再换：2.5和-2.5
        value_3 = 2.5
        point_pos_3 = self.numberline.n2p(value_3)
        point_neg_3 = self.numberline.n2p(-value_3)
        
        dot_pos_3 = Dot(point_pos_3, color=self.COLOR_POSITIVE, radius=0.1)
        dot_neg_3 = Dot(point_neg_3, color=self.COLOR_NEGATIVE, radius=0.1)
        
        label_pos_3 = MathTex("2.5", font_size=28, color=self.COLOR_POSITIVE).next_to(dot_pos_3, UP, buff=0.15)
        label_neg_3 = MathTex("-2.5", font_size=28, color=self.COLOR_NEGATIVE).next_to(dot_neg_3, UP, buff=0.15)
        
        arrow_pos_3 = DoubleArrow(
            start=self.origin_point,
            end=point_pos_3,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        arrow_neg_3 = DoubleArrow(
            start=self.origin_point,
            end=point_neg_3,
            color=self.COLOR_DISTANCE,
            buff=0,
            stroke_width=3,
            tip_length=0.12
        ).shift(DOWN * 0.4)
        
        self.play(
            Transform(dot_pos_1, dot_pos_3),
            Transform(dot_neg_1, dot_neg_3),
            Transform(label_pos_1, label_pos_3),
            Transform(label_neg_1, label_neg_3),
            Transform(arrow_pos_1, arrow_pos_3),
            Transform(arrow_neg_1, arrow_neg_3),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(symmetry_formula),
            FadeOut(dot_pos_1),
            FadeOut(dot_neg_1),
            FadeOut(label_pos_1),
            FadeOut(label_neg_1),
            FadeOut(symmetry_line),
            FadeOut(arrow_pos_1),
            FadeOut(arrow_neg_1),
            FadeOut(equal_dist),
            run_time=0.6
        )
    
    def scene_6_real_world_applications(self):
        """场景6: 实际应用示例 (36-48秒)"""
        # 标题
        title = Text(
            "生活中的绝对值",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.7)
        
        # 示例1：温度
        example_1_text = Text(
            "例1：温度 -5°C",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(example_1_text, shift=DOWN * 0.2), run_time=0.6)
        
        # 温度计（简化垂直）
        thermometer_body = Rectangle(
            width=0.5,
            height=3.5,
            fill_color=GRAY,
            fill_opacity=0.2,
            stroke_color=WHITE,
            stroke_width=2
        ).move_to(RIGHT * 3 + UP * 2.5)
        
        thermometer_fill = Rectangle(
            width=0.3,
            height=1.2,
            fill_color=BLUE_E,
            fill_opacity=0.7,
            stroke_width=0
        ).move_to(thermometer_body.get_bottom() + UP * 0.6)
        
        # 刻度
        scale_0 = Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=2).move_to(thermometer_body.get_center())
        scale_label_0 = MathTex("0", font_size=20).next_to(scale_0, RIGHT, buff=0.2)
        
        scale_neg5 = Line(LEFT * 0.25, RIGHT * 0.25, color=BLUE, stroke_width=2).move_to(thermometer_body.get_bottom() + UP * 0.6)
        scale_label_neg5 = MathTex("-5", font_size=20, color=BLUE).next_to(scale_neg5, RIGHT, buff=0.2)
        
        thermometer = VGroup(thermometer_body, thermometer_fill, scale_0, scale_label_0, scale_neg5, scale_label_neg5)
        
        self.play(Create(thermometer), run_time=0.8)
        
        # 标记-5°C
        temp_mark = Dot(scale_neg5.get_center(), color=BLUE, radius=0.1)
        self.play(FadeIn(temp_mark, scale=0.5), run_time=0.4)
        
        # 解释
        explanation_1 = Text(
            "距离0°C是5度",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5 + LEFT * 1.5)
        
        self.play(FadeIn(explanation_1), run_time=0.6)
        
        # 公式
        formula_temp = MathTex(r"|-5| = 5", font_size=36, color=self.COLOR_HIGHLIGHT).move_to(UP * 2.5 + LEFT * 1.5)
        self.play(Write(formula_temp), run_time=0.5)
        self.wait(1.0)
        
        # 淡出温度示例
        self.play(
            FadeOut(thermometer),
            FadeOut(temp_mark),
            FadeOut(explanation_1),
            FadeOut(formula_temp),
            run_time=0.5
        )
        
        # 示例2：欠款
        example_2_text = Text(
            "例2：欠款300元",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Transform(example_1_text, example_2_text), run_time=0.6)
        
        # 在数轴上标记（缩放到合适范围）
        # 临时创建小范围数轴
        small_numberline = NumberLine(
            x_range=[-400, 400, 100],
            length=7,
            color=WHITE,
            include_numbers=True,
            numbers_to_include=[-300, 0, 300],
            font_size=22,
            tick_size=0.08,
            stroke_width=2
        ).move_to(UP * 1.5)
        
        self.play(Create(small_numberline), run_time=0.5)
        
        # 标记-300
        debt_point = small_numberline.n2p(-300)
        debt_mark = Dot(debt_point, color=self.COLOR_NEGATIVE, radius=0.1)
        debt_label = MathTex("-300", font_size=28, color=self.COLOR_NEGATIVE).next_to(debt_mark, DOWN, buff=0.2)
        
        self.play(FadeIn(debt_mark), FadeIn(debt_label), run_time=0.5)
        
        # 解释
        explanation_2 = Text(
            "欠款数额是300元",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(explanation_2), run_time=0.6)
        
        # 公式
        formula_debt = MathTex(r"|-300| = 300", font_size=36, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 1.5)
        self.play(Write(formula_debt), run_time=0.5)
        self.wait(3.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example_1_text),
            FadeOut(small_numberline),
            FadeOut(debt_mark),
            FadeOut(debt_label),
            FadeOut(explanation_2),
            FadeOut(formula_debt),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与片尾 (48-60秒)"""
        # 标题
        title = Text(
            "绝对值三要点",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.7)
        
        # 要点卡片
        card_1 = self.create_summary_card(
            "定义",
            "到原点的距离",
            self.COLOR_PRIMARY,
            UP * 4.5
        )
        
        card_2 = self.create_summary_card(
            "性质",
            "|a| ≥ 0 (非负)",
            self.COLOR_POSITIVE,
            UP * 3
        )
        
        card_3 = self.create_summary_card(
            "对称",
            "|-a| = |a|",
            self.COLOR_HIGHLIGHT,
            UP * 1.5
        )
        
        # 卡片依次滑入
        self.play(card_1.animate.shift(RIGHT * 0), run_time=0.5)
        self.wait(0.2)
        self.play(card_2.animate.shift(RIGHT * 0), run_time=0.5)
        self.wait(0.2)
        self.play(card_3.animate.shift(RIGHT * 0), run_time=0.5)
        self.wait(1.0)
        
        # 公式汇总
        formula_summary = VGroup(
            MathTex(r"|a| = \begin{cases} a, & a \geq 0 \\ -a, & a < 0 \end{cases}", font_size=32),
            MathTex(r"|a| \geq 0", font_size=32),
            MathTex(r"|-a| = |a|", font_size=32)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 1.5)
        
        self.play(FadeIn(formula_summary, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)
        
        # 淡出所有内容
        self.play(
            FadeOut(title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(formula_summary),
            FadeOut(self.numberline),
            run_time=0.8
        )
        
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
        
        self.play(Transform(self.author_info, author_name), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.6)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画（数字符号）
        decorations = VGroup(*[
            MathTex(r"| \cdot |", font_size=28, color=GOLD).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        
        self.play(*[FadeIn(dec, scale=0.5) for dec in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.2))
        self.wait(0.6)
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 左侧色块
        color_bar = Rectangle(
            width=0.25,
            height=0.9,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(title, font="PingFang SC", font_size=28, color=WHITE, weight=BOLD)
        
        # 内容
        content_text = Text(content, font="PingFang SC", font_size=22, color=GRAY_A)
        
        # 组合
        text_group = VGroup(title_text, content_text).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        card = VGroup(color_bar, text_group).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql absolute_value.py AbsoluteValueConcept  # 快速预览
# manim -qh absolute_value.py AbsoluteValueConcept   # 高质量 1080p