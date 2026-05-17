from pathlib import Path

filename = Path(__file__).parent / "pi_digits.txt"

print(filename)

try:
    with filename.open(encoding="utf-8") as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print(f"File not found: {filename}")
    raise

for line in lines:
    print(
        line.rstrip()
    )  # rstrip() removes the trailing newline character from each line before printing it.
