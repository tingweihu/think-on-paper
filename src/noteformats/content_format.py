"""Unambiguous presentation of entries at worked-example label positions."""

import json


def region_example(entries, lang):
    heading = {
        "zh-TW": "依圖中填寫位置順序列出，每個編號是一筆示例條目：",
        "en": "Entries in example-position order; each number identifies one entry:",
        "ja": "図の記入位置の順に示します。番号一つが一つの記入例です：",
    }[lang]
    return heading + "\n\n" + "\n".join(f"{index}. {entry}" for index, entry in enumerate(entries, 1))


def inline_entries(entries, lang):
    if lang == "en":
        return "; ".join(f"{index}: {json.dumps(entry, ensure_ascii=False)}" for index, entry in enumerate(entries, 1))
    return "；".join(f"{index}「{entry}」" for index, entry in enumerate(entries, 1))
