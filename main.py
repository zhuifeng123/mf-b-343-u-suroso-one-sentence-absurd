import os

output_dir = "/output"
entry_file = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(entry_file, "w") as f:
    f.write("A coffee mug that automatically files a formal complaint with your boss when it detects you've had your third cup of the day, silently judging your life choices while you sip.")