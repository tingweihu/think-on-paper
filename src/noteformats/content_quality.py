"""Detect copied scenario sets and repeated sentences without claiming semantic review."""

import re
from collections import defaultdict
from .content_format import region_example

LANGS = ("zh-TW", "en", "ja")


def normalized(text):
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(".。!！?？")


def field_duplicates(content, field):
    duplicates = {}
    for lang in LANGS:
        groups = defaultdict(list)
        for layout_id, item in content.items():
            value = item["translations"][lang][field]
            key = tuple(sorted(normalized(entry) for entry in value)) if isinstance(value, list) else normalized(value)
            groups[key].append(layout_id)
        duplicates[lang] = [ids for ids in groups.values() if len(ids) > 1]
    return duplicates


def scenario_duplicates(content):
    return field_duplicates(content, "when")


def limitation_duplicates(content):
    return field_duplicates(content, "unsuitable")


def repeated_sentences(text):
    sentences = [normalized(value) for value in re.split(r"[。！？.!?]+", text)]
    seen, repeated = set(), set()
    for sentence in sentences:
        if len(sentence) < 12:
            continue
        if sentence in seen:
            repeated.add(sentence)
        seen.add(sentence)
    return sorted(repeated)


def content_issues(content):
    issues = []
    for lang, groups in scenario_duplicates(content).items():
        issues.extend(f"{lang}: identical usage scenarios: {', '.join(ids)}" for ids in groups)
    for lang, groups in limitation_duplicates(content).items():
        issues.extend(f"{lang}: identical limitations: {', '.join(ids)}" for ids in groups)
    for layout_id, item in content.items():
        for lang in LANGS:
            translation = item["translations"][lang]
            for field in ("purpose", "unsuitable", "example"):
                if repeated_sentences(translation[field]):
                    issues.append(f"{layout_id}/{lang}: repeated sentence in {field}")
            values = [normalized(value) for value in translation["when"]]
            if len(values) != len(set(values)):
                issues.append(f"{layout_id}/{lang}: repeated scenario within one page")
            if "example_entries" in translation:
                entries = translation["example_entries"]
                if entries != translation["labels"] or translation["example"] != region_example(entries, lang):
                    issues.append(f"{layout_id}/{lang}: worked-example entries do not match numbered positions")
    return issues
