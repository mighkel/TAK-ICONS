# Contributing to the NWCG GeoOps TAK Iconset

Thanks for helping keep this iconset current. Contributions can be as simple as opening an issue to flag a problem, or as involved as submitting corrected icon files.

---

## Reporting Issues

Open a GitHub issue for any of the following:

- **Missing icons** — something in NWCG PMS 936 that isn't in the set
- **Color or design errors** — symbol doesn't match the official NWCG standard
- **Grouping or naming issues** — hard to find in ATAK, or name doesn't match field usage
- **Compatibility problems** — broken display on a specific ATAK or WinTAK version

Please include your ATAK/WinTAK version and a screenshot if it helps illustrate the problem.

---

## Submitting Updates

1. Test in ATAK and WinTAK if you have access to both
2. Match the official NWCG PMS 936 name where one exists
3. Keep PNG format and match the resolution of existing icons
4. No white background fill — icons must have transparent backgrounds
5. If a symbol could be ambiguous for color-challenged users, add a text label (see Structure Triage icons as examples)
6. Update `NWCG/iconset.xml` — every icon file needs a corresponding entry, and the `name` attribute must match the filename exactly (case-sensitive)
7. Document your changes in [CHANGELOG.md](CHANGELOG.md)

---

## Icon Groups

Groups are organized by operational use, not strict PMS 936 category order:

| Group | Purpose |
|---|---|
| Air Operations | All aviation-related points |
| General | Field operations, fire behavior, hazards, assignment breaks, reference points |
| Logistics | Facilities, infrastructure, communications |
| Structure Triage | Structure status symbols (2024 NWCG addendum) |
| Water | Water sources and supply points |
| Point Repair Status | Road/resource repair workflow status (2024 NWCG addendum) |
| Numbered DP-LZ | Numbered Drop Points and Heli Spots 01–50 |

---

## Non-Standard Icons

This iconset includes a small number of icons not in the official NWCG PMS 936 list that have proven operationally useful (e.g., Fire Location, Water Source). Additions in this category are acceptable but should be clearly noted in the PR description and changelog entry.

---

## Standards Reference

- [NWCG PMS 936 — Point Feature Symbology](https://www.nwcg.gov/publications/pms936/symbology/pms-936-point-feature-symbology)
- [2026 NIFS Symbology Poster](https://storymaps.arcgis.com/stories/dbaa887b2b8a4e0b8e6aff4986e7f649)
- [2024 Addendum](https://www.nwcg.gov/publications/pms936) — Structure Triage and Point Repair Status symbols
