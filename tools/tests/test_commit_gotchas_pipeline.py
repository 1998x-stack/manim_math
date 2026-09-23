"""Regression tests for commit inventory, AST TODO scanning and single-scene rendering."""
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import build_video, commit_gotchas


class GotchaScannerTests(unittest.TestCase):
    def test_known_historical_patterns_and_false_positives(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scene.py"
            source.write_text('''from manim import *
class Demo(Scene):
    def construct(self):
        Text("中文和30°")
        MathTex("角度30°")
        Sector(inner_radius=1)
        Rectangle(corner_radius=0.2)
        self.play(self.play(FadeIn(Dot())))
        self.play(FadeOut(Dot()) if True else [])
''', encoding="utf-8")
            rules = {item["rule"] for item in commit_gotchas.inspect_source(source, root)}
            self.assertEqual(rules, {"CHINESE_IN_TEX", "UNICODE_IN_TEX",
                                     "SECTOR_RADIUS_KEYWORD", "RECTANGLE_CORNER_RADIUS",
                                     "NESTED_PLAY", "PLAY_EMPTY_ANIMATION"})
            source.write_text('class Broken(:\n    pass\n', encoding="utf-8")
            self.assertEqual(commit_gotchas.inspect_source(source, root)[0]["rule"], "SYNTAX_ERROR")

    def test_batches_and_stale_source_reopen(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / "小学" / "一年级"
            folder.mkdir(parents=True)
            a = folder / "a.py"
            b = folder / "b.py"
            a.write_text('MathTex("30°")\n', encoding="utf-8")
            b.write_text('MathTex("中文")\n', encoding="utf-8")
            first = commit_gotchas.scan(root, batch=0, batch_size=1)
            self.assertEqual(first["total_python_files"], 2)
            self.assertEqual(first["total_batches"], 2)
            self.assertEqual(first["scanned_file_count"], 1)
            first["items"][0]["status"] = "verified"
            stable = commit_gotchas.scan(root, batch=0, batch_size=1, previous=first)
            self.assertEqual(stable["items"][0]["status"], "verified")
            second = commit_gotchas.scan(root, batch=1, batch_size=1, previous=stable)
            self.assertEqual(second["scanned_file_count"], 2)
            self.assertEqual(len(second["items"]), 2)
            a.write_text('MathTex("30°")\n# changed source\n', encoding="utf-8")
            reopened = commit_gotchas.scan(root, batch=0, batch_size=1, previous=second)
            self.assertEqual(reopened["items"][0]["status"], "needs_review")
            self.assertEqual(reopened["scanned_file_count"], 2)

    def test_history_collects_real_changed_filenames(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.run(["git", "-C", str(root), *args], check=True,
                                      capture_output=True, text=True)
            git("init", "-q")
            git("config", "user.email", "ci@example.invalid")
            git("config", "user.name", "CI")
            (root / "数学.py").write_text("print(1)\n", encoding="utf-8")
            git("add", ".")
            git("commit", "-qm", "fix(math): repair sample")
            with patch.object(commit_gotchas, "ROOT", root):
                result = commit_gotchas.mine_history()
            self.assertEqual(result["scanned_commits"], 1)
            self.assertIn("数学.py", result["fix_related_commits"][0]["changed_files"])
            self.assertEqual(result["touched_files"]["数学.py"], 1)


class VideoPipelineTests(unittest.TestCase):
    def test_scene_validation_and_repo_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scene.py"
            source.write_text("class Demo:\n    pass\n", encoding="utf-8")
            with patch.object(build_video, "ROOT", root):
                build_video.validate_scene(source, "Demo")
                with self.assertRaises(ValueError):
                    build_video.validate_scene(source, "Demo;rm")
                with self.assertRaises(ValueError):
                    build_video.inside_repo("../escape.py", must_exist=False)

    def test_success_replaces_only_final_output_and_cleans_intermediates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "scene.py"
            source.write_text("class Demo:\n    pass\n", encoding="utf-8")
            original = root / "scene.mp4"
            original.write_bytes(b"old-video")
            def fake_run(command, **kwargs):
                if "--media_dir" in command:
                    media = Path(command[command.index("--media_dir") + 1])
                    (media / "videos").mkdir(parents=True)
                    (media / "videos" / "built.mp4").write_bytes(b"new-video")
                return subprocess.CompletedProcess(command, 0)
            with patch.object(build_video, "ROOT", root), \
                 patch.object(build_video, "provision_env", return_value=root / "python"), \
                 patch.object(build_video.subprocess, "run", side_effect=fake_run):
                with self.assertRaises(FileExistsError):
                    build_video.build("scene.py", "Demo")
                result = build_video.build("scene.py", "Demo", force=True)
            self.assertEqual(result.read_bytes(), b"new-video")
            self.assertEqual(list(root.glob(".manim-build-*")), [])

    def test_failed_render_keeps_previous_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scene.py").write_text("class Demo:\n    pass\n", encoding="utf-8")
            original = root / "scene.mp4"
            original.write_bytes(b"keep-me")
            with patch.object(build_video, "ROOT", root), \
                 patch.object(build_video, "provision_env", return_value=root / "python"), \
                 patch.object(build_video.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "manim")):
                with self.assertRaises(subprocess.CalledProcessError):
                    build_video.build("scene.py", "Demo", force=True)
            self.assertEqual(original.read_bytes(), b"keep-me")
            self.assertEqual(list(root.glob(".manim-build-*")), [])


if __name__ == "__main__":
    unittest.main()
