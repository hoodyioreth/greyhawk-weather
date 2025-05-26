# GREYHAWK_WEATHER_TODO.md

## Objective
Create a seasonal-aware weather generation system for the World of Greyhawk using canonical geography and climate data.

---

## ✅ Today’s Completed Tasks

- Implemented `moon_phases.json` to match canon:
  - Luna = 28-day cycle, 0 offset
  - Celene = 91-day cycle, 43-day offset
  - Both use phase maps (`new`, `waxing_half`, `full`, `waning_half`)
- Updated `generate_daily_weather.py` to v1.2.2:
  - Integrated calendar month view with region weather summaries
  - Prompted region selection properly in calendar month view
- Confirmed proper loading of `data/` files using `Path(__file__).parent`
- Verified canonical alignment with donjon calendar structure
- Merged `greyhawk_months.json` into `calendar_metadata.json`:
  - Now includes `number` and `season` for each month
  - Marked `greyhawk_months.json` as deprecated in file reference
- Created `calendar_utils.py` with month/season/real-month lookup tools

---

## 🔜 Next Steps

- [ ] 📝 Add export to `.txt` or `.md`
- [ ] 📆 Highlight festival days or warnings in output
- [ ] 🧪 Add test suite for moon cycle wraparound
- [ ] 🌗 Add moonrise/moonset or visibility flags (night toggle)
- [ ] Refactor seasonal profiles to pull season names from `calendar_metadata.json`
- [ ] Build shared `calendar_utils.py` to handle month lookups, season resolution, and real-world equivalents
- [ ] Restore export logic to include forecast headers + campaign timestamp metadata

---

## 💤 Future Ideas

- Export forecasts to World Anvil timelines via `.md`
- Highlight festivals visually (Needfest, Richfest, etc)
- GUI panel: checkbox to filter only 'visible' moons or flag 'omens'

---

## ✅ Foundation in Place

- Canonical JSON structure confirmed
- Moon cycle model accurate to Greyhawk standards
- CLI runner stable from any path
- Seasonal temperature and weather profiles load dynamically
- Ready to integrate into Turn Dashboard or export pipeline
