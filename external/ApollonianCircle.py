"""
阿波罗尼斯圆动画 - Apollonian Circle Animation
使用内外分点法尺规作图

作者: 上海初高中数学直通车 @emptyandcalm
格式: TikTok竖屏 (1080×1920)
"""

from manim import *
import numpy as np

# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ApollonianCircle(Scene):
    """
    阿波罗尼斯圆教学动画
    
    场景顺序:
    1. 开场钩子
    2. 揭示答案 - 圆
    3. 尺规作图引言
    4. 寻找内分点C
    5. 寻找外分点D
    6. 确定圆
    7. 验证与总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主圆
        self.COLOR_SECONDARY = "#e74c3c"     # 红色 - 辅助线
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
        self.COLOR_POINT_A = "#2ecc71"       # 绿色 - 点A
        self.COLOR_POINT_B = "#9b59b6"       # 紫色 - 点B
        self.COLOR_POINT_P = "#f39c12"       # 橙色 - 动点P
        self.COLOR_INTERNAL = "#1abc9c"      # 青色 - 内分点C
        self.COLOR_EXTERNAL = "#e67e22"      # 深橙 - 外分点D
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_reveal_circle()
        self.scene_3_construction_intro()
        self.scene_4_find_internal_point()
        self.scene_5_find_external_point()
        self.scene_6_construct_circle()
        self.scene_7_verification_summary()
    
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # 基准参数
        self.SCALE = 0.5
        self.OFFSET = UP * 0.5
        self.k_ratio = 2  # PA/PB = 2
        
        # 定义主要点A和B
        A_base = np.array([-2.5, 0, 0])
        B_base = np.array([2.5, 0, 0])
        
        self.A = A_base * self.SCALE + self.OFFSET
        self.B = B_base * self.SCALE + self.OFFSET
        
        # 计算内分点C (AC:CB = 2:1)
        # 公式: C = A + (k/(k+1)) * (B-A)
        self.C = self.A + (self.k_ratio / (self.k_ratio + 1)) * (self.B - self.A)
        
        # 计算外分点D (AD:DB = 2:1, D在AB外侧)
        # 公式: D = A + (k/(k-1)) * (B-A)
        self.D = self.A + (self.k_ratio / (self.k_ratio - 1)) * (self.B - self.A)
        
        # 计算圆心O (CD的中点)
        self.O = (self.C + self.D) / 2
        
        # 计算半径R
        self.R = np.linalg.norm(self.O - self.C)
        
        # 辅助射线相关点
        ray_direction = np.array([0.5, 1, 0])
        self.ray_direction = ray_direction / np.linalg.norm(ray_direction)
        
        AB_length = np.linalg.norm(self.B - self.A)
        self.unit_length = AB_length / 4
        
        self.M = self.A + self.ray_direction * self.unit_length
        self.N = self.A + self.ray_direction * (2 * self.unit_length)
        self.Q = self.A + self.ray_direction * (3 * self.unit_length)
        
        # 验证几何计算
        self.verify_geometry()
        
        print(f"✓ 几何初始化完成")
        print(f"  A坐标: {self.A}")
        print(f"  B坐标: {self.B}")
        print(f"  C坐标: {self.C}")
        print(f"  D坐标: {self.D}")
        print(f"  O坐标: {self.O}")
        print(f"  半径R: {self.R:.4f}")
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证内分点
        AC = np.linalg.norm(self.C - self.A)
        CB = np.linalg.norm(self.B - self.C)
        if abs(AC / CB - self.k_ratio) > epsilon:
            raise ValueError(f"内分点C计算错误! AC/CB = {AC/CB:.6f}")
        
        # 验证外分点
        AD = np.linalg.norm(self.D - self.A)
        DB = np.linalg.norm(self.B - self.D)
        if abs(AD / DB - self.k_ratio) > epsilon:
            raise ValueError(f"外分点D计算错误! AD/DB = {AD/DB:.6f}")
        
        # 验证半径
        R_check = np.linalg.norm(self.O - self.D)
        if abs(self.R - R_check) > epsilon:
            raise ValueError(f"半径计算不一致! R1={self.R:.6f}, R2={R_check:.6f}")
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 (分两行)
        hook_line1 = Text(
            "如果你到两个点的距离之比",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6)
        
        hook_line2 = Text(
            "永远是 2:1，你会画出什么轨迹?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.3)
        
        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)
        
        # 点A和B出现
        self.dot_A = Dot(self.A, color=self.COLOR_POINT_A, radius=0.12)
        self.dot_B = Dot(self.B, color=self.COLOR_POINT_B, radius=0.12)
        
        self.label_A = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.dot_A, DOWN, buff=0.15)
        self.label_B = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.dot_B, DOWN, buff=0.15)
        
        self.play(FadeIn(self.dot_A, scale=0.5), run_time=0.3)
        self.play(Flash(self.dot_A, color=self.COLOR_POINT_A, flash_radius=0.4), run_time=0.3)
        
        self.play(FadeIn(self.dot_B, scale=0.5), run_time=0.3)
        self.play(Flash(self.dot_B, color=self.COLOR_POINT_B, flash_radius=0.4), run_time=0.3)
        
        self.play(FadeIn(self.label_A), FadeIn(self.label_B), run_time=0.4)
        
        # 问号
        question_mark = Text("?", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 4)
        self.play(Write(question_mark), run_time=0.5)
        
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def scene_2_reveal_circle(self):
        """场景2: 揭示答案 - 圆 (5-10秒)"""
        # 标题
        title = Text(
            "阿波罗尼斯圆",
            font="Noto Sans CJK SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 绘制圆
        self.apollonian_circle_ref = Circle(
            radius=self.R,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.O)
        
        self.play(Create(self.apollonian_circle_ref), run_time=2.0)
        
        # 答案文字
        answer_text = Text(
            "答案: 这是一个圆!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(answer_text, scale=1.2), run_time=0.5)
        
        # 圆上一个点P演示
        angle_sample = 30 * DEGREES
        P_sample = self.O + self.R * np.array([np.cos(angle_sample), np.sin(angle_sample), 0])
        
        dot_P = Dot(P_sample, color=self.COLOR_POINT_P, radius=0.1)
        self.play(FadeIn(dot_P), run_time=0.3)
        
        # PA和PB线段
        line_PA = Line(P_sample, self.A, color=self.COLOR_POINT_A, stroke_width=2)
        line_PB = Line(P_sample, self.B, color=self.COLOR_POINT_B, stroke_width=2)
        
        self.play(Create(line_PA), Create(line_PB), run_time=0.6)
        
        # 长度标注
        PA_length = np.linalg.norm(P_sample - self.A)
        PB_length = np.linalg.norm(P_sample - self.B)
        
        length_PA = Text(
            f"PA={PA_length:.2f}",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_POINT_A
        ).next_to(line_PA.get_center(), LEFT, buff=0.1)
        
        length_PB = Text(
            f"PB={PB_length:.2f}",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_POINT_B
        ).next_to(line_PB.get_center(), RIGHT, buff=0.1)
        
        self.play(FadeIn(length_PA), FadeIn(length_PB), run_time=0.4)
        
        # 比值公式
        ratio_formula = MathTex(
            r"\frac{PA}{PB} = 2",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(ratio_formula), run_time=0.5)
        
        self.wait(0.9)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(answer_text),
            FadeOut(dot_P),
            FadeOut(line_PA),
            FadeOut(line_PB),
            FadeOut(length_PA),
            FadeOut(length_PB),
            FadeOut(ratio_formula),
            run_time=0.5
        )
    
    def scene_3_construction_intro(self):
        """场景3: 尺规作图引言 (10-15秒)"""
        # 问题文字
        question_text = Text(
            "如何用尺规画出这个圆?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(question_text), run_time=0.8)
        
        # 直线AB绘制并高亮
        self.line_AB_full = Line(
            self.A + LEFT * 0.5,
            self.B + RIGHT * 4.5,
            color=YELLOW,
            stroke_width=3
        )
        
        self.play(Create(self.line_AB_full), run_time=1.0)
        
        # 圆与AB交点闪烁
        self.play(
            Flash(self.C, color=self.COLOR_INTERNAL, flash_radius=0.4),
            Flash(self.D, color=self.COLOR_EXTERNAL, flash_radius=0.4),
            run_time=0.6
        )
        
        # 提示文字
        hint_text = Text(
            "关键: 找到圆与直线AB的两个交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(hint_text), run_time=0.6)
        
        # C和D点放大
        dot_C_temp = Dot(self.C, color=self.COLOR_INTERNAL, radius=0.12)
        dot_D_temp = Dot(self.D, color=self.COLOR_EXTERNAL, radius=0.12)
        
        self.play(
            FadeIn(dot_C_temp, scale=0.5),
            FadeIn(dot_D_temp, scale=0.5),
            run_time=0.5
        )
        
        # 说明
        explanation = Text(
            "CD是直径!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(explanation), run_time=0.8)
        
        self.wait(0.7)
        
        # 清理
        self.play(
            FadeOut(question_text),
            FadeOut(hint_text),
            FadeOut(explanation),
            FadeOut(dot_C_temp),
            FadeOut(dot_D_temp),
            run_time=0.6
        )
        
        # 圆变为虚线参考
        self.apollonian_circle_ref.set_stroke(opacity=0.3)
        self.line_AB_full.set_stroke(color=self.COLOR_AUXILIARY, opacity=0.5)
    
    def scene_4_find_internal_point(self):
        """场景4: 寻找内分点C (15-35秒)"""
        # 标题
        step_title = Text(
            "步骤1: 寻找内分点C",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_INTERNAL
        ).move_to(UP * 5.5)
        
        explanation_1 = Text(
            "在AB内，AC:CB = 2:1",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(step_title), FadeIn(explanation_1), run_time=0.8)
        self.wait(0.3)
        
        # 4.1 过A作辅助射线
        ray_end = self.A + self.ray_direction * 4.5
        ray_from_A = Line(self.A, ray_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(ray_from_A), run_time=0.8)
        
        aux_text = Text(
            "作辅助射线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(aux_text), run_time=0.4)
        self.wait(0.7)
        
        # 4.2 在射线上截取AM=MN
        dot_M = Dot(self.M, color=self.COLOR_AUXILIARY, radius=0.08)
        label_M = Text("M", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_M, UP, buff=0.1)
        
        self.play(FadeIn(dot_M), FadeIn(label_M), run_time=0.3)
        
        segment_AM = Line(self.A, self.M, color=YELLOW, stroke_width=4)
        self.play(Create(segment_AM), run_time=0.5)
        
        dot_N = Dot(self.N, color=self.COLOR_AUXILIARY, radius=0.08)
        label_N = Text("N", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_N, UP, buff=0.1)
        
        self.play(FadeIn(dot_N), FadeIn(label_N), run_time=0.3)
        
        segment_MN = Line(self.M, self.N, color=YELLOW, stroke_width=4)
        self.play(Create(segment_MN), run_time=0.5)
        
        equal_text = Text(
            "AM = MN",
            font="Noto Sans CJK SC",
            font_size=22,
            color=YELLOW
        ).move_to(DOWN * 5.5)
        
        self.play(Transform(aux_text, equal_text), run_time=0.5)
        self.wait(1.5)
        
        # 4.3 连接NB
        line_NB = Line(self.N, self.B, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(line_NB), run_time=0.8)
        self.wait(1.2)
        
        # 4.4 过M作NB的平行线
        parallel_text = Text(
            "过M作NB的平行线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeOut(aux_text), FadeIn(parallel_text), run_time=0.4)
        
        # 计算平行线
        vec_NB = self.B - self.N
        vec_NB_normalized = vec_NB / np.linalg.norm(vec_NB)
        
        # 平行线从M延伸
        parallel_start = self.M - vec_NB_normalized * 0.8
        parallel_end = self.M + vec_NB_normalized * 2.5
        
        parallel_line = DashedLine(
            parallel_start,
            parallel_end,
            color=self.COLOR_SECONDARY,
            dash_length=0.1
        )
        
        self.play(Create(parallel_line), run_time=1.0)
        
        # 平行符号标记（简化，不画复杂符号）
        self.wait(1.9)
        
        # 4.5 交点即为C
        self.dot_C = Dot(self.C, color=self.COLOR_INTERNAL, radius=0.1)
        
        self.play(Flash(self.dot_C, color=self.COLOR_INTERNAL, flash_radius=0.4), run_time=0.5)
        self.play(
            self.dot_C.animate.scale(2).set_fill(opacity=1),
            run_time=0.6
        )
        
        self.label_C = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.dot_C, DOWN, buff=0.15)
        self.play(FadeIn(self.label_C), run_time=0.3)
        
        # 标注AC和CB
        brace_AC = Brace(Line(self.A, self.C), direction=DOWN, buff=0.1, color=YELLOW)
        brace_label_AC = Text("2", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_AC, DOWN, buff=0.05)
        
        brace_CB = Brace(Line(self.C, self.B), direction=DOWN, buff=0.1, color=YELLOW)
        brace_label_CB = Text("1", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_CB, DOWN, buff=0.05)
        
        self.play(
            FadeIn(brace_AC),
            FadeIn(brace_label_AC),
            FadeIn(brace_CB),
            FadeIn(brace_label_CB),
            run_time=0.6
        )
        
        ratio_AC_CB = Text(
            "AC:CB = 2:1 ✓",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeOut(parallel_text), Write(ratio_AC_CB), run_time=0.7)
        self.wait(1.0)
        
        # 4.6 清理辅助线
        self.play(
            FadeOut(ray_from_A),
            FadeOut(dot_M),
            FadeOut(label_M),
            FadeOut(dot_N),
            FadeOut(label_N),
            FadeOut(segment_AM),
            FadeOut(segment_MN),
            FadeOut(line_NB),
            FadeOut(parallel_line),
            FadeOut(brace_AC),
            FadeOut(brace_label_AC),
            FadeOut(brace_CB),
            FadeOut(brace_label_CB),
            FadeOut(ratio_AC_CB),
            FadeOut(step_title),
            FadeOut(explanation_1),
            run_time=1.0
        )
        
        self.wait(2.0)
    
    def scene_5_find_external_point(self):
        """场景5: 寻找外分点D (35-55秒)"""
        # 标题
        step_title_2 = Text(
            "步骤2: 寻找外分点D",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_EXTERNAL
        ).move_to(UP * 5.5)
        
        explanation_2 = Text(
            "在AB外，AD:DB = 2:1",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(step_title_2), FadeIn(explanation_2), run_time=0.8)
        self.wait(0.3)
        
        # 5.2 在射线上截取AN=NQ
        continue_text = Text(
            "在之前射线上继续截取",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        # 重新显示射线和M、N点
        ray_end = self.A + self.ray_direction * 4.5
        ray_from_A = Line(self.A, ray_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        dot_M = Dot(self.M, color=self.COLOR_AUXILIARY, radius=0.08)
        dot_N = Dot(self.N, color=self.COLOR_AUXILIARY, radius=0.08)
        label_M = Text("M", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_M, UP, buff=0.08)
        label_N = Text("N", font="Noto Sans CJK SC", font_size=18, color=WHITE).next_to(dot_N, UP, buff=0.08)
        
        self.play(
            FadeIn(continue_text),
            FadeIn(ray_from_A),
            FadeIn(dot_M),
            FadeIn(dot_N),
            FadeIn(label_M),
            FadeIn(label_N),
            run_time=0.8
        )
        
        # Q点出现
        dot_Q = Dot(self.Q, color=self.COLOR_AUXILIARY, radius=0.08)
        label_Q = Text("Q", font="Noto Sans CJK SC", font_size=20, color=WHITE).next_to(dot_Q, UP, buff=0.1)
        
        self.play(FadeIn(dot_Q), FadeIn(label_Q), run_time=0.3)
        
        segment_NQ = Line(self.N, self.Q, color=YELLOW, stroke_width=4)
        self.play(Create(segment_NQ), run_time=0.5)
        
        equal_text_2 = Text(
            "NQ = AM = MN",
            font="Noto Sans CJK SC",
            font_size=22,
            color=YELLOW
        ).move_to(DOWN * 5.5)
        
        self.play(FadeOut(continue_text), FadeIn(equal_text_2), run_time=0.6)
        self.wait(1.6)
        
        # 5.3 连接QB
        line_QB = Line(self.Q, self.B, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(line_QB), run_time=0.8)
        self.wait(1.2)
        
        # 5.4 过N作QB的平行线
        parallel_text_2 = Text(
            "过N作QB的平行线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeOut(equal_text_2), FadeIn(parallel_text_2), run_time=0.4)
        
        # 计算平行线
        vec_QB = self.B - self.Q
        vec_QB_normalized = vec_QB / np.linalg.norm(vec_QB)
        
        # 平行线从N延伸到D
        parallel_start_2 = self.N - vec_QB_normalized * 0.5
        parallel_end_2 = self.N + vec_QB_normalized * 3.5
        
        parallel_line_2 = DashedLine(
            parallel_start_2,
            parallel_end_2,
            color=self.COLOR_SECONDARY,
            dash_length=0.1
        )
        
        self.play(Create(parallel_line_2), run_time=1.0)
        self.wait(1.9)
        
        # 5.5 交点即为D
        self.dot_D = Dot(self.D, color=self.COLOR_EXTERNAL, radius=0.1)
        
        self.play(Flash(self.dot_D, color=self.COLOR_EXTERNAL, flash_radius=0.4), run_time=0.5)
        self.play(
            self.dot_D.animate.scale(2).set_fill(opacity=1),
            run_time=0.6
        )
        
        self.label_D = Text("D", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.dot_D, DOWN, buff=0.15)
        self.play(FadeIn(self.label_D), run_time=0.3)
        
        # 标注AD和DB
        brace_AD = Brace(Line(self.A, self.D), direction=DOWN, buff=0.1, color=YELLOW)
        brace_label_AD = Text("2", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_AD, DOWN, buff=0.05)
        
        brace_DB = Brace(Line(self.D, self.B), direction=DOWN, buff=0.1, color=YELLOW)
        brace_label_DB = Text("1", font="Noto Sans CJK SC", font_size=20, color=YELLOW).next_to(brace_DB, DOWN, buff=0.05)
        
        self.play(
            FadeIn(brace_AD),
            FadeIn(brace_label_AD),
            FadeIn(brace_DB),
            FadeIn(brace_label_DB),
            run_time=0.6
        )
        
        ratio_AD_DB = Text(
            "AD:DB = 2:1 ✓",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeOut(parallel_text_2), Write(ratio_AD_DB), run_time=0.7)
        self.wait(1.0)
        
        # 5.6 清理辅助线
        self.play(
            FadeOut(ray_from_A),
            FadeOut(dot_M),
            FadeOut(label_M),
            FadeOut(dot_N),
            FadeOut(label_N),
            FadeOut(dot_Q),
            FadeOut(label_Q),
            FadeOut(segment_NQ),
            FadeOut(line_QB),
            FadeOut(parallel_line_2),
            FadeOut(brace_AD),
            FadeOut(brace_label_AD),
            FadeOut(brace_DB),
            FadeOut(brace_label_DB),
            FadeOut(ratio_AD_DB),
            FadeOut(step_title_2),
            FadeOut(explanation_2),
            run_time=1.0
        )
        
        self.wait(2.0)
    
    def scene_6_construct_circle(self):
        """场景6: 确定圆 (55-70秒)"""
        # 标题
        step_title_3 = Text(
            "步骤3: 确定圆",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(step_title_3), run_time=0.6)
        
        # 6.1 CD是直径
        line_CD = Line(self.C, self.D, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        self.play(Create(line_CD), run_time=0.8)
        
        diameter_text = Text(
            "CD是直径!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(diameter_text), run_time=0.6)
        self.wait(1.0)
        
        # 6.2 取CD中点为圆心O
        midpoint_text = Text(
            "取CD的中点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(midpoint_text), run_time=0.5)
        
        self.dot_O = Dot(self.O, color=self.COLOR_PRIMARY, radius=0.12)
        
        self.play(Flash(self.dot_O, color=self.COLOR_PRIMARY, flash_radius=0.4), run_time=0.3)
        self.play(FadeIn(self.dot_O), run_time=0.3)
        
        self.label_O = Text("O", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.dot_O, UP, buff=0.15)
        self.play(FadeIn(self.label_O), run_time=0.3)
        
        center_text = Text(
            "这就是圆心!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(center_text), run_time=0.6)
        self.wait(2.0)
        
        # 6.3 以OC或OD为半径画圆
        self.play(FadeOut(midpoint_text), FadeOut(center_text), run_time=0.3)
        
        radius_OC = Line(self.O, self.C, color=self.COLOR_PRIMARY, stroke_width=3)
        radius_OD = Line(self.O, self.D, color=self.COLOR_PRIMARY, stroke_width=3)
        
        self.play(Create(radius_OC), run_time=0.6)
        self.play(Create(radius_OD), run_time=0.6)
        
        radius_text = MathTex(
            r"R = OC = OD",
            font_size=28,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 5)
        
        self.play(Write(radius_text), run_time=0.7)
        
        # 最终圆绘制
        apollonian_circle_final = Circle(
            radius=self.R,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.O)
        
        self.play(
            FadeOut(self.apollonian_circle_ref),
            Create(apollonian_circle_final),
            run_time=2.5
        )
        
        self.play(Flash(self.dot_O, color=self.COLOR_PRIMARY, line_length=1.5), run_time=0.6)
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(step_title_3),
            FadeOut(diameter_text),
            FadeOut(radius_text),
            FadeOut(line_CD),
            FadeOut(radius_OC),
            FadeOut(radius_OD),
            run_time=0.6
        )
        
        # 保存最终圆供下一场景使用
        self.apollonian_circle_final = apollonian_circle_final
    
    def scene_7_verification_summary(self):
        """场景7: 验证与总结 (70-85秒)"""
        # 标题
        verify_title = Text(
            "验证: 圆上所有点都满足 PA/PB = 2",
            font="Noto Sans CJK SC",
            font_size=28,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(verify_title), run_time=0.8)
        
        # 7.1 圆上8个点验证
        angles = [i * 45 for i in range(8)]
        points_on_circle = [
            self.O + self.R * np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0])
            for angle in angles
        ]
        
        dots_on_circle = VGroup(*[
            Dot(p, radius=0.06, color=YELLOW)
            for p in points_on_circle
        ])
        
        self.play(FadeIn(dots_on_circle, lag_ratio=0.1), run_time=1.2)
        
        # 选一个点P演示
        P_demo = points_on_circle[1]  # 45度位置
        dot_P_demo = Dot(P_demo, color=self.COLOR_POINT_P, radius=0.1)
        
        self.play(
            dot_P_demo.animate.scale(2).set_fill(opacity=1),
            run_time=0.4
        )
        
        # PA和PB线段
        line_PA_demo = Line(P_demo, self.A, color=self.COLOR_POINT_A, stroke_width=2)
        line_PB_demo = Line(P_demo, self.B, color=self.COLOR_POINT_B, stroke_width=2)
        
        self.play(Create(line_PA_demo), Create(line_PB_demo), run_time=0.6)
        
        # 计算长度
        PA_val = np.linalg.norm(P_demo - self.A)
        PB_val = np.linalg.norm(P_demo - self.B)
        
        length_PA_text = Text(
            f"PA={PA_val:.2f}",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_POINT_A
        ).move_to(DOWN * 4.5 + LEFT * 1.5)
        
        length_PB_text = Text(
            f"PB={PB_val:.2f}",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_POINT_B
        ).move_to(DOWN * 4.5 + RIGHT * 1.5)
        
        self.play(FadeIn(length_PA_text), FadeIn(length_PB_text), run_time=0.5)
        
        ratio_val_text = Text(
            f"PA/PB = {PA_val/PB_val:.2f} ✓",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(ratio_val_text), run_time=0.7)
        
        # P点沿圆移动 (简化版，不做实时更新)
        self.wait(1.5)
        
        # 7.2 性质总结
        self.play(
            FadeOut(verify_title),
            FadeOut(dots_on_circle),
            FadeOut(dot_P_demo),
            FadeOut(line_PA_demo),
            FadeOut(line_PB_demo),
            FadeOut(length_PA_text),
            FadeOut(length_PB_text),
            FadeOut(ratio_val_text),
            run_time=0.5
        )
        
        # 总结卡片
        summary_1 = Text(
            "定义: PA/PB = k (常数)",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 2)
        
        summary_2 = Text(
            "轨迹是圆",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.5)
        
        summary_3 = Text(
            "内外分点法构造",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_INTERNAL
        ).move_to(DOWN * 1)
        
        summary_4 = Text(
            "CD是直径",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(summary_1), run_time=0.7)
        self.play(FadeIn(summary_2), run_time=0.7)
        self.play(FadeIn(summary_3), run_time=0.7)
        self.play(FadeIn(summary_4), run_time=0.7)
        
        beauty_title = Text(
            "阿波罗尼斯圆的美!",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(DOWN * 4.5)
        
        self.play(Write(beauty_title), run_time=0.8)
        self.wait(1.9)
        
        # 7.3 片尾
        self.play(
            FadeOut(self.apollonian_circle_final),
            FadeOut(self.dot_A),
            FadeOut(self.dot_B),
            FadeOut(self.dot_C),
            FadeOut(self.dot_D),
            FadeOut(self.dot_O),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_C),
            FadeOut(self.label_D),
            FadeOut(self.label_O),
            FadeOut(self.line_AB_full),
            FadeOut(summary_1),
            FadeOut(summary_2),
            FadeOut(summary_3),
            FadeOut(summary_4),
            FadeOut(beauty_title),
            run_time=1.0
        )
        
        # 作者信息放大
        self.play(
            self.author_info.animate.scale(2).move_to(UP * 1),
            run_time=0.8
        )
        
        follow_text = Text(
            "关注我，学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)
        
        self.wait(0.7)


# 运行命令:
# manim -pql apollonian_circle.py ApollonianCircle  # 快速预览
# manim -qh apollonian_circle.py ApollonianCircle   # 高质量渲染