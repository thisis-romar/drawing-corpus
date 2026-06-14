# Tool Registry — Free-First

**Spec:** EMBLEM-NLP-RSPEC-002. Tools are ranked free-first; every drawing in `agents.json` binds to
one or more of these. Existing repo helpers under `../../tools/` provide the 3D/boardview paths.

| Tool | License | Cost | Role | Used by |
|------|---------|------|------|---------|
| Inkscape | GPL v3 | free | vector trace board outlines, callouts, 2.5D explode | AG-01,02,03,04,05,06,08,12 |
| GIMP | GPL v3 | free | photo deskew/clean, annotation | AG-01,02,05,08 |
| draw.io (diagrams.net) | Apache-2.0 | free | interconnect / block diagrams | AG-01,03,07 |
| LibreCAD / QCAD | GPL v2 / GPL v3 | free | 2D orthographic + placement layout | AG-02,05,06 |
| FreeCAD + TechDraw | LGPL | free | optional true-3D exploded/iso views | AG-04 |
| LibreOffice Calc | MPL/LGPL | free | torque/fastener schedule tables | AG-12 |
| OpenBoardView | MIT | free | view acquired `.FZ/.brd` (needs FZ key) | AG-10 |
| FlexBV (Free tier) | freeware | free/paid | boardview viewer | AG-10 |
| PCB Tracer | freeware | free | manual net tracing / node analysis | AG-08,13 |
| DMM (diode/continuity) | hardware | operator | rail short detection | AG-13 |
| `../../tools/fw_explode.py` | repo | free | explode-render helper | AG-04 |
| `../../tools/cad_render.py` | repo | free | CAD render helper | AG-04 |
| `../../tools/pcb2brd.py` | repo | free | PCB→boardview helper | AG-10 |
| pypdfium2 + Pillow | BSD/Apache + MIT-CMU | free | render the source PDF to 300 DPI PNG (Phase 0) | evidence base |

**Paid/optional fallbacks (only if free path fails):** FlexBV Pro, paid boardview/schematic
databases (AG-10/AG-11, category c), CT/X-ray service (gap registry). No paywall bypass.
