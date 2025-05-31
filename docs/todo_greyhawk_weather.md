# ✅ TODO – Greyhawk Weather Generator Project  
_Last updated: 2025-05-28_

## 🔁 Completed Tasks (Do Not Delete – Archive Below)
These items are DONE and preserved here for reference:

- ✅ Color frequency scan of climate map image (top 20 RGBs)
- ✅ Build `koppen_palette.json` from uploaded legend
- ✅ Reduce `oerth_climate_map.png` to use only palette colors
- ✅ Implement color-matching in `enrich_climate.py` v2
- ✅ Create CLI `run_climate_pipeline_mac.sh` with clean-up option
- ✅ Create Windows `.bat` version of pipeline runner
- ✅ Auto-patch `longitudes_from_map.json` with climate classes
- ✅ Replace previous climate output; treat `longitudes_from_map.json` as authoritative
- ✅ Rebuild `weather_regions_greyhawk_pipeline_AUTO_FILLED_CORRECTED.json` with valid structure
- ✅ Validate that all fields are filled and none are missing across JSON
- ✅ Confirm Oerth map climate image resolution and lat/lon scaling
- ✅ Regenerate TOC & Reference Lists (PROJECT_STATUS, TODO, FILE_REFERENCE)

---

## 🧭 Navigation & Metadata

### 🔂 Project Structure & Workflow
- [ ] Build or regenerate `README.md` explaining:
  - Folder structure (`canonical`, `post_576CY`, etc.)
  - Upload and sync order (e.g., load PDFs, then update `weather_regions.json`)
  - Which files are canonical, which are drafts
- [ ] Suggest tags for clarity in README (e.g., ✓ canon, ⚠ draft, 🕸 legacy)

### 🧱 File & Data Structure
- [ ] Clean and reissue `weather_regions_greyhawk.json` with:
  - Full region hierarchy from Classic Guide, Oerik Players Guide, Anna B. Meyer map
  - Updated `proximity`, `travel_time_to`, `climate_koppen`, and `biome_notes`
  - All lat/lon validated via `longitudes_from_map.json`

---

## 🌐 GeoJSON & Coordinate Tools

### Coordinates & Map Integration
- [ ] Finish tool: `build_greyhawk_pipeline.py`
  - Automates lat/lon patching, validation, matrix generation
  - Optionally exports `.geojson`, `.csv`
- [ ] Implement GUI/CLI clickable map interface:
  - Drop pins and record lat/lon
  - Zoom/pan support
- [ ] Add scaffold/detection utility for:
  - Equator and key latitude lines (e.g., Tropics)
  - Create latitude_marker.json

### Validation & Distance Matrix
- [ ] Run final check for:
  - Missing fields in `longitudes_from_map.json` and `weather_regions_greyhawk.json`
  - Fields like `lat`, `lon`, `center`, `climate_description`, etc.
- [ ] Generate and verify `distance_matrix.json` from updated coordinates

---

## 🌦 Climate Enrichment Pipeline

### Image Processing
- [ ] Validate:
  - All entries now match palette-derived Köppen codes
  - All pixel color mismatches logged
- [ ] Add support for:
  - Manual override of climate for special regions (e.g., underdark, magical zones)
- [ ] Recalibrate climate pixel → lat/lon transform for:
  - `oerth_climate_map.png` vs. political map resolution mismatch

---

## 📊 Preview & Display

### Visual Tools
- [ ] Generate preview map:
  - Climate display using enriched lat/lon data
  - Use vector, SVG, or Leaflet-style layout
- [ ] Option: build lightweight macOS menu launcher or CLI browser

### Scripts and Viewers
- [ ] Script to display, filter, and edit `weather_regions_greyhawk.json`
  - CLI menu for adding missing fields
  - Optional: track update history/log
- [ ] Add `-png` option to all DOT-exporting tools
- [ ] Build long-term docs viewer for Markdown + JSON summaries

---

## 🗂 Project Management & Deployment

### Archival & Versioning
- [ ] Add auto-versioning to pipeline scripts
- [ ] Always update:
  - `GREYHAWK_COORDINATES_TODO.md`
  - `GREYHAWK_FILE_REFERENCE.md`
- [ ] Confirm these are included in:
  - `archive_session_mac.sh`
  - ZIP backups triggered by `goodnight`

### GitHub & Virtual Environments
- [ ] Refine `.gitignore` rules for:
  - `venv/`, `__pycache__/`, `*.zip`, intermediate `.csv`, `.geojson`
- [ ] Sync cleaned `run_climate_pipeline_mac.sh` and `.bat` versions to GitHub
- [ ] Ensure `python3 -m venv venv` + `source venv/bin/activate` is included in all setup README/launchers

---

## 🧪 Enhancement Ideas (Lower Priority or Pending)

- [ ] Annotate regions with political alignment, elevation, and faction notes
- [ ] Enable real-time validation in the editor script
- [ ] Add AI-assisted climate sanity checker
- [ ] Generate regional encounter tables using biome + season + threat logic
- [ ] Integrate with Turn Dashboard (hazards + weather sync)