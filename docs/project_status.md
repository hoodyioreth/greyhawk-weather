
# 📦 Project Status Block
Generated: 2025-05-25 12:17

---

## 🔹 TOEE-5e / PsychFinders Campaign

### Canon & Setting
- Greyhawk CY 576, using T0–T1–4, Player’s Guide, Greyhawk Rebooted/Expanded, and World Anvil's Verbobonc guide.
- PDFs hosted at: [hoodyioreth.github.io/toee-campaign-resources](https://hoodyioreth.github.io/toee-campaign-resources)
- Canon source hierarchy: PDFs → GitHub → External links

### Outputs
- Full 5e statblocks (2024 rules) for named NPCs, moathouse factions, monsters
- Token pack (photoreal, 144x144 PNGs), printable contact sheet
- Final PDF and DOCX exports

---

## 🔹 Stream Deck Profile Manager

### Modules & Scripts
- `main.py`: CLI menu
- `validate_audio.py`: Checks audio refs, applies tags
- `consolidate_audio.py`: Centralizes audio
- `convert_paths_mac_to_pc.py` and reverse
- `config.py`: Device-aware paths via `machines.json`

### Folder Layout
- `_to_process/`: Inputs
- `_processed/`: Outputs
- `_archived_project_uploads/`: Archived or superseded profiles
- `sounds/`: Consolidated valid assets

### Tagging Rules
- `Validated`: all links work or fuzzy matched
- `Placeholder`: some links patched with fallback
- `Unverified`: unresolved audio links
- `Complete`: all audio lives in `sounds/`

### Restore Flow
- Triggered by `goodmorning`, `restore now`
- Rebuilds session from uploaded archive
- Regenerates: `memory_snapshot.md`, `project_status.md`, `todo_master.md`, `VERIFICATION.md`

---

## 🔹 Greyhawk Series Projects

### 🌤️ Weather System
- Uses lat/lon, season, biome, and climate to generate regional weather
- Daily and multi-day outputs (°C, wind, rain, hazards)
- Tools: `generate_daily_weather.py`, `calendar_day_map.json`, `koppen_palette.json`
- Upcoming GUI: Tabs for Weather, Clocks, Status

### 🧭 Climate & Geography
- Source: Anna Meyer’s Atlas + PDFs
- JSON entries include: lat, lon, terrain, climate, biome
- `longitudes_from_map.json` = central data file
- Export to GeoJSON/CSV supported

### ⚔️ Encounter Tables & Hazards
- Regional wilderness/dungeon encounter logic
- Includes terrain-based lost tracker, encounter distance, and hazard clocks
- UI-ready modular system with reaction rolls and spell concentration manager

### 📁 Greyhawk Weather Data & Scripts

#### 📂 Data Files
| Filename                  | Description                                               | Status       |
|--------------------------|-----------------------------------------------------------|--------------|
| `calendar_metadata.json` | Canonical metadata: month names, weekdays, season tags    | 🟢 Active     |
| `calendar_day_map.json`  | Maps days (1–364) to months/festivals using metadata      | 🟢 Active     |
| `moon_phases.json`       | Tracks Luna and Celene moon phases                        | 🟢 Active     |
| `greyhawk_months.json`   | Legacy static season mapping (replaced)                   | 🟠 Stale      |

#### 🐍 Python Scripts
| Script                          | Purpose                                               | Status       |
|----------------------------------|-------------------------------------------------------|--------------|
| `generate_daily_weather.py`     | Canonical CLI forecast generator                      | 🟢 Active     |
| `merge_seasonal_profiles.py`    | One-time tool to merge seasonal biases into regions   | 🟡 One-off    |
| `preview_weather_region.py`     | Legacy preview CLI for single-region output           | 🟠 Stale      |
| `generate_daily_weather_multiday.py` | Deprecated multiday forecast engine             | 🔴 Deprecated |

#### 📤 Export Notes
- Forecast outputs generated as `.txt` or `.md`
- World Anvil–style markdown syntax used (`[h1]`, `[b]`, etc.)

---

## 🔹 Assistant Behavior & Commands

### Session Workflow
- Detects platform (macOS/Windows)
- Archive sync: validates `.py`, generates project markdowns
- Commands: `goodmorning`, `goodnight`, `restore now`, `pause`, `resume`, `topicshift`, `?model`

---

# Greyhawk Weather — Project Status

## Current Version
- CLI tool version: `generate_daily_weather.py` v1.2.2
- Calendar month view: `calendar_month_view.py` v0.3.2
- Stable main branch tagged as `v1.2.2-stable` on GitHub

## Recent Progress
- Integrated full calendar month ASCII view with region-aware weather summaries
- Added region prompt fixes and modular calendar utilities
- Created `GIT_WORKFLOW.md` documenting branch-based workflow
- .gitignore finalized and project README updated with Git workflow details

## Next Major Features
- Detailed daily weather stages (dawn, noon, dusk, midnight)
- Weather persistence across days
- Geographic influence between nearby towns

## Current Focus
- Prepare feature branches for safe development (e.g., `feature/daily-stages`)
- Plan export functionality for TXT and MD formats
- Begin unit tests and CI setup for project reliability

---

*Status last updated: [Insert date here]*


