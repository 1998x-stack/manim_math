"""
弧长与扇形面积教学动画 - Arc Length and Sector Area Animation
使用 Manim 创建的九年级几何教学视频

内容: 弧长公式、扇形面积公式及其应用
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


class ArcLengthAndSectorArea(Scene):
    """
    弧长与扇形面积教学动画场景
    
    场景顺序:
    1. 开场钩子（披萨问题）
    2. 圆心角介绍
    3. 弧长公式推导
    4. 弧长示例计算
    5. 扇形定义
    6. 扇形面积公式1推导
    7. 扇形面积公式2
    8. 综合示例
    9. 结尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"      # 红色 - 扇形/弧
        self.COLOR_SECONDARY = "#3498db"    # 蓝色 - 辅助线
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点标注
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
        self.COLOR_CIRCLE = WHITE           # 白色 - 圆
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_central_angle()
        self.scene_3_arc_length_formula()
        self.scene_4_arc_length_example()
        self.scene_5_sector_definition()
        self.scene_6_sector_area_formula_1()
        self.scene_7_sector_area_formula_2()
        self.scene_8_comprehensive_example()
        self.scene_9_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一计算和验证"""
        # ========== 基准参数 ==========
        self.center = np.array([0, 1.5, 0])  # 圆心位置
        self.radius = 2.0                     # 半径
        self.angle_deg = 60                   # 圆心角（度）
        self.angle_rad = np.radians(self.angle_deg)  # 圆心角（弧度）
        
        # ========== 派生点（精确计算）==========
        # 弧起点（水平向右）
        self.arc_start = self.center + self.radius * RIGHT
        
        # 弧终点（60度方向）
        self.arc_end = self.center + self.radius * np.array([
            np.cos(self.angle_rad),
            np.sin(self.angle_rad),
            0
        ])
        
        # 弧中点（30度方向）
        mid_angle = self.angle_rad / 2
        self.arc_mid = self.center + self.radius * np.array([
            np.cos(mid_angle),
            np.sin(mid_angle),
            0
        ])
        
        # ========== 计算值 ==========
        # 弧长: l = nπr/180
        self.arc_length = (self.angle_deg * PI * self.radius) / 180
        
        # 扇形面积: S = nπr²/360
        self.sector_area = (self.angle_deg * PI * self.radius**2) / 360
        
        # 验证公式2: S = lr/2
        self.sector_area_verify = (self.arc_length * self.radius) / 2
        
        # ========== 验证几何计算 ==========
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证弧端点到圆心的距离
        dist_start = np.linalg.norm(self.arc_start - self.center)
        dist_end = np.linalg.norm(self.arc_end - self.center)
        
        assert abs(dist_start - self.radius) < epsilon, f"弧起点距离错误: {dist_start}"
        assert abs(dist_end - self.radius) < epsilon, f"弧终点距离错误: {dist_end}"
        
        # 验证两个面积公式结果一致
        assert abs(self.sector_area - self.sector_area_verify) < epsilon, \
            f"面积公式不一致: {self.sector_area} vs {self.sector_area_verify}"
        
        # 验证角度范围
        assert 0 < self.angle_deg < 180, f"圆心角应在0-180度之间: {self.angle_deg}"
        
        print("✓ 几何验证通过")
        print(f"  - 弧长: {self.arc_length:.4f}")
        print(f"  - 扇形面积: {self.sector_area:.4f}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 - 披萨问题"""
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "切一块披萨",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 披萨扇形（60度，红色填充）
        pizza_sector = Sector(
            arc_center=self.center,
            radius=self.radius,
            angle=self.angle_rad,
            start_angle=0,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.7,
            stroke_width=4
        )
        
        self.play(Create(pizza_sector), run_time=1.0)
        
        # 问题文字
        question = VGroup(
            Text("边缘有多长？", font="PingFang SC", font_size=32, color=WHITE),
            Text("面积是多少？", font="PingFang SC", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 4)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            FadeOut(pizza_sector),
            run_time=0.6
        )
    
    def scene_2_central_angle(self):
        """场景2: 圆心角介绍"""
        # 标题
        title = Text(
            "圆心角",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 圆
        circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        self.play(Create(circle), run_time=1.0)
        
        # 圆心点
        center_dot = Dot(self.center, color=self.COLOR_HIGHLIGHT, radius=0.08)
        center_label = Text(
            "O", 
            font="PingFang SC", 
            font_size=24, 
            color=WHITE
        ).next_to(center_dot, DOWN, buff=0.15)
        
        self.play(
            Flash(center_dot, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            FadeIn(center_dot),
            run_time=0.3
        )
        self.play(Write(center_label), run_time=0.3)
        
        # 两条半径
        radius_1 = Line(
            self.center,
            self.arc_start,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        radius_2 = Line(
            self.center,
            self.arc_end,
            color=self.COLOR_SECONDARY,
            stroke_width=4
        )
        
        self.play(
            GrowFromPoint(radius_1, self.center),
            GrowFromPoint(radius_2, self.center),
            run_time=0.8
        )
        
        # 角弧 - 使用 Angle.from_three_points
        # 注意：从 arc_start 到 arc_end 是逆时针，角度 < 180°，使用默认参数
        angle_arc = Angle.from_three_points(
            self.arc_start,
            self.center,
            self.arc_end,
            radius=0.5,
            color=self.COLOR_HIGHLIGHT,
            other_angle=False  # 逆时针方向
        )
        
        self.play(Create(angle_arc), run_time=0.6)
        
        # 角度标签
        angle_label = MathTex(
            r"n^\circ",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(
            self.center + 0.8 * np.array([
                np.cos(self.angle_rad / 2),
                np.sin(self.angle_rad / 2),
                0
            ])
        )
        
        self.play(Write(angle_label), run_time=0.5)
        
        # 定义文字
        definition = Text(
            "顶点在圆心的角",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.wait(1.5)
        
        # 清理（保留圆和半径用于下一场景）
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.4
        )
        
        # 保存元素供后续使用
        self.circle = circle
        self.radius_1 = radius_1
        self.radius_2 = radius_2
        self.angle_arc = angle_arc
        self.angle_label = angle_label
        self.center_dot = center_dot
        self.center_label = center_label
    
    def scene_3_arc_length_formula(self):
        """场景3: 弧长公式推导"""
        # 标题
        title = Text(
            "弧长公式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 圆周长公式
        formula_circumference = MathTex(
            r"C = 2\pi r",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3.5)
        
        circ_label = Text(
            "(圆周长)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(formula_circumference, RIGHT, buff=0.3)
        
        self.play(Write(formula_circumference), FadeIn(circ_label), run_time=1.0)
        self.wait(0.8)
        
        # 高亮整个圆周
        full_circle_highlight = Circle(
            radius=self.radius,
            color=self.COLOR_SECONDARY,
            stroke_width=6
        ).move_to(self.center)
        
        self.play(
            Create(full_circle_highlight),
            self.circle.animate.set_stroke(opacity=0.3),
            run_time=0.8
        )
        self.play(FadeOut(full_circle_highlight), self.circle.animate.set_stroke(opacity=1), run_time=0.3)
        
        # 比例关系说明
        proportion_text = Text(
            "弧长与周长的比例 = 圆心角与360°的比例",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(proportion_text), run_time=0.6)
        
        # 比例公式
        proportion_formula = MathTex(
            r"\frac{l}{2\pi r}", r"=", r"\frac{n^\circ}{360^\circ}",
            font_size=34
        ).move_to(UP * 1.2)
        
        proportion_formula[0].set_color(self.COLOR_PRIMARY)
        proportion_formula[2].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(proportion_formula), run_time=1.2)
        self.wait(1.0)
        
        # 推导箭头
        arrow = Arrow(
            UP * 0.5,
            DOWN * 0.5,
            color=self.COLOR_FORMULA,
            buff=0.1
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 弧长公式
        arc_length_formula = MathTex(
            r"l", r"=", r"\frac{n\pi r}{180}",
            font_size=42
        ).move_to(DOWN * 1.5)
        
        arc_length_formula[0].set_color(self.COLOR_PRIMARY)
        arc_length_formula[2].set_color(self.COLOR_FORMULA)
        
        # 添加边框强调
        formula_box = SurroundingRectangle(
            arc_length_formula,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(arc_length_formula), run_time=1.2)
        self.play(Create(formula_box), run_time=0.5)
        self.play(Indicate(arc_length_formula, scale_factor=1.1), run_time=0.8)
        self.wait(2.0)
        
        # 清理并保留公式在顶部
        formula_small = VGroup(arc_length_formula, formula_box).copy()
        formula_small.scale(0.6).move_to(UP * 6.5 + RIGHT * 2)
        
        self.play(
            FadeOut(title),
            FadeOut(formula_circumference),
            FadeOut(circ_label),
            FadeOut(proportion_text),
            FadeOut(proportion_formula),
            FadeOut(arrow),
            Transform(VGroup(arc_length_formula, formula_box), formula_small),
            FadeOut(self.circle),
            FadeOut(self.radius_1),
            FadeOut(self.radius_2),
            FadeOut(self.angle_arc),
            FadeOut(self.angle_label),
            FadeOut(self.center_dot),
            FadeOut(self.center_label),
            run_time=0.6
        )
        
        # 保存小公式供后续参考
        self.arc_formula_small = formula_small
    
    def scene_4_arc_length_example(self):
        """场景4: 弧长示例计算"""
        # 标题
        title = Text(
            "例题：计算弧长",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 新的扇形（用于示例）
        example_center = self.center + DOWN * 0.5
        example_radius = 2.0
        example_angle = 60
        
        sector = Sector(
            arc_center=example_center,
            radius=example_radius,
            angle=np.radians(example_angle),
            start_angle=0,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.5,
            stroke_width=4
        )
        
        self.play(Create(sector), run_time=1.0)
        
        # 标注半径
        radius_line = Line(
            example_center,
            example_center + example_radius * RIGHT,
            color=self.COLOR_SECONDARY,
            stroke_width=3
        )
        
        radius_label = MathTex(
            r"r = 2",
            font_size=28,
            color=WHITE
        ).next_to(radius_line, DOWN, buff=0.1)
        
        self.play(Create(radius_line), Write(radius_label), run_time=0.5)
        
        # 标注角度
        angle_label = MathTex(
            r"n = 60^\circ",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(example_center + 0.7 * np.array([0.8, 0.4, 0]))
        
        self.play(Write(angle_label), run_time=0.5)
        
        # 计算过程
        calculation = VGroup(
            MathTex(r"l", r"=", r"\frac{60 \times \pi \times 2}{180}", font_size=32),
            MathTex(r"=", r"\frac{120\pi}{180}", font_size=32),
            MathTex(r"=", r"\frac{2\pi}{3}", font_size=32),
            MathTex(r"\approx", r"2.09", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 3.5)
        
        calculation[0][0].set_color(self.COLOR_PRIMARY)
        calculation[3][1].set_color(self.COLOR_FORMULA)
        
        # 逐步展示计算
        self.play(Write(calculation[0]), run_time=1.0)
        self.wait(0.3)
        self.play(Write(calculation[1]), run_time=0.8)
        self.wait(0.3)
        self.play(Write(calculation[2]), run_time=0.8)
        self.wait(0.3)
        
        # 结果高亮
        result_box = SurroundingRectangle(
            calculation[3],
            color=self.COLOR_FORMULA,
            buff=0.1
        )
        
        self.play(Write(calculation[3]), Create(result_box), run_time=0.6)
        self.play(Indicate(calculation[3], scale_factor=1.15), run_time=0.6)
        
        # 在扇形上标注弧长
        arc_end = example_center + example_radius * np.array([
            np.cos(np.radians(example_angle)),
            np.sin(np.radians(example_angle)),
            0
        ])
        
        arc_brace = Brace(
            Line(example_center + example_radius * RIGHT, arc_end),
            direction=UP * 0.5 + RIGHT * 0.5,
            buff=0.1,
            color=self.COLOR_PRIMARY
        )
        
        arc_length_label = MathTex(
            r"l \approx 2.09",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(arc_brace, UP * 0.5 + RIGHT * 0.5, buff=0.05)
        
        self.play(
            FadeIn(arc_brace),
            Write(arc_length_label),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sector),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(angle_label),
            FadeOut(calculation),
            FadeOut(result_box),
            FadeOut(arc_brace),
            FadeOut(arc_length_label),
            run_time=0.6
        )
    
    def scene_5_sector_definition(self):
        """场景5: 扇形定义"""
        # 标题
        title = Text(
            "什么是扇形？",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 扇形
        sector_center = self.center
        sector = Sector(
            arc_center=sector_center,
            radius=self.radius,
            angle=self.angle_rad,
            start_angle=0,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.6,
            stroke_width=4
        )
        
        self.play(FadeIn(sector, scale=0.8), run_time=0.6)
        
        # 依次高亮各部分
        # 半径1
        r1 = Line(sector_center, self.arc_start, color=YELLOW, stroke_width=6)
        label_r1 = Text("半径", font="PingFang SC", font_size=24, color=YELLOW).next_to(r1, DOWN, buff=0.1)
        
        self.play(Create(r1), run_time=0.5)
        self.play(Write(label_r1), run_time=0.3)
        self.wait(0.3)
        self.play(FadeOut(r1), FadeOut(label_r1), run_time=0.3)
        
        # 半径2
        r2 = Line(sector_center, self.arc_end, color=YELLOW, stroke_width=6)
        label_r2 = Text("半径", font="PingFang SC", font_size=24, color=YELLOW).next_to(r2, LEFT, buff=0.1)
        
        self.play(Create(r2), run_time=0.5)
        self.play(Write(label_r2), run_time=0.3)
        self.wait(0.3)
        self.play(FadeOut(r2), FadeOut(label_r2), run_time=0.3)
        
        # 弧
        arc_highlight = Arc(
            radius=self.radius,
            start_angle=0,
            angle=self.angle_rad,
            arc_center=sector_center,
            color=YELLOW,
            stroke_width=8
        )
        label_arc = Text("弧", font="PingFang SC", font_size=24, color=YELLOW).move_to(
            sector_center + (self.radius + 0.5) * np.array([
                np.cos(self.angle_rad / 2),
                np.sin(self.angle_rad / 2),
                0
            ])
        )
        
        self.play(Create(arc_highlight), run_time=0.5)
        self.play(Write(label_arc), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(arc_highlight), FadeOut(label_arc), run_time=0.3)
        
        # 定义文字
        definition = Text(
            "扇形 = 两条半径 + 一段弧",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        definition_box = SurroundingRectangle(definition, color=self.COLOR_HIGHLIGHT, buff=0.2)
        
        self.play(FadeIn(definition), Create(definition_box), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(definition_box),
            FadeOut(sector),
            run_time=0.6
        )
    
    def scene_6_sector_area_formula_1(self):
        """场景6: 扇形面积公式1推导"""
        # 标题
        title = Text(
            "扇形面积公式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 圆面积公式
        formula_circle = MathTex(
            r"S_{\text{circle}} = \pi r^2",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3.5)
        
        circle_label = Text(
            "(圆面积)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(formula_circle, RIGHT, buff=0.3)
        
        self.play(Write(formula_circle), FadeIn(circle_label), run_time=1.0)
        self.wait(0.8)
        
        # 比例关系
        proportion_text = Text(
            "扇形面积与圆面积的比例 = 圆心角与360°的比例",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(proportion_text), run_time=0.6)
        
        # 比例公式
        proportion_formula = MathTex(
            r"\frac{S}{{\pi r^2}}", r"=", r"\frac{n^\circ}{360^\circ}",
            font_size=34
        ).move_to(UP * 1.2)
        
        proportion_formula[0].set_color(self.COLOR_PRIMARY)
        proportion_formula[2].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(proportion_formula), run_time=1.2)
        self.wait(1.0)
        
        # 推导箭头
        arrow = Arrow(UP * 0.5, DOWN * 0.5, color=self.COLOR_FORMULA, buff=0.1)
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 扇形面积公式
        sector_area_formula = MathTex(
            r"S", r"=", r"\frac{n\pi r^2}{360}",
            font_size=42
        ).move_to(DOWN * 1.5)
        
        sector_area_formula[0].set_color(self.COLOR_PRIMARY)
        sector_area_formula[2].set_color(self.COLOR_FORMULA)
        
        # 边框
        formula_box = SurroundingRectangle(
            sector_area_formula,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(sector_area_formula), run_time=1.2)
        self.play(Create(formula_box), run_time=0.5)
        self.play(Indicate(sector_area_formula, scale_factor=1.1), run_time=0.8)
        self.wait(2.0)
        
        # 保存公式
        self.sector_formula_1 = VGroup(sector_area_formula, formula_box)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_circle),
            FadeOut(circle_label),
            FadeOut(proportion_text),
            FadeOut(proportion_formula),
            FadeOut(arrow),
            run_time=0.6
        )
    
    def scene_7_sector_area_formula_2(self):
        """场景7: 扇形面积公式2（弧长关系式）"""
        # 标题
        title = Text(
            "第二个公式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(
            self.sector_formula_1.animate.scale(0.7).move_to(UP * 3.5),
            FadeIn(title),
            run_time=0.6
        )
        
        # 说明
        explanation = Text(
            "利用弧长公式，可以得到另一个形式",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(explanation), run_time=0.6)
        
        # 弧长公式回顾
        arc_formula_recall = MathTex(
            r"l = \frac{n\pi r}{180}",
            font_size=30,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.5)
        
        hint = Text(
            "即：", 
            font="PingFang SC", 
            font_size=24, 
            color=GRAY_A
        ).next_to(arc_formula_recall, LEFT, buff=0.3)
        
        hint2 = MathTex(
            r"n\pi r = 180l",
            font_size=30,
            color=self.COLOR_SECONDARY
        ).next_to(arc_formula_recall, RIGHT, buff=0.8)
        
        self.play(Write(arc_formula_recall), FadeIn(hint), run_time=0.8)
        self.wait(0.3)
        self.play(Write(hint2), run_time=0.8)
        
        # 代入过程
        substitution = Text(
            "代入原公式：",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(substitution), run_time=0.5)
        
        # 推导步骤
        derivation = VGroup(
            MathTex(r"S = \frac{n\pi r^2}{360}", font_size=32),
            MathTex(r"= \frac{(n\pi r) \cdot r}{360}", font_size=32),
            MathTex(r"= \frac{180l \cdot r}{360}", font_size=32),
            MathTex(r"= \frac{lr}{2}", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 1.5)
        
        derivation[2][0][3:6].set_color(self.COLOR_SECONDARY)  # 高亮 180l
        
        for i, step in enumerate(derivation):
            self.play(Write(step), run_time=0.6 if i < 3 else 1.0)
            if i < len(derivation) - 1:
                self.wait(0.2)
        
        # 最终公式强调
        final_formula = MathTex(
            r"S", r"=", r"\frac{1}{2}", r"lr",
            font_size=44
        ).move_to(DOWN * 4)
        
        final_formula[0].set_color(self.COLOR_PRIMARY)
        final_formula[2:].set_color(self.COLOR_FORMULA)
        
        formula_box_2 = SurroundingRectangle(
            final_formula,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(final_formula), Create(formula_box_2), run_time=1.0)
        self.play(Indicate(final_formula, scale_factor=1.15), run_time=0.8)
        self.wait(1.5)
        
        # 保存两个公式并排显示
        formula_group = VGroup(
            self.sector_formula_1.copy(),
            VGroup(final_formula, formula_box_2).copy()
        ).arrange(DOWN, buff=0.4).scale(0.5).move_to(UP * 6.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(arc_formula_recall),
            FadeOut(hint),
            FadeOut(hint2),
            FadeOut(substitution),
            FadeOut(derivation),
            FadeOut(self.sector_formula_1),
            Transform(VGroup(final_formula, formula_box_2), formula_group[1]),
            run_time=0.6
        )
        
        self.formula_group = formula_group
    
    def scene_8_comprehensive_example(self):
        """场景8: 综合示例"""
        # 标题
        title = Text(
            "综合练习",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 题目
        problem = VGroup(
            Text("已知：", font="PingFang SC", font_size=28, color=GRAY_A),
            MathTex(r"r = 3,\ n = 120^\circ", font_size=28, color=WHITE)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4.5)
        
        question = Text(
            "求：弧长 l 和扇形面积 S",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).next_to(problem, DOWN, buff=0.3)
        
        self.play(FadeIn(problem), FadeIn(question), run_time=0.8)
        
        # 扇形图示（120度）
        example_center = np.array([0, 1.5, 0])
        example_radius = 1.8
        example_angle = 120
        
        sector = Sector(
            arc_center=example_center,
            radius=example_radius,
            angle=np.radians(example_angle),
            start_angle=0,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.5,
            stroke_width=3
        ).scale(0.8)
        
        self.play(Create(sector), run_time=1.0)
        
        # 计算弧长
        step1_title = Text(
            "① 计算弧长：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 0.5 + LEFT * 3)
        
        step1_calc = MathTex(
            r"l = \frac{120 \times \pi \times 3}{180} = 2\pi",
            font_size=28
        ).next_to(step1_title, RIGHT, buff=0.3)
        step1_calc[0][14:].set_color(self.COLOR_FORMULA)
        
        self.play(Write(step1_title), run_time=0.4)
        self.play(Write(step1_calc), run_time=0.8)
        
        result1_box = SurroundingRectangle(step1_calc[0][14:], color=self.COLOR_FORMULA, buff=0.05)
        self.play(Create(result1_box), run_time=0.3)
        self.wait(0.3)
        
        # 计算面积（公式1）
        step2_title = Text(
            "② 计算面积（公式1）：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1.8 + LEFT * 2.2)
        
        step2_calc = MathTex(
            r"S = \frac{120 \times \pi \times 9}{360} = 3\pi",
            font_size=28
        ).next_to(step2_title, RIGHT, buff=0.3)
        step2_calc[0][16:].set_color(self.COLOR_FORMULA)
        
        self.play(Write(step2_title), run_time=0.4)
        self.play(Write(step2_calc), run_time=0.8)
        
        result2_box = SurroundingRectangle(step2_calc[0][16:], color=self.COLOR_FORMULA, buff=0.05)
        self.play(Create(result2_box), run_time=0.3)
        self.wait(0.3)
        
        # 验证（公式2）
        step3_title = Text(
            "③ 验证（公式2）：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 3.2 + LEFT * 2.5)
        
        step3_calc = MathTex(
            r"S = \frac{2\pi \times 3}{2} = 3\pi",
            font_size=28
        ).next_to(step3_title, RIGHT, buff=0.3)
        step3_calc[0][10:].set_color(self.COLOR_FORMULA)
        
        self.play(Write(step3_title), run_time=0.4)
        self.play(Write(step3_calc), run_time=0.8)
        
        # 一致性标记
        checkmark = Text(
            "✓ 结果一致！",
            font="PingFang SC",
            font_size=28,
            color=GREEN,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(
            FadeIn(checkmark, scale=1.2),
            Indicate(checkmark, scale_factor=1.2),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in [
                title, problem, question, sector,
                step1_title, step1_calc, result1_box,
                step2_title, step2_calc, result2_box,
                step3_title, step3_calc, checkmark
            ]],
            run_time=0.6
        )
    
    def scene_9_outro(self):
        """场景9: 结尾关注"""
        # 总结卡片
        summary_title = Text(
            "知识总结",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4)
        
        # 三个公式
        formulas = VGroup(
            VGroup(
                Text("弧长：", font="PingFang SC", font_size=26, color=GRAY_A),
                MathTex(r"l = \frac{n\pi r}{180}", font_size=32, color=self.COLOR_FORMULA)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("面积1：", font="PingFang SC", font_size=26, color=GRAY_A),
                MathTex(r"S = \frac{n\pi r^2}{360}", font_size=32, color=self.COLOR_FORMULA)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("面积2：", font="PingFang SC", font_size=26, color=GRAY_A),
                MathTex(r"S = \frac{lr}{2}", font_size=32, color=self.COLOR_FORMULA)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.8)
        
        for formula in formulas:
            self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.5)
            self.wait(0.1)
        
        # 公式闪烁
        self.play(
            *[Flash(f[1], color=self.COLOR_HIGHLIGHT, flash_radius=0.5) for f in formulas],
            run_time=0.6
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            self.author_info.animate.become(author_large),
            FadeIn(author_id, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(
            Write(follow_text),
            follow_text.animate.scale(1.1),
            run_time=0.8
        )
        
        # 圆形装饰
        circles = VGroup(*[
            Circle(radius=0.2, color=self.COLOR_PRIMARY, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in [
                summary_title, formulas, self.author_info, 
                author_id, follow_text, circles
            ]],
            run_time=1.0
        )


# 运行命令:
# manim -pql arc_length_sector_area.py ArcLengthAndSectorArea  # 快速预览
# manim -qh arc_length_sector_area.py ArcLengthAndSectorArea   # 高质量 1080p
# manim -qk arc_length_sector_area.py ArcLengthAndSectorArea   # 4K质量