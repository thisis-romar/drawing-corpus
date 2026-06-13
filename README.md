# Laptop Electronics Drawing-Type Corpus

Execution output of **EMBLEM-NLP-RSPEC-001 v1.0.0** — *Research Agent Specification: Laptop
Electronics Drawing Type Discovery & Retrieval* (Emblem Projects Inc., 2026-06-12).

This corpus retrieves the single most accurate, highest-authority **publicly available** example
of each drawing type used in laptop electronics design, manufacturing, and repair. Every example is
traceable to a named standards body, OEM technical document, or verified open-hardware repository.
Generic diagrams, marketing infographics, AI-generated images, and DMCA-risk OEM schematic mirrors
are explicitly excluded.

## Contents

| Path | Description |
|------|-------------|
| `drawing-corpus.json` | **Main deliverable.** One structured record per drawing type (Section 8 schema): primary source, fallback source, validation result, confidence, license, and a `retrieval` block (status, `local_path`, `sha256`). |
| `sources/` | **Retrieved example files** (committed, redistributable only — see below). |
| `sources/MANIFEST.json` | Machine manifest: per-record retrieval status + a sha256 inventory of every committed file. |
| `sources/ATTRIBUTION.md` | Per-source license notices (CC BY 4.0 / GPL v3 / BSD / CERN-OHL-S / public domain). |
| `sources/fetch_sources.sh` | Optional helper to fetch the url-only items into a local (gitignored) cache for personal use. |
| `reports/summary-table.md` | Section 11.1 — one row per type (group, confidence, tier, license, **retrieved status**, flags). |
| `reports/gap-report.md` | Section 11.2 — low-confidence items, human-review items, paywalled standards, and the registry count reconciliation. |
| `reports/license-matrix.md` | Section 11.3 — examples grouped by license posture with redistribution guidance. |
| `spec/EMBLEM-NLP-RSPEC-001.md` | The source specification, stored verbatim for traceability. |

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
- **29 / 38** have a committed redistributable file in `sources/` (see *Retrieved files* below);
  the remaining 9 are non-redistributable by license (paywalled standards / vendor-restricted).

## Retrieved files (`sources/`)

The example files were retrieved on 2026-06-13 under a **links-only policy**: only redistributable
artifacts are committed; paywalled, vendor reference-only, and copyright-restricted sources are
recorded as URLs in `sources/MANIFEST.json` (nothing downloaded). **107 files (~24 MB)** are committed.

| Retrieval status | Count | Notes |
|------------------|-------|-------|
| committed (file) | 29 | Exact/derived artifact committed — Framework PDFs, EC docs, NASA PDF, MNT schematic, KiCad project + KiCad 9.0.9-rendered Gerbers/drill/IPC-D-356/placement/BOM/fab+assembly + a `pcbnew`-generated boardview, and cadquery-rendered isometric/section/exploded views from the CAD. |
| url-only | 9 | Paywalled / reference-only / copyright-restricted — link only. |

```
sources/
├── framework-laptop-13/   CC BY 4.0  — 6 interface schematics, 2D drawing, connectors, README, OpenSCAD
│   └── _generated/                   — cadquery/OpenCASCADE isometric + section SVGs, exploded PNG (from CAD .stp)
├── kicad-demos/           GPL v3     — video/ + pic_programmer/ KiCad projects
│   └── video/_generated/             — KiCad 9.0.9 Gerbers/drill/IPC-D-356/placement/BOM/fab+assembly PDFs + video.brd boardview
├── chromium-ec/           BSD-3      — EC firmware docs with state machines
├── mnt-reform/            CERN-OHL-S — open-hardware laptop motherboard schematic PDF
├── nasa/                  public dom — NASA-STD-8739.3 (cancelled 2011)
├── MANIFEST.json  ATTRIBUTION.md  fetch_sources.sh
```

Integrity: every committed file is checksummed in `sources/MANIFEST.json`; each `committed` record in
`drawing-corpus.json` carries the `sha256` of its primary file. Retrieve url-only items for personal
use with `bash sources/fetch_sources.sh` (paywalled/account-gated items must be obtained via their portals).

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
*Generated 2026-06-12 per EMBLEM-NLP-RSPEC-001 v1.0.0.*
