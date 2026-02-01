"""
向量的数乘运算 - Vector Scalar Multiplication Animation
使用 Manim 创建的九年级数学教学视频

内容: 向量数乘的定义、λ>0同向、λ<0反向、λ=0零向量、模长公式、分配律与结合律
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


class VectorScalarMult(Scene):
    """
    向量数乘教学动画

    场景顺序:
    1. 开场钩子
    2. 向量数乘是什么
    3. λ>0 同向演示（动态）
    4. λ<0 反向演示（动态）
    5. λ=0 零向量
    6. 模长公式
    7. 分配律与结合律
    8. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.C_PRIMARY = "#e94560"    # 红 - 主向量 a
        self.C_SCALED = "#00d4ff"     # 青 - λa
        self.C_HIGHLIGHT = "#f5c518"  # 金 - 高亮
        self.C_AUX = "#a8a8b3"        # 灰 - 辅助
        self.C_POS = "#2ecc71"        # 绿 - 正
        self.C_NEG = "#e74c3c"        # 红 - 负
        self.C_ZERO = "#95a5a6"       # 灰蓝 - 零

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_positive_lambda()
        self.scene_4_negative_lambda()
        self.scene_5_zero_lambda()
        self.scene_6_magnitude_formula()
        self.scene_7_laws()
        self.scene_8_outro()

    # =========================================================
    # 几何数据初始化（所有坐标精确计算）
    # =========================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # 向量 a 的起点和方向（主区域居中偏上）
        # 缩小方向向量确保 2a 和 -2a 不超出边界 x∈[-4,4]
        # 起点 x=0，2a终点 x = 0 + 2*dir_x ≤ 4 → dir_x ≤ 2.0
        # -2a终点 x = 0 - 2*dir_x ≥ -4 → dir_x ≤ 2.0
        self.vec_origin = np.array([0.0, 0.5, 0])       # 起点
        self.vec_a_dir = np.array([1.9, 0.95, 0])        # 方向向量 (缩小后约 2.12)
        self.vec_a_end = self.vec_origin + self.vec_a_dir  # 终点

        # 各倍数终点（精确计算）
        self.vec_2a_end = self.vec_origin + 2.0 * self.vec_a_dir
        self.vec_half_a_end = self.vec_origin + 0.5 * self.vec_a_dir
        self.vec_neg1_end = self.vec_origin + (-1.0) * self.vec_a_dir
        self.vec_neg2_end = self.vec_origin + (-2.0) * self.vec_a_dir

        # 向量长度缓存
        self.len_a = np.linalg.norm(self.vec_a_dir)

        # 验证
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        eps = 1e-10
        # 验证各倍数长度
        len_2a = np.linalg.norm(self.vec_2a_end - self.vec_origin)
        len_half = np.linalg.norm(self.vec_half_a_end - self.vec_origin)
        len_neg1 = np.linalg.norm(self.vec_neg1_end - self.vec_origin)
        len_neg2 = np.linalg.norm(self.vec_neg2_end - self.vec_origin)

        assert abs(len_2a - 2.0 * self.len_a) < eps, f"2a长度错误: {len_2a}"
        assert abs(len_half - 0.5 * self.len_a) < eps, f"0.5a长度错误: {len_half}"
        assert abs(len_neg1 - 1.0 * self.len_a) < eps, f"-a长度错误: {len_neg1}"
        assert abs(len_neg2 - 2.0 * self.len_a) < eps, f"-2a长度错误: {len_neg2}"

        # 验证反向：点积应为负
        dot_neg = np.dot(self.vec_a_dir, self.vec_neg1_end - self.vec_origin)
        assert dot_neg < 0, "反向验证失败"

        print("✓ 几何验证通过")

    # =========================================================
    # 辅助函数
    # =========================================================
    def make_arrow(self, start, end, color, stroke_width=3, tip_width=0.25):
        """创建向量箭头"""
        return Arrow(
            start, end,
            color=color,
            stroke_width=stroke_width,
            tip_width=tip_width,
            buff=0
        )

    def make_label(self, text, color, font_size=24):
        """创建中文标签"""
        return Text(text, font="Noto Sans CJK SC", font_size=font_size, color=color)

    # =========================================================
    # Scene 1: 开场钩子
    # =========================================================
    def scene_1_opening(self):
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.C_AUX
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "向量乘以一个数,",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.5)
        hook2 = Text(
            "会发生什么?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.C_HIGHLIGHT,
            weight="BOLD"
        ).move_to(UP * 4.7)

        self.play(Write(hook), run_time=0.7)
        self.play(Write(hook2), run_time=0.6)

        # 简单向量示意
        simple_vec = self.make_arrow(
            np.array([-1.5, 1.0, 0]),
            np.array([1.5, 2.5, 0]),
            self.C_PRIMARY, stroke_width=4
        )
        simple_label = MathTex(r"\vec{a}", color=self.C_PRIMARY, font_size=40).move_to(
            np.array([1.8, 2.8, 0])
        )
        # λ标注
        lam_label = MathTex(r"\lambda \vec{a} = ?", color=self.C_SCALED, font_size=36).move_to(
            np.array([0, -0.5, 0])
        )

        self.play(GrowArrow(simple_vec), run_time=0.6)
        self.play(Write(simple_label), run_time=0.3)
        self.wait(0.3)
        self.play(Write(lam_label), run_time=0.6)
        self.wait(1.0)

        # 清理开场元素
        self.play(
            FadeOut(hook), FadeOut(hook2),
            FadeOut(simple_vec), FadeOut(simple_label),
            FadeOut(lam_label),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 什么是数乘
    # =========================================================
    def scene_2_definition(self):
        # 标题
        title = self.make_label("向量的数乘", self.C_HIGHLIGHT, 36).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 定义文字
        def_text = self.make_label(
            "实数 λ 与向量 a 的积，记作 λa",
            self.C_AUX, 22
        ).move_to(UP * 5.0)
        self.play(FadeIn(def_text), run_time=0.5)

        # 展示向量 a
        vec_a = self.make_arrow(self.vec_origin, self.vec_a_end, self.C_PRIMARY, stroke_width=4)
        label_a = MathTex(r"\vec{a}", color=self.C_PRIMARY, font_size=36).move_to(
            self.vec_a_end + np.array([0.15, 0.3, 0])
        )
        origin_dot = Dot(self.vec_origin, radius=0.08, color=WHITE)

        self.play(GrowArrow(vec_a), run_time=0.8)
        self.play(FadeIn(origin_dot), Write(label_a), run_time=0.4)
        self.wait(0.5)

        # 旁注：λ = 2 作为示例
        example_text = self.make_label("例如 λ = 2 时：", self.C_AUX, 22).move_to(
            np.array([-3.2, -1.5, 0])
        )
        self.play(FadeIn(example_text), run_time=0.4)

        # 画 2a
        vec_2a = self.make_arrow(self.vec_origin, self.vec_2a_end, self.C_SCALED, stroke_width=3)
        label_2a = MathTex(r"2\vec{a}", color=self.C_SCALED, font_size=34).move_to(
            self.vec_2a_end + np.array([0.15, 0.3, 0])
        )
        self.play(GrowArrow(vec_2a), run_time=0.8)
        self.play(Write(label_2a), run_time=0.3)

        # 要点标注（底部）
        point1 = self.make_label("方向：与 a 相同 ✓", self.C_POS, 20).move_to(np.array([-1.5, -3.0, 0]))
        point2 = self.make_label("长度：是 a 的 2 倍 ✓", self.C_POS, 20).move_to(np.array([-1.5, -3.6, 0]))

        self.play(FadeIn(point1), run_time=0.4)
        self.play(FadeIn(point2), run_time=0.4)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(example_text),
            FadeOut(vec_a), FadeOut(label_a), FadeOut(origin_dot),
            FadeOut(vec_2a), FadeOut(label_2a),
            FadeOut(point1), FadeOut(point2),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: λ>0 同向演示（动态）
    # =========================================================
    def scene_3_positive_lambda(self):
        # 标题
        title = self.make_label("λ > 0 : 同向伸缩", self.C_POS, 34).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        subtitle = self.make_label("方向不变，长度变为 |λ| 倍", self.C_AUX, 20).move_to(UP * 5.1)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 使用 ValueTracker 做动态演示
        lam = ValueTracker(1.0)

        # 起点
        origin_dot = Dot(self.vec_origin, radius=0.07, color=WHITE)
        self.add(origin_dot)

        # 基础向量 a（灰色参考）
        vec_a_ref = self.make_arrow(
            self.vec_origin, self.vec_a_end, self.C_AUX, stroke_width=2
        )
        vec_a_ref.set_opacity(0.3)
        label_a_ref = MathTex(r"\vec{a}", color=self.C_AUX, font_size=28).move_to(
            self.vec_a_end + np.array([0.15, 0.25, 0])
        )
        label_a_ref.set_opacity(0.4)
        self.add(vec_a_ref, label_a_ref)

        # 动态向量 λa
        def make_dynamic_vec():
            l = lam.get_value()
            end = self.vec_origin + l * self.vec_a_dir
            return Arrow(
                self.vec_origin, end,
                color=self.C_SCALED, stroke_width=3.5, tip_width=0.22, buff=0
            )

        def make_dynamic_label():
            l = lam.get_value()
            end = self.vec_origin + l * self.vec_a_dir
            if abs(l - 1.0) < 0.05:
                tex = MathTex(r"\vec{a}", color=self.C_SCALED, font_size=32)
            elif abs(l - round(l)) < 0.05 and l == round(l):
                tex = MathTex(rf"{int(round(l))}\vec{{a}}", color=self.C_SCALED, font_size=32)
            else:
                tex = MathTex(rf"{l:.1f}\vec{{a}}", color=self.C_SCALED, font_size=32)
            tex.move_to(end + np.array([0.2, 0.3, 0]))
            return tex

        def make_lambda_display():
            l = lam.get_value()
            tex = MathTex(rf"\lambda = {l:.2f}", color=self.C_HIGHLIGHT, font_size=30)
            tex.move_to(np.array([-2.8, -2.0, 0]))
            return tex

        dynamic_vec = always_redraw(make_dynamic_vec)
        dynamic_label = always_redraw(make_dynamic_label)
        lam_display = always_redraw(make_lambda_display)

        self.play(GrowArrow(dynamic_vec), run_time=0.5)
        self.add(dynamic_label, lam_display)
        self.wait(0.5)

        # 演示 λ 从 1 → 2
        self.play(lam.animate.set_value(2.0), run_time=1.5, rate_func=smooth)
        self.wait(0.8)

        # λ = 2 标注
        note_2 = self.make_label("长度翻倍，方向不变 ✓", self.C_POS, 20).move_to(np.array([-1.0, -3.0, 0]))
        self.play(FadeIn(note_2), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(note_2), run_time=0.3)

        # λ 从 2 → 0.5
        self.play(lam.animate.set_value(0.5), run_time=1.8, rate_func=smooth)
        self.wait(0.8)

        note_half = self.make_label("长度缩短为一半，方向不变 ✓", self.C_POS, 20).move_to(np.array([-0.8, -3.0, 0]))
        self.play(FadeIn(note_half), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(note_half), run_time=0.3)

        # λ 回到 1
        self.play(lam.animate.set_value(1.0), run_time=1.0, rate_func=smooth)
        self.wait(0.5)

        # 结论
        conclusion = self.make_label(
            "λ > 0 时，λa 与 a 同向",
            self.C_HIGHLIGHT, 26
        ).move_to(np.array([0, -4.2, 0]))
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.remove(dynamic_vec, dynamic_label, lam_display)
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(vec_a_ref), FadeOut(label_a_ref),
            FadeOut(origin_dot), FadeOut(conclusion),
            run_time=0.5
        )

    # =========================================================
    # Scene 4: λ<0 反向演示（动态）
    # =========================================================
    def scene_4_negative_lambda(self):
        title = self.make_label("λ < 0 : 反向伸缩", self.C_NEG, 34).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        subtitle = self.make_label("方向反转！长度变为 |λ| 倍", self.C_AUX, 20).move_to(UP * 5.1)
        self.play(FadeIn(subtitle), run_time=0.4)

        lam = ValueTracker(1.0)

        origin_dot = Dot(self.vec_origin, radius=0.07, color=WHITE)
        self.add(origin_dot)

        # 基础向量 a（灰色参考）
        vec_a_ref = self.make_arrow(
            self.vec_origin, self.vec_a_end, self.C_AUX, stroke_width=2
        )
        vec_a_ref.set_opacity(0.3)
        label_a_ref = MathTex(r"\vec{a}", color=self.C_AUX, font_size=28).move_to(
            self.vec_a_end + np.array([0.15, 0.25, 0])
        )
        label_a_ref.set_opacity(0.4)
        self.add(vec_a_ref, label_a_ref)

        # 先展示 a 本身
        vec_a_show = self.make_arrow(
            self.vec_origin, self.vec_a_end, self.C_PRIMARY, stroke_width=3.5
        )
        self.play(GrowArrow(vec_a_show), run_time=0.6)
        self.wait(0.4)

        # λ display
        def make_lambda_display():
            l = lam.get_value()
            tex = MathTex(rf"\lambda = {l:.1f}", color=self.C_HIGHLIGHT, font_size=30)
            tex.move_to(np.array([-2.8, -2.0, 0]))
            return tex

        lam_display = always_redraw(make_lambda_display)

        # 动态向量（用于负数）— 添加近零保护
        def make_neg_vec():
            l = lam.get_value()
            end = self.vec_origin + l * self.vec_a_dir
            dist = np.linalg.norm(end - self.vec_origin)
            if dist < 0.08:
                # λ 接近 0 时退化为点，避免 Arrow 起终点重合崩溃
                return Dot(self.vec_origin, radius=0.06, color=self.C_SCALED)
            return Arrow(
                self.vec_origin, end,
                color=self.C_SCALED, stroke_width=3.5, tip_width=0.22, buff=0
            )

        def make_neg_label():
            l = lam.get_value()
            end = self.vec_origin + l * self.vec_a_dir
            dist = np.linalg.norm(end - self.vec_origin)
            if dist < 0.08:
                tex = MathTex(r"\vec{0}", color=self.C_SCALED, font_size=32)
                tex.move_to(self.vec_origin + np.array([0.3, 0.3, 0]))
                return tex
            if abs(l - round(l)) < 0.05:
                li = int(round(l))
                if li == -1:
                    tex = MathTex(r"-\vec{a}", color=self.C_SCALED, font_size=32)
                else:
                    tex = MathTex(rf"{li}\vec{{a}}", color=self.C_SCALED, font_size=32)
            else:
                tex = MathTex(rf"({l:.1f})\vec{{a}}", color=self.C_SCALED, font_size=32)
            # 放在终点附近，负方向需要偏移
            tex.move_to(end + np.array([-0.3, -0.4, 0]))
            return tex

        # λ: 1 → -1
        self.play(lam.animate.set_value(-1.0), run_time=0.01)  # jump instantly
        neg_vec = always_redraw(make_neg_vec)
        neg_label = always_redraw(make_neg_label)

        # 先移除展示用的 a
        self.play(FadeOut(vec_a_show), run_time=0.3)

        # 开始从 λ=1 慢慢变为 -1 的动态演示
        self.play(lam.animate.set_value(1.0), run_time=0.01)
        self.add(neg_vec, neg_label, lam_display)

        # 突变到 -1
        self.play(lam.animate.set_value(-1.0), run_time=1.2, rate_func=smooth)
        self.wait(0.8)

        note_neg1 = self.make_label("方向翻转，长度不变 ✓", self.C_NEG, 20).move_to(np.array([-0.5, -3.0, 0]))
        self.play(FadeIn(note_neg1), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(note_neg1), run_time=0.3)

        # λ: -1 → -2
        self.play(lam.animate.set_value(-2.0), run_time=1.2, rate_func=smooth)
        self.wait(0.8)

        note_neg2 = self.make_label("反向且长度翻倍 ✓", self.C_NEG, 20).move_to(np.array([-0.3, -3.0, 0]))
        self.play(FadeIn(note_neg2), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(note_neg2), run_time=0.3)

        # 结论
        conclusion = self.make_label(
            "λ < 0 时，λa 与 a 反向",
            self.C_HIGHLIGHT, 26
        ).move_to(np.array([0, -4.2, 0]))
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.remove(neg_vec, neg_label, lam_display)
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(vec_a_ref), FadeOut(label_a_ref),
            FadeOut(origin_dot), FadeOut(conclusion),
            run_time=0.5
        )

    # =========================================================
    # Scene 5: λ=0 零向量
    # =========================================================
    def scene_5_zero_lambda(self):
        title = self.make_label("λ = 0 : 零向量", self.C_ZERO, 34).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 展示向量 a
        origin_dot = Dot(self.vec_origin, radius=0.08, color=WHITE)
        vec_a = self.make_arrow(self.vec_origin, self.vec_a_end, self.C_PRIMARY, stroke_width=3.5)
        label_a = MathTex(r"\vec{a}", color=self.C_PRIMARY, font_size=34).move_to(
            self.vec_a_end + np.array([0.15, 0.3, 0])
        )

        self.play(GrowArrow(vec_a), FadeIn(origin_dot), run_time=0.6)
        self.play(Write(label_a), run_time=0.3)
        self.wait(0.5)

        # 0·a = 零向量（只有起点，没有长度和方向）
        zero_label = MathTex(r"0 \cdot \vec{a} = \vec{0}", color=self.C_ZERO, font_size=34).move_to(
            np.array([0, -1.5, 0])
        )
        self.play(Write(zero_label), run_time=0.6)

        # 向量 a 缩短到零的动画
        lam = ValueTracker(1.0)

        def make_shrink_vec():
            l = lam.get_value()
            if l < 0.02:
                return Dot(self.vec_origin, radius=0.08, color=self.C_SCALED)
            end = self.vec_origin + l * self.vec_a_dir
            return Arrow(
                self.vec_origin, end,
                color=self.C_SCALED, stroke_width=3, tip_width=0.2 * l + 0.05, buff=0
            )

        # 先淡出原来的 a
        self.play(FadeOut(vec_a), run_time=0.3)

        shrink_vec = always_redraw(make_shrink_vec)
        self.add(shrink_vec)

        # λ: 1 → 0 缩短
        self.play(lam.animate.set_value(0.0), run_time=1.5, rate_func=smooth)
        self.wait(0.8)

        # 解释
        explain = self.make_label(
            "长度为零 → 没有方向 → 零向量 $\\vec{0}$",
            self.C_AUX, 20
        ).move_to(np.array([0, -3.0, 0]))
        # 用 Text 避免混合中文和 MathTex 问题
        explain_cn = self.make_label("长度为零 → 没有方向 → 零向量", self.C_AUX, 20).move_to(np.array([0, -3.0, 0]))
        self.play(FadeIn(explain_cn), run_time=0.4)
        self.wait(1.0)

        # 清理
        self.remove(shrink_vec)
        self.play(
            FadeOut(title), FadeOut(origin_dot),
            FadeOut(label_a), FadeOut(zero_label),
            FadeOut(explain_cn),
            run_time=0.5
        )

    # =========================================================
    # Scene 6: 模长公式
    # =========================================================
    def scene_6_magnitude_formula(self):
        title = self.make_label("模长公式", self.C_HIGHLIGHT, 34).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 核心公式
        formula = MathTex(
            r"|\lambda \vec{a}| = |\lambda| \cdot |\vec{a}|",
            color=WHITE, font_size=42
        ).move_to(UP * 4.5)
        self.play(Write(formula), run_time=0.8)
        self.wait(0.5)

        # 用框高亮
        box = SurroundingRectangle(formula, color=self.C_HIGHLIGHT, buff=0.25, stroke_width=2)
        self.play(Create(box), run_time=0.4)
        self.wait(0.5)

        # 用图示解释：画向量 a 和 2a，标注模长
        # 向量 a
        origin_a = np.array([-3.0, 1.2, 0])
        end_a = origin_a + np.array([2.0, 0.0, 0])  # 水平向量便于标注长度
        vec_a_show = Arrow(origin_a, end_a, color=self.C_PRIMARY, stroke_width=3, buff=0)
        label_a_show = MathTex(r"\vec{a}", color=self.C_PRIMARY, font_size=28).move_to(
            (origin_a + end_a) / 2 + np.array([0, 0.35, 0])
        )
        len_a_label = MathTex(r"|\vec{a}|", color=self.C_PRIMARY, font_size=22).move_to(
            (origin_a + end_a) / 2 + np.array([0, -0.45, 0])
        )

        self.play(GrowArrow(vec_a_show), run_time=0.5)
        self.play(Write(label_a_show), Write(len_a_label), run_time=0.4)

        # 向量 2a（下面）
        origin_2a = np.array([-3.0, -0.5, 0])
        end_2a = origin_2a + np.array([4.0, 0.0, 0])  # 长度翻倍
        vec_2a_show = Arrow(origin_2a, end_2a, color=self.C_SCALED, stroke_width=3, buff=0)
        label_2a_show = MathTex(r"2\vec{a}", color=self.C_SCALED, font_size=28).move_to(
            (origin_2a + end_2a) / 2 + np.array([0, 0.35, 0])
        )
        len_2a_label = MathTex(r"|2\vec{a}| = 2|\vec{a}|", color=self.C_SCALED, font_size=22).move_to(
            (origin_2a + end_2a) / 2 + np.array([0, -0.45, 0])
        )

        self.play(GrowArrow(vec_2a_show), run_time=0.5)
        self.play(Write(label_2a_show), Write(len_2a_label), run_time=0.4)
        self.wait(0.5)

        # 负数示例：|-2a| = |-2|·|a| = 2|a|
        neg_example = MathTex(
            r"|-2\vec{a}| = |-2| \cdot |\vec{a}| = 2|\vec{a}|",
            color=self.C_NEG, font_size=24
        ).move_to(np.array([0, -2.8, 0]))
        self.play(Write(neg_example), run_time=0.7)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(formula), FadeOut(box),
            FadeOut(vec_a_show), FadeOut(label_a_show), FadeOut(len_a_label),
            FadeOut(vec_2a_show), FadeOut(label_2a_show), FadeOut(len_2a_label),
            FadeOut(neg_example),
            run_time=0.5
        )

    # =========================================================
    # Scene 7: 分配律与结合律
    # =========================================================
    def scene_7_laws(self):
        title = self.make_label("运算律", self.C_HIGHLIGHT, 34).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # --- 分配律 ---
        law1_title = self.make_label("① 分配律", self.C_POS, 26).move_to(UP * 4.8)
        self.play(Write(law1_title), run_time=0.4)

        # 第一个分配律
        dist1 = MathTex(
            r"\lambda(\vec{a} + \vec{b}) = \lambda\vec{a} + \lambda\vec{b}",
            color=WHITE, font_size=32
        ).move_to(UP * 3.9)
        self.play(Write(dist1), run_time=0.7)
        self.wait(0.3)

        # 解释：一个数乘以向量和 = 分别乘再加
        dist1_explain = self.make_label(
            "一个数乘向量之和 = 分别乘后再相加",
            self.C_AUX, 19
        ).move_to(UP * 3.2)
        self.play(FadeIn(dist1_explain), run_time=0.4)
        self.wait(0.5)

        # 第二个分配律
        dist2 = MathTex(
            r"(\lambda + \mu)\vec{a} = \lambda\vec{a} + \mu\vec{a}",
            color=WHITE, font_size=32
        ).move_to(UP * 2.3)
        self.play(Write(dist2), run_time=0.7)
        self.wait(0.3)

        dist2_explain = self.make_label(
            "数之和乘以向量 = 分别乘后再相加",
            self.C_AUX, 19
        ).move_to(UP * 1.6)
        self.play(FadeIn(dist2_explain), run_time=0.4)
        self.wait(0.6)

        # --- 结合律 ---
        law2_title = self.make_label("② 结合律", self.C_POS, 26).move_to(UP * 0.5)
        self.play(Write(law2_title), run_time=0.4)

        assoc = MathTex(
            r"(\lambda\mu)\vec{a} = \lambda(\mu\vec{a})",
            color=WHITE, font_size=32
        ).move_to(np.array([0, -0.4, 0]))
        self.play(Write(assoc), run_time=0.7)
        self.wait(0.3)

        assoc_explain = self.make_label(
            "先乘数再乘向量 = 先乘向量再乘数",
            self.C_AUX, 19
        ).move_to(np.array([0, -1.2, 0]))
        self.play(FadeIn(assoc_explain), run_time=0.4)
        self.wait(0.8)

        # 举例：(2×3)a = 2(3a) = 6a
        example = MathTex(
            r"(2 \times 3)\vec{a} = 2(3\vec{a}) = 6\vec{a}",
            color=self.C_HIGHLIGHT, font_size=26
        ).move_to(np.array([0, -2.3, 0]))
        self.play(Write(example), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(law1_title),
            FadeOut(dist1), FadeOut(dist1_explain),
            FadeOut(dist2), FadeOut(dist2_explain),
            FadeOut(law2_title), FadeOut(assoc), FadeOut(assoc_explain),
            FadeOut(example),
            run_time=0.5
        )

    # =========================================================
    # Scene 8: 片尾
    # =========================================================
    def scene_8_outro(self):
        # 总结卡片
        summary_title = self.make_label("核心知识点总结", self.C_HIGHLIGHT, 30).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.5)

        # 四条要点
        pts = [
            (r"\lambda > 0 \Rightarrow \lambda\vec{a} 与 \vec{a} 同向", self.C_POS),
            (r"\lambda < 0 \Rightarrow \lambda\vec{a} 与 \vec{a} 反向", self.C_NEG),
            (r"\lambda = 0 \Rightarrow \lambda\vec{a} = \vec{0}", self.C_ZERO),
            (r"|\lambda\vec{a}| = |\lambda| \cdot |\vec{a}|", self.C_HIGHLIGHT),
        ]
        # 全部用中文+公式分开写
        y_positions = [4.3, 3.3, 2.3, 1.3]
        pt_objects = []

        for i, (formula_str, color) in enumerate(pts):
            pt = MathTex(formula_str, color=color, font_size=24).move_to(
                np.array([0, y_positions[i], 0])
            )
            self.play(Write(pt), run_time=0.5)
            pt_objects.append(pt)
            self.wait(0.2)

        self.wait(0.8)

        # 清理总结
        self.play(*[FadeOut(p) for p in pt_objects], FadeOut(summary_title), run_time=0.4)

        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_AUX
        ).move_to(UP * 0.2)

        self.play(FadeIn(author_name), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)

        # 关注提示
        follow = self.make_label(
            "关注我，获得更多数学技巧！",
            self.C_HIGHLIGHT, 28
        ).move_to(np.array([0, -0.8, 0]))
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰：小向量箭头闪烁
        decorations = VGroup()
        for i in range(5):
            angle = i * 2 * np.pi / 5
            pos = np.array([1.8 * np.cos(angle), -2.5 + 0.8 * np.sin(angle), 0])
            arrow_dec = Arrow(
                pos, pos + np.array([0.4 * np.cos(angle + 0.5), 0.4 * np.sin(angle + 0.5), 0]),
                color=self.C_HIGHLIGHT, stroke_width=2, tip_width=0.12, buff=0
            )
            decorations.add(arrow_dec)

        self.play(*[FadeIn(d, scale=0.5) for d in decorations], run_time=0.5)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_name), FadeOut(author_id),
            FadeOut(follow), FadeOut(decorations),
            run_time=0.8
        )


# 运行命令:
# manim -pql vector_scalar_mult.py VectorScalarMult  # 快速预览
# manim -qh vector_scalar_mult.py VectorScalarMult   # 高质量渲染