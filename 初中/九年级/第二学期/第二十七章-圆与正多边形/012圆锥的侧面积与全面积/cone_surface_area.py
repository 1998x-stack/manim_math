"""
圆锥的侧面积与全面积教学动画 - Cone Surface Area Animation
使用 Manim 创建的九年级几何教学视频

内容: 圆锥侧面积、底面积、全面积公式及其推导
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


class ConeSurfaceArea(Scene):
    """
    圆锥侧面积与全面积教学动画场景
    
    场景顺序:
    1. 开场钩子（冰淇淋甜筒）
    2. 圆锥组成部分介绍
    3. 侧面展开动画（关键场景）
    4. 扇形与圆锥的关系
    5. 侧面积公式推导
    6. 底面积公式
    7. 全面积公式
    8. 综合示例
    9. 结尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_cone_parts()
        self.scene_3_unfold_animation()
        self.scene_4_sector_cone_relation()
        self.scene_5_lateral_area_formula()
        self.scene_6_base_area_formula()
        self.scene_7_total_area_formula()
        self.scene_8_comprehensive_example()
        self.scene_9_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一计算和验证"""
        # 配色方案
        self.COLOR_CONE = "#e74c3c"          # 红色 - 圆锥侧面
        self.COLOR_BASE = "#3498db"          # 蓝色 - 底面圆
        self.COLOR_SLANT = "#f39c12"         # 橙色 - 母线
        self.COLOR_SECTOR = "#e74c3c"        # 红色 - 扇形
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 重点标注
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助元素
        self.COLOR_FORMULA = "#2ecc71"       # 绿色 - 公式
        
        # ========== 圆锥基准参数 ==========
        self.radius = 1.5              # 底面半径
        self.height = 2.5              # 高度
        
        # ========== 派生参数（精确计算）==========
        # 母线长度（勾股定理）
        self.slant_length = np.sqrt(self.radius**2 + self.height**2)
        
        # 底面周长
        self.base_circumference = 2 * PI * self.radius
        
        # 扇形参数
        self.sector_radius = self.slant_length  # 扇形半径 = 母线长
        self.sector_arc_length = self.base_circumference  # 扇形弧长 = 底面周长
        self.sector_angle = self.sector_arc_length / self.sector_radius  # 扇形圆心角（弧度）
        
        # ========== 面积计算 ==========
        self.lateral_area = PI * self.radius * self.slant_length  # 侧面积
        self.base_area = PI * self.radius**2  # 底面积
        self.total_area = PI * self.radius * (self.slant_length + self.radius)  # 全面积
        
        # ========== 验证计算 ==========
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证母线长度（勾股定理）
        expected_slant = np.sqrt(self.radius**2 + self.height**2)
        assert abs(self.slant_length - expected_slant) < epsilon, \
            f"母线长度计算错误: {self.slant_length} vs {expected_slant}"
        
        # 验证扇形参数
        # 扇形弧长应该等于底面周长
        assert abs(self.sector_arc_length - self.base_circumference) < epsilon, \
            "扇形弧长不等于底面周长"
        
        # 验证扇形圆心角必须 < 2π (360度)
        assert self.sector_angle < 2 * PI, \
            f"扇形圆心角 {np.degrees(self.sector_angle)}° >= 360°"
        
        # 验证面积公式一致性
        # S_全 = S_侧 + S_底
        total_check = self.lateral_area + self.base_area
        assert abs(self.total_area - total_check) < epsilon, \
            f"全面积公式不一致: {self.total_area} vs {total_check}"
        
        print("✓ 几何验证通过")
        print(f"  - 底面半径: {self.radius:.2f}")
        print(f"  - 高度: {self.height:.2f}")
        print(f"  - 母线长: {self.slant_length:.4f}")
        print(f"  - 扇形圆心角: {np.degrees(self.sector_angle):.2f}°")
        print(f"  - 侧面积: {self.lateral_area:.4f}")
        print(f"  - 底面积: {self.base_area:.4f}")
        print(f"  - 全面积: {self.total_area:.4f}")
    
    def create_cone_2d(self, center, scale=1.0):
        """
        创建圆锥的2D侧视图
        
        返回: VGroup(left_line, right_line, base_ellipse, apex_dot)
        """
        r = self.radius * scale
        h = self.height * scale
        
        apex = center + (h/2) * UP
        base_center = center - (h/2) * UP
        
        # 左右轮廓线
        left_line = Line(
            apex,
            base_center + r * LEFT,
            color=self.COLOR_CONE,
            stroke_width=3
        )
        
        right_line = Line(
            apex,
            base_center + r * RIGHT,
            color=self.COLOR_CONE,
            stroke_width=3
        )
        
        # 底面椭圆（透视效果）
        base_ellipse = Ellipse(
            width=r * 2,
            height=r * 0.4,  # 压缩高度制造透视
            color=self.COLOR_BASE,
            stroke_width=2
        ).move_to(base_center)
        
        # 顶点
        apex_dot = Dot(apex, color=self.COLOR_CONE, radius=0.05)
        
        cone = VGroup(left_line, right_line, base_ellipse, apex_dot)
        return cone
    
    def scene_1_opening(self):
        """场景1: 开场钩子 - 冰淇淋甜筒"""
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "这个甜筒装多少？",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 圆锥示意图
        cone_center = np.array([0, 1.5, 0])
        cone_visual = self.create_cone_2d(cone_center, scale=1.2)
        
        # 填充颜色
        cone_fill = Polygon(
            cone_visual[0].get_start(),  # 顶点
            cone_visual[0].get_end(),    # 左底
            cone_visual[1].get_end(),    # 右底
            color=self.COLOR_CONE,
            fill_opacity=0.5,
            stroke_width=0
        )
        
        self.play(
            FadeIn(cone_fill, scale=0.8),
            Create(cone_visual),
            run_time=1.0
        )
        
        # 问题文字
        question = Text(
            "表面积是多少？",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            FadeOut(cone_visual),
            FadeOut(cone_fill),
            run_time=0.6
        )
    
    def scene_2_cone_parts(self):
        """场景2: 圆锥组成部分介绍"""
        # 标题
        title = Text(
            "圆锥的组成",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 圆锥主体
        cone_center = np.array([0, 1.0, 0])
        self.cone = self.create_cone_2d(cone_center, scale=1.3)
        
        # 填充
        cone_fill = Polygon(
            self.cone[0].get_start(),
            self.cone[0].get_end(),
            self.cone[1].get_end(),
            color=self.COLOR_CONE,
            fill_opacity=0.4,
            stroke_width=0
        )
        
        self.play(
            FadeIn(cone_fill, scale=0.8),
            Create(self.cone),
            run_time=1.0
        )
        
        # 获取关键点
        apex = self.cone[0].get_start()
        base_center = self.cone[2].get_center()
        base_right = self.cone[1].get_end()
        
        # 1. 底面高亮
        self.play(
            self.cone[2].animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            run_time=0.6
        )
        
        base_label = Text(
            "底面（圆）",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_BASE
        ).next_to(self.cone[2], DOWN, buff=0.3)
        
        self.play(Write(base_label), run_time=0.4)
        self.play(self.cone[2].animate.set_stroke(color=self.COLOR_BASE, width=2), run_time=0.3)
        self.wait(0.3)
        self.play(FadeOut(base_label), run_time=0.3)
        
        # 2. 母线高亮
        slant_line = Line(
            apex,
            base_right,
            color=self.COLOR_SLANT,
            stroke_width=5
        )
        
        self.play(Create(slant_line), run_time=0.5)
        
        # 母线标注
        slant_brace = Brace(slant_line, direction=RIGHT, buff=0.1, color=self.COLOR_SLANT)
        slant_label = Text(
            "l", 
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SLANT
        ).next_to(slant_brace, RIGHT, buff=0.1)
        
        slant_text = Text(
            "母线",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SLANT
        ).next_to(slant_label, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(slant_brace),
            Write(slant_label),
            Write(slant_text),
            run_time=0.6
        )
        self.wait(0.4)
        self.play(
            FadeOut(slant_brace),
            FadeOut(slant_text),
            slant_line.animate.set_stroke(width=3),
            run_time=0.3
        )
        
        # 3. 侧面高亮
        self.play(
            self.cone[0].animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            self.cone[1].animate.set_stroke(color=self.COLOR_HIGHLIGHT, width=5),
            cone_fill.animate.set_fill(opacity=0.7),
            run_time=0.6
        )
        
        lateral_label = Text(
            "侧面",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_CONE
        ).move_to(cone_center + UP * 0.5)
        
        self.play(Write(lateral_label), run_time=0.4)
        self.wait(0.5)
        
        # 恢复
        self.play(
            self.cone[0].animate.set_stroke(color=self.COLOR_CONE, width=3),
            self.cone[1].animate.set_stroke(color=self.COLOR_CONE, width=3),
            cone_fill.animate.set_fill(opacity=0.4),
            FadeOut(lateral_label),
            run_time=0.3
        )
        
        self.wait(1.0)
        
        # 保存元素供下一场景使用
        self.cone_fill = cone_fill
        self.slant_line = slant_line
        self.slant_label = slant_label
        
        # 清理
        self.play(FadeOut(title), run_time=0.4)
    
    def scene_3_unfold_animation(self):
        """场景3: 侧面展开动画（关键场景）"""
        # 标题
        title = Text(
            "侧面展开图",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 提示文字
        hint_text = Text(
            "剪开侧面，展平...",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(hint_text), run_time=0.5)
        
        # 圆锥轻微旋转
        self.play(
            Rotate(VGroup(self.cone, self.cone_fill, self.slant_line, self.slant_label), 
                   angle=PI/6, 
                   about_point=self.cone.get_center()),
            run_time=1.0
        )
        
        # 分离侧面（向右移动）
        lateral_group = VGroup(self.cone[0], self.cone[1], self.cone_fill)
        
        self.play(
            lateral_group.animate.shift(RIGHT * 1.5),
            self.slant_line.animate.shift(RIGHT * 1.5),
            self.slant_label.animate.shift(RIGHT * 1.5),
            FadeOut(self.cone[2]),  # 底面圆淡出
            FadeOut(self.cone[3]),  # 顶点淡出
            run_time=0.8
        )
        
        # 创建扇形（展开后的形状）
        sector_center = np.array([0, 1.0, 0])
        
        # 注意：扇形角度约185°（> 180°）是正常的
        # Sector 类直接使用 angle 参数，不需要 other_angle
        # 只有 Angle 类在角度 > 180° 时才需要 other_angle=True
        sector = Sector(
            arc_center=sector_center,
            radius=self.sector_radius * 1.3,  # 匹配圆锥缩放
            angle=self.sector_angle,
            start_angle=-self.sector_angle/2,  # 居中显示
            color=self.COLOR_SECTOR,
            fill_opacity=0.5,
            stroke_width=3
        )
        
        # 展开变换
        self.play(
            Transform(self.cone_fill, sector),
            FadeOut(self.cone[0]),
            FadeOut(self.cone[1]),
            FadeOut(self.slant_line),
            FadeOut(self.slant_label),
            FadeOut(hint_text),
            run_time=2.0
        )
        
        # 扇形高亮
        self.play(
            Indicate(self.cone_fill, scale_factor=1.1),
            run_time=0.6
        )
        
        self.wait(1.0)
        
        # 保存扇形供下一场景使用
        self.sector = self.cone_fill
        self.sector_center = sector_center
        
        # 清理
        self.play(FadeOut(title), run_time=0.4)
    
    def scene_4_sector_cone_relation(self):
        """场景4: 扇形与圆锥的关系"""
        # 标题
        title = Text(
            "参数对应",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 扇形移到上方
        self.play(
            self.sector.animate.scale(0.7).move_to(UP * 2.5),
            run_time=0.6
        )
        
        # 标注扇形半径
        sector_scaled_radius = self.sector_radius * 1.3 * 0.7
        radius_line = Line(
            UP * 2.5,
            UP * 2.5 + sector_scaled_radius * RIGHT * 0.9,
            color=self.COLOR_SLANT,
            stroke_width=4
        )
        
        radius_label = MathTex(
            "l",
            font_size=32,
            color=self.COLOR_SLANT
        ).next_to(radius_line, DOWN, buff=0.1)
        
        self.play(
            Create(radius_line),
            Write(radius_label),
            run_time=0.8
        )
        
        # 对应关系1
        relation_1 = Text(
            "扇形半径 = 母线长 l",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(relation_1), run_time=0.6)
        
        # 标注扇形弧长
        arc_mid_angle = -self.sector_angle/2 + self.sector_angle/2
        arc_mid_point = UP * 2.5 + sector_scaled_radius * np.array([
            np.cos(arc_mid_angle),
            np.sin(arc_mid_angle),
            0
        ]) * 0.9
        
        arc_label = MathTex(
            "2\\pi r",
            font_size=28,
            color=self.COLOR_BASE
        ).move_to(arc_mid_point + UP * 0.5)
        
        # 弧长箭头
        arc_arrow = CurvedArrow(
            arc_mid_point,
            arc_label.get_bottom(),
            color=self.COLOR_BASE,
            stroke_width=2
        )
        
        self.play(
            FadeIn(arc_label),
            Create(arc_arrow),
            run_time=0.8
        )
        
        # 对应关系2
        relation_2 = Text(
            "扇形弧长 = 底面周长 2πr",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(ORIGIN)
        
        self.play(FadeIn(relation_2), run_time=0.6)
        
        # 小圆锥示意图
        cone_small_center = DOWN * 2.5
        cone_small = self.create_cone_2d(cone_small_center, scale=0.6)
        
        # 标注
        r_label = MathTex(
            "r",
            font_size=24,
            color=self.COLOR_BASE
        ).next_to(cone_small[2], DOWN, buff=0.1)
        
        l_label = MathTex(
            "l",
            font_size=24,
            color=self.COLOR_SLANT
        ).next_to(cone_small[1].get_center(), RIGHT, buff=0.2)
        
        self.play(
            Create(cone_small),
            Write(r_label),
            Write(l_label),
            run_time=0.8
        )
        
        # 连接箭头
        arrow_1 = Arrow(
            relation_1.get_bottom(),
            l_label.get_top(),
            color=self.COLOR_AUXILIARY,
            buff=0.1,
            stroke_width=2
        )
        
        arrow_2 = Arrow(
            relation_2.get_bottom(),
            r_label.get_top(),
            color=self.COLOR_AUXILIARY,
            buff=0.1,
            stroke_width=2
        )
        
        self.play(
            GrowArrow(arrow_1),
            GrowArrow(arrow_2),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.sector),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(arc_label),
            FadeOut(arc_arrow),
            FadeOut(relation_1),
            FadeOut(relation_2),
            FadeOut(cone_small),
            FadeOut(r_label),
            FadeOut(l_label),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            run_time=0.6
        )
    
    def scene_5_lateral_area_formula(self):
        """场景5: 侧面积公式推导"""
        # 标题
        title = Text(
            "侧面积公式",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 扇形面积公式
        step_1_text = Text(
            "扇形面积:",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 3.5 + LEFT * 2.5)
        
        step_1_formula = MathTex(
            r"S = \frac{1}{2} \times", r"\text{arc} \times", r"\text{radius}",
            font_size=32
        ).next_to(step_1_text, RIGHT, buff=0.3)
        
        # 注意：这里用了英文避免LaTeX中文问题
        
        self.play(
            Write(step_1_text),
            Write(step_1_formula),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 代入提示
        hint = Text(
            "弧长 = 2πr, 半径 = l",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.3)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 代入步骤
        step_2 = MathTex(
            r"S = \frac{1}{2} \times 2\pi r \times l",
            font_size=34
        ).move_to(UP * 1.2)
        
        # Color the parts: check actual length and adjust indices
        if len(step_2[0]) > 14:
            step_2[0][10:15].set_color(self.COLOR_BASE)
        if len(step_2[0]) > 18:
            step_2[0][18].set_color(self.COLOR_SLANT)
        
        self.play(Write(step_2), run_time=1.2)
        self.wait(0.5)
        
        # 简化
        step_3 = MathTex(
            r"S = \pi r l",
            font_size=38
        ).move_to(DOWN * 0.3)
        
        step_3[0][2].set_color(self.COLOR_BASE)  # r
        step_3[0][3].set_color(self.COLOR_SLANT)  # l
        
        arrow = Arrow(UP * 0.7, DOWN * 0.1, color=self.COLOR_FORMULA, buff=0.1)
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(step_3), run_time=1.0)
        
        # 最终公式框
        final_formula = MathTex(
            r"S_{\text{lateral}} = \pi r l",
            font_size=44
        ).move_to(DOWN * 2)
        
        final_formula[0][0].set_color(self.COLOR_CONE)  # S
        final_formula[0][-2].set_color(self.COLOR_BASE)  # r
        final_formula[0][-1].set_color(self.COLOR_SLANT)  # l
        
        formula_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            Write(final_formula),
            Create(formula_box),
            run_time=1.2
        )
        self.play(Indicate(final_formula, scale_factor=1.1), run_time=0.8)
        self.wait(2.0)
        
        # 保存公式
        self.lateral_formula = VGroup(final_formula, formula_box)
        
        # 清理中间步骤
        self.play(
            FadeOut(title),
            FadeOut(step_1_text),
            FadeOut(step_1_formula),
            FadeOut(hint),
            FadeOut(step_2),
            FadeOut(arrow),
            FadeOut(step_3),
            run_time=0.6
        )
        
        # 公式移到顶部
        self.play(
            self.lateral_formula.animate.scale(0.5).move_to(UP * 6.5 + LEFT * 2),
            run_time=0.5
        )
    
    def scene_6_base_area_formula(self):
        """场景6: 底面积公式"""
        # 标题
        title = Text(
            "底面积",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 底面圆
        base_circle = Circle(
            radius=1.5,
            color=self.COLOR_BASE,
            fill_opacity=0.3,
            stroke_width=4
        ).move_to(UP * 1.5)
        
        self.play(Create(base_circle), run_time=0.8)
        
        # 半径标注
        center = base_circle.get_center()
        radius_point = center + 1.5 * RIGHT
        
        radius_line = Line(center, radius_point, color=self.COLOR_BASE, stroke_width=3)
        radius_dot = Dot(center, color=self.COLOR_BASE, radius=0.06)
        
        r_label = MathTex("r", font_size=32, color=self.COLOR_BASE).next_to(radius_line, DOWN, buff=0.1)
        
        self.play(
            Create(radius_line),
            FadeIn(radius_dot),
            Write(r_label),
            run_time=0.6
        )
        
        # 圆面积公式
        circle_formula = MathTex(
            r"S_{\text{circle}} = \pi r^2",
            font_size=36
        ).move_to(DOWN * 0.5)
        
        circle_formula[0][-2].set_color(self.COLOR_BASE)  # r
        
        self.play(Write(circle_formula), run_time=0.8)
        
        # 底面积公式
        base_formula = MathTex(
            r"S_{\text{base}} = \pi r^2",
            font_size=44
        ).move_to(DOWN * 2.5)
        
        base_formula[0][0].set_color(self.COLOR_BASE)  # S
        base_formula[0][-2].set_color(self.COLOR_BASE)  # r
        
        formula_box = SurroundingRectangle(
            base_formula,
            color=self.COLOR_FORMULA,
            buff=0.2,
            corner_radius=0.1
        )
        
        self.play(
            Write(base_formula),
            Create(formula_box),
            run_time=0.8
        )
        self.play(Indicate(base_formula, scale_factor=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 保存公式
        self.base_formula = VGroup(base_formula, formula_box)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(base_circle),
            FadeOut(radius_line),
            FadeOut(radius_dot),
            FadeOut(r_label),
            FadeOut(circle_formula),
            run_time=0.6
        )
        
        # 公式移到顶部
        self.play(
            self.base_formula.animate.scale(0.5).move_to(UP * 6.5 + RIGHT * 2),
            run_time=0.5
        )
    
    def scene_7_total_area_formula(self):
        """场景7: 全面积公式"""
        # 标题
        title = Text(
            "全面积",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 两个公式回顾（放大）
        lateral_copy = self.lateral_formula.copy().scale(2).move_to(UP * 3)
        base_copy = self.base_formula.copy().scale(2).move_to(UP * 1.5)
        
        self.play(
            FadeIn(lateral_copy),
            FadeIn(base_copy),
            run_time=0.6
        )
        
        # 加号
        plus_sign = MathTex("+", font_size=48, color=WHITE).move_to(UP * 2.25)
        self.play(Write(plus_sign), run_time=0.3)
        
        # 全面积定义
        definition = Text(
            "全面积 = 侧面积 + 底面积",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 0.3)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 相加公式
        sum_formula = MathTex(
            r"S_{\text{total}} = \pi r l + \pi r^2",
            font_size=36
        ).move_to(DOWN * 0.8)
        
        sum_formula[0][-4:-2].set_color(self.COLOR_SLANT)  # rl
        sum_formula[0][-1].set_color(self.COLOR_BASE)  # r²
        
        self.play(Write(sum_formula), run_time=1.0)
        self.wait(0.8)
        
        # 提取公因式
        hint = Text(
            "提取公因式 πr:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 最终公式
        final_formula = MathTex(
            r"S_{\text{total}} = \pi r (l + r)",
            font_size=46
        ).move_to(DOWN * 3.5)
        
        final_formula[0][0].set_color(self.COLOR_FORMULA)  # S
        final_formula[0][-4].set_color(self.COLOR_SLANT)  # l
        final_formula[0][-1].set_color(self.COLOR_BASE)  # r (最后一个)
        
        formula_box = SurroundingRectangle(
            final_formula,
            color=self.COLOR_FORMULA,
            buff=0.25,
            corner_radius=0.1
        )
        
        arrow = Arrow(DOWN * 1.5, DOWN * 3.2, color=self.COLOR_FORMULA, buff=0.1)
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(
            Write(final_formula),
            Create(formula_box),
            run_time=1.0
        )
        self.play(Indicate(final_formula, scale_factor=1.12), run_time=0.8)
        self.wait(1.5)
        
        # 保存公式
        self.total_formula = VGroup(final_formula, formula_box)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(lateral_copy),
            FadeOut(base_copy),
            FadeOut(plus_sign),
            FadeOut(definition),
            FadeOut(sum_formula),
            FadeOut(hint),
            FadeOut(arrow),
            run_time=0.6
        )
        
        # 三个公式并排
        formulas_group = VGroup(
            self.lateral_formula.copy(),
            self.base_formula.copy(),
            self.total_formula.copy().scale(0.5)
        ).arrange(RIGHT, buff=0.3).scale(0.8).move_to(UP * 6.8)
        
        self.play(
            Transform(self.lateral_formula, formulas_group[0]),
            Transform(self.base_formula, formulas_group[1]),
            Transform(self.total_formula, formulas_group[2]),
            run_time=0.6
        )
    
    def scene_8_comprehensive_example(self):
        """场景8: 综合示例"""
        # 标题
        title = Text(
            "综合练习",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 题目
        problem_text = Text(
            "已知：r = 3, h = 4",
            font="PingFang SC",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4.3)
        
        question_text = Text(
            "求：l, S侧, S底, S全",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).next_to(problem_text, DOWN, buff=0.3)
        
        self.play(
            FadeIn(problem_text),
            FadeIn(question_text),
            run_time=0.8
        )
        
        # 圆锥图示
        cone_center = np.array([0, 1.8, 0])
        cone_diagram = self.create_cone_2d(cone_center, scale=0.8)
        
        # 标注
        base_r = Text("r=3", font="PingFang SC", font_size=20, color=self.COLOR_BASE).next_to(
            cone_diagram[2], DOWN, buff=0.1
        )
        height_line = DashedLine(
            cone_diagram[0].get_start(),
            cone_diagram[2].get_center(),
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        height_label = Text("h=4", font="PingFang SC", font_size=20, color=self.COLOR_AUXILIARY).next_to(
            height_line, LEFT, buff=0.1
        )
        
        self.play(
            Create(cone_diagram),
            run_time=1.0
        )
        self.play(
            Write(base_r),
            Create(height_line),
            Write(height_label),
            run_time=0.8
        )
        
        # 计算区域
        calc_y_start = -0.5
        
        # 1. 计算母线
        step_1_title = Text(
            "① 母线：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(LEFT * 3 + UP * calc_y_start)
        
        step_1_calc = MathTex(
            r"l = \sqrt{r^2 + h^2} = \sqrt{9 + 16} = 5",
            font_size=28
        ).next_to(step_1_title, RIGHT, buff=0.3)
        
        step_1_calc[0][-1].set_color(self.COLOR_SLANT)
        
        self.play(Write(step_1_title), run_time=0.4)
        self.play(Write(step_1_calc), run_time=1.0)
        
        # 2. 侧面积
        step_2_title = Text(
            "② 侧面积：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(LEFT * 2.8 + UP * (calc_y_start - 1.2))
        
        step_2_calc = MathTex(
            r"S_1 = \pi r l = \pi \times 3 \times 5 = 15\pi",
            font_size=28
        ).next_to(step_2_title, RIGHT, buff=0.2)
        
        step_2_calc[0][-2:].set_color(self.COLOR_CONE)
        
        self.play(Write(step_2_title), run_time=0.4)
        self.play(Write(step_2_calc), run_time=0.8)
        
        # 数值
        step_2_num = MathTex(
            r"\approx 47.1",
            font_size=24,
            color=GRAY_A
        ).next_to(step_2_calc, RIGHT, buff=0.3)
        
        self.play(Write(step_2_num), run_time=0.4)
        
        # 3. 底面积
        step_3_title = Text(
            "③ 底面积：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(LEFT * 2.8 + UP * (calc_y_start - 2.4))
        
        step_3_calc = MathTex(
            r"S_2 = \pi r^2 = \pi \times 9 = 9\pi",
            font_size=28
        ).next_to(step_3_title, RIGHT, buff=0.2)
        
        step_3_calc[0][-2:].set_color(self.COLOR_BASE)
        
        self.play(Write(step_3_title), run_time=0.4)
        self.play(Write(step_3_calc), run_time=0.8)
        
        step_3_num = MathTex(
            r"\approx 28.3",
            font_size=24,
            color=GRAY_A
        ).next_to(step_3_calc, RIGHT, buff=0.3)
        
        self.play(Write(step_3_num), run_time=0.4)
        
        # 4. 全面积
        step_4_title = Text(
            "④ 全面积：",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(LEFT * 2.8 + UP * (calc_y_start - 3.6))
        
        step_4_calc = MathTex(
            r"S = \pi r(l+r) = \pi \times 3 \times 8 = 24\pi",
            font_size=28
        ).next_to(step_4_title, RIGHT, buff=0.2)
        
        step_4_calc[0][-2:].set_color(self.COLOR_FORMULA)
        
        self.play(Write(step_4_title), run_time=0.4)
        self.play(Write(step_4_calc), run_time=0.8)
        
        step_4_num = MathTex(
            r"\approx 75.4",
            font_size=24,
            color=GRAY_A
        ).next_to(step_4_calc, RIGHT, buff=0.3)
        
        self.play(Write(step_4_num), run_time=0.4)
        
        # 验证
        verify_text = Text(
            "验证：15π + 9π = 24π ✓",
            font="PingFang SC",
            font_size=24,
            color=GREEN,
            weight=BOLD
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(verify_text, scale=1.1),
            Indicate(verify_text, scale_factor=1.15),
            run_time=0.8
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            *[FadeOut(mob) for mob in [
                title, problem_text, question_text,
                cone_diagram, base_r, height_line, height_label,
                step_1_title, step_1_calc,
                step_2_title, step_2_calc, step_2_num,
                step_3_title, step_3_calc, step_3_num,
                step_4_title, step_4_calc, step_4_num,
                verify_text
            ]],
            run_time=0.6
        )
    
    def scene_9_outro(self):
        """场景9: 结尾关注"""
        # 总结标题
        summary_title = Text(
            "公式总结",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        
        # 三个公式
        formulas = VGroup(
            VGroup(
                Text("侧面积:", font="PingFang SC", font_size=28, color=GRAY_A),
                MathTex(r"S = \pi r l", font_size=36, color=self.COLOR_CONE)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("底面积:", font="PingFang SC", font_size=28, color=GRAY_A),
                MathTex(r"S = \pi r^2", font_size=36, color=self.COLOR_BASE)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("全面积:", font="PingFang SC", font_size=28, color=GRAY_A),
                MathTex(r"S = \pi r(l+r)", font_size=36, color=self.COLOR_FORMULA)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 2)
        
        for formula in formulas:
            self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.5)
            self.wait(0.1)
        
        # 闪烁
        self.play(
            *[Flash(f[1], color=self.COLOR_HIGHLIGHT, flash_radius=0.5) for f in formulas],
            run_time=0.6
        )
        
        # 记忆技巧
        tips = Text(
            "记住：展开是扇形，底面是圆",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(tips), run_time=0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            self.author_info.animate.become(author_large),
            FadeIn(author_id, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 4.8)
        
        self.play(
            Write(follow_text),
            follow_text.animate.scale(1.1),
            run_time=0.8
        )
        
        # 圆锥装饰
        cones = VGroup(*[
            self.create_cone_2d(
                follow_text.get_center() + 2.8 * np.array([np.cos(i * TAU / 5), np.sin(i * TAU / 5), 0]),
                scale=0.15
            )
            for i in range(5)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in cones],
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in [
                summary_title, formulas, tips,
                self.author_info, author_id,
                follow_text, cones,
                self.lateral_formula, self.base_formula, self.total_formula
            ]],
            run_time=1.0
        )


# 运行命令:
# manim -pql cone_surface_area.py ConeSurfaceArea  # 快速预览
# manim -qh cone_surface_area.py ConeSurfaceArea   # 高质量 1080p
# manim -qk cone_surface_area.py ConeSurfaceArea   # 4K质量