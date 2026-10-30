"""Check public-repository hygiene without network access or Git mutations."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from noteformats.safety import assert_safe_workspace
from noteformats.reviews import pixel_digest

assert_safe_workspace(ROOT)

errors: list[str] = []
ignore_rules = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()

public_markdown = [
    path for path in ROOT.glob("*.md")
    if f"/{path.name}" not in ignore_rules
]
public_markdown.extend((ROOT / "docs").rglob("*.md"))
public_markdown.extend((ROOT / "templates").rglob("*.md"))
if not (ROOT / ".gitattributes").is_file() or "* text=auto eol=lf" not in (ROOT / ".gitattributes").read_text(encoding="utf-8"):
    errors.append("missing LF line-ending policy")
text_suffixes = {".py", ".md", ".json", ".csv", ".yml", ".yaml", ".txt", ".svg"}
public_text = [path for path in ROOT.iterdir() if path.is_file()
               and f"/{path.name}" not in ignore_rules
               and (path.suffix in text_suffixes or path.name in {"LICENSE", ".gitignore", ".gitattributes"})]
for folder in ("src", "scripts", "tests", "content", "profiles", "docs", "templates", ".github"):
    public_text.extend(path for path in (ROOT / folder).rglob("*") if path.is_file() and path.suffix in text_suffixes)
for path in public_text:
    if b"\r\n" in path.read_bytes():
        errors.append(f"CRLF in public text: {path.relative_to(ROOT).as_posix()}")
for path in public_markdown:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT).as_posix()
    if re.search(r"[A-Za-z]:[\\/]", text):
        errors.append(f"personal or absolute local path in {relative}")
    if re.search(r"not_human_reviewed|實體試印|母語審校|実物の試し刷り|physical A5 proofing|professional language review|macOS and Linux execution are", text, re.IGNORECASE):
        errors.append(f"obsolete verification disclaimer in {relative}")
    links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
    links.extend(re.findall(r'(?:src|href)="([^"]+)"', text))
    for link in links:
        destination = link.split("#", 1)[0]
        if not destination or "://" in destination or destination.startswith("mailto:"):
            continue
        resolved = (path.parent / destination).resolve()
        if resolved != ROOT and ROOT not in resolved.parents:
            errors.append(f"link escapes checkout: {relative} -> {link}")
        elif not resolved.is_file():
            errors.append(f"missing public link: {relative} -> {link}")

banner_path = ROOT / "docs/assets/banner.svg"
if not banner_path.is_file():
    errors.append("missing public banner")
else:
    try:
        banner = ET.parse(banner_path).getroot()
        if banner.tag != "{http://www.w3.org/2000/svg}svg" or banner.get("viewBox") != "0 0 1440 480":
            errors.append("banner SVG dimensions or root are invalid")
        for node in banner.iter():
            if node.tag.split("}")[-1] in {"script", "foreignObject", "image", "use", "a"}:
                errors.append("banner contains an external-capable element")
            if any(key.split("}")[-1] == "href" for key in node.attrib):
                errors.append("banner contains a linked resource")
    except ET.ParseError:
        errors.append("banner SVG is malformed")

catalog = list(csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline="")))
for row in catalog:
    manifest_path = ROOT / "templates" / row["id"] / "manifest.json"
    if not manifest_path.is_file():
        errors.append(f"missing manifest: {row['id']}")
        continue
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest["id"] != row["id"] or manifest["license_status"] != "MIT":
        errors.append(f"manifest identity or license mismatch: {row['id']}")

visual = json.loads((ROOT / "content/visual-review.json").read_text(encoding="utf-8"))
evidence_paths = {note["evidence"] for note in visual.values()}
if len(evidence_paths) != 15 or any(not path.startswith("docs/visual-evidence/") for path in evidence_paths):
    errors.append("sealed visual evidence is not on a public path")
for path in evidence_paths:
    evidence = ROOT / path
    if ROOT not in evidence.resolve().parents or not evidence.is_file():
        errors.append(f"missing visual evidence: {path}")
        continue
    digest = pixel_digest(evidence)
    if any(note["evidence_pixel_sha256"] != digest for note in visual.values() if note["evidence"] == path):
        errors.append(f"changed visual evidence: {path}")

print(f"public_markdown={len(public_markdown)} layouts={len(catalog)} visual_evidence={len(evidence_paths)} release_hygiene={'PASS' if not errors else 'FAIL'}")
for error in errors:
    print(f"FAIL {error}")
if errors:
    raise SystemExit(1)
