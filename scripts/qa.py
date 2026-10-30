from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from noteformats.safety import assert_safe_workspace
assert_safe_workspace(ROOT)

from PIL import Image, ImageChops
from pypdf import PdfReader

from noteformats.docs import LANGS, DOC_NAMES, catalog_doc, choose_doc, home, template_doc
from noteformats.exporters import example_svg, pdf, svg
from noteformats.examples import TEACHING_MARK_IDS, example_marks
from noteformats.geometry import Scene
from noteformats.reviews import review_valid
from noteformats.catalog import VARIANTS, counts as catalog_counts
from noteformats.navigation import public_documents
from noteformats.content_quality import content_issues
from noteformats.runtime import require_pdf_renderer, RendererUnavailable
from noteformats.registry import BUILDERS
from noteformats.variant_content import make_variant_content
from noteformats.variants import ORIGINAL_MERGES, RECLASSIFIED_HEADERS, VARIANT_METHODS

PROFILE = json.loads((ROOT / "profiles" / "a5-draft.json").read_text(encoding="utf-8"))
CATALOG = list(csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline="")))
CONTENT = {}
for name in ("gate1.json", "foundation.json", "grid-dot.json", "geometry.json", "columns.json", "cards.json", "comparison.json", "matrix.json", "mandala.json", "flow.json", "causal.json", "concept-network.json", "hierarchy.json", "learning.json", "research.json", "ideation.json", "storyboard.json", "special-paper.json", "hybrid.json"):
    path = ROOT / "content" / name
    if path.exists():
        CONTENT.update(json.loads(path.read_text(encoding="utf-8")))
VISUAL = json.loads((ROOT / "content" / "visual-review.json").read_text(encoding="utf-8")) if (ROOT / "content" / "visual-review.json").exists() else {}
MERGED = json.loads((ROOT / "content" / "merged.json").read_text(encoding="utf-8")) if (ROOT / "content" / "merged.json").exists() else {}
CONTENT.update(make_variant_content(CONTENT, PROFILE, BUILDERS))
for layout_id, target in RECLASSIFIED_HEADERS.items():
    CONTENT[layout_id]["variant_of"] = target
    CONTENT[layout_id]["variant_classification"] = "parameter"
DISPLAY_VARIANTS = VARIANTS


def rel_exists(markdown: Path) -> list[str]:
    errors = []
    text = markdown.read_text(encoding="utf-8")
    links = [match.group(1) for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text)]
    links.extend(match.group(1) for match in re.finditer(r'(?:src|href)="([^"]+)"', text))
    for link in links:
        dest = link.split("#", 1)[0]
        if not dest or "://" in dest or dest.startswith("mailto:"):
            continue
        path = (markdown.parent / dest).resolve()
        if path != ROOT and ROOT not in path.parents:
            errors.append(f"external link {dest}")
        elif not path.exists():
            errors.append(f"missing link {dest}")
    return errors


def review_ok(layout_id: str, fingerprint: str) -> bool:
    return review_valid(ROOT, VISUAL.get(layout_id, {}), fingerprint, PROFILE)


def check_item(row: dict, renderer=None) -> tuple[list[str], dict]:
    renderer = renderer or require_pdf_renderer()
    layout_id = row["id"]
    errors = []
    base = ROOT / "templates" / layout_id
    manifest_path = base / "manifest.json"
    if not manifest_path.exists():
        return ["manifest absent"], {}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["id"] != layout_id or manifest["family"] != row["family"]:
        errors.append("manifest identity mismatch")
    item = CONTENT.get(layout_id)
    if (manifest.get("profile") != PROFILE["id"] or manifest.get("profile_status") != PROFILE["status"]
            or manifest.get("license_status") != "MIT" or item is None
            or manifest.get("content_revision") != item.get("content_revision", 1)
            or manifest.get("source_type") != item.get("source_type")
            or manifest.get("source_note") != item.get("source_note")):
        errors.append("manifest profile or provenance mismatch")
    if layout_id in VARIANT_METHODS:
        if manifest.get("variant_of") != ORIGINAL_MERGES[layout_id]["target"] or manifest.get("variant_classification") != VARIANT_METHODS[layout_id][0]:
            errors.append("variant manifest classification or target mismatch")
    if layout_id in RECLASSIFIED_HEADERS:
        if manifest.get("variant_of") != RECLASSIFIED_HEADERS[layout_id] or manifest.get("variant_classification") != "parameter":
            errors.append("reclassified variant relation mismatch")
    for role, path in manifest["files"].items():
        vals = path.values() if isinstance(path, dict) else [path]
        for v in vals:
            target = (ROOT / v).resolve()
            if ROOT not in target.parents or not target.is_file() or target.stat().st_size == 0:
                errors.append(f"missing or empty {role}: {v}")
    if errors:
        return errors, manifest
    if layout_id not in BUILDERS:
        errors.append("builder absent")
        return errors, manifest
    source_scene = Scene.from_profile(PROFILE)
    BUILDERS[layout_id](source_scene, PROFILE)
    if not source_scene.bounds_ok():
        errors.append("source geometry outside page")
    if not source_scene.bounds_ok(tolerance=0.001, safe=True):
        errors.append("source geometry outside A5 safe margin")
    shape_data = [[s.kind, [round(v, 4) for v in s.values], s.layer] for s in source_scene.shapes]
    source_hash = hashlib.sha256(json.dumps(shape_data, separators=(",", ":")).encode()).hexdigest()
    if source_hash != manifest["geometry_sha256"]:
        errors.append("manifest geometry differs from current builder")
    blank_svg = base / "exports" / "a5-draft" / "blank.svg"
    if blank_svg.read_text(encoding="utf-8") != svg(source_scene, PROFILE):
        errors.append("SVG differs from current source")
    root = ET.parse(blank_svg).getroot()
    if root.attrib.get("viewBox") != f"0 0 {PROFILE['page_mm'][0]} {PROFILE['page_mm'][1]}":
        errors.append("SVG page dimensions")
    allowed = {"svg", "line", "rect", "circle", "polyline", "polygon"}
    shapes = 0
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in allowed:
            errors.append(f"forbidden SVG element: {tag}")
        if tag != "svg":
            shapes += 1
            if el.attrib.get("fill") != "none":
                if not (tag == "circle" and el.attrib.get("stroke") == "none" and float(el.attrib.get("r", "99")) <= PROFILE["dot_diameter_mm"] / 2 + 0.001):
                    errors.append("SVG visible fill other than registered dots")
        if any(k in el.attrib for k in ("href", "xlink:href", "onload")):
            errors.append("SVG external resource or script")
    if shapes != manifest["shape_count"]:
        errors.append("SVG shape count mismatch")
    if shapes == 0 and layout_id != "blank":
        errors.append("unexpected empty geometry")
    pdf_path = base / "exports" / "a5-draft" / "blank.pdf"
    if pdf_path.read_bytes() != pdf(source_scene, PROFILE):
        errors.append("PDF differs from current source")
    reader = PdfReader(str(pdf_path))
    if len(reader.pages) != 1:
        errors.append("PDF page count")
    else:
        page = reader.pages[0]
        w, h = PROFILE["page_mm"]
        if abs(float(page.mediabox.width) - w * 72 / 25.4) > 0.02 or abs(float(page.mediabox.height) - h * 72 / 25.4) > 0.02:
            errors.append("PDF page dimensions")
        if (page.extract_text() or "").strip():
            errors.append("PDF extractable text")
        stream = page.get_contents().get_data()
        if re.search(rb"\b(?:BT|ET|Tf|Tj|TJ|Do|F)\b", stream):
            errors.append("PDF text, image or forbidden fill operator")
        if len(re.findall(rb"\bf\b", stream)) != manifest.get("dot_count", 0):
            errors.append("PDF fill count differs from dot count")
        if "/Font" in str(page.get("/Resources", {})):
            errors.append("PDF font resource")
    english_title = item["translations"]["en"]["title"] if item else ""
    titled_path = base / "exports" / "a5-draft" / "titled.pdf"
    if manifest.get("titled_pdf_english_name") != english_title:
        errors.append("titled PDF name differs from English content")
    if titled_path.read_bytes() != pdf(source_scene, PROFILE, english_title):
        errors.append("titled PDF differs from current source")
    titled_reader = PdfReader(str(titled_path))
    if len(titled_reader.pages) != 1:
        errors.append("titled PDF page count")
    else:
        titled_page = titled_reader.pages[0]
        if (titled_page.extract_text() or "").strip() != english_title:
            errors.append("titled PDF does not contain exactly its English name")
        if (abs(float(titled_page.mediabox.width) - w * 72 / 25.4) > 0.02
                or abs(float(titled_page.mediabox.height) - h * 72 / 25.4) > 0.02):
            errors.append("titled PDF page dimensions")
        titled_stream = titled_page.get_contents().get_data()
        if len(re.findall(rb"\bTj\b", titled_stream)) != 1 or len(re.findall(rb"\bBT\b", titled_stream)) != 1:
            errors.append("titled PDF has extra or missing text operators")
        if re.search(rb"\b(?:Do|F)\b", titled_stream):
            errors.append("titled PDF has image or forbidden fill operator")
        if len(re.findall(rb"\bf\b", titled_stream)) != manifest.get("dot_count", 0):
            errors.append("titled PDF fill count differs from dot count")
    contrast = json.loads((ROOT / "profiles/a5-contrast.json").read_text(encoding="utf-8"))
    contrast_scene = Scene.from_profile(contrast)
    BUILDERS[layout_id](contrast_scene, contrast)
    from noteformats.reviews import geometry_digest
    if geometry_digest(contrast_scene) != source_hash:
        errors.append("contrast geometry differs from default")
    for key, expected in (("svg", svg(contrast_scene, contrast).encode()),
                          ("pdf", pdf(contrast_scene, contrast)),
                          ("titled_pdf", pdf(contrast_scene, contrast, item["translations"]["en"]["title"]))):
        target = ROOT / manifest["files"]["contrast"][key]
        if target.read_bytes() != expected:
            errors.append(f"contrast {key} differs from source")
    if PdfReader(ROOT / manifest["files"]["contrast"]["pdf"]).pages[0].extract_text().strip():
        errors.append("contrast blank PDF contains text")
    preview = base / "previews" / "a5-draft.png"
    with Image.open(preview) as im:
        if im.width < 500 or abs(im.width / im.height - w / h) > 0.005:
            errors.append("PNG dimensions or aspect")
        corner = im.convert("RGB").getpixel((3, 3))
        if corner != tuple(int(PROFILE["preview_paper"][i:i+2], 16) for i in (1, 3, 5)):
            errors.append("PNG preview paper")
        if im.getbbox() is None:
            errors.append("PNG empty")
        cache_dir = ROOT / "reports" / ".qa-raster"
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_prefix = cache_dir / layout_id
        cache_png = cache_prefix.with_suffix(".png")
        try:
            subprocess.run([renderer, "-f", "1", "-singlefile", "-scale-to", "1000", "-png", str(pdf_path), str(cache_prefix)], check=True, cwd=ROOT, capture_output=True)
            with Image.open(cache_png) as raster:
                white = raster.convert("RGB")
                paper = Image.new("RGB", white.size, PROFILE["preview_paper"])
                expected = ImageChops.multiply(white, paper)
                if ImageChops.difference(expected, im.convert("RGB")).getbbox() is not None:
                    errors.append("PNG differs from independently rerendered PDF")
        finally:
            if cache_png.exists():
                cache_png.unlink()
    if item is None:
        errors.append("content absent")
    else:
        for lang in LANGS:
            t = item["translations"].get(lang, {})
            if any(not t.get(key) for key in ("title", "purpose", "unsuitable", "example")) or len(t.get("when", [])) < 2 or not 3 <= len(t.get("steps", [])) <= 5:
                errors.append(f"{lang} incomplete content")
            example_path = base / "examples" / f"{lang}.svg"
            if example_path.read_text(encoding="utf-8") != example_svg(source_scene, PROFILE, t["labels"], lang, layout_id):
                errors.append(f"{lang} example differs from current source/content")
            example = ET.parse(example_path).getroot()
            if layout_id in TEACHING_MARK_IDS and not any(el.attrib.get("data-example") == "teaching-marks" for el in example.iter()):
                errors.append(f"{lang} teaching marks absent")
            texts = [el for el in example.iter() if el.tag.split("}")[-1] == "text"]
            if len(texts) < manifest["example_slot_count"] and layout_id != "music-staff":
                errors.append(f"{lang} example labels missing")
            doc = base / DOC_NAMES[lang]
            if doc.read_text(encoding="utf-8") != template_doc(layout_id, row["family"], item, lang):
                errors.append(f"{lang} documentation differs from current content")
            errors.extend(f"{lang} {e}" for e in rel_exists(doc))
        if layout_id in TEACHING_MARK_IDS:
            # Teaching diagrams must have the same nontext geometry in all
            # three languages; captions and explanatory words may differ.
            def nontext_signature(lang):
                fragment = "\n".join(example_marks(layout_id, source_scene, lang))
                root = ET.fromstring(f"<svg>{fragment}</svg>")
                return [(el.tag, tuple(sorted(el.attrib.items()))) for el in root.iter()
                        if el.tag not in ("svg", "text")]
            if len({str(nontext_signature(lang)) for lang in LANGS}) != 1:
                errors.append("teaching diagram geometry differs across languages")
    return errors, manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdftoppm", help="Existing Poppler executable; defaults to pdftoppm on PATH")
    args = parser.parse_args()
    try:
        renderer = require_pdf_renderer(args.pdftoppm)
    except RendererUnavailable as error:
        print(f"QA prerequisite missing: {error}", file=sys.stderr)
        raise SystemExit(2)
    results = {}
    rows = []
    verified = []
    fingerprints = {}
    for row in CATALOG:
        layout_id = row["id"]
        manifest = {}
        manifest_path = ROOT / "templates" / layout_id / "manifest.json"
        if manifest_path.exists():
            try:
                errors, manifest = check_item(row, renderer)
            except Exception as exc:
                errors, manifest = [f"QA exception: {type(exc).__name__}: {exc}"], {}
            fingerprint = manifest.get("geometry_sha256", "")
            is_variant = layout_id in DISPLAY_VARIANTS
            if layout_id in ORIGINAL_MERGES and fingerprint:
                target_path = ROOT / "templates" / ORIGINAL_MERGES[layout_id]["target"] / "manifest.json"
                if target_path.is_file():
                    target_fingerprint = json.loads(target_path.read_text(encoding="utf-8"))["geometry_sha256"]
                    classification = VARIANT_METHODS[layout_id][0]
                    if (classification == "equivalent") != (fingerprint == target_fingerprint):
                        errors.append("variant equivalence classification contradicts geometry")
                else:
                    errors.append("variant canonical target missing")
            if fingerprint and not is_variant:
                if fingerprint in fingerprints:
                    errors.append(f"duplicate geometry of {fingerprints[fingerprint]}")
                else:
                    fingerprints[fingerprint] = layout_id
            if errors:
                state, qa = "generated", "FAIL"
            elif is_variant:
                state, qa = "merged", "PASS"
            elif review_ok(layout_id, fingerprint):
                state, qa = "verified", "PASS"
                verified.append((layout_id, row["family"], CONTENT[layout_id]))
            else:
                state, qa = "documented", "PARTIAL"
                errors.append("visual review pending or geometry/style changed since review")
        else:
            state, qa, errors = "planned", "NOT RUN", []
        results[layout_id] = {"status": state, "qa": qa, "errors": errors}
        rows.append({
            "id": layout_id, "family": row["family"], "candidate_stage": row["stage"],
            "status": state, "qa": qa, "zh-TW": "complete" if state in ("documented", "verified", "merged") else "not_run",
            "en": "complete" if state in ("documented", "verified", "merged") else "not_run",
            "ja": "complete" if state in ("documented", "verified", "merged") else "not_run",
            "source": manifest.get("builder", "") if manifest_path.exists() else "",
            "outputs": f"templates/{layout_id}/manifest.json" if manifest_path.exists() else "",
            "reason": (f"{VARIANT_METHODS[layout_id][0]} of {ORIGINAL_MERGES[layout_id]['target']}: {ORIGINAL_MERGES[layout_id]['reason']}" if layout_id in VARIANT_METHODS and state == "merged" else
                       f"Shared-header parameter variant of {RECLASSIFIED_HEADERS[layout_id]}" if layout_id in RECLASSIFIED_HEADERS and state == "merged" else "; ".join(errors)),
        })
    report_dir = ROOT / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    with (report_dir / "CATALOG-STATUS.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (report_dir / "qa-results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    all_available = [(row["id"], row["family"], CONTENT[row["id"]])
                     for row in CATALOG if row["id"] in CONTENT]
    guide_errors = content_issues(CONTENT)
    for name, expected in public_documents(PROFILE, CATALOG, CONTENT).items():
        path = ROOT / name
        if not path.is_file() or path.read_text(encoding="utf-8") != expected:
            guide_errors.append(f"{name}: navigation is stale; run scripts/generate_docs.py")
    for lang, name in (("zh-TW", "README.md"), ("en", "README.en.md"), ("ja", "README.ja.md")):
        readme = ROOT / name
        if not readme.is_file():
            guide_errors.append(f"missing guide: {name}")
            continue
        guide_errors.extend(f"{name}: {e}" for e in rel_exists(readme))
        readme_text = readme.read_text(encoding="utf-8")
        expected_ids = {layout_id for layout_id, _, _ in all_available}
        titles = set(re.findall(r"templates/([a-z0-9-]+)/exports/a5-draft/titled\.pdf", readme_text))
        if titles != {layout_id for layout_id, _, _ in all_available}:
            guide_errors.append(f"{name}: titled-PDF gallery does not cover every available format")
        example_images = re.findall(rf'<img src="templates/([a-z0-9-]+)/examples/{re.escape(lang)}\.svg"', readme_text)
        if len(example_images) != len(expected_ids) or set(example_images) != expected_ids:
            guide_errors.append(f"{name}: embedded worked-example gallery does not cover every available format exactly once")
        for layout_id, _, item in all_available:
            if item["translations"][lang]["example"] not in readme_text:
                guide_errors.append(f"{name}: missing written worked example for {layout_id}")
        if readme_text.count("<details id=\"family-") != len({family for _, family, _ in all_available}):
            guide_errors.append(f"{name}: collapsible family count mismatch")
    for lang in LANGS:
        for name in ("catalog", "choose", "print", "customize", "contribute"):
            guide_path = ROOT / "docs" / lang / f"{name}.md"
            if not guide_path.exists():
                guide_errors.append(f"missing guide: {guide_path.relative_to(ROOT)}")
            else:
                guide_errors.extend(f"{guide_path.relative_to(ROOT)}: {e}" for e in rel_exists(guide_path))
    counts = Counter(r["status"] for r in rows)
    geometry_counts = catalog_counts(PROFILE)
    next_ids = [r["id"] for r in rows if r["status"] == "planned"]
    qa_lines = [
        "# QA evidence", "", "## Current digital verification", "",
        "Generated by `python -B scripts/qa.py` from this checkout.", "",
        f"Catalog: {len(rows)} IDs, {counts['verified']} reviewed base formats, {counts['merged']} downloadable variants, {counts['documented']} pending visual reviews, {sum(v['qa'] == 'FAIL' for v in results.values())} failures.", "",
        "Checks: current source geometry hash and A5 bounds; source-to-SVG/PDF byte equality; wordless blank output; PDF dimensions and no full-page fill; Poppler PDF rerender versus preview PNG; three-language content and examples; manifest provenance and variant relationship; local links and independent geometry duplication.", "",
        f"Visual evidence: {len(verified)} base formats have current hashed Contact Sheets in `docs/visual-evidence/`.", "",
        f"Enhanced teaching-vector examples: {len(TEACHING_MARK_IDS)} IDs × 3 languages; structural example checks cover all {len(rows)} IDs.", "",
        f"Navigation links: {'PASS' if not guide_errors else 'FAIL'}.", "",
    ]
    if guide_errors:
        qa_lines.extend(f"- {e}" for e in guide_errors)
    qa_lines.extend(["", "Original project content uses the root MIT LICENSE with Copyright (c) 2026 tingweihu. See `docs/SOURCES-AND-RIGHTS.md` for the offline source audit.", ""])
    (report_dir / "QA.md").write_text("\n".join(qa_lines), encoding="utf-8", newline="\n")
    status_lines = [
        "# Status", "", "Current local digital preview candidate.", "",
        f"- {geometry_counts['unique_geometry']} distinct geometries across {len(rows)} downloadable IDs. {len(rows)} catalog IDs: {counts['verified']} reviewed base formats and {counts['merged']} downloadable variants.",
        f"- Structural failures: {counts['generated']}; visual review pending: {counts['documented']}; navigation: {'PASS' if not guide_errors else 'FAIL'}.",
        "- Reproducible wordless SVG/PDF, English-titled PDF, PDF-derived PNG, and three-language guides and examples are present for every ID.",
        "- Source of truth: `reports/CATALOG-STATUS.csv` and `reports/qa-results.json`; visual evidence lives in `docs/visual-evidence/`.",
        "- Original project content is MIT licensed; see `docs/SOURCES-AND-RIGHTS.md` for the source audit.", "",
    ]
    (report_dir / "STATUS.md").write_text("\n".join(status_lines), encoding="utf-8", newline="\n")
    print(f"verified={counts['verified']} documented={counts['documented']} failed={counts['generated']} merged={counts['merged']} planned={counts['planned']} link_errors={len(guide_errors)}")
    for layout_id, result in results.items():
        if result["qa"] == "FAIL":
            print(f"FAIL {layout_id}: {'; '.join(result['errors'])}")
    if guide_errors:
        print("GUIDE FAIL: " + "; ".join(guide_errors))
    if any(r["qa"] != "PASS" for r in results.values()) or guide_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
