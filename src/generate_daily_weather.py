# generate_daily_weather.py
# Version: 1.2.2
# Purpose: CLI forecast tool with option for daily or full month calendar view with weather summaries

import json
import random
from pathlib import Path
from calendar_utils import list_greyhawk_months
from calendar_month_view import render_month_view, prompt_user_selection

# Setup paths
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"

with open(DATA_DIR / "longitudes_with_seasonal_profiles.json") as f:
    regions = json.load(f)
with open(DATA_DIR / "calendar_day_map.json") as f:
    calendar = json.load(f)
with open(DATA_DIR / "moon_phases.json") as f:
    moons = json.load(f)

temp_ranges = {
    "freezing": (-15, -5), "cold": (-5, 5), "cool": (5, 15),
    "mild": (10, 20), "warm": (15, 25), "hot": (25, 35),
    "very hot": (30, 45), "dry": (20, 35), "hot (Af)": (28, 34)
}

def get_moon_phase(moon_name, day_of_year):
    moon = moons[moon_name]
    offset = moon.get("offset", 0)
    cycle = moon["cycle_days"]
    phases = moon["phases"]
    moon_day = (day_of_year - offset) % cycle
    phase_keys = sorted(int(k) for k in phases)
    for i in reversed(phase_keys):
        if moon_day >= i:
            return phases[str(i)]
    return "new"

def choose_days():
    print("\n🗓️ Choose forecast duration:")
    print("  [1] 3 days\n  [2] 5 days\n  [3] 7 days")
    while True:
        try:
            choice = int(input("\nEnter number of days: "))
            if choice in [1, 2, 3]:
                return [3, 5, 7][choice - 1]
        except ValueError:
            pass
        print("❌ Choose 1, 2, or 3.")

def month_day_to_day_of_year(month_name, day_of_month):
    for day, data in calendar.items():
        if data.get("month") == month_name and data.get("day_of_month") == day_of_month:
            return int(day)
    raise ValueError("Invalid month/day combination")

def generate_weather(region, day_of_year):
    entry = calendar[str(day_of_year)]
    month = entry.get("month", entry.get("festival"))
    month_key = month if entry.get("month") else None

    temp_label = regions[region]["seasonal_temperature_profile"].get(month_key, "mild")
    temp_range = temp_ranges.get(temp_label, (10, 20))
    min_temp = random.randint(*temp_range)
    max_temp = random.randint(min_temp + 1, temp_range[1] + 2)

    bias = regions[region]["seasonal_weather_bias"].get(month_key, "clear")
    roll = random.randint(1, 100)
    if roll <= 60: weather = bias
    elif roll <= 75: weather = "rain" if "storm" in bias else "cloudy"
    elif roll <= 85: weather = "fog" if "mist" not in bias else "drizzle"
    elif roll <= 95: weather = f"severe {bias}" if "storm" in bias else f"extreme {bias}"
    else: weather = "unseasonal shift"

    return {
        "calendar": entry,
        "temp_label": temp_label,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "weather": weather,
        "roll": roll,
        "luna": get_moon_phase("Luna", day_of_year),
        "celene": get_moon_phase("Celene", day_of_year)
    }

def display_weather_output(day, region, forecast):
    cal = forecast["calendar"]
    title = f"{cal.get('month', cal.get('festival'))} {cal.get('day_of_month', cal.get('day_of_festival'))}"
    real = f"({cal['real_weekday']}, {cal.get('real_month', '')} {cal.get('day_of_month', '')})"

    luna_txt = f"Luna: {forecast['luna'].replace('_', ' ').title()} moon"
    celene_phase = forecast['celene'].replace('_', ' ').title()
    celene_txt = (f"Celene: {celene_phase} moon (visible tonight 🌕)"
                  if forecast['celene'] == "full"
                  else f"Celene: {celene_phase} moon (not visible)")
    moon_line = f"{luna_txt} | {celene_txt}"

    print(f"🌤️ Weather Forecast for {region} on Day {day} ({title})")
    print(f"🗓️ Greyhawk: {title} {real}")
    print(f"🌡️ {forecast['temp_label'].capitalize()} ({forecast['min_temp']}–{forecast['max_temp']}°C)")
    print(f"🌧️ {forecast['weather']} (🎲 {forecast['roll']})")
    print(f"🌕 {moon_line}")

if __name__ == "__main__":
    print("🌦️ GREYHAWK WEATHER GENERATOR")

    print("\nSelect output mode:")
    print("  [1] Daily forecast (default)")
    print("  [2] Full calendar month view")

    mode = input("\nEnter choice (1 or 2): ").strip()
    if mode == "2":
        region_names = sorted(regions.keys())
        print("\n🌍 Choose a Region:")
        for i, name in enumerate(region_names):
            print(f"  [{i+1:2}] {name}")
        region = ""
        while not region:
            try:
                r = int(input("Enter region #: "))
                if 1 <= r <= len(region_names):
                    region = region_names[r - 1]
            except Exception:
                pass

        month, day = prompt_user_selection()
        render_month_view(month, region, day, weather_func=generate_weather)
    else:
        months = list_greyhawk_months()
        print("\n📆 Choose Current Greyhawk Month:")
        for i, m in enumerate(months):
            print(f"  [{i+1:2}] {m}")
        while True:
            try:
                m_idx = int(input("Enter month #: "))
                if 1 <= m_idx <= len(months):
                    month = months[m_idx - 1]
                    break
            except Exception:
                pass

        while True:
            try:
                d = int(input(f"Enter day of {month} (1–28): "))
                if 1 <= d <= 28:
                    day = d
                    break
            except Exception:
                pass

        print("\n💾 Choose export format:")
        print("  [1] TXT only\n  [2] MD (World Anvil style)\n  [3] Both")
        format_choice = ""
        while format_choice not in ("txt", "md", "both"):
            try:
                fmt = int(input("\nExport format: "))
                if fmt == 1: format_choice = "txt"
                elif fmt == 2: format_choice = "md"
                elif fmt == 3: format_choice = "both"
            except Exception:
                print("❌ Please enter a number.")

        region_names = sorted(regions.keys())
        print("\n🌍 Choose a Region:")
        for i, name in enumerate(region_names):
            print(f"  [{i+1:2}] {name}")
        region = ""
        while not region:
            try:
                r = int(input("Enter region #: "))
                if 1 <= r <= len(region_names):
                    region = region_names[r - 1]
            except Exception:
                pass

        days = choose_days()

        day_of_year = month_day_to_day_of_year(month, day)
        forecast_data = []
        for d in range(day_of_year, day_of_year + days):
            day_id = ((d - 1) % 364) + 1
            forecast = generate_weather(region, day_id)
            display_weather_output(day_id, region, forecast)
            forecast_data.append(forecast)
