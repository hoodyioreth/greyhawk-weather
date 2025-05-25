# 🌦️ Greyhawk Weather Generator

This repository provides a comprehensive, date-aware weather generator for the World of Greyhawk (576 CY), tailored to sandbox and hexcrawl campaigns.

## 🧰 Features

- 📅 364-day calendar system with Greyhawk months, festivals, and real-world equivalents
- 🌕 Luna and Celene moon phase tracking
- 🗺️ Region-aware weather bias and seasonal temperature profiles
- ✍️ Exports World Anvil–styled `.md` logs or `.txt` outputs
- 🐍 Fully modular Python code in `src/`

## 📁 Project Structure

```
greyhawk-weather/
├── src/           → Python source code
├── data/          → Regional, calendar, and climate JSON files
├── exports/       → Forecast output and token images
├── docs/          → Project markdown files (TODOs, file references)
├── archive/       → Deprecated scripts or backups
```

## 📦 Dependencies

See [`requirements.txt`](requirements.txt)

## 🔗 Related Tools

- [Greyhawk Town Mapper](https://github.com/hoodyioreth/greyhawk-towns)
- [Greyhawk Encounter Tables](https://github.com/hoodyioreth/greyhawk-encounters)

Part of the [Greyhawk Tools Suite](https://github.com/hoodyioreth/greyhawk-suite)

---

## 🧯 Deactivating the Virtual Environment

To exit the virtual environment after you're done working:

```bash
deactivate
```

This will return your terminal to the system Python context.
