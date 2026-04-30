"""
圆柱认识 - 一年级上册第三章认识图形（一）
目标受众: 一年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

知识点: 圆柱的特征
- 上下两个面是平平的、大小相同的圆形
- 侧面是弯曲的曲面，可以滚动
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CylinderLesson(Scene):
    """
    圆柱认识教学动画

    场景顺序:
    1. 开场 - 钩子问题
    2. 认识圆柱外形（2D近似展示）
    3. 上下底面是圆形
    4. 侧面是曲面，可以滚动
    5. 总结特征
    6. 结尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_CYLINDER_SIDE = "#4a90d9"
        self.COLOR_CYLINDER_TOP = "#7ec8e3"
        self.COLOR_CYLINDER_BOTTOM = "#5aa0c0"
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_TEXT = WHITE
        self.COLOR_SUBTEXT = "#b0b8c8"
        self.COLOR_CIRCLE = "#f0a030"
        self.COLOR_CURVE = "#e74c3c"

        self.scene_1_opening()
        self.scene_2_show_cylinder()
        self.scene_3_top_bottom_circles()
        self.scene_4_rolling_side()
        self.scene_5_summary()
        self.scene_6_outro()

    # ─── 辅助函数：构建2D圆柱图形 ──────────────────────────────────────────

    def build_cylinder_2d(self, center, width=3.2, height=3.8,
                          color_side=None, color_top=None, color_bottom=None):
        """
        用2D元素近似圆柱:
        - 矩形作为侧面
        - 上/下椭圆作为底面
        返回 (VGroup, side_rect, bottom_ell, top_ell)
        """
        if color_side is None:
            color_side = self.COLOR_CYLINDER_SIDE
        if color_top is None:
            color_top = self.COLOR_CYLINDER_TOP
        if color_bottom is None:
            color_bottom = self.COLOR_CYLINDER_BOTTOM

        cx, cy, _ = center
        half_h = height / 2
        ellipse_ry = width * 0.22  # 椭圆短轴

        # 侧面矩形
        side_rect = Rectangle(
            width=width, height=height,
            fill_color=color_side,
            fill_opacity=0.85,
            stroke_color=color_side,
            stroke_width=2,
        ).move_to(center)

        # 底部椭圆
        bottom_ell = Ellipse(
            width=width, height=ellipse_ry * 2,
            fill_color=color_bottom,
            fill_opacity=1.0,
            stroke_color=WHITE,
            stroke_width=2.5,
        ).move_to(np.array([cx, cy - half_h, 0]))

        # 顶部椭圆
        top_ell = Ellipse(
            width=width, height=ellipse_ry * 2,
            fill_color=color_top,
            fill_opacity=1.0,
            stroke_color=WHITE,
            stroke_width=2.5,
        ).move_to(np.array([cx, cy + half_h, 0]))

        group = VGroup(side_rect, bottom_ell, top_ell)
        return group, side_rect, bottom_ell, top_ell

    # ─── 场景1: 开场 ───────────────────────────────────────────────────────

    def scene_1_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.add(author)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "你见过这个形状吗？",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        # 展示几个实物名称
        items = VGroup(
            Text("茶叶罐", font="PingFang SC", font_size=28, color=self.COLOR_SUBTEXT),
            Text("易拉罐", font="PingFang SC", font_size=28, color=self.COLOR_SUBTEXT),
            Text("蜡  烛", font="PingFang SC", font_size=28, color=self.COLOR_SUBTEXT),
        ).arrange(RIGHT, buff=0.8).move_to(UP * 4.5)
        self.play(FadeIn(items, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        reveal = Text(
            "它们都是圆柱！",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_TEXT,
        ).move_to(UP * 3.3)
        self.play(Write(reveal), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(hook), FadeOut(items), FadeOut(reveal), run_time=0.5)
        self.author = author

    # ─── 场景2: 展示圆柱 ──────────────────────────────────────────────────

    def scene_2_show_cylinder(self):
        title = Text(
            "认识圆柱",
            font="PingFang SC",
            font_size=46,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.7)

        # 构建圆柱，放在画面中央偏上
        cyl_center = np.array([0, 1.0, 0])
        group, side_rect, bottom_ell, top_ell = self.build_cylinder_2d(
            cyl_center, width=3.2, height=3.8
        )

        self.play(FadeIn(side_rect), run_time=0.5)
        self.play(Create(bottom_ell), run_time=0.6)
        self.play(Create(top_ell), run_time=0.6)

        # 标注"圆柱"
        label = Text("圆柱", font="PingFang SC", font_size=38, color=GOLD)
        label.move_to(np.array([2.8, 1.0, 0]))
        arrow = Arrow(
            start=np.array([2.3, 1.0, 0]),
            end=np.array([1.7, 1.0, 0]),
            color=GOLD,
            buff=0.05,
        )
        self.play(FadeIn(label), Create(arrow), run_time=0.6)
        self.wait(1.0)

        # 轻微弹动以强调立体感
        self.play(group.animate.scale(1.05), run_time=0.4, rate_func=there_and_back)
        self.wait(0.5)

        self.play(FadeOut(label), FadeOut(arrow), run_time=0.4)

        self.title_scene2 = title
        self.cyl_group = group
        self.cyl_side = side_rect
        self.cyl_bottom = bottom_ell
        self.cyl_top = top_ell
        self.cyl_center = cyl_center
        self.cyl_width = 3.2
        self.cyl_height = 3.8

    # ─── 场景3: 上下底面是圆形 ─────────────────────────────────────────────

    def scene_3_top_bottom_circles(self):
        new_title = Text(
            "两个底面是圆形",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.title_scene2, new_title), run_time=0.5)

        cx, cy, _ = self.cyl_center
        half_h = self.cyl_height / 2

        # 高亮顶面
        top_hl = self.cyl_top.copy().set_stroke(color=self.COLOR_CIRCLE, width=5)
        self.play(Create(top_hl), run_time=0.5)

        label_top = Text(
            "顶面（圆形）",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_CIRCLE,
        ).move_to(np.array([0, cy + half_h + 0.75, 0]))
        self.play(FadeIn(label_top, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 高亮底面
        bot_hl = self.cyl_bottom.copy().set_stroke(color=self.COLOR_CIRCLE, width=5)
        self.play(Create(bot_hl), run_time=0.5)

        label_bot = Text(
            "底面（圆形）",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_CIRCLE,
        ).move_to(np.array([0, cy - half_h - 0.75, 0]))
        self.play(FadeIn(label_bot, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.5)

        # 说明文字
        desc1 = Text(
            "上下各有一个平平的圆形",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TEXT,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(desc1), run_time=0.4)

        same_size = Text(
            "大小完全相同！",
            font="PingFang SC",
            font_size=32,
            color=YELLOW,
        ).move_to(DOWN * 4.6)
        self.play(Write(same_size), run_time=0.6)
        self.wait(1.2)

        # 双箭头显示两个圆一样大
        arr_eq = DoubleArrow(
            start=np.array([-1.9, cy + half_h, 0]),
            end=np.array([-1.9, cy - half_h, 0]),
            color=YELLOW,
            buff=0.05,
            stroke_width=3,
        )
        arr_eq_label = Text(
            "同样大",
            font="PingFang SC",
            font_size=22,
            color=YELLOW,
        ).next_to(arr_eq, LEFT, buff=0.12)
        self.play(Create(arr_eq), FadeIn(arr_eq_label), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(top_hl), FadeOut(bot_hl),
            FadeOut(label_top), FadeOut(label_bot),
            FadeOut(desc1), FadeOut(same_size),
            FadeOut(arr_eq), FadeOut(arr_eq_label),
            run_time=0.5,
        )
        self.title_scene3 = new_title

    # ─── 场景4: 侧面是曲面，可以滚动 ──────────────────────────────────────

    def scene_4_rolling_side(self):
        new_title = Text(
            "侧面是曲面，能滚动",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.title_scene3, new_title), run_time=0.5)

        cx, cy, _ = self.cyl_center
        half_h = self.cyl_height / 2

        # 高亮侧面
        side_hl = self.cyl_side.copy().set_stroke(color=self.COLOR_CURVE, width=5)
        self.play(Create(side_hl), run_time=0.5)

        label_side = Text(
            "侧面（弯曲的曲面）",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_CURVE,
        ).move_to(np.array([0, cy - half_h - 1.2, 0]))
        self.play(FadeIn(label_side, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.6)

        # 用弧线强调弯曲
        # half_h = cyl_height/2 = 1.9, so radius must be > 1.9
        curve_left = ArcBetweenPoints(
            start=np.array([cx - self.cyl_width / 2, cy + half_h, 0]),
            end=np.array([cx - self.cyl_width / 2, cy - half_h, 0]),
            radius=-2.5,
            color=self.COLOR_CURVE,
            stroke_width=5,
        )
        curve_right = ArcBetweenPoints(
            start=np.array([cx + self.cyl_width / 2, cy + half_h, 0]),
            end=np.array([cx + self.cyl_width / 2, cy - half_h, 0]),
            radius=2.5,
            color=self.COLOR_CURVE,
            stroke_width=5,
        )
        curved_label = Text(
            "← 弯弯的！",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_CURVE,
        ).move_to(np.array([-3.0, cy, 0]))

        self.play(Create(curve_left), Create(curve_right), run_time=0.7)
        self.play(FadeIn(curved_label), run_time=0.4)
        self.wait(0.6)

        self.play(
            FadeOut(side_hl), FadeOut(curve_left),
            FadeOut(curve_right), FadeOut(curved_label),
            run_time=0.4,
        )

        # 滚动演示
        roll_title = Text(
            "圆柱可以滚动！",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(roll_title, shift=UP * 0.3), run_time=0.5)

        # 地面线
        ground_y = cy - half_h - 0.02
        ground = Line(
            start=np.array([-4.0, ground_y, 0]),
            end=np.array([4.0, ground_y, 0]),
            color=GRAY_B,
            stroke_width=2,
        )
        self.play(Create(ground), run_time=0.3)

        # 圆柱滚动（平移模拟）
        self.play(self.cyl_group.animate.shift(RIGHT * 2.0), run_time=1.2, rate_func=smooth)
        self.play(self.cyl_group.animate.shift(LEFT * 2.0), run_time=1.2, rate_func=smooth)
        self.wait(0.5)

        no_roll = Text(
            "正方体就不能滚动哦～",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUBTEXT,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(no_roll), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(label_side), FadeOut(roll_title),
            FadeOut(no_roll), FadeOut(ground),
            run_time=0.5,
        )
        self.title_scene4 = new_title

    # ─── 场景5: 总结 ──────────────────────────────────────────────────────

    def scene_5_summary(self):
        # 圆柱缩小移到上方
        self.play(
            self.cyl_group.animate.scale(0.55).move_to(UP * 3.5),
            run_time=0.8,
        )

        new_title = Text(
            "圆柱的特征",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.8)
        self.play(ReplacementTransform(self.title_scene4, new_title), run_time=0.5)

        # 四条特征逐一展示
        def make_feat(num_str, body_str, num_color, body_color, pos):
            num_t = Text(num_str, font="PingFang SC", font_size=30, color=num_color)
            body_t = Text(body_str, font="PingFang SC", font_size=28, color=body_color)
            return VGroup(num_t, body_t).arrange(RIGHT, buff=0.3).move_to(pos)

        feat1 = make_feat("①", "2个底面  是圆形", self.COLOR_CIRCLE, self.COLOR_TEXT, UP * 1.5)
        feat2 = make_feat("②", "两底面  大小相同", self.COLOR_CIRCLE, self.COLOR_TEXT, UP * 0.5)
        feat3 = make_feat("③", "侧面  弯曲的曲面", self.COLOR_CURVE, self.COLOR_TEXT, DOWN * 0.5)
        feat4 = make_feat("④", "可以  滚动！", YELLOW, self.COLOR_TEXT, DOWN * 1.5)

        for feat in [feat1, feat2, feat3, feat4]:
            self.play(FadeIn(feat, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        self.wait(1.0)

        # 闪烁圆柱
        self.play(
            Flash(self.cyl_group.get_center(), color=YELLOW, flash_radius=1.2),
            run_time=0.5,
        )

        # 口诀
        rhyme = Text(
            "两圆底，侧面弯，放倒就能滚！",
            font="PingFang SC",
            font_size=30,
            color=GOLD,
        ).move_to(DOWN * 3.2)
        self.play(Write(rhyme), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(new_title),
            FadeOut(feat1), FadeOut(feat2), FadeOut(feat3), FadeOut(feat4),
            FadeOut(rhyme),
            FadeOut(self.cyl_group),
            run_time=0.6,
        )

    # ─── 场景6: 结尾 ──────────────────────────────────────────────────────

    def scene_6_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(ReplacementTransform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 三个小圆柱装饰
        def mini_cyl(pos):
            g, _, _, _ = self.build_cylinder_2d(
                pos, width=1.0, height=1.4
            )
            return g

        mini1 = mini_cyl(np.array([-2.0, -2.5, 0]))
        mini2 = mini_cyl(np.array([0.0, -2.5, 0]))
        mini3 = mini_cyl(np.array([2.0, -2.5, 0]))

        self.play(
            FadeIn(mini1, scale=0.5),
            FadeIn(mini2, scale=0.5),
            FadeIn(mini3, scale=0.5),
            run_time=0.7,
        )

        card_text = Text(
            "圆柱：两个圆形底 + 一个曲面侧",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SUBTEXT,
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(card_text), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(mini1), FadeOut(mini2), FadeOut(mini3),
            FadeOut(card_text),
            run_time=1.0,
        )
        self.wait(0.5)
