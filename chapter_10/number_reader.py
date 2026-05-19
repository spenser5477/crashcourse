from pathlib import Path
import json

filename = Path(__file__).parent / 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)
