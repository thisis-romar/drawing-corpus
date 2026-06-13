#!/usr/bin/env python3
"""Render ASME Y14.3-style views from the Framework Laptop 13 CAD .stp (CC BY 4.0)
using cadquery/OpenCASCADE. Outputs vector SVG drawings. Each view is independent
so partial success is captured."""
import cadquery as cq
from cadquery import exporters
import traceback, os

STP = os.environ.get("FW_STEP", "/tmp/staging/fw-cad/Framework_Laptop_13_CAD.stp")
OUT = "sources/framework-laptop-13/_generated"
os.makedirs(OUT, exist_ok=True)

print("importing STEP ...", flush=True)
res = cq.importers.importStep(STP)
shape = res.val()
solids = shape.Solids()
bb = shape.BoundingBox()
print(f"imported: solids={len(solids)} bbox mm "
      f"x[{bb.xmin:.1f},{bb.xmax:.1f}] y[{bb.ymin:.1f},{bb.ymax:.1f}] z[{bb.zmin:.1f},{bb.zmax:.1f}]", flush=True)

def svg(obj, path, projdir, extra=None):
    opt = {"width": 1400, "height": 1000, "marginLeft": 12, "marginTop": 12,
           "showAxes": False, "projectionDir": projdir, "strokeWidth": 0.2,
           "strokeColor": (0, 0, 0), "hiddenColor": (160, 160, 160), "showHidden": False}
    if extra: opt.update(extra)
    exporters.export(obj, path, exportType="SVG", opt=opt)
    print(f"  wrote {path} ({os.path.getsize(path)} B)", flush=True)

# E04 — isometric pictorial
try:
    print("E04 isometric ...", flush=True)
    svg(res, f"{OUT}/framework-laptop-13-isometric.svg", (1, -1, 1))
except Exception:
    print("E04 FAILED:\n" + traceback.format_exc(), flush=True)

# D03 — section / cross-section at mid-height (cut away top half, view isometric of cut)
try:
    print("D03 section ...", flush=True)
    zmid = (bb.zmin + bb.zmax) / 2.0
    cutter = cq.Solid.makeBox(bb.xlen + 20, bb.ylen + 20, (bb.zmax - zmid) + 20,
                              pnt=cq.Vector(bb.xmin - 10, bb.ymin - 10, zmid))
    cut = cq.Workplane(obj=shape).cut(cq.Workplane(obj=cutter))
    svg(cut, f"{OUT}/framework-laptop-13-section.svg", (1, -1, 0.6))
except Exception:
    print("D03 FAILED:\n" + traceback.format_exc(), flush=True)

# E05 — approximate exploded (separate solids along Z by centroid order)
try:
    print(f"E05 exploded (solids={len(solids)}) ...", flush=True)
    if len(solids) < 2:
        print("  only one solid in STEP; true explode infeasible -> skip", flush=True)
    else:
        order = sorted(range(len(solids)), key=lambda i: solids[i].Center().z)
        step = max(bb.zlen, 1.0) * 1.2
        parts = []
        for rank, idx in enumerate(order):
            parts.append(solids[idx].translate(cq.Vector(0, 0, rank * step)))
        comp = cq.Compound.makeCompound(parts)
        svg(cq.Workplane(obj=comp), f"{OUT}/framework-laptop-13-exploded.svg", (1, -1, 1))
except Exception:
    print("E05 FAILED:\n" + traceback.format_exc(), flush=True)

print("done", flush=True)
