# calendar_month_view.py
# Version: 0.3.2
# Purpose: Generate an ASCII-style calendar for a Greyhawk month with weather/moon highlights
# Supports region-based weather summaries via optional weather_func callback

import json
from pathlib import Path
from calendar_utils import get_month_number

# Setup paths
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"

with open(DATA_DIR / "calendar_day_map.json") as f:
    calendar = json.load(f)
with open(DATA_DIR / "moon_phases.json") as f:
    moons = json.load(f)

DAYS_IN_WEEK = 7
WEEKDAYS = ["Starday", "Sunday", "Moonday", "Godsday", "Waterday", "Earthday", "Freeday"]


def get_moon_phase(moon_name, day_of_year):
    moon = moons[moon_name]
    offset = moon.get("offset", 0)
    cycle = moon["cycle_days"]
    phases = moon["phases"]
    moon_day = (day_of_year - offset) % cycle
    for key in sorted(map(int, phases.keys()), reverse=True):
        if moon_day >= key:
            return phases[str(key)]
    return "new"


def render_month_view(month_name, region_name, highlight_day, weather_func=None):
    print(f"\n      📅 {month_name.upper()} – {region_name} Forecast")
    print(" ".join([wd[:2] for wd in WEEKDAYS]))

    month_days = [
        (int(d), v) for d, v in calendar.items()
        if v.get("month") == month_name
    ]

    first_weekday = WEEKDAYS.index(month_days[0][1]["day_of_week"])

    day_cursor = 0
    printed = []
    while day_cursor < len(month_days):
        week = ["  "] * DAYS_IN_WEEK
        for i in range(DAYS_IN_WEEK):
            if (day_cursor == 0 and i < first_weekday) or day_cursor >= len(month_days):
                continue
            day_num = month_days[day_cursor][1].get("day_of_month", month_days[day_cursor][0])
            display = f"{day_num:2}"
            if day_num == highlight_day:
                display = f"[{day_num:2}]"
            week[i] = display
            day_cursor += 1
        printed.append(" ".join(week))

    for line in printed:
        print(line)

    print("\n📝 Daily Highlights:")
    for day, entry in month_days:
        luna = get_moon_phase("Luna", day)
        celene = get_moon_phase("Celene", day)
        weekday = entry['day_of_week']
        day_of_month = entry.get("day_of_month", day)

        weather_summary = ""
        if weather_func:
            forecast = weather_func(region_name, day)
            weather_summary = f", 🌡️ {forecast['temp_label'].capitalize()} ({forecast['min_temp']}–{forecast['max_temp']}°C), 🌧️ {forecast['weather']}"

        print(f"- {day_of_month:2} ({weekday}): 🌕 Luna = {luna}, 🌘 Celene = {celene}{weather_summary}")


def prompt_user_selection():
    # Only month and day selection here
    months = sorted(
        {v['month'] for v in calendar.values() if v.get('month')},
        key=lambda m: get_month_number(m)
    )

    print("\nAvailable months:")
    for i, month in enumerate(months, 1):
        print(f"  [{i}] {month}")
    while True:
        try:
            m_choice = int(input("Select a month by number: "))
            if 1 <= m_choice <= len(months):
                month_selected = months[m_choice - 1]
                break
        except Exception:
            pass

    while True:
        try:
            day_selected = int(input("Select a day to highlight (1-28): "))
            if 1 <= day_selected <= 28:
                break
        except Exception:
            pass

    return month_selected, day_selected


if __name__ == "__main__":
    # Example standalone usage with prompts
    month, day = prompt_user_selection()
    region = "Bright Desert"  # Default region for standalone usage
    render_month_view(month, region, day)
