# Triangular grid

`triangular-grid` · `geometry` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Triangular grid](previews/a5-draft.png)

Use three equally spaced line directions to draft diagonal structures and triangular divisions.

## When to use it

- Sketch a surface built from triangular pieces.
- Compare diagonal bracing ideas.

## How to use it

1. Choose a provisional meaning for one triangle side.
2. Trace outlines along the three directions without treating the thumbnail as a precise measure.
3. Write down angles and dimensions that still need measurement.

## What the page helps you see

A draft of direction, proportion, or placement, with measurements still to check.


## Worked example

A fictional display stand marks three support points and a diagonal brace, leaving its dimensions to measure.

![Triangular grid worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Long prose and rectangular tables are awkward on triangles; an uncalibrated grid does not replace drafting tools.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Adaptation of traditional writing paper · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:

`python scripts/build.py --ids triangular-grid`
