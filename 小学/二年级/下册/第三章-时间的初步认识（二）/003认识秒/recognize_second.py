"""
认识秒 - 二年级数学教学动画
知识点: 秒针走1小格是1秒，走一圈是60秒（1分钟）
核心进率: 1分 = 60秒

格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql recognize_second.py RecognizeSecond   # 快速预览
  manim -qh  recognize_second.py RecognizeSecond   # 高质量
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
# 颜色常量
# ============================================================
BG_COLOR        = "#1a1a2e"
CLOCK_FACE_COL  = "#f5f0e8"
CLOCK_RIM_COL   = "#2c3e50"
HAND_SEC_COL    = "#e74c3c"   # 秒针：醒目红
HAND_MIN_COL    = "#2c3e50"   # 分针：深色
HAND_HOUR_COL   = "#34495e"   # 时针：灰深色
TICK_MAJOR_COL  = "#2c3e50"   # 大刻度（每5秒）
TICK_MINOR_COL  = "#95a5a6"   # 小刻度
HIGHLIGHT_COL   = "#f1c40f"   # 强调黄
TEXT_MAIN_COL   = "#ecf0f1"   # 主文字
TEXT_SUB_COL    = "#bdc3c7"   # 副文字
FORMULA_COL     = "#2ecc71"   # 公式绿
ARC_COL         = "#e74c3c"   # 弧线颜色

FONT = "Noto Sans CJK SC"

# ============================================================
# 字体大小规范
# ============================================================
FS_TITLE    = 38
FS_SUBTITLE = 30
FS_BODY     = 24
FS_LABEL    = 20
FS_SMALL    = 18
FS_AUTHOR   = 20
FS_FORMULA  = 34


# ============================================================
# 时钟几何参数（精确定义，不臆想）
# ============================================================
CLOCK_CENTER   = np.array([0.0, 1.8, 0.0])
CLOCK_RADIUS   = 2.2
SEC_HAND_LEN   = 1.95    # 秒针：略短于半径
MIN_HAND_LEN   = 1.50    # 分针
HOUR_HAND_LEN  = 1.05    # 时针


def sec_angle(k: int) -> float:
    """
    第 k 秒对应的角度（弧度，Manim坐标系）
    k=0  → 12点 = PI/2
    顺时针旋转 → 角度递减
    每格 = 360°/60 = 6° = PI/30 弧度
    """
    return np.pi / 2 - 2 * np.pi * k / 60


def clock_point(k: int, radius: float = CLOCK_RADIUS) -> np.ndarray:
    """计算第 k 个刻度位置（k=0对应12点）"""
    a = sec_angle(k)
    return CLOCK_CENTER + np.array([radius * np.cos(a), radius * np.sin(a), 0.0])


def hand_endpoint(k: int, length: float) -> np.ndarray:
    """计算指针尖端坐标"""
    a = sec_angle(k)
    return CLOCK_CENTER + np.array([length * np.cos(a), length * np.sin(a), 0.0])


# ============================================================
# 主场景类
# ============================================================
class RecognizeSecond(Scene):
    """
    认识秒 - 教学动画
    
    场景顺序:
    1. 开场钩子
    2. 认识秒针
    3. 1格 = 1秒
    4. 一圈 = 60秒
    5. 公式总结
    6. 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self._verify_geometry()

        self.scene_1_opening()
        self.scene_2_introduce_hand()
        self.scene_3_one_tick()
        self.scene_4_full_circle()
        self.scene_5_formula()
        self.scene_6_outro()

    # ----------------------------------------------------------
    # 几何验证（内嵌版）
    # ----------------------------------------------------------
    def _verify_geometry(self):
        """验证时钟几何参数的正确性"""
        eps = 1e-8

        # 1. 验证12点位置
        p12 = clock_point(0)
        expected_12 = CLOCK_CENTER + np.array([0, CLOCK_RADIUS, 0])
        assert np.allclose(p12, expected_12, atol=eps), "12点刻度位置错误"

        # 2. 验证3点位置
        p3 = clock_point(15)
        expected_3 = CLOCK_CENTER + np.array([CLOCK_RADIUS, 0, 0])
        assert np.allclose(p3, expected_3, atol=eps), "3点刻度位置错误"

        # 3. 验证6点位置
        p6 = clock_point(30)
        expected_6 = CLOCK_CENTER + np.array([0, -CLOCK_RADIUS, 0])
        assert np.allclose(p6, expected_6, atol=eps), "6点刻度位置错误"

        # 4. 验证所有刻度点到圆心距离均为 CLOCK_RADIUS
        for k in range(60):
            dist = np.linalg.norm(clock_point(k) - CLOCK_CENTER)
            assert abs(dist - CLOCK_RADIUS) < eps, f"刻度 k={k} 距离错误: {dist}"

        # 5. 验证秒针长度 < 表盘半径
        assert SEC_HAND_LEN < CLOCK_RADIUS, "秒针太长，会超出表盘"

        # 6. 验证边界安全（竖屏: x∈[-4,4], y∈[-7.5,7.5]）
        for k in range(60):
            p = clock_point(k)
            assert -4.0 <= p[0] <= 4.0, f"刻度 k={k} x={p[0]:.3f} 超出横向边界"
            # 时钟中心 y=1.8，半径 2.2，最大 y=4.0 < 7.5
            assert -7.5 <= p[1] <= 7.5, f"刻度 k={k} y={p[1]:.3f} 超出纵向边界"

        print("✅ 几何验证全部通过")

    # ----------------------------------------------------------
    # 时钟构建工具方法
    # ----------------------------------------------------------
    def _build_clock_face(self) -> VGroup:
        """构建完整表盘（不含指针）"""
        # 外圆
        rim = Circle(radius=CLOCK_RADIUS, color=CLOCK_RIM_COL, stroke_width=5)
        rim.move_to(CLOCK_CENTER)

        # 表盘背景
        face = Circle(radius=CLOCK_RADIUS * 0.98, fill_color=CLOCK_FACE_COL,
                      fill_opacity=1, stroke_width=0)
        face.move_to(CLOCK_CENTER)

        # 60个刻度线
        ticks = VGroup()
        for k in range(60):
            outer = clock_point(k, CLOCK_RADIUS * 0.97)
            if k % 5 == 0:
                # 大刻度（每5格/分钟数字位置）
                inner = clock_point(k, CLOCK_RADIUS * 0.82)
                tick = Line(inner, outer, stroke_width=3.5, color=TICK_MAJOR_COL)
            else:
                inner = clock_point(k, CLOCK_RADIUS * 0.90)
                tick = Line(inner, outer, stroke_width=1.5, color=TICK_MINOR_COL)
            ticks.add(tick)

        # 12个数字（时间数字）
        numbers = VGroup()
        num_labels = {
            0: "12", 5: "1", 10: "2", 15: "3", 20: "4",
            25: "5", 30: "6", 35: "7", 40: "8", 45: "9",
            50: "10", 55: "11"
        }
        for k, label in num_labels.items():
            pos = clock_point(k, CLOCK_RADIUS * 0.70)
            num_text = Text(label, font=FONT, font_size=18, color=CLOCK_RIM_COL,
                            weight=BOLD)
            num_text.move_to(pos)
            numbers.add(num_text)

        # 中心点
        center_dot = Dot(CLOCK_CENTER, radius=0.08, color=CLOCK_RIM_COL)

        return VGroup(face, rim, ticks, numbers, center_dot)

    def _build_sec_hand(self, k: int = 0) -> Line:
        """构建秒针（位于第k秒位置）"""
        tip = hand_endpoint(k, SEC_HAND_LEN)
        tail = CLOCK_CENTER - (tip - CLOCK_CENTER) * 0.15  # 小尾巴
        hand = Line(tail, tip, stroke_width=2.5, color=HAND_SEC_COL)
        return hand

    def _build_min_hand(self, k_min: int = 0) -> Line:
        """构建分针（位于第k_min分钟位置，k_min∈[0,60)）"""
        tip = hand_endpoint(k_min, MIN_HAND_LEN)
        tail = CLOCK_CENTER - (tip - CLOCK_CENTER) * 0.12
        return Line(tail, tip, stroke_width=4, color=HAND_MIN_COL)

    def _build_hour_hand(self, k_hour: int = 0) -> Line:
        """构建时针（位于第k_hour位置，对应5*k_hour秒刻度）"""
        tip = hand_endpoint(k_hour, HOUR_HAND_LEN)
        tail = CLOCK_CENTER - (tip - CLOCK_CENTER) * 0.10
        return Line(tail, tip, stroke_width=6, color=HAND_HOUR_COL)

    def _build_author_info(self) -> Text:
        """作者信息小字"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=FS_AUTHOR, color=TEXT_SUB_COL
        ).move_to(UP * 7.2)

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author = self._build_author_info()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 钩子：大标题
        hook = Text("你知道", font=FONT, font_size=FS_TITLE + 4,
                    color=TEXT_MAIN_COL)
        hook2 = Text("1秒有多短吗？", font=FONT, font_size=FS_TITLE + 4,
                     color=HIGHLIGHT_COL)
        hook_group = VGroup(hook, hook2).arrange(DOWN, buff=0.3).move_to(UP * 5.5)

        self.play(Write(hook), run_time=0.7)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        # 构建时钟（不含指针，先让表盘出现）
        self.clock_face = self._build_clock_face()
        # 初始指针（时间定在大约10:10，经典位置）
        self.sec_hand = self._build_sec_hand(0)    # 秒针在12点
        self.min_hand = self._build_min_hand(10)   # 分针在2点
        self.hour_hand = self._build_hour_hand(50) # 时针在10点

        self.play(
            FadeIn(self.clock_face, scale=0.8),
            run_time=1.0
        )
        self.play(
            Create(self.hour_hand),
            Create(self.min_hand),
            Create(self.sec_hand),
            run_time=0.8
        )

        self.wait(0.6)

        # 清理钩子文字
        self.play(FadeOut(hook_group), run_time=0.4)

    # ----------------------------------------------------------
    # Scene 2: 认识秒针
    # ----------------------------------------------------------
    def scene_2_introduce_hand(self):
        # 场景标题
        title = Text("认识秒针", font=FONT, font_size=FS_TITLE,
                     color=HIGHLIGHT_COL).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 高亮秒针：变红变粗（秒针本身已经是红色）
        self.play(
            self.sec_hand.animate.set_stroke(width=5),
            Flash(
                self.sec_hand.get_end(),
                color=HAND_SEC_COL,
                flash_radius=0.3,
                num_lines=10
            ),
            run_time=0.6
        )

        # 箭头指向秒针
        arrow_target = self.sec_hand.get_center()
        arrow = Arrow(
            start=arrow_target + RIGHT * 1.8 + DOWN * 0.2,
            end=arrow_target + RIGHT * 0.15,
            color=HIGHLIGHT_COL,
            buff=0,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        self.play(GrowArrow(arrow), run_time=0.5)

        # 说明文字
        desc1 = Text("秒针", font=FONT, font_size=FS_BODY, color=HAND_SEC_COL, weight=BOLD)
        desc2 = Text("最细  最长  跑得最快", font=FONT, font_size=FS_BODY - 2,
                     color=TEXT_MAIN_COL)
        desc_group = VGroup(desc1, desc2).arrange(DOWN, buff=0.2).move_to(DOWN * 4.0)

        self.play(FadeIn(desc_group, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arrow),
            FadeOut(desc_group),
            self.sec_hand.animate.set_stroke(width=2.5),   # 恢复粗细
            self.min_hand.animate.set_opacity(0.3),         # 淡化分针
            self.hour_hand.animate.set_opacity(0.3),        # 淡化时针
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 3: 1小格 = 1秒
    # ----------------------------------------------------------
    def scene_3_one_tick(self):
        # 标题
        title = Text("秒针走1小格", font=FONT, font_size=FS_TITLE,
                     color=HIGHLIGHT_COL).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 把秒针重置到12点位置并高亮起始刻度
        self.play(
            self.sec_hand.animate.put_start_and_end_on(
                CLOCK_CENTER - (hand_endpoint(0, SEC_HAND_LEN) - CLOCK_CENTER) * 0.15,
                hand_endpoint(0, SEC_HAND_LEN)
            ),
            run_time=0.3
        )

        # 高亮最初两个刻度（k=0和k=1）之间的区域
        tick_0 = clock_point(0)
        tick_1 = clock_point(1)
        start_dot = Dot(tick_0, radius=0.1, color=HIGHLIGHT_COL)
        end_dot   = Dot(tick_1, radius=0.1, color=HIGHLIGHT_COL)

        # 弧线：从k=0到k=1（顺时针，弧度=-2PI/60）
        tick_arc = Arc(
            radius=CLOCK_RADIUS * 0.94,
            start_angle=sec_angle(0),
            angle=-2 * np.pi / 60,       # 顺时针6°
            color=HIGHLIGHT_COL,
            stroke_width=6
        ).move_to(CLOCK_CENTER)

        self.play(FadeIn(start_dot), run_time=0.3)
        self.play(Create(tick_arc), FadeIn(end_dot), run_time=0.8)

        hint1 = Text("这是1小格", font=FONT, font_size=FS_BODY, color=TEXT_MAIN_COL)
        hint1.move_to(DOWN * 3.8)
        self.play(FadeIn(hint1, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # ── 秒针转动1格，计数 +1 ──
        count_text = Text("1", font=FONT, font_size=60, color=HAND_SEC_COL, weight=BOLD)
        count_label = Text("秒", font=FONT, font_size=FS_SUBTITLE, color=TEXT_MAIN_COL)
        count_group = VGroup(count_text, count_label).arrange(RIGHT, buff=0.2)
        count_group.move_to(DOWN * 5.0)

        # 动画旋转秒针1格（绕时钟中心顺时针6°）
        self.play(
            Rotate(
                self.sec_hand,
                angle=-2 * np.pi / 60,   # 顺时针6°
                about_point=CLOCK_CENTER
            ),
            FadeOut(tick_arc),
            FadeOut(start_dot),
            FadeOut(end_dot),
            run_time=0.8
        )
        self.play(FadeIn(count_group, scale=1.2), run_time=0.4)
        self.wait(0.4)

        # 关键说明：1格 = 1秒
        eq1_ch = Text("走1小格", font=FONT, font_size=FS_BODY, color=TEXT_MAIN_COL)
        eq1_eq = Text("=", font=FONT, font_size=FS_BODY, color=TEXT_MAIN_COL)
        eq1_val = Text("1秒", font=FONT, font_size=FS_BODY, color=FORMULA_COL, weight=BOLD)
        eq1 = VGroup(eq1_ch, eq1_eq, eq1_val).arrange(RIGHT, buff=0.25)
        eq1.move_to(DOWN * 4.8)

        self.play(
            FadeOut(hint1),
            FadeOut(count_group),
            FadeIn(eq1, shift=UP * 0.2),
            run_time=0.5
        )
        self.wait(0.5)

        # ── 连续走3格，计数 1、2、3 ──
        counter_val = Integer(1, color=HAND_SEC_COL, font_size=60)
        counter_suffix = Text("秒", font=FONT, font_size=FS_SUBTITLE,
                              color=TEXT_MAIN_COL)
        counter = VGroup(counter_val, counter_suffix).arrange(RIGHT, buff=0.15)
        counter.move_to(DOWN * 6.0)

        self.play(FadeIn(counter), run_time=0.3)
        # 秒针已在 k=1，继续走到 k=4
        for step in range(2, 5):
            self.play(
                Rotate(
                    self.sec_hand,
                    angle=-2 * np.pi / 60,
                    about_point=CLOCK_CENTER
                ),
                ChangeDecimalToValue(counter_val, step),
                run_time=0.7
            )
            self.wait(0.2)

        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(eq1),
            FadeOut(counter),
            run_time=0.4
        )

    # ----------------------------------------------------------
    # Scene 4: 走一圈 = 60秒 = 1分钟
    # ----------------------------------------------------------
    def scene_4_full_circle(self):
        # 标题
        title = Text("秒针走一圈", font=FONT, font_size=FS_TITLE,
                     color=HIGHLIGHT_COL).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 说明
        desc = Text("从12点出发，转一圈...", font=FONT, font_size=FS_BODY,
                    color=TEXT_MAIN_COL).move_to(DOWN * 3.8)
        self.play(FadeIn(desc), run_time=0.4)

        # 把秒针复位到 k=0（12点）
        # 当前秒针在 k=4 位置
        # 用 Rotate 转回 k=0
        current_k = 4
        angle_to_reset = 2 * np.pi * current_k / 60   # 顺时针转回 = 正向旋转
        self.play(
            Rotate(
                self.sec_hand,
                angle=angle_to_reset,
                about_point=CLOCK_CENTER
            ),
            run_time=0.4
        )
        self.wait(0.2)

        # ── 显示旋转轨迹弧 ──
        trace_arc = Arc(
            radius=CLOCK_RADIUS * 0.75,
            start_angle=np.pi / 2,
            angle=-2 * np.pi,
            color=HAND_SEC_COL,
            stroke_width=3,
            stroke_opacity=0.4
        ).move_to(CLOCK_CENTER)

        # 秒针高速旋转一圈（run_time=3.5s）
        # 同时显示轨迹
        self.play(
            Create(trace_arc),
            Rotate(
                self.sec_hand,
                angle=-2 * np.pi,    # 顺时针一圈
                about_point=CLOCK_CENTER
            ),
            run_time=3.5,
            rate_func=linear
        )
        self.wait(0.3)

        # 弹出 60格 说明
        self.play(FadeOut(desc), run_time=0.2)

        tick_60 = Text("走了", font=FONT, font_size=FS_SUBTITLE, color=TEXT_MAIN_COL)
        tick_60b = Text("60", font=FONT, font_size=FS_TITLE + 6,
                        color=HAND_SEC_COL, weight=BOLD)
        tick_60c = Text("小格", font=FONT, font_size=FS_SUBTITLE, color=TEXT_MAIN_COL)
        tick_60_group = VGroup(tick_60, tick_60b, tick_60c).arrange(RIGHT, buff=0.2)
        tick_60_group.move_to(DOWN * 4.0)

        self.play(
            FadeIn(tick_60_group, scale=1.1),
            Flash(CLOCK_CENTER + UP * CLOCK_RADIUS * 0.1,
                  color=HIGHLIGHT_COL, flash_radius=0.5),
            run_time=0.7
        )
        self.wait(0.8)

        # 核心结论：一圈 = 60秒
        eq_row1_a = Text("一圈", font=FONT, font_size=FS_SUBTITLE, color=TEXT_MAIN_COL)
        eq_row1_b = Text("=", font=FONT, font_size=FS_SUBTITLE, color=TEXT_MAIN_COL)
        eq_row1_c = Text("60秒", font=FONT, font_size=FS_SUBTITLE,
                         color=FORMULA_COL, weight=BOLD)
        eq_row1 = VGroup(eq_row1_a, eq_row1_b, eq_row1_c).arrange(RIGHT, buff=0.3)
        eq_row1.move_to(DOWN * 5.2)

        self.play(
            FadeIn(eq_row1, shift=UP * 0.3),
            run_time=0.6
        )
        self.wait(1.0)

        # 分针向前走1格（提示分针关联）
        self.play(
            self.min_hand.animate.set_opacity(1.0),   # 恢复分针
            run_time=0.3
        )
        rotate_min = Rotate(
            self.min_hand,
            angle=-2 * np.pi / 60,   # 分针走1格
            about_point=CLOCK_CENTER
        )
        self.play(rotate_min, run_time=0.8)

        min_hint = Text("同时分针走了1小格", font=FONT, font_size=FS_BODY - 2,
                        color=HAND_MIN_COL).move_to(DOWN * 6.2)
        self.play(FadeIn(min_hint), run_time=0.4)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(trace_arc),
            FadeOut(tick_60_group),
            FadeOut(eq_row1),
            FadeOut(min_hint),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 5: 公式总结
    # ----------------------------------------------------------
    def scene_5_formula(self):
        # 淡出时钟（画面简洁化）
        self.play(
            self.clock_face.animate.scale(0.55).move_to(UP * 4.8),
            self.sec_hand.animate.scale(0.55).move_to(
                CLOCK_CENTER * 0.55 + UP * 4.8 * 0.45
            ).set_opacity(0.5),
            self.min_hand.animate.scale(0.55).set_opacity(0.4),
            self.hour_hand.animate.scale(0.55).set_opacity(0.4),
            run_time=0.8
        )

        # "记住啦！"
        remember = Text("记住啦！", font=FONT, font_size=FS_TITLE + 2,
                        color=HIGHLIGHT_COL, weight=BOLD).move_to(UP * 3.2)
        self.play(Write(remember), run_time=0.6)

        # 公式卡片背景
        card_bg = RoundedRectangle(
            width=7.0, height=2.8,
            corner_radius=0.4,
            fill_color="#0f3460",
            fill_opacity=0.9,
            stroke_color=FORMULA_COL,
            stroke_width=3
        ).move_to(UP * 1.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 公式：1分 = 60秒（用 Text 实现，避免 MathTex 中文问题）
        formula_a = Text("1", font=FONT, font_size=FS_FORMULA + 10,
                         color=HIGHLIGHT_COL, weight=BOLD)
        formula_b = Text("分", font=FONT, font_size=FS_FORMULA + 4,
                         color=TEXT_MAIN_COL, weight=BOLD)
        formula_c = Text("=", font=FONT, font_size=FS_FORMULA + 10,
                         color=TEXT_MAIN_COL, weight=BOLD)
        formula_d = Text("60", font=FONT, font_size=FS_FORMULA + 10,
                         color=FORMULA_COL, weight=BOLD)
        formula_e = Text("秒", font=FONT, font_size=FS_FORMULA + 4,
                         color=TEXT_MAIN_COL, weight=BOLD)

        formula = VGroup(formula_a, formula_b, formula_c, formula_d, formula_e)
        formula.arrange(RIGHT, buff=0.2).move_to(UP * 1.0)

        self.play(Write(formula), run_time=1.0)
        self.wait(0.3)

        # 强调闪烁
        self.play(
            Flash(formula_d.get_center(), color=FORMULA_COL, flash_radius=0.5),
            formula.animate.scale(1.05),
            run_time=0.4
        )
        self.play(formula.animate.scale(1 / 1.05), run_time=0.2)

        # 口诀
        mnemonic_1 = Text("秒针走1格", font=FONT, font_size=FS_BODY,
                           color=TEXT_MAIN_COL)
        mnemonic_eq = Text("→", font=FONT, font_size=FS_BODY, color=HIGHLIGHT_COL)
        mnemonic_2 = Text("1秒", font=FONT, font_size=FS_BODY,
                          color=HAND_SEC_COL, weight=BOLD)
        line1 = VGroup(mnemonic_1, mnemonic_eq, mnemonic_2).arrange(RIGHT, buff=0.3)

        mnemonic_3 = Text("秒针走一圈", font=FONT, font_size=FS_BODY,
                           color=TEXT_MAIN_COL)
        mnemonic_eq2 = Text("→", font=FONT, font_size=FS_BODY, color=HIGHLIGHT_COL)
        mnemonic_4 = Text("60秒", font=FONT, font_size=FS_BODY,
                          color=FORMULA_COL, weight=BOLD)
        line2 = VGroup(mnemonic_3, mnemonic_eq2, mnemonic_4).arrange(RIGHT, buff=0.3)

        lines = VGroup(line1, line2).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        lines.move_to(DOWN * 1.5)

        self.play(FadeIn(lines, shift=UP * 0.3), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(remember),
            FadeOut(card_bg),
            FadeOut(formula),
            FadeOut(lines),
            FadeOut(self.clock_face),
            FadeOut(self.sec_hand),
            FadeOut(self.min_hand),
            FadeOut(self.hour_hand),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 6: 片尾关注
    # ----------------------------------------------------------
    def scene_6_outro(self):
        # 作者名放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=TEXT_MAIN_COL, weight=BOLD
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=TEXT_SUB_COL
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        # 关注文字
        follow = Text(
            "关注我，学更多数学知识！",
            font=FONT, font_size=FS_SUBTITLE, color=HIGHLIGHT_COL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.5)

        # 装饰：小秒钟图标旋转
        small_clocks = VGroup()
        for i in range(5):
            angle_i = i * 2 * np.pi / 5
            offset = np.array([2.5 * np.cos(angle_i), 2.5 * np.sin(angle_i) - 2.5, 0])
            mini_rim = Circle(radius=0.3, color=HIGHLIGHT_COL, stroke_width=2)
            mini_hand = Line(
                ORIGIN, UP * 0.25,
                color=HAND_SEC_COL, stroke_width=2
            )
            mini_clock = VGroup(mini_rim, mini_hand).move_to(offset)
            small_clocks.add(mini_clock)

        self.play(
            *[FadeIn(c, scale=0.5) for c in small_clocks],
            run_time=0.5
        )
        self.play(
            Rotate(small_clocks, angle=-2 * np.pi, about_point=DOWN * 2.5),
            run_time=2.0
        )

        self.wait(0.5)
        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(small_clocks),
            run_time=0.8
        )