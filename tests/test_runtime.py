"""Missing local tools are setup failures, not 144 format failures."""

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from noteformats.runtime import require_pdf_renderer, RendererUnavailable


class RendererPreflightTests(unittest.TestCase):
    def test_missing_renderer_has_actionable_error(self):
        with patch("noteformats.runtime.shutil.which", return_value=None):
            with self.assertRaisesRegex(RendererUnavailable, "--pdftoppm"):
                require_pdf_renderer()

    def test_explicit_renderer_path_is_passed_as_one_argument(self):
        executable = "tool directory/pdftoppm"
        with patch("noteformats.runtime.shutil.which", return_value=executable), patch(
            "noteformats.runtime.subprocess.run",
            return_value=subprocess.CompletedProcess([executable, "-v"], 0, "", "pdftoppm version test"),
        ) as run:
            self.assertEqual(require_pdf_renderer(executable), executable)
            self.assertEqual(run.call_args.args[0], [executable, "-v"])

    def test_missing_renderer_preserves_reports_and_public_outputs(self):
        paths = [ROOT / "reports" / name for name in ("STATUS.md", "QA.md", "CATALOG-STATUS.csv", "qa-results.json")]
        paths += [ROOT / "README.md", ROOT / "docs/zh-TW/catalog.md",
                  ROOT / "templates/blank/exports/a5-draft/blank.svg",
                  ROOT / "templates/blank/exports/a5-draft/blank.pdf"]
        before = {path: path.read_bytes() if path.exists() else None for path in paths}
        missing = ROOT / "reports" / "missing-renderer-for-test"
        self.assertFalse(missing.exists())
        for script, extra in (("qa.py", []), ("build.py", ["--ids", "blank"])):
            result = subprocess.run(
                [sys.executable, "-B", "scripts/" + script, *extra, "--pdftoppm", str(missing)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            self.assertIn("prerequisite missing", result.stderr)
            self.assertNotIn("FAIL blank", result.stdout)
            self.assertLess(len(result.stderr.splitlines()), 4)
            self.assertEqual(before, {path: path.read_bytes() if path.exists() else None for path in paths})


if __name__ == "__main__":
    unittest.main()
