"""
数据的离散程度 - Manim 教学动画
知识点: 极差、方差、标准差、变异系数
目标受众: 高三学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 颜色配置
BG_COLOR = "#1a1a2e"
COLOR_A = "#00d4ff"      # 数据集A - 青蓝色（集中）
COLOR_B = "#ff6b6b"      # 数据集B - 红橙色（分散）
COLOR_MEAN = "#ffd700"   # 均值线 - 金色
COLOR_FORMULA = "#a8e6cf"  # 公式 - 浅绿色
COLOR_HIGHLIGHT = YELLOW
COLOR_DEV = "#ff9f43"    # 偏差 - 橙色

FONT = "Noto Sans CJK SC"

# 字体大小
FS_TITLE = 40
FS_SUBTITLE = 30
FS_BODY = 24
FS_SMALL = 20
FS_FORMULA = 28
FS_AUTHOR = 20

# 数据集
DATA_A = np.array([3, 4, 5, 6, 7], dtype=float)
DATA_B = np.array([1, 2, 5, 8, 9], dtype=float)

# 数据到逻辑坐标的映射 (数据范围 [0,10] → 逻辑x [-3.5, 3.5])
def d2x(val):
    """将数据值映射到逻辑 x 坐标"""
    return (val - 0) / 10 * 7.0 - 3.5


class DataDispersion(Scene):
    """数据的离散程度教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 初始化几何数据
        self.setup_data()

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_range()
        self.scene_3_variance()
        self.scene_4_std()
        self.scene_5_summary()
        self.scene_6_outro()

    # ============================================================
    # 数据初始化
    # ============================================================
    def setup_data(self):
        """统一初始化所有统计数据"""
        # 数据集
        self.data_A = DATA_A
        self.data_B = DATA_B

        # 均值
        self.mean_A = float(np.mean(self.data_A))  # 5.0
        self.mean_B = float(np.mean(self.data_B))  # 5.0

        # 极差
        self.range_A = float(np.max(self.data_A) - np.min(self.data_A))  # 4
        self.range_B = float(np.max(self.data_B) - np.min(self.data_B))  # 8

        # 方差
        self.var_A = float(np.sum((self.data_A - self.mean_A) ** 2) / len(self.data_A))  # 2
        self.var_B = float(np.sum((self.data_B - self.mean_B) ** 2) / len(self.data_B))  # 10

        # 标准差
        self.std_A = float(np.sqrt(self.var_A))   # √2 ≈ 1.41
        self.std_B = float(np.sqrt(self.var_B))   # √10 ≈ 3.16

        # 逻辑坐标（x方向）
        self.x_A = [d2x(v) for v in self.data_A]
        self.x_B = [d2x(v) for v in self.data_B]
        self.x_mean = d2x(self.mean_A)  # 均值的 x 坐标 = 0

        # 验证
        assert abs(self.mean_A - 5.0) < 1e-6
        assert abs(self.mean_B - 5.0) < 1e-6
        assert abs(self.var_A - 2.0) < 1e-6
        assert abs(self.var_B - 10.0) < 1e-6
        print("✓ 数据验证通过")

    # ============================================================
    # 辅助函数
    # ============================================================
    def make_number_line(self, y_pos, color=WHITE, tick_values=None):
        """创建数轴"""
        if tick_values is None:
            tick_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        line = Line(
            np.array([d2x(-0.3), y_pos, 0]),
            np.array([d2x(10.3), y_pos, 0]),
            color=color, stroke_width=2
        )
        # 箭头
        arrow_tip = Triangle(fill_color=color, fill_opacity=1, stroke_width=0)
        arrow_tip.scale(0.1).rotate(-PI/2)
        arrow_tip.move_to(np.array([d2x(10.3) + 0.1, y_pos, 0]))

        ticks = VGroup()
        labels = VGroup()
        for v in tick_values:
            lx = d2x(v)
            tick = Line(
                np.array([lx, y_pos - 0.12, 0]),
                np.array([lx, y_pos + 0.12, 0]),
                color=color, stroke_width=1.5
            )
            ticks.add(tick)
            lbl = Text(str(int(v)), font=FONT, font_size=16, color=color)
            lbl.move_to(np.array([lx, y_pos - 0.32, 0]))
            labels.add(lbl)

        return VGroup(line, arrow_tip, ticks, labels)

    def make_dot(self, x_logic, y_logic, color, radius=0.14):
        """创建数据点"""
        return Dot(
            np.array([x_logic, y_logic, 0]),
            radius=radius,
            color=color,
            fill_opacity=1
        )

    def make_data_dots(self, data, y_base, color, dot_spacing=0.32):
        """创建数据点群（支持堆叠）"""
        dots = VGroup()
        # 统计每个值的出现次数（用于堆叠）
        from collections import Counter
        count = Counter()
        for v in data:
            lx = d2x(float(v))
            ly = y_base + count[v] * dot_spacing
            dot = self.make_dot(lx, ly, color)
            dots.add(dot)
            count[v] += 1
        return dots

    def make_label_A(self, y_pos):
        """数据集A标签"""
        lbl = Text("A组", font=FONT, font_size=FS_SMALL, color=COLOR_A)
        lbl.move_to(np.array([d2x(-0.3) - 0.45, y_pos, 0]))
        return lbl

    def make_label_B(self, y_pos):
        """数据集B标签"""
        lbl = Text("B组", font=FONT, font_size=FS_SMALL, color=COLOR_B)
        lbl.move_to(np.array([d2x(-0.3) - 0.45, y_pos, 0]))
        return lbl

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        """开场：抓住注意力，引出问题"""
        # 作者信息
        self.author_text = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=FS_AUTHOR, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_text, shift=DOWN * 0.2), run_time=0.4)

        # 主标题
        title = Text("数据的离散程度", font=FONT, font_size=FS_TITLE, color=GOLD)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.8)

        # 钩子问题
        q_line1 = Text("两组同学的考试成绩", font=FONT, font_size=FS_BODY, color=WHITE)
        q_line2 = Text("平均分相同，谁更稳定？", font=FONT, font_size=FS_SUBTITLE, color=COLOR_HIGHLIGHT)
        q_line1.move_to(UP * 4.6)
        q_line2.move_to(UP * 3.9)

        self.play(FadeIn(q_line1), run_time=0.5)
        self.play(FadeIn(q_line2, scale=1.05), run_time=0.6)

        # 数轴 A（高位）
        AXIS_A_Y = 2.5
        AXIS_B_Y = 0.8
        axis_a = self.make_number_line(AXIS_A_Y, color=COLOR_A)
        axis_b = self.make_number_line(AXIS_B_Y, color=COLOR_B)
        lbl_a = self.make_label_A(AXIS_A_Y)
        lbl_b = self.make_label_B(AXIS_B_Y)

        # 数据集标注
        data_text_A = Text("A: {3, 4, 5, 6, 7}", font=FONT, font_size=FS_SMALL, color=COLOR_A)
        data_text_B = Text("B: {1, 2, 5, 8, 9}", font=FONT, font_size=FS_SMALL, color=COLOR_B)
        data_text_A.move_to(np.array([0, AXIS_A_Y + 0.55, 0]))
        data_text_B.move_to(np.array([0, AXIS_B_Y + 0.55, 0]))

        self.play(
            Create(axis_a), FadeIn(lbl_a), FadeIn(data_text_A),
            run_time=0.7
        )
        dots_A = self.make_data_dots(self.data_A, AXIS_A_Y + 0.02, COLOR_A)
        self.play(FadeIn(dots_A, scale=0.5), run_time=0.6)

        self.play(
            Create(axis_b), FadeIn(lbl_b), FadeIn(data_text_B),
            run_time=0.7
        )
        dots_B = self.make_data_dots(self.data_B, AXIS_B_Y + 0.02, COLOR_B)
        self.play(FadeIn(dots_B, scale=0.5), run_time=0.6)

        # 均值相同提示
        mean_hint = Text("两组平均分 x̄ = 5 相同！", font=FONT, font_size=FS_BODY, color=COLOR_MEAN)
        mean_hint.move_to(UP * (-0.5))
        self.play(FadeIn(mean_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理，保留数轴
        self.play(
            FadeOut(title), FadeOut(q_line1), FadeOut(q_line2),
            FadeOut(mean_hint),
            run_time=0.5
        )

        # 保存到 self
        self.axis_a = axis_a
        self.axis_b = axis_b
        self.lbl_a = lbl_a
        self.lbl_b = lbl_b
        self.dots_A = dots_A
        self.dots_B = dots_B
        self.data_text_A = data_text_A
        self.data_text_B = data_text_B
        self.AXIS_A_Y = AXIS_A_Y
        self.AXIS_B_Y = AXIS_B_Y

    # ============================================================
    # Scene 2: 极差
    # ============================================================
    def scene_2_range(self):
        """极差：最大值与最小值之差"""
        # 标题
        title = Text("① 极差（Range）", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        subtitle = Text("最大值 - 最小值", font=FONT, font_size=FS_BODY, color=GRAY_A)
        subtitle.move_to(UP * 5.1)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 公式
        formula_R = MathTex(r"R = x_{max} - x_{min}", font_size=FS_FORMULA, color=COLOR_FORMULA)
        formula_R.move_to(UP * 4.3)
        self.play(Write(formula_R), run_time=0.7)

        AXIS_A_Y = self.AXIS_A_Y
        AXIS_B_Y = self.AXIS_B_Y

        # ---- 标注 A 的极差 ----
        # 最大最小值点高亮
        dot_A_min = self.make_dot(d2x(3), AXIS_A_Y, YELLOW, radius=0.18)
        dot_A_max = self.make_dot(d2x(7), AXIS_A_Y, YELLOW, radius=0.18)

        label_A_min = MathTex(r"3", font_size=22, color=YELLOW)
        label_A_max = MathTex(r"7", font_size=22, color=YELLOW)
        label_A_min.move_to(np.array([d2x(3), AXIS_A_Y + 0.42, 0]))
        label_A_max.move_to(np.array([d2x(7), AXIS_A_Y + 0.42, 0]))

        self.play(
            FadeIn(dot_A_min, scale=1.5), FadeIn(dot_A_max, scale=1.5),
            FadeIn(label_A_min), FadeIn(label_A_max),
            run_time=0.5
        )

        # 极差线 A
        range_line_A = Line(
            np.array([d2x(3), AXIS_A_Y - 0.35, 0]),
            np.array([d2x(7), AXIS_A_Y - 0.35, 0]),
            color=COLOR_A, stroke_width=3
        )
        brace_A = BraceBetweenPoints(
            np.array([d2x(3), AXIS_A_Y - 0.4, 0]),
            np.array([d2x(7), AXIS_A_Y - 0.4, 0]),
            direction=DOWN, color=COLOR_A
        )
        result_A = Text("R = 4（较小）", font=FONT, font_size=FS_SMALL, color=COLOR_A)
        result_A.next_to(brace_A, DOWN, buff=0.1)

        self.play(Create(brace_A), run_time=0.5)
        self.play(FadeIn(result_A), run_time=0.4)

        # ---- 标注 B 的极差 ----
        dot_B_min = self.make_dot(d2x(1), AXIS_B_Y, YELLOW, radius=0.18)
        dot_B_max = self.make_dot(d2x(9), AXIS_B_Y, YELLOW, radius=0.18)

        label_B_min = MathTex(r"1", font_size=22, color=YELLOW)
        label_B_max = MathTex(r"9", font_size=22, color=YELLOW)
        label_B_min.move_to(np.array([d2x(1), AXIS_B_Y + 0.42, 0]))
        label_B_max.move_to(np.array([d2x(9), AXIS_B_Y + 0.42, 0]))

        self.play(
            FadeIn(dot_B_min, scale=1.5), FadeIn(dot_B_max, scale=1.5),
            FadeIn(label_B_min), FadeIn(label_B_max),
            run_time=0.5
        )

        brace_B = BraceBetweenPoints(
            np.array([d2x(1), AXIS_B_Y - 0.4, 0]),
            np.array([d2x(9), AXIS_B_Y - 0.4, 0]),
            direction=DOWN, color=COLOR_B
        )
        result_B = Text("R = 8（较大）", font=FONT, font_size=FS_SMALL, color=COLOR_B)
        result_B.next_to(brace_B, DOWN, buff=0.1)

        self.play(Create(brace_B), run_time=0.5)
        self.play(FadeIn(result_B), run_time=0.4)

        # 小结
        note = Text("⚠ 极差只考虑两端，忽略中间数据", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        note.move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, subtitle, formula_R,
                dot_A_min, dot_A_max, label_A_min, label_A_max, brace_A, result_A,
                dot_B_min, dot_B_max, label_B_min, label_B_max, brace_B, result_B,
                note
            )),
            run_time=0.5
        )

    # ============================================================
    # Scene 3: 方差
    # ============================================================
    def scene_3_variance(self):
        """方差：各数据与均值差的平方的平均"""
        AXIS_A_Y = self.AXIS_A_Y
        AXIS_B_Y = self.AXIS_B_Y

        # 标题
        title = Text("② 方差（Variance）", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 均值线
        mean_line_A = DashedLine(
            np.array([d2x(5) - 0.02, AXIS_A_Y - 0.5, 0]),
            np.array([d2x(5) - 0.02, AXIS_A_Y + 0.8, 0]),
            color=COLOR_MEAN, dash_length=0.08, stroke_width=2
        )
        mean_line_B = DashedLine(
            np.array([d2x(5) - 0.02, AXIS_B_Y - 0.5, 0]),
            np.array([d2x(5) - 0.02, AXIS_B_Y + 0.8, 0]),
            color=COLOR_MEAN, dash_length=0.08, stroke_width=2
        )
        mean_label_A = MathTex(r"\bar{x}=5", font_size=20, color=COLOR_MEAN)
        mean_label_A.move_to(np.array([d2x(5) + 0.35, AXIS_A_Y + 0.7, 0]))
        mean_label_B = MathTex(r"\bar{x}=5", font_size=20, color=COLOR_MEAN)
        mean_label_B.move_to(np.array([d2x(5) + 0.35, AXIS_B_Y + 0.7, 0]))

        self.play(
            Create(mean_line_A), Create(mean_line_B),
            FadeIn(mean_label_A), FadeIn(mean_label_B),
            run_time=0.7
        )

        # 偏差解释
        dev_explain = Text("每个数据与均值的距离 = 偏差", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        dev_explain.move_to(UP * 4.9)
        self.play(FadeIn(dev_explain), run_time=0.4)

        # 画偏差箭头（数据集A）
        dev_arrows_A = VGroup()
        for xi in self.data_A:
            if abs(xi - self.mean_A) < 0.01:
                continue
            x_start = d2x(self.mean_A)
            x_end = d2x(xi)
            arrow = Arrow(
                np.array([x_start, AXIS_A_Y + 0.25, 0]),
                np.array([x_end, AXIS_A_Y + 0.25, 0]),
                color=COLOR_DEV,
                buff=0,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15
            )
            dev_arrows_A.add(arrow)

        self.play(Create(dev_arrows_A), run_time=0.8)

        # 画偏差箭头（数据集B）
        dev_arrows_B = VGroup()
        for xi in self.data_B:
            if abs(xi - self.mean_B) < 0.01:
                continue
            x_start = d2x(self.mean_B)
            x_end = d2x(xi)
            arrow = Arrow(
                np.array([x_start, AXIS_B_Y + 0.25, 0]),
                np.array([x_end, AXIS_B_Y + 0.25, 0]),
                color=COLOR_DEV,
                buff=0,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.15
            )
            dev_arrows_B.add(arrow)

        self.play(Create(dev_arrows_B), run_time=0.8)
        self.wait(0.5)

        # 为什么平方？
        why_sq = Text("为什么要平方？消除正负号！", font=FONT, font_size=FS_SMALL, color=YELLOW)
        why_sq.move_to(np.array([0, AXIS_B_Y - 0.9, 0]))
        self.play(FadeIn(why_sq, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 清理偏差箭头，引入公式
        self.play(
            FadeOut(dev_arrows_A), FadeOut(dev_arrows_B),
            FadeOut(dev_explain), FadeOut(why_sq),
            run_time=0.4
        )

        # 方差公式（主要公式）
        formula_var = MathTex(
            r"s^2 = \frac{\sum(x_i - \bar{x})^2}{n}",
            font_size=FS_FORMULA,
            color=COLOR_FORMULA
        )
        formula_var.move_to(UP * 4.5)
        self.play(Write(formula_var), run_time=0.9)

        # 计算展示 - 数据集A
        calc_title_A = Text("A组计算：", font=FONT, font_size=FS_SMALL, color=COLOR_A)
        calc_title_A.move_to(np.array([-1.2, AXIS_B_Y - 0.9, 0]))

        calc_A = MathTex(
            r"s^2_A = \frac{(-2)^2+(-1)^2+0^2+1^2+2^2}{5} = \frac{10}{5} = 2",
            font_size=18,
            color=COLOR_A
        )
        calc_A.move_to(np.array([0, AXIS_B_Y - 1.5, 0]))

        self.play(FadeIn(calc_title_A), run_time=0.3)
        self.play(Write(calc_A), run_time=1.0)

        # 计算展示 - 数据集B
        calc_title_B = Text("B组计算：", font=FONT, font_size=FS_SMALL, color=COLOR_B)
        calc_title_B.move_to(np.array([-1.2, AXIS_B_Y - 2.2, 0]))

        calc_B = MathTex(
            r"s^2_B = \frac{(-4)^2+(-3)^2+0^2+3^2+4^2}{5} = \frac{50}{5} = 10",
            font_size=18,
            color=COLOR_B
        )
        calc_B.move_to(np.array([0, AXIS_B_Y - 2.8, 0]))

        self.play(FadeIn(calc_title_B), run_time=0.3)
        self.play(Write(calc_B), run_time=1.0)

        # 结论框
        conclusion = Text("s²越大，数据越分散", font=FONT, font_size=FS_BODY, color=COLOR_HIGHLIGHT)
        conclusion.move_to(np.array([0, -4.8, 0]))
        box = SurroundingRectangle(conclusion, color=COLOR_HIGHLIGHT, buff=0.2, stroke_width=2)
        self.play(FadeIn(conclusion), Create(box), run_time=0.6)
        self.wait(1.5)

        # 等价公式
        self.play(FadeOut(VGroup(calc_A, calc_B, calc_title_A, calc_title_B, conclusion, box)), run_time=0.4)

        alt_title = Text("等价公式（计算更简便）：", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        alt_title.move_to(np.array([0, AXIS_B_Y - 0.9, 0]))

        formula_alt = MathTex(
            r"s^2 = \frac{\sum x_i^2}{n} - \bar{x}^2",
            font_size=FS_FORMULA,
            color=COLOR_FORMULA
        )
        formula_alt.move_to(np.array([0, AXIS_B_Y - 1.7, 0]))

        self.play(FadeIn(alt_title), Write(formula_alt), run_time=0.8)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, formula_var, formula_alt, alt_title,
                mean_line_A, mean_line_B, mean_label_A, mean_label_B
            )),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 标准差
    # ============================================================
    def scene_4_std(self):
        """标准差 = 方差的算术平方根"""
        AXIS_A_Y = self.AXIS_A_Y
        AXIS_B_Y = self.AXIS_B_Y

        # 标题
        title = Text("③ 标准差（Standard Deviation）", font=FONT, font_size=26, color=COLOR_FORMULA)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 公式：标准差 = 开方
        formula_std = MathTex(r"s = \sqrt{s^2}", font_size=FS_FORMULA + 4, color=COLOR_FORMULA)
        formula_std.move_to(UP * 4.9)
        self.play(Write(formula_std), run_time=0.7)

        # 计算结果
        result_title = Text("计算结果：", font=FONT, font_size=FS_BODY, color=WHITE)
        result_title.move_to(UP * 4.0)
        self.play(FadeIn(result_title), run_time=0.4)

        result_A = MathTex(r"s_A = \sqrt{2} \approx 1.41", font_size=FS_FORMULA, color=COLOR_A)
        result_B = MathTex(r"s_B = \sqrt{10} \approx 3.16", font_size=FS_FORMULA, color=COLOR_B)
        result_A.move_to(UP * 3.3)
        result_B.move_to(UP * 2.6)
        self.play(Write(result_A), run_time=0.6)
        self.play(Write(result_B), run_time=0.6)

        # 可视化：用线段展示标准差范围
        mean_x = d2x(self.mean_A)

        # A 组标准差区间
        std_range_A = Line(
            np.array([mean_x - 0.7 * self.std_A, AXIS_A_Y + 0.5, 0]),
            np.array([mean_x + 0.7 * self.std_A, AXIS_A_Y + 0.5, 0]),
            color=COLOR_A, stroke_width=5
        )
        std_range_B = Line(
            np.array([mean_x - 0.7 * self.std_B, AXIS_B_Y + 0.5, 0]),
            np.array([mean_x + 0.7 * self.std_B, AXIS_B_Y + 0.5, 0]),
            color=COLOR_B, stroke_width=5
        )
        std_dot_A = Dot(np.array([mean_x, AXIS_A_Y + 0.5, 0]), color=COLOR_MEAN, radius=0.1)
        std_dot_B = Dot(np.array([mean_x, AXIS_B_Y + 0.5, 0]), color=COLOR_MEAN, radius=0.1)

        self.play(Create(std_range_A), FadeIn(std_dot_A), run_time=0.6)
        self.play(Create(std_range_B), FadeIn(std_dot_B), run_time=0.6)

        # 说明文字
        vis_note = Text("线越短 = 数据越集中", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        vis_note.move_to(UP * 1.8)
        self.play(FadeIn(vis_note), run_time=0.4)
        self.wait(1.0)

        # 变异系数（简介）
        cv_title = Text("补充：变异系数 CV（比较不同单位的数据）", font=FONT, font_size=18, color=GRAY_B)
        cv_title.move_to(np.array([0, AXIS_B_Y - 1.2, 0]))
        cv_formula = MathTex(r"CV = \frac{s}{\bar{x}}", font_size=FS_FORMULA, color=GRAY_B)
        cv_formula.move_to(np.array([0, AXIS_B_Y - 2.0, 0]))

        self.play(FadeIn(cv_title), Write(cv_formula), run_time=0.7)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, formula_std, result_title, result_A, result_B,
                std_range_A, std_range_B, std_dot_A, std_dot_B,
                vis_note, cv_title, cv_formula
            )),
            run_time=0.5
        )

        # 清理数轴
        self.play(
            FadeOut(VGroup(
                self.axis_a, self.axis_b,
                self.lbl_a, self.lbl_b,
                self.dots_A, self.dots_B,
                self.data_text_A, self.data_text_B
            )),
            run_time=0.5
        )

    # ============================================================
    # Scene 5: 公式汇总
    # ============================================================
    def scene_5_summary(self):
        """所有公式汇总展示"""
        # 大标题
        title = Text("公式总结", font=FONT, font_size=FS_TITLE, color=GOLD)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # ——— 极差卡片 ———
        card1_title = Text("极差", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        card1_title.move_to(UP * 5.3)
        card1_formula = MathTex(r"R = x_{max} - x_{min}", font_size=FS_FORMULA, color=WHITE)
        card1_formula.move_to(UP * 4.65)
        card1_desc = Text("反映数据波动范围", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        card1_desc.move_to(UP * 4.05)
        divider1 = Line(np.array([-3.5, 3.6, 0]), np.array([3.5, 3.6, 0]), color=GRAY_D, stroke_width=1)

        self.play(FadeIn(card1_title), Write(card1_formula), FadeIn(card1_desc), run_time=0.7)
        self.play(Create(divider1), run_time=0.3)

        # ——— 方差卡片 ———
        card2_title = Text("方差", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        card2_title.move_to(UP * 3.1)

        card2_f1 = MathTex(r"s^2 = \frac{\sum(x_i-\bar{x})^2}{n}", font_size=FS_FORMULA - 2, color=WHITE)
        card2_f1.move_to(UP * 2.4)

        card2_or = Text("或", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        card2_or.move_to(UP * 1.75)

        card2_f2 = MathTex(r"s^2 = \frac{\sum x_i^2}{n} - \bar{x}^2", font_size=FS_FORMULA - 2, color=WHITE)
        card2_f2.move_to(UP * 1.05)

        card2_desc = Text("s²越小，数据越集中", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        card2_desc.move_to(UP * 0.4)
        divider2 = Line(np.array([-3.5, 0.0, 0]), np.array([3.5, 0.0, 0]), color=GRAY_D, stroke_width=1)

        self.play(FadeIn(card2_title), Write(card2_f1), run_time=0.7)
        self.play(FadeIn(card2_or), Write(card2_f2), run_time=0.6)
        self.play(FadeIn(card2_desc), Create(divider2), run_time=0.4)

        # ——— 标准差卡片 ———
        card3_title = Text("标准差", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        card3_title.move_to(DOWN * 0.6)

        card3_formula = MathTex(r"s = \sqrt{s^2}", font_size=FS_FORMULA + 4, color=WHITE)
        card3_formula.move_to(DOWN * 1.35)

        card3_desc = Text("与数据单位相同，更直观", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        card3_desc.move_to(DOWN * 2.0)
        divider3 = Line(np.array([-3.5, -2.4, 0]), np.array([3.5, -2.4, 0]), color=GRAY_D, stroke_width=1)

        self.play(FadeIn(card3_title), Write(card3_formula), FadeIn(card3_desc), run_time=0.7)
        self.play(Create(divider3), run_time=0.3)

        # ——— 变异系数卡片 ———
        card4_title = Text("变异系数", font=FONT, font_size=FS_SUBTITLE, color=COLOR_FORMULA)
        card4_title.move_to(DOWN * 3.0)

        card4_formula = MathTex(r"CV = \frac{s}{\bar{x}}", font_size=FS_FORMULA, color=WHITE)
        card4_formula.move_to(DOWN * 3.7)

        card4_desc = Text("比较不同量纲数据的离散程度", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        card4_desc.move_to(DOWN * 4.4)

        self.play(FadeIn(card4_title), Write(card4_formula), FadeIn(card4_desc), run_time=0.7)

        # 底部示例对比
        compare = Text("本例: A组(s²=2) 比 B组(s²=10) 更稳定!", font=FONT, font_size=FS_SMALL, color=COLOR_HIGHLIGHT)
        compare.move_to(DOWN * 5.5)
        box = SurroundingRectangle(compare, color=COLOR_HIGHLIGHT, buff=0.15, stroke_width=2)
        self.play(FadeIn(compare), Create(box), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                card1_title, card1_formula, card1_desc, divider1,
                card2_title, card2_f1, card2_or, card2_f2, card2_desc, divider2,
                card3_title, card3_formula, card3_desc, divider3,
                card4_title, card4_formula, card4_desc,
                compare, box
            )),
            run_time=0.6
        )

    # ============================================================
    # Scene 6: 片尾
    # ============================================================
    def scene_6_outro(self):
        """片尾：作者信息 + 关注引导"""
        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=FS_TITLE, color=WHITE
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_SUBTITLE, color=GRAY_B
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_text, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=FS_SUBTITLE, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        follow_box = SurroundingRectangle(follow, color=COLOR_HIGHLIGHT, buff=0.2, stroke_width=22)

        self.play(FadeIn(follow), Create(follow_box), run_time=0.6)

        # 知识点闪卡
        tags = VGroup(
            Text("#极差", font=FONT, font_size=FS_SMALL, color=COLOR_FORMULA),
            Text("#方差", font=FONT, font_size=FS_SMALL, color=COLOR_FORMULA),
            Text("#标准差", font=FONT, font_size=FS_SMALL, color=COLOR_FORMULA),
            Text("#高三统计", font=FONT, font_size=FS_SMALL, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.2)

        self.play(FadeIn(tags, shift=UP * 0.2), run_time=0.5)

        # 装饰动画
        circles = VGroup(*[
            Circle(radius=0.2, color=c, fill_opacity=0.7, stroke_width=0)
            .move_to(DOWN * 3.5 + LEFT * 2 + RIGHT * i * 1.0)
            for i, c in enumerate([COLOR_A, COLOR_FORMULA, COLOR_MEAN, COLOR_B])
        ])
        self.play(*[GrowFromCenter(c) for c in circles], run_time=0.6)
        self.play(Rotate(circles, PI, about_point=DOWN * 3.5), run_time=1.5)

        self.wait(1.0)

        # 全体淡出
        self.play(
            FadeOut(VGroup(
                self.author_text, author_id, follow, follow_box, tags, circles
            )),
            run_time=0.8
        )


# ============================================================
# 渲染命令:
# 快速预览: manim -pql data_dispersion.py DataDispersion
# 高质量:   manim -qh  data_dispersion.py DataDispersion
# ============================================================