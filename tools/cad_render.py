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

# D03 — true cross-section: cut plane perpendicular to X at mid-width; the planar
# section curves are viewed along +X, giving the lengthwise (depth x thickness)
# cross-section profile of the case wall, ribs and standoffs.
try:
    print("D03 section ...", flush=True)
    xc = (bb.xmin + bb.xmax) / 2.0
    sec = cq.Workplane("YZ", origin=(xc, 0, 0)).add(shape).section()
    exporters.export(sec, f"{OUT}/framework-laptop-13-section.svg", exportType="SVG",
                     opt={"width": 1200, "height": 500, "strokeWidth": 0.3,
                          "showAxes": False, "projectionDir": (1, 0, 0)})
    print(f"  wrote section ({os.path.getsize(f'{OUT}/framework-laptop-13-section.svg')} B)", flush=True)
except Exception:
    print("D03 FAILED:\n" + traceback.format_exc(), flush=True)

# E05 — exploded view is rendered separately: fw_tess.py caches the tessellated
# meshes and fw_explode.py rasterizes the exploded layout. A vector hidden-line
# export of the full 107-solid exploded assembly is prohibitively slow, so the
# exploded view is a shaded raster (PNG) rather than an SVG.

print("done", flush=True)
