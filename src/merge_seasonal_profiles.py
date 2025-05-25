
import json
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent
months_file = BASE_DIR / "greyhawk_months.json"
regions_file = BASE_DIR / "longitudes_from_map.json"
output_file = BASE_DIR / "longitudes_with_seasonal_profiles.json"

# Load data
print("🔄 Loading data files...")
with open(months_file) as f:
    months = json.load(f)

with open(regions_file) as f:
    regions = json.load(f)

# Build month → season map
print("🧭 Building month to season mapping...")
month_to_season = {m['month_name']: m['season'] for m in months}

# Climate + season → temp/precip bias logic
print("🌍 Setting seasonal climate logic...")
temp_profiles = {
    ("Dfb", "Winter"): "cold",
    ("Dfb", "Spring"): "cool",
    ("Dfb", "Low Summer"): "warm",
    ("Dfb", "High Summer"): "hot",
    ("Dfb", "Autumn"): "cool",

    ("Cfb", "Winter"): "mild",
    ("Cfb", "Spring"): "mild",
    ("Cfb", "Low Summer"): "warm",
    ("Cfb", "High Summer"): "warm",
    ("Cfb", "Autumn"): "mild",

    ("Cfa", "Winter"): "mild",
    ("Cfa", "Spring"): "warm",
    ("Cfa", "Low Summer"): "hot",
    ("Cfa", "High Summer"): "hot",
    ("Cfa", "Autumn"): "warm",

    ("Aw", "Winter"): "dry",
    ("Aw", "Spring"): "humid",
    ("Aw", "Low Summer"): "hot",
    ("Aw", "High Summer"): "hot",
    ("Aw", "Autumn"): "dry",

    ("Af", "Winter"): "hot",
    ("Af", "Spring"): "hot",
    ("Af", "Low Summer"): "hot",
    ("Af", "High Summer"): "hot",
    ("Af", "Autumn"): "hot",

    ("BSh", "Winter"): "dry",
    ("BSh", "Spring"): "hot",
    ("BSh", "Low Summer"): "very hot",
    ("BSh", "High Summer"): "very hot",
    ("BSh", "Autumn"): "hot",

    ("Dfc", "Winter"): "freezing",
    ("Dfc", "Spring"): "cold",
    ("Dfc", "Low Summer"): "mild",
    ("Dfc", "High Summer"): "mild",
    ("Dfc", "Autumn"): "cold"
}

weather_bias = {
    ("Dfb", "Winter"): "snow",
    ("Dfb", "Spring"): "thunderstorm",
    ("Dfb", "Low Summer"): "rain",
    ("Dfb", "High Summer"): "thunderstorm",
    ("Dfb", "Autumn"): "fog",

    ("Cfb", "Winter"): "rain",
    ("Cfb", "Spring"): "rain",
    ("Cfb", "Low Summer"): "light rain",
    ("Cfb", "High Summer"): "storm",
    ("Cfb", "Autumn"): "fog",

    ("Cfa", "Winter"): "rain",
    ("Cfa", "Spring"): "storm",
    ("Cfa", "Low Summer"): "thunderstorm",
    ("Cfa", "High Summer"): "storm",
    ("Cfa", "Autumn"): "mist",

    ("Aw", "Winter"): "dry",
    ("Aw", "Spring"): "humid",
    ("Aw", "Low Summer"): "monsoon",
    ("Aw", "High Summer"): "storm",
    ("Aw", "Autumn"): "dry",

    ("Af", "Winter"): "rain",
    ("Af", "Spring"): "heavy rain",
    ("Af", "Low Summer"): "thunderstorm",
    ("Af", "High Summer"): "thunderstorm",
    ("Af", "Autumn"): "humid",

    ("BSh", "Winter"): "dry",
    ("BSh", "Spring"): "dust",
    ("BSh", "Low Summer"): "heatwave",
    ("BSh", "High Summer"): "dust storm",
    ("BSh", "Autumn"): "dry",

    ("Dfc", "Winter"): "blizzard",
    ("Dfc", "Spring"): "sleet",
    ("Dfc", "Low Summer"): "rain",
    ("Dfc", "High Summer"): "storm",
    ("Dfc", "Autumn"): "frost"
}

# Merge seasonal data into each region
print("🛠 Processing regions...")
for name, data in regions.items():
    koppen = data.get("climate_koppen", "Cfb")
    temp_profile = {}
    weather_profile = {}

    for m in months:
        month = m["month_name"]
        season = m["season"]
        key = (koppen, season)

        temp = temp_profiles.get(key, "mild")
        weather = weather_bias.get(key, "clear")

        temp_profile[month] = temp
        weather_profile[month] = weather

    data["seasonal_temperature_profile"] = temp_profile
    data["seasonal_weather_bias"] = weather_profile

# Save updated file
print(f"💾 Writing output to {output_file.name}")
with open(output_file, "w") as f:
    json.dump(regions, f, indent=2)

print("✅ Merge complete.")
