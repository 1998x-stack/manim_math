"""
曲线与方程 - Curve and Equation Animation
高二数学 - 解析几何基础概念

内容: 曲线与方程的关系、充要条件
目标观众: 高中生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CurveAndEquation(Scene):
    """
    曲线与方程教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. 引入方程概念
    4. 充要条件 - 正向（点在曲线上→满足方程）
    5. 充要条件 - 反向（满足方程→点在曲线上）
    6. 反例演示
    7. 总结定义
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 曲线
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 点
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        self.COLOR_FORMULA = "#2ecc71"      # 绿色 - 公式/正确
        self.COLOR_GRID = "#34495e"         # 深灰 - 网格
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_coordinate_system()
        self.show_equation_concept()
        self.show_sufficiency_forward()
        self.show_sufficiency_backward()
        self.show_counterexample()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化几何数据"""
        # 圆的参数
        self.circle_center = ORIGIN
        self.circle_radius = 2.0
        
        # 关键点坐标（精确计算）
        self.point_on_circle = np.array([np.sqrt(2), np.sqrt(2), 0])  # (√2, √2)
        self.point_outside = np.array([3, 0, 0])  # (3, 0)
        self.point_on_circle_2 = np.array([0, 2, 0])  # (0, 2)
        
        # 坐标系配置
        self.axes_x_range = [-4, 4, 1]
        self.axes_y_range = [-3, 3, 1]
        
        print("✓ 几何数据初始化完成")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何用方程表示一个图形？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=0.8)
        
        # 一个圆逐渐形成（先不在坐标系中，纯几何展示）
        circle_demo = Circle(
            radius=1.5,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(UP * 2)
        
        self.play(Create(circle_demo), run_time=1.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(circle_demo),
            run_time=0.5
        )
    
    def show_coordinate_system(self):
        """场景2: 建立坐标系"""
        # 创建坐标轴
        self.axes = Axes(
            x_range=self.axes_x_range,
            y_range=self.axes_y_range,
            x_length=7,
            y_length=5,
            axis_config={
                "include_numbers": False,
                "color": self.COLOR_GRID,
                "stroke_width": 2
            }
        ).move_to(UP * 1.5)
        
        # 添加网格
        grid = NumberPlane(
            x_range=self.axes_x_range,
            y_range=self.axes_y_range,
            x_length=7,
            y_length=5,
            background_line_style={
                "stroke_color": self.COLOR_GRID,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).move_to(UP * 1.5)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis, UP, buff=0.2)
        
        self.play(Create(grid), run_time=0.8)
        self.play(
            Create(self.axes),
            Write(x_label),
            Write(y_label),
            run_time=1.2
        )
        
        # 在坐标系中创建圆
        self.circle = Circle(
            radius=self.circle_radius * (7 / 8),  # 缩放以适应坐标系
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.axes.c2p(0, 0))
        
        # 说明文字
        explanation = Text(
            "在坐标系中画一个圆",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(
            Create(self.circle),
            FadeIn(explanation, shift=UP * 0.3),
            run_time=1.2
        )
        self.wait(2.0)
        
        # 清理
        self.play(FadeOut(explanation), FadeOut(grid), FadeOut(x_label), FadeOut(y_label), run_time=0.4)
        
        # 保留坐标轴和圆
    
    def show_equation_concept(self):
        """场景3: 引入方程概念"""
        # 圆的方程
        self.equation = MathTex(
            r"x^2 + y^2 = 4",
            font_size=48,
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(self.equation, shift=UP * 0.3), run_time=1.0)
        
        # 连接圆与方程：同时高亮
        self.play(
            self.circle.animate.set_color(self.COLOR_HIGHLIGHT).set_stroke(width=6),
            self.equation.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        self.play(
            self.circle.animate.set_color(self.COLOR_PRIMARY).set_stroke(width=4),
            self.equation.animate.set_color(WHITE),
            run_time=0.6
        )
        
        # 标题
        title = Text(
            "曲线的方程",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.5)
        
        self.play(Write(title), run_time=1.0)
        self.wait(2.5)
        
        # 清理标题，方程移到顶部
        self.play(
            FadeOut(title),
            self.equation.animate.scale(0.7).move_to(UP * 6.5),
            run_time=0.6
        )
    
    def show_sufficiency_forward(self):
        """场景4: 充要条件 - 正向（点在曲线上→满足方程）"""
        # 标题
        condition_title = Text(
            "充要条件（一）",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5)
        
        subtitle = Text(
            "点在曲线上 → 坐标满足方程",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.3)
        
        self.play(Write(condition_title), FadeIn(subtitle), run_time=0.8)
        
        # 在圆上取点P
        p_coords = self.axes.c2p(self.point_on_circle[0], self.point_on_circle[1])
        point_P = Dot(p_coords, radius=0.12, color=self.COLOR_SECONDARY)
        p_label = MathTex(r"P", font_size=28, color=self.COLOR_SECONDARY).next_to(point_P, UR, buff=0.15)
        
        self.play(FadeIn(point_P, scale=0.5), run_time=0.5)
        self.play(Flash(point_P, color=self.COLOR_SECONDARY, flash_radius=0.3), run_time=0.4)
        self.play(Write(p_label), run_time=0.3)
        
        # 标注坐标
        coords_text = MathTex(
            r"P(\sqrt{2}, \sqrt{2})",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3)
        
        self.play(Write(coords_text), run_time=0.8)
        self.wait(1.0)
        
        # "代入方程"提示
        substitute_text = Text(
            "代入方程验证：",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(substitute_text), run_time=0.5)
        
        # 计算步骤1
        calc_step1 = MathTex(
            r"(\sqrt{2})^2 + (\sqrt{2})^2",
            font_size=36
        ).move_to(DOWN * 5)
        
        self.play(Write(calc_step1), run_time=1.0)
        self.wait(0.8)
        
        # 计算步骤2
        calc_step2 = MathTex(
            r"= 2 + 2 = 4",
            font_size=36
        ).next_to(calc_step1, RIGHT, buff=0.3)
        
        self.play(Write(calc_step2), run_time=1.2)
        
        # 结论："满足！"
        check_mark = Text(
            "✓ 满足方程！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(check_mark, scale=1.5), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(condition_title),
            FadeOut(subtitle),
            FadeOut(coords_text),
            FadeOut(substitute_text),
            FadeOut(calc_step1),
            FadeOut(calc_step2),
            FadeOut(check_mark),
            FadeOut(point_P),
            FadeOut(p_label),
            run_time=0.6
        )
    
    def show_sufficiency_backward(self):
        """场景5: 充要条件 - 反向（满足方程→点在曲线上）"""
        # 标题
        condition_title = Text(
            "充要条件（二）",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5)
        
        subtitle = Text(
            "坐标满足方程 → 点在曲线上",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.3)
        
        self.play(Write(condition_title), FadeIn(subtitle), run_time=0.8)
        
        # 给出坐标
        given_coords = MathTex(
            r"\text{Given: } (\sqrt{2}, \sqrt{2})",
            font_size=30
        ).move_to(DOWN * 2.5)
        
        self.play(Write(given_coords), run_time=0.8)
        self.wait(0.5)
        
        # 验证满足方程
        verify_equation = MathTex(
            r"(\sqrt{2})^2 + (\sqrt{2})^2 = 4 \quad \checkmark",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.5)
        
        self.play(Write(verify_equation), run_time=1.2)
        self.wait(0.8)
        
        # 在坐标系中定位该点（先在旁边出现）
        new_point_start = Dot(
            self.axes.c2p(self.point_on_circle[0] + 1.5, self.point_on_circle[1] + 0.5),
            radius=0.12,
            color=self.COLOR_SECONDARY
        )
        
        question_text = Text(
            "这个点在曲线上吗？",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(new_point_start, scale=0.5),
            FadeIn(question_text),
            run_time=0.8
        )
        
        # 点移动到圆上正确位置
        target_position = self.axes.c2p(self.point_on_circle[0], self.point_on_circle[1])
        
        self.play(
            new_point_start.animate.move_to(target_position),
            run_time=1.2,
            rate_func=smooth
        )
        
        # 高亮重合
        self.play(
            Flash(new_point_start, color=self.COLOR_FORMULA, flash_radius=0.4),
            run_time=0.5
        )
        
        # 结论
        conclusion = Text(
            "✓ 点在曲线上！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 6.5)
        
        self.play(
            Transform(question_text, conclusion),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(condition_title),
            FadeOut(subtitle),
            FadeOut(given_coords),
            FadeOut(verify_equation),
            FadeOut(new_point_start),
            FadeOut(question_text),
            run_time=0.6
        )
    
    def show_counterexample(self):
        """场景6: 反例演示"""
        # 标题
        counterexample_title = Text(
            "反例：不在曲线上的点",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5)
        
        self.play(Write(counterexample_title), run_time=0.8)
        
        # 圆外点Q
        q_coords = self.axes.c2p(self.point_outside[0], self.point_outside[1])
        point_Q = Dot(q_coords, radius=0.12, color=self.COLOR_SECONDARY)
        q_label = MathTex(r"Q(3, 0)", font_size=28, color=self.COLOR_SECONDARY).next_to(point_Q, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(point_Q, scale=0.5),
            Write(q_label),
            run_time=0.8
        )
        
        # 代入验证
        verify_Q = MathTex(
            r"3^2 + 0^2 = 9",
            font_size=36
        ).move_to(DOWN * 3.5)
        
        self.play(Write(verify_Q), run_time=1.0)
        self.wait(0.5)
        
        # 不等式
        inequality = MathTex(
            r"9 \neq 4",
            font_size=40,
            color=RED
        ).move_to(DOWN * 4.8)
        
        self.play(Write(inequality), run_time=0.8)
        
        # 红叉
        cross_mark = Text(
            "✗ 不满足方程！",
            font="PingFang SC",
            font_size=32,
            color=RED
        ).move_to(DOWN * 6.2)
        
        self.play(FadeIn(cross_mark, scale=1.5), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(counterexample_title),
            FadeOut(point_Q),
            FadeOut(q_label),
            FadeOut(verify_Q),
            FadeOut(inequality),
            FadeOut(cross_mark),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结定义"""
        # 定义框背景
        definition_box = Rectangle(
            width=7.5,
            height=4,
            fill_color="#2c3e50",
            fill_opacity=0.9,
            stroke_color=self.COLOR_FORMULA,
            stroke_width=3
        ).move_to(DOWN * 0.5)
        
        # 定义标题
        def_title = Text(
            "曲线的方程",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)
        
        # 定义内容（分行）
        def_line1 = Text(
            "曲线C上的点的坐标",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 0.8)
        
        def_line2 = Text(
            "都是方程 F(x,y)=0 的解",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 0.2)
        
        # 双向箭头
        double_arrow = MathTex(
            r"\Updownarrow",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        def_line3 = Text(
            "以方程 F(x,y)=0 的解",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1.2)
        
        def_line4 = Text(
            "为坐标的点都在曲线C上",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 1.8)
        
        # 关键词
        key_word = Text(
            "充要条件",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2.8)
        
        # 动画：依次显示
        self.play(FadeIn(definition_box), run_time=0.6)
        self.play(Write(def_title), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeIn(def_line1, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(def_line2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        self.play(Create(double_arrow), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeIn(def_line3, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(def_line4, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)
        
        self.play(FadeIn(key_word, scale=1.2), run_time=0.6)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(definition_box),
            FadeOut(def_title),
            FadeOut(def_line1),
            FadeOut(def_line2),
            FadeOut(double_arrow),
            FadeOut(def_line3),
            FadeOut(def_line4),
            FadeOut(key_word),
            FadeOut(self.axes),
            FadeOut(self.circle),
            FadeOut(self.equation),
            run_time=0.8
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多解析几何！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰：圆点阵
        dots = VGroup(*[
            Dot(
                np.array([np.cos(i * TAU / 8), np.sin(i * TAU / 8), 0]) * 2 + DOWN * 0.5,
                radius=0.1,
                color=self.COLOR_PRIMARY
            )
            for i in range(8)
        ])
        
        self.play(*[FadeIn(dot, scale=0.5) for dot in dots], run_time=0.6)
        self.play(Rotate(dots, angle=PI, run_time=1.5))
        
        # 公式图标
        formula_icon = MathTex(
            r"x^2 + y^2 = r^2",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(formula_icon, scale=0.8), run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(dots),
            FadeOut(formula_icon),
            run_time=1.0
        )


# ========== 运行命令 ==========
# manim -pql curve_and_equation.py CurveAndEquation  # 快速预览
# manim -qh curve_and_equation.py CurveAndEquation   # 高质量输出
# manim -qk curve_and_equation.py CurveAndEquation   # 4K质量