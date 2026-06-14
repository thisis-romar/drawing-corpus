# H7604JV Drawing Valuation — Confirmed Against Extracted Page Imagery

**Spec:** EMBLEM-NLP-RSPEC-002
**Target:** ASUS ProArt StudioBook 16 OLED H7604JI/H7604JV — mainboard 60NB10B0-MB3110
**Evidence base:** all 26 PDF pages rendered to `../pages/page-NN.png` at 300 DPI (4001×2250).
**Method:** every rating below cites the specific page image it was confirmed against. Where the
input set cannot support a drawing, that is stated as **ABSENT** rather than scored optimistically.

> **Why this report exists.** The two source research reports ranked drawings from the *described*
> photo set. This valuation re-confirms each rating against the *actual rendered pixels*. Two
> ratings changed materially as a result (AG-08, AG-09 — see "Corrections" below).

## Legend

- **Feasibility:** `FULLY` / `PARTIAL` / `NOT-PRODUCIBLE` (from this photo set) / `ACQUIRE` (obtain off-the-shelf).
- **Availability category:** `a` free from ASUS · `b` free, self-captured · `c` paid third-party · `d` not available / derive.
- **Value (ROI):** combines **documentation value** (archival completeness) and **burn-repair value**
  (usefulness for diagnosing the CPU/VRM burn) on a 1–5 scale (5 = highest).

## A. Confirmed valuation — drawings PRODUCIBLE from the photo set

| Agent | Drawing (taxonomy) | Feasibility | Evidence page(s) | Usability | Value | Confirmed finding from pixels |
|-------|--------------------|-------------|------------------|-----------|-------|-------------------------------|
| AG-01 | Connector/Interconnect map (**C04**, **A14**) | **FULLY** | **page-19** | 1 | **5** | page-19 is a complete labelled connector-placement map (FAN, FFC_USB, LAN_IO_FPC, EDP, SPEAKER, CMOS, BL FPC, LED FFC, K/B FPC, BATTERY, TP FFC). Highest-value electrical asset in the set. |
| AG-02 | Component-placement / assembly (**A10**, **A05**) | **FULLY** (placement) / PARTIAL (assembly) | page-06, page-07, page-20 | 2 | 4 | page-06/07 name ~30 FRUs top+bottom; page-20 adds variant material zones. Board-level FRU placement is complete; net-level assembly is not. |
| AG-03 | Thermal / airflow layout (**B05**, **B07**) | **PARTIAL** | page-17, page-18 | 2 | 3 | page-18 shows dual-fan + heatpipe geometry and numbered screw sequence; airflow is inferable, not dimensioned. |
| AG-04 | Exploded / isometric assembly (**E05**, **E04**) | **PARTIAL** | page-06, page-07, page-08, page-10–18, page-22–26 | 3 | 3 | full disassembly sequence present; supports a 2.5D exploded illustration. No CAD geometry → illustrative only. |
| AG-05 | Orthographic / multi-view (**A12**) | **PARTIAL** (strong) | **page-05** | 2 | 3 | page-05 gives all 5 faces with port/feature callouts — a genuine multi-view. **No dimensions/scale** → silhouette/locational only, not a dimensioned drawing. |
| AG-06 | Chassis / enclosure outline (**E06**) | **PARTIAL** | page-05, page-10 | 3 | 2 | outer geometry + bottom-case fastener pattern recoverable as outline; uncalibrated. |
| AG-07 | Coarse block / adjacency diagram (**B01**) | **PARTIAL** | page-19 | 4 | 2 | connector adjacency on page-19 supports a coarse block diagram; no internal nets → topology only. |
| AG-12 | Fastener / torque schedule (assembly aid) | **PARTIAL** | **page-22**, page-18, page-10, page-14, page-25 | 3 | 3 | page-22 carries an explicit torque table (M2×3L, 2.0±0.2 kgf-cm, QTY 2); several pages show numbered screw maps → a partial torque schedule is producible. |

## B. Confirmed valuation — drawings requiring ACQUISITION (electrical, burn-critical)

| Agent | Drawing (taxonomy) | Feasibility | Availability | Usability | Value | Confirmed finding |
|-------|--------------------|-------------|--------------|-----------|-------|-------------------|
| AG-10 | Boardview .FZ/.brd (**C01** + embedded **A09**/**C03**) | **ACQUIRE** | **c** (paid) | **1** | **5** | Not in the photo set; the #1 burn-repair asset. Acquire H7604JV Rev 2.1 `.FZ`; open in OpenBoardView (+FZ key) / FlexBV. |
| AG-11 | Schematic (**A01**) | **ACQUIRE** | c / d | 1 | 5 | Not in set; paid databases only, not confirmed free. |
| AG-08 | Major-IC location map (**A10** partial) | **PARTIAL** (downgraded) | b | 4 | 2 | page-20/21 locate the CPU + GPU die and bracket footprint, **but the board is mylar-covered — no legible VRM phases or reference designators.** Targeting aid for major ICs only. |

## C. Gap registry — NOT producible AND not in the photo set

| Drawing (taxonomy) | Status | Availability | Next best |
|--------------------|--------|--------------|-----------|
| **C02** Silkscreen / legend (full) | **ABSENT** | d | derive from acquired boardview; mainboard silkscreen is mylar-covered in page-20/21 |
| A03 PCB layout · A08 Gerber · A06 drill · A07 stackup · A04/E07 fab | NOT-PRODUCIBLE | d | acquire boardview (partial), else not derivable |
| A11 GD&T · D03 cross-section | NOT-PRODUCIBLE | d | requires CT/X-ray or vendor CAD |
| B02 power tree · A02 logic | NOT-PRODUCIBLE | c/d | derive from acquired schematic |

## Corrections forced by the pixel-level review

1. **AG-08 (VRM/CPU component-location map): downgraded.** The plan and source report treated
   page-20/21 as a top-side component-location map. The rendered pixels show these are
   **material/mylar & bracket placement** pages — the board is covered in mylar/kapton, so only the
   CPU and GPU die positions are locatable. No VRM phases or reference designators are legible.
   Feasibility PARTIAL (major ICs only); value lowered 4→2.
2. **AG-09 / C02 (silkscreen transcription): removed from producible set.** There is no legible
   bare-board silkscreen anywhere in the 26 pages (page-20/21 are mylar-covered; page-19 is a
   connector-name overlay, not silkscreen). Moved to the Gap Registry as **ABSENT**. (The IO board
   on page-22 shows partial silkscreen only.)
3. **Page-count reconciliation:** PDF = **26 pages**, matching the report's "26-page set." The
   43-page figure used in early planning was an unverified guess and is withdrawn. Report refs
   p05–p21 map 1:1 onto `page-05`…`page-21` with no offset.
4. **AG-05 (multi-view) and AG-12 (torque schedule): confirmed stronger than the report implied.**
   page-05 is a real 5-face multi-view; page-22 carries an explicit torque table. Both retained as
   producible with cited evidence.

---
*EMBLEM-NLP-RSPEC-002 — valuation confirmed against extracted imagery — 2026-06-14*
