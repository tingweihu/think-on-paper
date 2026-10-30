# Flow with open detail area

`flow-and-free` · `hybrid` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Flow with open detail area](previews/a5-draft.png)

Set a four-step main path above and draw exceptions or field notes freely below.

## When to use it

- Plan an event registration path and its exceptions.
- Describe borrowing a book and add likely reader problems.

## How to use it

1. Put four main actions in order across the top.
2. Use the open field for exceptions, returns, or observed situations.
3. Check whether those details change the main path and revise it if needed.

## What the page helps you see

A drawing, short notes, and a conclusion kept separate but connected.


## Worked example

A fictional loan path goes find, borrow, read, return; below it a missing-book or late-return branch is sketched.

![Flow with open detail area worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Four steps are an overview; use a full flow or swimlane for complex branches and responsibilities.

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

`python scripts/build.py --ids flow-and-free`
