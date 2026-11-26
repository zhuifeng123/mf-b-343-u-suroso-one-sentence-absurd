import os

output_dir = "/output"
entry_file = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

entry = (
    "A fridge door that slowly shuts itself with a disappointed hum while you hover, "
    "then shoves your expired yogurt to the front with a magnetic sigh, "
    "because today is the day you finally deal with it."
)

with open(entry_file, "w") as f:
    f.write(entry)

print(entry)
print(f"[{len(entry)} chars] -> {entry_file}")