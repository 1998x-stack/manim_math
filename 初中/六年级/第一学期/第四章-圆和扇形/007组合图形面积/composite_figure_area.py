"""
组合图形面积计算教学动画
Composite Figure Area Calculation Teaching Animation

使用 Manim 创建的六年级数学教学视频
内容: 割补法计算组合图形面积（正方形+半圆-四分之一圆）
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


class CompositeFigureArea(Scene):
    """
    组合图形面积计算教学动画
    
    场景顺序:
    1. 开场钩子 - 提出问题
    2. 割补法介绍
    3. 分解步骤1: 正方形
    4. 分解步骤2: 半圆
    5. 分解步骤3: 四分之一圆（减去）
    6. 总结计算
    7. 结尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要图形
        self.COLOR_SECONDARY = "#e74c3c"     # 红色 - 需要减去的部分
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_SECTOR = "#2ecc71"        # 绿色 - 扇形/半圆
        self.COLOR_SQUARE = "#3498db"        # 蓝色 - 正方形
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduction()
        self.scene_3_square()
        self.scene_4_semicircle()
        self.scene_5_quarter_circle()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素和计算"""
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 1.0
        self.side_length = 2.5
        
        # 正方形中心点
        self.center = ORIGIN * self.SCALE + self.OFFSET
        
        # 正方形四个顶点
        half_side = self.side_length / 2
        self.A = self.center + UP * half_side + LEFT * half_side      # 左上
        self.B = self.center + UP * half_side + RIGHT * half_side     # 右上
        self.C = self.center + DOWN * half_side + RIGHT * half_side   # 右下
        self.D = self.center + DOWN * half_side + LEFT * half_side    # 左下
        
        # 半圆圆心（正方形上边中点）
        self.semicircle_center = (self.A + self.B) / 2
        
        # 四分之一圆圆心（正方形右下角）
        self.quarter_circle_center = self.C
        
        # 半径
        self.radius = half_side
        
        # 面积计算
        self.area_square = self.side_length ** 2
        self.area_semicircle = PI * self.radius ** 2 / 2
        self.area_quarter = PI * self.radius ** 2 / 4
        self.total_area = self.area_square + self.area_semicircle - self.area_quarter
        
        # 验证几何
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        # 验证正方形顶点距离
        AB = np.linalg.norm(self.B - self.A)
        BC = np.linalg.norm(self.C - self.B)
        CD = np.linalg.norm(self.D - self.C)
        DA = np.linalg.norm(self.A - self.D)
        
        epsilon = 1e-6
        assert abs(AB - self.side_length) < epsilon, "AB边长度不正确"
        assert abs(BC - self.side_length) < epsilon, "BC边长度不正确"
        assert abs(CD - self.side_length) < epsilon, "CD边长度不正确"
        assert abs(DA - self.side_length) < epsilon, "DA边长度不正确"
        
        # 验证半圆圆心位置
        dist_to_A = np.linalg.norm(self.semicircle_center - self.A)
        dist_to_B = np.linalg.norm(self.semicircle_center - self.B)
        assert abs(dist_to_A - self.radius) < epsilon, "半圆圆心到A的距离不正确"
        assert abs(dist_to_B - self.radius) < epsilon, "半圆圆心到B的距离不正确"
        
        print("✓ 几何验证通过")
        print(f"  正方形面积: {self.area_square:.2f}")
        print(f"  半圆面积: {self.area_semicircle:.2f}")
        print(f"  四分之一圆面积: {self.area_quarter:.2f}")
        print(f"  总面积: {self.total_area:.2f}")
    
    def create_composite_figure(self, color_mode="uniform"):
        """创建组合图形
        
        Args:
            color_mode: "uniform" (统一颜色) 或 "separate" (分别着色)
        """
        # 正方形
        square = Polygon(
            self.A, self.B, self.C, self.D,
            color=self.COLOR_SQUARE if color_mode == "separate" else self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=3
        )
        
        # 半圆（在正方形上方）
        semicircle = Arc(
            radius=self.radius,
            start_angle=0,
            angle=PI,
            color=self.COLOR_SECTOR if color_mode == "separate" else self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=3
        ).move_arc_center_to(self.semicircle_center)
        
        # 半圆底边闭合
        semicircle_base = Line(
            self.A, self.B,
            color=self.COLOR_SECTOR if color_mode == "separate" else self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        # 四分之一圆（在正方形内部右下角）
        quarter_circle = Arc(
            radius=self.radius,
            start_angle=PI,
            angle=PI/2,
            color=self.COLOR_SECONDARY if color_mode == "separate" else self.COLOR_PRIMARY,
            fill_opacity=0.2,
            stroke_width=3
        ).move_arc_center_to(self.quarter_circle_center)
        
        # 返回组
        if color_mode == "uniform":
            return VGroup(square, semicircle, semicircle_base, quarter_circle)
        else:
            return {
                "square": square,
                "semicircle": VGroup(semicircle, semicircle_base),
                "quarter_circle": quarter_circle,
                "all": VGroup(square, semicircle, semicircle_base, quarter_circle)
            }
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这个图形的面积怎么算？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 组合图形出现
        composite_fig = self.create_composite_figure("uniform")
        composite_fig.move_to(UP * 2)
        
        self.play(FadeIn(composite_fig, scale=0.8), run_time=1.0)
        self.wait(0.3)
        
        # 闪烁提示
        self.play(
            Flash(composite_fig, color=self.COLOR_HIGHLIGHT, flash_radius=1.2, num_lines=12),
            run_time=0.5
        )
        self.wait(1.0)
        
        # 清理钩子文字，保留图形
        self.play(FadeOut(hook_text), run_time=0.4)
        
        # 保存图形引用
        self.composite_figure = composite_fig
    
    def scene_2_introduction(self):
        """场景2: 割补法介绍"""
        # 标题
        title = Text(
            "割补法",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "把复杂图形分成简单图形",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.7)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 图形放大并居中
        self.play(
            self.composite_figure.animate.scale(1.1).move_to(UP * 1.0),
            run_time=0.8
        )
        
        # 分解箭头动画
        arrow_1 = Arrow(
            start=self.composite_figure.get_right() + RIGHT * 0.3,
            end=self.composite_figure.get_right() + RIGHT * 1.0,
            color=self.COLOR_AUXILIARY,
            buff=0
        )
        arrow_2 = Arrow(
            start=self.composite_figure.get_left() + LEFT * 0.3,
            end=self.composite_figure.get_left() + LEFT * 1.0,
            color=self.COLOR_AUXILIARY,
            buff=0
        )
        
        arrows = VGroup(arrow_1, arrow_2)
        
        self.play(Create(arrows), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(arrows),
            run_time=0.5
        )
    
    def scene_3_square(self):
        """场景3: 分解步骤1 - 正方形"""
        # 步骤标题
        step_title = Text(
            "第一步：找出正方形",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(step_title), run_time=0.8)
        
        # 创建分离的图形元素
        parts = self.create_composite_figure("separate")
        square_highlight = parts["square"].copy()
        
        # 替换原图形为分离版本
        self.play(
            Transform(self.composite_figure, parts["all"]),
            run_time=0.5
        )
        
        # 高亮正方形
        self.play(
            parts["square"].animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 边长标注
        side_label = MathTex(r"a = 2.5", font_size=32, color=WHITE)
        side_label.next_to(self.C, DOWN, buff=0.3)
        
        brace = Brace(Line(self.D, self.C), DOWN, buff=0.1, color=YELLOW)
        
        self.play(
            GrowFromCenter(brace),
            FadeIn(side_label, shift=DOWN * 0.2),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 面积公式
        formula_pos = LEFT * 3.5 + UP * 4
        formula = MathTex(
            r"S_1 = a^2",
            font_size=32,
            color=WHITE
        ).move_to(formula_pos)
        
        self.play(Write(formula), run_time=0.8)
        self.wait(0.3)
        
        # 计算结果
        result = MathTex(
            r"= 2.5^2 = 6.25",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, RIGHT, buff=0.2)
        
        self.play(Write(result), run_time=0.8)
        self.wait(1.5)
        
        # 恢复正方形颜色
        self.play(
            parts["square"].animate.set_stroke(color=self.COLOR_SQUARE, width=3),
            run_time=0.4
        )
        
        # 清理并保存
        self.play(
            FadeOut(step_title),
            FadeOut(brace),
            FadeOut(side_label),
            run_time=0.4
        )
        
        # 将公式和结果移到侧边记录
        formula_group = VGroup(formula, result)
        self.play(
            formula_group.animate.scale(0.7).move_to(LEFT * 3.5 + UP * 3.5),
            run_time=0.5
        )
        
        self.formula_1 = formula_group
    
    def scene_4_semicircle(self):
        """场景4: 分解步骤2 - 半圆"""
        # 步骤标题
        step_title = Text(
            "第二步：找出半圆",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(step_title), run_time=0.8)
        
        # 获取半圆（假设已经是分离着色的）
        parts = self.create_composite_figure("separate")
        
        # 高亮半圆
        semicircle_highlight = parts["semicircle"].copy().set_stroke(
            color=self.COLOR_HIGHLIGHT, width=5
        )
        
        self.play(Create(semicircle_highlight), run_time=0.8)
        self.wait(0.5)
        
        # 半径标注
        radius_line = DashedLine(
            self.semicircle_center,
            self.A,
            color=YELLOW,
            dash_length=0.08
        )
        
        radius_label = MathTex(r"r = 1.25", font_size=28, color=WHITE)
        radius_label.next_to(
            (self.semicircle_center + self.A) / 2,
            LEFT,
            buff=0.2
        )
        
        self.play(
            Create(radius_line),
            FadeIn(radius_label, shift=LEFT * 0.2),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 面积公式
        formula_pos = LEFT * 3.5 + UP * 2.8
        formula = MathTex(
            r"S_2 = \frac{\pi r^2}{2}",
            font_size=32,
            color=WHITE
        ).move_to(formula_pos)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.3)
        
        # 计算结果
        result = MathTex(
            r"\approx 2.45",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(formula, RIGHT, buff=0.2)
        
        self.play(Write(result), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(semicircle_highlight),
            FadeOut(radius_line),
            FadeOut(radius_label),
            run_time=0.4
        )
        
        # 保存公式
        formula_group = VGroup(formula, result)
        self.play(
            formula_group.animate.scale(0.7).move_to(LEFT * 3.5 + UP * 2.8),
            run_time=0.5
        )
        
        self.formula_2 = formula_group
    
    def scene_5_quarter_circle(self):
        """场景5: 分解步骤3 - 四分之一圆（需要减去）"""
        # 步骤标题
        step_title = Text(
            "第三步：注意多余部分",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(step_title), run_time=0.8)
        
        # 获取四分之一圆
        parts = self.create_composite_figure("separate")
        quarter_highlight = parts["quarter_circle"].copy()
        
        # 闪烁提示
        self.play(
            Flash(
                quarter_highlight,
                color=self.COLOR_SECONDARY,
                flash_radius=0.8,
                num_lines=8
            ),
            run_time=0.5
        )
        
        # 高亮红色
        quarter_highlight.set_stroke(color=RED, width=5)
        quarter_highlight.set_fill(color=RED, opacity=0.3)
        
        self.play(Create(quarter_highlight), run_time=0.8)
        self.wait(0.5)
        
        # 警告文字
        warning = Text(
            "这部分要减掉!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=RED,
            weight=BOLD
        ).move_to(DOWN * 0.5 + RIGHT * 2)
        
        arrow_warning = Arrow(
            start=warning.get_left(),
            end=self.quarter_circle_center + UP * 0.3 + RIGHT * 0.3,
            color=RED,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(
            Write(warning),
            Create(arrow_warning),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 面积公式
        formula_pos = LEFT * 3.5 + UP * 2.1
        formula = MathTex(
            r"S_3 = \frac{\pi r^2}{4}",
            font_size=32,
            color=WHITE
        ).move_to(formula_pos)
        
        self.play(Write(formula), run_time=1.0)
        self.wait(0.3)
        
        # 计算结果
        result = MathTex(
            r"\approx 1.23",
            font_size=32,
            color=RED
        ).next_to(formula, RIGHT, buff=0.2)
        
        self.play(Write(result), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(quarter_highlight),
            FadeOut(warning),
            FadeOut(arrow_warning),
            run_time=0.4
        )
        
        # 保存公式
        formula_group = VGroup(formula, result)
        self.play(
            formula_group.animate.scale(0.7).move_to(LEFT * 3.5 + UP * 2.1),
            run_time=0.5
        )
        
        self.formula_3 = formula_group
    
    def scene_6_summary(self):
        """场景6: 总结计算"""
        # 标题
        title = Text(
            "组合计算",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        
        # 总公式位置
        total_formula_pos = DOWN * 2.5
        
        # 总公式：S = S₁ + S₂ - S₃
        total_formula = MathTex(
            r"S = S_1 + S_2 - S_3",
            font_size=38,
            color=WHITE
        ).move_to(total_formula_pos)
        
        self.play(Write(total_formula), run_time=1.0)
        self.wait(0.8)
        
        # 代入数值
        calculation = MathTex(
            r"= 6.25 + 2.45 - 1.23",
            font_size=36,
            color=GRAY_A
        ).next_to(total_formula, DOWN, buff=0.5)
        
        self.play(Write(calculation), run_time=1.0)
        self.wait(0.8)
        
        # 等号
        equals = MathTex(r"=", font_size=36, color=WHITE).next_to(
            calculation, DOWN, buff=0.4
        )
        
        self.play(Write(equals), run_time=0.3)
        
        # 最终答案（大号、高亮）
        final_answer = MathTex(
            r"7.47",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).next_to(equals, DOWN, buff=0.4)
        
        unit = Text(
            "平方单位",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).next_to(final_answer, RIGHT, buff=0.3)
        
        answer_group = VGroup(final_answer, unit)
        
        self.play(
            Write(final_answer),
            FadeIn(unit, shift=LEFT * 0.2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 答案闪烁特效
        self.play(
            Flash(
                final_answer,
                color=YELLOW,
                flash_radius=1.0,
                num_lines=16
            ),
            final_answer.animate.scale(1.2),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 恢复大小
        self.play(final_answer.animate.scale(1/1.2), run_time=0.3)
        
        # 图形各部分依次闪烁展示
        parts = self.create_composite_figure("separate")
        
        flash_objects = [
            (parts["square"], self.COLOR_SQUARE),
            (parts["semicircle"], self.COLOR_SECTOR),
            (parts["quarter_circle"], self.COLOR_SECONDARY)
        ]
        
        for obj, color in flash_objects:
            self.play(
                Flash(obj, color=color, flash_radius=0.8, num_lines=8),
                run_time=0.4
            )
            self.wait(0.2)
        
        self.wait(2.0)
        
        # 全部淡出准备结尾
        self.play(
            FadeOut(title),
            FadeOut(total_formula),
            FadeOut(calculation),
            FadeOut(equals),
            FadeOut(answer_group),
            FadeOut(self.composite_figure),
            FadeOut(self.formula_1),
            FadeOut(self.formula_2),
            FadeOut(self.formula_3),
            run_time=0.8
        )
    
    def scene_7_outro(self):
        """场景7: 结尾总结和关注引导"""
        # 关键点提示框
        key_points_title = Text(
            "割补法三步骤",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4)
        
        self.play(Write(key_points_title), run_time=0.8)
        self.wait(0.5)
        
        # 三个关键点
        point_1 = Text(
            "① 识别基本图形",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 2.5)
        
        point_2 = Text(
            "② 加上凸出部分",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        point_3 = Text(
            "③ 减去重叠部分",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 0.5)
        
        # 依次显示要点
        for point in [point_1, point_2, point_3]:
            self.play(FadeIn(point, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.0)
        
        # 淡出要点
        self.play(
            FadeOut(key_points_title),
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 1.0)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.8
        )
        
        # 装饰：小图形漂浮
        decorations = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = follow_text.get_center() + 1.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            if i % 2 == 0:
                deco = Square(side_length=0.2, color=self.COLOR_SQUARE, fill_opacity=0.8)
            else:
                deco = Circle(radius=0.1, color=self.COLOR_SECTOR, fill_opacity=0.8)
            
            deco.move_to(pos)
            decorations.add(deco)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.8
        )
        
        # 旋转装饰
        self.play(Rotate(decorations, angle=PI, run_time=2.0))
        
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
# manim -pql composite_figure_area.py CompositeFigureArea  # 快速预览
# manim -qh composite_figure_area.py CompositeFigureArea   # 高质量渲染 (TikTok格式)