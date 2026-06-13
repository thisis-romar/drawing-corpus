# Attribution & License Notices — `sources/`

This directory contains the **retrieved example files** for EMBLEM-NLP-RSPEC-001, under the
**links-only policy**: only redistributable artifacts are committed here. Paywalled standards,
vendor reference-only documents, and free-but-copyright-restricted specs are *not* committed — they
are recorded as URLs in [`MANIFEST.json`](./MANIFEST.json) and can be retrieved with
[`fetch_sources.sh`](./fetch_sources.sh).

All committed files are unmodified copies of their upstream originals. Per-record mapping (which
drawing type each file serves) is in `MANIFEST.json` and in `../drawing-corpus.json` (`retrieval`).

---

## `framework-laptop-13/` — © Framework Computer Inc.
- **Source:** https://github.com/FrameworkComputer/Framework-Laptop-13
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0) — see `framework-laptop-13/LICENSE`.
- **Attribution:** "Framework Laptop 13" by Framework Computer Inc., used under CC BY 4.0.
- **Contents:** six `Mainboard_Interfaces_Schematic_*.pdf` interface schematics, the `Mainboard/2D`
  mechanical drawing PDF, two connector datasheets + `Connectors/README.md`, `Mainboard/README.md`,
  `OpenSCAD/tray.scad`, and the repo `README.md`.
- **Not committed (url-only, size):** `Framework Laptop 13 CAD.stp` (21 MB), `… Pro CAD.stp` (52 MB),
  the four `Mainboard/2D/*.dxf` vector files, and the Printable-Case STLs — fetch via `fetch_sources.sh`.

## `kicad-demos/` — © KiCad Developers
- **Source:** https://gitlab.com/kicad/kicad/-/tree/master/demos (mirror: https://github.com/KiCad/kicad-source-mirror)
- **License:** GNU GPL v3 — see `kicad-demos/LICENSE.GPLv3`.
- **Contents:** the complete `video/` and `pic_programmer/` demo projects (`.kicad_pro`, `.kicad_sch`,
  `.kicad_pcb`, symbol/footprint libraries).
- **Note:** Fabrication outputs (Gerber, drill, IPC-D-356 netlist, placement, silkscreen, BOM, fab/
  assembly PDFs) are *generated* from these projects — KiCad is not installed here, so the generation
  command is recorded per record instead of committing fabricated outputs.

## `chromium-ec/` — © The ChromiumOS Authors
- **Source:** https://chromium.googlesource.com/chromiumos/platform/ec
- **License:** BSD 3-Clause — see `chromium-ec/LICENSE`.
- **Contents:** firmware documentation containing state machines: `low_battery_startup.md`,
  `usb-tcpmv2.md`, `usb-c.md`, `usb_power.md`.

## `mnt-reform/` — © MNT Research GmbH
- **Source:** https://source.mnt.re/reform/reform
- **License:** CERN Open Hardware Licence v2 — Strongly Reciprocal (CERN-OHL-S v2) — see
  `mnt-reform/LICENSE` and `mnt-reform/CERN-OHL-S-v2.txt`.
- **Contents:** `reform2-motherboard-r2c.pdf` — the MNT Reform open-hardware laptop motherboard
  schematic (a second open-license real-laptop schematic specimen alongside Framework).

## `nasa/` — U.S. Government work (public domain)
- **Source:** https://nepp.nasa.gov/docuploads/06AA01BA-FC7E-4094-AE829CE371A7B05D/NASA-STD-8739.3.pdf
- **License:** Public domain (work of the U.S. Government, 17 U.S.C. §105).
- **Contents:** `nasa-std-8739.3.pdf` — NASA-STD-8739.3 "Soldered Electrical Connections."
- **Status note:** This standard was **cancelled 2011-10-17** and superseded by IPC J-STD-001 with a
  NASA addendum (NASA-STD-8739.6). Retained as a public-domain rework/workmanship specimen.
