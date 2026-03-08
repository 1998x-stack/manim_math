"""
clock_animation.py — 二年级数学：读写几时几分
TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ─── 全局配置（TikTok 竖屏）─────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─── 时钟常量 ────────────────────────────────────────────
CLOCK_CENTER   = np.array([0.0, 3.0, 0.0])
CLOCK_RADIUS   = 2.0
HOUR_HAND_LEN  = 1.1
MIN_HAND_LEN   = 1.7
FONT           = "Noto Sans CJK SC"
BG_COLOR       = "#1a1a2e"


# ─── 几何辅助函数 ────────────────────────────────────────
def clock_angle(hour: int = 0, minute: int = 0, is_minute_hand: bool = False) -> float:
    """返回时/分针角度（数学惯例：从正 x 轴逆时针量，12点 = π/2）"""
    if is_minute_hand:
        return np.pi / 2 - minute * np.pi / 30
    return np.pi / 2 - (hour % 12 + minute / 60) * np.pi / 6


def hand_tip(center: np.ndarray, length: float, angle: float) -> np.ndarray:
    return center + length * np.array([np.cos(angle), np.sin(angle), 0.0])


def num_pos(n: int, center: np.ndarray, r: float) -> np.ndarray:
    angle = np.pi / 2 - n * np.pi / 6
    return center + r * np.array([np.cos(angle), np.sin(angle), 0.0])


# ─────────────────────────────────────────────────────────
class ClockReadingLesson(Scene):
    """
    时间的初步认识（二）— 读写几时几分
    场景序列：
      1. 开场钩子
      2. 认识时针与分针
      3. 读时间方法（规律）
      4. 例题 8时45分
      5. 难点 8时06分（不指整数）
      6. 两种写法总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_clock_parts()
        self.scene_3_reading_rule()
        self.scene_4_example_845()
        self.scene_5_example_806()
        self.scene_6_summary()
        self.scene_7_outro()

    # ──────────────────────────────────────────────
    # 初始化（统一预计算）
    # ──────────────────────────────────────────────
    def setup_geometry(self):
        self.cc = CLOCK_CENTER.copy()
        self.cr = CLOCK_RADIUS

        # 12 个数字坐标（r=0.75×radius）
        num_r = self.cr * 0.75
        self.num_positions = {
            n: num_pos(n, self.cc, num_r) for n in range(1, 13)
        }

        # 特殊时刻的手角
        self.angle_h_845 = clock_angle(hour=8, minute=45)
        self.angle_m_845 = clock_angle(minute=45, is_minute_hand=True)
        self.angle_h_806 = clock_angle(hour=8, minute=6)
        self.angle_m_806 = clock_angle(minute=6,  is_minute_hand=True)

        # 60 个刻度坐标缓存
        self.tick_positions = []
        for i in range(60):
            a = np.pi / 2 - i * np.pi / 30
            self.tick_positions.append(
                self.cc + self.cr * np.array([np.cos(a), np.sin(a), 0])
            )

        self._verify()

    def _verify(self):
        # 验证 8:45 分针确实指向 9 点钟方向（左侧 x = -1.7）
        tip_m = hand_tip(self.cc, MIN_HAND_LEN, self.angle_m_845)
        assert tip_m[0] < -1.5, f"8:45分针位置异常: {tip_m}"
        # 验证 8:06 分针刚过 12（y 接近顶部）
        tip_m2 = hand_tip(self.cc, MIN_HAND_LEN, self.angle_m_806)
        assert tip_m2[1] > 4.0, f"8:06分针位置异常: {tip_m2}"
        print("✓ setup_geometry 验证通过")

    # ──────────────────────────────────────────────
    # 构建工具方法
    # ──────────────────────────────────────────────
    def make_clock_face(self, center=None, radius=None) -> VGroup:
        """构建时钟表盘（不含指针）"""
        c = center if center is not None else self.cc
        r = radius if radius is not None else self.cr

        group = VGroup()

        # 表盘外圆
        outer = Circle(radius=r, color=WHITE, stroke_width=4).move_to(c)
        group.add(outer)

        # 内装饰圆
        inner = Circle(radius=r * 0.93, color=BLUE_B,
                       stroke_width=1.2, stroke_opacity=0.35).move_to(c)
        group.add(inner)

        # 60 个刻度线
        for i in range(60):
            a    = np.pi / 2 - i * np.pi / 30
            is_h = (i % 5 == 0)
            r_in  = r * (0.84 if is_h else 0.91)
            r_out = r
            start = c + r_in  * np.array([np.cos(a), np.sin(a), 0])
            end   = c + r_out * np.array([np.cos(a), np.sin(a), 0])
            tick = Line(start, end,
                        stroke_width=3.5 if is_h else 1.5,
                        color=WHITE if is_h else GRAY_B)
            group.add(tick)

        # 数字 1–12
        num_r = r * 0.75
        for n in range(1, 13):
            pos  = num_pos(n, c, num_r)
            label = Text(str(n), font=FONT, font_size=28, color=WHITE)
            label.move_to(pos)
            group.add(label)

        # 圆心点
        group.add(Dot(c, radius=0.1, color=WHITE, fill_opacity=1))
        return group

    def make_hour_hand(self, hour: int, minute: int,
                       center=None, color=ORANGE) -> Line:
        c = center if center is not None else self.cc
        a = clock_angle(hour=hour, minute=minute)
        return Line(c, hand_tip(c, HOUR_HAND_LEN, a),
                    stroke_width=8, color=color)

    def make_minute_hand(self, minute: int,
                         center=None, color=TEAL) -> Line:
        c = center if center is not None else self.cc
        a = clock_angle(minute=minute, is_minute_hand=True)
        return Line(c, hand_tip(c, MIN_HAND_LEN, a),
                    stroke_width=5, color=color)

    def highlight_number(self, n: int, color=YELLOW, radius=0.3) -> Circle:
        return Circle(radius=radius, color=color, stroke_width=3
                      ).move_to(self.num_positions[n])

    def txt(self, content: str, size: int = 24, color=WHITE, **kw) -> Text:
        return Text(content, font=FONT, font_size=size, color=color, **kw)

    def answer_box(self, content: str, y_pos: float = -5.4) -> VGroup:
        box = RoundedRectangle(
            width=6.2, height=1.5, corner_radius=0.3,
            fill_color="#16213e", fill_opacity=0.95,
            stroke_color=YELLOW, stroke_width=3
        ).move_to(y_pos * UP)
        label = self.txt(content, size=36, color=YELLOW).move_to(box)
        return VGroup(box, label)

    # ──────────────────────────────────────────────
    # 场景 1：开场钩子
    # ──────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息（持续显示到片尾）
        self.author_bar = self.txt(
            "上海初高中数学直通车 @emptyandcalm",
            size=20, color=GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar), run_time=0.4)

        # 钩子标题
        hook = self.txt("你会看时钟吗？", size=46, color=YELLOW).move_to(UP * 5.8)
        self.play(Write(hook), run_time=0.7)

        # 出现钟表（8:45）
        self.clock = self.make_clock_face()
        hh = self.make_hour_hand(8, 45)
        mh = self.make_minute_hand(45)

        self.play(Create(self.clock), run_time=1.0)
        self.play(Create(hh), Create(mh), run_time=0.7)

        question = self.txt("这是几时几分？", size=34, color=WHITE
                            ).move_to(DOWN * 1.8)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        # 清场
        self.play(
            FadeOut(hook), FadeOut(question),
            FadeOut(hh), FadeOut(mh),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 2：认识时针和分针
    # ──────────────────────────────────────────────
    def scene_2_clock_parts(self):
        title = self.txt("认识时针和分针", size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 时针（指向10）
        hh = self.make_hour_hand(10, 0, color=ORANGE)
        self.play(Create(hh), run_time=0.6)

        h_box = RoundedRectangle(
            width=3.0, height=0.85, corner_radius=0.2,
            fill_color="#2d2010", fill_opacity=0.9,
            stroke_color=ORANGE, stroke_width=2
        ).move_to(LEFT * 2.5 + DOWN * 1.2)
        h_lbl = self.txt("时针（短粗）", size=24, color=ORANGE).move_to(h_box)
        h_arr = Arrow(
            h_box.get_right(),
            self.cc + np.array([-0.5, 0.6, 0]),
            color=ORANGE, buff=0.05, stroke_width=2, tip_length=0.15
        )
        self.play(FadeIn(h_box), Write(h_lbl), Create(h_arr), run_time=0.7)
        self.play(Indicate(hh, color=ORANGE, scale_factor=1.12), run_time=0.5)
        self.wait(0.8)

        # 分针（指向12）
        mh = self.make_minute_hand(0, color=TEAL)
        self.play(Create(mh), run_time=0.6)

        m_box = RoundedRectangle(
            width=3.0, height=0.85, corner_radius=0.2,
            fill_color="#0a2030", fill_opacity=0.9,
            stroke_color=TEAL, stroke_width=2
        ).move_to(RIGHT * 2.5 + DOWN * 0.5)
        m_lbl = self.txt("分针（长细）", size=24, color=TEAL).move_to(m_box)
        m_arr = Arrow(
            m_box.get_left(),
            self.cc + np.array([0.15, 1.5, 0]),
            color=TEAL, buff=0.05, stroke_width=2, tip_length=0.15
        )
        self.play(FadeIn(m_box), Write(m_lbl), Create(m_arr), run_time=0.7)
        self.play(Indicate(mh, color=TEAL, scale_factor=1.1), run_time=0.5)
        self.wait(0.8)

        # 记忆口诀
        rule = self.txt("短 = 时针    长 = 分针", size=30, color=YELLOW
                        ).move_to(DOWN * 5.0)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(hh), FadeOut(mh),
            FadeOut(h_box), FadeOut(h_lbl), FadeOut(h_arr),
            FadeOut(m_box), FadeOut(m_lbl), FadeOut(m_arr),
            FadeOut(rule), run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 3：读时间规律
    # ──────────────────────────────────────────────
    def scene_3_reading_rule(self):
        title = self.txt("怎么读时间？", size=36, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # ── 步骤1：先看时针 ──
        s1_icon = self.txt("①", size=34, color=ORANGE).move_to(LEFT * 3.0 + DOWN * 1.6)
        s1_text = self.txt("先看时针", size=34, color=ORANGE).move_to(LEFT * 0.9 + DOWN * 1.6)
        self.play(FadeIn(s1_icon), FadeIn(s1_text), run_time=0.5)

        s1_sub = self.txt("时针指着几，就是几时", size=24, color=GRAY_A
                          ).move_to(DOWN * 2.5)
        self.play(Write(s1_sub), run_time=0.5)

        # 演示时针指向8
        hh_demo = self.make_hour_hand(8, 0, color=ORANGE)
        self.play(Create(hh_demo), run_time=0.5)
        hl_8 = self.highlight_number(8, color=ORANGE)
        self.play(Create(hl_8), run_time=0.4)
        label_8 = self.txt("8时", size=28, color=ORANGE).move_to(LEFT * 3.3 + DOWN * 0.3)
        self.play(Write(label_8), run_time=0.4)
        self.wait(1.0)

        # ── 步骤2：再看分针 ──
        s2_icon = self.txt("②", size=34, color=TEAL).move_to(LEFT * 3.0 + DOWN * 3.5)
        s2_text = self.txt("再看分针", size=34, color=TEAL).move_to(LEFT * 0.9 + DOWN * 3.5)
        self.play(FadeIn(s2_icon), FadeIn(s2_text), run_time=0.5)

        s2_sub = self.txt("分针指着几，就是几×5分", size=24, color=GRAY_A
                          ).move_to(DOWN * 4.4)
        self.play(Write(s2_sub), run_time=0.5)

        # 演示分针指向9 → 9×5=45
        mh_demo = self.make_minute_hand(45, color=TEAL)
        self.play(Create(mh_demo), run_time=0.5)
        hl_9 = self.highlight_number(9, color=TEAL)
        self.play(Create(hl_9), run_time=0.4)

        calc = self.txt("9 × 5 = 45分", size=28, color=TEAL
                        ).move_to(RIGHT * 2.5 + DOWN * 0.2)
        self.play(Write(calc), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(s1_icon), FadeOut(s1_text), FadeOut(s1_sub),
            FadeOut(s2_icon), FadeOut(s2_text), FadeOut(s2_sub),
            FadeOut(hh_demo), FadeOut(mh_demo),
            FadeOut(hl_8), FadeOut(hl_9),
            FadeOut(label_8), FadeOut(calc),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 4：例题 8时45分
    # ──────────────────────────────────────────────
    def scene_4_example_845(self):
        title = self.txt("例：这是几时几分？", size=32, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        hh = self.make_hour_hand(8, 45)
        mh = self.make_minute_hand(45)
        self.play(Create(hh), Create(mh), run_time=0.7)
        self.wait(0.5)

        # ── 读时针 ──
        step1 = self.txt("① 先看时针", size=28, color=ORANGE).move_to(DOWN * 1.5)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Indicate(hh, color=ORANGE, scale_factor=1.15), run_time=0.6)

        hl8 = self.highlight_number(8, color=ORANGE)
        self.play(Create(hl8), run_time=0.4)

        h_note = self.txt("时针在8和9之间，是  8时", size=24, color=ORANGE
                          ).move_to(DOWN * 2.3)
        self.play(Write(h_note), run_time=0.6)
        self.wait(0.8)

        # ── 读分针 ──
        step2 = self.txt("② 再看分针", size=28, color=TEAL).move_to(DOWN * 3.2)
        self.play(FadeIn(step2), run_time=0.4)
        self.play(Indicate(mh, color=TEAL, scale_factor=1.1), run_time=0.6)

        hl9 = self.highlight_number(9, color=TEAL)
        self.play(Create(hl9), run_time=0.4)

        m_note = self.txt("分针指向9，9×5=45，是  45分", size=22, color=TEAL
                          ).move_to(DOWN * 4.0)
        self.play(Write(m_note), run_time=0.7)
        self.wait(0.8)

        # ── 答案 ──
        ans = self.answer_box("8时45分   /   8:45")
        self.play(FadeIn(ans[0]), Write(ans[1]), run_time=0.6)
        self.wait(2.2)

        self.play(
            FadeOut(title), FadeOut(hh), FadeOut(mh),
            FadeOut(step1), FadeOut(step2),
            FadeOut(hl8), FadeOut(hl9),
            FadeOut(h_note), FadeOut(m_note),
            FadeOut(ans),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 5：难点 8时06分
    # ──────────────────────────────────────────────
    def scene_5_example_806(self):
        title = self.txt("难点：分针不指数字怎么办？",
                         size=28, color=RED_B).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        hh = self.make_hour_hand(8, 6)
        mh = self.make_minute_hand(6)
        self.play(Create(hh), Create(mh), run_time=0.7)
        self.wait(0.5)

        # ── 读时针 ──
        step1 = self.txt("① 时针刚过8，是  8时", size=26, color=ORANGE
                         ).move_to(DOWN * 1.5)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Indicate(hh, color=ORANGE, scale_factor=1.15), run_time=0.5)
        self.wait(0.6)

        # ── 读分针 ──
        step2 = self.txt("② 分针不指数字，要数小格！", size=26, color=TEAL
                         ).move_to(DOWN * 2.4)
        self.play(FadeIn(step2), run_time=0.4)
        self.play(Indicate(mh, color=TEAL, scale_factor=1.1), run_time=0.5)

        # 从12开始逐格计数（前6格）
        count_dots = VGroup()
        for i in range(1, 7):
            a   = np.pi / 2 - i * np.pi / 30
            pos = self.cc + self.cr * 0.87 * np.array([np.cos(a), np.sin(a), 0])
            dot = Dot(pos, radius=0.1, color=YELLOW)
            count_dots.add(dot)

        count_label = self.txt("从12开始数：1、2、3、4、5、6",
                               size=22, color=YELLOW).move_to(DOWN * 3.3)
        self.play(Write(count_label), run_time=0.6)

        # 逐一出现点，带数字动效
        count_nums = VGroup()
        for i, dot in enumerate(count_dots, 1):
            num_lbl = self.txt(str(i), size=20, color=YELLOW
                               ).next_to(dot, RIGHT, buff=0.08)
            self.play(FadeIn(dot, scale=1.5), FadeIn(num_lbl), run_time=0.22)
            count_nums.add(num_lbl)

        self.wait(0.5)

        # 关键提示：06 不是 6
        tip = self.txt("6格 → 06分（个位要补0）", size=24, color=TEAL
                       ).move_to(DOWN * 4.3)
        self.play(Write(tip), run_time=0.6)
        self.wait(1.0)

        # 答案
        ans = self.answer_box("8时06分   /   8:06")
        self.play(FadeIn(ans[0]), Write(ans[1]), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(hh), FadeOut(mh),
            FadeOut(step1), FadeOut(step2),
            FadeOut(count_dots), FadeOut(count_nums),
            FadeOut(count_label), FadeOut(tip),
            FadeOut(ans),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 6：两种写法 + 口诀总结
    # ──────────────────────────────────────────────
    def scene_6_summary(self):
        title = self.txt("读时间口诀", size=40, color=GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 淡出表盘
        self.play(FadeOut(self.clock), run_time=0.4)

        # 背景卡
        card = RoundedRectangle(
            width=7.8, height=7.5, corner_radius=0.5,
            fill_color="#0f3460", fill_opacity=0.85,
            stroke_color=GOLD, stroke_width=2.5
        ).move_to(UP * 0.5)
        self.play(FadeIn(card), run_time=0.4)

        lines = [
            ("先看时针定几时",     ORANGE),
            ("再看分针定几分",     TEAL),
            ("指着数字 × 5 得分",  WHITE),
            ("不指数字数小格",     YELLOW),
            ("—— 两种写法 ——",    GRAY_A),
            ("文字式：8时45分",    WHITE),
            ("电子表式：8:45",     WHITE),
        ]

        texts = VGroup(*[
            self.txt(line, size=28, color=col) for line, col in lines
        ])
        texts.arrange(DOWN, buff=0.42).move_to(card)

        for t in texts:
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(2.2)

        self.play(
            FadeOut(title), FadeOut(card), FadeOut(texts),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # 场景 7：片尾
    # ──────────────────────────────────────────────
    def scene_7_outro(self):
        author_big = self.txt("上海初高中数学直通车", size=40, color=WHITE
                              ).move_to(UP * 1.5)
        author_id  = self.txt("@emptyandcalm", size=30, color=GRAY_B
                              ).move_to(UP * 0.5)

        self.play(Transform(self.author_bar, author_big), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)

        follow = self.txt("关注我，获得更多数学技巧！", size=30, color=YELLOW
                          ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 三个迷你时钟装饰
        mini_clocks = VGroup()
        positions = [LEFT * 2.8, ORIGIN, RIGHT * 2.8]
        times_demo = [(3, 0), (8, 45), (12, 30)]

        for pos, (h, m) in zip(positions, times_demo):
            center = pos + DOWN * 3.2
            r = 0.55
            face = Circle(radius=r, color=GOLD, stroke_width=2).move_to(center)

            # 小时针
            ha = clock_angle(hour=h, minute=m)
            hh = Line(center,
                      center + r * 0.55 * np.array([np.cos(ha), np.sin(ha), 0]),
                      stroke_width=3, color=ORANGE)
            # 小分针
            ma = clock_angle(minute=m, is_minute_hand=True)
            mh = Line(center,
                      center + r * 0.82 * np.array([np.cos(ma), np.sin(ma), 0]),
                      stroke_width=2, color=TEAL)

            mini_clocks.add(VGroup(face, hh, mh))

        self.play(*[FadeIn(mc, scale=0.4) for mc in mini_clocks], run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(mini_clocks),
            run_time=1.0
        )