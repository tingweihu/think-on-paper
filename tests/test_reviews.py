"""Review seals survive encoding changes and invalidate design changes."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from PIL import Image, PngImagePlugin
from noteformats.reviews import appearance_digest, pixel_digest, review_valid


class ReviewIdentityTests(unittest.TestCase):
    def test_encoding_is_not_visual_identity(self):
        (ROOT / "reports").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / "reports") as temporary:
            root = Path(temporary).resolve()
            evidence = root / "evidence.png"
            Image.new("RGB", (20, 30), "white").save(evidence, compress_level=0)
            profile = json.loads((ROOT / "profiles/a5-draft.json").read_text())
            note = {"date": "2026-10-30", "finding": "Recorded review", "evidence": "evidence.png",
                    "geometry_sha256": "geometry", "appearance_sha256": appearance_digest(profile),
                    "evidence_pixel_sha256": pixel_digest(evidence)}
            previous = evidence.read_bytes()
            metadata = PngImagePlugin.PngInfo()
            metadata.add_text("encoder", "different encoder metadata")
            Image.new("RGB", (20, 30), "white").save(evidence, compress_level=9, pnginfo=metadata)
            self.assertNotEqual(previous, evidence.read_bytes())
            self.assertTrue(review_valid(root, note, "geometry", profile))
            self.assertFalse(review_valid(root, note, "changed geometry", profile))
            altered = {**profile, "ink": {**profile["ink"], "light": "#737373"}}
            self.assertFalse(review_valid(root, note, "geometry", altered))
            Image.new("RGB", (20, 30), "black").save(evidence)
            self.assertFalse(review_valid(root, note, "geometry", profile))


if __name__ == "__main__":
    unittest.main()
