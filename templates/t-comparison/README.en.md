# T comparison

`t-comparison` · `comparison` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![T comparison](previews/a5-draft.png)

State one question above and place two possible answers in the columns below.

## When to use it

**Geometry relationship:** `parameter` · [two-equal-columns](../two-equal-columns/README.en.md)

- Compare two venues for one gathering.
- Sort reasons for and against a claim.

## How to use it

1. Write the comparison question in the upper band.
2. Assign one option or stance to each side.
3. Add evidence item by item, then identify what information is missing.

## What the page helps you see

Options compared against shared criteria rather than one impression.


## Worked example

A fictional reading group asks where to meet, comparing a library with an outdoor pavilion.

![T comparison worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

More than two options or numeric weighting need another structure.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Adaptation of a traditional format · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:

`python scripts/build.py --ids t-comparison`
