# Observability and System Introspection

## Overview
In this level, we add real-time observability to your state-based routing engine. This includes metrics collection, execution tracing, and a live dashboard to monitor the system's health, performance, and debugging. By providing visibility into the internal workings of the engine, we can track each line's journey, measure processing times, and expose error logs.

## Project Structure
```
├── README.md
├── cli.py
├── config.yaml
├── dashboard.py
├── main.py
├── metrics
│   ├── __init__.py
│   └── metrics.py
├── processors
│   ├── __init__.py
│   ├── filters.py
│   ├── formatters.py
│   ├── output.py
│   └── start.py
├── text.txt
└── tracing
    ├── __init__.py
    └── tracer.py
```

## How to run
```bash
python cli.py --trace
```

## Monitor system
Monitor System: Visit the following endpoints in your browser:
- Stats: `http://localhost:8000/stats`
- Trace: `http://localhost:8000/trace`
- Errors: `http://localhost:8000/errors`

