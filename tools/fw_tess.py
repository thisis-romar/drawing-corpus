#!/usr/bin/env python3
"""Import the Framework CAD STEP, tessellate each solid (coarse), cache meshes to npz.
Expensive step (OCC import + tessellation) — run once, then render from the cache."""
import os
import cadquery as cq
import numpy as np, time
STP = os.environ.get("FW_STEP", "/tmp/staging/fw-cad/Framework_Laptop_13_CAD.stp")
t0 = time.time()
print("importing STEP ...", flush=True)
shape = cq.importers.importStep(STP).val()
solids = shape.Solids()
print(f"solids={len(solids)} import_t={time.time()-t0:.0f}s", flush=True)

allv, allf, sid, meta = [], [], [], []
voff = 0
for i, s in enumerate(solids):
    try:
        v, t = s.tessellate(1.5, 0.5)
    except Exception:
        continue
    if not v or not t:
        continue
    V = np.array([(p.x, p.y, p.z) for p in v], float)
    T = np.array(t, int) + voff
    allv.append(V); allf.append(T); sid.append(np.full(len(T), i))
    try:
        vol = s.Volume(); c = s.Center(); bb = s.BoundingBox()
        meta.append((i, vol, c.x, c.y, c.z, bb.xmin, bb.ymin, bb.zmin, bb.xmax, bb.ymax, bb.zmax))
    except Exception:
        meta.append((i, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    voff += len(V)
    if i % 50 == 0:
        print(f"  tess {i}/{len(solids)} verts={voff} t={time.time()-t0:.0f}s", flush=True)

V = np.vstack(allv); F = np.vstack(allf); S = np.concatenate(sid); M = np.array(meta, float)
np.savez_compressed("/tmp/fw_mesh.npz", V=V, F=F, S=S, M=M)
print(f"SAVED verts={len(V)} faces={len(F)} solids_meshed={len(meta)} total_t={time.time()-t0:.0f}s", flush=True)
