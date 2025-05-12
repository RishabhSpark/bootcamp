import threading
import time
from pathlib import Path
import uvicorn
from dashboard import app
from file_monitor import monitor_folder, recover_files
from file_processor import process_file

def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")

def watch_mode():
    recover_files()
    
    threading.Thread(target=monitor_folder, daemon=True).start()
    threading.Thread(target=start_dashboard, daemon=True).start()
    
    print("Running in Watch Mode at http://localhost:8000")
    
    while True:
        time.sleep(10)

def single_file_mode(file_path: str):
    print(f"Processing single file: {file_path}")
    process_file(Path(file_path))