# AG-01 Connector / Interconnect Map producer (EMBLEM-NLP-RSPEC-002)
# Source evidence: page-19 (Mainboard connector placement) + page-17 (per-connector disconnect close-ups)
# Output: illustrative, UNCALIBRATED vector connector-location map + interconnect table.
import csv, html

# connector: (label, conn_x, conn_y, label_x, label_y, anchor, destination_FRU, source_page)
C = [
    ("FAN",        500,150, 500, 55,  "middle", "Cooling fans (dual)",        "p19/p17"),
    ("FFC_USB",    815,190, 950,150,  "end",    "USB / IO daughter (FFC)",    "p19"),
    ("LAN_IO_FPC", 840,250, 950,250,  "end",    "IO board (LAN/audio/SD) FPC","p19/p17"),
    ("EDP CABLE",  840,300, 950,300,  "end",    "OLED panel (eDP)",           "p19/p17"),
    ("SPEAKER",    815,352, 950,350,  "end",    "Speaker set",                "p19/p17"),
    ("CMOS CABLE", 185,290, 50, 290,  "start",  "RTC / CMOS battery",         "p19/p17"),
    ("BL FPC",     380,400, 330,525,  "middle", "Keyboard backlight",         "p19/p17"),
    ("LED FFC",    445,410, 445,525,  "middle", "Status LED board",           "p19/p17"),
    ("K/B FPC",    515,412, 560,525,  "middle", "Keyboard matrix",            "p19/p17"),
    ("BATTERY",    600,405, 670,525,  "middle", "Battery pack",               "p19/p17"),
    ("TP FFC",     660,398, 790,525,  "middle", "Touchpad module",            "p19/p17"),
]

W,H = 1000, 600
def esc(s): return html.escape(s)

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif">')
svg.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')
# title block
svg.append('<text x="500" y="30" text-anchor="middle" font-size="22" font-weight="bold">ASUS ProArt H7604J Mainboard - Connector / Interconnect Map</text>')
svg.append('<text x="500" y="48" text-anchor="middle" font-size="12" fill="#444">AG-01 - EMBLEM-NLP-RSPEC-002 - produces C04 (interconnect) / A14 (harness)</text>')
# board outline - stylized bat-wing shape echoing page-19
board = "M 150,360 L 150,250 Q 150,235 168,232 L 330,210 Q 360,150 400,150 L 600,150 Q 640,150 670,210 L 832,232 Q 850,235 850,250 L 850,360 Q 850,378 832,378 L 700,378 L 700,430 Q 700,445 685,445 L 315,445 Q 300,445 300,430 L 300,378 L 168,378 Q 150,378 150,360 Z"
svg.append(f'<path d="{board}" fill="#0b6b2e" fill-opacity="0.10" stroke="#0b6b2e" stroke-width="2.5"/>')
# CPU/GPU + fan zone hint (mylar/liquid-metal hazard area)
svg.append('<rect x="430" y="175" width="140" height="95" rx="6" fill="#d9534f" fill-opacity="0.10" stroke="#d9534f" stroke-dasharray="5 4" stroke-width="1.5"/>')
svg.append('<text x="500" y="225" text-anchor="middle" font-size="11" fill="#b52b27">CPU/GPU zone</text>')
svg.append('<text x="500" y="240" text-anchor="middle" font-size="9" fill="#b52b27">liquid-metal TIM (page-09)</text>')
# standoff hole lower-right (as on page-19)
svg.append('<circle cx="770" cy="410" r="22" fill="#ffffff" stroke="#0b6b2e" stroke-width="2"/>')

for (label,cx,cy,lx,ly,anchor,dest,src) in C:
    # leader line
    svg.append(f'<line x1="{cx}" y1="{cy}" x2="{lx}" y2="{ly}" stroke="#c0392b" stroke-width="1.4"/>')
    # connector marker (yellow box like the manual highlight)
    svg.append(f'<rect x="{cx-11}" y="{cy-8}" width="22" height="16" rx="2" fill="#f1c40f" stroke="#7a5c00" stroke-width="1.2"/>')
    # label
    svg.append(f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" font-size="13" font-weight="bold" fill="#111">{esc(label)}</text>')

# legend / provenance / disclaimer
svg.append('<g font-size="11" fill="#333">')
svg.append('<rect x="30" y="548" width="940" height="44" fill="#f7f7f7" stroke="#ccc"/>')
svg.append('<rect x="40" y="560" width="16" height="12" fill="#f1c40f" stroke="#7a5c00"/>')
svg.append('<text x="62" y="570">connector (yellow = board-side header)</text>')
svg.append('<text x="300" y="570" font-weight="bold" fill="#b52b27">NOT TO SCALE - illustrative; positions approximate page-19/page-17.</text>')
svg.append('<text x="40" y="586">Evidence: input-set.json pages 19,17,15,23 | No pin-level nets inferred (RSPEC-002 guardrail). Generated for EMBLEM-NLP-RSPEC-002.</text>')
svg.append('</g>')
svg.append('</svg>')

open("re-h7604/outputs/AG-01_connector-map.svg","w").write("\n".join(svg))

# interconnect table CSV
with open("re-h7604/outputs/AG-01_interconnect-table.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["connector_silkscreen","destination_FRU","evidence_page","note"])
    for (label,cx,cy,lx,ly,anchor,dest,src) in C:
        w.writerow([label, dest, src, "board-side header, location per page-19 map"])
print("wrote AG-01_connector-map.svg and AG-01_interconnect-table.csv with", len(C), "connectors")
