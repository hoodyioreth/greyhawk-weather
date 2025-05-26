# 🌦️ Greyhawk Weather Generator

This repository provides a comprehensive, date-aware weather generator for the World of Greyhawk (576 CY), tailored to sandbox and hexcrawl campaigns.

## 🧰 Features

- 📅 364-day calendar system with Greyhawk months, festivals, and real-world equivalents
- 🌕 Luna and Celene moon phase tracking
- 🗺️ Region-aware weather bias and seasonal temperature profiles
- ✍️ Exports World Anvil–styled `.md` logs or `.txt` outputs
- 🐍 Fully modular Python code in `src/`

## 📁 Project Structure

greyhawk-weather/
├── src/ → Python source code
├── data/ → Regional, calendar, and climate JSON files
├── exports/ → Forecast output and token images
├── docs/ → Project markdown files (TODOs, file references)
├── archive/ → Deprecated scripts or backups


## 📦 Dependencies

See [`requirements.txt`](requirements.txt)

## 🔗 Related Tools

- [Greyhawk Town Mapper](https://github.com/hoodyioreth/greyhawk-towns)
- [Greyhawk Encounter Tables](https://github.com/hoodyioreth/greyhawk-encounters)

Part of the [Greyhawk Tools Suite](https://github.com/hoodyioreth/greyhawk-suite)

---

## 🔧 Git Workflow for Stability and Experimentation

To keep the project stable while exploring new features, we use a simple branching strategy:

### 1. Main Branch (`main` or `master`)

- Contains the **stable, tested version** of the project.
- Tagged releases are made here, e.g., `v1.2.2-stable`.
- Used for production or demos.

### 2. Feature Branches

- Created for each new big change or experimental feature.
- Named descriptively, e.g., `feature/daily-stages` or `feature/weather-persistence`.
- Allows working on new ideas without risking the stable code.

### 3. Switching Between Branches

- To work on or deploy stable code:

```bash
git checkout main
