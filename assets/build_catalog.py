#!/usr/bin/env python3
"""Scan the manim_math repo and emit assets/catalog.json."""

import ast
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

GRADE_ORDER = {
    "一年级": 1, "二年级": 2, "三年级": 3, "四年级": 4,
    "五年级": 5, "六年级": 6, "七年级": 7, "八年级": 8,
    "九年级": 9, "高一": 10, "高二": 11, "高三": 12,
}

SEMESTER_ORDER = {"上册": 1, "下册": 2, "第一学期": 1, "第二学期": 2}

CHAPTER_NUM_RE = re.compile(r"第([一二三四五六七八九十百千万零\d]+)章")
CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
           "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
           "十一": 11, "十二": 12, "十三": 13, "十四": 14,
           "十五": 15, "十六": 16, "十七": 17, "十八": 18,
           "十九": 19, "二十": 20, "二十一": 21, "二十二": 22,
           "二十三": 23, "二十四": 24, "二十五": 25, "二十六": 26,
           "二十七": 27, "二十八": 28}


def cn_to_int(s: str) -> int:
    if s.isdigit():
        return int(s)
    return CN_NUM.get(s, 99)


def chapter_sort_key(name: str) -> int:
    m = CHAPTER_NUM_RE.search(name)
    return cn_to_int(m.group(1)) if m else 99


def extract_docstring(py_path: Path) -> str:
    try:
        source = py_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(source)
        ds = ast.get_docstring(tree)
        if ds:
            return ds.strip()
    except SyntaxError:
        m = re.search(r'"""(.*?)"""', py_path.read_text(encoding="utf-8", errors="replace"), re.DOTALL)
        if m:
            return m.group(1).strip()
    return ""


def find_video(topic_dir: Path) -> str | None:
    mp4s = list(topic_dir.glob("*.mp4"))
    finish = [f for f in mp4s if f.stem.endswith("_finish")]
    if finish:
        return str(finish[0].relative_to(ROOT))
    if mp4s:
        return str(mp4s[0].relative_to(ROOT))
    return None


def find_scene_py(topic_dir: Path) -> Path | None:
    pys = [f for f in topic_dir.glob("*.py")
           if not f.name.startswith(("verify_", "test_", "__"))]
    return pys[0] if pys else None


def topic_id(path_str: str) -> str:
    return hashlib.md5(path_str.encode()).hexdigest()[:10]


def extract_topic_number(name: str) -> str:
    m = re.match(r"(\d+)", name)
    return m.group(1) if m else ""


def extract_topic_name(dirname: str) -> str:
    return re.sub(r"^\d+", "", dirname).strip("_- ")


def scan_curriculum_level(level_dir: Path, level_id: str, level_name: str) -> dict:
    level = {"id": level_id, "name": level_name, "grades": []}
    if not level_dir.exists():
        return level

    grade_dirs = sorted(level_dir.iterdir(), key=lambda d: GRADE_ORDER.get(d.name, 99))
    for grade_dir in grade_dirs:
        if not grade_dir.is_dir():
            continue
        grade = {"name": grade_dir.name, "semesters": []}

        sem_dirs = sorted(grade_dir.iterdir(), key=lambda d: SEMESTER_ORDER.get(d.name, 99))
        for sem_dir in sem_dirs:
            if not sem_dir.is_dir():
                continue
            semester = {"name": sem_dir.name, "chapters": []}

            chap_dirs = sorted(sem_dir.iterdir(), key=lambda d: chapter_sort_key(d.name))
            for chap_dir in chap_dirs:
                if not chap_dir.is_dir():
                    continue
                chapter_short = re.sub(r"^第[一二三四五六七八九十百千万零\d]+章[-—]?", "", chap_dir.name).strip()
                chapter = {
                    "name": chap_dir.name,
                    "chapterShort": chapter_short or chap_dir.name,
                    "topics": [],
                }

                topic_dirs = sorted(chap_dir.iterdir(), key=lambda d: d.name)
                for topic_dir in topic_dirs:
                    if not topic_dir.is_dir():
                        continue
                    py_file = find_scene_py(topic_dir)
                    if py_file is None:
                        continue

                    rel_path = str(topic_dir.relative_to(ROOT))
                    video = find_video(topic_dir)
                    docstring = extract_docstring(py_file)

                    chapter["topics"].append({
                        "id": topic_id(rel_path),
                        "number": extract_topic_number(topic_dir.name),
                        "name": extract_topic_name(topic_dir.name) or topic_dir.name,
                        "docstring": docstring,
                        "pyFile": str(py_file.relative_to(ROOT)),
                        "videoFile": video,
                        "hasVideo": video is not None,
                    })

                if chapter["topics"]:
                    semester["chapters"].append(chapter)

            if semester["chapters"]:
                grade["semesters"].append(semester)

        if grade["semesters"]:
            level["grades"].append(grade)

    return level


def find_scene_class(py_path: Path) -> str | None:
    try:
        source = py_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                return node.name
    except SyntaxError:
        pass
    return None


def scan_external(ext_dir: Path) -> dict:
    level = {"id": "external", "name": "External", "grades": []}
    if not ext_dir.exists():
        return level

    all_mp4s = {mp4.stem: mp4 for mp4 in ext_dir.glob("*.mp4")}

    topics = []
    pys = sorted(ext_dir.glob("*.py"))
    for py_file in pys:
        if py_file.name.startswith(("verify_", "test_", "__")):
            continue
        stem = py_file.stem
        class_name = find_scene_class(py_file)

        video = None
        for candidate in [stem, class_name]:
            if candidate is None:
                continue
            finish_key = f"{candidate}_finish"
            if finish_key in all_mp4s:
                video = str(all_mp4s[finish_key].relative_to(ROOT))
                break
            if candidate in all_mp4s:
                video = str(all_mp4s[candidate].relative_to(ROOT))
                break
        if video is None:
            for mp4_stem, mp4_path in all_mp4s.items():
                if stem.lower().replace("_", "") in mp4_stem.lower():
                    if mp4_stem.endswith("_finish"):
                        video = str(mp4_path.relative_to(ROOT))
                        break
            if video is None:
                for mp4_stem, mp4_path in all_mp4s.items():
                    if stem.lower().replace("_", "") in mp4_stem.lower():
                        video = str(mp4_path.relative_to(ROOT))
                        break

        docstring = extract_docstring(py_file)
        topics.append({
            "id": topic_id(str(py_file.relative_to(ROOT))),
            "number": "",
            "name": stem.replace("_", " ").title(),
            "docstring": docstring,
            "pyFile": str(py_file.relative_to(ROOT)),
            "videoFile": video,
            "hasVideo": video is not None,
        })

    if topics:
        level["grades"] = [{
            "name": "Advanced Geometry",
            "semesters": [{
                "name": "",
                "chapters": [{
                    "name": "Geometry Explorations",
                    "chapterShort": "Geometry Explorations",
                    "topics": topics,
                }],
            }],
        }]

    return level


def compute_stats(levels: list[dict]) -> dict:
    total_topics = 0
    total_with_video = 0
    per_level = {}
    for lv in levels:
        count = 0
        with_vid = 0
        for g in lv["grades"]:
            for s in g["semesters"]:
                for c in s["chapters"]:
                    for t in c["topics"]:
                        count += 1
                        if t["hasVideo"]:
                            with_vid += 1
        per_level[lv["id"]] = {"total": count, "withVideo": with_vid}
        total_topics += count
        total_with_video += with_vid
    return {"totalTopics": total_topics, "totalWithVideo": total_with_video, "perLevel": per_level}


def main():
    levels = [
        scan_curriculum_level(ROOT / "小学", "xiaoxue", "小学"),
        scan_curriculum_level(ROOT / "初中", "chuzhong", "初中"),
        scan_curriculum_level(ROOT / "高中", "gaozhong", "高中"),
        scan_external(ROOT / "external"),
    ]
    stats = compute_stats(levels)
    catalog = {"levels": levels, "stats": stats}

    out = ROOT / "assets" / "catalog.json"
    out.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out} — {stats['totalTopics']} topics, {stats['totalWithVideo']} with video")


if __name__ == "__main__":
    main()
