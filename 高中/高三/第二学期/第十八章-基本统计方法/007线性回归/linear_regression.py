"""
线性回归教学动画 - Linear Regression Teaching Animation
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
知识点: 高三统计 - 线性回归
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 全局常量
# ============================================================
BG_COLOR      = "#1a1a2e"
COLOR_DOT     = "#e74c3c"   # 红 - 数据点
COLOR_LINE    = "#3498db"   # 蓝 - 回归直线
COLOR_MEAN    = "#2ecc71"   # 绿 - 均值线/均值点
COLOR_FORMULA = "#f39c12"   # 橙黄 - 公式高亮
COLOR_AUX     = "#9b59b6"   # 紫 - 辅助/残差
COLOR_R       = "#e67e22"   # 相关系数
COLOR_AXIS    = "#d0d0d0"

FONT_CN = "PingFang SC"

# 数据集 (已验证: b=0.8, a=1.8, r≈0.8528)
X_DATA = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
Y_DATA = np.array([2.0, 4.0, 5.0, 4.0, 6.0])
X_BAR  = 3.0
Y_BAR  = 4.2
B_REG  = 0.8
A_REG  = 1.8
R_CORR = 0.8528


class LinearRegressionScene(Scene):
    """线性回归完整教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_scatter_plot()
        self.scene_3_regression_line_concept()
        self.scene_4_least_squares()
        self.scene_5_formula()
        self.scene_6_calculation()
        self.scene_7_result_and_r()
        self.scene_8_outro()

    # ============================================================
    # setup_geometry: 统一初始化所有几何数据
    # ============================================================
    def setup_geometry(self):
        """所有坐标/尺寸在此统一初始化"""
        # ---- 坐标轴参数 ----
        self.AXES_X_RANGE = [0, 6.5, 1]
        self.AXES_Y_RANGE = [0, 8.5, 1]
        self.AXES_X_LENGTH = 5.0
        self.AXES_Y_LENGTH = 5.5
        self.AXES_CENTER = np.array([-1.0, -1.5, 0])  # 坐标轴在屏幕中的位置

        # ---- 预计算坐标转换 ----
        # axes.c2p 是运行时调用的，这里存储相关参数
        self.x_data = X_DATA
        self.y_data = Y_DATA
        self.x_bar = X_BAR
        self.y_bar = Y_BAR
        self.b = B_REG
        self.a = A_REG
        self.r = R_CORR

        # ---- 验证回归计算 ----
        b_check = np.sum((self.x_data - self.x_bar) * (self.y_data - self.y_bar)) / \
                  np.sum((self.x_data - self.x_bar) ** 2)
        a_check = self.y_bar - b_check * self.x_bar
        assert abs(b_check - self.b) < 1e-10, f"b值错误: {b_check}"
        assert abs(a_check - self.a) < 1e-6, f"a值错误: {a_check}"

        # 均值点在回归线上
        y_mean_on_line = self.b * self.x_bar + self.a
        assert abs(y_mean_on_line - self.y_bar) < 1e-6, "均值点不在回归线上!"

    def make_axes(self):
        """创建坐标轴"""
        axes = Axes(
            x_range=self.AXES_X_RANGE,
            y_range=self.AXES_Y_RANGE,
            x_length=self.AXES_X_LENGTH,
            y_length=self.AXES_Y_LENGTH,
            axis_config={
                "color": COLOR_AXIS,
                "stroke_width": 2,
                "include_numbers": True,
                "numbers_to_exclude": [0],
                "font_size": 18,
            },
            tips=True,
        )
        axes.move_to(self.AXES_CENTER)
        return axes

    def make_dots(self, axes):
        """创建5个数据点"""
        dots = VGroup()
        for xi, yi in zip(self.x_data, self.y_data):
            dot = Dot(axes.c2p(xi, yi), radius=0.12, color=COLOR_DOT)
            dots.add(dot)
        return dots

    def make_regression_line(self, axes):
        """创建回归直线"""
        x0, x1 = 0.3, 6.2
        return Line(
            axes.c2p(x0, self.b * x0 + self.a),
            axes.c2p(x1, self.b * x1 + self.a),
            color=COLOR_LINE,
            stroke_width=3
        )

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 钩子标题
        hook = Text(
            "两组数据之间\n藏着什么秘密？",
            font=FONT_CN, font_size=44, color=YELLOW,
            line_spacing=1.2
        ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=1.0)

        # 简单散点预览
        axes_preview = self.make_axes()
        dots_preview = self.make_dots(axes_preview)

        self.play(Create(axes_preview), run_time=0.8)
        for d in dots_preview:
            self.play(FadeIn(d, scale=0.5), run_time=0.2)

        self.wait(0.8)

        # 清理 hook, 保留 axes 和 dots
        self.play(FadeOut(hook), run_time=0.4)

        # 把 axes 和 dots 存起来复用
        self.axes = axes_preview
        self.dots = dots_preview

    # ============================================================
    # Scene 2: 散点图介绍
    # ============================================================
    def scene_2_scatter_plot(self):
        # 坐标轴标签
        x_label = MathTex("x", font_size=28, color=COLOR_AXIS).next_to(
            self.axes.x_axis.get_right(), RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=28, color=COLOR_AXIS).next_to(
            self.axes.y_axis.get_top(), UP, buff=0.1)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)

        # 标题
        title = Text("散点图", font=FONT_CN, font_size=42, color=YELLOW).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 说明文字
        desc1 = Text(
            "直观展示两变量之间的关系",
            font=FONT_CN, font_size=26, color=WHITE
        ).move_to(UP * 5.3)
        self.play(FadeIn(desc1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 数据点坐标标注 (标注第1、3、5个点)
        coord_labels = VGroup()
        for i in [0, 2, 4]:
            xi, yi = self.x_data[i], self.y_data[i]
            lbl = Text(
                f"({int(xi)},{int(yi)})",
                font=FONT_CN, font_size=18, color=COLOR_DOT
            ).next_to(self.axes.c2p(xi, yi), UP + RIGHT * 0.5, buff=0.08)
            coord_labels.add(lbl)

        self.play(*[FadeIn(l, scale=0.8) for l in coord_labels], run_time=0.6)

        # 观察: 正相关趋势
        desc2 = Text(
            "x 增大时，y 也有增大趋势",
            font=FONT_CN, font_size=24, color=COLOR_MEAN
        ).move_to(DOWN * 5.2)
        desc3 = Text(
            "→ 正相关关系",
            font=FONT_CN, font_size=28, color=YELLOW
        ).move_to(DOWN * 5.9)
        self.play(FadeIn(desc2), run_time=0.5)
        self.play(FadeIn(desc3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理本场景临时元素
        self.play(
            FadeOut(title), FadeOut(desc1),
            FadeOut(coord_labels), FadeOut(desc2), FadeOut(desc3),
            run_time=0.5
        )
        self.x_label = x_label
        self.y_label = y_label

    # ============================================================
    # Scene 3: 回归直线概念
    # ============================================================
    def scene_3_regression_line_concept(self):
        title = Text("怎样画一条最优的拟合直线？",
                     font=FONT_CN, font_size=32, color=YELLOW).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.8)

        # 候选直线1: 偏高斜率
        cand1 = Line(
            self.axes.c2p(0.5, 3.0),
            self.axes.c2p(6.0, 7.5),
            color=GRAY, stroke_width=2.5, stroke_opacity=0.7
        )
        # 候选直线2: 偏低斜率
        cand2 = Line(
            self.axes.c2p(0.5, 1.5),
            self.axes.c2p(6.0, 5.0),
            color=GRAY, stroke_width=2.5, stroke_opacity=0.7
        )
        # 候选直线3: 错误方向
        cand3 = Line(
            self.axes.c2p(0.5, 5.5),
            self.axes.c2p(6.0, 2.0),
            color=GRAY, stroke_width=2.5, stroke_opacity=0.7
        )

        self.play(Create(cand1), Create(cand2), Create(cand3), run_time=1.0)

        desc = Text("哪条线最好地描述数据趋势？",
                    font=FONT_CN, font_size=26, color=WHITE).move_to(DOWN * 5.2)
        self.play(FadeIn(desc), run_time=0.4)
        self.wait(0.5)

        # 淡出差的线，突出回归直线
        self.play(FadeOut(cand1), FadeOut(cand2), FadeOut(cand3), run_time=0.4)

        # 回归直线登场
        reg_line = self.make_regression_line(self.axes)
        reg_line_label = MathTex(r"\hat{y} = bx + a", font_size=32, color=COLOR_LINE
                                  ).move_to(DOWN * 5.9)

        self.play(Create(reg_line), run_time=1.2)
        self.play(Write(reg_line_label), run_time=0.8)

        intro_text = Text("回归直线！",
                          font=FONT_CN, font_size=34, color=COLOR_LINE).move_to(DOWN * 5.2)
        self.play(ReplacementTransform(desc, intro_text), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(intro_text), FadeOut(reg_line_label),
            run_time=0.4
        )
        self.reg_line = reg_line

    # ============================================================
    # Scene 4: 最小二乘法可视化
    # ============================================================
    def scene_4_least_squares(self):
        title = Text("最小二乘法", font=FONT_CN, font_size=42, color=YELLOW).move_to(UP * 6.2)
        subtitle = Text("使残差平方和最小",
                        font=FONT_CN, font_size=28, color=WHITE).move_to(UP * 5.4)
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)

        # 绘制每个点到回归直线的残差线段 (竖直方向)
        residual_lines = VGroup()
        residual_squares = VGroup()

        for xi, yi in zip(self.x_data, self.y_data):
            y_hat = self.b * xi + self.a
            residual = yi - y_hat

            # 竖直残差线
            pt_data  = self.axes.c2p(xi, yi)
            pt_line  = self.axes.c2p(xi, y_hat)
            vline = DashedLine(pt_data, pt_line,
                               color=COLOR_AUX, dash_length=0.08, stroke_width=2.5)
            residual_lines.add(vline)

            # 残差对应的小正方形 (示意)
            side = abs(pt_data[1] - pt_line[1])  # 屏幕像素高度
            sq_center = (pt_data + pt_line) / 2 + LEFT * side / 2
            sq = Square(side_length=side,
                        color=COLOR_AUX, fill_color=COLOR_AUX, fill_opacity=0.15,
                        stroke_width=1.5).move_to(sq_center)
            residual_squares.add(sq)

        self.play(*[Create(l) for l in residual_lines], run_time=1.0)
        self.play(*[Create(s) for s in residual_squares], run_time=0.8)

        # 标注: eᵢ = yᵢ - ŷᵢ
        e_label = MathTex(r"e_i = y_i - \hat{y}_i", font_size=30, color=COLOR_AUX
                          ).move_to(DOWN * 5.0)
        sum_label = MathTex(r"\sum e_i^2 \to \min", font_size=36, color=YELLOW
                            ).move_to(DOWN * 5.8)
        self.play(Write(e_label), run_time=0.6)
        self.play(Write(sum_label), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(residual_lines), FadeOut(residual_squares),
            FadeOut(e_label), FadeOut(sum_label),
            run_time=0.6
        )

    # ============================================================
    # Scene 5: 公式展示
    # ============================================================
    def scene_5_formula(self):
        title = Text("回归系数公式", font=FONT_CN, font_size=38, color=YELLOW).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 公式: b
        formula_b_title = Text("斜率 b：", font=FONT_CN, font_size=28, color=COLOR_FORMULA
                               ).move_to(UP * 5.1 + LEFT * 1.5)
        formula_b = MathTex(
            r"b = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}",
            font_size=34, color=WHITE
        ).move_to(UP * 4.0)

        self.play(FadeIn(formula_b_title), run_time=0.4)
        self.play(Write(formula_b), run_time=1.2)
        self.wait(0.5)

        # 等价形式
        equiv_label = Text("等价形式：", font=FONT_CN, font_size=22, color=GRAY_A
                           ).next_to(formula_b, DOWN, buff=0.4).shift(LEFT * 1.0)
        formula_b2 = MathTex(
            r"b = \frac{\sum x_i y_i - n\bar{x}\bar{y}}{\sum x_i^2 - n\bar{x}^2}",
            font_size=30, color=GRAY_A
        ).next_to(equiv_label, DOWN, buff=0.3)

        self.play(FadeIn(equiv_label), Write(formula_b2), run_time=0.9)

        # 分隔线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1
                   ).next_to(formula_b2, DOWN, buff=0.4)
        self.play(Create(sep), run_time=0.3)

        # 公式: a
        formula_a_title = Text("截距 a：", font=FONT_CN, font_size=28, color=COLOR_FORMULA
                               ).next_to(sep, DOWN, buff=0.3).shift(LEFT * 1.5)
        formula_a = MathTex(
            r"a = \bar{y} - b\bar{x}",
            font_size=40, color=WHITE
        ).next_to(formula_a_title, DOWN, buff=0.35)

        self.play(FadeIn(formula_a_title), run_time=0.3)
        self.play(Write(formula_a), run_time=0.8)
        self.wait(0.5)

        # 重要性质: 回归直线过 (x̄, ȳ)
        prop_box = RoundedRectangle(
            width=7.0, height=1.1, corner_radius=0.2,
            color=COLOR_MEAN, stroke_width=2,
            fill_color=COLOR_MEAN, fill_opacity=0.1
        ).next_to(formula_a, DOWN, buff=0.5)
        prop_text = Text(
            "回归直线必过均值点  (x̄, ȳ)",
            font=FONT_CN, font_size=26, color=COLOR_MEAN
        ).move_to(prop_box.get_center())

        self.play(Create(prop_box), FadeIn(prop_text), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula_b_title), FadeOut(formula_b),
            FadeOut(equiv_label), FadeOut(formula_b2), FadeOut(sep),
            FadeOut(formula_a_title), FadeOut(formula_a),
            FadeOut(prop_box), FadeOut(prop_text),
            run_time=0.5
        )

    # ============================================================
    # Scene 6: 代入具体数据计算
    # ============================================================
    def scene_6_calculation(self):
        title = Text("代入数据，计算回归系数",
                     font=FONT_CN, font_size=32, color=YELLOW).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 数据表格 (文字呈现)
        data_text = Text(
            "x:  1  2  3  4  5\ny:  2  4  5  4  6",
            font="Noto Sans Mono CJK SC", font_size=24, color=WHITE,
            line_spacing=1.3
        ).move_to(UP * 5.0)
        self.play(FadeIn(data_text), run_time=0.5)

        # Step1: 计算均值
        step1 = MathTex(
            r"\bar{x} = \frac{1+2+3+4+5}{5} = 3",
            font_size=30, color=WHITE
        ).move_to(UP * 3.5)
        step1b = MathTex(
            r"\bar{y} = \frac{2+4+5+4+6}{5} = 4.2",
            font_size=30, color=WHITE
        ).next_to(step1, DOWN, buff=0.35)

        step1_label = Text("① 计算均值", font=FONT_CN, font_size=24, color=COLOR_FORMULA
                           ).next_to(step1, LEFT, buff=0.3).shift(DOWN * 0.2)
        self.play(FadeIn(step1_label), Write(step1), run_time=0.7)
        self.play(Write(step1b), run_time=0.6)
        self.wait(0.4)

        # Step2: 计算 b
        step2_label = Text("② 计算 b", font=FONT_CN, font_size=24, color=COLOR_FORMULA
                           ).next_to(step1b, DOWN + LEFT * 1.5, buff=0.5)
        step2_num = MathTex(
            r"\sum(x_i-\bar{x})(y_i-\bar{y}) = 8",
            font_size=28, color=GRAY_A
        ).next_to(step2_label, DOWN, buff=0.3)
        step2_den = MathTex(
            r"\sum(x_i-\bar{x})^2 = 10",
            font_size=28, color=GRAY_A
        ).next_to(step2_num, DOWN, buff=0.25)
        step2_b = MathTex(
            r"b = \frac{8}{10} = 0.8",
            font_size=36, color=COLOR_LINE
        ).next_to(step2_den, DOWN, buff=0.3)

        self.play(FadeIn(step2_label), run_time=0.3)
        self.play(Write(step2_num), run_time=0.5)
        self.play(Write(step2_den), run_time=0.5)
        self.play(Write(step2_b), run_time=0.6)
        self.wait(0.4)

        # Step3: 计算 a
        step3_label = Text("③ 计算 a", font=FONT_CN, font_size=24, color=COLOR_FORMULA
                           ).next_to(step2_b, DOWN + LEFT * 1.0, buff=0.5)
        step3_a = MathTex(
            r"a = \bar{y} - b\bar{x} = 4.2 - 0.8 \times 3 = 1.8",
            font_size=28, color=COLOR_LINE
        ).next_to(step3_label, DOWN, buff=0.3)

        self.play(FadeIn(step3_label), Write(step3_a), run_time=0.8)
        self.wait(0.5)

        # 结果高亮
        result_box = SurroundingRectangle(
            VGroup(step2_b, step3_a),
            color=YELLOW, buff=0.2, corner_radius=0.15
        )
        result = MathTex(
            r"\hat{y} = 0.8x + 1.8",
            font_size=42, color=YELLOW
        ).next_to(step3_a, DOWN, buff=0.5)

        self.play(Create(result_box), run_time=0.4)
        self.play(Write(result), run_time=0.8)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(data_text),
            FadeOut(step1_label), FadeOut(step1), FadeOut(step1b),
            FadeOut(step2_label), FadeOut(step2_num),
            FadeOut(step2_den), FadeOut(step2_b),
            FadeOut(step3_label), FadeOut(step3_a),
            FadeOut(result_box), FadeOut(result),
            run_time=0.5
        )

    # ============================================================
    # Scene 7: 展示回归直线 + 相关系数
    # ============================================================
    def scene_7_result_and_r(self):
        title = Text("回归直线与相关系数",
                     font=FONT_CN, font_size=34, color=YELLOW).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 最终公式
        final_formula = MathTex(
            r"\hat{y} = 0.8x + 1.8",
            font_size=40, color=COLOR_LINE
        ).move_to(UP * 5.2)
        self.play(Write(final_formula), run_time=0.8)

        # 均值点标注
        mean_dot = Dot(self.axes.c2p(self.x_bar, self.y_bar),
                       radius=0.14, color=COLOR_MEAN)
        mean_label = MathTex(r"(\bar{x},\bar{y})", font_size=26, color=COLOR_MEAN
                              ).next_to(mean_dot, UP + RIGHT, buff=0.12)

        self.play(Flash(mean_dot, color=COLOR_MEAN, flash_radius=0.3))
        self.play(FadeIn(mean_dot), Write(mean_label), run_time=0.5)

        # 演示预测: x=3.5 时
        x_pred = 3.5
        y_pred = self.b * x_pred + self.a  # = 4.6
        pred_vline = DashedLine(
            self.axes.c2p(x_pred, 0),
            self.axes.c2p(x_pred, y_pred),
            color=GRAY_A, dash_length=0.08
        )
        pred_hline = DashedLine(
            self.axes.c2p(0, y_pred),
            self.axes.c2p(x_pred, y_pred),
            color=GRAY_A, dash_length=0.08
        )
        pred_dot = Dot(self.axes.c2p(x_pred, y_pred), radius=0.1, color=YELLOW)
        pred_text = Text("x=3.5 时，ŷ=4.6",
                         font=FONT_CN, font_size=24, color=YELLOW).move_to(DOWN * 4.8)

        self.play(Create(pred_vline), Create(pred_hline), run_time=0.6)
        self.play(FadeIn(pred_dot, scale=0.5), FadeIn(pred_text), run_time=0.5)
        self.wait(0.6)

        # 相关系数
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1
                   ).move_to(DOWN * 5.5)
        self.play(
            FadeOut(pred_vline), FadeOut(pred_hline),
            FadeOut(pred_dot), FadeOut(pred_text),
            Create(sep), run_time=0.4
        )

        r_title = Text("相关系数 r", font=FONT_CN, font_size=30, color=COLOR_R
                       ).move_to(DOWN * 6.0)
        r_formula = MathTex(
            r"r = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2 \cdot \sum(y_i-\bar{y})^2}}",
            font_size=26, color=WHITE
        ).move_to(DOWN * 6.9)

        self.play(FadeIn(r_title), run_time=0.4)
        self.play(Write(r_formula), run_time=1.0)

        r_value = MathTex(r"r \approx 0.85", font_size=38, color=COLOR_R
                          ).next_to(r_formula, DOWN, buff=0.4)
        r_desc = Text("|r| 越接近1，线性相关越强",
                      font=FONT_CN, font_size=22, color=GRAY_A
                      ).next_to(r_value, DOWN, buff=0.25)
        self.play(Write(r_value), run_time=0.5)
        self.play(FadeIn(r_desc), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(final_formula),
            FadeOut(mean_dot), FadeOut(mean_label),
            FadeOut(sep), FadeOut(r_title),
            FadeOut(r_formula), FadeOut(r_value), FadeOut(r_desc),
            run_time=0.5
        )

    # ============================================================
    # Scene 8: 片尾
    # ============================================================
    def scene_8_outro(self):
        # 淡出坐标轴和数据点
        self.play(
            FadeOut(self.axes), FadeOut(self.dots),
            FadeOut(self.reg_line),
            FadeOut(self.x_label), FadeOut(self.y_label),
            run_time=0.6
        )

        # 知识总结
        summary_title = Text("线性回归 · 核心公式",
                             font=FONT_CN, font_size=36, color=YELLOW).move_to(UP * 4.5)
        self.play(Write(summary_title), run_time=0.6)

        formula_group = VGroup()
        clean_lines = [
            (r"\hat{y} = bx + a",                                                    "回归直线"),
            (r"b = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2}",    "斜率"),
            (r"a = \bar{y} - b\bar{x}",                                              "截距"),
        ]
        for i, (tex, note) in enumerate(clean_lines):
            f = MathTex(tex, font_size=28, color=WHITE)
            n = Text(note, font=FONT_CN, font_size=20, color=GRAY_A)
            row = VGroup(f, n).arrange(RIGHT, buff=0.5)
            row.move_to(UP * (3.2 - i * 1.1))
            formula_group.add(row)

        r_formula_part = MathTex(r"|r| \to 1 \Rightarrow", font_size=28, color=WHITE)
        r_cn_part      = Text("强线性相关", font=FONT_CN, font_size=26, color=WHITE)
        r_note_part    = Text("相关系数", font=FONT_CN, font_size=20, color=GRAY_A)
        r_row = VGroup(
            VGroup(r_formula_part, r_cn_part).arrange(RIGHT, buff=0.15),
            r_note_part
        ).arrange(RIGHT, buff=0.5)
        r_row.move_to(UP * (3.2 - 3 * 1.1))
        formula_group.add(r_row)

        for row in formula_group:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(0.5)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=40, color=WHITE
        ).move_to(DOWN * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=30, color=GRAY_B
        ).next_to(author_big, DOWN, buff=0.4)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT_CN, font_size=30, color=YELLOW
        ).next_to(author_id, DOWN, buff=0.6)

        self.play(
            Transform(self.author_info, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(summary_title), FadeOut(formula_group),
            FadeOut(self.author_info), FadeOut(author_id), FadeOut(follow),
            run_time=0.8
        )

# manim -pql linear_regression.py LinearRegressionScene   # 快速预览
# manim -qh linear_regression.py LinearRegressionScene    # 高质量 1080p