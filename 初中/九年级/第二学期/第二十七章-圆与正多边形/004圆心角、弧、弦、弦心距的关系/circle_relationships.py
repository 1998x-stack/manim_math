"""
圆心角、弧、弦、弦心距的关系 - Manim 教学动画
Central Angle, Arc, Chord, and Sagitta Relationships in Circles

年级: 九年级
章节: 第二十七章 - 圆与正多边形
作者: 上海初高中数学直通车 @emptyandcalm
格式: TikTok 竖屏 (1080×1920)
"""

from manim import *
import numpy as np


# ===== 全局配置 - TikTok 竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CircleRelationships(Scene):
    """
    圆中四个量的关系动画场景
    
    核心知识点:
    在同圆或等圆中，圆心角相等 ⟺ 弧相等 ⟺ 弦相等 ⟺ 弦心距相等
    
    场景顺序:
    1. 开场钩子
    2. 概念介绍
    3. 第二组元素构建
    4. 圆心角相等 → 弧相等
    5. 弧相等 → 弦相等
    6. 弦相等 → 弦心距相等
    7. 总结与反向推导
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主圆
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_ARC_1 = "#2ecc71"        # 绿色 - 弧1
        self.COLOR_ARC_2 = "#9b59b6"        # 紫色 - 弧2
        self.COLOR_CHORD_1 = "#f39c12"      # 橙色 - 弦1
        self.COLOR_CHORD_2 = "#1abc9c"      # 青色 - 弦2
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_introduction()
        self.scene_3_second_group()
        self.scene_4_angle_to_arc()
        self.scene_5_arc_to_chord()
        self.scene_6_chord_to_sagitta()
        self.scene_7_summary()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何数据（基于verify_geometry.py的验证结果）"""
        # 基准参数
        self.O = np.array([0.0, 1.0, 0.0])  # 圆心
        self.R = 2.5                         # 半径
        self.angle_1 = np.pi / 3             # 60度
        self.angle_2 = np.pi / 3             # 60度
        
        # 第一组点 (弧AB: 从90°到30°)
        self.A = self.O + self.R * np.array([np.cos(np.pi/2), np.sin(np.pi/2), 0])
        self.B = self.O + self.R * np.array([np.cos(np.pi/6), np.sin(np.pi/6), 0])
        
        # 第二组点 (弧CD: 从-30°到-90°)
        self.C = self.O + self.R * np.array([np.cos(-np.pi/6), np.sin(-np.pi/6), 0])
        self.D = self.O + self.R * np.array([np.cos(-np.pi/2), np.sin(-np.pi/2), 0])
        
        # 弦的中点
        self.M1 = (self.A + self.B) / 2
        self.M2 = (self.C + self.D) / 2
        
        # 计算几何量
        self.chord_AB_length = np.linalg.norm(self.B - self.A)
        self.chord_CD_length = np.linalg.norm(self.D - self.C)
        self.sagitta_1 = np.linalg.norm(self.M1 - self.O)
        self.sagitta_2 = np.linalg.norm(self.M2 - self.O)
        self.arc_AB_length = self.R * self.angle_1
        self.arc_CD_length = self.R * self.angle_2
        
        print("✓ 几何数据初始化完成")
        print(f"  圆心O: {self.O[:2]}")
        print(f"  半径R: {self.R}")
        print(f"  圆心角: {np.degrees(self.angle_1):.1f}°")
        print(f"  弦长: {self.chord_AB_length:.3f}")
        print(f"  弦心距: {self.sagitta_1:.3f}")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).to_edge(UP, buff=0.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_line1 = Text(
            "圆中的四个量",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5)
        
        hook_line2 = Text(
            "有一个相等",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 4.2)
        
        hook_line3 = Text(
            "其余全等？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 3.4)
        
        self.play(Write(hook_line1), run_time=0.6)
        self.play(FadeIn(hook_line2, shift=UP * 0.2), run_time=0.5)
        self.play(Write(hook_line3), run_time=0.6)
        
        # 简单的圆预览
        preview_circle = Circle(
            radius=1.5,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 0.5)
        
        # 四个暗示点
        hint_dots = VGroup(*[
            Dot(
                preview_circle.point_at_angle(angle),
                radius=0.08,
                color=self.COLOR_HIGHLIGHT
            )
            for angle in [PI/4, 3*PI/4, 5*PI/4, 7*PI/4]
        ])
        
        self.play(Create(preview_circle), run_time=0.8)
        self.play(
            FadeIn(hint_dots, lag_ratio=0.2, scale=0.5),
            run_time=0.6
        )
        
        # 副标题
        subtitle = Text(
            "让我们一探究竟...",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 1.5)
        
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(hook_line3),
            FadeOut(subtitle),
            FadeOut(preview_circle),
            FadeOut(hint_dots),
            run_time=0.4
        )
    
    def scene_2_introduction(self):
        """场景2: 概念介绍"""
        # 标题
        title = Text(
            "四个关键元素",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 创建主圆
        self.main_circle = Circle(
            radius=self.R,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.main_circle), run_time=1.0)
        
        # 圆心O
        self.O_dot = Dot(self.O, radius=0.08, color=self.COLOR_SECONDARY)
        self.O_label = MathTex("O", font_size=28, color=WHITE).next_to(self.O_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(self.O_dot, scale=0.5), run_time=0.3)
        self.play(Flash(self.O_dot, color=self.COLOR_SECONDARY, flash_radius=0.4), run_time=0.4)
        self.play(Write(self.O_label), run_time=0.3)
        
        # 绘制半径OA和OB
        self.radius_OA = Line(self.O, self.A, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.radius_OB = Line(self.O, self.B, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(
            Create(self.radius_OA),
            Create(self.radius_OB),
            run_time=0.8
        )
        
        # 顶点A和B
        self.A_dot = Dot(self.A, radius=0.06, color=WHITE)
        self.B_dot = Dot(self.B, radius=0.06, color=WHITE)
        self.A_label = MathTex("A", font_size=24).next_to(self.A, UP, buff=0.1)
        self.B_label = MathTex("B", font_size=24).next_to(self.B, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(self.A_dot),
            FadeIn(self.B_dot),
            Write(self.A_label),
            Write(self.B_label),
            run_time=0.5
        )
        
        # ① 圆心角
        explanation_1 = Text(
            "① 圆心角 ∠AOB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.angle_AOB = Angle(
            self.radius_OB,
            self.radius_OA,
            radius=0.5,
            color=self.COLOR_SECONDARY,
            stroke_width=2
        )
        
        self.play(
            Create(self.angle_AOB),
            FadeIn(explanation_1),
            run_time=0.8
        )
        self.wait(0.6)
        
        # ② 弧
        explanation_2 = Text(
            "② 弧 ⌒AB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.arc_AB = Arc(
            radius=self.R,
            start_angle=PI/6,
            angle=PI/3,
            color=self.COLOR_ARC_1,
            stroke_width=5
        ).move_arc_center_to(self.O)
        
        self.play(
            Transform(explanation_1, explanation_2),
            Create(self.arc_AB),
            run_time=0.7
        )
        self.wait(0.5)
        
        # ③ 弦
        explanation_3 = Text(
            "③ 弦 AB",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.chord_AB = Line(
            self.A,
            self.B,
            color=self.COLOR_CHORD_1,
            stroke_width=4
        )
        
        self.play(
            Transform(explanation_1, explanation_3),
            Create(self.chord_AB),
            run_time=0.6
        )
        self.wait(0.5)
        
        # ④ 弦心距
        explanation_4 = Text(
            "④ 弦心距 OM",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.M1_dot = Dot(self.M1, radius=0.06, color=self.COLOR_AUXILIARY)
        self.M1_label = MathTex("M", font_size=20).next_to(self.M1, LEFT, buff=0.1)
        
        self.sagitta_OM = DashedLine(
            self.O,
            self.M1,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        # 垂直符号
        self.right_angle_1 = self.create_right_angle_mark(
            self.M1, self.O, self.A, size=0.2
        )
        
        self.play(
            Transform(explanation_1, explanation_4),
            Create(self.sagitta_OM),
            FadeIn(self.M1_dot),
            Write(self.M1_label),
            Create(self.right_angle_1),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 说明文字
        summary = Text(
            "圆心角 → 弧 → 弦 → 弦心距",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(
            FadeOut(explanation_1),
            FadeIn(summary),
            run_time=0.5
        )
        self.wait(1.2)
        
        # 清理标题和说明
        self.play(
            FadeOut(title),
            FadeOut(summary),
            run_time=0.4
        )
    
    def scene_3_second_group(self):
        """场景3: 第二组元素构建"""
        # 说明
        instruction = Text(
            "再取相等的圆心角 ∠COD",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(instruction), run_time=0.6)
        
        # 绘制半径OC和OD
        self.radius_OC = Line(self.O, self.C, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.radius_OD = Line(self.O, self.D, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(
            Create(self.radius_OC),
            Create(self.radius_OD),
            run_time=0.8
        )
        
        # 顶点C和D
        self.C_dot = Dot(self.C, radius=0.06, color=WHITE)
        self.D_dot = Dot(self.D, radius=0.06, color=WHITE)
        self.C_label = MathTex("C", font_size=24).next_to(self.C, RIGHT, buff=0.1)
        self.D_label = MathTex("D", font_size=24).next_to(self.D, DOWN, buff=0.1)
        
        self.play(
            FadeIn(self.C_dot),
            FadeIn(self.D_dot),
            Write(self.C_label),
            Write(self.D_label),
            run_time=0.5
        )
        
        # 圆心角∠COD
        self.angle_COD = Angle(
            self.radius_OD,
            self.radius_OC,
            radius=0.5,
            color=self.COLOR_SECONDARY,
            stroke_width=2
        )
        
        self.play(Create(self.angle_COD), run_time=0.6)
        
        # 弧CD
        self.arc_CD = Arc(
            radius=self.R,
            start_angle=-PI/2,
            angle=PI/3,
            color=self.COLOR_ARC_2,
            stroke_width=5
        ).move_arc_center_to(self.O)
        
        self.play(Create(self.arc_CD), run_time=0.7)
        
        # 弦CD
        self.chord_CD = Line(
            self.C,
            self.D,
            color=self.COLOR_CHORD_2,
            stroke_width=4
        )
        
        self.play(Create(self.chord_CD), run_time=0.6)
        
        # 弦心距ON
        self.M2_dot = Dot(self.M2, radius=0.06, color=self.COLOR_AUXILIARY)
        self.M2_label = MathTex("N", font_size=20).next_to(self.M2, RIGHT, buff=0.1)
        
        self.sagitta_ON = DashedLine(
            self.O,
            self.M2,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.right_angle_2 = self.create_right_angle_mark(
            self.M2, self.O, self.C, size=0.2
        )
        
        self.play(
            Create(self.sagitta_ON),
            FadeIn(self.M2_dot),
            Write(self.M2_label),
            Create(self.right_angle_2),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(instruction), run_time=0.3)
    
    def scene_4_angle_to_arc(self):
        """场景4: 圆心角相等 → 弧相等"""
        # 淡化其他元素
        fade_group = VGroup(
            self.chord_AB,
            self.chord_CD,
            self.sagitta_OM,
            self.sagitta_ON,
            self.M1_dot,
            self.M2_dot,
            self.M1_label,
            self.M2_label,
            self.right_angle_1,
            self.right_angle_2
        )
        
        self.play(fade_group.animate.set_opacity(0.2), run_time=0.4)
        
        # 标题
        title = Text(
            "① 圆心角相等 → 弧相等",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 角度标注
        angle_1_label = MathTex("60^\\circ", font_size=24, color=YELLOW).next_to(
            self.angle_AOB, LEFT, buff=0.3
        )
        angle_2_label = MathTex("60^\\circ", font_size=24, color=YELLOW).next_to(
            self.angle_COD, RIGHT, buff=0.3
        )
        
        self.play(
            Write(angle_1_label),
            Write(angle_2_label),
            run_time=0.8
        )
        
        # 角度闪烁
        self.play(
            Flash(self.angle_AOB, color=YELLOW),
            Flash(self.angle_COD, color=YELLOW),
            run_time=0.5
        )
        
        # 箭头
        arrow = MathTex("\\Rightarrow", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(GrowFromCenter(arrow), run_time=0.6)
        
        # 弧高亮
        self.play(
            self.arc_AB.animate.set_stroke(width=8, color=YELLOW),
            self.arc_CD.animate.set_stroke(width=8, color=YELLOW),
            run_time=0.4
        )
        
        # 弧长标注
        arc_label_1 = MathTex(
            f"\\overset{{\\frown}}{{AB}} = {self.arc_AB_length:.2f}",
            font_size=22,
            color=YELLOW
        ).move_to(LEFT * 2.5 + UP * 3.5)
        
        arc_label_2 = MathTex(
            f"\\overset{{\\frown}}{{CD}} = {self.arc_CD_length:.2f}",
            font_size=22,
            color=YELLOW
        ).move_to(RIGHT * 2.5 + DOWN * 0.5)
        
        self.play(
            Write(arc_label_1),
            Write(arc_label_2),
            run_time=0.8
        )
        
        # 等于符号
        equals = Text(
            "弧相等！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equals), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(angle_1_label),
            FadeOut(angle_2_label),
            FadeOut(arrow),
            FadeOut(arc_label_1),
            FadeOut(arc_label_2),
            FadeOut(equals),
            self.arc_AB.animate.set_stroke(width=5, color=self.COLOR_ARC_1),
            self.arc_CD.animate.set_stroke(width=5, color=self.COLOR_ARC_2),
            run_time=0.5
        )
    
    def scene_5_arc_to_chord(self):
        """场景5: 弧相等 → 弦相等"""
        # 恢复弦，淡化其他
        self.play(
            self.chord_AB.animate.set_opacity(1.0),
            self.chord_CD.animate.set_opacity(1.0),
            run_time=0.3
        )
        
        # 标题
        title = Text(
            "② 弧相等 → 弦相等",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.4)
        
        # 弧闪烁
        self.play(
            Indicate(self.arc_AB, scale_factor=1.1, color=YELLOW),
            Indicate(self.arc_CD, scale_factor=1.1, color=YELLOW),
            run_time=0.6
        )
        
        # 箭头
        arrow = MathTex("\\Rightarrow", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(GrowFromCenter(arrow), run_time=0.5)
        
        # 弦高亮
        self.play(
            self.chord_AB.animate.set_stroke(width=7, color=YELLOW),
            self.chord_CD.animate.set_stroke(width=7, color=YELLOW),
            run_time=0.6
        )
        
        # 弦长标注
        chord_label_1 = MathTex(
            f"AB = {self.chord_AB_length:.2f}",
            font_size=24,
            color=YELLOW
        ).next_to(self.chord_AB, LEFT, buff=0.3)
        
        chord_label_2 = MathTex(
            f"CD = {self.chord_CD_length:.2f}",
            font_size=24,
            color=YELLOW
        ).next_to(self.chord_CD, RIGHT, buff=0.3)
        
        self.play(
            Write(chord_label_1),
            Write(chord_label_2),
            run_time=0.8
        )
        
        # 等于符号
        equals = Text(
            "弦相等！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equals), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(chord_label_1),
            FadeOut(chord_label_2),
            FadeOut(equals),
            self.chord_AB.animate.set_stroke(width=4, color=self.COLOR_CHORD_1),
            self.chord_CD.animate.set_stroke(width=4, color=self.COLOR_CHORD_2),
            run_time=0.5
        )
    
    def scene_6_chord_to_sagitta(self):
        """场景6: 弦相等 → 弦心距相等"""
        # 恢复弦心距
        fade_group = VGroup(
            self.sagitta_OM,
            self.sagitta_ON,
            self.M1_dot,
            self.M2_dot,
            self.M1_label,
            self.M2_label,
            self.right_angle_1,
            self.right_angle_2
        )
        
        self.play(fade_group.animate.set_opacity(1.0), run_time=0.3)
        
        # 标题
        title = Text(
            "③ 弦相等 → 弦心距相等",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.4)
        
        # 弦闪烁
        self.play(
            Indicate(self.chord_AB, scale_factor=1.05, color=YELLOW),
            Indicate(self.chord_CD, scale_factor=1.05, color=YELLOW),
            run_time=0.6
        )
        
        # 箭头
        arrow = MathTex("\\Rightarrow", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(GrowFromCenter(arrow), run_time=0.5)
        
        # 弦心距高亮
        self.play(
            self.sagitta_OM.animate.set_stroke(width=4, color=YELLOW),
            self.sagitta_ON.animate.set_stroke(width=4, color=YELLOW),
            run_time=0.7
        )
        
        # 距离标注
        dist_label_1 = MathTex(
            f"OM = {self.sagitta_1:.2f}",
            font_size=22,
            color=YELLOW
        ).next_to(self.sagitta_OM, UP, buff=0.1)
        
        dist_label_2 = MathTex(
            f"ON = {self.sagitta_2:.2f}",
            font_size=22,
            color=YELLOW
        ).next_to(self.sagitta_ON, DOWN, buff=0.1)
        
        self.play(
            Write(dist_label_1),
            Write(dist_label_2),
            run_time=0.8
        )
        
        # 等于符号
        equals = Text(
            "弦心距相等！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(equals), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(dist_label_1),
            FadeOut(dist_label_2),
            FadeOut(equals),
            self.sagitta_OM.animate.set_stroke(width=2, color=self.COLOR_AUXILIARY),
            self.sagitta_ON.animate.set_stroke(width=2, color=self.COLOR_AUXILIARY),
            run_time=0.5
        )
    
    def scene_7_summary(self):
        """场景7: 总结与反向推导"""
        # 场景缩小移至上方
        entire_scene = VGroup(
            self.main_circle,
            self.O_dot,
            self.O_label,
            self.radius_OA,
            self.radius_OB,
            self.radius_OC,
            self.radius_OD,
            self.A_dot,
            self.B_dot,
            self.C_dot,
            self.D_dot,
            self.A_label,
            self.B_label,
            self.C_label,
            self.D_label,
            self.angle_AOB,
            self.angle_COD,
            self.arc_AB,
            self.arc_CD,
            self.chord_AB,
            self.chord_CD,
            self.sagitta_OM,
            self.sagitta_ON,
            self.M1_dot,
            self.M2_dot,
            self.M1_label,
            self.M2_label,
            self.right_angle_1,
            self.right_angle_2
        )
        
        self.play(
            entire_scene.animate.scale(0.35).to_edge(UP, buff=1.5),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "四个量的等价关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 四个量图标和文字
        icon_size = 0.4
        spacing = 1.8
        
        # 圆心角
        icon_1 = VGroup(
            Arc(radius=icon_size, angle=PI/2, color=self.COLOR_SECONDARY, stroke_width=3),
            Text("圆心角", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        # 弧
        icon_2 = VGroup(
            Arc(radius=icon_size, angle=PI/2, color=self.COLOR_ARC_1, stroke_width=4),
            Text("弧", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        # 弦
        icon_3 = VGroup(
            Line(LEFT * icon_size, RIGHT * icon_size, color=self.COLOR_CHORD_1, stroke_width=4),
            Text("弦", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        # 弦心距
        icon_4 = VGroup(
            DashedLine(ORIGIN, DOWN * icon_size, color=self.COLOR_AUXILIARY, dash_length=0.05),
            Text("弦心距", font="Noto Sans CJK SC", font_size=18, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        # 排列图标
        icons = VGroup(icon_1, icon_2, icon_3, icon_4).arrange(RIGHT, buff=0.6).move_to(UP * 1)
        
        self.play(FadeIn(icons, lag_ratio=0.2), run_time=1.0)
        
        # 双向箭头
        arrow_1 = MathTex("\\Leftrightarrow", font_size=40, color=YELLOW).move_to(
            (icon_1.get_center() + icon_2.get_center()) / 2
        )
        arrow_2 = MathTex("\\Leftrightarrow", font_size=40, color=YELLOW).move_to(
            (icon_2.get_center() + icon_3.get_center()) / 2
        )
        arrow_3 = MathTex("\\Leftrightarrow", font_size=40, color=YELLOW).move_to(
            (icon_3.get_center() + icon_4.get_center()) / 2
        )
        
        arrows = VGroup(arrow_1, arrow_2, arrow_3)
        
        self.play(
            GrowFromCenter(arrow_1),
            GrowFromCenter(arrow_2),
            GrowFromCenter(arrow_3),
            lag_ratio=0.1,
            run_time=1.2
        )
        
        # 核心公式
        formula = Text(
            "任一个相等 → 其余全等",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 1)
        
        self.play(Write(formula), run_time=1.0)
        
        # 强调"反之亦然"
        reverse_text = Text(
            "⇄ 反之亦然",
            font="Noto Sans CJK SC",
            font_size=26,
            color=YELLOW
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(reverse_text, scale=1.1), run_time=0.5)
        self.play(Indicate(reverse_text, scale_factor=1.2), run_time=0.5)
        
        # 应用提示
        application = Text(
            "这是圆中进行等量代换的重要依据",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.2)
        
        self.play(FadeIn(application), run_time=0.5)
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(entire_scene),
            FadeOut(summary_title),
            FadeOut(icons),
            FadeOut(arrows),
            FadeOut(formula),
            FadeOut(reverse_text),
            FadeOut(application),
            run_time=0.6
        )
    
    def scene_8_outro(self):
        """场景8: 片尾"""
        # 作者名放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.7
        )
        
        # ID
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        decorations = VGroup(*[
            Circle(
                radius=0.3,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6,
                stroke_width=0
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        
        # 四个量图标快闪
        quick_icons = VGroup(
            Arc(radius=0.3, angle=PI/3, color=self.COLOR_SECONDARY, stroke_width=3),
            Arc(radius=0.3, angle=PI/3, color=self.COLOR_ARC_1, stroke_width=4),
            Line(LEFT * 0.3, RIGHT * 0.3, color=self.COLOR_CHORD_1, stroke_width=4),
            DashedLine(ORIGIN, DOWN * 0.3, color=self.COLOR_AUXILIARY, dash_length=0.05)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in quick_icons], run_time=0.6)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            FadeOut(quick_icons),
            run_time=1.0
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = point1 - corner
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = point2 - corner
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
        return square


# 渲染命令:
# manim -pql circle_relationships.py CircleRelationships  # 快速预览 (480p 15fps)
# manim -qh circle_relationships.py CircleRelationships   # 高质量 (1080p 60fps)
# manim -qk circle_relationships.py CircleRelationships   # 4K质量