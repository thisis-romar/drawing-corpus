#!/usr/bin/env bash
# fetch_sources.sh — OPTIONAL personal-use helper.
#
# The corpus follows a links-only policy: redistributable files live in this repo; everything else
# is recorded as a URL in MANIFEST.json. This script downloads those url-only items (and the large
# open-licensed Framework binaries that were kept out of git for size) into a LOCAL, gitignored
# cache for your own use. Nothing it downloads is committed or redistributed.
#
# Usage:   bash sources/fetch_sources.sh            # fetch everything reachable
#          bash sources/fetch_sources.sh A01 B04     # fetch specific record IDs
#
# Note: paywalled standards (IEEE/IPC/ASME) and account-gated vendor docs (Intel EDC) cannot be
# fetched anonymously and will report SKIPPED — obtain those manually through their licensed portals.

set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE="$HERE/_fetch_cache"
MANIFEST="$HERE/MANIFEST.json"
mkdir -p "$CACHE"

dl() { # url destfile
  local url="$1" dest="$2"
  [ -s "$dest" ] && { echo "  cached: $dest"; return 0; }
  echo "  GET $url"
  if curl -fSL --retry 2 --max-time 180 -o "$dest.part" "$url" 2>/dev/null; then
    mv "$dest.part" "$dest"; echo "  saved: $dest"
  else
    rm -f "$dest.part"; echo "  SKIPPED (paywall/account/unreachable): $url"
  fi
}

# url-only records straight from the manifest
WANT="${*:-}"
python3 - "$MANIFEST" "$WANT" <<'PY' | while IFS=$'\t' read -r id url; do
import json, sys
m = json.load(open(sys.argv[1]))
want = set(sys.argv[2].split()) if len(sys.argv) > 2 and sys.argv[2] else None
for r in m["records"]:
    if r["status"] != "url_only":
        continue
    if want and r["id"] not in want:
        continue
    print(f'{r["id"]}\t{r["source_url"]}')
PY
  echo "[$id] url-only"
  dl "$url" "$CACHE/$id/$(basename "${url%%\?*}" | tr -c 'A-Za-z0-9._-' '_')"
done

# large open-licensed Framework binaries (CC BY 4.0) kept url-only for repo size
if [ -z "$WANT" ] || echo "$WANT" | grep -qiE 'framework|cad|dxf'; then
  echo "[framework] large open binaries (CC BY 4.0)"
  FWRAW="https://raw.githubusercontent.com/FrameworkComputer/Framework-Laptop-13/main"
  mkdir -p "$CACHE/framework-large"
  dl "$FWRAW/Framework%20Laptop%2013%20CAD.stp"      "$CACHE/framework-large/Framework_Laptop_13_CAD.stp"
  dl "$FWRAW/Framework%20Laptop%2013%20Pro%20CAD.stp" "$CACHE/framework-large/Framework_Laptop_13_Pro_CAD.stp"
  for n in 1 2 3 4; do
    dl "$FWRAW/Mainboard/2D/fw_main_pcb_generic_2_w_fan_${n}.dxf" "$CACHE/framework-large/fw_main_pcb_generic_2_w_fan_${n}.dxf"
  done
fi

echo "Done. Cache: $CACHE (gitignored)."
