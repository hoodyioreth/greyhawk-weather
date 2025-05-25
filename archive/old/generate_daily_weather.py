
import json
import random
from datetime import datetime

# Load data
with open("longitudes_with_seasonal_profiles.json") as f:
    regions = json.load(f)
with open("calendar_day_map.json") as f:
    calendar = json.load(f)
with open("moon_phases.json") as f:
    moons = json.load(f)

temp_ranges = {
    "freezing": (-15, -5), "cold": (-5, 5), "cool": (5, 15),
    "mild": (10, 20), "warm": (15, 25), "hot": (25, 35),
    "very hot": (30, 45), "dry": (20, 35), "hot (Af)": (28, 34)
}


def choose_days():
    print("\n🗓️ Choose forecast duration:")
    print("  [1] 3 days")
    print("  [2] 5 days")
    print("  [3] 7 days")
    while True:
        try:
            choice = int(input("\nEnter number of days: "))
            if choice == 1: return 3
            elif choice == 2: return 5
            elif choice == 3: return 7
            else: print("❌ Choose 1, 2, or 3.")
        except ValueError:
            print("❌ Please enter a valid number.")

months = [
    "Fireseek", "Readying", "Coldeven", "Planting", "Flocktime", "Wealsun",
    "Reaping", "Goodmonth", "Harvester", "Patchwall", "Ready'reat", "Sunsebb"
]

def month_day_to_day_of_year(month_name, day_of_month):
    for day, data in calendar.items():
        if data.get("month") == month_name and data.get("day_of_month") == day_of_month:
            return int(day)
    raise ValueError("Invalid month/day combination")

def choose_month_and_day():
    print("\n📆 Choose Current Greyhawk Month:")
    for i, m in enumerate(months):
        print(f"  [{i+1:2}] {m}")
    while True:
        try:
            m_idx = int(input("Enter month #: "))
            if 1 <= m_idx <= 12:
                month = months[m_idx - 1]
                break
        except ValueError:
            continue

    while True:
        try:
            d = int(input(f"Enter day of {month} (1–28): "))
            if 1 <= d <= 28:
                return month, d
        except ValueError:
            continue

def get_moon_phases(day, entry):
    luna_phase = moons["Luna"]["phases"].get(str((day % 28)), "new")
    celene_visible = False
    for fest, fest_day in moons["Celene"]["appearances"].items():
        if entry["festival"] == fest and entry["day_of_festival"] == fest_day:
            celene_visible = True
    return luna_phase, celene_visible

def generate_weather(region, day_of_year):
    entry = calendar[str(day_of_year)]
    luna, celene = get_moon_phases(day_of_year, entry)
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
        "luna": luna,
        "celene": celene
    }

def display_weather_output(day, region, forecast):
    cal = forecast["calendar"]
    title = f"{cal.get('month', cal.get('festival'))} {cal.get('day_of_month', cal.get('day_of_festival'))}"
    real = f"({cal['real_weekday']}, {cal.get('real_month', '')} {cal.get('day_of_month', '')})"
    moon_line = f"Luna: {forecast['luna'].capitalize()} moon"
    if forecast["celene"]:
        moon_line += ", Celene visible 🌕"

    print(f"🌤️ Weather Forecast for {region} on Day {day} ({title})")
    print(f"🗓️ Greyhawk: {title} {real}")
    print(f"🌡️ {forecast['temp_label'].capitalize()} ({forecast['min_temp']}–{forecast['max_temp']}°C)")
    print(f"🌧️ {forecast['weather']} (🎲 {forecast['roll']})")
    print(f"🌕 {moon_line}")

if __name__ == "__main__":
    print("🌦️ GREYHAWK DAILY WEATHER (DATE-AWARE)")
    month, day = choose_month_and_day()
    try:
        day_of_year = month_day_to_day_of_year(month, day)
    except ValueError:
        print("❌ Invalid Greyhawk date.")
        exit()

    
print("\n💾 Choose export format:")
print("  [1] TXT only")
print("  [2] MD (World Anvil style)")
print("  [3] Both")
format_choice = ""
while format_choice not in ("txt", "md", "both"):
    try:
        fmt = int(input("\nExport format: "))
        if fmt == 1: format_choice = "txt"
        elif fmt == 2: format_choice = "md"
        elif fmt == 3: format_choice = "both"
    except ValueError:
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
        except ValueError:
            pass

    
days = choose_days()

forecast_data = []
for d in range(day_of_year, day_of_year + days):
    day_id = ((d - 1) % 364) + 1
    forecast = generate_weather(region, day_id)
    display_weather_output(day_id, region, forecast)
    forecast_data.append(forecast)

