# Level 2: Modular Structure and Standardized Processing

## Overview

This version introduces a clean modular structure with well-separated concerns and a standardized function signature for line processors. Each processor is a function that transforms a line of text (`str -> str`), and multiple processors are applied in sequence as a pipeline.

## Project Structure
```
├── README.md
├── cli.py
├── core.py
├── custom_types.py
├── main.py
├── pipeline.py
```

## Processing Modes

- `uppercase`: Converts text to uppercase
- `snakecase`: Converts text to lowercase and replaces spaces with underscores

Each mode maps to a list of processors applied sequentially to each line.

## Features

- `typer` CLI just like Level 1
- `.env` for setting default mode
- Cleanly structured code
- Extensible: add new processors easily without modifying main logic

---