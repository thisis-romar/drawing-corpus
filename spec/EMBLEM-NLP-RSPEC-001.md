# EMBLEM-NLP-RSPEC-001
## Research Agent Specification: Laptop Electronics Drawing Type Discovery & Retrieval
**Version:** 1.0.0
**Build Date:** 2026-06-12
**Author:** EMBLEM-NLP | Reverse Engineering — Embodied Agencies
**Status:** DRAFT — Ready for Agent Implementation

> Stored verbatim for traceability. Execution output: `../drawing-corpus.json` and `../reports/`.
> Note: the Section 2 registry enumerates 38 distinct drawing types; the objective states 45.
> See `../reports/gap-report.md` §0 for the reconciliation.

---

## 1. Objective
Retrieve the single most accurate, highest-authority publicly available example of each of the 45 drawing types used in laptop electronics design, manufacturing, and repair. Each retrieved example must be traceable to a named standard body, OEM technical document, or verified open hardware repository. Generic diagrams, marketing infographics, and unattributed images are explicitly rejected.

**Output:** One structured JSON record per drawing type, with primary source, fallback source, validation result, confidence level, and license status.

---

## 2. Drawing Type Registry

### Group A — Standard-Body Specimen Drawings
| # | Drawing Type | Governing Standard |
|---|---|---|
| A01 | Schematic Diagram | IEEE 315 / IEC 60617 |
| A02 | Logic Diagram | IEEE 91 |
| A03 | PCB Layout Drawing | IPC-2221 |
| A04 | Fabrication Drawing (Fab) | IPC-2221 / IPC-2222 |
| A05 | Assembly Drawing (PCBA) | IPC-7711/7721 |
| A06 | Drill Drawing / Drill Map | IPC-2221 |
| A07 | Layer Stackup Drawing | IPC-2141 |
| A08 | Gerber / ODB++ Output | RS-274X / IPC-2581 |
| A09 | Netlist (IPC-D-356) | IPC-D-356 |
| A10 | Component Placement Diagram | IPC-7351 |
| A11 | GD&T Drawing | ASME Y14.5 |
| A12 | Orthographic / Multi-View Drawing | ASME Y14.3 |
| A13 | Solder Paste / Stencil Drawing | IPC-7525 |
| A14 | Cable / Harness Drawing | IPC/WHMA-A-620 |

### Group B — OEM / Open Hardware Best Source
| # | Drawing Type | Best Source |
|---|---|---|
| B01 | Block Diagram | Intel Platform Design Guide / AMD Reference Design |
| B02 | Power Tree / Power Distribution Diagram | Intel Evo Platform Design Guide |
| B03 | Bus Topology Diagram | Intel PCIe Design Guide / JEDEC |
| B04 | Memory Topology Drawing | JEDEC JESD79-5 / Intel DDR5 Platform Guide |
| B05 | Thermal Management Drawing | Intel Thermal Mechanical Design Guide |
| B06 | EMI / Shielding Drawing | FCC OET Authorization DB (test reports) |
| B07 | Thermal / Airflow Diagram | Intel Thermal Mechanical Design Guide |
| B08 | Functional Block Diagram | AMD Reference Design / Qualcomm Platform Overview |
| B09 | Signal Flow Diagram | Pro audio / AV system design documentation |
| B10 | Single-Line Diagram | IEEE 315A / utility engineering references |

### Group C — Repair Domain / Open Hardware Repo
| # | Drawing Type | Best Source |
|---|---|---|
| C01 | Boardview (.brd / .fz) | Framework Laptop GitHub (CC-licensed) |
| C02 | Silkscreen / Legend Drawing | KiCad demo project export |
| C03 | Test Point Drawing | Framework Laptop GitHub + IPC-9252 |
| C04 | Interconnect / Connection Diagram | IPC-2612 + open hardware repo |

### Group D — Process / Manufacturing Drawings
| # | Drawing Type | Best Source |
|---|---|---|
| D01 | Rework / Repair Drawing | NASA-STD-8739.3 (public domain) / IPC-7711 preview |
| D02 | BOM (Bill of Materials) | IPC-2612 + Framework Laptop GitHub |
| D03 | Section View / Cross-Section | ASME Y14.3 + Framework mechanical drawings |

### Group E — System / Architecture Drawings
| # | Drawing Type | Best Source |
|---|---|---|
| E01 | System Architecture Diagram | Intel NUC Technical Specification |
| E02 | Timing Diagram | JEDEC LPDDR5 Spec / MIPI CSI-2 / SMBus Spec 3.2 |
| E03 | State Machine Diagram | Chromium EC Platform Firmware (open source) |
| E04 | Isometric Drawing | ASME Y14.3 / Manufacturer service manuals |
| E05 | Exploded Assembly Diagram | Framework Laptop service guide / iFixit teardowns |
| E06 | Chassis / Enclosure Drawing | Framework Laptop GitHub mechanical files |
| E07 | PCB Fabrication Drawing (Fab) | Framework Laptop GitHub / KiCad demo |

---

## 3. Source Tier Hierarchy
| Tier | Type | Trust Level |
|---|---|---|
| 1 | Standards bodies (IEEE Xplore, IPC.org, ASME, JEDEC, MIPI) | Highest — normative |
| 2 | OEM technical docs + open hardware (Intel EDC, AMD, FCC OET, Framework, MNT Reform, KiCad) | High |
| 3 | Educational / reference (MIT OCW, university EE, NASA, PCB-mfr tutorials) | Medium |
| 4 | Community / repair (EEVBlog, CircuitMaker, IPC preview docs) | Low |

**NEVER USE:** Stock photo sites, AI image generators, unattributed Pinterest/Flickr, OEM schematics scraped from repair sites (DMCA risk).

---

## 4. Canonical Seed URLs
- **SEED-01** https://github.com/FrameworkComputer/Framework-Laptop-13 — Schematic, Boardview, Fab, Assembly, BOM, Silkscreen, Test Points, Chassis, Exploded — CC BY 4.0
- **SEED-02** https://gitlab.com/kicad/kicad/-/tree/master/demos — PCB Layout, Fab, Drill, Netlist, Assembly, Placement, Silkscreen, Gerber — GPL v3
- **SEED-03** https://source.mnt.re/reform/reform — Full open hardware laptop PCB package — CERN OHL v1.2
- **SEED-04** https://edc.intel.com — Block, Power Tree, Bus, Memory, Thermal, Functional Block, System Architecture — Intel reference only
- **SEED-05** https://apps.fcc.gov/oetcf/eas/reports/GenericSearch.cfm — EMI / Shielding (RF test report PDFs) — Public domain
- **SEED-06** https://chromium.googlesource.com/chromiumos/platform/ec — State Machine, Timing (EC docs) — BSD 3-Clause
- **SEED-07** https://standards.nasa.gov/standard/nasa/nasa-std-87393 — Rework / Repair — Public domain

---

## 5–10. Query Patterns, Execution Flow, Validation, Output Schema, Hard Cases, Edge Cases
The full Pattern Library (A–E), 7-step execution flow, structural/content/provenance validation
criteria, reject criteria, the Section 8 output-record schema, the seven hard cases (HC-01…HC-07),
and edge cases (EC-1…EC-5) are reproduced from the source brief and were applied during this run.
Refer to the originating brief for the complete normative text. Per-record application is captured in
`../drawing-corpus.json` (`validation`, `notes`, `confidence`, `human_review_required`, `paywalled`).

Key hard-case handling applied:
- **HC-01 Boardview** — Framework/KiCad open PCBs converted to OpenBoardView; Apple/OEM `.fz` mirrors rejected (DMCA).
- **HC-02 Power Tree** — Framework README power tree (CC BY 4.0) primary; TI PowerLab fallback.
- **HC-03 Timing** — SMBus 3.2 (freely downloadable) + JEDEC LPDDR5.
- **HC-04 Rework** — NASA-STD-8739.3 (public domain; flagged cancelled 2011); IPC-7711 paywalled.
- **HC-05 Stencil** — Sierra Circuits / Sunstone tutorials + KiCad paste layer (IPC-7525 paywalled).
- **HC-06 EMI** — FCC OET internal-photos exhibits (public domain).
- **HC-07 State Machine** — Chromium EC chipset power-state machine (BSD); System76 EC fallback.

---

## 11. Aggregate Output
- `../reports/summary-table.md` (11.1)
- `../reports/gap-report.md` (11.2)
- `../reports/license-matrix.md` (11.3)

---

## 12. Legal & License Guardrails (applied)
No paywall bypass; no unauthorized OEM schematic mirrors; FCC and NASA treated as public domain;
Intel/AMD guides recorded as URL-only reference; KiCad GPL v3 and Framework CC BY 4.0 attributed.

---
*EMBLEM-NLP-RSPEC-001 v1.0.0 — Emblem Projects Inc. — 2026-06-12*
