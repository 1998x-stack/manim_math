"""
椭圆蒙日圆动画 - Monge Circle of Ellipse
展示椭圆垂直切线交点轨迹的蒙日圆定理

内容: 蒙日圆的定义、证明和应用
目标观众: 高中学生
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


class MongeCircle(Scene):
    """
    椭圆蒙日圆教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 问题演示（动态切线）
    3. 核心结论展示
    4. 代数法证明
    5. 判别式法证明
    6. 几何意义
    7. 总结片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ELLIPSE = "#3498db"       # 蓝色 - 椭圆
        self.COLOR_MONGE = "#e74c3c"         # 红色 - 蒙日圆
        self.COLOR_TANGENT1 = "#2ecc71"      # 绿色 - 切线1
        self.COLOR_TANGENT2 = "#f39c12"      # 橙色 - 切线2
        self.COLOR_INTERSECTION = "#9b59b6"  # 紫色 - 交点T
        self.COLOR_FORMULA = YELLOW          # 黄色 - 公式
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_dynamic_demonstration()
        self.show_core_conclusion()
        self.show_algebraic_proof_part1()
        self.show_algebraic_proof_part2()
        self.show_discriminant_method()
        self.show_geometric_meaning()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化椭圆和蒙日圆的几何数据"""
        # ========== 椭圆参数 ==========
        self.a = 3.0  # 长半轴
        self.b = 2.0  # 短半轴
        
        # ========== 缩放和偏移 ==========
        self.ELLIPSE_SCALE = 0.8
        self.ELLIPSE_OFFSET = UP * 1.5
        
        # ========== 蒙日圆参数 ==========
        self.R = np.sqrt(self.a**2 + self.b**2)  # √13 ≈ 3.606
        
        # ========== 验证几何 ==========
        print(f"椭圆: a={self.a}, b={self.b}")
        print(f"蒙日圆: R=√(a²+b²)={self.R:.6f}")
        print(f"关系: R={self.R:.3f} > a={self.a} (蒙日圆在椭圆外)")
        print("✓ 几何初始化完成")
    
    def calculate_tangent_slopes(self, x0, y0):
        """
        计算从点(x0, y0)到椭圆的两条切线斜率
        返回: [k1, k2] 或 None
        """
        A = x0**2 - self.a**2
        B = -2 * x0 * y0
        C = y0**2 - self.b**2
        
        if abs(A) < 1e-10:
            if abs(B) > 1e-10:
                return [-C/B, None]
            return None
        
        discriminant = B**2 - 4*A*C
        
        if discriminant < 0:
            return None
        
        k1 = (-B + np.sqrt(discriminant)) / (2*A)
        k2 = (-B - np.sqrt(discriminant)) / (2*A)
        
        return [k1, k2]
    
    def point_on_monge(self, angle):
        """蒙日圆上的点（参数方程）"""
        x = self.R * np.cos(angle)
        y = self.R * np.sin(angle)
        return np.array([x, y, 0]) * self.ELLIPSE_SCALE + self.ELLIPSE_OFFSET
    
    def create_tangent_line(self, point, slope, length=4.0):
        """创建过point且斜率为slope的直线"""
        direction = np.array([1, slope, 0])
        direction = direction / np.linalg.norm(direction)
        
        start = point - direction * length / 2
        end = point + direction * length / 2
        
        return Line(start, end)
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子主标题
        hook_main = Text(
            "椭圆的蒙日圆",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        hook_sub = Text(
            "两条垂直切线的交点在哪里?",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_main), run_time=1.0)
        self.play(FadeIn(hook_sub), run_time=0.5)
        
        # 椭圆
        ellipse = Ellipse(
            width=2 * self.a * self.ELLIPSE_SCALE,
            height=2 * self.b * self.ELLIPSE_SCALE,
            color=self.COLOR_ELLIPSE,
            stroke_width=3
        ).move_to(self.ELLIPSE_OFFSET)
        
        self.play(Create(ellipse), run_time=1.0)
        
        # 蒙日圆
        monge_circle = Circle(
            radius=self.R * self.ELLIPSE_SCALE,
            color=self.COLOR_MONGE,
            stroke_width=3
        ).move_to(self.ELLIPSE_OFFSET)
        
        self.play(Create(monge_circle), run_time=1.0)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_main),
            FadeOut(hook_sub),
            run_time=0.5
        )
        
        # 保存对象
        self.ellipse = ellipse
        self.monge_circle = monge_circle
    
    def show_dynamic_demonstration(self):
        """场景2: 动态演示 (5-15秒)"""
        # 说明文字
        demo_text = Text(
            "从圆上的点作椭圆的两条垂直切线",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(demo_text), run_time=0.6)
        
        # 创建ValueTracker
        t_tracker = ValueTracker(np.pi / 6)
        
        # 动态点T
        dot_T = always_redraw(
            lambda: Dot(
                self.point_on_monge(t_tracker.get_value()),
                color=self.COLOR_INTERSECTION,
                radius=0.12
            )
        )
        
        label_T = always_redraw(
            lambda: MathTex("T", font_size=24, color=self.COLOR_INTERSECTION).next_to(
                dot_T, UR, buff=0.15
            )
        )
        
        self.play(
            FadeIn(dot_T, scale=0.5),
            Flash(dot_T, color=self.COLOR_INTERSECTION),
            Write(label_T),
            run_time=0.6
        )
        
        # 动态切线
        def get_tangent_line_1():
            angle = t_tracker.get_value()
            point = self.point_on_monge(angle)
            
            # 转换回原始坐标计算斜率
            point_orig = (point - self.ELLIPSE_OFFSET) / self.ELLIPSE_SCALE
            slopes = self.calculate_tangent_slopes(point_orig[0], point_orig[1])
            
            if slopes and slopes[0] is not None:
                return Line(
                    point + LEFT * 1.5 + DOWN * 1.5 * slopes[0],
                    point + RIGHT * 1.5 + UP * 1.5 * slopes[0],
                    color=self.COLOR_TANGENT1,
                    stroke_width=3
                )
            return VGroup()
        
        def get_tangent_line_2():
            angle = t_tracker.get_value()
            point = self.point_on_monge(angle)
            
            point_orig = (point - self.ELLIPSE_OFFSET) / self.ELLIPSE_SCALE
            slopes = self.calculate_tangent_slopes(point_orig[0], point_orig[1])
            
            if slopes and slopes[1] is not None:
                return Line(
                    point + LEFT * 1.5 + DOWN * 1.5 * slopes[1],
                    point + RIGHT * 1.5 + UP * 1.5 * slopes[1],
                    color=self.COLOR_TANGENT2,
                    stroke_width=3
                )
            return VGroup()
        
        tangent1 = always_redraw(get_tangent_line_1)
        tangent2 = always_redraw(get_tangent_line_2)
        
        self.play(
            Create(tangent1),
            run_time=0.8
        )
        
        self.play(
            Create(tangent2),
            run_time=0.8
        )
        
        # 直角标记
        right_angle_mark = always_redraw(
            lambda: self.create_right_angle_symbol(
                self.point_on_monge(t_tracker.get_value()),
                size=0.25
            )
        )
        
        self.play(FadeIn(right_angle_mark), run_time=0.5)
        self.play(Indicate(right_angle_mark, scale_factor=1.3), run_time=0.6)
        
        # T点移动动画
        self.play(
            t_tracker.animate.set_value(t_tracker.get_value() + 2 * PI),
            run_time=4.0,
            rate_func=linear
        )
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(demo_text),
            FadeOut(dot_T),
            FadeOut(label_T),
            FadeOut(tangent1),
            FadeOut(tangent2),
            FadeOut(right_angle_mark),
            run_time=0.6
        )
    
    def create_right_angle_symbol(self, point, size=0.25):
        """创建直角符号"""
        return VGroup(
            Line(point + LEFT * size, point),
            Line(point, point + DOWN * size),
            Line(point + LEFT * size, point + LEFT * size + DOWN * size),
            Line(point + LEFT * size + DOWN * size, point + DOWN * size)
        ).set_color(YELLOW).set_stroke(width=2)
    
    def show_core_conclusion(self):
        """场景3: 核心结论 (15-25秒)"""
        # 标题
        title = Text(
            "蒙日圆定理",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 核心公式
        formula = MathTex(
            r"x^2 + y^2 = a^2 + b^2",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5.5)
        
        formula_box = SurroundingRectangle(
            formula,
            color=YELLOW,
            buff=0.3,
            stroke_width=3
        )
        
        self.play(Write(formula), run_time=1.2)
        self.play(Create(formula_box), run_time=0.5)
        
        # 圆心标注
        center_dot = Dot(self.ELLIPSE_OFFSET, color=WHITE, radius=0.08)
        center_label = MathTex("O", font_size=24, color=WHITE).next_to(center_dot, DL, buff=0.1)
        
        self.play(
            FadeIn(center_dot),
            Write(center_label),
            run_time=0.4
        )
        
        # 半径标注
        radius_line = Line(
            self.ELLIPSE_OFFSET,
            self.ELLIPSE_OFFSET + RIGHT * self.R * self.ELLIPSE_SCALE,
            color=self.COLOR_MONGE,
            stroke_width=3
        )
        
        radius_label = MathTex(
            r"R = \sqrt{a^2 + b^2}",
            font_size=26,
            color=self.COLOR_MONGE
        ).next_to(radius_line, DOWN, buff=0.2)
        
        self.play(
            Create(radius_line),
            Write(radius_label),
            run_time=1.0
        )
        
        # 说明
        explanation = VGroup(
            Text("圆心: 椭圆中心O", font="PingFang SC", font_size=24, color=GRAY_A),
            Text("两条垂直切线交点的轨迹", font="PingFang SC", font_size=24, color=GRAY_A)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(center_dot),
            FadeOut(center_label),
            run_time=0.6
        )
        
        # 公式框移到左上角
        self.play(
            VGroup(formula, formula_box).animate.scale(0.6).to_corner(UL, buff=0.3),
            FadeOut(title),
            run_time=0.8
        )
        
        self.formula_group = VGroup(formula, formula_box)
    
    def show_algebraic_proof_part1(self):
        """场景4: 代数法证明Part1 (25-40秒)"""
        # 方法标题
        method_title = Text(
            "证明方法一: 代数法",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(method_title), run_time=0.6)
        
        # 步骤1
        step1 = Text(
            "步骤1: 椭圆切线方程",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5)
        
        self.play(FadeIn(step1), run_time=0.4)
        
        # 切线方程
        tangent_eq = MathTex(
            r"\text{Tangent: } \frac{x_0 x}{a^2} + \frac{y_0 y}{b^2} = 1",
            font_size=28
        ).move_to(UP * 4)
        
        self.play(Write(tangent_eq), run_time=1.2)
        
        # 斜率公式
        slope_formula = MathTex(
            r"k = -\frac{b^2 x_0}{a^2 y_0}",
            font_size=28
        ).move_to(UP * 2.8)
        
        self.play(Write(slope_formula), run_time=1.0)
        
        # 步骤2
        step2 = Text(
            "步骤2: 垂直条件",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(step2), run_time=0.4)
        
        # 垂直条件
        perpendicular = MathTex(
            r"k_1 \cdot k_2 = -1",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 0.5)
        
        self.play(Write(perpendicular), run_time=1.2)
        
        # 代入
        substitute = MathTex(
            r"\frac{b^4 x_1 x_2}{a^4 y_1 y_2} = -1",
            font_size=28
        ).move_to(DOWN * 1)
        
        self.play(Write(substitute), run_time=1.2)
        
        self.wait(5.0)
        
        # 清理
        self.play(
            FadeOut(method_title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(tangent_eq),
            FadeOut(slope_formula),
            FadeOut(perpendicular),
            FadeOut(substitute),
            run_time=0.6
        )
    
    def show_algebraic_proof_part2(self):
        """场景5: 代数法证明Part2 (40-55秒)"""
        # 继续推导
        continue_text = Text(
            "继续推导...",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(continue_text), run_time=0.5)
        
        # 整理
        step_text = Text(
            "(省略复杂代数步骤)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_B
        ).move_to(UP * 4)
        
        self.play(FadeIn(step_text), run_time=0.8)
        
        # 最终结果
        final_result = MathTex(
            r"x_0^2 + y_0^2 = a^2 + b^2",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 2)
        
        result_box = SurroundingRectangle(
            final_result,
            color=YELLOW,
            buff=0.3,
            stroke_width=3
        )
        
        self.play(Write(final_result), run_time=1.5)
        self.play(Create(result_box), run_time=0.5)
        self.play(Circumscribe(VGroup(final_result, result_box), color=YELLOW), run_time=1.0)
        
        # 说明
        conclusion_text = Text(
            "因此交点T(x₀,y₀)在圆上!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(conclusion_text, shift=UP * 0.3), run_time=0.8)
        
        self.wait(4.0)
        
        # 清理
        self.play(
            FadeOut(continue_text),
            FadeOut(step_text),
            FadeOut(final_result),
            FadeOut(result_box),
            FadeOut(conclusion_text),
            run_time=0.6
        )
    
    def show_discriminant_method(self):
        """场景6: 判别式法 (55-70秒)"""
        # 方法2标题
        method2_title = Text(
            "证明方法二: 判别式法 (更简洁)",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(method2_title), run_time=0.6)
        
        # 直线方程
        line_eq = MathTex(
            r"y = kx + m, \quad m = y_0 - kx_0",
            font_size=26
        ).move_to(UP * 5)
        
        self.play(Write(line_eq), run_time=1.0)
        
        # 相切条件
        tangent_cond = MathTex(
            r"\Delta = 0 \Rightarrow m^2 = a^2 k^2 + b^2",
            font_size=26
        ).move_to(UP * 3.8)
        
        self.play(Write(tangent_cond), run_time=1.2)
        
        # 二次方程
        quadratic = MathTex(
            r"(x_0^2 - a^2)k^2 - 2x_0 y_0 k + (y_0^2 - b^2) = 0",
            font_size=24
        ).move_to(UP * 2.3)
        
        self.play(Write(quadratic), run_time=1.2)
        
        # 韦达定理
        vieta = MathTex(
            r"k_1 k_2 = \frac{y_0^2 - b^2}{x_0^2 - a^2} = -1",
            font_size=26
        ).move_to(UP * 0.8)
        
        self.play(Write(vieta), run_time=1.0)
        
        # 结论
        conclusion = MathTex(
            r"x_0^2 + y_0^2 = a^2 + b^2",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1.5)
        
        conclusion_box = SurroundingRectangle(
            conclusion,
            color=YELLOW,
            buff=0.3,
            stroke_width=3
        )
        
        self.play(Write(conclusion), run_time=1.0)
        self.play(Create(conclusion_box), run_time=0.5)
        
        self.wait(4.0)
        
        # 清理
        self.play(
            FadeOut(method2_title),
            FadeOut(line_eq),
            FadeOut(tangent_cond),
            FadeOut(quadratic),
            FadeOut(vieta),
            FadeOut(conclusion),
            FadeOut(conclusion_box),
            run_time=0.6
        )
    
    def show_geometric_meaning(self):
        """场景7: 几何意义 (70-85秒)"""
        # 标题
        geo_title = Text(
            "几何意义与应用",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6)
        
        self.play(Write(geo_title), run_time=0.6)
        
        # 位置关系
        position_text = VGroup(
            Text("蒙日圆完全在椭圆外部", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"R = \sqrt{a^2 + b^2} > a", font_size=26)
        ).arrange(DOWN, buff=0.3).move_to(UP * 4.5)
        
        self.play(FadeIn(position_text), run_time=0.8)
        
        # 标注半径关系
        a_line = Line(
            self.ELLIPSE_OFFSET,
            self.ELLIPSE_OFFSET + RIGHT * self.a * self.ELLIPSE_SCALE,
            color=self.COLOR_ELLIPSE,
            stroke_width=3
        )
        
        a_label = MathTex("a", font_size=24, color=self.COLOR_ELLIPSE).next_to(a_line, DOWN, buff=0.1)
        
        R_line = Line(
            self.ELLIPSE_OFFSET,
            self.ELLIPSE_OFFSET + RIGHT * self.R * self.ELLIPSE_SCALE,
            color=self.COLOR_MONGE,
            stroke_width=3
        )
        
        R_label = MathTex("R", font_size=24, color=self.COLOR_MONGE).next_to(R_line, UP, buff=0.1)
        
        self.play(
            Create(a_line),
            Write(a_label),
            run_time=0.5
        )
        
        self.play(
            Create(R_line),
            Write(R_label),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 应用示例
        example_text = Text(
            "应用: 判断点能否作垂直切线",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(example_text), run_time=0.8)
        
        # 示例
        example = VGroup(
            Text("例: P(2,3) 能作垂直切线吗?", font="PingFang SC", font_size=22),
            MathTex(r"2^2 + 3^2 = 13 = a^2 + b^2", font_size=22),
            Text("✓ 能! P在蒙日圆上", font="PingFang SC", font_size=22, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 5.5)
        
        for item in example:
            self.play(FadeIn(item, shift=UP * 0.2), run_time=0.5)
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(geo_title),
            FadeOut(position_text),
            FadeOut(a_line),
            FadeOut(a_label),
            FadeOut(R_line),
            FadeOut(R_label),
            FadeOut(example_text),
            FadeOut(example),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 总结 (85-120秒)"""
        # 总结标题
        summary_title = Text(
            "核心总结",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(
            Transform(self.formula_group, summary_title),
            run_time=0.6
        )
        
        # 大号公式
        big_formula = MathTex(
            r"x^2 + y^2 = a^2 + b^2",
            font_size=48,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        big_box = SurroundingRectangle(
            big_formula,
            color=YELLOW,
            buff=0.4,
            stroke_width=4
        )
        
        self.play(
            Write(big_formula),
            Create(big_box),
            run_time=1.2
        )
        
        # 关键点
        key_points = VGroup(
            Text("✓ 两条垂直切线交点轨迹", font="PingFang SC", font_size=24, color=GRAY_A),
            Text("✓ 圆心在椭圆中心", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"\text{✓ 半径 } R = \sqrt{a^2 + b^2}", font_size=24, color=GRAY_A)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(UP * 1.5)
        
        for point in key_points:
            self.play(FadeIn(point, shift=RIGHT * 0.5), run_time=0.6)
        
        # 装饰动画
        self.play(
            Rotate(self.ellipse, angle=PI / 2),
            Rotate(self.monge_circle, angle=-PI / 2),
            run_time=2.0
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(DOWN * 4)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握圆锥曲线技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰圆环
        decorations = VGroup(*[
            Circle(radius=0.3, color=self.COLOR_MONGE, fill_opacity=0.3)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(FadeIn(decorations), run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=2.0))
        
        self.wait(20.0)


# 运行命令:
# manim -pql monge_circle.py MongeCircle  # 快速预览
# manim -qh monge_circle.py MongeCircle   # 高质量渲染