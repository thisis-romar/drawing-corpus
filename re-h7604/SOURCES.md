# Sources & Provenance — EMBLEM-NLP-RSPEC-002

## Input asset (category a — free from ASUS)
- **ASUS ProArt StudioBook 16 OLED W7604J/N7604J/H7604J series repair (service) manual** —
  26 pages. Source: official ASUS support / repair documentation.
- **Source PDF provenance:** `proart_w7604j_series_2.pdf`, supplied by the operator;
  `sha256 38ae8be1e69314b3024a3d9b24c06facf8c9c074c53f798d2cb3c6cd98f34203` (4,315,208 bytes).
  *Official ASUS download URL: to be supplied by the operator* (the manual is freely distributed via
  ASUS support; record the exact URL here when available). The PDF itself is **not** committed.
- **Provenance decision (2026-06-15):** the rendered/extracted page images are **committed to this
  repo with the operator's explicit authorization**, superseding the earlier RSPEC-001 §12
  URL-only / not-redistributed default for this asset.
- Two committed representations under `pages/`, both derived with `pypdfium2` + `Pillow`
  (per-file `sha256` in `pages/_index.json`):
  - `300dpi/` — 26× 4001×2250 PNG flattened page renders (the canonical cited evidence base).
  - `native/` — 273 raw embedded image objects (original encoding, w≥64 & h≥64); board shots
    1149×762, extracted **without** the manual's overlaid callouts. See `pages/_index.json`.
  - *(A 600 DPI render set was produced during the audit but is **not** retained — at the ~1149 px
    native ceiling it adds no photo detail over 300 DPI, only file size.)*
- Page count **26** confirmed (matches the report's "26-page set"; the early 43-page planning
  estimate is withdrawn).
- **Fidelity ceiling:** embedded photos are natively ≤~1149×762 px; this caps recoverable detail
  regardless of render DPI (drives AG-08 "major ICs only" and AG-09 "slot/connector silkscreen only").

## Research artifact 1 — Methods & Tools Report (producibility)
Ranked which drawings are *producible* from the photo set and with which free-first tools
(Objective 1). Drives the Stage-1 producer agents AG-01…AG-08, AG-12. Captured as the
`feasibility` / `tools` / `steps` fields in `agents.json` and `reports/feasibility-matrix.md`.

> Pixel-level review corrected two of its rankings: AG-08 (page-20/21 are material/mylar pages,
> not a VRM component map) and full silkscreen C02 (no legible mainboard silkscreen — moved to
> the gap registry). See `reports/valuation.md` "Corrections".

## Research artifact 2 — Availability Table (acquisition)
Ranked how each electrical drawing can be *acquired* off-the-shelf, using categories
**a/b/c/d**. Drives the acquisition agents AG-10 (boardview), AG-11 (schematic), and the gap
registry. Captured as the `availability_category` field and `reports/availability-matrix.md`.

## Copyright note
The committed page images remain ASUS's copyrighted material; they are included here as an
internal repair-engineering evidence base under the operator's authorization, not relicensed.

## Taxonomy reference
A01–E07 drawing-type codes are defined in [`../spec/EMBLEM-NLP-RSPEC-001.md`](../spec/EMBLEM-NLP-RSPEC-001.md) §2.

## Tooling references (FOSS)
Inkscape (GPL v3), GIMP (GPL v3), draw.io (Apache-2.0), LibreCAD (GPL v2), FreeCAD (LGPL),
OpenBoardView (MIT), pypdfium2 (BSD/Apache), Pillow (MIT-CMU). Full table:
`reports/tool-registry.md`.

---
*If the two research reports should be captured verbatim (rather than summarized) for full
traceability, paste their text here under explicit "Report 1"/"Report 2" headings — the structure
above is ready to receive them.*
