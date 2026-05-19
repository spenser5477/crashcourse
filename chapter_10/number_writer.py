import json
from pathlib import Path

numbers = [2, 3, 5, 7, 11, 13]

filename = Path(__file__).parent / 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
