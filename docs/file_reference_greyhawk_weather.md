# GREYHAWK_WEATHER_FILE_REFERENCE.md

Master index of Python scripts and key data files for the Greyhawk Weather Generation project.

---

## 📁 Data Files

| Filename                           | Description                                                        | Status   |
|----------------------------------|------------------------------------------------------------------|----------|
| `calendar_day_map.json`           | Maps 1–364 day-of-year to month, day, weekday, and festival using metadata. | 🟢 Active |
| `calendar_metadata.json`          | Canonical source for month names, day-of-week labels, real-world equivalents, seasons, and numeric order. | 🟢 Active |
| `moon_phases.json`                | Canonical, cycle-based moon phase system for Luna and Celene with offset & phase map. | 🟢 Active |
| `longitudes_with_seasonal_profiles.json` | Enriched regional weather logic for forecast generation.      | 🟢 Active |

---

## 🔍 Python Scripts

| Script                      | Purpose                                                         | Tags                           | Status   |
|-----------------------------|-----------------------------------------------------------------|-------------------------------|----------|
| `calendar_month_view.py`     | ASCII calendar display with moon phase & weather highlights    | `calendar`, `cli`, `visual`    | 🟢 Active |
| `calendar_utils.py`          | Utility to query months, seasons, real month, etc.              | `calendar`, `utils`             | 🟢 Active |
| `generate_daily_weather.py`  | CLI forecast tool with daily & full month views, region-based weather | `weather`, `cli`, `calendar` | 🟢 Active |

---

## 📁 Exports

- All `.txt` and `.md` forecast exports are generated in the `exports/` directory.

---

## 🔄 Session Wrap-Up (Most Recent Files)

| Filename                  | Status   | Notes                                             |
|---------------------------|----------|--------------------------------------------------|
| calendar_month_view.py    | 🟢 Active | v0.3.2 with weather summaries and improved prompts |
| calendar_utils.py         | 🟢 Active | month/season lookup utilities                      |
| generate_daily_weather.py | 🟢 Active | v1.2.2 with calendar month view integration        |
| calendar_day_map.json     | 🟢 Active | Primary day-to-date mapping                         |
| calendar_metadata.json    | 🟢 Active | Master calendar metadata                            |
| moon_phases.json          | 🟢 Active | Canonical moon cycle data                           |
| longitudes_with_seasonal_profiles.json | 🟢 Active | Region weather profiles                      |
