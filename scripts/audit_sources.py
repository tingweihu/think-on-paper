"""Offline provenance and bundled-asset audit for the 144 local formats.

This proves which files reproduce from repository source. It cannot prove that
the source was independently authored or clear rights in named methods.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from noteformats.exporters import example_svg, pdf, svg
from noteformats.geometry import Scene
from noteformats.registry import BUILDERS
from noteformats.safety import assert_safe_workspace, safe_project_path
from build import load_content

assert_safe_workspace(ROOT)
safe_project_path(ROOT, "reports").mkdir(exist_ok=True)

profile = json.loads(safe_project_path(ROOT, "profiles/a5-draft.json").read_text(encoding="utf-8"))
content = load_content(profile)
catalog = list(csv.DictReader(safe_project_path(ROOT, "catalog-144.csv").open(encoding="utf-8-sig", newline="")))
assert len(catalog) == len(content) == len(BUILDERS) == 144

named_conventions = {
    "frayer", "crazy-eight", "five-why-chain", "seyes-ruled", "hanzi-tian",
    "hanzi-mi", "hanzi-nine", "music-staff", "guitar-tablature", "mindmap-six",
    "mindmap-eight", "mandala-extended", "t-comparison", "three-way-comparison",
}
forbidden_svg_tags = {"image", "foreignObject", "script", "use", "style", "a"}
external_asset_references = []
rows = []
preview_png_paths = set()


def inspect_svg(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")
    root = ET.fromstring(raw)
    for element in root.iter():
        tag = element.tag.split("}")[-1]
        if tag in forbidden_svg_tags:
            external_asset_references.append(f"{path.relative_to(ROOT)}: element {tag}")
        for key, value in element.attrib.items():
            local = key.split("}")[-1].lower()
            if local in ("href", "src") or local.startswith("on") or "url(" in value.lower():
                external_asset_references.append(f"{path.relative_to(ROOT)}: attribute {local}")
    if re.search(r"<\s*(?:!ENTITY|!DOCTYPE)", raw, flags=re.IGNORECASE):
        external_asset_references.append(f"{path.relative_to(ROOT)}: entity or doctype")


for record in catalog:
    layout_id = record["id"]
    item = content[layout_id]
    manifest_path = safe_project_path(ROOT, f"templates/{layout_id}/manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["id"] == layout_id
    assert manifest["builder"] == f"{BUILDERS[layout_id].__module__}.{BUILDERS[layout_id].__name__}"
    assert manifest["source_type"] == item["source_type"]
    assert manifest["source_note"] == item["source_note"]
    scene = Scene.from_profile(profile)
    BUILDERS[layout_id](scene, profile)
    files = manifest["files"]
    blank_svg = safe_project_path(ROOT, files["svg"])
    blank_pdf = safe_project_path(ROOT, files["pdf"])
    titled_pdf = safe_project_path(ROOT, files["titled_pdf"])
    assert blank_svg.read_text(encoding="utf-8") == svg(scene, profile), layout_id
    assert blank_pdf.read_bytes() == pdf(scene, profile), layout_id
    assert titled_pdf.read_bytes() == pdf(scene, profile, item["translations"]["en"]["title"]), layout_id
    inspect_svg(blank_svg)
    contrast = json.loads((ROOT / "profiles/a5-contrast.json").read_text(encoding="utf-8"))
    contrast_scene = Scene.from_profile(contrast)
    BUILDERS[layout_id](contrast_scene, contrast)
    for key, expected in (("svg", svg(contrast_scene, contrast).encode()),
                          ("pdf", pdf(contrast_scene, contrast)),
                          ("titled_pdf", pdf(contrast_scene, contrast, item["translations"]["en"]["title"]))):
        assert safe_project_path(ROOT, files["contrast"][key]).read_bytes() == expected, (layout_id, key)
    inspect_svg(safe_project_path(ROOT, files["contrast"]["svg"]))
    for lang in ("zh-TW", "en", "ja"):
        path = safe_project_path(ROOT, files["examples"][lang])
        expected = example_svg(scene, profile, item["translations"][lang]["labels"], lang, layout_id)
        assert path.read_text(encoding="utf-8") == expected, (layout_id, lang)
        inspect_svg(path)
    assert safe_project_path(ROOT, files["preview"]).is_file()
    preview_png_paths.add(files["preview"])
    source_type = item["source_type"]
    if source_type == "existing-method-adaptation" or layout_id in named_conventions:
        review_group = "named method or named convention"
    elif source_type.startswith("traditional-"):
        review_group = "traditional paper or format"
    elif source_type in ("common-geometry", "generic-geometry"):
        review_group = "common geometry"
    else:
        review_group = "project-original layout claim"
    rows.append({
        "id": layout_id,
        "family": record["family"],
        "source_type": source_type,
        "source_note": item["source_note"],
        "variant_of": item.get("variant_of", ""),
        "review_group": review_group,
        "source_rebuild": "PASS",
        "example_svg_languages": "3/3",
        "embedded_external_assets": "NONE DETECTED",
        "authorship_or_external_similarity": "NOT VERIFIED",
    })

assert not external_asset_references, external_asset_references[:20]
all_files = [path for path in ROOT.rglob("*") if path.is_file()]
bundled_font_suffixes = {".ttf", ".otf", ".woff", ".woff2", ".eot"}
external_media_suffixes = {".jpg", ".jpeg", ".gif", ".webp", ".mp3", ".mp4", ".wav"}
fonts = [str(path.relative_to(ROOT)) for path in all_files if path.suffix.lower() in bundled_font_suffixes]
media = [str(path.relative_to(ROOT)) for path in all_files if path.suffix.lower() in external_media_suffixes]
assert not fonts and not media, (fonts, media)
png_paths = [path.relative_to(ROOT).as_posix() for path in all_files if path.suffix.lower() == ".png"]
report_png_paths = sorted(path for path in png_paths if path.startswith("reports/") and
                          Path(path).name.startswith(("contact-", "titled-sample-")))
review_png_paths = sorted(path for path in png_paths if path.startswith("docs/visual-evidence/contact-"))
unclassified_png_paths = sorted(set(png_paths) - preview_png_paths - set(report_png_paths) - set(review_png_paths))
assert not unclassified_png_paths, unclassified_png_paths

report = safe_project_path(ROOT, "reports/SOURCE-REVIEW.csv")
with report.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

groups = Counter(row["review_group"] for row in rows)
types = Counter(row["source_type"] for row in rows)
summary = {
    "layout_ids": len(rows),
    "source_rebuild_pass": len(rows),
    "example_svgs_rebuilt": 3 * len(rows),
    "blank_svgs_checked": 2 * len(rows),
    "pdfs_rebuilt": 4 * len(rows),
    "external_svg_assets_detected": len(external_asset_references),
    "bundled_font_files": len(fonts),
    "bundled_photo_audio_video_files": len(media),
    "pdf_derived_preview_png_paths": len(preview_png_paths),
    "report_evidence_png_paths": report_png_paths,
    "public_visual_evidence_png_paths": review_png_paths,
    "unclassified_png_paths": unclassified_png_paths,
    "source_types": dict(sorted(types.items())),
    "review_groups": dict(sorted(groups.items())),
    "external_similarity": "NOT VERIFIED (offline local-source audit only)",
}
safe_project_path(ROOT, "reports/SOURCE-AUDIT.json").write_text(
    json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)
print(f"layouts={len(rows)} source_rebuild=PASS example_svgs={3*len(rows)} embedded_external_assets=0 fonts=0 media=0 similarity=NOT_VERIFIED")
