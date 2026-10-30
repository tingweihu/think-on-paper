from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from noteformats.safety import assert_safe_workspace, safe_project_path
assert_safe_workspace(ROOT)

from noteformats.docs import LANGS, DOC_NAMES, template_doc
from noteformats.exporters import example_svg, pdf, svg
from noteformats.geometry import Scene
from noteformats.registry import BUILDERS
from noteformats.variant_content import make_variant_content
from noteformats.variants import RECLASSIFIED_HEADERS
from noteformats.runtime import require_pdf_renderer, RendererUnavailable


def load_content(profile: dict):
    content = {}
    for name in ("gate1.json", "foundation.json", "grid-dot.json", "geometry.json", "columns.json", "cards.json", "comparison.json", "matrix.json", "mandala.json", "flow.json", "causal.json", "concept-network.json", "hierarchy.json", "learning.json", "research.json", "ideation.json", "storyboard.json", "special-paper.json", "hybrid.json"):
        path = ROOT / "content" / name
        if path.exists():
            content.update(json.loads(path.read_text(encoding="utf-8")))
    content.update(make_variant_content(content, profile, BUILDERS))
    for layout_id, target in RECLASSIFIED_HEADERS.items():
        content[layout_id]["variant_of"] = target
        content[layout_id]["variant_classification"] = "parameter"
    return content


def inside(path: Path):
    try:
        relative = path.relative_to(ROOT)
    except ValueError as exc:
        raise RuntimeError(f"Refusing path outside project: {path}") from exc
    safe_project_path(ROOT, relative)


def write(path: Path, data: str | bytes):
    inside(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = data.encode("utf-8") if isinstance(data, str) else data
    if path.is_file() and path.read_bytes() == encoded:
        return
    if isinstance(data, str):
        path.write_text(data, encoding="utf-8", newline="\n")
    else:
        path.write_bytes(data)


def build_one(layout_id: str, family: str, item: dict, profile: dict, renderer=None):
    renderer = renderer or require_pdf_renderer()
    scene = Scene.from_profile(profile)
    BUILDERS[layout_id](scene, profile)
    if not scene.bounds_ok():
        raise ValueError(f"Geometry exceeds page: {layout_id}")
    out = ROOT / "templates" / layout_id
    svg_path = out / "exports" / "a5-draft" / "blank.svg"
    pdf_path = out / "exports" / "a5-draft" / "blank.pdf"
    titled_pdf_path = out / "exports" / "a5-draft" / "titled.pdf"
    english_title = item["translations"]["en"]["title"]
    write(svg_path, svg(scene, profile))
    pdf_bytes = pdf(scene, profile)
    write(pdf_path, pdf_bytes)
    write(titled_pdf_path, pdf(scene, profile, english_title))
    prefix = out / "previews" / "raster-white"
    inside(prefix)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([renderer, "-f", "1", "-singlefile", "-scale-to", "1000", "-png", str(pdf_path), str(prefix)], check=True, cwd=ROOT)
    from PIL import Image, ImageChops
    raster = prefix.with_suffix(".png")
    with Image.open(raster) as im:
        white = im.convert("RGB")
        paper = Image.new("RGB", white.size, profile["preview_paper"])
        preview = ImageChops.multiply(white, paper)
        preview.save(out / "previews" / "a5-draft.png", optimize=True)
    raster.unlink()
    contrast = json.loads((ROOT / "profiles/a5-contrast.json").read_text(encoding="utf-8"))
    contrast_scene = Scene.from_profile(contrast)
    BUILDERS[layout_id](contrast_scene, contrast)
    contrast_base = out / "exports/a5-contrast"
    write(contrast_base / "blank.svg", svg(contrast_scene, contrast))
    write(contrast_base / "blank.pdf", pdf(contrast_scene, contrast))
    write(contrast_base / "titled.pdf", pdf(contrast_scene, contrast, english_title))
    for lang in LANGS:
        t = item["translations"][lang]
        write(out / "examples" / f"{lang}.svg", example_svg(scene, profile, t["labels"], lang, layout_id))
        write(out / DOC_NAMES[lang], template_doc(layout_id, family, item, lang))
    shape_data = [[s.kind, [round(v, 4) for v in s.values], s.layer] for s in scene.shapes]
    fingerprint = hashlib.sha256(json.dumps(shape_data, separators=(",", ":")).encode()).hexdigest()
    manifest = {
        "id": layout_id, "family": family, "profile": profile["id"], "profile_status": profile["status"],
        "builder": f"{BUILDERS[layout_id].__module__}.{BUILDERS[layout_id].__name__}",
        "source_type": item["source_type"], "source_note": item["source_note"], "license_status": "MIT", "content_revision": item.get("content_revision", 1),
        "geometry_sha256": fingerprint,
        "titled_pdf_english_name": english_title,
        "shape_count": len(scene.shapes), "dot_count": sum(s.kind == "dot" for s in scene.shapes), "example_slot_count": len(scene.slots),
        "files": {
            "svg": str(svg_path.relative_to(ROOT)).replace("\\", "/"),
            "pdf": str(pdf_path.relative_to(ROOT)).replace("\\", "/"),
            "titled_pdf": str(titled_pdf_path.relative_to(ROOT)).replace("\\", "/"),
            "preview": f"templates/{layout_id}/previews/a5-draft.png",
            "contrast": {key: f"templates/{layout_id}/exports/a5-contrast/{name}" for key, name in (("svg", "blank.svg"), ("pdf", "blank.pdf"), ("titled_pdf", "titled.pdf"))},
            "examples": {lang: f"templates/{layout_id}/examples/{lang}.svg" for lang in LANGS},
            "docs": {lang: f"templates/{layout_id}/{DOC_NAMES[lang]}" for lang in LANGS},
        },
    }
    if "variant_of" in item:
        manifest["variant_of"] = item["variant_of"]
        manifest["variant_classification"] = item["variant_classification"]
    write(out / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ids", nargs="*", help="IDs to build; default is all implemented IDs")
    parser.add_argument("--pdftoppm", help="Existing Poppler executable; defaults to pdftoppm on PATH")
    args = parser.parse_args()
    try:
        renderer = require_pdf_renderer(args.pdftoppm)
    except RendererUnavailable as error:
        print(f"Build prerequisite missing: {error}", file=sys.stderr)
        raise SystemExit(2)
    ids = args.ids or list(BUILDERS)
    catalog = {r["id"]: r for r in csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline=""))}
    profile = json.loads((ROOT / "profiles" / "a5-draft.json").read_text(encoding="utf-8"))
    content = load_content(profile)
    for layout_id in ids:
        if layout_id not in BUILDERS or layout_id not in catalog or layout_id not in content:
            raise ValueError(f"No complete builder/catalog/content for {layout_id}")
        print(f"BUILD {layout_id}", flush=True)
        build_one(layout_id, catalog[layout_id]["family"], content[layout_id], profile, renderer)
    print(f"BUILT {len(ids)}")


if __name__ == "__main__":
    main()
