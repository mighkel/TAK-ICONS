# NWCG GeoOps Wildfire Iconset for TAK

Updated NWCG (National Wildfire Coordinating Group) GeoOps point symbology for ATAK, WinTAK, TAK Aware, and CloudTAK, aligned with the 2025/2026 National Incident Feature Service (NIFS) standards (PMS 936).

This is a community-maintained update to the original GeoOps iconset. If you're still running the 2021 version, this brings it current with the latest NWCG symbology — including Structure Triage, Point Repair Status, UAS, IR points, and several color corrections.

> **Feedback welcome.** If you spot a missing icon, color issue, or grouping problem, please open an issue.

---

## Install

Two packages are available — use the one that matches your platform:

| Package | Platform |
|---|---|
| `NWCG-GeoOps2026-R3.zip` | ATAK, WinTAK, TAK Aware |
| `NWCG-GeoOps2026-R3-CloudTAK.zip` | CloudTAK |

**ATAK / WinTAK / TAK Aware**
1. Download `NWCG-GeoOps2026-R3.zip` from the [Releases](../../releases) page
2. In **ATAK**: Settings → Import Manager → Import → select the file
3. In **WinTAK**: Settings → Import Manager → select the file
4. Icons appear in your palette under **NWCG-GeoOps2026**

**CloudTAK**
1. Download `NWCG-GeoOps2026-R3-CloudTAK.zip` from the [Releases](../../releases) page
2. Go to **Iconsets** → Import → select the file
3. Icons appear under **NWCG-GeoOps2026** as a flat list (CloudTAK does not display subgroups)

---

## What's Included

170 point icons in 7 groups, as they appear in the ATAK icon palette:

| Group | Contents |
|---|---|
| **Air Operations** | Aerial Hazard, Airport/Airstrip, Checkpoint, Heli Base, Heli Spot, Mobile Retardant Base, Sling Site, UAS Launch & Recovery, Unimproved Landing |
| **General** | Fire Origin, Spot Fire, IR points, hazards, assignment breaks (Division/Branch/Zone), repair and field operation symbols, reference points |
| **Logistics** | Camp, ICP, Medical, Drop Point, Staging, Fire Station, Closure, Weather (Wx), Internet Access, Repeater |
| **Structure Triage** | Defensible Prep & Hold, Defensible Stand Alone, Non-Defensible Prep & Leave, Non-Defensible Rescue Drive-By, Unknown — all with text labels |
| **Water** | Dip Site, Draft Site, Hydrant, Restricted Water Source, Water Dev, Water Source |
| **Point Repair Status** | Needs Assessment, Repair Needed, In Progress, Completed–Ready for Inspection, Completed Inspected, In Use Fire Mgt, Other–See Comments |
| **Numbered DP-LZ** | Drop Points 01–50, Heli Spots 01–50 |

See the [Icon Reference Sheet](NWCG_Icon_Reference.html) for a visual overview of every icon.

---

## Version

**R3 — June 2026** | Tested on ATAK 5.6.0.14, WinTAK v5.5.0.158 (CIV), TAK Aware, and CloudTAK

See [CHANGELOG.md](CHANGELOG.md) for what changed from the 2021 version.

---

## Reference

- [NWCG PMS 936 — Point Feature Symbology](https://www.nwcg.gov/publications/pms936/symbology/pms-936-point-feature-symbology)
- [2026 NIFS Symbology Poster](https://storymaps.arcgis.com/stories/dbaa887b2b8a4e0b8e6aff4986e7f649)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report issues or submit updates.

## License

Derived from NWCG public domain symbology. See [LICENSE](LICENSE) for details.
