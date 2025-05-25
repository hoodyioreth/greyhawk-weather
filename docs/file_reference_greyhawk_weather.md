# GREYHAWK_WEATHER_FILE_REFERENCE.md

Master index of Python scripts and key data files for the Greyhawk Weather Generation project.

---

## 📁 Data Files

| Filename | Description | Status |
|----------|-------------|--------|
| `greyhawk_months.json` | Legacy static month→season mapping. Superseded by `calendar_metadata.json`. | 🟠 Stale |
| `calendar_metadata.json` | Canonical source for month names, day-of-week labels, and real-world equivalents. | 🟢 Active |
| `calendar_day_map.json` | Maps 1–364 day-of-year to month, day, weekday, and festival using metadata. | 🟢 Active |
| `moon_phases.json` | Tracks phases of Luna and Celene. Used in daily forecast logic. | 🟢 Active |

---

## 🐍 Python Scripts

| Script | Purpose | Tags | Status |
|--------|---------|------|--------|
| `generate_daily_weather.py` | CLI forecast tool. Uses calendar metadata and maps to real-world equivalents. | `weather`, `cli`, `calendar`, `export` | 🟢 Active |
| `preview_weather_region.py` | Single-region weather query tool. No longer used in final flow. | `preview`, `cli` | 🟠 Stale |
| `merge_seasonal_profiles.py` | Merges seasonal temperature/weather bias into regions. One-time preprocessing. | `merge`, `seasonal`, `json` | 🟡 One-off |
| `generate_daily_weather_multiday.py` | Early version with hardcoded logic. Superseded by current `generate_daily_weather.py`. | `legacy`, `multiday` | 🔴 Deprecated |

---

## 📁 Exports

- All `.txt` and `.md` forecast exports are generated in the local directory.
- Format uses World Anvil–style Markdown (`[h1]`, `[b]`, `[i]`, etc.)
---

## 🔄 Session Wrap-Up (Most Recent Files)

| Filename                          | Status       | Notes |
|----------------------------------|--------------|-------|
| generate_daily_weather.py        | 🟢 Active     | Current canonical version |
| calendar_day_map.json            | 🟢 Synced     | Derived from metadata |
| calendar_metadata.json           | 🟢 Canonical  | Master calendar config |
| moon_phases.json                 | 🟢 Active     | Used for Luna and Celene |
| longitudes_with_seasonal_profiles.json | 🟢 Active | Regional weather logic |
| GREYHAWK_WEATHER_FILE_REFERENCE.md | 🟢 Updated | You’re reading it |
