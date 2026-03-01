"""
斜二测画法 - 直观图教学动画
高三 · 第十五章 · 简单几何体

格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
时长: ~55 秒
"""

from manim import *
import numpy as np

# ===== 全局配置 - TikTok 竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ObliqueAxonometric(Scene):
    """
    斜二测画法教学动画
    
    场景顺序:
    1. 开场钩子 (4s)
    2. 方法介绍 (4s)
    3. 坐标系建立 (8s)
    4. 规则一: x方向不变 (6s)
    5. 规则二: y方向变½ (8s)
    6. 矩形完整演示 (12s)
    7. 规则总结 (5s)
    8. 片尾 (4s)
    """
    
    # ===== 颜色配置 =====
    BG_COLOR = "#1a1a2e"
    X_COLOR = "#2ecc71"        # 绿色 - x轴
    Y_COLOR = "#e74c3c"        # 红色 - y'轴
    AXIS_COLOR = "#4a9eff"     # 蓝色 - 坐标轴
    ORIG_COLOR = "#3498db"     # 蓝色 - 原图
    OBLIQ_COLOR = "#f39c12"    # 橙色 - 直观图
    RULE_BG = "#16213e"        # 深蓝 - 规则背景
    
    def construct(self):
        self.camera.background_color = self.BG_COLOR
        
        # Phase 1: 统一初始化几何数据
        self.setup_geometry()
        
        # Phase 2: 执行动画场景
        self.scene_opening()
        self.scene_intro()
        self.scene_axes()
        self.scene_rule_x()
        self.scene_rule_y()
        self.scene_demo()
        self.scene_summary()
        self.scene_outro()
    
    # ==================== 几何初始化 ====================
    
    def setup_geometry(self):
        """统一初始化所有几何参数 - 所有坐标在此计算"""
        
        # 核心参数
        self.UNIT = 1.0           # 单位长度
        self.W = 2.8              # 矩形宽度 (x方向)
        self.H = 2.4              # 矩形高度 (y方向, 原始)
        self.OBL_ANGLE = 45       # y'轴角度 (度)
        
        # 屏幕上的参考位置
        self.AXES_ORIG = np.array([0, 0.5, 0])  # 坐标系原点
        
        # 斜二测变换: 将原坐标(x,y)转换为屏幕坐标
        # 以坐标系原点为中心, 矩形左右对称
        self.OBL_OFFSET = np.array([
            -self.W * self.UNIT / 2,  # 水平居中
            0,
            0
        ])
        
        # 预计算矩形四顶点
        self.pt_A = self._oblique(0, 0)
        self.pt_B = self._oblique(self.W, 0)
        self.pt_C = self._oblique(self.W, self.H)
        self.pt_D = self._oblique(0, self.H)
        
        # 预计算关键向量
        angle_rad = np.radians(self.OBL_ANGLE)
        self.y_prime_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        self.x_dir = np.array([1, 0, 0])
        
        # 几何验证
        self._verify_geometry()
    
    def _oblique(self, x, y):
        """
        斜二测变换公式:
        - x方向: 长度不变
        - y方向: 长度变为½, 沿45°角方向
        """
        angle_rad = np.radians(self.OBL_ANGLE)
        cos_a = np.cos(angle_rad)
        sin_a = np.sin(angle_rad)
        
        origin = self.AXES_ORIG + self.OBL_OFFSET
        
        screen_x = origin[0] + x * self.UNIT + (y / 2) * cos_a * self.UNIT
        screen_y = origin[1] + (y / 2) * sin_a * self.UNIT
        return np.array([screen_x, screen_y, 0])
    
    def _verify_geometry(self):
        """验证几何关系正确性"""
        eps = 1e-5
        
        # 验证x方向: AB = W * UNIT
        AB = np.linalg.norm(self.pt_B - self.pt_A)
        assert abs(AB - self.W * self.UNIT) < eps, f"AB length error: {AB:.4f}"
        
        # 验证y'方向: AD = H/2 * UNIT
        AD = np.linalg.norm(self.pt_D - self.pt_A)
        expected_AD = (self.H / 2) * self.UNIT
        assert abs(AD - expected_AD) < eps, f"AD length error: {AD:.4f}"
        
        # 验证45°角: AD方向应为45°
        AD_vec = self.pt_D - self.pt_A
        angle = np.degrees(np.arctan2(AD_vec[1], AD_vec[0]))
        assert abs(angle - 45.0) < 0.01, f"y' angle error: {angle:.4f}°"
        
        # 验证边界 (x∈[-4,4], y∈[-7,7])
        for pt, name in [(self.pt_A, 'A'), (self.pt_B, 'B'),
                         (self.pt_C, 'C'), (self.pt_D, 'D')]:
            assert abs(pt[0]) < 4.5, f"{name} x out of bounds: {pt[0]:.3f}"
            assert abs(pt[1]) < 7.5, f"{name} y out of bounds: {pt[1]:.3f}"
        
        print(f"✓ Geometry OK — A:{self.pt_A[:2]}, B:{self.pt_B[:2]}, "
              f"C:{self.pt_C[:2]}, D:{self.pt_D[:2]}")
    
    # ==================== 辅助方法 ====================
    
    def _make_oblique_axes(self, origin, x_len=3.2, y_len=2.6):
        """创建斜二测坐标系（x轴 + y'轴）"""
        angle_rad = np.radians(self.OBL_ANGLE)
        y_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        
        x_axis = Arrow(
            origin + LEFT * 0.4,
            origin + RIGHT * x_len,
            color=self.X_COLOR, buff=0, stroke_width=3.5
        )
        y_axis = Arrow(
            origin - y_dir * 0.4,
            origin + y_dir * y_len,
            color=self.Y_COLOR, buff=0, stroke_width=3.5
        )
        
        x_lbl = MathTex("x", color=self.X_COLOR, font_size=30)
        x_lbl.next_to(x_axis.get_end(), RIGHT, buff=0.15)
        
        y_lbl = MathTex("y'", color=self.Y_COLOR, font_size=30)
        y_lbl.next_to(y_axis.get_end(), UR, buff=0.1)
        
        return VGroup(x_axis, y_axis), VGroup(x_lbl, y_lbl)
    
    def _make_right_angle_mark(self, corner, p1, p2, size=0.18):
        """手动创建直角标记（方形符号）"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner, corner + v1, corner + v1 + v2, corner + v2,
            color=YELLOW, stroke_width=1.5, fill_opacity=0
        )
    
    # ==================== 场景 1: 开场 ====================
    
    def scene_opening(self):
        """开场钩子 - 4s"""
        
        # 作者信息 (顶部常驻)
        self.author_top = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=18, color=GRAY_B
        ).move_to(UP * 7.1)
        self.play(FadeIn(self.author_top, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        q1 = Text("在平面上画立体图形",
                  font="Noto Sans CJK SC", font_size=38, color=WHITE).move_to(UP * 5.8)
        q2 = Text("你会吗？",
                  font="Noto Sans CJK SC", font_size=52, color=YELLOW).move_to(UP * 4.9)
        
        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.5)
        
        # 简单线框立方体
        cube = self._make_cube_wireframe(center=np.array([0, 1.8, 0]), size=1.4)
        self.play(Create(cube), run_time=1.5)
        self.wait(0.8)
        
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(cube), run_time=0.5)
    
    def _make_cube_wireframe(self, center, size):
        """绘制简单立方体线框图"""
        s = size
        # 深度向量 (模拟斜二测效果)
        depth = np.array([s * 0.5, s * 0.38, 0])
        
        # 前面四角
        bl = center + np.array([-s/2, -s/2, 0])
        br = center + np.array([s/2, -s/2, 0])
        tr = center + np.array([s/2, s/2, 0])
        tl = center + np.array([-s/2, s/2, 0])
        
        # 后面四角
        bl_b, br_b, tr_b, tl_b = bl + depth, br + depth, tr + depth, tl + depth
        
        lines = VGroup()
        
        # 前面 (实线)
        for p, q in [(bl, br), (br, tr), (tr, tl), (tl, bl)]:
            lines.add(Line(p, q, color=self.OBLIQ_COLOR, stroke_width=3))
        
        # 可见后棱 (实线)
        for p, q in [(tr, tr_b), (tl, tl_b), (tr_b, tl_b), (tr_b, br_b)]:
            lines.add(Line(p, q, color=self.OBLIQ_COLOR, stroke_width=3))
        
        # 不可见后棱 (虚线)
        for p, q in [(bl, bl_b), (br, br_b), (bl_b, br_b), (bl_b, tl_b)]:
            lines.add(DashedLine(p, q, color=GRAY, stroke_width=1.8, dash_length=0.1))
        
        return lines
    
    # ==================== 场景 2: 介绍 ====================
    
    def scene_intro(self):
        """方法介绍 - 4s"""
        
        main_title = Text(
            "斜二测画法",
            font="Noto Sans CJK SC", font_size=54, color=GOLD
        ).move_to(UP * 5.5)
        subtitle = Text(
            "直观图绘制标准方法",
            font="Noto Sans CJK SC", font_size=28, color=GRAY_A
        ).move_to(UP * 4.5)
        chapter_tag = Text(
            "高三 · 第15章 · 简单几何体",
            font="Noto Sans CJK SC", font_size=20, color=self.AXIS_COLOR
        ).move_to(UP * 3.7)
        
        self.play(Write(main_title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(chapter_tag), run_time=0.3)
        self.wait(1.5)
        self.play(FadeOut(main_title), FadeOut(subtitle), FadeOut(chapter_tag), run_time=0.4)
    
    # ==================== 场景 3: 坐标系 ====================
    
    def scene_axes(self):
        """建立斜二测坐标系 - 8s"""
        
        step_title = Text(
            "步骤一：建立坐标系",
            font="Noto Sans CJK SC", font_size=32, color=GOLD
        ).move_to(UP * 5.8)
        self.play(Write(step_title), run_time=0.5)
        
        origin = self.AXES_ORIG
        angle_rad = np.radians(self.OBL_ANGLE)
        y_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        
        # ---- 先画 x 轴 ----
        x_axis = Arrow(
            origin + LEFT * 3.2,
            origin + RIGHT * 3.5,
            color=self.X_COLOR, buff=0, stroke_width=4
        )
        x_lbl = MathTex("x", color=self.X_COLOR, font_size=32)
        x_lbl.next_to(x_axis.get_end(), RIGHT, buff=0.12)
        
        explain_x = Text(
            "x 轴：水平方向",
            font="Noto Sans CJK SC", font_size=28, color=self.X_COLOR
        ).move_to(DOWN * 3.0)
        
        self.play(GrowArrow(x_axis), run_time=0.8)
        self.play(Write(x_lbl), run_time=0.3)
        self.play(FadeIn(explain_x, shift=UP * 0.2), run_time=0.3)
        self.wait(0.6)
        
        # ---- 再画 y' 轴 ----
        y_axis = Arrow(
            origin - y_dir * 0.4,
            origin + y_dir * 2.8,
            color=self.Y_COLOR, buff=0, stroke_width=4
        )
        y_lbl = MathTex("y'", color=self.Y_COLOR, font_size=32)
        y_lbl.next_to(y_axis.get_end(), UR, buff=0.1)
        
        explain_y = Text(
            "y' 轴：与 x 轴成 45° 角",
            font="Noto Sans CJK SC", font_size=28, color=self.Y_COLOR
        ).move_to(DOWN * 3.0)
        
        self.play(FadeOut(explain_x), run_time=0.2)
        self.play(GrowArrow(y_axis), run_time=0.8)
        self.play(Write(y_lbl), run_time=0.3)
        self.play(FadeIn(explain_y, shift=UP * 0.2), run_time=0.3)
        
        # ---- 画 45° 角弧 ----
        # 从 x 轴到 y' 轴是逆时针，叉积 z > 0 → other_angle=False
        line_x_ref = Line(origin, origin + RIGHT * 0.9, color=self.X_COLOR)
        line_y_ref = Line(origin, origin + y_dir * 0.9, color=self.Y_COLOR)
        
        # 叉积验证: v1=(1,0), v2=(cos45,sin45) → cross_z = 1*sin45 - 0*cos45 = sin45 > 0
        # → 逆时针 → other_angle=False ✓
        angle_arc = Angle(
            line_x_ref, line_y_ref,
            radius=0.6,
            color=YELLOW,
            other_angle=False
        )
        
        # 角度标注在弧的中间位置 (22.5°处)
        mid_rad = np.radians(22.5)
        angle_lbl = MathTex(r"45^\circ", color=YELLOW, font_size=26)
        angle_lbl.move_to(origin + np.array([
            0.92 * np.cos(mid_rad),
            0.92 * np.sin(mid_rad),
            0
        ]))
        
        self.play(Create(angle_arc), run_time=0.5)
        self.play(Write(angle_lbl), run_time=0.3)
        
        # 原点标记
        origin_dot = Dot(origin, color=WHITE, radius=0.07)
        origin_lbl = MathTex("O", color=WHITE, font_size=24)
        origin_lbl.next_to(origin_dot, DL, buff=0.1)
        self.play(FadeIn(origin_dot), Write(origin_lbl), run_time=0.3)
        
        self.wait(2.0)  # 关键停留 - 让学生理解坐标系
        
        # 存储坐标系供后续使用
        self.axes_vgroup = VGroup(
            x_axis, y_axis, x_lbl, y_lbl,
            angle_arc, angle_lbl, origin_dot, origin_lbl
        )
        
        self.play(FadeOut(explain_y), FadeOut(step_title), run_time=0.3)
    
    # ==================== 场景 4: 规则一 ====================
    
    def scene_rule_x(self):
        """规则一: x方向长度不变 - 6s"""
        
        rule_title = Text(
            "规则一：x 方向长度不变",
            font="Noto Sans CJK SC", font_size=30, color=self.X_COLOR
        ).move_to(UP * 5.8)
        self.play(Write(rule_title), run_time=0.5)
        
        origin = self.AXES_ORIG
        seg_half = 1.1  # 线段半长
        
        # 原始水平线段
        p_left = origin + LEFT * seg_half
        p_right = origin + RIGHT * seg_half
        
        orig_seg = Line(p_left, p_right, color=self.X_COLOR, stroke_width=5)
        dot_l = Dot(p_left, color=self.X_COLOR, radius=0.09)
        dot_r = Dot(p_right, color=self.X_COLOR, radius=0.09)
        
        length_lbl = MathTex("a", color=YELLOW, font_size=34)
        length_lbl.next_to(orig_seg, UP, buff=0.2)
        
        self.play(Create(orig_seg), FadeIn(dot_l), FadeIn(dot_r), run_time=0.6)
        self.play(Write(length_lbl), run_time=0.3)
        
        # 直观图中同样的线段 (下移)
        p_left2 = origin + LEFT * seg_half + DOWN * 1.0
        p_right2 = origin + RIGHT * seg_half + DOWN * 1.0
        
        obq_seg = Line(p_left2, p_right2, color=YELLOW, stroke_width=5)
        length_lbl2 = MathTex("a", color=YELLOW, font_size=34)
        length_lbl2.next_to(obq_seg, DOWN, buff=0.2)
        
        arrow_eq = Arrow(
            orig_seg.get_center() + DOWN * 0.2,
            obq_seg.get_center() + UP * 0.2,
            color=WHITE, buff=0.1, stroke_width=2
        )
        equal_note = Text(
            "直观图中：长度相同",
            font="Noto Sans CJK SC", font_size=26, color=YELLOW
        ).move_to(DOWN * 3.2)
        
        self.play(GrowArrow(arrow_eq), run_time=0.4)
        self.play(Create(obq_seg), Write(length_lbl2), run_time=0.6)
        self.play(FadeIn(equal_note, shift=UP * 0.2), run_time=0.3)
        
        # 高亮强调
        self.play(
            Flash(dot_l, color=self.X_COLOR, flash_radius=0.25),
            Flash(dot_r, color=self.X_COLOR, flash_radius=0.25),
            run_time=0.5
        )
        
        checkmark = Text(
            "✓  x 方向：原长不变",
            font="Noto Sans CJK SC", font_size=28, color=self.X_COLOR
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(checkmark, scale=1.1), run_time=0.4)
        self.wait(1.5)
        
        self.play(
            FadeOut(rule_title), FadeOut(orig_seg), FadeOut(obq_seg),
            FadeOut(dot_l), FadeOut(dot_r), FadeOut(length_lbl), FadeOut(length_lbl2),
            FadeOut(arrow_eq), FadeOut(equal_note), FadeOut(checkmark),
            run_time=0.4
        )
    
    # ==================== 场景 5: 规则二 ====================
    
    def scene_rule_y(self):
        """规则二: y方向变½且沿45° - 8s"""
        
        rule_title = Text(
            "规则二：y 方向变为原来的",
            font="Noto Sans CJK SC", font_size=27, color=self.Y_COLOR
        ).move_to(UP * 5.9)
        rule_title2_math = MathTex(r"\frac{1}{2}", color=YELLOW, font_size=36)
        rule_title2_text = Text(
            "，且沿 y' 轴方向",
            font="Noto Sans CJK SC", font_size=27, color=self.Y_COLOR
        )
        rule_title_row2 = VGroup(rule_title2_math, rule_title2_text).arrange(RIGHT, buff=0.1)
        rule_title_row2.move_to(UP * 5.1)
        
        self.play(Write(rule_title), run_time=0.5)
        self.play(FadeIn(rule_title_row2), run_time=0.3)
        
        origin = self.AXES_ORIG
        angle_rad = np.radians(self.OBL_ANGLE)
        y_dir = np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        
        orig_h = 1.6  # 原始y方向长度 (在原始坐标系中的视觉长度)
        
        # ---- 左: 原始 y 方向 (竖直线段) ----
        orig_base = origin + LEFT * 2.0
        orig_top = orig_base + UP * orig_h
        
        orig_seg = Line(orig_base, orig_top, color=BLUE_C, stroke_width=5)
        orig_dot_b = Dot(orig_base, color=BLUE_C, radius=0.08)
        orig_dot_t = Dot(orig_top, color=BLUE_C, radius=0.08)
        orig_h_lbl = MathTex("b", color=BLUE_C, font_size=32)
        orig_h_lbl.next_to(orig_seg, LEFT, buff=0.2)
        orig_caption = Text(
            "原来 y 方向",
            font="Noto Sans CJK SC", font_size=20, color=BLUE_C
        ).next_to(orig_base, DOWN, buff=0.2)
        
        self.play(
            Create(orig_seg), FadeIn(orig_dot_b), FadeIn(orig_dot_t),
            Write(orig_h_lbl), FadeIn(orig_caption),
            run_time=0.8
        )
        
        # ---- 转换箭头 ----
        xform_arrow = Arrow(
            origin + LEFT * 0.5,
            origin + RIGHT * 0.5,
            color=WHITE, buff=0, stroke_width=2.5
        )
        self.play(GrowArrow(xform_arrow), run_time=0.4)
        
        # ---- 右: 斜二测 y' 方向 (长度½, 45°) ----
        obq_base = origin + RIGHT * 1.2
        obq_end = obq_base + y_dir * (orig_h / 2)
        
        obq_seg = Line(obq_base, obq_end, color=self.Y_COLOR, stroke_width=5)
        obq_dot_b = Dot(obq_base, color=self.Y_COLOR, radius=0.08)
        obq_dot_t = Dot(obq_end, color=self.Y_COLOR, radius=0.08)
        obq_h_lbl = MathTex(r"\frac{b}{2}", color=YELLOW, font_size=28)
        obq_h_lbl.next_to(obq_end, UR, buff=0.15)
        obq_caption = Text(
            "直观图 y' 方向",
            font="Noto Sans CJK SC", font_size=20, color=self.Y_COLOR
        ).next_to(obq_base, DOWN, buff=0.2)
        
        self.play(
            Create(obq_seg), FadeIn(obq_dot_b), FadeIn(obq_dot_t),
            Write(obq_h_lbl), FadeIn(obq_caption),
            run_time=0.8
        )
        
        # 强调1: 长度是½
        half_note = Text(
            "长度 ×",
            font="Noto Sans CJK SC", font_size=26, color=WHITE
        )
        half_frac = MathTex(r"\frac{1}{2}", color=YELLOW, font_size=36)
        half_row = VGroup(half_note, half_frac).arrange(RIGHT, buff=0.15)
        half_row.move_to(DOWN * 3.0)
        
        self.play(FadeIn(half_row, shift=UP * 0.2), run_time=0.3)
        
        # 强调2: 方向是45°
        angle_note = Text(
            "方向沿 y' 轴（45°角）",
            font="Noto Sans CJK SC", font_size=24, color=self.Y_COLOR
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(angle_note, shift=UP * 0.2), run_time=0.3)
        
        # 高亮边框
        highlight_box = SurroundingRectangle(obq_h_lbl, color=YELLOW, buff=0.12, stroke_width=2.5)
        self.play(Create(highlight_box), run_time=0.4)
        
        self.wait(2.5)  # 关键停留 - 难点需要消化
        
        # 清理
        self.play(
            FadeOut(rule_title), FadeOut(rule_title_row2),
            FadeOut(orig_seg), FadeOut(orig_dot_b), FadeOut(orig_dot_t),
            FadeOut(orig_h_lbl), FadeOut(orig_caption),
            FadeOut(xform_arrow),
            FadeOut(obq_seg), FadeOut(obq_dot_b), FadeOut(obq_dot_t),
            FadeOut(obq_h_lbl), FadeOut(obq_caption),
            FadeOut(half_row), FadeOut(angle_note), FadeOut(highlight_box),
            run_time=0.5
        )
    
    # ==================== 场景 6: 矩形演示 ====================
    
    def scene_demo(self):
        """完整矩形演示 - 12s"""
        
        demo_title = Text(
            "实例：画矩形的直观图",
            font="Noto Sans CJK SC", font_size=30, color=GOLD
        ).move_to(UP * 5.8)
        self.play(Write(demo_title), run_time=0.5)
        
        origin = self.AXES_ORIG
        
        # ---- 先展示原始矩形 (标准坐标，左侧) ----
        orig_w = 2.2
        orig_h = 1.5
        orig_center = origin + UP * 2.3
        
        orig_A = orig_center + LEFT * orig_w/2 + DOWN * orig_h/2
        orig_B = orig_center + RIGHT * orig_w/2 + DOWN * orig_h/2
        orig_C = orig_center + RIGHT * orig_w/2 + UP * orig_h/2
        orig_D = orig_center + LEFT * orig_w/2 + UP * orig_h/2
        
        orig_rect = Polygon(orig_A, orig_B, orig_C, orig_D,
                            color=self.ORIG_COLOR, stroke_width=3)
        orig_caption = Text("原矩形",
                            font="Noto Sans CJK SC", font_size=22, color=self.ORIG_COLOR)
        orig_caption.next_to(orig_rect, UP, buff=0.15)
        
        orig_w_lbl = Text("宽 a",
                          font="Noto Sans CJK SC", font_size=18, color=self.ORIG_COLOR)
        orig_w_lbl.next_to(orig_rect, DOWN, buff=0.15)
        orig_h_lbl = Text("高 b",
                          font="Noto Sans CJK SC", font_size=18, color=self.ORIG_COLOR)
        orig_h_lbl.next_to(orig_rect, LEFT, buff=0.15)
        
        self.play(Create(orig_rect), run_time=0.6)
        self.play(FadeIn(orig_caption), FadeIn(orig_w_lbl), FadeIn(orig_h_lbl), run_time=0.3)
        self.wait(0.5)
        
        # 转变箭头
        step0_note = Text("斜二测画法 →",
                          font="Noto Sans CJK SC", font_size=26, color=WHITE).move_to(DOWN * 2.5)
        self.play(FadeIn(step0_note, shift=UP * 0.2), run_time=0.3)
        self.wait(0.3)
        
        # 清除原始图，开始绘制过程
        self.play(
            FadeOut(orig_rect), FadeOut(orig_caption),
            FadeOut(orig_w_lbl), FadeOut(orig_h_lbl), FadeOut(step0_note),
            run_time=0.4
        )
        
        # ---- 逐步绘制斜二测图 ----
        A = self.pt_A
        B = self.pt_B
        C = self.pt_C
        D = self.pt_D
        
        # Step 1: 画 x 轴方向 A'B'
        step1 = Text("① A'B'：x 方向，长度 = a（不变）",
                     font="Noto Sans CJK SC", font_size=20, color=self.X_COLOR).move_to(DOWN * 2.8)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.3)
        
        dot_A = Dot(A, color=WHITE, radius=0.09)
        dot_B = Dot(B, color=WHITE, radius=0.09)
        line_AB = Line(A, B, color=self.X_COLOR, stroke_width=4.5)
        lbl_A = Text("A'", font="Noto Sans CJK SC", font_size=21, color=WHITE)
        lbl_A.next_to(dot_A, DL, buff=0.08)
        lbl_B = Text("B'", font="Noto Sans CJK SC", font_size=21, color=WHITE)
        lbl_B.next_to(dot_B, DR, buff=0.08)
        
        self.play(FadeIn(dot_A), FadeIn(dot_B), run_time=0.2)
        self.play(Create(line_AB), run_time=0.7)
        self.play(Write(lbl_A), Write(lbl_B), run_time=0.3)
        self.wait(0.5)
        
        # Step 2: 从 A' 画 A'D'（沿y'方向, 长b/2）
        step2 = Text("② A'D'：沿 y' 方向，长度 = b/2",
                     font="Noto Sans CJK SC", font_size=20, color=self.Y_COLOR).move_to(DOWN * 2.8)
        self.play(FadeOut(step1), FadeIn(step2, shift=UP * 0.2), run_time=0.3)
        
        dot_D = Dot(D, color=WHITE, radius=0.09)
        line_AD = Line(A, D, color=self.Y_COLOR, stroke_width=4.5)
        lbl_D = Text("D'", font="Noto Sans CJK SC", font_size=21, color=WHITE)
        lbl_D.next_to(dot_D, LEFT, buff=0.08)
        
        # b/2 长度标注
        mid_AD = (A + D) / 2
        half_lbl = MathTex(r"\frac{b}{2}", color=YELLOW, font_size=22)
        half_lbl.next_to(mid_AD, LEFT, buff=0.18)
        
        self.play(Create(line_AD), run_time=0.8)
        self.play(FadeIn(dot_D), Write(lbl_D), Write(half_lbl), run_time=0.3)
        self.wait(0.5)
        
        # Step 3: 从 B' 画 B'C'（平行于 A'D'，同长）
        step3 = Text("③ B'C'：平行于 A'D'，等长",
                     font="Noto Sans CJK SC", font_size=20, color=self.Y_COLOR).move_to(DOWN * 2.8)
        self.play(FadeOut(step2), FadeIn(step3, shift=UP * 0.2), run_time=0.3)
        
        dot_C = Dot(C, color=WHITE, radius=0.09)
        line_BC = Line(B, C, color=self.Y_COLOR, stroke_width=4.5)
        lbl_C = Text("C'", font="Noto Sans CJK SC", font_size=21, color=WHITE)
        lbl_C.next_to(dot_C, RIGHT, buff=0.08)
        
        self.play(Create(line_BC), run_time=0.8)
        self.play(FadeIn(dot_C), Write(lbl_C), run_time=0.3)
        self.wait(0.4)
        
        # Step 4: 连接 D'C'
        step4 = Text("④ 连接 D'C'，完成！",
                     font="Noto Sans CJK SC", font_size=22, color=GOLD).move_to(DOWN * 2.8)
        self.play(FadeOut(step3), FadeIn(step4, shift=UP * 0.2), run_time=0.3)
        
        line_DC = Line(D, C, color=self.X_COLOR, stroke_width=4.5)
        self.play(Create(line_DC), run_time=0.7)
        
        # 填充颜色
        oblique_fill = Polygon(A, B, C, D,
                               fill_color=self.OBLIQ_COLOR, fill_opacity=0.22,
                               stroke_color=self.OBLIQ_COLOR, stroke_width=0)
        self.play(FadeIn(oblique_fill), run_time=0.5)
        
        # 成功标注
        success_bg = RoundedRectangle(width=5.0, height=0.8, corner_radius=0.2,
                                      fill_color=GOLD, fill_opacity=0.2,
                                      stroke_color=GOLD, stroke_width=2)
        success_text = Text("直观图绘制完成 ✓",
                            font="Noto Sans CJK SC", font_size=26, color=GOLD)
        success_group = VGroup(success_bg, success_text)
        success_group.arrange(ORIGIN).move_to(DOWN * 4.2)
        
        self.play(FadeIn(success_group, scale=1.1), run_time=0.5)
        self.wait(3.0)  # 关键停留 - 难点理解
        
        # 清理所有演示元素
        self.play(
            FadeOut(demo_title),
            FadeOut(oblique_fill),
            FadeOut(line_AB), FadeOut(line_AD), FadeOut(line_BC), FadeOut(line_DC),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C), FadeOut(dot_D),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C), FadeOut(lbl_D),
            FadeOut(half_lbl), FadeOut(step4), FadeOut(success_group),
            FadeOut(self.axes_vgroup),
            run_time=0.6
        )
    
    # ==================== 场景 7: 总结 ====================
    
    def scene_summary(self):
        """规则总结卡片 - 5s"""
        
        title = Text(
            "斜二测画法 · 三条规则",
            font="Noto Sans CJK SC", font_size=32, color=GOLD
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)
        
        # 规则卡片
        rule_data = [
            ("① 建立坐标系", "x 轴水平，y' 轴与 x 轴成 45° 角", self.AXIS_COLOR),
            ("② x 方向",    "平行 x 轴的线段，长度不变",         self.X_COLOR),
            ("③ y 方向",    "平行 y 轴的线段，长度变为原来的",    self.Y_COLOR),
        ]
        
        cards = VGroup()
        for title_ch, desc_ch, color in rule_data:
            bg = RoundedRectangle(
                width=7.8, height=1.25, corner_radius=0.22,
                fill_color=self.RULE_BG, fill_opacity=1,
                stroke_color=color, stroke_width=2.5
            )
            t1 = Text(title_ch, font="Noto Sans CJK SC", font_size=24, color=color)
            t2 = Text(desc_ch, font="Noto Sans CJK SC", font_size=20, color=GRAY_A)
            texts = VGroup(t1, t2).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            card = VGroup(bg, texts)
            card.move_to(ORIGIN)
            cards.add(card)
        
        cards.arrange(DOWN, buff=0.3).move_to(UP * 2.8)
        
        # 第三张卡片加½公式
        half_math = MathTex(r"\frac{1}{2}", color=YELLOW, font_size=26)
        # 附加到第三张卡片的文字后面
        card3_text_row2 = cards[2][1][1]
        half_math.next_to(card3_text_row2, RIGHT, buff=0.1)
        
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.35)
        self.play(FadeIn(half_math), run_time=0.3)
        
        # 面积公式
        area_line1 = Text("面积关系：", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        area_line2 = MathTex(r"S_{\rm oblique} = \frac{\sqrt{2}}{4} \, S_{\rm original}",
                             font_size=26, color=YELLOW)
        area_row = VGroup(area_line1, area_line2).arrange(RIGHT, buff=0.15)
        
        area_bg = RoundedRectangle(width=7.8, height=1.0, corner_radius=0.18,
                                   fill_color="#0d1b2a", fill_opacity=1,
                                   stroke_color=YELLOW, stroke_width=2)
        area_card = VGroup(area_bg, area_row)
        area_card.arrange(ORIGIN).move_to(DOWN * 0.8)
        
        self.play(FadeIn(area_card), run_time=0.4)
        self.wait(2.0)
        
        self.play(
            FadeOut(title), FadeOut(cards), FadeOut(half_math), FadeOut(area_card),
            run_time=0.5
        )
    
    # ==================== 场景 8: 片尾 ====================
    
    def scene_outro(self):
        """片尾关注 - 4s"""
        
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC", font_size=42, color=WHITE
        ).move_to(UP * 1.8)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC", font_size=32, color=GRAY_B
        ).move_to(UP * 0.8)
        
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC", font_size=30, color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(
            Transform(self.author_top, author_large),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2, scale=1.05), run_time=0.5)
        
        # 装饰小圆点旋转
        num_dots = 6
        dots = VGroup(*[
            Dot(radius=0.13, color=GOLD, fill_opacity=0.9).move_to(
                np.array([2.8 * np.cos(i * TAU / num_dots),
                          -2.5 + 2.8 * np.sin(i * TAU / num_dots),
                          0])
            )
            for i in range(num_dots)
        ])
        self.play(*[FadeIn(d, scale=0.5) for d in dots], run_time=0.5)
        self.play(Rotate(dots, angle=PI, run_time=1.2))
        self.wait(0.5)
        
        self.play(
            FadeOut(self.author_top), FadeOut(author_id),
            FadeOut(follow), FadeOut(dots),
            run_time=0.8
        )


# ===== 渲染命令 =====
# 快速预览: manim -pql oblique_axonometric.py ObliqueAxonometric
# 高质量:   manim -qh  oblique_axonometric.py ObliqueAxonometric
# 4K 制作:  manim -qk  oblique_axonometric.py ObliqueAxonometric