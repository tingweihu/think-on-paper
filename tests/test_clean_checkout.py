"""Regression tests in a public-file-only checkout inside this project."""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, PngImagePlugin

ROOT = Path(__file__).resolve().parents[1]


class CleanCheckoutTests(unittest.TestCase):
    def test_clean_checkout_encoding_and_failed_qa(self):
        report_root = ROOT / "reports"
        report_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="checkout-", dir=report_root) as temporary:
            fixture = Path(temporary).resolve()
            self.assertEqual(fixture.parent, report_root.resolve())
            ignored = (ROOT / ".gitignore").read_text().splitlines()
            for path in ROOT.iterdir():
                if path.is_file() and path.suffix != ".zip" and f"/{path.name}" not in ignored:
                    shutil.copy2(path, fixture / path.name)
            for name in ("src", "scripts", "content", "profiles", "templates", "docs", "tests"):
                shutil.copytree(ROOT / name, fixture / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

            def run(*arguments, success=True):
                process = subprocess.run([sys.executable, "-B", *arguments], cwd=fixture,
                                         capture_output=True, text=True)
                self.assertEqual(process.returncode == 0, success, process.stdout + process.stderr)
                return process

            def clear_reports():
                target = fixture / "reports"
                if target.exists():
                    self.assertEqual(target.resolve().parent, fixture)
                    shutil.rmtree(target)

            # Every command starts without ignored reports, in arbitrary order.
            for script in ("release_check.py", "audit_docs.py", "audit_examples.py", "audit_layouts.py", "audit_sources.py"):
                clear_reports()
                if script == "audit_sources.py":
                    cache = fixture / "reports" / "nested-checkout"
                    cache.mkdir(parents=True)
                    Image.new("RGB", (1, 1), "white").save(cache / "local-preview.png")
                    (cache / "local-font.ttf").write_bytes(b"local test cache")
                    (cache / "local-photo.jpg").write_bytes(b"local test cache")
                run("scripts/" + script)
                if script == "audit_sources.py":
                    # Excluding private caches must not hide an unknown public asset.
                    unexpected = fixture / "docs" / "unexpected-preview.png"
                    unexpected.write_bytes((cache / "local-preview.png").read_bytes())
                    try:
                        result = run("scripts/" + script, success=False)
                        self.assertIn("docs/unexpected-preview.png", result.stderr)
                    finally:
                        unexpected.unlink()
            clear_reports()
            run("-m", "unittest", "discover", "-s", "tests", "-p", "test_portability.py")
            public = list(fixture.glob("*.md")) + list((fixture / "docs").rglob("*.md")) + list((fixture / "templates").rglob("*.md"))
            before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in public}

            # Different compression + metadata, identical decoded pixels.
            for path in list((fixture / "templates").rglob("*.png")) + list((fixture / "docs/visual-evidence").glob("*.png")):
                with Image.open(path) as image:
                    pixels = image.convert("RGB")
                meta = PngImagePlugin.PngInfo()
                meta.add_text("encoder", "encoding-only regression")
                pixels.save(path, compress_level=1, pnginfo=meta)
            run("scripts/seal_reviews.py")
            run("scripts/qa.py")
            self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in public})

            # Actual output corruption must fail without editing any public file.
            svg = fixture / "templates/quadrant/exports/a5-draft/blank.svg"
            original = svg.read_bytes()
            svg.write_bytes(original + b"<!-- changed output -->")
            run("scripts/qa.py", success=False)
            self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in public})
            svg.write_bytes(original)

            # A style change cannot silently refresh public indexes or reviews.
            profile_path = fixture / "profiles/a5-draft.json"
            profile = json.loads(profile_path.read_text())
            profile["ink"]["light"] = "#111111"
            profile_path.write_text(json.dumps(profile))
            run("scripts/generate_docs.py", success=False)
            self.assertEqual(before, {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in public})


if __name__ == "__main__":
    unittest.main()
