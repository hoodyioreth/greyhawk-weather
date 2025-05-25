# 🧠 memory_snapshot.md  
Generated: 2025-05-25 12:08

---

## 🔹 TOEE-5e / PsychFinders Campaign

### 🧭 Campaign Setting & Canon
- Set in CY 576, World of Greyhawk
- Canon Sources:
  - T0–T1-4 modules
  - Greyhawk Rebooted / Expanded / Player’s Guide
  - Verbobonc Campaign Guide (576 CY)
  - hoodyioreth.github.io/toee-campaign-resources/

### 📚 Source Hierarchy & Tagging
- Primary: PDFs in local folders
- Secondary: GitHub resources
- Tertiary: external links or videos
- Tagging system: TOEE, Greyhawk, Both, Other
- Supports fractional source rankings and tied ranks

### 📘 Statblock Goals
- Fully converted 5e statblocks (2024 edition) for:
  - Named NPCs, monsters, factions, wilderness threats
- Output: DOCX, PDF, statblock index, token folder, contact sheet

### 🎨 Token Guidelines
- PNG format, transparent background, 144x144px
- Based on real player photos (for PCs)
- Style: class, faction, race, cultural cues
- Final output includes printable scenes and tokens

---

## 🔹 Stream Deck Profile Manager (Python Toolkit)

### 🧰 Toolset Overview
- Modular Python structure:
  - `main.py`, `validate_audio.py`, `consolidate_audio.py`, path converters
- Options:
  1. Validate audio (fuzzy logic, placeholder fallback)
  2. Consolidate audio
  3–4. Convert paths Mac ↔ PC
  5. Extract non-audio references

### 💾 File Behavior
- Input: `_to_process/`
- Output: `_processed/`
- Archive: `_archived_project_uploads/`
- Tagged filenames: `-MAC`, `-PC`, `-Validated`, `-Consolidated`, `DEP81302`, etc.

### 🔁 Restore + Archive Logic
- Commands: `goodmorning`, `restore now`, `goodnight`
- Extracts archive, syncs files, archives old versions
- Generates: `memory_snapshot.md`, `project_status.md`, `todo_master.md`, `VERIFICATION.md`

### 🧪 Future Enhancements
- Tkinter GUI
- Icon resize via ImageMagick (144x144px)
- Machine metadata via `machines.json`
- Tag-based routing & auto-move scripts

---

## 🔹 Greyhawk Series Projects

### 🌤️ Greyhawk Weather System

- Region-based weather forecasts using:
  - Season, terrain, biome, and Köppen classification
- Driven by regional JSON (e.g. `weather_regions_nested.json`)
- Forecast includes temperature (°C), wind, rain, and travel effects
- CLI and planned GUI (Tkinter tabs) with Weather, Clocks, Encounters
- Themed output (emoji + multi-line formatting)

Outputs:
- `weather_forecast.txt`, optionally `weather_forecast.geojson`, `.csv`
- Tied to `distance_matrix.json` for travel modifiers

---

### 🗺️ Greyhawk Climate + Geography

- Canonical climate types derived from:
  - Anna B. Meyer's Greyhawk map
  - Uploaded PDFs (descriptive enrichment)
  - Color-mapped Köppen data (`koppen_palette.json`)
- Master file: `longitudes_from_map.json`
- All locations include:
  - Latitude, Longitude
  - Climate (mapped + narrative)
  - Biome and terrain type
  - Optional: elevation, population, travel time estimates
- Future export: GeoJSON for use in mapping tools

---

### ⚔️ Encounter Tables & Hazard System (Modular)

- Region-specific encounter tables (wilderness, dungeon, road, etc.)
- Supports:
  - Terrain complexity
  - Visibility, time of day
  - Encounter distance rolls
- Integrated hazard clocks: fatigue, starvation, spell exhaustion
- Optional tracker UI includes:
  - Lost tracker (scaled by terrain)
  - Weather hazard triggers
  - Encounter reaction rolls (2d10 CHA-modified)
  - Multi-concentration checks (for spells)
- System synchronized with Turn Dashboard tab groupings:
  - Turn Roller, Clocks, Encounters, Weather, Status

---

## 🔹 Assistant Behavior & Commands

### ⚙️ Permanent Commands
- `goodmorning`, `goodnight`, `restore now`, `pause`, `resume`, `ssave`, `sload`, `rtp`, `?model`, `topicshift`, `permadeath`

### 🧠 Behavior
- OS-aware (macOS, Windows)
- Auto-prompts for archive handling
- Generates markdowns on restore/sync
- GitHub Desktop preferred for commits
- Avoids overwrites via counter-based renaming

---