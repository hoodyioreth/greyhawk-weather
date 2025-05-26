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
