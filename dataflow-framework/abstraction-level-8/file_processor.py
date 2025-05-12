from pathlib import Path
import time

CURRENT_FILE = None
RECENT_FILES = []

def process_file(file_path: Path):
    global CURRENT_FILE, RECENT_FILES
    CURRENT_FILE = file_path.name
    print(f"Processing: {CURRENT_FILE}")

    with file_path.open("r") as f:
        for line in f:
            line = line.strip()
            if "error" in line.lower():
                print(f"Filtered line: {line}")
            else:
                print(f"Ignored line: {line}")
            time.sleep(0.2)  # simulate processing delay

    RECENT_FILES.insert(0, (CURRENT_FILE, time.strftime("%Y-%m-%d %H:%M:%S")))
    RECENT_FILES = RECENT_FILES[:10]
    CURRENT_FILE = None