# Feasibility Matrix — Producible from the 26-Page Photo Set

**Spec:** EMBLEM-NLP-RSPEC-002 · **Objective 1:** what can be produced from the ASUS repair-manual
photos alone. Ratings confirmed against `../pages/page-NN.png` (see `valuation.md` for evidence).

| Rank | Agent | Drawing (A01–E07) | Feasibility | Evidence | Why |
|------|-------|-------------------|-------------|----------|-----|
| 1 | AG-01 | Connector/Interconnect map (C04, A14) | **FULLY** | page-19 | complete labelled connector-placement map |
| 2 | AG-02 | Component placement (A10, A05) | **FULLY** (placement) | page-06/07/20 | ~30 named FRUs top+bottom |
| 3 | AG-05 | Orthographic multi-view (A12) | PARTIAL (strong) | page-05 | 5 faces + port callouts, uncalibrated |
| 4 | AG-12 | Fastener/torque schedule (A05) | PARTIAL | page-22 +18/10/14/25 | explicit torque table present |
| 5 | AG-03 | Thermal/airflow (B05, B07) | PARTIAL | page-17/18 | fan+heatpipe geometry, inferred airflow |
| 6 | AG-04 | Exploded/isometric (E05, E04) | PARTIAL | page-08 + steps | full disassembly sequence, 2.5D only |
| 7 | AG-06 | Chassis/enclosure (E06) | PARTIAL | page-05/10 | outline + fastener pattern, uncalibrated |
| 8 | AG-07 | Coarse block (B01) | PARTIAL | page-19 | connector adjacency only |
| 9 | AG-08 | Major-IC location (A10 partial) | PARTIAL | page-20/21 | CPU/GPU die only — board mylar-covered |
| — | (C02) | Silkscreen/legend (full) | **NOT-PRODUCIBLE** | page-20/21 | no legible mainboard silkscreen (mylar) |
| — | A03/A08/A06/A07/A04/E07/A11/D03/B02/A02 | layout/fab/GD&T/power tree/logic | **NOT-PRODUCIBLE** | — | absent from photo set |

**Headline:** 8 producible drawing families (AG-01…AG-08, AG-12); 1 (connector map) is fully
producible. AG-08 and full silkscreen (C02) were downgraded after pixel-level review — the
mainboard is covered in mylar/kapton, so no reference-designator-level detail survives.
