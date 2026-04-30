"""
三角形外角定理证明动画 - Exterior Angle Theorem Proof
使用 Manim 创建的中学几何教学视频

内容: 证明三角形外角等于两个不相邻内角之和
方法: 过外角顶点作平行线,利用内错角和同位角
目标观众: 初中学生
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


class ExteriorAngleTheorem(Scene):
    """
    三角形外角定理证明动画场景
    
    场景顺序:
    1. 开场钩子
    2. 标注角度
    3. 引入辅助线
    4. 证明步骤1 - 内错角
    5. 证明步骤2 - 同位角
    6. 综合推导
    7. 结尾总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_EXTERIOR_ANGLE = "#e74c3c"  # 红色 - 外角
        self.COLOR_INTERIOR_ANGLE_1 = "#3498db"  # 蓝色 - 内角∠A
        self.COLOR_INTERIOR_ANGLE_2 = "#2ecc71"  # 绿色 - 内角∠B
        self.COLOR_AUXILIARY = YELLOW  # 辅助线
        self.COLOR_HIGHLIGHT = GOLD  # 高亮
        self.COLOR_GRAY = GRAY_B  # 说明文字
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_label_angles()
        self.scene_3_auxiliary_line()
        self.scene_4_alternate_angles()
        self.scene_5_corresponding_angles()
        self.scene_6_final_proof()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点
        self.SCALE = 1.0
        self.OFFSET = UP * 1.5
        
        # 主要顶点 (使用一般三角形)
        base_A = np.array([-2.5, 1.5, 0])
        base_B = np.array([2.5, 0.5, 0])
        base_C = np.array([0, -2, 0])
        
        # 应用缩放和偏移
        self.A = base_A * self.SCALE + self.OFFSET
        self.B = base_B * self.SCALE + self.OFFSET
        self.C = base_C * self.SCALE + self.OFFSET
        
        # BC延长线上的点D (延长BC)
        vec_BC = self.C - self.B
        self.EXTENSION_FACTOR = 1.5
        self.D = self.C + vec_BC * self.EXTENSION_FACTOR
        
        # 过C平行于AB的线上的点E
        vec_AB = self.B - self.A
        self.E = self.C + vec_AB * 1.5
        
        # 验证几何计算
        self.verify_geometry()
        
        # 创建主三角形
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=3
        )
    
    def verify_geometry(self):
        """验证几何关系"""
        epsilon = 1e-6
        
        # 验证D在BC延长线上
        vec_BC = self.C - self.B
        vec_BD = self.D - self.B
        # 检查方向相同(叉积为0)
        cross = np.cross(vec_BC[:2], vec_BD[:2])
        if abs(cross) > epsilon:
            print(f"WARNING: D点可能不在BC延长线上! 叉积: {cross}")
        
        # 验证CE平行于AB
        vec_AB = self.B - self.A
        vec_CE = self.E - self.C
        cross = np.cross(vec_AB[:2], vec_CE[:2])
        if abs(cross) > epsilon:
            print(f"WARNING: CE可能不平行于AB! 叉积: {cross}")
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_GRAY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "外角 = 两个内角之和?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 创建三角形
        self.play(Create(self.triangle), run_time=1.0)
        
        # 快速预览外角 (不详细标注)
        extend_preview = DashedLine(
            self.C, self.D,
            color=self.COLOR_GRAY,
            dash_length=0.08
        )
        
        # 外角预览圆弧 (简单版)
        angle_preview = Angle(
            Line(self.C, self.A),
            Line(self.C, self.D),
            radius=0.6,
            color=self.COLOR_EXTERIOR_ANGLE,
            stroke_width=3
        )
        
        self.play(Create(extend_preview), run_time=0.6)
        self.play(Create(angle_preview), run_time=0.5)
        self.play(Flash(angle_preview, color=self.COLOR_EXTERIOR_ANGLE), run_time=0.5)
        self.play(Indicate(hook_text, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(extend_preview),
            FadeOut(angle_preview),
            run_time=0.4
        )
    
    def scene_2_label_angles(self):
        """场景2: 标注角度 (7秒)"""
        # 延长BC
        self.extend_line = DashedLine(
            self.C, self.D,
            color=self.COLOR_GRAY,
            dash_length=0.1,
            stroke_width=2
        )
        
        self.play(Create(self.extend_line), run_time=0.6)
        
        # 标注外角∠ACD
        self.angle_ACD = Angle(
            Line(self.C, self.A),
            Line(self.C, self.D),
            radius=0.6,
            color=self.COLOR_EXTERIOR_ANGLE,
            stroke_width=4
        )
        
        # 外角标签 (使用希腊字母α)
        alpha_label = MathTex(r"\alpha", font_size=32, color=self.COLOR_EXTERIOR_ANGLE)
        # 放置在角度外侧
        angle_center = self.C + 0.8 * (
            (self.A - self.C) / np.linalg.norm(self.A - self.C) +
            (self.D - self.C) / np.linalg.norm(self.D - self.C)
        ) / 2
        alpha_label.move_to(angle_center)
        
        explain_exterior = Text(
            "外角 α",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GRAY
        ).move_to(DOWN * 5)
        
        self.play(
            Create(self.angle_ACD),
            Write(alpha_label),
            run_time=1.0
        )
        self.play(FadeIn(explain_exterior), run_time=0.4)
        self.wait(0.8)
        self.play(FadeOut(explain_exterior), run_time=0.3)
        
        # 标注内角∠A
        self.angle_A = Angle(
            Line(self.A, C:=self.C),
            Line(self.A, self.B),
            radius=0.5,
            color=self.COLOR_INTERIOR_ANGLE_1,
            stroke_width=3
        )
        
        label_A = MathTex(r"\angle A", font_size=28, color=self.COLOR_INTERIOR_ANGLE_1)
        label_A.next_to(self.angle_A, DOWN + RIGHT, buff=0.15)
        
        self.play(
            Create(self.angle_A),
            Write(label_A),
            run_time=0.8
        )
        
        # 标注内角∠B
        self.angle_B = Angle(
            Line(self.B, self.C),
            Line(self.B, self.A),
            radius=0.5,
            color=self.COLOR_INTERIOR_ANGLE_2,
            stroke_width=3
        )
        
        label_B = MathTex(r"\angle B", font_size=28, color=self.COLOR_INTERIOR_ANGLE_2)
        label_B.next_to(self.angle_B, DOWN + LEFT, buff=0.15)
        
        self.play(
            Create(self.angle_B),
            Write(label_B),
            run_time=0.8
        )
        
        # 提出问题
        question_chinese = Text(
            "α = ",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        question_math = MathTex(
            r"\angle A + \angle B",
            font_size=28,
            color=WHITE
        )
        question_mark = Text(" ?", font="PingFang SC", font_size=28, color=self.COLOR_HIGHLIGHT)
        
        question = VGroup(question_chinese, question_math, question_mark).arrange(RIGHT, buff=0.1)
        question.move_to(DOWN * 5)
        
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 保存标签以便后续使用
        self.alpha_label = alpha_label
        self.label_A = label_A
        self.label_B = label_B
        
        # 清理
        self.play(FadeOut(question), run_time=0.3)
    
    def scene_3_auxiliary_line(self):
        """场景3: 引入辅助线 (6秒)"""
        # 提示
        hint = Text(
            "关键: 过C作AB的平行线",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        
        # 绘制辅助线CE (虚线)
        vec_AB = self.B - self.A
        start_point = self.C - vec_AB * 0.3
        
        self.auxiliary_line = DashedLine(
            start_point,
            self.E,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(self.auxiliary_line), run_time=1.2)
        
        # 平行符号标记 (在AB和CE上)
        # AB上的标记
        mid_AB = (self.A + self.B) / 2
        vec_AB_perp = np.array([-vec_AB[1], vec_AB[0], 0])
        vec_AB_perp_norm = vec_AB_perp / np.linalg.norm(vec_AB_perp) * 0.15
        
        mark_AB = VGroup(
            Line(
                mid_AB + vec_AB_perp_norm * 0.7,
                mid_AB - vec_AB_perp_norm * 0.7,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            ),
            Line(
                mid_AB + vec_AB_perp_norm * 0.7 + vec_AB * 0.15,
                mid_AB - vec_AB_perp_norm * 0.7 + vec_AB * 0.15,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
        )
        
        # CE上的标记
        mid_CE = (self.C + self.E) / 2
        mark_CE = VGroup(
            Line(
                mid_CE + vec_AB_perp_norm * 0.7,
                mid_CE - vec_AB_perp_norm * 0.7,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            ),
            Line(
                mid_CE + vec_AB_perp_norm * 0.7 + vec_AB * 0.15,
                mid_CE - vec_AB_perp_norm * 0.7 + vec_AB * 0.15,
                color=self.COLOR_AUXILIARY,
                stroke_width=2
            )
        )
        
        self.parallel_marks = VGroup(mark_AB, mark_CE)
        
        self.play(FadeIn(self.parallel_marks), run_time=0.6)
        
        # 说明
        explain = Text(
            "CE // AB",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GRAY
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.play(Indicate(self.auxiliary_line, color=self.COLOR_AUXILIARY), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(FadeOut(hint), FadeOut(explain), run_time=0.3)
    
    def scene_4_alternate_angles(self):
        """场景4: 证明步骤1 - 内错角 (10秒)"""
        # 标题
        title_step1 = Text(
            "步骤1: 利用内错角",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title_step1, shift=DOWN * 0.2), run_time=0.4)
        
        # 绘制∠ACE (内错角)
        self.angle_ACE = Angle(
            Line(self.C, self.A),
            Line(self.C, self.E),
            radius=0.5,
            color=self.COLOR_INTERIOR_ANGLE_1,
            stroke_width=3,
            stroke_opacity=0.7
        )
        
        self.play(Create(self.angle_ACE), run_time=0.8)
        
        # 同时闪烁∠A和∠ACE
        self.play(
            Flash(self.angle_A, color=self.COLOR_INTERIOR_ANGLE_1, flash_radius=0.4),
            Flash(self.angle_ACE, color=self.COLOR_INTERIOR_ANGLE_1, flash_radius=0.4),
            run_time=0.6
        )
        
        # 内错角标记 (弧形箭头)
        # 从AB到CE的示意
        arc_start = self.A + (self.B - self.A) * 0.3
        arc_end = self.C + (self.E - self.C) * 0.3
        
        curved_arrow = CurvedArrow(
            arc_start,
            arc_end,
            color=self.COLOR_INTERIOR_ANGLE_1,
            stroke_width=2
        )
        
        self.play(Create(curved_arrow), run_time=0.6)
        
        # 等式1
        eq1_left = MathTex(r"\angle ACE", font_size=32, color=self.COLOR_INTERIOR_ANGLE_1)
        eq1_equal = MathTex(r"=", font_size=32, color=WHITE)
        eq1_right = MathTex(r"\angle A", font_size=32, color=self.COLOR_INTERIOR_ANGLE_1)
        
        self.equation_1 = VGroup(eq1_left, eq1_equal, eq1_right).arrange(RIGHT, buff=0.2)
        self.equation_1.move_to(DOWN * 4.5)
        
        self.play(Write(self.equation_1), run_time=1.0)
        
        # 解释
        explain_1 = Text(
            "CE // AB, 内错角相等",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_GRAY
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(2.0)  # 重要步骤,多停留
        
        self.play(Indicate(self.equation_1, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title_step1),
            FadeOut(explain_1),
            FadeOut(curved_arrow),
            run_time=0.4
        )
    
    def scene_5_corresponding_angles(self):
        """场景5: 证明步骤2 - 同位角 (10秒)"""
        # 标题
        title_step2 = Text(
            "步骤2: 利用同位角",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title_step2, shift=DOWN * 0.2), run_time=0.4)
        
        # 绘制∠ECD (同位角)
        self.angle_ECD = Angle(
            Line(self.C, self.E),
            Line(self.C, self.D),
            radius=0.5,
            color=self.COLOR_INTERIOR_ANGLE_2,
            stroke_width=3,
            stroke_opacity=0.7
        )
        
        self.play(Create(self.angle_ECD), run_time=0.8)
        
        # 同时闪烁∠B和∠ECD
        self.play(
            Flash(self.angle_B, color=self.COLOR_INTERIOR_ANGLE_2, flash_radius=0.4),
            Flash(self.angle_ECD, color=self.COLOR_INTERIOR_ANGLE_2, flash_radius=0.4),
            run_time=0.6
        )
        
        # 同位角标记
        arc_start_2 = self.B + (self.A - self.B) * 0.2 + (self.C - self.B) * 0.2
        arc_end_2 = self.C + (self.E - self.C) * 0.3 + (self.D - self.C) * 0.2
        
        curved_arrow_2 = CurvedArrow(
            arc_start_2,
            arc_end_2,
            color=self.COLOR_INTERIOR_ANGLE_2,
            stroke_width=2
        )
        
        self.play(Create(curved_arrow_2), run_time=0.6)
        
        # 等式2
        eq2_left = MathTex(r"\angle ECD", font_size=32, color=self.COLOR_INTERIOR_ANGLE_2)
        eq2_equal = MathTex(r"=", font_size=32, color=WHITE)
        eq2_right = MathTex(r"\angle B", font_size=32, color=self.COLOR_INTERIOR_ANGLE_2)
        
        self.equation_2 = VGroup(eq2_left, eq2_equal, eq2_right).arrange(RIGHT, buff=0.2)
        self.equation_2.move_to(DOWN * 5.5)
        
        self.play(Write(self.equation_2), run_time=1.0)
        
        # 解释
        explain_2 = Text(
            "CE // AB, 同位角相等",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_GRAY
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(explain_2), run_time=0.5)
        self.wait(2.0)  # 重要步骤,多停留
        
        self.play(Indicate(self.equation_2, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title_step2),
            FadeOut(explain_2),
            FadeOut(curved_arrow_2),
            run_time=0.4
        )
    
    def scene_6_final_proof(self):
        """场景6: 综合推导 (12秒)"""
        # 标题
        title_final = Text(
            "综合推导",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title_final, shift=DOWN * 0.2), run_time=0.4)
        
        # 提示外角拆分
        hint_split = Text(
            "外角 = ∠ACE + ∠ECD",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_GRAY
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(hint_split), run_time=0.5)
        
        # 高亮外角
        self.play(
            Indicate(self.angle_ACD, color=self.COLOR_EXTERIOR_ANGLE, scale_factor=1.2),
            run_time=0.6
        )
        
        # 显示拆分等式
        split_chinese = Text("α = ", font="PingFang SC", font_size=28, color=WHITE)
        split_math = MathTex(r"\angle ACE + \angle ECD", font_size=28, color=WHITE)
        split_equation = VGroup(split_chinese, split_math).arrange(RIGHT, buff=0.1)
        split_equation.move_to(DOWN * 3.5)
        
        self.play(Write(split_equation), run_time=1.0)
        
        # 移动等式1和等式2到合适位置
        self.play(
            self.equation_1.animate.move_to(DOWN * 4.5),
            run_time=0.8
        )
        self.play(
            self.equation_2.animate.move_to(DOWN * 5.5),
            run_time=0.8
        )
        
        # 替换符号 - 创建最终等式
        final_chinese = Text("α = ", font="PingFang SC", font_size=40, color=GOLD)
        final_math = MathTex(r"\angle A + \angle B", font_size=40, color=GOLD)
        final_checkmark = MathTex(r"\checkmark", font_size=40, color=GREEN).scale(1.2)
        
        final_equation = VGroup(final_chinese, final_math, final_checkmark).arrange(RIGHT, buff=0.2)
        final_equation.move_to(DOWN * 5)
        
        # 动画: 从拆分等式过渡到最终等式
        self.wait(0.5)
        self.play(
            FadeOut(split_equation),
            FadeOut(self.equation_1),
            FadeOut(self.equation_2),
            run_time=0.5
        )
        
        self.play(Write(final_equation), run_time=1.2)
        
        # 庆祝特效
        self.play(
            Flash(final_equation, color=GOLD, flash_radius=0.8, num_lines=16),
            run_time=1.0
        )
        self.play(
            Circumscribe(final_equation, color=GOLD, fade_out=True, run_time=1.0)
        )
        
        self.wait(2.0)  # 让学生欣赏结论
        
        # 保存最终等式
        self.final_equation = final_equation
        
        # 清理其他元素
        self.play(
            FadeOut(title_final),
            FadeOut(hint_split),
            FadeOut(self.angle_ACE),
            FadeOut(self.angle_ECD),
            FadeOut(self.angle_A),
            FadeOut(self.angle_B),
            FadeOut(self.angle_ACD),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.alpha_label),
            FadeOut(self.auxiliary_line),
            FadeOut(self.parallel_marks),
            FadeOut(self.extend_line),
            run_time=0.6
        )
    
    def scene_7_outro(self):
        """场景7: 结尾总结 (10秒)"""
        # 三角形缩小并移动
        triangle_small = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=2
        ).scale(0.6).move_to(UP * 3)
        
        self.play(
            Transform(self.triangle, triangle_small),
            run_time=0.8
        )
        
        # 定理卡片
        theorem_title = Text(
            "三角形外角定理",
            font="PingFang SC",
            font_size=36,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 1)
        
        self.play(FadeIn(theorem_title, shift=UP * 0.3), run_time=0.8)
        
        # 要点列表
        point_1 = Text(
            "• 外角 = 两个不相邻内角之和",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        point_2 = Text(
            "• 关键: 作平行线",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        )
        point_3 = Text(
            "• 利用内错角和同位角",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        key_points = VGroup(point_1, point_2, point_3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key_points.move_to(ORIGIN + DOWN * 0.5)
        
        self.play(Write(key_points), run_time=1.2)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_GRAY
        ).next_to(author_large, DOWN, buff=0.2)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            Flash(follow_text, color=GOLD, flash_radius=0.6),
            run_time=0.8
        )
        
        # 装饰 - 小三角形图标
        tri_icon_1 = Polygon(
            ORIGIN, RIGHT * 0.25, UP * 0.25,
            color=self.COLOR_EXTERIOR_ANGLE,
            fill_opacity=0.8
        ).scale(0.6).next_to(follow_text, LEFT, buff=0.5)
        
        tri_icon_2 = Polygon(
            ORIGIN, RIGHT * 0.25, UP * 0.25,
            color=self.COLOR_INTERIOR_ANGLE_1,
            fill_opacity=0.8
        ).scale(0.6).next_to(follow_text, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(tri_icon_1, scale=0.5),
            FadeIn(tri_icon_2, scale=0.5),
            run_time=0.6
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.final_equation),
            FadeOut(theorem_title),
            FadeOut(key_points),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(tri_icon_1),
            FadeOut(tri_icon_2),
            run_time=1.0
        )


# 运行命令:
# manim -pql exterior_angle_theorem.py ExteriorAngleTheorem  # 快速预览
# manim -qh exterior_angle_theorem.py ExteriorAngleTheorem   # 高质量渲染