
import json

# Load file
with open("longitudes_with_seasonal_profiles.json") as f:
    regions = json.load(f)

# Prompt loop
print("🌍 Greyhawk Weather Region Lookup")
print("Type a region name (e.g., Hommlet, Verbobonc, Nulb) or 'exit' to quit.")
while True:
    region = input("\n🔍 Region name: ").strip()
    if region.lower() == "exit":
        print("👋 Exiting.")
        break
    if region not in regions:
        print(f"❌ Region '{region}' not found. Try again.")
        continue

    data = regions[region]
    print(f"📍 {region}")
    print(f"  ➤ Climate: {data.get('climate_description')}")
    print(f"  ➤ Weather Flavor: {data.get('weather_profile')}")
    print("  ➤ Seasonal Temperature Profile:")
    for month, temp in data.get("seasonal_temperature_profile", {}).items():
        print(f"    {month:12} → {temp}")
    print("  ➤ Seasonal Weather Bias:")
    for month, weather in data.get("seasonal_weather_bias", {}).items():
        print(f"    {month:12} → {weather}")
