# Asymmetric mosaic cards

`mosaic-cards` · `cards` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Asymmetric mosaic cards](previews/a5-draft.png)

Separate a main item, supporting information, and short notes in four unequal cards.

## When to use it

- Record a large object drawing with specifications, materials, and questions.
- Place an article's main claim beside three types of annotation.

## How to use it

1. Put the content needing most room in the large upper-left card.
2. Use the other three for different support details without forcing equal length.
3. Review each side note against the main card to keep it relevant.

## What the page helps you see

Separate units that can be reordered, compared, or selected.


## Worked example

A fictional reading-corner sketch is the main card; lighting, seats, and an untested route occupy the others.

![Asymmetric mosaic cards worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Equal-sized topics waste space in unequal zones, and fixed-width tables need a regular grid.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Original layout · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:

`python scripts/build.py --ids mosaic-cards`
