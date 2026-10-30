# Indented outline notes

`outline-notes` · `learning` · `a5-draft`

[繁體中文](README.zh-TW.md) · [English](README.en.md) · [日本語](README.ja.md) · [Back to catalog](../../docs/en/catalog.md)

![Indented outline notes](previews/a5-draft.png)

Show topics, subtopics, and examples with three visible indent levels.

## When to use it

- Organize three sections of a talk with their details.
- Arrange a short essay's skeleton before drafting.

## How to use it

1. Put a topic on the first line of each group.
2. Indent subtopic and example one level at a time, keeping each under its parent.
3. Read the outline back and move or rewrite lines whose level is unclear.

## What the page helps you see

Concepts, cues, and recalled answers that can be checked against one another.


## Worked example

A fictional talk has background, demonstration, and discussion sections, each with a point and an example below it.

![Indented outline notes worked example](examples/en.svg)

[SVG](examples/en.svg)

## When not to use it

Indentation does not show time, causality, or rank; use a network for many cross-links.

## Downloads

- [Wordless SVG](exports/a5-draft/blank.svg)
- [Wordless PDF](exports/a5-draft/blank.pdf)
- [PDF with English name at top left](exports/a5-draft/titled.pdf)
- [Darker-ink wordless PDF](exports/a5-contrast/blank.pdf)
- [Darker-ink SVG](exports/a5-contrast/blank.svg)

The English name appears only on the titled PDF; the wordless version remains available for free writing.

Page size: A5 (148 × 210 mm); profile: `a5-draft`.

## Provenance and status

Common geometry · Detailed source record: [manifest.json](manifest.json)  
[MIT license scope](../../LICENSE-SCOPE.md)

[Trilingual glossary](../../docs/en/glossary.md)

## Modify and rebuild

Change `profiles/a5-draft.json` or the corresponding builder in `src/noteformats/layouts/`, then run from the project root:

`python scripts/build.py --ids outline-notes`
