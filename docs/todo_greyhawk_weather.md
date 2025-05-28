
---

## ✅ Current Focus: Step 2 – Merge Seasonal Profiles

### Purpose
Enrich `longitudes_from_map.json` by adding:
- `seasonal_temperature_profile` — e.g., {"Fireseek": "cold", "Planting": "mild", ...}
- `seasonal_weather_bias` — e.g., {"Fireseek": "snow", "Planting": "thunderstorm", ...}

### Steps
1. Load both JSONs:
- `longitudes_from_map.json`
- `greyhawk_months.json`
2. Build a `month_to_season` mapping from `greyhawk_months.json`
3. Define mapping logic:
- `(climate_koppen, season)` → qualitative temperature
- `(climate_koppen, season)` → dominant weather type
4. Iterate over each region in `longitudes_from_map.json`
- Assign temperature and weather bias for each month
- Add to region JSON structure
5. Output to: `longitudes_with_seasonal_profiles.json`

---

## 🧭 Next Steps After This
### Step 1 – CLI Weather Generator
- Accepts region + month input
- Returns daily weather based on enriched seasonal data

### Step 3 – Encounter & Travel Tags
- Add `biome`, `encounter_risks`, `travel_difficulty_modifiers`
- Supports hazard and monster encounter generation

---

## Notes
- Climate logic derived from Köppen codes + seasonal expectations
- Regions without `climate_koppen` or season fallback will default to "temperate/mild"
- Will integrate with travel system and Turn Dashboard in future phases
---

## ✅ Today’s Completed Tasks

- Reverted to a stable, working version of `generate_daily_weather.py`
- Confirmed multi-day terminal output working correctly
- Fixed calendar sync from `calendar_metadata.json`
- Moon phase logic now consistently shows Luna (and Celene when relevant)
- Export logic corrected and terminal display confirmed

## 💤 Ready for Tomorrow

- [ ] Consider restoring `preview_weather_region.py` as a lookup tool
- [ ] Add error fallback for Ctrl+Z or no region selected
- [ ] Re-enable optional export to campaign timeline

---

## 🌦 Greyhawk Weather + Climate System

### Forecast Engine
- [ ] Finalize CLI tool: `generate_daily_weather.py`
- [ ] Add forecast formatting (emoji + newline-safe)
- [ ] Support multi-day exports with overrideable day length

### Climate Mapping
- [ ] Complete lat/lon enrich for all regions in `longitudes_from_map.json`
- [ ] Assign Köppen classes via color map + override narrative data
- [ ] Export GeoJSON version for map tools

### Encounter Tables & Hazards
- [ ] Finalize terrain-based encounter table selector
- [ ] Implement hazard clocks UI (Lost, Exhaustion, Reaction)
- [ ] Integrate spell concentration tracker per turn roll

---
# Greyhawk Weather — TODO List

## Completed

- [x] Merge `greyhawk_months.json` into `calendar_metadata.json`
- [x] Add canonical moon phase modeling for Luna and Celene
- [x] Replace hardcoded months with `calendar_utils.py` lookups
- [x] Integrate calendar month view into CLI with region-aware weather summaries
- [x] Fix region prompt in calendar month view
- [x] Create `GIT_WORKFLOW.md` for simple branching workflow
- [x] Finalize `.gitignore` for Python/macOS/project files

## Upcoming

- [ ] Add export to `.txt` or `.md`
- [ ] Highlight festival days or warnings in calendar and forecasts
- [ ] Add unit tests for moon cycle wraparound logic
- [ ] Add moonrise/moonset or visibility flags for moons
- [ ] Refactor seasonal profiles to pull season names from `calendar_metadata.json`
- [ ] Build shared utilities for month, season, and real-world date resolution
- [ ] Restore and improve forecast export headers with campaign metadata

## Advanced Features (Long-Term)

- [ ] Implement detailed daily weather stages (dawn, noon, dusk, midnight)
- [ ] Add weather persistence to simulate multi-day weather systems
- [ ] Model geographic influence of weather between nearby towns using lat/lon and climate data
- [ ] Setup GitHub Actions CI workflows for automated tests



---

*Last updated: [Insert date here]*
