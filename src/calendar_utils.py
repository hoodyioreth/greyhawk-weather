# calendar_utils.py
# Version: 0.1.0
# Purpose: Utility functions for Greyhawk month/season lookup
# Dependencies: data/calendar_metadata.json

import json
from pathlib import Path

# Load metadata once
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_FILE = SCRIPT_DIR.parent / "data" / "calendar_metadata.json"

with open(DATA_FILE) as f:
    metadata = json.load(f)

_month_index = {m['greyhawk']: m for m in metadata['months']}
_month_number_map = {m['number']: m['greyhawk'] for m in metadata['months']}


def get_season_for_month(month_name):
    """Return the season (Winter, Spring, etc) for a given Greyhawk month."""
    return _month_index.get(month_name, {}).get("season")


def get_month_number(month_name):
    """Return the month number (1–12) for a Greyhawk month."""
    return _month_index.get(month_name, {}).get("number")


def get_month_name_by_number(num):
    """Return the Greyhawk month name from number."""
    return _month_number_map.get(num)


def get_real_world_equivalent(month_name):
    """Return the real-world month (e.g., 'January') for a Greyhawk month."""
    return _month_index.get(month_name, {}).get("real")


def list_greyhawk_months():
    """Return list of Greyhawk month names in correct order."""
    return [m['greyhawk'] for m in sorted(metadata['months'], key=lambda x: x['number'])]
