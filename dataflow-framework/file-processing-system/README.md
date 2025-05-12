# Real-Time File Processing System
A dynamic, observable, fault-tolerant file processing pipeline that supports both one-shot and continuous modes, with optional Docker deployment and FastAPI integration.

# Features
- Stream-based, memory-efficient file processing
- Plug-and-play processors via YAML config
- Dual execution modes: process a single file or watch a directory
- Real-time stats via FastAPI (/stats, /health, /files)
- Easily deployable via Docker
- Extensible and production-ready architecture

# Requirements
- Python 3.13+
- Docker

# How to run
```bash
python -m venv venv
source venv/bin/activate #linux/macOS
.\venv\Scripts\activate # windows
```

# Requirements
```bash
pip install -r requirements.txt
```

# Usage

## 1. Single File Mode
```bash
python main.py --input path/to/file.txt
```

## 2. Watch mode
```bash
python main.py --watch
```

# Deployement

## Docker
Build and run via docker
```bash
make docker-build
make docker-run
```

# Uploading Files

Drop files into watch_dir/unprocessed/ to trigger automatic processing.

# FastAPI Endpoints
Once running, access the API on http://localhost:8000:

- /health: Simple health check
- /stats: Runtime statistics (processed count, errors, uptime, etc.)
