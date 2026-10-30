# Cue and answer

`cue-answer` · `learning` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Cue and answer](previews/a5-draft.png)

Put a retrieval cue in the narrow column and a checkable answer in the wide one.

## When to use it

**Geometry relationship:** `equivalent` · [two-left-narrow](../two-left-narrow/README.en.md)

- Put self-test questions in the narrow column and practice recall with the wider answer area covered.
- Match short cues to full explanations after reading and identify questions you cannot answer unaided.

## How to use it

1. Write a short self-test question in the narrow left column and its full answer on the right.
2. Cover the right column, recall the answer from the question, then uncover and compare.
3. Turn incomplete answers into clearer cues or add the missing explanation.

## What the page helps you see

Concepts, cues, and recalled answers that can be checked against one another.


## Worked example

Entries in example-position order; each number identifies one entry:

1. Light and leaf color?
2. Window leaves darker; control watering too.

![Cue and answer worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Leaving the answer visible can turn recognition into an apparent recall success; overly revealing cues or unsupported answers also weaken the self-test.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Generic geometry · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Edit geometry in `src/noteformats/variants.py` or text in `src/noteformats/variant_content.py`, then run from the project root:

`python scripts/build.py --ids cue-answer`
