# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Manim-based math education video** repository producing short-form vertical videos (TikTok format, 1080x1920) for the Shanghai curriculum (沪教版/五四制). All animations target Chinese-speaking students from elementary through high school.

The brand is **上海初高中数学直通车 @emptyandcalm**.

## Rendering a Scene

```bash
# Render a single scene (produces media/ output alongside the .py file)
manim -pqh path/to/scene.py SceneClassName

# Render at production quality (1080x1920 vertical)
manim -qh --resolution 1080,1920 path/to/scene.py SceneClassName
```

Every scene file sets its own resolution via `config.pixel_width = 1080` / `config.pixel_height = 1920` at module level, so omitting `--resolution` usually works.

## Utility Scripts

```bash
# Add background music (files/Away.mp3) to all .mp4 files, producing *_finish.mp4 variants
./concat_mp4.sh

# Find all *_finish.mp4 files and write file:// links to finish_mp4_paths.md
./find_finish_mp4.sh

# Remove all __pycache__ and media/ directories recursively
./clean_pycache.sh
```

## Repository Structure

```
小学/          Elementary school (grades 1-6, 上册/下册 or 第一学期/第二学期)
初中/          Middle school (grades 6-9, 第一学期/第二学期)
高中/          High school (grades 10-12, 第一学期/第二学期)
external/      Standalone geometry animations (Euler line, nine-point circle, etc.)
videos/        Pre-rendered output videos (both raw and *_finish.mp4 with music)
files/         Assets: background music, curriculum JSON, architecture scripts
docs/          Curriculum outlines, prompt templates, geometry reference sheets
skills/        Skill files for manim, ffmpeg, sympy (compressed archives)
```

**Curriculum path convention:**
`{level}/{grade}/{semester}/{chapter}/{topic}/scene.py`

Example: `初中/七年级/第一学期/第九章-整式/001代数式与整式的概念/algebraic_expression.py`

Each topic folder typically contains a single Python file with one `Scene` subclass.

## Scene File Conventions

All scene files follow this pattern:

- **Module docstring** in Chinese describing the math topic, target audience, and video duration
- **Global config** block setting `config.pixel_width = 1080`, `config.pixel_height = 1920`, `config.frame_width = 9`, `config.frame_height = 16`
- **One Scene subclass** with a `construct()` method that runs the full animation sequence
- **Color scheme constants** defined as instance attributes in `construct()`
- **Author watermark** at the top: `"上海初高中数学直通车 @emptyandcalm"`

## Critical Manim Pitfalls

These are the most frequent sources of bugs in this codebase:

1. **Chinese text in MathTex causes LaTeX errors.** `MathTex` only accepts pure LaTeX. All Chinese text must use `Text(font="PingFang SC")` or `Text(font="Noto Sans CJK SC")` and be composed via `VGroup().arrange(RIGHT)`.

2. **Angle direction matters.** `Angle.from_three_points` defaults to counter-clockwise. For angles > 180°, you almost certainly need `other_angle=True`.

3. **Boundary checking.** With the vertical 9x16 frame, elements easily overflow. The safe area is roughly ±4 horizontally and ±7.5 vertically. Always verify positioning.

4. **Geometry precision.** For geometry-heavy scenes (external/), use helper classes (like `GeometryCalculator` in euler_line.py) to compute circumcenters, orthocenters, etc. with numpy. Verify collinearity and distances numerically before animating.

## Verification Workflow

Before considering a scene complete:

1. Write a `verify_geometry.py` (numpy only, no manim) with:
   - `verify_angles()` — check angle magnitudes and directions
   - `grep_MathTex()` — scan for Chinese characters inside MathTex calls
   - `verify_boundaries()` — confirm all positioned elements stay within frame
2. Run verification, fix issues, then render with manim.

## Dependencies

- **manim** (Community Edition)
- **numpy** (used extensively for geometry calculations)
- **ffmpeg** (for rendering and the concat_mp4.sh music overlay)
- **LaTeX** (BasicTeX on macOS; needs `collection-fontsrecommended` and CJK font packages)
- **System fonts**: PingFang SC or Noto Sans CJK SC for Chinese text rendering
