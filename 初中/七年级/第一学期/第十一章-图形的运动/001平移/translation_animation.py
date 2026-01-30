"""
平移 (Translation) 教学动画
使用 Manim 创建的七年级数学教学视频

内容: 平移的定义、性质和应用
目标观众: 七年级学生
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


class TranslationAnimation(Scene):
    """
    平移教学动画场景
    
    场景顺序:
    1. 开场钩子 - 吸引注意力
    2. 定义介绍 - 说明平移概念
    3. 构建主三角形 - 创建演示图形
    4. 展示平移向量 - 明确方向和距离
    5. 执行平移动画 - 展示变换过程
    6. 平移的性质 - 强调三个关键性质
    7. 总结与片尾 - 巩固知识点
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 原始图形
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 平移后图形
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 重点标注
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助线
        self.COLOR_ARROW = "#2ecc71"        # 绿色 - 平移箭头
        self.COLOR_PATH = "#9b59b6"         # 紫色 - 轨迹路径
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_main_triangle()
        self.show_translation_vector()
        self.show_translation_animation()
        self.show_properties()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的精确坐标"""
        # 基准参数
        self.SCALE = 0.85
        self.OFFSET = UP * 2.0
        
        # 原始三角形顶点（设计为斜三角形）
        base_A = np.array([-2.0, 0.5, 0])
        base_B = np.array([-0.5, 0.5, 0])
        base_C = np.array([-1.25, 2.0, 0])
        
        # 应用缩放和偏移
        self.A = base_A * self.SCALE + self.OFFSET
        self.B = base_B * self.SCALE + self.OFFSET
        self.C = base_C * self.SCALE + self.OFFSET
        
        # 平移向量
        self.dx = 3.0
        self.dy = 1.5
        self.translation_vector = np.array([self.dx, self.dy, 0])
        
        # 平移后的顶点
        self.A_prime = self.A + self.translation_vector
        self.B_prime = self.B + self.translation_vector
        self.C_prime = self.C + self.translation_vector
        
        # 验证几何计算
        self.verify_geometry()
        
        print(f"✓ 几何设置完成")
        print(f"  原始三角形: A={self.A[:2]}, B={self.B[:2]}, C={self.C[:2]}")
        print(f"  平移向量: ({self.dx}, {self.dy})")
        print(f"  平移后: A'={self.A_prime[:2]}, B'={self.B_prime[:2]}, C'={self.C_prime[:2]}")
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证平移向量的一致性
        vec_AA = self.A_prime - self.A
        vec_BB = self.B_prime - self.B
        vec_CC = self.C_prime - self.C
        
        # 所有对应点的位移向量应该相等
        assert np.allclose(vec_AA, vec_BB, atol=epsilon), "平移向量不一致 (AA' vs BB')!"
        assert np.allclose(vec_BB, vec_CC, atol=epsilon), "平移向量不一致 (BB' vs CC')!"
        
        # 验证边长不变（平移保持距离）
        AB_original = np.linalg.norm(self.B - self.A)
        AB_translated = np.linalg.norm(self.B_prime - self.A_prime)
        assert abs(AB_original - AB_translated) < epsilon, "边长改变，平移错误!"
        
        # 验证位置在安全边界内
        all_points = [self.A, self.B, self.C, self.A_prime, self.B_prime, self.C_prime]
        for point in all_points:
            assert -4.0 <= point[0] <= 4.0, f"X坐标越界: {point[0]}"
            assert -7.0 <= point[1] <= 7.0, f"Y坐标越界: {point[1]}"
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部小字)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_main = Text(
            "图形怎么移动？",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        hook_sub = Text(
            "平移变换的秘密",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 4.7)
        
        self.play(Write(hook_main), run_time=0.8)
        self.play(FadeIn(hook_sub), run_time=0.4)
        
        # 演示正方形
        demo_square = Square(
            side_length=1.2,
            color=self.COLOR_PRIMARY,
            fill_opacity=0.3,
            stroke_width=4
        ).move_to(LEFT * 1.5 + UP * 2)
        
        self.play(Create(demo_square), run_time=0.6)
        
        # 快速平移演示
        self.play(
            demo_square.animate.shift(RIGHT * 3),
            run_time=1.0,
            rate_func=smooth
        )
        
        # 问题文字
        question = Text(
            "什么是平移？",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(hook_main),
            FadeOut(hook_sub),
            FadeOut(demo_square),
            FadeOut(question),
            run_time=0.5
        )
    
    def show_definition(self):
        """场景2: 定义介绍 (5-12秒)"""
        # 标题
        title = Text(
            "什么是平移？",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义文字 - 分部分显示
        def_part1_cn = Text(
            "平移是把图形沿某个",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        )
        
        def_part1_key = Text(
            "方向",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        
        def_part1 = VGroup(def_part1_cn, def_part1_key).arrange(RIGHT, buff=0.1).move_to(UP * 4.5)
        
        def_part2_cn1 = Text(
            "移动一定",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        )
        
        def_part2_key = Text(
            "距离",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        
        def_part2_cn2 = Text(
            "的变换",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        )
        
        def_part2 = VGroup(def_part2_cn1, def_part2_key, def_part2_cn2).arrange(RIGHT, buff=0.1).move_to(UP * 3.8)
        
        self.play(FadeIn(def_part1, shift=DOWN * 0.2), run_time=0.6)
        self.play(FadeIn(def_part2, shift=DOWN * 0.2), run_time=0.6)
        
        # 高亮关键词
        self.play(
            Indicate(def_part1_key, scale_factor=1.3, color=YELLOW),
            Indicate(def_part2_key, scale_factor=1.3, color=YELLOW),
            run_time=0.8
        )
        
        # 补充说明
        note = Text(
            "方向 + 距离 = 平移向量",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.8)
        
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(def_part1),
            FadeOut(def_part2),
            FadeOut(note),
            run_time=0.6
        )
    
    def show_main_triangle(self):
        """场景3: 构建主三角形 (12-18秒)"""
        # 标题
        title = Text(
            "三角形ABC",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 创建三角形
        self.triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_PRIMARY
        )
        
        self.play(Create(self.triangle_ABC), run_time=1.2)
        
        # 顶点标签
        self.label_A = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.A, LEFT, buff=0.15)
        self.label_B = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.B, RIGHT, buff=0.15)
        self.label_C = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE).next_to(self.C, UP, buff=0.15)
        
        self.play(FadeIn(self.label_A), run_time=0.3)
        self.play(FadeIn(self.label_B), run_time=0.3)
        self.play(FadeIn(self.label_C), run_time=0.3)
        
        # 说明文字
        explain = Text(
            "这是我们的原始三角形",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(FadeOut(title), FadeOut(explain), run_time=0.5)
    
    def show_translation_vector(self):
        """场景4: 展示平移向量 (18-26秒)"""
        # 标题
        title = Text(
            "平移方向与距离",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_ARROW
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 平移箭头 - 从三角形重心开始
        triangle_center = (self.A + self.B + self.C) / 3
        arrow_start = triangle_center
        arrow_end = triangle_center + self.translation_vector
        
        self.translation_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_ARROW,
            stroke_width=6,
            buff=0,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(self.translation_arrow), run_time=1.0)
        
        # 水平和垂直分量虚线
        h_dash_start = arrow_start
        h_dash_end = arrow_start + np.array([self.dx, 0, 0])
        v_dash_start = h_dash_end
        v_dash_end = arrow_end
        
        h_dash = DashedLine(
            h_dash_start,
            h_dash_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        v_dash = DashedLine(
            v_dash_start,
            v_dash_end,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(h_dash), run_time=0.5)
        self.play(Create(v_dash), run_time=0.5)
        
        # 标注
        h_label_cn = Text("向右", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        h_label_num = Text("3", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        h_label_unit = Text("单位", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        h_label = VGroup(h_label_cn, h_label_num, h_label_unit).arrange(RIGHT, buff=0.05)
        h_label.next_to(h_dash, DOWN, buff=0.2)
        
        v_label_cn = Text("向上", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        v_label_num = Text("1.5", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        v_label_unit = Text("单位", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        v_label = VGroup(v_label_cn, v_label_num, v_label_unit).arrange(RIGHT, buff=0.05)
        v_label.next_to(v_dash, RIGHT, buff=0.2)
        
        self.play(FadeIn(h_label), run_time=0.4)
        self.play(FadeIn(v_label), run_time=0.4)
        
        # 说明文字
        explain = Text(
            "平移向量决定了移动的方向和距离",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(h_dash),
            FadeOut(v_dash),
            FadeOut(h_label),
            FadeOut(v_label),
            FadeOut(explain),
            run_time=0.6
        )
    
    def show_translation_animation(self):
        """场景5: 执行平移动画 (26-38秒)"""
        # 标题
        title = Text(
            "开始平移！",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title, scale=1.2), run_time=0.5)
        
        # 创建三角形副本用于平移
        self.triangle_prime = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_SECONDARY,
            stroke_width=4,
            fill_opacity=0.2,
            fill_color=self.COLOR_SECONDARY
        )
        
        # 添加到场景（初始与原三角形重合）
        self.add(self.triangle_prime)
        
        # 创建轨迹路径追踪器
        path_A = TracedPath(
            lambda: self.triangle_prime.get_vertices()[0],
            stroke_color=self.COLOR_PATH,
            stroke_width=2,
            dissipating_time=None
        )
        path_B = TracedPath(
            lambda: self.triangle_prime.get_vertices()[1],
            stroke_color=self.COLOR_PATH,
            stroke_width=2,
            dissipating_time=None
        )
        path_C = TracedPath(
            lambda: self.triangle_prime.get_vertices()[2],
            stroke_color=self.COLOR_PATH,
            stroke_width=2,
            dissipating_time=None
        )
        
        self.add(path_A, path_B, path_C)
        
        # 执行平移动画
        self.play(
            self.triangle_prime.animate.shift(self.translation_vector),
            run_time=2.5,
            rate_func=smooth
        )
        
        # 移除路径追踪器
        self.remove(path_A, path_B, path_C)
        
        # 添加对应点连线
        line_AA = DashedLine(
            self.A,
            self.A_prime,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        line_BB = DashedLine(
            self.B,
            self.B_prime,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        line_CC = DashedLine(
            self.C,
            self.C_prime,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(line_AA), run_time=0.5)
        self.play(Create(line_BB), run_time=0.5)
        self.play(Create(line_CC), run_time=0.5)
        
        # 平移后的顶点标签
        self.label_A_prime = Text("A'", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_SECONDARY).next_to(self.A_prime, LEFT, buff=0.15)
        self.label_B_prime = Text("B'", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_SECONDARY).next_to(self.B_prime, RIGHT, buff=0.15)
        self.label_C_prime = Text("C'", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_SECONDARY).next_to(self.C_prime, UP, buff=0.15)
        
        self.play(FadeIn(self.label_A_prime), run_time=0.3)
        self.play(FadeIn(self.label_B_prime), run_time=0.3)
        self.play(FadeIn(self.label_C_prime), run_time=0.3)
        
        # 说明文字
        explain = Text(
            "对应点沿着相同方向移动相同距离",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(explain), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(FadeOut(title), FadeOut(explain), run_time=0.5)
        
        # 保存连线以便后续使用
        self.connecting_lines = VGroup(line_AA, line_BB, line_CC)
    
    def show_properties(self):
        """场景6: 平移的性质 (38-52秒)"""
        # 标题
        title = Text(
            "平移的性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 性质1卡片
        prop1_icon = Circle(radius=0.15, fill_color=self.COLOR_PRIMARY, fill_opacity=1, stroke_width=0)
        prop1_text = Text(
            "形状、大小、方向均不变",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        prop1_card = VGroup(prop1_icon, prop1_text).arrange(RIGHT, buff=0.2).move_to(UP * 5.2)
        
        self.play(FadeIn(prop1_card, shift=UP * 0.3), run_time=0.6)
        
        # 闪烁强调
        self.play(
            Flash(self.triangle_ABC.get_center(), color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.4
        )
        self.play(
            Flash(self.triangle_prime.get_center(), color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.4
        )
        self.wait(1.0)
        
        # 性质2卡片
        prop2_icon = Circle(radius=0.15, fill_color=self.COLOR_ARROW, fill_opacity=1, stroke_width=0)
        prop2_text = Text(
            "对应点连线平行且相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        prop2_card = VGroup(prop2_icon, prop2_text).arrange(RIGHT, buff=0.2).move_to(UP * 4.3)
        
        self.play(FadeIn(prop2_card, shift=UP * 0.3), run_time=0.6)
        
        # 标注平行符号
        parallel_mark_1 = self.create_parallel_mark(self.A, self.A_prime)
        parallel_mark_2 = self.create_parallel_mark(self.B, self.B_prime)
        parallel_mark_3 = self.create_parallel_mark(self.C, self.C_prime)
        
        parallel_marks = VGroup(parallel_mark_1, parallel_mark_2, parallel_mark_3)
        
        self.play(FadeIn(parallel_marks), run_time=0.8)
        
        # 标注相等符号（在连线中点处）
        equal_mark_1 = self.create_equal_mark((self.A + self.A_prime) / 2)
        equal_mark_2 = self.create_equal_mark((self.B + self.B_prime) / 2)
        equal_mark_3 = self.create_equal_mark((self.C + self.C_prime) / 2)
        
        equal_marks = VGroup(equal_mark_1, equal_mark_2, equal_mark_3)
        
        self.play(FadeIn(equal_marks), run_time=0.6)
        self.wait(1.5)
        
        # 性质3卡片
        prop3_icon = Circle(radius=0.15, fill_color=self.COLOR_SECONDARY, fill_opacity=1, stroke_width=0)
        prop3_text = Text(
            "对应线段平行且相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        )
        prop3_card = VGroup(prop3_icon, prop3_text).arrange(RIGHT, buff=0.2).move_to(UP * 3.4)
        
        self.play(FadeIn(prop3_card, shift=UP * 0.3), run_time=0.6)
        
        # 高亮边AB和A'B'
        edge_AB = Line(self.A, self.B, color=YELLOW, stroke_width=6)
        edge_AB_prime = Line(self.A_prime, self.B_prime, color=YELLOW, stroke_width=6)
        
        self.play(Create(edge_AB), run_time=0.5)
        self.play(Create(edge_AB_prime), run_time=0.5)
        
        # 平行标记
        parallel_edge_mark = self.create_parallel_mark(
            (self.A + self.B) / 2,
            (self.A_prime + self.B_prime) / 2,
            size=0.3
        )
        
        self.play(FadeIn(parallel_edge_mark), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(prop1_card),
            FadeOut(prop2_card),
            FadeOut(prop3_card),
            FadeOut(parallel_marks),
            FadeOut(equal_marks),
            FadeOut(edge_AB),
            FadeOut(edge_AB_prime),
            FadeOut(parallel_edge_mark),
            run_time=0.6
        )
    
    def create_parallel_mark(self, point1, point2, size=0.2):
        """创建平行符号标记"""
        direction = point2 - point1
        direction_normalized = direction / np.linalg.norm(direction)
        perpendicular = np.array([-direction_normalized[1], direction_normalized[0], 0])
        
        midpoint = (point1 + point2) / 2
        
        line1 = Line(
            midpoint - perpendicular * size / 2,
            midpoint + perpendicular * size / 2,
            color=YELLOW,
            stroke_width=2
        )
        line2 = Line(
            midpoint - perpendicular * size / 2 + direction_normalized * 0.1,
            midpoint + perpendicular * size / 2 + direction_normalized * 0.1,
            color=YELLOW,
            stroke_width=2
        )
        
        return VGroup(line1, line2)
    
    def create_equal_mark(self, point, size=0.15):
        """创建相等符号标记"""
        line1 = Line(
            point + UP * size / 2,
            point + DOWN * size / 2,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        line2 = Line(
            point + UP * size / 2 + RIGHT * 0.08,
            point + DOWN * size / 2 + RIGHT * 0.08,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        return VGroup(line1, line2)
    
    def show_outro(self):
        """场景7: 总结与片尾 (52-65秒)"""
        # 清空所有图形
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.triangle_prime),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_C),
            FadeOut(self.label_A_prime),
            FadeOut(self.label_B_prime),
            FadeOut(self.label_C_prime),
            FadeOut(self.translation_arrow),
            FadeOut(self.connecting_lines),
            run_time=0.8
        )
        
        # 总结标题
        summary_title = Text(
            "平移变换 - 关键要点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 要点列表
        point1_icon = Text("1", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_PRIMARY, weight=BOLD)
        point1_text = Text(
            "平移 = 方向 + 距离",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        point1 = VGroup(point1_icon, point1_text).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        point1.shift(LEFT * 10)  # 初始在左侧外
        
        point2_icon = Text("2", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_ARROW, weight=BOLD)
        point2_text_cn = Text("对应点连线: ", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        point2_text_formula = MathTex(r"AA' \parallel BB'", font_size=28, color=self.COLOR_HIGHLIGHT)
        point2_text_and = Text(" 且相等", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        point2_content = VGroup(point2_text_cn, point2_text_formula, point2_text_and).arrange(RIGHT, buff=0.1)
        point2 = VGroup(point2_icon, point2_content).arrange(RIGHT, buff=0.3).move_to(UP * 2.3)
        point2.shift(LEFT * 10)
        
        point3_icon = Text("3", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_SECONDARY, weight=BOLD)
        point3_text = Text(
            "形状、大小、方向都不变",
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        point3 = VGroup(point3_icon, point3_text).arrange(RIGHT, buff=0.3).move_to(UP * 1.1)
        point3.shift(LEFT * 10)
        
        # 滑入动画
        self.play(point1.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(point2.animate.shift(RIGHT * 10), run_time=0.5)
        self.wait(0.2)
        self.play(point3.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 应用提示
        application_hint = Text(
            "平移在坐标系、向量、全等变换中都很重要！",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(application_hint), run_time=0.6)
        self.wait(2.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_B
        ).move_to(DOWN * 3.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        # 装饰小三角形
        triangles = VGroup(*[
            Polygon(
                ORIGIN,
                RIGHT * 0.3,
                UP * 0.3,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.8,
                stroke_width=0
            ).scale(0.4).move_to(
                follow_text.get_center() + 1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3),
            FadeOut(application_hint),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )


# 运行命令:
# manim -pql translation_animation.py TranslationAnimation  # 快速预览
# manim -qh translation_animation.py TranslationAnimation   # 高质量渲染