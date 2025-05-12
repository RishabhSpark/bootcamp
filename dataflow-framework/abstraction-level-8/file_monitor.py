import shutil
import time
from pathlib import Path
from file_processor import process_file

WATCH_DIR = Path("watch_dir")
UNPROCESSED = WATCH_DIR / "unprocessed"
UNDERPROCESS = WATCH_DIR / "underprocess"
PROCESSED = WATCH_DIR / "processed"

def recover_files():
    for file in UNDERPROCESS.glob("*"):
        if file.is_file():
            shutil.move(str(file), UNPROCESSED / file.name)
            print(f"Recovered: {file.name}")

def monitor_folder():
    while True:
        for file in sorted(UNPROCESSED.glob("*")):
            try:
                target = UNDERPROCESS / file.name
                shutil.move(str(file), target)
                process_file(target)
                shutil.move(str(target), PROCESSED / file.name)
                print(f"Processed: {file.name}")
            except Exception as e:
                print(f"Error: {file.name} – {e}")
        time.sleep(2)