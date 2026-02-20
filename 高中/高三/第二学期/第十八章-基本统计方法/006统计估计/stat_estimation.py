"""
统计估计 - Manim 教学动画
知识点: 点估计、区间估计、无偏性、有效性、一致性
目标受众: 高三学生
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染:
  manim -pql stat_estimation.py StatEstimation   # 快速预览
  manim -qh  stat_estimation.py StatEstimation   # 高质量
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

# ── 颜色 ──────────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
COLOR_POP      = "#a29bfe"   # 紫色 - 总体
COLOR_SAMPLE   = "#00d4ff"   # 青蓝 - 样本
COLOR_ESTIMATE = "#ffd700"   # 金色 - 估计量
COLOR_INTERVAL = "#ff6b6b"   # 红橙 - 区间
COLOR_FORMULA  = "#a8e6cf"   # 浅绿 - 公式
COLOR_MU       = "#fdcb6e"   # 暖橙 - μ 真实参数

FONT = "Noto Sans CJK SC"

# ── 字体大小 ──────────────────────────────────────────────
FS_TITLE   = 40
FS_SUB     = 30
FS_BODY    = 24
FS_SMALL   = 20
FS_TINY    = 17
FS_FORMULA = 28
FS_AUTHOR  = 20

# ── 正态曲线布局 ───────────────────────────────────────────
#   数据范围 x ∈ [-3, 3] → 屏幕 x = data * 1.2
#   PDF 值  → 屏幕 y = CURVE_BASE_Y + pdf * CURVE_AMP
CURVE_BASE_Y = 1.8    # 曲线基线（x 轴）的 y 坐标
CURVE_SCALE  = 1.2    # 数据 → 屏幕 x 缩放
CURVE_AMP    = 5.5    # PDF → 屏幕 y 放大（让曲线可见）

# 演示样本数据（已验证：均值 ≈ 0）
SAMPLE_DATA = np.array([-1.2, -0.4, 0.1, 0.7, 1.4])
X_BAR = float(np.mean(SAMPLE_DATA))   # 0.12

# 多次抽样均值（演示无偏性）
MULTI_MEANS = np.array([-0.8, -0.3, 0.0, 0.2, 0.5, -0.1, 0.4, -0.5, 0.1, 0.3])


# ============================================================
# 数学辅助函数
# ============================================================
def normal_pdf(x, mu=0.0, sigma=1.0):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)


def d2sx(x_data):
    """数据 x → 屏幕逻辑 x"""
    return x_data * CURVE_SCALE


def curve_point(t):
    """正态曲线上 t 处的屏幕坐标"""
    return np.array([d2sx(t), CURVE_BASE_Y + normal_pdf(t) * CURVE_AMP, 0])


# ============================================================
# 主场景
# ============================================================
class StatEstimation(Scene):
    """统计估计教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_data()

        self.scene_1_opening()
        self.scene_2_point_estimation()
        self.scene_3_unbiasedness()
        self.scene_4_interval_estimation()
        self.scene_5_criteria()
        self.scene_6_outro()

    # ──────────────────────────────────────────────────────
    # 数据初始化与验证
    # ──────────────────────────────────────────────────────
    def setup_data(self):
        self.sample = SAMPLE_DATA
        self.x_bar = X_BAR
        self.mu = 0.0
        self.sigma = 1.0
        self.multi_means = MULTI_MEANS

        # 预计算屏幕坐标
        self.sample_sx = [d2sx(xi) for xi in self.sample]
        self.mu_sx = d2sx(self.mu)          # 0.0
        self.xbar_sx = d2sx(self.x_bar)     # 0.144

        assert abs(self.x_bar) < 0.5, "样本均值偏离μ太远"
        print(f"✓ 数据初始化: x̄={self.x_bar:.3f}, μ={self.mu}, xbar_sx={self.xbar_sx:.3f}")

    # ──────────────────────────────────────────────────────
    # 辅助：绘制正态曲线
    # ──────────────────────────────────────────────────────
    def make_normal_curve(self, color=COLOR_POP, stroke_width=2.5):
        """返回正态曲线 ParametricFunction"""
        return ParametricFunction(
            lambda t: curve_point(t),
            t_range=[-3.0, 3.0, 0.02],
            color=color,
            stroke_width=stroke_width
        )

    def make_x_axis(self, color=GRAY_B):
        """绘制 x 轴（水平基线）"""
        line = Line(
            np.array([d2sx(-3.3), CURVE_BASE_Y, 0]),
            np.array([d2sx(3.3), CURVE_BASE_Y, 0]),
            color=color, stroke_width=1.5
        )
        # 刻度标签
        ticks = VGroup()
        for val in [-2, -1, 0, 1, 2]:
            t = Line(
                np.array([d2sx(val), CURVE_BASE_Y - 0.1, 0]),
                np.array([d2sx(val), CURVE_BASE_Y + 0.1, 0]),
                color=color, stroke_width=1.5
            )
            lbl = Text(str(val), font=FONT, font_size=16, color=color)
            lbl.move_to(np.array([d2sx(val), CURVE_BASE_Y - 0.32, 0]))
            ticks.add(t, lbl)
        return VGroup(line, ticks)

    def make_vline(self, x_data, y_bottom, y_top, color, dash=True, width=2):
        """绘制数据 x 处的竖直（虚）线"""
        sx = d2sx(x_data)
        if dash:
            return DashedLine(
                np.array([sx, y_bottom, 0]),
                np.array([sx, y_top, 0]),
                color=color, dash_length=0.12, stroke_width=width
            )
        return Line(
            np.array([sx, y_bottom, 0]),
            np.array([sx, y_top, 0]),
            color=color, stroke_width=width
        )

    def make_confidence_area(self, x_left, x_right, color=COLOR_INTERVAL, opacity=0.3):
        """生成置信区间填充多边形"""
        pts = []
        t_vals = np.linspace(x_left, x_right, 80)
        for t in t_vals:
            pts.append(curve_point(t))
        # 底部封口
        pts.append(np.array([d2sx(x_right), CURVE_BASE_Y, 0]))
        pts.append(np.array([d2sx(x_left), CURVE_BASE_Y, 0]))
        poly = Polygon(*pts, fill_color=color, fill_opacity=opacity,
                       stroke_width=0)
        return poly

    # ──────────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ──────────────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=FS_AUTHOR, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.15), run_time=0.4)

        # 大标题
        title = Text("用样本估计总体", font=FONT, font_size=FS_TITLE, color=GOLD)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.7)

        # 钩子问题
        hook1 = Text("全国 14 亿人，", font=FONT, font_size=FS_BODY, color=WHITE)
        hook2 = Text("抽 1000 人能代表所有人吗？", font=FONT, font_size=FS_SUB, color=COLOR_ESTIMATE)
        hook1.move_to(UP * 5.3)
        hook2.move_to(UP * 4.6)
        self.play(FadeIn(hook1), run_time=0.4)
        self.play(FadeIn(hook2, scale=1.05), run_time=0.5)

        # 视觉：大量总体点云
        np.random.seed(42)
        pop_dots = VGroup()
        for _ in range(120):
            x = np.random.uniform(-3.8, 3.8)
            y = np.random.uniform(-0.8, 3.5)
            d = Dot(np.array([x, y, 0]), radius=0.04, color=COLOR_POP, fill_opacity=0.4)
            pop_dots.add(d)

        self.play(FadeIn(pop_dots, lag_ratio=0.01), run_time=0.9)

        # 样本：从中圈选几个
        sample_circle = Circle(radius=1.0, color=COLOR_SAMPLE, stroke_width=2)
        sample_circle.move_to(np.array([0.5, 1.0, 0]))
        sample_label = Text("样本", font=FONT, font_size=FS_SMALL, color=COLOR_SAMPLE)
        sample_label.next_to(sample_circle, RIGHT, buff=0.15)

        self.play(Create(sample_circle), FadeIn(sample_label), run_time=0.7)

        # 箭头：样本 → 总体
        arrow = Arrow(
            np.array([0.5, 2.15, 0]),
            np.array([0.5, 3.3, 0]),
            color=COLOR_ESTIMATE,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        est_label = Text("估计", font=FONT, font_size=FS_SMALL, color=COLOR_ESTIMATE)
        est_label.next_to(arrow, RIGHT, buff=0.1)

        pop_label = Text("总体", font=FONT, font_size=FS_SMALL, color=COLOR_POP)
        pop_label.move_to(np.array([-2.8, 3.3, 0]))

        self.play(Create(arrow), FadeIn(est_label), FadeIn(pop_label), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(VGroup(title, hook1, hook2, pop_dots, sample_circle,
                           sample_label, arrow, est_label, pop_label)),
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────
    # Scene 2: 点估计
    # ──────────────────────────────────────────────────────
    def scene_2_point_estimation(self):
        # ── 标题 ──
        title = Text("① 点估计", font=FONT, font_size=FS_SUB, color=COLOR_FORMULA)
        title.move_to(UP * 6.8)
        subtitle = Text("用样本统计量直接估计总体参数", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        subtitle.move_to(UP * 6.15)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # ── x 轴 + 正态曲线 ──
        axis = self.make_x_axis()
        curve = self.make_normal_curve()
        self.play(Create(axis), run_time=0.5)
        self.play(Create(curve), run_time=1.0)

        # 总体标注
        pop_lbl = Text("总体分布", font=FONT, font_size=FS_SMALL, color=COLOR_POP)
        pop_lbl.move_to(np.array([-2.5, CURVE_BASE_Y + normal_pdf(-2.0) * CURVE_AMP + 0.35, 0]))
        self.play(FadeIn(pop_lbl), run_time=0.4)

        # ── μ 真实参数线 ──
        mu_peak_y = CURVE_BASE_Y + normal_pdf(0) * CURVE_AMP
        mu_line = self.make_vline(self.mu, CURVE_BASE_Y - 0.1, mu_peak_y + 0.45,
                                  COLOR_MU, dash=True, width=2)
        mu_lbl = MathTex(r"\mu = 0", font_size=FS_FORMULA - 2, color=COLOR_MU)
        mu_lbl.move_to(np.array([self.mu_sx + 0.55, mu_peak_y + 0.55, 0]))
        mu_note = Text("（真实参数，未知）", font=FONT, font_size=FS_TINY, color=GRAY_B)
        mu_note.move_to(np.array([self.mu_sx + 0.6, mu_peak_y + 0.1, 0]))

        self.play(Create(mu_line), FadeIn(mu_lbl), run_time=0.6)
        self.play(FadeIn(mu_note), run_time=0.4)

        # ── 样本点逐个出现 ──
        sample_y = CURVE_BASE_Y - 0.55
        sample_dots = VGroup()
        for sx in self.sample_sx:
            d = Dot(np.array([sx, sample_y, 0]), radius=0.13, color=COLOR_SAMPLE)
            sample_dots.add(d)

        sample_row_lbl = Text("5 个样本数据", font=FONT, font_size=FS_TINY, color=COLOR_SAMPLE)
        sample_row_lbl.move_to(np.array([-2.5, sample_y, 0]))

        self.play(FadeIn(sample_row_lbl), run_time=0.3)
        for d in sample_dots:
            self.play(FadeIn(d, scale=0.5), run_time=0.2)

        # ── x̄ 估计量线 ──
        xbar_line = self.make_vline(self.x_bar, CURVE_BASE_Y - 0.75,
                                    CURVE_BASE_Y + 0.5, COLOR_ESTIMATE, dash=False, width=2.5)
        xbar_lbl = MathTex(r"\bar{x} = 0.12", font_size=FS_FORMULA - 2, color=COLOR_ESTIMATE)
        xbar_lbl.move_to(np.array([self.xbar_sx - 0.9, CURVE_BASE_Y + 0.65, 0]))
        xbar_note = Text("（估计值）", font=FONT, font_size=FS_TINY, color=COLOR_ESTIMATE)
        xbar_note.move_to(np.array([self.xbar_sx - 0.7, CURVE_BASE_Y + 0.22, 0]))

        self.play(Create(xbar_line), FadeIn(xbar_lbl), FadeIn(xbar_note), run_time=0.7)

        # ── 近似箭头: x̄ ≈ μ ──
        approx_arrow = CurvedArrow(
            np.array([self.xbar_sx, CURVE_BASE_Y - 0.9, 0]),
            np.array([self.mu_sx, CURVE_BASE_Y - 0.9, 0]),
            color=YELLOW,
            angle=-TAU / 8,
            stroke_width=2.5
        )
        approx_lbl = MathTex(r"\bar{x} \approx \mu", font_size=FS_FORMULA, color=YELLOW)
        approx_lbl.move_to(np.array([self.xbar_sx / 2 - 0.1, CURVE_BASE_Y - 1.45, 0]))

        self.play(Create(approx_arrow), Write(approx_lbl), run_time=0.8)

        # ── 关键公式 ──
        formula_row = VGroup(
            Text("点估计：", font=FONT, font_size=FS_SMALL, color=WHITE),
            MathTex(r"\bar{x} \rightarrow \mu", font_size=FS_FORMULA, color=COLOR_ESTIMATE),
            Text("，", font=FONT, font_size=FS_SMALL, color=WHITE),
            MathTex(r"s^2 \rightarrow \sigma^2", font_size=FS_FORMULA, color=COLOR_ESTIMATE),
        ).arrange(RIGHT, buff=0.15)
        formula_row.move_to(np.array([0, CURVE_BASE_Y - 2.2, 0]))

        self.play(FadeIn(formula_row), run_time=0.7)
        self.wait(1.8)

        # 保留 axis + curve + μ线 用于下一场景
        self.curve_objs = VGroup(axis, curve, pop_lbl)
        self.mu_objs = VGroup(mu_line, mu_lbl, mu_note)
        self.sample_objs = VGroup(sample_dots, sample_row_lbl)
        self.xbar_objs = VGroup(xbar_line, xbar_lbl, xbar_note)

        self.play(
            FadeOut(VGroup(title, subtitle, approx_arrow, approx_lbl, formula_row)),
            run_time=0.4
        )

    # ──────────────────────────────────────────────────────
    # Scene 3: 无偏性
    # ──────────────────────────────────────────────────────
    def scene_3_unbiasedness(self):
        # ── 标题 ──
        title = Text("② 无偏性", font=FONT, font_size=FS_SUB, color=COLOR_FORMULA)
        title.move_to(UP * 6.8)
        subtitle = Text("多次抽样，x̄ 的期望等于 μ", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        subtitle.move_to(UP * 6.15)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 淡出当前样本和 x̄，保留曲线与 μ 线
        self.play(FadeOut(VGroup(self.sample_objs, self.xbar_objs)), run_time=0.4)

        # ── 快速显示 10 个不同的 x̄ ──
        multi_mean_y = CURVE_BASE_Y - 0.6
        mean_dots = VGroup()
        mean_lbls = VGroup()

        for i, xm in enumerate(self.multi_means):
            sx = d2sx(xm)
            col = interpolate_color(COLOR_SAMPLE, COLOR_INTERVAL, i / len(self.multi_means))
            d = Dot(np.array([sx, multi_mean_y, 0]), radius=0.10, color=col)
            mean_dots.add(d)

        self.play(FadeIn(mean_dots, lag_ratio=0.08), run_time=1.2)

        # 标注：这些都是不同抽样的 x̄
        hint = Text("10 次不同抽样的 x̄", font=FONT, font_size=FS_TINY, color=GRAY_A)
        hint.move_to(np.array([0, multi_mean_y - 0.45, 0]))
        self.play(FadeIn(hint), run_time=0.4)

        # 计算这 10 个 x̄ 的均值
        grand_mean_x = d2sx(np.mean(self.multi_means))  # ≈ d2sx(0) = 0
        grand_dot = Dot(np.array([grand_mean_x, multi_mean_y, 0]),
                        radius=0.18, color=YELLOW)
        grand_lbl = Text("均值 ≈ 0 = μ", font=FONT, font_size=FS_SMALL, color=YELLOW)
        grand_lbl.move_to(np.array([grand_mean_x + 1.5, multi_mean_y - 0.05, 0]))

        self.play(Flash(grand_dot, color=YELLOW, flash_radius=0.4),
                  FadeIn(grand_dot), run_time=0.6)
        self.play(FadeIn(grand_lbl), run_time=0.4)

        # ── 核心公式 E(x̄) = μ ──
        formula_unbiased = MathTex(r"E(\bar{x}) = \mu", font_size=FS_FORMULA + 4, color=COLOR_FORMULA)
        formula_unbiased.move_to(np.array([0, CURVE_BASE_Y - 2.0, 0]))
        self.play(Write(formula_unbiased), run_time=0.8)

        explain = Text("x̄ 是 μ 的无偏估计", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        explain.move_to(np.array([0, CURVE_BASE_Y - 2.7, 0]))
        self.play(FadeIn(explain), run_time=0.4)

        # s² 无偏估计
        formula_s2 = MathTex(r"E(s^2) = \sigma^2", font_size=FS_FORMULA, color=COLOR_FORMULA)
        formula_s2.move_to(np.array([0, CURVE_BASE_Y - 3.4, 0]))
        note_s2 = Text("(注：需用 n-1 除，才是无偏的)", font=FONT, font_size=FS_TINY, color=GRAY_B)
        note_s2.move_to(np.array([0, CURVE_BASE_Y - 4.0, 0]))
        self.play(Write(formula_s2), run_time=0.6)
        self.play(FadeIn(note_s2), run_time=0.4)
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, subtitle,
                mean_dots, hint, grand_dot, grand_lbl,
                formula_unbiased, explain, formula_s2, note_s2
            )),
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────
    # Scene 4: 区间估计
    # ──────────────────────────────────────────────────────
    def scene_4_interval_estimation(self):
        # ── 标题 ──
        title = Text("③ 区间估计", font=FONT, font_size=FS_SUB, color=COLOR_FORMULA)
        title.move_to(UP * 6.8)
        subtitle = Text("给出参数可能所在的范围", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        subtitle.move_to(UP * 6.15)
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 重新显示样本均值线
        xbar_line = self.make_vline(self.x_bar, CURVE_BASE_Y - 0.1,
                                    CURVE_BASE_Y + 0.8, COLOR_ESTIMATE, dash=False, width=2.5)
        xbar_lbl = MathTex(r"\bar{x}", font_size=FS_FORMULA, color=COLOR_ESTIMATE)
        xbar_lbl.move_to(np.array([self.xbar_sx + 0.3, CURVE_BASE_Y + 0.95, 0]))
        self.play(Create(xbar_line), FadeIn(xbar_lbl), run_time=0.5)

        # ── 区间向两侧展开动画 ──
        EPSILON = 1.0
        left_val  = self.x_bar - EPSILON   # -0.88
        right_val = self.x_bar + EPSILON   # 1.12

        # 双向箭头展开
        interval_y = CURVE_BASE_Y - 0.38
        arrow_right = Arrow(
            np.array([self.xbar_sx, interval_y, 0]),
            np.array([d2sx(right_val), interval_y, 0]),
            color=COLOR_INTERVAL, buff=0,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )
        arrow_left = Arrow(
            np.array([self.xbar_sx, interval_y, 0]),
            np.array([d2sx(left_val), interval_y, 0]),
            color=COLOR_INTERVAL, buff=0,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.18
        )

        self.play(Create(arrow_right), Create(arrow_left), run_time=0.8)

        # ε 标注
        eps_right = MathTex(r"\varepsilon", font_size=22, color=COLOR_INTERVAL)
        eps_left  = MathTex(r"\varepsilon", font_size=22, color=COLOR_INTERVAL)
        eps_right.move_to(np.array([(self.xbar_sx + d2sx(right_val)) / 2, interval_y + 0.28, 0]))
        eps_left.move_to(np.array([(self.xbar_sx + d2sx(left_val)) / 2, interval_y + 0.28, 0]))
        self.play(FadeIn(eps_right), FadeIn(eps_left), run_time=0.4)

        # ── 填充置信区间阴影 ──
        area = self.make_confidence_area(left_val, right_val, COLOR_INTERVAL, opacity=0.28)
        self.play(FadeIn(area), run_time=0.8)

        # 边界线
        left_bound = self.make_vline(left_val, CURVE_BASE_Y - 0.55,
                                     CURVE_BASE_Y + 0.4, COLOR_INTERVAL, dash=True, width=1.5)
        right_bound = self.make_vline(right_val, CURVE_BASE_Y - 0.55,
                                      CURVE_BASE_Y + 0.4, COLOR_INTERVAL, dash=True, width=1.5)
        self.play(Create(left_bound), Create(right_bound), run_time=0.5)

        # ── 区间公式 ──
        formula_interval = MathTex(
            r"(\bar{x} - \varepsilon,\ \bar{x} + \varepsilon)",
            font_size=FS_FORMULA, color=COLOR_INTERVAL
        )
        formula_interval.move_to(np.array([0, CURVE_BASE_Y - 1.3, 0]))
        self.play(Write(formula_interval), run_time=0.7)

        # ── 置信度说明 ──
        conf_note1 = Text("置信度越高 → 区间越宽（更保守）", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        conf_note2 = Text("区间越窄 → 估计越精确（更大样本）", font=FONT, font_size=FS_SMALL, color=GRAY_A)
        conf_note1.move_to(np.array([0, CURVE_BASE_Y - 2.1, 0]))
        conf_note2.move_to(np.array([0, CURVE_BASE_Y - 2.7, 0]))
        self.play(FadeIn(conf_note1), run_time=0.4)
        self.play(FadeIn(conf_note2), run_time=0.4)

        # 频率解释
        freq_note = Text("含 μ 的频率 ≈ 置信度（如 95%）", font=FONT, font_size=FS_TINY, color=GRAY_B)
        freq_note.move_to(np.array([0, CURVE_BASE_Y - 3.3, 0]))
        self.play(FadeIn(freq_note), run_time=0.4)
        self.wait(2.0)

        # 清理（保留曲线和μ线）
        self.play(
            FadeOut(VGroup(
                title, subtitle,
                xbar_line, xbar_lbl,
                arrow_right, arrow_left, eps_right, eps_left,
                area, left_bound, right_bound,
                formula_interval, conf_note1, conf_note2, freq_note
            )),
            run_time=0.5
        )

        # 清理曲线和 μ 线
        self.play(
            FadeOut(VGroup(self.curve_objs, self.mu_objs)),
            run_time=0.4
        )

    # ──────────────────────────────────────────────────────
    # Scene 5: 估计量三个评价标准
    # ──────────────────────────────────────────────────────
    def scene_5_criteria(self):
        # 大标题
        title = Text("估计量的评价标准", font=FONT, font_size=FS_SUB, color=GOLD)
        title.move_to(UP * 6.8)
        self.play(Write(title), run_time=0.6)

        divider = Line(np.array([-3.5, 6.35, 0]), np.array([3.5, 6.35, 0]),
                       color=GRAY_D, stroke_width=1)
        self.play(Create(divider), run_time=0.3)

        # ── 评价标准 1：无偏性 ──
        def make_criterion_card(num_str, name_str, formula_str, desc_str, y_center):
            num  = Text(num_str, font=FONT, font_size=FS_TITLE, color=GOLD)
            name = Text(name_str, font=FONT, font_size=FS_SUB, color=COLOR_FORMULA)
            fml  = MathTex(formula_str, font_size=FS_FORMULA, color=WHITE)
            desc = Text(desc_str, font=FONT, font_size=FS_TINY, color=GRAY_A)

            num.move_to(np.array([-3.2, y_center + 0.2, 0]))
            name.move_to(np.array([0.5, y_center + 0.5, 0]))
            fml.move_to(np.array([0.5, y_center - 0.15, 0]))
            desc.move_to(np.array([0.5, y_center - 0.7, 0]))
            return VGroup(num, name, fml, desc)

        card1 = make_criterion_card(
            "①", "无偏性",
            r"E(\hat{\theta}) = \theta",
            "期望等于真实参数",
            4.5
        )
        self.play(FadeIn(card1, shift=RIGHT * 0.3), run_time=0.6)

        div1 = Line(np.array([-3.5, 3.5, 0]), np.array([3.5, 3.5, 0]),
                    color=GRAY_D, stroke_width=1)
        self.play(Create(div1), run_time=0.2)

        card2 = make_criterion_card(
            "②", "有效性",
            r"D(\hat{\theta}_1) < D(\hat{\theta}_2)",
            "方差更小 = 估计更精确",
            2.5
        )
        self.play(FadeIn(card2, shift=RIGHT * 0.3), run_time=0.6)

        div2 = Line(np.array([-3.5, 1.5, 0]), np.array([3.5, 1.5, 0]),
                    color=GRAY_D, stroke_width=1)
        self.play(Create(div2), run_time=0.2)

        card3 = make_criterion_card(
            "③", "一致性",
            r"\hat{\theta} \xrightarrow{n \to \infty} \theta",
            "样本量越大，估计越准",
            0.5
        )
        self.play(FadeIn(card3, shift=RIGHT * 0.3), run_time=0.6)

        # ── 横向对比记忆提示 ──
        div3 = Line(np.array([-3.5, -0.5, 0]), np.array([3.5, -0.5, 0]),
                    color=GRAY_D, stroke_width=1)
        self.play(Create(div3), run_time=0.2)

        memory_title = Text("记忆口诀：", font=FONT, font_size=FS_SMALL, color=COLOR_ESTIMATE)
        memory_title.move_to(np.array([0, -1.1, 0]))
        memory_text = Text("准（无偏）  稳（有效）  随量增精（一致）",
                           font=FONT, font_size=FS_SMALL, color=WHITE)
        memory_text.move_to(np.array([0, -1.75, 0]))
        self.play(FadeIn(memory_title), FadeIn(memory_text), run_time=0.6)

        # ── 点估计/区间估计对比框 ──
        compare = VGroup(
            Text("点估计", font=FONT, font_size=FS_SMALL, color=COLOR_ESTIMATE),
            Text("单一数值，操作简单", font=FONT, font_size=FS_TINY, color=GRAY_B),
        ).arrange(DOWN, buff=0.1)
        compare_box = SurroundingRectangle(compare, color=COLOR_ESTIMATE, buff=0.2, stroke_width=1.5)
        compare.move_to(np.array([-1.5, -3.1, 0]))
        compare_box.move_to(np.array([-1.5, -3.1, 0]))

        compare2 = VGroup(
            Text("区间估计", font=FONT, font_size=FS_SMALL, color=COLOR_INTERVAL),
            Text("范围 + 置信度，更可靠", font=FONT, font_size=FS_TINY, color=GRAY_B),
        ).arrange(DOWN, buff=0.1)
        compare2_box = SurroundingRectangle(compare2, color=COLOR_INTERVAL, buff=0.2, stroke_width=1.5)
        compare2.move_to(np.array([1.7, -3.1, 0]))
        compare2_box.move_to(np.array([1.7, -3.1, 0]))

        self.play(
            FadeIn(compare), Create(compare_box),
            FadeIn(compare2), Create(compare2_box),
            run_time=0.7
        )
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, divider,
                card1, div1, card2, div2, card3, div3,
                memory_title, memory_text,
                compare, compare_box, compare2, compare2_box
            )),
            run_time=0.6
        )

    # ──────────────────────────────────────────────────────
    # Scene 6: 片尾
    # ──────────────────────────────────────────────────────
    def scene_6_outro(self):
        # 作者放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=FS_TITLE, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=FS_SUB, color=GRAY_B
        ).move_to(UP * 1.1)

        self.play(Transform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.15), run_time=0.4)

        # 关注引导
        follow = Text("关注我，获得更多统计技巧！",
                      font=FONT, font_size=FS_SUB, color=COLOR_ESTIMATE)
        follow.move_to(DOWN * 0.2)
        follow_box = SurroundingRectangle(follow, color=COLOR_ESTIMATE, buff=0.2, stroke_width=1.5)
        self.play(FadeIn(follow), Create(follow_box), run_time=0.6)

        # 知识点标签
        tags = VGroup(
            Text("#点估计", font=FONT, font_size=FS_TINY, color=COLOR_FORMULA),
            Text("#区间估计", font=FONT, font_size=FS_TINY, color=COLOR_FORMULA),
            Text("#无偏性", font=FONT, font_size=FS_TINY, color=COLOR_FORMULA),
            Text("#高三统计", font=FONT, font_size=FS_TINY, color=COLOR_FORMULA),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 1.6)
        self.play(FadeIn(tags, shift=UP * 0.2), run_time=0.5)

        # 三个动态圆（代表3个评价标准）
        circles = VGroup(
            Circle(radius=0.22, color=COLOR_FORMULA, fill_opacity=0.7, stroke_width=0)
                .move_to(DOWN * 3.0 + LEFT * 1.3),
            Circle(radius=0.22, color=COLOR_ESTIMATE, fill_opacity=0.7, stroke_width=0)
                .move_to(DOWN * 3.0),
            Circle(radius=0.22, color=COLOR_INTERVAL, fill_opacity=0.7, stroke_width=0)
                .move_to(DOWN * 3.0 + RIGHT * 1.3),
        )
        clabels = VGroup(
            Text("无偏", font=FONT, font_size=14, color=WHITE).move_to(circles[0].get_center()),
            Text("有效", font=FONT, font_size=14, color=WHITE).move_to(circles[1].get_center()),
            Text("一致", font=FONT, font_size=14, color=WHITE).move_to(circles[2].get_center()),
        )
        self.play(
            *[GrowFromCenter(c) for c in circles],
            run_time=0.6
        )
        self.play(FadeIn(clabels), run_time=0.3)
        self.play(Rotate(circles, PI * 0.5, about_point=DOWN * 3.0), run_time=1.2)

        self.wait(1.0)
        self.play(
            FadeOut(VGroup(self.author, author_id, follow, follow_box,
                           tags, circles, clabels)),
            run_time=0.8
        )
