import json

from pathlib import Path

filename = Path(__file__).parent / "data/eq_data_1_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = Path(__file__).parent / "data/eq_data_1_day_m1_ident.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)
