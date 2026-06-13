# Laptop Electronics Drawing-Type Corpus

Execution output of **EMBLEM-NLP-RSPEC-001 v1.0.0** — *Research Agent Specification: Laptop
Electronics Drawing Type Discovery & Retrieval* (Emblem Projects Inc., 2026-06-12).

This corpus retrieves the single most accurate, highest-authority **publicly available** example of
each drawing type used in laptop electronics design, manufacturing, and repair. Every example is
traceable to a named standards body, OEM technical document, or verified open-hardware repository.
Generic diagrams, marketing infographics, AI-generated images, and DMCA-risk OEM schematic mirrors
are explicitly excluded.

## Key result

**38 drawing types** processed (the spec registry enumerates 38, although the objective/title says 45
— see `reports/gap-report.md` §0 for the reconciliation and the near-duplicate / plausibly-missing
analysis).

| Confidence | Count | Meaning |
|-----------|-------|---------|
| high | 17 | Tier 1–2 source, structural checks pass, content markers present |
| medium | 17 | Tier 2–3 source, most checks pass |
| low | 4 | Tier 3–4 or incomplete; human review recommended |

- **7** items flagged `human_review_required` (thermal, EMI, logic, single-line, boardview, rework).
- **4** items depend on a paywalled standard and use a fair-use / tutorial specimen (IEEE 91, IPC-2141, ASME Y14.5, IPC-7525).
- **0** items required dropping to Tier 4.
- **28 / 38** examples carry an open license (CC BY 4.0, GPL v3, CERN-OHL-S, BSD, public domain / FCC).
- **29 / 38** have a committed redistributable file in `sources/`; the remaining 9 are
  non-redistributable by license (paywalled standards / vendor-restricted) and recorded as URLs.

## Repository layout

| Path | What it is |
|------|------------|
| `drawing-corpus.json` | **Main deliverable.** One record per drawing type (Section 8 schema): primary/fallback source, validation, confidence, license, and a `retrieval` block (status, `local_path`, `sha256`). |
| `sources/` | Retrieved + rendered example files — redistributable only (tree below). |
| `sources/MANIFEST.json` | Per-record retrieval status + a sha256 inventory of every committed file. |
| `sources/ATTRIBUTION.md` | Per-source license notices + the CC BY change notices for rendered derivatives. |
| `sources/fetch_sources.sh` | Optional helper to fetch the url-only items into a local (gitignored) cache. |
| `reports/` | Section 11 outputs — `summary-table.md`, `gap-report.md`, `license-matrix.md`. |
| `spec/EMBLEM-NLP-RSPEC-001.md` | The source specification, stored verbatim for traceability. |
| `tools/` | Generation scripts + `tools/README.md` — reproduce the rendered specimens and rebuild the metadata. |

```
sources/
├── framework-laptop-13/   CC BY 4.0  — 6 interface schematics, 2D drawing, connectors, README, OpenSCAD
│   └── _generated/                   — cadquery/OpenCASCADE isometric + section SVGs, exploded PNG (from CAD .stp)
├── kicad-demos/           GPL v3     — video/ + pic_programmer/ KiCad projects
│   └── video/_generated/             — KiCad 9.0.9 Gerbers/drill/IPC-D-356/placement/BOM/fab+assembly PDFs + video.brd
├── chromium-ec/           BSD-3      — EC firmware docs with state machines
├── mnt-reform/            CERN-OHL-S — open-hardware laptop motherboard schematic PDF
├── nasa/                  public dom — NASA-STD-8739.3 (cancelled 2011)
├── MANIFEST.json  ATTRIBUTION.md  fetch_sources.sh
```

## File formats

The **PDFs (14)** are the published or rendered *drawing documents* — schematics, datasheets, the
NASA standard, and the KiCad-rendered fabrication / assembly / drill drawings. Every other tracked
file falls into one of the groups below (counts from `git ls-files`). The short answer to "why so
many formats": each drawing *type* is represented by the artifact a real engineer would use for it —
editable CAD source, the standard manufacturing format, or a rendered view — not a screenshot.

**KiCad EDA source** — the GPL-v3 `video` + `pic_programmer` demo projects, committed so the
schematic (A01/A02) and PCB-layout (A03) types are real, *editable* specimens and every rendered
output below is reproducible.

| Format | # | Purpose |
|--------|---|---------|
| `.kicad_pcb` | 2 | Routed multi-layer PCB layout (A03; source of all fab outputs) |
| `.kicad_sch` | 10 | Hierarchical schematic sheets (A01/A02; source of the BOM) |
| `.kicad_pro` | 2 | KiCad project file (settings; ties schematic + PCB together) |
| `.kicad_sym` | 2 | Schematic symbol libraries |
| `.kicad_mod` | 36 | Footprint land-pattern modules — one per file, inside `*.pretty/` |
| `sym-lib-table`, `fp-lib-table` | 2, 2 | KiCad library-table config (no extension); required to open the project cleanly |
| `.wrl` | 3 | VRML 3D component models (KiCad 3D viewer) |
| `.wings` | 1 | Wings3D source a `.wrl` was authored from |

**Rendered fabrication outputs** — `sources/kicad-demos/video/_generated/`, produced by `kicad-cli`
(KiCad 9.0.9) from the `video` board. These standard manufacturing formats *are* the fab specimens.

| Format | # | Layer / content | Type |
|--------|---|-----------------|------|
| `.gtl` / `.gbl` | 1 / 1 | Top / bottom copper (Gerber RS-274X) | A08 |
| `.gto` / `.gbo` | 1 / 1 | Top / bottom silkscreen | C02 |
| `.gtp` / `.gbp` | 1 / 1 | Top / bottom solder paste | A13 |
| `.gts` / `.gbs` | 1 / 1 | Top / bottom solder mask | A08 |
| `.gbr` | 2 | Fab layers (F.Fab / B.Fab) | A08 |
| `.gm1` | 1 | Edge.Cuts board outline | A08 |
| `.gbrjob` | 1 | Gerber job file (JSON index describing the set) | A08 |
| `.drl` | 1 | Excellon drill (hole coordinates + sizes) | A06 |
| `.d356` | 1 | IPC-D-356 bare-board test netlist | A09 / C03 |

**Other rendered specimens**

| Format | # | What / type |
|--------|---|-------------|
| `.csv` | 2 | BOM (D02) + pick-and-place placement (A10) — KiCad exports |
| `.brd` | 1 | OpenBoardView BRD2 boardview (C01), generated via the `pcbnew` API |
| `.svg` | 2 | cadquery isometric (E04) + true cross-section (D03) |
| `.png` | 1 | cadquery + matplotlib exploded assembly (E05) |
| `.scad` | 1 | OpenSCAD parametric mechanical source (Framework tray) |

**Corpus metadata, docs & text specimens**

| Format | # | Purpose |
|--------|---|---------|
| `.json` | 2 | `drawing-corpus.json` (dataset) + `MANIFEST.json` (inventory + checksums) |
| `.md` | 14 | Dual role: **corpus docs** (README, `reports/*`, `spec/*`, `ATTRIBUTION.md`, `tools/README.md`) and **specimens** — Chromium EC state-machine docs (B-series) and the Framework READMEs (system block diagram, E01/B01) |
| `.sh` | 1 | `fetch_sources.sh` — pull url-only items into a gitignored cache |
| `.gitignore` | 1 | Ignores that cache (`sources/_fetch_cache/`) |
| `.py` | 5 | `tools/` generation scripts — boardview, CAD renders, mesh cache, and the corpus builder |

**License files** (the legal basis for redistribution)

| File | # | License |
|------|---|---------|
| `LICENSE` (no ext) | 3 | Framework CC BY 4.0 · Chromium EC BSD-3 · MNT Reform CERN-OHL-S v2 |
| `LICENSE.GPLv3` | 1 | KiCad demos GPL v3 |
| `.txt` | 1 | `CERN-OHL-S-v2.txt` (full license text) |

> **Naming quirk:** the top-copper Gerber is `video-top_copper.gtl` (vs `video-B_Cu.gbl`) — that is
> the demo board's own F.Cu layer name, not an inconsistency introduced here.

## Retrieval policy & integrity

Files were retrieved on 2026-06-13 under a **links-only policy**: only redistributable artifacts are
committed; paywalled, vendor reference-only, and copyright-restricted sources are recorded as URLs in
`sources/MANIFEST.json` (nothing downloaded). **107 files (~22 MB)** are committed.

| Retrieval status | Count | Notes |
|------------------|-------|-------|
| committed (file) | 29 | Exact upstream files **plus** the rendered drawing-type specimens (Gerbers/drill/IPC-D-356/placement/BOM/fab+assembly, the `pcbnew` boardview, and the cadquery isometric/section/exploded views). |
| url-only | 9 | Paywalled / reference-only / copyright-restricted — link only. |

Integrity: every committed file is checksummed in `sources/MANIFEST.json`, and each committed record
in `drawing-corpus.json` carries the `sha256` of its primary file. Retrieve url-only items for
personal use with `bash sources/fetch_sources.sh` (paywalled/account-gated items must be obtained via
their portals).

## Primary verified sources (seeds)

| Seed | Source | Covers | License |
|------|--------|--------|---------|
| SEED-01 | [FrameworkComputer/Framework-Laptop-13](https://github.com/FrameworkComputer/Framework-Laptop-13) | Schematic, block diagram, power tree, 2D/fab, assembly, connectors/harness, chassis, exploded, BOM | CC BY 4.0 |
| SEED-02 | [KiCad demos](https://gitlab.com/kicad/kicad/-/tree/master/demos) (`video`, `pic_programmer`) | PCB layout, fab, drill, netlist (IPC-D-356), placement, silkscreen, Gerber | GPL v3 |
| SEED-03 | [MNT Reform](https://source.mnt.re/reform/reform) | Full open-hardware laptop KiCad package (fallback) | CERN-OHL-S 2.0 |
| SEED-04 | [Intel EDC](https://edc.intel.com) | Block/power/bus/memory/thermal/system architecture (reference only) | Intel reference use |
| SEED-05 | [FCC OET EAS](https://apps.fcc.gov/oetcf/eas/reports/GenericSearch.cfm) | EMI / shielding (internal photos in RF test reports) | Public domain |
| SEED-06 | [Chromium EC](https://chromium.googlesource.com/chromiumos/platform/ec) | State machine, timing (EC firmware docs) | BSD 3-Clause |
| SEED-07 | [NASA-STD-8739.3](https://standards.nasa.gov/standard/nasa/nasa-std-87393) | Rework / repair (public domain; note: cancelled 2011, superseded by J-STD-001) | Public domain |

Additional verified standards-body / vendor sources: JEDEC JESD79-5D (DDR5) and JESD209-5 (LPDDR5),
[SMBus 3.2 spec](https://www.smbus.org/specs/SMBus_3_2_20220112.pdf) (freely downloadable timing
diagrams), [TI Power Topologies](https://www.ti.com/lit/ml/sluw001g/sluw001g.pdf), and Sierra Circuits
(protoexpress.com) IPC tutorials.

## How to read a record

Each `drawing-corpus.json` record follows the Section 8 schema: `drawing_type`, `group`, `domain`,
`governing_standard`, `example_title`, `source_tier`, `source_type`, `source_url` (plus
`native_file_url` / `rendered_view_url` for software-native files per EC-2), `file_format`,
`native_format`, `license`, a `validation` block (`title_block`, `standard_referenced`,
`revision_block`, `drawing_number`, `scale`, `content_check`), `confidence`, `notes`,
`fallback_source`, `human_review_required`, and `paywalled`.

## Method & honest limitations

- This run **verified** the canonical seed repositories and key standards/vendor URLs live
  (Framework repo tree and license, KiCad demo set, NASA standard status, JEDEC/SMBus/TI pages,
  FCC OET, MNT Reform, ASME/GD&T fair-use specimens) via web search/fetch on 2026-06-12.
- For paywalled standards (IEEE/IPC/ASME) the run did **not** bypass paywalls (Section 12 guardrail);
  it records the normative purchase URL and supplies a fair-use or open specimen as the retrievable example.
- Several records point at a **stable entry point** rather than a single immutable file where the best
  example is a figure embedded in a large platform PDF (EC-1) or a selection in a live database
  (FCC OET) — these are marked `human_review_required` so a person can pin the exact exhibit/figure.
- A genuine **sequential-thinking MCP tool was not available** in this environment; the spec's
  step-by-step execution flow (CLASSIFY → SEED CHECK → SEARCH → FETCH → VALIDATE → RECORD) was
  applied as a structured orchestrated retrieval instead.
- **Retrieval (2026-06-13):** files were fetched via blobless/sparse `git clone` and `curl` from the
  canonical upstreams (GitHub, the KiCad GitHub mirror — GitLab anonymous clone is blocked on this
  egress, the GitHub API was rate-limited — googlesource, source.mnt.re, nepp.nasa.gov). Each PDF was
  verified as a real multi-page document and each KiCad/EC file as valid source, then checksummed
  (`sources/MANIFEST.json`). No paywall was bypassed and no DMCA-risk OEM schematic mirror was used.
- **KiCad 9.0.9** was then installed (kicad-9.0-releases PPA) and `kicad-cli` used to render the
  fabrication outputs (Gerbers, Excellon drill + map, IPC-D-356 netlist, placement CSV, BOM,
  fab/assembly PDFs) from the committed `video` demo into `sources/kicad-demos/video/_generated/`;
  the `pcbnew` Python API produced an OpenBoardView BRD2 `video.brd` (C01). *Scope: these electrical
  fab specimens are rendered from KiCad's generic `video` demo board (a drawing-type specimen), not a
  laptop board.*
- **cadquery / OpenCASCADE** rendered the isometric (E04, SVG), cross-section (D03, SVG — true
  cut-plane profile through the case at mid-width) and exploded (E05, shaded PNG — 107 solids
  tessellated and separated along the thickness axis) views from the Framework CAD `.stp` (fetched to
  a temp dir, not committed) into `sources/framework-laptop-13/_generated/`.

---
*Corpus generated 2026-06-12 per EMBLEM-NLP-RSPEC-001 v1.0.0; sources retrieved and rendered 2026-06-13.*
