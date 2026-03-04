"""
两角和与差的三角函数 - Sum and Difference of Angles
使用 Manim 创建的高一数学教学视频

内容: 两角和差的余弦、正弦、正切公式及几何证明
目标观众: 高一学生
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


class SumDifferenceAngles(Scene):
    """
    两角和与差的三角函数教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 单位圆介绍
    3. 角α和角β的可视化
    4. cos(α-β) 几何证明
    5. cos(α+β) 公式
    6. sin(α±β) 公式
    7. tan(α±β) 公式
    8. 公式总结 + 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ALPHA = "#e74c3c"          # 红色 - 角α
        self.COLOR_BETA = "#3498db"           # 蓝色 - 角β
        self.COLOR_SUM = "#2ecc71"            # 绿色 - 和角
        self.COLOR_DIFF = "#9b59b6"           # 紫色 - 差角
        self.COLOR_UNIT_CIRCLE = WHITE        # 白色 - 单位圆
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_FORMULA = "#f39c12"        # 橙色 - 公式
        self.COLOR_WARNING = "#e67e22"        # 橙红色 - 警告
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_unit_circle()
        self.show_angles_visualization()
        self.show_cosine_difference_proof()
        self.show_cosine_sum()
        self.show_sine_formulas()
        self.show_tangent_formulas()
        self.show_summary_outro()
    
    def setup_geometry(self):
        """初始化单位圆和关键角度"""
        # 单位圆配置
        self.circle_center = DOWN * 1.0
        self.radius = 1.8
        
        # 示例角度（使用精确值避免浮点误差）
        self.alpha = PI / 4      # 45°
        self.beta = PI / 6       # 30°
        self.alpha_plus_beta = self.alpha + self.beta   # 75° = 5π/12
        self.alpha_minus_beta = self.alpha - self.beta  # 15° = π/12
        
        # 计算关键点位置（在单位圆上）
        self.point_A = self.circle_center + self.radius * np.array([
            np.cos(self.alpha),
            np.sin(self.alpha),
            0
        ])
        
        self.point_B = self.circle_center + self.radius * np.array([
            np.cos(self.beta),
            np.sin(self.beta),
            0
        ])
        
        self.point_C = self.circle_center + self.radius * np.array([
            np.cos(self.alpha_plus_beta),
            np.sin(self.alpha_plus_beta),
            0
        ])
        
        self.point_D = self.circle_center + self.radius * np.array([
            np.cos(self.alpha_minus_beta),
            np.sin(self.alpha_minus_beta),
            0
        ])
        
        # x轴正方向参考点
        self.point_X = self.circle_center + self.radius * RIGHT
        
        # 验证几何
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证所有点在单位圆上
        points = {
            'A': self.point_A,
            'B': self.point_B,
            'C': self.point_C,
            'D': self.point_D,
            'X': self.point_X
        }
        
        print("✓ 几何验证:")
        for name, point in points.items():
            dist = np.linalg.norm(point - self.circle_center)
            if abs(dist - self.radius) < epsilon:
                print(f"  ✓ 点{name}在单位圆上: r = {dist:.6f}")
            else:
                print(f"  ✗ 点{name}不在单位圆上: r = {dist:.6f} (应为 {self.radius})")
        
        # 验证角度
        print(f"\n  角度验证:")
        print(f"  α = {np.degrees(self.alpha):.1f}° = π/{4})")
        print(f"  β = {np.degrees(self.beta):.1f}° = π/{6}")
        print(f"  α+β = {np.degrees(self.alpha_plus_beta):.1f}°")
        print(f"  α-β = {np.degrees(self.alpha_minus_beta):.1f}°")
        
        # 验证边界
        y_max = self.circle_center[1] + self.radius
        y_min = self.circle_center[1] - self.radius
        print(f"\n  单位圆边界:")
        print(f"  中心: y = {self.circle_center[1]:.1f}")
        print(f"  范围: y ∈ [{y_min:.1f}, {y_max:.1f}]")
        print(f"  安全检查: {'✓' if y_min >= -7 and y_max <= 7 else '✗'}")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        opening_group = VGroup()
        
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        opening_group.add(self.author_info)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = MathTex(
            r"\cos(45^\circ + 30^\circ) = \; ?",
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        opening_group.add(hook_question)
        
        self.play(Write(hook_question), run_time=1.2)
        
        # 提示文字
        hint_text = Text(
            "能直接计算吗？",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).next_to(hook_question, DOWN, buff=0.8)
        opening_group.add(hint_text)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理开场除作者信息外的所有元素
        opening_group.remove(self.author_info)
        self.play(FadeOut(opening_group), run_time=0.5)
    
    def show_unit_circle(self):
        """场景2: 单位圆介绍"""
        unit_circle_group = VGroup()
        
        # 标题
        title = Text(
            "单位圆",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        unit_circle_group.add(title)
        
        self.play(FadeIn(title), run_time=0.6)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15
            }
        ).move_to(self.circle_center)
        unit_circle_group.add(axes)
        
        self.play(Create(axes), run_time=1.0)
        
        # 单位圆
        unit_circle = Circle(
            radius=self.radius,
            color=self.COLOR_UNIT_CIRCLE,
            stroke_width=2.5
        ).move_to(self.circle_center)
        unit_circle_group.add(unit_circle)
        
        self.play(Create(unit_circle), run_time=1.5)
        
        # 标注关键角度
        # 0° (右)
        label_0 = MathTex(r"0^\circ", font_size=20).next_to(
            self.circle_center + self.radius * RIGHT, RIGHT, buff=0.15
        )
        
        # 90° (上)
        label_90 = MathTex(r"90^\circ", font_size=20).next_to(
            self.circle_center + self.radius * UP, UP, buff=0.15
        )
        
        # 180° (左)
        label_180 = MathTex(r"180^\circ", font_size=20).next_to(
            self.circle_center + self.radius * LEFT, LEFT, buff=0.15
        )
        
        # 270° (下)
        label_270 = MathTex(r"270^\circ", font_size=20).next_to(
            self.circle_center + self.radius * DOWN, DOWN, buff=0.15
        )
        
        angle_labels = VGroup(label_0, label_90, label_180, label_270)
        unit_circle_group.add(angle_labels)
        
        self.play(
            FadeIn(label_0),
            FadeIn(label_90),
            FadeIn(label_180),
            FadeIn(label_270),
            run_time=1.0
        )
        
        # 说明文字
        explanation = Text(
            "半径为1的圆",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.5)
        unit_circle_group.add(explanation)
        
        self.play(Write(explanation), run_time=0.8)
        self.wait(1.0)
        
        # 清理标题和说明，保留坐标轴、单位圆和角度标签
        unit_circle_group.remove(title, explanation)
        self.play(FadeOut(title, explanation), run_time=0.4)
        
        # 保存元素供后续使用
        self.axes = axes
        self.unit_circle = unit_circle
        self.angle_labels = angle_labels
        self.unit_circle_core = VGroup(axes, unit_circle, angle_labels)
    
    def show_angles_visualization(self):
        """场景3: 角α和角β的可视化"""
        angles_group = VGroup()
        
        # 标题
        title = Text(
            "两个角",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        angles_group.add(title)
        
        self.play(Write(title), run_time=0.6)
        
        # 角α = 45°
        angle_alpha = Angle.from_three_points(
            self.point_X,
            self.circle_center,
            self.point_A,
            radius=0.5,
            other_angle=False,
            color=self.COLOR_ALPHA,
            stroke_width=2
        )
        angles_group.add(angle_alpha)
        
        self.play(Create(angle_alpha), run_time=1.0)
        
        # 半径 OA
        radius_OA = Line(
            self.circle_center,
            self.point_A,
            color=self.COLOR_ALPHA,
            stroke_width=2.5
        )
        angles_group.add(radius_OA)
        
        self.play(Create(radius_OA), run_time=0.6)
        
        # 点A
        point_A_dot = Dot(
            self.point_A,
            color=self.COLOR_ALPHA,
            radius=0.08
        )
        angles_group.add(point_A_dot)
        
        label_alpha = MathTex(
            r"\alpha = 45^\circ",
            font_size=26,
            color=self.COLOR_ALPHA
        ).next_to(angle_alpha, RIGHT, buff=0.3).shift(UP * 0.2)
        angles_group.add(label_alpha)
        
        self.play(
            FadeIn(point_A_dot, scale=0.5),
            Write(label_alpha),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 角β = 30°
        angle_beta = Angle.from_three_points(
            self.point_X,
            self.circle_center,
            self.point_B,
            radius=0.4,
            other_angle=False,
            color=self.COLOR_BETA,
            stroke_width=2
        )
        angles_group.add(angle_beta)
        
        self.play(Create(angle_beta), run_time=1.0)
        
        # 半径 OB
        radius_OB = Line(
            self.circle_center,
            self.point_B,
            color=self.COLOR_BETA,
            stroke_width=2.5
        )
        angles_group.add(radius_OB)
        
        self.play(Create(radius_OB), run_time=0.6)
        
        # 点B
        point_B_dot = Dot(
            self.point_B,
            color=self.COLOR_BETA,
            radius=0.08
        )
        angles_group.add(point_B_dot)
        
        label_beta = MathTex(
            r"\beta = 30^\circ",
            font_size=26,
            color=self.COLOR_BETA
        ).next_to(angle_beta, RIGHT, buff=0.2).shift(DOWN * 0.1)
        angles_group.add(label_beta)
        
        self.play(
            FadeIn(point_B_dot, scale=0.5),
            Write(label_beta),
            run_time=0.8
        )
        
        # 坐标标注
        coord_A = MathTex(
            r"(\cos\alpha, \sin\alpha)",
            font_size=18,
            color=self.COLOR_ALPHA
        ).next_to(point_A_dot, UR, buff=0.15)
        angles_group.add(coord_A)
        
        coord_B = MathTex(
            r"(\cos\beta, \sin\beta)",
            font_size=18,
            color=self.COLOR_BETA
        ).next_to(point_B_dot, UR, buff=0.15)
        angles_group.add(coord_B)
        
        self.play(
            FadeIn(coord_A),
            FadeIn(coord_B),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理标题和坐标标注，保留角度相关元素
        angles_group.remove(title, coord_A, coord_B)
        self.play(FadeOut(title, coord_A, coord_B), run_time=0.4)
        
        # 保存元素
        self.angle_elements = VGroup(
            angle_alpha, angle_beta, radius_OA, radius_OB,
            point_A_dot, point_B_dot, label_alpha, label_beta
        )
    
    def show_cosine_difference_proof(self):
        """场景4: cos(α-β) 几何证明（简化版）"""
        cos_diff_group = VGroup()
        
        # 标题
        title = Text(
            "余弦差角公式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_DIFF
        ).move_to(UP * 6)
        cos_diff_group.add(title)
        
        self.play(Write(title), run_time=0.6)
        
        # 连线 AB
        line_AB = Line(
            self.point_A,
            self.point_B,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        cos_diff_group.add(line_AB)
        
        self.play(Create(line_AB), run_time=0.8)
        
        # 说明文字
        explanation = Text(
            "利用两点距离公式",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5)
        cos_diff_group.add(explanation)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # 距离公式（简化展示）
        distance_formula = MathTex(
            r"|AB|^2 = (\cos\alpha - \cos\beta)^2 + (\sin\alpha - \sin\beta)^2",
            font_size=20
        ).move_to(UP * 4)
        cos_diff_group.add(distance_formula)
        
        self.play(Write(distance_formula), run_time=1.5)
        self.wait(1.0)
        
        # 展开
        expanded = MathTex(
            r"= 2 - 2(\cos\alpha\cos\beta + \sin\alpha\sin\beta)",
            font_size=20
        ).next_to(distance_formula, DOWN, buff=0.3)
        cos_diff_group.add(expanded)
        
        self.play(Write(expanded), run_time=1.2)
        self.wait(0.8)
        
        # 结论
        conclusion = MathTex(
            r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta",
            font_size=28,
            color=self.COLOR_DIFF
        ).move_to(UP * 2.5)
        cos_diff_group.add(conclusion)
        
        conclusion_box = SurroundingRectangle(
            conclusion,
            color=self.COLOR_DIFF,
            buff=0.2,
            corner_radius=0.1
        )
        cos_diff_group.add(conclusion_box)
        
        self.play(
            Write(conclusion),
            Create(conclusion_box),
            run_time=1.2
        )
        
        self.wait(1.5)
        
        # 清理当前场景所有元素
        self.play(FadeOut(cos_diff_group), run_time=0.5)
    
    def show_cosine_sum(self):
        """场景5: 余弦和角公式"""
        cos_sum_group = VGroup()
        
        # 标题
        title = Text(
            "余弦和角公式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_SUM
        ).move_to(UP * 6)
        cos_sum_group.add(title)
        
        self.play(Write(title), run_time=0.6)
        
        # 说明
        explanation = Text(
            "利用 cos(α+β) = cos[α-(-β)]",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5)
        cos_sum_group.add(explanation)
        
        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(1.0)
        
        # 推导步骤
        step1 = MathTex(
            r"\cos(\alpha + \beta) = \cos\alpha\cos(-\beta) + \sin\alpha\sin(-\beta)",
            font_size=22
        ).move_to(UP * 3.8)
        cos_sum_group.add(step1)
        
        self.play(Write(step1), run_time=1.5)
        self.wait(0.8)
        
        # 最终公式
        final_formula = MathTex(
            r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta",
            font_size=28,
            color=self.COLOR_SUM
        ).move_to(UP * 2.5)
        cos_sum_group.add(final_formula)
        
        final_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_SUM,
            buff=0.2,
            corner_radius=0.1
        )
        cos_sum_group.add(final_box)
        
        self.play(
            Write(final_formula),
            Create(final_box),
            run_time=1.2
        )
        
        self.wait(1.5)
        
        # 清理当前场景所有元素
        self.play(FadeOut(cos_sum_group), run_time=0.5)
    
    def show_sine_formulas(self):
        """场景6: 正弦和差公式"""
        sine_group = VGroup()
        
        # 标题
        title = Text(
            "正弦和差公式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        sine_group.add(title)
        
        self.play(Write(title), run_time=0.6)
        
        # 说明
        explanation = Text(
            "利用诱导公式推导",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5)
        sine_group.add(explanation)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(0.8)
        
        # sin(α+β) 公式
        sin_sum = MathTex(
            r"\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta",
            font_size=26,
            color=self.COLOR_SUM
        ).move_to(UP * 3.5)
        sine_group.add(sin_sum)
        
        sin_sum_box = SurroundingRectangle(
            sin_sum,
            color=self.COLOR_SUM,
            buff=0.15,
            corner_radius=0.1
        )
        sine_group.add(sin_sum_box)
        
        self.play(
            Write(sin_sum),
            Create(sin_sum_box),
            run_time=1.2
        )
        
        self.wait(1.0)
        
        # sin(α-β) 公式
        sin_diff = MathTex(
            r"\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta",
            font_size=26,
            color=self.COLOR_DIFF
        ).move_to(UP * 2.2)
        sine_group.add(sin_diff)
        
        sin_diff_box = SurroundingRectangle(
            sin_diff,
            color=self.COLOR_DIFF,
            buff=0.15,
            corner_radius=0.1
        )
        sine_group.add(sin_diff_box)
        
        self.play(
            Write(sin_diff),
            Create(sin_diff_box),
            run_time=1.2
        )
        
        # 符号对比
        plus_sign = sin_sum[0][10]  # + 号
        minus_sign = sin_diff[0][10]  # - 号
        
        self.play(
            Indicate(plus_sign, color=YELLOW, scale_factor=1.5),
            Indicate(minus_sign, color=YELLOW, scale_factor=1.5),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理当前场景所有元素
        self.play(FadeOut(sine_group), run_time=0.5)
    
    def show_tangent_formulas(self):
        """场景7: 正切和差公式"""
        tangent_group = VGroup()
        
        # 标题
        title = Text(
            "正切和差公式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        tangent_group.add(title)
        
        self.play(Write(title), run_time=0.6)
        
        # tan(α+β) 公式
        tan_sum = MathTex(
            r"\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}",
            font_size=26,
            color=self.COLOR_SUM
        ).move_to(UP * 3.5)
        tangent_group.add(tan_sum)
        
        tan_sum_box = SurroundingRectangle(
            tan_sum,
            color=self.COLOR_SUM,
            buff=0.15,
            corner_radius=0.1
        )
        tangent_group.add(tan_sum_box)
        
        self.play(
            Write(tan_sum),
            Create(tan_sum_box),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # tan(α-β) 公式
        tan_diff = MathTex(
            r"\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}",
            font_size=26,
            color=self.COLOR_DIFF
        ).move_to(UP * 2)
        tangent_group.add(tan_diff)
        
        tan_diff_box = SurroundingRectangle(
            tan_diff,
            color=self.COLOR_DIFF,
            buff=0.15,
            corner_radius=0.1
        )
        tangent_group.add(tan_diff_box)
        
        self.play(
            Write(tan_diff),
            Create(tan_diff_box),
            run_time=1.5
        )
        
        self.wait(0.8)
        
        # 条件说明
        condition = Text(
            "* 要求分母不为0",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_WARNING
        ).move_to(UP * 0.5)
        tangent_group.add(condition)
        
        self.play(FadeIn(condition), run_time=0.5)
        
        self.wait(1.2)
        
        # 清理当前场景所有元素
        self.play(FadeOut(tangent_group), run_time=0.5)
    
    def show_summary_outro(self):
        """场景8: 公式总结 + 片尾"""
        summary_group = VGroup()
        
        # 先清理之前保留的所有几何元素
        self.play(
            FadeOut(self.unit_circle_core),
            FadeOut(self.angle_elements),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "两角和差公式总结",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        summary_group.add(title)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式列表（重新创建，清晰排列）
        formula_list = VGroup(
            MathTex(r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta", 
                   font_size=22, color=self.COLOR_DIFF),
            MathTex(r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta", 
                   font_size=22, color=self.COLOR_SUM),
            MathTex(r"\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta", 
                   font_size=22, color=self.COLOR_SUM),
            MathTex(r"\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta", 
                   font_size=22, color=self.COLOR_DIFF),
            MathTex(r"\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha\tan\beta}", 
                   font_size=22, color=self.COLOR_SUM),
            MathTex(r"\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha\tan\beta}", 
                   font_size=22, color=self.COLOR_DIFF),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 1.5)
        summary_group.add(formula_list)
        
        self.play(FadeIn(formula_list, shift=UP * 0.5), run_time=1.2)
        
        # 逐个高亮
        for formula in formula_list:
            self.play(Indicate(formula, color=YELLOW, scale_factor=1.1), run_time=0.4)
            self.wait(0.2)
        
        self.wait(1.0)
        
        # 淡出标题和公式列表
        summary_group.remove(title, formula_list)
        self.play(FadeOut(title, formula_list), run_time=0.6)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        summary_group.add(author_name)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 1)
        summary_group.add(author_id)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多三角函数技巧!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        summary_group.add(follow_text)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰图标 - 三角函数符号
        icons = VGroup(
            MathTex(r"\sin", font_size=40, color=self.COLOR_SUM),
            MathTex(r"\cos", font_size=40, color=self.COLOR_DIFF),
            MathTex(r"\tan", font_size=40, color=self.COLOR_FORMULA),
        ).arrange(RIGHT, buff=1.2).move_to(DOWN * 2.5)
        summary_group.add(icons)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        self.wait(1.0)
        
        # 全部淡出
        summary_group.add(self.author_info)
        self.play(FadeOut(summary_group), run_time=1.0)


# 渲染命令:
# manim -pql sum_difference_angles.py SumDifferenceAngles  # 快速预览
# manim -qh sum_difference_angles.py SumDifferenceAngles   # 高质量 1080p