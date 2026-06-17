# re-h7604 — H7604JV Drawing Production & Acquisition Roster

Execution output of **[EMBLEM-NLP-RSPEC-002](../spec/EMBLEM-NLP-RSPEC-002.md)** — the agent
specification for producing/acquiring every drawing of the ASUS ProArt StudioBook 16 OLED
**H7604JI/H7604JV** (mainboard 60NB10B0-MB3110), driven by a CPU/VRM burn-repair need.

> Part of the [laptop-electronics drawing-type corpus](../README.md) — this sub-project applies that
> corpus's `A01–E07` taxonomy to one specific machine.

## Contents
| Path | What |
|------|------|
| [`pages/300dpi/`](pages/300dpi/)`page-NN.png` | All 26 repair-manual pages rendered at 300 DPI (4001×2250) — the **canonical cited evidence base**. Flattened page renders (photo + vector callouts composited). |
| [`pages/native/`](pages/native/)`page-NN-imgKK.{jpg,png}` | The 273 **raw embedded image objects** (original encoding, w≥64 & h≥64) extracted at native resolution — the source photos **without** the manual's overlaid callouts/labels. Highest photo fidelity; the board shots are 1149×762. |
| [`pages/_index.json`](pages/_index.json) | Manifest of both representations per page (pixel dims, native-image dims, `dup_of` chrome flags, per-file `sha256`). |
| [`pages/_contact-sheet.png`](pages/_contact-sheet.png) | Thumbnail index of the 26 pages. |
| [`input-set.json`](input-set.json) | Page-level manifest: content, visible labels, consuming agents, page-count reconciliation. |
| [`agents.json`](agents.json) | Machine-readable agent roster (13 agents + gap registry). |
| [`outputs/`](outputs/README.md) | Produced drawing artifacts (e.g. the AG-01 connector map) — original vector derivatives. |
| [`reports/valuation.md`](reports/valuation.md) | Per-drawing valuation, each rating confirmed against a cited page image. |
| [`reports/feasibility-matrix.md`](reports/feasibility-matrix.md) | Producible-from-photos ranking. |
| [`reports/availability-matrix.md`](reports/availability-matrix.md) | Acquire-off-the-shelf (a/b/c/d) ranking. |
| [`reports/tool-registry.md`](reports/tool-registry.md) | Free-first tool table (license + cost). |
| [`SOURCES.md`](SOURCES.md) | The two source research reports + the input PDF provenance. |

## How to read it
1. Start with [`reports/valuation.md`](reports/valuation.md) — it ranks every drawing by feasibility
   and value and points at the exact [`pages/300dpi/`](pages/300dpi/)`page-NN.png` evidence behind
   each rating.
2. [`agents.json`](agents.json) is the executable roster: one record per drawing, with the
   free-first tool chain, steps, outputs, and guardrails.
3. The A01–E07 codes in `produces` reference the taxonomy in
   [`../spec/EMBLEM-NLP-RSPEC-001.md`](../spec/EMBLEM-NLP-RSPEC-001.md) §2.

## Key facts
- **26 pages** (matches the report's "26-page set"); report refs p05–p21 = `page-05`…`page-21`.
- **Highest-value photo-derived drawing:** AG-01 connector map from **page-19** (FULLY producible).
- **Highest-value overall:** AG-10 boardview acquisition (not in photos; the #1 burn-repair asset).
- **Hazard:** the page-09 materials list names **Conductonaut (liquid-metal) TIM** on the CPU/GPU
  die — electrically conductive; see [`../spec/EMBLEM-NLP-RSPEC-002.md`](../spec/EMBLEM-NLP-RSPEC-002.md) §9.

## Regenerating / extracting the page assets
Both representations are committed (see [`SOURCES.md`](SOURCES.md) for the provenance decision), so this
is only needed to re-derive them from the source PDF:
```
pip install pypdfium2 Pillow
# Flattened page renders at 300 DPI (300dpi/):
python3 -c "import pypdfium2 as p; d=p.PdfDocument(SRC_PDF); [d[i].render(scale=300/72).to_pil().save(f'pages/300dpi/page-{i+1:02d}.png') for i in range(len(d))]"
# Raw embedded image objects at native resolution (native/), original encoding:
#   iterate page.get_objects(), keep FPDF_PAGEOBJ_IMAGE with w>=64 & h>=64, call obj.extract(stem).
```
(`SRC_PDF` = the ASUS ProArt W7604J/N7604J/H7604J series repair manual — see [`SOURCES.md`](SOURCES.md).)

> **Note on fidelity.** The embedded photos are natively only ~1149×762 px, so re-rendering the page
> above 300 DPI recovers **no** more photo detail than `native/` (it only sharpens the vector
> callouts) — which is why no higher-DPI page set is retained. The native extracts are the raw photos
> *without* the manual's overlaid callout arrows/numbers. *(Fine silkscreen reading during the audit
> used a transient 600 DPI render; that confirmation is recorded in the reports but the 600 DPI
> images are not committed.)*
