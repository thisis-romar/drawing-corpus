# EMBLEM-NLP-RSPEC-002
## Reverse-Engineering Agent Specification: H7604JV Drawing Production & Acquisition
**Version:** 1.0.0
**Build Date:** 2026-06-14
**Author:** EMBLEM-NLP | Reverse Engineering — Embodied Agencies
**Status:** DRAFT — Ready for Agent Implementation

> Sibling to RSPEC-001 (drawing-type *discovery/retrieval*). Where RSPEC-001 catalogs generic
> open-hardware specimens of each A01–E07 drawing type, RSPEC-002 defines the agents that
> **produce or acquire** every drawing for one concrete target: the ASUS ProArt StudioBook 16 OLED
> **H7604JI/H7604JV** (mainboard **60NB10B0-MB3110**), driven by a CPU/VRM burn-repair need.
>
> Execution output: `../re-h7604/agents.json`, `../re-h7604/input-set.json`,
> `../re-h7604/reports/valuation.md`, and the extracted evidence in `../re-h7604/pages/`.

---

## 1. Objective
Produce the maximal set of mechanical, locational, and assembly drawings derivable from a fixed
**26-page ASUS repair manual photo set**, and **acquire** the electrical drawings that the photos
cannot yield (schematic, boardview). Every output is mapped to an RSPEC-001 **A01–E07** code, every
input is traceable to a rendered `page-NN.png`, and every valuation is confirmed against the actual
pixels (not the manual's prose). The burn-repair motivation (CPU/VRM failure, liquid-metal TIM
hazard) sets priority: locating and electrically characterizing the mainboard ranks above archival
completeness.

**Output:** one agent record per drawing (`agents.json`), a page-level evidence manifest
(`input-set.json`), and a per-drawing valuation report citing page images (`valuation.md`).

---

## 2. Evidence Base (Phase 0 — completed)
The source PDF was rendered with **pypdfium2 + Pillow** to two committed representations under
`../re-h7604/pages/`: **300 DPI** (`300dpi/page-01.png` … `page-26.png`, uniform 4001×2250 — the
canonical cited evidence base) and **native embedded-image extracts** (`native/`, 273 raw image
objects at original encoding, w≥64 & h≥64). Manifest: `../re-h7604/pages/_index.json` (per-file
`sha256`).

**Fidelity ceiling (Phase 0b).** The embedded board photos are natively **≤~1149×762 px**, so no
render DPI recovers more photo detail than `native/` — re-rendering the page higher only sharpens the
vector text. The `native/` extracts are the raw photos **without** the manual's overlaid callout
arrows/numbers (higher photo fidelity, no annotations) — which is why both representations are kept,
and why a higher-DPI page set is *not* retained (it would add bytes, not detail). This ceiling is the
physical basis for AG-08 ("major ICs only") and AG-09 ("slot/connector silkscreen only"); the AG-09
silkscreen confirmation used a transient 600 DPI render, recorded in the reports but not committed.
**Provenance:** these images are committed with the operator's explicit authorization (2026-06-15),
superseding the URL-only default for this asset (see §9 and `../re-h7604/SOURCES.md`).

**Page-count reconciliation:** the PDF is **26 pages**, matching the report's "26-page set." Report
references `p05–p21` map 1:1 onto `page-05`…`page-21` with no offset. (An early planning estimate
of 43 pages — made before a rasterizer was available — is withdrawn.)

Eight burn-critical pages were inspected at full 300 DPI (5, 6, 7, 18, 19, 20, 21, 22); the
remaining pages were verified via a contact sheet. Full inventory: `../re-h7604/input-set.json`.

Findings that corrected the source report's optimism (and one second-pass self-correction):
1. **page-20/21** are *material/mylar & bracket* placement pages, **not** a VRM component-location
   map — the CPU/GPU die zone is mylar-covered, so only the die positions are locatable (AG-08
   downgraded).
2. **Silkscreen is PARTIAL, not absent** — at 600 DPI the peripheral slot/connector silkscreen is
   legible (WLAN, SSD0, SSD1; IO board `N7604JV_IAR_BD R2.0`) → AG-09 (a first-pass "ABSENT" call
   was reversed after re-rendering at higher DPI). Full component-level legend still needs the
   acquired boardview.
3. **Torque schedule is comprehensive** — explicit torque tables appear on every FRU disassembly
   page (page-10/14/22…), so AG-12 is FULLY producible, not partial.

> **Unverified external assumptions** (flagged in `agents.json` → `target.unverified_external_assumptions`):
> the mainboard P/N `60NB10B0-MB3110` and boardview `Rev 2.1` are **not** confirmed by any inspected
> page; the only board rev confirmed from pixels is the IO board `R2.0`. Operator to verify before
> acquisition/rework. *(The liquid-metal **Conductonaut** TIM, by contrast, **is** confirmed — it is
> named in the page-09 required-materials list; see §9.)*

---

## 3. Agent Registry

| Agent | Produces (A01–E07) | Feasibility | Avail. | Evidence page(s) | Value |
|-------|--------------------|-------------|--------|------------------|-------|
| AG-01 Connector/Interconnect Map | C04, A14 | FULLY | b | **19** | 5 |
| AG-02 Component-Placement / Assembly | A10, A05 | PARTIAL | b | 6, 7, 20 | 4 |
| AG-03 Thermal / Airflow Layout | B05, B07 | PARTIAL | b | 17, 18 | 3 |
| AG-04 Exploded / Isometric Assembly | E05, E04 | PARTIAL | b | 6–8, 10–18, 22–26 | 3 |
| AG-05 Orthographic / Multi-View | A12 | PARTIAL | b | **5** | 3 |
| AG-06 Chassis / Enclosure Outline | E06 | PARTIAL | b | 5, 10 | 2 |
| AG-07 Coarse Block / Adjacency | B01 | PARTIAL | b | 19 | 2 |
| AG-08 Major-IC Location Map | A10 (partial) | PARTIAL | b | 20, 21 | 2 |
| AG-09 Silkscreen / Legend (slot/connector) | C02 | PARTIAL | b | 20, 22 | 3 |
| AG-12 Fastener / Torque Schedule | A05 | **FULLY** | b | 10, 14, **22**, 18, 25 | 4 |
| AG-10 Boardview Acquisition | C01, A09, C03 | ACQUIRE | c | — | 5 |
| AG-11 Schematic Acquisition | A01 | ACQUIRE | c/d | — | 5 |
| AG-13 Burn-Triage Workflow | D01 | PARTIAL | d | 4, 11 | 4 |

Availability categories: **a** free-from-ASUS · **b** free self-captured · **c** paid third-party ·
**d** not available / derive. Full records (tools, steps, outputs, guardrails): `agents.json`.

---

## 4. Input Photo Set
The 26-page manifest — page → content → visible labels → consuming agents — is in
`../re-h7604/input-set.json`. Highlights:
- **page-05** — 5-face orthographic overview with port/feature callouts (AG-05, AG-06).
- **page-06/07** — FRU identification grids, top & bottom (AG-02, AG-04).
- **page-18** — thermal module, dual-fan + heatpipe geometry, numbered screw sequence (AG-03, AG-12).
- **page-19** — *the crown jewel*: complete labelled mainboard connector-placement map (AG-01).
- **page-20/21** — mylar/kapton material & bracket placement; JI-vs-JV GPU differentiation (AG-08).
- **page-22** — IO board with an explicit torque table (AG-12).

---

## 5. Tool Registry (free-first)
Ranked free-first; full table with license/cost/role in `reports/tool-registry.md`.
Inkscape · GIMP · draw.io · LibreCAD/QCAD · FreeCAD+TechDraw · OpenBoardView · FlexBV (Free) ·
PCB Tracer · LibreOffice Calc. Existing repo helpers (`../tools/fw_explode.py`,
`../tools/cad_render.py`, `../tools/pcb2brd.py`) provide the 3D/boardview tool paths.

---

## 6. Feasibility & Availability Matrices
- Producible-from-photos ranking: `reports/feasibility-matrix.md`.
- Acquire-off-the-shelf (a/b/c/d) ranking: `reports/availability-matrix.md`.
- Evidence-confirmed per-drawing valuation: `reports/valuation.md`.

---

## 7. Orchestration / Execution Flow
- **Stage 1 — Document (free, photo-derived):** AG-01 … AG-08, AG-12 run in parallel off the
  rendered pages. AG-01 (connector map) and AG-02 (placement) are the highest-value Stage-1 outputs.
- **Stage 2 — Burn-repair (acquire + triage):** AG-10 (boardview) is the gating acquisition; on
  success, AG-13 cross-references the AG-08 die map and AG-10 rails for diode/continuity triage of
  the CPU/VRM burn site. AG-11 (schematic) runs opportunistically.
- **Decision threshold:** if AG-10 boardview is unobtainable, fall back to manual net tracing from
  the AG-08 major-IC map plus DMM measurement (AG-13).

---

## 8. Output Schema (`agents.json`)
Per-agent record: `agent_id`, `name`, `produces` [A01–E07], `drawing_type`, `feasibility`
(FULLY/PARTIAL/NOT-PRODUCIBLE/ACQUIRE), `availability_category` (a/b/c/d), `usability_rank`,
`value_rating` {documentation, burn_repair, overall}, `input_pages` [], `evidence` [] (cited
`page-NN.png`), `tools` [{name, license, cost, role}], `steps` [], `outputs` [], `effort`,
`fidelity_ceiling`, `guardrails` [], `next_best`, `source_report` (Methods&Tools | Availability).

---

## 9. Guardrails
1. **Fidelity ceiling** — all photo-derived outputs are illustrative and **uncalibrated** (no
   scale/GD&T); never present as dimensioned engineering drawings (NOT-TO-SCALE stamp required).
2. **No AI hallucination** — never synthesize nets, component values, reference designators, or
   back-side traces not visible in a cited page image.
3. **Boardview legality** — acquire `.FZ/.brd` through legitimate channels; no paywall bypass, no
   DMCA OEM-mirror redistribution; `.FZ` decryption key sourced separately by the operator; never
   commit the `.FZ`/key to this repo.
4. **Liquid-metal hazard (CONFIRMED in the manual, page-09)** — the page-09 required-materials list
   names **"Conductonaut 1g (Liquid Metal)"** as the CPU/GPU die TIM (alongside GA500 grease,
   FCR-AS, thermal pad); the manual also shows the kapton/mylar die zones (page-20/21). Liquid metal
   is electrically conductive: clean residue before powering and avoid bridging adjacent components
   during rework. Disconnect the battery (page-11) before probing.
5. **Provenance** — the ASUS repair manual is category a. The derived page images (300/600 DPI
   renders + native embedded-image extracts under `../re-h7604/pages/`) are **committed with the
   operator's explicit authorization (2026-06-15)**, superseding the RSPEC-001 §12 URL-only default
   for this asset; the **source PDF itself is not committed**. The images remain ASUS copyright,
   included as an internal repair-engineering evidence base (see `../re-h7604/SOURCES.md`).

---

## 10. Gap Registry (not producible — next-best acquisition)
| Codes | Drawing | Status | Avail. | Next best |
|-------|---------|--------|--------|-----------|
| C02 | Silkscreen / legend (full component-level) | PARTIAL via AG-09 | b/d | slot/connector silkscreen self-captured (AG-09); full legend → acquired boardview |
| A03, A08, A06, A07, A04, E07 | PCB layout / Gerber / drill / stackup / fab | NOT-PRODUCIBLE | d | partial from boardview, else not derivable |
| A11, D03 | GD&T / cross-section | NOT-PRODUCIBLE | d | CT / X-ray or vendor CAD |
| B02, A02 | Power tree / logic | NOT-PRODUCIBLE | c | derive from acquired schematic |

---

## 11. Legal & License Guardrails (applied)
No paywall bypass; no unauthorized OEM schematic/boardview mirrors; ASUS repair manual recorded
URL-only; all production tools are FOSS (GPL/LGPL/MPL/Apache/MIT) or free-tier. Consistent with
RSPEC-001 §12.

---
*EMBLEM-NLP-RSPEC-002 v1.0.0 — Emblem Projects Inc. — 2026-06-14*
