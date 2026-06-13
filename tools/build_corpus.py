#!/usr/bin/env python3
"""Add retrieval blocks to drawing-corpus.json, build sources/MANIFEST.json,
and regenerate reports/summary-table.md. Links-only policy: only redistributable
artifacts are committed; everything else is recorded as a URL."""
import json, hashlib, datetime, collections, os

ROOT = "/home/user/drawing-corpus"
RETRIEVED_AT = "2026-06-13"

# --- load sha256 table produced earlier ---
SHA = {}
with open("/tmp/sources_sha256.txt") as f:
    for line in f:
        h, p = line.strip().split("  ", 1)
        SHA[p] = h

def sha_of(path):  # path relative to repo root
    return SHA.get(path)

# upstream provenance per source dir
UPSTREAM = {
    "framework-laptop-13": ("https://github.com/FrameworkComputer/Framework-Laptop-13",
                            "Creative Commons Attribution 4.0 (CC BY 4.0)"),
    "kicad-demos":         ("https://gitlab.com/kicad/kicad/-/tree/master/demos (mirror: github.com/KiCad/kicad-source-mirror)",
                            "GNU GPL v3"),
    "chromium-ec":         ("https://chromium.googlesource.com/chromiumos/platform/ec/+/refs/heads/main/docs/",
                            "BSD 3-Clause"),
    "mnt-reform":          ("https://source.mnt.re/reform/reform",
                            "CERN-OHL-S v2"),
    "nasa":                ("https://nepp.nasa.gov/docuploads/06AA01BA-FC7E-4094-AE829CE371A7B05D/NASA-STD-8739.3.pdf",
                            "Public domain (US Government work)"),
}

# data artifacts only (exclude the meta files we generate: MANIFEST/ATTRIBUTION/fetch script)
DATA = {p: h for p, h in SHA.items() if p.split("/")[1] in UPSTREAM}

FW = "sources/framework-laptop-13"
KV = "sources/kicad-demos/video/video.kicad_pcb"
SCH = FW + "/Mainboard/Mainboard_Interfaces_Schematic_Intel_Core_Ultra_Series_1.pdf"
AMD = FW + "/Mainboard/Mainboard_Interfaces_Schematic_AMD_Ryzen_AI_300_Series.pdf"
TWOD = FW + "/Mainboard/2D/fw_main_pcb_generic_2_w_fan.pdf"
CONN = FW + "/Mainboard/Connectors/README.md"
MBREADME = FW + "/Mainboard/README.md"
NASA = "sources/nasa/nasa-std-8739.3.pdf"
ECDOC = "sources/chromium-ec/docs/low_battery_startup.md"
SCAD = FW + "/Mainboard/OpenSCAD/tray.scad"
VSCH = "sources/kicad-demos/video/video.kicad_sch"

KCMD = "kicad-cli pcb export {sub} sources/kicad-demos/video/video.kicad_pcb"
GEN = "sources/kicad-demos/video/_generated"
GERB = GEN + "/gerbers"
BRD = GEN + "/video.brd"
FWGEN = "sources/framework-laptop-13/_generated"
ISO = FWGEN + "/framework-laptop-13-isometric.svg"
SEC = FWGEN + "/framework-laptop-13-section.svg"
EXPL = FWGEN + "/framework-laptop-13-exploded.png"

# id -> (status, [local_paths], note, extra)
# status: committed_file | generated_from_committed | url_only
MAP = {
 "A01": ("committed_file", [SCH], "Six Framework interface schematics committed (11th/12th Gen, 7040, Ryzen AI 300, Chromebook, Intel Core Ultra Series 1); MNT Reform motherboard schematic PDF (CERN-OHL-S) committed as a second open specimen at sources/mnt-reform/.", None),
 "A02": ("committed_file", [VSCH], "Applied IEEE-91-style logic-gate symbols are present in the committed KiCad 'video' schematics. The normative IEEE 91/91a standard is paywalled (url_only).", None),
 "A03": ("committed_file", [KV], "Complete KiCad 'video' multi-layer routed PCB. Opens natively in KiCad PCB editor.", None),
 "A04": ("committed_file", [GEN+"/video-fab.pdf", KV], "Fabrication drawing PDF rendered from the committed KiCad project with KiCad 9.0.9 (Edge.Cuts + F/B fab + user layers). Sierra Circuits IPC-2221 specimen is url_only.", KCMD.format(sub="pdf")),
 "A05": ("committed_file", [GEN+"/video-assembly.pdf", KV, TWOD], "Assembly drawing PDF rendered with KiCad 9.0.9 (F.Fab + silkscreen + Edge.Cuts). Framework 2D placement context PDF also committed.", KCMD.format(sub="pdf")),
 "A06": ("committed_file", [GEN+"/drill/video-drl_map.pdf", GEN+"/drill/video.drl", KV], "Drill map (PDF) + Excellon .drl rendered with KiCad 9.0.9.", KCMD.format(sub="drill")),
 "A07": ("url_only", [], "No real layer-stackup *drawing* is redistributable: IPC-2141/IPC-4101 paywalled; Sierra Circuits specimen is reference/fair-use. The committed KiCad video.kicad_pcb contains a 2-layer stackup definition.", None),
 "A08": ("committed_file", [GERB+"/video-job.gbrjob", KV], "Full RS-274X Gerber set (per-layer, X2) rendered with KiCad 9.0.9 into _generated/gerbers/; the .gbrjob is the index. Render online with Tracespace.", KCMD.format(sub="gerbers")),
 "A09": ("committed_file", [GEN+"/video.d356", KV], "IPC-D-356A bare-board test netlist rendered with KiCad 9.0.9 (317 records: net names, pad coords, access side).", "kicad-cli pcb export ipcd356 sources/kicad-demos/video/video.kicad_pcb"),
 "A10": ("committed_file", [GEN+"/video-pos.csv", KV], "Pick-and-place position file (186 components, mm) rendered with KiCad 9.0.9.", "kicad-cli pcb export pos --format csv --units mm sources/kicad-demos/video/video.kicad_pcb"),
 "A11": ("url_only", [], "ASME Y14.5-2018 paywalled; GD&T Basics feature-control-frame specimen is reference/fair-use. No redistributable GD&T drawing committed.", None),
 "A12": ("committed_file", [TWOD], "Framework Mainboard 2D multi-view mechanical drawing (PDF) committed. Native DXF vector versions are url_only (size).", None),
 "A13": ("committed_file", [GERB+"/video-F_Paste.gtp", GERB+"/video-B_Paste.gbp", KV], "Solder-paste stencil aperture set = F/B paste Gerbers rendered with KiCad 9.0.9. IPC-7525 paywalled; Sierra/Sunstone tutorials url_only.", KCMD.format(sub="gerbers")),
 "A14": ("committed_file", [CONN], "Framework connector pinout documentation + two connector datasheets (ACES 50458, AUSB0534) committed. IPC/WHMA-A-620 paywalled.", None),
 "B01": ("committed_file", [MBREADME], "Framework Mainboard README system block diagram committed; interface block diagram also on schematic sheet 1 (committed PDFs). Intel Platform Design Guide is reference-only (url_only).", None),
 "B02": ("committed_file", [MBREADME], "Framework Mainboard README power tree committed. TI PowerLab notebook reference designs are url_only.", None),
 "B03": ("committed_file", [SCH], "Framework interface schematics show real PCIe/USB/I2C topology. Intel PCIe/USB design guides reference-only (url_only).", None),
 "B04": ("url_only", [], "JEDEC JESD79-5 (DDR5) free with registration but redistribution-restricted; Intel DDR5 routing guide reference-only. Recorded as links.", None),
 "B05": ("url_only", [], "Intel Thermal Mechanical Design Guide is account-gated and reference-only (no redistribution). Recorded as link.", None),
 "B06": ("url_only", [], "FCC OET 'Internal Photos' exhibits are public domain but no single FCC ID was pinned (search entry point); flagged human_review. Recorded as link.", None),
 "B07": ("url_only", [], "Intel Thermal Mechanical Design Guide airflow figure is account-gated/reference-only. Recorded as link.", None),
 "B08": ("committed_file", [AMD], "Framework AMD Ryzen AI 300 interface schematic (functional partitioning) committed. SoC-vendor briefs are redistribution-restricted (url_only).", None),
 "B09": ("url_only", [], "TI signal-flow application note is publicly downloadable but copyright-restricted (no redistribution). Recorded as link.", None),
 "B10": ("url_only", [], "IEEE 315A single-line symbols; limited laptop applicability. Reference/fair-use only, nothing redistributable committed.", None),
 "C01": ("committed_file", [BRD, KV], "OpenBoardView BRD2 ASCII boardview (video.brd) generated from the committed KiCad PCB via a pcbnew script (589 nets / 189 parts / 2118 pins; real board outline). Open in OpenBoardView/FlexBV. No DMCA-risk OEM mirror used.", "python pcb2brd.py (KiCad pcbnew API) -> sources/kicad-demos/video/_generated/video.brd"),
 "C02": ("committed_file", [GERB+"/video-F_Silkscreen.gto", GERB+"/video-B_Silkscreen.gbo", KV], "Silkscreen/legend = F/B silkscreen Gerbers rendered with KiCad 9.0.9.", KCMD.format(sub="gerbers")),
 "C03": ("committed_file", [GEN+"/video.d356", KV], "Test-point/access map derived from the committed IPC-D-356 net-access export (rendered with KiCad 9.0.9).", "kicad-cli pcb export ipcd356 sources/kicad-demos/video/video.kicad_pcb"),
 "C04": ("committed_file", [CONN], "Framework inter-board connection/interconnect documentation committed. IPC-2612 paywalled.", None),
 "D01": ("committed_file", [NASA], "NASA-STD-8739.3 'Soldered Electrical Connections' (84-pp public-domain PDF) committed. NOTE: cancelled 2011-10-17, superseded by IPC J-STD-001 + NASA addendum. IPC-7711/7721 paywalled.", None),
 "D02": ("committed_file", [GEN+"/video-bom.csv", CONN, KV], "BOM CSV (64 grouped lines: refs, value, footprint, qty) rendered with KiCad 9.0.9. Framework connector/part-number tables also committed.", "kicad-cli sch export bom --group-by Value sources/kicad-demos/video/video.kicad_sch"),
 "D03": ("committed_file", [SEC], "Cross-section SVG rendered from the Framework CAD .stp (CC BY 4.0) with cadquery/OpenCASCADE: a true cut-plane profile through the case at mid-width (case wall, ribs, standoffs). The 21 MB .stp itself is url_only.", "cadquery: import STEP, section() at mid-width YZ plane, export SVG"),
 "E01": ("committed_file", [MBREADME], "Framework Mainboard README system block diagram committed as the open-license alternative. Intel NUC Technical Product Specification is redistribution-restricted (url_only).", None),
 "E02": ("url_only", [], "SMBus 3.2 spec is freely downloadable but copyright-restricted (no redistribution); JEDEC LPDDR5 free with registration. Timing diagrams recorded as links.", None),
 "E03": ("committed_file", [ECDOC], "Chromium EC firmware docs with state machines committed: low_battery_startup.md, usb-tcpmv2.md (TCPMv2 state machine), usb-c.md, usb_power.md (BSD-3).", None),
 "E04": ("committed_file", [ISO], "Isometric pictorial SVG rendered from the Framework CAD .stp (CC BY 4.0) with cadquery/OpenCASCADE (projectionDir 1,-1,1). The 21 MB .stp itself is url_only.", "cadquery: import STEP, export isometric SVG"),
 "E05": ("committed_file", [EXPL], "Exploded assembly view rendered from the Framework CAD .stp (CC BY 4.0): 107 solids tessellated with OpenCASCADE, separated along the thin (thickness) axis preserving stack order, lambertian-shaded raster (matplotlib). The 21 MB .stp itself is url_only.", "cadquery tessellate (OCC) + matplotlib exploded raster"),
 "E06": ("committed_file", [SCAD], "Framework OpenSCAD mechanical source (tray.scad) committed as a chassis/enclosure mechanical specimen. Full chassis CAD .stp (21 MB) and Printable Case STLs are url_only.", None),
 "E07": ("committed_file", [TWOD], "Framework Mainboard 2D fabrication-context drawing (PDF) committed; KiCad demo provides the full generated IPC-style fab sheet (project source committed).", None),
}

# --- update drawing-corpus.json ---
with open(f"{ROOT}/drawing-corpus.json") as f:
    corpus = json.load(f)

counts = collections.Counter()
for rec in corpus["records"]:
    rid = rec["id"]
    status, paths, note, extra = MAP[rid]
    counts[status] += 1
    primary_sha = sha_of(paths[0]) if paths else None
    block = {
        "status": status,
        "committed": status != "url_only",
        "local_path": paths if paths else None,
        "sha256": primary_sha,
        "retrieved_at": RETRIEVED_AT,
        "note": note,
    }
    if extra:
        block["generation_command"] = extra
    rec["retrieval"] = block

corpus["retrieval_summary"] = {
    "policy": "links-only",
    "retrieved_at": RETRIEVED_AT,
    "committed_file": counts["committed_file"],
    "generated_from_committed": counts["generated_from_committed"],
    "url_only": counts["url_only"],
    "committed_total": counts["committed_file"] + counts["generated_from_committed"],
    "committed_files_on_disk": len(DATA),
    "note": ("Only redistributable artifacts are committed (CC BY 4.0 Framework, GPL v3 KiCad, "
             "BSD-3 Chromium EC, CERN-OHL-S MNT Reform, public-domain NASA). committed_file covers "
             "both exact upstream files and drawing-type renders generated from the committed open "
             "sources (KiCad 9.0.9 fab outputs + pcbnew boardview, and cadquery/OpenCASCADE CAD "
             "views); each render carries its generation_command and the scripts live in tools/. "
             "url_only = paywalled / reference-only / free-but-copyright-restricted, recorded as "
             "links per the links-only policy. See sources/ATTRIBUTION.md for modification notices."),
}

with open(f"{ROOT}/drawing-corpus.json", "w") as f:
    json.dump(corpus, f, indent=2, ensure_ascii=False)
    f.write("\n")

# --- build sources/MANIFEST.json ---
records_out = []
for rec in corpus["records"]:
    r = rec["retrieval"]
    records_out.append({
        "id": rec["id"],
        "drawing_type": rec["drawing_type"],
        "status": r["status"],
        "license": rec["license"],
        "local_path": r["local_path"],
        "sha256": r["sha256"],
        "source_url": rec["source_url"],
        "note": r["note"],
        **({"generation_command": r["generation_command"]} if "generation_command" in r else {}),
    })

# committed file inventory (all 84 files)
inventory = []
for path in sorted(DATA):
    top = path.split("/")[1]  # sources/<top>/...
    up, lic = UPSTREAM[top]
    inventory.append({"path": path, "sha256": DATA[path], "license": lic, "upstream": up,
                      "bytes": os.path.getsize(os.path.join(ROOT, path))})

manifest = {
    "spec": corpus["spec"],
    "generated": RETRIEVED_AT,
    "policy": "links-only: only redistributable artifacts committed; all else url_only",
    "record_count": len(records_out),
    "counts": dict(counts),
    "committed_total": counts["committed_file"] + counts["generated_from_committed"],
    "committed_files_on_disk": len(inventory),
    "committed_bytes_on_disk": sum(i["bytes"] for i in inventory),
    "sources": {
        top: {"upstream": UPSTREAM[top][0], "license": UPSTREAM[top][1]}
        for top in sorted({p.split("/")[1] for p in DATA})
    },
    "records": records_out,
    "committed_file_inventory": inventory,
}
with open(f"{ROOT}/sources/MANIFEST.json", "w") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
    f.write("\n")

# --- regenerate summary-table.md with Retrieved column ---
STAT = {"committed_file": "committed", "generated_from_committed": "committed (gen)", "url_only": "url-only"}
def yn(b): return "YES" if b else "no"
lines = []
lines.append("# EMBLEM-NLP-RSPEC-001 — Summary Table\n")
lines.append(f"*Section 11.1 — one row per drawing type. Generated {RETRIEVED_AT} from `drawing-corpus.json`.*\n")
lines.append("| ID | Drawing Type | Group | Confidence | Tier | License | Retrieved | Human Review | Paywalled |")
lines.append("|----|--------------|-------|-----------|------|---------|-----------|--------------|-----------|")
lic_short = {
 "Creative Commons Attribution 4.0 (CC BY 4.0)": "Creative Commons Attribution 4.0",
 "JEDEC reference (free download with registration; redistribution restricted)": "JEDEC reference",
 "Intel reference use only (no redistribution)": "Intel reference use only",
 "TI reference (publicly downloadable application material)": "TI reference",
 "Intel reference use (publicly downloadable TPS; redistribution restricted)": "Intel reference use",
 "Public (SMBus spec freely downloadable from smbus.org)": "Public",
 "Public domain (FCC equipment-authorization submissions)": "Public domain",
 "Public domain (US Government work)": "Public domain",
 "Fair use / CC (reproduced IEEE 91 symbols)": "Fair use / CC",
 "Fair use / CC (reproduced IEEE 315A symbols)": "Fair use / CC",
 "Reference / fair use (manufacturer educational content)": "Reference / fair use",
 "Reference / fair use (educational, cites ASME Y14.5)": "Reference / fair use",
 "GNU GPL v3 (KiCad) / CC BY 4.0 (Framework)": "GNU GPL v3 (KiCad) / CC BY 4.0 (Framework)",
}
for rec in corpus["records"]:
    lic = lic_short.get(rec["license"], rec["license"])
    lines.append("| {id} | {dt} | {g} | {c} | {t} | {lic} | {ret} | {hr} | {pw} |".format(
        id=rec["id"], dt=rec["drawing_type"], g=rec["group"], c=rec["confidence"].upper(),
        t=rec["source_tier"], lic=lic, ret=STAT[rec["retrieval"]["status"]],
        hr=yn(rec["human_review_required"]), pw=yn(rec["paywalled"])))
ct = counts["committed_file"] + counts["generated_from_committed"]
lines.append("")
lines.append(f"**Totals:** 38 drawing types — 17 high, 17 medium, 4 low confidence. "
             f"7 flagged for human review, 4 paywalled.")
lines.append("")
lines.append(f"**Retrieval (links-only policy):** {ct}/38 have a committed redistributable specimen "
             f"(exact upstream files plus drawing-type renders generated from the committed open "
             f"sources); {counts['url_only']}/38 are url-only "
             f"(paywalled / reference-only / copyright-restricted). "
             f"{len(inventory)} files / {manifest['committed_bytes_on_disk']//1024} KiB committed under `sources/`. "
             f"See `sources/MANIFEST.json`.")
with open(f"{ROOT}/reports/summary-table.md", "w") as f:
    f.write("\n".join(lines) + "\n")

print("counts:", dict(counts), "committed_total:", ct)
print("files on disk:", len(inventory), "bytes:", manifest["committed_bytes_on_disk"])
print("records missing sha (expect url_only=%d):" % counts["url_only"],
      [r["id"] for r in records_out if r["sha256"] is None])
