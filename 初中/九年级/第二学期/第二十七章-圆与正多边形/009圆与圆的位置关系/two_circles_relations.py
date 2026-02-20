"""
圆与圆的位置关系 - Two Circles Position Relationships
使用 Manim 创建的初中几何教学视频

内容: 外离、外切、相交、内切、内含五种位置关系
目标观众: 初中生
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


class TwoCirclesRelations(Scene):
    """
    圆与圆的位置关系教学动画
    
    场景顺序:
    1. 开场钩子
    2. 基础概念介绍
    3. 外离 (d > R+r)
    4. 外切 (d = R+r)
    5. 相交 (R-r < d < R+r)
    6. 内切 (d = R-r)
    7. 内含 (d < R-r)
    8. 总结对比
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE_1 = "#3498db"      # 蓝色 - 大圆
        self.COLOR_CIRCLE_2 = "#e74c3c"      # 红色 - 小圆
        self.COLOR_DISTANCE = "#2ecc71"      # 绿色 - 圆心距
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        self.COLOR_TANGENT = "#f39c12"       # 橙色 - 切点/交点
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_basic_concepts()
        self.scene_3_external_separation()
        self.scene_4_external_tangency()
        self.scene_5_intersection()
        self.scene_6_internal_tangency()
        self.scene_7_containment()
        self.scene_8_summary()
        self.scene_9_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素"""
        # 圆的基本参数
        self.O1 = np.array([-1.2, 1.5, 0])  # 大圆圆心
        self.R = 1.5                         # 大圆半径
        self.r = 1.0                         # 小圆半径
        
        # 五种情况下的圆心距d
        self.d_separate = 3.0            # 外离: d > R+r
        self.d_external_tangent = 2.5    # 外切: d = R+r
        self.d_intersect = 1.8           # 相交: R-r < d < R+r
        self.d_internal_tangent = 0.5    # 内切: d = R-r
        self.d_contain = 0.2             # 内含: d < R-r
        
        # 计算各种情况下的O2位置
        self.O2_separate = self.calculate_O2_position(self.d_separate)
        self.O2_external_tangent = self.calculate_O2_position(self.d_external_tangent)
        self.O2_intersect = self.calculate_O2_position(self.d_intersect)
        self.O2_internal_tangent = self.calculate_O2_position(self.d_internal_tangent)
        self.O2_contain = self.calculate_O2_position(self.d_contain)
        
        # 验证几何参数
        self.verify_geometry()
        
        # 创建圆对象 (但不添加到场景)
        self.circle1 = Circle(
            radius=self.R,
            color=self.COLOR_CIRCLE_1,
            stroke_width=3
        ).move_to(self.O1)
        
        # 小圆初始在相交位置
        self.circle2 = Circle(
            radius=self.r,
            color=self.COLOR_CIRCLE_2,
            stroke_width=3
        ).move_to(self.O2_intersect)
    
    def calculate_O2_position(self, distance):
        """
        计算小圆圆心O2的位置
        O2在O1右侧, 距离为distance
        """
        return self.O1 + np.array([distance, 0, 0])
    
    def verify_geometry(self):
        """验证几何参数的正确性"""
        epsilon = 1e-6
        
        # 验证五种情况
        assert self.d_separate > self.R + self.r, "外离条件错误"
        assert abs(self.d_external_tangent - (self.R + self.r)) < epsilon, "外切条件错误"
        assert self.R - self.r < self.d_intersect < self.R + self.r, "相交条件错误"
        assert abs(self.d_internal_tangent - (self.R - self.r)) < epsilon, "内切条件错误"
        assert self.d_contain < self.R - self.r, "内含条件错误"
        
        # 验证边界安全
        # 最右侧的位置是外离时
        rightmost = self.O2_separate[0] + self.r
        assert rightmost < 4.0, f"小圆右侧溢出: x={rightmost:.2f}"
        
        # 大圆边界
        circle1_right = self.O1[0] + self.R
        circle1_left = self.O1[0] - self.R
        circle1_top = self.O1[1] + self.R
        circle1_bottom = self.O1[1] - self.R
        
        assert circle1_right < 4.0, "大圆右侧溢出"
        assert circle1_left > -4.0, "大圆左侧溢出"
        assert circle1_top < 7.0, "大圆顶部溢出"
        assert circle1_bottom > -7.0, "大圆底部溢出"
        
        print("✓ 几何验证通过")
        print(f"  大圆中心: {self.O1}, 半径: {self.R}")
        print(f"  小圆半径: {self.r}")
        print(f"  外离: d={self.d_separate:.1f} > R+r={self.R+self.r:.1f}")
        print(f"  外切: d={self.d_external_tangent:.1f} = R+r={self.R+self.r:.1f}")
        print(f"  相交: {self.R-self.r:.1f} < d={self.d_intersect:.1f} < {self.R+self.r:.1f}")
        print(f"  内切: d={self.d_internal_tangent:.1f} = R-r={self.R-self.r:.1f}")
        print(f"  内含: d={self.d_contain:.1f} < R-r={self.R-self.r:.1f}")
    
    def calculate_intersection_points(self, O1, R, O2, r):
        """
        计算两圆的交点
        返回: (point_A, point_B) 或 (None, None)
        
        使用解析几何方法:
        圆1: (x-x1)² + (y-y1)² = R²
        圆2: (x-x2)² + (y-y2)² = r²
        """
        d = np.linalg.norm(O2 - O1)
        
        # 检查是否相交
        if d > R + r or d < abs(R - r) or d < 1e-10:
            return None, None
        
        # 计算交点
        # 使用公式: a = (R² - r² + d²) / (2d)
        # 交点在O1O2连线上的投影距离
        a = (R**2 - r**2 + d**2) / (2 * d)
        
        # 交点到O1O2连线的距离
        h = np.sqrt(R**2 - a**2)
        
        # O1到投影点P的向量
        direction = (O2 - O1) / d
        P = O1 + a * direction
        
        # 垂直方向
        perpendicular = np.array([-direction[1], direction[0], 0])
        
        # 两个交点
        point_A = P + h * perpendicular
        point_B = P - h * perpendicular
        
        return point_A, point_B
    
    def calculate_tangent_point(self, O1, R, O2, distance, external=True):
        """
        计算两圆的切点
        external=True: 外切
        external=False: 内切
        """
        direction = (O2 - O1) / distance
        
        if external:
            # 外切: 切点从O1出发, 距离为R
            tangent_point = O1 + R * direction
        else:
            # 内切: 切点从O1出发, 距离为R
            tangent_point = O1 + R * direction
        
        return tangent_point
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "两个圆相遇有几种方式?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.2)
        self.wait(0.3)
        
        # 大圆淡入
        self.play(FadeIn(self.circle1, scale=0.8), run_time=0.5)
        
        # 小圆从右侧进入
        circle2_temp = self.circle2.copy().shift(RIGHT * 6)
        self.play(circle2_temp.animate.shift(LEFT * 6), run_time=0.8)
        
        # 两圆轻微移动示意
        self.play(
            self.circle1.animate.shift(LEFT * 0.3),
            circle2_temp.animate.shift(RIGHT * 0.3),
            run_time=0.6,
            rate_func=there_and_back
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(circle2_temp),
            self.circle1.animate.move_to(self.O1),  # 恢复位置
            run_time=0.4
        )
    
    def scene_2_basic_concepts(self):
        """场景2: 基础概念介绍"""
        # 标题
        title = Text(
            "关键要素",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 添加小圆到场景
        self.play(FadeIn(self.circle2, scale=0.8), run_time=0.5)
        
        # 标记大圆圆心O₁
        O1_dot = Dot(self.O1, color=self.COLOR_HIGHLIGHT, radius=0.08)
        O1_label = MathTex("O_1", font_size=28, color=self.COLOR_HIGHLIGHT).next_to(
            O1_dot, DOWN, buff=0.15
        )
        
        self.play(FadeIn(O1_dot, scale=0.5), run_time=0.3)
        self.play(Write(O1_label), run_time=0.3)
        
        # 标记大圆半径R
        radius1_end = self.O1 + RIGHT * self.R
        radius1_line = Line(self.O1, radius1_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        R_label = MathTex("R", font_size=24, color=WHITE).next_to(
            radius1_line.get_center(), UP, buff=0.1
        )
        
        self.play(Create(radius1_line), run_time=0.5)
        self.play(Write(R_label), run_time=0.3)
        self.wait(0.3)
        
        # 标记小圆圆心O₂
        O2_dot = Dot(self.circle2.get_center(), color=self.COLOR_TANGENT, radius=0.08)
        O2_label = MathTex("O_2", font_size=28, color=self.COLOR_TANGENT).next_to(
            O2_dot, DOWN, buff=0.15
        )
        
        self.play(FadeIn(O2_dot, scale=0.5), run_time=0.3)
        self.play(Write(O2_label), run_time=0.3)
        
        # 标记小圆半径r
        O2_pos = self.circle2.get_center()
        radius2_end = O2_pos + RIGHT * self.r
        radius2_line = Line(O2_pos, radius2_end, color=self.COLOR_AUXILIARY, stroke_width=2)
        r_label = MathTex("r", font_size=24, color=WHITE).next_to(
            radius2_line.get_center(), UP, buff=0.1
        )
        
        self.play(Create(radius2_line), run_time=0.5)
        self.play(Write(r_label), run_time=0.3)
        self.wait(0.3)
        
        # 绘制O₁O₂连线
        distance_line = Line(self.O1, O2_pos, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.8)
        
        # 标注圆心距d
        d_brace = Brace(distance_line, direction=UP, buff=0.1, color=YELLOW)
        d_label = MathTex("d", font_size=24, color=YELLOW).next_to(d_brace, UP, buff=0.05)
        
        self.play(FadeIn(d_brace), Write(d_label), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "d = 两圆圆心距",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(radius1_line),
            FadeOut(R_label),
            FadeOut(radius2_line),
            FadeOut(r_label),
            FadeOut(distance_line),
            FadeOut(d_brace),
            FadeOut(d_label),
            FadeOut(explain),
            run_time=0.5
        )
        
        # 保留圆心标注
        self.O1_dot = O1_dot
        self.O1_label = O1_label
        self.O2_dot = O2_dot
        self.O2_label = O2_label
    
    def scene_3_external_separation(self):
        """场景3: 外离 (d > R+r)"""
        # 标题
        title = VGroup(
            Text("情况1: ", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("外离", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 小圆移动到外离位置
        new_O2 = self.O2_separate
        self.play(
            self.circle2.animate.move_to(new_O2),
            self.O2_dot.animate.move_to(new_O2),
            self.O2_label.animate.next_to(new_O2, DOWN, buff=0.15),
            run_time=1.0
        )
        
        # 绘制连线
        distance_line = Line(self.O1, new_O2, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.5)
        
        # 标注d
        d_brace = Brace(distance_line, direction=UP, buff=0.1, color=YELLOW)
        d_value = MathTex(f"d={self.d_separate:.1f}", font_size=22, color=YELLOW).next_to(
            d_brace, UP, buff=0.05
        )
        
        self.play(FadeIn(d_brace), Write(d_value), run_time=0.5)
        
        # 显示公式
        formula = MathTex(
            "d", ">", "R", "+", "r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(formula), run_time=0.8)
        
        # 高亮两圆之间的间隙
        gap_start = self.O1 + RIGHT * self.R
        gap_end = new_O2 - RIGHT * self.r
        gap_indicator = DoubleArrow(
            gap_start, gap_end,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=2,
            tip_length=0.15
        )
        
        self.play(Create(gap_indicator), run_time=0.5)
        
        # 说明文字
        explain = Text(
            "外离: 无公共点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(distance_line),
            FadeOut(d_brace),
            FadeOut(d_value),
            FadeOut(gap_indicator),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_4_external_tangency(self):
        """场景4: 外切 (d = R+r)"""
        # 标题
        title = VGroup(
            Text("情况2: ", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("外切", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 小圆移动到外切位置
        new_O2 = self.O2_external_tangent
        self.play(
            self.circle2.animate.move_to(new_O2),
            self.O2_dot.animate.move_to(new_O2),
            self.O2_label.animate.next_to(new_O2, DOWN, buff=0.15),
            run_time=0.8
        )
        
        # 计算切点
        tangent_point = self.calculate_tangent_point(
            self.O1, self.R, new_O2, self.d_external_tangent, external=True
        )
        
        # 标记切点
        T_dot = Dot(tangent_point, color=self.COLOR_TANGENT, radius=0.10)
        T_label = MathTex("T", font_size=24, color=self.COLOR_TANGENT).next_to(
            T_dot, UP, buff=0.15
        )
        
        self.play(FadeIn(T_dot, scale=0.5), run_time=0.3)
        self.play(Flash(T_dot, color=self.COLOR_TANGENT, flash_radius=0.3), run_time=0.3)
        self.play(Write(T_label), run_time=0.3)
        
        # 绘制连线
        distance_line = Line(self.O1, new_O2, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.5)
        
        # 显示公式
        formula = MathTex(
            "d", "=", "R", "+", "r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(formula), run_time=0.8)
        
        # 绘制公切线 (垂直于O₁O₂)
        direction = (new_O2 - self.O1) / self.d_external_tangent
        perpendicular = np.array([-direction[1], direction[0], 0])
        
        tangent_line = Line(
            tangent_point - perpendicular * 1.2,
            tangent_point + perpendicular * 1.2,
            color=self.COLOR_TANGENT,
            stroke_width=2
        )
        
        self.play(Create(tangent_line), run_time=0.6)
        
        # 说明文字
        explain = Text(
            "外切: 一个公共点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(T_dot),
            FadeOut(T_label),
            FadeOut(distance_line),
            FadeOut(tangent_line),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_5_intersection(self):
        """场景5: 相交 (R-r < d < R+r)"""
        # 标题
        title = VGroup(
            Text("情况3: ", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("相交", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_TANGENT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 小圆移动到相交位置
        new_O2 = self.O2_intersect
        self.play(
            self.circle2.animate.move_to(new_O2),
            self.O2_dot.animate.move_to(new_O2),
            self.O2_label.animate.next_to(new_O2, DOWN, buff=0.15),
            run_time=0.8
        )
        
        # 绘制连线
        distance_line = Line(self.O1, new_O2, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.5)
        
        # 计算交点
        point_A, point_B = self.calculate_intersection_points(self.O1, self.R, new_O2, self.r)
        
        # 标记交点
        A_dot = Dot(point_A, color=self.COLOR_TANGENT, radius=0.10)
        B_dot = Dot(point_B, color=self.COLOR_TANGENT, radius=0.10)
        
        A_label = MathTex("A", font_size=24, color=self.COLOR_TANGENT).next_to(A_dot, UP, buff=0.12)
        B_label = MathTex("B", font_size=24, color=self.COLOR_TANGENT).next_to(B_dot, DOWN, buff=0.12)
        
        self.play(FadeIn(A_dot, scale=0.5), run_time=0.3)
        self.play(Flash(A_dot, color=self.COLOR_TANGENT, flash_radius=0.3), run_time=0.3)
        self.play(Write(A_label), run_time=0.3)
        
        self.play(FadeIn(B_dot, scale=0.5), run_time=0.3)
        self.play(Flash(B_dot, color=self.COLOR_TANGENT, flash_radius=0.3), run_time=0.3)
        self.play(Write(B_label), run_time=0.3)
        
        # 显示公式
        formula = VGroup(
            MathTex("R", "-", "r", font_size=28),
            MathTex("<", font_size=32, color=self.COLOR_HIGHLIGHT),
            MathTex("d", font_size=28, color=YELLOW),
            MathTex("<", font_size=32, color=self.COLOR_HIGHLIGHT),
            MathTex("R", "+", "r", font_size=28)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 绘制公共弦AB
        chord = Line(point_A, point_B, color=self.COLOR_TANGENT, stroke_width=3)
        self.play(Create(chord), run_time=0.6)
        
        # 说明文字
        explain = Text(
            "相交: 两个交点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(distance_line),
            FadeOut(A_dot),
            FadeOut(B_dot),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(chord),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_6_internal_tangency(self):
        """场景6: 内切 (d = R-r)"""
        # 标题
        title = VGroup(
            Text("情况4: ", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("内切", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 小圆移动到内切位置
        new_O2 = self.O2_internal_tangent
        self.play(
            self.circle2.animate.move_to(new_O2),
            self.O2_dot.animate.move_to(new_O2),
            self.O2_label.animate.next_to(new_O2, RIGHT, buff=0.15),
            run_time=0.8
        )
        
        # 计算切点
        tangent_point = self.calculate_tangent_point(
            self.O1, self.R, new_O2, self.d_internal_tangent, external=False
        )
        
        # 标记切点
        T_dot = Dot(tangent_point, color=self.COLOR_TANGENT, radius=0.10)
        T_label = MathTex("T", font_size=24, color=self.COLOR_TANGENT).next_to(
            T_dot, RIGHT, buff=0.15
        )
        
        self.play(FadeIn(T_dot, scale=0.5), run_time=0.3)
        self.play(Flash(T_dot, color=self.COLOR_TANGENT, flash_radius=0.3), run_time=0.3)
        self.play(Write(T_label), run_time=0.3)
        
        # 绘制连线
        distance_line = Line(self.O1, new_O2, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.5)
        
        # 显示公式
        formula = MathTex(
            "d", "=", "R", "-", "r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(formula), run_time=0.8)
        
        # 绘制公切线 (垂直于O₁O₂)
        direction = (new_O2 - self.O1) / self.d_internal_tangent
        perpendicular = np.array([-direction[1], direction[0], 0])
        
        tangent_line = Line(
            tangent_point - perpendicular * 1.0,
            tangent_point + perpendicular * 1.0,
            color=self.COLOR_TANGENT,
            stroke_width=2
        )
        
        self.play(Create(tangent_line), run_time=0.6)
        
        # 说明文字
        explain = Text(
            "内切: 一个公共点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(T_dot),
            FadeOut(T_label),
            FadeOut(distance_line),
            FadeOut(tangent_line),
            FadeOut(formula),
            FadeOut(explain),
            run_time=0.6
        )
    
    def scene_7_containment(self):
        """场景7: 内含 (d < R-r)"""
        # 标题
        title = VGroup(
            Text("情况5: ", font="Noto Sans CJK SC", font_size=32, color=WHITE),
            Text("内含", font="Noto Sans CJK SC", font_size=36, color=self.COLOR_AUXILIARY)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 小圆移动到内含位置
        new_O2 = self.O2_contain
        self.play(
            self.circle2.animate.move_to(new_O2),
            self.O2_dot.animate.move_to(new_O2),
            self.O2_label.animate.next_to(new_O2, RIGHT, buff=0.15),
            run_time=0.8
        )
        
        # 绘制连线
        distance_line = Line(self.O1, new_O2, color=self.COLOR_DISTANCE, stroke_width=2)
        self.play(Create(distance_line), run_time=0.5)
        
        # 标注d
        d_brace = Brace(distance_line, direction=DOWN, buff=0.1, color=YELLOW)
        d_value = MathTex(f"d={self.d_contain:.1f}", font_size=20, color=YELLOW).next_to(
            d_brace, DOWN, buff=0.05
        )
        
        self.play(FadeIn(d_brace), Write(d_value), run_time=0.5)
        
        # 显示公式
        formula = MathTex(
            "d", "<", "R", "-", "r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 3.5)
        formula[0].set_color(YELLOW)
        formula[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(formula), run_time=0.8)
        
        # 说明文字
        explain = Text(
            "内含: 无公共点",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5)
        
        note = Text(
            "(小圆完全在大圆内部)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 5.8)
        
        self.play(FadeIn(explain), FadeIn(note), run_time=0.5)
        
        # 闪烁提示包含关系
        self.play(
            Indicate(self.circle1, color=self.COLOR_CIRCLE_1, scale_factor=1.05),
            Indicate(self.circle2, color=self.COLOR_CIRCLE_2, scale_factor=1.05),
            run_time=1.0
        )
        self.wait(1.2)
        
        # 清理所有圆和标注
        self.play(
            FadeOut(title),
            FadeOut(distance_line),
            FadeOut(d_brace),
            FadeOut(d_value),
            FadeOut(formula),
            FadeOut(explain),
            FadeOut(note),
            FadeOut(self.circle1),
            FadeOut(self.circle2),
            FadeOut(self.O1_dot),
            FadeOut(self.O1_label),
            FadeOut(self.O2_dot),
            FadeOut(self.O2_label),
            run_time=0.6
        )
    
    def scene_8_summary(self):
        """场景8: 总结对比"""
        # 标题
        title = Text(
            "位置关系判定",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建五组对比 (竖排)
        scale_factor = 0.35
        spacing = 2.0
        base_y = 4.0
        
        # 组1: 外离
        group_1 = self.create_comparison_group(
            "外离",
            self.d_separate,
            "d > R+r",
            "无公共点",
            scale_factor
        ).move_to(UP * base_y)
        
        # 组2: 外切
        group_2 = self.create_comparison_group(
            "外切",
            self.d_external_tangent,
            "d = R+r",
            "一个切点",
            scale_factor,
            show_tangent=True
        ).move_to(UP * (base_y - spacing))
        
        # 组3: 相交
        group_3 = self.create_comparison_group(
            "相交",
            self.d_intersect,
            "R-r < d < R+r",
            "两个交点",
            scale_factor,
            show_intersections=True
        ).move_to(UP * (base_y - 2 * spacing))
        
        # 组4: 内切
        group_4 = self.create_comparison_group(
            "内切",
            self.d_internal_tangent,
            "d = R-r",
            "一个切点",
            scale_factor,
            show_tangent=True,
            internal=True
        ).move_to(UP * (base_y - 3 * spacing))
        
        # 组5: 内含
        group_5 = self.create_comparison_group(
            "内含",
            self.d_contain,
            "d < R-r",
            "无公共点",
            scale_factor,
            internal=True
        ).move_to(UP * (base_y - 4 * spacing))
        
        # 所有组
        all_groups = VGroup(group_1, group_2, group_3, group_4, group_5)
        
        # 依次显示
        for i, group in enumerate(all_groups):
            self.play(FadeIn(group, shift=RIGHT * 0.5), run_time=0.4)
            if i < len(all_groups) - 1:
                self.wait(0.2)
        
        self.wait(1.0)
        
        # 依次闪烁
        for group in all_groups:
            self.play(Indicate(group[1], scale_factor=1.08), run_time=0.4)
            self.wait(0.2)
        
        # 关键规律
        pattern = Text(
            "比较d与R+r、R-r的大小关系",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(Write(pattern), run_time=1.0)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_groups),
            FadeOut(pattern),
            run_time=0.6
        )
    
    def create_comparison_group(self, label_text, distance, formula_text, 
                               explain_text, scale, show_tangent=False, 
                               show_intersections=False, internal=False):
        """创建对比组"""
        group = VGroup()
        
        # 缩放后的参数
        R_scaled = self.R * scale
        r_scaled = self.r * scale
        d_scaled = distance * scale
        
        # 圆心位置
        O1_scaled = LEFT * 1.5
        O2_scaled = O1_scaled + RIGHT * d_scaled
        
        # 大圆
        circle1 = Circle(radius=R_scaled, color=self.COLOR_CIRCLE_1, stroke_width=2).move_to(O1_scaled)
        
        # 小圆
        circle2 = Circle(radius=r_scaled, color=self.COLOR_CIRCLE_2, stroke_width=2).move_to(O2_scaled)
        
        circles = VGroup(circle1, circle2)
        
        # 添加特殊标记
        if show_tangent:
            # 切点
            direction = (O2_scaled - O1_scaled) / np.linalg.norm(O2_scaled - O1_scaled)
            tangent_point = O1_scaled + R_scaled * direction
            T_dot = Dot(tangent_point, radius=0.05, color=self.COLOR_TANGENT)
            circles.add(T_dot)
        
        elif show_intersections:
            # 交点
            point_A, point_B = self.calculate_intersection_points(O1_scaled, R_scaled, O2_scaled, r_scaled)
            if point_A is not None:
                A_dot = Dot(point_A, radius=0.05, color=self.COLOR_TANGENT)
                B_dot = Dot(point_B, radius=0.05, color=self.COLOR_TANGENT)
                circles.add(A_dot, B_dot)
        
        # 标签
        label = Text(label_text, font="Noto Sans CJK SC", font_size=20, weight=BOLD).next_to(circles, LEFT, buff=0.4)
        
        # 公式
        formula = Text(formula_text, font="Noto Sans CJK SC", font_size=16, color=YELLOW).next_to(circles, RIGHT, buff=0.4)
        
        # 说明
        explain = Text(explain_text, font="Noto Sans CJK SC", font_size=14, color=self.COLOR_AUXILIARY).next_to(
            circles, DOWN, buff=0.2
        )
        
        return VGroup(label, circles, formula, explain)
    
    def scene_9_outro(self):
        """场景9: 片尾关注"""
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
            color=self.COLOR_AUXILIARY
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
        
        # 两个圆形装饰
        circle_deco_1 = Circle(
            radius=0.8,
            color=self.COLOR_CIRCLE_1,
            stroke_width=3,
            fill_opacity=0.1
        ).move_to(LEFT * 1.5 + DOWN * 2.5)
        
        circle_deco_2 = Circle(
            radius=0.5,
            color=self.COLOR_CIRCLE_2,
            stroke_width=3,
            fill_opacity=0.1
        ).move_to(RIGHT * 1.5 + DOWN * 2.5)
        
        self.play(
            FadeIn(circle_deco_1, scale=0.5),
            FadeIn(circle_deco_2, scale=0.5),
            run_time=0.6
        )
        
        # 两圆旋转动画
        self.play(
            Rotate(circle_deco_1, angle=PI, run_time=1.5),
            Rotate(circle_deco_2, angle=-PI, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circle_deco_1),
            FadeOut(circle_deco_2),
            run_time=1.0
        )


# 运行命令:
# manim -pql two_circles_relations.py TwoCirclesRelations  # 快速预览
# manim -qh two_circles_relations.py TwoCirclesRelations   # 高质量渲染