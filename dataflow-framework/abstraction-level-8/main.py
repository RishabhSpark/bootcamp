import threading
import time
from file_monitor import monitor_folder, recover_files
import uvicorn
from dashboard import app

def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")

def main():
    recover_files()

    threading.Thread(target=monitor_folder, daemon=True).start()
    threading.Thread(target=start_dashboard, daemon=True).start()

    print("Monitoring started. Dashboard at http://localhost:8000")

    while True:
        time.sleep(10)

if __name__ == "__main__":
    main()