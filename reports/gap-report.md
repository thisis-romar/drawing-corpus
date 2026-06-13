# EMBLEM-NLP-RSPEC-001 — Gap Report

*Section 11.2 — items needing follow-up. Generated 2026-06-12 from `drawing-corpus.json`.*

## 0. Count reconciliation (registry vs. objective)

The spec objective/title states **45** drawing types, but the Section 2 registry enumerates only **38** distinct entries (A01–A14 = 14, B01–B10 = 10, C01–C04 = 4, D01–D03 = 3, E01–E07 = 7). All 38 enumerated types are processed. The 7-entry gap is unresolved in the source spec. Likely contributors:

- **Near-duplicate types** already in the registry that may have been intended as distinct rows:
  - A04 *Fabrication Drawing* ≈ E07 *PCB Fabrication Drawing*
  - B01 *Block Diagram* ≈ B08 *Functional Block Diagram*
  - B05 *Thermal Management Drawing* ≈ B07 *Thermal / Airflow Diagram*
- **Plausibly-missing types** common in laptop electronics but absent from the registry (candidates to reach 45): Wiring Diagram, Pinout/Ball-Map Diagram, Impedance/Stack Calculation Sheet, Panelization/Array Drawing, Test Coverage/ICT Fixture Drawing, Thermal Profile (reflow) Drawing, Mechanical Tolerance Stack-up. **Recommend the spec author confirm the intended 45-item list.**

## 1. Low-confidence items (confidence = low)

| ID | Drawing Type | Reason | Recommended manual action |
|----|--------------|--------|---------------------------|
| A02 | Logic Diagram | IEEE 91 paywalled; no standalone laptop logic diagram exists (logic lives inside schematics). | Purchase IEEE 91/91a for a stamped specimen, or accept the KiCad-schematic applied example. |
| B05 | Thermal Management Drawing | Intel Thermal Mechanical Design Guide is account-gated/reference-only; no open-hardware laptop publishes a thermal mechanical drawing. | Retrieve via an Intel account, or generate a heatsink-footprint view from Framework cooling CAD. |
| B07 | Thermal / Airflow Diagram | Airflow/CFD diagrams are embedded in account-gated Intel guides; no open CFD specimen. | Source a vendor cooling white paper or university thermal-design course airflow figure. |
| B10 | Single-Line Diagram | Single-line diagrams belong to power systems, not laptop PCB design (nearest analog = power tree B02). | Accept an IEEE 315A educational specimen and annotate limited laptop applicability. |

## 2. Human-review-required items

| ID | Drawing Type | Paywalled? | Purchase / retrieval URL for follow-up |
|----|--------------|-----------|----------------------------------------|
| A02 | Logic Diagram | YES | https://standards.ieee.org/ieee/91/ (IEEE 91/91a — paywalled) |
| B05 | Thermal Management Drawing | no | https://edc.intel.com (Intel Thermal Mechanical Design Guide — account required) |
| B06 | EMI / Shielding Drawing | no | https://apps.fcc.gov/oetcf/eas/reports/GenericSearch.cfm (select specific FCC ID exhibit) |
| B07 | Thermal / Airflow Diagram | no | https://edc.intel.com (Intel Thermal Mechanical Design Guide — account required) |
| B10 | Single-Line Diagram | no | IEEE 315A educational reference (no single normative purchase needed) |
| C01 | Boardview (.brd / .fz) | no | https://github.com/OpenBoardView/OpenBoardView (convert open PCB to .fz; avoid DMCA mirrors) |
| D01 | Rework / Repair Drawing | no | https://www.ipc.org (IPC-7711/7721 — paywalled) / NASA-STD-8739.3 is public but cancelled |

## 3. Tier-4 (community/repair) sources used

None. No drawing type required dropping to Tier 4 — every type was satisfied at Tier 1–3 (open hardware, standards bodies, or educational/manufacturer references).


## 4. Paywalled standards (normative source not retrieved; specimen via fallback)

| ID | Drawing Type | Paywalled standard | Specimen strategy used |
|----|--------------|--------------------|------------------------|
| A02 | Logic Diagram | IEEE 91 (IEEE Std 91/91a, logic symbols) | IEEE 91 — fair-use symbol reference |
| A07 | Layer Stackup Drawing | IPC-2141 (controlled impedance) / IPC-4101 (materials) | IPC-2141/IPC-4101 — Sierra Circuits annotated stackup specimen |
| A11 | GD&T Drawing | ASME Y14.5-2018 | ASME Y14.5-2018 — GD&T Basics feature-control-frame specimen |
| A13 | Solder Paste / Stencil Drawing | IPC-7525 (stencil design) | IPC-7525 — Sierra Circuits/Sunstone stencil tutorial + KiCad paste layer |

## 5. Retrieval outcome (links-only, 2026-06-13)

The example files were retrieved and committed under `sources/` (manifest: `sources/MANIFEST.json`).
Under the links-only policy only redistributable artifacts were committed. Two toolchains were
installed to render derived specimens: **KiCad 9.0.9** (kicad-9.0-releases PPA) for the fabrication
outputs and a `.brd` boardview (via `pcbnew`), and **cadquery/OpenCASCADE** for the isometric and
section, and exploded views from the Framework CAD `.stp`.

- **29 committed as files** — A01, A02, A03, A04, A05, A06, A08, A09, A10, A12, A13, A14, B01, B02,
  B03, B08, C01, C02, C03, C04, D01, D02, D03, E01, E03, E04, E05, E06, E07. Includes the Framework
  CC BY 4.0 schematics/2D/connectors/README/OpenSCAD, the KiCad GPL v3 demo project, Chromium EC
  BSD-3 docs, NASA public-domain PDF, MNT Reform CERN-OHL-S schematic, the KiCad-rendered fab set
  under `kicad-demos/video/_generated/` (Gerbers incl. paste/silkscreen, Excellon drill + map PDF,
  IPC-D-356, placement CSV, fab/assembly PDFs, BOM CSV), the **OpenBoardView BRD2 boardview**
  (C01, `video.brd`), and the cadquery/OpenCASCADE-rendered **isometric** (E04, SVG), **section**
  (D03, SVG) and **exploded** (E05, shaded PNG) views under `framework-laptop-13/_generated/`. Each
  rendered/derived record keeps its `generation_command`.
- **9 url-only** — A07, A11 (paywalled IPC-2141 / ASME Y14.5; reference specimens), B04 (JEDEC,
  registration), B05/B07 (Intel EDC, account-gated reference-only), B06 (FCC OET search entry; no
  single exhibit pinned), B09 (TI app note, copyright-restricted), B10 (IEEE 315A reference),
  E02 (SMBus 3.2 / JEDEC, copyright-restricted). All are paywalled, account-gated, or
  copyright-restricted; retrieve for personal use with `sources/fetch_sources.sh`.

**No open follow-up:** every redistributable or derivable drawing type now has a committed specimen.
The 9 url-only types are non-redistributable by license (standards bodies / vendor-restricted) and
cannot be committed; they remain recorded as URLs with their license and access notes.