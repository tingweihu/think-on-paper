"""Explicitly refresh public indexes after building the complete catalog."""

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from noteformats.safety import assert_safe_workspace, safe_project_path
from noteformats.catalog import VARIANTS
from noteformats.navigation import public_documents, write_if_changed
from noteformats.reviews import review_valid
from build import load_content

assert_safe_workspace(ROOT)
profile = json.loads((ROOT / "profiles/a5-draft.json").read_text(encoding="utf-8"))
catalog = list(csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline="")))
reviews = json.loads((ROOT / "content/visual-review.json").read_text(encoding="utf-8"))
for row in catalog:
    layout_id = row["id"]
    manifest = json.loads((ROOT / "templates" / layout_id / "manifest.json").read_text(encoding="utf-8"))
    if layout_id not in VARIANTS and not review_valid(ROOT, reviews.get(layout_id, {}), manifest["geometry_sha256"], profile):
        raise SystemExit(f"Review is stale: {layout_id}; public indexes preserved")
documents = public_documents(profile, catalog, load_content(profile))
changed = sum(write_if_changed(safe_project_path(ROOT, name), value) for name, value in documents.items())
print(f"public_documents={len(documents)} changed={changed}")
