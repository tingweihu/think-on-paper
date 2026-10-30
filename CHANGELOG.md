# Changelog

## Unreleased

- Added 144 downloadable A5 format IDs covering 127 distinct geometries, with 14 shared-geometry groups documented explicitly.
- Added wordless SVG/PDF, English-titled PDF, PDF-derived PNG previews, and matching worked examples in Traditional Chinese, English, and Japanese.
- Added local rebuild and QA scripts, trilingual guides, a source and rights inventory, and an MIT license for original project content.
- Made review identity independent of PNG encoding, separated public index generation from QA, and added clean-checkout and failure-preservation regression tests.
- Added darker-ink SVG/PDF options for every ID, corrected the five-whys relationship, and unified current catalog counts across audits.
- Rewrote variant-specific usage scenarios in all three languages, corrected named-method steps, and added copied-scenario and repeated-sentence checks.
- Standardized public text to LF and hardened CI repository permissions and untracked-file checks.
- Added format-specific limitations for previously shared text and a cross-format limitation audit; generated example entries now use numbered regions so commas within entries remain unambiguous.
- Added renderer preflight and `--pdftoppm` for build/QA, so a missing local tool stops once without replacing prior QA reports or classifying every format as broken.

No public release has been made from this checkout.
