# GREYHAWK_WEATHER_TODO.md

## Objective
Create a seasonal-aware weather generation system for the World of Greyhawk using canonical geography and climate data.

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
