"""
拿破仑点 (Napoleon's Point) 数学教学动画
Napoleon's Point Mathematical Teaching Animation

内容: 拿破仑定理 - 以三角形各边向外/内作正三角形，连接中心得正三角形
目标观众: 高中生 / 数学竞赛
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

运行命令:
manim -pql napoleon_point.py NapoleonPoint     # 快速预览
manim -qh napoleon_point.py NapoleonPoint      # 高质量渲染
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ==================== 几何计算工具类 ====================
class GeometryCalculator:
    """精确几何计算工具类 - 所有几何计算必须使用此类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """计算中点"""
        return (P1 + P2) / 2
    
    @staticmethod
    def centroid(A, B, C):
        """三角形重心"""
        return (A + B + C) / 3
    
    @staticmethod
    def distance(P1, P2):
        """两点间距离"""
        return np.linalg.norm(P2 - P1)
    
    @staticmethod
    def construct_equilateral_triangle(P1, P2, direction_point, outward=True):
        """
        以P1P2为底边构造正三角形
        
        参数:
            P1, P2: 底边两端点
            direction_point: 用于判断方向的参考点（通常是原三角形的第三个顶点）
            outward: True表示向外，False表示向内
        
        返回:
            第三个顶点P3的坐标
        """
        # 计算中点
        mid = (P1 + P2) / 2
        
        # 计算边向量和长度
        edge_vec = P2 - P1
        edge_length = np.linalg.norm(edge_vec)
        
        # 正三角形高度
        height = edge_length * np.sqrt(3) / 2
        
        # 垂直方向（逆时针旋转90度）
        perp = np.array([-edge_vec[1], edge_vec[0], 0])
        perp_normalized = perp / np.linalg.norm(perp)
        
        # 判断direction_point在P1P2的哪一侧
        to_dir = direction_point - P1
        cross_z = edge_vec[0] * to_dir[1] - edge_vec[1] * to_dir[0]
        
        # 如果outward=True，选择与direction_point相反的一侧
        # 如果outward=False，选择与direction_point相同的一侧
        if outward:
            # 向外: 与direction_point相反侧
            if cross_z > 0:
                perp_normalized = -perp_normalized
        else:
            # 向内: 与direction_point相同侧
            if cross_z < 0:
                perp_normalized = -perp_normalized
        
        # 第三个顶点
        P3 = mid + height * perp_normalized
        
        return P3
    
    @staticmethod
    def verify_equilateral(P1, P2, P3, eps=1e-4):
        """验证三点构成正三角形"""
        a = GeometryCalculator.distance(P1, P2)
        b = GeometryCalculator.distance(P2, P3)
        c = GeometryCalculator.distance(P3, P1)
        
        is_equilateral = (abs(a - b) < eps and abs(b - c) < eps)
        
        if not is_equilateral:
            print(f"WARNING: 不是正三角形! 边长: {a:.6f}, {b:.6f}, {c:.6f}")
        
        return is_equilateral


# ==================== 主场景类 ====================
class NapoleonPoint(Scene):
    """
    拿破仑点教学动画主场景
    
    场景顺序:
    1. 开场钩子
    2. 外侧正三角形构造
    3. 内侧正三角形构造
    4. 拿破仑定理陈述
    5. 神奇性质揭示
    6. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"           # 蓝色 - 主三角形
        self.COLOR_OUTER_TRIANGLE = "#e74c3c"    # 红色 - 外侧正三角形
        self.COLOR_INNER_TRIANGLE = "#2ecc71"    # 绿色 - 内侧正三角形
        self.COLOR_NAPOLEON_OUTER = "#f39c12"    # 橙色 - 外拿破仑三角形
        self.COLOR_NAPOLEON_INNER = "#9b59b6"    # 紫色 - 内拿破仑三角形
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_TEXT = WHITE
        
        # 字体大小配置
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "small": 18,
        }
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_outer_construction()
        self.show_inner_construction()
        self.show_napoleon_theorem()
        self.show_amazing_property()
        self.show_outro()
    
    def setup_geometry(self):
        """统一初始化所有几何元素"""
        print("\n========== 几何初始化开始 ==========")
        
        # ===== 基准参数 =====
        self.SCALE = 1.2
        self.OFFSET = UP * 0.5
        
        # ===== 主三角形顶点（任意三角形）=====
        # 使用斜三角形便于展示所有特性
        self.A = np.array([-2.5, 1.2, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.2, -0.8, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([-0.8, -1.8, 0]) * self.SCALE + self.OFFSET
        
        print(f"主三角形顶点:")
        print(f"  A = {self.A}")
        print(f"  B = {self.B}")
        print(f"  C = {self.C}")
        
        # ===== 边长 =====
        self.a = GeometryCalculator.distance(self.B, self.C)  # BC
        self.b = GeometryCalculator.distance(self.C, self.A)  # CA
        self.c = GeometryCalculator.distance(self.A, self.B)  # AB
        
        print(f"\n边长:")
        print(f"  a (BC) = {self.a:.4f}")
        print(f"  b (CA) = {self.b:.4f}")
        print(f"  c (AB) = {self.c:.4f}")
        
        # ===== 重心 =====
        self.G = GeometryCalculator.centroid(self.A, self.B, self.C)
        print(f"\n重心 G = {self.G}")
        
        # ===== 外侧正三角形构造 =====
        print("\n----- 外侧正三角形构造 -----")
        
        # 以BC为底，向外作正三角形△BCA'
        self.A_outer = GeometryCalculator.construct_equilateral_triangle(
            self.B, self.C, self.A, outward=True
        )
        print(f"A' (外) = {self.A_outer}")
        
        # 以CA为底，向外作正三角形△CAB'
        self.B_outer = GeometryCalculator.construct_equilateral_triangle(
            self.C, self.A, self.B, outward=True
        )
        print(f"B' (外) = {self.B_outer}")
        
        # 以AB为底，向外作正三角形△ABC'
        self.C_outer = GeometryCalculator.construct_equilateral_triangle(
            self.A, self.B, self.C, outward=True
        )
        print(f"C' (外) = {self.C_outer}")
        
        # 验证外侧正三角形
        assert GeometryCalculator.verify_equilateral(self.B, self.C, self.A_outer), "△BCA' 不是正三角形!"
        assert GeometryCalculator.verify_equilateral(self.C, self.A, self.B_outer), "△CAB' 不是正三角形!"
        assert GeometryCalculator.verify_equilateral(self.A, self.B, self.C_outer), "△ABC' 不是正三角形!"
        print("✓ 外侧三个正三角形验证通过")
        
        # 外侧正三角形的中心
        self.O_A = GeometryCalculator.centroid(self.B, self.C, self.A_outer)
        self.O_B = GeometryCalculator.centroid(self.C, self.A, self.B_outer)
        self.O_C = GeometryCalculator.centroid(self.A, self.B, self.C_outer)
        
        print(f"\n外侧正三角形中心:")
        print(f"  O_A = {self.O_A}")
        print(f"  O_B = {self.O_B}")
        print(f"  O_C = {self.O_C}")
        
        # 外拿破仑三角形（连接三个中心）
        # 验证这是正三角形（拿破仑定理）
        assert GeometryCalculator.verify_equilateral(self.O_A, self.O_B, self.O_C), "外拿破仑三角形不是正三角形!"
        print("✓ 外拿破仑三角形是正三角形（拿破仑定理验证）")
        
        # 外拿破仑点（外拿破仑三角形的中心）
        self.N_outer = GeometryCalculator.centroid(self.O_A, self.O_B, self.O_C)
        print(f"外拿破仑点 N_outer = {self.N_outer}")
        
        # ===== 内侧正三角形构造 =====
        print("\n----- 内侧正三角形构造 -----")
        
        # 以BC为底，向内作正三角形△BCA''
        self.A_inner = GeometryCalculator.construct_equilateral_triangle(
            self.B, self.C, self.A, outward=False
        )
        print(f"A'' (内) = {self.A_inner}")
        
        # 以CA为底，向内作正三角形△CAB''
        self.B_inner = GeometryCalculator.construct_equilateral_triangle(
            self.C, self.A, self.B, outward=False
        )
        print(f"B'' (内) = {self.B_inner}")
        
        # 以AB为底，向内作正三角形△ABC''
        self.C_inner = GeometryCalculator.construct_equilateral_triangle(
            self.A, self.B, self.C, outward=False
        )
        print(f"C'' (内) = {self.C_inner}")
        
        # 验证内侧正三角形
        assert GeometryCalculator.verify_equilateral(self.B, self.C, self.A_inner), "△BCA'' 不是正三角形!"
        assert GeometryCalculator.verify_equilateral(self.C, self.A, self.B_inner), "△CAB'' 不是正三角形!"
        assert GeometryCalculator.verify_equilateral(self.A, self.B, self.C_inner), "△ABC'' 不是正三角形!"
        print("✓ 内侧三个正三角形验证通过")
        
        # 内侧正三角形的中心
        self.I_A = GeometryCalculator.centroid(self.B, self.C, self.A_inner)
        self.I_B = GeometryCalculator.centroid(self.C, self.A, self.B_inner)
        self.I_C = GeometryCalculator.centroid(self.A, self.B, self.C_inner)
        
        print(f"\n内侧正三角形中心:")
        print(f"  I_A = {self.I_A}")
        print(f"  I_B = {self.I_B}")
        print(f"  I_C = {self.I_C}")
        
        # 内拿破仑三角形（连接三个中心）
        # 验证这是正三角形（拿破仑定理）
        assert GeometryCalculator.verify_equilateral(self.I_A, self.I_B, self.I_C), "内拿破仑三角形不是正三角形!"
        print("✓ 内拿破仑三角形是正三角形（拿破仑定理验证）")
        
        # 内拿破仑点（内拿破仑三角形的中心）
        self.N_inner = GeometryCalculator.centroid(self.I_A, self.I_B, self.I_C)
        print(f"内拿破仑点 N_inner = {self.N_inner}")
        
        # ===== 验证神奇性质: 两拿破仑点连线中点 = 重心 =====
        midpoint_N = GeometryCalculator.midpoint(self.N_outer, self.N_inner)
        distance_to_G = GeometryCalculator.distance(midpoint_N, self.G)
        
        print(f"\n----- 神奇性质验证 -----")
        print(f"两拿破仑点连线中点 = {midpoint_N}")
        print(f"三角形重心 G = {self.G}")
        print(f"距离差 = {distance_to_G:.10f}")
        
        if distance_to_G < 1e-4:
            print("✓ 神奇性质验证: 中点 = 重心!")
        else:
            print(f"⚠ WARNING: 中点与重心距离 = {distance_to_G}")
        
        print("\n========== 几何初始化完成 ==========\n")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        print("Scene 1: 开场钩子")
        
        # 作者信息（顶部小字）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "任意三角形中隐藏的秘密",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 主三角形
        self.triangle = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(self.triangle), run_time=1.2)
        
        # 顶点标签
        label_A = Text("A", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE)
        label_A.next_to(self.A, DL, buff=0.15)
        
        label_B = Text("B", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE)
        label_B.next_to(self.B, DR, buff=0.15)
        
        label_C = Text("C", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=WHITE)
        label_C.next_to(self.C, DOWN, buff=0.15)
        
        self.labels_ABC = VGroup(label_A, label_B, label_C)
        
        self.play(FadeIn(self.labels_ABC), run_time=0.5)
        
        # 提示文字
        hint = Text(
            "拿破仑点是什么?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), FadeOut(hint), run_time=0.4)
    
    def show_outer_construction(self):
        """场景2: 外侧正三角形构造"""
        print("Scene 2: 外侧正三角形构造")
        
        # 标题
        title = Text(
            "外拿破仑点构造",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_OUTER_TRIANGLE
        ).move_to(UP * 6)
        
        subtitle = Text(
            "以各边为底, 向外作正三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # Step 1: 构造第一个外侧正三角形△BCA'
        explain_1 = Text(
            "以BC为底边",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain_1), run_time=0.4)
        
        # 高亮BC边
        line_BC = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=5)
        self.play(Create(line_BC), run_time=0.5)
        
        # 创建外侧正三角形△BCA'
        triangle_BCA_outer = Polygon(
            self.B, self.C, self.A_outer,
            color=self.COLOR_OUTER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_OUTER_TRIANGLE
        )
        
        self.play(Create(triangle_BCA_outer), run_time=1.5)
        
        # 标记A'点
        dot_A_outer = Dot(self.A_outer, color=self.COLOR_OUTER_TRIANGLE, radius=0.08)
        label_A_outer = Text("A'", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_A_outer.next_to(dot_A_outer, UP, buff=0.1)
        
        self.play(FadeIn(dot_A_outer), FadeIn(label_A_outer), run_time=0.4)
        
        # 标记中心O_A
        dot_O_A = Dot(self.O_A, color=self.COLOR_OUTER_TRIANGLE, radius=0.10)
        label_O_A = MathTex("O_A", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_O_A.next_to(dot_O_A, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(dot_O_A, scale=0.5),
            Flash(dot_O_A, color=self.COLOR_OUTER_TRIANGLE),
            FadeIn(label_O_A),
            run_time=0.6
        )
        
        self.play(FadeOut(line_BC), FadeOut(explain_1), run_time=0.3)
        
        # Step 2 & 3: 快速构造另外两个外侧正三角形
        triangle_CAB_outer = Polygon(
            self.C, self.A, self.B_outer,
            color=self.COLOR_OUTER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_OUTER_TRIANGLE
        )
        
        triangle_ABC_outer = Polygon(
            self.A, self.B, self.C_outer,
            color=self.COLOR_OUTER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_OUTER_TRIANGLE
        )
        
        self.play(
            Create(triangle_CAB_outer),
            Create(triangle_ABC_outer),
            run_time=1.5
        )
        
        # 标记B', C'点和中心
        dot_B_outer = Dot(self.B_outer, color=self.COLOR_OUTER_TRIANGLE, radius=0.08)
        dot_C_outer = Dot(self.C_outer, color=self.COLOR_OUTER_TRIANGLE, radius=0.08)
        
        label_B_outer = Text("B'", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_B_outer.next_to(dot_B_outer, LEFT, buff=0.1)
        
        label_C_outer = Text("C'", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_C_outer.next_to(dot_C_outer, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(dot_B_outer),
            FadeIn(dot_C_outer),
            FadeIn(label_B_outer),
            FadeIn(label_C_outer),
            run_time=0.5
        )
        
        # 标记中心O_B, O_C
        dot_O_B = Dot(self.O_B, color=self.COLOR_OUTER_TRIANGLE, radius=0.10)
        dot_O_C = Dot(self.O_C, color=self.COLOR_OUTER_TRIANGLE, radius=0.10)
        
        label_O_B = MathTex("O_B", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_O_B.next_to(dot_O_B, UL, buff=0.1)
        
        label_O_C = MathTex("O_C", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_O_C.next_to(dot_O_C, DOWN, buff=0.1)
        
        self.play(
            FadeIn(dot_O_B, scale=0.5),
            FadeIn(dot_O_C, scale=0.5),
            Flash(dot_O_B, color=self.COLOR_OUTER_TRIANGLE),
            Flash(dot_O_C, color=self.COLOR_OUTER_TRIANGLE),
            FadeIn(label_O_B),
            FadeIn(label_O_C),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # Step 4: 连接三个中心形成外拿破仑三角形
        text_connect = Text(
            "连接三个中心",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(Write(text_connect), run_time=0.5)
        
        # 外拿破仑三角形
        self.napoleon_outer_triangle = Polygon(
            self.O_A, self.O_B, self.O_C,
            color=self.COLOR_NAPOLEON_OUTER,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_NAPOLEON_OUTER
        )
        
        self.play(Create(self.napoleon_outer_triangle), run_time=1.5)
        
        # 强调
        self.play(Indicate(self.napoleon_outer_triangle, color=self.COLOR_HIGHLIGHT), run_time=0.8)
        
        text_equilateral = Text(
            "这是一个正三角形!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.3)
        
        self.play(FadeIn(text_equilateral, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # Step 5: 标记外拿破仑点
        self.dot_N_outer = Dot(self.N_outer, color=GOLD, radius=0.14)
        
        label_N_outer = Text("外拿破仑点", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=GOLD)
        label_N_outer.next_to(self.dot_N_outer, RIGHT, buff=0.15)
        
        self.play(
            FadeIn(self.dot_N_outer, scale=0.5),
            Flash(self.dot_N_outer, color=GOLD, flash_radius=0.4),
            run_time=0.6
        )
        self.play(Write(label_N_outer), run_time=0.5)
        self.wait(1.0)
        
        # 清理临时元素，保留关键元素
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(text_connect),
            FadeOut(text_equilateral),
            FadeOut(label_N_outer),
            # 淡化外侧正三角形
            triangle_BCA_outer.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            triangle_CAB_outer.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            triangle_ABC_outer.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            # 淡化顶点标签
            FadeOut(dot_A_outer),
            FadeOut(dot_B_outer),
            FadeOut(dot_C_outer),
            FadeOut(label_A_outer),
            FadeOut(label_B_outer),
            FadeOut(label_C_outer),
            run_time=0.6
        )
        
        # 保存外侧正三角形对象用于后续
        self.outer_triangles = VGroup(triangle_BCA_outer, triangle_CAB_outer, triangle_ABC_outer)
        self.outer_centers = VGroup(dot_O_A, dot_O_B, dot_O_C)
        self.outer_center_labels = VGroup(label_O_A, label_O_B, label_O_C)
    
    def show_inner_construction(self):
        """场景3: 内侧正三角形构造"""
        print("Scene 3: 内侧正三角形构造")
        
        # 标题
        title = Text(
            "内拿破仑点构造",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_INNER_TRIANGLE
        ).move_to(UP * 6)
        
        subtitle = Text(
            "以各边为底, 向内作正三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(UP * 5.3)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 快速构造三个内侧正三角形（观众已理解流程）
        triangle_BCA_inner = Polygon(
            self.B, self.C, self.A_inner,
            color=self.COLOR_INNER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_INNER_TRIANGLE
        )
        
        triangle_CAB_inner = Polygon(
            self.C, self.A, self.B_inner,
            color=self.COLOR_INNER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_INNER_TRIANGLE
        )
        
        triangle_ABC_inner = Polygon(
            self.A, self.B, self.C_inner,
            color=self.COLOR_INNER_TRIANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.COLOR_INNER_TRIANGLE
        )
        
        self.play(
            Create(triangle_BCA_inner),
            Create(triangle_CAB_inner),
            Create(triangle_ABC_inner),
            run_time=2.0
        )
        
        # 标记三个中心
        dot_I_A = Dot(self.I_A, color=self.COLOR_INNER_TRIANGLE, radius=0.10)
        dot_I_B = Dot(self.I_B, color=self.COLOR_INNER_TRIANGLE, radius=0.10)
        dot_I_C = Dot(self.I_C, color=self.COLOR_INNER_TRIANGLE, radius=0.10)
        
        label_I_A = MathTex("I_A", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_I_A.next_to(dot_I_A, DOWN, buff=0.1)
        
        label_I_B = MathTex("I_B", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_I_B.next_to(dot_I_B, LEFT, buff=0.1)
        
        label_I_C = MathTex("I_C", font_size=self.FONT_SIZES["small"], color=WHITE)
        label_I_C.next_to(dot_I_C, UP, buff=0.1)
        
        self.play(
            FadeIn(dot_I_A, scale=0.5),
            FadeIn(dot_I_B, scale=0.5),
            FadeIn(dot_I_C, scale=0.5),
            Flash(dot_I_A, color=self.COLOR_INNER_TRIANGLE),
            Flash(dot_I_B, color=self.COLOR_INNER_TRIANGLE),
            Flash(dot_I_C, color=self.COLOR_INNER_TRIANGLE),
            FadeIn(label_I_A),
            FadeIn(label_I_B),
            FadeIn(label_I_C),
            run_time=0.8
        )
        
        # 连接内侧中心
        text_connect = Text(
            "连接内侧中心",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(Write(text_connect), run_time=0.5)
        
        # 内拿破仑三角形
        self.napoleon_inner_triangle = Polygon(
            self.I_A, self.I_B, self.I_C,
            color=self.COLOR_NAPOLEON_INNER,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_NAPOLEON_INNER
        )
        
        self.play(Create(self.napoleon_inner_triangle), run_time=1.5)
        
        text_also = Text(
            "同样是正三角形!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.3)
        
        self.play(FadeIn(text_also, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 标记内拿破仑点
        self.dot_N_inner = Dot(self.N_inner, color=PURPLE, radius=0.14)
        
        label_N_inner = Text("内拿破仑点", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=PURPLE)
        label_N_inner.next_to(self.dot_N_inner, LEFT, buff=0.15)
        
        self.play(
            FadeIn(self.dot_N_inner, scale=0.5),
            Flash(self.dot_N_inner, color=PURPLE, flash_radius=0.4),
            run_time=0.6
        )
        self.play(Write(label_N_inner), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(text_connect),
            FadeOut(text_also),
            FadeOut(label_N_inner),
            # 淡化内侧正三角形
            triangle_BCA_inner.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            triangle_CAB_inner.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            triangle_ABC_inner.animate.set_fill_opacity(0.05).set_stroke_opacity(0.3),
            run_time=0.6
        )
        
        # 保存内侧正三角形对象
        self.inner_triangles = VGroup(triangle_BCA_inner, triangle_CAB_inner, triangle_ABC_inner)
        self.inner_centers = VGroup(dot_I_A, dot_I_B, dot_I_C)
        self.inner_center_labels = VGroup(label_I_A, label_I_B, label_I_C)
    
    def show_napoleon_theorem(self):
        """场景4: 拿破仑定理陈述"""
        print("Scene 4: 拿破仑定理陈述")
        
        # 缩小图形并上移
        all_visible = VGroup(
            self.triangle,
            self.labels_ABC,
            self.outer_triangles,
            self.outer_centers,
            self.outer_center_labels,
            self.napoleon_outer_triangle,
            self.dot_N_outer,
            self.inner_triangles,
            self.inner_centers,
            self.inner_center_labels,
            self.napoleon_inner_triangle,
            self.dot_N_inner
        )
        
        self.play(
            all_visible.animate.scale(0.65).move_to(UP * 3),
            run_time=1.0
        )
        
        # 定理标题
        theorem_title = Text(
            "拿破仑定理",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 1.2)
        
        self.play(Write(theorem_title), run_time=0.8)
        
        # 定理陈述
        statement_1 = Text(
            "1. 以任意三角形各边为底",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"]+2,
            color=WHITE
        ).move_to(UP * 0.3)
        
        statement_2 = Text(
            "2. 向外/内作正三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"]+2,
            color=WHITE
        ).next_to(statement_1, DOWN, buff=0.3, aligned_edge=LEFT)
        
        statement_3 = Text(
            "3. 连接三个正三角形的中心",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"]+2,
            color=WHITE
        ).next_to(statement_2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        statement_4 = Text(
            "4. 得到的三角形必为正三角形",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"]+2,
            color=self.COLOR_HIGHLIGHT
        ).next_to(statement_3, DOWN, buff=0.3, aligned_edge=LEFT)
        
        statements = VGroup(statement_1, statement_2, statement_3, statement_4)
        statements.move_to(ORIGIN + DOWN * 0.3)
        
        self.play(FadeIn(statement_1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        
        self.play(FadeIn(statement_2, shift=UP * 0.2), run_time=0.6)
        self.play(Indicate(self.napoleon_outer_triangle), run_time=0.5)
        self.wait(0.3)
        
        self.play(FadeIn(statement_3, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        
        self.play(FadeIn(statement_4, shift=UP * 0.2), run_time=0.6)
        
        # 强调"必为正三角形"
        emphasis = Text(
            "必然是正三角形!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GOLD,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        self.play(Write(emphasis), run_time=0.8)
        
        # 两个拿破仑点闪烁
        self.play(
            Flash(self.dot_N_outer, color=GOLD),
            Flash(self.dot_N_inner, color=PURPLE),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(theorem_title),
            FadeOut(statements),
            FadeOut(emphasis),
            run_time=0.6
        )
    
    def show_amazing_property(self):
        """场景5: 神奇性质揭示"""
        print("Scene 5: 神奇性质揭示")
        
        # 放大图形回到中心
        all_visible = VGroup(
            self.triangle,
            self.labels_ABC,
            self.outer_triangles,
            self.outer_centers,
            self.outer_center_labels,
            self.napoleon_outer_triangle,
            self.dot_N_outer,
            self.inner_triangles,
            self.inner_centers,
            self.inner_center_labels,
            self.napoleon_inner_triangle,
            self.dot_N_inner
        )
        
        self.play(
            all_visible.animate.scale(1/0.65).move_to(UP * 0.5),
            run_time=0.8
        )
        
        # 提示神奇性质
        amazing_text = Text(
            "更神奇的性质...",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(amazing_text), run_time=0.6)
        self.wait(0.5)
        
        # 连接两个拿破仑点
        line_N = DashedLine(
            self.N_outer, self.N_inner,
            color=GOLD,
            stroke_width=3,
            dash_length=0.1
        )
        
        self.play(Create(line_N), run_time=1.0)
        
        # 高亮两个点
        self.play(
            Indicate(self.dot_N_outer),
            Indicate(self.dot_N_inner),
            run_time=0.6
        )
        
        # 标记中点
        midpoint_N = GeometryCalculator.midpoint(self.N_outer, self.N_inner)
        dot_M = Dot(midpoint_N, color=YELLOW, radius=0.10)
        
        label_M = Text("M", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["small"], color=YELLOW)
        label_M.next_to(dot_M, UP, buff=0.1)
        
        self.play(
            FadeIn(dot_M, scale=0.5),
            FadeIn(label_M),
            run_time=0.5
        )
        
        text_midpoint = Text(
            "连线的中点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(text_midpoint), run_time=0.4)
        self.wait(0.8)
        
        # 显示重心
        dot_G = Dot(self.G, color=GREEN, radius=0.12)
        
        label_G = Text("G", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["label"], color=GREEN, weight=BOLD)
        label_G.next_to(dot_G, DOWN, buff=0.15)
        
        text_centroid = Text(
            "三角形的重心",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GREEN
        ).move_to(DOWN * 6.3)
        
        self.play(
            FadeIn(dot_G, scale=0.5),
            Flash(dot_G, color=GREEN, flash_radius=0.4),
            FadeIn(label_G),
            FadeIn(text_centroid),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 中点移动到重心（展示重合）
        self.play(
            dot_M.animate.move_to(self.G),
            label_M.animate.next_to(dot_G, UP, buff=0.1),
            run_time=1.2,
            rate_func=there_and_back_with_pause
        )
        
        # 爆炸效果强调重合
        self.play(
            Flash(dot_G, color=GOLD, flash_radius=0.6, num_lines=16),
            run_time=0.8
        )
        
        # 结论
        conclusion = Text(
            "中点恰好是重心!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GOLD,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        self.play(Write(conclusion), run_time=1.0)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(amazing_text),
            FadeOut(line_N),
            FadeOut(dot_M),
            FadeOut(label_M),
            FadeOut(dot_G),
            FadeOut(label_G),
            FadeOut(text_midpoint),
            FadeOut(text_centroid),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 总结与片尾"""
        print("Scene 8: 总结与片尾")
        
        # 清理并缩小图形
        all_visible = VGroup(
            self.triangle,
            self.labels_ABC,
            self.outer_triangles,
            self.outer_centers,
            self.outer_center_labels,
            self.napoleon_outer_triangle,
            self.dot_N_outer,
            self.inner_triangles,
            self.inner_centers,
            self.inner_center_labels,
            self.napoleon_inner_triangle,
            self.dot_N_inner
        )
        
        self.play(
            all_visible.animate.scale(0.4).move_to(UP * 5),
            run_time=0.8
        )
        
        # 要点回顾卡片
        card_1 = self.create_summary_card(
            "拿破仑定理: 必得正三角形",
            self.COLOR_NAPOLEON_OUTER,
            UP * 2
        )
        
        card_2 = self.create_summary_card(
            "两个拿破仑点: 外 / 内",
            self.COLOR_NAPOLEON_INNER,
            UP * 0.7
        )
        
        card_3 = self.create_summary_card(
            "神奇性质: 连线中点 = 重心",
            GOLD,
            DOWN * 0.6
        )
        
        card_4 = self.create_summary_card(
            "对任意三角形都成立",
            self.COLOR_HIGHLIGHT,
            DOWN * 1.9
        )
        
        cards = VGroup(card_1, card_2, card_3, card_4)
        
        # 卡片依次滑入
        for card in cards:
            card.shift(LEFT * 15)  # 初始在左侧外
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 15), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(1.0)
        
        # 卡片闪烁
        self.play(*[Indicate(card) for card in cards], run_time=0.8)
        
        self.wait(0.5)
        
        # 清理卡片
        self.play(FadeOut(cards), FadeOut(all_visible), run_time=0.6)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
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
            "关注我, 学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小三角形装饰（旋转动画）
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )
        
        print("\n动画渲染完成!")
    
    def create_summary_card(self, text, color, position):
        """创建要点卡片"""
        # 图标圆
        icon = Circle(radius=0.2, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 文字
        text_obj = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"]+2,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, text_obj).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        return card


# 运行命令:
# manim -pql napoleon_point.py NapoleonPoint  # 快速预览
# manim -qh napoleon_point.py NapoleonPoint   # 高质量渲染