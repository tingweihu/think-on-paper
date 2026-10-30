"""Seal recorded reviews to geometry, appearance and evidence pixels."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from noteformats.safety import assert_safe_workspace
from noteformats.reviews import appearance_digest, pixel_digest
from noteformats.navigation import write_if_changed
assert_safe_workspace(ROOT)
profile = json.loads((ROOT / "profiles/a5-draft.json").read_text(encoding="utf-8"))
reviews_path = ROOT / "content/visual-review.json"
reviews = json.loads(reviews_path.read_text(encoding="utf-8"))
for layout_id, note in reviews.items():
    manifest = json.loads((ROOT / "templates" / layout_id / "manifest.json").read_text(encoding="utf-8"))
    preview = ROOT / "templates" / layout_id / "previews/a5-draft.png"
    evidence = (ROOT / note["evidence"]).resolve()
    if ROOT not in evidence.parents or not evidence.is_file():
        raise RuntimeError(f"Missing review evidence: {layout_id}")
    current = {"geometry_sha256": manifest["geometry_sha256"],
               "appearance_sha256": appearance_digest(profile),
               "evidence_pixel_sha256": pixel_digest(evidence)}
    if not note.get("date") or not note.get("finding"):
        raise RuntimeError(f"Review date or finding missing: {layout_id}")
    for key, digest in current.items():
        if key in note and note[key] != digest:
            raise RuntimeError(f"Review is stale: {layout_id}/{key}; inspect before approving")
    # One-time migration requires the exact previously sealed files. It cannot
    # silently approve new geometry, colors or a different evidence image.
    for key, path in (("preview_sha256", preview), ("evidence_sha256", evidence)):
        if key in note and note[key] != hashlib.sha256(path.read_bytes()).hexdigest():
            raise RuntimeError(f"Legacy seal mismatch: {layout_id}/{key}")
    note.update(current)
    note.setdefault("preview_pixel_sha256", pixel_digest(preview))
    note["review_basis"] = "geometry-and-appearance-v1"
    note.pop("preview_sha256", None)
    note.pop("evidence_sha256", None)
write_if_changed(reviews_path, json.dumps(reviews, ensure_ascii=False, indent=2) + "\n")
print(f"Sealed {len(reviews)} recorded visual reviews")
