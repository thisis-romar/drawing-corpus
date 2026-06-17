# H7604JV Drawing Valuation — Confirmed Against Extracted Page Imagery

**Spec:** EMBLEM-NLP-RSPEC-002
**Target:** ASUS ProArt StudioBook 16 OLED H7604JI/H7604JV — mainboard 60NB10B0-MB3110
**Evidence base:** all 26 PDF pages committed in two representations under `../pages/` —
`300dpi/` (4001×2250, the cited renders below) and `native/` (273 raw embedded image objects at
~1149×762). See `../pages/_index.json`.
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
| AG-12 | Fastener / torque schedule (assembly aid) | **FULLY** | page-10, page-14, **page-22**, page-18, page-25 | 3 | 4 | explicit torque tables on **every** FRU disassembly page (confirmed page-10 bottom case, page-14 battery, page-22 IO board — all 2.0±0.2 kgf-cm with per-screw M-specs) → a near-complete torque schedule is producible. |
| AG-09 | Silkscreen / legend (slot/connector level) (**C02**) | **PARTIAL** | page-20, page-22 | 3 | 3 | at 600 DPI, peripheral slot/connector silkscreen is legible (WLAN, SSD0, SSD1 on page-20; IO board name+rev `N7604JV_IAR_BD R2.0` + designators on page-22). CPU/GPU zone mylar-covered; fine-pitch R/C/U designators not legible. |

## B. Confirmed valuation — drawings requiring ACQUISITION (electrical, burn-critical)

| Agent | Drawing (taxonomy) | Feasibility | Availability | Usability | Value | Confirmed finding |
|-------|--------------------|-------------|--------------|-----------|-------|-------------------|
| AG-10 | Boardview .FZ/.brd (**C01** + embedded **A09**/**C03**) | **ACQUIRE** | **c** (paid) | **1** | **5** | Not in the photo set; the #1 burn-repair asset. Acquire H7604JV Rev 2.1 `.FZ`; open in OpenBoardView (+FZ key) / FlexBV. |
| AG-11 | Schematic (**A01**) | **ACQUIRE** | c / d | 1 | 5 | Not in set; paid databases only, not confirmed free. |
| AG-08 | Major-IC location map (**A10** partial) | **PARTIAL** (downgraded) | b | 4 | 2 | page-20/21 locate the CPU + GPU die and bracket footprint, **but the board is mylar-covered — no legible VRM phases or reference designators.** Targeting aid for major ICs only. |

## C. Gap registry — NOT producible AND not in the photo set

| Drawing (taxonomy) | Status | Availability | Next best |
|--------------------|--------|--------------|-----------|
| **C02** Silkscreen / legend (full component-level) | **PARTIAL** (slot/connector only — see AG-09) | b/d | slot/connector silkscreen self-captured (AG-09); full component-level legend → derive from acquired boardview |
| A03 PCB layout · A08 Gerber · A06 drill · A07 stackup · A04/E07 fab | NOT-PRODUCIBLE | d | acquire boardview (partial), else not derivable |
| A11 GD&T · D03 cross-section | NOT-PRODUCIBLE | d | requires CT/X-ray or vendor CAD |
| B02 power tree · A02 logic | NOT-PRODUCIBLE | c/d | derive from acquired schematic |

## Corrections forced by the pixel-level review

*(Items 5–7 were added in a second-pass self-audit that inspected pages at 600 DPI and opened
disassembly pages not read in the first pass — see "Audit gaps closed" below.)*

1. **AG-08 (VRM/CPU component-location map): downgraded.** The plan and source report treated
   page-20/21 as a top-side component-location map. The rendered pixels show these are
   **material/mylar & bracket placement** pages — the board is covered in mylar/kapton, so only the
   CPU and GPU die positions are locatable. No VRM phases or fine-pitch designators are legible.
   Feasibility PARTIAL (major ICs only); value lowered 4→2.
2. **Page-count reconciliation:** PDF = **26 pages**, matching the report's "26-page set." The
   43-page figure used in early planning was an unverified guess and is withdrawn. Report refs
   p05–p21 map 1:1 onto `page-05`…`page-21` with no offset.
3. **AG-05 (multi-view):** confirmed stronger than the report implied — page-05 is a real 5-face
   orthographic multi-view with port callouts (uncalibrated). Retained as producible.
4. **Provenance:** the rendered/extracted pages are the copyrighted ASUS asset; they are committed
   with the operator's explicit authorization (2026-06-15), superseding the RSPEC-001 §12 URL-only
   default for this asset. The source PDF itself is not committed. See [`../SOURCES.md`](../SOURCES.md).

### Audit gaps closed (second pass)

5. **C02 silkscreen: ABSENT → PARTIAL (over-correction reversed).** A 600 DPI re-render shows
   peripheral slot/connector silkscreen IS legible — `WLAN`, `SSD0`, `SSD1` on page-20, and the IO
   board name+revision `N7604JV_IAR_BD R2.0` plus connector designators on page-22. The first pass
   under-rated this by judging only the full-page 300 DPI render. New agent **AG-09** added.
6. **AG-12 torque schedule: PARTIAL → FULLY.** The first pass cited only page-22; opening
   page-10 (bottom case) and page-14 (battery) shows explicit torque tables on **every** FRU
   disassembly page. A near-complete fastener/torque schedule is producible. Value 3→4.
7. **Unverified external facts flagged.** Mainboard P/N `60NB10B0-MB3110` and boardview `Rev 2.1`
   are **not** confirmed by any inspected page (page-08 directs to the ASUS "Orderbook" for the
   SKU part number) — marked `unverified_external_assumptions` in `agents.json`. The only board
   revision confirmed from pixels is the IO board `R2.0` (page-22).

### Full-sweep findings (all 26 pages read at full resolution)

8. **Liquid-metal hazard is CONFIRMED, not assumed (reverses correction #7's first draft).** The
   page-09 required-materials list explicitly names **"Conductonaut 1g (Liquid Metal)"** as the
   die TIM (with GA500 grease, FCR-AS, thermal pad). The hazard guardrail is manual-stated.
9. **AG-01 gains a second connector reference.** page-17 ("MB with THERMAL MODULE and FAN") shows
   every MB connector being disconnected with a close-up label (LAN_IO_FPC, EDP, CMOS, FAN, TP,
   LED, BL, SPEAKER) — it pairs with the page-19 placement map. Antenna routing (page-15
   MAIN/AUX) and speaker/wifi cable tidy paths (page-23) further feed the harness drawing.
10. **AG-12 torque schedule is broader than the second pass found.** Explicit torque tables appear
    on **10** disassembly pages (10,12,14,15,16,17,22,24,25,26) with real spec variation —
    M1.6 @ 1.0, M2 @ 2.0, M2.5 @ 3.0 kgf-cm. Confirms FULLY producible with strong coverage.
11. **Native resolution sets a hard fidelity ceiling (Phase 0b).** Extracting the raw embedded
    image objects (`../pages/native/`) shows the mainboard photos are stored at only **1149×762 px**
    (e.g. `native/page-19-img02.jpg`, the bat-wing board shot). The 300 DPI page render is an
    *upscale* of these same pixels — re-rendering higher (a transient 600 DPI pass was used to read
    silkscreen during this audit) sharpens the vector callouts but adds **no** new photo detail, so
    no higher-DPI set is committed. This is the physical reason AG-08 stays "major ICs only" and AG-09
    stays "slot/connector silkscreen only": the detail is not in the source pixels at any DPI. Note the
    native extracts are the raw photos *without* the manual's overlaid callout arrows/numbers — so
    the `300dpi/` renders remain the better evidence for reading labels, `native/` for the raw photo.

---
*EMBLEM-NLP-RSPEC-002 — valuation confirmed against extracted imagery — 2026-06-14;
native-resolution fidelity ceiling + committed image set added 2026-06-16*
