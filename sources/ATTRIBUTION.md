# Attribution & License Notices — `sources/`

This directory contains the **example files** for EMBLEM-NLP-RSPEC-001, under the **links-only
policy**: only redistributable artifacts are committed here. Paywalled standards, vendor
reference-only documents, and free-but-copyright-restricted specs are *not* committed — they are
recorded as URLs in [`MANIFEST.json`](./MANIFEST.json) and can be retrieved with
[`fetch_sources.sh`](./fetch_sources.sh).

Two kinds of files are committed:

- **Committed as-is** — exact, unmodified copies of their upstream originals (the PDFs and project
  source trees described below).
- **Committed derived renders** — drawing-type specimens **generated from the committed open
  sources** and stored under `_generated/` directories. These are derivative works (modifications);
  the tool and exact command for each are recorded per record in `../drawing-corpus.json`
  (`retrieval.generation_command`), and the generation scripts live in [`../tools/`](../tools/).
  The derived files are:
  - `kicad-demos/video/_generated/` — produced from the KiCad `video` demo project with **KiCad
    9.0.9** (`kicad-cli`) and the `pcbnew` Python API: RS-274X Gerbers (incl. paste/silkscreen),
    Excellon drill + drill-map PDF, IPC-D-356 netlist, placement CSV, BOM CSV, fabrication &
    assembly PDFs, and an OpenBoardView BRD2 boardview (`video.brd`).
  - `framework-laptop-13/_generated/` — rendered from `Framework Laptop 13 CAD.stp` with
    **cadquery/OpenCASCADE** (+ matplotlib): isometric view (SVG), cross-section (SVG), and exploded
    assembly (PNG).

**Scope note:** the electrical fabrication specimens above are rendered from KiCad's generic `video`
demo board (a redistributable GPL-v3 example) — they are specimens of the *drawing type*, not
laptop-specific artifacts. The mechanical views (isometric / section / exploded) are the actual
Framework Laptop 13 CAD.

Per-record mapping (which drawing type each file serves) is in `MANIFEST.json` and in
`../drawing-corpus.json` (`retrieval`).

---

## `framework-laptop-13/` — © Framework Computer Inc.
- **Source:** https://github.com/FrameworkComputer/Framework-Laptop-13
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0) — see `framework-laptop-13/LICENSE`.
- **Attribution:** "Framework Laptop 13" by Framework Computer Inc., used under CC BY 4.0.
- **Committed as-is:** six `Mainboard_Interfaces_Schematic_*.pdf` interface schematics, the
  `Mainboard/2D` mechanical drawing PDF, two connector datasheets + `Connectors/README.md`,
  `Mainboard/README.md`, `OpenSCAD/tray.scad`, and the repo `README.md`.
- **Derived renders under `_generated/` (changes made):** isometric, cross-section, and
  exploded-assembly views were **rendered from `Framework Laptop 13 CAD.stp`** using
  cadquery/OpenCASCADE and matplotlib. Per CC BY 4.0 §3(a)(1)(B), changes are indicated here:
  *the 3D CAD model was rendered to 2D/pictorial drawing views; no design changes were made.* These
  adaptations remain under CC BY 4.0 with attribution to Framework Computer Inc.
- **Not committed (url-only, size):** `Framework Laptop 13 CAD.stp` (21 MB), `… Pro CAD.stp` (52 MB),
  the four `Mainboard/2D/*.dxf` vector files, and the Printable-Case STLs — fetch via `fetch_sources.sh`.

## `kicad-demos/` — © KiCad Developers
- **Source:** https://gitlab.com/kicad/kicad/-/tree/master/demos (mirror: https://github.com/KiCad/kicad-source-mirror)
- **License:** GNU GPL v3 — see `kicad-demos/LICENSE.GPLv3`.
- **Committed as-is:** the complete `video/` and `pic_programmer/` demo projects (`.kicad_pro`,
  `.kicad_sch`, `.kicad_pcb`, symbol/footprint libraries).
- **Derived renders under `video/_generated/` (changes made):** the fabrication outputs (Gerbers
  incl. paste/silkscreen, Excellon drill + drill-map PDF, IPC-D-356 netlist, placement CSV, BOM CSV,
  fabrication/assembly PDFs) and the OpenBoardView BRD2 boardview (`video.brd`) were **generated from
  the committed `video` project** with KiCad 9.0.9 (`kicad-cli`) and `pcbnew`. As outputs of a
  GPL-v3 design they remain under GPL v3; the generating source (`video.kicad_pcb` / `.kicad_sch`) is
  committed alongside them.

## `chromium-ec/` — © The ChromiumOS Authors
- **Source:** https://chromium.googlesource.com/chromiumos/platform/ec
- **License:** BSD 3-Clause — see `chromium-ec/LICENSE`.
- **Contents (committed as-is):** firmware documentation containing state machines:
  `low_battery_startup.md`, `usb-tcpmv2.md`, `usb-c.md`, `usb_power.md`.

## `mnt-reform/` — © MNT Research GmbH
- **Source:** https://source.mnt.re/reform/reform
- **License:** CERN Open Hardware Licence v2 — Strongly Reciprocal (CERN-OHL-S v2) — see
  `mnt-reform/LICENSE` and `mnt-reform/CERN-OHL-S-v2.txt`.
- **Contents (committed as-is):** `reform2-motherboard-r2c.pdf` — the MNT Reform open-hardware laptop
  motherboard schematic (a second open-license real-laptop schematic specimen alongside Framework).

## `nasa/` — U.S. Government work (public domain)
- **Source:** https://nepp.nasa.gov/docuploads/06AA01BA-FC7E-4094-AE829CE371A7B05D/NASA-STD-8739.3.pdf
- **License:** Public domain (work of the U.S. Government, 17 U.S.C. §105).
- **Contents (committed as-is):** `nasa-std-8739.3.pdf` — NASA-STD-8739.3 "Soldered Electrical Connections."
- **Status note:** This standard was **cancelled 2011-10-17** and superseded by IPC J-STD-001 with a
  NASA addendum (NASA-STD-8739.6). Retained as a public-domain rework/workmanship specimen.

---

The scripts that produce every derived render are in [`../tools/`](../tools/) (see
[`../tools/README.md`](../tools/README.md)); this file is maintained by hand alongside them.
