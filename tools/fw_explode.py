#!/usr/bin/env python3
"""Render an exploded isometric view from cached meshes (/tmp/fw_mesh.npz).
Explodes solids along the assembly's thin axis (preserving stack order) and
shades faces with a simple lambertian model. Raster PNG (cheap vs. vector HLR)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import time, os

OUT = "sources/framework-laptop-13/_generated/framework-laptop-13-exploded.png"
TRI_BUDGET = 160000
EXPLODE_K = 24.0
t0 = time.time()

d = np.load("/tmp/fw_mesh.npz")
V, F, S, M = d["V"], d["F"], d["S"], d["M"]
print(f"loaded verts={len(V)} faces={len(F)} solids={len(M)}", flush=True)

# overall bbox -> thin axis = smallest extent
lo = M[:, 5:8].min(axis=0); hi = M[:, 8:11].max(axis=0)
ext = hi - lo
axis = int(np.argmin(ext)); mid = (lo[axis] + hi[axis]) / 2.0
print(f"extent xyz={ext.round(1)} explode_axis={'XYZ'[axis]}", flush=True)

# budget: keep largest-volume solids until tri budget reached
vol = {int(r[0]): r[1] for r in M}
order = sorted(vol, key=lambda i: vol[i], reverse=True)
keep, acc = set(), 0
fcount = {i: int((S == i).sum()) for i in order}
for i in order:
    if acc + fcount[i] > TRI_BUDGET and keep:
        break
    keep.add(i); acc += fcount[i]
mask = np.isin(S, list(keep))
F2, S2 = F[mask], S[mask]
print(f"rendering {len(keep)}/{len(M)} solids, faces={len(F2)} (dropped tiny parts)", flush=True)

# explode: shift each solid's vertices along axis by K*(centroid_axis - mid)
cen = {int(r[0]): r[2:5] for r in M}
Vd = V.copy()
shift = np.zeros(len(V))
for i in keep:
    sv = np.unique(F[S == i].ravel())
    shift[sv] = EXPLODE_K * (cen[i][axis] - mid)
Vd[:, axis] = V[:, axis] + shift

# triangle polys + lambertian shading
tris = Vd[F2]                                   # (m,3,3)
n = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
nl = np.linalg.norm(n, axis=1); nl[nl == 0] = 1
n /= nl[:, None]
light = np.array([0.4, 0.5, 0.75]); light /= np.linalg.norm(light)
sh = 0.35 + 0.65 * np.clip(np.abs(n @ light), 0, 1)
# per-solid base hue
us = {s: k for k, s in enumerate(sorted(keep))}
cmap = plt.get_cmap("tab20")
base = np.array([cmap(us[s] % 20)[:3] for s in S2])
col = np.clip(base * sh[:, None], 0, 1)
col = np.concatenate([col, np.full((len(col), 1), 0.9)], axis=1)  # RGBA, slight transparency

fig = plt.figure(figsize=(16, 11), dpi=110)
ax = fig.add_subplot(111, projection="3d")
pc = Poly3DCollection(tris, facecolors=col, edgecolors=(0, 0, 0, 0.12), linewidths=0.05)
ax.add_collection3d(pc)
mn = Vd.min(axis=0); mx = Vd.max(axis=0)
ax.set_xlim(mn[0], mx[0]); ax.set_ylim(mn[1], mx[1]); ax.set_zlim(mn[2], mx[2])
ax.set_box_aspect(mx - mn)
ax.view_init(elev=22, azim=-65)
ax.set_axis_off()
ax.set_title("Framework Laptop 13 — exploded assembly (rendered from open CAD)", fontsize=13)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", pad_inches=0.2)
print(f"WROTE {OUT} ({os.path.getsize(OUT)} B) t={time.time()-t0:.0f}s", flush=True)
