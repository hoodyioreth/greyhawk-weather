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
