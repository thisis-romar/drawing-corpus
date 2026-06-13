#!/usr/bin/env python3
"""Convert the committed KiCad PCB to an OpenBoardView BRD2 ASCII boardview (.brd).
My own converter (uses the KiCad pcbnew API); format per OpenBoardView BRD2File parser:
  BRDOUT: <n_outline> <max_x> <max_y> / outline pts / NETS: / PARTS: / PINS: / NAILS:
  side: 1=Top 2=Bottom. Coordinates emitted in micrometres (integer)."""
import sys, pcbnew

PCB = "sources/kicad-demos/video/video.kicad_pcb"
OUT = "sources/kicad-demos/video/_generated/video.brd"

b = pcbnew.LoadBoard(PCB)
um = lambda nm: int(round(nm / 1000.0))  # nm -> micrometre

# --- board outline (fall back to edge bbox rectangle) ---
outline = []
try:
    poly = pcbnew.SHAPE_POLY_SET()
    b.GetBoardPolygonOutlines(poly)
    if poly.OutlineCount() > 0:
        o = poly.Outline(0)
        outline = [(um(o.CPoint(i).x), um(o.CPoint(i).y)) for i in range(o.PointCount())]
except Exception:
    pass
if not outline:
    bb = b.GetBoardEdgesBoundingBox()
    L, T, R, B = um(bb.GetLeft()), um(bb.GetTop()), um(bb.GetRight()), um(bb.GetBottom())
    outline = [(L, T), (R, T), (R, B), (L, B)]

# --- parts, pins, nets ---
nets = {0: "UNCONNECTED"}
parts, pins = [], []
for fp in b.GetFootprints():
    ref = fp.GetReference() or "?"
    side = 2 if fp.IsFlipped() else 1
    pads = list(fp.Pads())
    if not pads:
        continue
    xs, ys = [], []
    for pad in pads:
        pos = pad.GetPosition()
        x, y = um(pos.x), um(pos.y)
        nc = pad.GetNetCode()
        name = (pad.GetNetname() or "UNCONNECTED").replace(" ", "_")
        nets.setdefault(nc, name)
        pins.append((x, y, nc, side))
        xs.append(x); ys.append(y)
    parts.append((ref.replace(" ", "_"), min(xs), min(ys), max(xs), max(ys), len(pins), side))

max_x = max([p[0] for p in pins] + [o[0] for o in outline])
max_y = max([p[1] for p in pins] + [o[1] for o in outline])

with open(OUT, "w") as f:
    f.write(f"BRDOUT: {len(outline)} {max_x} {max_y}\n")
    for x, y in outline:
        f.write(f"{x} {y}\n")
    f.write(f"\nNETS: {len(nets)}\n")
    for nid in sorted(nets):
        f.write(f"{nid} {nets[nid]}\n")
    f.write(f"\nPARTS: {len(parts)}\n")
    for name, x1, y1, x2, y2, end, side in parts:
        f.write(f"{name} {x1} {y1} {x2} {y2} {end} {side}\n")
    f.write(f"\nPINS: {len(pins)}\n")
    for x, y, nid, side in pins:
        f.write(f"{x} {y} {nid} {side}\n")
    f.write("\nNAILS: 0\n")

print(f"wrote {OUT}: outline={len(outline)} nets={len(nets)} parts={len(parts)} pins={len(pins)}")
