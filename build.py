#!/usr/bin/env python3
"""Build NWCG GeoOps TAK iconset data packages.

Produces two outputs from the same source:

  NWCG-GeoOps2026-R3.zip
    TAK Mission Package (zip-in-zip) for ATAK, WinTAK, and TAK Aware.
    Icons are organised into subgroup folders inside an inner iconset zip.

  NWCG-GeoOps2026-R3-CloudTAK.zip
    Flat zip for CloudTAK direct import.
    All icons at root, version="1" iconset.xml, no MANIFEST.
"""

import hashlib
import io
import os
import re
import zipfile

ICONSET_DIR = "NWCG"
VERSION = "R3"
INNER_NAME = f"NWCG-GeoOps2026-{VERSION}.zip"

# Output filenames
OUT_TAK   = INNER_NAME
OUT_CLOUD = f"NWCG-GeoOps2026-{VERSION}-CloudTAK.zip"

# Stable Mission Package UID (distinct from the iconset UID inside iconset.xml)
PACKAGE_UID = "8c40fffd-28f7-4166-84c4-a44511563fee"


def collect_icons(iconset_dir):
    """Return sorted list of (zip_path, disk_path) for all PNGs and iconset.xml."""
    entries = []
    for root, dirs, files in os.walk(iconset_dir):
        dirs.sort()
        for fname in sorted(files):
            if fname.endswith(".png") or fname == "iconset.xml":
                disk_path = os.path.join(root, fname)
                zip_path = os.path.relpath(disk_path, iconset_dir).replace("\\", "/")
                entries.append((zip_path, disk_path))
    return entries


def build_tak(entries):
    """Zip-in-zip Mission Package for ATAK / WinTAK / TAK Aware."""
    inner_buf = io.BytesIO()
    with zipfile.ZipFile(inner_buf, "w", zipfile.ZIP_DEFLATED) as inner:
        for zip_path, disk_path in entries:
            inner.write(disk_path, zip_path)
    inner_bytes = inner_buf.getvalue()

    md5 = hashlib.md5(inner_bytes).hexdigest()
    inner_entry = f"{md5}/{INNER_NAME}"

    manifest = f"""<?xml version="1.0" encoding="UTF-8"?>
<MissionPackageManifest version="2">
   <Configuration>
      <Parameter name="uid" value="{PACKAGE_UID}"/>
      <Parameter name="name" value="{INNER_NAME}"/>
      <Parameter name="onReceiveImport" value="true"/>
      <Parameter name="onReceiveDelete" value="true"/>
   </Configuration>
   <Contents>
      <Content ignore="false" zipEntry="{inner_entry}"/>
   </Contents>
</MissionPackageManifest>"""

    with zipfile.ZipFile(OUT_TAK, "w", zipfile.ZIP_DEFLATED) as outer:
        outer.writestr("MANIFEST/manifest.xml", manifest)
        outer.writestr(inner_entry, inner_bytes)

    icon_count = sum(1 for zp, _ in entries if zp.endswith(".png"))
    print(f"TAK (zip-in-zip): {OUT_TAK}  ({icon_count} icons)")


def build_cloudtak(entries):
    """Flat zip for CloudTAK — all icons at root, version=1 iconset.xml, no manifest."""
    # Read source iconset.xml and downgrade to version="1" (CloudTAK native format)
    xml_path = next(dp for zp, dp in entries if zp == "iconset.xml")
    with open(xml_path, "r", encoding="utf-8") as f:
        xml = f.read()
    xml = re.sub(r'version="2"', 'version="1"', xml, count=1)

    with zipfile.ZipFile(OUT_CLOUD, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("iconset.xml", xml)
        for zip_path, disk_path in entries:
            if zip_path == "iconset.xml":
                continue
            # Flatten: strip subgroup folder, write icon at root
            flat_name = zip_path.split("/")[-1]
            zf.write(disk_path, flat_name)

    icon_count = sum(1 for zp, _ in entries if zp.endswith(".png"))
    print(f"CloudTAK (flat):  {OUT_CLOUD}  ({icon_count} icons)")


if __name__ == "__main__":
    entries = collect_icons(ICONSET_DIR)
    build_tak(entries)
    build_cloudtak(entries)
