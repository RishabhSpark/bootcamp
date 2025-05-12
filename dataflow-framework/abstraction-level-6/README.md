# State-Based Routing System

## Overview
In this level, we transition from a fixed pipeline to a state-based routing engine. This system uses tags to route lines dynamically, enabling complex workflows that can branch, loop, and terminate based on tag values. It's designed like a state machine, where processors act as states, and tags drive transitions between states.

This approach decouples routing logic from processing code, allowing for more flexibility, retries, and asynchronous behavior in future stages.

## Features
- Stateful Routing: Tags guide the flow of data dynamically.
- End-to-End Process: Begins with start and ends with end, allowing for flexible processing flows.
- Dynamic Tagging and Routing: Supports branching, merging, and cyclic paths.
- Modular System: Easily extensible with custom processors.

## Example Workflow
- Start Processor: Begins the process, emitting tags like error, warn, or general.
- Tag-Based Routing:
- Error Tag: Directed to an error-specific processor.
- Warn Tag: Sent to a warning-specific processor.
- General Tag: Formatted into a snake_case and passed to the next processor.
- End Processor: Terminates the process once it receives the end tag.

## Project Structure
```
├── README.md
├── cli.py
├── config.yaml
├── processors
│   ├── __init__.py
│   ├── filters.py
│   ├── formatters.py
│   ├── output.py
│   └── start.py
├── router.py
└── text.txt
```

## How to Run
From the abstraction-level-6/ directory:
```bash
python main.py --input path/to/input.txt --config config.yaml
```