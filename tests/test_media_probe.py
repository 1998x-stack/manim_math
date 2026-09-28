import unittest

from tools.media_probe import parse_rate, validate_probe


class TestMediaProbe(unittest.TestCase):
    def test_fractional_frame_rate(self):
        self.assertAlmostEqual(29.97, parse_rate("30000/1001"), places=2)

    def test_valid_media_probe(self):
        data = {
            "streams": [{
                "codec_type": "video",
                "width": 270,
                "height": 480,
                "r_frame_rate": "30/1",
            }],
            "format": {"duration": "12.5"},
        }
        self.assertEqual([], validate_probe(data, 270, 480))

    def test_dimensions_are_hard_gate(self):
        data = {
            "streams": [{
                "codec_type": "video",
                "width": 480,
                "height": 270,
                "r_frame_rate": "30/1",
            }],
            "format": {"duration": "2.0"},
        }
        errors = validate_probe(data, 270, 480)
        self.assertTrue(any("width" in error for error in errors))
        self.assertTrue(any("height" in error for error in errors))

    def test_missing_video_stream_fails(self):
        self.assertEqual(["no video stream found"], validate_probe({"streams": [], "format": {}}, 270, 480))

    def test_zero_fps_and_duration_fail(self):
        data = {
            "streams": [{
                "codec_type": "video",
                "width": 270,
                "height": 480,
                "r_frame_rate": "0/1",
            }],
            "format": {"duration": "0"},
        }
        errors = validate_probe(data, 270, 480)
        self.assertTrue(any("frame rate" in error for error in errors))
        self.assertTrue(any("duration" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
