"""Verify that music muxing is isolated and never damages the previous deliverable."""
from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools import build_video


class MusicMuxTests(unittest.TestCase):
    def test_music_mux_replaces_audio_only_on_success(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scene.py").write_text("class Demo:\n    pass\n", encoding="utf-8")
            (root / "licensed.mp3").write_bytes(b"audio")
            original = root / "scene.mp4"
            original.write_bytes(b"previous-release")
            calls = []
            def fake_run(command, **kwargs):
                calls.append(command)
                if "--media_dir" in command:
                    media = Path(command[command.index("--media_dir") + 1])
                    media.mkdir(parents=True)
                    (media / "built.mp4").write_bytes(b"rendered-video")
                elif "-stream_loop" in command:
                    Path(command[-1]).write_bytes(b"video-with-new-music")
                return subprocess.CompletedProcess(command, 0)
            with patch.object(build_video, "ROOT", root), \
                 patch.object(build_video, "provision_env", return_value=root / "python"), \
                 patch.object(build_video, "require_executable", return_value="ffmpeg"), \
                 patch.object(build_video.subprocess, "run", side_effect=fake_run):
                build_video.build("scene.py", "Demo", music="licensed.mp3", force=True)
            self.assertEqual(original.read_bytes(), b"video-with-new-music")
            command = calls[1]
            self.assertEqual([command[i + 1] for i, arg in enumerate(command[:-1]) if arg == "-map"],
                             ["0:v:0", "1:a:0"])
            self.assertIn("-shortest", command)
            self.assertEqual(list(root.glob(".manim-build-*")), [])

    def test_mux_failure_keeps_previous_release(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "scene.py").write_text("class Demo:\n    pass\n", encoding="utf-8")
            (root / "licensed.mp3").write_bytes(b"audio")
            output = root / "scene.mp4"
            output.write_bytes(b"previous-release")
            def fake_run(command, **kwargs):
                if "--media_dir" in command:
                    media = Path(command[command.index("--media_dir") + 1])
                    media.mkdir(parents=True)
                    (media / "built.mp4").write_bytes(b"rendered-video")
                else:
                    raise subprocess.CalledProcessError(1, "ffmpeg")
                return subprocess.CompletedProcess(command, 0)
            with patch.object(build_video, "ROOT", root), \
                 patch.object(build_video, "provision_env", return_value=root / "python"), \
                 patch.object(build_video, "require_executable", return_value="ffmpeg"), \
                 patch.object(build_video.subprocess, "run", side_effect=fake_run):
                with self.assertRaises(subprocess.CalledProcessError):
                    build_video.build("scene.py", "Demo", music="licensed.mp3", force=True)
            self.assertEqual(output.read_bytes(), b"previous-release")
            self.assertEqual(list(root.glob(".manim-build-*")), [])


if __name__ == "__main__":
    unittest.main()
