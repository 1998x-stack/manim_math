"""
003_体积与体积单位.py — 体积与体积单位 教学动画

知识点: 体积的概念与体积单位
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 体积的定义: 物体所占空间的大小
  2. 体积单位: cm³, dm³, m³
  3. 单位体积的表象: 1cm³ ≈ 骰子, 1dm³ ≈ 粉笔盒, 1m³ ≈ 洗衣机
  4. 体积(三维) vs 面积(二维) vs 长度(一维)
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR     = "#1a1a2e"
COLOR_CM     = "#3b82f6"    # 蓝色 cm³
COLOR_DM     = "#22c55e"    # 绿色 dm³
COLOR_M      = "#ef4444"    # 红色 m³
COLOR_EDGE   = "#f59e0b"    # 橙色 棱/标注
COLOR_HL     = "#fbbf24"    # 黄色 高亮
COLOR_DIM    = "#a78bfa"    # 紫色 维度对比
COLOR_SPACE  = "#38bdf8"    # 天蓝色 空间概念
COLOR_AUTHOR = "#6b7280"    # 灰色 作者
FONT         = "Noto Sans CJK SC"


# ======================================================================
# 辅助: 2D 等轴测正方体
# ======================================================================

def cube_2d(a, color, fill_opacity=0.25, stroke_width=2.5):
    """
    用三个平行四边形模拟等轴测正方体 (2D).
    a = 棱长, 返回 VGroup(front, top, side)
    """
    dx = np.array([1.0, 0.0, 0.0])
    dy = np.array([0.5, 0.35, 0.0])
    dz = np.array([0.0, 1.0, 0.0])

    O = ORIGIN
    A = O + a * dx
    B = O + a * dx + a * dy
    C = O + a * dy

    front = Polygon(
        O, A, A + a * dz, O + a * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity, stroke_width=stroke_width
    )
    top = Polygon(
        O + a * dz, A + a * dz, B + a * dz, C + a * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity * 0.6, stroke_width=stroke_width
    )
    side = Polygon(
        A, B, B + a * dz, A + a * dz,
        color=color, fill_color=color,
        fill_opacity=fill_opacity * 0.8, stroke_width=stroke_width
    )
    return VGroup(front, top, side)


# ======================================================================
# 主场景
# ======================================================================

class VolumeUnitLesson(Scene):
    """
    体积与体积单位教学动画
    Scene 1: 开场钩子 — "空间有多大？"
    Scene 2: 体积概念 — 物体所占空间的大小
    Scene 3: 体积单位 — cm³, dm³, m³ 及生活类比
    Scene 4: 维度对比 — 长度(一维) vs 面积(二维) vs 体积(三维)
    Scene 5: 知识总结
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_volume_concept()
        self.scene_3_volume_units()
        self.scene_4_dimension_comparison()
        self.scene_5_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '体积与体积单位 — 空间有多大？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "体积与体积单位", font=FONT, font_size=48,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "空间有多大？", font=FONT, font_size=52,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.2)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 三个不同大小的正方体, 暗示体积大小不同
        small_cube = cube_2d(0.6, COLOR_CM, fill_opacity=0.35, stroke_width=2)
        small_cube.move_to(LEFT * 2.5 + DOWN * 0.5)
        mid_cube = cube_2d(1.2, COLOR_DM, fill_opacity=0.30, stroke_width=2)
        mid_cube.move_to(ORIGIN + DOWN * 0.2)
        big_cube = cube_2d(1.8, COLOR_M, fill_opacity=0.25, stroke_width=2)
        big_cube.move_to(RIGHT * 2.0 + UP * 0.2)

        self.play(Create(small_cube), run_time=0.6)
        self.play(Create(mid_cube), run_time=0.6)
        self.play(Create(big_cube), run_time=0.6)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 3.0)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子
        self.play(
            FadeOut(VGroup(hook1, hook2, q, small_cube, mid_cube, big_cube)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 体积概念
    # ------------------------------------------------------------------

    def scene_2_volume_concept(self):
        """体积 = 物体所占空间的大小"""

        title = Text(
            "什么是体积？", font=FONT, font_size=38,
            color=COLOR_SPACE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义
        defn_box = RoundedRectangle(
            width=8.0, height=1.8,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_SPACE, stroke_width=3
        ).move_to(UP * 3.5)

        defn_text = Text(
            "物体所占空间的大小叫做体积",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.5)

        self.play(FadeIn(defn_box), run_time=0.3)
        self.play(Write(defn_text), run_time=0.8)
        self.wait(0.5)

        # 举例: 西瓜 vs 苹果
        example_title = Text(
            "谁占的空间大？", font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 1.8)
        self.play(Write(example_title), run_time=0.5)

        # 用圆近似水果
        watermelon = Circle(
            radius=1.2, color="#22c55e", fill_color="#22c55e",
            fill_opacity=0.4, stroke_width=3
        ).move_to(LEFT * 2.0 + DOWN * 0.3)
        wm_label = Text(
            "西瓜", font=FONT, font_size=22, color="#22c55e"
        ).next_to(watermelon, DOWN, buff=0.2)

        apple = Circle(
            radius=0.5, color="#ef4444", fill_color="#ef4444",
            fill_opacity=0.4, stroke_width=3
        ).move_to(RIGHT * 2.0 + DOWN * 0.3)
        ap_label = Text(
            "苹果", font=FONT, font_size=22, color="#ef4444"
        ).next_to(apple, DOWN, buff=0.2)

        self.play(
            Create(watermelon), FadeIn(wm_label),
            run_time=0.6
        )
        self.play(
            Create(apple), FadeIn(ap_label),
            run_time=0.6
        )
        self.wait(0.3)

        # 对比结论
        compare = Text(
            "西瓜占的空间大 → 体积大",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(
            Indicate(watermelon, color="#22c55e", scale_factor=1.1),
            FadeIn(compare, shift=UP * 0.2),
            run_time=0.7
        )
        self.wait(0.5)

        # 关键理解
        key_point = Text(
            "体积描述的是三维空间的大小",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 3.8)
        three_d = Text(
            "长 + 宽 + 高 → 三个维度",
            font=FONT, font_size=22, color=COLOR_EDGE
        ).move_to(DOWN * 4.6)
        self.play(Write(key_point), run_time=0.6)
        self.play(FadeIn(three_d, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, defn_box, defn_text, example_title,
                watermelon, wm_label, apple, ap_label,
                compare, key_point, three_d
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 体积单位 cm³, dm³, m³
    # ------------------------------------------------------------------

    def scene_3_volume_units(self):
        """三个体积单位及生活类比"""

        title = Text(
            "体积单位", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        intro = Text(
            "计量体积需要统一单位",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.3)
        self.play(Write(intro), run_time=0.5)
        self.wait(0.3)

        # ===== 1 cm³ =====
        cm_title = Text(
            "立方厘米", font=FONT, font_size=28,
            color=COLOR_CM, weight=BOLD
        ).move_to(UP * 3.0)
        cm_symbol = MathTex(
            r"\text{cm}^3", font_size=36, color=COLOR_CM
        ).next_to(cm_title, RIGHT, buff=0.3)
        self.play(FadeIn(cm_title), FadeIn(cm_symbol), run_time=0.4)

        # 小正方体
        cm_cube = cube_2d(0.7, COLOR_CM, fill_opacity=0.40, stroke_width=2.5)
        cm_cube.move_to(LEFT * 2.0 + UP * 1.2)
        self.play(Create(cm_cube), run_time=0.6)

        cm_edge_lbl = VGroup(
            Text("棱长", font=FONT, font_size=18, color=COLOR_CM),
            MathTex(r"1\text{cm}", font_size=22, color=COLOR_CM),
        ).arrange(RIGHT, buff=0.04).next_to(cm_cube, DOWN, buff=0.15)
        self.play(FadeIn(cm_edge_lbl), run_time=0.3)

        cm_life = Text(
            "1cm³ ≈ 一粒骰子的大小",
            font=FONT, font_size=22, color=WHITE
        ).move_to(RIGHT * 1.2 + UP * 1.2)
        self.play(FadeIn(cm_life, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.6)

        # ===== 1 dm³ =====
        dm_title = Text(
            "立方分米", font=FONT, font_size=28,
            color=COLOR_DM, weight=BOLD
        ).move_to(DOWN * 0.5)
        dm_symbol = MathTex(
            r"\text{dm}^3", font_size=36, color=COLOR_DM
        ).next_to(dm_title, RIGHT, buff=0.3)
        self.play(FadeIn(dm_title), FadeIn(dm_symbol), run_time=0.4)

        dm_cube = cube_2d(1.1, COLOR_DM, fill_opacity=0.30, stroke_width=2.5)
        dm_cube.move_to(LEFT * 2.0 + DOWN * 2.2)
        self.play(Create(dm_cube), run_time=0.6)

        dm_edge_lbl = VGroup(
            Text("棱长", font=FONT, font_size=18, color=COLOR_DM),
            MathTex(r"1\text{dm}", font_size=22, color=COLOR_DM),
        ).arrange(RIGHT, buff=0.04).next_to(dm_cube, DOWN, buff=0.15)
        self.play(FadeIn(dm_edge_lbl), run_time=0.3)

        dm_life = Text(
            "1dm³ ≈ 一个粉笔盒的大小",
            font=FONT, font_size=22, color=WHITE
        ).move_to(RIGHT * 1.2 + DOWN * 2.2)
        self.play(FadeIn(dm_life, shift=LEFT * 0.3), run_time=0.5)
        self.wait(0.6)

        # ===== 1 m³ =====
        m_title = Text(
            "立方米", font=FONT, font_size=28,
            color=COLOR_M, weight=BOLD
        ).move_to(DOWN * 4.2)
        m_symbol = MathTex(
            r"\text{m}^3", font_size=36, color=COLOR_M
        ).next_to(m_title, RIGHT, buff=0.3)
        self.play(FadeIn(m_title), FadeIn(m_symbol), run_time=0.4)

        m_cube = cube_2d(1.5, COLOR_M, fill_opacity=0.22, stroke_width=2.5)
        m_cube.move_to(LEFT * 1.8 + DOWN * 6.0)
        self.play(Create(m_cube), run_time=0.6)

        m_edge_lbl = VGroup(
            Text("棱长", font=FONT, font_size=18, color=COLOR_M),
            MathTex(r"1\text{m}", font_size=22, color=COLOR_M),
        ).arrange(RIGHT, buff=0.04).next_to(m_cube, DOWN, buff=0.15)
        self.play(FadeIn(m_edge_lbl), run_time=0.3)

        m_life = Text(
            "1m³ ≈ 一台洗衣机的大小",
            font=FONT, font_size=22, color=WHITE
        ).move_to(RIGHT * 1.2 + DOWN * 6.0)
        self.play(FadeIn(m_life, shift=LEFT * 0.3), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, intro,
                cm_title, cm_symbol, cm_cube, cm_edge_lbl, cm_life,
                dm_title, dm_symbol, dm_cube, dm_edge_lbl, dm_life,
                m_title, m_symbol, m_cube, m_edge_lbl, m_life,
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 维度对比 — 长度 vs 面积 vs 体积
    # ------------------------------------------------------------------

    def scene_4_dimension_comparison(self):
        """一维(长度) vs 二维(面积) vs 三维(体积)"""

        title = Text(
            "维度对比", font=FONT, font_size=38,
            color=COLOR_DIM, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 一维: 长度 =====
        dim1_box = RoundedRectangle(
            width=7.6, height=2.8,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_EDGE, stroke_width=2.5
        ).move_to(UP * 2.8)

        dim1_title = Text(
            "一维 — 长度", font=FONT, font_size=26,
            color=COLOR_EDGE, weight=BOLD
        ).move_to(UP * 3.8)

        # 线段
        line_seg = Line(
            LEFT * 1.5, RIGHT * 1.5,
            color=COLOR_EDGE, stroke_width=4
        ).move_to(UP * 2.8)
        dim1_unit = Text(
            "单位: cm, dm, m", font=FONT, font_size=20, color=GRAY_A
        ).move_to(UP * 1.9)

        self.play(FadeIn(dim1_box), run_time=0.2)
        self.play(Write(dim1_title), run_time=0.4)
        self.play(Create(line_seg), run_time=0.5)
        self.play(FadeIn(dim1_unit), run_time=0.3)
        self.wait(0.3)

        # ===== 二维: 面积 =====
        dim2_box = RoundedRectangle(
            width=7.6, height=2.8,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_DM, stroke_width=2.5
        ).move_to(DOWN * 0.5)

        dim2_title = Text(
            "二维 — 面积", font=FONT, font_size=26,
            color=COLOR_DM, weight=BOLD
        ).move_to(UP * 0.5)

        # 正方形
        sq = Square(
            side_length=1.6,
            color=COLOR_DM, fill_color=COLOR_DM,
            fill_opacity=0.35, stroke_width=3
        ).move_to(DOWN * 0.5)
        dim2_unit = Text(
            "单位: cm², dm², m²",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(dim2_box), run_time=0.2)
        self.play(Write(dim2_title), run_time=0.4)
        self.play(Create(sq), run_time=0.5)
        self.play(FadeIn(dim2_unit), run_time=0.3)
        self.wait(0.3)

        # ===== 三维: 体积 =====
        dim3_box = RoundedRectangle(
            width=7.6, height=2.8,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_CM, stroke_width=2.5
        ).move_to(DOWN * 3.8)

        dim3_title = Text(
            "三维 — 体积", font=FONT, font_size=26,
            color=COLOR_CM, weight=BOLD
        ).move_to(DOWN * 2.8)

        # 正方体
        cube = cube_2d(0.9, COLOR_CM, fill_opacity=0.35, stroke_width=2.5)
        cube.move_to(DOWN * 3.8)
        dim3_unit = Text(
            "单位: cm³, dm³, m³",
            font=FONT, font_size=20, color=GRAY_A
        ).move_to(DOWN * 4.9)

        self.play(FadeIn(dim3_box), run_time=0.2)
        self.play(Write(dim3_title), run_time=0.4)
        self.play(Create(cube), run_time=0.5)
        self.play(FadeIn(dim3_unit), run_time=0.3)
        self.wait(0.5)

        # 关键对比
        key = Text(
            "维度越高，度量越复杂！",
            font=FONT, font_size=26, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(key, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                dim1_box, dim1_title, line_seg, dim1_unit,
                dim2_box, dim2_title, sq, dim2_unit,
                dim3_box, dim3_title, cube, dim3_unit,
                key
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 知识总结
    # ------------------------------------------------------------------

    def scene_5_summary(self):
        """四点总结"""

        title = Text(
            "知识总结", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 总结卡片背景
        card_bg = RoundedRectangle(
            width=8.2, height=10.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(card_bg), run_time=0.3)

        # 第一条: 体积定义
        s1_title = Text(
            "1. 体积的定义", font=FONT, font_size=24,
            color=COLOR_SPACE, weight=BOLD
        ).move_to(UP * 3.8).align_to(card_bg, LEFT).shift(RIGHT * 0.8)
        s1_content = Text(
            "物体所占空间的大小",
            font=FONT, font_size=22, color=WHITE
        ).next_to(s1_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(s1_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(s1_content, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(0.2)

        # 第二条: 体积单位
        s2_title = Text(
            "2. 体积单位", font=FONT, font_size=24,
            color=COLOR_CM, weight=BOLD
        ).next_to(s1_content, DOWN, buff=0.5, aligned_edge=LEFT)

        s2_row1 = VGroup(
            MathTex(r"1\text{cm}^3", font_size=28, color=COLOR_CM),
            Text(" = 棱长1cm的正方体体积", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s2_title, DOWN, buff=0.2, aligned_edge=LEFT)

        s2_row2 = VGroup(
            MathTex(r"1\text{dm}^3", font_size=28, color=COLOR_DM),
            Text(" = 棱长1dm的正方体体积", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s2_row1, DOWN, buff=0.12, aligned_edge=LEFT)

        s2_row3 = VGroup(
            MathTex(r"1\text{m}^3", font_size=28, color=COLOR_M),
            Text(" = 棱长1m的正方体体积", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s2_row2, DOWN, buff=0.12, aligned_edge=LEFT)

        self.play(FadeIn(s2_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(s2_row1, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s2_row2, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s2_row3, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(0.2)

        # 第三条: 生活表象
        s3_title = Text(
            "3. 生活感知", font=FONT, font_size=24,
            color=COLOR_EDGE, weight=BOLD
        ).next_to(s2_row3, DOWN, buff=0.5, aligned_edge=LEFT)

        s3_row1 = VGroup(
            MathTex(r"1\text{cm}^3", font_size=24, color=COLOR_CM),
            Text(" ≈ 一粒骰子", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s3_title, DOWN, buff=0.2, aligned_edge=LEFT)

        s3_row2 = VGroup(
            MathTex(r"1\text{dm}^3", font_size=24, color=COLOR_DM),
            Text(" ≈ 一个粉笔盒", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s3_row1, DOWN, buff=0.12, aligned_edge=LEFT)

        s3_row3 = VGroup(
            MathTex(r"1\text{m}^3", font_size=24, color=COLOR_M),
            Text(" ≈ 一台洗衣机", font=FONT, font_size=18, color=WHITE),
        ).arrange(RIGHT, buff=0.06).next_to(s3_row2, DOWN, buff=0.12, aligned_edge=LEFT)

        self.play(FadeIn(s3_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(s3_row1, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s3_row2, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s3_row3, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(0.2)

        # 第四条: 维度对比
        s4_title = Text(
            "4. 维度对比", font=FONT, font_size=24,
            color=COLOR_DIM, weight=BOLD
        ).next_to(s3_row3, DOWN, buff=0.5, aligned_edge=LEFT)

        s4_row1 = Text(
            "长度 → 一维  (cm, m)",
            font=FONT, font_size=18, color=WHITE
        ).next_to(s4_title, DOWN, buff=0.2, aligned_edge=LEFT)

        s4_row2 = Text(
            "面积 → 二维  (cm², m²)",
            font=FONT, font_size=18, color=WHITE
        ).next_to(s4_row1, DOWN, buff=0.12, aligned_edge=LEFT)

        s4_row3 = Text(
            "体积 → 三维  (cm³, m³)",
            font=FONT, font_size=18, color=COLOR_HL
        ).next_to(s4_row2, DOWN, buff=0.12, aligned_edge=LEFT)

        self.play(FadeIn(s4_title, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(s4_row1, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s4_row2, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(s4_row3, shift=RIGHT * 0.2), run_time=0.3)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, card_bg,
                s1_title, s1_content,
                s2_title, s2_row1, s2_row2, s2_row3,
                s3_title, s3_row1, s3_row2, s3_row3,
                s4_title, s4_row1, s4_row2, s4_row3,
            )),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------

    def scene_6_outro(self):
        """作者信息放大 + 关注提示 + 小方块装饰"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 6个小方块围绕旋转 (象征三种体积单位)
        colors = [COLOR_CM, COLOR_DM, COLOR_M,
                  COLOR_EDGE, COLOR_DIM, COLOR_HL]
        mini_cubes = VGroup(*[
            Square(
                side_length=0.35,
                fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).rotate(i * PI / 6).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(
            *[FadeIn(s, scale=0.3) for s in mini_cubes],
            run_time=0.5
        )
        self.play(
            Rotate(
                mini_cubes, angle=2 * PI / 3,
                run_time=1.2, rate_func=smooth
            )
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(
                self.author_mob, author_id, follow, mini_cubes
            )),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql --disable_caching 003_体积与体积单位.py VolumeUnitLesson
#   高质量:   manim -qh  003_体积与体积单位.py VolumeUnitLesson
#   4K:       manim -qk  003_体积与体积单位.py VolumeUnitLesson
# ======================================================================
