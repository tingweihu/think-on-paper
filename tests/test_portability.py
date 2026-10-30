"""Local, in-project portability and output-boundary smoke tests."""

from __future__ import annotations

import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from noteformats.safety import safe_project_path


class PortableCheckoutTests(unittest.TestCase):
    def test_output_path_rejects_traversal_and_absolute_path(self):
        for value in ("../escape.svg", "templates/../../escape.pdf", str(ROOT / "escape.png"),
                      "C:drive-relative.pdf", "\\root-relative.pdf"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                safe_project_path(ROOT, value)
        self.assertEqual(safe_project_path(ROOT, "templates/example/blank.pdf"), ROOT / "templates/example/blank.pdf")

    def test_rebuild_from_different_in_project_checkout(self):
        # The fixture stays within this task's authorized root. It is the only
        # directory this test creates and removes.
        fixture = ROOT / "reports" / ".portable-fixture"
        resolved = fixture.resolve(strict=False)
        (ROOT / "reports").mkdir(exist_ok=True)
        report_root = (ROOT / "reports").resolve(strict=True)
        self.assertEqual(resolved.parent, report_root)
        self.assertFalse(fixture.exists(), "Refusing to replace an existing fixture")
        try:
            fixture.mkdir()
            for name in ("src", "scripts", "content", "profiles"):
                shutil.copytree(ROOT / name, fixture / name,
                                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            shutil.copy2(ROOT / "catalog-144.csv", fixture / "catalog-144.csv")
            completed = subprocess.run(
                [sys.executable, "-B", "scripts/build.py", "--ids", "blank", "three-columns",
                 "crazy-eight", "problem-solution-three"],
                cwd=fixture, capture_output=True, text=True, check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            for layout_id in ("blank", "three-columns", "crazy-eight", "problem-solution-three"):
                for name in ("blank.svg", "blank.pdf"):
                    self.assertTrue((fixture / "templates" / layout_id / "exports" / "a5-draft" / name).is_file())
                self.assertTrue((fixture / "templates" / layout_id / "previews" / "a5-draft.png").is_file())
        finally:
            # Verify the resolved deletion target immediately before cleanup.
            if fixture.exists():
                self.assertEqual(fixture.resolve(strict=True).parent, report_root)
                shutil.rmtree(fixture)

    def test_output_path_rejects_linked_component(self):
        # Simulate a linked component without creating a link to any external
        # location in the authorized workspace.
        with patch("noteformats.safety._linked", side_effect=lambda path: Path(path).name == "linked"):
            with self.assertRaises(ValueError):
                safe_project_path(ROOT, "templates/linked/blank.pdf")


if __name__ == "__main__":
    unittest.main()
