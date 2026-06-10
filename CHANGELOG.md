# Changelog

## R3 — June 2026

### Compatibility

- **TAK Aware / TAK Server**: repackaged as a TAK Mission Package (zip-in-zip format) — use `NWCG-GeoOps2026-R3.zip`
- **CloudTAK**: added a separate flat-zip build target — use `NWCG-GeoOps2026-R3-CloudTAK.zip`

### Fixes

- Fixed Numbered DP-LZ icon entries in `iconset.xml` missing `.png` file extension, which caused those icons to display as generic `a-u-G` points in strict TAK clients

---

## R2 — March 2026

Aligned with NWCG PMS 936 (2025) and the 2026 NIFS symbology standards.

### New Icons

**Accountable Property**
- Other Property
- Pump
- Water Tank

**Air Operations**
- UAS Launch & Recovery

**Water**
- Draft Site
- Hydrant

**Structure Triage** *(2024 NWCG addendum)*
- Defensible Prep & Hold
- Defensible Stand Alone
- Non-Defensible Prep & Leave
- Non-Defensible Rescue Drive-By
- Unknown Structure Triage
- *(All five include text labels for accessibility)*

**Point Repair Status** *(2024 NWCG addendum)*
- Needs Assessment
- Repair Needed
- In Progress
- Completed — Ready for Inspection
- Completed Inspected
- In Use Fire Management
- Other — See Comments

**IR Points**
- IR Isolated Heat Source
- Possible IR Heat Source

### Corrections

- **Hazard** and **Hazard Tree**: removed incorrect white background fill
- **Aerial Hazard**: updated to yellow infill with red dot, consistent with other hazard symbols

### Organizational Changes

- Improved group structure for faster icon selection in the ATAK palette
- Air Operations separated as its own group
- Structure Triage and Point Repair Status added as distinct groups
- General group reorganized; reduced from a sprawling catch-all to a more focused set

---

## R1 — 2021

Initial NWCG GeoOps iconset for ATAK. Based on NWCG PMS 936 symbology available at time of release. Credit to the original GeoOps iconset creator.
