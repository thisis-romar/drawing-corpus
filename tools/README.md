# tools/ — generation scripts for the derived specimens

These are the exact scripts used to produce the *derived* artifacts under
`sources/**/_generated/`. They make the corpus reproducible: every record in
[`../drawing-corpus.json`](../drawing-corpus.json) whose `retrieval.generation_command` names one of
these can be regenerated from the committed open sources. Run all commands from the repository root.

## Prerequisites

| Script | Needs | Install used (Ubuntu 24.04) |
|--------|-------|------------------------------|
| [`pcb2brd.py`](pcb2brd.py) | KiCad 9 `pcbnew` Python API | `kicad` from `ppa:kicad/kicad-9.0-releases` |
| [`cad_render.py`](cad_render.py), [`fw_tess.py`](fw_tess.py), [`fw_explode.py`](fw_explode.py) | cadquery / OpenCASCADE (+ numpy, matplotlib) | `python3 -m venv venv && venv/bin/pip install cadquery matplotlib` |
| [`build_corpus.py`](build_corpus.py) | python3 stdlib only | — |

The KiCad fab outputs (`sources/kicad-demos/video/_generated/gerbers|drill`,
`video.d356`, `video-pos.csv`, `video-bom.csv`, `video-*.pdf`) are produced directly
by `kicad-cli` — the exact commands are stored in each record's `generation_command`
and summarized in the repo `README.md`.

## Regenerate

```sh
# C01 — OpenBoardView BRD2 boardview from the committed KiCad PCB
python3 tools/pcb2brd.py                     # -> sources/kicad-demos/video/_generated/video.brd

# E04 isometric + D03 section (SVG) from the Framework CAD .stp.
# The 21 MB .stp is url_only (not committed) — fetch it first, then point FW_STEP at it:
#   (see the A14/E04 entries in sources/MANIFEST.json for the URL, or sources/fetch_sources.sh)
export FW_STEP=/path/to/Framework_Laptop_13_CAD.stp
venv/bin/python tools/cad_render.py          # -> .../_generated/framework-laptop-13-{isometric,section}.svg

# E05 exploded (PNG): tessellate once (cache), then render
venv/bin/python tools/fw_tess.py             # -> /tmp/fw_mesh.npz   (set $FW_STEP as above)
venv/bin/python tools/fw_explode.py          # -> .../_generated/framework-laptop-13-exploded.png

# Rebuild drawing-corpus.json + sources/MANIFEST.json + reports/summary-table.md
find sources -type f -print0 | sort -z | xargs -0 sha256sum > /tmp/sources_sha256.txt
python3 tools/build_corpus.py
```

[`build_corpus.py`](build_corpus.py) holds the master record→retrieval mapping (license, upstream,
local paths, generation commands) and is the single source of truth that emits
[`../drawing-corpus.json`](../drawing-corpus.json), [`../sources/MANIFEST.json`](../sources/MANIFEST.json),
and [`../reports/summary-table.md`](../reports/summary-table.md); edit it there, never the generated
files. It reads `/tmp/sources_sha256.txt` (the `find … | sha256sum` line above) for the checksums.

Notes: `cad_render.py`/`fw_tess.py` read the STEP path from `$FW_STEP`. The Framework
CAD `.stp` and other url-only sources are intentionally not committed (license/size);
nothing here downloads or bypasses a paywall.
