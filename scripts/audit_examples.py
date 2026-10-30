"""Per-ID teaching-example inventory; automated evidence is not human review."""

from __future__ import annotations

import csv
import json
import re
import sys
from math import hypot
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from noteformats.examples import TEACHING_MARK_IDS
from noteformats.geometry import Scene
from noteformats.registry import BUILDERS
from noteformats.safety import assert_safe_workspace, safe_project_path
from build import load_content

assert_safe_workspace(ROOT)
safe_project_path(ROOT, "reports").mkdir(exist_ok=True)
profile = json.loads((ROOT / "profiles/a5-draft.json").read_text(encoding="utf-8"))
content = load_content(profile)
catalog = list(csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline="")))

DRAWING_REQUIRED = {
    "blank", "grid-fine", "grid-standard", "grid-large", "engineering-grid",
    "grid-hierarchical", "dot-fine", "dot-standard", "dot-staggered",
    "dot-grid-split", "hex-grid", "rhombus-grid", "diagonal-guides",
    "radial-polar", "triangular-grid", "isometric-grid", "pixel-stitch-grid",
    "perspective-guides", "music-staff", "ruled-sketch-top", "ruled-and-sketch",
    "hero-three-cards", "mosaic-cards", "dot-and-blank", "column-dot-main",
    "hybrid-multi-zone", "three-sketch-proposals", "main-sketch-side-notes",
    "detail-sketch", "two-sketch-notes", "mixed-storyboard", "crazy-eight",
    "seven-ideation-cards", "storyboard-three", "storyboard-four",
    "storyboard-6", "storyboard-eight-mixed",
}
PLACEHOLDER = re.compile(r"(?:\b(?:TODO|TBD|Next\s+\d+)\b|補充\s*\d+|追加\s*\d+)", re.I)

rows = []
for row in catalog:
    layout_id, family = row["id"], row["family"]
    scene = Scene.from_profile(profile)
    BUILDERS[layout_id](scene, profile)
    item = content[layout_id]
    all_labels = [item["translations"][lang]["labels"] for lang in ("zh-TW", "en", "ja")]
    # The staff teaches notation through the vector notes themselves. Its
    # three positioning slots are intentionally empty in every language.
    drawn_notation = layout_id == "music-staff" and all(
        len(labels) == len(scene.slots) and not any(label.strip() for label in labels)
        for labels in all_labels
    )
    complete = drawn_notation or all(
        len(labels) == len(scene.slots) and all(label.strip() for label in labels)
        for labels in all_labels
    )
    narrative = all(bool(item["translations"][lang].get("example", "").strip())
                    for lang in ("zh-TW", "en", "ja"))
    placeholder = any(PLACEHOLDER.search(label) for labels in all_labels for label in labels)
    vector = layout_id in TEACHING_MARK_IDS
    region_logic = "NOT APPLICABLE"
    if layout_id in ("venn-two", "venn-three"):
        circles = [shape.values for shape in scene.shapes if shape.kind == "circle"]
        expected = (
            ((True, False), (True, True), (False, True)) if layout_id == "venn-two" else
            ((True, False, False), (False, True, False), (False, False, True),
             (True, True, False), (True, False, True), (False, True, True),
             (True, True, True))
        )
        actual = tuple(tuple(hypot(x + width / 2 - cx, y - 1.5 - cy) < radius
                             for cx, cy, radius in circles)
                       for x, y, width in scene.slots)
        region_logic = "PASS" if actual == expected else "FAIL"
    xml_ok = True
    for lang in ("zh-TW", "en", "ja"):
        example = ROOT / "templates" / layout_id / "examples" / f"{lang}.svg"
        try:
            root = ET.parse(example).getroot()
            if vector and not any(e.attrib.get("data-example") == "teaching-marks" for e in root.iter()):
                xml_ok = False
        except (OSError, ET.ParseError):
            xml_ok = False
    short_en = sum(len(label.split()) <= 2 and not any(c in label for c in (":", "?", "!", ","))
                   for label in all_labels[1])
    weak_cue = short_en >= max(2, len(all_labels[1]) // 2)
    action = ("repair missing/placeholder content" if not complete or not narrative or placeholder or not xml_ok or region_logic == "FAIL" else
              "add an original drawing aligned with the paper" if layout_id in DRAWING_REQUIRED and not vector else
              "review whether short entries teach the method" if weak_cue and not vector else
              "human visual and semantic review")
    rows.append({
        "id": layout_id, "family": family,
        "example_complete": "PASS" if complete and narrative else "FAIL",
        "functional_fit": "NOT VERIFIED", "specific_scenario": "PARTIAL" if narrative else "FAIL",
        "information_relationship": "PARTIAL" if vector else "NOT VERIFIED",
        "drawing_required": "YES" if layout_id in DRAWING_REQUIRED else "NO",
        "original_vector_marks": "PASS" if vector else "NOT PRESENT",
        "three_language_structure": "PASS" if complete else "FAIL",
        "three_language_meaning": "NOT VERIFIED",
        "venn_region_position": region_logic,
        "overflow_guard": "AUTO PASS; FONT NOT VERIFIED" if xml_ok else "FAIL",
        "automated_xml": "PASS" if xml_ok else "FAIL",
        "human_review": "NOT VERIFIED",
        "teaching_quality": "FAIL" if not complete or not narrative or placeholder or not xml_ok or region_logic == "FAIL" else "PARTIAL",
        "short_label_review_cue": "YES" if weak_cue else "NO",
        "next_action": action,
    })

out = safe_project_path(ROOT, "reports/EXAMPLE-QUALITY.csv")
with out.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f"example_records={len(rows)} automatic_failures={sum(r['teaching_quality']=='FAIL' for r in rows)} vector_enhanced={sum(r['original_vector_marks']=='PASS' for r in rows)} drawing_gaps={sum(r['drawing_required']=='YES' and r['original_vector_marks']!='PASS' for r in rows)}")
if any(row["teaching_quality"] == "FAIL" for row in rows):
    raise SystemExit(1)
