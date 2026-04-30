"""
线段的和差倍分 - Line Segment Operations Animation
使用 Manim 创建的六年级数学教学视频

内容: 线段的和、差、倍、分（中点）
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


class LineSegmentOperations(Scene):
    """
    线段的和差倍分教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 线段的和 (AB + BC = AC)
    3. 线段的差 (长 - 短)
    4. 线段的倍 (2倍关系)
    5. 线段的分 (中点)
    6. 综合总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要线段
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 辅助线段
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮强调
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助元素
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 结果
        self.COLOR_POINT = "#f39c12"        # 橙色 - 关键点
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_sum()
        self.show_difference()
        self.show_multiple()
        self.show_division()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素和坐标 - 所有点都基于精确的数学计算"""
        # 缩放和偏移
        self.SCALE = 0.8  # 减小缩放以适应边界
        self.OFFSET = UP * 2
        
        # 定义基准单位长度 (减小以适应边界)
        self.UNIT_LENGTH = 1.2  # 基准长度（逻辑单位）- 从2.0减小到1.2
        
        # ===== Scene 2: 线段的和 =====
        # 设计: AB长度为2个单位，BC长度为1.5个单位
        # A点作为起点 (向右移动以居中)
        self.A_sum = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
        
        # B点：从A点沿x轴正方向移动AB长度
        AB_length = 2.0 * self.UNIT_LENGTH
        self.B_sum = self.A_sum + np.array([AB_length, 0, 0])
        
        # C点：从B点沿x轴正方向移动BC长度  
        BC_length = 1.5 * self.UNIT_LENGTH
        self.C_sum = self.B_sum + np.array([BC_length, 0, 0])
        
        # 计算实际长度
        self.len_AB = np.linalg.norm(self.B_sum - self.A_sum)
        self.len_BC = np.linalg.norm(self.C_sum - self.B_sum)
        self.len_AC = np.linalg.norm(self.C_sum - self.A_sum)
        
        # ===== Scene 3: 线段的差 =====
        # 设计: DE长度为2.5个单位，DF长度为1.5个单位
        # D点作为起点
        self.D = np.array([-2.0, 0, 0]) * self.SCALE + self.OFFSET
        
        # E点：从D点沿x轴正方向移动DE长度
        DE_length = 2.5 * self.UNIT_LENGTH
        self.E = self.D + np.array([DE_length, 0, 0])
        
        # F点：从D点沿x轴正方向移动DF长度（DF < DE）
        DF_length = 1.5 * self.UNIT_LENGTH
        self.F = self.D + np.array([DF_length, 0, 0])
        
        # 计算实际长度
        self.len_DE = np.linalg.norm(self.E - self.D)
        self.len_DF = np.linalg.norm(self.F - self.D)
        self.len_FE = np.linalg.norm(self.E - self.F)
        
        # ===== Scene 4: 线段的倍 =====
        # 设计: PQ是基准长度，PR = 2 × PQ（精确2倍关系）
        # P点作为起点
        self.P = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
        
        # Q点：从P点沿x轴正方向移动PQ长度
        PQ_length = 1.8 * self.UNIT_LENGTH  # 减小PQ长度
        self.Q = self.P + np.array([PQ_length, 0, 0])
        
        # R点：从P点沿x轴正方向移动2倍PQ长度（精确计算）
        PR_length = 2.0 * PQ_length  # 这是关键：2倍关系
        self.R = self.P + np.array([PR_length, 0, 0])
        
        # 计算实际长度
        self.len_PQ = np.linalg.norm(self.Q - self.P)
        self.len_QR = np.linalg.norm(self.R - self.Q)
        self.len_PR = np.linalg.norm(self.R - self.P)
        
        # ===== Scene 5: 线段的分 (中点) =====
        # 设计: AB长度为3个单位，M是精确中点
        # A点作为起点
        self.A_div = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
        
        # B点：从A点沿x轴正方向移动AB长度
        AB_div_length = 3.0 * self.UNIT_LENGTH
        self.B_div = self.A_div + np.array([AB_div_length, 0, 0])
        
        # M点：精确中点计算
        self.M = (self.A_div + self.B_div) / 2.0
        
        # 计算实际长度
        self.len_AB_div = np.linalg.norm(self.B_div - self.A_div)
        self.len_AM = np.linalg.norm(self.M - self.A_div)
        self.len_MB = np.linalg.norm(self.B_div - self.M)
        
        # 验证几何计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性 - 确保没有臆想的坐标"""
        epsilon = 1e-6
        
        print("\n========== 几何验证开始 ==========")
        
        # ===== 验证 Scene 2: 线段的和 =====
        print("\n[Scene 2] 验证线段的和:")
        calc_AC = self.len_AB + self.len_BC
        error_AC = abs(self.len_AC - calc_AC)
        
        print(f"  AB = {self.len_AB:.6f}")
        print(f"  BC = {self.len_BC:.6f}")
        print(f"  AC (实际) = {self.len_AC:.6f}")
        print(f"  AB + BC (计算) = {calc_AC:.6f}")
        print(f"  误差 = {error_AC:.10f}")
        
        if error_AC > epsilon:
            print(f"  ❌ 错误: AC ≠ AB + BC")
            raise ValueError(f"线段和计算错误! AC={self.len_AC:.6f}, AB+BC={calc_AC:.6f}")
        else:
            print(f"  ✓ 通过: AC = AB + BC")
        
        # ===== 验证 Scene 3: 线段的差 =====
        print("\n[Scene 3] 验证线段的差:")
        calc_FE = self.len_DE - self.len_DF
        error_FE = abs(self.len_FE - calc_FE)
        
        print(f"  DE = {self.len_DE:.6f}")
        print(f"  DF = {self.len_DF:.6f}")
        print(f"  FE (实际) = {self.len_FE:.6f}")
        print(f"  DE - DF (计算) = {calc_FE:.6f}")
        print(f"  误差 = {error_FE:.10f}")
        
        if error_FE > epsilon:
            print(f"  ❌ 错误: FE ≠ DE - DF")
            raise ValueError(f"线段差计算错误! FE={self.len_FE:.6f}, DE-DF={calc_FE:.6f}")
        else:
            print(f"  ✓ 通过: FE = DE - DF")
        
        # ===== 验证 Scene 4: 线段的倍 =====
        print("\n[Scene 4] 验证线段的倍 (2倍关系):")
        expected_PR = 2.0 * self.len_PQ
        error_PR = abs(self.len_PR - expected_PR)
        
        # 验证QR = PQ（两段应该相等）
        error_QR_PQ = abs(self.len_QR - self.len_PQ)
        
        print(f"  PQ = {self.len_PQ:.6f}")
        print(f"  QR = {self.len_QR:.6f}")
        print(f"  PR (实际) = {self.len_PR:.6f}")
        print(f"  2 × PQ (计算) = {expected_PR:.6f}")
        print(f"  PR误差 = {error_PR:.10f}")
        print(f"  QR-PQ误差 = {error_QR_PQ:.10f}")
        
        if error_PR > epsilon:
            print(f"  ❌ 错误: PR ≠ 2 × PQ")
            raise ValueError(f"线段倍数计算错误! PR={self.len_PR:.6f}, 2*PQ={expected_PR:.6f}")
        
        if error_QR_PQ > epsilon:
            print(f"  ❌ 错误: QR ≠ PQ (两段应该相等)")
            raise ValueError(f"线段QR和PQ不相等! QR={self.len_QR:.6f}, PQ={self.len_PQ:.6f}")
        
        print(f"  ✓ 通过: PR = 2 × PQ")
        print(f"  ✓ 通过: QR = PQ")
        
        # ===== 验证 Scene 5: 中点 =====
        print("\n[Scene 5] 验证中点:")
        error_AM_MB = abs(self.len_AM - self.len_MB)
        expected_half = self.len_AB_div / 2.0
        error_AM_half = abs(self.len_AM - expected_half)
        error_MB_half = abs(self.len_MB - expected_half)
        
        print(f"  AB = {self.len_AB_div:.6f}")
        print(f"  AM = {self.len_AM:.6f}")
        print(f"  MB = {self.len_MB:.6f}")
        print(f"  AB/2 (计算) = {expected_half:.6f}")
        print(f"  AM-MB误差 = {error_AM_MB:.10f}")
        print(f"  AM-(AB/2)误差 = {error_AM_half:.10f}")
        print(f"  MB-(AB/2)误差 = {error_MB_half:.10f}")
        
        if error_AM_MB > epsilon:
            print(f"  ❌ 错误: AM ≠ MB")
            raise ValueError(f"中点计算错误! AM={self.len_AM:.6f}, MB={self.len_MB:.6f}")
        
        if error_AM_half > epsilon or error_MB_half > epsilon:
            print(f"  ❌ 错误: AM 或 MB ≠ AB/2")
            raise ValueError(f"中点长度错误! AM={self.len_AM:.6f}, MB={self.len_MB:.6f}, AB/2={expected_half:.6f}")
        
        print(f"  ✓ 通过: AM = MB")
        print(f"  ✓ 通过: AM = MB = AB/2")
        
        # ===== 验证坐标在边界内 =====
        print("\n[边界检查] 验证所有点在安全区域内:")
        all_points = [
            ("A_sum", self.A_sum),
            ("B_sum", self.B_sum),
            ("C_sum", self.C_sum),
            ("D", self.D),
            ("E", self.E),
            ("F", self.F),
            ("P", self.P),
            ("Q", self.Q),
            ("R", self.R),
            ("A_div", self.A_div),
            ("B_div", self.B_div),
            ("M", self.M)
        ]
        
        x_min, x_max = -4.0, 4.0
        y_min, y_max = -7.0, 7.0
        
        all_in_bounds = True
        for name, point in all_points:
            x, y = point[0], point[1]
            if not (x_min <= x <= x_max and y_min <= y <= y_max):
                print(f"  ❌ {name} 超出边界: ({x:.2f}, {y:.2f})")
                all_in_bounds = False
            else:
                print(f"  ✓ {name} 在边界内: ({x:.2f}, {y:.2f})")
        
        if all_in_bounds:
            print(f"  ✓ 所有点都在安全区域内")
        else:
            raise ValueError("有点超出安全边界!")
        
        print("\n========== ✓ 所有几何验证通过 ==========\n")
    
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
        hook_text = Text(
            "两条线段能相加吗?\n它们的一半在哪里?",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 演示：三个点快速连成线段
        demo_A = np.array([-2, 0, 0]) * 0.7 + UP * 2
        demo_B = np.array([0, 0, 0]) * 0.7 + UP * 2
        demo_C = np.array([2, 0, 0]) * 0.7 + UP * 2
        
        dots = VGroup(
            Dot(demo_A, color=self.COLOR_POINT, radius=0.1),
            Dot(demo_B, color=self.COLOR_POINT, radius=0.1),
            Dot(demo_C, color=self.COLOR_POINT, radius=0.1)
        )
        
        self.play(FadeIn(dots, scale=0.5), run_time=0.6)
        
        demo_line = Line(demo_A, demo_C, color=self.COLOR_PRIMARY, stroke_width=4)
        self.play(Create(demo_line), run_time=1.0)
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(demo_line),
            FadeOut(dots),
            run_time=0.6
        )
    
    def show_sum(self):
        """场景2: 线段的和"""
        # 标题
        title = Text(
            "线段的和",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 绘制线段AB
        line_AB = Line(self.A_sum, self.B_sum, color=self.COLOR_PRIMARY, stroke_width=4)
        self.play(Create(line_AB), run_time=0.5)
        
        # 标注点A, B
        dot_A = Dot(self.A_sum, color=self.COLOR_POINT, radius=0.08)
        dot_B = Dot(self.B_sum, color=self.COLOR_POINT, radius=0.08)
        label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_A, DOWN, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_B, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dot_A),
            FadeIn(label_A),
            FadeIn(dot_B),
            FadeIn(label_B),
            run_time=0.5
        )
        
        # 测量AB长度
        brace_AB = Brace(line_AB, direction=UP, buff=0.1, color=self.COLOR_AUXILIARY)
        length_AB_value = round(self.len_AB, 1)
        length_AB = Text(
            f"AB = {length_AB_value}",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_AB, UP, buff=0.1)
        
        self.play(Create(brace_AB), FadeIn(length_AB), run_time=1.0)
        
        # 绘制线段BC
        line_BC = Line(self.B_sum, self.C_sum, color=self.COLOR_SECONDARY, stroke_width=4)
        self.play(Create(line_BC), run_time=0.5)
        
        # 标注点C
        dot_C = Dot(self.C_sum, color=self.COLOR_POINT, radius=0.08)
        label_C = Text("C", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_C, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_C), FadeIn(label_C), run_time=0.5)
        
        # 测量BC长度
        brace_BC = Brace(line_BC, direction=UP, buff=0.1, color=self.COLOR_AUXILIARY)
        length_BC_value = round(self.len_BC, 1)
        length_BC = Text(
            f"BC = {length_BC_value}",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_BC, UP, buff=0.1)
        
        self.play(Create(brace_BC), FadeIn(length_BC), run_time=1.0)
        
        # 公式出现
        formula_sum = MathTex(
            r"AB + BC = AC",
            font_size=32
        ).move_to(DOWN * 1)
        
        self.play(Write(formula_sum), run_time=1.0)
        
        # 高亮整体线段AC
        self.play(
            line_AB.animate.set_color(self.COLOR_SUCCESS),
            line_BC.animate.set_color(self.COLOR_SUCCESS),
            run_time=1.0
        )
        
        # 测量AC总长
        line_AC_full = Line(self.A_sum, self.C_sum, color=self.COLOR_SUCCESS, stroke_width=4)
        brace_AC = Brace(line_AC_full, direction=DOWN, buff=0.5, color=self.COLOR_SUCCESS)
        length_AC_value = round(self.len_AC, 1)
        length_AC = Text(
            f"AC = {length_AC_value}",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).next_to(brace_AC, DOWN, buff=0.1)
        
        self.play(Create(brace_AC), FadeIn(length_AC), run_time=1.0)
        
        # 闪烁强调
        self.play(Flash(formula_sum, color=YELLOW, flash_radius=0.5), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "首尾相连，长度相加",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_AB),
            FadeOut(line_BC),
            FadeOut(dot_A),
            FadeOut(dot_B),
            FadeOut(dot_C),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(brace_AB),
            FadeOut(brace_BC),
            FadeOut(brace_AC),
            FadeOut(length_AB),
            FadeOut(length_BC),
            FadeOut(length_AC),
            FadeOut(formula_sum),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_difference(self):
        """场景3: 线段的差"""
        # 标题
        title = Text(
            "线段的差",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 绘制长线段DE
        line_DE = Line(self.D, self.E, color=self.COLOR_PRIMARY, stroke_width=4)
        self.play(Create(line_DE), run_time=0.5)
        
        # 标注D, E点
        dot_D = Dot(self.D, color=self.COLOR_POINT, radius=0.08)
        dot_E = Dot(self.E, color=self.COLOR_POINT, radius=0.08)
        label_D = Text("D", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_D, DOWN, buff=0.15)
        label_E = Text("E", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_E, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dot_D),
            FadeIn(label_D),
            FadeIn(dot_E),
            FadeIn(label_E),
            run_time=0.5
        )
        
        # 测量DE长度
        brace_DE = Brace(line_DE, direction=UP, buff=0.1, color=self.COLOR_AUXILIARY)
        length_DE_value = round(self.len_DE, 1)
        length_DE = Text(
            f"DE = {length_DE_value}",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_DE, UP, buff=0.1)
        
        self.play(Create(brace_DE), FadeIn(length_DE), run_time=1.0)
        
        # 绘制短线段DF (覆盖部分)
        line_DF = Line(self.D, self.F, color=self.COLOR_SECONDARY, stroke_width=5)
        self.play(Create(line_DF), run_time=0.5)
        
        # 标注F点
        dot_F = Dot(self.F, color=self.COLOR_POINT, radius=0.08)
        label_F = Text("F", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_F, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_F), FadeIn(label_F), run_time=0.5)
        
        # 测量DF长度
        brace_DF = Brace(line_DF, direction=UP, buff=0.1, color=self.COLOR_SECONDARY)
        length_DF_value = round(self.len_DF, 1)
        length_DF = Text(
            f"DF = {length_DF_value}",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_DF, UP, buff=0.1)
        
        self.play(Create(brace_DF), FadeIn(length_DF), run_time=1.0)
        
        # 公式出现
        formula_diff = MathTex(
            r"DE - DF = FE",
            font_size=32
        ).move_to(DOWN * 1)
        
        self.play(Write(formula_diff), run_time=1.0)
        
        # 高亮剩余部分FE
        line_FE = Line(self.F, self.E, color=self.COLOR_SUCCESS, stroke_width=6)
        self.play(
            line_DE.animate.set_color(GRAY),
            line_DF.animate.set_color(GRAY),
            Create(line_FE),
            run_time=1.0
        )
        
        # 测量FE长度
        brace_FE = Brace(line_FE, direction=DOWN, buff=0.5, color=self.COLOR_SUCCESS)
        length_FE_value = round(self.len_FE, 1)
        length_FE = Text(
            f"FE = {length_FE_value}",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).next_to(brace_FE, DOWN, buff=0.1)
        
        self.play(Create(brace_FE), FadeIn(length_FE), run_time=1.0)
        
        # 闪烁强调
        self.play(Flash(formula_diff, color=YELLOW, flash_radius=0.5), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "较长减较短",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_DE),
            FadeOut(line_DF),
            FadeOut(line_FE),
            FadeOut(dot_D),
            FadeOut(dot_E),
            FadeOut(dot_F),
            FadeOut(label_D),
            FadeOut(label_E),
            FadeOut(label_F),
            FadeOut(brace_DE),
            FadeOut(brace_DF),
            FadeOut(brace_FE),
            FadeOut(length_DE),
            FadeOut(length_DF),
            FadeOut(length_FE),
            FadeOut(formula_diff),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_multiple(self):
        """场景4: 线段的倍"""
        # 标题
        title = Text(
            "线段的倍",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 绘制短线段PQ
        line_PQ = Line(self.P, self.Q, color=self.COLOR_SECONDARY, stroke_width=4)
        self.play(Create(line_PQ), run_time=0.5)
        
        # 标注P, Q点
        dot_P = Dot(self.P, color=self.COLOR_POINT, radius=0.08)
        dot_Q = Dot(self.Q, color=self.COLOR_POINT, radius=0.08)
        label_P = Text("P", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_P, DOWN, buff=0.15)
        label_Q = Text("Q", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_Q, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dot_P),
            FadeIn(label_P),
            FadeIn(dot_Q),
            FadeIn(label_Q),
            run_time=0.5
        )
        
        # 测量PQ长度，标注为"1倍"
        brace_PQ = Brace(line_PQ, direction=UP, buff=0.1, color=self.COLOR_AUXILIARY)
        length_PQ = Text(
            "PQ (1倍)",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_PQ, UP, buff=0.1)
        
        self.play(Create(brace_PQ), FadeIn(length_PQ), run_time=1.0)
        
        # 复制线段PQ (虚线)
        line_PQ_copy = DashedLine(self.P, self.Q, color=self.COLOR_SECONDARY, dash_length=0.1)
        line_PQ_copy.move_to(self.Q + (self.Q - self.P) / 2 + UP * 0.8)
        
        self.play(Create(line_PQ_copy), run_time=0.5)
        
        # 平移虚线到Q点右侧
        target_pos = self.Q + (self.Q - self.P) / 2
        self.play(line_PQ_copy.animate.move_to(target_pos), run_time=1.0)
        
        # 虚线变实线，拼接成QR
        line_QR = Line(self.Q, self.R, color=self.COLOR_SECONDARY, stroke_width=4)
        self.play(Transform(line_PQ_copy, line_QR), run_time=0.5)
        
        # 标注R点
        dot_R = Dot(self.R, color=self.COLOR_POINT, radius=0.08)
        label_R = Text("R", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_R, DOWN, buff=0.15)
        
        self.play(FadeIn(dot_R), FadeIn(label_R), run_time=0.5)
        
        # 公式出现
        formula_multiple = MathTex(
            r"PR = 2 \times PQ",
            font_size=32
        ).move_to(DOWN * 1)
        
        self.play(Write(formula_multiple), run_time=1.0)
        
        # 高亮整体PR
        line_PR_full = Line(self.P, self.R, color=self.COLOR_SUCCESS, stroke_width=6)
        self.play(
            line_PQ.animate.set_color(self.COLOR_SUCCESS),
            line_QR.animate.set_color(self.COLOR_SUCCESS),
            run_time=1.0
        )
        
        # 测量PR长度，标注为"2倍"
        brace_PR = Brace(line_PR_full, direction=DOWN, buff=0.5, color=self.COLOR_SUCCESS)
        length_PR = Text(
            "PR (2倍)",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).next_to(brace_PR, DOWN, buff=0.1)
        
        self.play(Create(brace_PR), FadeIn(length_PR), run_time=1.0)
        
        # 闪烁强调
        self.play(Flash(formula_multiple, color=YELLOW, flash_radius=0.5), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "首尾相连得倍数",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_PQ),
            FadeOut(line_PQ_copy),
            FadeOut(dot_P),
            FadeOut(dot_Q),
            FadeOut(dot_R),
            FadeOut(label_P),
            FadeOut(label_Q),
            FadeOut(label_R),
            FadeOut(brace_PQ),
            FadeOut(brace_PR),
            FadeOut(length_PQ),
            FadeOut(length_PR),
            FadeOut(formula_multiple),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_division(self):
        """场景5: 线段的分 (中点)"""
        # 标题
        title = Text(
            "线段的分 - 中点",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 绘制线段AB
        line_AB = Line(self.A_div, self.B_div, color=self.COLOR_PRIMARY, stroke_width=4)
        self.play(Create(line_AB), run_time=0.5)
        
        # 标注A, B点
        dot_A = Dot(self.A_div, color=self.COLOR_POINT, radius=0.08)
        dot_B = Dot(self.B_div, color=self.COLOR_POINT, radius=0.08)
        label_A = Text("A", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_A, DOWN, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=22, color=WHITE).next_to(dot_B, DOWN, buff=0.15)
        
        self.play(
            FadeIn(dot_A),
            FadeIn(label_A),
            FadeIn(dot_B),
            FadeIn(label_B),
            run_time=0.5
        )
        
        # 测量AB长度
        brace_AB = Brace(line_AB, direction=UP, buff=0.1, color=self.COLOR_AUXILIARY)
        length_AB_value = round(self.len_AB_div, 1)
        length_AB = Text(
            f"AB = {length_AB_value}",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).next_to(brace_AB, UP, buff=0.1)
        
        self.play(Create(brace_AB), FadeIn(length_AB), run_time=1.0)
        
        # 问题出现
        question = Text(
            "如何找到中点?",
            font="PingFang SC",
            font_size=28,
            color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(question), run_time=1.0)
        
        # 中点M闪现 (放大效果)
        dot_M = Dot(self.M, color=YELLOW, radius=0.12)
        self.play(FadeIn(dot_M, scale=1.5), run_time=0.5)
        
        # 标注M点
        label_M = Text(
            "M (中点)",
            font="PingFang SC",
            font_size=22,
            color=YELLOW
        ).next_to(dot_M, UP, buff=0.2)
        
        self.play(FadeIn(label_M), run_time=0.5)
        
        # 公式出现
        formula_midpoint = MathTex(
            r"AM = MB = \frac{AB}{2}",
            font_size=32
        ).move_to(DOWN * 1.5)
        
        self.play(Write(formula_midpoint), FadeOut(question), run_time=1.0)
        
        # 测量AM段
        line_AM = Line(self.A_div, self.M, color=self.COLOR_SUCCESS, stroke_width=5)
        brace_AM = Brace(line_AM, direction=DOWN, buff=0.3, color=self.COLOR_SUCCESS)
        length_AM_value = round(self.len_AM, 1)
        length_AM = Text(
            f"AM = {length_AM_value}",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_SUCCESS
        ).next_to(brace_AM, DOWN, buff=0.1)
        
        self.play(
            Create(brace_AM),
            FadeIn(length_AM),
            run_time=1.0
        )
        
        # 测量MB段
        line_MB = Line(self.M, self.B_div, color=self.COLOR_SUCCESS, stroke_width=5)
        brace_MB = Brace(line_MB, direction=DOWN, buff=0.3, color=self.COLOR_SUCCESS)
        length_MB_value = round(self.len_MB, 1)
        length_MB = Text(
            f"MB = {length_MB_value}",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_SUCCESS
        ).next_to(brace_MB, DOWN, buff=0.1)
        
        self.play(
            Create(brace_MB),
            FadeIn(length_MB),
            run_time=1.0
        )
        
        # 等号闪烁强调
        self.play(Flash(formula_midpoint, color=YELLOW, flash_radius=0.5), run_time=0.5)
        
        # 虚线分割 (从M点垂直)
        dashed_line_M = DashedLine(
            self.M + UP * 0.5,
            self.M + DOWN * 1.8,
            color=YELLOW,
            dash_length=0.1
        )
        
        self.play(Create(dashed_line_M), run_time=1.0)
        
        # 说明文字
        explanation = Text(
            "中点二等分线段",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(2.0)  # 重点内容多停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_AB),
            FadeOut(dot_A),
            FadeOut(dot_B),
            FadeOut(dot_M),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(label_M),
            FadeOut(brace_AB),
            FadeOut(brace_AM),
            FadeOut(brace_MB),
            FadeOut(length_AB),
            FadeOut(length_AM),
            FadeOut(length_MB),
            FadeOut(formula_midpoint),
            FadeOut(dashed_line_M),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 综合总结"""
        # 标题
        title = Text(
            "知识点回顾",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 创建四个卡片
        cards_data = [
            {
                "title": "和",
                "content": "AB + BC = AC (首尾相连)",
                "icon_color": self.COLOR_PRIMARY,
                "position": UP * 3
            },
            {
                "title": "差",
                "content": "长减短得差",
                "icon_color": self.COLOR_SECONDARY,
                "position": UP * 1.5
            },
            {
                "title": "倍",
                "content": "重复拼接",
                "icon_color": PURPLE,
                "position": ORIGIN
            },
            {
                "title": "分",
                "content": "中点二等分",
                "icon_color": self.COLOR_SUCCESS,
                "position": DOWN * 1.5
            }
        ]
        
        cards = VGroup()
        
        for data in cards_data:
            card = self.create_summary_card(
                data["title"],
                data["content"],
                data["icon_color"],
                data["position"]
            )
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 关键提示
        key_point = Text(
            "牢记中点性质!",
            font="PingFang SC",
            font_size=32,
            color=YELLOW
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(key_point, shift=UP * 0.3), run_time=0.6)
        
        # 所有卡片闪烁
        for card in cards:
            self.play(Flash(card, color=YELLOW, flash_radius=0.3), run_time=0.2)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(cards),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def create_summary_card(self, title, content, icon_color, position):
        """创建知识点总结卡片"""
        # 图标圆
        icon = Circle(radius=0.25, fill_color=icon_color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=28,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 线段装饰动画 (6条小线段环绕)
        decoration_lines = VGroup()
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
        
        for i in range(6):
            angle = i * PI / 3
            start = follow_text.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            end = follow_text.get_center() + 2.3 * np.array([np.cos(angle), np.sin(angle), 0])
            
            line = Line(start, end, color=colors[i], stroke_width=4)
            decoration_lines.add(line)
        
        self.play(
            *[Create(line) for line in decoration_lines],
            run_time=0.6
        )
        
        # 装饰旋转
        self.play(Rotate(decoration_lines, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decoration_lines),
            run_time=1.0
        )


# 运行命令:
# manim -pql line_segment_operations.py LineSegmentOperations  # 快速预览
# manim -qh line_segment_operations.py LineSegmentOperations   # 高质量渲染