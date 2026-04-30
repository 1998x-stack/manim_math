"""
点的平移 - Point Translation in Coordinate Plane
平面直角坐标系中点的平移规律教学动画

内容: 演示点在坐标平面内平移的规律
目标观众: 七年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

平移规律:
- 向右平移a个单位: (x, y) → (x+a, y)
- 向左平移a个单位: (x, y) → (x-a, y)
- 向上平移b个单位: (x, y) → (x, y+b)
- 向下平移b个单位: (x, y) → (x, y-b)

口诀: 左减右加，下减上加
"""

from manim import *
import numpy as np


# ===== 全局配置 - TikTok竖屏尺寸 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PointTranslation(Scene):
    """
    点的平移教学动画场景
    
    场景顺序:
    0. 开场钩子
    1. 建立坐标系
    2. 向右平移
    3. 向左平移
    4. 向上平移
    5. 向下平移
    6. 综合平移
    7. 口诀总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要点
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 平移后的点
        self.COLOR_ARROW = "#f39c12"          # 橙色 - 平移箭头
        self.COLOR_AXIS = "#95a5a6"           # 灰色 - 坐标轴
        self.COLOR_GRID = "#34495e"           # 深灰 - 网格
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_TEXT = WHITE               # 白色 - 文字
        self.COLOR_FORMULA_BG = "#2c3e50"     # 深蓝 - 公式背景
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_0_opening_hook()
        self.scene_1_setup_coordinate_system()
        self.scene_2_translate_right()
        self.scene_3_translate_left()
        self.scene_4_translate_up()
        self.scene_5_translate_down()
        self.scene_6_combined_translation()
        self.scene_7_summary()
        self.scene_8_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据和参数"""
        # ===== 坐标系参数 =====
        self.SCALE = 0.4  # 坐标系缩放系数
        self.OFFSET = UP * 1.5  # 坐标系垂直偏移
        
        # 坐标轴范围
        self.x_range = [-6, 6, 1]
        self.y_range = [-5, 5, 1]
        self.x_length = 8
        self.y_length = 7
        
        # ===== 关键点坐标 (逻辑坐标) =====
        # 初始点P(2, 3)
        self.P_coords = np.array([2, 3, 0])
        self.P = self.coords_to_point(self.P_coords)
        
        # 右平移: P(2,3) → P'(5,3)
        self.P1_right_coords = self.P_coords + np.array([3, 0, 0])
        self.P1_right = self.coords_to_point(self.P1_right_coords)
        
        # 左平移: P(2,3) → P'(0,3)
        self.P2_left_coords = self.P_coords + np.array([-2, 0, 0])
        self.P2_left = self.coords_to_point(self.P2_left_coords)
        
        # 上平移: P(2,3) → P'(2,5)
        self.P3_up_coords = self.P_coords + np.array([0, 2, 0])
        self.P3_up = self.coords_to_point(self.P3_up_coords)
        
        # 下平移: P(2,3) → P'(2,2)
        self.P4_down_coords = self.P_coords + np.array([0, -1, 0])
        self.P4_down = self.coords_to_point(self.P4_down_coords)
        
        # 综合平移: P(2,3) → 中间(4,3) → P'(4,0)
        self.P5_mid_coords = self.P_coords + np.array([2, 0, 0])  # 先右2
        self.P5_mid = self.coords_to_point(self.P5_mid_coords)
        
        self.P5_combined_coords = self.P5_mid_coords + np.array([0, -3, 0])  # 再下3
        self.P5_combined = self.coords_to_point(self.P5_combined_coords)
        
        # 验证几何数据
        self.verify_geometry()
    
    def coords_to_point(self, coords):
        """将逻辑坐标转换为Manim场景坐标"""
        return np.array([
            coords[0] * self.SCALE,
            coords[1] * self.SCALE,
            0
        ]) + self.OFFSET
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证右平移: 只有x坐标变化
        assert abs(self.P1_right_coords[1] - self.P_coords[1]) < epsilon, "右平移y坐标应不变"
        assert abs(self.P1_right_coords[0] - self.P_coords[0] - 3) < epsilon, "右平移x应+3"
        
        # 验证左平移: 只有x坐标变化
        assert abs(self.P2_left_coords[1] - self.P_coords[1]) < epsilon, "左平移y坐标应不变"
        assert abs(self.P2_left_coords[0] - self.P_coords[0] + 2) < epsilon, "左平移x应-2"
        
        # 验证上平移: 只有y坐标变化
        assert abs(self.P3_up_coords[0] - self.P_coords[0]) < epsilon, "上平移x坐标应不变"
        assert abs(self.P3_up_coords[1] - self.P_coords[1] - 2) < epsilon, "上平移y应+2"
        
        # 验证下平移: 只有y坐标变化
        assert abs(self.P4_down_coords[0] - self.P_coords[0]) < epsilon, "下平移x坐标应不变"
        assert abs(self.P4_down_coords[1] - self.P_coords[1] + 1) < epsilon, "下平移y应-1"
        
        # 验证综合平移
        expected = self.P_coords + np.array([2, -3, 0])
        assert np.allclose(self.P5_combined_coords, expected), "综合平移计算错误"
        
        print("✓ 几何验证通过")
    
    def create_coordinate_plane(self):
        """创建坐标平面"""
        plane = NumberPlane(
            x_range=self.x_range,
            y_range=self.y_range,
            x_length=self.x_length,
            y_length=self.y_length,
            background_line_style={
                "stroke_color": self.COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
            axis_config={
                "stroke_color": self.COLOR_AXIS,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 16,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to(self.OFFSET)
        
        return plane
    
    def create_point_with_label(self, position, coords, label_text, 
                                 color=None, label_direction=UR):
        """创建带坐标标签的点"""
        if color is None:
            color = self.COLOR_PRIMARY
        
        dot = Dot(position, color=color, radius=0.08)
        
        # 坐标标签
        coord_label = MathTex(
            f"({coords[0]:.0f}, {coords[1]:.0f})",
            font_size=20,
            color=WHITE
        ).next_to(dot, label_direction, buff=0.15)
        
        # 可选的点名标签 (如 "P", "P'")
        if label_text:
            name_label = Text(
                label_text,
                font="PingFang SC",
                font_size=18,
                color=color
            ).next_to(coord_label, DOWN, buff=0.05, aligned_edge=LEFT)
            return VGroup(dot, coord_label, name_label)
        
        return VGroup(dot, coord_label)
    
    def create_translation_arrow(self, start, end, color=None):
        """创建平移箭头"""
        if color is None:
            color = self.COLOR_ARROW
        
        arrow = Arrow(
            start=start,
            end=end,
            buff=0.1,
            color=color,
            stroke_width=5,
            tip_length=0.2,
            max_tip_length_to_length_ratio=0.25
        )
        return arrow
    
    def create_formula_box(self, formula_tex, position=DOWN*4.5, bg_color=None):
        """创建公式背景框"""
        if bg_color is None:
            bg_color = self.COLOR_FORMULA_BG
        
        formula = MathTex(formula_tex, font_size=28, color=WHITE)
        
        bg_rect = SurroundingRectangle(
            formula,
            color=bg_color,
            fill_opacity=0.8,
            fill_color=bg_color,
            buff=0.3,
            corner_radius=0.1
        )
        
        formula_group = VGroup(bg_rect, formula).move_to(position)
        return formula_group
    
    # ========================================
    # Scene 0: 开场钩子
    # ========================================
    
    def scene_0_opening_hook(self):
        """Scene 0: 开场钩子 - 吸引注意力"""
        # 作者信息 (顶部, 始终保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "点在坐标系里怎么\"移动\"?",
            font="PingFang SC",
            font_size=36,
            color=YELLOW
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简单坐标系和点
        simple_plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=4,
            background_line_style={
                "stroke_color": self.COLOR_GRID,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
            axis_config={
                "stroke_color": self.COLOR_AXIS,
                "stroke_width": 1.5,
                "include_tip": False,
            }
        ).move_to(UP * 2)
        
        simple_dot = Dot(
            simple_plane.coords_to_point(1, 1),
            color=self.COLOR_PRIMARY,
            radius=0.1
        )
        
        self.play(FadeIn(simple_plane), run_time=0.5)
        self.play(
            FadeIn(simple_dot, scale=0.5),
            Flash(simple_dot, color=self.COLOR_PRIMARY, flash_radius=0.3),
            run_time=0.5
        )
        self.wait(0.9)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(simple_plane),
            FadeOut(simple_dot),
            run_time=0.4
        )
    
    # ========================================
    # Scene 1: 建立坐标系
    # ========================================
    
    def scene_1_setup_coordinate_system(self):
        """Scene 1: 建立坐标系和初始点"""
        # 标题
        title = Text(
            "点的平移",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建坐标平面
        self.plane = self.create_coordinate_plane()
        self.play(Create(self.plane), run_time=1.2)
        
        # 轴标签
        x_label = MathTex("x", font_size=24).next_to(
            self.plane.get_x_axis().get_end(), DOWN, buff=0.2
        )
        y_label = MathTex("y", font_size=24).next_to(
            self.plane.get_y_axis().get_end(), LEFT, buff=0.2
        )
        
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 初始点P(2, 3)
        self.dot_P = Dot(self.P, color=self.COLOR_PRIMARY, radius=0.1)
        self.coord_label_P = MathTex(
            "P(2, 3)",
            font_size=24,
            color=WHITE
        ).next_to(self.dot_P, UR, buff=0.2)
        
        self.play(
            FadeIn(self.dot_P, scale=0.5),
            run_time=0.5
        )
        self.play(Write(self.coord_label_P), run_time=0.6)
        
        # 从点到坐标轴的虚线
        x_line = DashedLine(
            self.P,
            self.coords_to_point([2, 0, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        y_line = DashedLine(
            self.P,
            self.coords_to_point([0, 3, 0]),
            color=GRAY_B,
            dash_length=0.08
        )
        
        self.play(Create(x_line), Create(y_line), run_time=0.8)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(x_line),
            FadeOut(y_line),
            FadeOut(x_label),
            FadeOut(y_label),
            run_time=0.5
        )
    
    # ========================================
    # Scene 2: 向右平移
    # ========================================
    
    def scene_2_translate_right(self):
        """Scene 2: 向右平移 - 横坐标加"""
        # 说明文字
        explanation = Text(
            "向右平移3个单位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation, shift=DOWN * 0.2), run_time=0.5)
        
        # 公式
        formula = self.create_formula_box(
            r"(x, y) \rightarrow (x+3, y)"
        )
        self.play(FadeIn(formula), run_time=0.8)
        
        # 平移箭头
        arrow_right = self.create_translation_arrow(
            self.P,
            self.P1_right
        )
        self.play(GrowArrow(arrow_right), run_time=1.0)
        
        # 点移动
        new_dot = Dot(self.P1_right, color=self.COLOR_SECONDARY, radius=0.1)
        new_label = MathTex(
            "P'(5, 3)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(new_dot, UR, buff=0.2)
        
        self.play(
            Transform(self.dot_P.copy(), new_dot),
            run_time=1.2
        )
        self.add(new_dot)
        self.play(Write(new_label), run_time=0.6)
        
        # 高亮横坐标变化
        highlight_box = SurroundingRectangle(
            new_label[0][2:4],  # "5" in "P'(5, 3)"
            color=YELLOW,
            buff=0.05
        )
        self.play(Create(highlight_box), run_time=0.4)
        self.play(FadeOut(highlight_box), run_time=0.4)
        
        self.wait(2.0)  # 关键停留
        
        # 点恢复原位
        self.play(
            FadeOut(new_dot),
            FadeOut(new_label),
            run_time=0.4
        )
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(arrow_right),
            run_time=0.3
        )
    
    # ========================================
    # Scene 3: 向左平移
    # ========================================
    
    def scene_3_translate_left(self):
        """Scene 3: 向左平移 - 横坐标减"""
        explanation = Text(
            "向左平移2个单位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        formula = self.create_formula_box(
            r"(x, y) \rightarrow (x-2, y)"
        )
        self.play(FadeIn(formula), run_time=0.8)
        
        arrow_left = self.create_translation_arrow(
            self.P,
            self.P2_left,
            color="#9b59b6"
        )
        self.play(GrowArrow(arrow_left), run_time=1.0)
        
        new_dot = Dot(self.P2_left, color=self.COLOR_SECONDARY, radius=0.1)
        new_label = MathTex(
            "P'(0, 3)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(new_dot, UL, buff=0.2)
        
        self.play(
            Transform(self.dot_P.copy(), new_dot),
            run_time=1.2
        )
        self.add(new_dot)
        self.play(Write(new_label), run_time=0.6)
        
        self.wait(1.5)
        
        # 恢复
        self.play(
            FadeOut(new_dot),
            FadeOut(new_label),
            run_time=0.4
        )
        
        self.play(
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(arrow_left),
            run_time=0.3
        )
    
    # ========================================
    # Scene 4: 向上平移
    # ========================================
    
    def scene_4_translate_up(self):
        """Scene 4: 向上平移 - 纵坐标加"""
        explanation = Text(
            "向上平移2个单位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        formula = self.create_formula_box(
            r"(x, y) \rightarrow (x, y+2)"
        )
        self.play(FadeIn(formula), run_time=0.8)
        
        arrow_up = self.create_translation_arrow(
            self.P,
            self.P3_up,
            color=GREEN
        )
        self.play(GrowArrow(arrow_up), run_time=1.0)
        
        new_dot = Dot(self.P3_up, color=self.COLOR_SECONDARY, radius=0.1)
        new_label = MathTex(
            "P'(2, 5)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(new_dot, UR, buff=0.2)
        
        self.play(
            Transform(self.dot_P.copy(), new_dot),
            run_time=1.2
        )
        self.add(new_dot)
        self.play(Write(new_label), run_time=0.6)
        
        self.wait(1.5)
        
        self.play(
            FadeOut(new_dot),
            FadeOut(new_label),
            run_time=0.4
        )
        
        self.play(
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(arrow_up),
            run_time=0.3
        )
    
    # ========================================
    # Scene 5: 向下平移
    # ========================================
    
    def scene_5_translate_down(self):
        """Scene 5: 向下平移 - 纵坐标减"""
        explanation = Text(
            "向下平移1个单位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEXT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        formula = self.create_formula_box(
            r"(x, y) \rightarrow (x, y-1)"
        )
        self.play(FadeIn(formula), run_time=0.8)
        
        arrow_down = self.create_translation_arrow(
            self.P,
            self.P4_down,
            color=PURPLE
        )
        self.play(GrowArrow(arrow_down), run_time=1.0)
        
        new_dot = Dot(self.P4_down, color=self.COLOR_SECONDARY, radius=0.1)
        new_label = MathTex(
            "P'(2, 2)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(new_dot, DR, buff=0.2)
        
        self.play(
            Transform(self.dot_P.copy(), new_dot),
            run_time=1.2
        )
        self.add(new_dot)
        self.play(Write(new_label), run_time=0.6)
        
        self.wait(1.5)
        
        self.play(
            FadeOut(new_dot),
            FadeOut(new_label),
            run_time=0.4
        )
        
        self.play(
            FadeOut(explanation),
            FadeOut(formula),
            FadeOut(arrow_down),
            run_time=0.3
        )
    
    # ========================================
    # Scene 6: 综合平移
    # ========================================
    
    def scene_6_combined_translation(self):
        """Scene 6: 综合平移 - 同时改变横纵坐标"""
        explanation = Text(
            "向右2个单位，向下3个单位",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_TEXT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        formula = self.create_formula_box(
            r"(x, y) \rightarrow (x+2, y-3)"
        )
        self.play(FadeIn(formula), run_time=0.8)
        
        # 分步提示
        step_hint = Text(
            "分两步:",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).next_to(explanation, DOWN, buff=0.3)
        
        self.play(FadeIn(step_hint), run_time=0.4)
        
        # 第一步: 向右2
        arrow_h = self.create_translation_arrow(
            self.P,
            self.P5_mid,
            color=GREEN
        )
        arrow_h.set_style(stroke_width=3)
        
        self.play(GrowArrow(arrow_h), run_time=0.8)
        
        # 点移动到中间
        mid_dot = Dot(self.P5_mid, color=BLUE, radius=0.08)
        mid_label = MathTex(
            "(4, 3)",
            font_size=18,
            color=BLUE
        ).next_to(mid_dot, UR, buff=0.15)
        
        self.play(
            Transform(self.dot_P.copy(), mid_dot),
            run_time=1.0
        )
        self.add(mid_dot)
        self.play(Write(mid_label), run_time=0.5)
        
        # 第二步: 向下3
        arrow_v = self.create_translation_arrow(
            self.P5_mid,
            self.P5_combined,
            color=BLUE
        )
        arrow_v.set_style(stroke_width=3)
        
        self.play(GrowArrow(arrow_v), run_time=0.8)
        
        # 点移动到终点
        final_dot = Dot(self.P5_combined, color=self.COLOR_SECONDARY, radius=0.1)
        final_label = MathTex(
            "P'(4, 0)",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(final_dot, DR, buff=0.2)
        
        self.play(
            Transform(mid_dot.copy(), final_dot),
            run_time=1.0
        )
        self.add(final_dot)
        self.play(Write(final_label), run_time=0.5)
        
        self.wait(1.0)
        
        # 直接路径
        direct_arrow = self.create_translation_arrow(
            self.P,
            self.P5_combined,
            color=self.COLOR_ARROW
        )
        direct_arrow.set_style(stroke_width=6)
        
        direct_hint = Text(
            "也可以一步到位!",
            font="PingFang SC",
            font_size=20,
            color=YELLOW
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(direct_arrow),
            FadeIn(direct_hint),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(step_hint),
            FadeOut(formula),
            FadeOut(arrow_h),
            FadeOut(arrow_v),
            FadeOut(direct_arrow),
            FadeOut(mid_dot),
            FadeOut(mid_label),
            FadeOut(final_dot),
            FadeOut(final_label),
            FadeOut(direct_hint),
            FadeOut(self.dot_P),
            FadeOut(self.coord_label_P),
            run_time=0.6
        )
    
    # ========================================
    # Scene 7: 口诀总结
    # ========================================
    
    def scene_7_summary(self):
        """Scene 7: 口诀总结"""
        # 坐标系缩小并上移
        self.play(
            self.plane.animate.scale(0.45).move_to(UP * 4.5),
            run_time=0.8
        )
        
        # 标题
        title = Text(
            "平移规律总结",
            font="PingFang SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 四个公式卡片
        cards_data = [
            ("向右a", r"(x,y) \to (x+a, y)", self.COLOR_PRIMARY, UP * 1.2 + LEFT * 2),
            ("向左a", r"(x,y) \to (x-a, y)", "#9b59b6", UP * 1.2 + RIGHT * 2),
            ("向上b", r"(x,y) \to (x, y+b)", GREEN, DOWN * 0.3 + LEFT * 2),
            ("向下b", r"(x,y) \to (x, y-b)", PURPLE, DOWN * 0.3 + RIGHT * 2),
        ]
        
        cards = VGroup()
        for text, formula, color, pos in cards_data:
            # 标题
            card_title = Text(
                text,
                font="PingFang SC",
                font_size=20,
                color=color
            )
            
            # 公式
            card_formula = MathTex(
                formula,
                font_size=20
            )
            
            # 组合
            card = VGroup(card_title, card_formula).arrange(DOWN, buff=0.15)
            
            # 背景框
            card_bg = SurroundingRectangle(
                card,
                color=color,
                fill_opacity=0.2,
                fill_color=color,
                buff=0.2,
                corner_radius=0.08
            )
            
            card_group = VGroup(card_bg, card).move_to(pos)
            cards.add(card_group)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 8)  # 初始在左侧外
            self.play(
                card.animate.shift(RIGHT * 8),
                run_time=0.4
            )
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.5)
        
        # 口诀
        mnemonic = Text(
            "左减右加，下减上加",
            font="PingFang SC",
            font_size=42,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 2.2)
        
        self.play(FadeIn(mnemonic, scale=1.2), run_time=0.8)
        self.play(Circumscribe(mnemonic, color=YELLOW, run_time=1.0))
        
        self.wait(2.5)  # 记忆时间
        
        # 练习提示
        practice_hint = Text(
            "多做练习，熟能生巧!",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(practice_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理所有内容
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.6
        )
    
    # ========================================
    # Scene 8: 片尾
    # ========================================
    
    def scene_8_outro(self):
        """Scene 8: 片尾关注"""
        # 作者名放大
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
        
        self.play(FadeIn(author_name, scale=1.2), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，轻松学坐标!",
            font="PingFang SC",
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.6)
        
        # 装饰点阵
        dots = VGroup(*[
            Dot(
                follow_text.get_center() + 2.5 * np.array([
                    np.cos(i * TAU / 6),
                    np.sin(i * TAU / 6),
                    0
                ]),
                radius=0.08,
                color=self.COLOR_PRIMARY
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(dot, scale=0.5) for dot in dots],
            run_time=0.6
        )
        self.play(Rotate(dots, angle=PI, run_time=1.5))
        
        self.wait(1.0)


# 运行命令:
# manim -pql point_translation.py PointTranslation  # 快速预览
# manim -qh point_translation.py PointTranslation   # 高质量 (推荐)
# manim -qk point_translation.py PointTranslation   # 4K质量