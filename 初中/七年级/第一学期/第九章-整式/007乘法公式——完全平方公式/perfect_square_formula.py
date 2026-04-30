"""
完全平方公式教学动画 - Perfect Square Formula Animation
使用 Manim 创建的初中数学教学视频

内容: (a+b)² = a² + 2ab + b² 的几何推导与理解
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


class PerfectSquareFormula(Scene):
    """
    完全平方公式教学动画场景
    
    场景顺序:
    1. 开场钩子 - 提出问题
    2. 公式展开 - 展示完整公式
    3. 几何直观 - 构造大正方形
    4. 几何分割 - 分割成四个区域
    5. 区域着色 - 标注各区域面积
    6. 公式推导 - 从几何到代数
    7. 例题结尾 - 应用与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - a项
        self.COLOR_TERTIARY = "#2ecc71"     # 绿色 - b项
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_formula_introduction()
        self.show_geometric_construction()
        self.show_geometric_division()
        self.show_area_coloring()
        self.show_formula_derivation()
        self.show_example_and_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 基准参数
        self.side_a = 2.0
        self.side_b = 1.0
        self.total_side = self.side_a + self.side_b  # 3.0
        
        # 缩放因子（适应屏幕）
        self.SCALE = 1.0
        self.center = np.array([0, 1.5, 0])
        
        # 大正方形顶点（边长 a+b）
        half = self.total_side / 2 * self.SCALE
        self.vertices = [
            self.center + np.array([-half, -half, 0]),  # 左下 [0]
            self.center + np.array([half, -half, 0]),   # 右下 [1]
            self.center + np.array([half, half, 0]),    # 右上 [2]
            self.center + np.array([-half, half, 0])    # 左上 [3]
        ]
        
        # 分割点坐标
        # 水平分割线 y 坐标（从底部往上 side_b 的位置）
        self.split_horizontal_y = self.center[1] - half + self.side_b * self.SCALE
        
        # 垂直分割线 x 坐标（从左边往右 side_a 的位置）
        self.split_vertical_x = self.center[0] - half + self.side_a * self.SCALE
        
        # 四个区域的顶点
        # 区域1: a×a (左上红色)
        self.region_aa_vertices = [
            self.vertices[3],  # 左上角
            np.array([self.split_vertical_x, self.vertices[3][1], 0]),  # 右上
            np.array([self.split_vertical_x, self.split_horizontal_y, 0]),  # 右下
            np.array([self.vertices[3][0], self.split_horizontal_y, 0])  # 左下
        ]
        
        # 区域2: a×b (右上绿色)
        self.region_ab_1_vertices = [
            np.array([self.split_vertical_x, self.vertices[2][1], 0]),  # 左上
            self.vertices[2],  # 右上
            np.array([self.vertices[2][0], self.split_horizontal_y, 0]),  # 右下
            np.array([self.split_vertical_x, self.split_horizontal_y, 0])  # 左下
        ]
        
        # 区域3: b×a (左下绿色)
        self.region_ab_2_vertices = [
            np.array([self.vertices[0][0], self.split_horizontal_y, 0]),  # 左上
            np.array([self.split_vertical_x, self.split_horizontal_y, 0]),  # 右上
            np.array([self.split_vertical_x, self.vertices[0][1], 0]),  # 右下
            self.vertices[0]  # 左下
        ]
        
        # 区域4: b×b (右下蓝色)
        self.region_bb_vertices = [
            np.array([self.split_vertical_x, self.split_horizontal_y, 0]),  # 左上
            np.array([self.vertices[1][0], self.split_horizontal_y, 0]),  # 右上
            self.vertices[1],  # 右下
            np.array([self.split_vertical_x, self.vertices[1][1], 0])  # 左下
        ]
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证大正方形边长
        side_length = np.linalg.norm(self.vertices[1] - self.vertices[0])
        expected_side = self.total_side * self.SCALE
        
        if abs(side_length - expected_side) > epsilon:
            print(f"WARNING: 大正方形边长计算错误! 实际: {side_length:.6f}, 期望: {expected_side:.6f}")
        
        # 验证分割点位置
        # 水平线应该把正方形分成高度为 b 和 a 的两部分
        bottom_height = abs(self.split_horizontal_y - self.vertices[0][1])
        expected_bottom_height = self.side_b * self.SCALE
        
        if abs(bottom_height - expected_bottom_height) > epsilon:
            print(f"WARNING: 水平分割位置错误! 实际: {bottom_height:.6f}, 期望: {expected_bottom_height:.6f}")
        
        print("✓ 几何验证完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_chinese = Text(
            "你知道",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        )
        hook_formula = MathTex(
            r"(a+b)^2",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        )
        hook_chinese_2 = Text(
            "等于什么吗？",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        )
        
        hook_text = VGroup(hook_chinese, hook_formula, hook_chinese_2).arrange(RIGHT, buff=0.3).move_to(UP * 5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 神秘公式
        formula_preview = MathTex(
            r"(a+b)^2 = \,?",
            font_size=52,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2)
        
        self.play(FadeIn(formula_preview, scale=1.2), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(formula_preview),
            run_time=0.5
        )
    
    def show_formula_introduction(self):
        """场景2: 公式展开"""
        # 标题
        title = Text(
            "完全平方公式",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 第一个公式: (a+b)²
        formula_1 = MathTex(
            r"(a+b)^2", r"=", r"a^2", r"+", r"2ab", r"+", r"b^2",
            font_size=40
        ).move_to(UP * 3.5)
        
        # 设置颜色
        formula_1[2].set_color(self.COLOR_SECONDARY)  # a²
        formula_1[4].set_color(self.COLOR_TERTIARY)   # 2ab
        formula_1[6].set_color(self.COLOR_PRIMARY)    # b²
        
        self.play(Write(formula_1), run_time=1.5)
        
        # 强调中间项 2ab
        middle_term_box = SurroundingRectangle(
            formula_1[4],
            color=self.COLOR_HIGHLIGHT,
            buff=0.15
        )
        
        self.play(Create(middle_term_box), run_time=0.5)
        self.play(Flash(formula_1[4], color=self.COLOR_HIGHLIGHT), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "注意中间项！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(middle_term_box, DOWN, buff=0.4)
        
        self.play(FadeIn(explanation), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(middle_term_box), FadeOut(explanation), run_time=0.3)
        
        # 第二个公式: (a-b)²
        formula_2 = MathTex(
            r"(a-b)^2", r"=", r"a^2", r"-", r"2ab", r"+", r"b^2",
            font_size=40
        ).move_to(UP * 1.5)
        
        # 设置颜色
        formula_2[2].set_color(self.COLOR_SECONDARY)  # a²
        formula_2[4].set_color(self.COLOR_TERTIARY)   # 2ab
        formula_2[6].set_color(self.COLOR_PRIMARY)    # b²
        
        self.play(Write(formula_2), run_time=1.5)
        
        # 强调符号差异
        minus_box = SurroundingRectangle(
            formula_2[3],
            color=RED,
            buff=0.1
        )
        
        self.play(Create(minus_box), Flash(formula_2[3], color=RED), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(minus_box), run_time=0.3)
        
        # 记忆口诀
        mnemonic_1 = Text(
            "首平方，尾平方",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        mnemonic_2 = Text(
            "首尾二倍放中央",
            font="PingFang SC",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(mnemonic_1, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(mnemonic_2, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)
        
        # 清理，保留第一个公式并缩小移到顶部
        self.play(
            FadeOut(title),
            FadeOut(formula_2),
            FadeOut(mnemonic_1),
            FadeOut(mnemonic_2),
            run_time=0.5
        )
        
        # 缩小公式移到顶部
        formula_1_small = formula_1.copy().scale(0.7).move_to(UP * 6.5)
        self.play(Transform(formula_1, formula_1_small), run_time=0.6)
        self.formula_top = formula_1
    
    def show_geometric_construction(self):
        """场景3: 几何直观 - 构造大正方形"""
        # 说明文字
        explanation = Text(
            "用正方形来理解",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(explanation), run_time=0.8)
        
        # 创建大正方形
        big_square = Polygon(
            *self.vertices,
            color=WHITE,
            stroke_width=4
        )
        
        self.play(Create(big_square), run_time=1.2)
        
        # 标注边长 (顶部)
        label_top_a = MathTex(r"a", font_size=32, color=self.COLOR_SECONDARY)
        label_top_b = MathTex(r"b", font_size=32, color=self.COLOR_PRIMARY)
        
        # 计算标注位置（顶边中点上方）
        top_left = self.vertices[3]
        top_split = np.array([self.split_vertical_x, self.vertices[3][1], 0])
        top_right = self.vertices[2]
        
        label_top_a.next_to((top_left + top_split) / 2, UP, buff=0.2)
        label_top_b.next_to((top_split + top_right) / 2, UP, buff=0.2)
        
        # 大括号标注整体边长
        brace_top = Brace(Line(self.vertices[3], self.vertices[2]), direction=UP, buff=0.1)
        label_total = MathTex(r"a+b", font_size=36, color=self.COLOR_HIGHLIGHT)
        label_total.next_to(brace_top, UP, buff=0.1)
        
        self.play(
            FadeIn(brace_top),
            FadeIn(label_total),
            run_time=0.8
        )
        
        # 面积公式
        area_formula = MathTex(
            r"S = (a+b)^2",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(area_formula), run_time=1.0)
        self.wait(1.0)
        
        # 提示分割
        hint = Text(
            "让我们分割这个正方形",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(hint),
            FadeOut(brace_top),
            FadeOut(label_total),
            run_time=0.4
        )
        
        # 保留
        self.big_square = big_square
        self.area_formula = area_formula
    
    def show_geometric_division(self):
        """场景4: 几何分割"""
        # 绘制水平分割线
        h_line_left = self.vertices[0]
        h_line_right = self.vertices[1]
        h_line = DashedLine(
            np.array([h_line_left[0], self.split_horizontal_y, 0]),
            np.array([h_line_right[0], self.split_horizontal_y, 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(h_line), run_time=0.8)
        
        # 标注上方高度 a
        left_top = np.array([self.vertices[0][0], self.split_horizontal_y, 0])
        left_upper = self.vertices[3]
        
        brace_left_a = Brace(
            Line(left_top, left_upper),
            direction=LEFT,
            buff=0.1
        )
        label_height_a = MathTex(r"a", font_size=28, color=self.COLOR_SECONDARY)
        label_height_a.next_to(brace_left_a, LEFT, buff=0.1)
        
        self.play(
            FadeIn(brace_left_a),
            FadeIn(label_height_a),
            run_time=0.6
        )
        
        # 标注下方高度 b
        left_bottom = self.vertices[0]
        
        brace_left_b = Brace(
            Line(left_bottom, left_top),
            direction=LEFT,
            buff=0.1
        )
        label_height_b = MathTex(r"b", font_size=28, color=self.COLOR_PRIMARY)
        label_height_b.next_to(brace_left_b, LEFT, buff=0.1)
        
        self.play(
            FadeIn(brace_left_b),
            FadeIn(label_height_b),
            run_time=0.6
        )
        
        # 绘制垂直分割线
        v_line_bottom = self.vertices[0]
        v_line_top = self.vertices[3]
        v_line = DashedLine(
            np.array([self.split_vertical_x, v_line_bottom[1], 0]),
            np.array([self.split_vertical_x, v_line_top[1], 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(v_line), run_time=0.8)
        
        # 标注左侧宽度 a
        bottom_left = self.vertices[0]
        bottom_split = np.array([self.split_vertical_x, self.vertices[0][1], 0])
        
        brace_bottom_a = Brace(
            Line(bottom_left, bottom_split),
            direction=DOWN,
            buff=0.1
        )
        label_width_a = MathTex(r"a", font_size=28, color=self.COLOR_SECONDARY)
        label_width_a.next_to(brace_bottom_a, DOWN, buff=0.1)
        
        self.play(
            FadeIn(brace_bottom_a),
            FadeIn(label_width_a),
            run_time=0.6
        )
        
        # 标注右侧宽度 b
        bottom_right = self.vertices[1]
        
        brace_bottom_b = Brace(
            Line(bottom_split, bottom_right),
            direction=DOWN,
            buff=0.1
        )
        label_width_b = MathTex(r"b", font_size=28, color=self.COLOR_PRIMARY)
        label_width_b.next_to(brace_bottom_b, DOWN, buff=0.1)
        
        self.play(
            FadeIn(brace_bottom_b),
            FadeIn(label_width_b),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 保留线条，淡出标注
        self.play(
            FadeOut(brace_left_a),
            FadeOut(label_height_a),
            FadeOut(brace_left_b),
            FadeOut(label_height_b),
            FadeOut(brace_bottom_a),
            FadeOut(label_width_a),
            FadeOut(brace_bottom_b),
            FadeOut(label_width_b),
            run_time=0.4
        )
        
        # 保留
        self.h_line = h_line
        self.v_line = v_line
    
    def show_area_coloring(self):
        """场景5: 区域着色与标注"""
        # 区域1: a×a (左上红色)
        region_aa = Polygon(
            *self.region_aa_vertices,
            fill_color=self.COLOR_SECONDARY,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        self.play(FadeIn(region_aa), run_time=0.6)
        
        # 计算中心位置
        center_aa = np.mean(self.region_aa_vertices, axis=0)
        label_aa = MathTex(r"a^2", font_size=36, color=WHITE).move_to(center_aa)
        
        self.play(Write(label_aa), run_time=0.5)
        
        # 区域2: a×b (右上绿色)
        region_ab_1 = Polygon(
            *self.region_ab_1_vertices,
            fill_color=self.COLOR_TERTIARY,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        self.play(FadeIn(region_ab_1), run_time=0.6)
        
        center_ab_1 = np.mean(self.region_ab_1_vertices, axis=0)
        label_ab_1 = MathTex(r"ab", font_size=36, color=WHITE).move_to(center_ab_1)
        
        self.play(Write(label_ab_1), run_time=0.5)
        
        # 区域3: b×a (左下绿色)
        region_ab_2 = Polygon(
            *self.region_ab_2_vertices,
            fill_color=self.COLOR_TERTIARY,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        self.play(FadeIn(region_ab_2), run_time=0.6)
        
        center_ab_2 = np.mean(self.region_ab_2_vertices, axis=0)
        label_ab_2 = MathTex(r"ab", font_size=36, color=WHITE).move_to(center_ab_2)
        
        self.play(Write(label_ab_2), run_time=0.5)
        
        # 区域4: b×b (右下蓝色)
        region_bb = Polygon(
            *self.region_bb_vertices,
            fill_color=self.COLOR_PRIMARY,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        self.play(FadeIn(region_bb), run_time=0.6)
        
        center_bb = np.mean(self.region_bb_vertices, axis=0)
        label_bb = MathTex(r"b^2", font_size=36, color=WHITE).move_to(center_bb)
        
        self.play(Write(label_bb), run_time=0.5)
        
        # 强调两个 ab
        self.play(
            Indicate(label_ab_1, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            Indicate(label_ab_2, scale_factor=1.3, color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 说明文字
        note = Text(
            "注意：有两个 ab",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.5)
        
        self.play(FadeOut(note), run_time=0.3)
        
        # 保留所有元素
        self.region_aa = region_aa
        self.region_ab_1 = region_ab_1
        self.region_ab_2 = region_ab_2
        self.region_bb = region_bb
        self.label_aa = label_aa
        self.label_ab_1 = label_ab_1
        self.label_ab_2 = label_ab_2
        self.label_bb = label_bb
    
    def show_formula_derivation(self):
        """场景6: 公式推导"""
        # 说明文字
        explanation = Text(
            "总面积 = 四个小区域之和",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).move_to(DOWN * 3.5)
        
        self.play(Write(explanation), run_time=1.0)
        
        # 公式推导位置
        formula_y = -5
        
        # 等号左边
        lhs = MathTex(r"(a+b)^2", r"=", font_size=36).move_to(LEFT * 3 + UP * formula_y)
        
        self.play(Write(lhs), run_time=0.8)
        
        # 收集各项
        # a²
        term_aa = MathTex(r"a^2", font_size=36, color=self.COLOR_SECONDARY)
        term_aa.move_to(RIGHT * (-1.2) + UP * formula_y)
        
        self.play(
            TransformFromCopy(self.label_aa, term_aa),
            self.label_aa.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        # + ab (第一个)
        plus_1 = MathTex(r"+", font_size=36).next_to(term_aa, RIGHT, buff=0.15)
        term_ab_1 = MathTex(r"ab", font_size=36, color=self.COLOR_TERTIARY)
        term_ab_1.next_to(plus_1, RIGHT, buff=0.15)
        
        self.play(
            Write(plus_1),
            TransformFromCopy(self.label_ab_1, term_ab_1),
            self.label_ab_1.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        # + ab (第二个)
        plus_2 = MathTex(r"+", font_size=36).next_to(term_ab_1, RIGHT, buff=0.15)
        term_ab_2 = MathTex(r"ab", font_size=36, color=self.COLOR_TERTIARY)
        term_ab_2.next_to(plus_2, RIGHT, buff=0.15)
        
        self.play(
            Write(plus_2),
            TransformFromCopy(self.label_ab_2, term_ab_2),
            self.label_ab_2.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        # 合并 ab + ab = 2ab
        term_2ab = MathTex(r"2ab", font_size=36, color=self.COLOR_TERTIARY)
        term_2ab.move_to((term_ab_1.get_center() + term_ab_2.get_center()) / 2)
        
        box_combine = SurroundingRectangle(
            VGroup(term_ab_1, plus_2, term_ab_2),
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(Create(box_combine), run_time=0.4)
        self.play(
            FadeOut(term_ab_1),
            FadeOut(plus_2),
            FadeOut(term_ab_2),
            FadeOut(box_combine),
            FadeIn(term_2ab),
            run_time=0.8
        )
        
        # + b²
        plus_3 = MathTex(r"+", font_size=36).next_to(term_2ab, RIGHT, buff=0.15)
        term_bb = MathTex(r"b^2", font_size=36, color=self.COLOR_PRIMARY)
        term_bb.next_to(plus_3, RIGHT, buff=0.15)
        
        self.play(
            Write(plus_3),
            TransformFromCopy(self.label_bb, term_bb),
            self.label_bb.animate.set_opacity(0.3),
            run_time=0.8
        )
        
        # 完整公式
        complete_formula = VGroup(lhs, term_aa, plus_1, term_2ab, plus_3, term_bb)
        
        # 框选强调
        final_box = SurroundingRectangle(
            complete_formula,
            color=GOLD,
            buff=0.2
        )
        
        self.play(Create(final_box), run_time=0.6)
        self.play(Flash(complete_formula, color=GOLD), run_time=0.5)
        self.wait(1.5)
        
        # 清理图形部分
        self.play(
            FadeOut(self.big_square),
            FadeOut(self.h_line),
            FadeOut(self.v_line),
            FadeOut(self.region_aa),
            FadeOut(self.region_ab_1),
            FadeOut(self.region_ab_2),
            FadeOut(self.region_bb),
            FadeOut(self.label_aa),
            FadeOut(self.label_ab_1),
            FadeOut(self.label_ab_2),
            FadeOut(self.label_bb),
            FadeOut(self.area_formula),
            FadeOut(explanation),
            FadeOut(final_box),
            run_time=0.6
        )
        
        # 公式移到顶部
        complete_small = complete_formula.copy().scale(0.8).move_to(UP * 5.5)
        self.play(
            Transform(complete_formula, complete_small),
            FadeOut(self.formula_top),
            run_time=0.6
        )
        
        self.complete_formula = complete_formula
    
    def show_example_and_outro(self):
        """场景7: 例题与结尾"""
        # 例题标题
        example_title = Text(
            "例题",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 3.5)
        
        self.play(Write(example_title), run_time=0.6)
        
        # 题目
        question_chinese = Text(
            "计算：",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        question_formula = MathTex(r"(x+3)^2", font_size=36)
        
        question = VGroup(question_chinese, question_formula).arrange(RIGHT, buff=0.3).move_to(UP * 2.2)
        
        self.play(Write(question), run_time=0.8)
        
        # 解答步骤
        step_1 = MathTex(
            r"(x+3)^2", r"=", r"x^2", r"+", r"2 \cdot x \cdot 3", r"+", r"3^2",
            font_size=32
        ).move_to(UP * 0.5)
        
        self.play(Write(step_1), run_time=1.2)
        
        # 简化
        step_2 = MathTex(
            r"=", r"x^2", r"+", r"6x", r"+", r"9",
            font_size=32
        ).move_to(DOWN * 1)
        
        self.play(TransformMatchingTex(step_1.copy(), step_2), run_time=1.0)
        
        # 答案框
        answer_box = SurroundingRectangle(
            step_2,
            color=self.COLOR_HIGHLIGHT,
            buff=0.2
        )
        
        self.play(Create(answer_box), run_time=0.5)
        self.play(Flash(step_2, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        self.wait(1.0)
        
        # 清理例题
        self.play(
            FadeOut(example_title),
            FadeOut(question),
            FadeOut(step_1),
            FadeOut(step_2),
            FadeOut(answer_box),
            FadeOut(self.complete_formula),
            run_time=0.6
        )
        
        # 总结
        summary = Text(
            "掌握公式，展开轻松！",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(FadeIn(summary, scale=1.2), run_time=0.8)
        self.wait(0.8)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(ORIGIN)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).move_to(DOWN * 2.5)
        
        self.play(
            Transform(self.author_info, author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 装饰 - 小方块
        squares = VGroup(*[
            Square(side_length=0.3, fill_color=color, fill_opacity=0.8, stroke_width=0)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i, color in enumerate([self.COLOR_SECONDARY, self.COLOR_TERTIARY, self.COLOR_PRIMARY] * 2)
        ])
        
        self.play(*[FadeIn(sq, scale=0.5) for sq in squares], run_time=0.6)
        self.play(Rotate(squares, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql perfect_square_formula.py PerfectSquareFormula  # 快速预览
# manim -qh perfect_square_formula.py PerfectSquareFormula   # 高质量渲染