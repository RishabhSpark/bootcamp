from fastapi import FastAPI
from pathlib import Path
from file_processor import CURRENT_FILE, RECENT_FILES

app = FastAPI()
WATCH_DIR = Path("watch_dir")

@app.get("/")
def root():
    return {"message": "Dashboard running. Visit /status for live view."}

@app.get("/status")
def get_status():
    return {
        "unprocessed": len(list((WATCH_DIR / "unprocessed").glob("*"))),
        "underprocess": len(list((WATCH_DIR / "underprocess").glob("*"))),
        "processed": len(list((WATCH_DIR / "processed").glob("*"))),
        "currently_processing": CURRENT_FILE,
        "recent_files": RECENT_FILES,
    }
