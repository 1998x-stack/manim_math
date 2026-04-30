"""
平行线分线段成比例定理 - Parallel Lines Proportional Segments Theorem
使用 Manim 创建的九年级几何教学视频

内容: 
1. 三条平行线截两条直线定理
2. 三角形推论
3. 逆定理
4. 应用示例

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


class GeometryCalculator:
    """几何计算工具类"""
    
    @staticmethod
    def line_intersection(P1, D1, P2, D2):
        """
        计算两直线交点
        直线1: P1 + t*D1
        直线2: P2 + s*D2
        """
        A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        
        if np.abs(np.linalg.det(A)) < 1e-10:
            return None  # 平行线，无交点
        
        params = np.linalg.solve(A, b)
        return np.array([*(P1[:2] + params[0] * D1[:2]), 0])
    
    @staticmethod
    def point_on_line(start, end, t):
        """在线段上找参数为t的点 (t∈[0,1])"""
        return start + t * (end - start)
    
    @staticmethod
    def are_parallel(vec1, vec2, epsilon=1e-6):
        """验证两向量是否平行"""
        cross = np.cross(vec1[:2], vec2[:2])
        return abs(cross) < epsilon


class ParallelLinesTheorem(Scene):
    """
    平行线分线段成比例定理教学动画
    
    场景顺序:
    1. 开场钩子
    2. 三条平行线截两条直线
    3. 三角形推论
    4. 逆定理
    5. 应用示例
    6. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"    # 红色
        self.COLOR_PARALLEL = "#2ecc71"     # 绿色
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_FORMULA = "#f39c12"
        
        # 作者信息 (始终显示在顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.author_info)
        
        # 执行动画序列
        self.show_opening()
        self.show_three_parallel_lines()
        self.show_triangle_corollary()
        self.show_converse_theorem()
        self.show_application()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 钩子问题
        hook = Text(
            "平行线有什么神奇性质?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.3)
        
        # 快速展示三条平行线
        parallel_demo = VGroup()
        for i in range(3):
            line = Line(
                LEFT * 3, RIGHT * 3,
                color=self.COLOR_PARALLEL,
                stroke_width=4
            ).shift(DOWN * (i - 1) * 1.2)
            parallel_demo.add(line)
        
        self.play(
            *[Create(line) for line in parallel_demo],
            run_time=1.2
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(parallel_demo),
            run_time=0.5
        )
    
    def show_three_parallel_lines(self):
        """场景2: 三条平行线截两条直线定理"""
        # 初始化几何数据
        self.setup_parallel_lines_geometry()
        
        # 标题
        title = Text(
            "定理: 三条平行线截两条直线",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # Step 1: 创建两条相交直线
        line1 = Line(self.L1_start, self.L1_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        line2 = Line(self.L2_start, self.L2_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(line1), Create(line2), run_time=1.0)
        
        # Step 2: 依次创建三条平行线并标记交点
        # 平行线1
        pline1 = Line(
            self.A + LEFT * 1.5, self.D + RIGHT * 1.5,
            color=self.COLOR_PARALLEL, stroke_width=4
        )
        dot_A = Dot(self.A, color=self.COLOR_PRIMARY, radius=0.08)
        dot_D = Dot(self.D, color=self.COLOR_PRIMARY, radius=0.08)
        label_A = Text("A", font="PingFang SC", font_size=20).next_to(dot_A, LEFT, buff=0.1)
        label_D = Text("D", font="PingFang SC", font_size=20).next_to(dot_D, RIGHT, buff=0.1)
        
        self.play(Create(pline1), run_time=0.6)
        self.play(
            FadeIn(dot_A, scale=0.5),
            FadeIn(dot_D, scale=0.5),
            Write(label_A),
            Write(label_D),
            run_time=0.5
        )
        
        # 平行线2
        pline2 = Line(
            self.B + LEFT * 1.5, self.E + RIGHT * 1.5,
            color=self.COLOR_PARALLEL, stroke_width=4
        )
        dot_B = Dot(self.B, color=self.COLOR_PRIMARY, radius=0.08)
        dot_E = Dot(self.E, color=self.COLOR_PRIMARY, radius=0.08)
        label_B = Text("B", font="PingFang SC", font_size=20).next_to(dot_B, LEFT, buff=0.1)
        label_E = Text("E", font="PingFang SC", font_size=20).next_to(dot_E, RIGHT, buff=0.1)
        
        self.play(Create(pline2), run_time=0.6)
        self.play(
            FadeIn(dot_B, scale=0.5),
            FadeIn(dot_E, scale=0.5),
            Write(label_B),
            Write(label_E),
            run_time=0.5
        )
        
        # 平行线3
        pline3 = Line(
            self.C + LEFT * 1.5, self.F + RIGHT * 1.5,
            color=self.COLOR_PARALLEL, stroke_width=4
        )
        dot_C = Dot(self.C, color=self.COLOR_PRIMARY, radius=0.08)
        dot_F = Dot(self.F, color=self.COLOR_PRIMARY, radius=0.08)
        label_C = Text("C", font="PingFang SC", font_size=20).next_to(dot_C, LEFT, buff=0.1)
        label_F = Text("F", font="PingFang SC", font_size=20).next_to(dot_F, RIGHT, buff=0.1)
        
        self.play(Create(pline3), run_time=0.6)
        self.play(
            FadeIn(dot_C, scale=0.5),
            FadeIn(dot_F, scale=0.5),
            Write(label_C),
            Write(label_F),
            run_time=0.5
        )
        
        # Step 3: 依次高亮线段
        seg_AB = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        seg_BC = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        seg_DE = Line(self.D, self.E, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        seg_EF = Line(self.E, self.F, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        
        # AB
        self.play(Create(seg_AB), run_time=0.4)
        self.wait(0.3)
        self.play(seg_AB.animate.set_stroke(opacity=0.3), run_time=0.2)
        
        # BC
        self.play(Create(seg_BC), run_time=0.4)
        self.wait(0.3)
        self.play(seg_BC.animate.set_stroke(opacity=0.3), run_time=0.2)
        
        # DE
        self.play(Create(seg_DE), run_time=0.4)
        self.wait(0.3)
        self.play(seg_DE.animate.set_stroke(opacity=0.3), run_time=0.2)
        
        # EF
        self.play(Create(seg_EF), run_time=0.4)
        self.wait(0.3)
        self.play(seg_EF.animate.set_stroke(opacity=0.3), run_time=0.2)
        
        # Step 4: 显示比例公式
        formula = MathTex(
            r"\frac{AB}{BC} = \frac{DE}{EF}",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 验证数值
        ab_len = np.linalg.norm(self.B - self.A)
        bc_len = np.linalg.norm(self.C - self.B)
        de_len = np.linalg.norm(self.E - self.D)
        ef_len = np.linalg.norm(self.F - self.E)
        
        ratio_text = Text(
            f"验证: {ab_len/bc_len:.2f} = {de_len/ef_len:.2f}",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(ratio_text), run_time=0.5)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line1), FadeOut(line2),
            FadeOut(pline1), FadeOut(pline2), FadeOut(pline3),
            FadeOut(VGroup(dot_A, dot_B, dot_C, dot_D, dot_E, dot_F)),
            FadeOut(VGroup(label_A, label_B, label_C, label_D, label_E, label_F)),
            FadeOut(VGroup(seg_AB, seg_BC, seg_DE, seg_EF)),
            FadeOut(formula),
            FadeOut(ratio_text),
            run_time=0.6
        )
    
    def setup_parallel_lines_geometry(self):
        """初始化三条平行线的几何数据"""
        # 两条相交直线
        self.L1_start = np.array([-3, 3, 0])
        self.L1_dir = np.array([1, -1.5, 0])
        self.L1_dir = self.L1_dir / np.linalg.norm(self.L1_dir)
        self.L1_end = self.L1_start + self.L1_dir * 8
        
        self.L2_start = np.array([-2, 3, 0])
        self.L2_dir = np.array([1, -1.3, 0])
        self.L2_dir = self.L2_dir / np.linalg.norm(self.L2_dir)
        self.L2_end = self.L2_start + self.L2_dir * 8
        
        # 三条平行线的方向（水平方向，带一点倾斜）
        parallel_dir = np.array([1, 0.1, 0])
        parallel_dir = parallel_dir / np.linalg.norm(parallel_dir)
        
        # 平行线1通过的点
        y1 = 2.5
        point1 = np.array([0, y1, 0])
        
        # 平行线2通过的点
        y2 = 0.5
        point2 = np.array([0, y2, 0])
        
        # 平行线3通过的点
        y3 = -1.5
        point3 = np.array([0, y3, 0])
        
        # 计算交点
        calc = GeometryCalculator
        self.A = calc.line_intersection(self.L1_start, self.L1_dir, point1, parallel_dir)
        self.B = calc.line_intersection(self.L1_start, self.L1_dir, point2, parallel_dir)
        self.C = calc.line_intersection(self.L1_start, self.L1_dir, point3, parallel_dir)
        
        self.D = calc.line_intersection(self.L2_start, self.L2_dir, point1, parallel_dir)
        self.E = calc.line_intersection(self.L2_start, self.L2_dir, point2, parallel_dir)
        self.F = calc.line_intersection(self.L2_start, self.L2_dir, point3, parallel_dir)
        
        # 验证平行性
        vec_AD = self.D - self.A
        vec_BE = self.E - self.B
        vec_CF = self.F - self.C
        
        assert calc.are_parallel(vec_AD, vec_BE), "平行线1和平行线2不平行!"
        assert calc.are_parallel(vec_BE, vec_CF), "平行线2和平行线3不平行!"
        
        # 验证比例
        ab = np.linalg.norm(self.B - self.A)
        bc = np.linalg.norm(self.C - self.B)
        de = np.linalg.norm(self.E - self.D)
        ef = np.linalg.norm(self.F - self.E)
        
        ratio1 = ab / bc
        ratio2 = de / ef
        
        if abs(ratio1 - ratio2) > 1e-3:
            print(f"WARNING: 比例不相等! {ratio1:.4f} vs {ratio2:.4f}")
        else:
            print(f"✓ 比例验证通过: {ratio1:.4f} = {ratio2:.4f}")
    
    def show_triangle_corollary(self):
        """场景3: 三角形推论"""
        # 初始化几何数据
        self.setup_triangle_geometry()
        
        # 标题
        title = Text(
            "推论: 三角形中的平行线",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6)
        
        subtitle = Text(
            "平行于一边的直线截其他两边",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # Step 1: 创建三角形
        triangle = Polygon(
            self.tri_A, self.tri_B, self.tri_C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        dot_A = Dot(self.tri_A, color=WHITE, radius=0.08)
        dot_B = Dot(self.tri_B, color=WHITE, radius=0.08)
        dot_C = Dot(self.tri_C, color=WHITE, radius=0.08)
        
        label_A = Text("A", font="PingFang SC", font_size=24).next_to(dot_A, UP, buff=0.1)
        label_B = Text("B", font="PingFang SC", font_size=24).next_to(dot_B, DOWN+LEFT, buff=0.1)
        label_C = Text("C", font="PingFang SC", font_size=24).next_to(dot_C, DOWN+RIGHT, buff=0.1)
        
        self.play(Create(triangle), run_time=1.0)
        self.play(
            FadeIn(VGroup(dot_A, dot_B, dot_C), scale=0.5),
            Write(VGroup(label_A, label_B, label_C)),
            run_time=0.6
        )
        
        # Step 2: 点D和E动态滑入
        dot_D = Dot(self.tri_D, color=self.COLOR_SECONDARY, radius=0.08)
        dot_E = Dot(self.tri_E, color=self.COLOR_SECONDARY, radius=0.08)
        
        # 从A开始滑动到D
        dot_D_temp = Dot(self.tri_A, color=self.COLOR_SECONDARY, radius=0.08)
        dot_E_temp = Dot(self.tri_A, color=self.COLOR_SECONDARY, radius=0.08)
        
        self.play(FadeIn(dot_D_temp, scale=0.5), run_time=0.3)
        self.play(dot_D_temp.animate.move_to(self.tri_D), run_time=0.8)
        
        self.play(FadeIn(dot_E_temp, scale=0.5), run_time=0.3)
        self.play(dot_E_temp.animate.move_to(self.tri_E), run_time=0.8)
        
        # 添加标签
        label_D = Text("D", font="PingFang SC", font_size=24).next_to(dot_D_temp, LEFT, buff=0.1)
        label_E = Text("E", font="PingFang SC", font_size=24).next_to(dot_E_temp, RIGHT, buff=0.1)
        self.play(Write(label_D), Write(label_E), run_time=0.4)
        
        # Step 3: 创建线段DE
        line_DE = DashedLine(
            self.tri_D, self.tri_E,
            color=self.COLOR_PARALLEL,
            stroke_width=4,
            dash_length=0.1
        )
        
        self.play(Create(line_DE), run_time=0.8)
        
        # 标注平行符号
        parallel_mark = MathTex(
            r"DE \parallel BC",
            font_size=28,
            color=self.COLOR_PARALLEL
        ).move_to(UP * 1.5)
        
        self.play(Write(parallel_mark), run_time=0.6)
        
        # Step 4: 依次高亮线段
        seg_AD = Line(self.tri_A, self.tri_D, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        seg_DB = Line(self.tri_D, self.tri_B, color=self.COLOR_SECONDARY, stroke_width=6)
        seg_AE = Line(self.tri_A, self.tri_E, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        seg_EC = Line(self.tri_E, self.tri_C, color=self.COLOR_SECONDARY, stroke_width=6)
        
        self.play(Create(seg_AD), run_time=0.4)
        self.wait(0.2)
        self.play(Create(seg_DB), run_time=0.4)
        self.wait(0.2)
        self.play(Create(seg_AE), run_time=0.4)
        self.wait(0.2)
        self.play(Create(seg_EC), run_time=0.4)
        self.wait(0.3)
        
        # Step 5: 显示比例公式
        formula = MathTex(
            r"\frac{AD}{DB} = \frac{AE}{EC}",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 验证数值
        ad_len = np.linalg.norm(self.tri_D - self.tri_A)
        db_len = np.linalg.norm(self.tri_B - self.tri_D)
        ae_len = np.linalg.norm(self.tri_E - self.tri_A)
        ec_len = np.linalg.norm(self.tri_C - self.tri_E)
        
        ratio_text = Text(
            f"验证: {ad_len/db_len:.2f} = {ae_len/ec_len:.2f}",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(ratio_text), run_time=0.5)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(triangle),
            FadeOut(VGroup(dot_A, dot_B, dot_C, dot_D_temp, dot_E_temp)),
            FadeOut(VGroup(label_A, label_B, label_C, label_D, label_E)),
            FadeOut(line_DE),
            FadeOut(parallel_mark),
            FadeOut(VGroup(seg_AD, seg_DB, seg_AE, seg_EC)),
            FadeOut(formula),
            FadeOut(ratio_text),
            run_time=0.6
        )
    
    def setup_triangle_geometry(self):
        """初始化三角形的几何数据"""
        # 三角形顶点
        self.tri_A = np.array([0, 2.5, 0])
        self.tri_B = np.array([-2.5, -1, 0])
        self.tri_C = np.array([2.5, -1, 0])
        
        # 点D在AB上，点E在AC上，比例为 2:3
        t = 2 / 5  # AD/AB = 2/5
        
        calc = GeometryCalculator
        self.tri_D = calc.point_on_line(self.tri_A, self.tri_B, t)
        self.tri_E = calc.point_on_line(self.tri_A, self.tri_C, t)
        
        # 验证DE平行于BC
        vec_DE = self.tri_E - self.tri_D
        vec_BC = self.tri_C - self.tri_B
        
        assert calc.are_parallel(vec_DE, vec_BC), "DE不平行于BC!"
        
        # 验证比例
        ad = np.linalg.norm(self.tri_D - self.tri_A)
        db = np.linalg.norm(self.tri_B - self.tri_D)
        ae = np.linalg.norm(self.tri_E - self.tri_A)
        ec = np.linalg.norm(self.tri_C - self.tri_E)
        
        ratio1 = ad / db
        ratio2 = ae / ec
        
        if abs(ratio1 - ratio2) > 1e-3:
            print(f"WARNING: 三角形比例不相等! {ratio1:.4f} vs {ratio2:.4f}")
        else:
            print(f"✓ 三角形比例验证通过: {ratio1:.4f} = {ratio2:.4f}")
    
    def show_converse_theorem(self):
        """场景4: 逆定理"""
        # 重用三角形几何数据
        
        # 标题
        title = Text(
            "逆定理: 比例相等则平行",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # Step 1: 显示比例条件
        condition_text = Text(
            "已知:",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.8 + LEFT * 2.5)
        
        condition = MathTex(
            r"\frac{AD}{DB} = \frac{AE}{EC}",
            font_size=36,
            color=self.COLOR_FORMULA
        ).next_to(condition_text, RIGHT, buff=0.3)
        
        # 创建三角形 (简化版本)
        triangle = Polygon(
            self.tri_A, self.tri_B, self.tri_C,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        )
        
        dot_D = Dot(self.tri_D, color=self.COLOR_SECONDARY, radius=0.08)
        dot_E = Dot(self.tri_E, color=self.COLOR_SECONDARY, radius=0.08)
        
        self.play(
            Write(condition_text),
            Write(condition),
            Create(triangle),
            FadeIn(VGroup(dot_D, dot_E), scale=0.5),
            run_time=1.0
        )
        
        # Step 2: 创建线段DE
        line_DE = Line(
            self.tri_D, self.tri_E,
            color=GRAY,
            stroke_width=3
        )
        
        self.play(Create(line_DE), run_time=0.6)
        self.wait(0.5)
        
        # Step 3: 验证平行 - 闪烁效果
        self.play(
            line_DE.animate.set_color(self.COLOR_PARALLEL).set_stroke(width=5),
            run_time=0.5
        )
        self.play(Flash(line_DE, color=self.COLOR_PARALLEL, flash_radius=0.5), run_time=0.4)
        
        # Step 4: 显示结论
        conclusion = MathTex(
            r"\therefore DE \parallel BC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(conclusion), run_time=1.0)
        self.wait(2.0)  # 关键停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(condition_text),
            FadeOut(condition),
            FadeOut(triangle),
            FadeOut(VGroup(dot_D, dot_E)),
            FadeOut(line_DE),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_application(self):
        """场景5: 应用示例"""
        # 标题
        title = Text(
            "例题: 计算未知线段",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 三角形 (带数值)
        A = np.array([0, 2, 0])
        B = np.array([-2, -1.5, 0])
        C = np.array([2.5, -1.5, 0])
        
        # D, E 使得 AD=2, DB=3, AE=4, EC=?
        # AD/AB = 2/5
        t = 2 / 5
        D = A + t * (B - A)
        E = A + t * (C - A)
        
        triangle = Polygon(A, B, C, color=self.COLOR_PRIMARY, stroke_width=3)
        line_DE = DashedLine(D, E, color=self.COLOR_PARALLEL, stroke_width=4, dash_length=0.1)
        
        # 点和标签
        dots = VGroup(
            Dot(A, radius=0.06),
            Dot(B, radius=0.06),
            Dot(C, radius=0.06),
            Dot(D, color=self.COLOR_SECONDARY, radius=0.06),
            Dot(E, color=self.COLOR_SECONDARY, radius=0.06)
        )
        
        labels = VGroup(
            Text("A", font="PingFang SC", font_size=20).next_to(A, UP, buff=0.08),
            Text("B", font="PingFang SC", font_size=20).next_to(B, LEFT, buff=0.08),
            Text("C", font="PingFang SC", font_size=20).next_to(C, RIGHT, buff=0.08),
            Text("D", font="PingFang SC", font_size=20).next_to(D, LEFT, buff=0.08),
            Text("E", font="PingFang SC", font_size=20).next_to(E, RIGHT, buff=0.08)
        )
        
        self.play(
            Create(triangle),
            Create(line_DE),
            FadeIn(dots, scale=0.5),
            Write(labels),
            run_time=1.2
        )
        
        # 标注已知量
        ad_label = Text("AD=2", font="PingFang SC", font_size=18, color=YELLOW).move_to((A + D) / 2 + LEFT * 0.5)
        db_label = Text("DB=3", font="PingFang SC", font_size=18, color=YELLOW).move_to((D + B) / 2 + LEFT * 0.5)
        ae_label = Text("AE=4", font="PingFang SC", font_size=18, color=YELLOW).move_to((A + E) / 2 + RIGHT * 0.5)
        ec_label = Text("EC=?", font="PingFang SC", font_size=18, color=self.COLOR_HIGHLIGHT).move_to((E + C) / 2 + RIGHT * 0.5)
        
        self.play(
            Write(VGroup(ad_label, db_label, ae_label, ec_label)),
            run_time=1.0
        )
        
        # 解题过程
        step1 = MathTex(
            r"\frac{AD}{DB} = \frac{AE}{EC}",
            font_size=32
        ).move_to(DOWN * 3.5)
        
        self.play(Write(step1), run_time=0.8)
        
        step2 = MathTex(
            r"\frac{2}{3} = \frac{4}{EC}",
            font_size=32
        ).move_to(DOWN * 4.5)
        
        self.play(
            TransformMatchingTex(step1.copy(), step2),
            run_time=0.8
        )
        
        step3 = MathTex(
            r"EC = 6",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(step3), run_time=0.8)
        
        # 闪烁答案
        self.play(Flash(step3, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 更新标签
        ec_label_new = Text("EC=6", font="PingFang SC", font_size=18, color=self.COLOR_HIGHLIGHT).move_to(ec_label.get_center())
        self.play(Transform(ec_label, ec_label_new), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(triangle),
            FadeOut(line_DE),
            FadeOut(dots),
            FadeOut(labels),
            FadeOut(VGroup(ad_label, db_label, ae_label, ec_label)),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景6: 片尾关注"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 平行线装饰图标
        icon_lines = VGroup()
        for i in range(3):
            line = Line(
                LEFT * 1.5, RIGHT * 1.5,
                color=self.COLOR_PARALLEL,
                stroke_width=3
            ).shift(DOWN * (2 + i * 0.5))
            icon_lines.add(line)
        
        self.play(
            *[Create(line) for line in icon_lines],
            run_time=0.8
        )
        
        # 旋转动画
        self.play(
            Rotate(icon_lines, angle=PI, run_time=1.5)
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icon_lines),
            run_time=1.0
        )


# 运行命令:
# manim -pql parallel_lines_theorem.py ParallelLinesTheorem  # 快速预览
# manim -qh parallel_lines_theorem.py ParallelLinesTheorem   # 高质量渲染