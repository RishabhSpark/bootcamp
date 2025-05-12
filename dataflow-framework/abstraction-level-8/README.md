# Automated Folder Monitor and Recovery

## Overview
In this level, we will transform your file processing tool into a self-running, fault-tolerant system. Instead of processing just one file at a time, your system will continuously monitor a folder for new files, process them, and recover automatically if it crashes or is restarted. This will help you mimic a real-world ingestion service or ETL daemon, which operates autonomously, robustly, and safely.

## Features
- Folder Queue Structure: A directory structure that mimics a queue with state to track files.
- Continuous Monitoring: Watch a folder for new files and process them as they appear.
- Resilient Recovery: If the system crashes or is restarted, it will resume from where it left off, processing unprocessed or interrupted files.
- Dashboard Updates: The web dashboard will reflect real-time progress, showing the number of files in each folder, the file currently being processed, and the last few processed files with timestamps.

## Folder Structure
```
├── cli.py
├── dashboard.py
├── file_monitor.py
├── file_processor.py
├── main.py
├── text.txt
└── watch_dir
    ├── processed
    ├── underprocess
    │   └── text.txt
    └── unprocessed
```

## File Lifecycle
- Incoming Files: New files land in the unprocessed/ directory.
- Processing: The system moves the file to the underprocess/ folder and begins processing.
- Completion: Once processing is done, the file is moved to the processed/ directory.
- System Crash or Restart: If the system crashes, it will move any files in the underprocess/ folder back to the unprocessed/ folder when it starts up again. This ensures the system retries the files without causing data duplication.

## How to Run
```bash
python cli.py
```
Press `ctrl+C` to exit

This will:
- Start monitoring the unprocessed/ folder.
- Begin processing files as they appear.
- Launch a FastAPI dashboard to track real-time progress.
- Monitor System State: Visit the dashboard at http://localhost:8000/:
- Stats: View the status: /status