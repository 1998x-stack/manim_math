"""
计数单位与数位顺序表 - Place Value Units and Number Position Table
四年级第一学期 第二章：大数的认识

内容: 计数单位（个、十、百、千、万...亿），数位顺序表，四位一级
目标观众: 四年级学生
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


class PlaceValueLesson(Scene):
    """
    计数单位与数位顺序表教学动画

    场景顺序:
    1. 开场钩子
    2. 认识计数单位（个→十→百→千）
    3. 万级计数单位
    4. 亿级计数单位
    5. 完整数位顺序表
    6. 四位一级的分级
    7. 进率关系 10倍
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_GE_JI = "#4fc3f7"      # 个级 - 浅蓝
        self.COLOR_WAN_JI = "#81c784"      # 万级 - 浅绿
        self.COLOR_YI_JI = "#ffb74d"       # 亿级 - 橙色
        self.COLOR_HIGHLIGHT = "#ffd54f"   # 高亮黄
        self.COLOR_TITLE = "#e0e0e0"
        self.COLOR_BODY = "#b0bec5"
        self.COLOR_ACCENT = "#f48fb1"      # 粉红强调

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_ge_ji()
        self.scene_3_wan_ji()
        self.scene_4_yi_ji()
        self.scene_5_full_table()
        self.scene_6_si_wei_yi_ji()
        self.scene_7_jin_lv()
        self.scene_8_outro()

    # ─────────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.add(author)
        self.author = author

        # 钩子问题
        hook_line1 = Text(
            "你知道",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_TITLE,
        )
        hook_line2 = Text(
            "1后面9个0",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
        )
        hook_line3 = Text(
            "是多少吗？",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_TITLE,
        )
        hook = VGroup(hook_line1, hook_line2, hook_line3).arrange(DOWN, buff=0.3)
        hook.move_to(UP * 4.5)

        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(hook_line1), run_time=0.5)
        self.play(Write(hook_line2), run_time=0.7)
        self.play(Write(hook_line3), run_time=0.5)
        self.wait(0.5)

        # 显示数字
        big_num = Text(
            "1,000,000,000",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_ACCENT,
        ).move_to(UP * 1.8)
        num_label = Text(
            "十亿！",
            font="PingFang SC",
            font_size=56,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.5)

        self.play(FadeIn(big_num, shift=UP * 0.3), run_time=0.6)
        self.play(Write(num_label), run_time=0.6)
        self.wait(0.4)

        # 主题
        subtitle = Text(
            "今天我们来学习",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_BODY,
        ).move_to(DOWN * 1.0)
        title_main = Text(
            "计数单位与数位顺序表",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.0)

        self.play(FadeIn(subtitle), run_time=0.4)
        self.play(Write(title_main), run_time=0.8)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(hook),
            FadeOut(big_num),
            FadeOut(num_label),
            FadeOut(subtitle),
            FadeOut(title_main),
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # 场景 2: 个级计数单位
    # ─────────────────────────────────────────────
    def scene_2_ge_ji(self):
        section_title = Text(
            "第一步：个级计数单位",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_GE_JI,
        ).move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.6)

        # 介绍语
        intro = Text(
            "我们已经认识了这些计数单位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_BODY,
        ).move_to(UP * 5.0)
        self.play(FadeIn(intro), run_time=0.4)

        # 个、十、百、千 四个方块逐一出现
        units = ["个", "十", "百", "千"]
        unit_colors = ["#4fc3f7", "#29b6f6", "#039be5", "#0277bd"]

        ge_group = VGroup()
        for u, c in zip(units, unit_colors):
            box = RoundedRectangle(
                width=1.6,
                height=1.6,
                corner_radius=0.15,
                fill_color=c,
                fill_opacity=0.25,
                stroke_color=c,
                stroke_width=2.5,
            )
            lbl = Text(u, font="PingFang SC", font_size=36, color=c)
            lbl.move_to(box.get_center())
            ge_group.add(VGroup(box, lbl))

        ge_group.arrange(RIGHT, buff=0.35)
        ge_group.move_to(UP * 3.2)

        # 逐个出现
        for g in ge_group:
            self.play(GrowFromCenter(g), run_time=0.4)

        self.wait(0.3)

        # 进率箭头
        arrows = VGroup()
        arrow_labels = VGroup()
        for i in range(3):
            left_box = ge_group[i][0]
            right_box = ge_group[i + 1][0]
            mid_y = ge_group.get_center()[1] - 1.1

            arr = Arrow(
                start=np.array([left_box.get_center()[0], mid_y, 0]),
                end=np.array([right_box.get_center()[0], mid_y, 0]),
                buff=0,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            )
            arr_lbl = Text(
                "x10", font="PingFang SC", font_size=20, color=self.COLOR_HIGHLIGHT
            ).next_to(arr, DOWN, buff=0.08)
            arrows.add(arr)
            arrow_labels.add(arr_lbl)

        self.play(
            LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.2),
            run_time=0.8,
        )
        self.play(
            LaggedStart(*[FadeIn(al) for al in arrow_labels], lag_ratio=0.2),
            run_time=0.5,
        )

        # 说明文字
        explain1 = Text(
            "10个一 = 1个十",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.2)
        explain2 = Text(
            "10个十 = 1个百",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.4)
        explain3 = Text(
            "10个百 = 1个千",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.4)

        self.play(Write(explain1), run_time=0.5)
        self.play(Write(explain2), run_time=0.5)
        self.play(Write(explain3), run_time=0.5)
        self.wait(1.0)

        # 底部提示
        note = Text(
            "这四个是个级的计数单位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_GE_JI,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # 保留方块组，其余清理
        self.play(
            FadeOut(section_title),
            FadeOut(intro),
            FadeOut(arrows),
            FadeOut(arrow_labels),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(explain3),
            FadeOut(note),
            run_time=0.5,
        )

        # 缩小个级方块，移到上方
        self.ge_group = ge_group
        self.play(
            ge_group.animate.scale(0.75).move_to(UP * 5.0),
            run_time=0.6,
        )

        # 添加"个级"标签
        ge_ji_label = Text(
            "个级", font="PingFang SC", font_size=22, color=self.COLOR_GE_JI
        ).next_to(ge_group, LEFT, buff=0.3)
        self.play(FadeIn(ge_ji_label), run_time=0.3)
        self.ge_ji_label = ge_ji_label

    # ─────────────────────────────────────────────
    # 场景 3: 万级计数单位
    # ─────────────────────────────────────────────
    def scene_3_wan_ji(self):
        section_title = Text(
            "第二步：认识万级",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_WAN_JI,
        ).move_to(UP * 3.8)
        self.play(Write(section_title), run_time=0.6)

        intro = Text(
            "10个千 = 1个万，继续往上…",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_BODY,
        ).move_to(UP * 3.0)
        self.play(FadeIn(intro), run_time=0.4)

        # 万级四个方块
        wan_units = ["万", "十万", "百万", "千万"]
        wan_colors = ["#81c784", "#66bb6a", "#43a047", "#2e7d32"]

        wan_group = VGroup()
        for u, c in zip(wan_units, wan_colors):
            box = RoundedRectangle(
                width=1.6,
                height=1.6,
                corner_radius=0.15,
                fill_color=c,
                fill_opacity=0.25,
                stroke_color=c,
                stroke_width=2.5,
            )
            lbl = Text(u, font="PingFang SC", font_size=30, color=c)
            lbl.move_to(box.get_center())
            wan_group.add(VGroup(box, lbl))

        wan_group.arrange(RIGHT, buff=0.35)
        wan_group.move_to(UP * 1.8)

        # 先只显示"万"
        self.play(GrowFromCenter(wan_group[0]), run_time=0.5)

        # 提示：10个千=1个万
        tip1 = Text(
            "10个千 = 1个万",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 0.5)
        self.play(Write(tip1), run_time=0.5)
        self.wait(0.4)
        self.play(FadeOut(tip1), run_time=0.3)

        # 继续出现其他万级单位
        for g in wan_group[1:]:
            self.play(GrowFromCenter(g), run_time=0.4)

        self.wait(0.3)

        # 万级进率箭头
        wan_arrows = VGroup()
        wan_arr_labels = VGroup()
        for i in range(3):
            lb = wan_group[i][0]
            rb = wan_group[i + 1][0]
            mid_y = wan_group.get_center()[1] - 1.1
            arr = Arrow(
                start=np.array([lb.get_center()[0], mid_y, 0]),
                end=np.array([rb.get_center()[0], mid_y, 0]),
                buff=0,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            )
            arr_lbl = Text(
                "x10", font="PingFang SC", font_size=20, color=self.COLOR_HIGHLIGHT
            ).next_to(arr, DOWN, buff=0.08)
            wan_arrows.add(arr)
            wan_arr_labels.add(arr_lbl)

        self.play(Create(wan_arrows), run_time=0.6)
        self.play(FadeIn(wan_arr_labels), run_time=0.4)
        self.wait(0.5)

        # 说明
        explain = Text(
            "万、十万、百万、千万\n都是万级的计数单位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_WAN_JI,
        ).move_to(DOWN * 1.0)
        self.play(Write(explain), run_time=0.7)
        self.wait(1.0)

        # 清理，移动
        self.play(
            FadeOut(section_title),
            FadeOut(intro),
            FadeOut(wan_arrows),
            FadeOut(wan_arr_labels),
            FadeOut(explain),
            run_time=0.5,
        )

        self.wan_group = wan_group
        self.play(
            wan_group.animate.scale(0.75).move_to(UP * 3.7),
            run_time=0.6,
        )
        wan_ji_label = Text(
            "万级", font="PingFang SC", font_size=22, color=self.COLOR_WAN_JI
        ).next_to(wan_group, LEFT, buff=0.3)
        self.play(FadeIn(wan_ji_label), run_time=0.3)
        self.wan_ji_label = wan_ji_label

        # 同时把个级也往上移动
        self.play(
            self.ge_group.animate.move_to(UP * 5.5),
            run_time=0.4,
        )
        self.ge_ji_label.next_to(self.ge_group, LEFT, buff=0.15)

    # ─────────────────────────────────────────────
    # 场景 4: 亿级计数单位
    # ─────────────────────────────────────────────
    def scene_4_yi_ji(self):
        section_title = Text(
            "第三步：认识亿级",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_YI_JI,
        ).move_to(UP * 2.4)
        self.play(Write(section_title), run_time=0.6)

        intro = Text(
            "10个千万 = 1个亿！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.6)
        self.play(Write(intro), run_time=0.5)
        self.wait(0.3)

        # 亿级四个方块
        yi_units = ["亿", "十亿", "百亿", "千亿"]
        yi_colors = ["#ffb74d", "#ffa726", "#fb8c00", "#e65100"]

        yi_group = VGroup()
        for u, c in zip(yi_units, yi_colors):
            box = RoundedRectangle(
                width=1.6,
                height=1.6,
                corner_radius=0.15,
                fill_color=c,
                fill_opacity=0.25,
                stroke_color=c,
                stroke_width=2.5,
            )
            lbl = Text(u, font="PingFang SC", font_size=30, color=c)
            lbl.move_to(box.get_center())
            yi_group.add(VGroup(box, lbl))

        yi_group.arrange(RIGHT, buff=0.35)
        yi_group.move_to(UP * 0.4)

        for g in yi_group:
            self.play(GrowFromCenter(g), run_time=0.4)

        self.wait(0.3)

        # 亿级进率
        yi_arrows = VGroup()
        yi_arr_labels = VGroup()
        for i in range(3):
            lb = yi_group[i][0]
            rb = yi_group[i + 1][0]
            mid_y = yi_group.get_center()[1] - 1.1
            arr = Arrow(
                start=np.array([lb.get_center()[0], mid_y, 0]),
                end=np.array([rb.get_center()[0], mid_y, 0]),
                buff=0,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            )
            arr_lbl = Text(
                "x10", font="PingFang SC", font_size=20, color=self.COLOR_HIGHLIGHT
            ).next_to(arr, DOWN, buff=0.08)
            yi_arrows.add(arr)
            yi_arr_labels.add(arr_lbl)

        self.play(Create(yi_arrows), run_time=0.5)
        self.play(FadeIn(yi_arr_labels), run_time=0.4)

        explain = Text(
            "亿、十亿、百亿、千亿\n是亿级的计数单位",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_YI_JI,
        ).move_to(DOWN * 1.5)
        self.play(Write(explain), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(section_title),
            FadeOut(intro),
            FadeOut(yi_arrows),
            FadeOut(yi_arr_labels),
            FadeOut(explain),
            run_time=0.5,
        )

        self.yi_group = yi_group
        self.play(
            yi_group.animate.scale(0.75).move_to(UP * 2.0),
            run_time=0.6,
        )
        yi_ji_label = Text(
            "亿级", font="PingFang SC", font_size=22, color=self.COLOR_YI_JI
        ).next_to(yi_group, LEFT, buff=0.3)
        self.play(FadeIn(yi_ji_label), run_time=0.3)
        self.yi_ji_label = yi_ji_label

        # 调整已有的组位置
        self.play(
            self.ge_group.animate.move_to(UP * 6.5),
            self.wan_group.animate.move_to(UP * 4.2),
            run_time=0.5,
        )
        self.ge_ji_label.next_to(self.ge_group, LEFT, buff=0.15)
        self.wan_ji_label.next_to(self.wan_group, LEFT, buff=0.15)

    # ─────────────────────────────────────────────
    # 场景 5: 完整数位顺序表
    # ─────────────────────────────────────────────
    def scene_5_full_table(self):
        # 清空屏幕，重新建立完整数位表
        self.play(
            FadeOut(self.ge_group),
            FadeOut(self.ge_ji_label),
            FadeOut(self.wan_group),
            FadeOut(self.wan_ji_label),
            FadeOut(self.yi_group),
            FadeOut(self.yi_ji_label),
            run_time=0.6,
        )

        title = Text(
            "数位顺序表",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 完整数位：从高到低 千亿→个
        col_names = ["千亿", "百亿", "十亿", "亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        col_units = ["千亿", "百亿", "十亿", "亿", "千万", "百万", "十万", "万", "千", "百", "十", "一"]
        col_levels = [self.COLOR_YI_JI] * 4 + [self.COLOR_WAN_JI] * 4 + [self.COLOR_GE_JI] * 4

        # 表格尺寸参数
        col_w = 0.68
        row_h = 0.90
        n_cols = 12
        total_w = col_w * n_cols
        start_x = -total_w / 2 + col_w / 2
        table_top_y = 5.2   # y坐标（逻辑单位）

        # 级别行 y
        level_y_val = table_top_y
        # 数位名称行 y
        name_y_val = table_top_y - row_h
        # 计数单位行 y
        unit_y_val = table_top_y - row_h * 2.0

        # 级别背景 (三个大色块)
        level_bg_yi = Rectangle(
            width=col_w * 4,
            height=row_h * 0.85,
            fill_color=self.COLOR_YI_JI,
            fill_opacity=0.18,
            stroke_color=self.COLOR_YI_JI,
            stroke_width=1.5,
        ).move_to(np.array([start_x + col_w * 1.5, level_y_val, 0]))

        level_bg_wan = Rectangle(
            width=col_w * 4,
            height=row_h * 0.85,
            fill_color=self.COLOR_WAN_JI,
            fill_opacity=0.18,
            stroke_color=self.COLOR_WAN_JI,
            stroke_width=1.5,
        ).move_to(np.array([start_x + col_w * 5.5, level_y_val, 0]))

        level_bg_ge = Rectangle(
            width=col_w * 4,
            height=row_h * 0.85,
            fill_color=self.COLOR_GE_JI,
            fill_opacity=0.18,
            stroke_color=self.COLOR_GE_JI,
            stroke_width=1.5,
        ).move_to(np.array([start_x + col_w * 9.5, level_y_val, 0]))

        yi_lbl = Text(
            "亿级", font="PingFang SC", font_size=22, color=self.COLOR_YI_JI
        ).move_to(level_bg_yi.get_center())
        wan_lbl = Text(
            "万级", font="PingFang SC", font_size=22, color=self.COLOR_WAN_JI
        ).move_to(level_bg_wan.get_center())
        ge_lbl = Text(
            "个级", font="PingFang SC", font_size=22, color=self.COLOR_GE_JI
        ).move_to(level_bg_ge.get_center())

        level_row = VGroup(
            level_bg_yi, level_bg_wan, level_bg_ge,
            yi_lbl, wan_lbl, ge_lbl,
        )

        self.play(
            FadeIn(level_bg_yi), FadeIn(level_bg_wan), FadeIn(level_bg_ge),
            Write(yi_lbl), Write(wan_lbl), Write(ge_lbl),
            run_time=0.8,
        )

        # 数位名称行 (每列一个格子)
        name_cells = VGroup()
        name_texts = VGroup()
        for i, (name, color) in enumerate(zip(col_names, col_levels)):
            x = start_x + col_w * i
            cell = Rectangle(
                width=col_w * 0.95,
                height=row_h * 0.85,
                fill_color=color,
                fill_opacity=0.12,
                stroke_color=color,
                stroke_width=1.2,
            ).move_to(np.array([x, name_y_val, 0]))
            txt = Text(
                name, font="PingFang SC", font_size=17, color=color
            ).move_to(cell.get_center())
            name_cells.add(cell)
            name_texts.add(txt)

        self.play(
            LaggedStart(
                *[GrowFromCenter(c) for c in name_cells],
                lag_ratio=0.05,
            ),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                *[Write(t) for t in name_texts],
                lag_ratio=0.05,
            ),
            run_time=0.8,
        )

        # 计数单位行
        unit_cells = VGroup()
        unit_texts = VGroup()
        for i, (u, color) in enumerate(zip(col_units, col_levels)):
            x = start_x + col_w * i
            cell = Rectangle(
                width=col_w * 0.95,
                height=row_h * 0.85,
                fill_color=color,
                fill_opacity=0.08,
                stroke_color=color,
                stroke_width=1.2,
            ).move_to(np.array([x, unit_y_val, 0]))
            txt = Text(
                u, font="PingFang SC", font_size=16, color=color
            ).move_to(cell.get_center())
            unit_cells.add(cell)
            unit_texts.add(txt)

        self.play(
            LaggedStart(
                *[GrowFromCenter(c) for c in unit_cells],
                lag_ratio=0.05,
            ),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                *[Write(t) for t in unit_texts],
                lag_ratio=0.05,
            ),
            run_time=0.8,
        )

        self.wait(1.0)

        # 行标签
        row_label_name = Text(
            "数位", font="PingFang SC", font_size=19, color=self.COLOR_BODY
        ).next_to(name_cells[0], LEFT, buff=0.12)
        row_label_unit = Text(
            "计数\n单位", font="PingFang SC", font_size=15, color=self.COLOR_BODY
        ).next_to(unit_cells[0], LEFT, buff=0.05)

        self.play(FadeIn(row_label_name), FadeIn(row_label_unit), run_time=0.4)
        self.wait(1.5)

        # 保存引用
        self.table_elements = VGroup(
            level_row, name_cells, name_texts, unit_cells, unit_texts,
            row_label_name, row_label_unit, title,
        )
        self.level_row = level_row
        self.name_cells = name_cells
        self.name_texts = name_texts
        self.unit_cells = unit_cells
        self.unit_texts = unit_texts
        self.row_label_name = row_label_name
        self.row_label_unit = row_label_unit
        self.table_title = title

        # 记录参数
        self.col_w = col_w
        self.row_h = row_h
        self.start_x = start_x
        self.level_y_val = level_y_val
        self.name_y_val = name_y_val
        self.unit_y_val = unit_y_val

    # ─────────────────────────────────────────────
    # 场景 6: 四位一级
    # ─────────────────────────────────────────────
    def scene_6_si_wei_yi_ji(self):
        section_title = Text(
            "四位一级",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.2)
        self.play(Write(section_title), run_time=0.6)

        explain = Text(
            "每4个数位为一级",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_BODY,
        ).move_to(DOWN * 2.1)
        self.play(FadeIn(explain), run_time=0.4)

        # 高亮个级 (最右边4列，索引8-11)
        highlight_ge = SurroundingRectangle(
            VGroup(self.name_cells[8], self.name_cells[11]),
            color=self.COLOR_GE_JI,
            stroke_width=3,
            buff=0.05,
        )
        self.play(Create(highlight_ge), run_time=0.5)

        tip_ge = Text(
            "个、十、百、千 → 个级（4个）",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_GE_JI,
        ).move_to(DOWN * 3.2)
        self.play(Write(tip_ge), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(highlight_ge), FadeOut(tip_ge), run_time=0.4)

        # 高亮万级 (索引4-7)
        highlight_wan = SurroundingRectangle(
            VGroup(self.name_cells[4], self.name_cells[7]),
            color=self.COLOR_WAN_JI,
            stroke_width=3,
            buff=0.05,
        )
        self.play(Create(highlight_wan), run_time=0.5)

        tip_wan = Text(
            "万、十万、百万、千万 → 万级（4个）",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_WAN_JI,
        ).move_to(DOWN * 3.2)
        self.play(Write(tip_wan), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(highlight_wan), FadeOut(tip_wan), run_time=0.4)

        # 高亮亿级 (索引0-3)
        highlight_yi = SurroundingRectangle(
            VGroup(self.name_cells[0], self.name_cells[3]),
            color=self.COLOR_YI_JI,
            stroke_width=3,
            buff=0.05,
        )
        self.play(Create(highlight_yi), run_time=0.5)

        tip_yi = Text(
            "亿、十亿、百亿、千亿 → 亿级（4个）",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_YI_JI,
        ).move_to(DOWN * 3.2)
        self.play(Write(tip_yi), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(highlight_yi), FadeOut(tip_yi), run_time=0.4)

        # 总结
        summary = Text(
            "记住：四位一级！",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.2)
        self.play(Write(summary), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(section_title),
            FadeOut(explain),
            FadeOut(summary),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 7: 进率关系
    # ─────────────────────────────────────────────
    def scene_7_jin_lv(self):
        section_title = Text(
            "相邻计数单位的进率",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 1.0)
        self.play(Write(section_title), run_time=0.6)

        rule = Text(
            "相邻计数单位之间的进率是",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_BODY,
        ).move_to(DOWN * 2.0)
        rule_num = Text(
            "10",
            font="PingFang SC",
            font_size=72,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(rule), run_time=0.4)
        self.play(GrowFromCenter(rule_num), run_time=0.7)
        self.wait(0.4)

        # 在数位名称行上方用小箭头表示 x10（从低位到高位）
        mini_arrows = VGroup()
        for i in range(11):
            # 从右到左：低位→高位
            x_low = self.start_x + self.col_w * (11 - i)
            x_high = self.start_x + self.col_w * (11 - i - 1)
            arr = Arrow(
                start=np.array([x_low - self.col_w * 0.25, self.name_y_val + 0.55, 0]),
                end=np.array([x_high + self.col_w * 0.25, self.name_y_val + 0.55, 0]),
                buff=0,
                color=self.COLOR_HIGHLIGHT,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.3,
            )
            mini_arrows.add(arr)

        self.play(
            LaggedStart(*[Create(a) for a in mini_arrows], lag_ratio=0.04),
            run_time=1.2,
        )

        times10_label = Text(
            "每向左一位 x10",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(times10_label), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(section_title),
            FadeOut(rule),
            FadeOut(rule_num),
            FadeOut(mini_arrows),
            FadeOut(times10_label),
            run_time=0.6,
        )

        # 清空整个表格
        self.play(
            FadeOut(self.table_elements),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # 场景 8: 片尾
    # ─────────────────────────────────────────────
    def scene_8_outro(self):
        # 总结卡片
        summary_title = Text(
            "今天学了什么？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 5.0)
        self.play(Write(summary_title), run_time=0.6)

        points = [
            ("个级", "个、十、百、千", self.COLOR_GE_JI),
            ("万级", "万、十万、百万、千万", self.COLOR_WAN_JI),
            ("亿级", "亿、十亿、百亿、千亿", self.COLOR_YI_JI),
            ("四位一级", "每4个数位构成一级", self.COLOR_HIGHLIGHT),
            ("进率", "相邻计数单位进率为10", self.COLOR_ACCENT),
        ]

        point_groups = VGroup()
        for key, val, color in points:
            dot = Circle(
                radius=0.12,
                fill_color=color,
                fill_opacity=1,
                stroke_width=0,
            )
            key_text = Text(
                key + "：",
                font="PingFang SC",
                font_size=24,
                color=color,
            )
            val_text = Text(
                val,
                font="PingFang SC",
                font_size=22,
                color=self.COLOR_BODY,
            )
            row = VGroup(dot, key_text, val_text).arrange(RIGHT, buff=0.2)
            point_groups.add(row)

        point_groups.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        point_groups.move_to(UP * 2.5)

        for pg in point_groups:
            self.play(FadeIn(pg, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.0)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(DOWN * 3.0)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color="#6b7280",
        ).next_to(author_big, DOWN, buff=0.3)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).next_to(author_id, DOWN, buff=0.5)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 小装饰：三个彩色圆
        deco = VGroup(
            Circle(radius=0.18, fill_color=self.COLOR_GE_JI, fill_opacity=0.9, stroke_width=0).shift(LEFT * 1.5),
            Circle(radius=0.18, fill_color=self.COLOR_WAN_JI, fill_opacity=0.9, stroke_width=0),
            Circle(radius=0.18, fill_color=self.COLOR_YI_JI, fill_opacity=0.9, stroke_width=0).shift(RIGHT * 1.5),
        ).move_to(DOWN * 6.2)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in deco], lag_ratio=0.2),
            run_time=0.6,
        )
        self.wait(2.0)

        self.play(
            FadeOut(summary_title),
            FadeOut(point_groups),
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco),
            run_time=1.0,
        )
