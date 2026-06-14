# Availability Matrix — Acquire Off-the-Shelf

**Spec:** EMBLEM-NLP-RSPEC-002 · **Objective 2:** how each (mainly electrical) drawing can be
obtained rather than produced. Categories: **a** free from ASUS · **b** free, self-captured from
photos · **c** paid third-party · **d** not available / must be derived.

| Drawing (A01–E07) | Agent | Category | Usability | Source / route |
|-------------------|-------|----------|-----------|----------------|
| Boardview C01 (+A09 netlist, +C03 test points) | AG-10 | **c** | 1 | H7604JV Rev 2.1 `.FZ`; OpenBoardView/FlexBV (FZ key operator-sourced) |
| Schematic A01 | AG-11 | **c / d** | 1 | paid database; else derive partial from boardview |
| Connector map C04 / harness A14 | AG-01 | **b** | 1 | self-captured from page-19 |
| Component placement A10 | AG-02 | **b** | 2 | self-captured from page-06/07 |
| Multi-view A12 / chassis E06 | AG-05/06 | **b** | 2–3 | self-captured from page-05 |
| Thermal B05/B07 | AG-03 | **b** | 2 | self-captured from page-17/18 |
| Exploded E05/E04 | AG-04 | **b** | 3 | self-captured from disassembly steps |
| Torque schedule (A05) | AG-12 | **b** | 3 | self-captured from page-22 torque table |
| Major-IC map (A10 partial) | AG-08 | **b** | 4 | self-captured from page-20/21 (CPU/GPU only) |
| Repair manual (whole) | — | **a** | — | free from ASUS (URL-only; cited, not redistributed) |
| Silkscreen C02 (full) | gap | **d** | — | derive from acquired boardview |
| PCB layout/Gerber/drill/stackup/fab; GD&T; cross-section; power tree; logic | gap | **d** (B02/A02: c) | — | not available; derive from schematic/boardview or CT |

**Headline:** the two electrical drawings that actually drive burn repair — **boardview (C01)** and
**schematic (A01)** — are **not** in the free ASUS set and must be acquired (category c). Everything
the photo set yields is category **b** (free, self-captured). The manual itself is category **a**.
