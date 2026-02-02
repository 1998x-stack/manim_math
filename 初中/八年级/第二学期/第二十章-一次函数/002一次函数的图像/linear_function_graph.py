"""
一次函数的图像 - Linear Function Graph Animation
使用 Manim 创建的中学数学教学视频

内容: 一次函数 y=kx+b 的图像特征、斜率k和截距b的影响
目标观众: 八年级学生
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


class LinearFunctionGraph(Scene):
    """
    一次函数图像教学动画场景
    
    场景顺序:
    1. 开场钩子 - 神秘直线引入
    2. 建立坐标系 - 数学框架
    3. 绘制主函数 y=2x+1 - 基本形态
    4. 斜率k的影响 (k>0) - 倾斜方向
    5. 斜率k的影响 (k<0) - 对比展示
    6. 截距b的影响 - 位置变化
    7. 总结与结尾 - 关注引导
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色 - 主函数线
        self.COLOR_SECONDARY = "#e74c3c"     # 红色 - 对比函数线
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮标注
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        self.COLOR_POSITIVE_K = "#2ecc71"    # 绿色 - k>0的线
        self.COLOR_NEGATIVE_K = "#9b59b6"    # 紫色 - k<0的线
        
        # 字体大小配置
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_coordinate_system()
        self.scene_3_main_function()
        self.scene_4_slope_positive()
        self.scene_5_slope_negative()
        self.scene_6_intercept_effect()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化坐标系和函数参数"""
        # 坐标系参数
        self.AXES_X_RANGE = [-4, 4, 1]
        self.AXES_Y_RANGE = [-3, 5, 1]
        self.AXES_SCALE = 0.85
        self.AXES_OFFSET = UP * 1.5
        
        # 主函数: y = 2x + 1
        self.k_main = 2
        self.b_main = 1
        
        # 对比函数1: y = 0.5x - 1 (较平缓)
        self.k_compare1 = 0.5
        self.b_compare1 = -1
        
        # 对比函数2: y = -x + 2 (k<0)
        self.k_negative = -1
        self.b_negative = 2
        
        # 计算关键点
        # 主函数的交点
        self.y_intercept_main = np.array([0, self.b_main, 0])  # (0, b)
        self.x_intercept_main = np.array([-self.b_main / self.k_main, 0, 0])  # (-b/k, 0)
        
        # 验证计算
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证 y = kx + b 在交点处的值
        # y轴交点: x=0, y应该等于b
        y_at_y_intercept = self.k_main * 0 + self.b_main
        if abs(y_at_y_intercept - self.b_main) > epsilon:
            print(f"WARNING: y轴交点计算错误! y={y_at_y_intercept}, 应为 {self.b_main}")
        
        # x轴交点: y=0, x应该等于-b/k
        x_at_x_intercept = -self.b_main / self.k_main
        y_at_x_intercept = self.k_main * x_at_x_intercept + self.b_main
        if abs(y_at_x_intercept) > epsilon:
            print(f"WARNING: x轴交点计算错误! y={y_at_x_intercept}, 应为 0")
        
        print("✓ 几何验证完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook_text = Text(
            "这条直线藏着什么秘密?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 神秘的直线 (部分显示)
        mystery_line = Line(
            LEFT * 3 + DOWN * 2,
            RIGHT * 3 + UP * 3,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(UP * 0.5)
        
        self.play(Create(mystery_line), run_time=0.8)
        
        # 问号
        question_mark = Text(
            "?",
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).next_to(mystery_line, RIGHT, buff=0.5)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.3)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            mystery_line.animate.set_opacity(0.2),
            run_time=0.5
        )
        self.remove(mystery_line)
    
    def scene_2_coordinate_system(self):
        """场景2: 建立坐标系"""
        # 标题
        title = Text(
            "一次函数的图像",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.5)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=self.AXES_X_RANGE,
            y_range=self.AXES_Y_RANGE,
            x_length=8 * self.AXES_SCALE,
            y_length=7 * self.AXES_SCALE,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            },
            tips=True
        ).move_to(self.AXES_OFFSET)
        
        self.play(Create(self.axes), run_time=1.2)
        
        # 原点标注
        origin_label = Text(
            "O",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=WHITE
        ).next_to(self.axes.c2p(0, 0), DL, buff=0.15)
        
        self.play(FadeIn(origin_label), run_time=0.3)
        
        # 轴标签
        x_label = Text(
            "x",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        
        y_label = Text(
            "y",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).next_to(self.axes.y_axis.get_end(), UP, buff=0.2)
        
        self.play(Write(x_label), Write(y_label), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "所有一次函数都在这个坐标系中",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(FadeOut(title), FadeOut(explanation), run_time=0.4)
    
    def scene_3_main_function(self):
        """场景3: 绘制主函数 y=2x+1"""
        # 函数表达式
        formula = MathTex(
            r"y = 2x + 1",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(formula), run_time=0.8)
        
        # 绘制图像
        graph = self.axes.plot(
            lambda x: self.k_main * x + self.b_main,
            x_range=[-3, 3],
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        self.play(Create(graph), run_time=1.5)
        self.graph_main = graph  # 保存引用
        self.formula_main = formula
        
        # 说明文字1
        explanation1 = Text(
            "图像是一条直线",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(explanation1), run_time=0.3)
        
        # y轴交点标记
        y_intercept_point = self.axes.c2p(0, self.b_main)
        y_intercept_dot = Dot(
            y_intercept_point,
            color=self.COLOR_HIGHLIGHT,
            radius=0.08
        )
        
        y_intercept_label = Text(
            "y轴交点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(y_intercept_dot, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(y_intercept_dot, scale=0.5),
            Write(y_intercept_label),
            run_time=0.5
        )
        
        # 虚线连接y轴
        dashed_line_y = DashedLine(
            self.axes.c2p(0, 0),
            y_intercept_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(dashed_line_y), run_time=0.4)
        
        # 坐标标注
        coord_y = MathTex(
            r"(0, 1)",
            font_size=self.FONT_SMALL,
            color=WHITE
        ).next_to(y_intercept_dot, LEFT, buff=0.2)
        
        self.play(FadeIn(coord_y), run_time=0.3)
        
        # 说明文字2
        explanation2 = Text(
            "与y轴交于 (0, b)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(explanation2), run_time=0.3)
        
        # x轴交点标记
        x_intercept_value = -self.b_main / self.k_main
        x_intercept_point = self.axes.c2p(x_intercept_value, 0)
        x_intercept_dot = Dot(
            x_intercept_point,
            color=self.COLOR_HIGHLIGHT,
            radius=0.08
        )
        
        x_intercept_label = Text(
            "x轴交点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_HIGHLIGHT
        ).next_to(x_intercept_dot, DOWN, buff=0.2)
        
        self.play(
            FadeIn(x_intercept_dot, scale=0.5),
            Write(x_intercept_label),
            run_time=0.5
        )
        
        # 虚线连接x轴
        dashed_line_x = DashedLine(
            self.axes.c2p(0, 0),
            x_intercept_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(dashed_line_x), run_time=0.4)
        
        # 坐标标注
        coord_x = MathTex(
            r"(-0.5, 0)",
            font_size=self.FONT_SMALL,
            color=WHITE
        ).next_to(x_intercept_dot, UP, buff=0.2)
        
        self.play(FadeIn(coord_x), run_time=0.3)
        
        # 说明文字3
        explanation3 = Text(
            "与x轴交于 (-b/k, 0)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理虚线和部分标注
        self.play(
            FadeOut(dashed_line_y),
            FadeOut(dashed_line_x),
            FadeOut(explanation3),
            FadeOut(y_intercept_label),
            FadeOut(x_intercept_label),
            run_time=0.4
        )
    
    def scene_4_slope_positive(self):
        """场景4: 斜率k的影响 (k>0)"""
        # 高亮k值
        formula_highlight = MathTex(
            r"y = {{ 2 }}x + 1",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        formula_highlight.set_color_by_tex("2", RED)
        
        self.play(Transform(self.formula_main, formula_highlight), run_time=0.6)
        
        # 箭头指示方向 (从左下到右上)
        arrow_start = self.axes.c2p(-2, -3)
        arrow_end = self.axes.c2p(2, 5)
        direction_arrow = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_POSITIVE_K,
            stroke_width=6,
            buff=0.5,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(direction_arrow), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "k > 0: 直线从左下到右上倾斜",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 对比: k=0.5的直线 (较平缓)
        compare_graph = self.axes.plot(
            lambda x: self.k_compare1 * x + self.b_compare1,
            x_range=[-3, 3],
            color=self.COLOR_POSITIVE_K,
            stroke_width=3,
            stroke_opacity=0.6
        )
        
        compare_label = MathTex(
            r"y = 0.5x - 1",
            font_size=self.FONT_SMALL,
            color=self.COLOR_POSITIVE_K
        ).move_to(self.axes.c2p(2.5, 0.5))
        
        self.play(Create(compare_graph), run_time=1.0)
        self.play(FadeIn(compare_label), run_time=0.4)
        
        # 对比说明
        compare_text = Text(
            "|k|越大, 直线越陡",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(compare_text, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(direction_arrow),
            FadeOut(compare_graph),
            FadeOut(compare_label),
            FadeOut(compare_text),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 恢复原公式
        formula_normal = MathTex(
            r"y = 2x + 1",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula_main, formula_normal), run_time=0.3)
    
    def scene_5_slope_negative(self):
        """场景5: 斜率k的影响 (k<0)"""
        # 原函数变淡
        self.play(
            self.graph_main.animate.set_opacity(0.3),
            self.formula_main.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # 新函数表达式
        new_formula = MathTex(
            r"y = -x + 2",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_NEGATIVE_K
        ).move_to(UP * 5.2)
        
        self.play(Write(new_formula), run_time=0.8)
        
        # 新直线绘制
        negative_graph = self.axes.plot(
            lambda x: self.k_negative * x + self.b_negative,
            x_range=[-2, 4],
            color=self.COLOR_NEGATIVE_K,
            stroke_width=4
        )
        
        self.play(Create(negative_graph), run_time=1.2)
        
        # 高亮k值
        formula_highlight = MathTex(
            r"y = {{ -1 }}x + 2",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_NEGATIVE_K
        ).move_to(UP * 5.2)
        formula_highlight.set_color_by_tex("-1", PURPLE)
        
        self.play(Transform(new_formula, formula_highlight), run_time=0.6)
        
        # 箭头指示方向 (从左上到右下)
        arrow_start = self.axes.c2p(-1, 3)
        arrow_end = self.axes.c2p(3, -1)
        direction_arrow_down = Arrow(
            arrow_start,
            arrow_end,
            color=self.COLOR_NEGATIVE_K,
            stroke_width=6,
            buff=0.5,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(direction_arrow_down), run_time=0.5)
        
        # 说明文字
        explanation_negative = Text(
            "k < 0: 直线从左上到右下倾斜",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation_negative, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(negative_graph),
            FadeOut(new_formula),
            FadeOut(direction_arrow_down),
            FadeOut(explanation_negative),
            run_time=0.6
        )
        
        # 恢复原函数
        self.play(
            self.graph_main.animate.set_opacity(1.0),
            self.formula_main.animate.set_opacity(1.0),
            run_time=0.5
        )
    
    def scene_6_intercept_effect(self):
        """场景6: 截距b的影响"""
        # 三条平行线: y=2x+2, y=2x+1, y=2x-1
        line_upper = self.axes.plot(
            lambda x: self.k_main * x + 2,
            x_range=[-3, 3],
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            stroke_opacity=0.6
        )
        
        line_lower = self.axes.plot(
            lambda x: self.k_main * x + (-1),
            x_range=[-3, 3],
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            stroke_opacity=0.6
        )
        
        # 标签
        label_upper = MathTex(
            r"y=2x+2",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIMARY
        ).move_to(self.axes.c2p(2.2, 6.5))
        
        label_lower = MathTex(
            r"y=2x-1",
            font_size=self.FONT_SMALL,
            color=self.COLOR_PRIMARY
        ).move_to(self.axes.c2p(2.2, 3))
        
        parallel_lines = VGroup(line_upper, line_lower)
        labels = VGroup(label_upper, label_lower)
        
        self.play(
            FadeIn(parallel_lines, lag_ratio=0.3),
            FadeIn(labels, lag_ratio=0.3),
            run_time=1.2
        )
        
        # 高亮b值
        formula_highlight = MathTex(
            r"y = 2x + {{ 1 }}",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        formula_highlight.set_color_by_tex("1", YELLOW)
        
        self.play(Transform(self.formula_main, formula_highlight), run_time=0.6)
        
        # y轴交点标记
        y_intercept_upper = Dot(self.axes.c2p(0, 2), color=YELLOW, radius=0.06)
        y_intercept_main = Dot(self.axes.c2p(0, 1), color=YELLOW, radius=0.06)
        y_intercept_lower = Dot(self.axes.c2p(0, -1), color=YELLOW, radius=0.06)
        
        y_intercepts = VGroup(y_intercept_upper, y_intercept_main, y_intercept_lower)
        
        self.play(FadeIn(y_intercepts), run_time=0.5)
        
        # 说明文字1
        explanation_b = Text(
            "b 决定直线与y轴的交点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation_b, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)
        
        # 说明文字2
        explanation_b2 = Text(
            "b增大, 直线整体上移",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(FadeIn(explanation_b2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(parallel_lines),
            FadeOut(labels),
            FadeOut(y_intercepts),
            FadeOut(explanation_b),
            FadeOut(explanation_b2),
            run_time=0.6
        )
        
        # 恢复原公式
        formula_normal = MathTex(
            r"y = 2x + 1",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Transform(self.formula_main, formula_normal), run_time=0.3)
    
    def scene_7_summary(self):
        """场景7: 总结与结尾"""
        # 清空场景
        mobjects_to_clear = [
            self.axes,
            self.graph_main,
            self.formula_main
        ]
        
        self.play(
            *[FadeOut(mob) for mob in mobjects_to_clear],
            run_time=0.5
        )
        
        # 创建总结卡片
        card1 = self.create_summary_card(
            "直线形态",
            "一次函数图像是直线",
            self.COLOR_PRIMARY,
            UP * 2
        )
        
        card2 = self.create_summary_card(
            "斜率影响",
            "k决定倾斜方向和陡峭程度",
            self.COLOR_POSITIVE_K,
            ORIGIN
        )
        
        card3 = self.create_summary_card(
            "截距影响",
            "b决定与y轴交点位置",
            self.COLOR_HIGHLIGHT,
            DOWN * 2
        )
        
        cards = VGroup(card1, card2, card3)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(1.0)
        
        # 卡片淡出
        self.play(FadeOut(cards), run_time=0.5)
        
        # 作者信息放大
        author_large = Text(
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
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多函数技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰动画 - 小图标
        icon_line = Line(
            LEFT * 0.3,
            RIGHT * 0.3,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        )
        
        icons = VGroup(*[
            icon_line.copy().move_to(
                follow_text.get_center() + 1.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.6
        )
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
    
    def create_summary_card(self, title, content, color, position):
        """创建总结卡片"""
        # 图标
        icon = Circle(
            radius=0.2,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        return card


# 渲染命令:
# manim -pql linear_function_graph.py LinearFunctionGraph  # 快速预览
# manim -qh linear_function_graph.py LinearFunctionGraph   # 高质量 1080p