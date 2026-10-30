"""Generate public navigation explicitly; verification never writes it."""

from .catalog import VARIANTS, counts, geometry_groups
from .docs import LANGS, DOC_NAMES, home, catalog_doc, choose_doc


def public_documents(profile, catalog, content):
    formats = [(row["id"], row["family"], content[row["id"]]) for row in catalog]
    base = [item for item in formats if item[0] not in VARIANTS]
    stats = counts(profile)
    documents = {}
    for lang, name in zip(LANGS, ("README.md", "README.en.md", "README.ja.md")):
        documents[name] = home(lang, base, len(VARIANTS), formats, stats["unique_geometry"])
        documents[f"docs/{lang}/catalog.md"] = catalog_doc(lang, base, VARIANTS)
        documents[f"docs/{lang}/choose.md"] = choose_doc(lang, base)
    lines = ["# Geometry groups｜共用幾何｜共通の図形", "",
             f"{stats['ids']} downloadable IDs / {stats['unique_geometry']} distinct geometries / {stats['shared_geometry_groups']} shared groups.", "",
             "幾何數依相同 profile 下的原語、座標與線條層級計算；用途名稱、教學與參數分類另行保留。18 個導覽家族沿用候選目錄，並非 144 種獨立方法的宣稱。", "",
             "Geometry counts compare primitives, coordinates, and stroke layers under the same profile. Named uses and parameter relationships remain separate. The 18 browsing families come from the candidate catalog; they do not imply 144 independent methods.", "",
             "図形数は同じ設定の要素・座標・線の階層で数えます。用途名と派生関係は別に記録しています。18分類は候補目録の案内で、144の独立した方法を意味しません。", "",
             "| Shared geometry / 共用幾何 | IDs and guides / 版型說明 |", "|---|---|"]
    for digest, ids in geometry_groups(profile).items():
        if len(ids) > 1:
            links = [f"[{layout_id}](../templates/{layout_id}/{DOC_NAMES['en']})" for layout_id in ids]
            lines.append(f"| `{digest[:12]}` | {' · '.join(links)} |")
    documents["docs/GEOMETRY-GROUPS.md"] = "\n".join(lines) + "\n"
    return documents


def write_if_changed(path, text):
    if not path.is_file() or path.read_text(encoding="utf-8") != text:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False
