"""Audit the current catalog, geometry groups, capacities and variant links."""

import csv
import json
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from noteformats.safety import assert_safe_workspace, safe_project_path
from noteformats.catalog import VARIANTS, counts, geometry_groups
from noteformats.geometry import Scene
from noteformats.registry import BUILDERS
from noteformats.reviews import geometry_digest
from build import load_content

assert_safe_workspace(ROOT)
safe_project_path(ROOT, "reports").mkdir(exist_ok=True)
profile = json.loads((ROOT / "profiles/a5-draft.json").read_text(encoding="utf-8"))
content = load_content(profile)
catalog = {row["id"]: row for row in csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline=""))}
groups = geometry_groups(profile)
reviews, capacity, variants = [], [], []

def write_csv(name, rows):
    with safe_project_path(ROOT, "reports/" + name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

for layout_id, builder in BUILDERS.items():
    item = content[layout_id]
    scene = Scene.from_profile(profile)
    builder(scene, profile)
    digest = geometry_digest(scene)
    relation = VARIANTS.get(layout_id, {})
    reviews.append({
        "id": layout_id, "family": catalog[layout_id]["family"],
        "classification": relation.get("classification", "base"),
        "geometry_sha256": digest, "same_geometry_ids": ";".join(groups[digest]),
        "geometry_structure": item["source_note"],
        "main_writing_behavior": item["translations"]["en"]["purpose"],
        "core_scenario": item["translations"]["en"]["when"][0],
        "variant_of": relation.get("target", ""),
        "difference_or_reason": relation.get("reason", item["source_note"]),
    })
    boxes = [shape.values for shape in scene.shapes if shape.kind == "rect"]
    smallest = min(boxes, key=lambda b: b[2]*b[3]) if boxes else None
    capacity.append({"id": layout_id, "safe_bounds_pass": "PASS" if scene.bounds_ok(tolerance=.001,safe=True) else "FAIL",
                     "shape_count": len(scene.shapes),
                     "smallest_rect_width_mm": round(smallest[2],2) if smallest else "",
                     "smallest_rect_height_mm": round(smallest[3],2) if smallest else "",
                     "narrowest_example_slot_mm": min((slot[2] for slot in scene.slots),default="")})
    if relation:
        variants.append({"id": layout_id, **relation, "same_geometry_ids": ";".join(groups[digest]),
                         "stable_id_output": "PASS" if (ROOT / "templates" / layout_id / "manifest.json").is_file() else "MISSING"})
write_csv("FORMAT-REVIEW.csv", reviews)
write_csv("A5-CAPACITY.csv", capacity)
write_csv("VARIANT-REVIEW.csv", variants)
print(f"catalog={len(reviews)} {counts(profile)} variant_outputs={len(variants)}")
if any(row["safe_bounds_pass"] != "PASS" for row in capacity) or any(row["stable_id_output"] != "PASS" for row in variants):
    raise SystemExit(1)
