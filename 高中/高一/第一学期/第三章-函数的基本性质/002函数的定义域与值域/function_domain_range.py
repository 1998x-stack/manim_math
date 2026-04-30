"""
函数的定义域与值域 - Function Domain and Range Animation
使用 Manim 创建的高一数学教学视频

内容: 定义域与值域的概念、常见限制条件、求值域方法
目标观众: 高一学生
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


class FunctionDomainRange(Scene):
    """
    函数定义域与值域教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 定义域概念引入
    3. 定义域可视化
    4. 值域概念引入
    5. 常见限制条件总结
    6. 值域求法提示
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主函数
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 定义域
        self.COLOR_HIGHLIGHT = "#f39c12"      # 橙色 - 值域
        self.COLOR_AUXILIARY = "#95a5a6"      # 灰色 - 辅助线
        self.COLOR_DOMAIN_FILL = "#3498db"    # 定义域填充
        self.COLOR_RANGE_FILL = "#f39c12"     # 值域填充
        
        # 初始化几何/数学元素
        self.setup_elements()
        
        # 执行动画序列
        self.show_opening()
        self.show_domain_concept()
        self.show_domain_visualization()
        self.show_range_concept()
        self.show_common_constraints()
        self.show_range_methods()
        self.show_outro()
    
    def setup_elements(self):
        """初始化所有数学元素和坐标系"""
        # 坐标系配置
        self.AXES_SCALE = 0.8
        self.AXES_OFFSET = UP * 1.5
        
        # 创建坐标系（但不添加到场景）
        self.axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 4, 1],
            x_length=7 * self.AXES_SCALE,
            y_length=9 * self.AXES_SCALE,
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "include_tip": True,
            },
            tips=True
        ).move_to(self.AXES_OFFSET)
        
        # 添加坐标轴标签
        x_label = MathTex("x", font_size=28).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", font_size=28).next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
        self.axes_labels = VGroup(x_label, y_label)
        
        # 示例函数: f(x) = √(x+1)
        # 定义域: x ≥ -1
        # 值域: y ≥ 0
        
        # 关键点计算
        self.domain_start_x = -1
        self.domain_end_x = 3  # 显示范围
        self.range_start_y = 0
        self.range_end_y = 2  # √(3+1) = 2
        
        # 验证数学正确性
        self.verify_math()
    
    def verify_math(self):
        """验证数学计算的正确性"""
        # 验证 f(-1) = 0
        f_at_start = np.sqrt(self.domain_start_x + 1)
        assert abs(f_at_start - 0) < 1e-10, f"f(-1) 应该等于 0，但计算得到 {f_at_start}"
        
        # 验证 f(3) = 2
        f_at_end = np.sqrt(self.domain_end_x + 1)
        assert abs(f_at_end - 2) < 1e-10, f"f(3) 应该等于 2，但计算得到 {f_at_end}"
        
        print("✓ 数学验证通过")
    
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
        hook_text = Text(
            "这个函数能取所有x值吗？",
            font="PingFang SC",
            font_size=42,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=1.0)
        
        # 神秘函数图像（简化版坐标系）
        mini_axes = Axes(
            x_range=[-2, 3],
            y_range=[-1, 3],
            x_length=4,
            y_length=4,
            axis_config={"include_tip": False, "stroke_opacity": 0.3}
        ).move_to(UP * 2.5)
        
        mystery_graph = mini_axes.plot(
            lambda x: np.sqrt(x + 1),
            x_range=[-1, 3],
            color=self.COLOR_PRIMARY,
            stroke_opacity=0.5
        )
        
        question_mark = Text(
            "?",
            font="PingFang SC",
            font_size=80,
            color=YELLOW
        ).move_to(DOWN * 1)
        
        self.play(
            Create(mini_axes, run_time=0.8),
            Create(mystery_graph, run_time=1.2, rate_func=smooth)
        )
        
        self.play(Flash(question_mark, color=YELLOW, flash_radius=0.5), run_time=0.5)
        self.play(FadeIn(question_mark, scale=1.2), run_time=0.3)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(mini_axes),
            FadeOut(mystery_graph),
            FadeOut(question_mark),
            run_time=0.6
        )
    
    def show_domain_concept(self):
        """场景2: 定义域概念引入"""
        # 标题
        title = Text(
            "定义域 Domain",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5)
        
        definition = Text(
            "函数有意义的x的取值范围",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(title.animate.shift(RIGHT * 0), run_time=0.5)
        self.play(FadeIn(definition), run_time=0.6)
        
        # 绘制坐标系
        axes_group = VGroup(self.axes, self.axes_labels)
        self.play(Create(self.axes), Write(self.axes_labels), run_time=1.0)
        
        # x轴高亮
        self.play(self.axes.x_axis.animate.set_color(YELLOW), run_time=0.4)
        
        explain_x = Text(
            "x轴表示输入值",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_x), run_time=0.5)
        
        # 函数公式
        formula = MathTex(
            r"f(x) = \sqrt{x+1}",
            font_size=36,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(formula), run_time=0.8)
        
        # 限制条件
        constraint = Text(
            "被开方数 ≥ 0",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.8)
        
        self.play(Write(constraint), run_time=0.6)
        
        # 定义域高亮（x轴上的线段）
        domain_start_point = self.axes.c2p(self.domain_start_x, 0)
        domain_end_point = self.axes.c2p(self.domain_end_x, 0)
        
        domain_highlight = Line(
            domain_start_point,
            domain_end_point,
            color=self.COLOR_SECONDARY,
            stroke_width=8
        )
        
        # 起点标记
        start_dot = Dot(domain_start_point, color=self.COLOR_SECONDARY, radius=0.1)
        start_label = MathTex(r"x \geq -1", font_size=24, color=self.COLOR_SECONDARY).next_to(start_dot, DOWN, buff=0.3)
        
        self.play(Create(domain_highlight), run_time=0.8)
        self.play(
            FadeIn(start_dot, scale=0.5),
            Flash(start_dot, color=self.COLOR_SECONDARY),
            run_time=0.5
        )
        self.play(FadeIn(start_label), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理部分元素
        self.play(
            FadeOut(explain_x),
            FadeOut(constraint),
            self.axes.x_axis.animate.set_color(WHITE),
            run_time=0.5
        )
        
        # 保存元素供后续使用
        self.title_domain = title
        self.definition_domain = definition
        self.formula = formula
        self.domain_highlight = domain_highlight
        self.start_dot = start_dot
        self.start_label = start_label
    
    def show_domain_visualization(self):
        """场景3: 定义域可视化"""
        # 绘制函数图像
        func_graph = self.axes.plot(
            lambda x: np.sqrt(x + 1),
            x_range=[-1, 3],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(func_graph), run_time=1.5)
        
        # 端点闪烁
        self.play(Flash(self.start_dot, color=self.COLOR_SECONDARY, flash_radius=0.3), run_time=0.4)
        
        # x轴投影虚线（从函数图像到x轴）
        projection_x_values = [-1, 0, 1, 2, 3]
        projection_lines = VGroup(*[
            DashedLine(
                self.axes.c2p(x, 0),
                self.axes.c2p(x, np.sqrt(x + 1)),
                color=self.COLOR_AUXILIARY,
                dash_length=0.08,
                stroke_width=2
            )
            for x in projection_x_values
        ])
        
        self.play(Create(projection_lines), run_time=0.6)
        
        # 定义域括号
        domain_brace = Brace(
            Line(self.axes.c2p(-1, 0), self.axes.c2p(3, 0)),
            direction=DOWN,
            color=self.COLOR_SECONDARY,
            buff=0.3
        )
        
        # 避免 LaTeX 错误：使用 Text + MathTex 组合
        domain_text_safe = VGroup(
            Text("定义域: ", font="PingFang SC", font_size=24, color=self.COLOR_SECONDARY),
            MathTex(r"[-1, +\infty)", font_size=24, color=self.COLOR_SECONDARY)
        ).arrange(RIGHT, buff=0.1)
        domain_text_safe.next_to(domain_brace, DOWN, buff=0.2)
        
        self.play(Create(domain_brace), run_time=0.5)
        self.play(Write(domain_text_safe), run_time=0.6)
        
        # 重点提示
        highlight_text = Text(
            "x只能从-1开始取值",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(projection_lines),
            FadeOut(highlight_text),
            run_time=0.5
        )
        
        # 保存元素
        self.func_graph = func_graph
        self.domain_brace = domain_brace
        self.domain_text_safe = domain_text_safe
    
    def show_range_concept(self):
        """场景4: 值域概念引入"""
        # 标题切换
        title_range = Text(
            "值域 Range",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        definition_range = Text(
            "函数所有可能的y值的集合",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(
            Transform(self.title_domain, title_range),
            Transform(self.definition_domain, definition_range),
            run_time=0.6
        )
        
        # y轴高亮
        self.play(self.axes.y_axis.animate.set_color(YELLOW), run_time=0.4)
        self.play(self.axes.x_axis.animate.set_color(WHITE), run_time=0.3)
        
        explain_y = Text(
            "y轴表示输出值",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_y), run_time=0.5)
        
        # 值域高亮（y轴上的线段）
        range_start_point = self.axes.c2p(0, self.range_start_y)
        range_end_point = self.axes.c2p(0, 3.5)  # 延伸到y=3.5
        
        range_highlight = Line(
            range_start_point,
            range_end_point,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=8
        )
        
        self.play(Create(range_highlight), run_time=0.8)
        
        # y轴投影虚线（从函数图像到y轴）
        y_values = [0, 1, np.sqrt(2), np.sqrt(3), 2]
        y_projection_lines = VGroup(*[
            DashedLine(
                self.axes.c2p(y**2 - 1, y),  # x = y² - 1 (从 f(x)=√(x+1) 反解)
                self.axes.c2p(0, y),
                color=self.COLOR_AUXILIARY,
                dash_length=0.08,
                stroke_width=2
            )
            for y in y_values
        ])
        
        self.play(Create(y_projection_lines), run_time=0.6)
        
        # 值域括号
        range_brace = Brace(
            Line(self.axes.c2p(0, 0), self.axes.c2p(0, 2)),
            direction=RIGHT,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3
        )
        
        range_text_safe = VGroup(
            Text("值域: ", font="PingFang SC", font_size=24, color=self.COLOR_HIGHLIGHT),
            MathTex(r"[0, +\infty)", font_size=24, color=self.COLOR_HIGHLIGHT)
        ).arrange(RIGHT, buff=0.1)
        range_text_safe.next_to(range_brace, RIGHT, buff=0.2)
        
        self.play(Create(range_brace), run_time=0.5)
        self.play(Write(range_text_safe), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(explain_y),
            FadeOut(y_projection_lines),
            self.axes.y_axis.animate.set_color(WHITE),
            run_time=0.5
        )
        
        # 保存元素
        self.range_highlight = range_highlight
        self.range_brace = range_brace
        self.range_text_safe = range_text_safe
    
    def show_common_constraints(self):
        """场景5: 常见限制条件总结"""
        # 清屏
        self.play(
            FadeOut(self.func_graph),
            FadeOut(self.axes),
            FadeOut(self.axes_labels),
            FadeOut(self.domain_highlight),
            FadeOut(self.start_dot),
            FadeOut(self.start_label),
            FadeOut(self.domain_brace),
            FadeOut(self.domain_text_safe),
            FadeOut(self.range_highlight),
            FadeOut(self.range_brace),
            FadeOut(self.range_text_safe),
            FadeOut(self.formula),
            FadeOut(self.title_domain),
            FadeOut(self.definition_domain),
            run_time=0.5
        )
        
        # 总结标题
        summary_title = Text(
            "常见定义域限制",
            font="PingFang SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 创建5个约束条件卡片
        constraints = [
            ("① 分式", r"\text{分母} \neq 0"),
            ("② 偶次根", r"\text{被开方数} \geq 0"),
            ("③ 对数", r"\text{真数} > 0, \text{底数} > 0 \text{且} \neq 1"),
            ("④ 零次幂", r"\text{底数} \neq 0"),
            ("⑤ 实际问题", "考虑实际意义")
        ]
        
        y_positions = [3, 1.5, 0, -1.5, -3]
        cards = VGroup()
        
        for i, ((num_text, latex_text), y_pos) in enumerate(zip(constraints, y_positions)):
            # 创建卡片
            if i < 4:  # 前4个使用 LaTeX
                card_content = VGroup(
                    Text(num_text, font="PingFang SC", font_size=26, color=WHITE),
                    Text(": ", font="PingFang SC", font_size=26, color=WHITE),
                    # 分离中文和符号
                    self.create_constraint_formula(latex_text, i)
                ).arrange(RIGHT, buff=0.15)
            else:  # 最后一个纯中文
                card_content = Text(
                    f"{num_text}: {latex_text}",
                    font="PingFang SC",
                    font_size=26,
                    color=WHITE
                )
            
            card_content.move_to(UP * y_pos)
            card_content.shift(LEFT * 10)  # 初始位置在左侧外
            
            cards.add(card_content)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 全部卡片高亮
        self.play(cards.animate.set_color(YELLOW), run_time=0.4)
        self.play(cards.animate.set_color(WHITE), run_time=0.3)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.6
        )
    
    def create_constraint_formula(self, latex_text, index):
        """创建约束条件公式（避免 LaTeX 中文错误）"""
        if index == 0:  # 分式
            return VGroup(
                Text("分母", font="PingFang SC", font_size=26, color=WHITE),
                MathTex(r"\neq 0", font_size=26, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        elif index == 1:  # 偶次根
            return VGroup(
                Text("被开方数", font="PingFang SC", font_size=26, color=WHITE),
                MathTex(r"\geq 0", font_size=26, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        elif index == 2:  # 对数
            return VGroup(
                Text("真数", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"> 0", font_size=22, color=WHITE),
                Text(", 底数", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"> 0", font_size=22, color=WHITE),
                Text("且", font="PingFang SC", font_size=22, color=WHITE),
                MathTex(r"\neq 1", font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=0.08)
        elif index == 3:  # 零次幂
            return VGroup(
                Text("底数", font="PingFang SC", font_size=26, color=WHITE),
                MathTex(r"\neq 0", font_size=26, color=WHITE)
            ).arrange(RIGHT, buff=0.1)
        else:
            return Text("", font_size=26)
    
    def show_range_methods(self):
        """场景6: 值域求法提示"""
        # 方法标题
        methods_title = Text(
            "求值域常用方法",
            font="PingFang SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(methods_title), run_time=0.6)
        
        # 方法列表
        methods = VGroup(
            Text("① 观察法（简单函数）", font="PingFang SC", font_size=26, color=WHITE),
            Text("② 配方法（二次函数）", font="PingFang SC", font_size=26, color=self.COLOR_HIGHLIGHT),
            Text("③ 换元法", font="PingFang SC", font_size=26, color=WHITE),
            Text("④ 判别式法", font="PingFang SC", font_size=26, color=WHITE),
            Text("⑤ 单调性法", font="PingFang SC", font_size=26, color=self.COLOR_HIGHLIGHT),
            Text("⑥ 数形结合法", font="PingFang SC", font_size=26, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 1.5)
        
        self.play(FadeIn(methods, lag_ratio=0.2), run_time=2.0)
        
        # 重点高亮
        self.play(
            Indicate(methods[1], color=self.COLOR_HIGHLIGHT),
            Indicate(methods[4], color=self.COLOR_HIGHLIGHT),
            run_time=0.8
        )
        
        # 提示文字
        tip_text = Text(
            "掌握方法，灵活运用！",
            font="PingFang SC",
            font_size=32,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(tip_text, scale=1.2), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(methods_title),
            FadeOut(methods),
            FadeOut(tip_text),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景7: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.6
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多函数知识！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, scale=1.2), run_time=0.6)
        
        # 图标装饰
        icon_size = 0.25
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_PRIMARY, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_SECONDARY, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_HIGHLIGHT, fill_opacity=0.8)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        
        # 图标闪烁
        for icon in icons:
            self.play(Flash(icon, color=icon.get_color(), flash_radius=0.3), run_time=0.3)
        
        # 图标旋转
        self.play(Rotate(icons, angle=PI, run_time=1.0))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql function_domain_range.py FunctionDomainRange  # 快速预览
# manim -qh function_domain_range.py FunctionDomainRange   # 高质量渲染