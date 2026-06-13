# EMBLEM-NLP-RSPEC-001 — License Matrix

*Section 11.3 — retrieved examples grouped by license posture. Generated 2026-06-12 from `drawing-corpus.json`; retrieval status added 2026-06-13.*

## Retrieval status (links-only policy)

The actual example files were retrieved on 2026-06-13 under a **links-only policy**: only
redistributable artifacts are committed to `sources/`; paywalled, reference-only, and
copyright-restricted sources are recorded as URLs only. See `sources/MANIFEST.json`.

| Status | Count | Meaning |
|--------|-------|---------|
| committed (file) | 15 | The example artifact is a redistributable file committed under `sources/`. |
| committed (generated) | 11 | A standard KiCad output; the **generating project** is committed (run the recorded `generation_command`). |
| url-only | 12 | Paywalled / reference-only / copyright-restricted — recorded as a link, nothing downloaded. |

**26 / 38** drawing types have a committed redistributable specimen (84 files, ~18 MB). The 12
url-only IDs are: A07, A11, B04, B05, B06, B07, B09, B10, D03, E02, E04, E05. Note that "open
license" (28, below) and "committed" (26) differ: B06 (FCC public domain) was not pinned to a single
exhibit, and D03/E04/E05 (CC BY 4.0) derive from the 21 MB Framework CAD `.stp` kept url-only for size.

## Open (CC / CERN OHL / GPL / BSD / public domain / FCC)  (28)

| ID | Drawing Type | License (as recorded) |
|----|--------------|------------------------|
| A01 | Schematic Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| A03 | PCB Layout Drawing | GNU GPL v3 |
| A04 | Fabrication Drawing (Fab) | GNU GPL v3 |
| A05 | Assembly Drawing (PCBA) | GNU GPL v3 |
| A06 | Drill Drawing / Drill Map | GNU GPL v3 |
| A08 | Gerber / ODB++ Output | GNU GPL v3 |
| A09 | Netlist (IPC-D-356) | GNU GPL v3 |
| A10 | Component Placement Diagram | GNU GPL v3 |
| A12 | Orthographic / Multi-View Drawing | Creative Commons Attribution 4.0 (CC BY 4.0) |
| A14 | Cable / Harness Drawing | Creative Commons Attribution 4.0 (CC BY 4.0) |
| B01 | Block Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| B02 | Power Tree / Power Distribution Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| B03 | Bus Topology Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| B06 | EMI / Shielding Drawing | Public domain (FCC equipment-authorization submissions) |
| B08 | Functional Block Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| C01 | Boardview (.brd / .fz) | Creative Commons Attribution 4.0 (CC BY 4.0) |
| C02 | Silkscreen / Legend Drawing | GNU GPL v3 |
| C03 | Test Point Drawing | GNU GPL v3 |
| C04 | Interconnect / Connection Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| D01 | Rework / Repair Drawing | Public domain (US Government work) |
| D02 | BOM (Bill of Materials) | GNU GPL v3 (KiCad) / CC BY 4.0 (Framework) |
| D03 | Section View / Cross-Section | Creative Commons Attribution 4.0 (CC BY 4.0) |
| E02 | Timing Diagram | Public (SMBus spec freely downloadable from smbus.org) |
| E03 | State Machine Diagram | BSD 3-Clause |
| E04 | Isometric Drawing | Creative Commons Attribution 4.0 (CC BY 4.0) |
| E05 | Exploded Assembly Diagram | Creative Commons Attribution 4.0 (CC BY 4.0) |
| E06 | Chassis / Enclosure Drawing | Creative Commons Attribution 4.0 (CC BY 4.0) |
| E07 | PCB Fabrication Drawing (Fab) | Creative Commons Attribution 4.0 (CC BY 4.0) |

## Reference / publicly downloadable (redistribution restricted)  (3)

| ID | Drawing Type | License (as recorded) |
|----|--------------|------------------------|
| B04 | Memory Topology Drawing | JEDEC reference (free download with registration; redistribution restricted) |
| B09 | Signal Flow Diagram | TI reference (publicly downloadable application material) |
| E01 | System Architecture Diagram | Intel reference use (publicly downloadable TPS; redistribution restricted) |

## Reference only (no redistribution)  (2)

| ID | Drawing Type | License (as recorded) |
|----|--------------|------------------------|
| B05 | Thermal Management Drawing | Intel reference use only (no redistribution) |
| B07 | Thermal / Airflow Diagram | Intel reference use only (no redistribution) |

## Fair-use reproductions (educational, cites standard)  (5)

| ID | Drawing Type | License (as recorded) |
|----|--------------|------------------------|
| A02 | Logic Diagram | Fair use / CC (reproduced IEEE 91 symbols) |
| A07 | Layer Stackup Drawing | Reference / fair use (manufacturer educational content) |
| A11 | GD&T Drawing | Reference / fair use (educational, cites ASME Y14.5) |
| A13 | Solder Paste / Stencil Drawing | Reference / fair use (manufacturer educational content) |
| B10 | Single-Line Diagram | Fair use / CC (reproduced IEEE 315A symbols) |

## Redistribution guidance

- **Open bucket** — safe to redistribute with attribution (CC BY 4.0 → attribute Framework; GPL v3 → attribute KiCad; CERN-OHL-S → attribute MNT; BSD → attribute Chromium EC; public domain / FCC / NASA → no restriction).
- **Reference / publicly downloadable** — link only; do not embed/redistribute the PDF (JEDEC, SMBus, TI literature, Intel NUC TPS).
- **Reference only (no redistribution)** — Intel/AMD platform design guides: record URL only, never embed content.
- **Fair-use reproductions** — cite both the educational source and the original standard; do not present as the normative document.
