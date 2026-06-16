# Sources & Provenance — EMBLEM-NLP-RSPEC-002

## Input asset (category a — free from ASUS, recorded URL-only)
- **ASUS ProArt StudioBook 16 OLED W7604J/N7604J/H7604J series repair (service) manual** —
  26 pages. Source: official ASUS support / repair documentation.
- Provenance policy (per RSPEC-001 §12): recorded **URL-only**; the PDF is **not redistributed** in
  this repo. The manual was rendered locally to `pages/page-NN.png` for analysis; page numbers are
  cited throughout the spec and reports.
- Rendered with `pypdfium2` + `Pillow` at 300 DPI → 26× 4001×2250 PNG. Page count **26** confirmed
  (matches the report's "26-page set"; the early 43-page planning estimate is withdrawn).

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

## Taxonomy reference
A01–E07 drawing-type codes are defined in [`../../spec/EMBLEM-NLP-RSPEC-001.md`](../../spec/EMBLEM-NLP-RSPEC-001.md) §2.

## Tooling references (FOSS)
Inkscape (GPL v3), GIMP (GPL v3), draw.io (Apache-2.0), LibreCAD (GPL v2), FreeCAD (LGPL),
OpenBoardView (MIT), pypdfium2 (BSD/Apache), Pillow (MIT-CMU). Full table:
`reports/tool-registry.md`.

---
*If the two research reports should be captured verbatim (rather than summarized) for full
traceability, paste their text here under explicit "Report 1"/"Report 2" headings — the structure
above is ready to receive them.*
