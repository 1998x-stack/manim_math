"""
二倍角与半角公式教学动画 - Double Angle and Half Angle Formulas
使用 Manim 创建的高中三角函数教学视频

内容: 二倍角公式、半角公式、降幂公式的几何推导与可视化
目标观众: 高一学生 (第二学期)
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


class DoubleAngleFormulas(Scene):
    """
    二倍角与半角公式教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立单位圆基础
    3. 二倍角 sin 公式推导
    4. 二倍角 cos 公式展示
    5. 二倍角 tan 公式
    6. 半角公式推导
    7. 降幂公式与总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要角度α
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 二倍角2α
        self.COLOR_HALF_ANGLE = "#2ecc71"     # 绿色 - 半角α/2
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_CIRCLE = WHITE             # 白色 - 单位圆
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_unit_circle()
        self.show_double_angle_sin()
        self.show_double_angle_cos()
        self.show_double_angle_tan()
        self.show_half_angle()
        self.show_power_reduction_and_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的精确坐标"""
        # 基准参数
        self.OFFSET = UP * 1.5
        self.RADIUS = 1.8
        self.ALPHA = PI / 6  # 30度作为示例角度
        
        # 单位圆圆心
        self.center = self.OFFSET
        
        # 关键点的精确计算
        self.P_alpha = self.center + self.RADIUS * np.array([
            np.cos(self.ALPHA),
            np.sin(self.ALPHA),
            0
        ])
        
        self.P_2alpha = self.center + self.RADIUS * np.array([
            np.cos(2 * self.ALPHA),
            np.sin(2 * self.ALPHA),
            0
        ])
        
        self.P_half_alpha = self.center + self.RADIUS * np.array([
            np.cos(self.ALPHA / 2),
            np.sin(self.ALPHA / 2),
            0
        ])
        
        # 投影点
        self.P_alpha_x = self.center + np.array([
            self.RADIUS * np.cos(self.ALPHA),
            0,
            0
        ])
        
        self.P_alpha_y = self.center + np.array([
            0,
            self.RADIUS * np.sin(self.ALPHA),
            0
        ])
        
        # 验证几何
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证点在圆上
        dist_P_alpha = np.linalg.norm(self.P_alpha - self.center)
        dist_P_2alpha = np.linalg.norm(self.P_2alpha - self.center)
        dist_P_half = np.linalg.norm(self.P_half_alpha - self.center)
        
        assert abs(dist_P_alpha - self.RADIUS) < epsilon, f"点P_alpha不在圆上: {dist_P_alpha}"
        assert abs(dist_P_2alpha - self.RADIUS) < epsilon, f"点P_2alpha不在圆上: {dist_P_2alpha}"
        assert abs(dist_P_half - self.RADIUS) < epsilon, f"点P_half不在圆上: {dist_P_half}"
        
        print("✓ 几何验证通过")
    
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
        hook_line1 = Text(
            "你知道 sin²α + cos²α = 1",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 2)
        
        hook_line2 = Text(
            "那 sin 2α 等于多少?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(Write(hook_line1), run_time=1.0)
        self.play(Write(hook_line2), run_time=1.0)
        
        # 闪烁效果
        mystery = MathTex(r"?", font_size=80, color=self.COLOR_SECONDARY).move_to(DOWN * 2)
        self.play(FadeIn(mystery, scale=2), run_time=0.5)
        self.play(Flash(mystery, color=self.COLOR_SECONDARY, flash_radius=0.8), run_time=0.5)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(mystery),
            run_time=0.5
        )
    
    def show_unit_circle(self):
        """场景2: 建立单位圆基础"""
        # 标题
        title = Text(
            "单位圆与三角函数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 坐标轴
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1, 1, 1],
            x_length=6,
            y_length=3,
            axis_config={"color": GRAY_B, "include_tip": False, "include_numbers": False}
        ).move_to(self.center)
        
        self.play(Create(axes), run_time=1.0)
        
        # 单位圆
        circle = Circle(
            radius=self.RADIUS,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        self.play(Create(circle), run_time=1.2)
        
        # 角α的扇形
        angle_alpha_sector = Sector(
            arc_center=self.center,
            radius=self.RADIUS,
            angle=self.ALPHA,
            start_angle=0,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(Create(angle_alpha_sector), run_time=1.0)
        
        # 点P
        dot_P = Dot(self.P_alpha, color=self.COLOR_PRIMARY, radius=0.08)
        label_P = MathTex(r"P", font_size=24, color=WHITE).next_to(dot_P, UR, buff=0.1)
        
        self.play(FadeIn(dot_P, scale=0.5), Write(label_P), run_time=0.5)
        
        # 投影线
        proj_x = DashedLine(
            self.P_alpha,
            self.P_alpha_x,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        proj_y = DashedLine(
            self.P_alpha,
            self.center + np.array([self.P_alpha[0] - self.center[0], 0, 0]),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        
        # 标注 cosα 和 sinα
        label_cos = MathTex(r"\cos\alpha", font_size=22, color=self.COLOR_PRIMARY).next_to(
            (self.center + self.P_alpha_x) / 2, DOWN, buff=0.2
        )
        
        label_sin = MathTex(r"\sin\alpha", font_size=22, color=self.COLOR_PRIMARY).next_to(
            (self.P_alpha + self.P_alpha_x) / 2, RIGHT, buff=0.15
        )
        
        self.play(Write(label_cos), Write(label_sin), run_time=0.8)
        
        # 角度标注
        angle_label = MathTex(r"\alpha", font_size=24, color=self.COLOR_PRIMARY).move_to(
            self.center + np.array([0.5, 0.2, 0])
        )
        self.play(Write(angle_label), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理，但保留基本元素
        self.play(
            FadeOut(title),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(label_cos),
            FadeOut(label_sin),
            run_time=0.5
        )
        
        # 保存元素供后续使用
        self.axes = axes
        self.circle = circle
        self.angle_alpha_sector = angle_alpha_sector
        self.dot_P = dot_P
        self.label_P = label_P
        self.angle_label = angle_label
    
    def show_double_angle_sin(self):
        """场景3: 二倍角 sin 公式推导"""
        # 标题
        title = Text(
            "二倍角公式: sin 2α",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 角2α的扇形
        angle_2alpha_sector = Sector(
            arc_center=self.center,
            radius=self.RADIUS,
            angle=2 * self.ALPHA,
            start_angle=0,
            color=self.COLOR_SECONDARY,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        # 先让α角旋转复制一份
        self.play(
            self.angle_alpha_sector.animate.set_fill(opacity=0.15),
            run_time=0.5
        )
        
        self.play(Create(angle_2alpha_sector), run_time=1.2)
        
        # 点Q (2α对应的点)
        dot_Q = Dot(self.P_2alpha, color=self.COLOR_SECONDARY, radius=0.08)
        label_Q = MathTex(r"Q", font_size=24, color=WHITE).next_to(dot_Q, UR, buff=0.1)
        
        self.play(FadeIn(dot_Q, scale=0.5), Write(label_Q), run_time=0.5)
        
        # 角度标注2α
        angle_2alpha_label = MathTex(r"2\alpha", font_size=26, color=self.COLOR_SECONDARY).move_to(
            self.center + np.array([0.7, 0.3, 0])
        )
        self.play(Write(angle_2alpha_label), run_time=0.5)
        
        self.wait(0.5)
        
        # 公式推导区域(底部)
        formula_y = -4.5
        
        # 问题
        question = MathTex(
            r"\sin 2\alpha = ?",
            font_size=32,
            color=WHITE
        ).move_to(UP * formula_y)
        
        self.play(Write(question), run_time=0.8)
        self.wait(0.5)
        
        # 提示: 利用两角和公式
        hint = Text(
            "利用两角和公式: sin(α+β)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * (formula_y - 0.8))
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        # 推导步骤1
        step1 = MathTex(
            r"\sin 2\alpha", r"=", r"\sin(\alpha + \alpha)",
            font_size=28
        ).move_to(UP * (formula_y - 1.6))
        
        self.play(TransformMatchingTex(question.copy(), step1), run_time=1.0)
        
        # 推导步骤2
        step2 = MathTex(
            r"=", r"\sin\alpha \cos\alpha", r"+", r"\cos\alpha \sin\alpha",
            font_size=28
        ).move_to(UP * (formula_y - 2.4))
        
        self.play(Write(step2), run_time=1.2)
        
        # 最终公式
        final = MathTex(
            r"\sin 2\alpha", r"=", r"2\sin\alpha \cos\alpha",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * (formula_y - 3.5))
        
        final[0].set_color(self.COLOR_SECONDARY)
        final[2].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(final), run_time=1.0)
        self.play(Circumscribe(final, color=YELLOW, run_time=1.2))
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(hint),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(angle_2alpha_sector),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            FadeOut(angle_2alpha_label),
            run_time=0.6
        )
        
        # 将最终公式移到顶部小字保留
        final_small = final.copy().scale(0.6).move_to(UP * 5.5 + LEFT * 2)
        self.play(
            Transform(final, final_small),
            run_time=0.5
        )
        self.remove(final)
        self.add(final_small)
        self.sin_formula_saved = final_small
    
    def show_double_angle_cos(self):
        """场景4: 二倍角 cos 公式展示"""
        # 标题
        title = Text(
            "二倍角公式: cos 2α",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        formula_y = -3
        
        # 第一种形式
        form1 = MathTex(
            r"\cos 2\alpha", r"=", r"\cos^2\alpha - \sin^2\alpha",
            font_size=30,
            color=WHITE
        ).move_to(UP * formula_y)
        form1[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(form1), run_time=1.0)
        self.wait(0.8)
        
        # 提示
        hint = Text(
            "利用 sin²α + cos²α = 1",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * (formula_y - 1.0))
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.6)
        self.wait(0.6)
        
        # 第二种形式
        form2 = MathTex(
            r"\cos 2\alpha", r"=", r"2\cos^2\alpha - 1",
            font_size=30,
            color=WHITE
        ).move_to(UP * (formula_y - 1.8))
        form2[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(form2), run_time=1.0)
        self.wait(0.6)
        
        # 第三种形式
        form3 = MathTex(
            r"\cos 2\alpha", r"=", r"1 - 2\sin^2\alpha",
            font_size=30,
            color=WHITE
        ).move_to(UP * (formula_y - 2.6))
        form3[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(form3), run_time=1.0)
        
        # 高亮三个等价形式
        box = SurroundingRectangle(
            VGroup(form1, form2, form3),
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1
        )
        self.play(Create(box), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(form1),
            FadeOut(form2),
            FadeOut(form3),
            FadeOut(hint),
            FadeOut(box),
            run_time=0.6
        )
    
    def show_double_angle_tan(self):
        """场景5: 二倍角 tan 公式"""
        # 标题
        title = Text(
            "二倍角公式: tan 2α",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        formula_y = -3.5
        
        # 推导思路
        hint = MathTex(
            r"\tan 2\alpha = \frac{\sin 2\alpha}{\cos 2\alpha}",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * formula_y)
        
        self.play(Write(hint), run_time=1.0)
        self.wait(0.8)
        
        # 代入已知公式
        step1 = MathTex(
            r"= \frac{2\sin\alpha \cos\alpha}{\cos^2\alpha - \sin^2\alpha}",
            font_size=26
        ).move_to(UP * (formula_y - 1.0))
        
        self.play(Write(step1), run_time=1.2)
        self.wait(0.6)
        
        # 分子分母同除以cos²α
        step2 = Text(
            "分子分母同除以 cos²α",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * (formula_y - 2.0))
        
        self.play(FadeIn(step2, shift=UP * 0.2), run_time=0.6)
        
        # 最终公式
        final = MathTex(
            r"\tan 2\alpha", r"=", r"\frac{2\tan\alpha}{1 - \tan^2\alpha}",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * (formula_y - 3.2))
        
        final[0].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(final), run_time=1.0)
        self.play(Circumscribe(final, color=YELLOW, run_time=1.0))
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(hint),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(final),
            run_time=0.6
        )
    
    def show_half_angle(self):
        """场景6: 半角公式推导"""
        # 标题
        title = Text(
            "半角公式",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HALF_ANGLE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 显示半角的扇形
        angle_half_sector = Sector(
            arc_center=self.center,
            radius=self.RADIUS,
            angle=self.ALPHA / 2,
            start_angle=0,
            color=self.COLOR_HALF_ANGLE,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            self.angle_alpha_sector.animate.set_fill(opacity=0.15),
            Create(angle_half_sector),
            run_time=1.0
        )
        
        # 点R
        dot_R = Dot(self.P_half_alpha, color=self.COLOR_HALF_ANGLE, radius=0.08)
        label_R = MathTex(r"R", font_size=24, color=WHITE).next_to(dot_R, UR, buff=0.1)
        
        self.play(FadeIn(dot_R, scale=0.5), Write(label_R), run_time=0.5)
        
        # 角度标注
        angle_half_label = MathTex(
            r"\frac{\alpha}{2}",
            font_size=24,
            color=self.COLOR_HALF_ANGLE
        ).move_to(self.center + np.array([0.6, 0.15, 0]))
        
        self.play(Write(angle_half_label), run_time=0.5)
        
        self.wait(0.5)
        
        # 公式推导区域
        formula_y = -3.5
        
        # 推导思路
        hint = Text(
            "令 2α → α, α → α/2 代入二倍角公式",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * formula_y)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.8)
        self.wait(0.8)
        
        # sin²(α/2) 公式
        sin_half = MathTex(
            r"\sin^2\frac{\alpha}{2}", r"=", r"\frac{1 - \cos\alpha}{2}",
            font_size=30,
            color=WHITE
        ).move_to(UP * (formula_y - 1.2))
        sin_half[0].set_color(self.COLOR_HALF_ANGLE)
        
        self.play(Write(sin_half), run_time=1.0)
        self.wait(0.6)
        
        # cos²(α/2) 公式
        cos_half = MathTex(
            r"\cos^2\frac{\alpha}{2}", r"=", r"\frac{1 + \cos\alpha}{2}",
            font_size=30,
            color=WHITE
        ).move_to(UP * (formula_y - 2.2))
        cos_half[0].set_color(self.COLOR_HALF_ANGLE)
        
        self.play(Write(cos_half), run_time=1.0)
        self.wait(0.6)
        
        # tan(α/2) 公式
        tan_half = MathTex(
            r"\tan\frac{\alpha}{2}", r"=", r"\frac{\sin\alpha}{1 + \cos\alpha}",
            font_size=30,
            color=WHITE
        ).move_to(UP * (formula_y - 3.2))
        tan_half[0].set_color(self.COLOR_HALF_ANGLE)
        
        self.play(Write(tan_half), run_time=1.0)
        
        # 框选三个公式
        box = SurroundingRectangle(
            VGroup(sin_half, cos_half, tan_half),
            color=self.COLOR_HALF_ANGLE,
            buff=0.3,
            corner_radius=0.1
        )
        self.play(Create(box), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(angle_half_sector),
            FadeOut(dot_R),
            FadeOut(label_R),
            FadeOut(angle_half_label),
            FadeOut(hint),
            FadeOut(sin_half),
            FadeOut(cos_half),
            FadeOut(tan_half),
            FadeOut(box),
            run_time=0.6
        )
    
    def show_power_reduction_and_summary(self):
        """场景7: 降幂公式与总结"""
        # 淡出圆和坐标系
        self.play(
            FadeOut(self.circle),
            FadeOut(self.axes),
            FadeOut(self.angle_alpha_sector),
            FadeOut(self.dot_P),
            FadeOut(self.label_P),
            FadeOut(self.angle_label),
            *[FadeOut(mob) for mob in [self.sin_formula_saved] if hasattr(self, 'sin_formula_saved')],
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "降幂公式",
            font="PingFang SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 降幂公式
        power_sin = MathTex(
            r"\sin^2\alpha", r"=", r"\frac{1 - \cos 2\alpha}{2}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        power_sin[0].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(power_sin), run_time=1.0)
        self.wait(0.6)
        
        power_cos = MathTex(
            r"\cos^2\alpha", r"=", r"\frac{1 + \cos 2\alpha}{2}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 0.3)
        power_cos[0].set_color(self.COLOR_PRIMARY)
        
        self.play(Write(power_cos), run_time=1.0)
        
        self.wait(1.0)
        
        # 清理标题和降幂公式
        self.play(
            FadeOut(title),
            FadeOut(power_sin),
            FadeOut(power_cos),
            run_time=0.5
        )
        
        # 公式汇总
        summary_title = Text(
            "公式汇总",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 创建公式卡片
        formulas = [
            (r"\sin 2\alpha = 2\sin\alpha \cos\alpha", self.COLOR_SECONDARY),
            (r"\cos 2\alpha = \cos^2\alpha - \sin^2\alpha", self.COLOR_SECONDARY),
            (r"\tan 2\alpha = \frac{2\tan\alpha}{1-\tan^2\alpha}", self.COLOR_SECONDARY),
            (r"\sin^2\frac{\alpha}{2} = \frac{1-\cos\alpha}{2}", self.COLOR_HALF_ANGLE),
            (r"\cos^2\frac{\alpha}{2} = \frac{1+\cos\alpha}{2}", self.COLOR_HALF_ANGLE),
            (r"\tan\frac{\alpha}{2} = \frac{\sin\alpha}{1+\cos\alpha}", self.COLOR_HALF_ANGLE),
            (r"\sin^2\alpha = \frac{1-\cos 2\alpha}{2}", GOLD),
            (r"\cos^2\alpha = \frac{1+\cos 2\alpha}{2}", GOLD),
        ]
        
        formula_cards = VGroup()
        y_start = 4
        y_step = 1.1
        
        for i, (formula_text, color) in enumerate(formulas):
            formula = MathTex(formula_text, font_size=24, color=WHITE)
            
            # 左侧加色标
            color_bar = Rectangle(
                width=0.15,
                height=0.5,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0
            )
            
            card = VGroup(color_bar, formula).arrange(RIGHT, buff=0.2)
            card.move_to(UP * (y_start - i * y_step))
            
            formula_cards.add(card)
        
        # 逐个显示公式
        for card in formula_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.3)
        
        self.wait(1.5)
        
        # 全部公式闪烁
        self.play(
            *[Indicate(card, color=YELLOW) for card in formula_cards],
            run_time=1.5,
            lag_ratio=0.1
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(formula_cards),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
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
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握更多三角公式!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰性数学符号
        symbols = VGroup(
            MathTex(r"\sin", font_size=40, color=self.COLOR_PRIMARY),
            MathTex(r"\cos", font_size=40, color=self.COLOR_SECONDARY),
            MathTex(r"\tan", font_size=40, color=self.COLOR_HALF_ANGLE),
            MathTex(r"\alpha", font_size=40, color=GOLD),
        ).arrange(RIGHT, buff=1.0).move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in symbols],
            run_time=0.8,
            lag_ratio=0.2
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            run_time=1.0
        )


# 运行命令:
# manim -pql double_angle_formulas.py DoubleAngleFormulas  # 快速预览
# manim -qh double_angle_formulas.py DoubleAngleFormulas   # 高质量 1080p
# manim -qk double_angle_formulas.py DoubleAngleFormulas   # 4K质量