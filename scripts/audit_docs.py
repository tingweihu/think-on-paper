"""Check all generated language pages and create a per-format coverage matrix."""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from noteformats.docs import DOC_NAMES, LABELS, LANGS, RESULT_LABEL, template_doc
from noteformats.registry import BUILDERS
from noteformats.safety import assert_safe_workspace, safe_project_path
from build import load_content
from qa import rel_exists
from noteformats.content_quality import scenario_duplicates, limitation_duplicates, content_issues, repeated_sentences

assert_safe_workspace(ROOT)
safe_project_path(ROOT, "reports").mkdir(exist_ok=True)
profile = json.loads((ROOT / "profiles/a5-draft.json").read_text(encoding="utf-8"))
content = load_content(profile)
catalog = list(csv.DictReader((ROOT / "catalog-144.csv").open(encoding="utf-8-sig", newline="")))
rows = []
scenario_groups = scenario_duplicates(content)
limitation_groups = limitation_duplicates(content)
quality_issues = content_issues(content)
purposes = {lang: Counter(content[row["id"]]["translations"][lang]["purpose"] for row in catalog)
            for lang in LANGS}

for row in catalog:
    layout_id = row["id"]
    result = {"id": layout_id, "family": row["family"]}
    for lang in LANGS:
        t = content[layout_id]["translations"][lang]
        path = ROOT / "templates" / layout_id / DOC_NAMES[lang]
        actual = path.read_text(encoding="utf-8") if path.is_file() else ""
        expected = template_doc(layout_id, row["family"], content[layout_id], lang)
        headings = all(f"## {heading}" in actual for heading in
                       (LABELS[lang]["when"], LABELS[lang]["steps"], LABELS[lang]["example"],
                        LABELS[lang]["unsuitable"], LABELS[lang]["downloads"], RESULT_LABEL[lang]))
        fields = all(t.get(key) for key in ("title", "purpose", "example", "unsuitable")) and len(t.get("when", [])) >= 2 and len(t.get("steps", [])) >= 3
        links = rel_exists(path) if path.is_file() else ["missing page"]
        result[f"{lang}_source_complete"] = "PASS" if fields else "FAIL"
        result[f"{lang}_current_page"] = "PASS" if actual == expected else "FAIL"
        result[f"{lang}_required_sections"] = "PASS" if headings else "FAIL"
        result[f"{lang}_local_links"] = "PASS" if not links else "FAIL"
        result[f"{lang}_same_scenario_ids"] = ";".join(ids for group in scenario_groups[lang] if layout_id in group for ids in group)
        result[f"{lang}_same_limitation_ids"] = ";".join(ids for group in limitation_groups[lang] if layout_id in group for ids in group)
        result[f"{lang}_numbered_example_entries"] = len(t.get("example_entries", []))
        result[f"{lang}_repeated_sentences"] = sum(len(repeated_sentences(t[field])) for field in ("purpose", "unsuitable", "example"))
        result[f"{lang}_purpose_repeated"] = purposes[lang][t["purpose"]]
        result[f"{lang}_generic_purpose"] = "FAIL" if (
            "This candidate has its own downloadable geometry" in t["purpose"]
            or "這是可直接下載的候選版型" in t["purpose"]
            or "この候補には対応するダウンロード可能な図形" in t["purpose"]
        ) else "PASS"
    result["human_native_review"] = "NOT VERIFIED"
    rows.append(result)

out = safe_project_path(ROOT, "reports/TRILINGUAL-COVERAGE.csv")
with out.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
failures = sum(value == "FAIL" for row in rows for key, value in row.items() if key.endswith(("_complete", "_page", "_sections", "_links", "_purpose")))
repeats = sum(int(row[f"{lang}_purpose_repeated"]) > 1
              for row in rows for lang in LANGS)
print(f"trilingual_pages={len(rows)*3} automatic_failures={failures} repeated_purposes={repeats} human_review=NOT_VERIFIED")
print(f"shared_scenario_groups={sum(len(groups) for groups in scenario_groups.values())} shared_limitation_groups={sum(len(groups) for groups in limitation_groups.values())} content_issues={len(quality_issues)}")
for issue in quality_issues:
    print(f"FAIL {issue}")
if quality_issues:
    raise SystemExit(1)
if repeats:
    raise SystemExit(1)
if failures:
    raise SystemExit(1)
