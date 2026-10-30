# Narrow left reference column

`two-left-narrow` · `columns` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Narrow left reference column](previews/a5-draft.png)

Keep brief references on the left and leave the wide area for continuous notes or drawings.

## When to use it

- Put source codes on the left while drawing a relationship map on the right.
- Use short interview themes beside fuller notes.

## How to use it

1. Reserve the left rail for short indexes rather than full sentences.
2. Record the main material on the right at roughly the same height as its cue.
3. Review using the rail and check that the main text still has enough context.

## What the page helps you see

Parallel notes whose agreements, differences, and unanswered points can be checked.


## Worked example

A fictional interview uses a venue cue at left and a description of entrances and seating at right.

![Narrow left reference column worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

For a bottom summary and self-testing by covering the main text, choose a Cornell layout.

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

Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:

`python scripts/build.py --ids two-left-narrow`
